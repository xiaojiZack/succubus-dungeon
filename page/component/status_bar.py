import erajs.api as a 
def status_bar():
    data = a.tmp()
    succubus = data['succubus']
    a.divider()
    #状态栏
    a.mode('grid', 4)
    a.t('第{}天'.format(a.tmp()['day']))
    a.t('{}'.format(a.tmp()['day_time']), style={'color': '#ff0'})
    a.t()
    a.t('{}'.format(a.tmp()['succubus'].name))
    a.t()
    a.t('{}G'.format(a.tmp()['money']))
    a.t()
    a.t('{}ml'.format(a.tmp()['semen']))
    a.t()

    a.t('level:{}'.format(succubus.level))
    a.t()
    a.t('生命')
    a.progress(succubus.health, succubus.max_health, [{'width': '100px'}, {'background-color': '#0f0'}])
    a.t('{}/{}'.format(succubus.health, succubus.max_health))
    a.t()
    a.t('俘虏:{}'.format(len(data['prisoner_list'])))
    a.t()
    a.t('succubus:{}'.format(len(data['family_list'])))