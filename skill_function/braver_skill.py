import erajs.api as a 
#部分技能效果
from control.skill import skill as t 

class BS1(t):
    #"农民"

    def __init__(self):
        super(BS1,self).__init__("braver", 1)
    
    def trigger(self, subject, action=None, obejct=None):
        #本技能触发条件，subject为技能拥有者，object为对象，action为伴随动作
        pass