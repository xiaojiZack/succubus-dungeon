import erajs.api as a 
#此页面用于设定facility基本模板

class facility:
    ID = 0
    
    def __init__(self, template="1"):
        path = 'facility_mode'
        facility.ID = facility.ID + 1
        self.ID = facility.ID
        self.Type = "facility"
        self.template = template
        self.level = 1
        self.name = a.dat()[path][template]['name']
        self.skill = a.dat()[path][template]['skill']
        self.capacity = a.dat()[path][template]['capacity']
        self.value = a.dat()[path][template]['value']
        self.growth = a.dat()[path][template]['growth']
        self.description = a.dat()[path][template]['description']

    def change(self, key, value):
        eval("self.{} = value".format(key))

    def normal_upgrade(self, up_level):
        i = 0
        grow = 0
        while grow in self.growth:
            self.value[i] = grow*up_level
            i = i+1

