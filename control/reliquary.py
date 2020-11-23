import erajs.api as a 
#此页面用于设定facility基本模板

class reliquary:
    ID = 0
    
    def __init__(self, template="1"):
        path = 'reliquary'
        reliquary.ID = reliquary.ID + 1
        self.ID = reliquary.ID
        self.Type = "reliquary"
        self.template = template
        self.level = 1
        self.name = a.dat()[path][template]['name']
        self.skill = a.dat()[path][template]['skill']
        self.value = a.dat()[path][template]['value']
        self.growth = a.dat()[path][template]['growth']
        self.description = a.dat()[path][template]['description']
        self.enable = True

    def change(self, key, value):
        eval("self.{} = value".format(key))

    def normal_upgrade(self, up_level):
        i = 0
        grow = 0
        while grow in self.growth:
            self.value[i] = grow*up_level
            i = i+1

