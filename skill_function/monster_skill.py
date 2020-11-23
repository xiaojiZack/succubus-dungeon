import erajs.api as a 
#部分技能效果
from control.skill import skill as t 

class MS1(t):
    #"再生"

    def __init__(self):
        super(MS1,self).__init__(1)
    
    def trigger(self, subject, action=None, obejct=None):
        #本技能触发条件，subject为技能拥有者，object为对象，action为伴随动作
        if action == "be hitten":
            subject.addbuff(a.dat()["buff_list"]["再生"][id], 1)



