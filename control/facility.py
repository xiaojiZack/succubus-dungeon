import erajs.api as a 
#此页面用于设定facility基本模板

class facility:
    ID = 0
    
    def __init__(self, template="1"):
        path = 'facility'
        facility.ID = facility.ID + 1
        self.ID = facility.ID
        self.Type = "facility"
        self.template = template
        self.level = 1
        self.name = a.dat()[path][template]['name']
        self.skill = a.dat()[path][template]['skill']
        self.growth = a.dat()[path][template]['growth']
        self.description = a.dat()[path][template]['description']
        self.alive = True