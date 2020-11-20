import erajs.api as a 
#此页面用于设定braver基本模板

class braver:
    ID = 0
    
    def __init__(self, template="1"):
        path = 'braver_mode'
        braver.ID = braver.ID + 1
        self.ID = braver.ID
        self.Type = "braver"
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