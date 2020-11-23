import erajs.api as a 
#此页面用于设定succubus基本模板

class succubus:
    
    def __init__(self, template=1):
        path = 'succubus_mode.{}'.format(template)
        self.Type = "succubus"
        self.template = template
        self.name = a.dat()[path]['name']
        self.level = 1
        self.gender = a.dat()[path]['gender']
        self.skill = a.dat()[path]['skill']
        self.superpower = a.dat()[path]['superpower']
        self.max_health = a.dat()[path]['max_health']
        self.health = self.max_health
        self.atk = a.dat()[path]['atk']
        self.dEf = a.dat()[path]['def']
        self.growth = a.dat()[path]['growth']
        self.description = a.dat()[path]['description']
    
    def change(self,key, value):
        eval("self.{} = value".format(key))

    def normal_upgrade(self, up_level):
        self.level = self.level + up_level
        self.max_health = self.max_health + self.growth[0]*up_level
        self.atk = self.atk + self.growth[1]*up_level
        self.dEf = self.dEf + self.growth[2]*up_level

    def save(self):
        a.sav()['succubus'] = [self.template, self.name, self.level, self.gender, self.skill, 
        self.superpower, self.max_health, self.health, self.atk, self.dEf, self.growth, self.description]

    def load(self):
        load_data = a.sav()['succubus']
        self.template = load_data[0]
        self.name = load_data[1]
        self.level = load_data[2]
        self.gender = load_data[3]
        self.skill = load_data[4]
        self.superpower = load_data[5]
        self.max_health = load_data[6]
        self.health =load_data[7]
        self.atk = load_data[8]
        self.dEf =load_data[9]
        self.growth = load_data[10]
        self.description = load_data[11]


