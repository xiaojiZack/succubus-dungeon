#游戏主程序
version = '0.0.1'
import erajs.api as a
import page.creat_new_game as creat_new_game
from control.succubus import succubus

def title():
    a.page
    a.mode()
    a.t('这里是主页面')
    a.mode('grid',1)
    a.t()
    a.b('新的旅程', a.goto, creat_new_game.select_succubus)
    a.t()

def test():
    a.page
    a.mode
    x = succubus(1)
    a.t(x.name)

def main():
    a.init()
    a.mode('grid', 1)
    a.h('Succubus Dungeon')
    a.t()
    a.t()
    a.t('version {}'.format(version))
    a.t()
    a.b('苏醒',a.goto, title)
    a.t()
    a.b('测试用', a.goto, test)


#---------------
main()