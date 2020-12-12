import erajs.api as a 
import random
from page.component.blankpage import blank_page

class fate_card():

    def __init__(self, type = 0):
        cards = a.dat()['fatecard'][type]
        self.name = cards['name']
        self.picture = cards['picture']
        self.is_able = False
        self.type = type
        self.page = blank_page
        self.get_page()
        self.style = cards['style']
    
    def get_page(self):
        if self.type == 0:
            self.page = blank_page
        elif self.type == 1:
            pass

    def print_card(self, is_able = True):
        #根据输入的卡片类型打印相应卡片按钮
        my_style = {'white-space':'pre-wrap'}
        my_style.update(self.style)
        a.b(self.picture, a.goto, self.page,
            disabled=is_able, style=my_style, popup=self.name)
        

def random_create():    
    #生成简易图纸,1战斗2精英战斗3活动4怪物商人5设施商人6装备商人7黑商8休息9决战
    map = {1:[], 19:[], 20:[]}
    for i in range(1, 10+1):
        map[1].append(1)
        map[19].append(8)
        map[20].append(9)
    map[2] = []
    for i in range(2, 18+1):
        map[i] = []
        for j in range(1, 10+1): #提供fate卡出现概率
            rand = random.randint(0,100)
            t = 1
            if rand<40:
                t=1
            elif rand<60:
                t=2
            elif rand<70:
                t=3
            elif rand<75:
                t=4
            elif rand<80:
                t=5
            elif rand<85:
                t=6
            elif rand<90:
                t=7
            elif rand<=100:
                t=8
            map[i].append(t)
    a.tmp()['fate_map'] = map

def fate_map():
    #每日走向选择展示
    a.divider(text='前路')
    a.mode('grid', 10)
    random_create()
    for i in range(1,20+1):
        for j in range(0, 10):
            card = fate_card(a.tmp()['fate_map'][21-i][j])
            card.print_card(is_able=True)
            #a.t(a.tmp()['fate_map'][i][j]) 测试用
            a.t()
    




#测试用————————————————————
    #for i in range(0,10):
        # a.t('┏')
        # for j in range(0, len('┃ ☢ ┃')):
        #     a.t('━')
        #a.t('┓')
#         a.b('''
#   ＿
# =|¿|=
#   ￣''', a.goto, blank_page, style={'white-space':'pre-wrap'})
        # a.t('┗')
        # for j in range(0, len('┃ ☢ ┃')):
        #     a.t('━')
        # a.t('┛')
        #a.t()

