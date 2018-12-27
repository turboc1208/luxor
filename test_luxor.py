import appdaemon.plugins.hass.hassapi as hass
#import appdaemon.appapi as appapi

class test_luxor(hass.Hass):

  def initialize(self):
    self.log("about to fire SPEAK event")
    self.entities={"input_number.patlights_intensity":{"type":"group","index":2},
            "input_number.stairway_intensity":{"type":"group","index":3},
            "input_number.wall_intensity":{"type":"group","index":4},
            "input_number.tree_front_right":{"type":"group","index":5},
            "input_number.tree_front_left":{"type":"group","index":6},
            "input_number.tree_back_left":{"type":"group","index":7},
            "input_number.tree_back_right":{"type":"group","index":8},
            "input_number.xmas_theme":{"type":"theme","index":1},
            "input_number.everyday_theme":{"type":"theme","index":0}}

    for e in self.entities:
      self.listen_state(self.action_handler,e)
      self.log("Listening for {}".format(e))

  def action_handler(self,entity,state,old,new,kwargs):
    self.log("entity: {}, state={}, old={}, new={}".format(entity,state,self.ftoi(old),self.ftoi(new)))
    if not entity in self.entities:
      self.log("entity : {} not found in self.entities {}".format(entity,self.entities))
    else:
      self.fire_event("LUXOR_EVENT",type=self.entities[entity]["type"],index=self.entities[entity]["index"],
              action=self.ftoi(new) if self.entities[entity]["type"]=="group" else "on" if self.ftoi(new)==1 else "off")
      self.log("fired LUXOR_EVENT")

  def ftoi(self,f):
    return int(float(str(f)))

