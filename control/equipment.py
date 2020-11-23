import erajs.api as a 
#此页面用于设定equipment基本模板

class equipment:
    ID = 0
    
    def __init__(self, template="1"):
        path = 'equipment_mode'
        equipment.ID = equipment.ID + 1
        self.ID = equipment.ID
        self.Type = "equipment"
        self.template = template
        self.level = 1
        self.name = a.dat()[path][template]['name']
        self.owner = None                               #此处考虑填写拥有者ID？
        self.skill = a.dat()[path][template]['skill']   #考虑从已有技能中选取
        self.value = a.dat()[path][template]['value']
        self.growth = a.dat()[path][template]['growth']
        self.grade = a.dat()[path][template]['grade']
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

