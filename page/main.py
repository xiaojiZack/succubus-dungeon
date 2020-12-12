import erajs.api as a 
from page.component.status_bar import status_bar
from page.component.fatemap import fate_map
from page.component.check_item import check_buttons
from page.component.sys_items import sys_buttons

#def status_bar():
    # a.divider()
    # #状态栏
    # a.mode('grid', 4)
    # a.t('第{}天'.format(a.tmp()['day']))
    # a.t('{}'.format(a.tmp()['day_time']), style={'color': '#ff0'})
    # a.t()
    # a.t('{}'.format(a.tmp()['succubus'].name))
    # a.t()
    # a.t('{}G'.format(a.tmp()['money']))
    # a.t()
    # a.t('{}ml'.format(a.tmp()['semen']))
    # a.t()

    # a.t('level:{}'.format(succubus.level))
    # a.t()
    # a.t('生命')
    # a.progress(succubus.health-50, succubus.max_health, [{"width": "100px"}, {"background-color": "#0f0"}])
    # a.t('{}/{}'.format(succubus.health, succubus.max_health))
    # a.t()
    # a.t('俘虏:{}'.format(len(data['prisoner_list'])))
    # a.t()
    # a.t('succubus:{}'.format(len(data['family_list'])))

def show_main():
    #此处为测试用界面0.1
    data = a.tmp()
    succubus = data['succubus']
    a.page()
    a.mode()
    a.t('此处为主界面')

    status_bar() #状态栏

    #考虑放置每日三选一计划或者是地宫结构图？
    fate_map()

    #考虑放置一些检查选项，如检查设施情况，查看配方，已经拥有的遗物，查看地宫结构等。
    check_buttons()

    #考虑放置系统相关，如设置，存读档案，回到标题，放弃等
    sys_buttons()