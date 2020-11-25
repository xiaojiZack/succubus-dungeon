#创建新存档界面
import erajs.api as a
from control.succubus import succubus 

def change_number(dir):
    number_of_succubus = a.dat()['overall']['number_of_succubus']
    number = (number+dir+number_of_succubus) % number_of_succubus
    a.repeat()

def select_difficulty():
    #选择难度
    a.page()
    a.mode()
    a.t('敬请期待')
    a.t()
    a.b('苏醒')

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

def select_loation():
    #选择出生地
    a.page()
    a.mode()
    a.t('敬请期待')
    a.t()
    a.b('轮回', a.goto, select_inherit)

def select_succubus(number=0):
    #选择起源模板
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
    a.b('何处?', a.goto, select_loation)
    a.t()

    a.divider()
    a.mode()
    a.b('沉睡',a.back)

