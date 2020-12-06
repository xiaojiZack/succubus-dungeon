#创建新存档界面
import erajs.api as a
from page.main import show_main 
from control.succubus import succubus 

def change_number(dir):
    #修改 选择序号并刷新页面
    number_of_succubus = a.dat()['overall']['number_of_succubus']
    number = (number+dir+number_of_succubus) % number_of_succubus
    a.repeat()

def select_difficulty():
    def goto_difficulty(difficulty):
        a.clear()
        #初始化新游戏，考虑之后用一个函数代替，此处先作测试用途
        a.tmp()['day'] = 1
        a.tmp()['money'] = 0
        a.tmp()['semen'] = 0
        a.tmp()['day_time'] = '日间'
        a.tmp()['capture_list'] = []
        a.tmp()['family_list'] = []
        a.tmp()['difficulty'] = difficulty
        show_main()
        
    #选择难度
    a.page()
    a.mode('grid', 1)
    a.h('前往哪一个世界？')
    a.divider()

    a.mode()
    #此处放置难度世界列表
    a.b('普通', goto_difficulty, 1)
    a.divider()
    a.mode('line',1)
    a.b('返回', a.back)

def select_ban():
    #选择禁用
    a.page()
    a.mode()
    a.t('敬请期待')
    a.t()
    a.b('困顿', a.goto, select_difficulty)

def select_inherit():
    #选择继承
    a.page()
    a.mode()
    a.t('敬请期待')
    a.t()
    a.b('绝缘', a.goto, select_ban)

def select_location():
    #选择出生地
    def change_location(selection):
        # description = a.dat()['location'][location['value']]['description']
        # a.t(description)
        a.tmp()['location_mode'] = selection['index']
        a.repeat()
        pass
    a.page()
    a.mode('grid',1)
    a.t('何处？')
    a.divider()
    a.mode()
    a.t()
    a.t()
    a.radio(['平原'], change_location, a.tmp()['location_mode'])
    a.t()
    description = a.dat()['location'][a.tmp()['location_mode']]['description']
    a.t(description)
    a.t()
    a.divider()
    a.b('下一步', a.goto, select_inherit)
    a.t()
    a.b('何人？', a.back)

def select_succubus(number=0):
    #选择起源模板
    def goto_select_location(number):
        a.tmp()['succubus'] = succubus(number)
        a.tmp()['succubus_mode'] = number
        a.tmp()['location_mode'] = 0
        a.goto(select_location)
    a.page()
    a.mode('grid',1)
    a.h('起源')
    a.t()
    a.divider()

    a.mode('grid',3)
    a.b('<--', change_number, -1)
    a.t()
    a.t('何人?')
    a.t()
    a.b('-->', change_number, 1)
    a.divider()

    a.mode('grid',3)
    selected_mode = succubus()
    a.t()
    a.h(selected_mode.name, style={'opacity': '0.6'})
    a.t()
    a.t()
    a.t('生命：{}'.format(selected_mode.health))
    a.t()
    a.t('攻击：{}'.format(selected_mode.atk))
    a.t()
    a.t('防御：{}'.format(selected_mode.dEf))

    for i in range(3):
        a.t()
    
    a.t()
    a.t()
    a.t(selected_mode.description, style={'font-style':'italic'})
    a.t()

    for i in range(3):
            a.t()

    a.t()
    a.t()
    a.b('何处?', goto_select_location, number)
    a.t()

    a.divider()
    a.mode()
    a.b('沉睡',a.back)

