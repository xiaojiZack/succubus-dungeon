#游戏主程序
version = '0.0.1'
import erajs.api as a


def main():
    a.init()
    a.mode('grid', 1)
    a.h('Succubus Dungeon')
    a.t()
    a.t()
    a.t('version {}'.format(version))

    
#---------------
main()