import erajs.api as a 
#部分技能效果
#from control.skill import skill as t 
#reliquary类技能考虑不继承skill模板

class RS1():
    #破稿子
   
   def __init__(self, value):
       self.value = value
       a.tmp()["dig_speed"] = self.value[0]
    