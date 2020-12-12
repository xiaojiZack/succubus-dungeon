import erajs.api as a 

def settings():
    #设置相关
    pass

def save_button():
    #存档
    pass

def load_button():
    #读档
    pass

def giveup():
    #放弃
    pass

def sys_buttons():
    a.divider()
    a.mode('grid', 4)
    a.b('存档', a.goto, save_button)
    a.t()
    a.b('读档', a.goto, load_button)
    a.t()
    a.b('设置', a.goto, settings)
    a.t()
    a.b('放弃', a.goto, giveup)