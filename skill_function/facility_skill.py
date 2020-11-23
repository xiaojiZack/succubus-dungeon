import erajs.api as a 
#部分设施技能效果
#本技能触发条件，subject为设施内布置人员，
# object为入侵设施人员，action为伴随动作
from control.skill import skill as t 

class FS1(t):
    #"战斗"
    #"给布置其中的怪物提供额外最大生命值"

    def __init__(self, value=None):
        super(FS1,self).__init__(1)
        self.value = value
    
    def trigger(self, subject=None, action=None, obejct=None):
        #本技能触发条件，subject为设施内布置人员，
        # object为入侵设施人员，action为伴随动作
        if action == "begin_battle":
            for i in subject:
                i.addbuff(a.dat()["buff_list"]["最大生命值"][id], self.value[0])
       


