import erajs.api as a 
#此页面用于设定monster基本模板

class monster:
    ID = 0
    
    def __init__(self, template="1"):
        path = 'monster_mode'
        monster.ID = monster.ID + 1
        self.ID = monster.ID
        self.Type = "monster"
        self.template = template
        self.level = 1
        self.name = a.dat()[path][template]['name']
        self.gender = a.dat()[path][template]['gender']
        self.skill = a.dat()[path][template]['skill']
        self.max_health = a.dat()[path][template]['max_health']
        self.health = self.max_health
        self.atk = a.dat()[path][template]['atk']
        self.dEf = a.dat()[path][template]['def']
        self.growth = a.dat()[path][template]['growth']
        self.description = a.dat()[path][template]['description']
        self.alive = True
    
    def change(self,key, value):
        eval("self.{} = value".format(key))
    
    def die(self):
        self.alive = False

    def normal_upgrade(self, up_level):
        self.level = self.level + up_level
        self.max_health = self.max_health + self.growth[0]
        self.atk = self.atk + self.growth[1]
        self.dEf = self.dEf + self.growth[2]
