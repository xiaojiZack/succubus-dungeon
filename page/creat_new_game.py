#创建新存档界面
import erajs.api as a

def select_succubus():
    #选择模板
    a.page()
    a.mode()
    a.t('select')
    a.t()
    
    a.b('返回',a.back)
