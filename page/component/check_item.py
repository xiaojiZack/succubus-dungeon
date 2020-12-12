import erajs.api as a 

def check_monster():
    #检查手上拥有的怪物
    pass

def check_facility():
    #检查地宫设施
    pass

def check_formula():
    #检查可合成配方
    pass

def check_reliquary():
    #检查遗物
    pass

def check_information():
    #显示杂项信息，如当前战斗难度，禁用，恶堕情况
    pass

def check_prisoner():
    #检查俘虏情况
    pass

def check_family():
    #检查眷族
    pass

def check_Illustrated():
    #检查图鉴
    pass


def check_buttons():
    #考虑放置一些检查选项，如检查设施情况，查看配方，已经拥有的遗物，查看地宫结构等。
    a.divider(text='查看')
    a.mode('grid', 5)
    a.b('拥有怪物', a.goto, check_monster)
    a.t()
    a.b('地宫设施', a.goto, check_facility)
    a.t()
    a.b('俘虏', a.goto, check_prisoner)
    a.t()
    a.b('眷族', a.goto, check_family)
    a.t()
    a.b('配方', a.goto, check_formula)
    a.t()
    a.b('遗物', a.goto, check_reliquary)
    a.t()
    a.b('杂项', a.goto, check_information)
    a.t()
    a.b('图鉴', a.goto, check_Illustrated)