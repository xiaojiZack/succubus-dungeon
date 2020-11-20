import erajs.api as a 
#此页面用于设定skill基本模板

class skill:

    def __init__(self, id):
        path = "skill.1"
        self.id = id
        self.name = a.dat()[path][id]["name"]
        self.type = a.dat()[path][id]["type"]
        self.grade = a.dat()[path][id]["grade"]
        self.priority = a.dat()[path][id]["priority"]
        self.cool_down = a.dat()[path][id]["cool_down"]
        self.description = a.dat()[path][id]["description"]
        self.ready = True
        
    def change(self,key, value):
        eval("self.{} = value".format(key))
