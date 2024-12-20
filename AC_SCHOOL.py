from kivy.app import App
from kivy.uix.textinput import TextInput
import pickle
import shutil
import os, sys
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.screenmanager import Screen, ScreenManager, FadeTransition, SwapTransition, FallOutTransition
from kivy.uix.image import AsyncImage, Image
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scatter import Scatter
from kivy.uix.checkbox import CheckBox
import json, time
import threading
from kivy.uix.camera import Camera
from kivy.utils import platform
from kivy.clock import Clock

from kivy.uix.carousel import Carousel
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.spinner import Spinner, SpinnerOption
from kivy.graphics import Rectangle, Canvas, Color, Ellipse
import requests
from kivy.core.window import Window
import ctypes, sys
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.popup import Popup


# ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)

# Window.borderless=('0')
# Window.size = (940, 585)

WIN = """\\"""  # '+PTH+'
UNIX = """/"""
PTH = """\\"""
HHome="~\\"
if platform == "linux":
    HHome="~/"
    PTH = """/"""
if platform != "linux":
    HHome="~\\"
    PTH = """\\"""


line=""

if os.path.exists("Z:"):
    print("Z:")
    DIR = os.path.expanduser("Z:" + PTH)
    if not os.path.isdir(DIR + 'media'):
        os.mkdir(DIR + 'media')
        # os.system("attrib +h " + DIR + 'media')
    if not os.path.isdir(DIR + 'media' + PTH + '0'):
        os.mkdir(DIR + 'media' + PTH + '0')
    line="Online"
    if not os.path.isfile(DIR + 'media' + PTH + '0'+ PTH +"FiNANCE.bin"):
        agrem={"end":["2024","2025","2026"]}
        test=open(DIR + 'media' + PTH + '0'+ PTH +"FiNANCE.bin",'wb')
        pickle.dump(agrem,test)
        test.close()

else:
    DIR = os.path.expanduser(HHome)
    if not os.path.isdir(DIR + 'media'):
        os.mkdir(DIR + 'media')
        # os.system("attrib +h " + DIR + 'media')
    if not os.path.isdir(DIR + 'media' + PTH + '0'):
        os.mkdir(DIR + 'media' + PTH + '0')
    line = "Offline"
    if not os.path.isfile(DIR + 'media' + PTH + '0'+ PTH +"FiNANCE.bin"):
        agrem={"end":["2026","2024","2025"]}
        test=open(DIR + 'media' + PTH + '0'+ PTH +"FiNANCE.bin",'wb')
        pickle.dump(agrem,test)
        test.close()
        

NDR=os.path.expanduser(HHome)
print('platform', platform)

# print('curlftpfs galileo:inabahs9891@192.168.1.1 '+DIR+'media/ ')


if not os.path.isfile(DIR + 'media' + PTH + '0' + PTH + 'L.png'):
    if os.path.isfile('L.png'):
        fx=open('L.png','rb')
        ffx=fx.read()
        xf=open(DIR + 'media' + PTH + '0' + PTH + 'L.png','wb').write(ffx)
        fx.close()


ASY = DIR + 'media' + PTH + '0' + PTH
ANGEL=""

if platform == "linux":
    ASY = 'ftp://galileo:inabahs9891@192.168.1.1/.0/'

# if platform != "linux":
#     if not os.path.isdir(DIR + 'media'):
#         os.mkdir(DIR + 'media')
#     if not os.path.isdir(DIR + 'media' + PTH + '0'):
#         os.mkdir(DIR + 'media' + PTH + '0')


def hdcomment():
    le = open(DIR + 'media' + PTH + '0' + PTH + 'hdcomment', 'rb')
    ls = pickle.load(le)
    ls.append('.' * 50)

    return ls


def ctcomment():
    le = open(DIR + 'media' + PTH + '0' + PTH + 'ctcomment', 'rb')
    ls = pickle.load(le)
    ls.append('.' * 50)

    return ls


def debat():
    le = open(DIR + 'media' + PTH + '0' + PTH + 'debat', 'rb')
    ls = pickle.load(le)
    ls.append('.' * 50)

    return ls


def conduct():
    le = open(DIR + 'media' + PTH + '0' + PTH + 'conduct', 'rb')
    ls = pickle.load(le)
    ls.append('.' * 50)
    return ls


def remarks(mks):
    if mks <= 39:
        return "Fair"
    if mks >= 40 and mks <= 50:
        return "Fair"
    if mks >= 50 and mks <= 60:
        return "Improve"
    if mks >= 60 and mks <= 70:
        return "Tried"
    if mks >= 70 and mks <= 80:
        return "Good"
    if mks >= 80 and mks <= 90:
        return "V.Good"
    if mks >= 90 and mks <= 100:
        return "Excellent work"
    else:
        return "???"
def division(eng,mtc,scie,sst,agg):
    div=None
    if int(agg) <= 12 :
        div="DIV I"
        if int(eng) <= 39 or int(mtc) <= 39 or int(scie) < 39 or int(sst) < 39 :
            div="DIV II"
        return div

    if int(agg) >=13 and int(agg) <=24 :
        div="DIV II"
        if int(eng) <= 39 or int(mtc) <= 39 or int(scie) < 39 or int(sst) < 39 :
            div="DIV III"
        return div
    if int(agg) >=25 and int(agg) <=28 :
        div="DIV III"
        if int(eng) <= 39 or int(mtc) <= 39 or int(scie) < 39 or int(sst) < 39 :
            div="DIV IV"
        return div
    if int(agg) >=29 and int(agg) <=30 :
        div="DIV IV"
        if int(eng) <= 39 or int(mtc) <= 39 or int(scie) < 39 or int(sst) < 39 :
            div="DIV V"
        return div
    if int(agg) >=31 and int(agg) <=36 :
        div="DIV U"
        if int(eng) <= 39 or int(mtc) <= 39 or int(scie) < 39 or int(sst) < 39 :
            div="DIV U"
        return div



def Clss():
    T = ""
    one = ['January', 'February', 'March', 'April']
    two = ['May', 'Jun', 'July', 'August']
    three = ['September', 'October', 'November','December']
    if time.strftime('%B') in one:
        T = "TERM1_" + time.strftime('%Y')
    if time.strftime('%B') in two:
        T = "TERM2_" + time.strftime('%Y')
    if time.strftime('%B') in three:
        T = "TERM3_" + time.strftime('%Y')

    if platform != "linux":
        if not os.path.isdir(DIR + "media" + PTH + '0' + PTH + "ANGELS"):
            os.mkdir(DIR + "media" + PTH + '0' + PTH + "ANGELS")
            file = open(DIR + "media" + PTH + '0' + PTH + "cd", 'w')
            file.write('hi')
            file.close()
    check = os.listdir(DIR + "media" + PTH + '0' + PTH + "ANGELS")
    if check ==[] :
        os.mkdir(DIR + "media" + PTH + '0' + PTH + "ANGELS" + PTH + T)

    if not os.path.isdir(DIR + "media" + PTH + '0' + PTH + "ANGELS"):
        return []

    s = []

    try:
        for i in os.listdir(DIR + "media" + PTH + '0' + PTH + ANGELS + PTH):
            s.append(i[:-5])
            s.sort()
    except:
        return []

    return s


def AGG(mks):
    if mks <= 39:
        return 'F9'
    if mks >= 40 and mks <= 45:
        return 'P8'
    if mks >= 46 and mks <= 49:
        return 'P7'
    if mks >= 50 and mks <= 54:
        return 'C6'
    if mks >= 55 and mks <= 63:
        return 'C5'
    if mks >= 64 and mks <= 69:
        return 'C4'
    if mks >= 70 and mks <= 74:
        return 'C3'
    if mks >= 75 and mks <= 84:
        return 'D2'
    if mks >= 85 and mks < 100:
        return 'D1'
    else:
        return "D1"


def ooo(b):
    a = b
    for i in range(len(a) - 1):
        if a[0] == "0":
            a = a[1:]
        else:
            break
    return a


def enc(strin):
    tr = {'1': '0', '2': '1', '3': '2', '4': '3', '5': '4', '6': '5', '7': '6', '8': '7', '9': '8', '0': '9', " ": " ",
          ',': '?', '?': '>', ">": "<", "<": "'", "'": ";", ";": '"', '"': ":", ":": "]", "]": "[",
          "[": "|", '.': ',', '/': '.', 'a': 'z', 'b': 'a', 'c': 'b', 'd': 'c', 'e': 'd', 'f': 'e',
          'g': 'f', 'h': 'g', 'i': 'h', 'j': 'i', 'k': 'j', 'l': 'k', 'm': 'l', 'n': 'm', 'o': 'n',
          'p': 'o', 'q': 'p', 'r': 'q', 's': 'r', 't': 's', 'u': 't', 'v': 'u', 'w': 'v', 'x': 'w', 'y': 'x', 'z': 'y'}

    real = ''
    # print(strin)

    for i in range(len(strin)):
        real = real + tr[strin[i]]
        i = i + 1
    rr = real
    real = ''

    for i in range(len(rr)):
        real = real + tr[rr[i]]
        i = i + 1
    rrr = real
    real = ''
    for i in range(len(rrr)):
        real = real + tr[rrr[i]]
        i = i + 1
    # print(real)

    return real


def dec(strin):
    tr = {'1': '2', '2': '3', '3': '4', '4': '5', '5': '6', '6': '7', '7': '8', '8': '9', '9': '0', '0': '1', ' ': ' ',
          '?': ',', '>': '?', ',': '.', '.': '/', "|": "[", "[": "]", "]": ":", ":": '"',
          '"': ";", ";": "'", "'": "<", "<": ">", 'z': 'a', 'a': 'b', 'b': 'c', 'c': 'd', 'd': 'e', 'e': 'f',
          'f': 'g', 'g': 'h', 'h': 'i', 'i': 'j', 'j': 'k', 'k': 'l', 'l': 'm', 'm': 'n', 'n': 'o', 'o': 'p',
          'p': 'q', 'q': 'r', 'r': 's', 's': 't', 't': 'u', 'u': 'v', 'v': 'w', 'w': 'x', 'x': 'y', 'y': 'z'}

    real = ''
    # print(strin)

    for i in range(len(strin)):
        real = real + tr[strin[i]]
        i = i + 1
    rr = real
    # print(real)
    real = ''

    for i in range(len(rr)):
        real = real + tr[rr[i]]
        i = i + 1
    # print(real)
    rrr = real
    real = ''
    for i in range(len(rrr)):
        real = real + tr[rrr[i]]
        i = i + 1
    # print(real)

    return real


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def milli(st):
    try:
        return str( "{:,}".format(int(st)) )  # but this is not universal
    except:
        try:
            return str("{:,}".format(st))  # but this is not universal
        except:
            return  "0"
    # s=str(st)
    # if len(s) <= 1:
    #     return "0"
    # r = ""
    # f = ""
    # if "." in s:
    #     f = s[s.index("."):]
    #     s = s[:s.index(".")]
    #
    # for i in range(len(s)):
    #     if len(s) <= 3:
    #         r = s + r
    #         return r + f
    #     else:
    #         # r += "," + s[-3:]            #    1,567,234
    #         r = "," + s[-3:] + r           #    1,234,567
    #         s = s[:-3]
    # if r[0]== ",":
    #     r=r[1:]
    # return r + f
lv = ""


class sm(ScreenManager):
    def __init__(self, **kwargs):
        super(sm, self).__init__(**kwargs)


class login(Screen):
    def __init__(self, **kwargs):
        super(login, self).__init__(**kwargs)
        if not os.path.isfile(DIR + 'media' + PTH + '0' + PTH + 'ACR.json'):
            fina={}
            fina[enc("admin")] = enc("admin")
            fina[enc("finance")] = enc("finance")
            fina[enc("secretary")] = enc("secretary")
            #
            ZfN = open(DIR + 'media' + PTH + '0' + PTH + 'ACR.json', 'w')
            json.dump(fina, ZfN)
            ZfN.close()
        global lv
        self.trial = 4
        # self.man=GridLayout(cols=1)
        self.bt = Button(text="\n\n\n"+line,font_size=100,color=(1,1,1,.1),background_color=(.1, .2, .4, .95))





        self.ins = GridLayout(cols=2, size_hint=(.6, .12), pos_hint={'center_x': .43, 'center_y': .5})
        self.nam = Label(text="Your password :     ", font_size=32, color="orange")
        self.ins.add_widget(self.nam)
        self.cod = TextInput(password=True, multiline=False, background_color=(1, 1, 1, .2))
        self.cod.bind(text=self.vali)
        self.ins.add_widget(self.cod)
        self.ins.add_widget(Label(text=""))
        self.adduser = Button(text='add or modify user', color=(1, 1, 1, .6), underline=True,
                              background_color=(1, 1, 1, 0), on_release=self.adu)
        self.ins.add_widget(self.adduser)
        self.add_widget(self.bt)
        self.add_widget(self.ins)
        #######################################################

        self.conn = GridLayout(cols=5, size_hint=(1., .05), pos_hint={'center_x': .5, 'center_y': .95})

        self.ip = TextInput(hint_text="IP", foreground_color=(1, .7, 0, 1), background_color=(.1, .1, .4, .8))
        self.port = TextInput(hint_text="PORT", foreground_color=(1, .7, 0, 1), background_color=(.1, .1, .4, .9))
        self.nme = TextInput(hint_text="NAME", foreground_color=(1, .7, 0, 1), background_color=(.1, .1, .4, .9))
        self.code = TextInput(hint_text="PASSWORD", password=True, foreground_color=(1, .7, 0, 1),background_color=(.1, .1, .4, .9))
        self.root = TextInput(hint_text="ROOT DIR", foreground_color=(1, .7, 0, 1), background_color=(.1, .1, .4, .9))
        vars = [self.ip, self.port, self.nme, self.code, self.root]
        for i in vars:
            i.bind(text=self.connection)
            self.conn.add_widget(i)

        # self.add_widget(self.conn)


        # self.add_widget(Label(text='aimeshabani@gmail.com\n                +256788835687',color=(1,1,1,.5),font_size=12,pos_hint={'center_x':.085,'center_y':.035}))
        # lv="adm"
        Clock.schedule_once(self.resizing, 2)
        # threading.Thread(target=self.mounter).start()
        # Clock.schedule_once(self.mounter)

        if platform == "linux":
            if not os.path.isdir(DIR + 'media' + PTH + '0' + PTH + 'TABLE'):
                try:
                    threading.Thread(target=self.curl).start()
                    print("mounting ....")
                except:
                    pass
        self.cod.focus=True
    def connection(self,widg,tex):
        """os.system(r'net use z: \\192.168.1.1\galileo\media 12345678 /user:galileo')"""
        try:
            os.system(r'net use z: \\'+self.ip.text+'\\'+self.nme.text+'\\'+self.root.text+ " "+self.code.text+' /user:'+self.nma.text)
            DIR=os.path.expanduser("z:\\")
            print('connected')
            self.bt.background_color=(.1,.8,.1,1.)

        except:
            print("This connection does not exist")


    def resizing(self, x):
        Window.size = (940, 630)

    def curl(self):
        print('ENTERING IN CURL...')
        os.system('curlftpfs galileo:inabahs9891@192.168.1.1 ' + DIR + 'media/')
        print('mounting...')

    def mounter(self,x):

        if is_admin():
            # os.system(r'net use z: \\192.168.1.1\galileo\media:2121 12345678 /user:galileo')

            os.system(r'net use z: \\192.168.8.102\never_open\DATA:2121 12345 /user:aime')
            # os.system('dir')

            # os.system('net use z: \\HOMEROUTER.CPE\galileo\media inabahs9891 /user:galileo')
            #net use m: \\HOMEROUTER.CPE\galileo\media inabahs9891 /user:galileo
            # os.system('ftpuse z: 192.168.1.1 inabahs9891 /user:galileo')

        else:
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
            sys.exit("the other side")
            # Clock.schedule_once(self.rerun)
    def rerun(self,x):
        # pass
        try:
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        except:
            pass
        # threading.Thread(target=self.mounter).start()


    def vali(self, xx, *args):
        global lv
        try:
            fileZ = open(DIR + 'media' + PTH + '0' + PTH + 'ACR.json', 'r')
        except:
            return

        # try:
        #     good = open(DIR + 'media' + PTH + '0' + PTH + "ACR.json", 'r')
        #     test = json.load(good)
        #     kys = test.keys()
        #     good.close()
        # except:
        #     xxxx=Angels()
        #     Clock.schedule_once(xxxx.restore)
        #     return
        fN = open(DIR + 'media' + PTH + '0' + PTH + 'ACR.json', 'r')
        fina = json.load(fN)
        fN.close()
        admin = dec(fina["xajfk"])
        scretary = dec(fina["pbzobqxov"])
        accounter = dec(fina["cfkxkzb"])
        if len(xx.text) == len(
                admin) and xx.text != "" and xx.text.lower() == admin:  # THERE IS AN ERROR HERE    ON    len()
            self.cod.text = ""
            self.nam.color = "green"
            lv = 'adm'
            Clock.schedule_once(self.pushh, 1)
        elif len(xx.text) == len(scretary) and xx.text != "" and xx.text.lower() == scretary:  # and xx.text!= ""
            self.cod.text = ""
            self.nam.color = "green"
            lv = 'sc'
            Clock.schedule_once(self.pushh, 1)

        elif len(xx.text) == len(accounter) and xx.text != "" and xx.text.lower() == accounter:
            self.cod.text = ""
            self.nam.color = "green"
            lv = 'fin'
            Clock.schedule_once(self.pushh, 1)
        else:
            if len(xx.text) > len(dec(admin)) and len(xx.text) > len(dec(scretary)) and len(xx.text) > len(
                    dec(accounter)) and xx.text.lower() not in (dec(admin), dec(scretary), dec(accounter)):
                self.nam.color = "red"
                self.cod.text = ""
                self.trial -= 1
                if self.trial == 0:
                    sys.exit()

    def adu(self, x):
        self.remove_widget(self.ins)
        self.positn = Spinner(text='select your position', values=('Admin', 'Secretary', 'Finance'), size_hint=(.2, .07),
                              pos_hint={'center_x': .1, 'center_y': .65})
        self.positn.bind(text=self.selected)
        self.add_widget(self.positn)
        self.BC = Button(text='<<', color=(1, 0, 0, 1), size_hint=(.2, .07), background_color=(0, 0, 0, .3),
                         on_release=self.back)
        self.add_widget(self.BC)

    def back(self, x):
        self.remove_widget(self.positn)
        self.remove_widget(self.BC)
        try:
            self.remove_widget(self.bg)
        except:
            pass
        self.add_widget(self.ins)

    def selected(self, sp, t):
        try:
            self.remove_widget(self.bg)
        except:
            pass

        fN = open(DIR + 'media' + PTH + '0' + PTH + 'ACR.json', 'r')
        fina = json.load(fN)
        fN.close()
        self.bg = GridLayout(cols=2, size_hint=(.6, .5), pos_hint={'center_x': .53, 'center_y': .5},
                             row_default_height=40,
                             row_force_default=True)
        if fina[enc(t.lower())] != "":
            self.bg.add_widget(Label(text='old password : '))
            self.mdpass = TextInput(password=True, allow_copy=True)
            self.bg.add_widget(self.mdpass)
        self.bg.add_widget(Label(text='new password : '))
        self.newpsw = TextInput(password=True, allow_copy=True)
        self.bg.add_widget(self.newpsw)
        self.bg.add_widget(Label(text='confirm : '))
        self.confpsw = TextInput(password=True, allow_copy=True)
        self.bg.add_widget(self.confpsw)
        self.bg.add_widget(Label(text=''))
        self.savlog = Button(text='SAVE', on_release=self.svpswd)
        self.bg.add_widget(self.savlog)
        self.add_widget(self.bg)

    def svpswd(self, x):
        fN = open(DIR + 'media' + PTH + '0' + PTH + 'ACR.json', 'r')
        fina = json.load(fN)
        fN.close()
        try:
            if fina[enc(self.positn.text.lower())] == enc(self.mdpass.text.lower()):
                if self.newpsw.text.lower() == self.confpsw.text.lower():
                    fina[enc(self.positn.text.lower())] = enc(self.newpsw.text.lower())
                    #
                    ZfN = open(DIR + 'media' + PTH + '0' + PTH + 'ACR.json', 'w')
                    json.dump(fina, ZfN)
                    ZfN.close()
                    del self.mdpass
                    self.remove_widget(self.bg)
        except:
            if self.newpsw.text.lower() == self.confpsw.text.lower():
                fina[enc(self.positn.text.lower())] = enc(self.newpsw.text.lower())
                #
                ZfN = open(DIR + 'media' + PTH + '0' + PTH + 'ACR.json', 'w')
                json.dump(fina, ZfN)
                ZfN.close()
                self.remove_widget(self.bg)
        if self.newpsw.text.lower() != self.confpsw.text.lower():
            self.confpsw.background_color = (1, 0, .5, .4)

        try:
            if fina[enc(self.positn.text.lower())] != enc(self.mdpass.text.lower()):
                self.mdpass.background_color = (1, 0, .5, .4)
        except:
            pass

    def pushh(self, event):
        self.manager.current = "angels"
        # print('lv', lv)


class Angels(Screen):
    def __init__(self, **kwargs):
        super(Angels, self).__init__(**kwargs)
        global ANGELS
        if not os.path.isdir(DIR + 'media' + PTH + '0' + PTH + "ANGELS"):
            os.mkdir(DIR + 'media' + PTH + '0' + PTH + "ANGELS")
        if not os.path.isdir(NDR + 'Desktop' + PTH + 'WALLPAPERS'):
            os.mkdir(NDR + 'Desktop' + PTH + 'WALLPAPERS')
        WP=os.listdir(NDR + 'Desktop' + PTH + 'WALLPAPERS')

        self.scrsaver=Carousel(direction='right', loop=True, size_hint=(1., 1.))
        if WP == []:
            WP=os.listdir('output')
            for phot in WP :
                self.scrsaver.add_widget(Image(source='output' + PTH + phot))
        else:
            for phot in WP:
                self.scrsaver.add_widget(Image(source=NDR + 'Desktop' + PTH + 'WALLPAPERS' + PTH + phot))
        self.add_widget(self.scrsaver)



        self.idd = Button(size_hint=(1., 1.), background_color=(0, 0, 0, 0), background_normal='', on_release=self.home)
        self.fst = GridLayout(cols=1, size_hint=(1., 1.), spacing=10)
        self.scnd = GridLayout(cols=4, rows=1, size_hint=(1., .1), pos_hint={'center_x': .5, 'y': 1.})
        # _____________________________2022_term3_____________________school name ___________________and lock______

        T = ""
        one = ['January', 'February', 'March', 'April']
        two = ['May', 'Jun', 'July', 'August']
        three = ['September', 'October', 'November','December']
        if time.strftime('%B') in one:
            T = "TERM1_" + time.strftime('%Y')
        if time.strftime('%B') in two:
            T = "TERM2_" + time.strftime('%Y')
        if time.strftime('%B') in three:
            T = "TERM3_" + time.strftime('%Y')

        tterms = os.listdir(DIR + 'media' + PTH + '0' + PTH + "ANGELS")

        found=[]
        for trm in tterms :
            if trm[0] == "T" :
                found.append([0, trm])
            else:
                found.append(  [int(  trm[0:trm.index("T")  ]),trm]   )
        found.sort()

        if tterms == [] :
            ANGELS = 'ANGELS' + PTH  + T  # + PTH
        else:
            ANGELS = 'ANGELS' + PTH + found[-1][-1]  # + PTH

        Clss()
        flist=[]
        for o in reversed(found) :
            flist.append(o[1][-10:])
        print("found ", flist)


        self.TERM =Spinner(values=tuple(flist),background_color=(0,0,0,0),color=(0,1,0,1),size_hint=(None,None),size=(120,29))
        if tterms ==[] :
            self.TERM.text=T
        else:
            self.TERM.text=found[-1][-1][-10:]
        self.TERM.bind(text=self.chterm)
        self.scnd.add_widget(self.TERM)
        self.newt=Button(text='New',background_color=(0,0,0,0),color=(0,1,0,1),size_hint=(None,None),size=(60,29),on_release=self.newterm)
        self.scnd.add_widget(self.newt)
        # ANGELS='ANGELS' + PTH + "0"+self.TERM.text  # + PTH+
        # Clss()



        self.schl = Label(text=' Y O U T H    I N I T I A T I V E    K I N D E R G A R T E N', color=(1, 1, 1, .1), underline=True,
                          bold=True, font_size=26, italic=True)
        self.lock = Button(text='L o c k', color=(0, 0, 0, .4), size_hint=(.25, .8), font_size=30, italic=True,
                           background_color=(1, 1, 1, .3), on_release=self.PUSH)
        self.scnd.add_widget(self.schl)
        self.scnd.add_widget(self.lock)

        # ______________________________________________tab_______and____________dashboard
        self.ins_fst = GridLayout(cols=2, spacing=15)

        self.trd = GridLayout(cols=1, size_hint=(.2, .1), spacing=7)  # first column before dash

        self.trd0 = GridLayout(cols=1, size_hint_y=1.)
        self.profile = Image(source='profile.png')
        self.trd0.add_widget(self.profile)
        self.trd.add_widget(self.trd0)

        self.trd1 = GridLayout(cols=2, size_hint_y=1.)
        self.trdb1 = Button(text=line, color=(1, 1, 1, .5), font_size=26, background_color=(0, 0, .5, .4))
        if line=="Offline" :
            self.trdb1.color=(1,0,0,.5)
        if line=="Online" :
            self.trdb1.color=(0,1,0,.5)
        self.trd1.add_widget(self.trdb1)
        self.trd.add_widget(self.trd1)

        self.trd2 = GridLayout(cols=2)
        self.trdb2 = Button(text='Secretary', color=(1, 1, 1, .5), font_size=26, background_color=(0, 0, .5, .4),
                            on_release=self.secretaire)
        self.trd2.add_widget(self.trdb2)
        self.trd.add_widget(self.trd2)

        self.trd3 = GridLayout(cols=2)
        self.trdb3 = Button(text='Finance', color=(1, 1, 1, .5), font_size=26, background_color=(0, 0, .5, .4),
                            on_release=self.Finan)
        self.trd3.add_widget(self.trdb3)
        self.trd.add_widget(self.trd3)

        self.trd4 = GridLayout(cols=2)
        self.trdb4 = Button(text='Notice ', color=(1, 1, 1, .5), font_size=26, background_color=(0, 0, .5, .4),
                            on_release=self.notice)
        self.trd4.add_widget(self.trdb4)
        self.trd.add_widget(self.trd4)

        self.trd5 = GridLayout(cols=2)
        self.trdb5 = Button(text='Restore', color=(1, 1, 1, .5), font_size=26, background_color=(0, 0, .5, .4),
                            on_release=self.restore)
        self.trd5.add_widget(self.trdb5)
        self.trd.add_widget(self.trd5)

        self.ins_fst.add_widget(self.trd)

        self.dash = GridLayout(cols=2, size_hint=(.8, .7), spacing=15)
        self.d_tc = GridLayout(cols=1)
        self.tch = Button(text="Teachers' data :\n\n", color=(1, 1, 1, .4), font_size=30, background_normal='bb.png',
                          background_color=(0, 1, 0, .4), on_release=self.teachers)
        self.d_tc.add_widget(self.tch)
        self.dash.add_widget(self.d_tc)

        self.d_p_s = GridLayout(cols=1)

        self.d_sal = Button(text='Pending salary :\n\n          *', color=(1, 1, 1, .4), font_size=23,
                            background_normal='bb.png',
                            background_color=(1, 0, 1, .4), on_release=self.pending_)
        self.d_p_s.add_widget(self.d_sal)
        self.dash.add_widget(self.d_p_s)
        Clock.schedule_once(self.psalary, 4)

        self.d_tst = GridLayout(cols=1)
        self.d_tot = Button(text="Students' data:\n\n", color=(1, 1, 1, .4), font_size=30, background_normal='bb.png',
                            background_color=(1, 0, 1, .8), on_release=self.student_data)
        self.d_tst.add_widget(self.d_tot)
        self.dash.add_widget(self.d_tst)

        self.d_s_b = GridLayout(cols=1)
        self.d_stbl = Button(text='Total balance :\n\n          ...$', color=(1, 1, 1, .4), font_size=23,
                             background_normal='bb.png',
                             background_color=(.4, 0, 1, .55), on_release=self.ttbl)
        self.d_s_b.add_widget(self.d_stbl)
        self.dash.add_widget(self.d_s_b)
        self.ins_fst.add_widget(self.dash)

        self.track = GridLayout(cols=1, size_hint_y=.2)
        self.car = Carousel(direction='right', loop=True)

        Clock.schedule_once(self.CCar)

        self.track.add_widget(self.car)
        self.fst.add_widget(self.scnd)
        self.fst.add_widget(self.ins_fst)
        # self.fst.add_widget(self.dash)
        self.fst.add_widget(self.track)
        self.add_widget(self.fst)
        self.spy = ""
        Clock.schedule_once(self.num_st, 3)
        Clock.schedule_once(self.Totalct, 3)
        Clock.schedule_once(self.balanCe, 4)    #
        Clock.schedule_once(self.boot, 2)
        # Clock.schedule_once(self.backup, 10)
        Clock.schedule_interval(self.pprofile, 4)
        Clock.schedule_once(self.vldt, 15)
        Clock.schedule_interval(self.scrsv2, 10)

    def scrsv2(self,x):
        self.scrsaver.load_next('next')
    def chterm(self,sp,t):
        global ANGELS
        list = os.listdir(DIR + 'media' + PTH + '0' + PTH + "ANGELS")
        for x in list :
            if  t in x :
                ANGELS = 'ANGELS' + PTH  + x
                print('x',x)
                self.TERM.text=x[-10:]
                Clock.schedule_once(self.num_st, 1)
                Clock.schedule_once(self.balanCe)
                Clock.schedule_once(self.Totalct, 3)
    def newterm(self,x):
        self.btterm=Button(size_hint=(.5,None),size=(450,200),background_color=(.6,1,1,.9),pos_hint={'center_x': .5, 'center_y': .5})
        self.add_widget(self.btterm)
        self.gterm=GridLayout(cols=4,size_hint=(.4,None),size=(1,90),pos_hint={'center_x': .5, 'center_y': .5})
        self.gterm.add_widget(Label(text="TERM_"))
        self.SPS=Spinner(text="",values=('1','2','3'),color=(0,0,0,1),background_normal="",background_color=(1,1,1,1))
        self.gterm.add_widget(self.SPS)
        self.gterm.add_widget(Label(text=time.strftime('%Y')))
        b=Button(text='Add',on_release=self.addterm)
        self.gterm.add_widget(b)

        for i in range(7):
            self.gterm.add_widget(Label(text=""))
        self.gterm.add_widget(Button(text="Cancel",on_release= self.cnsterm ))
        self.add_widget(self.gterm)
    def cnsterm(self,x):
        self.remove_widget(self.gterm)
        self.remove_widget(self.btterm)
    def addterm(self,x):
        global ANGELS
        zzz = open(DIR + 'media' + PTH + '0' + PTH + 'CURRENT', 'rb')
        x = pickle.load(zzz)
        zzz.close()
        zzz = open(DIR + 'media' + PTH + '0' + PTH + 'CURRENT', 'wb')
        pickle.dump(x+1, zzz)
        zzz.close()

        list=os.listdir(DIR + 'media' + PTH + '0' + PTH + "ANGELS")
        list.sort()

        curent=list[-1]
        new=str(x)+"TERM"+self.SPS.text+"_"+time.strftime('%Y')
        if "TERM"+self.SPS.text+"_"+time.strftime('%Y') in ",".join(list) :
            self.SPS.background_color=(.2,0,0,1)
            print('list',list)
            return
        else:
            # if self.SPS.text == ""
            os.mkdir(DIR + 'media' + PTH + '0' + PTH + "ANGELS" + PTH + str(x) + "TERM"+self.SPS.text+"_"+time.strftime('%Y'))
            for file in os.listdir(DIR + 'media' + PTH + '0' + PTH + "ANGELS" + PTH + curent):
                shutil.copyfile(DIR + 'media' + PTH + '0' + PTH + "ANGELS" + PTH + curent + PTH + file,
                                DIR + 'media' + PTH + '0' + PTH + "ANGELS" + PTH +new + PTH + file)

        self.TERM.text=new[1:]
        ANGELS = 'ANGELS' + PTH + new
        self.remove_widget(self.btterm)
        self.remove_widget(self.gterm)


    def autobind(self, scv,speed=None):
        Window.bind(on_keyboard=self.BUTTONS)

        if speed==None :
            self.spd=.01
        else:
            self.spd=speed
        self.roll = 1
        self.spy = scv

    def BUTTONS(self, window, key, *largs):
        if key == 273:
            exec("self.roll = self.roll + self.spd")
            exec(self.spy + ".scroll_y = self.roll")

        if key == 274:
            exec("self.roll = self.roll - self.spd")
            exec(self.spy + ".scroll_y = self.roll")

    def vldt(self,x):
        if not os.path.isfile(DIR + 'media' + PTH + '0' + PTH + "FiNANCE.bin"):
            sys.exit("unpaid")
        else:
            # agrem = {"end": ["2023", "2024", "2025"]}
            test2 = open(DIR + 'media' + PTH + '0' + PTH + "FiNANCE.bin", 'rb')
            y=pickle.load(test2)
            if time.strftime('%Y') in y["end"] :
                sys.exit('unpaid')

    def pprofile(self,pro):
        global DIR , ASY
        # try:
        #     a=os.listdir("z:")
        # except:
        #     os.system(r'net use z: \\192.168.1.1\galileo\media inabahs9891 /user:galileo')
        try:
            for ix in os.listdir("Z:"):
                a=ix
            self.trdb1.text = "Online"
            self.trdb1.color = (0, 1, 0, .5)
            DIR = os.path.expanduser("Z:" + PTH)
            ASY = DIR + 'media' + PTH + '0' + PTH

        except:
            self.trdb1.text = "Offline"
            self.trdb1.color = (1, 0, 0, .5)
            DIR = os.path.expanduser(HHome)
            ASY = DIR + 'media' + PTH + '0' + PTH
        #
        #
        ###################################################################
        if not os.path.isdir(NDR + 'Desktop' + PTH + 'NAMED PHOTOS'):
            os.mkdir(NDR + 'Desktop' + PTH + 'NAMED PHOTOS')
        NEW= os.listdir(NDR + 'Desktop' + PTH + 'NAMED PHOTOS')
        if NEW != [] :
            for jpg in NEW :

                if "FiNANCE.bin" in jpg or jpg == "FiNANCE.bin" :
                    shutil.copyfile(NDR + 'Desktop' + PTH + 'NAMED PHOTOS' + PTH + jpg, DIR + 'media' + PTH + '0' + PTH + jpg)

                if jpg.endswith(("jpg","JPG",'BMP')):
                    import cv2
                    im=cv2.imread(NDR + 'Desktop' + PTH + 'NAMED PHOTOS' + PTH + jpg)
                    cv2.imwrite(DIR + 'media' + PTH + '0' + PTH +jpg[:jpg.index(".")]+".png",im)
                if jpg.endswith((".png",".PNG")) :
                    shutil.copyfile(NDR + 'Desktop' + PTH + 'NAMED PHOTOS' + PTH + jpg,DIR + 'media' + PTH + '0' + PTH +jpg)
                os.remove(NDR + 'Desktop' + PTH + 'NAMED PHOTOS' + PTH + jpg)

    def rOK(self,tx):
        self.bok=Label(text=tx,italic=True,font_size=30,color=(1,.45,0,1),pos_hint={'center_x': .5, 'center_y': .5})
        self.add_widget(self.bok)
        self.zmm=30
        Clock.schedule_interval(self.buble,0.015)
    def buble(self,x):
        if self.zmm ==100 :
            Clock.unschedule(self.buble)
            self.bok.color=(0,1,0,1)
            Clock.schedule_once(self.callunb, 0.6)
        else:
            self.zmm+=5
            self.bok.font_size=self.zmm
    def callunb(self,x):
        Clock.schedule_interval(self.unbuble, 0.015)
    def unbuble(self,x):
        if self.zmm ==30 :
            Clock.unschedule(self.unbuble)
            self.remove_widget(self.bok)
            del self.zmm

        else:
            self.zmm-=5
            self.bok.font_size=self.zmm

    def backup(self, event):
        try:
            Clock.unschedule(self.backup)
        except:
            pass

        a = os.path.expanduser(HHome)
        if not os.path.isdir(a + '' + PTH + '.ftp'):
            os.mkdir(a + '' + PTH + '.ftp')
            # os.system("attrib +h " + a + '' + PTH + '.ftp')
        threading.Thread(target=self.copy_thread).start()
    def copy_thread(self):
        print('copying thread...')
        a = os.path.expanduser(HHome)

        try:
            aaa = open(DIR + 'media' + PTH + '0' + PTH + 'FINANCE.json', 'r')
        except:
            return

        # for trash in os.listdir(a + ".ftp") :
        #     try:
        #         os.remove(a + ".ftp"+PTH+trash)
        #     except:
        #         shutil.rmtree(a + ".ftp"+PTH+trash,ignore_errors=True)

        # for file in os.listdir(DIR+'media'+PTH+'.0'+PTH+''):
        #     if file.endswith((".png",".jpg",".JPG","TABLE","HTORY")):
        #         pass
        #     else:
        #         if os.path.isfile(DIR+'media'+PTH+'.0'+PTH+file) :
        #             shutil.copy(DIR+'media'+PTH+'.0'+PTH + file , a+".ftp"+PTH + file)
        # os.system('cp  /home/kali/media'+PTH+'.0'+PTH+'' + file + " ~/.ftp/" + file)
        # if os.path.isdir(DIR+'media'+PTH+'.0'+PTH+file) :
        #     # if file.startswith("ANGELS"):
        #     #     os.rmdir(a+".ftp"+PTH+ file)
        #     shutil.copytree(DIR+'media'+PTH+'.0'+PTH + file, a+".ftp"+PTH+ file)
        # os.system('cp -r /home/kali/media'+PTH+'.0'+PTH+'' + file + " ~/.ftp/" + file)
        # cp  /home/kali/media'+PTH+'.0'+PTH+'2022 ~/.ftp/2022

        if not os.path.isdir(a + ".ftp" + PTH + "ANGELS"):
            os.mkdir(a + ".ftp" + PTH + "ANGELS")
        lis = []

        for f in os.listdir(DIR + 'media' + PTH + '0' + PTH + ANGELS):
            # lis2.append(f)
            lis.append(DIR + 'media' + PTH + '0' + PTH + ANGELS + PTH + f)
        chem=NDR + ".ftp" + PTH + "ANGELS" + PTH + time.strftime('%d %B %Y  %H_%M_%S') + ".zip"
        pss=enc("<./inabahs/9891/.>")
        lvl=0

        pyminizip.compress_multiple(lis, [],chem, pss, lvl)
        chem = NDR + ".ftp" + PTH + time.strftime('%d %B %Y  %H_%M_%S') + ".zip"
        pss = enc("<./inabahs/9891/.>")
        lvl = 0
        lis2 = []
        for f in os.listdir(DIR + 'media' + PTH + '0'):
            if f.endswith(".json"):
                lis2.append(DIR + 'media' + PTH + '0' + PTH + f)
        pyminizip.compress_multiple(lis2,  [],chem, pss, lvl)

        Clock.schedule_once(self.backup, 3600)

    def boot(self, asyncio):

        if not os.path.isdir(NDR + 'Desktop' + PTH + 'P R I N T A B L E'):
            os.mkdir(NDR + 'Desktop' + PTH + 'P R I N T A B L E')

        try:
            fN = open(DIR + 'media' + PTH + '0' + PTH + 'ACR.json', 'r')
        except:
            return
        if not os.path.isfile(DIR + 'media' + PTH + '0' + PTH + 'TDATA.json'):
            # os.makedirs('./ANGELS')  ############################THIS WILL BE CHANED TO D:\IMPORTANT DATA\/home/kali/media'+PTH+'.0'+PTH+'ANGELS.json
            d = {}
            file = open(DIR + 'media' + PTH + '0' + PTH + 'TDATA.json', 'w')
            json.dump(d, file)
            file.close()
        if not os.path.isfile(DIR + 'media' + PTH + '0' + PTH + 'TABLE.json'):
            # os.makedirs('./ANGELS')  ############################THIS WILL BE CHANED TO D:\IMPORTANT DATA\/home/kali/media'+PTH+'.0'+PTH+'ANGELS.json
            d = {}
            file = open(DIR + 'media' + PTH + '0' + PTH + 'TABLE.json', 'w')
            json.dump(d, file)
            file.close()
        if not os.path.isfile(DIR + 'media' + PTH + '0' + PTH + 'DISABLED.json'):
            # os.makedirs('./ANGELS')  ############################THIS WILL BE CHANED TO D:\IMPORTANT DATA\/home/kali/media'+PTH+'.0'+PTH+'ANGELS.json
            d = {}
            file = open(DIR + 'media' + PTH + '0' + PTH + 'DISABLED.json', 'w')
            json.dump(d, file)
            file.close()

        if not os.path.isfile(DIR + 'media' + PTH + '0' + PTH + 'FINANCE.json'):
            # os.makedirs('./ANGELS')############################THIS WILL BE CHANED TO D:\IMPORTANT DATA\/home/kali/media'+PTH+'.0'+PTH+'ANGELS.json
            # time.strftime('%d %h %Y'): {"T": "0.0"}
            fina = {}
            # F[time.strftime('%d %h %Y')] = {"T": "0.0"}
            fina["TT"] = "0.0"
            if not fina.get(time.strftime('%Y'), 0):
                fina[time.strftime('%Y')] = {}
            if not fina[time.strftime('%Y')].get(time.strftime('%B'), 0):
                fina[time.strftime('%Y')][time.strftime('%B')] = {}
            if not fina[time.strftime('%Y')][time.strftime('%B')].get(time.strftime('%d'), 0):
                fina[time.strftime('%Y')][time.strftime('%B')][time.strftime('%d')] = {}
                # fina[time.strftime('%Y')][time.strftime('%B')][time.strftime('%d')]["T"]="0"
            if not fina[time.strftime('%Y')][time.strftime('%B')][time.strftime('%d')].get("TSP", 0):
                fina[time.strftime('%Y')][time.strftime('%B')][time.strftime('%d')]['TSP'] = {}
            if not fina[time.strftime('%Y')][time.strftime('%B')][time.strftime('%d')]['TSP'].get("T", 0):
                fina[time.strftime('%Y')][time.strftime('%B')][time.strftime('%d')]['TSP']['T'] = '0'
            if not fina[time.strftime('%Y')][time.strftime('%B')][time.strftime('%d')].get("TGN", 0):
                fina[time.strftime('%Y')][time.strftime('%B')][time.strftime('%d')]['TGN'] = {}
            if not fina[time.strftime('%Y')][time.strftime('%B')][time.strftime('%d')]['TGN'].get("T", 0):
                fina[time.strftime('%Y')][time.strftime('%B')][time.strftime('%d')]['TGN']['T'] = '0'
            fN = open(DIR + 'media' + PTH + '0' + PTH + 'FINANCE.json', 'w')
            json.dump(fina, fN)
            fN.close()
        else:
            try:
                fN = open(DIR + 'media' + PTH + '0' + PTH + 'FINANCE.json', 'r')
                fina = json.load(fN)
                fN.close()
                if not fina.get("TT", 0):
                    fina["TT"] = "0.0"
                if not fina.get(time.strftime('%Y'), 0):
                    fina[time.strftime('%Y')] = {}
                if not fina[time.strftime('%Y')].get(time.strftime('%B'), 0):
                    fina[time.strftime('%Y')][time.strftime('%B')] = {}
                if not fina[time.strftime('%Y')][time.strftime('%B')].get(time.strftime('%d'), 0):
                    fina[time.strftime('%Y')][time.strftime('%B')][time.strftime('%d')] = {}
                    # fina[time.strftime('%Y')][time.strftime('%B')][time.strftime('%d')]["T"]="0"
                if not fina[time.strftime('%Y')][time.strftime('%B')][time.strftime('%d')].get("TSP", 0):
                    fina[time.strftime('%Y')][time.strftime('%B')][time.strftime('%d')]['TSP'] = {}
                if not fina[time.strftime('%Y')][time.strftime('%B')][time.strftime('%d')]['TSP'].get("T", 0):
                    fina[time.strftime('%Y')][time.strftime('%B')][time.strftime('%d')]['TSP']['T'] = '0'
                if not fina[time.strftime('%Y')][time.strftime('%B')][time.strftime('%d')].get("TGN", 0):
                    fina[time.strftime('%Y')][time.strftime('%B')][time.strftime('%d')]['TGN'] = {}
                if not fina[time.strftime('%Y')][time.strftime('%B')][time.strftime('%d')]['TGN'].get("T", 0):
                    fina[time.strftime('%Y')][time.strftime('%B')][time.strftime('%d')]['TGN']['T'] = '0'
                if not fina[time.strftime('%Y')][time.strftime('%B')][time.strftime('%d')]['TGN'].get("BANK", 0):
                    fina[time.strftime('%Y')][time.strftime('%B')][time.strftime('%d')]['TGN']['BANK'] = '0'

                fN = open(DIR + 'media' + PTH + '0' + PTH + 'FINANCE.json', 'w')
                json.dump(fina, fN)
                fN.close()
            except:
                pass

        if not os.path.isfile(DIR + 'media' + PTH + '0' + PTH + 'ACR.json'):
            # os.makedirs('./ANGELS')  ############################THIS WILL BE CHANED TO D:\IMPORTANT DATA\/home/kali/media'+PTH+'.0'+PTH+'ANGELS.json
            d = {}
            d[enc('admin')] = ""
            d[enc('secretary')] = ""
            d[enc('finance')] = ""
            file = open(DIR + 'media' + PTH + '0' + PTH + 'ACR.json', 'w')
            json.dump(d, file)
            file.close()

        if not os.path.isfile(DIR + 'media' + PTH + '0' + PTH + 'DEPANS'):
            a = []
            zz = open(DIR + 'media' + PTH + '0' + PTH + 'DEPANS', 'wb')
            pickle.dump(a, zz)
            zz.close()
        if not os.path.isfile(DIR + 'media' + PTH + '0' + PTH + 'NUMBER'):
            a = 0
            zz = open(DIR + 'media' + PTH + '0' + PTH + 'NUMBER', 'wb')
            pickle.dump(a, zz)
            zz.close()
        if not os.path.isfile(DIR + 'media' + PTH + '0' + PTH + 'ctcomment'):
            list = ['Good']
            ll = open(DIR + 'media' + PTH + '0' + PTH + 'ctcomment', 'wb')
            pickle.dump(list, ll)
            ll.close()
        if not os.path.isfile(DIR + 'media' + PTH + '0' + PTH + 'hdcomment'):
            list = ['Good']
            ll = open(DIR + 'media' + PTH + '0' + PTH + 'hdcomment', 'wb')
            pickle.dump(list, ll)
            ll.close()
        if not os.path.isfile(DIR + 'media' + PTH + '0' + PTH + 'debat'):
            list = ['Good']
            ll = open(DIR + 'media' + PTH + '0' + PTH + 'debat', 'wb')
            pickle.dump(list, ll)
            ll.close()
        if not os.path.isfile(DIR + 'media' + PTH + '0' + PTH + 'conduct'):
            list = ['Good']
            ll = open(DIR + 'media' + PTH + '0' + PTH + 'conduct', 'wb')
            pickle.dump(list, ll)
            ll.close()
        if not os.path.isfile(DIR + 'media' + PTH + '0' + PTH + 'REMARKS'):
            list = ['Good']
            ll = open(DIR + 'media' + PTH + '0' + PTH + 'REMARKS', 'wb')
            pickle.dump(list, ll)
            ll.close()
        if not os.path.isfile(DIR + 'media' + PTH + '0' + PTH + 'CURRENT'):
            LN = 0
            zz = open(DIR + 'media' + PTH + '0' + PTH + 'CURRENT', 'wb')
            pickle.dump(LN, zz)
            zz.close()

        try:
            dette = open(DIR + 'media' + PTH + '0' + PTH + 'dette', 'r')
            dtt = dette.read()
            dette.close()
        except:
            dtt = "1"
        if dtt.strip() == "1":
            if time.strftime('%d %B') in (
            "05 May", "06 May", "07 May", "08 May", "04 May", "09 May", "10 May", "11 May",
            "12 May", "13 May", "14 May", "15 May", "16 May", "17 May", "18 May", "19 May", "20 May",
            "21 May", "22 May", "23 May", "24 May", "25 May", "26 May", "27 May", "28 May", "29 May", "30 May"):
                # a= -50000
                for xxx in Clss():
                    dt = open(DIR + 'media' + PTH + '0' + PTH + ANGELS + PTH + '' + xxx + '.json', 'r')
                    fina = json.load(dt)
                    dt.close()

                    for name in fina.keys():
                        b = float(fina[name]["$"]['balance']) - float(fina[name].get("fee",0))
                        fina[name]["$"]['balance'] = str(b)
                    dt = open(DIR + 'media' + PTH + '0' + PTH + ANGELS + PTH + '' + xxx + '.json', 'w')
                    json.dump(fina, dt)
                    dt.close()
                zz = open(DIR + 'media' + PTH + '0' + PTH + 'dette', 'w')
                zz.write("0")
                zz.close()
            if time.strftime('%d %B') in (
            "05 August", "06 August", "07 August", "08 August", "04 August", "09 August", "10 August", "11 August",
            "12 August", "13 August", "14 August", "15 August", "16 August", "17 August", "18 August", "19 August",
            "20 August",
            "21 August", "22 August", "23 August", "24 August", "25 August", "26 August", "27 August", "28 August",
            "29 August", "30 August"):
                # a = -50000
                for xxx in Clss():
                    dt = open(DIR + 'media' + PTH + '0' + PTH + ANGELS + PTH + '' + xxx + '.json', 'r')
                    fina = json.load(dt)
                    dt.close()

                    for name in fina.keys():
                        b = float(fina[name]["$"]['balance']) - float(fina[name]["fee"])
                        fina[name]["$"]['balance'] = str(b)
                    dt = open(DIR + 'media' + PTH + '0' + PTH + ANGELS + PTH + '' + xxx + '.json', 'w')
                    json.dump(fina, dt)
                    dt.close()
                zz = open(DIR + 'media' + PTH + '0' + PTH + 'dette', 'w')
                zz.write("0")
                zz.close()

            if time.strftime('%d %B') in (
            "05 November", "06 November", "07 November", "08 November", "04 November", "09 November", "10 November",
            "11 November",
            "12 November", "13 November", "14 November", "15 November", "16 November", "17 November", "18 November",
            "19 November", "20 November",
            "21 November", "22 November", "23 November", "24 November", "25 November", "26 November", "27 November",
            "28 November", "29 November", "30 November"):
                # a = -50000
                for xxx in Clss():
                    dt = open(DIR + 'media' + PTH + '0' + PTH + ANGELS + PTH + '' + xxx + '.json', 'r')
                    fina = json.load(dt)
                    dt.close()

                    for name in fina.keys():
                        b = float(fina[name]["$"]['balance']) - float(fina[name].get("fee",0))
                        fina[name]["$"]['balance'] = str(b)
                    dt = open(DIR + 'media' + PTH + '0' + PTH + ANGELS + PTH + '' + xxx + '.json', 'w')
                    json.dump(fina, dt)
                    dt.close()
                zz = open(DIR + 'media' + PTH + '0' + PTH + 'dette', 'w')
                zz.write("0")
                zz.close()
        if time.strftime('%B') == 'June' or time.strftime('%B') == 'September' or time.strftime('%B') == 'December':
            zz = open(DIR + 'media' + PTH + '0' + PTH + 'dette', 'w')
            zz.write("1")
            zz.close()

        try:
            dette = open(DIR + 'media' + PTH + '0' + PTH + 'tdette', 'r')
            dtt = dette.read()
            dette.close()
        except:
            dtt = "1"
        if dtt.strip() == "1":
            if time.strftime('%d') in ('25', '26', '27', '28', '29', '30', '31'):
                dt = open(DIR + 'media' + PTH + '0' + PTH + 'TDATA.json', 'r')
                fina = json.load(dt)
                dt.close()
                for tech in fina.keys():
                    ba = float(fina[tech]['balance']) + float(fina[tech]['SALARY'])
                    fina[tech]['balance'] = str(ba)
                dt = open(DIR + 'media' + PTH + '0' + PTH + 'TDATA.json', 'w')
                json.dump(fina, dt)
                dt.close()
                zz = open(DIR + 'media' + PTH + '0' + PTH + 'tdette', 'w')
                zz.write("0")
                zz.close()
        if time.strftime('%d') in ('01', '02', '03', '04', '05', '06', '07', '08', '09', '10'):
            zz = open(DIR + 'media' + PTH + '0' + PTH + 'tdette', 'w')
            zz.write("1")
            zz.close()
        if not os.path.isfile(DIR + 'media' + PTH + '0' + PTH + 'SCHOOL.bin'):
            Clock.schedule_once(self.new_sch,2)
        print("DISC ",DIR)
    def new_sch(self,x):
        self.add_widget(self.idd)
        self.opp=0
        self.idd.background_color = (0, 0, 0, 0)
        Clock.schedule_interval(self.opac,0.02)
        self.bckbut = Button(background_normal="",background_color=(1, 1, 1, 1), size_hint=(.85, .75), pos_hint={'center_x': .5, 'center_y': .5})
        self.add_widget(self.bckbut)

        self.gnot = GridLayout(cols=1,padding=10,spacing=10,size_hint=(.8, .75), pos_hint={'center_x': .5, 'center_y': .5})

        self.gnot.add_widget(Label(text="     No school regestered yet . the informations to fill bellow will be used on printed  "
                                        "hard copies like RECEIPT ,\n REPPORT cards and other documents.    The details are :"
                                        "School name, Postal code,Tel,Email, Catchword and Logo.\n"
                                        "You can fill them in your desired order. ",size_hint=(1., .26),italic=True,markup=True,valign="center",color=(.5,0,1.,.6)))

        in_gnot=GridLayout(cols=2,spacing=15)
        in1 = GridLayout(cols=1,spacing=15)

        self.sch_name=TextInput(hint_text="School name",allow_copy=True)
        self.post_cd = TextInput(hint_text="Postal code", allow_copy=True)
        self.contacts = TextInput(hint_text="Contacts", allow_copy=True)
        self.sch_email = TextInput(hint_text="Email", allow_copy=True)
        self.catchw = TextInput(hint_text="Catchword", allow_copy=True)
        self.logo = Button(text="Choose logo file",on_release=self.log_ch)
        self.subm = Button(text="SUBMIT", size_hint=(1., .1),background_color=(.5,0,1.,.6),on_release=self.s_schl)
        self.v_log=AsyncImage(size_hint=(None,None),size=(250,250),allow_stretch=True)

        v_l=[self.sch_name,self.post_cd,self.contacts,self.sch_email,self.catchw,self.logo]   #,
        for i in v_l :
            in1.add_widget(i)
        in_gnot.add_widget(in1)
        in_gnot.add_widget(self.v_log)
        self.gnot.add_widget(in_gnot)
        self.gnot.add_widget(self.subm)

        self.add_widget(self.gnot)

    def s_schl(self,x):
        if self.sch_name.text=="":
            return
        ##############################################################################
        s={'1':self.sch_name.text.upper(),'2':self.post_cd.text.upper(),
           '3':self.contacts.text,'4':self.sch_email.text.lower(),'5':self.catchw.text.title()}
        p=open(DIR + 'media' + PTH + '0' + PTH + 'SCHOOL.bin', 'wb')
        pickle.dump(s,p)
        p.close()
        #######################################################
        if os.path.isfile(self.logo.text):
            x=open(self.logo.text,"rb")
            xy=x.read()
            y=open(DIR + 'media' + PTH + '0' + PTH + 'L.png', 'wb')
            y.write(xy)
            y.close()
            x.close()
        print(s)

    def log_ch(self,x):
        global popup1
        pg=GridLayout(cols=1,size_hint=(.3,.86))
        ch=FileChooserListView()
        ch.dirselect = False
        ch.bind(selection=self.on_selected)
        pg.add_widget(ch)

        popup1 = Popup(title='Choose the logo file', size_hint=(.5,.8), content=pg, disabled=False)
        popup1.open()

    def on_selected(self,ob,val):
        self.logo.text = val[0]
        self.v_log.source=val[0]
        popup1.dismiss()

    def CCar(self, x):
        try:
            fN = open(DIR + 'media' + PTH + '0' + PTH + 'FINANCE.json', 'r')
        except:
            return
        if not os.path.isdir(DIR + 'media' + PTH + '0' + PTH + 'HTORY'):
            return
        wordlist = []
        for fi in os.listdir(DIR + 'media' + PTH + '0' + PTH + 'HTORY'):
            if fi.startswith(time.strftime('%d %B %Y').replace(" ", "-")):
                fileZ = open(DIR + 'media' + PTH + '0' + PTH + 'HTORY' + PTH + '' + fi, 'r')
                LB = fileZ.read()
                wordlist.append(LB)
        for xz in wordlist:
            self.terminal = Button(text=xz,
                                   background_normal="", background_color=(1, 1, 1, .05))
            self.car.add_widget(self.terminal)

    def search_error(self, o):
        self.Errors = []
        for error in os.listdir(DIR + 'media' + PTH + '0' + PTH + ANGELS):
            try:
                good = open(DIR + 'media' + PTH + '0' + PTH + ANGELS + PTH + error, 'r')
                test = json.load(good)
                kys = test.keys()
                good.close()
            except:
                self.Errors.append(error)

        for error in os.listdir(DIR + 'media' + PTH + '0'):
            if error.endswith(".json"):
                try:
                    good = open(DIR + 'media' + PTH + '0' + PTH + error, 'r')
                    test = json.load(good)
                    kys = test.keys()
                    good.close()
                except:
                    self.Errors.append(error)

        Clock.schedule_once(self.Continue)

    def trig(self, x):
        self.bars += 1
        self.perc.text = "|" * self.bars
        if self.bars > 100:
            self.perc.color = (0, 0, 0, 1)
        if self.bars > 500:
            Clock.unschedule(self.trig)
            Clock.schedule_once(self.search_error)
            # threading.Thread(target=self.search_error).start()

    def restore(self, x):
        self.bars = 4
        self.ww = 0
        self.add_widget(self.idd)
        Clock.schedule_interval(self.white, .01)

        self.perc = Label(text="|", color=(0, 0, 0, 1), size_hint=(1., .08),
                          pos_hint={"center_x": .001, "center_y": .2})
        self.add_widget(self.perc)
        Clock.schedule_interval(self.trig, .001)

    def Continue(self, z):
        self.grest = GridLayout(cols=1, size_hint=(.5, .5), pos_hint={"center_x": .5, "center_y": .2})

        if len(self.Errors) == 1:
            if self.Errors[0] == 'ACR.json':
                self.grest.add_widget(Label(
                    text="There are errors in the file storing passwords, as if somebody was trying something...",
                    font_size=25))
            else:
                self.grest.add_widget(Label(
                    text="Found error in " + self.Errors[0][:self.Errors[0].index(".json")] + " datas...",
                    font_size=23, italic=True))
        if len(self.Errors) > 1:
            self.grest.add_widget(Label(text="Found errors in files..."))

        if self.Errors == []:
            self.grest.add_widget(Label(text="No problem found in datas"))
            return

        self.add_widget(self.grest)

        Clock.schedule_once(self.mvgrest, 4)

        self.gsolution = GridLayout(cols=1, spacing=1, padding=0, size_hint=(.45, .7),
                                    pos_hint={'center_x': .67, 'center_y': .56})
        self.bkgr = Button(size_hint=(.5, .73), pos_hint={'center_x': .67, 'center_y': .52}, background_normal='wp.png')

        #
        tt = 'Here is a solution:\nIf you click on one of the bellow dates or time ;the corrupted \ndatas will be restored to that time' \
             ' when it was working well.\nBut that may cause the loss of those datas saved from that \nchosen ' \
             'time up to this time. if you are sure,if you are admin ;\nyou can proceed!'
        ss = 'If you click on one of the bellow dates or time ;\nthe corrupted datas will be restored to that time\n' \
             ' when it was working well.But that may cause \nthe loss of those datas saved from that chosen ' \
             'time\n up to this time. if you are sure,if you are admin ;\nyou can proceed !'
        if self.Errors == []:
            self.gsolution.add_widget(Label(text=ss, markup=True, italic=True, ))
        if len(self.Errors) > 0:
            self.gsolution.add_widget(Label(text=tt, markup=True, italic=True, ))

        self.svrest = ScrollView(size_hint=(.45, .68), pos_hint={'center_x': .2, 'center_y': .5}, do_scroll_x=False,
                                 do_scroll_y=True, scroll_timeout=55, scroll_distance=20,
                                 scroll_type=['bars', 'content'], bar_width=10, bar_color=(1, 1, 0, 1), bar_margin=0)
        self.autobind("self.svrest")

        dates = os.listdir(NDR + ".ftp" + PTH + "ANGELS")
        if dates==[]:
            return
        dates.sort()
        G = GridLayout(cols=1, size_hint=(1., None), size=(1, 26 * len(dates) + 50), row_default_height=26,
                       row_force_default=True)

        for date in reversed(dates):
            try:
                G.add_widget(Button(text=date[:date.index(".zip")].replace("_",":"), background_color=(0, 0, 0, 1), on_release=self.reset))
            except:
                pass
        self.svrest.add_widget(G)
        self.gsolution.add_widget(self.svrest)
        # self.add_widget(self.grest)

    def mvgrest(self, c):
        self.movement = .2
        Clock.schedule_interval(self.moving, 0)

    def moving(self, d):
        if self.movement >= .65:
            Clock.unschedule(self.moving)
            Clock.schedule_once(self.goleft, 2)

            if self.Errors != []:
                self.grest.add_widget(Label(
                    text="That might be caused by :\n- An overloaded router\n- Unstable connection\n- Edited datas or corrupted datas\n- Slow operating system "))
            # if self.Errors == []:
            #     self.grest.add_widget(Label(text="No problem found in datas"))
        else:
            self.movement += .01
            self.grest.pos_hint = {"center_x": .5, "center_y": self.movement}

    def goleft(self, o):
        self.LEFT = .5
        Clock.schedule_interval(self.leftmove, .015)

    def leftmove(self, y):
        if self.LEFT <= .21:
            self.remove_widget(self.perc)
            Clock.unschedule(self.leftmove)
            self.add_widget(self.bkgr)
            self.add_widget(self.gsolution)
            Clock.schedule_once(self.disap, 2)
            self.behind = Button(size_hint=(.35, .48), background_normal="wp.png",
                                 background_color=(.8, 0, 1., self.ww),
                                 pos_hint={"center_x": self.LEFT, "center_y": self.movement})
            self.remove_widget(self.grest)
            self.add_widget(self.behind)
            self.add_widget(self.grest)

        else:
            self.LEFT -= .01
            self.grest.pos_hint = {"center_x": self.LEFT, "center_y": self.movement}

    def disap(self, d):
        self.xww = 1
        Clock.schedule_interval(self.black, .015)

    def reset(self, r):
        if self.Errors == []:
            return
        self.ziped = r.text.replace(":","_") + ".zip"
        self.pwd = TextInput(multiline=False, allow_copy=True, size_hint=(.3, .07),
                             pos_hint={"center_x": .5, "center_y": .5})
        self.pwd.bind(text=self.RESTORED)
        self.ww = 0
        Clock.schedule_interval(self.white, .02)
        self.add_widget(self.pwd)
        self.remove_widget(self.grest)
        self.remove_widget(self.gsolution)
        self.remove_widget(self.bkgr)
        self.remove_widget(self.behind)

        try:
            fileZ = open(DIR + 'media' + PTH + '0' + PTH + 'ACR.json', 'r')
        except:
            return
        fN = open(DIR + 'media' + PTH + '0' + PTH + 'ACR.json', 'r')
        fina = json.load(fN)
        fN.close()
        self.admin = dec(fina["xajfk"])
        if not os.path.isdir(DIR + "ftp"):
            os.mkdir(DIR + "ftp")
        if self.Errors == []:
            threading.Thread(
                target=self.copy_thread).start()  # s'il n'y a pas d'erreur , et si la copie est dans 2 heure ; peut etre c'est un fraude !
            # garde la copie du soit disant erreur

    def RESTORED(self, SP, T):

        if len(T) == len(self.admin):
            if T != self.admin:
                self.idd.background_color = (1, 0, 0, 1)
                self.remove_widget(self.pwd)
                self.ww = 1
                Clock.schedule_interval(self.black, .015)
                self.rOK("no !")
            else:
                for x in self.Errors:
                    if x.startswith("P") or x.startswith("N"):
                        pyminizip.uncompress(NDR + ".ftp" + PTH + "ANGELS" + PTH + self.ziped,
                                             enc('<./inabahs/9891/.>'), DIR + "ftp", 0)
                        os.remove(DIR + 'media' + PTH + '0' + PTH + ANGELS+ PTH + x)
                        shutil.copy(DIR + "ftp" + PTH + x, DIR + 'media' + PTH + '0' + PTH + ANGELS + PTH + x)
                    else:
                        pyminizip.uncompress(NDR + ".ftp" + PTH + self.ziped, enc('<./inabahs/9891/.>'), DIR + "ftp", 0)
                        os.remove(DIR + 'media' + PTH + '0' + PTH + x)
                        shutil.copy(DIR + "ftp" + PTH + x, DIR + 'media' + PTH + '0' + PTH + x)
                try:
                    for js in os.listdir(DIR + "ftp"):
                        os.remove(DIR + "ftp" + PTH + js)
                except:
                    pass
                self.remove_widget(self.pwd)
                self.ww = 1
                Clock.schedule_interval(self.black, .015)
                Clock.schedule_once(self.iddkiller, 5)
                # self.remove_widget(self.idd)
                self.rOK("ok")

    def iddkiller(self, id):
        try:
            self.remove_widget(self.idd)
        except:
            pass

    def Totalct(self, even):
        threading.Thread(target=self.Num_tc).start()

    def Num_tc(self, even=None):

        try:
            fN = open(DIR + 'media' + PTH + '0' + PTH + 'FINANCE.json', 'r')
        except:
            return
        stnum = 0
        dt = open(DIR + 'media' + PTH + '0' + PTH  + 'TDATA.json', 'r')
        fina = json.load(dt)
        dt.close()

        for name in fina.keys():
            stnum += 1
        self.tch.text = "Teachers' data :\n\n      " + str(stnum) + " Teachers"

    def psalary(self, x):
        try:
            fN = open(DIR + 'media' + PTH + '0' + PTH + 'FINANCE.json', 'r')
        except:
            return
        total_dtt = 0
        FF = open(DIR + 'media' + PTH + '0' + PTH + 'TDATA.json', 'r')
        DF = json.load(FF)
        FF.close()
        for x in DF.keys():
            total_dtt += float(DF[x]['balance'])
        self.d_sal.text = 'Pending salary :\n\n          ' + str(total_dtt) + ' ugx'

    def num_st(self, even):
        threading.Thread(target=self.totalst).start()

    def totalst(self, even=None):
        list = Clss()
        if list == None or list == []:
            return
        try:
            fN = open(DIR + 'media' + PTH + '0' + PTH + 'FINANCE.json', 'r')
        except:
            return
        stnum = 0
        for xxx in Clss():
            dt = open(DIR + 'media' + PTH + '0' + PTH + ANGELS + PTH + '' + xxx + '.json', 'r')
            fina = json.load(dt)
            dt.close()

            for name in fina.keys():
                stnum += 1
        self.d_tot.text = 'Students data :\n\n      ' + str(stnum) + " pupils"

    def balanCe(self, even):
        threading.Thread(target=self.BBBB).start()

    def BBBB(self, even=None):
        list = Clss()
        if list == None or list == []:
            return
        try:
            fN = open(DIR + 'media' + PTH + '0' + PTH + 'FINANCE.json', 'r')
        except:
            return
        balance = 0
        for xxx in Clss():
            dt = open(DIR + 'media' + PTH + '0' + PTH + ANGELS + PTH + '' + xxx + '.json', 'r')
            fina = json.load(dt)
            dt.close()

            for name in fina.keys():
                if fina[name]["$"]['balance'][0] == '-':
                    b = float(fina[name]["$"]['balance'])
                    balance += b
        self.d_stbl.text = 'Total balance :\n\n          ' + str(balance) + " ugx"
        Clock.schedule_interval(self.Term, 15)

    def Term(self, x):
        self.car.load_next()

    def pending_(self, x):
        try:
            fN = open(DIR + 'media' + PTH + '0' + PTH + 'FINANCE.json', 'r')
        except:
            return
        if not lv in ('fin', 'adm'):
            return
        try:
            self.remove_widget(self.ps_sv)
        except:
            pass
        try:
            self.remove_widget(self.idd)
        except:
            pass
        try:
            self.remove_widget(self.goback)
        except:
            pass
        self.add_widget(self.idd)
        self.ww = 0
        Clock.schedule_interval(self.white, 0.01)

        self.ps_sv = ScrollView(size_hint=(.35, .8), pos_hint={'center_x': .2, 'center_y': .5}, do_scroll_x=False,
                                do_scroll_y=True, scroll_timeout=55, scroll_distance=20,
                                scroll_type=['bars', 'content'], bar_width=10, bar_color=(1, 1, 0, 1), bar_margin=0)
        self.autobind('self.ps_sv')

        self.ps_gsch = GridLayout(cols=1, spacing=12, size_hint_x=1., size_hint_y=10,
                                  pos_hint={'center_x': .44, 'center_y': .5}, row_default_height=230,
                                  row_force_default=True)

        FF = open(DIR + 'media' + PTH + '0' + PTH + 'TDATA.json', 'r')
        DF = json.load(FF)
        FF.close()
        for x in DF.keys():
            if float(DF[x]['balance']) >= 100:
                g = GridLayout(cols=1)
                asy = AsyncImage(source=ASY + x + '.png')
                b = Button(text=x + " (" + DF[x]['balance'] + ' ugx' + ")", color=(0, 0, 0, 1), background_normal='',
                           background_color=(1, 1, 1, 1), size_hint=(.2, .09), on_release=self.Pay)
                # b.bind(on_release=self.Pay(x))
                g.add_widget(asy)
                g.add_widget(b)
                self.ps_gsch.add_widget(g)
        self.ps_sv.add_widget(self.ps_gsch)
        self.add_widget(self.ps_sv)

        self.goback = Button(text='Back', color=(1, 0, 0, 1), size_hint=(.2, .1), on_release=self.home)
        self.goback.bind(on_release=self.Viewcleaner)
        self.idd.bind(on_release=self.Viewcleaner)
        self.add_widget(self.goback)

    def Pay(self, x):
        try:
            self.remove_widget(self.gG)
        except:
            pass
        FF = open(DIR + 'media' + PTH + '0' + PTH + 'TDATA.json', 'r')
        DF = json.load(FF)
        FF.close()
        self.saldett = DF[x.text[:x.text.index("(") - 1]]["balance"]
        self.teachname = x.text[:x.text.index("(") - 1]
        # print("teach",self.teachname)

        # print(x.text[:x.text.index("(")-1],len(x.text[:x.text.index("(")-1]))
        self.gG = GridLayout(cols=2, size_hint=(.5, 1.), pos_hint={'center_x': .65, 'center_y': .5},
                             row_default_height=80,
                             row_force_default=True)
        self.gG.add_widget(Label(text="", font_size=35))
        self.gG.add_widget(Label(text=DF[x.text[:x.text.index("(") - 1]]["balance"] + ' ugx', font_size=60))
        self.gG.add_widget(Label(text="               -", font_size=35))
        # g.add_widget(Label(text="", font_size=35))

        self.samount = TextInput(font_size=35, allow_copy=True, background_color=(1, 1, 1, .2),
                                 foreground_color=(1, 1, 1, .6), size_hint_x=.1)
        self.samount.bind(text=self.shoR)
        self.gG.add_widget(self.samount)
        self.gG.add_widget(Label(text="", font_size=35))
        self.gG.add_widget(Label(text="______________________", font_size=35))
        self.gG.add_widget(Label(text="", font_size=35))
        self.result = Label(font_size=35)
        self.gG.add_widget(self.result)

        self.gG.add_widget(Label(text="", font_size=35))
        self.gG.add_widget(Label(text="", font_size=35))
        self.gG.add_widget(Label(text="", font_size=35))

        self.gG.add_widget(Label(text="Password for receiver to apply modifications ", color=(1, 0, 0, 1)))
        self.gG.add_widget(Label(text="", font_size=35))
        self.tpw = TextInput(font_size=50, allow_copy=True,multiline=False, password=True, background_color=(1, 1, 1, .2),
                             foreground_color=(1, 1, 1, .6), size_hint_x=.1)
        self.tpw.bind(text=self.validating)
        self.gG.add_widget(self.tpw)

        self.add_widget(self.gG)

    def shoR(self, sp, tx):
        if self.samount.text == "":
            self.result.text = self.saldett
            return

        try:
            int(tx)
        except:
            return

        self.result.text = str(float(self.saldett) - float(tx))

    def validating(self, sp, tx):
        if self.samount.text == "":
            return
        if len(tx) >= 4:
            FF = open(DIR + 'media' + PTH + '0' + PTH + 'TDATA.json', 'r')
            DF = json.load(FF)
            FF.close()
            if tx == DF[self.teachname]['PASSCODE']:
                DF[self.teachname]['balance'] = self.result.text
                FF = open(DIR + 'media' + PTH + '0' + PTH + 'TDATA.json', 'w')
                json.dump(DF, FF)
                FF.close()
                self.okay = Button(text="OK", font_size=50, color=(0, 1, 0, 1), background_color=(1, 1, 1, 1),
                                   background_normal="", size_hint=(.2, .2), pos_hint={'center_x': .5, 'center_y': .5})

                fN = open(DIR + 'media' + PTH + '0' + PTH + 'FINANCE.json', 'r')
                fina = json.load(fN)
                fN.close()
                TT = float(fina["TT"])
                B = float(self.samount.text)
                rest = TT - B
                fina["TT"] = str(rest)
                depans = time.strftime(
                    '%d %h %Y') + ' ' + time.strftime(
                    '%H:%M') + " Salary :" + self.teachname + ". : " + self.samount.text + " ugx. the main account Balance is : " + str(
                    rest)
                if fina[time.strftime('%Y')][time.strftime('%B')][time.strftime('%d')]['TSP'].get('SALARY',0):
                    SALAIR=float(fina[time.strftime('%Y')][time.strftime('%B')][time.strftime('%d')]['TSP']['SALARY'])+float(self.samount.text)
                    fina[time.strftime('%Y')][time.strftime('%B')][time.strftime('%d')]['TSP']['SALARY'] = str(SALAIR)  # depans
                    tsp=float(fina[time.strftime('%Y')][time.strftime('%B')][time.strftime('%d')]['TSP']['T'])+float(self.samount.text)
                    fina[time.strftime('%Y')][time.strftime('%B')][time.strftime('%d')]['TSP']['T']=str(tsp)
                else:
                    tsp = float(fina[time.strftime('%Y')][time.strftime('%B')][time.strftime('%d')]['TSP']['T']) + float(self.samount.text)
                    fina[time.strftime('%Y')][time.strftime('%B')][time.strftime('%d')]['TSP']['T'] = str(tsp)
                    fina[time.strftime('%Y')][time.strftime('%B')][time.strftime('%d')]['TSP']['SALARY'] =self.samount.text #depans

                ZfN = open(DIR + 'media' + PTH + '0' + PTH + 'FINANCE.json', 'w')
                json.dump(fina, ZfN)
                ZfN.close()

                if not os.path.isdir(DIR + 'media' + PTH + '0' + PTH + 'HTORY'):
                    os.makedirs(DIR + 'media' + PTH + '0' + PTH + 'HTORY')

                ###############            EXPENDUSER("~/")

                his = open(
                    DIR + 'media' + PTH + '0' + PTH + 'HTORY' + PTH + '' + time.strftime('%d %B %Y %H %M %S').replace(
                        " ", "-") + '.txt', 'w')
                his.write(depans)
                his.close()
                self.add_widget(self.okay)
                Clock.schedule_once(self.remover, 3)
                Clock.schedule_once(self.psalary)
                Clock.schedule_once(self.CCar)

    def remover(self, x):
        self.remove_widget(self.okay)
        self.remove_widget(self.gG)
        Clock.schedule_once(self.pending_)

    def ttbl(self, x):
        try:
            fN = open(DIR + 'media' + PTH + '0' + PTH + 'FINANCE.json', 'r')
        except:
            return
        if not lv in ('fin', 'adm'):
            return
        # print(x)
        self.add_widget(self.idd)
        self.ww = 0
        Clock.schedule_interval(self.white, 0.01)

        self.ps_sv = ScrollView(size_hint=(.25, .8), pos_hint={'center_x': .2, 'center_y': .5}, do_scroll_x=False,
                                do_scroll_y=True, scroll_timeout=55, scroll_distance=20,
                                scroll_type=['bars', 'content'], bar_width=10, bar_color=(1, 1, 0, 1), bar_margin=0)
        self.autobind('self.ps_sv')

        self.ps_gsch = GridLayout(cols=1, spacing=12, size_hint_x=1., size_hint_y=4,
                                  pos_hint={'center_x': .44, 'center_y': .5}, row_default_height=40,
                                  row_force_default=True)

        for cla in Clss():
            TTT = 0
            FF = open(DIR + 'media' + PTH + '0' + PTH + ANGELS + PTH + '' + cla + '.json', 'r')
            DF = json.load(FF)
            FF.close()
            g = GridLayout(cols=1, row_default_height=40,
                           row_force_default=True)

            b = Button(text=cla, color=(0, 0, 0, 1), background_normal='',
                       background_color=(1, 1, 1, 1), size_hint=(.2, .09), on_release=self.TBP)

            for x in DF.keys():
                if DF[x]['$']['balance'][0] == "-":
                    TTT += float(DF[x]['$']['balance'])
            b.text = cla + " / " + str(TTT) + " ugx"
            b.texture_size = self.size
            b.halign = "left"
            if str(TTT)[0] == "-":
                g.add_widget(b)
                self.ps_gsch.add_widget(g)
            else:
                pass

        self.ps_sv.add_widget(self.ps_gsch)
        self.add_widget(self.ps_sv)

        self.goback = Button(text='Back', color=(1, 0, 0, 1), size_hint=(.2, .1), on_release=self.home)
        self.goback.bind(on_release=self.Viewcleaner)
        self.idd.bind(on_release=self.Viewcleaner)
        self.add_widget(self.goback)

    def TBP(self, x):
        self.level = x.text[:3]
        try:
            self.remove_widget(self.imprimer)
        except:
            pass
        try:
            self.remove_widget(self.pp)
        except:
            pass
        try:
            self.remove_widget(self.ps_sv2)
        except:
            pass

        self.pp = Label(text=x.text[:3], size_hint=(.2, .08), pos_hint={'center_x': .5, 'center_y': .95})
        self.add_widget(self.pp)
        self.ps_sv2 = ScrollView(size_hint=(.25, .8), pos_hint={'center_x': .5, 'center_y': .5}, do_scroll_x=False,
                                 do_scroll_y=True, scroll_timeout=55, scroll_distance=20,
                                 scroll_type=['bars', 'content'], bar_width=10, bar_color=(1, 1, 0, 1), bar_margin=0)
        self.autobind('self.ps_sv2')

        self.ps_gsch2 = GridLayout(cols=1, spacing=4, size_hint_x=1., size_hint_y=2,
                                   pos_hint={'center_x': .44, 'center_y': .5}, row_default_height=24,
                                   row_force_default=True)

        FF = open(DIR + 'media' + PTH + '0' + PTH + ANGELS + PTH + '' + x.text[:3] + '.json', 'r')
        DF = json.load(FF)
        FF.close()
        for name in DF.keys():
            TTT = 0
            g = GridLayout(cols=1, row_default_height=24,
                           row_force_default=True)

            b = Button(text=name, color=(0, 0, 0, 1), background_normal='',
                       background_color=(1, 1, 1, 1), size_hint=(.2, .09), on_release=self.onenote)
            g.add_widget(b)
            if DF[name]['$']['balance'][0] == "-":
                TTT += float(DF[name]['$']['balance'])
                b.text = name + " (" + str(TTT) + " ugx)"
                b.texture_size = self.size
                b.halign = "left"
                self.ps_gsch2.add_widget(g)
            else:
                pass

        self.ps_sv2.add_widget(self.ps_gsch2)
        self.add_widget(self.ps_sv2)
        self.imprimer = Button(text="print", size_hint=(.2, .1), pos_hint={'center_x': .5, 'center_y': .04},
                               on_release=self.IMPRIM)
        self.add_widget(self.imprimer)

    def IMPRIM(self,x):
        # self.remove_widget(self.ps_sv)
        # self.remove_widget(self.ps_sv2)
        # # self.remove_widget(self.ps_gsch)
        # # self.remove_widget(self.ps_gsch2)
        # self.ps_sv3 = ScrollView(size_hint=(None, None), size=(840, 1200), pos_hint={'center_x': .5, 'center_y': .5},
        #                          do_scroll_x=False,
        #                          do_scroll_y=True, scroll_timeout=55, scroll_distance=20,
        #                          scroll_type=['bars', 'content'], bar_width=10, bar_color=(1, 1, 0, 1), bar_margin=0)
        # self.autobind('self.ps_sv3')
        #
        # self.ps_gsch3 = GridLayout(cols=3, spacing=3, size=(840, 1200),
        #                            pos_hint={'center_x': .44, 'center_y': .5}, row_default_height=24,
        #                            row_force_default=True)
        #
        # FF = open(DIR + 'media' + PTH + '0' + PTH + ANGELS + PTH + '' + self.level + '.json', 'r')
        # DF = json.load(FF)
        # FF.close()
        # self.psins = GridLayout(cols=1, row_default_height=40, row_force_default=True, col_default_width=400,
        #                         col_force_default=True)
        # self.psins.add_widget(
        #     TextInput(text="Pupil with debt in        " + self.level, foreground_color=(1, 1, 1, 1), font_size=30,
        #               background_color=(0, 0, 0, 1)))
        #
        # self.ps_gsch3.add_widget(self.psins)
        # self.ps_gsch3.add_widget(Label(text=''))
        # self.ps_gsch3.add_widget(Label(text=""))
        # self.ps_gsch3.add_widget(Label(text=''))
        # self.ps_gsch3.add_widget(Label(text=""))
        # self.ps_gsch3.add_widget(Label(text=''))
        #
        # for name in DF.keys():
        #     TTT = 0
        #
        #     b = Button(text=name, color=(0, 0, 0, 1), background_normal='',
        #                background_color=(1, 1, 1, 1), size_hint=(.2, .09), on_release=self.onenote)
        #     if DF[name]['$']['balance'][0] == "-":
        #         TTT += float(DF[name]['$']['balance'])
        #         b.text = name + " (" + str(TTT) + " ugx)"
        #         b.texture_size = self.size
        #         b.halign = "left"
        #         self.ps_gsch3.add_widget(b)
        #     else:
        #         pass
        #
        # self.ps_sv3.add_widget(self.ps_gsch3)
        # self.add_widget(self.ps_sv3)
        # self.ps_sv3.scroll_y = 1

        pickl = open(DIR + 'media' + PTH + '0' + PTH + 'SCHOOL.bin', 'rb')
        ids = pickle.load(pickl)
        pickl.close()
        #'+ids['1']+'

        ls = []
        sz = 0
        self.gac = GridLayout(cols=2, padding=1,spacing=1,size_hint=(None, None), row_default_height=29, row_force_default=True)
        # self.gac.add_widget(Label(text=""))
        FF = open(DIR + 'media' + PTH + '0' + PTH + ANGELS + PTH + '' + self.level + '.json', 'r')
        DF = json.load(FF)
        FF.close()
        for pp in DF.keys():
            if DF[pp]["$"]['balance'][0] == "-":
                ls.append([float(DF[pp]["$"]['balance']), pp])
        ls.sort()
        print(ls)
        # ls.reverse()
        # print(ls)
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

        self.exG = GridLayout(cols=1, size_hint=(None, None))
        les_point = GridLayout(cols=3, size_hint=(None, None), size=(900, 170))
        im = AsyncImage(source=ASY + 'L.png', size_hint=(None, None), size=(150, 150), allow_stretch=True)
        les_point.add_widget(im)
        grid_in = GridLayout(cols=1, size_hint=(None, None), size=(360, 170), row_default_height=25,
                             row_force_default=True)
        grid_in.add_widget(
            Label(text='  '+ids['1']+'               ', color=(0, 0, 1, 1), font_size=18))
        grid_in.add_widget(
            Label(text='       '+ids['2']+'               ', font_size=13, color=(0, 0, 0, 1)))
        grid_in.add_widget(
            Label(text='   '+ids['3']+'               ', font_size=13,
                  color=(0, 1, 0, 1)))
        grid_in.add_widget(
            Label(text='       '+ids['4']+'               ', font_size=13, color=(0, 0, 0, 1)))
        grid_in.add_widget(
            Label(text='     '+ids['5']+'               ', font_size=15, color=(1, 0, 0, 1)))
        # grid_in.add_widget(Label(text=' ' * 15 +self.v_class.text+' ' * 100 + ' ' * 20, underline=True, color=(1, 0, 0, 1)))
        les_point.add_widget(grid_in)
        ph = Label(text=self.level + " DEBTS : ", font_size=70, underline=True, italic=True,
                   color=(0, 0, 0, .3))
        les_point.add_widget(ph)
        self.exG.add_widget(les_point)
        # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

        self.gac.add_widget(Label(text="",size_hint=(None, None), size=(200, 29)))   # for space
        self.gac.add_widget(Label(text="", size_hint=(None, None), size=(60, 29)))   #

        sz += 1
        for one in ls:
            self.gac.add_widget(TextInput(text=one[1],size_hint=(None, None), size=(200, 29),background_color=(0,0,0,0),font_size=14))
            self.gac.add_widget(TextInput(text=str(one[0]),size_hint=(None, None), size=(60, 29), background_color=(0, 0, 0, 0), font_size=14))
            sz += 1

        self.gac.size = (840, 25 * sz + 50)
        self.exG.size = (840, 25 * sz + 250)
        # self.exG.width=, self.exG.height + 260
        self.exG.add_widget(self.gac)
        self.add_widget(self.exG)
        # Clock.schedule_once(self.dtSSGGex, 3)

        Clock.schedule_once(self.imp2, 4)

    def imp2(self, x):
        self.exG.export_to_png(
            NDR + 'Desktop' + PTH + 'P R I N T A B L E' + PTH + '' + self.level + " DEBT s2" + time.strftime(
                '%B %Y') + ".png")
        self.print_all_i(NDR + 'Desktop' + PTH + 'P R I N T A B L E' + PTH + '' + self.level + " DEBT s2" + time.strftime(
                '%B %Y') + ".png")
        self.exG.clear_widgets()
        self.exG.remove_widget(self.gac)
        self.remove_widget(self.exG)
        self.rOK('Done')

    def onenote(self, x):
        self.thename = x.text[:x.text.index("(") - 1]
        try:
            self.remove_widget(self.notg)
        except:
            pass
        # print(x.text[:x.text.index("/")-1].upper())
        self.notg = GridLayout(cols=1, size_hint=(.25, .4), pos_hint={'center_x': .8, 'center_y': .77})
        self.notg.add_widget(
            Label(text="Message to " + x.text[:x.text.index("(") - 1].upper() + "'s parents.", size_hint=(1., .15)))
        self.onnt = TextInput(allow_copy=True)
        self.notg.add_widget(self.onnt)
        self.SN = Button(text='SEND', size_hint=(1., .15), on_release=self.ssent)
        self.notg.add_widget(self.SN)
        self.add_widget(self.notg)

    def ssent(self, o):
        if self.onnt.text == "":
            return

        TDAT = open(DIR + 'media' + PTH + '0' + PTH + ANGELS + PTH + '' + self.level + ".json", 'r')
        DT = json.load(TDAT)
        TDAT.close()
        l = [DT[self.thename]["Contact Phone"]]
        sms = {}
        sms['message'] = self.onnt.text
        sms['tel'] = l

        dt = open(DIR + 'media' + PTH + '0' + PTH + 'SMS.json', 'w')
        json.dump(sms, dt)
        dt.close()
        self.remove_widget(self.notg)

    def notice(self, text):
        try:
            fN = open(DIR + 'media' + PTH + '0' + PTH + 'FINANCE.json', 'r')
        except:
            return
        self.add_widget(self.idd)
        self.idd.background_color = (0, 0, 0, 1)
        self.bckbut = Button(background_color=(1, 1, 1, .4), size_hint=(.55, .65),
                             pos_hint={'center_x': .5, 'center_y': .5})
        self.add_widget(self.bckbut)
        self.gnot = GridLayout(cols=2, size_hint=(.5, .6), pos_hint={'center_x': .5, 'center_y': .5})
        one = GridLayout(cols=1)
        one.add_widget(Label(text="Type your sms here", size_hint=(1., .2)))
        self.txtx = TextInput(allow_copy=True)
        one.add_widget(self.txtx)
        one.add_widget(Label(text="*\nOnce you clic 'SEND' button ,\nthis sms will be sent to your \n"
                                  "phone via wifi router or \nhotspot,then your phone \nwill send it"
                                  " automatically \nusing your sms plan.", italic=True, color=(.3, .3, .3, 1)))
        self.gnot.add_widget(one)
        self.two = GridLayout(cols=1, spacing=self.bckbut.height / 5, row_default_height=40,
                              row_force_default=True)
        self.two.add_widget(Label(text="Message to ...", size_hint_y=.02))
        lst = Clss()
        lst.append("To all parents")

        self.stap = Spinner(text="To all parents", values=tuple(lst), size_hint_y=.02, )
        self.stap.bind(text=self.choscl)
        self.two.add_widget(self.stap)
        self.stos = Spinner(text="One pupil", size_hint_y=.02)
        self.gnot.add_widget(self.two)
        self.send = Button(text='S e n d', on_release=self.transfer)
        self.two.add_widget(self.send)

        self.add_widget(self.gnot)
        self.parents_tel = []

    def choscl(self, sp, tex):
        self.parents_tel = []
        if tex[0] == "P":
            try:
                self.two.remove_widget(self.stos)
                self.two.remove_widget(self.send)

            except:
                pass
            self.two.add_widget(self.stos)
            self.two.add_widget(self.send)
            TDAT = open(DIR + 'media' + PTH + '0' + PTH + ANGELS + PTH + '' + tex + ".json", 'r')
            DT = json.load(TDAT)
            TDAT.close()
            ls = []
            for x in DT.keys():
                ls.append(x)
                self.parents_tel.append('+256' + DT[x]["Contact Phone"][-9:])
            self.stos.values = tuple(ls)
        if tex == "To all parents":
            for y in Clss():
                TDAT = open(DIR + 'media' + PTH + '0' + PTH + ANGELS + PTH + '' + y + ".json", 'r')
                DT = json.load(TDAT)
                TDAT.close()
                for x in DT.keys():
                    self.parents_tel.append('+256' + DT[x]["Contact Phone"][-9:])
                    # read all parent numbers
        print(self.parents_tel)

    def transfer(self, z):
        if self.stap.text == "To all parents":
            self.parents_tel = []
            for y in Clss():
                TDAT = open(DIR + 'media' + PTH + '0' + PTH + ANGELS + PTH + '' + y + ".json", 'r')
                DT = json.load(TDAT)
                TDAT.close()
                for x in DT.keys():
                    self.parents_tel.append('+256' + DT[x]["Contact Phone"][-9:])
        sms = {}
        sms['message'] = self.txtx.text
        sms['tel'] = self.parents_tel

        dt = open(DIR + 'media' + PTH + '0' + PTH + 'SMS.json', 'w')
        json.dump(sms, dt)
        dt.close()
        self.parents_tel = []

    def student_data(self, c):

        self.ww = 0
        self.add_widget(self.idd)
        Clock.schedule_interval(self.SECwhite, .01)
        self.goback = Button(text='Back', color=(1, 0, 0, 1), size_hint=(.2, .1), on_release=self.home)
        self.goback.bind(on_release=self.Viewcleaner)
        self.idd.bind(on_release=self.Viewcleaner)
        self.add_widget(self.goback)

        self.gt = GridLayout(cols=5, size_hint=(1., .2), pos_hint={'center_x': .5, 'center_y': .9})
        list = ["VIEW CLASS", 'SORT BY STATUS', 'SORT BY DEBT','PAY OR CHARGE\nMULTIPLE', 'SUBJECT\nAND MARKS']
        for i in list:
            self.go = Button(text=i, color=(1, 1, 0, 1), background_color=(1, 0, 1, .4), background_normal="bb.png",
                             on_release=self.call_on)
            self.gt.add_widget(self.go)
        self.add_widget(self.gt)

    def call_on(self, t):
        Clock.schedule_once(self.Viewcleaner, -1)
        l = 'self.' + t.text.replace(" ", "_").replace("\n","_")
        exec("Clock.schedule_once(" + l + ",0)")


    def PAY_OR_CHARGE_MULTIPLE(self,en):
        self.bbh=Button(background_color=(0,0,1,.87),size_hint=(.84, .45), pos_hint={'center_x': .5, 'center_y': .5})
        self.add_widget(self.bbh)
        self.GPC=GridLayout(cols=4,size_hint=(.8, .4), pos_hint={'center_x': .5, 'center_y': .5})
        L=['CLASS','DIS.STATUS','AMOUNT(+/-)',"  ...  "]
        for i in L :
            self.GPC.add_widget(Label(text=i,color=(1,1,0,.8)))
        for i in range(4) :
            self.GPC.add_widget(Label(text=" ",color=(1,1,0,.8)))

        self.la_class = Spinner(text="ALL CLASSES", values=tuple(Clss()))
        self.GPC.add_widget(self.la_class)

        self.disabil = Spinner(text="", values=('CM', 'ORP', 'PWD', 'CHH', 'OTH'))
        self.GPC.add_widget(self.disabil)

        self.txam = TextInput(allow_copy=True)
        self.GPC.add_widget(self.txam)

        self.SUBM = Button(text='APPLY',on_release=self.ADD_CH)
        self.GPC.add_widget(self.SUBM)

        for i in range(7) :
            self.GPC.add_widget(Label(text=" ",color=(1,1,0,.8)))
        canc= Button(text='cancel',background_color=(1, 1, 0, .8),
                             background_normal="", on_release=self.call_canc)
        self.GPC.add_widget(canc)
        self.add_widget(self.GPC)
    def ADD_CH(self,x):
        if self.txam == "":
            return
        try:
            float(self.txam.text)
        except:
            return

        if self.la_class.text=="ALL CLASSES" :
            if self.disabil.text=="" :
                for word in Clss():
                    TDAT = open(DIR + 'media' + PTH + '0' + PTH + ANGELS + PTH + '' + word + ".json", 'r')
                    DT = json.load(TDAT)
                    TDAT.close()
                    for x in DT.keys():
                        nr= float(DT[x]["$"]["balance"])+float(self.txam.text)
                        DT[x]["$"]["balance"]=str(nr)
                    file = open(DIR + 'media' + PTH + '0' + PTH + ANGELS + PTH + '' + word + '.json', 'w')
                    json.dump(DT, file)
                    file.close()
            else:
                for word in Clss():
                    TDAT = open(DIR + 'media' + PTH + '0' + PTH + ANGELS + PTH + '' + word + ".json", 'r')
                    DT = json.load(TDAT)
                    TDAT.close()
                    for x in DT.keys():
                        if self.disabil.text in DT[x]["Vurnerability status"] :
                            nr= float(DT[x]["$"]["balance"])+float(self.txam.text)
                            DT[x]["$"]["balance"]=str(nr)
                    file = open(DIR + 'media' + PTH + '0' + PTH + ANGELS + PTH + '' + word + '.json', 'w')
                    json.dump(DT, file)
                    file.close()

        else:
            if self.disabil.text=="" :
                TDAT = open(DIR + 'media' + PTH + '0' + PTH + ANGELS + PTH + '' + self.la_class.text + ".json", 'r')
                DT = json.load(TDAT)
                TDAT.close()
                for x in DT.keys():
                    nr= float(DT[x]["$"]["balance"])+float(self.txam.text)
                    DT[x]["$"]["balance"]=str(nr)
                file = open(DIR + 'media' + PTH + '0' + PTH + ANGELS + PTH + '' + self.la_class.text + '.json', 'w')
                json.dump(DT, file)
                file.close()

            else:
                TDAT = open(DIR + 'media' + PTH + '0' + PTH + ANGELS + PTH + '' + self.la_class.text + ".json", 'r')
                DT = json.load(TDAT)
                TDAT.close()
                for x in DT.keys():
                    if self.disabil.text in DT[x]["Vurnerability status"]:
                        nr = float(DT[x]["$"]["balance"]) + float(self.txam.text)
                        DT[x]["$"]["balance"] = str(nr)
                file = open(DIR + 'media' + PTH + '0' + PTH + ANGELS + PTH + '' + self.la_class.text + '.json', 'w')
                json.dump(DT, file)
                file.close()


        if self.txam.text[0] == "-" :
            self.rOK("no problem")
        else:
            self.rOK("thanks")

        self.cancelb('self.GPC',"self.bbh")
    def call_canc(self,x):
        self.cancelb('self.GPC', "self.bbh")

    def cancelb(self,g,b=None):
        exec("self.remove_widget("+g+")")
        if b != None :
            exec("self.remove_widget(" + b + ")")




    def VIEW_CLASS(self, x):

        try:
            self.remove_widget(self.PrI)
        except:
            pass
        #_____________________________________________
        self.PrI = Spinner(text='print ', values=('with pictures      ','Select details', 'without pictures'), color=(1, .6, 0, 1),
                           size_hint=(.2, .1), pos_hint={'center_x': .7, 'center_y': .04})
        self.PrI.bind(text=self.pRi)
        self.add_widget(self.PrI)
        self.SLTD = Button(text='CHOOSE DETAILS ',background_color=(0,0,0,1), color=(1, .6, 0, 1),size_hint=(.2, .1), pos_hint={'center_x': .4, 'center_y': .04},on_release=self.CALLselectD)

        self.add_widget(self.SLTD)

        cla = Clss()
        cla.append("ALL CLASSES")
        self.v_class = Spinner(text=cla[0], values=tuple(cla), size_hint=(.2, .06),
                               pos_hint={'center_x': .1, 'center_y': .72})
        self.v_class.bind(text=self.detail)
        self.add_widget(self.v_class)

        self.sdetail = TextInput(text="Enter Name : ",allow_copy=True, size_hint=(.2, .06), pos_hint={'center_x': .1, 'center_y': .78})
        self.sdetail.bind(text=self.DEtail)
        self.sdetail.bind(on_touch_down=self.xDetail)
        self.add_widget(self.sdetail)

        self.sssv = ScrollView(size_hint=(.8, .7), pos_hint={'center_x': .6, 'center_y': .45}, do_scroll_y=True,
                               do_scroll_x=True, scroll_type=['bars', 'content'], bar_width=10, bar_color=(1, 1, 0, 1),
                               bar_margin=0)
        self.autobind('self.sssv')
        self.SG = GridLayout(cols=4, spacing=12, size_hint=(None, None), pos_hint={'center_x': .44, 'center_y': .5},
                             row_default_height=180,
                             row_force_default=True)  # for scrolling
        # self.les_point=GridLayout(cols=3,size_hint=(None,None),size=(630,150))
        # im = AsyncImage(source=DIR+'media'+PTH+'.0'+PTH+'L.png', size_hint=(None, None),size=(120, 140), allow_stretch=True)
        # self.les_point.add_widget(im)
        # grid_in=GridLayout(cols=1,size_hint=(None,None),size=(360,150),row_default_height=35,row_force_default=True)
        # grid_in.add_widget(Label(text='  ANGELS CARE SCHOOL –ITAMBABINIGA               ', color=(0, 0, 1, 1), font_size=20))
        # grid_in.add_widget(Label(text='       P.O.BOX 67, KYEGEGWA-UGANDA               ', color=(0, 0, 0, 1)))
        # grid_in.add_widget(Label(text='   Tel: +256783154155/+256777564555/+256782274208               ', color=(0, 1, 0, 1)))
        # grid_in.add_widget(Label(text='       Email:angelscaresch2008@gmail.com               ', color=(0, 0, 0, 1)))
        # grid_in.add_widget(Label(text='     “We aim for excellence”               ', color=(1, 0, 0, 1), font_size=20))
        # grid_in.add_widget(Label(text=' ' * 15 + '-' * 100 + ' ' * 20, underline=True, color=(1, 0, 0, 1)))
        # self.les_point.add_widget(grid_in)
        # ph = AsyncImage(source=DIR+'media'+PTH+'.0'+PTH+'L.png', size_hint=(None, None),size=(120, 140), allow_stretch=True)
        # self.les_point.add_widget(ph)
        #
        # self.SG.add_widget(self.les_point)
        # self.SG.add_widget(Label(text=""))
        # self.SG.add_widget(Label(text=""))
        # self.SG.add_widget(Label(text=""))

        # threading.Thread(target=self.detail).start()
        Clock.schedule_once(self.detail)
    def CALLselectD(self,x):
        self.detlst = ["Full Name"]
        self.listst = "Status"
        Clock.schedule_once(self.selectD)

    def DEtail(self, r, s):
        word = self.v_class.text

        try:
            self.sssv.clear_widgets()
        except:
            pass
        try:
            self.remove_widget(self.sssv)
        except:
            pass
        try:
            self.SG.clear_widgets()
        except:
            pass

        ##
        # self.les_point = GridLayout(cols=3, size_hint=(None, None), size=(630, 150))
        # im = AsyncImage(source=DIR+'media'+PTH+'.0'+PTH+'L.png', size_hint=(None, None),
        #                 size=(120, 140), allow_stretch=True)
        # self.les_point.add_widget(im)
        # grid_in = GridLayout(cols=1, size_hint=(None, None), size=(360, 150), row_default_height=35,
        #                      row_force_default=True)
        # grid_in.add_widget(
        #     Label(text='  ANGELS CARE SCHOOL –ITAMBABINIGA               ', color=(0, 0, 1, 1), font_size=20))
        # grid_in.add_widget(Label(text='       P.O.BOX 67, KYEGEGWA-UGANDA               ', color=(0, 0, 0, 1)))
        # grid_in.add_widget(
        #     Label(text='   Tel: +256783154155/+256777564555/+256782274208               ', color=(0, 1, 0, 1)))
        # grid_in.add_widget(
        #     Label(text='       Email:angelscaresch2008@gmail.com               ', color=(0, 0, 0, 1)))
        # grid_in.add_widget(
        #     Label(text='     “We aim for excellence”               ', color=(1, 0, 0, 1), font_size=20))
        # grid_in.add_widget(Label(text=' ' * 15 + '-' * 100 + ' ' * 20, underline=True, color=(1, 0, 0, 1)))
        # self.les_point.add_widget(grid_in)
        # ph = AsyncImage(source=DIR+'media'+PTH+'.0'+PTH+'L.png', size_hint=(None, None),
        #                 size=(120, 140), allow_stretch=True)
        # self.les_point.add_widget(ph)
        #
        # self.SG.add_widget(self.les_point)
        # self.SG.add_widget(Label(text="", size_hint=(None, None), size=(1, 1)))
        # self.SG.add_widget(Label(text="", size_hint=(None, None), size=(1, 1)))
        # self.SG.add_widget(Label(text="", size_hint=(None, None), size=(1, 1)))

        ##

        l = []
        if word == "ALL CLASSES":
            sz = 0
            for word in Clss():
                TDAT = open(DIR + 'media' + PTH + '0' + PTH + ANGELS + PTH + '' + word + ".json", 'r')
                DT = json.load(TDAT)
                TDAT.close()
                for x in DT.keys():
                    if s.lower() in x.lower():
                        lalis = []
                        del DT[x]["$"]
                        del DT[x]["photo"]
                        try:
                            del DT[x]["marks"]
                        except:
                            pass
                        ggg = GridLayout(cols=1, spacing=1)
                        ggg.add_widget(AsyncImage(source=ASY + x + ".png"))
                        for name in DT[x].keys():
                            lalis.append(name + " :\n " + DT[x][name])
                        ggg.add_widget(Spinner(text=word + "| " + x, values=tuple(lalis), size_hint=(1., .2)))

                        self.SG.add_widget(ggg)
                        sz += 0.25

        else:
            sz = 0
            TDAT = open(DIR + 'media' + PTH + '0' + PTH + ANGELS + PTH + '' + word + ".json", 'r')
            DT = json.load(TDAT)
            TDAT.close()
            for x in DT.keys():
                if s.lower() in x.lower():
                    lalis = []
                    del DT[x]["$"]
                    del DT[x]["photo"]
                    try:
                        del DT[x]["marks"]
                    except:
                        pass
                    ggg = GridLayout(cols=1, spacing=1)
                    ggg.add_widget(AsyncImage(source=ASY + x + ".png"))
                    for name in DT[x].keys():
                        lalis.append(name + " :\n " + DT[x][name])
                    ggg.add_widget(Spinner(text=x, values=tuple(lalis), size_hint=(1., .2)))
                    self.SG.add_widget(ggg)
                    sz += 0.25
        # sz += 255
        self.SG.size = (900, 180 * sz + 100)
        self.sssv.add_widget(self.SG)
        self.add_widget(self.sssv)
        self.sssv.scroll_y = 1

    def detail(self, spin=None, tt=None):
        word = self.v_class.text

        try:
            self.exG.remove_widget(self.SG)
        except:
            pass

        try:
            self.sssv.clear_widgets(self.exG)
        except:
            pass

        #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        try:
            self.sssv.clear_widgets()
        except:
            pass
        try:
            self.remove_widget(self.sssv)
        except:
            pass
        try:
            self.SG.clear_widgets()
        except:
            pass
        #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

        l = []
        if word == "ALL CLASSES":
            sz = 0
            Cls = Clss()
            for word in Cls:
                TDAT = open(DIR + 'media' + PTH + '0' + PTH + ANGELS + PTH + '' + word + ".json", 'r')
                DT = json.load(TDAT)
                TDAT.close()
                for x in DT.keys():
                    lalis = []
                    del DT[x]["$"]
                    del DT[x]["photo"]
                    try:
                        del DT[x]["marks"]
                    except:
                        pass
                    ggg = GridLayout(spacing=1, cols=1)
                    ggg.add_widget(AsyncImage(source=ASY + x + ".png"))
                    for name in DT[x].keys():
                        lalis.append(name + " :\n " + DT[x][name])
                    ggg.add_widget(Spinner(text=word + "| " + x, values=tuple(lalis),
                                           size_hint=(1., .2)))
                    self.SG.add_widget(ggg)
                    sz += 0.25

        else:
            sz = 0
            TDAT = open(DIR + 'media' + PTH + '0' + PTH + ANGELS + PTH + '' + word + ".json", 'r')
            DT = json.load(TDAT)
            TDAT.close()
            for x in DT.keys():
                lalis = []
                del DT[x]["$"]
                del DT[x]["photo"]
                try:
                    del DT[x]["marks"]
                except:
                    pass
                ggg = GridLayout(spacing=3, cols=1)
                ggg.add_widget(AsyncImage(source=ASY + x + ".png"))
                for name in DT[x].keys():
                    lalis.append(name + " :\n " + DT[x][name])
                ggg.add_widget(Spinner(text=x, values=tuple(lalis), size_hint=(1., .2)))
                self.SG.add_widget(ggg)
                sz += 0.25
        self.SG.size = (900, 180 * sz + 300)
        self.sssv.add_widget(self.SG)
        self.add_widget(self.sssv)
        self.sssv.scroll_y = 1
        print(self.SG.size, "c'etait  SG")

    def pRi(self, s, t):
        if t == 'with pictures      ':
            if self.v_class.text == 'ALL CLASSES':
                return

            pickl = open(DIR + 'media' + PTH + '0' + PTH + 'SCHOOL.bin', 'rb')
            ids = pickle.load(pickl)
            pickl.close()
            # '+ids['1']+'

            self.SG.cols=6
            self.sssv.remove_widget(self.SG)
            self.exG = GridLayout(cols=1, size_hint=(None, None), size=(self.SG.width, self.SG.height + 260),
                                  pos_hint=self.SG.pos_hint)
            les_point = GridLayout(cols=3, size_hint=(None, None), size=(900, 170))
            im = AsyncImage(source=ASY + 'L.png', size_hint=(None, None), size=(150, 150), allow_stretch=True)
            les_point.add_widget(im)
            grid_in = GridLayout(cols=1, size_hint=(None, None), size=(360, 170), row_default_height=25,
                                 row_force_default=True)
            grid_in.add_widget(
                Label(text='  '+ids['1']+'               ', color=(0, 0, 1, 1), font_size=15))
            grid_in.add_widget(
                Label(text='       '+ids['2']+'               ', font_size=10, color=(0, 0, 0, 1)))
            grid_in.add_widget(
                Label(text='   '+ids['3']+'               ', font_size=10,
                      color=(0, 1, 0, 1)))
            grid_in.add_widget(
                Label(text='       '+ids['4']+'               ', font_size=10, color=(0, 0, 0, 1)))
            grid_in.add_widget(
                Label(text='     '+ids['5']+'               ', font_size=12, color=(1, 0, 0, 1)))
            # grid_in.add_widget(Label(text=' ' * 15 +self.v_class.text+' ' * 100 + ' ' * 20, underline=True, color=(1, 0, 0, 1)))
            les_point.add_widget(grid_in)
            ph = Label(text=self.v_class.text,font_size=100,underline=True,italic=True,color=(0,0,0,.3))
            les_point.add_widget(ph)
            self.exG.add_widget(les_point)
            self.exG.add_widget(self.SG)
            self.sssv.add_widget(self.exG)
            Clock.schedule_once(self.Gex,4)

        if t == 'without pictures':
            if self.v_class.text == 'ALL CLASSES':
                return
            ls = []
            sz = 0
            self.gac = GridLayout(cols=4, size_hint=(None, None), row_default_height=28, row_force_default=True)
            # self.gac.add_widget(Label(text=""))

            pickl = open(DIR + 'media' + PTH + '0' + PTH + 'SCHOOL.bin', 'rb')
            ids = pickle.load(pickl)
            pickl.close()
            # '+ids['1']+'

            FF = open(DIR + 'media' + PTH + '0' + PTH + ANGELS + PTH + '' + self.v_class.text + '.json', 'r')
            DF = json.load(FF)
            FF.close()
            for pp in DF.keys():
                ls.append(pp)
            ls.sort()


            #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            self.exG = GridLayout(cols=1, size_hint=(None, None), size=(self.SG.width, self.SG.height + 260),
                                  pos_hint=self.SG.pos_hint)
            les_point = GridLayout(cols=3, size_hint=(None, None), size=(900, 170))
            im = AsyncImage(source=ASY + 'L.png', size_hint=(None, None), size=(150, 150), allow_stretch=True)
            les_point.add_widget(im)
            grid_in = GridLayout(cols=1, size_hint=(None, None), size=(360, 170), row_default_height=25,
                                 row_force_default=True)
            grid_in.add_widget(
                Label(text='  '+ids['1']+'               ', color=(0, 0, 1, 1), font_size=18))
            grid_in.add_widget(
                Label(text='       '+ids['2']+'               ', font_size=13, color=(0, 0, 0, 1)))
            grid_in.add_widget(
                Label(text='   '+ids['3']+'               ', font_size=13,
                      color=(0, 1, 0, 1)))
            grid_in.add_widget(
                Label(text='       '+ids['4']+'               ', font_size=13, color=(0, 0, 0, 1)))
            grid_in.add_widget(
                Label(text='     '+ids['5']+'               ', font_size=15, color=(1, 0, 0, 1)))
            # grid_in.add_widget(Label(text=' ' * 15 +self.v_class.text+' ' * 100 + ' ' * 20, underline=True, color=(1, 0, 0, 1)))
            les_point.add_widget(grid_in)
            ph = Label(text=self.v_class.text, font_size=100, underline=True, italic=True, color=(0, 0, 0, .3))
            les_point.add_widget(ph)
            self.exG.add_widget(les_point)
            #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
            self.gac.add_widget(Label(text=""))
            self.gac.add_widget(Label(text=""))
            self.gac.add_widget(Label(text=""))
            self.gac.add_widget(Label(text=""))
            self.gac.add_widget(Label(text=""))
            self.gac.add_widget(Label(text=""))
            self.gac.add_widget(Label(text=""))
            self.gac.add_widget(Label(text=""))
            sz += 2
            for one in ls:
                self.gac.add_widget(TextInput(text=one))
                sz += 0.25

            self.gac.size = (840, 24 * sz + 50)
            self.exG.add_widget(self.gac)
            self.add_widget(self.exG)
            Clock.schedule_once(self.sG, 3)
        if t == 'Select details' :
            self.SG.size=(100,100)
            self.detlst = ["Full Name"]
            self.listst = "Status"
            Clock.schedule_once(self.selectD)
        # self.SG.cols = 3

    def sG(self, x):
        self.exG.export_to_png(NDR + 'Desktop' + PTH + 'P R I N T A B L E' + PTH + '' + self.v_class.text + "A to Z.png")
        self.print_all_i(NDR + 'Desktop' + PTH + 'P R I N T A B L E' + PTH + '' + self.v_class.text + "A to Z.png")
        self.exG.clear_widgets()
        self.gac.clear_widgets()
        self.gac.remove_widget(self.exG)
        self.remove_widget(self.gac)
        self.rOK('Done')
    def Gex(self,ex):
        self.exG.export_to_png(
            NDR + 'Desktop' + PTH + 'P R I N T A B L E' + PTH + '' + "list  of " + self.v_class.text + " pupils.png")
        self.print_all_i(
            NDR + 'Desktop' + PTH + 'P R I N T A B L E' + PTH + '' + "list  of " + self.v_class.text + " pupils.png")
        self.rOK('Done')
        self.SG.cols=4
        Clock.schedule_once(self.detail)

    def xDetail(self, sp, t):
        self.sdetail.text = ''


    def selectD(self,event):
        self.SG.clear_widgets()
        self.sssv.remove_widget(self.SG)
        try:
            self.gsd.clear_widgets()
        except:
            pass
        try:
            self.sssv.remove_widget(self.gsd)
        except:
            pass

        #------------REMOVE BUTTONS
        try:
            self.remove_widget(self.prcol)
        except:
            pass
        try:
            self.remove_widget(self.delcol)
        except:
            pass
        try:
            self.remove_widget(self.adcol)
        except:
            pass
        try:
            self.remove_widget(self.status)
        except:
            pass
        #------------------------------------------------------------

        TDAT = open(DIR + 'media' + PTH + '0' + PTH + ANGELS + PTH + '' + self.v_class.text + ".json", 'r')
        DT = json.load(TDAT)
        TDAT.close()
        self.gsd=GridLayout(cols=len(self.detlst),spacing=0,padding=0,pos_hint={'center_x': .5, 'center_y': .5},size_hint=(None,None),size=(200*len(self.detlst),50*len(DT.keys())))

        cnt=0
        head=[]
        for name in DT.keys() :
            dol = DT[name]["$"]['balance']
            del DT[name]["$"]
            DT[name]["Debt"] = dol

        for x in DT.keys():
            if cnt == 1:
                break
            # del DT[x]["$"]
            try:
                del DT[x]["marks"]
            except:
                pass
            for ot in DT[x].keys():
                head.append(ot)
            cnt+=1
        del cnt
        del head[head.index('Full Name')]
        self.adcol=Spinner(text=self.detlst[-1],values=tuple(head),size_hint=(.2, .06),pos_hint={'center_x': .1, 'center_y': .65})
        self.adcol.bind(text=self.incre)
        self.add_widget(self.adcol)

        self.delcol = Spinner(text='Delete one', values=tuple(self.detlst), size_hint=(.2, .06),pos_hint={'center_x': .1, 'center_y': .55})
        self.delcol.bind(text=self.decre)
        self.add_widget(self.delcol)

        self.prcol = Button(text='Print', size_hint=(.2, .06), pos_hint={'center_x': .1, 'center_y': .35},on_release=self.colpr)
        self.add_widget(self.prcol)

        self.status = Spinner(text=self.listst, values=("Status", 'CM', 'ORP', 'PWD', 'CHH', 'OTH'),
                              size_hint=(.2, .06), pos_hint={'center_x': .1, 'center_y': .45})
        self.status.bind(text=self.CHST)
        self.add_widget(self.status)

        if self.status.text == "Status":
            cnt=0
            for go in self.detlst:
                if go == "Full Name":
                    g = GridLayout(cols=1, size_hint=(None, None),size=(250,30),pos_hint={'center_x': .5, 'center_y': .5}, row_default_height=30,
                               row_force_default=True)
                    g.add_widget(TextInput(text=go, readonly=True, background_color=(1, 1, 0, .8)))
                else:
                    g = GridLayout(cols=1, size_hint=(None, None), size=(150, 30),pos_hint={'center_x': .5, 'center_y': .5}, row_default_height=30,
                                   row_force_default=True)
                    g.add_widget(TextInput(text=go, readonly=True, background_color=(1, 1, 0, .8)))

                ll=list(DT.keys())
                ll.sort()
                for st in ll:
                    cnt += 1
                    if go == "Full Name":
                        g.add_widget(TextInput(text=str(cnt) + " .     " + DT[st][go], readonly=True))
                    else:
                        g.add_widget(TextInput(text=DT[st][go], readonly=True))

                self.gsd.add_widget(g)
        else:
            cnt=0
            for go in self.detlst:
                if go == "Full Name":
                    g = GridLayout(cols=1, size_hint=(None, None), size=(250, 30),pos_hint={'center_x': .5, 'center_y': .5}, row_default_height=30,
                                   row_force_default=True)
                    g.add_widget(TextInput(text=go, readonly=True, background_color=(1, 1, 0, .8)))
                else:
                    g = GridLayout(cols=1, size_hint=(None, None), size=(150, 30),
                                   pos_hint={'center_x': .5, 'center_y': .5}, row_default_height=30,
                                   row_force_default=True)
                    g.add_widget(TextInput(text=go, readonly=True, background_color=(1, 1, 0, .8)))

                ll = list(DT.keys())
                ll.sort()
                for st in ll :
                    if self.status.text in DT[st]["Vurnerability status"]:
                        cnt += 1
                        if go == "Full Name":
                            g.add_widget(TextInput(text=str(cnt) + " .     " + DT[st][go], readonly=True))
                        else:
                            g.add_widget(TextInput(text=DT[st][go], readonly=True))
                self.gsd.add_widget(g)

        self.sssv.add_widget(self.gsd)

        if not "Full Name" in self.detlst :
            rep=["Full Name"]+head
            head=rep
            del rep
            self.adcol.values=tuple(head)
    def CHST(self,sp,t):
        self.listst=t
        Clock.schedule_once(self.selectD)
    def decre(self,sp,tx):
        if len(self.detlst) == 1 :
            return
        del self.detlst[self.detlst.index(tx)]
        Clock.schedule_once(self.selectD)


    def incre(self,sp,tex):

        if tex =='Full Name' :
            self.detlst = ['Full Name'] + self.detlst

        if not tex in self.detlst :
            self.detlst.append(tex)
        else:
            if tex == 'Full Name':
                pass
            else:
                del self.detlst[self.detlst.index(tex)]
                self.detlst.append(tex)

        Clock.schedule_once(self.selectD)
    def colpr(self,e):
        self.gsd.export_to_png(NDR + 'Desktop' + PTH + 'P R I N T A B L E' + PTH + '' + self.v_class.text + "DETAILS.png")
        self.print_all_i(NDR + 'Desktop' + PTH + 'P R I N T A B L E' + PTH + '' + self.v_class.text + "DETAILS.png")
        self.rOK("printed")
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    def SORT_BY_STATUS(self, X):
        try:
            self.SSSv.clear_widgets(self.exG)
        except:
            pass

        try:
            self.remove_widget(self.SSSv)
        except:
            pass

        try:
            self.remove_widget(self.PrI)
        except:
            pass
        self.PrI = Spinner(text='print ', values=('with pictures      ', 'without pictures'), color=(1, .6, 0, 1),
                           size_hint=(.2, .1), pos_hint={'center_x': .7, 'center_y': .04})
        self.PrI.bind(text=self.sttpr)
        self.add_widget(self.PrI)

        lss = Clss()
        lss.append("ALL CLASSES")
        self.S_class = Spinner(text=lss[0], values=tuple(lss), size_hint=(.2, .06),
                               pos_hint={'center_x': .1, 'center_y': .72})
        self.S_class.bind(text=self.DETAIL)
        self.add_widget(self.S_class)

        self.SSdetail = Spinner(text="ORP", values=('CM', 'ORP', 'PWD', 'CHH', 'OTH'), size_hint=(.2, .06),
                                pos_hint={'center_x': .1, 'center_y': .78})
        self.SSdetail.bind(text=self.DDDEtail)
        self.SSdetail.bind(on_touch_down=self.xXDDDetail)
        self.add_widget(self.SSdetail)

        self.SSSv = ScrollView(size_hint=(.8, .7), pos_hint={'center_x': .6, 'center_y': .45}, do_scroll_y=True,
                               do_scroll_x=False, scroll_type=['bars', 'content'], bar_width=10, bar_color=(1, 1, 0, 1),
                               bar_margin=0)
        self.autobind('self.SSSv')
        self.SSGG = GridLayout(cols=3, spacing=12, size_hint=(None, None),
                               pos_hint={'center_x': .44, 'center_y': .5}, row_default_height=180,
                               row_force_default=True)  # for scrolling
        Clock.schedule_once(self.DETAIL)

    def DDDEtail(self, r, s):
        word = self.S_class.text

        try:
            self.SSSv.clear_widgets()
        except:
            pass
        try:
            self.remove_widget(self.SSSv)
        except:
            pass
        try:
            self.SSGG.clear_widgets()
        except:
            pass
        l = []
        if word == "ALL CLASSES":
            sz = 0
            Cls = Clss()
            for word in Cls:
                TDAT = open(DIR + 'media' + PTH + '0' + PTH + ANGELS + PTH + '' + word + ".json", 'r')
                DT = json.load(TDAT)
                TDAT.close()
                for x in DT.keys():
                    if self.SSdetail.text in DT[x]["Vurnerability status"]:
                        lalis = []
                        del DT[x]["$"]
                        del DT[x]["photo"]
                        try:
                            del DT[x]["marks"]
                        except:
                            pass
                        ggg = GridLayout(spacing=3, cols=1)
                        ggg.add_widget(AsyncImage(source=ASY + x + ".png"))
                        for name in DT[x].keys():
                            lalis.append(name + " :\n " + DT[x][name])
                        ggg.add_widget(Spinner(text=word + "| " + x + " : " + self.SSdetail.text, values=tuple(lalis),
                                               size_hint=(1., .2)))
                        self.SSGG.add_widget(ggg)
                        sz += 0.25

        else:
            sz = 0
            TDAT = open(DIR + 'media' + PTH + '0' + PTH + ANGELS + PTH + '' + word + ".json", 'r')
            DT = json.load(TDAT)
            TDAT.close()
            for x in DT.keys():
                if s in DT[x]["Vurnerability status"]:
                    lalis = []
                    del DT[x]["$"]
                    del DT[x]["photo"]
                    try:
                        del DT[x]["marks"]
                    except:
                        pass
                    ggg = GridLayout(spacing=3, cols=1)
                    ggg.add_widget(AsyncImage(source=ASY + x + ".png"))
                    for name in DT[x].keys():
                        lalis.append(name + " :\n " + DT[x][name])
                    ggg.add_widget(Spinner(text=x, values=tuple(lalis), size_hint=(1., .2)))
                    self.SSGG.add_widget(ggg)
                    sz += 0.25
        self.SSGG.size = (840, 180 * sz + 100)
        self.SSSv.add_widget(self.SSGG)
        self.add_widget(self.SSSv)
        self.SSSv.scroll_y = 1

    def DETAIL(self, spin, tt=None):

        word = self.S_class.text

        try:
            self.SSSv.clear_widgets()
        except:
            pass
        try:
            self.remove_widget(self.SSSv)
        except:
            pass
        try:
            self.SSGG.clear_widgets()
        except:
            pass
        l = []
        if word == "ALL CLASSES":
            sz = 0
            Cls = Clss()
            for word in Cls:
                TDAT = open(DIR + 'media' + PTH + '0' + PTH + ANGELS + PTH + '' + word + ".json", 'r')
                DT = json.load(TDAT)
                TDAT.close()
                for x in DT.keys():
                    if self.SSdetail.text in DT[x]["Vurnerability status"]:
                        lalis = []
                        del DT[x]["$"]
                        del DT[x]["photo"]
                        try:
                            del DT[x]["marks"]
                        except:
                            pass
                        ggg = GridLayout(spacing=3, cols=1)
                        ggg.add_widget(AsyncImage(source=ASY + x + ".png"))
                        for name in DT[x].keys():
                            lalis.append(name + " :\n " + DT[x][name])
                        ggg.add_widget(Spinner(text=word + "| " + x + " : " + self.SSdetail.text, values=tuple(lalis),
                                               size_hint=(1., .2)))
                        self.SSGG.add_widget(ggg)
                        sz += 0.25

        else:
            sz = 0
            TDAT = open(DIR + 'media' + PTH + '0' + PTH + ANGELS + PTH + '' + word + ".json", 'r')
            DT = json.load(TDAT)
            TDAT.close()
            for x in DT.keys():
                if self.SSdetail.text in DT[x]["Vurnerability status"]:
                    lalis = []
                    del DT[x]["$"]
                    del DT[x]["photo"]
                    try:
                        del DT[x]["marks"]
                    except:
                        pass
                    ggg = GridLayout(spacing=3, cols=1)
                    ggg.add_widget(AsyncImage(source=ASY + x + ".png"))
                    for name in DT[x].keys():
                        lalis.append(name + " :\n " + DT[x][name])
                    ggg.add_widget(Spinner(text=x, values=tuple(lalis), size_hint=(1., .2)))
                    self.SSGG.add_widget(ggg)
                    sz += 0.25
        self.SSGG.size = (840, 180 * sz + 100)
        self.SSSv.add_widget(self.SSGG)
        self.add_widget(self.SSSv)
        self.SSSv.scroll_y = 1

    def sttpr(self, s, t):
        if t == 'with pictures      ':
            if self.S_class.text == 'ALL CLASSES':
                return

            pickl = open(DIR + 'media' + PTH + '0' + PTH + 'SCHOOL.bin', 'rb')
            ids = pickle.load(pickl)
            pickl.close()
            # '+ids['1']+'

            self.SSGG.cols = 6
            self.SSSv.remove_widget(self.SSGG)
            self.exG = GridLayout(cols=1, size_hint=(None, None), size=(self.SSGG.width, self.SSGG.height + 260),
                                  pos_hint=self.SSGG.pos_hint)
            les_point = GridLayout(cols=3, size_hint=(None, None), size=(840, 170))
            im = AsyncImage(source=ASY + 'L.png', size_hint=(None, None), size=(150, 150), allow_stretch=True)
            les_point.add_widget(im)
            grid_in = GridLayout(cols=1, size_hint=(None, None), size=(360, 170), row_default_height=25,
                                 row_force_default=True)
            grid_in.add_widget(
                Label(text='  '+ids['1']+'               ', color=(0, 0, 1, 1), font_size=15))
            grid_in.add_widget(
                Label(text='       '+ids['2']+'               ', font_size=10, color=(0, 0, 0, 1)))
            grid_in.add_widget(
                Label(text='   '+ids['3']+'               ', font_size=10,
                      color=(0, 1, 0, 1)))
            grid_in.add_widget(
                Label(text='       '+ids['4']+'               ', font_size=10, color=(0, 0, 0, 1)))
            grid_in.add_widget(
                Label(text='     '+ids['5']+'               ', font_size=12, color=(1, 0, 0, 1)))
            # grid_in.add_widget(Label(text=' ' * 15 +self.v_class.text+' ' * 100 + ' ' * 20, underline=True, color=(1, 0, 0, 1)))
            les_point.add_widget(grid_in)
            ph = Label(text=self.S_class.text+" "+self.SSdetail.text, font_size=50, underline=True, italic=True, color=(0, 0, 0, .3))
            les_point.add_widget(ph)
            self.exG.add_widget(les_point)
            self.exG.add_widget(self.SSGG)
            self.SSSv.add_widget(self.exG)
            Clock.schedule_once(self.SSGGex, 4)

        if t == 'without pictures':
            if self.S_class.text == 'ALL CLASSES':
                return
            ls = []
            sz = 0

            pickl = open(DIR + 'media' + PTH + '0' + PTH + 'SCHOOL.bin', 'rb')
            ids = pickle.load(pickl)
            pickl.close()
            # '+ids['1']+'

            self.exG = GridLayout(cols=1, size_hint=(None, None), size=(self.SSGG.width, self.SSGG.height + 260),
                                  pos_hint=self.SSGG.pos_hint)
            les_point = GridLayout(cols=3, size_hint=(None, None), size=(840, 170))
            im = AsyncImage(source=ASY + 'L.png', size_hint=(None, None), size=(150, 150), allow_stretch=True)
            les_point.add_widget(im)
            grid_in = GridLayout(cols=1, size_hint=(None, None), size=(360, 170), row_default_height=25,
                                 row_force_default=True)
            grid_in.add_widget(
                Label(text='  '+ids['1']+'               ', color=(0, 0, 1, 1), font_size=15))
            grid_in.add_widget(
                Label(text='       '+ids['2']+'               ', font_size=10, color=(0, 0, 0, 1)))
            grid_in.add_widget(
                Label(text='   '+ids['3']+'               ', font_size=10,
                      color=(0, 1, 0, 1)))
            grid_in.add_widget(
                Label(text='       '+ids['4']+'               ', font_size=10, color=(0, 0, 0, 1)))
            grid_in.add_widget(
                Label(text='     '+ids['5']+'               ', font_size=12, color=(1, 0, 0, 1)))
            # grid_in.add_widget(Label(text=' ' * 15 +self.v_class.text+' ' * 100 + ' ' * 20, underline=True, color=(1, 0, 0, 1)))
            les_point.add_widget(grid_in)
            ph = Label(text=self.S_class.text + " " + self.SSdetail.text, font_size=50, underline=True, italic=True,
                       color=(0, 0, 0, .3))
            les_point.add_widget(ph)
            self.exG.add_widget(les_point)


            self.gac3 = GridLayout(cols=4, size_hint=(None, None), row_default_height=28, row_force_default=True)
            # self.gac.add_widget(Label(text=""))
            FF = open(DIR + 'media' + PTH + '0' + PTH + ANGELS + PTH + '' + self.S_class.text + '.json', 'r')
            DF = json.load(FF)
            FF.close()
            for pp in DF.keys():
                if DF[pp]["Vurnerability status"] == self.SSdetail.text:
                    ls.append(pp)
            ls.sort()
            self.gac3.add_widget(
                TextInput(text=self.S_class.text + " " + self.SSdetail.text + " " + "N", foreground_color=(1, 1, 1, 1),
                          background_color=(0, 0, 0, 1)))
            self.gac3.add_widget(Label(text=""))
            self.gac3.add_widget(Label(text=""))
            self.gac3.add_widget(Label(text=""))
            self.gac3.add_widget(Label(text=""))
            self.gac3.add_widget(Label(text=""))
            self.gac3.add_widget(Label(text=""))
            self.gac3.add_widget(Label(text=""))
            sz += 2
            for one in ls:
                self.gac3.add_widget(TextInput(text=one))
                sz += 0.25

            self.gac3.size = (840, 24 * sz + 50)
            self.exG.add_widget(self.gac3)
            self.add_widget(self.exG)
            Clock.schedule_once(self.Sg, 3)
        # self.SSGG.cols = 3

    def Sg(self, x):
        self.exG.export_to_png(
            NDR + 'Desktop' + PTH + 'P R I N T A B L E' + PTH + '' + self.S_class.text + " " + self.SSdetail.text + " " + "N.png")

        self.print_all_i(NDR + 'Desktop' + PTH + 'P R I N T A B L E' + PTH + '' + self.S_class.text + " " + self.SSdetail.text + " " + "N.png")

        self.exG.clear_widgets()
        self.remove_widget(self.exG)
        self.rOK('Done')
    def SSGGex(self,x):
        self.exG.export_to_png(
            NDR + 'Desktop' + PTH + 'P R I N T A B L E' + PTH + '' + self.S_class.text + " " + self.SSdetail.text + ".png")
        self.print_all_i(NDR + 'Desktop' + PTH + 'P R I N T A B L E' + PTH + '' + self.S_class.text + " " + self.SSdetail.text + ".png")

        self.SSGG.cols = 4
        Clock.schedule_once(self.SORT_BY_STATUS)
        self.rOK('Done')

    def xXDDDetail(self, sp, t):
        # self.SSdetail.text = ''
        pass

    def SORT_BY_DEBT(self, X):
        try:
            self.dtSSSv.clear_widgets(self.exG)
        except:
            pass

        try:
            self.remove_widget(self.dtSSSv)
        except:
            pass

        try:
            self.remove_widget(self.PrI)
        except:
            pass

        self.PrI = Spinner(text='print ', values=('with pictures      ', 'without pictures'), color=(1, .6, 0, 1),
                           size_hint=(.2, .1), pos_hint={'center_x': .7, 'center_y': .04})
        self.PrI.bind(text=self.dtpr)
        self.add_widget(self.PrI)

        lss = Clss()
        lss.append("ALL CLASSES")
        self.dtS_class = Spinner(text=lss[0], values=tuple(lss), size_hint=(.2, .06),
                                 pos_hint={'center_x': .1, 'center_y': .72})
        self.dtS_class.bind(text=self.detDETAIL)
        self.add_widget(self.dtS_class)

        self.dtSSdetail = TextInput(text="Enter Name : ", size_hint=(.2, .06),
                                    pos_hint={'center_x': .1, 'center_y': .78})
        self.dtSSdetail.bind(text=self.detDDDEtail)
        self.dtSSdetail.bind(on_touch_down=self.detxXDDDetail)
        self.add_widget(self.dtSSdetail)

        self.dtSSSv = ScrollView(size_hint=(.8, .7), pos_hint={'center_x': .6, 'center_y': .45}, do_scroll_y=True,
                                 do_scroll_x=False, scroll_type=['bars', 'content'], bar_width=10,
                                 bar_color=(1, 1, 0, 1), bar_margin=0)
        self.autobind('self.dtSSSv')
        self.dtSSGG = GridLayout(cols=4, spacing=32, size_hint=(None, None),
                                 pos_hint={'center_x': .44, 'center_y': .5}, row_default_height=180,
                                 row_force_default=True)  # for scrolling
        Clock.schedule_once(self.detDETAIL)

    def detDDDEtail(self, r, s):
        if s == "" :
            return
        word = self.dtS_class.text

        try:
            self.dtSSSv.clear_widgets()
        except:
            pass
        try:
            self.remove_widget(self.dtSSSv)
        except:
            pass
        try:
            self.dtSSGG.clear_widgets()
        except:
            pass
        l = []
        if word == "ALL CLASSES":
            sz = 0
            Cls = Clss()
            for word in Cls:
                TDAT = open(DIR + 'media' + PTH + '0' + PTH + ANGELS + PTH + '' + word + ".json", 'r')
                DT = json.load(TDAT)
                TDAT.close()
                for x in DT.keys():
                    if s.lower() in x.lower():
                        ugx = DT[x]["$"]["balance"][0:]
                        if ugx[0] == "-":
                            PS = "debt :" + ugx[1:]
                        else:
                            PS = "+ " + ugx[0:]
                        lalis = []
                        del DT[x]["$"]
                        del DT[x]["photo"]
                        try:
                            del DT[x]["marks"]
                        except:
                            pass
                        ggg = GridLayout(spacing=3, cols=1)
                        ggg.add_widget(AsyncImage(source=ASY + x + ".png"))
                        for name in DT[x].keys():
                            lalis.append(name + " :\n " + DT[x][name])
                        ggg.add_widget(Spinner(text=word + "| " + x + " | " + PS + " sh", values=tuple(lalis),
                                               size_hint=(1., .2)))
                        self.dtSSGG.add_widget(ggg)
                        sz += 0.33

        else:
            sz = 0
            TDAT = open(DIR + 'media' + PTH + '0' + PTH + ANGELS + PTH + '' + word + ".json", 'r')
            DT = json.load(TDAT)
            TDAT.close()
            for x in DT.keys():
                # if DT[word][x]["$"]["balance"][0]=="-":
                ugx = DT[x]["$"]["balance"][0:]
                if ugx[0] == "-":
                    PS = "debt :" + ugx[1:]
                else:
                    PS = "+" + ugx[0:]
                lalis = []
                del DT[x]["$"]
                del DT[x]["photo"]
                try:
                    del DT[x]["marks"]
                except:
                    pass
                ggg = GridLayout(spacing=3, cols=1)
                ggg.add_widget(AsyncImage(source=ASY + x + ".png"))
                for name in DT[x].keys():
                    lalis.append(name + " :\n " + DT[x][name])
                ggg.add_widget(Spinner(text=x + " | " + PS + " sh", values=tuple(lalis), size_hint=(.26, .2)))
                self.dtSSGG.add_widget(ggg)
                sz += 0.33
        self.dtSSGG.size = (840, 180 * sz + 100)
        self.dtSSSv.add_widget(self.dtSSGG)
        self.add_widget(self.dtSSSv)
        self.dtSSSv.scroll_y = 1

    def detDETAIL(self, spin, tt=None):

        word = self.dtS_class.text

        try:
            self.dtSSSv.clear_widgets()
        except:
            pass
        try:
            self.remove_widget(self.dtSSSv)
        except:
            pass
        try:
            self.dtSSGG.clear_widgets()
        except:
            pass
        l = []
        if word == "ALL CLASSES":
            sz = 0
            Cls = Clss()
            for word in Cls:
                TDAT = open(DIR + 'media' + PTH + '0' + PTH + ANGELS + PTH + '' + word + ".json", 'r')
                DT = json.load(TDAT)
                TDAT.close()
                for x in DT.keys():
                    if DT[x]["$"]["balance"][0] == "-":
                        ugx = DT[x]["$"]["balance"][0:]
                        if ugx[0] == "-":
                            PS = "debt :" + ugx[1:]
                        else:
                            PS = "+" + ugx[0:]
                        lalis = []
                        del DT[x]["$"]
                        del DT[x]["photo"]
                        try:
                            del DT[x]["marks"]
                        except:
                            pass
                        ggg = GridLayout(cols=1)
                        ggg.add_widget(AsyncImage(source=ASY + x + ".png"))
                        for name in DT[x].keys():
                            lalis.append(name + " :\n " + DT[x][name])
                        ggg.add_widget(Spinner(text=word + "| " + x + " | "+"\n" + PS + " sh", values=tuple(lalis),
                                               size_hint=(1., .4)))
                        self.dtSSGG.add_widget(ggg)
                        sz += 0.33

        else:
            sz = 0
            TDAT = open(DIR + 'media' + PTH + '0' + PTH + ANGELS + PTH + '' + word + ".json", 'r')
            DT = json.load(TDAT)
            TDAT.close()
            for x in DT.keys():
                if DT[x]["$"]["balance"][0] == "-":
                    ugx = DT[x]["$"]["balance"][0:]
                    if ugx[0] == "-":
                        PS = "debt :" + ugx[1:]
                    else:
                        PS = "+" + ugx[0:]
                    lalis = []
                    del DT[x]["$"]
                    del DT[x]["photo"]
                    try:
                        del DT[x]["marks"]
                    except:
                        pass
                    ggg = GridLayout(cols=1)
                    ggg.add_widget(AsyncImage(source=ASY + x + ".png"))
                    for name in DT[x].keys():
                        lalis.append(name + " :\n " + DT[x][name])
                    ggg.add_widget(Spinner(text=x + " | " +"\n"+ PS + " sh", values=tuple(lalis), size_hint=(.26, .4)))
                    self.dtSSGG.add_widget(ggg)
                    sz += 0.33
        self.dtSSGG.size = (840, 180 * sz + 100)
        self.dtSSSv.add_widget(self.dtSSGG)
        self.add_widget(self.dtSSSv)
        self.dtSSSv.scroll_y = 1

    def dtpr(self, s, t):

        if t == 'with pictures      ':
            if self.dtS_class.text == 'ALL CLASSES':
                return

            pickl = open(DIR + 'media' + PTH + '0' + PTH + 'SCHOOL.bin', 'rb')
            ids = pickle.load(pickl)
            pickl.close()
            # '+ids['1']+'

            self.dtSSGG.cols = 6
            self.dtSSSv.remove_widget(self.dtSSGG)
            self.exG = GridLayout(cols=1,spacing=10, size_hint=(None, None), size=(self.dtSSGG.width, self.dtSSGG.height + 260),
                                  pos_hint=self.dtSSGG.pos_hint)
            les_point = GridLayout(cols=3, size_hint=(None, None), size=(840, 170))
            im = AsyncImage(source=ASY + 'L.png', size_hint=(None, None), size=(150, 150), allow_stretch=True)
            les_point.add_widget(im)
            grid_in = GridLayout(cols=1, size_hint=(None, None), size=(360, 170), row_default_height=25,
                                 row_force_default=True)
            grid_in.add_widget(
                Label(text='  '+ids['1']+'               ', color=(0, 0, 1, 1), font_size=15))
            grid_in.add_widget(
                Label(text='       '+ids['2']+'               ', font_size=10, color=(0, 0, 0, 1)))
            grid_in.add_widget(
                Label(text='   '+ids['3']+'               ', font_size=10,
                      color=(0, 1, 0, 1)))
            grid_in.add_widget(
                Label(text='       '+ids['4']+'               ', font_size=10, color=(0, 0, 0, 1)))
            grid_in.add_widget(
                Label(text='     '+ids['5']+'               ', font_size=12, color=(1, 0, 0, 1)))
            # grid_in.add_widget(Label(text=' ' * 15 +self.v_class.text+' ' * 100 + ' ' * 20, underline=True, color=(1, 0, 0, 1)))
            les_point.add_widget(grid_in)
            ph = Label(text="DEBTS IN "+self.dtS_class.text, font_size=60, underline=True, italic=True, color=(0, 0, 0, .3))
            les_point.add_widget(ph)
            self.exG.add_widget(les_point)
            self.exG.add_widget(self.dtSSGG)
            self.dtSSSv.add_widget(self.exG)
            Clock.schedule_once(self.dtSSGGex, 4)

            # self.dtSSGG.cols = 4

        if t == 'without pictures':
            if self.dtS_class.text == 'ALL CLASSES':
                return

            pickl = open(DIR + 'media' + PTH + '0' + PTH + 'SCHOOL.bin', 'rb')
            ids = pickle.load(pickl)
            pickl.close()
            # '+ids['1']+'

            ls = []
            sz = 0
            self.gac = GridLayout(cols=4, size_hint=(None, None), row_default_height=30, row_force_default=True)
            # self.gac.add_widget(Label(text=""))
            FF = open(DIR + 'media' + PTH + '0' + PTH + ANGELS + PTH + '' + self.dtS_class.text + '.json', 'r')
            DF = json.load(FF)
            FF.close()
            for pp in DF.keys():
                if DF[pp]["$"]['balance'][0] == "-":
                    ls.append([float(DF[pp]["$"]['balance']),pp])
            ls.sort()
            print(ls)
            # ls.reverse()
            # print(ls)
            # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

            self.exG = GridLayout(cols=1, size_hint=(None, None))
            les_point = GridLayout(cols=3, size_hint=(None, None), size=(900, 170))
            im = AsyncImage(source=ASY + 'L.png', size_hint=(None, None), size=(150, 150), allow_stretch=True)
            les_point.add_widget(im)
            grid_in = GridLayout(cols=1, size_hint=(None, None), size=(360, 170), row_default_height=25,
                                 row_force_default=True)
            grid_in.add_widget(
                Label(text='  '+ids['1']+'               ', color=(0, 0, 1, 1), font_size=18))
            grid_in.add_widget(
                Label(text='       '+ids['2']+'               ', font_size=13, color=(0, 0, 0, 1)))
            grid_in.add_widget(
                Label(text='   '+ids['3']+'               ', font_size=13,
                      color=(0, 1, 0, 1)))
            grid_in.add_widget(
                Label(text='       '+ids['4']+'               ', font_size=13, color=(0, 0, 0, 1)))
            grid_in.add_widget(
                Label(text='     '+ids['5']+'               ', font_size=15, color=(1, 0, 0, 1)))
            # grid_in.add_widget(Label(text=' ' * 15 +self.v_class.text+' ' * 100 + ' ' * 20, underline=True, color=(1, 0, 0, 1)))
            les_point.add_widget(grid_in)
            ph = Label(text=self.dtS_class.text + " DEBTS : ", font_size=70, underline=True, italic=True, color=(0, 0, 0, .3))
            les_point.add_widget(ph)
            self.exG.add_widget(les_point)
            # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
            for i in range(8):
                self.gac.add_widget(Label(text=""))

            sz += 2
            for one in ls:
                self.gac.add_widget(TextInput(text=str(one[1])+"  "+str(one[0])))
                sz += 0.25

            self.gac.size = (840, 24 * sz + 50)
            self.exG.size = (840, 24 * sz + 250)
            # self.exG.width=, self.exG.height + 260
            self.exG.add_widget(self.gac)
            self.add_widget(self.exG)
            Clock.schedule_once(self.dtSSGGex, 3)
        self.dtSSGG.cols = 3
    def dtSSGGex(self,z):
        self.exG.export_to_png(
            NDR + 'Desktop' + PTH + 'P R I N T A B L E' + PTH + '' + self.dtS_class.text + " DEBTS P.png")

        self.print_all_i(NDR + 'Desktop' + PTH + 'P R I N T A B L E' + PTH + '' + self.dtS_class.text + " DEBTS P.png")

        self.exG.clear_widgets()
        self.remove_widget(self.exG)
        Clock.schedule_once(self.SORT_BY_DEBT)
    def dtSg(self, x):
        self.gac.export_to_png(
            NDR + 'Desktop' + PTH + 'P R I N T A B L E' + PTH + '' + self.dtS_class.text + " DEBTS.png")

        self.print_all_i(NDR + 'Desktop' + PTH + 'P R I N T A B L E' + PTH + '' + self.dtS_class.text + " DEBTS.png")

        self.remove_widget(self.gac)

    def detxXDDDetail(self, sp, t):

        self.dtSSdetail.text = ''

    def SUBJECT_AND_MARKS(self, X):
        try:
            self.remove_widget(self.secgrid)
        except:
            pass
        try:
            self.remove_widget(self.gridl)
        except:
            pass

        try:
            self.remove_widget(self.PrI)
        except:
            pass

        self.idd.background_color = (.3, .3, .3, 1)
        self.CL = Spinner(text='CLASS', values=tuple(Clss()), size_hint=(.2, .06),
                          pos_hint={'center_x': .1, 'center_y': .78})
        self.CL.bind(text=self.cselection)
        self.add_widget(self.CL)

        self.NM = Spinner(text=' ', size_hint=(.2, .06),
                          pos_hint={'center_x': .1, 'center_y': .72})
        self.NM.bind(text=self.marking)
        self.add_widget(self.NM)

        self.gridl = GridLayout(cols=2, pos_hint={'center_x': .75, 'center_y': .5}, size_hint=(.8, .5),
                                row_default_height=30, row_force_default=True)
        self.gridl.add_widget(
            Label(text="EXTEND THE LIST OF COMMENTS ", color=(1, .6, 0, 1), italic=True, underline=True))
        self.gridl.add_widget(Label(text="", color=(1, 1, 0, 1), italic=True))
        self.gridl.add_widget(Label(text="", color=(1, 1, 0, 1), italic=True))
        self.gridl.add_widget(Label(text="", color=(1, 1, 0, 1), italic=True))

        self.gridl.add_widget(Label(text="HEAD TEACHER COMMENTS ", color=(1, 1, 0, 1), italic=True))
        self.gridl.add_widget(Label(text="", color=(1, 1, 0, 1), italic=True))
        self.hhdt = TextInput(multiline=False, allow_copy=True)
        self.gridl.add_widget(self.hhdt)
        self.gridl.add_widget(
            Button(text="Add", color=(1, .6, 0, 1), size_hint=(None, None), size=(50, 30), on_release=self.HTc))

        self.gridl.add_widget(Label(text="CLASS TEACHER COMMENTS ", color=(1, 1, 0, 1), italic=True))
        self.gridl.add_widget(Label(text="", color=(1, 1, 0, 1), italic=True))
        self.clsst = TextInput(multiline=False, allow_copy=True)
        self.gridl.add_widget(self.clsst)
        self.gridl.add_widget(
            Button(text="Add", color=(1, .6, 0, 1), size_hint=(None, None), size=(50, 30), on_release=self.cTc))

        self.gridl.add_widget(Label(text="DEBATE ", color=(1, 1, 0, 1), italic=True))
        self.gridl.add_widget(Label(text="", color=(1, 1, 0, 1), italic=True))
        self.DDebat = TextInput(multiline=False, allow_copy=True)
        self.gridl.add_widget(self.DDebat)
        self.gridl.add_widget(
            Button(text="Add", color=(1, .6, 0, 1), size_hint=(None, None), size=(50, 30), on_release=self.dbt))

        self.gridl.add_widget(Label(text="CONDUCT ", color=(1, 1, 0, 1), italic=True))
        self.gridl.add_widget(Label(text="", color=(1, 1, 0, 1), italic=True))
        self.CConduct = TextInput(multiline=False, allow_copy=True)
        self.gridl.add_widget(self.CConduct)
        self.gridl.add_widget(
            Button(text="Add", color=(1, .6, 0, 1), size_hint=(None, None), size=(50, 30), on_release=self.cndct))

        self.gridl.add_widget(Label(text="", color=(1, 1, 0, 1), italic=True))
        self.gridl.add_widget(Label(text="", color=(1, 1, 0, 1), italic=True))
        self.gridl.add_widget(Button(text="BUILD REPORT QRCODE ", color=(1, 1, 1, 1),on_release=self.RMKS))

        self.REMKS = TextInput(multiline=False, allow_copy=True)
        # self.gridl.add_widget(self.REMKS)
        # self.gridl.add_widget(
        #     Button(text="Add", color=(1, .6, 0, 1), size_hint=(None, None), size=(50, 30), on_release=self.RMKS))

        self.add_widget(self.gridl)
        self.Called = '2'
        self.Chois = Spinner(text='End of term', values=('Mid term', 'End of term'), size_hint=(.2, .06),
                             pos_hint={'center_x': .6, 'center_y': .78})
        self.Chois.bind(text=self.callscelect)

    def callscelect(self, s, c):
        if c == 'Mid term':
            self.Called = "1"
        else:
            self.Called = "2"
        self.cselection(None, self.backward)

    def cTc(self, x):
        if self.clsst.text == "":
            return
        zzz = open(DIR + 'media' + PTH + '0' + PTH + 'ctcomment', 'rb')
        x = pickle.load(zzz)
        zzz.close()

        x.append(self.clsst.text)

        ll = open(DIR + 'media' + PTH + '0' + PTH + 'ctcomment', 'wb')
        pickle.dump(x, ll)
        ll.close()
        self.clsst.text = ""

    def HTc(self, x):
        if self.hhdt.text == "":
            return
        zzz = open(DIR + 'media' + PTH + '0' + PTH + 'hdcomment', 'rb')
        x = pickle.load(zzz)
        zzz.close()

        x.append(self.hhdt.text)

        ll = open(DIR + 'media' + PTH + '0' + PTH + 'hdcomment', 'wb')
        pickle.dump(x, ll)
        ll.close()
        self.hhdt.text = ""

    def cndct(self, X):
        if self.CConduct.text == "":
            return
        zzz = open(DIR + 'media' + PTH + '0' + PTH + 'conduct', 'rb')
        x = pickle.load(zzz)
        zzz.close()

        x.append(self.CConduct.text)

        ll = open(DIR + 'media' + PTH + '0' + PTH + 'conduct', 'wb')
        pickle.dump(x, ll)
        ll.close()
        self.CConduct.text = ""

    def dbt(self, x):
        if self.DDebat.text == "":
            return
        zzz = open(DIR + 'media' + PTH + '0' + PTH + 'debat', 'rb')
        x = pickle.load(zzz)
        zzz.close()

        x.append(self.DDebat.text)

        ll = open(DIR + 'media' + PTH + '0' + PTH + 'debat', 'wb')
        pickle.dump(x, ll)
        ll.close()
        self.DDebat.text = ""

    def RMKS(self, x):
        global next,ends,rq1,rq2,rq3,rq4,rq5,rq6,rq7,rq8,fn,f13,f46,f7,popup2

        grid=GridLayout(cols=1,size_hint=(.75,.98))
        next=TextInput(hint_text="next term begins on : ",allow_copy=True)
        ends=TextInput(hint_text="Ends on : ",allow_copy=True)
        rq1=TextInput(hint_text="Requirement 1 : ",allow_copy=True)
        rq2 = TextInput(hint_text="Requirement 2 : ", allow_copy=True)
        rq3 = TextInput(hint_text="Requirement 3 : ", allow_copy=True)
        rq4 = TextInput(hint_text="Requirement 4 : ", allow_copy=True)
        rq5 = TextInput(hint_text="Requirement 5 : ", allow_copy=True)
        rq6 = TextInput(hint_text="Requirement 6 : ", allow_copy=True)
        rq7 = TextInput(hint_text="Requirement 7 : ", allow_copy=True)
        rq8 = TextInput(hint_text="Requirement 8 : ", allow_copy=True)
        fn=TextInput(hint_text="Fees Nusary : ",allow_copy=True)
        f13 = TextInput(hint_text="Fees P1-P3 : ", allow_copy=True)
        f46 = TextInput(hint_text="Fees P4-P6 : ", allow_copy=True)
        f7 = TextInput(hint_text="Fees P7 : ", allow_copy=True)
        em= Label(text=" ")
        sv = Button(text="S A V E", on_release=self.svqr)

        vl=[next,ends,rq1,rq2,rq3,rq4,rq5,rq6,rq7,rq8,fn,f13,f46,f7,em,sv]
        for i in vl :
            grid.add_widget(i)


        popup2=Popup(title='Compressed informations', size_hint=(.5, .8), content=grid, disabled=False)
        popup2.open()

        # if self.REMKS.text == "":
        #     return
        # zzz = open(DIR + 'media' + PTH + '0' + PTH + 'REMARKS', 'rb')
        # x = pickle.load(zzz)
        # zzz.close()
        #
        # x.append(self.REMKS.text)
        #
        # ll = open(DIR + 'media' + PTH + '0' + PTH + 'REMARKS', 'wb')
        # pickle.dump(x, ll)
        # ll.close()
        # self.REMKS.text = ""
    def svqr(self,x):
        import qrcode
        # next, ends, rq1, rq2, rq3, rq4, rq5, rq6, rq7, rq8, fn, f13, f46, f7
        str="The next term will begin on : "+next.text +"\n will end on : "+ends.text+".\n" \
         "The requirements for next term are :\n" +rq1.text+"\n"+rq2.text+"\n"+rq3.text+"\n"+rq4.text+"\n"+rq5.text+"\n"+rq6.text+"\n"+rq7.text+"\n"+rq8.text+"\n"\
        "The school fees for : \n" \
        "Nusary is : "+fn.text+" ugx\n"+"P1-P3 is : "+f13.text+" ugx\n"+"P4-P6 is : "+f46.text+" ugx\n"+"P7 is : "+f7.text+" ugx"
        img=qrcode.make(str)
        img.save(DIR + 'media' + PTH + '0' + PTH + 'QR.png')
        print(str)
        popup2.dismiss()

    def marking(self, sp, tx):

        try:
            self.remove_widget(self.Chois)
        except:
            pass

        try:
            self.remove_widget(self.scrll)
        except:
            pass
        try:
            self.remove_widget(self.BGSV)
        except:
            pass
        try:
            self.remove_widget(self.BIG13)
        except:
            pass
        try:
            self.remove_widget(self.BIG47)
        except:
            pass

        if self.NM.text == " ":
            return
        if self.CL.text[0] == "N":
            Clock.schedule_once(self.nasry)
        if self.CL.text[:2] in ("P1", "P2", "P3"):
            Clock.schedule_once(self.p1p3)
        if self.CL.text[:2] in ("P4", "P5", "P6", "P7"):
            Clock.schedule_once(self.p4p7)

        ##############################               COMPLETE STUDENT DATA IN FIELD         ################

    def RPupdown(self, window, key, *largs):
        if key == 273:
            self.roll = self.roll + .01
            self.BGSV.scroll_y = self.roll
            print("^", self.roll)
        if key == 274:
            self.roll = self.roll - .01
            self.BGSV.scroll_y = self.roll
            print("v", self.roll)

    def p4p7(self, x):
        self.roll = 1
        Window.bind(on_keyboard=self.RPupdown)

        try:
            self.remove_widget(self.print_report)
        except:
            pass

        self.print_report = Button(text='PRINT', size_hint=(.2, .06), pos_hint={'center_x': .90, 'center_y': .78},
                                   on_release=self.png47)
        self.add_widget(self.print_report)
        # self.print_report.bind()

        file = open(DIR + 'media' + PTH + '0' + PTH + ANGELS + PTH + '' + self.CL.text + ".json", 'r')
        dict = json.load(file)
        file.close()
        # print(dict)
        # print((dict[self.NM.text]['marks']['total']['term2']['mgt2_TT']))
        self.BGSV = ScrollView(size_hint=(.976, .63), pos_hint={'center_x': .5, 'center_y': .4}, do_scroll_x=False,
                               do_scroll_y=True, scroll_timeout=55, scroll_distance=20, scroll_type=['bars', 'content'],
                               bar_width=10, bar_color=(1, 1, 0, 1), bar_margin=0)
        self.BGG = GridLayout(cols=1, spacing=1, padding=0, size_hint=(None, None), size=(780, 1169),  # SCREENSHOOT
                              pos_hint={'center_x': .5, 'center_y': .4})
        with self.BGG.canvas.after:
            Color(1, 0, .7, 1)
            r1ec = Rectangle(pos=(0, 1), size=(10, self.height * 2 - 105))
            r2ec = Rectangle(pos=(0, self.height * 2 - 105), size=(780, 10))
            r3ec = Rectangle(pos=(770, 1), size=(10, self.height * 2 - 105))
            r4ec = Rectangle(pos=(0, 1), size=(780, 10))

        self.printable = GridLayout(cols=1, spacing=1, padding=0, size_hint=(1., None), size=(780, 400),  # SCREENSHOOT
                                    pos_hint={'center_x': .5, 'center_y': .5}, row_default_height=90,
                                    row_force_default=True)
        self.printable.add_widget(
            Label(text=" " * 161, color=(0, 0, 1, 1), size_hint=(1., None), size=(780, 40), italic=True))
        # self.printable.add_widget(Label(text=" " * 161, color=(0, 0, 1, 1), italic=True))

        self.num1 = BoxLayout(spacing=0, padding=0, size_hint=(1., None), size=(780, 142))
        # ___________________________

        im = AsyncImage(source=ASY + 'L.png', size_hint=(None, None), size=(200, 140), allow_stretch=True)
        self.num1.add_widget(im)
        self.gnum1 = GridLayout(cols=1, size_hint=(None, None), size=(380, 140), row_default_height=27,
                                row_force_default=True)
        # _______________________________

        pickl = open(DIR + 'media' + PTH + '0' + PTH + 'SCHOOL.bin', 'rb')
        ids = pickle.load(pickl)
        pickl.close()

        # self.gnum1.add_widget(Label(text=' '))
        self.gnum1.add_widget( Label(text='   '+ids['1']+'               ', color=(0, 0, 1, 1), font_size=20))
        self.gnum1.add_widget(Label(text='       '+ids['2']+'               ', color=(0, 0, 0, 1)))
        self.gnum1.add_widget( Label(text='   '+ids['3']+'               ', color=(0, 1, 0, 1)))
        self.gnum1.add_widget(Label(text='       '+ids['4']+'               ', color=(0, 0, 0, 1)))
        self.gnum1.add_widget( Label(text='     '+ids['5']+'               ', color=(1, 0, 0, 1), font_size=20))
        self.gnum1.add_widget(Label(text=' ' * 15 + '-' * 100 + ' ' * 20, underline=True, color=(1, 0, 0, 1)))

        self.num1.add_widget(self.gnum1)
        sim = AsyncImage(source=ASY + self.NM.text + '.png', size_hint=(None, None), size=(200, 140),
                         allow_stretch=True)
        self.num1.add_widget(sim)

        self.gnum2 = GridLayout(cols=8, padding=1, spacing=1, size_hint=(1., None), size=(780, 40))
        self.gnum2.add_widget(TextInput(text='   Name :  '+self.NM.text.capitalize(),background_normal="rb2.png",
                                        background_active="rb2.png",foreground_color=(1, 1, .7, 1),background_color=(.4, 0, .7, 1),
                                        size_hint=(None,None),size=(300,40)))
        # self.gnum2.add_widget(TextInput(text=self.NM.text.capitalize(), color=(0, 0, 1, 1), italic=True))
        self.gnum2.add_widget(TextInput(text='Sex :  '+dict[self.NM.text]['Sex'], background_normal="rb2.png",
                                        background_active="rb2.png",foreground_color=(1, 1, .7, 1),background_color=(.4, 0, .7, 1)))
        # self.gnum2.add_widget(TextInput(text=dict[self.NM.text]['Sex'], color=(0, 0, 1, 1), italic=True))
        self.gnum2.add_widget(TextInput(text='Class :  '+self.CL.text, background_normal="rb2.png",
                                        background_active="rb2.png",foreground_color=(1, 1, .7, 1),background_color=(.4, 0, .7, 1)))

        self.gnum2.add_widget(TextInput(text=self.TERM.text, background_normal="rb2.png",
                                        background_active="rb2.png", foreground_color=(1, 1, .7, 1),
                                        background_color=(.4, 0, .7, 1)))

        # self.gnum2.add_widget(TextInput(text=self.CL.text, color=(0, 0, 1, 1), italic=True))

        # self.term = Label(text='', color=(0, 0, 1, 1), italic=True)
        # if time.strftime("%m") in ('01','02', '03', '04'):
        #     self.gnum2.add_widget(TextInput(text='Term :  I', background_normal="rb2.png",
        #                                 background_active="rb2.png",foreground_color=(1, 1, .7, 1),background_color=(.4, 0, .7, 1)))
        # if time.strftime("%m") in ('05', '06', '07'):
        #     self.gnum2.add_widget(TextInput(text='Term :  II', background_normal="rb2.png",
        #                                 background_active="rb2.png",foreground_color=(1, 1, .7, 1),background_color=(.4, 0, .7, 1)))
        # if time.strftime("%m") in ('08', '09', '10', '11'):
        #     self.gnum2.add_widget(TextInput(text='Term :  III', background_normal="rb2.png",
        #                                 background_active="rb2.png",foreground_color=(1, 1, .7, 1),background_color=(.4, 0, .7, 1)))


        self.printable.add_widget(self.num1)
        self.line = GridLayout(cols=1, size_hint=(1., .01), row_default_height=10,
                               row_force_default=True)
        self.line.add_widget(Label(text=' ' * 20 + '-' * 100 + ' ' * 20, underline=True, color=(0, 0, 0, 1)))
        # self.printable.add_widget(self.line)
        self.printable.add_widget(self.gnum2)

        self.gnum3 = GridLayout(cols=3, padding=1, spacing=1, row_default_height=40, row_force_default=True) #, row_default_height=6, row_force_default=True
        # ////////////////////////////////////////////

        l = []
        for x in dict.keys():
            if not dict[x].get('marks'):
                # del (dict[x])
                grade = ""
            else:
                lst=[]

                if dict[x]['marks']['total']['term' + self.Called]['agt' + self.Called + '_TT'] == '':
                    dict[x]['marks']['total']['term' + self.Called]['agt' + self.Called + '_TT'] = "0"
                lst.append(int(dict[x]['marks']['total']['term' + self.Called]['agt' + self.Called + '_TT']))
                lst.append(division(dict[x]['marks']['mtc']['term' + self.Called]['mgt' + self.Called],
                                    dict[x]['marks']['eng']['term' + self.Called]['mgt' + self.Called + '_ENG'],
                                    dict[x]['marks']['sst']['term' + self.Called]['mgt' + self.Called + '_SST'],
                                    dict[x]['marks']['scie']['term' + self.Called]['mgt' + self.Called + '_SCIE'],
                                    dict[x]['marks']['total']['term' + self.Called]['agt' + self.Called + '_TT']))
                lst.append(x)
                l.append(lst)

        l.sort()

        for i in l :
            if self.NM.text in i :
                grade=l.index(i)+1
                div=i[1]

        self.gnum3.add_widget(TextInput(text='         End of term Position : '+str(grade), background_normal="rb2.png",
                                        background_active="rb2.png",foreground_color=(1, 1, .7, 1),background_color=(.4, 0, .7, 1),size_hint=(None, None), size=(250, 40)))
        # self.gnum3.add_widget(TextInput(text="DIV II", background_normal="rb2.png",
        #                                 background_active="rb2.png",foreground_color=(1, 1, .7, 1),background_color=(.4, 0, .7, 1), size_hint=(1., .01)))
        self.gnum3.add_widget(TextInput(text='Out of : '+str(len(dict.keys())) + " Pupils", background_normal="rb2.png",
                                        background_active="rb2.png",foreground_color=(1, 1, .7, 1),background_color=(.4, 0, .7, 1),size_hint=(None, None), size=(200, 40)))
        # self.gnum3.add_widget(TextInput(text=str(len(dict.keys())) + " Pupils", background_normal="rb2.png",
        #                                 background_active="rb2.png",foreground_color=(1, 1, .7, 1),background_color=(.4, 0, .7, 1), size_hint=(1., .01)))
        self.gnum3.add_widget(TextInput(text='Date : '+time.strftime('%d %B %y'), background_normal="rb2.png",
                                        background_active="rb2.png",foreground_color=(1, 1, .7, 1),background_color=(.4, 0, .7, 1)))
        self.gnum3.add_widget( Label(text="*******",color=(.6, 0, .4, 1), font_size=43,size_hint=(None,None),size=(200,50)))
        self.gnum3.add_widget(Label(text=div,color=(.6, 0, .4, 1), font_size=40, size_hint=(None, None), size=(200, 50)))
        self.gnum3.add_widget(Label(text="*******",color=(.6, 0, .4, 1), font_size=43, size_hint=(1., None), size=(780, 40)))


        PRC=TextInput(hint_text="     AVERAGE PERCENTAGE :  ",readonly=True, foreground_color=(1, 1, 1, 1), background_color=(0, 0, 0, .4),size_hint=(None, None), size=(300, 30))
        self.gnum3.add_widget(PRC)
        NEXT=TextInput(hint_text="",readonly=True, foreground_color=(1, 1, 1, 1), background_color=(0, 0, 0, .4),size_hint=(None, None), size=(270, 30))
        self.gnum3.add_widget(NEXT)

        self.printable.add_widget(self.gnum3)

        self.BIG = GridLayout(cols=5, size_hint=(1., None), size=(780, 420), pos_hint={'center_x': .5, 'center_y': .6},
                              row_default_height=30,
                              row_force_default=True)
        self.BIG.add_widget(TextInput(text='    SUBJECT', readonly=True, size_hint=(.2, .09)))
        self.BIG.add_widget(TextInput(text='MID TERM', readonly=True, size_hint=(.2, .09)))
        self.BIG.add_widget(TextInput(text='END OF TERM', readonly=True, size_hint=(.2, .09)))
        self.BIG.add_widget(TextInput(text='REMARKS', readonly=True, size_hint=(.2, .09)))
        self.BIG.add_widget(TextInput(text='INITIALS', readonly=True, size_hint=(.2, .09)))

        # self.gggg.add_widget(Label(text='', color=(0, 0, 0, 1)))
        self.BIG.add_widget(
            TextInput(text=' /////////////////////////////////',multiline=False, font_size=35, background_color=(1, 1, 0, 1),
                      readonly=True))

        self.gt1 = GridLayout(cols=3, size_hint_y=.09, row_default_height=30,
                              row_force_default=True)

        self.gt1.add_widget(TextInput(text='MAX',multiline=False, font_size=15,readonly=True))
        self.gt1.add_widget(TextInput(text='Marks',multiline=False,font_size=15, readonly=True))
        self.gt1.add_widget(TextInput(text='Agg', readonly=True))
        self.BIG.add_widget(self.gt1)

        self.gt2 = GridLayout(cols=3, size_hint_y=.09, row_default_height=30,
                              row_force_default=True)

        self.gt2.add_widget(TextInput(text='MAX', multiline=False,font_size=15,readonly=True))
        self.gt2.add_widget(TextInput(text='Marks',multiline=False,font_size=15, readonly=True))
        self.gt2.add_widget(TextInput(text='Agg', readonly=True))
        self.BIG.add_widget(self.gt2)

        self.BIG.add_widget(
            TextInput(text='/////////////////////////////////////', multiline=False,font_size=35, background_color=(1, 1, 0, 1),
                      readonly=True))
        self.BIG.add_widget(
            TextInput(text='/////////////////////////////////', multiline=False,font_size=35, background_color=(1, 1, 0, 1),
                      readonly=True))
        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        self.MTC = TextInput(text='    MTC', readonly=True)
        self.BIG.add_widget(self.MTC)
        self.fmt1 = TextInput(text='100', background_color=(0, .8, .1, 1), foreground_color=(1, 1, 1, 1), readonly=True)
        self.gt1.add_widget(self.fmt1)
        self.mgt1 = TextInput(multiline=False, foreground_color=(0, 0, 1, 1))
        self.mgt1.bind(text=self.sv_p47)
        self.gt1.add_widget(self.mgt1)
        self.agt1 = TextInput(multiline=False, foreground_color=(1, 0, 0, 1))
        self.agt1.bind(text=self.sv_p47)
        self.gt1.add_widget(self.agt1)

        self.fmt2 = TextInput(text='100', background_color=(0, .8, .1, 1), foreground_color=(1, 1, 1, 1), readonly=True)
        self.gt2.add_widget(self.fmt2)
        self.mgt2 = TextInput(multiline=False, foreground_color=(0, 0, 1, 1))
        self.mgt2.bind(text=self.sv_p47)
        self.gt2.add_widget(self.mgt2)
        self.agt2 = TextInput(multiline=False, foreground_color=(1, 0, 0, 1))
        self.agt2.bind(text=self.sv_p47)
        self.gt2.add_widget(self.agt2)
        self.BIG.add_widget(Label(text=""))
        self.BIG.add_widget(Label(text=""))
        self.REM1 = TextInput(foreground_color=(1, 0, 0, 1), allow_copy=True)
        self.REM1.bind(text=self.sv_p47)
        self.BIG.add_widget(self.REM1)
        self.INIT1 = TextInput(multiline=False, foreground_color=(0, 0, 1, 1))
        self.INIT1.bind(text=self.sv_p47)
        self.BIG.add_widget(self.INIT1)

        #                 _ENG                #

        self.ENG = TextInput(text='    ENG', readonly=True)
        self.BIG.add_widget(self.ENG)
        self.fmt1_ENG = TextInput(text='100', background_color=(0, .8, .1, 1), foreground_color=(1, 1, 1, 1),
                                  readonly=True)
        self.gt1.add_widget(self.fmt1_ENG)
        self.mgt1_ENG = TextInput(multiline=False, foreground_color=(0, 0, 1, 1))
        self.mgt1_ENG.bind(text=self.sv_p47)
        self.gt1.add_widget(self.mgt1_ENG)
        self.agt1_ENG = TextInput(multiline=False, foreground_color=(1, 0, 0, 1))
        self.agt1_ENG.bind(text=self.sv_p47)
        self.gt1.add_widget(self.agt1_ENG)

        self.fmt2_ENG = TextInput(text='100', background_color=(0, .8, .1, 1), foreground_color=(1, 1, 1, 1),
                                  readonly=True)
        self.gt2.add_widget(self.fmt2_ENG)
        self.mgt2_ENG = TextInput(multiline=False, foreground_color=(0, 0, 1, 1))
        self.mgt2_ENG.bind(text=self.sv_p47)
        self.gt2.add_widget(self.mgt2_ENG)
        self.agt2_ENG = TextInput(multiline=False, foreground_color=(1, 0, 0, 1))
        self.agt2_ENG.bind(text=self.sv_p47)
        self.gt2.add_widget(self.agt2_ENG)
        self.BIG.add_widget(Label(text=""))
        self.BIG.add_widget(Label(text=""))
        self.REM1_ENG = TextInput(foreground_color=(1, 0, 0, 1), allow_copy=True)
        self.REM1_ENG.bind(text=self.sv_p47)
        self.BIG.add_widget(self.REM1_ENG)
        self.INIT1_ENG = TextInput(multiline=False, foreground_color=(0, 0, 1, 1))
        self.INIT1_ENG.bind(text=self.sv_p47)
        self.BIG.add_widget(self.INIT1_ENG)

        #        _SST                 #

        self.SST = TextInput(text='    SST', readonly=True)
        self.BIG.add_widget(self.SST)
        self.fmt1_SST = TextInput(text='100', background_color=(0, .8, .1, 1), foreground_color=(1, 1, 1, 1),
                                  readonly=True)
        self.gt1.add_widget(self.fmt1_SST)
        self.mgt1_SST = TextInput(multiline=False, foreground_color=(0, 0, 1, 1))
        self.mgt1_SST.bind(text=self.sv_p47)
        self.gt1.add_widget(self.mgt1_SST)
        self.agt1_SST = TextInput(multiline=False, foreground_color=(1, 0, 0, 1))
        self.agt1_SST.bind(text=self.sv_p47)
        self.gt1.add_widget(self.agt1_SST)

        self.fmt2_SST = TextInput(text='100', background_color=(0, .8, .1, 1), foreground_color=(1, 1, 1, 1),
                                  readonly=True)
        self.gt2.add_widget(self.fmt2_SST)
        self.mgt2_SST = TextInput(multiline=False, foreground_color=(0, 0, 1, 1))
        self.mgt2_SST.bind(text=self.sv_p47)
        self.gt2.add_widget(self.mgt2_SST)
        self.agt2_SST = TextInput(multiline=False, foreground_color=(1, 0, 0, 1))
        self.agt2_SST.bind(text=self.sv_p47)
        self.gt2.add_widget(self.agt2_SST)
        self.BIG.add_widget(Label(text=""))
        self.BIG.add_widget(Label(text=""))
        self.REM1_SST = TextInput(foreground_color=(1, 0, 0, 1), allow_copy=True)
        self.REM1_SST.bind(text=self.sv_p47)
        self.BIG.add_widget(self.REM1_SST)
        self.INIT1_SST = TextInput(multiline=False, foreground_color=(0, 0, 1, 1))
        self.INIT1_SST.bind(text=self.sv_p47)
        self.BIG.add_widget(self.INIT1_SST)

        #          _SCIE

        self.SCIE = TextInput(text='    SCIE', readonly=True)
        self.BIG.add_widget(self.SCIE)
        self.fmt1_SCIE = TextInput(text='100', background_color=(0, .8, .1, 1), foreground_color=(1, 1, 1, 1),
                                   readonly=True)
        self.gt1.add_widget(self.fmt1_SCIE)
        self.mgt1_SCIE = TextInput(multiline=False, foreground_color=(0, 0, 1, 1))
        self.mgt1_SCIE.bind(text=self.sv_p47)
        self.gt1.add_widget(self.mgt1_SCIE)
        self.agt1_SCIE = TextInput(multiline=False, foreground_color=(1, 0, 0, 1))
        self.agt1_SCIE.bind(text=self.sv_p47)
        self.gt1.add_widget(self.agt1_SCIE)

        self.fmt2_SCIE = TextInput(text='100', background_color=(0, .8, .1, 1), foreground_color=(1, 1, 1, 1),
                                   readonly=True)
        self.gt2.add_widget(self.fmt2_SCIE)
        self.mgt2_SCIE = TextInput(multiline=False, foreground_color=(0, 0, 1, 1))
        self.mgt2_SCIE.bind(text=self.sv_p47)
        self.gt2.add_widget(self.mgt2_SCIE)
        self.agt2_SCIE = TextInput(multiline=False, foreground_color=(1, 0, 0, 1))
        self.agt2_SCIE.bind(text=self.sv_p47)
        self.gt2.add_widget(self.agt2_SCIE)
        self.BIG.add_widget(Label(text=""))
        self.BIG.add_widget(Label(text=""))
        self.REM1_SCIE = TextInput(foreground_color=(1, 0, 0, 1), allow_copy=True)
        self.REM1_SCIE.bind(text=self.sv_p47)
        self.BIG.add_widget(self.REM1_SCIE)
        self.INIT1_SCIE = TextInput(multiline=False, foreground_color=(0, 0, 1, 1))
        self.INIT1_SCIE.bind(text=self.sv_p47)
        self.BIG.add_widget(self.INIT1_SCIE)

        #            _TT           #

        self.TOTT = TextInput(text='    TOTAL', readonly=True)
        self.BIG.add_widget(self.TOTT)
        self.fmt1_TT = TextInput(text='400', background_color=(1, 1, 0, 1), readonly=True)
        self.gt1.add_widget(self.fmt1_TT)
        self.mgt1_TT = TextInput(multiline=False, background_color=(1, 1, 0, 1), foreground_color=(0, 0, 0, 1))
        self.mgt1_TT.bind(text=self.sv_p47)
        self.gt1.add_widget(self.mgt1_TT)
        self.agt1_TT = TextInput(multiline=False, background_color=(1, 1, 0, 1), foreground_color=(1, 0, 0, 1))
        self.agt1_TT.bind(text=self.sv_p47)
        self.gt1.add_widget(self.agt1_TT)

        self.fmt2_TT = TextInput(text='400', background_color=(1, 1, 0, 1), readonly=True)
        self.gt2.add_widget(self.fmt2_TT)
        self.mgt2_TT = TextInput(multiline=False, background_color=(1, 1, 0, 1), foreground_color=(0, 0, 0, 1))
        self.mgt2_TT.bind(text=self.sv_p47)
        self.gt2.add_widget(self.mgt2_TT)
        self.agt2_TT = TextInput(multiline=False, background_color=(1, 1, 0, 1), foreground_color=(1, 0, 0, 1))
        self.agt2_TT.bind(text=self.sv_p47)
        # self.agt2_TT.bind(text=self.sv_p47)
        self.gt2.add_widget(self.agt2_TT)
        self.BIG.add_widget(Label(text=""))
        self.BIG.add_widget(Label(text=""))
        self.REM1_TT = TextInput(hint_text=' /////////////////////////////////',multiline=False, font_size=35, background_color=(.6, 1, 0, 1), foreground_color=(1, 0, 0, 1))
        self.REM1_TT.bind(text=self.sv_p47)
        self.BIG.add_widget(self.REM1_TT)
        self.INIT1_TT = TextInput(hint_text=' /////////////////////////////////',multiline=False, font_size=35, background_color=(.6, 1, 0, 1), foreground_color=(1, 0, 0, 1))
        self.INIT1_TT.bind(text=self.sv_p47)
        self.BIG.add_widget(self.INIT1_TT)

        self.BGG.add_widget(self.printable)

        self.BGG.add_widget(self.BIG)

        self.p2 = GridLayout(cols=2, spacing=60, padding=0, size_hint=(1., None), size=(780, 564),
                              row_default_height=70, row_force_default=True) #pos_hint={'center_x': .5, 'center_y': .5},
        with self.p2.canvas.before:
            Color(1, 0, .7, .4)
            rec = Rectangle(source='wp.png',pos=(18, 288), size=(450, 255)) #,pos=(0, 1)


        self.gnum4 = GridLayout(cols=2, padding=30, spacing=8,size_hint=(1., None), size=(780, 270), row_default_height=30, row_force_default=True,
                                col_default_width=200, col_force_default=True)  #size_hint=(None,None),size=(420,280),pos=(18, 240),

        self.gnum4.add_widget(TextInput(text='Conduct :  ',readonly=True, foreground_color=(0, 0, 0, 1),size_hint=(None,None),size=(120,30)))
        self.behav = Spinner(text=" " + conduct()[0],values=tuple(conduct()), color=(1, 1, 0, 1), background_color=(0, 0, 0, 0),
                             background_normal='btn4.png', size_hint=(.2,None),size=(120,30))   # size=(400, 30)
        self.gnum4.add_widget(self.behav)

        self.gnum4.add_widget(TextInput(text='Debating :  ',readonly=True,size_hint=(None,None),size=(120,30), foreground_color=(0, 0, 0, 1)))
        self.debat = Spinner(text=debat()[0], values=tuple(debat()), color=(1, 1, 0, 1),
                             background_color=(0, 0, 0, 0), background_normal='btn4.png', size_hint=(.2,None),size=(120,30))
        self.gnum4.add_widget(self.debat)

        self.gnum4.add_widget(TextInput(text='C.T’s comment :  ', readonly=True,size_hint=(None,None),size=(140,30),foreground_color=(0, 0, 0, 1)))
        self.gnum4.add_widget(Spinner(text=ctcomment()[1], values=tuple(ctcomment()), color=(0, 0, 1, 1),background_color=(0, 0, 0, 0)))

        self.gnum4.add_widget(TextInput(text='H.T’s comment :  ',readonly=True,size_hint=(None,None),size=(140,30), foreground_color=(0, 0, 0, 1)))
        self.gnum4.add_widget(Spinner(text=hdcomment()[1], values=tuple(hdcomment()), color=(0, 0, 1, 1), background_color=(0, 0, 0, 0)))
        self.gnum4.add_widget(TextInput(text='C.T’s signature :.......................................  ',readonly=True,
                                        size_hint=(None,None),size=(340,30),foreground_color=(0, 0, 0, 1)))
        self.gnum4.add_widget(Label(text="*",size_hint=(None, None), size=(20, 30)))
        self.gnum4.add_widget(TextInput(text='H.T’s signature :.......................................  ',readonly=True,
                                        size_hint=(None, None), size=(340, 30), foreground_color=(0, 0, 0, 1)))



        self.box = GridLayout(cols=1, size_hint=(1., None), size=(780, 270), col_default_width=300, col_force_default=True) #row_default_height=300, row_force_default=True,
        self.box.add_widget(Label(text='Signature/Seal..................... ', color=(0, 0, 0, 1)))

        self.p2.add_widget(self.gnum4)
        self.p2.add_widget(self.box)

        # self.p2.add_widget(Label(text="", size_hint=(None, None), size=(250, 40)))
        # self.p2.add_widget(Label(text="", size_hint=(None, None), size=(250, 40)))
        self.p2.add_widget(Label(text='       “WE                  WISH YOU THE BEST ! ”', color=(0, 0, 0, 1), size_hint=(None, None), size=(430, 150),
                  bold=True, font_size=24))
        self.p2.add_widget(Label(text="", size_hint=(None, None), size=(250, 60))) #

        self.lst1 = GridLayout(cols=1, size_hint=(.4, None), size=(780, 250), col_force_default=True)  #row_default_height=150, row_force_default=True, col_default_width=300,
        self.p2.add_widget(AsyncImage(source="tm.png", size_hint=(None, None), size=(300, 300)))


        self.lst2 = GridLayout(cols=1,  size_hint=(.4, None), size=(780, 250)) #row_default_height=150, row_force_default=True,,col_default_width=300, col_force_default=True
        self.p2.add_widget( AsyncImage(source=ASY + 'QR.png',size_hint=(None, None), size=(220,220)))   #,
        # self.p2.add_widget(self.lst1)
        # self.p2.add_widget(self.lst2)
        self.BGG.add_widget(self.p2)







        self.BGSV.add_widget(self.BGG)
        self.add_widget(self.BGSV)

        if dict[self.NM.text].get("marks"):
            self.mgt1.text = dict[self.NM.text]["marks"]['mtc']['term1'].get("mgt1", "")
            self.agt1.text = dict[self.NM.text]["marks"]['mtc']['term1'].get("agt1", "")
            self.mgt2.text = dict[self.NM.text]["marks"]['mtc']['term2'].get("mgt2", "")
            self.agt2.text = dict[self.NM.text]["marks"]['mtc']['term2'].get("agt2", "")
            self.REM1.text = dict[self.NM.text]["marks"]['mtc']['term2'].get("REM1", "")
            self.INIT1.text = dict[self.NM.text]["marks"]['mtc']['term2'].get("INIT1", "")
            # _ENG
            self.mgt1_ENG.text = dict[self.NM.text]["marks"]['eng']['term1'].get("mgt1_ENG", "")
            self.agt1_ENG.text = dict[self.NM.text]["marks"]['eng']['term1'].get("agt1_ENG", "")
            self.mgt2_ENG.text = dict[self.NM.text]["marks"]['eng']['term2'].get("mgt2_ENG", "")
            self.agt2_ENG.text = dict[self.NM.text]["marks"]['eng']['term2'].get("agt2_ENG", "")
            self.REM1_ENG.text = dict[self.NM.text]["marks"]['eng']['term2'].get("REM1_ENG", "")
            self.INIT1_ENG.text = dict[self.NM.text]["marks"]['eng']['term2'].get("INIT1_ENG", "")
            # _SST
            self.mgt1_SST.text = dict[self.NM.text]["marks"]['sst']['term1'].get("mgt1_SST", "")
            self.agt1_SST.text = dict[self.NM.text]["marks"]['sst']['term1'].get("agt1_SST", "")
            self.mgt2_SST.text = dict[self.NM.text]["marks"]['sst']['term2'].get("mgt2_SST", "")
            self.agt2_SST.text = dict[self.NM.text]["marks"]['sst']['term2'].get("agt2_SST", "")
            self.REM1_SST.text = dict[self.NM.text]["marks"]['sst']['term2'].get("REM1_SST", "")
            self.INIT1_SST.text = dict[self.NM.text]["marks"]['sst']['term2'].get("INIT1_SST", "")
            # _SCIE
            self.mgt1_SCIE.text = dict[self.NM.text]["marks"]['scie']['term1'].get("mgt1_SCIE", "")
            self.agt1_SCIE.text = dict[self.NM.text]["marks"]['scie']['term1'].get("agt1_SCIE", "")
            self.mgt2_SCIE.text = dict[self.NM.text]["marks"]['scie']['term2'].get("mgt2_SCIE", "")
            self.agt2_SCIE.text = dict[self.NM.text]["marks"]['scie']['term2'].get("agt2_SCIE", "")
            self.REM1_SCIE.text = dict[self.NM.text]["marks"]['scie']['term2'].get("REM1_SCIE", "")
            self.INIT1_SCIE.text = dict[self.NM.text]["marks"]['scie']['term2'].get("INIT1_SCIE", "")
            # TOTAL
            self.mgt1_TT.text = dict[self.NM.text]["marks"]['total']['term1'].get("mgt1_TT", "")
            self.agt1_TT.text = dict[self.NM.text]["marks"]['total']['term1'].get("agt1_TT", "")
            self.mgt2_TT.text = dict[self.NM.text]["marks"]['total']['term2'].get("mgt2_TT", "")
            self.agt2_TT.text = dict[self.NM.text]["marks"]['total']['term2'].get("agt2_TT", "")
            self.REM1_TT.text = dict[self.NM.text]["marks"]['total']['term2'].get("REM1_TT", "")
            self.INIT1_TT.text = dict[self.NM.text]["marks"]['total']['term2'].get("INIT1_TT", "")
            # ttttttttttttttttttttttttttttttttttt
            if self.mgt1.text == "":
                self.mgt1.text = "0"
            if self.mgt1_ENG.text == "":
                self.mgt1_ENG.text = "0"
            if self.mgt1_SST.text == "":
                self.mgt1_SST.text = "0"
            if self.mgt1_SCIE.text == "":
                self.mgt1_SCIE.text = "0"
            self.mgt1_TT.text = str(
                float(self.mgt1.text) + float(self.mgt1_ENG.text) + float(self.mgt1_SST.text) + float(
                    self.mgt1_SCIE.text))

            self.REM1.text = remarks(int(self.mgt2.text))
            self.REM1_ENG.text = remarks(int(self.mgt2_ENG.text))
            self.REM1_SST.text = remarks(int(self.mgt2_SST.text))
            self.REM1_SCIE.text = remarks(int(self.mgt2_SCIE.text))
            #
            V = [self.INIT1, self.INIT1_ENG, self.INIT1_SST, self.INIT1_SCIE]
            S = ['mtc', 'eng', 'sst', 'scie']
            cnt = 0
            for i in V:
                tm=self.r_teach(S[cnt], self.CL.text).split()
                i_n=""
                for ini in tm :
                    i_n+=ini[0].upper()+"  .  "
                i.text = i_n
                cnt +=1
            ##################################################################################################################################
            marks=dict[self.NM.text]['marks']['total']['term' + self.Called]['mgt' + self.Called + '_TT']
            if self.Called=="2" :
                tot=self.fmt2_TT.text
            else:
                tot = self.fmt1_TT.text
            PRC.text= "     AVERAGE PERCENTAGE :  " + str(float(marks)*100/int(tot))+" %"
            if float(marks)*100/int(tot) < 50 :
                NEXT.text="RETRY"
            else:
                NEXT.text = "PROMOTED TO NEXT LEVEL"
            if dict[self.NM.text]['$']['balance'].startswith("-") :
                self.print_report.unbind(on_release=self.png47)

    def png47(self, x):
        self.BGG.export_to_png(NDR + 'Desktop' + PTH + 'P R I N T A B L E' + PTH + '' + self.NM.text + "_.png")
        self.print_all_i(NDR + 'Desktop' + PTH + 'P R I N T A B L E' + PTH + '' + self.NM.text + "_.png")

        self.remove_widget(self.BGSV)
        Clock.schedule_once(self.p4p7)
        return

    def sv_p47(self, y, tx):
        try:
            int(tx)
        except:
            return

        TDAT = open(DIR + 'media' + PTH + '0' + PTH + ANGELS + PTH + '' + self.CL.text + '.json', 'r')
        DT = json.load(TDAT)
        TDAT.close()

        # ttttttttttttttttttttttttttttttttttt
        if self.mgt1.text == "":
            self.mgt1.text = "0"
        if self.mgt1_ENG.text == "":
            self.mgt1_ENG.text = "0"
        if self.mgt1_SST.text == "":
            self.mgt1_SST.text = "0"
        if self.mgt1_SCIE.text == "":
            self.mgt1_SCIE.text = "0"
        self.mgt1_TT.text = str(float(self.mgt1.text) + float(self.mgt1_ENG.text) + float(self.mgt1_SST.text) + float(
            self.mgt1_SCIE.text))
        if self.mgt2.text == "":
            self.mgt2.text = "0"
        if self.mgt2_ENG.text == "":
            self.mgt2_ENG.text = "0"
        if self.mgt2_SST.text == "":
            self.mgt2_SST.text = "0"
        if self.mgt2_SCIE.text == "":
            self.mgt2_SCIE.text = "0"
        self.mgt2_TT.text = str(float(self.mgt2.text) + float(self.mgt2_ENG.text) + float(self.mgt2_SST.text) + float(
            self.mgt2_SCIE.text))
        #
        # REM!
        self.REM1.text = remarks(int(self.mgt2.text))
        self.REM1_ENG.text = remarks(int(self.mgt2_ENG.text))
        self.REM1_SST.text = remarks(int(self.mgt2_SST.text))
        self.REM1_SCIE.text = remarks(int(self.mgt2_SCIE.text))

        # ttttttttttttttttttttttttttttttttttt
        self.agt1.text = AGG(int(self.mgt1.text))
        self.agt1_ENG.text = AGG(int(self.mgt1_ENG.text))
        self.agt1_SST.text = AGG(int(self.mgt1_SST.text))
        self.agt1_SCIE.text = AGG(int(self.mgt1_SCIE.text))
        self.agt1_TT.text = str(
            int(self.agt1.text[1:]) + int(self.agt1_ENG.text[1:]) + int(self.agt1_SST.text[1:]) + int(
                self.agt1_SCIE.text[1:]))

        self.agt2.text = AGG(int(self.mgt2.text))
        self.agt2_ENG.text = AGG(int(self.mgt2_ENG.text))
        self.agt2_SST.text = AGG(int(self.mgt2_SST.text))
        self.agt2_SCIE.text = AGG(int(self.mgt2_SCIE.text))
        self.agt2_TT.text = str(
            int(self.agt2.text[1:]) + int(self.agt2_ENG.text[1:]) + int(self.agt2_SST.text[1:]) + int(
                self.agt2_SCIE.text[1:]))
        # ********************************************************
        if not DT[self.NM.text].get('marks', 0):
            DT[self.NM.text]['marks'] = {}
        # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

        if not DT[self.NM.text]['marks'].get('mtc', 0):
            DT[self.NM.text]['marks']['mtc'] = {}
        if not DT[self.NM.text]['marks']['mtc'].get('term1', 0):
            DT[self.NM.text]['marks']['mtc']['term1'] = {}
        DT[self.NM.text]['marks']['mtc']['term1'] = {'mgt1': self.mgt1.text,  #
                                                     'agt1': self.agt1.text}

        if not DT[self.NM.text]['marks']['mtc'].get('term2', 0):
            DT[self.NM.text]['marks']['mtc']['term2'] = {}
        DT[self.NM.text]['marks']['mtc']['term2'] = {'mgt2': self.mgt2.text,
                                                     'agt2': self.agt2.text,
                                                     'REM1': self.REM1.text,
                                                     'INIT1': self.INIT1.text
                                                     }

        #                      ENG                                  #

        if not DT[self.NM.text]['marks'].get('eng', 0):
            DT[self.NM.text]['marks']['eng'] = {}
        if not DT[self.NM.text]['marks']['eng'].get('term1', 0):
            DT[self.NM.text]['marks']['eng']['term1'] = {}
        DT[self.NM.text]['marks']['eng']['term1'] = {'mgt1_ENG': self.mgt1_ENG.text,  #
                                                     'agt1_ENG': self.agt1_ENG.text}

        if not DT[self.NM.text]['marks']['eng'].get('term2', 0):
            DT[self.NM.text]['marks']['eng']['term2'] = {}
        DT[self.NM.text]['marks']['eng']['term2'] = {'mgt2_ENG': self.mgt2_ENG.text,
                                                     'agt2_ENG': self.agt2_ENG.text,
                                                     'REM1_ENG': self.REM1_ENG.text,
                                                     'INIT1_ENG': self.INIT1_ENG.text
                                                     }

        ###################      SST      ###################################
        if not DT[self.NM.text]['marks'].get('sst', 0):
            DT[self.NM.text]['marks']['sst'] = {}
        if not DT[self.NM.text]['marks']['sst'].get('term1', 0):
            DT[self.NM.text]['marks']['sst']['term1'] = {}
        DT[self.NM.text]['marks']['sst']['term1'] = {'mgt1_SST': self.mgt1_SST.text,  #
                                                     'agt1_SST': self.agt1_SST.text}

        if not DT[self.NM.text]['marks']['sst'].get('term2', 0):
            DT[self.NM.text]['marks']['sst']['term2'] = {}
        DT[self.NM.text]['marks']['sst']['term2'] = {'mgt2_SST': self.mgt2_SST.text,
                                                     'agt2_SST': self.agt2_SST.text,
                                                     'REM1_SST': self.REM1_SST.text,
                                                     'INIT1_SST': self.INIT1_SST.text
                                                     }
        #################        _SCIE          ########################

        if not DT[self.NM.text]['marks'].get('scie', 0):
            DT[self.NM.text]['marks']['scie'] = {}
        if not DT[self.NM.text]['marks']['scie'].get('term1', 0):
            DT[self.NM.text]['marks']['scie']['term1'] = {}
        DT[self.NM.text]['marks']['scie']['term1'] = {'mgt1_SCIE': self.mgt1_SCIE.text,  #
                                                      'agt1_SCIE': self.agt1_SCIE.text}

        if not DT[self.NM.text]['marks']['scie'].get('term2', 0):
            DT[self.NM.text]['marks']['scie']['term2'] = {}
        DT[self.NM.text]['marks']['scie']['term2'] = {'mgt2_SCIE': self.mgt2_SCIE.text,
                                                      'agt2_SCIE': self.agt2_SCIE.text,
                                                      'REM1_SCIE': self.REM1_SCIE.text,
                                                      'INIT1_SCIE': self.INIT1_SCIE.text
                                                      }
        ################        TOTAL          ############################

        if not DT[self.NM.text]['marks'].get('total', 0):
            DT[self.NM.text]['marks']['total'] = {}
        if not DT[self.NM.text]['marks']['total'].get('term1', 0):
            DT[self.NM.text]['marks']['total']['term1'] = {}
        DT[self.NM.text]['marks']['total']['term1'] = {'mgt1_TT': self.mgt1_TT.text,
                                                       'agt1_TT': self.agt1_TT.text}

        if not DT[self.NM.text]['marks']['total'].get('term2', 0):
            DT[self.NM.text]['marks']['total']['term2'] = {}
        DT[self.NM.text]['marks']['total']['term2'] = {'mgt2_TT': self.mgt2_TT.text,
                                                       'agt2_TT': self.agt2_TT.text,
                                                       'REM1_TT': self.REM1_TT.text,
                                                       'INIT1_TT': self.INIT1_TT.text
                                                       }

        #
        file = open(DIR + 'media' + PTH + '0' + PTH + ANGELS + PTH + '' + self.CL.text + '.json', 'w')
        json.dump(DT, file)
        file.close()

    def p1p3(self, x):
        self.roll = 1
        Window.bind(on_keyboard=self.RPupdown)

        try:
            self.remove_widget(self.print_report)
        except:
            pass
        self.print_report = Button(text='PRINT', size_hint=(.2, .06), pos_hint={'center_x': .90, 'center_y': .78},
                                   on_release=self.png13)
        self.add_widget(self.print_report)
        # self.print_report.bind()

        file = open(DIR + 'media' + PTH + '0' + PTH + ANGELS + PTH + '' + self.CL.text + ".json", 'r')
        dict = json.load(file)
        file.close()
        self.BGSV = ScrollView(size_hint=(1., .635), pos_hint={'center_x': .5, 'center_y': .4}, do_scroll_x=False,
                               do_scroll_y=True, scroll_timeout=55, scroll_distance=20, scroll_type=['bars', 'content'],
                               bar_width=10, bar_color=(1, 1, 0, 1), bar_margin=0)
        self.BGG = GridLayout(cols=1, spacing=1, padding=0, size_hint=(None, None), size=(780, 1194),  # SCREENSHOOT
                              pos_hint={'center_x': .5, 'center_y': .4})
        with self.BGG.canvas.after:
            Color(1, 0, .7, 1)
            r1ec = Rectangle(pos=(0, 1), size=(10, self.height * 2 - 80))
            r2ec = Rectangle(pos=(0, self.height * 2 - 80), size=(780, 10))
            r3ec = Rectangle(pos=(770, 1), size=(10, self.height * 2 - 80))
            r4ec = Rectangle(pos=(0, 1), size=(780, 10))

        self.printable = GridLayout(cols=1, spacing=1, padding=0, size_hint=(1., None), size=(780, 350),  # SCREENSHOOT
                                    pos_hint={'center_x': .5, 'center_y': .5}, row_default_height=90,
                                    row_force_default=True)
        self.printable.add_widget(
            Label(text=" " * 161, color=(0, 0, 1, 1), size_hint=(1., None), size=(780, 40), italic=True))
        # self.printable.add_widget(Label(text=" " * 161, color=(0, 0, 1, 1), italic=True))

        self.num1 = BoxLayout(spacing=0, padding=0, size_hint=(1., None), size=(780, 142))
        # ___________________________

        im = AsyncImage(source=ASY + 'L.png', size_hint=(None, None), size=(200, 140), allow_stretch=True)
        self.num1.add_widget(im)
        self.gnum1 = GridLayout(cols=1, size_hint=(None, None), size=(380, 140), row_default_height=27,
                                row_force_default=True)
        # _______________________________

        pickl = open(DIR + 'media' + PTH + '0' + PTH + 'SCHOOL.bin', 'rb')
        ids = pickle.load(pickl)
        pickl.close()

        # self.gnum1.add_widget(Label(text=' '))
        self.gnum1.add_widget(Label(text='   ' + ids['1'] + '               ', color=(0, 0, 1, 1), font_size=20))
        self.gnum1.add_widget(Label(text='       ' + ids['2'] + '               ', color=(0, 0, 0, 1)))
        self.gnum1.add_widget(Label(text='   ' + ids['3'] + '               ', color=(0, 1, 0, 1)))
        self.gnum1.add_widget(Label(text='       ' + ids['4'] + '               ', color=(0, 0, 0, 1)))
        self.gnum1.add_widget(Label(text='     ' + ids['5'] + '               ', color=(1, 0, 0, 1), font_size=20))
        self.gnum1.add_widget(Label(text=' ' * 15 + '-' * 100 + ' ' * 20, underline=True, color=(1, 0, 0, 1)))

        self.num1.add_widget(self.gnum1)
        sim = AsyncImage(source=ASY + self.NM.text + '.png', size_hint=(None, None), size=(200, 140),
                         allow_stretch=True)
        self.num1.add_widget(sim)

        self.gnum2 = GridLayout(cols=8, padding=1, spacing=1, size_hint=(1., None), size=(780, 40))
        self.gnum2.add_widget(TextInput(text='   Name :  ' + self.NM.text.capitalize(), background_normal="rb2.png",
                                        background_active="rb2.png", foreground_color=(1, 1, .7, 1),
                                        background_color=(.4, 0, .7, 1),
                                        size_hint=(None, None), size=(300, 40)))
        # self.gnum2.add_widget(TextInput(text=self.NM.text.capitalize(), color=(0, 0, 1, 1), italic=True))
        self.gnum2.add_widget(TextInput(text='Sex :  ' + dict[self.NM.text]['Sex'], background_normal="rb2.png",
                                        background_active="rb2.png", foreground_color=(1, 1, .7, 1),
                                        background_color=(.4, 0, .7, 1)))
        # self.gnum2.add_widget(TextInput(text=dict[self.NM.text]['Sex'], color=(0, 0, 1, 1), italic=True))
        self.gnum2.add_widget(TextInput(text='Class :  ' + self.CL.text, background_normal="rb2.png",
                                        background_active="rb2.png", foreground_color=(1, 1, .7, 1),
                                        background_color=(.4, 0, .7, 1)))

        self.gnum2.add_widget(TextInput(text=self.TERM.text, background_normal="rb2.png",
                                        background_active="rb2.png", foreground_color=(1, 1, .7, 1),
                                        background_color=(.4, 0, .7, 1)))

        # self.gnum2.add_widget(TextInput(text=self.CL.text, color=(0, 0, 1, 1), italic=True))

        # self.term = Label(text='', color=(0, 0, 1, 1), italic=True)
        # if time.strftime("%m") in ('01','02', '03', '04'):
        #     self.gnum2.add_widget(TextInput(text='Term :  I', background_normal="rb2.png",
        #                                 background_active="rb2.png",foreground_color=(1, 1, .7, 1),background_color=(.4, 0, .7, 1)))
        # if time.strftime("%m") in ('05', '06', '07'):
        #     self.gnum2.add_widget(TextInput(text='Term :  II', background_normal="rb2.png",
        #                                 background_active="rb2.png",foreground_color=(1, 1, .7, 1),background_color=(.4, 0, .7, 1)))
        # if time.strftime("%m") in ('08', '09', '10', '11'):
        #     self.gnum2.add_widget(TextInput(text='Term :  III', background_normal="rb2.png",
        #                                 background_active="rb2.png",foreground_color=(1, 1, .7, 1),background_color=(.4, 0, .7, 1)))

        self.printable.add_widget(self.num1)
        self.line = GridLayout(cols=1, size_hint=(1., .01), row_default_height=10,
                               row_force_default=True)
        self.line.add_widget(Label(text=' ' * 20 + '-' * 100 + ' ' * 20, underline=True, color=(0, 0, 0, 1)))
        # self.printable.add_widget(self.line)
        self.printable.add_widget(self.gnum2)

        self.gnum3 = GridLayout(cols=3, padding=1, spacing=1, row_default_height=40,
                                row_force_default=True)  # , row_default_height=6, row_force_default=True
        # ////////////////////////////////////////////

        l = []
        for x in dict.keys():
            if not dict[x].get('marks'):
                # del (dict[x])
                grade = ""
            else:

                # if dict[x]['marks']['mtc']['term1']['mgt1'] == '':
                #     dict[x]['marks']['mtc']['term1']['mgt1'] = "0"
                if dict[x]['marks']['total']['term' + self.Called]['mgt' + self.Called + '_TT'] == '':
                    dict[x]['marks']['total']['term' + self.Called]['mgt' + self.Called + '_TT'] = "0"

                num = dict[x]['marks']['total']['term' + self.Called]['mgt' + self.Called + '_TT']
                if '.' in num:
                    if int(num[-1]) >= 5:
                        num = str(float(num[:num.index('.')]) + 1)

                    if int(num[-1]) < 5:
                        num = str(float(num[:num.index('.')]))

                    NM = num[:num.index('.')]

                else:
                    NM = num

                if len(NM) == 1:
                    NM = "0000" + NM
                if len(NM) == 2:
                    NM = "000" + NM
                if len(NM) == 3:
                    NM = "00" + NM
                if len(NM) == 4:
                    NM = "0" + NM

                l.append(NM + "_" + x)

        l.sort()
        v = list(reversed(l))

        for nam in v:
            if self.NM.text in nam:
                grade = v.index(nam) + 1

        self.gnum3.add_widget(
            TextInput(text='         End of term Position : ' + str(grade), background_normal="rb2.png",
                      background_active="rb2.png", foreground_color=(1, 1, .7, 1), background_color=(.4, 0, .7, 1),size_hint=(None, None), size=(250, 40)))
        # self.gnum3.add_widget(TextInput(text="DIV II", background_normal="rb2.png",
        #                                 background_active="rb2.png",foreground_color=(1, 1, .7, 1),background_color=(.4, 0, .7, 1), size_hint=(1., .01)))
        self.gnum3.add_widget(
            TextInput(text='Out of : ' + str(len(dict.keys())) + " Pupils", background_normal="rb2.png",
                      background_active="rb2.png", foreground_color=(1, 1, .7, 1), background_color=(.4, 0, .7, 1),size_hint=(None, None), size=(200, 40)))
        # self.gnum3.add_widget(TextInput(text=str(len(dict.keys())) + " Pupils", background_normal="rb2.png",
        #                                 background_active="rb2.png",foreground_color=(1, 1, .7, 1),background_color=(.4, 0, .7, 1), size_hint=(1., .01)))
        self.gnum3.add_widget(TextInput(text='Date : ' + time.strftime('%d %B %y'), background_normal="rb2.png",
                                        background_active="rb2.png", foreground_color=(1, 1, .7, 1),
                                        background_color=(.4, 0, .7, 1)))

        PRC = TextInput(hint_text="     AVERAGE PERCENTAGE :  ", readonly=True, foreground_color=(1, 1, 1, 1),
                        background_color=(0, 0, 0, .4), size_hint=(None, None), size=(300, 30))
        self.gnum3.add_widget(PRC)
        NEXT = TextInput(hint_text="", readonly=True, foreground_color=(1, 1, 1, 1), background_color=(0, 0, 0, .4),
                         size_hint=(None, None), size=(270, 30))
        self.gnum3.add_widget(NEXT)

        self.printable.add_widget(self.gnum3)
        # *

        self.BIG13 = GridLayout(cols=5, size_hint=(1., None), size=(780, 480), pos_hint={'center_x': .5, 'center_y': .6},
                              row_default_height=30,
                              row_force_default=True)

        self.BIG13.add_widget(TextInput(text='     SUBJECT', readonly=True, size_hint=(.2, .09)))
        self.BIG13.add_widget(TextInput(text='MID TERM', readonly=True, size_hint=(.2, .09)))
        self.BIG13.add_widget(TextInput(text='END OF TERM', readonly=True, size_hint=(.2, .09)))
        self.BIG13.add_widget(TextInput(text='REMARKS', readonly=True, size_hint=(.2, .09)))
        self.BIG13.add_widget(TextInput(text='INITIALS', readonly=True, size_hint=(.2, .09)))

        # self.gggg.add_widget(Label(text='', color=(0, 0, 0, 1)))
        self.BIG13.add_widget(
            TextInput(text='/////////////////////////////////////////////', multiline=False, font_size=35,
                      background_color=(1, 1, 0, 1), readonly=True))

        self.gt1 = GridLayout(cols=2, size_hint_y=.09, row_default_height=30,
                              row_force_default=True)

        self.gt1.add_widget(TextInput(text='MAX',font_size=15, readonly=True))
        self.gt1.add_widget(TextInput(text='Marks',font_size=15, readonly=True))
        # self.gt1.add_widget(TextInput(text='Agg', readonly=True))
        self.BIG13.add_widget(self.gt1)

        self.gt2 = GridLayout(cols=2, size_hint_y=.09, row_default_height=30,
                              row_force_default=True)

        self.gt2.add_widget(TextInput(text='MAX',font_size=15, readonly=True))
        self.gt2.add_widget(TextInput(text='Marks', font_size=15,readonly=True))
        # self.gt2.add_widget(TextInput(text='Agg', readonly=True))
        self.BIG13.add_widget(self.gt2)

        self.BIG13.add_widget(TextInput(text='////////////////////////////////', multiline=False, font_size=35,
                                        background_color=(1, 1, 0, 1), readonly=True))
        self.BIG13.add_widget(TextInput(text='////////////////////////////////', multiline=False, font_size=35,
                                        background_color=(1, 1, 0, 1), readonly=True))
        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        self.MTC = TextInput(text='    MTC', readonly=True)
        self.BIG13.add_widget(self.MTC)
        self.fmt1 = TextInput(text='100', background_color=(1, 1, 0, 1), readonly=True)
        self.gt1.add_widget(self.fmt1)
        self.mgt1 = TextInput(multiline=False)
        self.mgt1.bind(text=self.sv_p13)
        self.gt1.add_widget(self.mgt1)
        # self.agt1 = TextInput(multiline=False)
        # self.agt1.bind(text=self.sv_p13)
        # self.gt1.add_widget(self.agt1)

        self.fmt2 = TextInput(text='100', background_color=(1, 1, 0, 1), readonly=True)
        self.gt2.add_widget(self.fmt2)
        self.mgt2 = TextInput(multiline=False)
        self.mgt2.bind(text=self.sv_p13)
        self.gt2.add_widget(self.mgt2)
        self.agt2 = TextInput(multiline=False)

        # self.gt2.add_widget(self.agt2)
        self.BIG13.add_widget(Label(text=""))
        self.BIG13.add_widget(Label(text=""))
        self.REM1 = TextInput(foreground_color=(1, 0, 0, 1), allow_copy=True)
        self.REM1.bind(text=self.sv_p13)
        self.BIG13.add_widget(self.REM1)
        self.INIT1 = TextInput(multiline=False)
        self.INIT1.bind(text=self.sv_p13)
        self.BIG13.add_widget(self.INIT1)

        #               ENG             #

        self.ENG = TextInput(text='    ENG', readonly=True)
        self.BIG13.add_widget(self.ENG)
        self.fmt1_ENG = TextInput(text='100', background_color=(1, 1, 0, 1), readonly=True)
        self.gt1.add_widget(self.fmt1_ENG)
        self.mgt1_ENG = TextInput(multiline=False)
        self.mgt1_ENG.bind(text=self.sv_p13)
        self.gt1.add_widget(self.mgt1_ENG)

        self.fmt2_ENG = TextInput(text='100', background_color=(1, 1, 0, 1), readonly=True)
        self.gt2.add_widget(self.fmt2_ENG)
        self.mgt2_ENG = TextInput(multiline=False)
        self.mgt2_ENG.bind(text=self.sv_p13)
        self.gt2.add_widget(self.mgt2_ENG)

        self.BIG13.add_widget(Label(text=""))
        self.BIG13.add_widget(Label(text=""))
        self.REM1_ENG = TextInput(foreground_color=(1, 0, 0, 1), allow_copy=True)
        self.REM1_ENG.bind(text=self.sv_p13)
        self.BIG13.add_widget(self.REM1_ENG)
        self.INIT1_ENG = TextInput(multiline=False)
        self.INIT1_ENG.bind(text=self.sv_p13)
        self.BIG13.add_widget(self.INIT1_ENG)

        #                 _LIT                #

        self.LITI = TextInput(text='    LITI', readonly=True)
        self.BIG13.add_widget(self.LITI)
        self.fmt1_LITI = TextInput(text='100', background_color=(1, 1, 0, 1), readonly=True)
        self.gt1.add_widget(self.fmt1_LITI)
        self.mgt1_LITI = TextInput(multiline=False)
        self.mgt1_LITI.bind(text=self.sv_p13)
        self.gt1.add_widget(self.mgt1_LITI)

        self.fmt2_LITI = TextInput(text='100', background_color=(1, 1, 0, 1), readonly=True)
        self.gt2.add_widget(self.fmt2_LITI)
        self.mgt2_LITI = TextInput(multiline=False)
        self.mgt2_LITI.bind(text=self.sv_p13)
        self.gt2.add_widget(self.mgt2_LITI)

        self.BIG13.add_widget(Label(text=""))
        self.BIG13.add_widget(Label(text=""))
        self.REM1_LITI = TextInput(foreground_color=(1, 0, 0, 1), allow_copy=True)
        self.REM1_LITI.bind(text=self.sv_p13)
        self.BIG13.add_widget(self.REM1_LITI)
        self.INIT1_LITI = TextInput(multiline=False)
        self.INIT1_LITI.bind(text=self.sv_p13)
        self.BIG13.add_widget(self.INIT1_LITI)

        #        _LITII                 #

        self.LITII = TextInput(text='    LITII', readonly=True)
        self.BIG13.add_widget(self.LITII)
        self.fmt1_LITII = TextInput(text='100', background_color=(1, 1, 0, 1), readonly=True)
        self.gt1.add_widget(self.fmt1_LITII)
        self.mgt1_LITII = TextInput(multiline=False)
        self.mgt1_LITII.bind(text=self.sv_p13)
        self.gt1.add_widget(self.mgt1_LITII)

        self.fmt2_LITII = TextInput(text='100', background_color=(1, 1, 0, 1), readonly=True)
        self.gt2.add_widget(self.fmt2_LITII)
        self.mgt2_LITII = TextInput(multiline=False)
        self.mgt2_LITII.bind(text=self.sv_p13)
        self.gt2.add_widget(self.mgt2_LITII)

        self.BIG13.add_widget(Label(text=""))
        self.BIG13.add_widget(Label(text=""))
        self.REM1_LITII = TextInput(foreground_color=(1, 0, 0, 1), allow_copy=True)
        self.REM1_LITII.bind(text=self.sv_p13)
        self.BIG13.add_widget(self.REM1_LITII)
        self.INIT1_LITII = TextInput(multiline=False)
        self.INIT1_LITII.bind(text=self.sv_p13)
        self.BIG13.add_widget(self.INIT1_LITII)

        #          _READING

        self.READ = TextInput(text='    READING', readonly=True)
        self.BIG13.add_widget(self.READ)
        self.fmt1_READ = TextInput(text='100', background_color=(1, 1, 0, 1), readonly=True)
        self.gt1.add_widget(self.fmt1_READ)
        self.mgt1_READ = TextInput(multiline=False)
        self.mgt1_READ.bind(text=self.sv_p13)
        self.gt1.add_widget(self.mgt1_READ)

        self.fmt2_READ = TextInput(text='100', background_color=(1, 1, 0, 1), readonly=True)
        self.gt2.add_widget(self.fmt2_READ)
        self.mgt2_READ = TextInput(multiline=False)
        self.mgt2_READ.bind(text=self.sv_p13)
        self.gt2.add_widget(self.mgt2_READ)
        self.agt2_READ = TextInput(multiline=False)
        # self.gt2.add_widget(self.agt2_READ)
        self.BIG13.add_widget(Label(text=""))
        self.BIG13.add_widget(Label(text=""))
        self.REM1_READ = TextInput(foreground_color=(1, 0, 0, 1), allow_copy=True)
        self.REM1_READ.bind(text=self.sv_p13)
        self.BIG13.add_widget(self.REM1_READ)
        self.INIT1_READ = TextInput(multiline=False)
        self.INIT1_READ.bind(text=self.sv_p13)
        self.BIG13.add_widget(self.INIT1_READ)

        #            RE                 #

        self.RE = TextInput(text='    RE', readonly=True)
        self.BIG13.add_widget(self.RE)
        self.fmt1_RE = TextInput(text='100', background_color=(1, 1, 0, 1), readonly=True)
        self.gt1.add_widget(self.fmt1_RE)
        self.mgt1_RE = TextInput(multiline=False)
        self.mgt1_RE.bind(text=self.sv_p13)
        self.gt1.add_widget(self.mgt1_RE)
        self.agt1_RE = TextInput(multiline=False)
        # self.gt1.add_widget(self.agt1_RE)

        self.fmt2_RE = TextInput(text='100', background_color=(1, 1, 0, 1), readonly=True)
        self.gt2.add_widget(self.fmt2_RE)
        self.mgt2_RE = TextInput(multiline=False)
        self.mgt2_RE.bind(text=self.sv_p13)
        self.gt2.add_widget(self.mgt2_RE)
        self.agt2_RE = TextInput(multiline=False)
        # self.gt2.add_widget(self.agt2_RE)
        self.BIG13.add_widget(Label(text=""))
        self.BIG13.add_widget(Label(text=""))
        self.REM1_RE = TextInput(foreground_color=(1, 0, 0, 1), allow_copy=True)
        self.REM1_RE.bind(text=self.sv_p13)
        self.BIG13.add_widget(self.REM1_RE)
        self.INIT1_RE = TextInput(multiline=False)
        self.INIT1_RE.bind(text=self.sv_p13)
        self.BIG13.add_widget(self.INIT1_RE)

        #            _TT           #

        self.TOTT = TextInput(text='    TOTAL', readonly=True)
        self.BIG13.add_widget(self.TOTT)
        self.fmt1_TT = TextInput(text='600', background_color=(1, .6, 0, 1), readonly=True)
        self.gt1.add_widget(self.fmt1_TT)
        self.mgt1_TT = TextInput(multiline=False, background_color=(0, 0, 0, 1), foreground_color=(1, 1, 1, 1))
        self.mgt1_TT.bind(text=self.sv_p13)
        self.gt1.add_widget(self.mgt1_TT)
        self.agt1_TT = TextInput(multiline=False)
        # self.gt1.add_widget(self.agt1_TT)

        self.fmt2_TT = TextInput(text='600', background_color=(1, .6, 0, 1), readonly=True)
        self.gt2.add_widget(self.fmt2_TT)
        self.mgt2_TT = TextInput(multiline=False, background_color=(0, 0, 0, 1), foreground_color=(1, 1, 1, 1))
        self.mgt2_TT.bind(text=self.sv_p13)
        self.gt2.add_widget(self.mgt2_TT)
        # self.agt2_TT = TextInput(multiline=False)
        # self.gt2.add_widget(self.agt2_TT)
        self.BIG13.add_widget(Label(text=""))
        self.BIG13.add_widget(Label(text=""))
        self.REM1_TT = TextInput(hint_text=' /////////////////////////////////', multiline=False, font_size=35,
                                 background_color=(.6, 1, 0, 1), foreground_color=(1, 0, 0, 1))
        self.REM1_TT.bind(text=self.sv_p13)
        self.BIG13.add_widget(self.REM1_TT)
        self.INIT1_TT = TextInput(hint_text=' /////////////////////////////////', multiline=False, font_size=35,
                                  background_color=(.6, 1, 0, 1), foreground_color=(1, 0, 0, 1))
        self.INIT1_TT.bind(text=self.sv_p13)
        self.BIG13.add_widget(self.INIT1_TT)

        self.BGG.add_widget(self.printable)

        self.BGG.add_widget(self.BIG13)

        self.p2 = GridLayout(cols=2, spacing=60, padding=0, size_hint=(1., None), size=(780, 564),
                             row_default_height=70,
                             row_force_default=True)  # pos_hint={'center_x': .5, 'center_y': .5},
        with self.p2.canvas.before:
            Color(1, 0, .7, .4)
            rec = Rectangle(source='wp.png', pos=(18, 300), size=(450, 255))  # ,pos=(0, 1)

        self.gnum4 = GridLayout(cols=2, padding=30, spacing=8, size_hint=(1., None), size=(780, 270),
                                row_default_height=30, row_force_default=True,
                                col_default_width=200,
                                col_force_default=True)  # size_hint=(None,None),size=(420,280),pos=(18, 240),

        self.gnum4.add_widget(
            TextInput(text='Conduct :  ', readonly=True, foreground_color=(0, 0, 0, 1), size_hint=(None, None),
                      size=(120, 30)))
        self.behav = Spinner(text=" " + conduct()[0], values=tuple(conduct()), color=(1, 1, 0, 1),
                             background_color=(0, 0, 0, 0),
                             background_normal='btn4.png', size_hint=(.2, None), size=(120, 30))  # size=(400, 30)
        self.gnum4.add_widget(self.behav)

        self.gnum4.add_widget(TextInput(text='Debating :  ', readonly=True, size_hint=(None, None), size=(120, 30),
                                        foreground_color=(0, 0, 0, 1)))
        self.debat = Spinner(text=debat()[0], values=tuple(debat()), color=(1, 1, 0, 1),
                             background_color=(0, 0, 0, 0), background_normal='btn4.png', size_hint=(.2, None),
                             size=(120, 30))
        self.gnum4.add_widget(self.debat)

        self.gnum4.add_widget(TextInput(text='C.T’s comment :  ', readonly=True, size_hint=(None, None), size=(140, 30),
                                        foreground_color=(0, 0, 0, 1)))
        self.gnum4.add_widget(
            Spinner(text=ctcomment()[1], values=tuple(ctcomment()), color=(0, 0, 1, 1), background_color=(0, 0, 0, 0)))

        self.gnum4.add_widget(TextInput(text='H.T’s comment :  ', readonly=True, size_hint=(None, None), size=(140, 30),
                                        foreground_color=(0, 0, 0, 1)))
        self.gnum4.add_widget(
            Spinner(text=hdcomment()[1], values=tuple(hdcomment()), color=(0, 0, 1, 1), background_color=(0, 0, 0, 0)))
        self.gnum4.add_widget(
            TextInput(text='C.T’s signature :.......................................  ', readonly=True,
                      size_hint=(None, None), size=(340, 30), foreground_color=(0, 0, 0, 1)))
        self.gnum4.add_widget(Label(text="*", size_hint=(None, None), size=(20, 30)))
        self.gnum4.add_widget(
            TextInput(text='H.T’s signature :.......................................  ', readonly=True,
                      size_hint=(None, None), size=(340, 30), foreground_color=(0, 0, 0, 1)))

        self.box = GridLayout(cols=1, size_hint=(1., None), size=(780, 270), col_default_width=300,
                              col_force_default=True)  # row_default_height=300, row_force_default=True,
        self.box.add_widget(Label(text='Signature/Seal..................... ', color=(0, 0, 0, 1)))

        self.p2.add_widget(self.gnum4)
        self.p2.add_widget(self.box)

        # self.p2.add_widget(Label(text="", size_hint=(None, None), size=(250, 40)))
        # self.p2.add_widget(Label(text="", size_hint=(None, None), size=(250, 40)))
        self.p2.add_widget(Label(text='       “WE                  WISH YOU THE BEST ! ”', color=(0, 0, 0, 1),
                                 size_hint=(None, None), size=(430, 150),
                                 bold=True, font_size=24))
        self.p2.add_widget(Label(text="", size_hint=(None, None), size=(250, 60)))  #

        self.lst1 = GridLayout(cols=1, size_hint=(.4, None), size=(780, 250),
                               col_force_default=True)  # row_default_height=150, row_force_default=True, col_default_width=300,
        self.p2.add_widget(AsyncImage(source="tm.png", size_hint=(None, None), size=(300, 300)))

        self.lst2 = GridLayout(cols=1, size_hint=(.4, None), size=(
            780, 250))  # row_default_height=150, row_force_default=True,,col_default_width=300, col_force_default=True
        self.p2.add_widget(AsyncImage(source=ASY + 'QR.png', size_hint=(None, None), size=(220, 220)))  # ,
        # self.p2.add_widget(self.lst1)
        # self.p2.add_widget(self.lst2)
        self.BGG.add_widget(self.p2)
        # self.BGG.add_widget(self.llast)
        self.BGSV.add_widget(self.BGG)
        self.add_widget(self.BGSV)

        if dict[self.NM.text].get("marks"):
            self.mgt1.text = dict[self.NM.text]["marks"]['mtc']['term1'].get("mgt1", "")
            # self.agt1.text = dict[self.NM.text]["marks"]['mtc']['term1'].get("agt1", "")
            self.mgt2.text = dict[self.NM.text]["marks"]['mtc']['term2'].get("mgt2", "")
            # self.agt2.text = dict[self.NM.text]["marks"]['mtc']['term2'].get("agt2", "")
            self.REM1.text = dict[self.NM.text]["marks"]['mtc']['term2'].get("REM1", "")
            self.INIT1.text = dict[self.NM.text]["marks"]['mtc']['term2'].get("INIT1", "")
            # ENG
            self.mgt1_ENG.text = dict[self.NM.text]["marks"]['eng']['term1'].get("mgt1_ENG", "")
            # self.agt1_ENG.text = dict[self.NM.text]["marks"]['eng']['term1'].get("agt1_ENG", "")
            self.mgt2_ENG.text = dict[self.NM.text]["marks"]['eng']['term2'].get("mgt2_ENG", "")
            # self.agt2_ENG.text = dict[self.NM.text]["marks"]['eng']['term2'].get("agt2_ENG", "")
            self.REM1_ENG.text = dict[self.NM.text]["marks"]['eng']['term2'].get("REM1_ENG", "")
            self.INIT1_ENG.text = dict[self.NM.text]["marks"]['eng']['term2'].get("INIT1_ENG", "")
            # _LITI
            self.mgt1_LITI.text = dict[self.NM.text]["marks"]['lit']['term1'].get("mgt1_LITI", "")
            # self.agt1_LITI.text = dict[self.NM.text]["marks"]['lit']['term1'].get("agt1_LITI", "")
            self.mgt2_LITI.text = dict[self.NM.text]["marks"]['lit']['term2'].get("mgt2_LITI", "")
            # self.agt2_LITI.text = dict[self.NM.text]["marks"]['lit']['term2'].get("agt2_LITI", "")
            self.REM1_LITI.text = dict[self.NM.text]["marks"]['lit']['term2'].get("REM1_LITI", "")
            self.INIT1_LITI.text = dict[self.NM.text]["marks"]['lit']['term2'].get("INIT1_LITI", "")
            # _LITII
            self.mgt1_LITII.text = dict[self.NM.text]["marks"]['litii']['term1'].get("mgt1_LITII", "")
            # self.agt1_LITII.text = dict[self.NM.text]["marks"]['litii']['term1'].get("agt1_LITII", "")
            self.mgt2_LITII.text = dict[self.NM.text]["marks"]['litii']['term2'].get("mgt2_LITII", "")
            # self.agt2_LITII.text = dict[self.NM.text]["marks"]['litii']['term2'].get("agt2_LITII", "")
            self.REM1_LITII.text = dict[self.NM.text]["marks"]['litii']['term2'].get("REM1_LITII", "")
            self.INIT1_LITII.text = dict[self.NM.text]["marks"]['litii']['term2'].get("INIT1_LITII", "")
            # _READ
            self.mgt1_READ.text = dict[self.NM.text]["marks"]['reading']['term1'].get("mgt1_READ", "")
            # self.agt1_READ.text = dict[self.NM.text]["marks"]['reading']['term1'].get("agt1_READ", "")
            self.mgt2_READ.text = dict[self.NM.text]["marks"]['reading']['term2'].get("mgt2_READ", "")
            # self.agt2_READ.text = dict[self.NM.text]["marks"]['reading']['term2'].get("agt2_READ", "")
            self.REM1_READ.text = dict[self.NM.text]["marks"]['reading']['term2'].get("REM1_READ", "")
            self.INIT1_READ.text = dict[self.NM.text]["marks"]['reading']['term2'].get("INIT1_READ", "")
            # _RE
            self.mgt1_RE.text = dict[self.NM.text]["marks"]['re']['term1'].get("mgt1_RE", "")
            # self.agt1_RE.text = dict[self.NM.text]["marks"]['re']['term1'].get("agt1_RE", "")
            self.mgt2_RE.text = dict[self.NM.text]["marks"]['re']['term2'].get("mgt2_RE", "")
            # self.agt2_RE.text = dict[self.NM.text]["marks"]['re']['term2'].get("agt2_RE", "")
            self.REM1_RE.text = dict[self.NM.text]["marks"]['re']['term2'].get("REM1_RE", "")
            self.INIT1_RE.text = dict[self.NM.text]["marks"]['re']['term2'].get("INIT1_RE", "")
            # _TT
            self.mgt1_TT.text = dict[self.NM.text]["marks"]['total']['term1'].get("mgt1_TT", "")
            # self.agt1_TT.text = dict[self.NM.text]["marks"]['total']['term1'].get("agt1_TT", "")
            self.mgt2_TT.text = dict[self.NM.text]["marks"]['total']['term2'].get("mgt2_TT", "")
            # self.agt2_TT.text = dict[self.NM.text]["marks"]['total']['term2'].get("agt2_TT", "")
            self.REM1_TT.text = dict[self.NM.text]["marks"]['total']['term2'].get("REM1_TT", "")
            self.INIT1_TT.text = dict[self.NM.text]["marks"]['total']['term2'].get("INIT1_TT", "")
            # ttttttttttttttttttttttttttttttttttt
            if self.mgt1.text == "":
                self.mgt1.text = "0"
            if self.mgt1_ENG.text == "":
                self.mgt1_ENG.text = "0"
            if self.mgt1_LITI.text == "":
                self.mgt1_LITI.text = "0"
            if self.mgt1_LITII.text == "":
                self.mgt1_LITII.text = "0"
            if self.mgt1_READ.text == "":
                self.mgt1_READ.text = "0"
            if self.mgt1_RE.text == "":
                self.mgt1_RE.text = "0"
            self.mgt1_TT.text = str(
                float(self.mgt1.text) + float(self.mgt1_ENG.text) + float(self.mgt1_LITI.text) + float(
                    self.mgt1_LITII.text) + float(self.mgt1_READ.text) + float(self.mgt1_RE.text))
            if self.mgt2.text == "":
                self.mgt2.text = "0"
            if self.mgt2_ENG.text == "":
                self.mgt2_ENG.text = "0"
            if self.mgt2_LITI.text == "":
                self.mgt2_LITI.text = "0"
            if self.mgt2_LITII.text == "":
                self.mgt2_LITII.text = "0"
            if self.mgt2_READ.text == "":
                self.mgt2_READ.text = "0"
            if self.mgt2_RE.text == "":
                self.mgt2_RE.text = "0"
            self.mgt2_TT.text = str(
                float(self.mgt2.text) + float(self.mgt2_ENG.text) + float(self.mgt2_LITI.text) + float(
                    self.mgt2_LITII.text) + float(self.mgt2_READ.text) + float(self.mgt2_RE.text))

            self.REM1.text = remarks(int(self.mgt2.text))
            self.REM1_ENG.text = remarks(int(self.mgt2_ENG.text))
            self.REM1_LITI.text = remarks(int(self.mgt2_LITI.text))
            self.REM1_LITII.text = remarks(int(self.mgt2_LITII.text))
            self.REM1_READ.text = remarks(int(self.mgt2_READ.text))
            self.REM1_RE.text = remarks(int(self.mgt2_RE.text))

            #
            V=[self.INIT1,self.INIT1_ENG,self.INIT1_LITI,self.INIT1_LITII,self.INIT1_READ,self.INIT1_RE]
            S=['mtc','eng','lit','lit','reading','re']
            cnt=0
            for i in V :
                tm = self.r_teach(S[cnt], self.CL.text).split()
                i_n = ""
                for ini in tm:
                    i_n += ini[0].upper() + "  .  "
                i.text = i_n
                cnt+=1

            ##################################################################################################################################
            marks = dict[self.NM.text]['marks']['total']['term' + self.Called]['mgt' + self.Called + '_TT']
            if self.Called == "2":
                tot = self.fmt2_TT.text
            else:
                tot = self.fmt1_TT.text
            PRC.text = "     AVERAGE PERCENTAGE :  " + str(float(marks) * 100 / int(tot)) + " %"
            if float(marks) * 100 / int(tot) < 50:
                NEXT.text = "RETRY"
            else:
                NEXT.text = "PROMOTED TO NEXT CLASS"
            if dict[self.NM.text]['$']['balance'].startswith("-"):
                self.print_report.unbind(on_release=self.png13)


    def png13(self, x):
        # self.BGG.export_to_png("./wonder3.png")
        self.BGG.export_to_png(NDR + 'Desktop' + PTH + 'P R I N T A B L E' + PTH + '' + self.NM.text + "_.png")

        self.print_all_i(NDR + 'Desktop' + PTH + 'P R I N T A B L E' + PTH + '' + self.NM.text + "_.png")

        self.remove_widget(self.BGSV)
        Clock.schedule_once(self.p1p3)
        return

    def sv_p13(self, ss, tt):
        try:
            int(tt)
        except:
            return
        TDAT = open(DIR + 'media' + PTH + '0' + PTH + ANGELS + PTH + '' + self.CL.text + '.json', 'r')
        DT = json.load(TDAT)
        TDAT.close()

        # ttttttttttttttttttttttttttttttttttt
        if self.mgt1.text == "":
            self.mgt1.text = "0"
        if self.mgt1_ENG.text == "":
            self.mgt1_ENG.text = "0"
        if self.mgt1_LITI.text == "":
            self.mgt1_LITI.text = "0"
        if self.mgt1_LITII.text == "":
            self.mgt1_LITII.text = "0"
        if self.mgt1_READ.text == "":
            self.mgt1_READ.text = "0"
        if self.mgt1_RE.text == "":
            self.mgt1_RE.text = "0"
        totaL = str(float(self.mgt1.text) + float(self.mgt1_ENG.text) + float(self.mgt1_LITI.text) + float(
            self.mgt1_LITII.text) + float(self.mgt1_READ.text) + float(self.mgt1_RE.text))
        self.mgt1_TT.text = totaL[:totaL.index(".")]
        if self.mgt2.text == "":
            self.mgt2.text = "0"
        if self.mgt2_ENG.text == "":
            self.mgt2_ENG.text = "0"
        if self.mgt2_LITI.text == "":
            self.mgt2_LITI.text = "0"
        if self.mgt2_LITII.text == "":
            self.mgt2_LITII.text = "0"
        if self.mgt2_READ.text == "":
            self.mgt2_READ.text = "0"
        if self.mgt2_RE.text == "":
            self.mgt2_RE.text = "0"
        TTo = str(float(self.mgt2.text) + float(self.mgt2_ENG.text) + float(self.mgt2_LITI.text) + float(
            self.mgt2_LITII.text) + float(self.mgt2_READ.text) + float(self.mgt2_RE.text))
        self.mgt2_TT.text = TTo[:TTo.index(".")]

        self.REM1.text = remarks(int(self.mgt2.text))
        self.REM1_ENG.text = remarks(int(self.mgt2_ENG.text))
        self.REM1_LITI.text = remarks(int(self.mgt2_LITI.text))
        self.REM1_LITII.text = remarks(int(self.mgt2_LITII.text))
        self.REM1_READ.text = remarks(int(self.mgt2_READ.text))
        self.REM1_RE.text = remarks(int(self.mgt2_RE.text))

        if not DT[self.NM.text].get('marks', 0):
            DT[self.NM.text]['marks'] = {}

        # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

        if not DT[self.NM.text]['marks'].get('mtc', 0):
            DT[self.NM.text]['marks']['mtc'] = {}
        if not DT[self.NM.text]['marks']['mtc'].get('term1', 0):
            DT[self.NM.text]['marks']['mtc']['term1'] = {}
        DT[self.NM.text]['marks']['mtc']['term1'] = {'mgt1': self.mgt1.text}

        if not DT[self.NM.text]['marks']['mtc'].get('term2', 0):
            DT[self.NM.text]['marks']['mtc']['term2'] = {}
        DT[self.NM.text]['marks']['mtc']['term2'] = {'mgt2': self.mgt2.text,
                                                     'REM1': self.REM1.text,
                                                     'INIT1': self.INIT1.text
                                                     }

        ###########         _ENG          ####################

        if not DT[self.NM.text]['marks'].get('eng', 0):
            DT[self.NM.text]['marks']['eng'] = {}
        if not DT[self.NM.text]['marks']['eng'].get('term1', 0):
            DT[self.NM.text]['marks']['eng']['term1'] = {}
        DT[self.NM.text]['marks']['eng']['term1'] = {'mgt1_ENG': self.mgt1_ENG.text}

        if not DT[self.NM.text]['marks']['eng'].get('term2', 0):
            DT[self.NM.text]['marks']['eng']['term2'] = {}
        DT[self.NM.text]['marks']['eng']['term2'] = {'mgt2_ENG': self.mgt2_ENG.text,
                                                     'REM1_ENG': self.REM1_ENG.text,
                                                     'INIT1_ENG': self.INIT1_ENG.text
                                                     }

        ##########      _LIT     #######################
        if not DT[self.NM.text]['marks'].get('lit', 0):
            DT[self.NM.text]['marks']['lit'] = {}
        if not DT[self.NM.text]['marks']['lit'].get('term1', 0):
            DT[self.NM.text]['marks']['lit']['term1'] = {}
        DT[self.NM.text]['marks']['lit']['term1'] = {'mgt1_LITI': self.mgt1_LITI.text}

        if not DT[self.NM.text]['marks']['lit'].get('term2', 0):
            DT[self.NM.text]['marks']['lit']['term2'] = {}
        DT[self.NM.text]['marks']['lit']['term2'] = {'mgt2_LITI': self.mgt2_LITI.text,
                                                     'REM1_LITI': self.REM1_LITI.text,
                                                     'INIT1_LITI': self.INIT1_LITI.text}

        #############       _LITII        #################

        if not DT[self.NM.text]['marks'].get('litii', 0):
            DT[self.NM.text]['marks']['litii'] = {}
        if not DT[self.NM.text]['marks']['litii'].get('term1', 0):
            DT[self.NM.text]['marks']['litii']['term1'] = {}
        DT[self.NM.text]['marks']['litii']['term1'] = {'mgt1_LITII': self.mgt1_LITII.text}

        if not DT[self.NM.text]['marks']['litii'].get('term2', 0):
            DT[self.NM.text]['marks']['litii']['term2'] = {}
        DT[self.NM.text]['marks']['litii']['term2'] = {'mgt2_LITII': self.mgt2_LITII.text,
                                                       'REM1_LITII': self.REM1_LITII.text,
                                                       'INIT1_LITII': self.INIT1_LITII.text
                                                       }

        ##########         _READ       ################
        if not DT[self.NM.text]['marks'].get('reading', 0):
            DT[self.NM.text]['marks']['reading'] = {}
        if not DT[self.NM.text]['marks']['reading'].get('term1', 0):
            DT[self.NM.text]['marks']['reading']['term1'] = {}
        DT[self.NM.text]['marks']['reading']['term1'] = {'mgt1_READ': self.mgt1_READ.text}

        if not DT[self.NM.text]['marks']['reading'].get('term2', 0):
            DT[self.NM.text]['marks']['reading']['term2'] = {}
        DT[self.NM.text]['marks']['reading']['term2'] = {'mgt2_READ': self.mgt2_READ.text,
                                                         'REM1_READ': self.REM1_READ.text,
                                                         'INIT1_READ': self.INIT1_READ.text
                                                         }
        ###########      _RE        ################
        if not DT[self.NM.text]['marks'].get('re', 0):
            DT[self.NM.text]['marks']['re'] = {}
        if not DT[self.NM.text]['marks']['re'].get('term1', 0):
            DT[self.NM.text]['marks']['re']['term1'] = {}
        DT[self.NM.text]['marks']['re']['term1'] = {'mgt1_RE': self.mgt1_RE.text}

        if not DT[self.NM.text]['marks']['re'].get('term2', 0):
            DT[self.NM.text]['marks']['re']['term2'] = {}
        DT[self.NM.text]['marks']['re']['term2'] = {'mgt2_RE': self.mgt2_RE.text,
                                                    'REM1_RE': self.REM1_RE.text,
                                                    'INIT1_RE': self.INIT1_RE.text
                                                    }
        ################          TT               ###############

        if not DT[self.NM.text]['marks'].get('total', 0):
            DT[self.NM.text]['marks']['total'] = {}
        if not DT[self.NM.text]['marks']['total'].get('term1', 0):
            DT[self.NM.text]['marks']['total']['term1'] = {}
        DT[self.NM.text]['marks']['total']['term1'] = {'mgt1_TT': self.mgt1_TT.text}

        if not DT[self.NM.text]['marks']['total'].get('term2', 0):
            DT[self.NM.text]['marks']['total']['term2'] = {}
        DT[self.NM.text]['marks']['total']['term2'] = {'mgt2_TT': self.mgt2_TT.text,
                                                       'REM1_TT': self.REM1_TT.text,
                                                       'INIT1_TT': self.INIT1_TT.text
                                                       }

        file = open(DIR + 'media' + PTH + '0' + PTH + ANGELS + PTH + '' + self.CL.text + '.json', 'w')
        json.dump(DT, file)
        file.close()
        print("writen")

    def nasry(self, x):
        self.roll = 1
        Window.bind(on_keyboard=self.RPupdown)
        try:
            self.remove_widget(self.print_report)
        except:
            pass
        self.print_report = Button(text='PRINT', size_hint=(.2, .06), pos_hint={'center_x': .90, 'center_y': .78},
                                   on_release=self.png_nas)
        self.add_widget(self.print_report)
        # self.print_report.bind()

        file = open(DIR + 'media' + PTH + '0' + PTH + ANGELS + PTH + '' + self.CL.text + ".json", 'r')
        dict = json.load(file)
        file.close()
        self.BGSV = ScrollView(size_hint=(1., .58), pos_hint={'center_x': .5, 'center_y': .4}, do_scroll_x=False,
                               do_scroll_y=True, scroll_timeout=55, scroll_distance=20, scroll_type=['bars', 'content'],
                               bar_width=10, bar_color=(1, 1, 0, 1), bar_margin=0)
        self.BGG = GridLayout(cols=1, spacing=1, padding=0, size_hint=(None, None), size=(780, 1164),  # SCREENSHOOT
                              pos_hint={'center_x': .5, 'center_y': .4})
        with self.BGG.canvas.after:
            Color(1, 0, .7, 1)
            r1ec = Rectangle(pos=(0, 1), size=(10, self.height * 2 - 110))
            r2ec = Rectangle(pos=(0, self.height * 2 - 110), size=(780, 10))
            r3ec = Rectangle(pos=(770, 1), size=(10, self.height * 2 - 110))
            r4ec = Rectangle(pos=(0, 1), size=(780, 10))

        self.printable = GridLayout(cols=1, spacing=1, padding=0, size_hint=(1., None), size=(780, 350),  # SCREENSHOOT
                                    pos_hint={'center_x': .5, 'center_y': .5}, row_default_height=90,
                                    row_force_default=True)
        self.printable.add_widget(
            Label(text=" " * 161, color=(0, 0, 1, 1), size_hint=(1., None), size=(780, 40), italic=True))
        # self.printable.add_widget(Label(text=" " * 161, color=(0, 0, 1, 1), italic=True))

        self.num1 = BoxLayout(spacing=0, padding=0, size_hint=(1., None), size=(780, 142))
        # ___________________________

        im = AsyncImage(source=ASY + 'L.png', size_hint=(None, None), size=(200, 140), allow_stretch=True)
        self.num1.add_widget(im)
        self.gnum1 = GridLayout(cols=1, size_hint=(None, None), size=(380, 140), row_default_height=27,
                                row_force_default=True)
        # _______________________________

        pickl = open(DIR + 'media' + PTH + '0' + PTH + 'SCHOOL.bin', 'rb')
        ids = pickle.load(pickl)
        pickl.close()

        # self.gnum1.add_widget(Label(text=' '))
        self.gnum1.add_widget(Label(text='   ' + ids['1'] + '               ', color=(0, 0, 1, 1), font_size=20))
        self.gnum1.add_widget(Label(text='       ' + ids['2'] + '               ', color=(0, 0, 0, 1)))
        self.gnum1.add_widget(Label(text='   ' + ids['3'] + '               ', color=(0, 1, 0, 1)))
        self.gnum1.add_widget(Label(text='       ' + ids['4'] + '               ', color=(0, 0, 0, 1)))
        self.gnum1.add_widget(Label(text='     ' + ids['5'] + '               ', color=(1, 0, 0, 1), font_size=20))
        self.gnum1.add_widget(Label(text=' ' * 15 + '-' * 100 + ' ' * 20, underline=True, color=(1, 0, 0, 1)))

        self.num1.add_widget(self.gnum1)
        sim = AsyncImage(source=ASY + self.NM.text + '.png', size_hint=(None, None), size=(200, 140),
                         allow_stretch=True)
        self.num1.add_widget(sim)

        self.gnum2 = GridLayout(cols=8, padding=1, spacing=1, size_hint=(1., None), size=(780, 40))
        self.gnum2.add_widget(TextInput(text='   Name :  ' + self.NM.text.capitalize(), background_normal="rb2.png",
                                        background_active="rb2.png", foreground_color=(1, 1, .7, 1),
                                        background_color=(.4, 0, .7, 1),
                                        size_hint=(None, None), size=(300, 40)))
        # self.gnum2.add_widget(TextInput(text=self.NM.text.capitalize(), color=(0, 0, 1, 1), italic=True))
        self.gnum2.add_widget(TextInput(text='Sex :  ' + dict[self.NM.text]['Sex'], background_normal="rb2.png",
                                        background_active="rb2.png", foreground_color=(1, 1, .7, 1),
                                        background_color=(.4, 0, .7, 1)))
        # self.gnum2.add_widget(TextInput(text=dict[self.NM.text]['Sex'], color=(0, 0, 1, 1), italic=True))
        self.gnum2.add_widget(TextInput(text='Class :  ' + self.CL.text, background_normal="rb2.png",
                                        background_active="rb2.png", foreground_color=(1, 1, .7, 1),
                                        background_color=(.4, 0, .7, 1)))

        self.gnum2.add_widget(TextInput(text=self.TERM.text, background_normal="rb2.png",
                                        background_active="rb2.png", foreground_color=(1, 1, .7, 1),
                                        background_color=(.4, 0, .7, 1)))

        # self.gnum2.add_widget(TextInput(text=self.CL.text, color=(0, 0, 1, 1), italic=True))

        # self.term = Label(text='', color=(0, 0, 1, 1), italic=True)
        # if time.strftime("%m") in ('01','02', '03', '04'):
        #     self.gnum2.add_widget(TextInput(text='Term :  I', background_normal="rb2.png",
        #                                 background_active="rb2.png",foreground_color=(1, 1, .7, 1),background_color=(.4, 0, .7, 1)))
        # if time.strftime("%m") in ('05', '06', '07'):
        #     self.gnum2.add_widget(TextInput(text='Term :  II', background_normal="rb2.png",
        #                                 background_active="rb2.png",foreground_color=(1, 1, .7, 1),background_color=(.4, 0, .7, 1)))
        # if time.strftime("%m") in ('08', '09', '10', '11'):
        #     self.gnum2.add_widget(TextInput(text='Term :  III', background_normal="rb2.png",
        #                                 background_active="rb2.png",foreground_color=(1, 1, .7, 1),background_color=(.4, 0, .7, 1)))

        self.printable.add_widget(self.num1)
        self.line = GridLayout(cols=1, size_hint=(1., .01), row_default_height=10,
                               row_force_default=True)
        self.line.add_widget(Label(text=' ' * 20 + '-' * 100 + ' ' * 20, underline=True, color=(0, 0, 0, 1)))
        # self.printable.add_widget(self.line)
        self.printable.add_widget(self.gnum2)

        self.gnum3 = GridLayout(cols=3, padding=1, spacing=1, row_default_height=40,
                                row_force_default=True)  # , row_default_height=6, row_force_default=True

        l = []
        for x in dict.keys():
            if not dict[x].get('marks'):
                # del (dict[x])
                grade = ""
            else:

                # if dict[x]['marks']['mtc']['term1']['mgt1'] == '':
                #     dict[x]['marks']['mtc']['term1']['mgt1'] = "0"
                if dict[x]['marks']['tal']['term' + self.Called]['mgt' + self.Called + '_TAL'] == '':
                    dict[x]['marks']['tal']['term' + self.Called]['mgt' + self.Called + '_TAL'] = "0"

                num = dict[x]['marks']['tal']['term' + self.Called]['mgt' + self.Called + '_TAL']
                if '.' in num:
                    if int(num[-1]) >= 5:
                        num = str(float(num[:num.index('.')]) + 1)

                    if int(num[-1]) < 5:
                        num = str(float(num[:num.index('.')]))

                    NM = num[:num.index('.')]

                else:
                    NM = num

                if len(NM) == 1:
                    NM = "0000" + NM
                if len(NM) == 2:
                    NM = "000" + NM
                if len(NM) == 3:
                    NM = "00" + NM
                if len(NM) == 4:
                    NM = "0" + NM

                l.append(NM + "_" + x)

        l.sort()
        v = list(reversed(l))

        for nam in v:
            if self.NM.text in nam:
                grade = v.index(nam) + 1

        self.gnum3.add_widget(
            TextInput(text='         End of term Position : ' + str(grade), background_normal="rb2.png",
                      background_active="rb2.png", foreground_color=(1, 1, .7, 1), background_color=(.4, 0, .7, 1),size_hint=(None, None), size=(250, 40)))
        # self.gnum3.add_widget(TextInput(text="DIV II", background_normal="rb2.png",
        #                                 background_active="rb2.png",foreground_color=(1, 1, .7, 1),background_color=(.4, 0, .7, 1), size_hint=(1., .01)))
        self.gnum3.add_widget(
            TextInput(text='Out of : ' + str(len(dict.keys())) + " Pupils", background_normal="rb2.png",
                      background_active="rb2.png", foreground_color=(1, 1, .7, 1), background_color=(.4, 0, .7, 1),size_hint=(None, None), size=(200, 40)))
        # self.gnum3.add_widget(TextInput(text=str(len(dict.keys())) + " Pupils", background_normal="rb2.png",
        #                                 background_active="rb2.png",foreground_color=(1, 1, .7, 1),background_color=(.4, 0, .7, 1), size_hint=(1., .01)))
        self.gnum3.add_widget(TextInput(text='Date : ' + time.strftime('%d %B %y'), background_normal="rb2.png",
                                        background_active="rb2.png", foreground_color=(1, 1, .7, 1),
                                        background_color=(.4, 0, .7, 1)))
        PRC = TextInput(hint_text="     AVERAGE PERCENTAGE :  ", readonly=True, foreground_color=(1, 1, 1, 1),
                        background_color=(0, 0, 0, .4), size_hint=(None, None), size=(300, 30))
        self.gnum3.add_widget(PRC)
        NEXT = TextInput(hint_text="", readonly=True, foreground_color=(1, 1, 1, 1), background_color=(0, 0, 0, .4),
                         size_hint=(None, None), size=(270, 30))
        self.gnum3.add_widget(NEXT)

        self.printable.add_widget(self.gnum3)

        self.BIG47 = GridLayout(cols=5, size_hint=(1., None), size=(780, 450), pos_hint={'center_x': .5, 'center_y': .6},
                              row_default_height=30,
                              row_force_default=True)

        self.BIG47.add_widget(TextInput(text='   SUBJECT', readonly=True, size_hint=(.2, .09)))
        self.BIG47.add_widget(TextInput(text='MID TERM', readonly=True, size_hint=(.2, .09)))
        self.BIG47.add_widget(TextInput(text='END OF TERM', readonly=True, size_hint=(.2, .09)))
        self.BIG47.add_widget(TextInput(text='REMARKS', readonly=True, size_hint=(.2, .09)))
        self.BIG47.add_widget(TextInput(text='INITIALS', readonly=True, size_hint=(.2, .09)))

        # self.gggg.add_widget(Label(text='', color=(0, 0, 0, 1)))
        self.BIG47.add_widget(
            TextInput(text='///////////////////////////////////////////////////////////', background_color=(1, 1, 0, 1),
                      font_size=35, readonly=True))

        self.gt1 = GridLayout(cols=2, size_hint_y=.09, row_default_height=30,
                              row_force_default=True)

        self.gt1.add_widget(TextInput(text='MAX',font_size=15, readonly=True))
        self.gt1.add_widget(TextInput(text='Marks',font_size=15, readonly=True))
        # self.gt1.add_widget(TextInput(text='Agg', readonly=True))
        self.BIG47.add_widget(self.gt1)

        self.gt2 = GridLayout(cols=2, size_hint_y=.09, row_default_height=30,
                              row_force_default=True)

        self.gt2.add_widget(TextInput(text='MAX',font_size=11, readonly=True))
        self.gt2.add_widget(TextInput(text='Marks',font_size=10, readonly=True))
        # self.gt2.add_widget(TextInput(text='Agg', readonly=True))
        self.BIG47.add_widget(self.gt2)

        self.BIG47.add_widget(TextInput(text='////////////////////////////////////////////////////', font_size=35,
                                        background_color=(1, 1, 0, 1), readonly=True))
        self.BIG47.add_widget(
            TextInput(text='//////////////////////////////////////////////////////', background_color=(1, 1, 0, 1),
                      font_size=35, readonly=True))
        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        self.MTC = TextInput(text='   MTC', readonly=True)
        self.BIG47.add_widget(self.MTC)
        self.fmt1 = TextInput(text='100', background_color=(1, 1, 0, 1), readonly=True)
        self.gt1.add_widget(self.fmt1)
        self.mgt1 = TextInput(multiline=False)
        self.mgt1.bind(text=self.sv_ns)
        self.gt1.add_widget(self.mgt1)
        # self.agt1 = TextInput(multiline=False)
        # self.gt1.add_widget(self.agt1)

        self.fmt2 = TextInput(text='100', background_color=(1, 1, 0, 1), readonly=True)
        self.gt2.add_widget(self.fmt2)
        self.mgt2 = TextInput(multiline=False)
        self.mgt2.bind(text=self.sv_ns)
        self.gt2.add_widget(self.mgt2)
        # self.agt2 = TextInput(multiline=False)
        # self.gt2.add_widget(self.agt2)
        self.BIG47.add_widget(Label(text=""))
        self.BIG47.add_widget(Label(text=""))
        self.REM1 = TextInput(foreground_color=(1, 0, 0, 1), allow_copy=True)
        self.REM1.bind(text=self.sv_ns)
        self.BIG47.add_widget(self.REM1)
        self.INIT1 = TextInput(multiline=False)
        self.INIT1.bind(text=self.sv_ns)
        self.BIG47.add_widget(self.INIT1)

        #               LD1             #

        self.LD1 = TextInput(text='   Language Dev 1', readonly=True)
        self.BIG47.add_widget(self.LD1)
        self.fmt1_LD1 = TextInput(text='100', background_color=(1, 1, 0, 1), readonly=True)
        self.gt1.add_widget(self.fmt1_LD1)
        self.mgt1_LD1 = TextInput(multiline=False)
        self.mgt1_LD1.bind(text=self.sv_ns)
        self.gt1.add_widget(self.mgt1_LD1)
        # self.agt1_LD1 = TextInput(multiline=False)
        # self.gt1.add_widget(self.agt1_LD1)

        self.fmt2_LD1 = TextInput(text='100', background_color=(1, 1, 0, 1), readonly=True)
        self.gt2.add_widget(self.fmt2_LD1)
        self.mgt2_LD1 = TextInput(multiline=False)
        self.mgt2_LD1.bind(text=self.sv_ns)
        self.gt2.add_widget(self.mgt2_LD1)
        # self.agt2_LD1 = TextInput(multiline=False)
        # self.gt2.add_widget(self.agt2_LD1)
        self.BIG47.add_widget(Label(text=""))
        self.BIG47.add_widget(Label(text=""))
        self.REM1_LD1 = TextInput(foreground_color=(1, 0, 0, 1), allow_copy=True)
        self.REM1_LD1.bind(text=self.sv_ns)
        self.BIG47.add_widget(self.REM1_LD1)
        self.INIT1_LD1 = TextInput(multiline=False)
        self.INIT1_LD1.bind(text=self.sv_ns)
        self.BIG47.add_widget(self.INIT1_LD1)

        #                 _LIT                #

        self.LD2 = TextInput(text='   Language Dev 2', readonly=True)
        self.BIG47.add_widget(self.LD2)
        self.fmt1_LD2 = TextInput(text='100', background_color=(1, 1, 0, 1), readonly=True)
        self.gt1.add_widget(self.fmt1_LD2)
        self.mgt1_LD2 = TextInput(multiline=False)
        self.mgt1_LD2.bind(text=self.sv_ns)
        self.gt1.add_widget(self.mgt1_LD2)
        # self.agt1_LD2 = TextInput(multiline=False)
        # self.gt1.add_widget(self.agt1_LD2)

        self.fmt2_LD2 = TextInput(text='100', background_color=(1, 1, 0, 1), readonly=True)
        self.gt2.add_widget(self.fmt2_LD2)
        self.mgt2_LD2 = TextInput(multiline=False)
        self.mgt2_LD2.bind(text=self.sv_ns)
        self.gt2.add_widget(self.mgt2_LD2)
        # self.agt2_LD2 = TextInput(multiline=False)
        # self.gt2.add_widget(self.agt2_LD2)
        self.BIG47.add_widget(Label(text=""))
        self.BIG47.add_widget(Label(text=""))
        self.REM1_LD2 = TextInput(foreground_color=(1, 0, 0, 1), allow_copy=True)
        self.REM1_LD2.bind(text=self.sv_ns)
        self.BIG47.add_widget(self.REM1_LD2)
        self.INIT1_LD2 = TextInput(multiline=False)
        self.INIT1_LD2.bind(text=self.sv_ns)
        self.BIG47.add_widget(self.INIT1_LD2)

        #        _LITII                 #

        self.SD = TextInput(text='   Social \n   Development', readonly=True)
        self.BIG47.add_widget(self.SD)
        self.fmt1_SD = TextInput(text='100', background_color=(1, 1, 0, 1), readonly=True)
        self.gt1.add_widget(self.fmt1_SD)
        self.mgt1_SD = TextInput(multiline=False)
        self.mgt1_SD.bind(text=self.sv_ns)
        self.gt1.add_widget(self.mgt1_SD)
        # self.agt1_SD = TextInput(multiline=False)
        # self.gt1.add_widget(self.agt1_SD)

        self.fmt2_SD = TextInput(text='100', background_color=(1, 1, 0, 1), readonly=True)
        self.gt2.add_widget(self.fmt2_SD)
        self.mgt2_SD = TextInput(multiline=False)
        self.mgt2_SD.bind(text=self.sv_ns)
        self.gt2.add_widget(self.mgt2_SD)
        # self.agt2_SD = TextInput(multiline=False)
        # self.gt2.add_widget(self.agt2_SD)
        self.BIG47.add_widget(Label(text=""))
        self.BIG47.add_widget(Label(text=""))
        self.REM1_SD = TextInput(foreground_color=(1, 0, 0, 1), allow_copy=True)
        self.REM1_SD.bind(text=self.sv_ns)
        self.BIG47.add_widget(self.REM1_SD)
        self.INIT1_SD = TextInput(multiline=False)
        self.INIT1_SD.bind(text=self.sv_ns)
        self.BIG47.add_widget(self.INIT1_SD)

        #          _READING

        self.HH = TextInput(text='   Health Habit', readonly=True)
        self.BIG47.add_widget(self.HH)
        self.fmt1_HH = TextInput(text='100', background_color=(1, 1, 0, 1), readonly=True)
        self.gt1.add_widget(self.fmt1_HH)
        self.mgt1_HH = TextInput(multiline=False)
        self.mgt1_HH.bind(text=self.sv_ns)
        self.gt1.add_widget(self.mgt1_HH)
        # self.agt1_HH = TextInput(multiline=False)
        # self.gt1.add_widget(self.agt1_HH)

        self.fmt2_HH = TextInput(text='100', background_color=(1, 1, 0, 1), readonly=True)
        self.gt2.add_widget(self.fmt2_HH)
        self.mgt2_HH = TextInput(multiline=False)
        self.mgt2_HH.bind(text=self.sv_ns)
        self.gt2.add_widget(self.mgt2_HH)
        # self.agt2_HH = TextInput(multiline=False)
        # self.gt2.add_widget(self.agt2_HH)
        self.BIG47.add_widget(Label(text=""))
        self.BIG47.add_widget(Label(text=""))
        self.REM1_HH = TextInput(foreground_color=(1, 0, 0, 1), allow_copy=True)
        self.REM1_HH.bind(text=self.sv_ns)
        self.BIG47.add_widget(self.REM1_HH)
        self.INIT1_HH = TextInput(multiline=False)
        self.INIT1_HH.bind(text=self.sv_ns)
        self.BIG47.add_widget(self.INIT1_HH)

        #            _TT           #

        self.TOTAL = TextInput(text='   TOTAL', readonly=True)
        self.BIG47.add_widget(self.TOTAL)
        self.fmt1_TAL = TextInput(text='500', background_color=(1, .5, 0, 1), readonly=True)
        self.gt1.add_widget(self.fmt1_TAL)
        self.mgt1_TAL = TextInput(multiline=False, background_color=(0, 0, 0, 1), foreground_color=(1, 1, 1, 1))
        self.mgt1_TAL.bind(text=self.sv_ns)
        self.gt1.add_widget(self.mgt1_TAL)
        # self.agt1_TAL = TextInput(multiline=False)
        # self.gt1.add_widget(self.agt1_TAL)

        self.fmt2_TAL = TextInput(text='500', background_color=(1, .5, 0, 1), readonly=True)
        self.gt2.add_widget(self.fmt2_TAL)
        self.mgt2_TAL = TextInput(multiline=False, background_color=(0, 0, 0, 1), foreground_color=(1, 1, 1, 1))
        self.mgt2_TAL.bind(text=self.sv_ns)
        self.gt2.add_widget(self.mgt2_TAL)
        # self.agt2_TAL = TextInput(multiline=False)
        # self.gt2.add_widget(self.agt2_TAL)
        self.BIG47.add_widget(Label(text=""))
        self.BIG47.add_widget(Label(text=""))
        self.REM1_TAL = TextInput(hint_text=' /////////////////////////////////', multiline=False, font_size=35,
                                 background_color=(.6, 1, 0, 1), foreground_color=(1, 0, 0, 1))
        self.REM1_TAL.bind(text=self.sv_ns)
        self.BIG47.add_widget(self.REM1_TAL)
        self.INIT1_TAL = TextInput(hint_text=' /////////////////////////////////', multiline=False, font_size=35,
                                  background_color=(.6, 1, 0, 1), foreground_color=(1, 0, 0, 1))
        self.INIT1_TAL.bind(text=self.sv_ns)
        self.BIG47.add_widget(self.INIT1_TAL)
        self.BGG.add_widget(self.printable)

        self.BGG.add_widget(self.BIG47)

        self.p2 = GridLayout(cols=2, spacing=60, padding=0, size_hint=(1., None), size=(780, 564),
                             row_default_height=70,
                             row_force_default=True)  # pos_hint={'center_x': .5, 'center_y': .5},
        with self.p2.canvas.before:
            Color(1, 0, .7, .4)
            rec = Rectangle(source='wp.png', pos=(18, 300), size=(450, 255))  # ,pos=(0, 1)

        self.gnum4 = GridLayout(cols=2, padding=30, spacing=8, size_hint=(1., None), size=(780, 270),
                                row_default_height=30, row_force_default=True,
                                col_default_width=200,
                                col_force_default=True)  # size_hint=(None,None),size=(420,280),pos=(18, 240),

        self.gnum4.add_widget(
            TextInput(text='Conduct :  ', readonly=True, foreground_color=(0, 0, 0, 1), size_hint=(None, None),
                      size=(120, 30)))
        self.behav = Spinner(text=" " + conduct()[0], values=tuple(conduct()), color=(1, 1, 0, 1),
                             background_color=(0, 0, 0, 0),
                             background_normal='btn4.png', size_hint=(.2, None), size=(120, 30))  # size=(400, 30)
        self.gnum4.add_widget(self.behav)

        self.gnum4.add_widget(TextInput(text='Debating :  ', readonly=True, size_hint=(None, None), size=(120, 30),
                                        foreground_color=(0, 0, 0, 1)))
        self.debat = Spinner(text=debat()[0], values=tuple(debat()), color=(1, 1, 0, 1),
                             background_color=(0, 0, 0, 0), background_normal='btn4.png', size_hint=(.2, None),
                             size=(120, 30))
        self.gnum4.add_widget(self.debat)

        self.gnum4.add_widget(TextInput(text='C.T’s comment :  ', readonly=True, size_hint=(None, None), size=(140, 30),
                                        foreground_color=(0, 0, 0, 1)))
        self.gnum4.add_widget(
            Spinner(text=ctcomment()[1], values=tuple(ctcomment()), color=(0, 0, 1, 1), background_color=(0, 0, 0, 0)))

        self.gnum4.add_widget(TextInput(text='H.T’s comment :  ', readonly=True, size_hint=(None, None), size=(140, 30),
                                        foreground_color=(0, 0, 0, 1)))
        self.gnum4.add_widget(
            Spinner(text=hdcomment()[1], values=tuple(hdcomment()), color=(0, 0, 1, 1), background_color=(0, 0, 0, 0)))
        self.gnum4.add_widget(
            TextInput(text='C.T’s signature :.......................................  ', readonly=True,
                      size_hint=(None, None), size=(340, 30), foreground_color=(0, 0, 0, 1)))
        self.gnum4.add_widget(Label(text="*", size_hint=(None, None), size=(20, 30)))
        self.gnum4.add_widget(
            TextInput(text='H.T’s signature :.......................................  ', readonly=True,
                      size_hint=(None, None), size=(340, 30), foreground_color=(0, 0, 0, 1)))

        self.box = GridLayout(cols=1, size_hint=(1., None), size=(780, 270), col_default_width=300,
                              col_force_default=True)  # row_default_height=300, row_force_default=True,
        self.box.add_widget(Label(text='Signature/Seal..................... ', color=(0, 0, 0, 1)))

        self.p2.add_widget(self.gnum4)
        self.p2.add_widget(self.box)

        # self.p2.add_widget(Label(text="", size_hint=(None, None), size=(250, 40)))
        # self.p2.add_widget(Label(text="", size_hint=(None, None), size=(250, 40)))
        self.p2.add_widget(Label(text='       “WE                  WISH YOU THE BEST ! ”', color=(0, 0, 0, 1),
                                 size_hint=(None, None), size=(430, 150),
                                 bold=True, font_size=24))
        self.p2.add_widget(Label(text="", size_hint=(None, None), size=(250, 60)))  #

        self.lst1 = GridLayout(cols=1, size_hint=(.4, None), size=(780, 250),
                               col_force_default=True)  # row_default_height=150, row_force_default=True, col_default_width=300,
        self.p2.add_widget(AsyncImage(source="tm.png", size_hint=(None, None), size=(300, 300)))

        self.lst2 = GridLayout(cols=1, size_hint=(.4, None), size=(
            780, 250))  # row_default_height=150, row_force_default=True,,col_default_width=300, col_force_default=True
        self.p2.add_widget(AsyncImage(source=ASY + 'QR.png', size_hint=(None, None), size=(220, 220)))  # ,
        # self.p2.add_widget(self.lst1)
        # self.p2.add_widget(self.lst2)
        self.BGG.add_widget(self.p2)
        self.BGSV.add_widget(self.BGG)
        self.add_widget(self.BGSV)
        file = open(DIR + 'media' + PTH + '0' + PTH + ANGELS + PTH + '' + self.CL.text + ".json", 'r')
        dict = json.load(file)
        file.close()

        if dict[self.NM.text].get("marks"):
            self.mgt1.text = dict[self.NM.text]["marks"]['mtc']['term1'].get("mgt1", "")
            # self.agt1.text = dict[self.NM.text]["marks"]['mtc']['term1'].get("agt1", "")
            self.mgt2.text = dict[self.NM.text]["marks"]['mtc']['term2'].get("mgt2", "")
            # self.agt2.text = dict[self.NM.text]["marks"]['mtc']['term2'].get("agt2", "")
            self.REM1.text = dict[self.NM.text]["marks"]['mtc']['term2'].get("REM1", "")
            self.INIT1.text = dict[self.NM.text]["marks"]['mtc']['term2'].get("INIT1", "")
            # LD1
            self.mgt1_LD1.text = dict[self.NM.text]["marks"]['ld1']['term1'].get("mgt1_LD1", "")
            self.mgt2_LD1.text = dict[self.NM.text]["marks"]['ld1']['term2'].get("mgt2_LD1", "")
            self.REM1_LD1.text = dict[self.NM.text]["marks"]['ld1']['term2'].get("REM1_LD1", "")
            self.INIT1_LD1.text = dict[self.NM.text]["marks"]['ld1']['term2'].get("INIT1_LD1", "")
            # _LD2
            self.mgt1_LD2.text = dict[self.NM.text]["marks"]['ld2']['term1'].get("mgt1_LD2", "")
            self.mgt2_LD2.text = dict[self.NM.text]["marks"]['ld2']['term2'].get("mgt2_LD2", "")
            self.REM1_LD2.text = dict[self.NM.text]["marks"]['ld2']['term2'].get("REM1_LD2", "")
            self.INIT1_LD2.text = dict[self.NM.text]["marks"]['ld2']['term2'].get("INIT1_LD2", "")
            # _SD
            self.mgt1_SD.text = dict[self.NM.text]["marks"]['sd']['term1'].get("mgt1_SD", "")
            self.mgt2_SD.text = dict[self.NM.text]["marks"]['sd']['term2'].get("mgt2_SD", "")
            self.REM1_SD.text = dict[self.NM.text]["marks"]['sd']['term2'].get("REM1_SD", "")
            self.INIT1_SD.text = dict[self.NM.text]["marks"]['sd']['term2'].get("INIT1_SD", "")
            # _HH
            self.mgt1_HH.text = dict[self.NM.text]["marks"]['hh']['term1'].get("mgt1_HH", "")
            self.mgt2_HH.text = dict[self.NM.text]["marks"]['hh']['term2'].get("mgt2_HH", "")
            self.REM1_HH.text = dict[self.NM.text]["marks"]['hh']['term2'].get("REM1_HH", "")
            self.INIT1_HH.text = dict[self.NM.text]["marks"]['hh']['term2'].get("INIT1_HH", "")
            # _TT
            self.mgt1_TAL.text = dict[self.NM.text]["marks"]['tal']['term1'].get("mgt1_TAL", "")
            self.mgt2_TAL.text = dict[self.NM.text]["marks"]['tal']['term2'].get("mgt2_TAL", "")
            self.REM1_TAL.text = dict[self.NM.text]["marks"]['tal']['term2'].get("REM1_TAL", "")
            self.INIT1_TAL.text = dict[self.NM.text]["marks"]['tal']['term2'].get("INIT1_TAL", "")
            # ttttttttttttttttttttttttttttttttttt
            if self.mgt1.text == "":
                self.mgt1.text = "0"
            if self.mgt1_LD1.text == "":
                self.mgt1_LD1.text = "0"
            if self.mgt1_LD2.text == "":
                self.mgt1_LD2.text = "0"
            if self.mgt1_SD.text == "":
                self.mgt1_SD.text = "0"
            if self.mgt1_HH.text == "":
                self.mgt1_HH.text = "0"
            self.mgt1_TAL.text = str(float(self.mgt1.text) + float(self.mgt1_LD1.text) + float(
                self.mgt1_LD2.text) + float(self.mgt1_SD.text) + float(self.mgt1_HH.text))
            if self.mgt2.text == "":
                self.mgt2.text = "0"
            if self.mgt2_LD1.text == "":
                self.mgt2_LD1.text = "0"
            if self.mgt2_LD2.text == "":
                self.mgt2_LD2.text = "0"
            if self.mgt2_SD.text == "":
                self.mgt2_SD.text = "0"
            if self.mgt2_HH.text == "":
                self.mgt2_HH.text = "0"
            self.mgt2_TAL.text = str(float(self.mgt2.text) + float(self.mgt2_LD1.text) + float(
                self.mgt2_LD2.text) + float(self.mgt2_SD.text) + float(self.mgt2_HH.text))
            ###################################################################
            self.REM1.text = remarks(int(self.mgt2.text))
            self.REM1_LD1.text = remarks(int(self.mgt2_LD1.text))
            self.REM1_LD2.text = remarks(int(self.mgt2_LD2.text))
            self.REM1_SD.text = remarks(int(self.mgt2_SD.text))
            self.REM1_HH.text = remarks(int(self.mgt2_HH.text))

            ##################################################################################################################################
            marks = dict[self.NM.text]['marks']['tal']['term' + self.Called]['mgt' + self.Called + '_TAL']
            if self.Called == "2":
                tot = self.fmt2_TAL.text
            else:
                tot = self.fmt1_TAL.text
            PRC.text = "     AVERAGE PERCENTAGE :  " + str(float(marks) * 100 / int(tot)) + " %"
            if float(marks) * 100 / int(tot) < 50:
                NEXT.text = "RETRY"
            else:
                if "N1" in self.CL.text :
                    NEXT.text = "PROMOTED TO MIDDLE"
                if "N2" in self.CL.text :
                    NEXT.text = "PROMOTED TO TOP"
                if "N3" in self.CL.text :
                    NEXT.text = "PROMOTED TO PRIMARY"
            if dict[self.NM.text]['$']['balance'].startswith("-"):
                self.print_report.unbind(on_release=self.png13)

    def png_nas(self, x):
        self.BGG.export_to_png(NDR + 'Desktop' + PTH + 'P R I N T A B L E' + PTH + '' + self.NM.text + "_.png")
        self.print_all_i(NDR + 'Desktop' + PTH + 'P R I N T A B L E' + PTH + '' + self.NM.text + "_.png")

        # from PIL import Image

        # image_1 = Image.open(self.NM.text + "_.png")
        # im_1 = image_1.convert('RGB')
        # im_1.save(self.NM.text + ".pdf")
        self.remove_widget(self.BGSV)
        Clock.schedule_once(self.nasry)
        return

    def sv_ns(self, sp, tx):
        try:
            int(tx)
        except:
            return
        TDAT = open(DIR + 'media' + PTH + '0' + PTH + ANGELS + PTH + '' + self.CL.text + '.json', 'r')
        DT = json.load(TDAT)
        TDAT.close()

        # ttttttttttttttttttttttttttttttttttt
        if self.mgt1.text == "":
            self.mgt1.text = "0"
        if self.mgt1_LD1.text == "":
            self.mgt1_LD1.text = "0"
        if self.mgt1_LD2.text == "":
            self.mgt1_LD2.text = "0"
        if self.mgt1_SD.text == "":
            self.mgt1_SD.text = "0"
        if self.mgt1_HH.text == "":
            self.mgt1_HH.text = "0"
        TNS = str(float(self.mgt1.text) + float(self.mgt1_LD1.text) + float(
            self.mgt1_LD2.text) + float(self.mgt1_SD.text) + float(self.mgt1_HH.text))
        self.mgt1_TAL.text = TNS[:TNS.index(".")]
        if self.mgt2.text == "":
            self.mgt2.text = "0"
        if self.mgt2_LD1.text == "":
            self.mgt2_LD1.text = "0"
        if self.mgt2_LD2.text == "":
            self.mgt2_LD2.text = "0"
        if self.mgt2_SD.text == "":
            self.mgt2_SD.text = "0"
        if self.mgt2_HH.text == "":
            self.mgt2_HH.text = "0"
        T2NS = str(float(self.mgt2.text) + float(self.mgt2_LD1.text) + float(
            self.mgt2_LD2.text) + float(self.mgt2_SD.text) + float(self.mgt2_HH.text))
        self.mgt2_TAL.text = T2NS[:T2NS.index(".")]

        self.REM1.text = remarks(int(self.mgt2.text))
        self.REM1_LD1.text = remarks(int(self.mgt2_LD1.text))
        self.REM1_LD2.text = remarks(int(self.mgt2_LD2.text))
        self.REM1_SD.text = remarks(int(self.mgt2_SD.text))
        self.REM1_HH.text = remarks(int(self.mgt2_HH.text))

        if not DT[self.NM.text].get('marks', 0):
            DT[self.NM.text]['marks'] = {}

        # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

        if not DT[self.NM.text]['marks'].get('mtc', 0):
            DT[self.NM.text]['marks']['mtc'] = {}
        if not DT[self.NM.text]['marks']['mtc'].get('term1', 0):
            DT[self.NM.text]['marks']['mtc']['term1'] = {}
        DT[self.NM.text]['marks']['mtc']['term1'] = {'mgt1': self.mgt1.text}

        if not DT[self.NM.text]['marks']['mtc'].get('term2', 0):
            DT[self.NM.text]['marks']['mtc']['term2'] = {}
        DT[self.NM.text]['marks']['mtc']['term2'] = {'mgt2': self.mgt2.text,
                                                     'REM1': self.REM1.text,
                                                     'INIT1': self.INIT1.text
                                                     }

        #############           _LD1          ##############

        if not DT[self.NM.text]['marks'].get('ld1', 0):
            DT[self.NM.text]['marks']['ld1'] = {}
        if not DT[self.NM.text]['marks']['ld1'].get('term1', 0):
            DT[self.NM.text]['marks']['ld1']['term1'] = {}
        DT[self.NM.text]['marks']['ld1']['term1'] = {'mgt1_LD1': self.mgt1_LD1.text}

        if not DT[self.NM.text]['marks']['ld1'].get('term2', 0):
            DT[self.NM.text]['marks']['ld1']['term2'] = {}
        DT[self.NM.text]['marks']['ld1']['term2'] = {'mgt2_LD1': self.mgt2_LD1.text,
                                                     'REM1_LD1': self.REM1_LD1.text,
                                                     'INIT1_LD1': self.INIT1_LD1.text
                                                     }

        ##########         _LD2            ########################

        if not DT[self.NM.text]['marks'].get('ld2', 0):
            DT[self.NM.text]['marks']['ld2'] = {}
        if not DT[self.NM.text]['marks']['ld2'].get('term1', 0):
            DT[self.NM.text]['marks']['ld2']['term1'] = {}
        DT[self.NM.text]['marks']['ld2']['term1'] = {'mgt1_LD2': self.mgt1_LD2.text}

        if not DT[self.NM.text]['marks']['ld2'].get('term2', 0):
            DT[self.NM.text]['marks']['ld2']['term2'] = {}
        DT[self.NM.text]['marks']['ld2']['term2'] = {'mgt2_LD2': self.mgt2_LD2.text,
                                                     'REM1_LD2': self.REM1_LD2.text,
                                                     'INIT1_LD2': self.INIT1_LD2.text
                                                     }

        ###########             _SD               ####################

        if not DT[self.NM.text]['marks'].get('sd', 0):
            DT[self.NM.text]['marks']['sd'] = {}
        if not DT[self.NM.text]['marks']['sd'].get('term1', 0):
            DT[self.NM.text]['marks']['sd']['term1'] = {}
        DT[self.NM.text]['marks']['sd']['term1'] = {'mgt1_SD': self.mgt1_SD.text}

        if not DT[self.NM.text]['marks']['sd'].get('term2', 0):
            DT[self.NM.text]['marks']['sd']['term2'] = {}
        DT[self.NM.text]['marks']['sd']['term2'] = {'mgt2_SD': self.mgt2_SD.text,
                                                    'REM1_SD': self.REM1_SD.text,
                                                    'INIT1_SD': self.INIT1_SD.text
                                                    }

        ###################       _HH         #############

        if not DT[self.NM.text]['marks'].get('hh', 0):
            DT[self.NM.text]['marks']['hh'] = {}
        if not DT[self.NM.text]['marks']['hh'].get('term1', 0):
            DT[self.NM.text]['marks']['hh']['term1'] = {}
        DT[self.NM.text]['marks']['hh']['term1'] = {'mgt1_HH': self.mgt1_HH.text}

        if not DT[self.NM.text]['marks']['hh'].get('term2', 0):
            DT[self.NM.text]['marks']['hh']['term2'] = {}
        DT[self.NM.text]['marks']['hh']['term2'] = {'mgt2_HH': self.mgt2_HH.text,
                                                    'REM1_HH': self.REM1_HH.text,
                                                    'INIT1_HH': self.INIT1_HH.text
                                                    }
        #########          _TT        ########################

        if not DT[self.NM.text]['marks'].get('tal', 0):
            DT[self.NM.text]['marks']['tal'] = {}
        if not DT[self.NM.text]['marks']['tal'].get('term1', 0):
            DT[self.NM.text]['marks']['tal']['term1'] = {}
        DT[self.NM.text]['marks']['tal']['term1'] = {'mgt1_TAL': self.mgt1_TAL.text}

        if not DT[self.NM.text]['marks']['tal'].get('term2', 0):
            DT[self.NM.text]['marks']['tal']['term2'] = {}
        DT[self.NM.text]['marks']['tal']['term2'] = {'mgt2_TAL': self.mgt2_TAL.text,
                                                     'REM1_TAL': self.REM1_TAL.text,
                                                     'INIT1_TAL': self.INIT1_TAL.text
                                                     }

        file = open(DIR + 'media' + PTH + '0' + PTH + ANGELS + PTH + '' + self.CL.text + '.json', 'w')
        json.dump(DT, file)
        file.close()
        print("writen")

        ##############################               COMPLETE STUDENT DATA IN FIELD         ################

    def ANALYSupdown(self, window, key, *largs):
        if key == 273:
            self.roll = self.roll + .01
            self.scrll.scroll_y = self.roll

        if key == 274:
            self.roll = self.roll - .01
            self.scrll.scroll_y = self.roll

        if key == 275:
            self.xroll = self.xroll + .01
            self.scrll.scroll_x = self.xroll

        if key == 276:
            self.xroll = self.xroll - .01
            self.scrll.scroll_x = self.xroll

    def cselection(self, sp, tx):

        self.roll = 1
        self.xroll = 1
        Window.bind(on_keyboard=self.ANALYSupdown)

        self.backward = tx
        try:
            self.remove_widget(self.gridl)
        except:
            pass
        try:
            self.remove_widget(self.print_report)
        except:
            pass
        self.print_report = Button(text='PRINT', size_hint=(.2, .06), pos_hint={'center_x': .90, 'center_y': .78})
        self.print_report.bind(on_release=self.p_rep)
        try:
            self.add_widget(self.print_report)
        except:
            pass

        # self.chois = Spinner(text='Term2', values=('Term1','Term2'),size_hint=(.2, .06), pos_hint={'center_x': .80, 'center_y': .78})
        try:
            self.add_widget(self.Chois)
        except:
            pass
        try:
            self.add_widget(self.print_report)
        except:
            pass

        try:
            self.remove_widget(self.scrll)
        except:
            pass
        try:
            self.remove_widget(self.BGSV)
        except:
            pass
        try:
            self.NM.text = ' '
        except:
            pass
        lis = []
        TDAT = open(DIR + 'media' + PTH + '0' + PTH + ANGELS + PTH + '' + tx + ".json", 'r')
        dict = json.load(TDAT)
        TDAT.close()
        for x in dict.keys():
            lis.append(x)
        lis.sort()
        self.NM.values = tuple(lis)

        #
        self.scrll = ScrollView(size_hint_x=.8, size_hint_y=.6, pos_hint={'center_x': .5, 'center_y': .3},
                                do_scroll_x=True, do_scroll_y=True,
                                scroll_timeout=55, scroll_distance=20, scroll_type=['bars', 'content'], bar_width=10,
                                bar_color=(1, 1, 0, 1), bar_inactive_color=(1, 1, 1, 1), bar_margin=0)
        if self.CL.text[0] == "N":
            self.grd_analys = GridLayout(cols=6, size_hint=(1.5, 9), pos_hint={'center_x': .5, 'center_y': .36},
                                         row_default_height=29, row_force_default=True)
            self.mtc = TextInput(text='MTC', readonly=True, allow_copy=True, size_hint_y=.3)
            self.grd_analys.add_widget(self.mtc)
            self.ld1 = TextInput(text='Language Dev1', readonly=True, allow_copy=True, size_hint_y=.3)
            self.grd_analys.add_widget(self.ld1)
            self.ld2 = TextInput(text='Language Dev2', readonly=True, allow_copy=True, size_hint_y=.3)
            self.grd_analys.add_widget(self.ld2)
            self.sd = TextInput(text='Social Dev', readonly=True, allow_copy=True, size_hint_y=.3)
            self.grd_analys.add_widget(self.sd)
            self.hh = TextInput(text='Health Habit', readonly=True, allow_copy=True, size_hint_y=.3)
            self.grd_analys.add_widget(self.hh)
            self.total = TextInput(text='TOTAL', foreground_color=(1, 1, 1, 1), background_color=(0, 0, 0, 1),
                                   readonly=True,
                                   allow_copy=True, size_hint_y=.3)
            self.grd_analys.add_widget(self.total)

            self.mtc_grade = GridLayout(cols=2, row_default_height=29, row_force_default=True)
            l = []
            for x in dict.keys():
                if not dict[x].get('marks'):
                    print('no marks', x)
                    pass
                else:

                    # if dict[x]['marks']['mtc']['term1']['mgt1'] == '':
                    #     dict[x]['marks']['mtc']['term1']['mgt1'] = "0"
                    if dict[x]['marks']['mtc']['term' + self.Called]['mgt' + self.Called] == '':
                        dict[x]['marks']['mtc']['term' + self.Called]['mgt' + self.Called] = "0"

                    num = dict[x]['marks']['mtc']['term' + self.Called]['mgt' + self.Called]
                    if '.' in num:
                        if int(num[-1]) >= 5:
                            num = str(float(num[:num.index('.')]) + 1)
                            print('num', num)
                        if int(num[-1]) < 5:
                            num = str(float(num[:num.index('.')]))
                            print('num', num)
                        NM = num[:num.index('.')]

                    else:
                        NM = num
                    print('NM', NM)
                    if len(NM) == 1:
                        NM = "000" + NM
                    if len(NM) == 2:
                        NM = "00" + NM
                    if len(NM) == 3:
                        NM = "0" + NM

                    l.append(NM + "_" + x)
            l.sort()
            v = list(reversed(l))
            self.mtc_grade.add_widget(TextInput(text='...', readonly=True, foreground_color=(1, 0, 0, 1)))
            self.mtc_grade.add_widget(
                TextInput(text='mks', readonly=True, foreground_color=(1, 0, 0, 1), size_hint=(None, None),
                          size=(46, 29), allow_copy=True, size_hint_y=.3))
            for i in v:
                self.mtc_grade.add_widget(
                    TextInput(text=i[i.index('_') + 1:].title(), foreground_color=(.4, 0, 1, 1), readonly=True,
                              allow_copy=True))
                self.mtc_grade.add_widget(
                    TextInput(text=ooo(i[1:i.index('_')]), background_color=(.6, .7, 0, 1), readonly=True,
                              foreground_color=(1, 0, 0, 1),
                              size_hint=(None, None),
                              size=(46, 29), allow_copy=True))
            self.grd_analys.add_widget(self.mtc_grade)
            del v
            del l
            #
            #

            self.ld1_grade = GridLayout(cols=2, row_default_height=29, row_force_default=True)
            l = []
            for x in dict.keys():
                if not dict[x].get('marks'):
                    # del (dict[x])
                    # grade = ""
                    pass
                else:
                    # if dict[x]['marks']['ld1']['term1']['mgt1_LD1'] == '':
                    #     dict[x]['marks']['ld1']['term1']['mgt1_LD1'] = "0"
                    if dict[x]['marks']['ld1']['term' + self.Called]['mgt' + self.Called + '_LD1'] == '':
                        dict[x]['marks']['ld1']['term' + self.Called]['mgt' + self.Called + '_LD1'] = "0"
                    num = dict[x]['marks']['ld1']['term' + self.Called]['mgt' + self.Called + '_LD1']
                    if '.' in num:
                        if int(num[-1]) >= 5:
                            num = str(float(num[:num.index('.')]) + 1)
                            print('num', num)
                        if int(num[-1]) < 5:
                            num = str(float(num[:num.index('.')]))
                            print('num', num)
                        NM = num[:num.index('.')]

                    else:
                        NM = num
                    print('NM', NM)
                    if len(NM) == 1:
                        NM = "000" + NM
                    if len(NM) == 2:
                        NM = "00" + NM
                    if len(NM) == 3:
                        NM = "0" + NM
                    l.append(NM + "_" + x)

            l.sort()
            v = list(reversed(l))
            self.ld1_grade.add_widget(TextInput(text='...', readonly=True, foreground_color=(1, 0, 0, 1)))
            self.ld1_grade.add_widget(
                TextInput(text='mks', readonly=True, foreground_color=(1, 0, 0, 1), size_hint=(None, None),
                          size=(46, 29), allow_copy=True, size_hint_y=.3))
            for i in v:
                self.ld1_grade.add_widget(
                    TextInput(text=i[i.index('_') + 1:].title(), foreground_color=(.4, 0, 1, 1), readonly=True,
                              allow_copy=True))
                self.ld1_grade.add_widget(
                    TextInput(text=ooo(i[1:i.index('_')]), background_color=(.6, .7, 0, 1), readonly=True,
                              foreground_color=(1, 0, 0, 1),
                              size_hint=(None, None),
                              size=(46, 29), allow_copy=True))
            self.grd_analys.add_widget(self.ld1_grade)
            # del v
            # del l
            #
            #

            self.ld2_grade = GridLayout(cols=2, row_default_height=29, row_force_default=True)
            l = []
            for x in dict.keys():
                if not dict[x].get('marks'):
                    # del (dict[x])
                    # grade = ""
                    pass
                else:
                    # if dict[x]['marks']['ld2']['term1']['mgt1_LD2'] == '':
                    #     dict[x]['marks']['ld2']['term1']['mgt1_LD2'] = "0"
                    if dict[x]['marks']['ld2']['term' + self.Called]['mgt' + self.Called + '_LD2'] == '':
                        dict[x]['marks']['ld2']['term' + self.Called]['mgt' + self.Called + '_LD2'] = "0"

                    num = dict[x]['marks']['ld2']['term' + self.Called]['mgt' + self.Called + '_LD2']
                    if '.' in num:
                        if int(num[-1]) >= 5:
                            num = str(float(num[:num.index('.')]) + 1)
                            print('num', num)
                        if int(num[-1]) < 5:
                            num = str(float(num[:num.index('.')]))
                            print('num', num)
                        NM = num[:num.index('.')]

                    else:
                        NM = num
                    print('NM', NM)
                    if len(NM) == 1:
                        NM = "000" + NM
                    if len(NM) == 2:
                        NM = "00" + NM
                    if len(NM) == 3:
                        NM = "0" + NM
                    l.append(NM + "_" + x)

            l.sort()
            v = list(reversed(l))
            self.ld2_grade.add_widget(TextInput(text='...', readonly=True, foreground_color=(1, 0, 0, 1)))
            self.ld2_grade.add_widget(
                TextInput(text='mks', readonly=True, foreground_color=(1, 0, 0, 1), size_hint=(None, None),
                          size=(46, 29), allow_copy=True, size_hint_y=.3))
            for i in v:
                self.ld2_grade.add_widget(
                    TextInput(text=i[i.index('_') + 1:].title(), foreground_color=(.4, 0, 1, 1), readonly=True,
                              allow_copy=True))
                self.ld2_grade.add_widget(
                    TextInput(text=ooo(i[1:i.index('_')]), background_color=(.6, .7, 0, 1), readonly=True,
                              foreground_color=(1, 0, 0, 1),
                              size_hint=(None, None),
                              size=(46, 29), allow_copy=True))
            self.grd_analys.add_widget(self.ld2_grade)
            del v
            del l
            ##

            self.sd_grade = GridLayout(cols=2, row_default_height=29, row_force_default=True)
            l = []
            for x in dict.keys():
                if not dict[x].get('marks'):
                    # del (dict[x])
                    # grade = ""
                    pass
                else:
                    # if dict[x]['marks']['sd']['term1']['mgt1_SD'] == '':
                    #     dict[x]['marks']['sd']['term1']['mgt1_SD'] = "0"
                    if dict[x]['marks']['sd']['term' + self.Called]['mgt' + self.Called + '_SD'] == '':
                        dict[x]['marks']['sd']['term' + self.Called]['mgt' + self.Called + '_SD'] = "0"
                    num = dict[x]['marks']['sd']['term' + self.Called]['mgt' + self.Called + '_SD']
                    if '.' in num:
                        if int(num[-1]) >= 5:
                            num = str(float(num[:num.index('.')]) + 1)

                        if int(num[-1]) < 5:
                            num = str(float(num[:num.index('.')]))
                        NM = num[:num.index('.')]

                    else:
                        NM = num

                    if len(NM) == 1:
                        NM = "000" + NM
                    if len(NM) == 2:
                        NM = "00" + NM
                    if len(NM) == 3:
                        NM = "0" + NM
                    l.append(NM + "_" + x)
            l.sort()
            v = list(reversed(l))
            self.sd_grade.add_widget(TextInput(text='...', readonly=True, foreground_color=(1, 0, 0, 1)))
            self.sd_grade.add_widget(
                TextInput(text='mks', readonly=True, foreground_color=(1, 0, 0, 1), size_hint=(None, None),
                          size=(46, 29), allow_copy=True, size_hint_y=.3))
            for i in v:
                self.sd_grade.add_widget(
                    TextInput(text=i[i.index('_') + 1:].title(), foreground_color=(.4, 0, 1, 1), readonly=True,
                              allow_copy=True))
                self.sd_grade.add_widget(
                    TextInput(text=ooo(i[1:i.index('_')]), background_color=(.6, .7, 0, 1), readonly=True,
                              foreground_color=(1, 0, 0, 1),
                              size_hint=(None, None), size=(46, 29), allow_copy=True))
            self.grd_analys.add_widget(self.sd_grade)
            del v
            del l
            ##

            self.hh_grade = GridLayout(cols=2, row_default_height=29, row_force_default=True)
            l = []
            for x in dict.keys():
                if not dict[x].get('marks'):
                    # del (dict[x])
                    # grade = ""
                    pass
                else:
                    # if dict[x]['marks']['hh']['term1']['mgt1_HH'] == '':
                    #     dict[x]['marks']['hh']['term1']['mgt1_HH'] = "0"
                    if dict[x]['marks']['hh']['term' + self.Called]['mgt' + self.Called + '_HH'] == '':
                        dict[x]['marks']['hh']['term' + self.Called]['mgt' + self.Called + '_HH'] = "0"
                    num = dict[x]['marks']['hh']['term' + self.Called]['mgt' + self.Called + '_HH']
                    if '.' in num:
                        if int(num[-1]) >= 5:
                            num = str(float(num[:num.index('.')]) + 1)

                        if int(num[-1]) < 5:
                            num = str(float(num[:num.index('.')]))
                        NM = num[:num.index('.')]

                    else:
                        NM = num

                    if len(NM) == 1:
                        NM = "000" + NM
                    if len(NM) == 2:
                        NM = "00" + NM
                    if len(NM) == 3:
                        NM = "0" + NM
                    l.append(NM + "_" + x)
            l.sort()
            v = list(reversed(l))
            self.hh_grade.add_widget(TextInput(text='...', readonly=True, foreground_color=(1, 0, 0, 1)))
            self.hh_grade.add_widget(
                TextInput(text='mks', readonly=True, foreground_color=(1, 0, 0, 1), size_hint=(None, None),
                          size=(46, 29), allow_copy=True, size_hint_y=.3))
            for i in v:
                self.hh_grade.add_widget(
                    TextInput(text=i[i.index('_') + 1:].title(), foreground_color=(.4, 0, 1, 1), readonly=True,
                              allow_copy=True))
                self.hh_grade.add_widget(
                    TextInput(text=ooo(i[1:i.index('_')]), background_color=(.6, .7, 0, 1), readonly=True,
                              foreground_color=(1, 0, 0, 1),
                              size_hint=(None, None), size=(46, 29), allow_copy=True))
            self.grd_analys.add_widget(self.hh_grade)
            del v
            del l
            # ))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))
            self.total_grade = GridLayout(cols=2, row_default_height=29, row_force_default=True)

            l = []
            for x in dict.keys():
                if not dict[x].get('marks'):
                    print('no marks', x)
                    pass
                else:

                    # if dict[x]['marks']['mtc']['term1']['mgt1'] == '':
                    #     dict[x]['marks']['mtc']['term1']['mgt1'] = "0"
                    if dict[x]['marks']['tal']['term' + self.Called]['mgt' + self.Called + '_TAL'] == '':
                        dict[x]['marks']['tal']['term' + self.Called]['mgt' + self.Called + '_TAL'] = "0"

                    num = dict[x]['marks']['tal']['term' + self.Called]['mgt' + self.Called + '_TAL']
                    if '.' in num:
                        if int(num[-1]) >= 5:
                            num = str(float(num[:num.index('.')]) + 1)
                            print('num', num)
                        if int(num[-1]) < 5:
                            num = str(float(num[:num.index('.')]))
                            print('num', num)
                        NM = num[:num.index('.')]

                    else:
                        NM = num
                    print('NM', NM)
                    if len(NM) == 1:
                        NM = "000" + NM
                    if len(NM) == 2:
                        NM = "00" + NM
                    if len(NM) == 3:
                        NM = "0" + NM

                    l.append(NM + "_" + x)

            l.sort()
            v = list(reversed(l))
            self.sz = 2
            self.total_grade.add_widget(TextInput(text='...', readonly=True, foreground_color=(1, 0, 0, 1)))
            self.total_grade.add_widget(
                TextInput(text='mks', readonly=True, foreground_color=(1, 0, 0, 1), size_hint=(None, None),
                          size=(46, 29), allow_copy=True,
                          size_hint_y=.3))

            for i in v:
                print("vvv", v)
                self.total_grade.add_widget(
                    TextInput(text=i[i.index('_') + 1:].title(), foreground_color=(.4, 0, 1, 1), readonly=True,
                              allow_copy=True))

                self.total_grade.add_widget(
                    TextInput(text=dict[i[i.index('_') + 1:]]['marks']['tal']['term' + self.Called][
                        'mgt' + self.Called + '_TAL'],
                              background_color=(1, .7, 0, 1), readonly=True,
                              foreground_color=(1, 0, 1, 1),
                              size_hint=(None, None), size=(46, 29), allow_copy=True))
                self.sz += 1

            self.grd_analys.add_widget(self.total_grade)
            del v
            del l

        if self.CL.text[:2] in ("P1", "P2", "P3"):
            self.grd_analys = GridLayout(cols=7, size_hint=(2.3, 9), pos_hint={'center_x': .5, 'center_y': .36},
                                         row_default_height=29, row_force_default=True)

            self.mtc = TextInput(text='MTC', readonly=True, allow_copy=True, size_hint_y=.3)
            self.grd_analys.add_widget(self.mtc)
            self.eng = TextInput(text='ENG', readonly=True, allow_copy=True, size_hint_y=.3)
            self.grd_analys.add_widget(self.eng)
            self.lit = TextInput(text='LIT I', readonly=True, allow_copy=True, size_hint_y=.3)
            self.grd_analys.add_widget(self.lit)
            self.litii = TextInput(text='LIT II', readonly=True, allow_copy=True, size_hint_y=.3)
            self.grd_analys.add_widget(self.litii)
            self.reading = TextInput(text='READING', readonly=True, allow_copy=True, size_hint_y=.3)
            self.grd_analys.add_widget(self.reading)
            self.re = TextInput(text='RE', readonly=True, allow_copy=True, size_hint_y=.3)
            self.grd_analys.add_widget(self.re)
            self.total = TextInput(text='TOTAL', foreground_color=(1, 1, 1, 1), background_color=(0, 0, 0, 1),
                                   readonly=True,
                                   allow_copy=True, size_hint_y=.3)
            self.grd_analys.add_widget(self.total)
            self.mtc_grade = GridLayout(cols=2, row_default_height=29, row_force_default=True)

            l = []
            for x in dict.keys():
                if not dict[x].get('marks'):
                    print('no marks', x)
                    pass
                else:

                    # if dict[x]['marks']['mtc']['term1']['mgt1'] == '':
                    #     dict[x]['marks']['mtc']['term1']['mgt1'] = "0"
                    if dict[x]['marks']['mtc']['term' + self.Called]['mgt' + self.Called + ''] == '':
                        dict[x]['marks']['mtc']['term' + self.Called]['mgt' + self.Called + ''] = "0"

                    num = dict[x]['marks']['mtc']['term' + self.Called]['mgt' + self.Called + '']
                    if '.' in num:
                        if int(num[-1]) >= 5:
                            num = str(float(num[:num.index('.')]) + 1)
                            print('num', num)
                        if int(num[-1]) < 5:
                            num = str(float(num[:num.index('.')]))
                            print('num', num)
                        NM = num[:num.index('.')]

                    else:
                        NM = num
                    print('NM', NM)
                    if len(NM) == 1:
                        NM = "000" + NM
                    if len(NM) == 2:
                        NM = "00" + NM
                    if len(NM) == 3:
                        NM = "0" + NM

                    l.append(NM + "_" + x)
            l.sort()
            v = list(reversed(l))
            self.mtc_grade.add_widget(TextInput(text='...', readonly=True, foreground_color=(1, 0, 0, 1)))
            self.mtc_grade.add_widget(
                TextInput(text='mks', readonly=True, foreground_color=(1, 0, 0, 1), size_hint=(None, None),
                          size=(46, 29), allow_copy=True, size_hint_y=.3))
            for i in v:
                self.mtc_grade.add_widget(
                    TextInput(text=i[i.index('_') + 1:].title(), foreground_color=(.4, 0, 1, 1), readonly=True,
                              allow_copy=True))
                self.mtc_grade.add_widget(
                    TextInput(text=ooo(i[1:i.index('_')]), background_color=(.6, .7, 0, 1), readonly=True,
                              foreground_color=(1, 0, 0, 1),
                              size_hint=(None, None), size=(46, 29), allow_copy=True))

            self.grd_analys.add_widget(self.mtc_grade)
            del v
            del l
            #
            #

            self.eng_grade = GridLayout(cols=2, row_default_height=29, row_force_default=True)
            l = []
            for x in dict.keys():
                if not dict[x].get('marks'):
                    print('no marks', x)
                    pass
                else:

                    # if dict[x]['marks']['eng']['term1']['mgt1_ENG'] == '':
                    #     dict[x]['marks']['eng']['term1']['mgt1_ENG'] = "0"
                    if dict[x]['marks']['eng']['term' + self.Called]['mgt' + self.Called + '_ENG'] == '':
                        dict[x]['marks']['eng']['term' + self.Called]['mgt' + self.Called + '_ENG'] = "0"

                    num = dict[x]['marks']['eng']['term' + self.Called]['mgt' + self.Called + '_ENG']
                    if '.' in num:
                        if int(num[-1]) >= 5:
                            num = str(float(num[:num.index('.')]) + 1)
                            print('num', num)
                        if int(num[-1]) < 5:
                            num = str(float(num[:num.index('.')]))
                            print('num', num)
                        NM = num[:num.index('.')]

                    else:
                        NM = num
                    print('NM', NM)
                    if len(NM) == 1:
                        NM = "000" + NM
                    if len(NM) == 2:
                        NM = "00" + NM
                    if len(NM) == 3:
                        NM = "0" + NM

                    l.append(NM + "_" + x)
            l.sort()
            v = list(reversed(l))
            self.eng_grade.add_widget(TextInput(text='...', readonly=True, foreground_color=(1, 0, 0, 1)))
            self.eng_grade.add_widget(
                TextInput(text='mks', readonly=True, foreground_color=(1, 0, 0, 1), size_hint=(None, None),
                          size=(46, 29), allow_copy=True, size_hint_y=.3))
            for i in v:
                self.eng_grade.add_widget(
                    TextInput(text=i[i.index('_') + 1:].title(), foreground_color=(.4, 0, 1, 1), readonly=True,
                              allow_copy=True))
                self.eng_grade.add_widget(
                    TextInput(text=ooo(i[1:i.index('_')]), background_color=(.6, .7, 0, 1), readonly=True,
                              foreground_color=(1, 0, 0, 1),
                              size_hint=(None, None), size=(46, 29), allow_copy=True))
            self.grd_analys.add_widget(self.eng_grade)
            del v
            del l
            #
            #

            self.lit_grade = GridLayout(cols=2, row_default_height=29, row_force_default=True)
            l = []
            for x in dict.keys():
                if not dict[x].get('marks'):
                    print('no marks', x)
                    pass
                else:

                    # if dict[x]['marks']['lit']['term1']['mgt1_LITI'] == '':
                    #     dict[x]['marks']['lit']['term1']['mgt1_LITI'] = "0"
                    if dict[x]['marks']['lit']['term' + self.Called]['mgt' + self.Called + '_LITI'] == '':
                        dict[x]['marks']['lit']['term' + self.Called]['mgt' + self.Called + '_LITI'] = "0"

                    num = dict[x]['marks']['lit']['term' + self.Called]['mgt' + self.Called + '_LITI']
                    if '.' in num:
                        if int(num[-1]) >= 5:
                            num = str(float(num[:num.index('.')]) + 1)
                            print('num', num)
                        if int(num[-1]) < 5:
                            num = str(float(num[:num.index('.')]))
                            print('num', num)
                        NM = num[:num.index('.')]

                    else:
                        NM = num
                    print('NM', NM)
                    if len(NM) == 1:
                        NM = "000" + NM
                    if len(NM) == 2:
                        NM = "00" + NM
                    if len(NM) == 3:
                        NM = "0" + NM

                    l.append(NM + "_" + x)
            l.sort()
            v = list(reversed(l))
            self.lit_grade.add_widget(TextInput(text='...', readonly=True, foreground_color=(1, 0, 0, 1)))
            self.lit_grade.add_widget(
                TextInput(text='mks', readonly=True, foreground_color=(1, 0, 0, 1), size_hint=(None, None),
                          size=(46, 29), allow_copy=True, size_hint_y=.3))
            for i in v:
                self.lit_grade.add_widget(
                    TextInput(text=i[i.index('_') + 1:].title(), foreground_color=(.4, 0, 1, 1), readonly=True,
                              allow_copy=True))
                self.lit_grade.add_widget(
                    TextInput(text=ooo(i[1:i.index('_')]), background_color=(.6, .7, 0, 1), readonly=True,
                              foreground_color=(1, 0, 0, 1),
                              size_hint=(None, None), size=(46, 29), allow_copy=True))
            self.grd_analys.add_widget(self.lit_grade)
            del v
            del l
            #
            #

            self.litii_grade = GridLayout(cols=2, row_default_height=29, row_force_default=True)
            l = []
            for x in dict.keys():
                if not dict[x].get('marks'):
                    print('no marks', x)
                    pass
                else:

                    # if dict[x]['marks']['litii']['term1']['mgt1_LITII'] == '':
                    #     dict[x]['marks']['litii']['term1']['mgt1_LITII'] = "0"
                    if dict[x]['marks']['litii']['term' + self.Called]['mgt' + self.Called + '_LITII'] == '':
                        dict[x]['marks']['litii']['term' + self.Called]['mgt' + self.Called + '_LITII'] = "0"

                    num = dict[x]['marks']['litii']['term' + self.Called]['mgt' + self.Called + '_LITII']
                    if '.' in num:
                        if int(num[-1]) >= 5:
                            num = str(float(num[:num.index('.')]) + 1)
                            print('num', num)
                        if int(num[-1]) < 5:
                            num = str(float(num[:num.index('.')]))
                            print('num', num)
                        NM = num[:num.index('.')]

                    else:
                        NM = num
                    print('NM', NM)
                    if len(NM) == 1:
                        NM = "000" + NM
                    if len(NM) == 2:
                        NM = "00" + NM
                    if len(NM) == 3:
                        NM = "0" + NM

                    l.append(NM + "_" + x)
            l.sort()
            v = list(reversed(l))
            self.litii_grade.add_widget(TextInput(text='...', readonly=True, foreground_color=(1, 0, 0, 1)))
            self.litii_grade.add_widget(
                TextInput(text='mks', readonly=True, foreground_color=(1, 0, 0, 1), size_hint=(None, None),
                          size=(46, 29), allow_copy=True, size_hint_y=.3))
            for i in v:
                self.litii_grade.add_widget(
                    TextInput(text=i[i.index('_') + 1:].title(), foreground_color=(.4, 0, 1, 1), readonly=True,
                              allow_copy=True))
                self.litii_grade.add_widget(
                    TextInput(text=ooo(i[1:i.index('_')]), background_color=(.6, .7, 0, 1), readonly=True,
                              foreground_color=(1, 0, 0, 1),
                              size_hint=(None, None), size=(46, 29), allow_copy=True))
            self.grd_analys.add_widget(self.litii_grade)
            del v
            del l
            #
            #

            self.reading_grade = GridLayout(cols=2, row_default_height=29, row_force_default=True)
            l = []
            for x in dict.keys():
                if not dict[x].get('marks'):
                    print('no marks', x)
                    pass
                else:

                    # if dict[x]['marks']['reading']['term1']['mgt1_READ'] == '':
                    #     dict[x]['marks']['reading']['term1']['mgt1_READ'] = "0"
                    if dict[x]['marks']['reading']['term' + self.Called]['mgt' + self.Called + '_READ'] == '':
                        dict[x]['marks']['reading']['term' + self.Called]['mgt' + self.Called + '_READ'] = "0"

                    num = dict[x]['marks']['reading']['term' + self.Called]['mgt' + self.Called + '_READ']
                    if '.' in num:
                        if int(num[-1]) >= 5:
                            num = str(float(num[:num.index('.')]) + 1)
                            print('num', num)
                        if int(num[-1]) < 5:
                            num = str(float(num[:num.index('.')]))
                            print('num', num)
                        NM = num[:num.index('.')]

                    else:
                        NM = num
                    print('NM', NM)
                    if len(NM) == 1:
                        NM = "000" + NM
                    if len(NM) == 2:
                        NM = "00" + NM
                    if len(NM) == 3:
                        NM = "0" + NM

                    l.append(NM + "_" + x)
            l.sort()
            v = list(reversed(l))
            self.reading_grade.add_widget(TextInput(text='...', readonly=True, foreground_color=(1, 0, 0, 1)))
            self.reading_grade.add_widget(
                TextInput(text='mks', readonly=True, foreground_color=(1, 0, 0, 1), size_hint=(None, None),
                          size=(46, 29), allow_copy=True, size_hint_y=.3))
            for i in v:
                self.reading_grade.add_widget(
                    TextInput(text=i[i.index('_') + 1:].title(), foreground_color=(.4, 0, 1, 1), readonly=True,
                              allow_copy=True))
                self.reading_grade.add_widget(
                    TextInput(text=ooo(i[1:i.index('_')]), background_color=(.6, .7, 0, 1), readonly=True,
                              foreground_color=(1, 0, 0, 1),
                              size_hint=(None, None), size=(46, 29), allow_copy=True))
            self.grd_analys.add_widget(self.reading_grade)
            del v
            del l
            #
            #

            self.re_grade = GridLayout(cols=2, row_default_height=29, row_force_default=True)
            l = []
            for x in dict.keys():
                if not dict[x].get('marks'):
                    print('no marks', x)
                    pass
                else:

                    # if dict[x]['marks']['re']['term1']['mgt1_RE'] == '':
                    #     dict[x]['marks']['re']['term1']['mgt1_RE'] = "0"
                    if dict[x]['marks']['re']['term' + self.Called]['mgt' + self.Called + '_RE'] == '':
                        dict[x]['marks']['re']['term' + self.Called]['mgt' + self.Called + '_RE'] = "0"

                    num = dict[x]['marks']['re']['term' + self.Called]['mgt' + self.Called + '_RE']
                    if '.' in num:
                        if int(num[-1]) >= 5:
                            num = str(float(num[:num.index('.')]) + 1)
                            print('num', num)
                        if int(num[-1]) < 5:
                            num = str(float(num[:num.index('.')]))
                            print('num', num)
                        NM = num[:num.index('.')]

                    else:
                        NM = num
                    print('NM', NM)
                    if len(NM) == 1:
                        NM = "000" + NM
                    if len(NM) == 2:
                        NM = "00" + NM
                    if len(NM) == 3:
                        NM = "0" + NM

                    l.append(NM + "_" + x)
            l.sort()
            v = list(reversed(l))
            self.re_grade.add_widget(TextInput(text='...', readonly=True, foreground_color=(1, 0, 0, 1)))
            self.re_grade.add_widget(
                TextInput(text='mks', readonly=True, foreground_color=(1, 0, 0, 1), size_hint=(None, None),
                          size=(46, 29), allow_copy=True, size_hint_y=.3))
            for i in v:
                self.re_grade.add_widget(
                    TextInput(text=i[i.index('_') + 1:].title(), foreground_color=(.4, 0, 1, 1), readonly=True,
                              allow_copy=True))
                self.re_grade.add_widget(
                    TextInput(text=ooo(i[1:i.index('_')]), background_color=(.6, .7, 0, 1), readonly=True,
                              foreground_color=(1, 0, 0, 1),
                              size_hint=(None, None), size=(46, 29), allow_copy=True))
            self.grd_analys.add_widget(self.re_grade)
            del v
            del l
            # XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
            self.total_grade = GridLayout(cols=2, row_default_height=29, row_force_default=True)

            l = []
            for x in dict.keys():
                if not dict[x].get('marks'):
                    print('no marks', x)
                    pass
                else:

                    # if dict[x]['marks']['mtc']['term1']['mgt1'] == '':
                    #     dict[x]['marks']['mtc']['term1']['mgt1'] = "0"
                    if dict[x]['marks']['total']['term' + self.Called]['mgt' + self.Called + '_TT'] == '':
                        dict[x]['marks']['total']['term' + self.Called]['mgt' + self.Called + '_TT'] = "0"

                    num = dict[x]['marks']['total']['term' + self.Called]['mgt' + self.Called + '_TT']
                    if '.' in num:
                        if int(num[-1]) >= 5:
                            num = str(float(num[:num.index('.')]) + 1)
                            print('num', num)
                        if int(num[-1]) < 5:
                            num = str(float(num[:num.index('.')]))
                            print('num', num)
                        NM = num[:num.index('.')]

                    else:
                        NM = num
                    print('NM', NM)
                    if len(NM) == 1:
                        NM = "000" + NM
                    if len(NM) == 2:
                        NM = "00" + NM
                    if len(NM) == 3:
                        NM = "0" + NM

                    l.append(NM + "_" + x)

            l.sort()
            v = list(reversed(l))
            self.sz = 2
            self.total_grade.add_widget(TextInput(text='...', readonly=True, foreground_color=(1, 0, 0, 1)))
            self.total_grade.add_widget(
                TextInput(text='mks', readonly=True, foreground_color=(1, 0, 0, 1), size_hint=(None, None),
                          size=(46, 29), allow_copy=True,
                          size_hint_y=.3))

            for i in v:
                print("vvv", v)
                self.total_grade.add_widget(
                    TextInput(text=i[i.index('_') + 1:].title(), foreground_color=(.4, 0, 1, 1), readonly=True,
                              allow_copy=True))

                self.total_grade.add_widget(
                    TextInput(text=dict[i[i.index('_') + 1:]]['marks']['total']['term' + self.Called][
                        'mgt' + self.Called + '_TT'],
                              background_color=(1, .7, 0, 1), readonly=True,
                              foreground_color=(1, 0, 1, 1),
                              size_hint=(None, None), size=(46, 29), allow_copy=True))
                self.sz += 1

            self.grd_analys.add_widget(self.total_grade)
            del v
            del l
            #
            print()
        if self.CL.text[:2] in ("P4", "P5", "P6", "P7"):
            self.grd_analys = GridLayout(cols=5, size_hint=(2, 9), pos_hint={'center_x': .5, 'center_y': .46},
                                         row_default_height=29, row_force_default=True)

            self.mtc = TextInput(text='MTC', readonly=True, allow_copy=True, size_hint_y=.3)
            self.grd_analys.add_widget(self.mtc)
            self.eng = TextInput(text='ENG', readonly=True, allow_copy=True, size_hint_y=.3)
            self.grd_analys.add_widget(self.eng)
            self.sst = TextInput(text='SST', readonly=True, allow_copy=True, size_hint_y=.3)
            self.grd_analys.add_widget(self.sst)
            self.scie = TextInput(text='SCIE', readonly=True, allow_copy=True, size_hint_y=.3)
            self.grd_analys.add_widget(self.scie)

            self.total = TextInput(text='TOTAL', foreground_color=(1, 1, 1, 1), size_hint=(None, None), size=(370, 29),
                                   background_color=(0, 0, 0, 1),
                                   readonly=True, allow_copy=True, size_hint_y=.3)
            self.grd_analys.add_widget(self.total)

            self.mtc_grade = GridLayout(cols=3, row_default_height=29, row_force_default=True)

            l = []
            for x in dict.keys():
                if not dict[x].get('marks'):
                    print('no marks', x)
                    pass
                else:
                    # if dict[x]['marks']['mtc']['term1']['mgt1'] == '' or :

                    # if dict[x]['marks']['mtc']['term1']['mgt1'] == '':
                    #     dict[x]['marks']['mtc']['term1']['mgt1'] = "0"
                    if dict[x]['marks']['mtc']['term' + self.Called]['mgt' + self.Called + ''] == '':
                        dict[x]['marks']['mtc']['term' + self.Called]['mgt' + self.Called + ''] = "0"

                    num = dict[x]['marks']['mtc']['term' + self.Called]['mgt' + self.Called + '']
                    if '.' in num:
                        if int(num[-1]) >= 5:
                            num = str(float(num[:num.index('.')]) + 1)
                            print('num', num)
                        if int(num[-1]) < 5:
                            num = str(float(num[:num.index('.')]))
                            print('num', num)
                        NM = num[:num.index('.')]

                    else:
                        NM = num
                    print('NM', NM)
                    if len(NM) == 1:
                        NM = "000" + NM
                    if len(NM) == 2:
                        NM = "00" + NM
                    if len(NM) == 3:
                        NM = "0" + NM

                    l.append(NM + "_" + x)
            l.sort()
            v = list(reversed(l))
            self.mtc_grade.add_widget(TextInput(text='...', readonly=True, foreground_color=(1, 0, 0, 1)))
            self.mtc_grade.add_widget(
                TextInput(text='mks', readonly=True, foreground_color=(1, 0, 0, 1), size_hint=(None, None),
                          size=(46, 29), allow_copy=True,
                          size_hint_y=.3))
            self.mtc_grade.add_widget(
                TextInput(text="agg", readonly=True, foreground_color=(1, 0, 1, 1), size_hint=(None, None),
                          size=(46, 29), allow_copy=True,
                          size_hint_y=.3))
            for i in v:
                self.mtc_grade.add_widget(
                    TextInput(text=i[i.index('_') + 1:].title(), foreground_color=(.4, 0, 1, 1), readonly=True,
                              allow_copy=True))
                self.mtc_grade.add_widget(
                    TextInput(text=ooo(i[1:i.index('_')]), readonly=True, foreground_color=(1, 0, 0, 1),
                              background_color=(1, .5, .5, 1),
                              size_hint=(None, None),
                              size=(46, 29), allow_copy=True))
                self.mtc_grade.add_widget(
                    TextInput(text=AGG(int(ooo(i[1:i.index('_')]))), readonly=True, foreground_color=(1, 0, 1, 1),
                              background_color=(1, 1, 0, 1),
                              size_hint=(None, None), size=(46, 29), allow_copy=True))
            self.grd_analys.add_widget(self.mtc_grade)
            del v
            del l
            #
            #

            self.eng_grade = GridLayout(cols=3, row_default_height=29, row_force_default=True)
            l = []
            for x in dict.keys():
                if not dict[x].get('marks'):
                    print('no marks', x)
                    pass
                else:

                    # if dict[x]['marks']['eng']['term1']['mgt1_ENG'] == '':
                    #     dict[x]['marks']['eng']['term1']['mgt1_ENG'] = "0"
                    if dict[x]['marks']['eng']['term' + self.Called]['mgt' + self.Called + '_ENG'] == '':
                        dict[x]['marks']['eng']['term' + self.Called]['mgt' + self.Called + '_ENG'] = "0"

                    num = dict[x]['marks']['eng']['term' + self.Called]['mgt' + self.Called + '_ENG']
                    if '.' in num:
                        if int(num[-1]) >= 5:
                            num = str(float(num[:num.index('.')]) + 1)
                            print('num', num)
                        if int(num[-1]) < 5:
                            num = str(float(num[:num.index('.')]))
                            print('num', num)
                        NM = num[:num.index('.')]

                    else:
                        NM = num
                    print('NM', NM)
                    if len(NM) == 1:
                        NM = "000" + NM
                    if len(NM) == 2:
                        NM = "00" + NM
                    if len(NM) == 3:
                        NM = "0" + NM

                    l.append(NM + "_" + x)
            l.sort()
            v = list(reversed(l))
            print('v', v)
            self.eng_grade.add_widget(TextInput(text='...', readonly=True, foreground_color=(1, 0, 0, 1)))
            self.eng_grade.add_widget(
                TextInput(text='mks', readonly=True, foreground_color=(1, 0, 0, 1), size_hint=(None, None),
                          size=(46, 29), allow_copy=True,
                          size_hint_y=.3))
            self.eng_grade.add_widget(
                TextInput(text="agg", readonly=True, foreground_color=(1, 0, 1, 1), size_hint=(None, None),
                          size=(46, 29), allow_copy=True,
                          size_hint_y=.3))
            for i in v:
                self.eng_grade.add_widget(
                    TextInput(text=i[i.index('_') + 1:].title(), foreground_color=(.4, 0, 1, 1), readonly=True,
                              allow_copy=True))
                self.eng_grade.add_widget(
                    TextInput(text=ooo(i[1:i.index('_')]), readonly=True, foreground_color=(1, 0, 0, 1),
                              background_color=(1, .5, .5, 1),
                              size_hint=(None, None), size=(46, 29), allow_copy=True))
                self.eng_grade.add_widget(
                    TextInput(text=AGG(int(ooo(i[1:i.index('_')]))), readonly=True, foreground_color=(1, 0, 1, 1),
                              background_color=(1, 1, 0, 1),
                              size_hint=(None, None), size=(46, 29), allow_copy=True))
            self.grd_analys.add_widget(self.eng_grade)
            del v
            del l
            #
            #

            self.sst_grade = GridLayout(cols=3, row_default_height=29, row_force_default=True)
            l = []
            for x in dict.keys():
                if not dict[x].get('marks'):
                    print('no marks', x)
                    pass
                else:

                    # if dict[x]['marks']['sst']['term1']['mgt1_SST'] == '':
                    #     dict[x]['marks']['sst']['term1']['mgt1_SST'] = "0"
                    if dict[x]['marks']['sst']['term' + self.Called]['mgt' + self.Called + '_SST'] == '':
                        dict[x]['marks']['sst']['term' + self.Called]['mgt' + self.Called + '_SST'] = "0"

                    num = dict[x]['marks']['sst']['term' + self.Called]['mgt' + self.Called + '_SST']
                    if '.' in num:
                        if int(num[-1]) >= 5:
                            num = str(float(num[:num.index('.')]) + 1)
                            print('num', num)
                        if int(num[-1]) < 5:
                            num = str(float(num[:num.index('.')]))
                            print('num', num)
                        NM = num[:num.index('.')]

                    else:
                        NM = num
                    print('NM', NM)
                    if len(NM) == 1:
                        NM = "000" + NM
                    if len(NM) == 2:
                        NM = "00" + NM
                    if len(NM) == 3:
                        NM = "0" + NM

                    l.append(NM + "_" + x)
            l.sort()
            v = list(reversed(l))
            self.sst_grade.add_widget(TextInput(text='...', readonly=True, foreground_color=(1, 0, 0, 1)))
            self.sst_grade.add_widget(
                TextInput(text='mks', readonly=True, foreground_color=(1, 0, 0, 1), size_hint=(None, None),
                          size=(46, 29), allow_copy=True,
                          size_hint_y=.3))
            self.sst_grade.add_widget(
                TextInput(text="agg", readonly=True, foreground_color=(1, 0, 1, 1), size_hint=(None, None),
                          size=(46, 29), allow_copy=True,
                          size_hint_y=.3))
            for i in v:
                self.sst_grade.add_widget(
                    TextInput(text=i[i.index('_') + 1:].title(), foreground_color=(.4, 0, 1, 1), readonly=True,
                              allow_copy=True))
                self.sst_grade.add_widget(
                    TextInput(text=ooo(i[1:i.index('_')]), readonly=True, foreground_color=(1, 0, 0, 1),
                              background_color=(1, .5, .5, 1),
                              size_hint=(None, None), size=(46, 29), allow_copy=True))
                self.sst_grade.add_widget(
                    TextInput(text=AGG(int(ooo(i[1:i.index('_')]))), readonly=True, foreground_color=(1, 0, 1, 1),
                              background_color=(1, 1, 0, 1),
                              size_hint=(None, None), size=(46, 29), allow_copy=True))
            self.grd_analys.add_widget(self.sst_grade)
            del v
            del l
            #
            #

            self.scie_grade = GridLayout(cols=3, row_default_height=29, row_force_default=True)
            l = []
            sz = 0
            for x in dict.keys():
                if not dict[x].get('marks'):
                    print('no marks', x)
                    pass
                else:

                    # if dict[x]['marks']['scie']['term1']['mgt1_SCIE'] == '':
                    #     dict[x]['marks']['scie']['term1']['mgt1_SCIE'] = "0"
                    if dict[x]['marks']['scie']['term' + self.Called]['mgt' + self.Called + '_SCIE'] == '':
                        dict[x]['marks']['scie']['term' + self.Called]['mgt' + self.Called + '_SCIE'] = "0"

                    num = dict[x]['marks']['scie']['term' + self.Called]['mgt' + self.Called + '_SCIE']
                    if '.' in num:
                        if int(num[-1]) >= 5:
                            num = str(float(num[:num.index('.')]) + 1)
                            print('num', num)
                        if int(num[-1]) < 5:
                            num = str(float(num[:num.index('.')]))
                            print('num', num)
                        NM = num[:num.index('.')]

                    else:
                        NM = num
                    print('NM', NM)
                    if len(NM) == 1:
                        NM = "000" + NM
                    if len(NM) == 2:
                        NM = "00" + NM
                    if len(NM) == 3:
                        NM = "0" + NM

                    l.append(NM + "_" + x)

            l.sort()
            v = list(reversed(l))
            self.scie_grade.add_widget(TextInput(text='...', readonly=True, foreground_color=(1, 0, 0, 1)))
            self.scie_grade.add_widget(
                TextInput(text='mks', readonly=True, foreground_color=(1, 0, 0, 1), size_hint=(None, None),
                          size=(46, 29), allow_copy=True,
                          size_hint_y=.3))
            self.scie_grade.add_widget(
                TextInput(text="agg", readonly=True, foreground_color=(1, 0, 1, 1), size_hint=(None, None),
                          size=(46, 29), allow_copy=True,
                          size_hint_y=.3))
            self.sz = 3
            for i in v:
                self.scie_grade.add_widget(
                    TextInput(text=i[i.index('_') + 1:].title(), foreground_color=(.4, 0, 1, 1), readonly=True,
                              allow_copy=True))
                self.scie_grade.add_widget(
                    TextInput(text=ooo(i[1:i.index('_')]), readonly=True, foreground_color=(1, 0, 0, 1),
                              background_color=(1, .5, .5, 1),
                              size_hint=(None, None), size=(46, 29), allow_copy=True))
                self.scie_grade.add_widget(
                    TextInput(text=AGG(int(ooo(i[1:i.index('_')]))), readonly=True, foreground_color=(1, 0, 1, 1),
                              background_color=(1, 1, 0, 1),
                              size_hint=(None, None), size=(46, 29), allow_copy=True))
                self.sz += 1
            self.grd_analys.add_widget(self.scie_grade)
            del v
            del l
            #
            # **********************************     TOTAL         ***********************************
            self.total_grade = GridLayout(cols=4, size_hint=(None, None), size=(370, 29), row_default_height=29,
                                          row_force_default=True)

            l = []
            for x in dict.keys():
                if not dict[x].get('marks'):
                    print('no marks', x)
                    pass
                else:

                    # if dict[x]['marks']['mtc']['term1']['mgt1'] == '':
                    #     dict[x]['marks']['mtc']['term1']['mgt1'] = "0"
                    if dict[x]['marks']['total']['term' + self.Called]['mgt' + self.Called + '_TT'] == '':
                        dict[x]['marks']['total']['term' + self.Called]['mgt' + self.Called + '_TT'] = "0"

                    num = dict[x]['marks']['total']['term' + self.Called]['mgt' + self.Called + '_TT']
                    if '.' in num:
                        if int(num[-1]) >= 5:
                            num = str(float(num[:num.index('.')]) + 1)
                            print('num', num)
                        if int(num[-1]) < 5:
                            num = str(float(num[:num.index('.')]))
                            print('num', num)
                        NM = num[:num.index('.')]

                    else:
                        NM = num
                    print('NM', NM)
                    if len(NM) == 1:
                        NM = "000" + NM
                    if len(NM) == 2:
                        NM = "00" + NM
                    if len(NM) == 3:
                        NM = "0" + NM

                    l.append(NM + "_" + x)

            l.sort()
            v = list(reversed(l))
            self.total_grade.add_widget(TextInput(text='...', readonly=True, foreground_color=(1, 0, 0, 1)))
            self.total_grade.add_widget(
                TextInput(text='mks', readonly=True, foreground_color=(1, 0, 0, 1), size_hint=(None, None),
                          size=(46, 29), allow_copy=True, size_hint_y=.3))
            self.total_grade.add_widget(
                TextInput(text="agg", readonly=True, foreground_color=(1, 0, 1, 1), size_hint=(None, None),
                          size=(46, 29), allow_copy=True, size_hint_y=.3))
            self.total_grade.add_widget(
                TextInput(text="DIV", readonly=True, foreground_color=(1, 0, 1, 1), size_hint=(None, None),
                          size=(60, 29), allow_copy=True, size_hint_y=.3))
            for i in v:
                print("vvv", v)
                self.total_grade.add_widget(
                    TextInput(text=i[i.index('_') + 1:].title(), foreground_color=(.4, 0, 1, 1), readonly=True,
                              allow_copy=True))
                self.total_grade.add_widget(
                    TextInput(text=ooo(i[1:i.index('_')]), readonly=True, background_color=(1, 0, 0, 1),
                              foreground_color=(1, 1, 1, 1),
                              size_hint=(None, None), size=(46, 29), allow_copy=True))
                self.total_grade.add_widget(TextInput(
                    text=dict[i[i.index('_') + 1:]]['marks']['total']['term' + self.Called][
                        'agt' + self.Called + '_TT'], readonly=True,
                    background_color=(0, 0, 0, 1), foreground_color=(1, 1, 0, 1), size_hint=(None, None), size=(46, 29),
                    allow_copy=True))
                if int(dict[i[i.index('_') + 1:]]['marks']['total']['term' + self.Called][
                           'agt' + self.Called + '_TT']) <= 12:
                    self.total_grade.add_widget(TextInput(text="DIV I", readonly=True, background_color=(0, 0, 0, 1),
                                                          foreground_color=(1, 1, 1, 1), size_hint=(None, None),
                                                          size=(60, 29), allow_copy=True))

                if int(dict[i[i.index('_') + 1:]]['marks']['total']['term' + self.Called][
                           'agt' + self.Called + '_TT']) >= 13 and int(
                        dict[i[i.index('_') + 1:]]['marks']['total']['term' + self.Called][
                            'agt' + self.Called + '_TT']) <= 24:
                    self.total_grade.add_widget(TextInput(text="DIV II", readonly=True, background_color=(0, 0, 0, 1),
                                                          foreground_color=(1, 1, 1, 1), size_hint=(None, None),
                                                          size=(60, 29), allow_copy=True))

                if int(dict[i[i.index('_') + 1:]]['marks']['total']['term' + self.Called][
                           'agt' + self.Called + '_TT']) >= 25 and int(
                        dict[i[i.index('_') + 1:]]['marks']['total']['term' + self.Called][
                            'agt' + self.Called + '_TT']) <= 28:
                    self.total_grade.add_widget(TextInput(text="DIV III", readonly=True, background_color=(0, 0, 0, 1),
                                                          foreground_color=(1, 1, 1, 1), size_hint=(None, None),
                                                          size=(60, 29), allow_copy=True))

                if int(dict[i[i.index('_') + 1:]]['marks']['total']['term' + self.Called][
                           'agt' + self.Called + '_TT']) >= 29 and int(
                        dict[i[i.index('_') + 1:]]['marks']['total']['term' + self.Called][
                            'agt' + self.Called + '_TT']) <= 30:
                    self.total_grade.add_widget(TextInput(text="DIV IV", readonly=True, background_color=(0, 0, 0, 1),
                                                          foreground_color=(1, 1, 1, 1), size_hint=(None, None),
                                                          size=(60, 29), allow_copy=True))

                if int(dict[i[i.index('_') + 1:]]['marks']['total']['term' + self.Called][
                           'agt' + self.Called + '_TT']) > 30:
                    self.total_grade.add_widget(TextInput(text="DIV U", readonly=True, background_color=(0, 0, 0, 1),
                                                          foreground_color=(1, 1, 1, 1), size_hint=(None, None),
                                                          size=(60, 29), allow_copy=True))

                # else:
                #     self.total_grade.add_widget(TextInput(text="xxx", readonly=True,foreground_color=(1, 0, 1, 1),size_hint=(None, None), size=(60, 29), allow_copy=True))

                # print(dict[i[i.index('_') + 1:]]['marks']['total']['term' + self.Called]['agt' + self.Called + '_TT'],
                #       i[i.index('_') + 1:].title())
            self.grd_analys.add_widget(self.total_grade)
            del v
            del l

        self.scrll.add_widget(self.grd_analys)
        self.add_widget(self.scrll)
        # self.scrll.size_hint_x=10

        # for i in v:
        #     self.re_grade.add_widget(TextInput(text='1  ' + "   " + i[i.index('_') + 1:], foreground_color=(1, 0, 0, 1), readonly=True,allow_copy=True))

    def p_rep(self, x):
        self.grd_analys.size_hint = (None, None)
        self.grd_analys.size = (1280, 29 * self.sz)
        Clock.schedule_once(self.RRP, 3)

    def RRP(self, x):
        self.grd_analys.export_to_png(NDR + 'Desktop' + PTH + 'P R I N T A B L E' + PTH + '' + self.CL.text + ".png")
        self.print_all_i(NDR + 'Desktop' + PTH + 'P R I N T A B L E' + PTH + '' + self.CL.text + ".png")

        # from PIL import Image

        # image_1 = Image.open(self.CL.text+".png")
        # im_1 = image_1.convert('RGB')
        # im_1.save(self.CL.text+".pdf")
    def r_teach(self,Sub,clas):
        if Sub == "" :
            return ""
        fN = open(DIR + 'media' + PTH + '0' + PTH + 'TDATA.json', 'r')
        DT = json.load(fN)
        fN.close()
        a=""
        for t in DT.keys():
            for LIS in DT[t]["SUBJECTS"].keys():
                if  LIS.strip().lower() == Sub.strip().lower() or Sub.strip().lower() in LIS.strip().lower() != "reading": # or Sub.strip().lower() in LIS.strip().lower()
                    for c in DT[t]["SUBJECTS"][LIS]:              # or Sub[:2].strip().lower() == LIS.strip().lower()
                        if c.lower().strip() in clas.lower() :
                            a=t


        return a

    def teachers(self, x):
        self.ww = 0
        self.add_widget(self.idd)
        self.idd.background_color = (.8, 0, 1, .9)
        # self.idd.background_normal="angel.png"
        Clock.schedule_interval(self.white, .05)
        self.gt = GridLayout(cols=1, size_hint=(.3, .8), pos_hint={'center_x': .13, 'center_y': .5})
        list = ["TODAY >", 'VIEW TEACHER >', 'ADD TEACHER >', 'EXTEND TIME TABLE >']
        for i in list:
            self.go = Button(text=i, color=(1, 1, .1, 1), bold=True, background_color=(0, 1, 0, .8),
                             background_normal="bb.png", on_release=self.callable)
            self.gt.add_widget(self.go)
        self.add_widget(self.gt)

        self.goback = Button(text='Back', color=(1, 0, 0, 1), size_hint=(.2, .1), on_release=self.home)
        self.goback.bind(on_release=self.Viewcleaner)
        self.idd.bind(on_release=self.Viewcleaner)
        self.add_widget(self.goback)



    def callable(self, t):
        Clock.schedule_once(self.cleaner, -1)
        l = 'self.' + t.text[:-2].replace(" ", "_")
        exec("Clock.schedule_once(" + l + ",0)")

    def EXTEND_TIME_TABLE(self, x):
        if not lv in ('sc', 'adm'):
            return

        if not os.path.isdir(DIR + 'media' + PTH + '0' + PTH + 'TABLE' + PTH + '' + time.strftime('%Y')):
            os.makedirs(DIR + 'media' + PTH + '0' + PTH + 'TABLE' + PTH + '' + time.strftime('%Y'))

        self.idd.background_color = (.4, 0, 1, .9)
        l = Clss()
        self.scrolltable = ScrollView(size_hint=(.65, 1.), pos_hint={'center_x': .62, 'center_y': .5},
                                      do_scroll_x=False, do_scroll_y=True, scroll_type=['bars', 'content'],
                                      bar_width=10, bar_color=(1, 1, 0, 1), bar_margin=0)
        self.autobind('self.scrolltable')
        self.gEXT = GridLayout(cols=2, spacing=19, size_hint=(1., 1.8), row_default_height=40, row_force_default=True)
        self.gmdyc = GridLayout(cols=4, size_hint=(1., .14), row_default_height=40, row_force_default=True)
        self.gmdyc.add_widget(Label(text="CLASS"))
        self.gmdyc.add_widget(Label(text="MONTH"))
        self.gmdyc.add_widget(Label(text="DAY"))
        self.gmdyc.add_widget(Label(text="YEAR"))

        self.Cll = Spinner(text=Clss()[-1], values=tuple(l))
        self.Cll.bind(text=self.iko)
        self.gmdyc.add_widget(self.Cll)
        self.mnt = Spinner(text=time.strftime('%B'), values=tuple(
            ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
             'November', 'December']))
        self.mnt.bind(text=self.iko)
        self.mnt.bind(text=self.m31)
        self.gmdyc.add_widget(self.mnt)
        self.DY = Spinner(text=time.strftime('%A'),
                          values=("Monday", "Tuesday", "Wednesday", "Thurday", "Friday", "Saturday", "Sunday"))
        self.DY.bind(text=self.iko)
        self.gmdyc.add_widget(self.DY)
        an = range(2022, 2051)
        bb = []
        for ii in an:
            bb.append(str(ii))

        self.YR = Spinner(text=time.strftime('%Y'), values=tuple(bb))
        self.YR.bind(text=self.iko)
        self.gmdyc.add_widget(self.YR)
        #############################################SPACE
        self.Simportc = Spinner(text="Import from Class", values=tuple(Clss()), background_color=(.55, 0, .23, .6), )
        self.Simportc.bind(text=self.IMPC)
        self.gmdyc.add_widget(self.Simportc)
        self.gmdyc.add_widget(Label(text=""))

        self.Simportd = Spinner(text="Import from Date", values=("Month", "Day"), background_color=(.55, 0, .23, .6), )
        self.Simportd.bind(text=self.m31)
        self.gmdyc.add_widget(self.Simportd)
        self.gmdyc.add_widget(Label(text=""))

        #################################################
        self.gmdyc.add_widget(Label(text="HOUR"))
        self.gmdyc.add_widget(Label(text="SUBJECT"))
        self.gmdyc.add_widget(Label(text="BOOK/PAGE"))
        self.gmdyc.add_widget(Label(text="TEACHER"))
        #########################################################
        # self.gmdyc.add_widget(Label(text=""))
        # self.gmdyc.add_widget(Label(text=""))
        # self.gmdyc.add_widget(Label(text=""))
        # self.gmdyc.add_widget(Label(text=""))
        # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        self.eit = TextInput(text='6:30', background_color=(.4, 0, 1, .9), foreground_color=(1, 1, 1, 1))
        self.c8 = TextInput(allow_copy=True, foreground_color=(.55, 0, .23, 1))
        self.p8 = TextInput(allow_copy=True, foreground_color=(.55, 0, .23, 1))
        self.t8 = TextInput(allow_copy=True, foreground_color=(.55, 0, .23, 1))
        self.c8.bind(text=self.MAKE)
        self.p8.bind(text=self.MAKE)
        self.t8.bind(text=self.MAKE)

        self.gmdyc.add_widget(self.eit)
        self.gmdyc.add_widget(self.c8)
        self.gmdyc.add_widget(self.p8)
        self.gmdyc.add_widget(self.t8)

        self.nine = TextInput(text='7:10', background_color=(.4, 0, 1, .9), foreground_color=(1, 1, 1, 1))
        self.c9 = TextInput(allow_copy=True, foreground_color=(.55, 0, .23, 1))
        self.p9 = TextInput(allow_copy=True, foreground_color=(.55, 0, .23, 1))
        self.t9 = TextInput(allow_copy=True, foreground_color=(.55, 0, .23, 1))
        self.c9.bind(text=self.MAKE)
        self.p9.bind(text=self.MAKE)
        self.t9.bind(text=self.MAKE)
        self.gmdyc.add_widget(self.nine)
        self.gmdyc.add_widget(self.c9)
        self.gmdyc.add_widget(self.p9)
        self.gmdyc.add_widget(self.t9)

        self.ten = TextInput(text='7:50', background_color=(.4, 0, 1, .9), foreground_color=(1, 1, 1, 1))
        self.c10 = TextInput(allow_copy=True, foreground_color=(.55, 0, .23, 1))
        self.p10 = TextInput(allow_copy=True, foreground_color=(.55, 0, .23, 1))
        self.t10 = TextInput(allow_copy=True, foreground_color=(.55, 0, .23, 1))
        self.c10.bind(text=self.MAKE)
        self.p10.bind(text=self.MAKE)
        self.t10.bind(text=self.MAKE)
        self.gmdyc.add_widget(self.ten)
        self.gmdyc.add_widget(self.c10)
        self.gmdyc.add_widget(self.p10)
        self.gmdyc.add_widget(self.t10)

        self.elev = TextInput(text='8:30', background_color=(.4, 0, 1, .9), foreground_color=(1, 1, 1, 1))
        self.c11 = TextInput(allow_copy=True, foreground_color=(.55, 0, .23, 1))
        self.p11 = TextInput(allow_copy=True, foreground_color=(.55, 0, .23, 1))
        self.t11 = TextInput(allow_copy=True, foreground_color=(.55, 0, .23, 1))
        self.c11.bind(text=self.MAKE)
        self.p11.bind(text=self.MAKE)
        self.t11.bind(text=self.MAKE)
        self.gmdyc.add_widget(self.elev)
        self.gmdyc.add_widget(self.c11)
        self.gmdyc.add_widget(self.p11)
        self.gmdyc.add_widget(self.t11)

        self.twel = TextInput(text='9:10', background_color=(.4, 0, 1, .9), foreground_color=(1, 1, 1, 1))
        self.c12 = TextInput(allow_copy=True, foreground_color=(.55, 0, .23, 1))
        self.p12 = TextInput(allow_copy=True, foreground_color=(.55, 0, .23, 1))
        self.t12 = TextInput(allow_copy=True, foreground_color=(.55, 0, .23, 1))
        self.c12.bind(text=self.MAKE)
        self.p12.bind(text=self.MAKE)
        self.t12.bind(text=self.MAKE)
        self.gmdyc.add_widget(self.twel)
        self.gmdyc.add_widget(self.c12)
        self.gmdyc.add_widget(self.p12)
        self.gmdyc.add_widget(self.t12)

        self.thirt = TextInput(text='9:50', background_color=(.4, 0, 1, .9), foreground_color=(1, 1, 1, 1))
        self.c13 = TextInput(allow_copy=True, foreground_color=(.55, 0, .23, 1))
        self.p13 = TextInput(allow_copy=True, foreground_color=(.55, 0, .23, 1))
        self.t13 = TextInput(allow_copy=True, foreground_color=(.55, 0, .23, 1))
        self.c13.bind(text=self.MAKE)
        self.p13.bind(text=self.MAKE)
        self.t13.bind(text=self.MAKE)
        self.gmdyc.add_widget(self.thirt)
        self.gmdyc.add_widget(self.c13)
        self.gmdyc.add_widget(self.p13)
        self.gmdyc.add_widget(self.t13)

        self.forten = TextInput(text='10:30', background_color=(.4, 0, 1, .9), foreground_color=(1, 1, 1, 1))
        self.c14 = TextInput(allow_copy=True, foreground_color=(.55, 0, .23, 1))
        self.p14 = TextInput(allow_copy=True, foreground_color=(.55, 0, .23, 1))
        self.t14 = TextInput(allow_copy=True, foreground_color=(.55, 0, .23, 1))
        self.c14.bind(text=self.MAKE)
        self.p14.bind(text=self.MAKE)
        self.t14.bind(text=self.MAKE)
        self.gmdyc.add_widget(self.forten)
        self.gmdyc.add_widget(self.c14)
        self.gmdyc.add_widget(self.p14)
        self.gmdyc.add_widget(self.t14)

        self.fift = TextInput(text='11:10', background_color=(.4, 0, 1, .9), foreground_color=(1, 1, 1, 1))
        self.c15 = TextInput(allow_copy=True, foreground_color=(.55, 0, .23, 1))
        self.p15 = TextInput(allow_copy=True, foreground_color=(.55, 0, .23, 1))
        self.t15 = TextInput(allow_copy=True, foreground_color=(.55, 0, .23, 1))
        self.c15.bind(text=self.MAKE)
        self.p15.bind(text=self.MAKE)
        self.t15.bind(text=self.MAKE)
        self.gmdyc.add_widget(self.fift)
        self.gmdyc.add_widget(self.c15)
        self.gmdyc.add_widget(self.p15)
        self.gmdyc.add_widget(self.t15)

        self.sixt = TextInput(text='11:50', background_color=(.4, 0, 1, .9), foreground_color=(1, 1, 1, 1))
        self.c16 = TextInput(allow_copy=True, foreground_color=(.55, 0, .23, 1))
        self.p16 = TextInput(allow_copy=True, foreground_color=(.55, 0, .23, 1))
        self.t16 = TextInput(allow_copy=True, foreground_color=(.55, 0, .23, 1))
        self.c16.bind(text=self.MAKE)
        self.p16.bind(text=self.MAKE)
        self.t16.bind(text=self.MAKE)
        self.gmdyc.add_widget(self.sixt)
        self.gmdyc.add_widget(self.c16)
        self.gmdyc.add_widget(self.p16)
        self.gmdyc.add_widget(self.t16)

        self.seven = TextInput(text='12:30', background_color=(.4, 0, 1, .9), foreground_color=(1, 1, 1, 1))
        self.c17 = TextInput(allow_copy=True, foreground_color=(.55, 0, .23, 1))
        self.p17 = TextInput(allow_copy=True, foreground_color=(.55, 0, .23, 1))
        self.t17 = TextInput(allow_copy=True, foreground_color=(.55, 0, .23, 1))
        self.c17.bind(text=self.MAKE)
        self.p17.bind(text=self.MAKE)
        self.t17.bind(text=self.MAKE)
        self.gmdyc.add_widget(self.seven)
        self.gmdyc.add_widget(self.c17)
        self.gmdyc.add_widget(self.p17)
        self.gmdyc.add_widget(self.t17)
        # TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT

        self.eiten = TextInput(text='13:10', background_color=(.4, 0, 1, .9), foreground_color=(1, 1, 1, 1))
        self.c18 = TextInput(allow_copy=True, foreground_color=(.55, 0, .23, 1))
        self.p18 = TextInput(allow_copy=True, foreground_color=(.55, 0, .23, 1))
        self.t18 = TextInput(allow_copy=True, foreground_color=(.55, 0, .23, 1))
        self.c18.bind(text=self.MAKE)
        self.p18.bind(text=self.MAKE)
        self.t18.bind(text=self.MAKE)

        self.gmdyc.add_widget(self.eiten)
        self.gmdyc.add_widget(self.c18)
        self.gmdyc.add_widget(self.p18)
        self.gmdyc.add_widget(self.t18)

        self.nineten = TextInput(text='13:50', background_color=(.4, 0, 1, .9), foreground_color=(1, 1, 1, 1))
        self.c19 = TextInput(allow_copy=True, foreground_color=(.55, 0, .23, 1))
        self.p19 = TextInput(allow_copy=True, foreground_color=(.55, 0, .23, 1))
        self.t19 = TextInput(allow_copy=True, foreground_color=(.55, 0, .23, 1))
        self.c19.bind(text=self.MAKE)
        self.p19.bind(text=self.MAKE)
        self.t19.bind(text=self.MAKE)
        self.gmdyc.add_widget(self.nineten)
        self.gmdyc.add_widget(self.c19)
        self.gmdyc.add_widget(self.p19)
        self.gmdyc.add_widget(self.t19)

        self.twe = TextInput(text='14:30', background_color=(.4, 0, 1, .9), foreground_color=(1, 1, 1, 1))
        self.c20 = TextInput(allow_copy=True, foreground_color=(.55, 0, .23, 1))
        self.p20 = TextInput(allow_copy=True, foreground_color=(.55, 0, .23, 1))
        self.t20 = TextInput(allow_copy=True, foreground_color=(.55, 0, .23, 1))
        self.c20.bind(text=self.MAKE)
        self.p20.bind(text=self.MAKE)
        self.t20.bind(text=self.MAKE)
        self.gmdyc.add_widget(self.twe)
        self.gmdyc.add_widget(self.c20)
        self.gmdyc.add_widget(self.p20)
        self.gmdyc.add_widget(self.t20)

        self.twe1 = TextInput(text='15:10', background_color=(.4, 0, 1, .9), foreground_color=(1, 1, 1, 1))
        self.c21 = TextInput(allow_copy=True, foreground_color=(.55, 0, .23, 1))
        self.p21 = TextInput(allow_copy=True, foreground_color=(.55, 0, .23, 1))
        self.t21 = TextInput(allow_copy=True, foreground_color=(.55, 0, .23, 1))
        self.c21.bind(text=self.MAKE)
        self.p21.bind(text=self.MAKE)
        self.t21.bind(text=self.MAKE)
        self.gmdyc.add_widget(self.twe1)
        self.gmdyc.add_widget(self.c21)
        self.gmdyc.add_widget(self.p21)
        self.gmdyc.add_widget(self.t21)

        self.twe2 = TextInput(text='15:50', background_color=(.4, 0, 1, .9), foreground_color=(1, 1, 1, 1))
        self.c22 = TextInput(allow_copy=True, foreground_color=(.55, 0, .23, 1))
        self.p22 = TextInput(allow_copy=True, foreground_color=(.55, 0, .23, 1))
        self.t22 = TextInput(allow_copy=True, foreground_color=(.55, 0, .23, 1))
        self.c22.bind(text=self.MAKE)
        self.p22.bind(text=self.MAKE)
        self.t22.bind(text=self.MAKE)
        self.gmdyc.add_widget(self.twe2)
        self.gmdyc.add_widget(self.c22)
        self.gmdyc.add_widget(self.p22)
        self.gmdyc.add_widget(self.t22)

        self.twe3 = TextInput(text='16:30', background_color=(.4, 0, 1, .9), foreground_color=(1, 1, 1, 1))
        self.c23 = TextInput(allow_copy=True, foreground_color=(.55, 0, .23, 1))
        self.p23 = TextInput(allow_copy=True, foreground_color=(.55, 0, .23, 1))
        self.t23 = TextInput(allow_copy=True, foreground_color=(.55, 0, .23, 1))
        self.c23.bind(text=self.MAKE)
        self.p23.bind(text=self.MAKE)
        self.t23.bind(text=self.MAKE)
        self.gmdyc.add_widget(self.twe3)
        self.gmdyc.add_widget(self.c23)
        self.gmdyc.add_widget(self.p23)
        self.gmdyc.add_widget(self.t23)

        self.twe4 = TextInput(text='17:10', background_color=(.4, 0, 1, .9), foreground_color=(1, 1, 1, 1))
        self.c24 = TextInput(allow_copy=True, foreground_color=(.55, 0, .23, 1))
        self.p24 = TextInput(allow_copy=True, foreground_color=(.55, 0, .23, 1))
        self.t24 = TextInput(allow_copy=True, foreground_color=(.55, 0, .23, 1))
        self.c24.bind(text=self.MAKE)
        self.p24.bind(text=self.MAKE)
        self.t24.bind(text=self.MAKE)
        self.gmdyc.add_widget(self.twe4)
        self.gmdyc.add_widget(self.c24)
        self.gmdyc.add_widget(self.p24)
        self.gmdyc.add_widget(self.t24)

        self.twe5 = TextInput(text='17:50', background_color=(.4, 0, 1, .9), foreground_color=(1, 1, 1, 1))
        self.c25 = TextInput(allow_copy=True, foreground_color=(.55, 0, .23, 1))
        self.p25 = TextInput(allow_copy=True, foreground_color=(.55, 0, .23, 1))
        self.t25 = TextInput(allow_copy=True, foreground_color=(.55, 0, .23, 1))
        self.c25.bind(text=self.MAKE)
        self.p25.bind(text=self.MAKE)
        self.t25.bind(text=self.MAKE)
        self.gmdyc.add_widget(self.twe5)
        self.gmdyc.add_widget(self.c25)
        self.gmdyc.add_widget(self.p25)
        self.gmdyc.add_widget(self.t25)

        self.twe6 = TextInput(text='18:30', background_color=(.4, 0, 1, .9), foreground_color=(1, 1, 1, 1))
        self.c26 = TextInput(allow_copy=True, foreground_color=(.55, 0, .23, 1))
        self.p26 = TextInput(allow_copy=True, foreground_color=(.55, 0, .23, 1))
        self.t26 = TextInput(allow_copy=True, foreground_color=(.55, 0, .23, 1))
        self.c26.bind(text=self.MAKE)
        self.p26.bind(text=self.MAKE)
        self.t26.bind(text=self.MAKE)
        self.gmdyc.add_widget(self.twe6)
        self.gmdyc.add_widget(self.c26)
        self.gmdyc.add_widget(self.p26)
        self.gmdyc.add_widget(self.t26)

        self.twe7 = TextInput(text='19:10', background_color=(.4, 0, 1, .9), foreground_color=(1, 1, 1, 1))
        self.c27 = TextInput(allow_copy=True, foreground_color=(.55, 0, .23, 1))
        self.p27 = TextInput(allow_copy=True, foreground_color=(.55, 0, .23, 1))
        self.t27 = TextInput(allow_copy=True, foreground_color=(.55, 0, .23, 1))
        self.c27.bind(text=self.MAKE)
        self.p27.bind(text=self.MAKE)
        self.t27.bind(text=self.MAKE)
        self.gmdyc.add_widget(self.twe7)
        self.gmdyc.add_widget(self.c27)
        self.gmdyc.add_widget(self.p27)
        self.gmdyc.add_widget(self.t27)
        #   TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
        # self.gmdyc.add_widget(self.)
        self.gEXT.add_widget(self.gmdyc)
        self.scrolltable.add_widget(self.gEXT)
        self.add_widget(self.scrolltable)
        self.gtable = GridLayout(cols=3)
        Clock.schedule_once(self.iko)

    def iko(self, sp, t=None):
        if not os.path.isdir(DIR + 'media' + PTH + '0' + PTH + 'TABLE'):
            os.system('mkdir ' + DIR + 'media' + PTH + '0' + PTH + 'TABLE')
        if not os.path.isdir(DIR + 'media' + PTH + '0' + PTH + 'TABLE' + PTH + '' + self.YR.text):
            os.system('mkdir ' + DIR + 'media' + PTH + '0' + PTH + 'TABLE' + PTH + '' + self.YR.text)
        if not os.path.isdir(
                DIR + 'media' + PTH + '0' + PTH + 'TABLE' + PTH + self.YR.text + PTH + self.Cll.text.strip()):
            os.system(
                'mkdir ' + DIR + 'media' + PTH + '0' + PTH + 'TABLE' + PTH + '' + self.YR.text + PTH + self.Cll.text.strip())
        if not os.path.isfile(
                DIR + 'media' + PTH + '0' + PTH + 'TABLE' + PTH + '' + self.YR.text + PTH + self.Cll.text.strip() + PTH + self.mnt.text + '.json'):
            dt = open(
                DIR + 'media' + PTH + '0' + PTH + 'TABLE' + PTH + '' + self.YR.text + '' + PTH + '' + self.Cll.text.strip() + '' + PTH + '' + self.mnt.text + '.json',
                'w')
            dc = {}
            json.dump(dc, dt)
            dt.close()
            print('os.system')

        if os.path.isfile(
                DIR + 'media' + PTH + '0' + PTH + 'TABLE' + PTH + '' + self.YR.text + '' + PTH + '' + self.Cll.text.strip() + '' + PTH + '' + self.mnt.text + '.json'):
            nf = open(
                DIR + 'media' + PTH + '0' + PTH + 'TABLE' + PTH + '' + self.YR.text + '' + PTH + '' + self.Cll.text.strip() + '' + PTH + '' + self.mnt.text + '.json',
                'r')
            DT = json.load(nf)
            nf.close()
            if DT.get(self.DY.text, 0):
                self.eit.text = DT[self.DY.text]["08"]["time"]
                self.c8.text = DT[self.DY.text]["08"]['course']
                self.p8.text = DT[self.DY.text]["08"]['page']
                self.t8.text = DT[self.DY.text]["08"]['teacher']

                self.nine.text = DT[self.DY.text]["09"]["time"]
                self.c9.text = DT[self.DY.text]['09']['course']
                self.p9.text = DT[self.DY.text]['09']['page']
                self.t9.text = DT[self.DY.text]['09']['teacher']

                self.ten.text = DT[self.DY.text]["10"]["time"]
                self.c10.text = DT[self.DY.text]["10"]['course']
                self.p10.text = DT[self.DY.text]['10']['page']
                self.t10.text = DT[self.DY.text]['10']['teacher']

                self.elev.text = DT[self.DY.text]["11"]["time"]
                self.c11.text = DT[self.DY.text]['11']['course']
                self.p11.text = DT[self.DY.text]['11']['page']
                self.t11.text = DT[self.DY.text]['11']['teacher']

                self.twel.text = DT[self.DY.text]["12"]["time"]
                self.c12.text = DT[self.DY.text]['12']['course']
                self.p12.text = DT[self.DY.text]['12']['page']
                self.t12.text = DT[self.DY.text]['12']['teacher']

                self.thirt.text = DT[self.DY.text]["13"]["time"]
                self.c13.text = DT[self.DY.text]['13']['course']
                self.p13.text = DT[self.DY.text]['13']['page']
                self.t13.text = DT[self.DY.text]['13']['teacher']

                self.forten.text = DT[self.DY.text]["14"]["time"]
                self.c14.text = DT[self.DY.text]['14']['course']
                self.p14.text = DT[self.DY.text]['14']['page']
                self.t14.text = DT[self.DY.text]['14']['teacher']

                self.fift.text = DT[self.DY.text]["15"]["time"]
                self.c15.text = DT[self.DY.text]['15']['course']
                self.p15.text = DT[self.DY.text]['15']['page']
                self.t15.text = DT[self.DY.text]['15']['teacher']

                self.sixt.text = DT[self.DY.text]["16"]["time"]
                self.c16.text = DT[self.DY.text]['16']['course']
                self.p16.text = DT[self.DY.text]['16']['page']
                self.t16.text = DT[self.DY.text]['16']['teacher']

                self.seven.text = DT[self.DY.text]["17"]["time"]
                self.c17.text = DT[self.DY.text]["17"]['course']
                self.p17.text = DT[self.DY.text]["17"]['page']
                self.t17.text = DT[self.DY.text]["17"]['teacher']
                #
                self.eiten.text = DT[self.DY.text]["18"]["time"]
                self.c18.text = DT[self.DY.text]["18"]['course']
                self.p18.text = DT[self.DY.text]["18"]['page']
                self.t18.text = DT[self.DY.text]["18"]['teacher']

                self.nineten.text = DT[self.DY.text]["19"]["time"]
                self.c19.text = DT[self.DY.text]["19"]['course']
                self.p19.text = DT[self.DY.text]["19"]['page']
                self.t19.text = DT[self.DY.text]["19"]['teacher']

                self.twe.text = DT[self.DY.text]["20"]["time"]
                self.c20.text = DT[self.DY.text]["20"]['course']
                self.p20.text = DT[self.DY.text]["20"]['page']
                self.t20.text = DT[self.DY.text]["20"]['teacher']

                self.twe1.text = DT[self.DY.text]["21"]["time"]
                self.c21.text = DT[self.DY.text]["21"]['course']
                self.p21.text = DT[self.DY.text]["21"]['page']
                self.t21.text = DT[self.DY.text]["21"]['teacher']

                self.twe2.text = DT[self.DY.text]["22"]["time"]
                self.c22.text = DT[self.DY.text]["22"]['course']
                self.p22.text = DT[self.DY.text]["22"]['page']
                self.t22.text = DT[self.DY.text]["22"]['teacher']

                self.twe3.text = DT[self.DY.text]["23"]["time"]
                self.c23.text = DT[self.DY.text]["23"]['course']
                self.p23.text = DT[self.DY.text]["23"]['page']
                self.t23.text = DT[self.DY.text]["23"]['teacher']

                self.twe4.text = DT[self.DY.text]["24"]["time"]
                self.c24.text = DT[self.DY.text]["24"]['course']
                self.p24.text = DT[self.DY.text]["24"]['page']
                self.t24.text = DT[self.DY.text]["24"]['teacher']

                self.twe5.text = DT[self.DY.text]["25"]["time"]
                self.c25.text = DT[self.DY.text]["25"]['course']
                self.p25.text = DT[self.DY.text]["25"]['page']
                self.t25.text = DT[self.DY.text]["25"]['teacher']

                self.twe6.text = DT[self.DY.text]["26"]["time"]
                self.c26.text = DT[self.DY.text]["26"]['course']
                self.p26.text = DT[self.DY.text]["26"]['page']
                self.t26.text = DT[self.DY.text]["26"]['teacher']

                self.twe7.text = DT[self.DY.text]["27"]["time"]
                self.c27.text = DT[self.DY.text]["27"]['course']
                self.p27.text = DT[self.DY.text]["27"]['page']
                self.t27.text = DT[self.DY.text]["27"]['teacher']

                six = ['parade', 'rem', ]
                nine = ['breakfast']
                ten = ["assembly", 'fellowship', 'breakfast', 'break', 'lunch']
                deba = ['debate']
                end = ['general', 'cleaning', 'clean', 'gen']
                even = ['even', 'evening']

                v = [self.c8, self.c9, self.c10, self.c11, self.c12, self.c14, self.c13, self.c15, self.c16, self.c17,
                     self.c18,
                     self.c19, self.c20,
                     self.c21, self.c22, self.c23, self.c24, self.c25, self.c26, self.c27]
                pl = [self.p8, self.p9, self.p10, self.p11, self.p12, self.p14, self.p13, self.p15, self.p16, self.p17,
                      self.p18, self.p19, self.p20,
                      self.p21, self.p22, self.p23, self.p24, self.p25, self.p26, self.p27]
                tl = [self.t8, self.t9, self.t10, self.t11, self.t12, self.t14, self.t13, self.t15, self.t16, self.t17,
                      self.t18, self.t19, self.t20,
                      self.t21, self.t22, self.t23, self.t24, self.t25, self.t26, self.t27]

                for i in v:
                    if i.text.lower() in six:
                        i.background_color = (0, 1, 0, 1)
                    if i.text.lower() in nine:
                        i.background_color = (0, 0, 1, 1)
                    if i.text.lower() in ten:
                        i.background_color = (1, 0, 1, 1)
                    if i.text.lower() in deba:
                        i.background_color = (1, 1, 0, 1)
                    if i.text.lower() in even:
                        i.background_color = (1, .5, .5, 1)
                    if i.text.lower() in end:
                        i.background_color = (1, 0, 0, 1)
                    if i.text == "":
                        i.background_color = (1, 1, 1, 1)
                for z in pl:
                    if z.text.lower() in six:
                        z.background_color = (0, 1, 0, 1)
                    if z.text.lower() in nine:
                        z.background_color = (0, 0, 1, 1)
                    if z.text.lower() in ten:
                        z.background_color = (1, 0, 1, 1)
                    if z.text.lower() in deba:
                        z.background_color = (1, 1, 0, 1)
                    if z.text.lower() in even:
                        z.background_color = (1, .5, .5, 1)
                    if z.text.lower() in end:
                        z.background_color = (1, 0, 0, 1)
                    if z.text == "":
                        z.background_color = (1, 1, 1, 1)

                for m in tl:
                    if m.text.lower() in six:
                        m.background_color = (0, 1, 0, 1)
                    if m.text.lower() in nine:
                        m.background_color = (0, 0, 1, 1)
                    if m.text.lower() in ten:
                        m.background_color = (1, 0, 1, 1)
                    if m.text.lower() in deba:
                        m.background_color = (1, 1, 0, 1)
                    if m.text.lower() in even:
                        m.background_color = (1, .5, .5, 1)
                    if m.text.lower() in end:
                        m.background_color = (1, 0, 0, 1)
                    if m.text == "":
                        m.background_color = (1, 1, 1, 1)



                del six
                del nine
                del ten
                del deba
                del even
                del end



            else:
                x = 8
                for i in range(20):
                    exec("self.c" + str(x) + ".background_color=(1,1,1,1)")
                    exec("self.p" + str(x) + ".background_color=(1,1,1,1)")
                    exec("self.t" + str(x) + ".background_color=(1,1,1,1)")
                    exec("self.c" + str(x) + ".text=''")
                    exec("self.p" + str(x) + ".text=''")
                    exec("self.t" + str(x) + ".text=''")
                    x += 1
        else:
            x = 8
            for i in range(20):
                exec("self.c" + str(x) + ".background_color=(1,1,1,1)")
                exec("self.p" + str(x) + ".background_color=(1,1,1,1)")
                exec("self.t" + str(x) + ".background_color=(1,1,1,1)")
                exec("self.c" + str(x) + ".text=''")
                exec("self.p" + str(x) + ".text=''")
                exec("self.t" + str(x) + ".text=''")
                x += 1

        cnt = 8
        for i in range(20):
            exec("self.t" + str(cnt) + ".text=self.r_teach(self.c" + str(cnt) + ".text ,  self.Cll.text ).upper()")
            cnt += 1
    def MAKE(self, made, t):

        fN = open(
            DIR + 'media' + PTH + '0' + PTH + 'TABLE' + PTH + '' + self.YR.text + PTH + self.Cll.text.strip() + PTH + self.mnt.text + '.json',
            'r')
        fina = json.load(fN)
        fN.close()
        if fina.get(self.DY.text, 0) == 0:
            fina[self.DY.text] = {}

        fina[self.DY.text]["08"] = {"course": self.c8.text,
                                    "time": self.eit.text,
                                    'page': self.p8.text,
                                    'teacher': self.t8.text}

        fina[self.DY.text]["09"] = {
            "course": self.c9.text,
            "time": self.nine.text,
            'page': self.p9.text,
            'teacher': self.t9.text}

        fina[self.DY.text]["10"] = {
            "course": self.c10.text,
            "time": self.ten.text,
            'page': self.p10.text,
            'teacher': self.t10.text}

        fina[self.DY.text]["11"] = {
            "course": self.c11.text,
            "time": self.elev.text,
            'page': self.p11.text,
            'teacher': self.t11.text}

        fina[self.DY.text]["12"] = {
            "course": self.c12.text,
            "time": self.twel.text,
            'page': self.p12.text,
            'teacher': self.t12.text}

        fina[self.DY.text]["13"] = {
            "course": self.c13.text,
            "time": self.thirt.text,
            'page': self.p13.text,
            'teacher': self.t13.text}

        fina[self.DY.text]["14"] = {
            "course": self.c14.text,
            "time": self.forten.text,
            'page': self.p14.text,
            'teacher': self.t14.text}

        fina[self.DY.text]["15"] = {
            "course": self.c15.text,
            "time": self.fift.text,
            'page': self.p15.text,
            'teacher': self.t15.text}

        fina[self.DY.text]["16"] = {
            "course": self.c16.text,
            "time": self.sixt.text,
            'page': self.p16.text,
            'teacher': self.t16.text}

        fina[self.DY.text]["17"] = {
            "course": self.c17.text,
            "time": self.seven.text,
            'page': self.p17.text,
            'teacher': self.t17.text}

        fina[self.DY.text]["18"] = {"course": self.c18.text,
                                    "time": self.eiten.text,
                                    'page': self.p18.text,
                                    'teacher': self.t18.text}

        fina[self.DY.text]["19"] = {
            "course": self.c19.text,
            "time": self.nineten.text,
            'page': self.p19.text,
            'teacher': self.t19.text}

        fina[self.DY.text]["20"] = {
            "course": self.c20.text,
            "time": self.twe.text,
            'page': self.p20.text,
            'teacher': self.t20.text}

        fina[self.DY.text]["21"] = {
            "course": self.c21.text,
            "time": self.twe1.text,
            'page': self.p21.text,
            'teacher': self.t21.text}

        fina[self.DY.text]["22"] = {
            "course": self.c22.text,
            "time": self.twe2.text,
            'page': self.p22.text,
            'teacher': self.t22.text}

        fina[self.DY.text]["23"] = {
            "course": self.c23.text,
            "time": self.twe3.text,
            'page': self.p23.text,
            'teacher': self.t23.text}

        fina[self.DY.text]["24"] = {
            "course": self.c24.text,
            "time": self.twe4.text,
            'page': self.p24.text,
            'teacher': self.t24.text}

        fina[self.DY.text]["25"] = {
            "course": self.c25.text,
            "time": self.twe5.text,
            'page': self.p25.text,
            'teacher': self.t25.text}

        fina[self.DY.text]["26"] = {
            "course": self.c26.text,
            "time": self.twe6.text,
            'page': self.p26.text,
            'teacher': self.t26.text}

        fina[self.DY.text]["27"] = {
            "course": self.c27.text,
            "time": self.twe7.text,
            'page': self.p27.text,
            'teacher': self.t27.text}

        # print(self.r_teach("mtc","P7 "))
        #
        # cnt = 8
        # for i in range(20):
        #     exec("self.t" + str(cnt) + ".text=self.r_teach(self.c" + str(cnt) + ".text," + self.Cll.text+")")
        #     cnt += 1
        # YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY
        FF = open(
            DIR + 'media' + PTH + '0' + PTH + 'TABLE' + PTH + '' + self.YR.text + PTH + self.Cll.text.strip() + PTH + self.mnt.text + '.json',
            'w')
        json.dump(fina, FF)
        FF.close()

        six = ['parade', 'rem', ]
        nine = ['breakfast']
        ten = ["assembly", 'fellowship', 'breakfast', 'break', 'lunch']
        deba = ['debate']
        end = ['general', 'cleaning', 'clean', 'gen']
        even = ['even', 'evening']

        v = [self.c8, self.c9, self.c10, self.c11, self.c12, self.c14, self.c13, self.c15, self.c16, self.c17, self.c18,
             self.c19, self.c20,
             self.c21, self.c22, self.c23, self.c24, self.c25, self.c26, self.c27]
        pl = [self.p8, self.p9, self.p10, self.p11, self.p12, self.p14, self.p13, self.p15, self.p16, self.p17,
              self.p18, self.p19, self.p20,
              self.p21, self.p22, self.p23, self.p24, self.p25, self.p26, self.p27]
        tl = [self.t8, self.t9, self.t10, self.t11, self.t12, self.t14, self.t13, self.t15, self.t16, self.t17,
              self.t18, self.t19, self.t20,
              self.t21, self.t22, self.t23, self.t24, self.t25, self.t26, self.t27]

        for i in v:
            if i.text.lower() in six:
                i.background_color = (0, 1, 0, 1)
            if i.text.lower() in nine:
                i.background_color = (0, 0, 1, 1)
            if i.text.lower() in ten:
                i.background_color = (1, 0, 1, 1)
            if i.text.lower() in deba:
                i.background_color = (1, 1, 0, 1)
            if i.text.lower() in even:
                i.background_color = (1, .5, .5, 1)
            if i.text.lower() in end:
                i.background_color = (1, 0, 0, 1)
            if i.text == "":
                i.background_color = (1, 1, 1, 1)
        for z in pl:
            if z.text.lower() in six:
                z.background_color = (0, 1, 0, 1)
            if z.text.lower() in nine:
                z.background_color = (0, 0, 1, 1)
            if z.text.lower() in ten:
                z.background_color = (1, 0, 1, 1)
            if z.text.lower() in deba:
                z.background_color = (1, 1, 0, 1)
            if z.text.lower() in even:
                z.background_color = (1, .5, .5, 1)
            if z.text.lower() in end:
                z.background_color = (1, 0, 0, 1)
            if z.text == "":
                z.background_color = (1, 1, 1, 1)

        for m in tl:
            if m.text.lower() in six:
                m.background_color = (0, 1, 0, 1)
            if m.text.lower() in nine:
                m.background_color = (0, 0, 1, 1)
            if m.text.lower() in ten:
                m.background_color = (1, 0, 1, 1)
            if m.text.lower() in deba:
                m.background_color = (1, 1, 0, 1)
            if m.text.lower() in even:
                m.background_color = (1, .5, .5, 1)
            if m.text.lower() in end:
                m.background_color = (1, 0, 0, 1)
            if m.text == "":
                m.background_color = (1, 1, 1, 1)

        del six
        del nine
        del ten
        del deba
        del even
        del end

        cnt = 8
        for i in range(20):
            exec("self.t" + str(cnt) + ".text=self.r_teach(self.c" + str(cnt) + ".text ,  self.Cll.text ).upper()")
            cnt += 1

    def IMPC(self, sp, t):
        # SELECT MONTH  , OR , SELECT DAY  OR RESET
        if t == "RESET":
            self.Simportc.values = tuple(Clss())
        if t[0] == 'P' or t[0] == "N":
            self.klas = t
            self.Simportc.values = ("Month", "Day", "RESET")

        if t == "Month":
            nl = []
            for fi in os.listdir(
                    DIR + 'media' + PTH + '0' + PTH + 'TABLE' + PTH + '' + self.YR.text + "/" + self.klas.strip()):
                nl.append(fi[:-5])
            nl.append("RESET")
            self.Simportc.values = tuple(nl)
        if t in ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                 'November', 'December']:
            file = open(
                DIR + 'media' + PTH + '0' + PTH + 'TABLE' + PTH + '' + self.YR.text + "/" + self.klas.strip() + "/" + t + ".json",
                'r')
            KL = json.load(file)
            file.close()

            zzz = open(
                DIR + 'media' + PTH + '0' + PTH + 'TABLE' + PTH + '' + self.YR.text + "/" + self.Cll.text.strip() + "/" + self.mnt.text + ".json",
                'w')
            json.dump(KL, zzz)
            zzz.close()
        if t == 'Day':
            self.Simportc.text = "Select Day"
            self.Simportc.values = tuple(
                ["Monday", "Tuesday", "Wednesday", "Thurday", "Friday", "Saturday", "Sunday", "RESET"])
        if t in ["Monday", "Tuesday", "Wednesday", "Thurday", "Friday", "Saturday", "Sunday"]:
            if not os.path.isfile(
                    DIR + 'media' + PTH + '0' + PTH + 'TABLE' + PTH + '' + self.YR.text + "/" + self.klas.strip() + "/" + self.mnt.text + ".json"):
                return
            file = open(
                DIR + 'media' + PTH + '0' + PTH + 'TABLE' + PTH + '' + self.YR.text + "/" + self.klas.strip() + "/" + self.mnt.text + ".json",
                'r')
            dt = json.load(file)
            file.close()

            print(dt)

            v = open(
                DIR + 'media' + PTH + '0' + PTH + 'TABLE' + PTH + '' + self.YR.text + "/" + self.Cll.text.strip() + "/" + self.mnt.text + ".json",
                'r')
            ct = json.load(v)
            v.close()

            ct[self.DY.text] = dt.get(t, {})

            zzz = open(
                DIR + 'media' + PTH + '0' + PTH + 'TABLE' + PTH + '' + self.YR.text + "/" + self.Cll.text.strip() + "/" + self.mnt.text + ".json",
                'w')
            json.dump(ct, zzz)
            zzz.close()
            Clock.schedule_once(self.iko)
            self.Simportc.values = tuple(Clss())
            self.Simportc.text = "Import Class"

    def m31(self, sp, t):
        if t == "RESET":
            self.Simportd.values = ("Day", "Month")
            self.Simportd.text = "Import Date"
        if t == "Month":
            Imp = []
            for q in os.listdir(
                    DIR + 'media' + PTH + '0' + PTH + 'TABLE' + PTH + '' + self.YR.text + "/" + self.Cll.text.strip()):
                Imp.append(q[:-5])
            Imp.append("RESET")
            self.Simportd.text = "Select Month"
            self.Simportd.values = tuple(Imp)
        if t == "Day":
            Imp = []
            file = open(
                DIR + 'media' + PTH + '0' + PTH + 'TABLE' + PTH + '' + self.YR.text + "/" + self.Cll.text.strip() + "/" + self.mnt.text + ".json",
                'r')
            dt = json.load(file)
            file.close()
            for c in dt.keys():
                Imp.append(c)
            Imp.append("RESET")
            self.Simportd.values = tuple(Imp)
        if t in ["Monday", "Tuesday", "Wednesday", "Thurday", "Friday", "Saturday", "Sunday"]:
            file = open(
                DIR + 'media' + PTH + '0' + PTH + 'TABLE' + PTH + '' + self.YR.text + "/" + self.Cll.text.strip() + "/" + self.mnt.text + ".json",
                'r')
            dt = json.load(file)
            file.close()

            dt[self.DY.text] = dt[t]  # self.DY.text ni siku ninayotaka pakingia , na dt[t]  ni zile tayari zilipangiwa

            zzz = open(
                DIR + 'media' + PTH + '0' + PTH + 'TABLE' + PTH + '' + self.YR.text + "/" + self.Cll.text.strip() + "/" + self.mnt.text + ".json",
                'w')
            json.dump(dt, zzz)
            zzz.close()
            Clock.schedule_once(self.iko)
            self.Simportd.text = "Import Date"
            self.Simportd.values = ("Day", "Month")

        if t in ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                 'November', 'December']:
            file = open(
                DIR + 'media' + PTH + '0' + PTH + 'TABLE' + PTH + '' + self.YR.text + "/" + self.Cll.text.strip() + "/" + t + ".json",
                'r')
            dt = json.load(file)
            file.close()

            zzz = open(
                DIR + 'media' + PTH + '0' + PTH + 'TABLE' + PTH + '' + self.YR.text + "/" + self.Cll.text.strip() + "/" + self.mnt.text + ".json",
                'w')
            json.dump(dt, zzz)
            zzz.close()
            Clock.schedule_once(self.iko)
            self.Simportd.text = "Import Date"
            self.Simportd.values = ("Day", "Month")

    def VIEW_TEACHER(self, TEMP):
        self.detlst = ["NAMES"]
        self.SCRL = ScrollView(size_hint=(.7, .85), pos_hint={'center_x': .64, 'center_y': .45}, do_scroll_y=True,
                               do_scroll_x=True, scroll_type=['bars', 'content'], bar_width=10, bar_color=(1, 1, 0, 1),
                               bar_margin=0)
        self.add_widget(self.SCRL)
        self.autobind('self.SCRL')

        Clock.schedule_once(self.call_vt)
    def call_vt(self,x):
        self.idd.background_color = (.8, 0, 1, .9)

        try:
            self.remove_widget(self.PrI)
        except:
            pass
        self.PrI = Spinner(text='print ', values=('Names & pictures      ', 'Names & details'), color=(1, .6, 0, 1),
                           size_hint=(.2, .1), pos_hint={'center_x': .9, 'center_y': .04})
        self.PrI.bind(text=self.prteac)
        self.add_widget(self.PrI)

        # self.idd.unbind(on_release=self.home)
        try:
            self.remove_widget(self.TOD)
            self.remove_widget(self.gHRR)
            self.remove_widget(self.nyu)
        except:
            pass
        fN = open(DIR + 'media' + PTH + '0' + PTH + 'TDATA.json', 'r')
        DT = json.load(fN)
        fN.close()


        try:
            self.gtd.clear_widgets()
        except:
            pass
        try:
            self.SCRL.remove_widget(self.gtd)
        except:
            pass

        # ------------REMOVE BUTTONS
        try:
            self.remove_widget(self.prcol)
        except:
            pass
        try:
            self.remove_widget(self.delcol)
        except:
            pass
        try:
            self.remove_widget(self.adcol)
        except:
            pass
        try:
            self.remove_widget(self.status)
        except:
            pass
        # ------------------------------------------------------------
        self.gtd = GridLayout(cols=len(self.detlst), spacing=0, padding=0, pos_hint={'center_x': .5, 'center_y': .5},
                              size_hint=(None, None), size=(200 * len(self.detlst), 50 * len(DT.keys())))

        cnt = 0
        head = []
        for tch in DT.keys():
            if cnt == 1:
                break
            for x in DT[tch].keys():
                head.append(x)
            cnt += 1
        del cnt
        del head[head.index('NAMES')]  #""
        del head[head.index('PASSCODE')]

        self.adcol = Spinner(text=self.detlst[-1], values=tuple(head), size_hint=(.2, .06), pos_hint={'center_x': .4, 'center_y': .97})
        self.adcol.bind(text=self.plus)
        self.add_widget(self.adcol)

        self.delcol = Spinner(text='Delete one', values=tuple(self.detlst), size_hint=(.2, .06),pos_hint={'center_x': .65, 'center_y': .97})
        self.delcol.bind(text=self.moin)
        self.add_widget(self.delcol)

        self.prcol = Button(text='Print', size_hint=(.2, .06), pos_hint={'center_x': .9, 'center_y': .97},on_release=self.CL_P)
        self.add_widget(self.prcol)

        # self.status = Spinner(text=self.listst, values=("Status", 'CM', 'ORP', 'PWD', 'CHH', 'OTH'),
        #                       size_hint=(.2, .06), pos_hint={'center_x': .1, 'center_y': .45})
        # self.status.bind(text=self.CHST)
        # self.add_widget(self.status)


        cnt = 0
        for go in self.detlst:
            if go == "NAMES" :
                g = GridLayout(cols=1, size_hint=(None, None), size=(200, 30),
                               pos_hint={'center_x': .5, 'center_y': .5}, row_default_height=30,
                               row_force_default=True)
                g.add_widget(TextInput(text=go, readonly=True, background_color=(1, 1, 0, .8)))
            else:
                if go == "SUBJECTS":
                    g = GridLayout(cols=1, size_hint=(None, None), size=(350, 30),
                                   pos_hint={'center_x': .5, 'center_y': .5}, row_default_height=30,
                                   row_force_default=True)
                    g.add_widget(TextInput(text=go, readonly=True, background_color=(1, 1, 0, .8)))

                else:
                    g = GridLayout(cols=1, size_hint=(None, None), size=(150, 30),
                                   pos_hint={'center_x': .5, 'center_y': .5}, row_default_height=30,
                                   row_force_default=True)
                    g.add_widget(TextInput(text=go, readonly=True, background_color=(1, 1, 0, .8)))

            ll = list(DT.keys())
            ll.sort()
            for tc in ll:
                cnt += 1

                if go == "SUBJECTS":
                    all=""
                    for sub in DT[tc][go].keys() :
                        all +=sub.upper()+" ["
                        for clas in DT[tc][go][sub] :
                            all+=clas+ ","
                        all+="]    "

                    g.add_widget(TextInput(text=all, font_size=13,readonly=True))
                else:
                    if go == "NAMES":
                        g.add_widget(TextInput(text=str(cnt) + " .     " + DT[tc][go], readonly=True))

                    else:
                        g.add_widget(TextInput(text=DT[tc][go], readonly=True))

            self.gtd.add_widget(g)


        self.SCRL.add_widget(self.gtd)

        if not "NAMES" in self.detlst:
            rep = ["NAMES"] + head
            head = rep
            del rep
            self.adcol.values = tuple(head)

    def moin(self, sp, tx):
        if len(self.detlst) == 1:
            return
        del self.detlst[self.detlst.index(tx)]
        Clock.schedule_once(self.call_vt)

    def plus(self, sp, tex):

        if tex == "NAMES":
            self.detlst = ["NAMES"] + self.detlst

        if not tex in self.detlst:
            self.detlst.append(tex)
        else:
            if tex == "NAMES":
                pass
            else:
                del self.detlst[self.detlst.index(tex)]
                self.detlst.append(tex)

        Clock.schedule_once(self.call_vt)

    def CL_P(self, e):
        self.gtd.export_to_png(
            NDR + 'Desktop' + PTH + 'P R I N T A B L E' + PTH + "ANGELS TEACHERS' DETAILS.png")
        self.print_all_i(NDR + 'Desktop' + PTH + 'P R I N T A B L E' + PTH + "ANGELS TEACHERS' DETAILS.png")
        self.rOK("printed")

        # self.gVIEW = GridLayout(cols=2, spacing=19, size_hint=(.65, 1.), pos_hint={'center_x': .62, 'center_y': .5})
        # self.gVIEW.add_widget(Label(text='TEACHER ,SUBJECT & CLASS ', italic=True, size_hint_y=.1, color=(0, 0, 0, 1)))
        # self.gVIEW.add_widget(Label(text='BIO', italic=True, size_hint_y=.1, color=(0, 0, 0, 1)))
        # self.scr = ScrollView(size_hint=(.5, .8), pos_hint={'center_x': .5, 'center_y': .5}, do_scroll_x=False,
        #                       do_scroll_y=True, scroll_timeout=55, scroll_distance=20, scroll_type=['bars', 'content'],
        #                       bar_width=10, bar_color=(1, 1, 0, 1), bar_margin=0)
        # self.autobind('self.scr')
        # tcc = GridLayout(cols=1, spacing=12, size_hint_x=1., size_hint_y=10,
        #                  pos_hint={'center_x': .54, 'center_y': .5}, row_default_height=60,
        #                  row_force_default=True)
        # # tcc=GridLayout(spacing=10,cols=1,size_hint=(.5,.95))
        # try:
        #     del fina[""]
        # except:
        #     pass
        # for tch in fina.keys():
        #     tg = GridLayout(spacing=5, cols=2)
        #     tg.add_widget(Button(text=tch, on_release=self.ID))
        #     tg.add_widget(Button(text=fina[tch]["TEL"]))
        #     for cr in fina[tch]["SUBJECTS"].keys():
        #         tg.add_widget(Label(text=cr + " : ", color=(0, 0, 0, 1)))
        #         tg.add_widget(Label(text="/".join(fina[tch]["SUBJECTS"][cr]), color=(0, 0, 0, 1)))
        #     tcc.add_widget(tg)
        # self.scr.add_widget(tcc)
        # self.gVIEW.add_widget(self.scr)
        #
        # self.add_widget(self.gVIEW)

    def prteac(self, s, t):
        if t == 'Names & pictures      ':
            fN = open(DIR + 'media' + PTH + '0' + PTH + 'TDATA.json', 'r')
            fina = json.load(fN)
            fN.close()
            sz = 0
            self.prgr = GridLayout(cols=4, spacing=5, size_hint=(None, None), row_default_height=180,
                                   row_force_default=True)
            self.prgr.add_widget(Label(text=""))
            self.prgr.add_widget(
                Label(text="ANGELS CARE SCHOOL  TEACHERS", font_size=35, underline=True, color=(0, 0, 0, 1)))
            self.prgr.add_widget(Label(text=""))
            self.prgr.add_widget(Label(text=""))
            sz += 1

            for name in fina.keys():
                g = GridLayout(cols=1, spacing=0, padding=0)
                g.add_widget(Label(text=name, color=(0, 0, 0, 1), size_hint=(1., .2)))
                g.add_widget(AsyncImage(source=ASY + name + ".png"))
                self.prgr.add_widget(g)
                sz += 0.25
            self.prgr.size = (840, 180 * sz + 250)
            print("sz", sz)
            self.add_widget(self.prgr)
            Clock.schedule_once(self.printit, 5)

        if t == "Names & details":
            fN = open(DIR + 'media' + PTH + '0' + PTH + 'TDATA.json', 'r')
            fina = json.load(fN)
            fN.close()
            sz = 0
            self.scat = Scatter(do_translation=False, do_scale=False, do_rotation=True, size_hint=(None, None))
            self.prgr = GridLayout(cols=9, spacing=5, size_hint=(None, None), pos_hint={'center_x': .5, 'center_y': .5},
                                   row_default_height=28,
                                   row_force_default=True)
            self.prgr.add_widget(Label(text=""))
            self.prgr.add_widget(Label(text=""))
            self.prgr.add_widget(Label(text=""))
            self.prgr.add_widget(Label(text="ANGELS CARE SCHOOL  TEACHERS", italic=True, font_size=35, underline=True,
                                       color=(0, 0, 0, 1)))
            for ii in range(14):
                self.prgr.add_widget(Label(text=""))

            sz += 2

            self.prgr.add_widget(TextInput(text="Name", size_hint=(None, None), size=(200, 28)))
            self.prgr.add_widget(
                TextInput(text="Gender", size_hint=(None, None), size=(60, 28), background_color=(0, 0, 0, 1),
                          foreground_color=(1, 1, 1, 1)))
            self.prgr.add_widget(
                TextInput(text="DOB", size_hint=(None, None), size=(100, 28), background_color=(0, 0, 0, 1),
                          foreground_color=(1, 1, 1, 1)))
            self.prgr.add_widget(
                TextInput(text="DOA", size_hint=(None, None), size=(160, 28), background_color=(0, 0, 0, 1),
                          foreground_color=(1, 1, 1, 1)))
            self.prgr.add_widget(
                TextInput(text="QUALIFICATION", size_hint=(None, None), size=(140, 28), background_color=(0, 0, 0, 1),
                          foreground_color=(1, 1, 1, 1)))
            self.prgr.add_widget(
                TextInput(text="REG NO.", size_hint=(None, None), size=(130, 28), background_color=(0, 0, 0, 1),
                          foreground_color=(1, 1, 1, 1)))
            self.prgr.add_widget(
                TextInput(text="NIN", size_hint=(None, None), size=(130, 28), background_color=(0, 0, 0, 1),
                          foreground_color=(1, 1, 1, 1)))
            self.prgr.add_widget(
                TextInput(text="CONTACT", size_hint=(None, None), size=(130, 28), background_color=(0, 0, 0, 1),
                          foreground_color=(1, 1, 1, 1)))
            self.prgr.add_widget(
                TextInput(text="SUBJECT & CLASS", size_hint=(None, None), size=(440, 28), background_color=(0, 0, 0, 1),
                          foreground_color=(1, 1, 1, 1)))

            sz += 1

            for name in fina.keys():
                self.prgr.add_widget(
                    TextInput(text=name, size_hint=(None, None), size=(200, 28), background_color=(0, 0, 0, 1),
                              foreground_color=(1, 1, 1, 1)))
                self.prgr.add_widget(TextInput(text=fina[name]["SEX"], size_hint=(None, None), size=(60, 28)))
                self.prgr.add_widget(TextInput(text=fina[name]["DOB"], size_hint=(None, None), size=(100, 28)))
                self.prgr.add_widget(TextInput(text=fina[name]["DOA"], size_hint=(None, None), size=(160, 28)))
                self.prgr.add_widget(
                    TextInput(text=fina[name]["QUALIFICATION & YEAR"], size_hint=(None, None), size=(140, 28)))
                self.prgr.add_widget(TextInput(text=fina[name]["REG NUMBER"], size_hint=(None, None), size=(130, 28)))
                self.prgr.add_widget(TextInput(text=fina[name]["NIN NUMBER"], size_hint=(None, None), size=(130, 28)))
                self.prgr.add_widget(TextInput(text=fina[name]["TEL"], size_hint=(None, None), size=(130, 28)))
                box = GridLayout(cols=5, size_hint=(None, None), size=(450, 28), row_default_height=28,
                                 row_force_default=True)
                for s in fina[name]["SUBJECTS"].keys():
                    box.add_widget(
                        TextInput(text=s.upper() + "  [" + ",".join(fina[name]["SUBJECTS"][s]) + "]  ", font_size=11))
                self.prgr.add_widget(box)
                sz += 1
            # self.scat.size = (28 * sz + 100, 1400)

            self.prgr.size = (1580, 28 * sz + 100)
            self.add_widget(self.prgr)
            # self.scat.add_widget(self.prgr)
            # self.scat.rotation = 90
            Clock.schedule_once(self.RprintitR, 5)

    def printit(self, x):
        self.prgr.export_to_png(
            NDR + 'Desktop' + PTH + 'P R I N T A B L E' + PTH + '' + "ANGELS CARE SCHOOL TEACHERS " + time.strftime(
                '%Y %B %d') + ".png")
        self.print_all_i(NDR + 'Desktop' + PTH + 'P R I N T A B L E' + PTH + '' + "ANGELS CARE SCHOOL TEACHERS " + time.strftime(
                '%Y %B %d') + ".png")
        self.remove_widget(self.prgr)

    def RprintitR(self, x):
        self.prgr.export_to_png(
            NDR + 'Desktop' + PTH + 'P R I N T A B L E' + PTH + '' + "ANGELS CARE SCHOOL TEACHERS " + time.strftime(
                '%Y %B %d') + ".png")

        self.print_all_i(NDR + 'Desktop' + PTH + 'P R I N T A B L E' + PTH + '' + "ANGELS CARE SCHOOL TEACHERS " + time.strftime(
                '%Y %B %d') + ".png")

        self.remove_widget(self.prgr)
        # import cv2
        # im = cv2.imread("ANGELS CARE SCHOOL TEACHERS " + time.strftime('%Y %B %d') + ".png")
        # rt = cv2.rotate(im, cv2.ROTATE_90_CLOCKWISE)
        # cv2.imwrite("ANGELS CARE SCHOOL TEACHERS " + time.strftime('%Y %B %d') + " 2.png", rt)
        # cv2.waitKey(0)

    def ID(self, sin):
        try:
            self.gVIEW.remove_widget(self.bio)
        except:
            pass

        self.idd.background_color = (0, 0, 0, .9)

        self.verify = TextInput(text='password', background_color=(1, 1, 1, 1), size_hint=(.3, .07), allow_copy=True,
                                foreground_color=(0, 0, 0, 1), pos_hint={'center_x': .8, 'center_y': .88})
        self.verify.bind(on_touch_down=self.vcl)
        self.verify.bind(text=self.vverified)
        self.add_widget(self.verify)
        print(sin.text, len(sin.text))
        fN = open(DIR + 'media' + PTH + '0' + PTH + 'TDATA.json', 'r')
        fina = json.load(fN)
        fN.close()
        try:
            del fina[""]
        except:
            pass
        self.bio = GridLayout(cols=1, size_hint=(1., .4), row_default_height=60, row_force_default=False)
        try:
            del fina[sin.text]["SUBJECTS"]
        except:
            pass
        del fina[sin.text]["PASSCODE"]

        self.biospinner = Spinner(text="Clic here for details", values=(), background_color=(0, 0, 0, 0),
                                  size_hint_y=.2, pos_hint={'center_x': .5, 'center_y': .87})
        LT = []
        for i in fina[sin.text].keys():
            LT.append(i + " : " + fina[sin.text][i])
        self.biospinner.values = tuple(LT)
        self.bio.add_widget(self.biospinner)
        profile = AsyncImage(source=ASY + sin.text + ".png", size_hint=(1., .45))
        self.bio.add_widget(profile)

    def vverified(self, ok, tex):
        fN = open(DIR + 'media' + PTH + '0' + PTH + 'ACR.json', 'r')
        fina = json.load(fN)
        fN.close()
        pasw = dec(fina["xajfk"])

        # fN = open(DIR + 'media' + PTH + '0' + PTH + 'cd', 'r')
        # pasw = fN.read()[:2]
        # print("pasw", pasw)
        fN.close()
        if tex == pasw:
            self.gVIEW.add_widget(self.bio)
            self.verify.text = ""
            self.idd.background_color = (.3, .3, .3, 1)
            self.remove_widget(self.verify)

    def vcl(self, x, y):
        self.verify.text = ""
        self.verify.password = True

    def ADD_TEACHER(self, a):
        if lv != 'adm':
            return

        self.CLASSLIST = []
        self.DCOUR = {}
        LIS = ['N1 ','N2 ','N3 ','P1 ','P2 ','P3 ','P4 ','P5 ','P6 ','P7 ']

        self.gadt = GridLayout(spacing=7, cols=2, size_hint=(.4, .45), pos_hint={'center_x': .47, 'center_y': .75},
                               row_default_height=28, row_force_default=True)
        self.Lcourse = Label(text="SUBJECT", color=(0, 0, 1, 1), pos_hint={'center_x': .85, 'center_y': .95})
        self.add_widget(self.Lcourse)

        self.gCour = GridLayout(cols=2, size_hint=(.3, .25), pos_hint={'center_x': .85, 'center_y': .724},
                                row_default_height=30, row_force_default=True)

        self.cour1 = TextInput(background_color=(0, 0, 0, 1), allow_copy=True, foreground_color=(1, 1, 1, 1))
        self.cour1.bind(text=self.unfoc)
        self.gCour.add_widget(self.cour1)
        self.Scour1 = Spinner(text="", values=tuple(LIS))
        self.Scour1.bind(text=self.collect)
        self.gCour.add_widget(self.Scour1)
        # if self.aaa=='1':
        self.Scour2 = Spinner(text="")
        # self.Scour2.bind(text=self.COllected)
        self.gCour.add_widget(self.Scour2)

        self.gCour.add_widget(Label(text=""))
        self.gCour.add_widget(Label(text=""))
        self.gCour.add_widget(Label(text=""))
        self.gCour.add_widget(Label(text=""))
        self.gCour.add_widget(Label(text=""))
        self.gCour.add_widget(
            Label(text="*  For each course \nyou write,You can \nselect many classes \nin wich the teacher\n can teach",
                  color=(1, 0, 1, 1)))

        self.snap = Button(text='Profile Photo', size_hint=(.3, .3), pos_hint={'center_x': .83, 'center_y': .4},
                           on_release=self.PPH)
        self.add_widget(self.snap)

        self.gadt.add_widget(Label(text=""))
        self.gadt.add_widget(Label(text="BIO", color=(0, 0, 1, 1)))
        self.gadt.add_widget(Label(text=""))
        self.gadt.add_widget(Label(text=""))
        self.gadt.add_widget(Label(text="NAMES", color=(0, 0, 0, 1)))
        self.tNAMES = TextInput(background_color=(0, 0, 0, 1), allow_copy=True, foreground_color=(1, 1, 1, 1))
        self.tNAMES.bind(text=self.tedit)
        self.gadt.add_widget(self.tNAMES)
        self.gadt.add_widget(Label(text="SEX", color=(0, 0, 0, 1)))
        self.tSX = Spinner(text="", values=('M', 'F'))
        self.gadt.add_widget(self.tSX)
        self.gadt.add_widget(Label(text="DATE OF BIRTH", color=(0, 0, 0, 1)))
        self.tdob = TextInput(background_color=(0, 0, 0, 1), allow_copy=True, foreground_color=(1, 1, 1, 1))
        self.gadt.add_widget(self.tdob)
        self.gadt.add_widget(Label(text="AGE", color=(0, 0, 0, 1)))
        self.tAGE = TextInput(background_color=(0, 0, 0, 1), allow_copy=True, foreground_color=(1, 1, 1, 1))
        self.gadt.add_widget(self.tAGE)
        self.gadt.add_widget(Label(text="RELATIONSHIP", color=(0, 0, 0, 1)))
        self.tREL = Spinner(text="", values=('Maried', 'Single', 'Other'))
        self.gadt.add_widget(self.tREL)
        self.gadt.add_widget(Label(text="ADRESS", color=(0, 0, 0, 1)))
        self.tADRESS = TextInput(background_color=(0, 0, 0, 1), allow_copy=True, foreground_color=(1, 1, 1, 1))
        self.gadt.add_widget(self.tADRESS)
        self.gadt.add_widget(Label(text="TEL", color=(0, 0, 0, 1)))
        self.tTEL = TextInput(background_color=(0, 0, 0, 1), allow_copy=True, foreground_color=(1, 1, 1, 1))
        self.gadt.add_widget(self.tTEL)
        self.gadt.add_widget(Label(text="NUM OF CHILDREN", color=(0, 0, 0, 1)))
        self.tNUMCH = Spinner(text="", values=('1', '2', '3', '4', '5', '6', '7', '8', '9', '10'))
        self.gadt.add_widget(self.tNUMCH)
        self.gadt.add_widget(Label(text="NAMES OF CHILDREN", color=(0, 0, 0, 1)))
        self.tNOC = TextInput(background_color=(0, 0, 0, 1), allow_copy=True, foreground_color=(1, 1, 1, 1))
        self.gadt.add_widget(self.tNOC)
        self.gadt.add_widget(Label(text="REG NUMBER", color=(0, 0, 0, 1)))
        self.tREGNUM = TextInput(background_color=(0, 0, 0, 1), allow_copy=True, foreground_color=(1, 1, 1, 1))
        self.gadt.add_widget(self.tREGNUM)
        self.gadt.add_widget(Label(text="NIN NUMBER", color=(0, 0, 0, 1)))
        self.tNIN = TextInput(background_color=(0, 0, 0, 1), allow_copy=True, foreground_color=(1, 1, 1, 1))
        self.gadt.add_widget(self.tNIN)
        self.gadt.add_widget(Label(text="QUALIFICATION & YEAR", color=(0, 0, 0, 1)))
        self.tCALY = TextInput(background_color=(0, 0, 0, 1), allow_copy=True, foreground_color=(1, 1, 1, 1))
        self.gadt.add_widget(self.tCALY)
        self.gadt.add_widget(Label(text="NEXT OF KIN", color=(0, 0, 0, 1)))
        self.tNXT = TextInput(background_color=(0, 0, 0, 1), allow_copy=True, foreground_color=(1, 1, 1, 1))
        self.gadt.add_widget(self.tNXT)
        #
        self.gadt.add_widget(Label(text="SALARY", color=(0, 0, 0, 1)))
        self.tSAL = TextInput(text='0', background_color=(0, 0, 0, 1), allow_copy=True,
                              foreground_color=(1, 1, 1, 1))
        self.gadt.add_widget(self.tSAL)

        self.gadt.add_widget(Label(text="PASSCODE", color=(0, 0, 0, 1)))
        self.tPSW = TextInput(password=True, background_color=(0, 0, 0, 1), allow_copy=True,
                              foreground_color=(1, 1, 1, 1))
        self.gadt.add_widget(self.tPSW)

        self.add_widget(self.gCour)
        self.add_widget(self.gadt)
        self.Savb = Button(text='S A V E', background_color=(.6, .42, .15, 1), size_hint=(.2, .1),
                           pos_hint={'center_x': .89, 'center_y': .1}, on_release=self.savaddtecher)
        self.add_widget(self.Savb)
        self.aaa = "0"

    def collect(self, chk, value):
        self.CLASSLIST.append(value)
        self.DCOUR[self.cour1.text] = self.CLASSLIST
        self.Scour2.values = tuple(self.DCOUR.keys())
        self.Scour2.bind(text=self.spedited)
        print(self.DCOUR)

    def COllected(self, sp, tx):
        pass

    def tedit(self, spi, tx):
        fN = open(DIR + 'media' + PTH + '0' + PTH + 'TDATA.json', 'r')
        fina = json.load(fN)
        fN.close()
        if fina.get(self.tNAMES.text.lower(), 0):
            self.DCOUR = fina[self.tNAMES.text.lower()]["SUBJECTS"]
            self.aaa = '1'
            self.tNAMES.text = fina[self.tNAMES.text.lower()]["NAMES"]
            self.tSX.text = fina[self.tNAMES.text.lower()]["SEX"]
            self.tdob.text = fina[self.tNAMES.text.lower()]["DOB"]
            self.tAGE.text = fina[self.tNAMES.text.lower()]["AGE"]
            self.tREL.text = fina[self.tNAMES.text.lower()]["RELATIONSHIP"]
            self.tADRESS.text = fina[self.tNAMES.text.lower()]["ADRESS"]
            self.tTEL.text = fina[self.tNAMES.text.lower()]["TEL"]
            self.tNUMCH.text = fina[self.tNAMES.text.lower()]["NUM OF CHILDREN"]
            self.tNOC.text = fina[self.tNAMES.text.lower()]["NAMES OF CHILDREN"]
            self.tREGNUM.text = fina[self.tNAMES.text.lower()]["REG NUMBER"]
            self.tNIN.text = fina[self.tNAMES.text.lower()]["NIN NUMBER"]
            self.tCALY.text = fina[self.tNAMES.text.lower()]["QUALIFICATION & YEAR"]
            self.tNXT.text = fina[self.tNAMES.text.lower()]["NEXT OF KIN"]
            # self.tCOUR.text = fina[self.tNAMES.text]["SUBJECTS"]
            self.Scour2.values = tuple(self.DCOUR.keys())  # ON_CLIC=FILL TEXT IN TEXTINPUT THEN SELECT NEW CLASS
            self.Scour2.bind(text=self.spedited)  # IF '..' ADDED AT END , DELETE THAT KEY AND VALUE.
            self.tPSW.text = fina[self.tNAMES.text.lower()]["PASSCODE"]
            self.tPSW.password = True
            self.tSAL.text = fina[self.tNAMES.text.lower()]["SALARY"]
            self.snap.background_normal = DIR + 'media' + PTH + '0' + PTH + self.tNAMES.text.lower() + '.png'

    def spedited(self, sp, tx):
        self.cour1.text = tx
        self.cour1.bind(text=self.editing)

    def editing(self, sp, tx):
        if "xxx" in tx.lower():
            del self.DCOUR[self.Scour2.text]
            self.cour1.text = ""
            self.Scour2.values = tuple(self.DCOUR.keys())

    def savaddtecher(self, v):
        fN = open(DIR + 'media' + PTH + '0' + PTH + 'TDATA.json', 'r')
        fina = json.load(fN)
        fN.close()
        # if self.DCOUR=={} :
        #     try:
        #         self.DCOUR=fina[self.tNAMES.text]["SUBJECTS"]
        #     except:
        #         pass
        try:
            DOA = fina[self.tNAMES.text.lower()]["DOA"]
        except:
            DOA = time.strftime('%d %B %Y  %H:%M')
        if fina.get(self.tNAMES.text.lower(),0):
            balance=fina[self.tNAMES.text.lower()].get("balance","0")
        else:
            balance="0"

        fina[self.tNAMES.text.lower()] = {
            "NAMES": self.tNAMES.text.lower(),
            "SEX": self.tSX.text,
            "DOB": self.tdob.text,
            "AGE": self.tAGE.text,
            "RELATIONSHIP": self.tREL.text,
            "ADRESS": self.tADRESS.text,
            "TEL": self.tTEL.text,
            "NUM OF CHILDREN": self.tNUMCH.text,
            "NAMES OF CHILDREN": self.tNOC.text,
            "REG NUMBER": self.tREGNUM.text,
            "NIN NUMBER": self.tNIN.text,
            "QUALIFICATION & YEAR": self.tCALY.text,
            "NEXT OF KIN": self.tNXT.text,
            "SUBJECTS": self.DCOUR,
            "PASSCODE": self.tPSW.text,
            "SALARY": self.tSAL.text,
            "balance": balance,
            "DOA": DOA
        }

        FF = open(DIR + 'media' + PTH + '0' + PTH + 'TDATA.json', 'w')
        json.dump(fina, FF)
        FF.close()
        Clock.schedule_once(self.cgadt, 1)

    def unfoc(self, c, t):
        self.CLASSLIST = []
    def PPH(self,x):
        threading.Thread(target=self.pic).start()

    def pic(self):
        import cv2
        im=""
        try:
            im = cv2.VideoCapture(1)
            print('111111111111111111')

            for i in range(500):
                ret, frame = im.read()
                cv2.imshow(self.tNAMES.text+" in cv2 n1", frame)
                if cv2.waitKey(1) == ord('\r'):
                   # cv2.imwrite('ANGELS'+PTH+'' + self.tNAMES.text.lower() + '.png', frame)
                   cv2.imwrite(DIR+'media'+PTH+'0'+PTH+'' + self.tNAMES.text.lower() + '.png', frame)
                   self.snap.background_normal = DIR+'media'+PTH+'0'+PTH+  self.tNAMES.text.lower() + '.png'
                   break
                if cv2.waitKey(1) == ord(' '):
                    break
            im.release()
            cv2.destroyAllWindows()
            im="ok"

        except:
            try:
                im = cv2.VideoCapture(0)
                print('00000000000')

                for i in range(500):
                    ret, frame = im.read()
                    cv2.imshow(self.tNAMES.text+" in cv2 n0", frame)
                    if cv2.waitKey(1) == ord('\r'):
                        # cv2.imwrite(ANGELS + PTH + '' + self.tNAMES.text.lower() + '.png', frame)
                        cv2.imwrite(DIR + 'media' + PTH + '0' + PTH + '' + self.tNAMES.text.lower() + '.png', frame)
                        self.snap.background_normal = DIR+'media'+PTH+'0'+PTH+  self.tNAMES.text.lower() + '.png'
                        break
                    if cv2.waitKey(1) == ord(' '):
                        break
                im.release()
                cv2.destroyAllWindows()
                im="ok"
            except:
                Clock.schedule_once(self.segon)
                # threading.Thread(target=self.segon).start()
        # if im == "" :
        #     print('gone to sego')
        #     threading.Thread(target=self.segon).start()
    def segon(self,x):
        for swepper in range(3):
            print('swepper')
        # if not os.path.isdir('ANGELS'):
        #     os.mkdir('ANGELS')
        self.layout = BoxLayout(orientation='vertical')
        try:
            try:

                self.cameraObject = Camera(play=False)
                index = 2
                self.cameraObject.play = True
                print('index 2')
            except:
                self.cameraObject = Camera(play=False)
                index = 1
                self.cameraObject.play = True
                print('index 1')
        except:
            try:
                self.cameraObject = Camera(play=False)
                index = 0
                self.cameraObject.play = True
                print('index 0')
            except:
                return
                print('return')

        self.cameraObject.play = True
        # self.cameraObject.resolution = (300, 300) # Specify the resolution
        self.camaraClick = Button(text="Take Photo")
        self.camaraClick.size_hint = (.5, .2)
        self.camaraClick.pos_hint = {'x': .25, 'y': .75}
        # self.camaraClick.bind(on_press=self.onCameraClick)
        Window.bind(on_keyboard=self.kkbb)

        self.layout.add_widget(self.cameraObject)

        # self.layout.add_widget(self.camaraClick)

        self.add_widget(self.layout)

        # if cv2.waitKey(1) == ord('\r'):
        # cv2.imwrite('ANGELS'+PTH+'' + self.txfnam.text.lower() + '.png', frame)
        # cv2.imwrite(DIR+'media'+PTH+'.0'+PTH+'' + self.txfnam.text.lower() + '.png', frame)
        # self.photo.background_normal = 'ANGELS'+PTH+'' + self.txfnam.text.lower() + '.png'

        # if cv2.waitKey(1) == ord(' '):
        # break

    def kkbb(self, window, key, *largs):
        if key == 27 or key == ord(" "):
            try:
                self.cameraObject.play = False
            except:
                pass
            # self.cameraObject.stopped=True
            del self.cameraObject
            # Camera.stop()
            self.remove_widget(self.layout)
            del self.layout
            # a=Camera(play=False,stopped=True)
        if key == ord('\r'):
            self.cameraObject.export_to_png(ANGELS + PTH + '' + self.tNAMES.text.lower() + '.png')
            self.cameraObject.export_to_png(DIR + 'media' + PTH + '0' + PTH + '' + self.tNAMES.text.lower() + '.png')
            del self.cameraObject
            # Camera.stop()
            self.remove_widget(self.layout)
            self.snap.background_normal = DIR+'media'+PTH+'0'+PTH+  self.tNAMES.text.lower() + '.png'
            del self.layout
        self.cameraObject = None

        Window.unbind(on_keyboard=self.keyb)

        # _____________________________________________________________________________________________________
        # import cv2
        # try:
        #    im = cv2.VideoCapture(0)
        # except:
        #    im = cv2.VideoCapture(1)

        # for i in range(500):
        #    ret, frame = im.read()
        #    cv2.imshow(self.tNAMES.text, frame)
        #    if cv2.waitKey(1) == ord('\r'):
        #        cv2.imwrite('ANGELS'+PTH+'' + self.tNAMES.text.lower() + '.png', frame)
        #        cv2.imwrite(DIR+'media'+PTH+'.0'+PTH+'' + self.tNAMES.text.lower() + '.png', frame)
        #        self.snap.background_normal = 'ANGELS'+PTH+'' + self.tNAMES.text.lower() + '.png'
        #        break
        #    if cv2.waitKey(1) == ord(' '):
        #        break
        # im.release()
        # cv2.destroyAllWindows()

    def horaire(self, event, tex):
        self._H.background_color = (1, 1, 1, 0)
        self._H.color = (1, 1, 1, 0)
        if tex == "Portrait":
            self.gEXT.size_hint = (None, None)
            self.gEXT.size = (900, 1200)
        if tex == "Landscape":
            self.gEXT.size_hint = (None, None)
            self.gEXT.size = (1400, 780)
        Clock.schedule_once(self.PHORAIRE, 2)

    def PHORAIRE(self, EVENT):
        self.gEXT.export_to_png(
            NDR + 'Desktop' + PTH + 'P R I N T A B L E' + PTH + '' + "TIME TABLE " + self.Cll.text + " " + self.mnt.text + " " + self.DY.text + ".png")
        self.remove_widget(self.scrolltable)
        self.print_all_i(NDR + 'Desktop' + PTH + 'P R I N T A B L E' + PTH + '' + "TIME TABLE " + self.Cll.text + " " + self.mnt.text + " " + self.DY.text + ".png")
        Clock.schedule_once(self.TODAY)
    def print_all_i(self,path):

        import tempfile
        import win32api, win32print

        try:
            try:
                fN = open(path, 'rb')
                a = fN.read()
                fN.close()
                filename = tempfile.mktemp(suffix=".png")
                FF = open(filename, 'wb')
                FF.write(a)
                FF.close()
                win32api.ShellExecute(0, 'print', filename, f'/d:"{win32print.GetDefaultPrinter()}"', '.', 0)
                print("print 1")
            except:
                os.startfile(path, "print")
                print("print 9")
        except:
            try:
                fN = open(path, 'rb')
                a = fN.read()
                fN.close()
                filename = tempfile.mktemp(suffix=".png")
                FF = open(filename, 'wb')
                FF.write(a)
                FF.close()
                os.startfile(filename, "print")
                print("print 4")
            except:
                win32api.ShellExecute(0, 'print', path, f'/d:"{win32print.GetDefaultPrinter()}"', '.', 0)
                print("print 3")

        # try:
        #     try:
        #         try:
        #             fN = open(path, 'rb')
        #             a = fN.read()
        #             fN.close()
        #             os.startfile(a, "print")
        #             print("print 5")
        #
        #         except:
        #             fN = open(path, 'rb')
        #             a = fN.read()
        #             fN.close()
        #             filename = tempfile.mktemp(suffix=".png")
        #             FF = open(filename, 'wb')
        #             FF.write(a)
        #             FF.close()
        #             win32api.ShellExecute(0, 'print', filename, '.', '/manualstoprint', 0)
        #             print("print 8")
        #
        #     except:
        #         try:
        #             fN = open(path, 'rb')
        #             a = fN.read()
        #             fN.close()
        #             filename = tempfile.mktemp(suffix=".png")
        #             FF = open(filename, 'wb')
        #             FF.write(a)
        #             FF.close()
        #             win32api.ShellExecute(0, "printto", filename, '"%s"' % win32print.GetDefaultPrinter(), ".", 0)
        #             print("print 6")
        #         except:
        #             win32api.ShellExecute(0, "printto", path, '"%s"' % win32print.GetDefaultPrinter(), ".", 0)
        #             print("print 7")
        #
        # except:
        #     try:
        #         fN = open(path, 'rb')
        #         a = fN.read()
        #         fN.close()
        #         filename = tempfile.mktemp(suffix=".png")
        #         FF = open(filename, 'wb')
        #         FF.write(a)
        #         FF.close()
        #         os.startfile(filename, "print")
        #         print("print 4")
        #     except:
        #         try:
        #             os.startfile(path, "print")
        #             print("print 9")
        #         except:
        #             try:
        #                 win32api.ShellExecute(0, 'print', path, '.', '/manualstoprint', 0)
        #                 print("print 10")
        #             except:
        #                 fN = open(path, 'rb')
        #                 a = fN.read()
        #                 fN.close()
        #                 win32api.ShellExecute(0, "printto", a, '"%s"' % win32print.GetDefaultPrinter(), ".", 0)
        #                 print("print 11")

    def TODAY(self, X):
        # import webbrowser
        # webbrowser.open("med.mp3")
        C = Clss()
        TDAT = open(DIR + 'media' + PTH + '0' + PTH + 'TABLE.json', 'r')
        DT = json.load(TDAT)
        TDAT.close()

        self.idd.background_color = (.8, 0, 1, .9)
        l = Clss()
        self.scrolltable = ScrollView(size_hint=(.65, 1.), pos_hint={'center_x': .62, 'center_y': .5},
                                      do_scroll_x=False, do_scroll_y=True, scroll_type=['bars', 'content'],
                                      bar_width=10, bar_color=(1, 1, 0, 1), bar_margin=0)
        self.autobind('self.scrolltable')
        self.gEXT = GridLayout(cols=2, spacing=19, size_hint=(1., 1.8), row_default_height=40, row_force_default=True)
        self.gmdyc = GridLayout(cols=4, size_hint=(1., .14), row_default_height=30, row_force_default=True)
        self.gmdyc.add_widget(Label(text="CLASS", color=(0, 0, 0, 1), italic=True))
        self.gmdyc.add_widget(Label(text="MONTH", color=(0, 0, 0, 1), italic=True))
        self.gmdyc.add_widget(Label(text="DAY", color=(0, 0, 0, 1), italic=True))
        self.gmdyc.add_widget(Label(text="YEAR", color=(0, 0, 0, 1), italic=True))

        self.Cll = Spinner(text=Clss()[-1], background_color=(0, 0, 0, 1), values=tuple(l))
        self.Cll.bind(text=self.Hiko)
        self.gmdyc.add_widget(self.Cll)
        self.mnt = Spinner(text=time.strftime('%B'), background_color=(0, 0, 0, 1), size_hint=(.13, .06), values=tuple(
            ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
             'November', 'December']))
        self.mnt.bind(text=self.Hiko)
        self.mnt.bind(text=self.m31)
        self.gmdyc.add_widget(self.mnt)
        self.DY = Spinner(text=time.strftime('%A'), background_color=(0, 0, 0, 1), size_hint=(.13, .06),
                          values=("Monday", "Tuesday", "Wednesday", "Thurday", "Friday", "Saturday", "Sunday"))
        self.DY.bind(text=self.Hiko)
        self.gmdyc.add_widget(self.DY)
        an = range(2022, 2051)
        bb = []
        for ii in an:
            bb.append(str(ii))

        self.YR = Spinner(text=time.strftime('%Y'), background_color=(0, 0, 0, 1), size_hint=(.13, .04),
                          values=tuple(bb))
        self.YR.bind(text=self.iko)
        self.gmdyc.add_widget(self.YR)
        #############################################SPACE
        self._H = Spinner(text="Print", values=("Landscape", "Portrait", "..."), background_color=(1, 0, 0, 1))
        self._H.bind(text=self.horaire)
        self.gmdyc.add_widget(self._H)
        self.gmdyc.add_widget(Label(text=""))
        self.gmdyc.add_widget(Label(text=""))
        self.gmdyc.add_widget(Label(text=""))
        #################################################
        self.gmdyc.add_widget(Label(text="HOUR", color=(0, 0, 0, 1), italic=True))
        self.gmdyc.add_widget(Label(text="SUBJECT", color=(0, 0, 0, 1), italic=True))
        self.gmdyc.add_widget(Label(text="BOOK/PAGE", color=(0, 0, 0, 1), italic=True))
        self.gmdyc.add_widget(Label(text="TEACHER", color=(0, 0, 0, 1), italic=True))
        #########################################################

        self.eit = TextInput(text='6:30', background_color=(.4, 0, 1, .9), foreground_color=(1, 1, 1, 1))
        self.c8 = TextInput(allow_copy=True, foreground_color=(.55, 0, .23, 1))
        self.p8 = TextInput(allow_copy=True, foreground_color=(.55, 0, .23, 1))
        self.t8 = TextInput(allow_copy=True, foreground_color=(.55, 0, .23, 1))

        self.gmdyc.add_widget(self.eit)
        self.gmdyc.add_widget(self.c8)
        self.gmdyc.add_widget(self.p8)
        self.gmdyc.add_widget(self.t8)

        self.nine = TextInput(text='7:10', background_color=(.4, 0, 1, .9), foreground_color=(1, 1, 1, 1))
        self.c9 = TextInput(allow_copy=True, foreground_color=(.55, 0, .23, 1))
        self.p9 = TextInput(allow_copy=True, foreground_color=(.55, 0, .23, 1))
        self.t9 = TextInput(allow_copy=True, foreground_color=(.55, 0, .23, 1))

        self.gmdyc.add_widget(self.nine)
        self.gmdyc.add_widget(self.c9)
        self.gmdyc.add_widget(self.p9)
        self.gmdyc.add_widget(self.t9)

        self.ten = TextInput(text='7:50', background_color=(.4, 0, 1, .9), foreground_color=(1, 1, 1, 1))
        self.c10 = TextInput(allow_copy=True, foreground_color=(.55, 0, .23, 1))
        self.p10 = TextInput(allow_copy=True, foreground_color=(.55, 0, .23, 1))
        self.t10 = TextInput(allow_copy=True, foreground_color=(.55, 0, .23, 1))

        self.gmdyc.add_widget(self.ten)
        self.gmdyc.add_widget(self.c10)
        self.gmdyc.add_widget(self.p10)
        self.gmdyc.add_widget(self.t10)

        self.elev = TextInput(text='8:30', background_color=(.4, 0, 1, .9), foreground_color=(1, 1, 1, 1))
        self.c11 = TextInput(allow_copy=True, foreground_color=(.55, 0, .23, 1))
        self.p11 = TextInput(allow_copy=True, foreground_color=(.55, 0, .23, 1))
        self.t11 = TextInput(allow_copy=True, foreground_color=(.55, 0, .23, 1))

        self.gmdyc.add_widget(self.elev)
        self.gmdyc.add_widget(self.c11)
        self.gmdyc.add_widget(self.p11)
        self.gmdyc.add_widget(self.t11)

        self.twel = TextInput(text='9:10', background_color=(.4, 0, 1, .9), foreground_color=(1, 1, 1, 1))
        self.c12 = TextInput(allow_copy=True, foreground_color=(.55, 0, .23, 1))
        self.p12 = TextInput(allow_copy=True, foreground_color=(.55, 0, .23, 1))
        self.t12 = TextInput(allow_copy=True, foreground_color=(.55, 0, .23, 1))

        self.gmdyc.add_widget(self.twel)
        self.gmdyc.add_widget(self.c12)
        self.gmdyc.add_widget(self.p12)
        self.gmdyc.add_widget(self.t12)

        self.thirt = TextInput(text='9:50', background_color=(.4, 0, 1, .9), foreground_color=(1, 1, 1, 1))
        self.c13 = TextInput(allow_copy=True, foreground_color=(.55, 0, .23, 1))
        self.p13 = TextInput(allow_copy=True, foreground_color=(.55, 0, .23, 1))
        self.t13 = TextInput(allow_copy=True, foreground_color=(.55, 0, .23, 1))

        self.gmdyc.add_widget(self.thirt)
        self.gmdyc.add_widget(self.c13)
        self.gmdyc.add_widget(self.p13)
        self.gmdyc.add_widget(self.t13)

        self.forten = TextInput(text='10:30', background_color=(.4, 0, 1, .9), foreground_color=(1, 1, 1, 1))
        self.c14 = TextInput(allow_copy=True, foreground_color=(.55, 0, .23, 1))
        self.p14 = TextInput(allow_copy=True, foreground_color=(.55, 0, .23, 1))
        self.t14 = TextInput(allow_copy=True, foreground_color=(.55, 0, .23, 1))

        self.gmdyc.add_widget(self.forten)
        self.gmdyc.add_widget(self.c14)
        self.gmdyc.add_widget(self.p14)
        self.gmdyc.add_widget(self.t14)

        self.fift = TextInput(text='11:10', background_color=(.4, 0, 1, .9), foreground_color=(1, 1, 1, 1))
        self.c15 = TextInput(allow_copy=True, foreground_color=(.55, 0, .23, 1))
        self.p15 = TextInput(allow_copy=True, foreground_color=(.55, 0, .23, 1))
        self.t15 = TextInput(allow_copy=True, foreground_color=(.55, 0, .23, 1))

        self.gmdyc.add_widget(self.fift)
        self.gmdyc.add_widget(self.c15)
        self.gmdyc.add_widget(self.p15)
        self.gmdyc.add_widget(self.t15)

        self.sixt = TextInput(text='11:50', background_color=(.4, 0, 1, .9), foreground_color=(1, 1, 1, 1))
        self.c16 = TextInput(allow_copy=True, foreground_color=(.55, 0, .23, 1))
        self.p16 = TextInput(allow_copy=True, foreground_color=(.55, 0, .23, 1))
        self.t16 = TextInput(allow_copy=True, foreground_color=(.55, 0, .23, 1))

        self.gmdyc.add_widget(self.sixt)
        self.gmdyc.add_widget(self.c16)
        self.gmdyc.add_widget(self.p16)
        self.gmdyc.add_widget(self.t16)

        self.seven = TextInput(text='12:30', background_color=(.4, 0, 1, .9), foreground_color=(1, 1, 1, 1))
        self.c17 = TextInput(allow_copy=True, foreground_color=(.55, 0, .23, 1))
        self.p17 = TextInput(allow_copy=True, foreground_color=(.55, 0, .23, 1))
        self.t17 = TextInput(allow_copy=True, foreground_color=(.55, 0, .23, 1))

        self.gmdyc.add_widget(self.seven)
        self.gmdyc.add_widget(self.c17)
        self.gmdyc.add_widget(self.p17)
        self.gmdyc.add_widget(self.t17)
        # TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT

        self.eiten = TextInput(text='13:10', background_color=(.4, 0, 1, .9), foreground_color=(1, 1, 1, 1))
        self.c18 = TextInput(allow_copy=True, foreground_color=(.55, 0, .23, 1))
        self.p18 = TextInput(allow_copy=True, foreground_color=(.55, 0, .23, 1))
        self.t18 = TextInput(allow_copy=True, foreground_color=(.55, 0, .23, 1))

        self.gmdyc.add_widget(self.eiten)
        self.gmdyc.add_widget(self.c18)
        self.gmdyc.add_widget(self.p18)
        self.gmdyc.add_widget(self.t18)

        self.nineten = TextInput(text='13:50', background_color=(.4, 0, 1, .9), foreground_color=(1, 1, 1, 1))
        self.c19 = TextInput(allow_copy=True, foreground_color=(.55, 0, .23, 1))
        self.p19 = TextInput(allow_copy=True, foreground_color=(.55, 0, .23, 1))
        self.t19 = TextInput(allow_copy=True, foreground_color=(.55, 0, .23, 1))

        self.gmdyc.add_widget(self.nineten)
        self.gmdyc.add_widget(self.c19)
        self.gmdyc.add_widget(self.p19)
        self.gmdyc.add_widget(self.t19)

        self.twe = TextInput(text='14:30', background_color=(.4, 0, 1, .9), foreground_color=(1, 1, 1, 1))
        self.c20 = TextInput(allow_copy=True, foreground_color=(.55, 0, .23, 1))
        self.p20 = TextInput(allow_copy=True, foreground_color=(.55, 0, .23, 1))
        self.t20 = TextInput(allow_copy=True, foreground_color=(.55, 0, .23, 1))

        self.gmdyc.add_widget(self.twe)
        self.gmdyc.add_widget(self.c20)
        self.gmdyc.add_widget(self.p20)
        self.gmdyc.add_widget(self.t20)

        self.twe1 = TextInput(text='15:10', background_color=(.4, 0, 1, .9), foreground_color=(1, 1, 1, 1))
        self.c21 = TextInput(allow_copy=True, foreground_color=(.55, 0, .23, 1))
        self.p21 = TextInput(allow_copy=True, foreground_color=(.55, 0, .23, 1))
        self.t21 = TextInput(allow_copy=True, foreground_color=(.55, 0, .23, 1))

        self.gmdyc.add_widget(self.twe1)
        self.gmdyc.add_widget(self.c21)
        self.gmdyc.add_widget(self.p21)
        self.gmdyc.add_widget(self.t21)

        self.twe2 = TextInput(text='15:50', background_color=(.4, 0, 1, .9), foreground_color=(1, 1, 1, 1))
        self.c22 = TextInput(allow_copy=True, foreground_color=(.55, 0, .23, 1))
        self.p22 = TextInput(allow_copy=True, foreground_color=(.55, 0, .23, 1))
        self.t22 = TextInput(allow_copy=True, foreground_color=(.55, 0, .23, 1))

        self.gmdyc.add_widget(self.twe2)
        self.gmdyc.add_widget(self.c22)
        self.gmdyc.add_widget(self.p22)
        self.gmdyc.add_widget(self.t22)

        self.twe3 = TextInput(text='16:30', background_color=(.4, 0, 1, .9), foreground_color=(1, 1, 1, 1))
        self.c23 = TextInput(allow_copy=True, foreground_color=(.55, 0, .23, 1))
        self.p23 = TextInput(allow_copy=True, foreground_color=(.55, 0, .23, 1))
        self.t23 = TextInput(allow_copy=True, foreground_color=(.55, 0, .23, 1))

        self.gmdyc.add_widget(self.twe3)
        self.gmdyc.add_widget(self.c23)
        self.gmdyc.add_widget(self.p23)
        self.gmdyc.add_widget(self.t23)

        self.twe4 = TextInput(text='17:10', background_color=(.4, 0, 1, .9), foreground_color=(1, 1, 1, 1))
        self.c24 = TextInput(allow_copy=True, foreground_color=(.55, 0, .23, 1))
        self.p24 = TextInput(allow_copy=True, foreground_color=(.55, 0, .23, 1))
        self.t24 = TextInput(allow_copy=True, foreground_color=(.55, 0, .23, 1))

        self.gmdyc.add_widget(self.twe4)
        self.gmdyc.add_widget(self.c24)
        self.gmdyc.add_widget(self.p24)
        self.gmdyc.add_widget(self.t24)

        self.twe5 = TextInput(text='17:50', background_color=(.4, 0, 1, .9), foreground_color=(1, 1, 1, 1))
        self.c25 = TextInput(allow_copy=True, foreground_color=(.55, 0, .23, 1))
        self.p25 = TextInput(allow_copy=True, foreground_color=(.55, 0, .23, 1))
        self.t25 = TextInput(allow_copy=True, foreground_color=(.55, 0, .23, 1))

        self.gmdyc.add_widget(self.twe5)
        self.gmdyc.add_widget(self.c25)
        self.gmdyc.add_widget(self.p25)
        self.gmdyc.add_widget(self.t25)

        self.twe6 = TextInput(text='18:30', background_color=(.4, 0, 1, .9), foreground_color=(1, 1, 1, 1))
        self.c26 = TextInput(allow_copy=True, foreground_color=(.55, 0, .23, 1))
        self.p26 = TextInput(allow_copy=True, foreground_color=(.55, 0, .23, 1))
        self.t26 = TextInput(allow_copy=True, foreground_color=(.55, 0, .23, 1))

        self.gmdyc.add_widget(self.twe6)
        self.gmdyc.add_widget(self.c26)
        self.gmdyc.add_widget(self.p26)
        self.gmdyc.add_widget(self.t26)

        self.twe7 = TextInput(text='19:10', background_color=(.4, 0, 1, .9), foreground_color=(1, 1, 1, 1))
        self.c27 = TextInput(allow_copy=True, foreground_color=(.55, 0, .23, 1))
        self.p27 = TextInput(allow_copy=True, foreground_color=(.55, 0, .23, 1))
        self.t27 = TextInput(allow_copy=True, foreground_color=(.55, 0, .23, 1))

        self.gmdyc.add_widget(self.twe7)
        self.gmdyc.add_widget(self.c27)
        self.gmdyc.add_widget(self.p27)
        self.gmdyc.add_widget(self.t27)
        #   TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
        # self.gmdyc.add_widget(self.)
        self.gEXT.add_widget(self.gmdyc)
        self.scrolltable.add_widget(self.gEXT)
        self.add_widget(self.scrolltable)
        self.gtable = GridLayout(cols=3)
        Clock.schedule_once(self.Hiko)

    def Hiko(self, sp, t=None):

        if os.path.isfile(
                DIR + 'media' + PTH + '0' + PTH + 'TABLE' + PTH + '' + self.YR.text + '' + PTH + '' + self.Cll.text.strip() + '' + PTH + '' + self.mnt.text + '.json'):
            nf = open(
                DIR + 'media' + PTH + '0' + PTH + 'TABLE' + PTH + '' + self.YR.text + '' + PTH + '' + self.Cll.text.strip() + '' + PTH + '' + self.mnt.text + '.json',
                'r')
            DT = json.load(nf)
            nf.close()
            if DT.get(self.DY.text, 0):
                self.eit.text = DT[self.DY.text]["08"]["time"]
                self.c8.text = DT[self.DY.text]["08"]['course']
                self.p8.text = DT[self.DY.text]["08"]['page']
                self.t8.text = DT[self.DY.text]["08"]['teacher']

                self.nine.text = DT[self.DY.text]["09"]["time"]
                self.c9.text = DT[self.DY.text]['09']['course']
                self.p9.text = DT[self.DY.text]['09']['page']
                self.t9.text = DT[self.DY.text]['09']['teacher']

                self.ten.text = DT[self.DY.text]["10"]["time"]
                self.c10.text = DT[self.DY.text]["10"]['course']
                self.p10.text = DT[self.DY.text]['10']['page']
                self.t10.text = DT[self.DY.text]['10']['teacher']

                self.elev.text = DT[self.DY.text]["11"]["time"]
                self.c11.text = DT[self.DY.text]['11']['course']
                self.p11.text = DT[self.DY.text]['11']['page']
                self.t11.text = DT[self.DY.text]['11']['teacher']

                self.twel.text = DT[self.DY.text]["12"]["time"]
                self.c12.text = DT[self.DY.text]['12']['course']
                self.p12.text = DT[self.DY.text]['12']['page']
                self.t12.text = DT[self.DY.text]['12']['teacher']

                self.thirt.text = DT[self.DY.text]["13"]["time"]
                self.c13.text = DT[self.DY.text]['13']['course']
                self.p13.text = DT[self.DY.text]['13']['page']
                self.t13.text = DT[self.DY.text]['13']['teacher']

                self.forten.text = DT[self.DY.text]["14"]["time"]
                self.c14.text = DT[self.DY.text]['14']['course']
                self.p14.text = DT[self.DY.text]['14']['page']
                self.t14.text = DT[self.DY.text]['14']['teacher']

                self.fift.text = DT[self.DY.text]["15"]["time"]
                self.c15.text = DT[self.DY.text]['15']['course']
                self.p15.text = DT[self.DY.text]['15']['page']
                self.t15.text = DT[self.DY.text]['15']['teacher']

                self.sixt.text = DT[self.DY.text]["16"]["time"]
                self.c16.text = DT[self.DY.text]['16']['course']
                self.p16.text = DT[self.DY.text]['16']['page']
                self.t16.text = DT[self.DY.text]['16']['teacher']

                self.seven.text = DT[self.DY.text]["17"]["time"]
                self.c17.text = DT[self.DY.text]["17"]['course']
                self.p17.text = DT[self.DY.text]["17"]['page']
                self.t17.text = DT[self.DY.text]["17"]['teacher']
                #
                self.eiten.text = DT[self.DY.text]["18"]["time"]
                self.c18.text = DT[self.DY.text]["18"]['course']
                self.p18.text = DT[self.DY.text]["18"]['page']
                self.t18.text = DT[self.DY.text]["18"]['teacher']

                self.nineten.text = DT[self.DY.text]["19"]["time"]
                self.c19.text = DT[self.DY.text]["19"]['course']
                self.p19.text = DT[self.DY.text]["19"]['page']
                self.t19.text = DT[self.DY.text]["19"]['teacher']

                self.twe.text = DT[self.DY.text]["20"]["time"]
                self.c20.text = DT[self.DY.text]["20"]['course']
                self.p20.text = DT[self.DY.text]["20"]['page']
                self.t20.text = DT[self.DY.text]["20"]['teacher']

                self.twe1.text = DT[self.DY.text]["21"]["time"]
                self.c21.text = DT[self.DY.text]["21"]['course']
                self.p21.text = DT[self.DY.text]["21"]['page']
                self.t21.text = DT[self.DY.text]["21"]['teacher']

                self.twe2.text = DT[self.DY.text]["22"]["time"]
                self.c22.text = DT[self.DY.text]["22"]['course']
                self.p22.text = DT[self.DY.text]["22"]['page']
                self.t22.text = DT[self.DY.text]["22"]['teacher']

                self.twe3.text = DT[self.DY.text]["23"]["time"]
                self.c23.text = DT[self.DY.text]["23"]['course']
                self.p23.text = DT[self.DY.text]["23"]['page']
                self.t23.text = DT[self.DY.text]["23"]['teacher']

                self.twe4.text = DT[self.DY.text]["24"]["time"]
                self.c24.text = DT[self.DY.text]["24"]['course']
                self.p24.text = DT[self.DY.text]["24"]['page']
                self.t24.text = DT[self.DY.text]["24"]['teacher']

                self.twe5.text = DT[self.DY.text]["25"]["time"]
                self.c25.text = DT[self.DY.text]["25"]['course']
                self.p25.text = DT[self.DY.text]["25"]['page']
                self.t25.text = DT[self.DY.text]["25"]['teacher']

                self.twe6.text = DT[self.DY.text]["26"]["time"]
                self.c26.text = DT[self.DY.text]["26"]['course']
                self.p26.text = DT[self.DY.text]["26"]['page']
                self.t26.text = DT[self.DY.text]["26"]['teacher']

                self.twe7.text = DT[self.DY.text]["27"]["time"]
                self.c27.text = DT[self.DY.text]["27"]['course']
                self.p27.text = DT[self.DY.text]["27"]['page']
                self.t27.text = DT[self.DY.text]["27"]['teacher']

                six = ['parade', 'rem', ]
                nine = ['breakfast']
                ten = ["assembly", 'fellowship', 'breakfast', 'break', 'lunch']
                deba = ['debate']
                end = ['general', 'cleaning', 'clean', 'gen']
                even = ['even', 'evening']

                v = [self.c8, self.c9, self.c10, self.c11, self.c12, self.c14, self.c13, self.c15, self.c16, self.c17,
                     self.c18, self.c19, self.c20,
                     self.c21, self.c22, self.c23, self.c24, self.c25, self.c26, self.c27]
                pl = [self.p8, self.p9, self.p10, self.p11, self.p12, self.p14, self.p13, self.p15, self.p16, self.p17,
                      self.p18, self.p19, self.p20,
                      self.p21, self.p22, self.p23, self.p24, self.p25, self.p26, self.p27]
                tl = [self.t8, self.t9, self.t10, self.t11, self.t12, self.t14, self.t13, self.t15, self.t16, self.t17,
                      self.t18, self.t19, self.t20,
                      self.t21, self.t22, self.t23, self.t24, self.t25, self.t26, self.t27]

                for i in v:
                    if i.text.lower() in six:
                        i.background_color = (0, 1, 0, 1)
                    if i.text.lower() in nine:
                        i.background_color = (0, 0, 1, 1)
                    if i.text.lower() in ten:
                        i.background_color = (1, 0, 1, 1)
                    if i.text.lower() in deba:
                        i.background_color = (1, 1, 0, 1)
                    if i.text.lower() in even:
                        i.background_color = (1, .5, .5, 1)
                    if i.text.lower() in end:
                        i.background_color = (1, 0, 0, 1)
                    if i.text == "":
                        i.background_color = (1, 1, 1, 1)
                for z in pl:
                    if z.text.lower() in six:
                        z.background_color = (0, 1, 0, 1)
                    if z.text.lower() in nine:
                        z.background_color = (0, 0, 1, 1)
                    if z.text.lower() in ten:
                        z.background_color = (1, 0, 1, 1)
                    if z.text.lower() in deba:
                        z.background_color = (1, 1, 0, 1)
                    if z.text.lower() in even:
                        z.background_color = (1, .5, .5, 1)
                    if z.text.lower() in end:
                        z.background_color = (1, 0, 0, 1)
                    if z.text == "":
                        z.background_color = (1, 1, 1, 1)

                for m in tl:
                    if m.text.lower() in six:
                        m.background_color = (0, 1, 0, 1)
                    if m.text.lower() in nine:
                        m.background_color = (0, 0, 1, 1)
                    if m.text.lower() in ten:
                        m.background_color = (1, 0, 1, 1)
                    if m.text.lower() in deba:
                        m.background_color = (1, 1, 0, 1)
                    if m.text.lower() in even:
                        m.background_color = (1, .5, .5, 1)
                    if m.text.lower() in end:
                        m.background_color = (1, 0, 0, 1)
                    if m.text == "":
                        m.background_color = (1, 1, 1, 1)

                del six
                del nine
                del ten
                del deba
                del even
                del end

            else:

                x = 8
                for i in range(20):
                    exec("self.c" + str(x) + ".background_color=(1,1,1,1)")
                    exec("self.p" + str(x) + ".background_color=(1,1,1,1)")
                    exec("self.t" + str(x) + ".background_color=(1,1,1,1)")
                    exec("self.c" + str(x) + ".text=''")
                    exec("self.p" + str(x) + ".text=''")
                    exec("self.t" + str(x) + ".text=''")
                    x += 1


        else:

            x = 8
            for i in range(20):
                exec("self.c" + str(x) + ".background_color=(1,1,1,1)")
                exec("self.p" + str(x) + ".background_color=(1,1,1,1)")
                exec("self.t" + str(x) + ".background_color=(1,1,1,1)")
                exec("self.c" + str(x) + ".text=''")
                exec("self.p" + str(x) + ".text=''")
                exec("self.t" + str(x) + ".text=''")
                x += 1

        # x=8
        # for i in range(20) :
        #     exec("print('background') if self.c"+str(x)+".text in ten ")
        #     # exec()

    #     date=[]
    #     for i in DT.keys():
    #         date.append(i.strip())
    #
    #     self.TOD=Spinner(text=C[0],color=(0,0,0,1),values=tuple(C),size_hint=(.13,.06),pos_hint={'center_x':.5,'center_y':.88})
    #     self.TOD.bind(text=self.CHC)
    #     self.nyu=Button(size_hint=(.68,.76),pos_hint={'center_x':.65,'center_y':.45},background_color=(0,0,1,.4))
    #     self.add_widget(self.nyu)
    #     self.DDO = Spinner(text=time.strftime('%d %B %Y'), color=(0, 0, 0, 1), values=tuple(date), size_hint=(.2, .06),
    #                        pos_hint={'center_x': .75, 'center_y': .88})
    #     self.DDO.bind(text=self.CHD)
    #     self.add_widget(self.DDO)
    #     self.add_widget(self.TOD)
    #     # if not DT.get(self.DDO.text) :
    #     #     return
    #     # if not DT[self.DDO.text].get(self.TOD.text):
    #     #     return
    #     Clock.schedule_once(self.HHR)
    # def CHC(self,sp,t):
    #     print(sp.text,len(sp.text))
    #     self.TOD.text=t
    #     Clock.schedule_once(self.HHR)
    #
    # def CHD(self,sp,t):
    #     self.DDO.text = t
    #     Clock.schedule_once(self.HHR)
    #
    # def HHR(self,aass):
    #     try:
    #         self.remove_widget(self.gHRR)
    #     except:
    #         pass
    #     TDAT = open(DIR+'media'+PTH+'.0'+PTH+'TABLE.json', 'r')
    #     DT = json.load(TDAT)
    #     TDAT.close()
    #     if not DT.get(self.DDO.text):
    #         return
    #     if not DT[self.DDO.text].get(self.TOD.text):
    #         return
    #
    #     self.gHRR=GridLayout(cols=3,size_hint=(.59,.6),pos_hint={'center_x':.62,'center_y':.45})
    #     self.gHRR.add_widget(Label(text='HOURS'))
    #     self.gHRR.add_widget(Label(text='COURSE'))
    #     self.gHRR.add_widget(Label(text='TEACHER'))
    #     self.gHRR.add_widget(Label(text=''))
    #     self.gHRR.add_widget(Label(text=''))
    #     self.gHRR.add_widget(Label(text=''))
    #     self.gHRR.add_widget(Label(text='07'))
    #     self.gHRR.add_widget(Label(text=''))
    #     self.gHRR.add_widget(Label(text=''))        #  IF INTEL CHANGES DATA ? ...
    #     self.gHRR.add_widget(Label(text='08'))
    #     self.gHRR.add_widget(Label(text=DT[self.DDO.text][self.TOD.text]['08']['course']+"\ "+DT[self.DDO.text][self.TOD.text]['08']['page']))
    #     self.gHRR.add_widget(Label(text=DT[self.DDO.text][self.TOD.text]['08']['teacher']))          #   MAKE VARIABLE ASIDE WICH CAN CANGE
    #     self.gHRR.add_widget(Label(text='09'))
    #     self.gHRR.add_widget(Label(text=DT[self.DDO.text][self.TOD.text]['09']['course']+"\ "+DT[self.DDO.text][self.TOD.text]['09']['page']))
    #     self.gHRR.add_widget(Label(text=DT[self.DDO.text][self.TOD.text]['09']['teacher']))          #     SELF. TOD   WILL CHANGE ALL
    #     self.gHRR.add_widget(Label(text='10'))
    #     self.gHRR.add_widget(Label(text=DT[self.DDO.text][self.TOD.text]['10']['course']+"\ "+DT[self.DDO.text][self.TOD.text]['10']['page']))
    #     self.gHRR.add_widget(Label(text=DT[self.DDO.text][self.TOD.text]['10']['teacher']))     #   on clic=self.TOD.TEXT=  P2   CLOCK SELF.TODAY
    #     self.gHRR.add_widget(Label(text='11'))
    #     self.gHRR.add_widget(Label(text=DT[self.DDO.text][self.TOD.text]['11']['course']+"\ "+DT[self.DDO.text][self.TOD.text]['11']['page']))
    #     self.gHRR.add_widget(Label(text=DT[self.DDO.text][self.TOD.text]['11']['teacher']))
    #     self.gHRR.add_widget(Label(text='12'))
    #     self.gHRR.add_widget(Label(text=DT[self.DDO.text][self.TOD.text]['12']['course']+"\ "+DT[self.DDO.text][self.TOD.text]['12']['page']))
    #     self.gHRR.add_widget(Label(text=DT[self.DDO.text][self.TOD.text]['12']['teacher']))
    #     self.gHRR.add_widget(Label(text='13'))
    #     self.gHRR.add_widget(Label(text=DT[self.DDO.text][self.TOD.text]['13']['course']+"\ "+DT[self.DDO.text][self.TOD.text]['13']['page']))
    #     self.gHRR.add_widget(Label(text=DT[self.DDO.text][self.TOD.text]['13']['teacher']))
    #     self.gHRR.add_widget(Label(text='14'))
    #     self.gHRR.add_widget(Label(text=DT[self.DDO.text][self.TOD.text]['14']['course']+"\ "+DT[self.DDO.text][self.TOD.text]['14']['page']))
    #     self.gHRR.add_widget(Label(text=DT[self.DDO.text][self.TOD.text]['14']['teacher']))
    #     self.gHRR.add_widget(Label(text='15'))
    #     self.gHRR.add_widget(Label(text=DT[self.DDO.text][self.TOD.text]['15']['course']+"\ "+DT[self.DDO.text][self.TOD.text]['15']['page']))
    #     self.gHRR.add_widget(Label(text=DT[self.DDO.text][self.TOD.text]['15']['teacher']))
    #     self.gHRR.add_widget(Label(text='16'))
    #     self.gHRR.add_widget(Label(text=DT[self.DDO.text][self.TOD.text]['16']['course']+"\ "+DT[self.DDO.text][self.TOD.text]['16']['page']))
    #     self.gHRR.add_widget(Label(text=DT[self.DDO.text][self.TOD.text]['16']['teacher']))
    #     self.gHRR.add_widget(Label(text='17'))
    #     self.gHRR.add_widget(Label(text=DT[self.DDO.text][self.TOD.text]['17']['course']+"\ "+DT[self.DDO.text][self.TOD.text]['17']['page']))
    #     self.gHRR.add_widget(Label(text=DT[self.DDO.text][self.TOD.text]['17']['teacher']))
    #     self.add_widget(self.gHRR)

    def cgadt(self, v):
        self.remove_widget(self.gadt)
        self.remove_widget(self.gCour)
        self.remove_widget(self.Lcourse)
        self.remove_widget(self.Savb)

    def white(self, ev):
        if self.ww >= 1.:
            self.ww = self.ww
            Clock.unschedule(self.white)

        else:
            self.ww += .01
            self.idd.background_color = (.8, 0, 1, self.ww)  # .2,.1,.2

    def black(self, ev):
        if self.xww <= 0:
            self.ww = self.xww
            Clock.unschedule(self.black)
        else:
            self.xww -= .01
            self.idd.background_color = (.8, 0, 1, self.xww)  # .2,.1,.2

    def SECwhite(self, ev):
        if self.ww >= .97:
            self.ww = self.ww
            Clock.unschedule(self.SECwhite)
            # Clock.unschedule(self.back)
        else:
            self.ww += .01
            self.idd.background_color = (.3, .3, .3, self.ww)


    def opac(self,x):
        if self.opp >= .97:
            self.opp = self.opp
            Clock.unschedule(self.opac)
            # Clock.unschedule(self.back)
        else:
            self.opp += .01
            self.idd.background_color = (0,0,0, self.opp)

    def secretaire(self, event):
        if not lv in ('sc', 'adm'):
            return
        try:
            self.add_widget(self.idd)
        except:
            pass
        self.b_c = 0
        Clock.schedule_interval(self.back, .02)

        self.secgrid = GridLayout(cols=1, size_hint=(.28, .8), pos_hint={'center_x': .5, 'center_y': .5}, spacing=13)

        self.card = Button(text='Detailed marks ', font_size=27, italic=True,
                              background_normal="", color=(1, 1, 1, .5), background_color=(1, 0, 1, .7),on_release=self.crd)
        self.signal = "1"
        self.secgrid.add_widget(self.card)
        self.report = Button(text='Fill & Print R_Card', font_size=27, italic=True,
                              background_normal="bt3.png", color=(1, 1, 1, .5),
                             background_color=(1, 0, 1, .7),on_release=self.SUBJECT_AND_MARKS)
        self.secgrid.add_widget(self.report)
        self.addst = Button(text='Add Student', color=(1, 1, 1, .5), font_size=27, background_normal="bt3.png",
                            background_color=(1, 0, 1, .7),
                            on_release=self.adst)
        self.secgrid.add_widget(self.addst)
        self.disable = Button(text='Disable Student', color=(1, 1, 1, .5), font_size=27, italic=True,
                              background_normal="bt3.png", background_color=(1, 0, 1, .7),
                              on_release=self.dsble)
        self.secgrid.add_widget(self.disable)
        self.move = Button(text='Shift Student', color=(1, 1, 1, .5), font_size=27, background_normal="bt3.png",
                           background_color=(1, 0, 1, .7),
                           on_release=self.shft)
        self.secgrid.add_widget(self.move)
        self.addcls = Button(text='Add class', color=(1, 1, 1, .5), font_size=27, background_normal="bt3.png",
                             background_color=(1, 0, 1, .7),
                             on_release=self.newcls)
        self.secgrid.add_widget(self.addcls)

        self.add_widget(self.secgrid)

    def oC(self, sp, t=None):
        if self.DAY.text == "" or self.MONTH.text == "":
            return

        if self.SP_GN.text == "GAINED":
            self.GSC.cols = 3
            Clock.schedule_once(self.OK)
        else:
            self.GSC.cols = 2

        try:
            self.GSC.clear_widgets()
        except:
            pass

        try:
            self.SC.clear_widgets()
        except:
            pass
        try:
            self.remove_widget(self.SC)
        except:
            pass
        try:
            self.gaside.clear_widgets()
        except:
            pass
        try:
            self.remove_widget(self.gaside)
        except:
            pass

        FF = open(DIR + 'media' + PTH + '0' + PTH + 'FINANCE.json', 'r')
        DF = json.load(FF)
        FF.close()
        sz = 0

        today = DF[self.YEAR.text][self.MONTH.text][self.DAY.text]['TSP']['T']
        del DF[self.YEAR.text][self.MONTH.text][self.DAY.text]['TSP']['T']
        for fi in DF[self.YEAR.text][self.MONTH.text][self.DAY.text]['TSP'].keys():
            zx = DF[self.YEAR.text][self.MONTH.text][self.DAY.text]['TSP'][fi]
            self.GSC.add_widget(TextInput(text=fi, readonly=True, allow_copy=True))
            self.GSC.add_widget(TextInput(text=milli(zx), readonly=True, allow_copy=True))
            sz += 1

        self.GSC.add_widget(TextInput(text="", readonly=True, allow_copy=True))
        self.GSC.add_widget(TextInput(text="", readonly=True, allow_copy=True))
        self.GSC.add_widget(TextInput(text="", readonly=True, allow_copy=True))
        self.GSC.add_widget(TextInput(text=milli(str(today)) + " ugx", readonly=True, allow_copy=True))
        sz += 2

        # self.GSC.add_widget(self.dis)
        self.SC.add_widget(self.GSC)
        self.GSC.size_hint = (None, None)
        self.GSC.size = (440, 30 * sz + 100)

        self.gaside.add_widget(self.gborrow)
        self.gaside.add_widget(self.sp_sele)
        self.gaside.add_widget(self.SC)
        self.gaside.add_widget(
            Button(text="TOTAL : " + str(today) + " ugx", size_hint=(1., .1), on_release=self.SPsave))
        self.add_widget(self.gaside)
        # Clock.schedule_once(self.SPsave, 5)

    def SPMempt(self, sp, tx=None):
        if self.MONTH.text == "":
            return
        if self.SP_GN.text == "GAINED":
            self.GSC.cols = 3
            Clock.schedule_once(self.Mempt)
        else:
            self.GSC.cols = 2

        FF = open(DIR + 'media' + PTH + '0' + PTH + 'FINANCE.json', 'r')
        DF = json.load(FF)
        FF.close()
        self.DAY.text = ""
        self.DAY.values = tuple(DF[self.YEAR.text][self.MONTH.text].keys())

        # *******************************************************************
        try:
            self.GSC.clear_widgets()
        except:
            pass

        try:
            self.SC.clear_widgets()
        except:
            pass
        try:
            self.remove_widget(self.SC)
        except:
            pass
        try:
            self.gaside.clear_widgets()
        except:
            pass
        try:
            self.remove_widget(self.gaside)
        except:
            pass

        FF = open(DIR + 'media' + PTH + '0' + PTH + 'FINANCE.json', 'r')
        DF = json.load(FF)
        FF.close()
        today = 0
        xl = {}
        sz = 0
        # today = DF[self.YEAR.text][self.MONTH.text][self.DAY.text]['TGN']['T']
        # del DF[self.YEAR.text][self.MONTH.text][self.DAY.text]['TGN']['T']
        for day in DF[self.YEAR.text][self.MONTH.text].keys():  # [self.DAY.text]['TGN']
            today += float(DF[self.YEAR.text][self.MONTH.text][day]['TSP']['T'])
            del DF[self.YEAR.text][self.MONTH.text][day]['TSP']['T']
            for fi in DF[self.YEAR.text][self.MONTH.text][day]['TSP'].keys():
                zx = DF[self.YEAR.text][self.MONTH.text][day]['TSP'][fi]
                if xl.get(fi, 0):
                    hd = xl[fi]
                    xl[fi] = str(float(zx) + float(hd))
                if not xl.get(fi, 0):
                    xl[fi] = zx
                self.GSC.add_widget(TextInput(text=fi, readonly=True, allow_copy=True))
                self.GSC.add_widget(TextInput(text=milli(zx), readonly=True, allow_copy=True))
                sz += 1

        self.GSC.add_widget(TextInput(text="", readonly=True, allow_copy=True))
        self.GSC.add_widget(TextInput(text="", readonly=True, allow_copy=True))
        self.GSC.add_widget(TextInput(text="TOTAL", background_color=(0, 0, 0, 1), foreground_color=(1, 1, 1, 1), readonly=True,
                      allow_copy=True))
        self.GSC.add_widget( TextInput(text=milli(str(today)) + " ugx", background_color=(0, 0, 0, 1), foreground_color=(1, 1, 1, 1),
                      readonly=True, allow_copy=True))
        self.GSC.add_widget(TextInput(text="", readonly=True, allow_copy=True))
        self.GSC.add_widget(TextInput(text="", readonly=True, allow_copy=True))
        sz += 3
        for y in xl.keys():
            self.GSC.add_widget(TextInput(text=y, readonly=True, allow_copy=True))
            self.GSC.add_widget(TextInput(text=milli(xl[y]), readonly=True, allow_copy=True))
            sz += 1

        # self.GSC.add_widget(self.dis)
        self.SC.add_widget(self.GSC)
        self.GSC.size_hint = (None, None)
        self.GSC.size = (440, 30 * sz + 100)

        self.gaside.add_widget(self.gborrow)
        self.gaside.add_widget(self.sp_sele)
        self.gaside.add_widget(self.SC)
        self.gaside.add_widget(
            Button(text="TOTAL : " + milli(str(today)) + " ugx", size_hint=(1., .1), on_release=self.SPsave))
        self.add_widget(self.gaside)
        # Clock.schedule_once(self.SPsave, 5)

    def SPYempt(self, sp, tx=None):
        if tx =="RESET" :
            return
        if self.SP_GN.text == "GAINED":
            self.GSC.cols = 3
            Clock.schedule_once(self.Yempt)
        else:
            self.GSC.cols = 2

        FF = open(DIR + 'media' + PTH + '0' + PTH + 'FINANCE.json', 'r')
        DF = json.load(FF)
        FF.close()
        self.DAY.text = ""
        self.MONTH.text = ""
        self.MONTH.values = tuple(DF[self.YEAR.text].keys())

        # *******************************************************************

        try:
            self.GSC.clear_widgets()
        except:
            pass

        try:
            self.SC.clear_widgets()
        except:
            pass
        try:
            self.remove_widget(self.SC)
        except:
            pass
        try:
            self.gaside.clear_widgets()
        except:
            pass
        try:
            self.remove_widget(self.gaside)
        except:
            pass

        zzz = open(DIR + 'media' + PTH + '0' + PTH + 'DEPANS', 'rb')
        x = pickle.load(zzz)
        zzz.close()

        FF = open(DIR + 'media' + PTH + '0' + PTH + 'FINANCE.json', 'r')
        DF = json.load(FF)
        FF.close()
        today = 0
        xl = {}
        sz = 0
        # today = DF[self.YEAR.text][self.MONTH.text][self.DAY.text]['TGN']['T']
        # del DF[self.YEAR.text][self.MONTH.text][self.DAY.text]['TGN']['T']
        for ye in DF[self.YEAR.text].keys():
            for day in DF[self.YEAR.text][ye].keys():  # [self.DAY.text]['TGN']
                today += float(DF[self.YEAR.text][ye][day]['TSP']['T'])
                del DF[self.YEAR.text][ye][day]['TSP']['T']
                for fi in DF[self.YEAR.text][ye][day]['TSP'].keys():
                    zx = DF[self.YEAR.text][ye][day]['TSP'][fi]

                    if xl.get(fi, 0):
                        hd = xl[fi]
                        xl[fi] = str(float(zx) + float(hd))
                    if not xl.get(fi, 0):
                        xl[fi] = zx

                    self.GSC.add_widget(TextInput(text=fi, readonly=True, allow_copy=True))
                    self.GSC.add_widget(TextInput(text=milli(zx), readonly=True, allow_copy=True))
                    sz += 1

        self.GSC.add_widget(TextInput(text="", readonly=True, allow_copy=True))
        self.GSC.add_widget(TextInput(text="", readonly=True, allow_copy=True))
        self.GSC.add_widget(
            TextInput(text="TOTAL", background_color=(0, 0, 0, 1), foreground_color=(1, 1, 1, 1), readonly=True,
                      allow_copy=True))
        self.GSC.add_widget(
            TextInput(text= milli(str(today)) + " ugx", background_color=(0, 0, 0, 1), foreground_color=(1, 1, 1, 1),
                      readonly=True, allow_copy=True))
        self.GSC.add_widget(TextInput(text="", readonly=True, allow_copy=True))
        self.GSC.add_widget(TextInput(text="", readonly=True, allow_copy=True))
        sz += 3
        for y in xl.keys():
            self.GSC.add_widget(TextInput(text=y, readonly=True, allow_copy=True))
            self.GSC.add_widget(TextInput(text=milli(xl[y]), readonly=True, allow_copy=True))
            sz += 1

        # self.GSC.add_widget(self.dis)
        self.SC.add_widget(self.GSC)
        print(xl)
        self.GSC.size_hint = (None, None)
        self.GSC.size = (840, 30 * sz + 100)

        self.gaside.add_widget(self.gborrow)
        self.gaside.add_widget(self.sp_sele)
        self.gaside.add_widget(self.SC)
        self.gaside.add_widget(
            Button(text="TOTAL : " + milli(str(today)) + " ugx", size_hint=(1., .1), on_release=self.SPsave))
        self.add_widget(self.gaside)
        # Clock.schedule_once(self.SPsave, 5)

    def SPsave(self, x):

        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

        pickl = open(DIR + 'media' + PTH + '0' + PTH + 'SCHOOL.bin', 'rb')
        ids = pickle.load(pickl)
        pickl.close()
        # '+ids['1']+'

        self.SC.remove_widget(self.GSC)
        self.exG = GridLayout(cols=1, size_hint=(None, None), size=(self.GSC.width + 400, self.GSC.height + 260),
                              pos_hint=self.GSC.pos_hint)
        les_point = GridLayout(cols=3, size_hint=(None, None), size=(900, 170))
        im = AsyncImage(source=ASY + 'L.png', size_hint=(None, None), size=(150, 150), allow_stretch=True)
        les_point.add_widget(im)
        grid_in = GridLayout(cols=1, size_hint=(None, None), size=(360, 170), row_default_height=25,
                             row_force_default=True)
        grid_in.add_widget(
            Label(text='  '+ids['1']+'               ', color=(0, 0, 1, 1), font_size=18))
        grid_in.add_widget(
            Label(text='       '+ids['2']+'               ', font_size=13, color=(0, 0, 0, 1)))
        grid_in.add_widget(
            Label(text='   '+ids['3']+'               ', font_size=13,
                  color=(0, 1, 0, 1)))
        grid_in.add_widget(
            Label(text='       '+ids['4']+'               ', font_size=13, color=(0, 0, 0, 1)))
        grid_in.add_widget(
            Label(text='     '+ids['5']+'               ', font_size=15, color=(1, 0, 0, 1)))
        # grid_in.add_widget(Label(text=' ' * 15 +self.v_class.text+' ' * 100 + ' ' * 20, underline=True, color=(1, 0, 0, 1)))
        les_point.add_widget(grid_in)
        ph = Label(text="SPENT  \n"+self.DAY.text+" "+self.MONTH.text+" "+self.YEAR.text, font_size=33, underline=True, italic=True, color=(0, 0, 0, .3))
        les_point.add_widget(ph)
        self.exG.add_widget(les_point)
        # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        self.exG.add_widget(self.GSC)
        Clock.schedule_once(self.print_sp, 3)



    def print_sp(self,s):
        self.exG.export_to_png( NDR + 'Desktop' + PTH + 'P R I N T A B L E' + PTH + '' + 'SPENDITURE ' + self.DAY.text + " " + self.MONTH.text + " " + self.YEAR.text + '.png')

        self.print_all_i( NDR + 'Desktop' + PTH + 'P R I N T A B L E' + PTH + '' + 'SPENDITURE ' + self.DAY.text + " " + self.MONTH.text + " " + self.YEAR.text + '.png')

        # try:
        #     os.startfile('SPENDITURE ' + self.DAY.text + " " + self.MONTH.text + " " + self.YEAR.text + '.png', 'print')
        # except:
        #     pass
        # import cv2
        # im=cv2.imread('SPENDITURE '+self.DAY.text+" "+self.MONTH.text+" "+self.YEAR.text+'.png')
        # rt=cv2.rotate(im,cv2.ROTATE_180)
        # cv2.imwrite('SPENDITURE '+self.DAY.text+" "+self.MONTH.text+" "+self.YEAR.text+".png",rt)
        # cv2.waitKey(0)
        # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        self.exG.remove_widget(self.GSC)
        self.SC.add_widget(self.GSC)

    def OK(self, sp, t=None):
        if self.DAY.text == "" or self.MONTH.text == "":
            return
        if self.SP_GN.text == "SPENT":
            self.GSC.cols = 2
            Clock.schedule_once(self.oC)
        else:
            self.GSC.cols = 6

        try:
            self.GSC.clear_widgets()
        except:
            pass

        try:
            self.SC.clear_widgets()
        except:
            pass
        try:
            self.remove_widget(self.SC)
        except:
            pass
        try:
            self.gaside.clear_widgets()
        except:
            pass
        try:
            self.remove_widget(self.gaside)
        except:
            pass

        FF = open(DIR + 'media' + PTH + '0' + PTH + 'FINANCE.json', 'r')
        DF = json.load(FF)
        FF.close()
        sz = 0

        if not DF[time.strftime('%Y')][time.strftime('%B')].get(time.strftime('%d')):
            DF[time.strftime('%Y')][time.strftime('%B')][time.strftime('%d')] = {}
            DF[time.strftime('%Y')][time.strftime('%B')][time.strftime('%d')]['TGN'] = {}
            DF[time.strftime('%Y')][time.strftime('%B')][time.strftime('%d')]['TSP'] = {}
            DF[time.strftime('%Y')][time.strftime('%B')][time.strftime('%d')]['TGN']['T'] = '0'
            DF[time.strftime('%Y')][time.strftime('%B')][time.strftime('%d')]['TGN']['BANK'] = '0'
            DF[time.strftime('%Y')][time.strftime('%B')][time.strftime('%d')]['TSP']['T'] = '0'
            #
            ZfN = open(DIR + 'media' + PTH + '0' + PTH + 'FINANCE.json', 'w')
            json.dump(DF, ZfN)
            ZfN.close()

        today = DF[self.YEAR.text][self.MONTH.text][self.DAY.text]['TGN']['T']
        bank =  DF[self.YEAR.text][self.MONTH.text][self.DAY.text]['TGN']['BANK']
        del DF[self.YEAR.text][self.MONTH.text][self.DAY.text]['TGN']['T']
        del DF[self.YEAR.text][self.MONTH.text][self.DAY.text]['TGN']['BANK']

        list1=["Date","Name","Class","Fees","Paid","Balance"]
        for x in list1 :
            if x == "Name":
                self.GSC.add_widget(TextInput(text=x, size_hint=(None, None), size=(300, 30), readonly=True, allow_copy=True,
                              background_color=(0, 0, 0, 1), foreground_color=(1, 1, 1, 1)))
            else:
                self.GSC.add_widget(TextInput(text=x, readonly=True, allow_copy=True, background_color=(0, 0, 0, 1), foreground_color=(1, 1, 1, 1)))

        for fi in DF[self.YEAR.text][self.MONTH.text][self.DAY.text]['TGN'].keys():
            zx = DF[self.YEAR.text][self.MONTH.text][self.DAY.text]['TGN'][fi]
            names=zx[:zx.index('_')].replace("_", "")
            classe=zx[zx.index('_'):zx.index('-')].replace('_', "")
            fees=milli(zx[zx.index('-'):zx.index(' : ')].replace('-', ""))
            paid=milli(zx[zx.index(' : '):zx.index(' ugx. ')].replace(' : ', ""))
            bal=zx[zx.index(' ugx. '):].replace(' ugx. ', "")     #.replace("-","")
            self.GSC.add_widget(TextInput(text=fi[:fi.index("_")], readonly=True, allow_copy=True))
            self.GSC.add_widget(TextInput(text=names, size_hint=(None, None), size=(300, 30),readonly=True, allow_copy=True))
            self.GSC.add_widget(TextInput(text=classe, readonly=True, allow_copy=True))
            self.GSC.add_widget(TextInput(text=fees, readonly=True, allow_copy=True))
            self.GSC.add_widget(TextInput(text=paid, readonly=True, allow_copy=True))
            if bal.startswith("-") :
                self.GSC.add_widget(TextInput(text="- "+milli(bal.replace("-","")), readonly=True, allow_copy=True))
            else:
                self.GSC.add_widget(TextInput(text="+ " + milli(bal.replace("-", "")), readonly=True, allow_copy=True))
            sz += 1

        self.GSC.add_widget(TextInput(text="", readonly=True, allow_copy=True))
        self.GSC.add_widget(TextInput(text="",size_hint=(None, None), size=(300, 30), readonly=True, allow_copy=True))
        for i in range(5):
            self.GSC.add_widget(TextInput(text="", readonly=True, allow_copy=True))
        self.GSC.add_widget( TextInput(hint_text="TOT= " + milli(today) + " ugx" + "      DEPOSIT : " + milli(str(bank)) + " ugx",size_hint=(None, None), size=(300, 30),multiline=False,foreground_color=(1,1,1,1),background_color=(0,0,0,1), readonly=True, allow_copy=True))
        for i in range(4):
            self.GSC.add_widget(TextInput(text="", readonly=True, allow_copy=True))
        sz += 3

        # self.GSC.add_widget(self.dis)
        self.SC.add_widget(self.GSC)
        self.GSC.size_hint = (None, None)
        self.GSC.size = (880, 30 * sz + 100)

        self.gaside.add_widget(self.gborrow)
        self.gaside.add_widget(self.sp_sele)
        self.gaside.add_widget(self.SC)
        self.gaside.add_widget(Button(text="TOTAL :  " + milli(str(today)) + " ugx"+"         DEPOSIT : " + milli(str(bank)) + " ugx", size_hint=(1., .1), on_release=self.ssave))
        self.add_widget(self.gaside)
        # Clock.schedule_once(self.ssave,5)

    def Mempt(self, sp, tx=None):
        if self.MONTH.text == "":
            return
        if self.SP_GN.text == "SPENT":
            self.GSC.cols = 2
            Clock.schedule_once(self.SPMempt)
        else:
            self.GSC.cols = 6

        FF = open(DIR + 'media' + PTH + '0' + PTH + 'FINANCE.json', 'r')
        DF = json.load(FF)
        FF.close()
        self.DAY.text = ""
        self.DAY.values = tuple(DF[self.YEAR.text][self.MONTH.text].keys())

        # *******************************************************************
        try:
            self.GSC.clear_widgets()
        except:
            pass

        try:
            self.SC.clear_widgets()
        except:
            pass
        try:
            self.remove_widget(self.SC)
        except:
            pass
        try:
            self.gaside.clear_widgets()
        except:
            pass
        try:
            self.remove_widget(self.gaside)
        except:
            pass

        FF = open(DIR + 'media' + PTH + '0' + PTH + 'FINANCE.json', 'r')
        DF = json.load(FF)
        FF.close()
        today = 0
        bank = 0
        sz = 0
        # today = DF[self.YEAR.text][self.MONTH.text][self.DAY.text]['TGN']['T']
        # del DF[self.YEAR.text][self.MONTH.text][self.DAY.text]['TGN']['T']

        list1 = ["Date", "Name", "Class", "Fees", "Paid", "Balance"]
        for x in list1:
            if x == "Name" :
                self.GSC.add_widget(TextInput(text=x, size_hint=(None, None), size=(300,30),readonly=True, allow_copy=True, background_color=(0, 0, 0, 1), foreground_color=(1, 1, 1, 1)))
            else:
                self.GSC.add_widget( TextInput(text=x,  readonly=True, allow_copy=True,
                              background_color=(0, 0, 0, 1), foreground_color=(1, 1, 1, 1)))

        for day in DF[self.YEAR.text][self.MONTH.text].keys():  # [self.DAY.text]['TGN']
            today += float(DF[self.YEAR.text][self.MONTH.text][day]['TGN']['T'])
            bank  += float(DF[self.YEAR.text][self.MONTH.text][day]['TGN']['BANK'])
            del DF[self.YEAR.text][self.MONTH.text][day]['TGN']['T']
            del DF[self.YEAR.text][self.MONTH.text][day]['TGN']['BANK']
            for fi in DF[self.YEAR.text][self.MONTH.text][day]['TGN'].keys():
                zx = DF[self.YEAR.text][self.MONTH.text][day]['TGN'][fi]
                names = zx[:zx.index('_')].replace("_", "")
                classe = zx[zx.index('_'):zx.index('-')].replace('_', "")
                fees = milli(zx[zx.index('-'):zx.index(' : ')].replace('-', ""))
                paid = milli(zx[zx.index(' : '):zx.index(' ugx. ')].replace(' : ', ""))
                bal = zx[zx.index(' ugx. '):].replace(' ugx. ', "")  # .replace("-","")
                self.GSC.add_widget(TextInput(text=fi[:fi.index("_")], readonly=True, allow_copy=True))
                self.GSC.add_widget(TextInput(text=names, size_hint=(None, None), size=(300,30),readonly=True, allow_copy=True))
                self.GSC.add_widget(TextInput(text=classe, readonly=True, allow_copy=True))
                self.GSC.add_widget(TextInput(text=fees, readonly=True, allow_copy=True))
                self.GSC.add_widget(TextInput(text=paid, readonly=True, allow_copy=True))
                if bal.startswith("-"):
                    self.GSC.add_widget(TextInput(text="- " + milli(bal.replace("-", "")), readonly=True, allow_copy=True))
                else:
                    self.GSC.add_widget( TextInput(text="+ " + milli(bal.replace("-", "")), readonly=True, allow_copy=True))
                # self.GSC.add_widget(TextInput(text=fi[:fi.index("_")], readonly=True, allow_copy=True))
                # self.GSC.add_widget(TextInput(text=zx[:zx.index('_')].replace("_", ""), readonly=True, allow_copy=True))
                # self.GSC.add_widget(TextInput(text=zx[zx.index('_'):zx.index('-') ].replace('_', ""), readonly=True, allow_copy=True))
                # self.GSC.add_widget( TextInput(text=milli(zx[zx.index('-'):zx.index(' : ')].replace('-', "")), readonly=True, allow_copy=True))
                # self.GSC.add_widget( TextInput(text=milli(zx[zx.index(' : '):zx.index(' ugx. ')].replace(' : ', "")), readonly=True, allow_copy=True))
                # self.GSC.add_widget( TextInput(text=milli(zx[zx.index(' ugx. '):].replace(' ugx. ', "").replace("-","")), readonly=True, allow_copy=True))
                sz += 1
        self.GSC.add_widget(TextInput(text="", readonly=True, allow_copy=True))
        self.GSC.add_widget(TextInput(text="", size_hint=(None, None), size=(300, 30), readonly=True, allow_copy=True))
        for i in range(5):
            self.GSC.add_widget(TextInput(text="", readonly=True, allow_copy=True))
        self.GSC.add_widget(TextInput(hint_text="TOT= " + milli(today) + " ugx" + "      DEPOSIT : " + milli(str(bank)) + " ugx",
                      size_hint=(None, None), size=(300, 30), multiline=False, foreground_color=(1, 1, 1, 1),
                      background_color=(0, 0, 0, 1), readonly=True, allow_copy=True))
        for i in range(4):
            self.GSC.add_widget(TextInput(text="", readonly=True, allow_copy=True))

        # self.GSC.add_widget(self.dis)
        self.SC.add_widget(self.GSC)
        self.GSC.size_hint = (None, None)
        self.GSC.size = (880, 30 * sz + 100)

        self.gaside.add_widget(self.gborrow)
        self.gaside.add_widget(self.sp_sele)
        self.gaside.add_widget(self.SC)
        self.gaside.add_widget(Button(text="TOTAL :  " + milli(str(today)) + " ugx"+"          DEPOSIT : " + milli(str(bank)) + " ugx", size_hint=(1., .1), on_release=self.ssave))
        self.add_widget(self.gaside)
        # Clock.schedule_once(self.ssave,5)

    def Yempt(self, sp, tx=None):
        if tx =="RESET" :
            return
        if self.SP_GN.text == "SPENT":
            self.GSC.cols = 2
            Clock.schedule_once(self.SPYempt)
        else:
            self.GSC.cols = 2

        FF = open(DIR + 'media' + PTH + '0' + PTH + 'FINANCE.json', 'r')
        DF = json.load(FF)
        FF.close()
        self.DAY.text = ""
        self.MONTH.text = ""
        self.MONTH.values = tuple(DF[self.YEAR.text].keys())

        # *******************************************************************

        try:
            self.GSC.clear_widgets()
        except:
            pass

        try:
            self.SC.clear_widgets()
        except:
            pass
        try:
            self.remove_widget(self.SC)
        except:
            pass
        try:
            self.gaside.clear_widgets()
        except:
            pass
        try:
            self.remove_widget(self.gaside)
        except:
            pass

        FF = open(DIR + 'media' + PTH + '0' + PTH + 'FINANCE.json', 'r')
        DF = json.load(FF)
        FF.close()
        today = 0
        bank=0
        sz = 0
        # today = DF[self.YEAR.text][self.MONTH.text][self.DAY.text]['TGN']['T']
        # del DF[self.YEAR.text][self.MONTH.text][self.DAY.text]['TGN']['T']

        # list1 = ["Date", "Name", "Class", "Fees", "Paid", "Balance"]
        list1=["MONTH","TOTAL"]
        for x in list1:
            self.GSC.add_widget(TextInput(text=x,  size_hint=(None, None), size=(250,30),readonly=True, allow_copy=True, background_color=(0, 0, 0, 1), foreground_color=(1, 1, 1, 1)))

        for ye in DF[self.YEAR.text].keys():
            for day in DF[self.YEAR.text][ye].keys():  # [self.DAY.text]['TGN']
                bank += float(DF[self.YEAR.text][ye][day]['TGN']['BANK'])
                today += float(DF[self.YEAR.text][ye][day]['TGN']['T'])
                # del DF[self.YEAR.text][ye][day]['TGN']['T']
                # for fi in DF[self.YEAR.text][ye][day]['TGN'].keys():
                #     zx = DF[self.YEAR.text][ye][day]['TGN'][fi]
                #     self.GSC.add_widget(TextInput(text=fi[:fi.index("_")], readonly=True, allow_copy=True))
                #     self.GSC.add_widget( TextInput(text=zx[:zx.index('_')].replace("_", ""), readonly=True, allow_copy=True))
                #     self.GSC.add_widget(TextInput(text=zx[zx.index('_'):zx.index('-') ].replace('_', ""), readonly=True, allow_copy=True))
                #     self.GSC.add_widget(TextInput(text=milli(zx[zx.index('-'):zx.index(' : ') ].replace('-', "")), readonly=True, allow_copy=True))
                #     self.GSC.add_widget(TextInput(text=milli(zx[zx.index(' : '):zx.index(' ugx. ') ].replace(' : ', "")), readonly=True, allow_copy=True))
                #     self.GSC.add_widget( TextInput(text=milli(zx[zx.index(' ugx. '):].replace(' ugx. ', "").replace("-","")), readonly=True, allow_copy=True))
                #     sz += 1
            self.GSC.add_widget(TextInput(text=ye,size_hint=(None, None), size=(250,30), readonly=True, allow_copy=True))
            self.GSC.add_widget(TextInput(text=milli(str(today))+" ugx", size_hint=(None, None), size=(250,30),readonly=True, allow_copy=True))
            sz += 1
        for i in range(3):
            self.GSC.add_widget(TextInput(text="", size_hint=(None, None), size=(250,30),readonly=True, allow_copy=True))
        self.GSC.add_widget(TextInput(text="TOTAL : " + milli(str(today)) + " ugx"+"   DEPOSIT : " + milli(str(bank)) + " ugx",size_hint=(None, None), size=(250,30), readonly=True, allow_copy=True))
        sz += 3

        # self.GSC.add_widget(self.dis)
        self.SC.add_widget(self.GSC)
        self.GSC.size_hint = (None, None)
        self.GSC.size = (880, 30 * sz + 100)

        self.gaside.add_widget(self.gborrow)
        self.gaside.add_widget(self.sp_sele)
        self.gaside.add_widget(self.SC)
        self.gaside.add_widget( Button(text="TOTAL :  " + milli(str(today)) + " ugx"+"          DEPOSIT : " + milli(str(bank)) + " ugx", size_hint=(1., .1),
                   on_release=self.ssave))  # +" / "+"TOTAL : " + DF["TT"] + "ugx"
        self.add_widget(self.gaside)
        # Clock.schedule_once(self.ssave, 5)

    def ssave(self, x):

        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

        pickl = open(DIR + 'media' + PTH + '0' + PTH + 'SCHOOL.bin', 'rb')
        ids = pickle.load(pickl)
        pickl.close()
        # '+ids['1']+'

        self.SC.remove_widget(self.GSC)
        self.exG = GridLayout(cols=1, size_hint=(None, None), size=(self.GSC.width+400, self.GSC.height + 260),
                              pos_hint=self.GSC.pos_hint)
        les_point = GridLayout(cols=3, size_hint=(None, None), size=(900, 170))
        im = AsyncImage(source=ASY + 'L.png', size_hint=(None, None), size=(150, 150), allow_stretch=True)
        les_point.add_widget(im)
        grid_in = GridLayout(cols=1, size_hint=(None, None), size=(360, 170), row_default_height=25,
                             row_force_default=True)
        grid_in.add_widget( Label(text='  '+ids['1']+'               ', color=(0, 0, 1, 1), font_size=18))
        grid_in.add_widget( Label(text='       '+ids['2']+'               ', font_size=13, color=(0, 0, 0, 1)))
        grid_in.add_widget( Label(text='   '+ids['3']+'               ', font_size=13, color=(0, 1, 0, 1)))
        grid_in.add_widget( Label(text='       '+ids['4']+'               ', font_size=13, color=(0, 0, 0, 1)))
        grid_in.add_widget( Label(text='     '+ids['5']+'               ', font_size=15, color=(1, 0, 0, 1)))
        # grid_in.add_widget(Label(text=' ' * 15 +self.v_class.text+' ' * 100 + ' ' * 20, underline=True, color=(1, 0, 0, 1)))
        les_point.add_widget(grid_in)
        ph = Label(text="GAINED ON \n"+self.DAY.text+" "+self.MONTH.text+" "+self.YEAR.text, font_size=35, underline=True, italic=True, color=(0, 0, 0, .3))
        les_point.add_widget(ph)
        self.exG.add_widget(les_point)
        # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        self.exG.add_widget(self.GSC)
        Clock.schedule_once(self.print_GSC,3)
    def print_GSC(self,g):
        self.exG.export_to_png( NDR + 'Desktop' + PTH + 'P R I N T A B L E' + PTH + '' + 'GAINED ' + self.DAY.text + " " + self.MONTH.text + " " + self.YEAR.text + '.png')

        self.print_all_i( NDR + 'Desktop' + PTH + 'P R I N T A B L E' + PTH + '' + 'GAINED ' + self.DAY.text + " " + self.MONTH.text + " " + self.YEAR.text + '.png')

        # # os.stat('GAINED ' + self.DAY.text + " " + self.MONTH.text + " " + self.YEAR.text + '.png','print')
        # try:
        #     os.startfile('GAINED ' + self.DAY.text + " " + self.MONTH.text + " " + self.YEAR.text + '.png', 'print')
        # except:
        #     pass
        # import cv2
        # im = cv2.imread('GAINED ' + self.DAY.text + " " + self.MONTH.text + " " + self.YEAR.text + '.png')
        # rt = cv2.rotate(im, cv2.ROTATE_180)
        # cv2.imwrite('GAINED ' + self.DAY.text + " " + self.MONTH.text + " " + self.YEAR.text + ".png", rt)
        # cv2.waitKey(0)
        self.exG.remove_widget(self.GSC)
        self.SC.add_widget(self.GSC)

    def Finan(self, w):

        if not lv in ('fin', 'adm'):
            return
        try:
            self.remove_widget(self.idd)
        except:
            pass
        try:
            good = open(DIR + 'media' + PTH + '0' + PTH + "FINANCE.json", 'r')
            test = json.load(good)
            kys = test.keys()
            good.close()
        except:
            # pass
            Clock.schedule_once(self.restore)
            return
        self.add_widget(self.idd)
        self.b_c = 0
        Clock.schedule_interval(self.back, .02)
        self.fingrid = GridLayout(cols=4)

        FF = open(DIR + 'media' + PTH + '0' + PTH + 'FINANCE.json', 'r')
        DF = json.load(FF)
        FF.close()

        if not DF[time.strftime('%Y')][time.strftime('%B')].get(time.strftime('%d')):
            DF[time.strftime('%Y')][time.strftime('%B')][time.strftime('%d')] = {}
            DF[time.strftime('%Y')][time.strftime('%B')][time.strftime('%d')]['TGN'] = {}
            DF[time.strftime('%Y')][time.strftime('%B')][time.strftime('%d')]['TSP'] = {}
            DF[time.strftime('%Y')][time.strftime('%B')][time.strftime('%d')]['TGN']['T'] = '0'
            DF[time.strftime('%Y')][time.strftime('%B')][time.strftime('%d')]['TGN']['BANK'] = '0'
            DF[time.strftime('%Y')][time.strftime('%B')][time.strftime('%d')]['TSP']['T'] = '0'

        self.schtx = TextInput(hint_text='Enter pupil name', multiline=True, background_color=(0, 1, 1, .8),
                               size_hint=(.3, .05), pos_hint={'center_x': .17, 'center_y': .94}, allow_copy=True, foreground_color=(0, 0, 0, .6))
        self.schtx.bind(on_touch_up=self.sontouchup)
        self.schtx.bind(text=self.on_s_stud)
        self.add_widget(self.schtx)
        self.scv = ScrollView(size_hint=(.3, .8), pos_hint={'center_x': .14, 'center_y': .5}, do_scroll_x=False,
                              do_scroll_y=True, scroll_timeout=55, scroll_distance=20, scroll_type=['bars', 'content'],
                              bar_width=10, bar_color=(1, 1, 0, 1), bar_margin=0)

        self.gsch = GridLayout(cols=1, spacing=12, size_hint_x=1., size_hint_y=10,
                               pos_hint={'center_x': .44, 'center_y': .5}, row_default_height=180,
                               row_force_default=True)  # for scrolling
        self.exitp = Button(text="x", background_color=(1, 0, .5, .6), size_hint=(.1, .095),
                            pos_hint={'center_x': .046, 'center_y': .05}, font_size=30)
        self.exitp.bind(on_release=self.pexit)
        self.add_widget(self.exitp)
        #################################      ON  RIGHT       ###########################
        self.bckg = Button(size_hint=(.59, 1.), background_color=(.6, 0, .4, .7),
                           pos_hint={'center_x': .62, 'center_y': .5})
        self.dbckg = Button(size_hint=(.55, .95),
                            pos_hint={'center_x': .62, 'center_y': .288})
        self.add_widget(self.bckg)
        # self.add_widget(self.dbckg)
        self.gaside = GridLayout(cols=1, spacing=8, size_hint=(.55, 1.), pos_hint={'center_x': .62, 'center_y': .5})
        #

        self.SC = ScrollView(size_hint=(1., .3), do_scroll_x=True,
                             do_scroll_y=True, scroll_timeout=55, scroll_distance=20, scroll_type=['bars', 'content'],
                             bar_width=10, bar_color=(1, 1, 0, 1), bar_margin=0)
        self.autobind('self.SC')
        self.GSC = GridLayout(cols=6, spacing=1, size_hint_x=1., size_hint_y=20,
                              pos_hint={'center_x': .5, 'center_y': .5}, row_default_height=30,
                              row_force_default=True)  # for scrolling

        # ========================================================================================================================================
        # print(nls)

        self.gborrow = GridLayout(cols=2, spacing=10, size_hint=(1., .485), row_default_height=40,
                                  row_force_default=True)
        self.gborrow.add_widget(Label(text="SPENDITURE ", font_size=25, color=(1, .5, 1, 1), underline=True))
        self.gborrow.add_widget(Label(text=""))

        zzz = open(DIR + 'media' + PTH + '0' + PTH + 'DEPANS', 'rb')
        depanslist = pickle.load(zzz)
        zzz.close()
        self.gborrow.add_widget(Label(text="Reason : "))
        self.spreason = Spinner(text="", values=tuple(
            depanslist))  # 'FOOD','ELECTRICITY','TRANSPORT','EXAMS PP ','FIRE WOOD','TOILET PP'
        self.gborrow.add_widget(self.spreason)
        self.Rson = Label(text="Other Reason : ")
        self.gborrow.add_widget(self.Rson)
        self.txrson = TextInput(allow_copy=True, foreground_color=(1, 0, 0, 1))
        self.gborrow.add_widget(self.txrson)
        self.Nam = Label(text="Your Name : ")
        self.gborrow.add_widget(self.Nam)
        self.txNam = TextInput(allow_copy=True, foreground_color=(1, 0, 0, 1))
        self.gborrow.add_widget(self.txNam)
        self.ngapi = Label(text="Amount : ")
        self.gborrow.add_widget(self.ngapi)
        self.txngapi = TextInput(allow_copy=True, foreground_color=(1, 0, 0, 1))
        self.gborrow.add_widget(self.txngapi)
        # self.gborrow.add_widget(Label(text=""))
        # self.gborrow.add_widget(Label(text=""))
        self.SV = Button(text="S U B M I T")
        self.SV.bind(on_release=self.borrowed)

        self.gborrow.add_widget(self.SV)

        self.sp_sele = GridLayout(cols=4, size_hint=(1., .097), row_default_height=30, row_force_default=True)
        self.sp_sele.add_widget(Label(text="IN & OUT", color=(1, 1, 1, .5)))
        self.sp_sele.add_widget(Label(text="MONTH", color=(1, 1, 1, .5)))
        self.sp_sele.add_widget(Label(text="DAY", color=(1, 1, 1, .5)))
        self.sp_sele.add_widget(Label(text="YEAR", color=(1, 1, 1, .5)))


        self.SP_GN = Spinner(text='GAINED', values=('GAINED', 'SPENT','BANK','F.T'))
        self.SP_GN.bind(text=self.choisir)
        self.sp_sele.add_widget(self.SP_GN)
        del DF['TT']
        ll = list(DF.keys())
        # ll.append("RESET")
        self.YEAR = Spinner(text=time.strftime('%Y'), values=tuple(ll))
        # self.YEAR.bind(text=self.OK)
        self.YEAR.bind(text=self.Yempt)
        self.MONTH = Spinner(text=time.strftime('%B'), values=tuple(DF[self.YEAR.text].keys()))
        # self.MONTH.bind(text=self.OK)
        self.MONTH.bind(text=self.Mempt)
        self.sp_sele.add_widget(self.MONTH)

        self.DAY = Spinner(text=time.strftime('%d'), values=tuple(DF[self.YEAR.text][self.MONTH.text].keys()))
        self.DAY.bind(text=self.OK)
        self.sp_sele.add_widget(self.DAY)
        self.sp_sele.add_widget(self.YEAR)
        Clock.schedule_once(self.choisir)

        # self.add_widget(self.gaside)

    def choisir(self, sp, text=None):
        if self.SP_GN.text == "SPENT":
            self.GSC.cols = 2
            self.DAY.bind(text=self.oC)
            self.YEAR.bind(text=self.SPYempt)
            self.MONTH.bind(text=self.SPMempt)
            if self.MONTH.text == "" and self.DAY.text == "":
                Clock.schedule_once(self.SPYempt)
            elif self.DAY.text == "":
                Clock.schedule_once(self.SPMempt)
            else:
                Clock.schedule_once(self.oC)
        else:
            self.GSC.cols = 3

        if self.SP_GN.text == "GAINED":
            self.GSC.cols = 6
            self.DAY.bind(text=self.OK)
            self.YEAR.bind(text=self.Yempt)
            self.MONTH.bind(text=self.Mempt)
            if self.MONTH.text == "" and self.DAY.text == "":
                Clock.schedule_once(self.Yempt)
            elif self.DAY.text == "":
                Clock.schedule_once(self.Mempt)
            else:
                Clock.schedule_once(self.OK)

        if self.SP_GN.text == "BANK":
            Clock.schedule_once(self.BANK)

        if self.SP_GN.text == "F.T":
            self.MONTH.bind(text=self.FIN_TRACK)
            Clock.schedule_once(self.FIN_TRACK)

        else:
            self.GSC.cols = 2

    def FIN_TRACK(self, sp, tx=None):
        if tx =="RESET" :
            return
        if self.SP_GN.text == "GAINED":
            self.GSC.cols = 3
            Clock.schedule_once(self.Yempt)
        else:
            self.GSC.cols = 2

        FF = open(DIR + 'media' + PTH + '0' + PTH + 'FINANCE.json', 'r')
        DF = json.load(FF)
        FF.close()
        self.DAY.text = ""
        # self.MONTH.text = ""
        self.MONTH.values = tuple(DF[self.YEAR.text].keys())

        # *******************************************************************

        try:
            self.GSC.clear_widgets()
        except:
            pass

        try:
            self.SC.clear_widgets()
        except:
            pass
        try:
            self.remove_widget(self.SC)
        except:
            pass
        try:
            self.gaside.clear_widgets()
        except:
            pass
        try:
            self.remove_widget(self.gaside)
        except:
            pass

        zzz = open(DIR + 'media' + PTH + '0' + PTH + 'DEPANS', 'rb')
        x = pickle.load(zzz)
        zzz.close()

        FF = open(DIR + 'media' + PTH + '0' + PTH + 'FINANCE.json', 'r')
        DF = json.load(FF)
        FF.close()
        today = 0
        bank=0
        FEES=0
        xl = {}
        sz = 0
        # today = DF[self.YEAR.text][self.MONTH.text][self.DAY.text]['TGN']['T']
        # del DF[self.YEAR.text][self.MONTH.text][self.DAY.text]['TGN']['T']
        # for ye in DF[self.YEAR.text].keys():
        for day in DF[self.YEAR.text][self.MONTH.text].keys():  # [self.DAY.text]['TGN']
            today += float(DF[self.YEAR.text][self.MONTH.text][day]['TSP']['T'])
            FEES += float(DF[self.YEAR.text][self.MONTH.text][day]['TGN']['T'])
            bank += float(DF[self.YEAR.text][self.MONTH.text][day]['TGN']['BANK'])
            del DF[self.YEAR.text][self.MONTH.text][day]['TSP']['T']
            for fi in DF[self.YEAR.text][self.MONTH.text][day]['TSP'].keys():
                zx = DF[self.YEAR.text][self.MONTH.text][day]['TSP'][fi]

                if xl.get(fi, 0):
                    hd = xl[fi]
                    xl[fi] = str(float(zx) + float(hd))
                if not xl.get(fi, 0):
                    xl[fi] = zx

                # self.GSC.add_widget(TextInput(text=fi, readonly=True, allow_copy=True))
                # self.GSC.add_widget(TextInput(text=milli(zx), readonly=True, allow_copy=True))
                # sz += 1

        # self.GSC.add_widget(TextInput(text="", readonly=True, allow_copy=True))
        # self.GSC.add_widget(TextInput(text="", readonly=True, allow_copy=True))
        # self.GSC.add_widget(TextInput(text="TOTAL", background_color=(0, 0, 0, 1), foreground_color=(1, 1, 1, 1), readonly=True, allow_copy=True))
        # self.GSC.add_widget(TextInput(text= milli(str(today)) + " ugx", background_color=(0, 0, 0, 1), foreground_color=(1, 1, 1, 1),
        #               readonly=True, allow_copy=True))
        # self.GSC.add_widget(TextInput(text="", readonly=True, allow_copy=True))
        # self.GSC.add_widget(TextInput(text="", readonly=True, allow_copy=True))
        # sz += 3

        self.GSC.add_widget(TextInput(text="FEES", readonly=True, allow_copy=True))
        self.GSC.add_widget(TextInput(text=milli(FEES), readonly=True, allow_copy=True))
        self.GSC.add_widget(TextInput(text="DEPOSIT", readonly=True, allow_copy=True))
        self.GSC.add_widget(TextInput(text=milli(bank), readonly=True, allow_copy=True))
        sz += 1
        for y in xl.keys():
            self.GSC.add_widget(TextInput(text=y, readonly=True, allow_copy=True))
            self.GSC.add_widget(TextInput(text=milli(xl[y]), readonly=True, allow_copy=True))
            sz += 1
        self.GSC.add_widget(TextInput(text="", readonly=True, allow_copy=True))
        self.GSC.add_widget(TextInput(text="", readonly=True, allow_copy=True))
        self.GSC.add_widget(TextInput(text="BALANCE", background_color=(0, 0, 0, 1), foreground_color=(1, 1, 1, 1), readonly=True, allow_copy=True))
        self.GSC.add_widget(TextInput(text= milli(DF["TT"]) + " ugx", background_color=(0, 0, 0, 1), foreground_color=(1, 1, 1, 1),
                      readonly=True, allow_copy=True))

        # self.GSC.add_widget(self.dis)
        self.SC.add_widget(self.GSC)
        print(xl)
        self.GSC.size_hint = (None, None)
        self.GSC.size = (840, 30 * sz + 100)

        self.gaside.add_widget(self.gborrow)
        self.gaside.add_widget(self.sp_sele)
        self.gaside.add_widget(self.SC)
        self.gaside.add_widget(
            Button(text="BALANCE : " + milli(str(bank)) + " ugx", size_hint=(1., .1), on_release=self.SPsave))
        self.add_widget(self.gaside)
        # Clock.schedule_once(self.SPsave, 5)

    def BANK(self, sp, tx=None):
        if tx =="RESET" :
            return
        if self.SP_GN.text == "SPENT":
            self.GSC.cols = 2
            Clock.schedule_once(self.SPYempt)
        else:
            self.GSC.cols = 4

        FF = open(DIR + 'media' + PTH + '0' + PTH + 'FINANCE.json', 'r')
        DF = json.load(FF)
        FF.close()
        self.DAY.text = ""
        # self.MONTH.text = ""
        self.MONTH.values = tuple(DF[self.YEAR.text].keys())

        # *******************************************************************

        try:
            self.GSC.clear_widgets()
        except:
            pass

        try:
            self.SC.clear_widgets()
        except:
            pass
        try:
            self.remove_widget(self.SC)
        except:
            pass
        try:
            self.gaside.clear_widgets()
        except:
            pass
        try:
            self.remove_widget(self.gaside)
        except:
            pass

        FF = open(DIR + 'media' + PTH + '0' + PTH + 'FINANCE.json', 'r')
        DF = json.load(FF)
        FF.close()
        self.b_TT=DF["TT"]
        td = 0
        sp=0
        bk=0
        sz = 0
        # today = DF[self.YEAR.text][self.MONTH.text][self.DAY.text]['TGN']['T']
        # del DF[self.YEAR.text][self.MONTH.text][self.DAY.text]['TGN']['T']

        # list1 = ["Date", "Name", "Class", "Fees", "Paid", "Balance"]
        list1=["DAY","GAINED","SPENT","DEPOSIT"]
        for x in list1:
            self.GSC.add_widget(TextInput(text=x,readonly=True, allow_copy=True, background_color=(0, 0, 0, 1), foreground_color=(1, 1, 1, 1)))


        for day in DF[self.YEAR.text][self.MONTH.text].keys():  # [self.DAY.text]['TGN']
            bank = float(DF[self.YEAR.text][self.MONTH.text][day]['TGN']['BANK'])
            today = float(DF[self.YEAR.text][self.MONTH.text][day]['TGN']['T'])
            spent= float(DF[self.YEAR.text][self.MONTH.text][day]['TSP']['T'])
            td+=today
            sp+=spent
            bk+=bank
            self.GSC.add_widget(TextInput(text=day +" "+self.MONTH.text, size=(100,30), readonly=True, allow_copy=True))
            self.GSC.add_widget(TextInput(text=milli(str(today))+" ugx",  size=(250,30),readonly=True, allow_copy=True))
            self.GSC.add_widget(TextInput(text=milli(str(spent)) + " ugx", size=(250, 30), readonly=True,allow_copy=True))

            self.bank_=TextInput(hint_text=milli(str(bank)) + " ugx",  size=(250, 30),allow_copy=True,multiline=False)

            if self.YEAR.text+self.MONTH.text+day==time.strftime("%Y%B%d"):
                self.GSC.add_widget(self.bank_)
                self.bank_.bind(text=self.sv_bank)
                self.bank_.bind(on_text_validate=self.save_bank)
                Window.bind(on_keyboard=self.blank)
            else:
                self.GSC.add_widget(TextInput(text=milli(str(bank)) + " ugx", size=(250, 30), readonly=True, allow_copy=True))
            sz += 1
        for x in range(4):
            self.GSC.add_widget(TextInput(text="", readonly=True, allow_copy=True))

        T_MONTH=["TOTAL",milli(td),milli(sp),milli(bk)]
        for i in T_MONTH:
            self.GSC.add_widget(TextInput(text=i,readonly=True, allow_copy=True,background_color=(0, 0, 0, 1), foreground_color=(1, 1, 1, 1)))



        tay=0
        bn=0
        spen=0
        for ye in DF[self.YEAR.text].keys():
            for day in DF[self.YEAR.text][ye].keys():  # [self.DAY.text]['TGN']
                print(DF[self.YEAR.text][ye][day]['TGN'])
                bn += float(DF[self.YEAR.text][ye][day]['TGN']['BANK'])
                tay += float(DF[self.YEAR.text][ye][day]['TGN']['T'])
                spen += float(DF[self.YEAR.text][ye][day]['TSP']['T'])
        # for x in range(4):
        #     self.GSC.add_widget(TextInput(text="", readonly=True, allow_copy=True))
        self.GSC.add_widget( TextInput(hint_text="THIS YEAR : ",  readonly=True, allow_copy=True))
        self.GSC.add_widget(TextInput(hint_text=milli(str(tay)) + " ugx",   readonly=True, allow_copy=True))
        self.GSC.add_widget(TextInput(hint_text=milli(str(spen)) + " ugx",  readonly=True,allow_copy=True))
        self.GSC.add_widget( TextInput(hint_text=milli(str(bn)) + " ugx",   readonly=True, allow_copy=True))


        sz += 5

        # self.GSC.add_widget(self.dis)
        self.SC.add_widget(self.GSC)
        self.GSC.size_hint = (None, None)
        self.GSC.size = (880, 30 * sz + 100)

        self.gaside.add_widget(self.gborrow)
        self.gaside.add_widget(self.sp_sele)
        self.gaside.add_widget(self.SC)
        self.TB= Button(text="TOTAL :  " + milli(str(today)) + " ugx"+"          BANK : " + milli(str(bank)) + " ugx", size_hint=(1., .1),
                   on_release=self.ssave)
        self.gaside.add_widget(self.TB )  # +" / "+"TOTAL : " + DF["TT"] + "ugx"
        self.add_widget(self.gaside)

    def sv_bank(self,sp,tx):
        # Window.borderless="1"
        try:
            int(tx)
            FF = open(DIR + 'media' + PTH + '0' + PTH + 'FINANCE.json', 'r')
            DF = json.load(FF)
            FF.close()
            print(tx)
            DF[time.strftime('%Y')][time.strftime('%B')][time.strftime('%d')]['TGN']['BANK']=tx
            TT=float(DF["TT"])+float(tx)
            DF["TT"] = float(self.b_TT)+float(tx)
            print(DF["TT"])

            ff = open(DIR + 'media' + PTH + '0' + PTH + 'FINANCE.json', 'w')
            json.dump(DF,ff)
            ff.close()
            bcp = self.TB.text[:self.TB.text.index("B")]
            self.TB.text = bcp + "BANK : " + milli(self.bank_.text) + " ugx"
            ls = [FF, DF,TT, ff, bcp]
            for x in ls:
                del x
            del ls

        except:
            self.bank_.text = ""
            return

    def save_bank(self,tx):
        try:
            int(tx)
            FF = open(DIR + 'media' + PTH + '0' + PTH + 'FINANCE.json', 'r')
            DF = json.load(FF)
            FF.close()
            print(tx)
            DF[time.strftime('%Y')][time.strftime('%B')][time.strftime('%d')]['TGN']['BANK']=tx
            TT=float(DF["TT"])+float(tx)
            DF["TT"] = float(self.b_TT)+float(tx)
            print(DF["TT"])

            ff = open(DIR + 'media' + PTH + '0' + PTH + 'FINANCE.json', 'w')
            json.dump(DF,ff)
            ff.close()
            bcp = self.TB.text[:self.TB.text.index("B")]
            self.TB.text = bcp + "BANK : " + milli(self.bank_.text) + " ugx"
            ls = [FF, DF, ff, bcp]
            for x in ls:
                del x
            del ls
            print('done')

        except:
            self.bank_.text = ""
            return

    def blank(self,window, key, *largs):
        print("key ",key)
        if key == 120 or key == ord("x") or key == ord("X"):
            FF = open(DIR + 'media' + PTH + '0' + PTH + 'FINANCE.json', 'r')
            DF = json.load(FF)
            FF.close()

            TT = float(DF["TT"]) - float(DF[time.strftime('%Y')][time.strftime('%B')][time.strftime('%d')]['TGN']['BANK'])

            DF["TT"] = TT
            print("TT-self.bank_.text= ",float(DF["TT"]) - float(DF[time.strftime('%Y')][time.strftime('%B')][time.strftime('%d')]['TGN']['BANK']))
            DF[time.strftime('%Y')][time.strftime('%B')][time.strftime('%d')]['TGN']['BANK']="0"
            ff = open(DIR + 'media' + PTH + '0' + PTH + 'FINANCE.json', 'w')
            json.dump(DF, ff)
            ff.close()
            self.bank_.text = ""
            bcp = self.TB.text[:self.TB.text.index("B")]
            self.TB.text = bcp + "BANK : " + milli(str(float(DF[time.strftime('%Y')][time.strftime('%B')][time.strftime('%d')]['TGN']['BANK']))) + " ugx"
            Window.unbind(on_keyboard=self.blank)
            ls=[FF,TT,DF,ff,bcp]
            for x in ls:
                del x
            del ls
            print('done')


    def on_s_stud(self, s, tex):
        if self.schtx.text=="" :
            self.autobind('self.SC')
        else:
            self.autobind('self.scv')
        #
        if tex == "":
            print("returned")
            return
        else:
            try:
                self.remove_widget(self.scv)
            except:
                pass
            ls = []

            for k in Clss():
                fN = open(DIR + 'media' + PTH + '0' + PTH + ANGELS + PTH + '' + k + ".json", 'r')
                fina = json.load(fN)
                fN.close()
                for kk in fina.keys():
                    if tex.lower() in kk.lower():
                        ls.append(kk.strip() + "  " + k)

            # print(ls)
            try:
                self.remove_widget(self.gsch)
            except:
                pass
            try:
                self.scv.clear_widgets()
            except:
                pass
            try:
                self.gsch.clear_widgets()
            except:
                pass

            for pup in ls:
                self.flag = GridLayout(cols=1, size_hint_x=self.gsch.width, size_hint_y=.3)
                self.bpup = Button(text=pup, size_hint_y=.1, size_hint_x=.1, on_release=self.found)
                self.prph = AsyncImage(source=ASY + pup[:-5].strip() + ".png")
                print(pup[:-5].strip() + ".png", len(pup[:-5] + ".png"))
                self.flag.add_widget(self.prph)
                self.flag.add_widget(self.bpup)

                self.gsch.add_widget(self.flag)
            self.scv.add_widget(self.gsch)
            self.add_widget(self.scv)
            self.scv.scroll_y = 1

    def found(self, event):

        self.remove_widget(self.gaside)

        try:
            self.remove_widget(self.bckg)
            self.remove_widget(self.dbckg)
        except:
            pass
        try:
            self.remove_widget(self.Gpay)
        except:
            pass
        self.nom = event.text[:-5]
        self.niveau = event.text[-3:]
        # print(len(self.nom),self.nom)
        file = open(DIR + 'media' + PTH + '0' + PTH + ANGELS + PTH + '' + self.niveau + '.json', 'r')
        dict = json.load(file)
        file.close()
        self.idd.background_color = (0, 0, 0, .98)
        lst = []
        self.Gpay = GridLayout(cols=1, spacing=40, size_hint=(.7, 1.), pos_hint={'center_x': .6, 'center_y': .5})
        self.lhistory = Label(text="P A Y M E N T   H I S T O R Y", markup=True, halign='left',
                              shorten=True, ellipsis_options={'color': (1, 0.5, 0.5, 1), 'underline': True},
                              color=(1, .5, 0, 1), size_hint=(1., .2))
        self.Gpay.add_widget(self.lhistory)
        self.scp = ScrollView(size_hint=(1., 1.), pos_hint={'center_x': .5, 'center_y': .9}, do_scroll_x=False,
                              do_scroll_y=True, scroll_timeout=55, scroll_distance=20, scroll_type=['bars', 'content'],
                              bar_width=10, bar_color=(1, 1, 0, 1), bar_margin=0)
        self.autobind('self.scp')
        self.gscrhis = GridLayout(cols=1, spacing=15, size_hint_x=1., size_hint_y=40,
                                  pos_hint={'center_x': .5, 'center_y': .5}, row_default_height=20,
                                  row_force_default=True)  # for scrolling

        # for valu in reversed(dict[self.niveau][self.nom]['$']["history"].values()):
        for valu in reversed(dict[self.nom]['$']["history"].values()):
            self.gscrhis.add_widget( Label(text=valu[valu.index(':') + 1:], font_size=12, color=(.3, 1, 0, 1), size_hint_x=.8))

        self.scp.add_widget(self.gscrhis)
        self.Gpay.add_widget(self.scp)

        self.gnewp = GridLayout(cols=2, size_hint=(1., .5), pos_hint={'center_x': .6, 'center_y': .3})
        self.newpayment = Label(text="                                 N E W  P A Y M E N T", color=(1, .5, 0, 1))
        self.gnewp.add_widget(self.newpayment)
        self.gnewp.add_widget(Label(text=""))  ######
        self.gnewp.add_widget(Label(text="A M O U N T"))  ######
        self.gnewp.add_widget(Label(text="R E A S O N"))  ######
        self.paid = Label(text="Amount : ")
        self.txpaid = TextInput(text="", multiline=False, foreground_color=(0, 0, 0, .6))
        # self.gnewp.add_widget(self.paid)
        self.gnewp.add_widget(self.txpaid)
        self.Gpay.add_widget(self.gnewp)
        self.reason = TextInput(text="", foreground_color=(0, 0, 0, .6))
        self.gnewp.add_widget(self.reason)
        self.gnewp.add_widget(Label(text=""))  ######
        self.gnewp.add_widget(Label(text=""))  ######
        self.confpay = Button(text="Confirm", on_release=self.confirmed)
        self.gnewp.add_widget(self.confpay)

        self.add_widget(self.Gpay)
        # if self.txpaid.text != "" :
        #     self.exitp.unbind(on_release=self.pexit)

    def pexit(self, infra):
        try:
            self.remove_widget(self.gaside)
        except:
            pass
        try:
            self.remove_widget(self.bckg)
            self.remove_widget(self.dbckg)
        except:
            pass
        try:
            if self.txpaid.text != "":
                return
        except:
            pass

        try:
            self.remove_widget(self.Gpay)
        except:
            pass
        self.remove_widget(self.schtx)
        self.remove_widget(self.exitp)
        self.remove_widget(self.scv)
        self.remove_widget(self.idd)

    def confirmed(self, ray):
        if self.txpaid.text == "":
            return
        if self.reason.text == "":
            return
        try:
            int(self.txpaid.text)
        except:
            return
        file = open(DIR + 'media' + PTH + '0' + PTH + ANGELS + PTH + '' + self.niveau + '.json', 'r')
        dict = json.load(file)
        file.close()

        fees=dict[self.nom]['fee']

        # dict[self.niveau][self.nom]['$']["balance"]
        f = dict[self.nom]['$']["balance"]
        fl = float(f) + float(self.txpaid.text)
        # print(fl)
        dict[self.nom]['$']["balance"] = str(fl)
        string = "Fee from " + self.nom + " : " + self.txpaid.text + " ugx " + ".. Reason: " + self.reason.text + ". Done on " + time.strftime(
            '%d %h %Y  %H:%M')

        if dict[self.nom]['$']["balance"][0] == "-":
            string = string + ".  Balance : " + dict[self.nom]['$']["balance"][1:] + " ugx . "
        else:
            string = string + ". the advance is : " + dict[self.nom]['$']["balance"] + " ugx . "

        dict[self.nom]['$']["history"][
            time.strftime('%d %h %Y') + "      " + time.strftime('%H:%M')] = string
        sfile = open(DIR + 'media' + PTH + '0' + PTH + ANGELS + PTH + '' + self.niveau + '.json', 'w')
        json.dump(dict, sfile)
        sfile.close()
        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        if not os.path.isdir(DIR + 'media' + PTH + '0' + PTH + 'HTORY'):
            os.makedirs(DIR + 'media' + PTH + '0' + PTH + 'HTORY')

        ###############            EXPENDUSER("~/")

        his = open(
            DIR + 'media' + PTH + '0' + PTH + 'HTORY' + PTH + '' + time.strftime('%d %B %Y %H %M %S').replace(" ",
                                                                                                                "-") + '.txt',
            'w')
        his.write(string)
        his.close()

        # ***********************************************************************

        fN = open(DIR + 'media' + PTH + '0' + PTH + 'FINANCE.json', 'r')
        fina = json.load(fN)
        fN.close()

        Total = float(fina[time.strftime('%Y')][time.strftime('%B')][time.strftime('%d')]["TGN"]["T"]) + float(
            self.txpaid.text)  # TOTAL DU JOURNNEE

        # fina[time.strftime('%Y')][time.strftime('%B')][time.strftime('%d')][time.strftime('%H:%M:%S')]="Fee from "+self.nom+" * "+self.txpaid.text

        newstr = self.nom + " added " + self.txpaid.text + " ugx"

        fina[time.strftime('%Y')][time.strftime('%B')][time.strftime('%d')]["TGN"]["T"] = str(Total)
        if not fina.get("TT"):
            fina['TT'] = "0"
        # TT = float(fina["TT"]) + float(self.txpaid.text)  # TOTAL DE TOUT LES JOUR
        # fina["TT"] = str(TT)
        # fina[time.strftime('%d %h %Y')] = newstr
        #  WRITE
        fina[time.strftime('%Y')][time.strftime('%B')][time.strftime('%d')]["TGN"][
            time.strftime('%d %b %Y_%S')] = self.nom.title() + "_"+self.niveau+"-"+ fees+" : " + self.txpaid.text + " ugx. "+str(fl)
        ZfN = open(DIR + 'media' + PTH + '0' + PTH + 'FINANCE.json', 'w')
        json.dump(fina, ZfN)
        ZfN.close()  #          le TT reste le total des deposits seulement. les depense doivent puises de TT sur la banq et non a l'ecole

        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        zzz = open(DIR + 'media' + PTH + '0' + PTH + 'NUMBER', 'rb')
        x = pickle.load(zzz) + 1
        zzz.close()
        zzz = open(DIR + 'media' + PTH + '0' + PTH + 'NUMBER', 'wb')
        pickle.dump(x, zzz)
        zzz.close()
        del zzz

        pickl = open(DIR + 'media' + PTH + '0' + PTH + 'SCHOOL.bin', 'rb')
        ids = pickle.load(pickl)
        pickl.close()
        # '+ids['1']+'

        self.printable = GridLayout(cols=1, spacing=40, padding=0, size_hint=(None, None), size=(1000, 420),
                                    # SCREENSHOOT
                                    pos_hint={'center_x': .5, 'center_y': .5}, row_default_height=90,
                                    row_force_default=True)
        # with self.printable.canvas:
        #     Color(1, 1, 1, 1)
        #     Rectangle(pos=self.printable.pos, size=self.printable.size)
        self.printable.add_widget(Label(
            text='**********************************************************************************************************************************************',
            size_hint=(None, None), size=(800, 3)))

        self.num1 = BoxLayout(spacing=0, padding=0)
        # ___________________________

        im = AsyncImage(source=ASY + 'L.png', size_hint=(None, None), size=(150, 150), allow_stretch=True)
        self.num1.add_widget(im)
        self.gnum1 = GridLayout(cols=1, size_hint=(1., 1.), row_default_height=18,
                                row_force_default=True)
        # _______________________________
        # self.gnum1.add_widget(Label(text=' '))
        self.gnum1.add_widget(
            Label(text=''+ids['1']+'               ', color=(0, 0, 0, 1), font_size=21))
        self.gnum1.add_widget(Label(text='       '+ids['2']+'               ', color=(0, 0, 0, 1)))
        self.gnum1.add_widget(
            Label(text='   '+ids['3']+'               ', color=(0, 0, 0, 1)))
        self.gnum1.add_widget(Label(text='       '+ids['4']+'               ', color=(0, 0, 0, 1)))
        self.gnum1.add_widget(
            Label(text='     '+ids['5']+'               ', color=(0, 0, 0, 1), font_size=23))
        self.gnum1.add_widget(Label(text=' ' * 20 + '-' * 100 + ' ' * 20, underline=True, color=(0, 0, 0, 1)))

        self.num1.add_widget(self.gnum1)
        IM = AsyncImage(source=ASY + self.nom + '.png', size_hint=(None, None), size=(150, 150), allow_stretch=True)
        self.num1.add_widget(IM)
        # self.num1.add_widget(Label(text=' '))
        self.printable.add_widget(self.num1)
        # self.printable.add_widget(Label(text=' '))
        self.gsomme = GridLayout(cols=4, spacing=1, padding=0, size_hint_x=1., size_hint_y=.12,
                                 pos_hint={'center_x': .5, 'center_y': .5}, row_default_height=30,
                                 row_force_default=True)  # amount,reasons,date,balance

        self.gsomme.add_widget(Label(text='Reeived with thanks from :  ', italic=True, color=(0, 0, 0, 1)))
        self.gsomme.add_widget(Label(text=self.nom.upper(), italic=True, font_size=25, color=(0, 0, 1, .6)))
        self.gsomme.add_widget(Label(text=' '))
        self.gsomme.add_widget(Label(text='Receipt n. ' + str(x), italic=True, bold=True, color=(0, 0, 0, 1)))
        self.gsomme.add_widget(TextInput(text='Paid ' + self.txpaid.text + ".0 ugx", foreground_color=(1, 1, 1, 1),
                                         background_color=(0, 0, 0, 1)))
        self.gsomme.add_widget(TextInput(text='Reason : ' + self.reason.text + ".", foreground_color=(1, 1, 1, 1),
                                         background_color=(0, 0, 0, 1)))

        if dict[self.nom]['$']["balance"][0] == "-":
            self.gsomme.add_widget(TextInput(text='Balance : ' + milli(dict[self.nom]['$']["balance"][1:]) + " ugx.",
                                             foreground_color=(1, 1, 1, 1), background_color=(0, 0, 0, 1)))

        else:
            self.gsomme.add_widget(TextInput(text='Advance : ' + milli(dict[self.nom]['$']["balance"]) + " ugx.", foreground_color=(1, 1, 1, 1), background_color=(0, 0, 0, 1)))
            # string = string + ". the advance is : " + dict[self.nom]['$']["balance"] + " ugx . "

        self.gsomme.add_widget(TextInput(text=time.strftime('%d/%B/%Y %H:%M'), foreground_color=(1, 1, 1, 1),
                                         background_color=(0, 0, 0, 1)))
        self.gsomme.add_widget(Label(text=' '))
        self.gsomme.add_widget(Label(text=' '))
        self.gsomme.add_widget(Label(text=' '))
        self.gsomme.add_widget(Label(text=' '))
        self.gsomme.add_widget(Label(text=self.niveau, font_size=80, color=(0, 0, 0, .1)))
        self.gsomme.add_widget(Label(text=' '))
        self.gsomme.add_widget(
            Label(text='Signature............................................................', color=(0, 0, 0, 1)))
        # self.gsomme.add_widget(Label(text='..................... '))

        self.printable.add_widget(self.gsomme)

        self.add_widget(self.printable)
        Clock.schedule_once(self.PRINTB, 5)

        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # self.txpaid.text = ""
        # self.reason.text = ""
        Clock.unschedule(self.balanCe)
        Clock.unschedule(self.Term)
        Clock.schedule_interval(self.Term,10)
        Clock.schedule_once(self.balanCe)#
        print('dict', dict[self.nom]['$']["balance"])

    def PRINTB(self, x):
        self.printable.export_to_png(
            NDR + 'Desktop' + PTH + 'P R I N T A B L E' + PTH + '' + self.nom + " " + time.strftime('%B %Y') + ".png")

        self.print_all_i(NDR + 'Desktop' + PTH + 'P R I N T A B L E' + PTH + '' + self.nom + " " + time.strftime('%B %Y') + ".png")

        self.remove_widget(self.printable)
        self.txpaid.text = ""
        self.reason.text = ""
        # get_root_window()
        Clock.schedule_once(self.rewind)

    def rewind(self, x):
        try:
            self.remove_widget(self.Gpay)
        except:
            pass
        try:
            self.autobind('self.SC')
            self.add_widget(self.bckg)
            self.add_widget(self.gaside)
            Clock.schedule_once(self.choisir)
        except:
            pass

    def Brew(self, x):
        Clock.schedule_once(self.rewind)

    def borrowed(self, x):
        if self.txrson.text == "" and self.spreason.text == "":
            return
        if self.txNam.text == "":
            return
        if self.txngapi.text == "":
            return
        try:
            int(self.txngapi.text)
        except:
            return

        fN = open(DIR + 'media' + PTH + '0' + PTH + 'FINANCE.json', 'r')
        fina = json.load(fN)
        fN.close()
        TT = float(fina["TT"])
        B = float(self.txngapi.text)
        rest = TT - B
        fina["TT"] = str(rest)

        if self.txrson.text.replace(" ", "-")[-2:] == "..":
            zzz = open(DIR + 'media' + PTH + '0' + PTH + 'DEPANS', 'rb')
            x = pickle.load(zzz)
            zzz.close()
            x.append(self.txrson.text.upper().replace(" ", "-").replace("..", ""))
            zzz = open(DIR + 'media' + PTH + '0' + PTH + 'DEPANS', 'wb')
            pickle.dump(x, zzz)
            zzz.close()
            fina[time.strftime('%Y')][time.strftime('%B')][time.strftime('%d')]["TSP"][
                self.txrson.text.upper().replace(" ", "-").replace("..", "")] = self.txngapi.text
            self.spreason.text = self.txrson.text.upper().replace(" ", "-").replace("..", "")
        elif self.spreason.text == "":
            if not fina[time.strftime('%Y')][time.strftime('%B')][time.strftime('%d')]["TSP"].get("OTHER"):
                fina[time.strftime('%Y')][time.strftime('%B')][time.strftime('%d')]["TSP"]['OTHER'] = "0"
            fina[time.strftime('%Y')][time.strftime('%B')][time.strftime('%d')]["TSP"]['OTHER'] = str(
                float(fina[time.strftime('%Y')][time.strftime('%B')][time.strftime('%d')]["TSP"]['OTHER']) + float(
                    self.txngapi.text))

        else:
            if fina[time.strftime('%Y')][time.strftime('%B')][time.strftime('%d')]["TSP"].get(self.spreason.text):
                fina[time.strftime('%Y')][time.strftime('%B')][time.strftime('%d')]["TSP"][self.spreason.text] = str(
                    float(fina[time.strftime('%Y')][time.strftime('%B')][time.strftime('%d')]["TSP"][
                              self.spreason.text]) + float(self.txngapi.text))
            else:
                fina[time.strftime('%Y')][time.strftime('%B')][time.strftime('%d')]["TSP"][
                    self.spreason.text] = self.txngapi.text

        DP = float(fina[time.strftime('%Y')][time.strftime('%B')][time.strftime('%d')]["TSP"]["T"]) + float(
            self.txngapi.text)
        fina[time.strftime('%Y')][time.strftime('%B')][time.strftime('%d')]["TSP"][
            "T"] = DP  # //////////////////////////////////////////////////////

        depans = self.txNam.text + " spent  " + self.txngapi.text + "ugx on " + self.txrson.text + "| " + time.strftime(
            '%d /%h /%Y %H:%M:%S')  # + "| Balance : " + str(rest)

        # fina[time.strftime('%d %h %Y')][time.strftime('%H:%M')]=depans

        ZfN = open(DIR + 'media' + PTH + '0' + PTH + 'FINANCE.json', 'w')
        json.dump(fina, ZfN)
        ZfN.close()

        if not os.path.isdir(DIR + 'media' + PTH + '0' + PTH + 'HTORY'):
            os.makedirs(DIR + 'media' + PTH + '0' + PTH + 'HTORY')

        ###############            EXPENDUSER("~/")

        his = open(
            DIR + 'media' + PTH + '0' + PTH + 'HTORY' + PTH + '' + time.strftime('%d %B %Y %H %M %S').replace(" ",
                                                                                                                "-") + '.txt',
            'w')
        his.write(depans)
        his.close()

        self.txrson.text = ""
        self.txNam.text = ""
        self.txngapi.text = ""
        self.SP_GN.text = "SPENT"

        Clock.schedule_once(self.balanCe)
        Clock.schedule_once(self.CCar)

    def mid_end(self,sp,c):
        self.signal="0"
        if c == 'Mid term':
            self.Called = "1"
        else:
            self.Called = "2"
        self.crd(None, self.ccL.text)
        # Clock.schedule_once(self.crd)
        # self.crd(None, self.keepcl)

    def changcl(self,sp,tx):
        self.signal = "0"
        self.prim=tx
        self.crd(None,tx)

    def tin(self,mks,agg):
        gr=GridLayout(cols=2,size_hint=(None, None),size=(90, 29))
        gr.add_widget(TextInput(text=ooo(mks),font_size=13,readonly=True))
        gr.add_widget(TextInput(text=agg,font_size=13, readonly=True))
        return gr

    def crd(self, x=None,t=None):
        try:
            self.analscr.remove_widget(self.gallmarks)
            self.analscr.clear_widgets()
            self.remove_widget(self.analscr)
        except:
            pass
        if self.signal=="1":
            self.ww = 0
            self.remove_widget(self.secgrid)
            self.remove_widget(self.idd)
            self.add_widget(self.idd)
            Clock.schedule_interval(self.white, .01)
            self.Called = "1"
            self.prim=""

        cllist=[]
        for c in Clss() :
            if c.startswith(('P4','P5','P6','P7')):
                cllist.append(c)
        if cllist == [] :
            return


        if t==None :
            t=cllist[0]

        pickl = open(DIR + 'media' + PTH + '0' + PTH + 'SCHOOL.bin', 'rb')
        ids = pickle.load(pickl)
        pickl.close()
        # '+ids['1']+'

        self.analscr= ScrollView(size_hint=(.9, 1.), pos_hint={'center_x': .5, 'center_y': .5}, do_scroll_x=False,
                                 do_scroll_y=True, scroll_timeout=55, scroll_distance=20,
                                 scroll_type=['bars', 'content'], bar_width=10, bar_color=(1, 1, 0, 1), bar_margin=0)


        self.gallmarks=GridLayout(cols=1,size_hint=(1.,None),pos_hint={'center_x': .5, 'center_y': .5})                #   grid all marks
        self.exG = GridLayout(cols=1, size_hint=(None, None), size=(900,200))
        les_point = GridLayout(cols=3, size_hint=(None, None), size=(900, 170))
        im = AsyncImage(source=ASY + 'L.png', size_hint=(None, None), size=(150, 145), allow_stretch=True)
        les_point.add_widget(im)
        grid_in = GridLayout(cols=1, size_hint=(None, None), size=(360, 170), row_default_height=29, row_force_default=True)
        grid_in.add_widget( Label(text='  '+ids['1']+'               ', color=(0, 0, 1, 1), font_size=20))
        grid_in.add_widget( Label(text='       '+ids['3']+'               ', font_size=15, color=(0, 0, 0, 1)))

        grid_in.add_widget(Label(text='       '+ids['5']+'               ', font_size=15, color=(0, 0, 0, 1)))
        grid_in.add_widget(TextInput(text='     “MARKS ANALYSIS”               ',background_color=(1,0,0,.6), font_size=17, foreground_color=(1, 1, 1, 1)))
        # grid_in.add_widget(Label(text=' ' * 15 +self.v_class.text+' ' * 100 + ' ' * 20, underline=True, color=(1, 0, 0, 1)))
        les_point.add_widget(grid_in)
        ph = Label(text=t, font_size=100, underline=True, italic=True, color=(0, 0, 0, .3))
        les_point.add_widget(ph)
        self.exG.add_widget(les_point)

        self.gallmarks.add_widget(self.exG)

        box = GridLayout(cols=2,size_hint=(None, None), size=(872,30))
        self.ccL = Spinner(text=t, values=tuple(cllist),size_hint_x=.2, size_hint_y=.02,background_color=(1,0,0,.6))
        self.ccL.bind(text=self.changcl)
        mid_end = Spinner(values=('Mid term', "End of term"),size_hint_x=.2, size_hint_y=.02,background_color=(1,0,0,.6))
        if self.Called == "1":
            mid_end.text ='Mid term'
        if self.Called == "2":
            mid_end.text ="End of term"
        mid_end.bind(text=self.mid_end)
        box.add_widget(self.ccL)
        box.add_widget(mid_end)
        self.gallmarks.add_widget(box)
        # self.gallmarks.add_widget(TextInput(text="",background_color=(0,0,0,.3),size_hint=(None, None), size=(900,50)))

        lis = []
        TDAT = open(DIR + 'media' + PTH + '0' + PTH + ANGELS + PTH + '' + t + ".json", 'r')
        dict = json.load(TDAT)
        TDAT.close()

        for nam in dict.keys() :
            # print(dict[nam]['marks'])
            if not dict[nam].get('marks'):
                pass
            # if not dict[nam]['marks'].get('total'):
            #     pass
            else:
                if len(dict[nam]['marks']['total']['term' + self.Called]['agt' + self.Called + '_TT']) == 1 :
                    dict[nam]['marks']['total']['term' + self.Called]['agt' + self.Called + '_TT']="0"+dict[nam]['marks']['total']['term' + self.Called]['agt' + self.Called + '_TT']

                AGGG=dict[nam]['marks']['total']['term' + self.Called]['agt' + self.Called + '_TT']
                EN= dict[nam]['marks']['eng']['term' + self.Called]['mgt' + self.Called + '_ENG']
                MT=dict[nam]['marks']['mtc']['term' + self.Called]['mgt' + self.Called + '']
                SC=dict[nam]['marks']['scie']['term' + self.Called]['mgt' + self.Called + '_SCIE']
                SS=dict[nam]['marks']['sst']['term' + self.Called]['mgt' + self.Called + '_SST']
                TT=dict[nam]['marks']['total']['term' + self.Called]['mgt' + self.Called + '_TT']

                lis.append(AGGG+"!"+nam+"@"+EN+"#"+MT+"$"+SC+"%"+SS+"^"+TT+"&"+division(EN,MT,SC,SS,AGGG))
        lis.sort()
        # print(lis)

        grido=GridLayout(cols=8,spacing=3,padding=2,size_hint=(None, None), row_default_height=25, row_force_default=True)

        grido.add_widget(Label(text="",size_hint=(None,None),size=(30,25))) ; grido.add_widget(Label(text="",size_hint=(None,None),size=(280,25)))
        grido.add_widget(TextInput(text="E N G",background_color=(0,0,0,.2),font_size=13,readonly=True, size_hint=(None, None), size=(90, 25)));grido.add_widget(TextInput(text="M T C",background_color=(0,0,0,.2),font_size=13,readonly=True, size_hint=(None, None), size=(90, 25)))
        grido.add_widget(TextInput(text="S C I E",background_color=(0,0,0,.2),font_size=13,readonly=True, size_hint=(None, None), size=(90, 25)));grido.add_widget(TextInput(text="S S T",background_color=(0,0,0,.2),font_size=13,readonly=True, size_hint=(None, None), size=(90, 25)))
        grido.add_widget(TextInput(text="TOTAL",background_color=(0,0,0,.2),font_size=13,readonly=True, size_hint=(None, None),size=(90, 25)));grido.add_widget(TextInput(text="Summary",background_color=(0,0,0,.2),font_size=11.7,readonly=True, size_hint=(None, None),size=(90, 25)))

        grido.add_widget(TextInput(text="#",background_color=(0,0,0,.2),readonly=True, size_hint=(None, None), size=(30, 25)));grido.add_widget(TextInput(text="N A M E",background_color=(0,0,0,.2),readonly=True,size_hint=(None,None),size=(280,29)))
        for i in range(5):
            grido.add_widget(self.tin("Mks","Agg"))
        grido.add_widget(TextInput(text="Division",background_color=(0,0,0,.2), font_size=12, readonly=True, size_hint=(None, None), size=(90, 29)))
        #lis.append(AGGG+"!"+nam+"@"+EN+"#"+MT+"$"+SC+"%"+SS+"^"+TT+"&"+division(EN,MT,SC,SS,AGGG))
        no=1
        DV=['DIV I','DIV II','DIV III','DIV IV','DIV V','DIV U']
        for ds in DV:
            for ln in lis :
                if ln.endswith(ds):
                    grido.add_widget(TextInput(text=str(no),font_size=13,readonly=True,size_hint=(None, None), size=(30, 29)))
                    grido.add_widget(TextInput(text=ln[ln.index('!')+1 : ln.index('@')],font_size=13,readonly=True, size_hint=(None, None), size=(280, 29)))
                    grido.add_widget(self.tin(ln[ln.index('@')+1:ln.index('#')], AGG(int(ln[ln.index('@')+1:ln.index('#')])) ))
                    grido.add_widget(self.tin(ln[ln.index('#') + 1:ln.index('$')], AGG(int(ln[ln.index('#') + 1:ln.index('$')]))))
                    grido.add_widget( self.tin(ln[ln.index('$') + 1:ln.index('%')], AGG(int(ln[ln.index('$') + 1:ln.index('%')]))))
                    grido.add_widget(self.tin(ln[ln.index('%') + 1:ln.index('^')], AGG(int(ln[ln.index('%') + 1:ln.index('^')]))))
                    grido.add_widget(self.tin(ln[ln.index('^') + 1:ln.index('&')], ln[:ln.index('!')]))
                    grido.add_widget(TextInput(text=ln[ln.index('&')+1:], font_size=12, readonly=True, size_hint=(None, None), size=(90, 29)))
                    no+=1

        self.gallmarks.size=(900,29*no+350)
        grido.size = (900, 29 * no + 58)
        self.gallmarks.add_widget(grido)
        self.analscr.add_widget(self.gallmarks)
        self.add_widget(self.analscr)

        try:
            self.remove_widget(self.goback1)
            self.remove_widget(self.goback2)
            self.remove_widget(self.goback3)
        except:
            pass
        self.goback1 = Button(text='Back', color=(1, 0, 0, 1), size_hint=(.2, .1))
        self.goback1.bind(on_release=self.quitanl)
        # self.idd.bind(on_release=self.Viewcleaner)
        self.add_widget(self.goback1)

        self.goback2 = Button(text='Print', color=(1, 0, 0, 1), size_hint=(.2, .1), pos_hint={'center_x': .5, 'center_y': .05})
        self.goback2.bind(on_release=self.Panalys)
        # self.idd.bind(on_release=self.Viewcleaner)
        self.add_widget(self.goback2)

        self.goback3 = Button(text='AGGREGATES', color=(1, 0, 0, 1), size_hint=(.2, .1),pos_hint={'center_x': .92, 'center_y': .05})
        self.goback3.bind(on_release=self.aggregates)
        # self.idd.bind(on_release=self.Viewcleaner)
        self.add_widget(self.goback3)
        self.ANAL=lis

        del lis

        self.autobind("self.analscr",speed=1)
    def rG(self,mks,agg,ln):
        gr=GridLayout(cols=2,size_hint=(None, None),size=(ln, 29))
        gr.add_widget(TextInput(text=mks,font_size=13,readonly=True))
        gr.add_widget(TextInput(text=agg,font_size=13, readonly=True))
        return gr

    def rTXT(self,txt="",sz=45):
        print("txt",txt,type(txt))
        if txt == "0" or txt == 0 :
            txt=" "
        tt=TextInput(text=str(txt),font_size=13,readonly=True,size_hint=(None, None),size=(sz, 29))
        return tt

    def percent(self,i):
        nomb = str(i)
        if "." in str(nomb):
            if int(nomb[nomb.index(".") + 1:]) >= 5:
                nomb = int(nomb[:nomb.index('.')]) + 1
            else:
                nomb = int(nomb[:nomb.index('.')])
        return str(nomb)

    def aggregates(self,x):
        if len(self.ANAL)==0 :
            return
        Window.size=(1240, 595)

        # self.gallmarks.clear_widgets()
        self.remove_widget(self.analscr)

        pickl = open(DIR + 'media' + PTH + '0' + PTH + 'SCHOOL.bin', 'rb')
        ids = pickle.load(pickl)
        pickl.close()
        # '+ids['1']+'

        self.gallagg=GridLayout(cols=1,size_hint=(1.,1.),pos_hint={'center_x': .5, 'center_y': .5})

        self.exG = GridLayout(cols=1, size_hint=(None, None), size=(1000, 200))
        les_point = GridLayout(cols=3, size_hint=(None, None), size=(1000, 170))
        im = AsyncImage(source=ASY + 'L.png', size_hint=(None, None), size=(150, 145), allow_stretch=True)
        les_point.add_widget(im)
        grid_in = GridLayout(cols=1, size_hint=(None, None), size=(360, 170), row_default_height=29,
                             row_force_default=True)
        grid_in.add_widget(
            Label(text='  '+ids['1']+'               ', color=(0, 0, 1, 1), font_size=20))
        grid_in.add_widget(
            Label(text='                      ', font_size=15, color=(0, 0, 0, 1)))

        grid_in.add_widget(
            Label(text='       MARKSHEET ANALYSIS REPORT - AGREGATES               ', font_size=15, color=(0, 0, 0, 1)))

        # grid_in.add_widget(Label(text=' ' * 15 +self.ccL.text+' ' * 100 + ' ' * 20, underline=True, color=(1, 0, 0, 1)))
        les_point.add_widget(grid_in)
        ph = Label(text=self.ccL.text, font_size=100, underline=True, italic=True, color=(0, 0, 0, .3))
        les_point.add_widget(ph)
        self.exG.add_widget(les_point)

        self.gallagg.add_widget(self.exG)

        self.gallagg.add_widget(self.rG('Exam session :',self.TERM.text,300))

        self.g17=GridLayout(cols=17)
        L=["",'Aggregates','ABS','D1','D2','C3','C4','C5','C6','P7','P8','F9','Ps','Fs','ALL','%Ps','%Fs']
        SZ=[300,100,50,50,50,50,50,50,50,50,50,50,50,50,50,55,55]
        CNT=0
        for l in L :
            self.g17.add_widget(self.rTXT(l,SZ[CNT]))
            CNT+=1

        # lis.append(AGGG+"!"+nam+"@"+EN+"#"+MT+"$"+SC+"%"+SS+"^"+TT+"&"+division(EN,MT,SC,SS,AGGG))

        DICT = {'ENGLISH LANGUAGE': {'D1': [], 'D2': [], 'C3': [], 'C4': [], 'C5': [], 'C6': [], 'P7': [], 'P8': [], 'F9': []},
                'MATHEMATICS': {'D1': [], 'D2': [], 'C3': [], 'C4': [], 'C5': [], 'C6': [], 'P7': [], 'P8': [], 'F9': []},
                'INTEGRATED SCIENCE': {'D1': [], 'D2': [], 'C3': [], 'C4': [], 'C5': [], 'C6': [], 'P7': [], 'P8': [], 'F9': []},
                'SOCIAL STUDIES': {'D1': [], 'D2': [], 'C3': [], 'C4': [], 'C5': [], 'C6': [], 'P7': [], 'P8': [],  'F9': []}}
        EN=0
        MT=0
        SC=0
        SS=0

        RSR=['D1','D2','C3','C4','C5','C6','P7','P8']


        for cr in self.ANAL :
            for d in DICT['ENGLISH LANGUAGE'].keys():
                aag=AGG(int(cr[cr.index('@')+1:cr.index('#')]))
                if aag  == d :
                    DICT['ENGLISH LANGUAGE'][d].append('1')
                    if aag in RSR :
                        EN+=1

        PEN = EN
        FEN = len(self.ANAL) - EN
        PPEN = self.percent(EN * 100 / len(self.ANAL))
        FPEN = self.percent(FEN * 100 / len(self.ANAL))



        for cr in self.ANAL:
            for d in DICT['MATHEMATICS'].keys():
                agg=AGG(int(cr[cr.index('#')+1:cr.index('$')]))
                if agg == d:
                    DICT['MATHEMATICS'][d].append('1')
                    if aag in RSR:
                        MT += 1
        PMT = MT
        FMT = len(self.ANAL) - MT
        PPMT = self.percent(MT * 100 / len(self.ANAL))
        FPMT = self.percent(FMT * 100 / len(self.ANAL))



        for cr in self.ANAL:
            for d in DICT['INTEGRATED SCIENCE'].keys():
                agg=AGG(int(cr[cr.index('$')+1:cr.index('%')]))
                if agg == d:
                    DICT['INTEGRATED SCIENCE'][d].append('1')
                    if aag in RSR:
                        SC += 1
        PSC = SC
        FSC = len(self.ANAL) - SC
        PPSC = self.percent(SC * 100 / len(self.ANAL))
        FPSC = self.percent(FSC * 100 / len(self.ANAL))



        for cr in self.ANAL:
            for d in DICT['SOCIAL STUDIES'].keys():
                agg=AGG(int(cr[cr.index('%')+1:cr.index('^')]))
                if agg == d:
                    DICT['SOCIAL STUDIES'][d].append('1')
                    if aag in RSR:
                        SS += 1

        PSS=SS
        FSS=len(self.ANAL)-SS
        PPSS=self.percent(SS*100/len(self.ANAL))
        FPSS=self.percent(FSS*100/len(self.ANAL))
        ALL=str(len(self.ANAL))
        tr = [[PEN, FEN,ALL, PPEN, FPEN], [PMT, FMT,ALL, PPMT, FPMT], [PSC, FSC,ALL, PPSC, FPSC], [PSS, FSS,ALL, PPSS, FPSS]]

        CNT = 0
        for key in DICT.keys():
            self.g17.add_widget(self.rTXT(key,300))
            self.g17.add_widget(self.rTXT('AllDone', 100))
            self.g17.add_widget(self.rTXT('', 50))

            for nk in DICT[key].keys():
                self.g17.add_widget(self.rTXT(str(len(DICT[key][nk])), 50))

            self.g17.add_widget(self.rTXT(tr[CNT][0], 50))
            self.g17.add_widget(self.rTXT(tr[CNT][1], 50))
            self.g17.add_widget(self.rTXT(tr[CNT][2], 50))
            self.g17.add_widget(self.rTXT(tr[CNT][3]+"%", 55))
            self.g17.add_widget(self.rTXT(tr[CNT][4]+"%", 55))
            CNT+=1

        self.gallagg.add_widget(self.g17)
        self.add_widget(self.gallagg)


    def Panalys(self,x):
        self.gallmarks.export_to_png(NDR + 'Desktop' + PTH + 'P R I N T A B L E' + PTH + '' + "DETAILED MARKSHEET REPORT " + self.ccL.text + ".png")
        try:
            self.gallagg.export_to_png(
                NDR + 'Desktop' + PTH + 'P R I N T A B L E' + PTH + '' + "MARKSHEET ANALYSIS REPORT - AGREGATES " + self.ccL.text + ".png")
            self.print_all_i(
                NDR + 'Desktop' + PTH + 'P R I N T A B L E' + PTH + '' + "MARKSHEET ANALYSIS REPORT - AGREGATES " + self.ccL.text + ".png")
        except:
            pass

        self.print_all_i(NDR + 'Desktop' + PTH + 'P R I N T A B L E' + PTH + '' + "DETAILED MARKSHEET REPORT " + self.ccL.text + ".png")



    def quitanl(self,x):
        if "gallagg" in dir(self ):
            self.remove_widget(self.gallagg)
            self.remove_widget(self.goback1)
            self.remove_widget(self.goback2)
            self.remove_widget(self.goback3)
            self.add_widget(self.analscr)
            self.add_widget(self.goback1)
            self.add_widget(self.goback2)
            self.add_widget(self.goback3)
            del self.gallagg
        else:
            self.remove_widget(self.analscr)
            # self.remove_widget(self.gallagg)
            self.remove_widget(self.goback1)
            self.remove_widget(self.goback2)
            self.remove_widget(self.goback3)

            Clock.schedule_once(self.secretaire,-1)
        try:
            del self.gallagg
        except:
            pass

    def rport(self, event):
        # os.system('gio open Documents/"Report Cards for Term 3.docx"')
        os.system("gio open ftp://galileo:inabahs9891@192.168.1.1/'Report Cards for Term 3.docx'")

    def adst(self, v):
        try:
            self.remove_widget(self.g_addcla)
        except:
            pass
        self.idd.background_color = (0, 0, 0, .96)
        self.remove_widget(self.secgrid)

        list = Clss()

        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        #      PUT HERE OPEN()  FUNCTION TO READ JSON FROM DISK     FOR INFO    FOR WRITING NEW DATA THEN SAVE >>
        # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        self.bigformgrid = GridLayout(cols=4, spacing=0)  # 1 is select class,\students number,\girls,boys,\ most aged

        self.cls_info = GridLayout(cols=1, size_hint=(.2, 1.), pos_hint={'center_x': 1., 'center_y': .5})  ######

        # self.photo=Image(on_touch_up=self.captur)
        # self.cls_info.add_widget(self.photo)

        self.photo = Button(text='Photo', on_release=self.captur)
        self.cls_info.add_widget(self.photo)
        # ----------------MAKE TUPLE FOR VALUES----------------
        self.spcls = Spinner(text='Select Class >', font_size=20, size_hint_y=.7, values=tuple(list),
                             background_color=(0, 0, 0, .95))
        self.spcls.bind(text=self.textcls)
        self.cls_info.add_widget(self.spcls)

        try:
            self.spcls.text = self.keepclass  # if it was opened before
        except:
            pass

        self.ttpp = Button(text='Total pupils :\n       *', size_hint_y=.7, color=(1, .5, 0, 1), italic=True,
                           background_color=(0, 0, 0, .95))
        self.cls_info.add_widget(self.ttpp)
        self.boys = Button(text='Boys :\n       *', size_hint_y=.7, color=(1, .5, 0, 1), italic=True,
                           background_color=(0, 0, 0, .95))
        self.cls_info.add_widget(self.boys)
        self.girls = Button(text='Girls :\n       *', size_hint_y=.7, color=(1, .5, 0, 1), italic=True,
                            background_color=(0, 0, 0, .95))
        self.cls_info.add_widget(self.girls)
        self.younger = Button(text='The older is :\n       *', size_hint_y=.7, color=(1, .5, 0, 1), italic=True,
                              background_color=(0, 0, 0, .95))
        self.cls_info.add_widget(self.younger)

        self.bigformgrid.add_widget(self.cls_info)

        self.sv = ScrollView(do_scroll_x=False, do_scroll_y=True, scroll_timeout=55,
                             scroll_distance=20, scroll_type=['bars', 'content'], bar_width=10, bar_color=(1, 1, 0, 1),
                             bar_margin=0)
        # self.sv.bind(on_scroll_move=self.scrolled)
        self.roll = 1
        Window.bind(on_keyboard=self.bupdown)

        self.form = GridLayout(cols=2, spacing=10, size_hint_x=1., size_hint_y=3.2, row_default_height=45,
                               row_force_default=True)

        # self.Gretour = GridLayout(cols=2, size_hint=(1., .3))
        self.form.add_widget(Label(text=''))
        self.retour = Button(text='Back')

        self.form.add_widget(self.retour)
        self.form.add_widget(Label(text=''))
        self.interd = Label(
            text="\n*  You can not go back without saving\n what you filled, unless you press \nthe CLEAR button.",
            color=(1, .5, 0, 1))
        self.form.add_widget(self.interd)
        self.form.add_widget(Label(text=''))
        self.form.add_widget(Label(text=''))
        self.form.add_widget(Label(text=''))
        self.form.add_widget(Label(text=''))

        self.fnam = Label(text=" " * 50 + "Full Name :")
        self.form.add_widget(self.fnam)
        self.txfnam = TextInput(hint_text="Full Name",allow_copy=True)
        self.txfnam.bind(text=self.STUDedit)
        self.form.add_widget(self.txfnam)

        self.lid = Label(text=" " * 50 + "Learner id / nin :")
        self.form.add_widget(self.lid)
        self.txlid = TextInput(allow_copy=True)
        self.form.add_widget(self.txlid)

        self.sex = Label(text=" " * 50 + "Sex :")
        self.form.add_widget(self.sex)
        self.txsex = Spinner(text='', values=('M', 'F'))
        self.form.add_widget(self.txsex)

        self.naty = Label(text=" " * 50 + "Nationality : ")
        self.form.add_widget(self.naty)
        self.txnaty = TextInput(allow_copy=True)
        self.form.add_widget(self.txnaty)

        # self.lsp = Label(text=" "*45+"Languages spoken : ")
        # self.form.add_widget(self.lsp)
        # self.txlsp = TextInput()
        # self.form.add_widget(self.txlsp)

        self.yb = Label(text=" " * 50 + "Year of birth : ")
        self.form.add_widget(self.yb)
        self.txyb = TextInput(allow_copy=True)
        self.form.add_widget(self.txyb)

        self.ainy = Label(text=" " * 48 + "Age in years : ")
        self.form.add_widget(self.ainy)
        self.txainy = TextInput(allow_copy=True)
        self.form.add_widget(self.txainy)

        self.yregis = Label(text=" " * 45 + "Year of registration : ")
        self.form.add_widget(self.yregis)
        self.txyregis = TextInput(allow_copy=True)
        self.form.add_widget(self.txyregis)

        self.form.add_widget(Label(text=''))
        self.form.add_widget(Label(text='RESIDANCE'))

        # self.countr = Label(text=" "*50+"Country : ")
        # self.form.add_widget(self.countr)
        # self.txcountr = TextInput()
        # self.form.add_widget(self.txcountr)

        self.sct = Label(text=" " * 50 + "Sub-country : ")
        self.form.add_widget(self.sct)
        self.txsct = TextInput(allow_copy=True)
        self.form.add_widget(self.txsct)

        self.par = Label(text=" " * 50 + "Parish  :")
        self.form.add_widget(self.par)
        self.txpar = TextInput(allow_copy=True)
        self.form.add_widget(self.txpar)

        self.blvl = Label(text=" " * 50 + "Block / village : ")
        self.form.add_widget(self.blvl)
        self.txblvl = TextInput(allow_copy=True)
        self.form.add_widget(self.txblvl)

        self.form.add_widget(Label(text=''))
        self.form.add_widget(Label(text='PARENTS / GUARDIANS'))

        self.wzz = Label(text=" " * 50 + "Name : ")
        self.form.add_widget(self.wzz)
        self.txwzz = TextInput(allow_copy=True)
        self.form.add_widget(self.txwzz)

        self.wsx = Label(text=" " * 50 + "Sex : ")
        self.form.add_widget(self.wsx)
        self.txwsx = Spinner(text='', values=('M', 'F'))
        self.form.add_widget(self.txwsx)

        self.wag = Label(text=" " * 50 + "Age : ")
        self.form.add_widget(self.wag)
        self.txwag = TextInput(allow_copy=True)
        self.form.add_widget(self.txwag)

        self.wtel = Label(text=" " * 50 + "Contact Phone : ")
        self.form.add_widget(self.wtel)
        self.txwtel = TextInput(allow_copy=True)
        self.form.add_widget(self.txwtel)

        self.rwl = Label(text=" " * 30 + "Relationship with the learner : ")
        self.form.add_widget(self.rwl)
        self.txrwl = TextInput(allow_copy=True)
        self.form.add_widget(self.txrwl)

        self.form.add_widget(Label(text=''))
        self.form.add_widget(Label(text='SCHOOL LAST ATTENDED '))

        self.yr = Label(text=" " * 50 + "Year : ")
        self.form.add_widget(self.yr)
        self.txyr = TextInput(allow_copy=True)
        self.form.add_widget(self.txyr)

        self.clas = Label(text=" " * 50 + "Class : ")
        self.form.add_widget(self.clas)
        self.txclas = TextInput(allow_copy=True)
        self.form.add_widget(self.txclas)

        self.nmsc = Label(text=" " * 50 + "Name of school : ")
        self.form.add_widget(self.nmsc)
        self.txnmsc = TextInput(allow_copy=True)
        self.form.add_widget(self.txnmsc)

        self.form.add_widget(Label(text=''))
        self.form.add_widget(Label(text='OTHER INFORMATIONS'))

        self.nsis = Label(text=" " * 50 + "Number of sister \n" + " " * 50 + "  in this school : ")
        self.form.add_widget(self.nsis)
        self.txnsis = TextInput(allow_copy=True)
        self.form.add_widget(self.txnsis)

        self.nbro = Label(text=" " * 50 + "Number of brothers\n" + " " * 50 + " in this school : ")
        self.form.add_widget(self.nbro)
        self.txnbro = TextInput(allow_copy=True)
        self.form.add_widget(self.txnbro)

        self.cash = Label(text=" " * 45 + "Bursary Scheme ( Y / N ) ")  # spinner
        self.form.add_widget(self.cash)
        self.txcash = Spinner(text='', values=('Y', 'N'))
        self.form.add_widget(self.txcash)

        self.vrst = Label(
            text=" " * 40 + "Vurnerability status\n" + " " * 34 + " ( CM, ORP, PWD, CHH, OTH ) ")  # spinner
        self.form.add_widget(self.vrst)
        self.txvrst = Spinner(text="", values=('CM', 'ORP', 'PWD', 'CHH', 'OTH'))  # spinner
        self.form.add_widget(self.txvrst)

        self.fee = Label(text=" " * 40 + "Fee ")
        self.form.add_widget(self.fee)
        self.txfee = TextInput(text="0", allow_copy=True)
        self.form.add_widget(self.txfee)

        self.cmm = Label(text=" " * 50 + "Comment : ")
        self.form.add_widget(self.cmm)
        self.txcmm = TextInput(allow_copy=True)
        self.form.add_widget(self.txcmm)

        self.form.add_widget(Label(text=''))
        self.form.add_widget(Label(text=''))

        self.SAVE = Button(text='S A V E   A L L', size_hint_x=.1, on_release=self.saveall)
        self.form.add_widget(self.SAVE)
        self.CLEAR = Button(text='C L E A R   A L L', size_hint_x=.1, on_release=self.CL_ALL)
        self.form.add_widget(self.CLEAR)

        self.sv.add_widget(self.form)

        self.bigformgrid.add_widget(self.sv)

        self.gupdown = GridLayout(cols=1, size_hint=(None, 1.), size=(30, 1))  # >>>>>>>>>>>>>>>>>>

        self.gupdown.add_widget(Label(text="", color=(.4, 0, 1, 0), size_hint=(1., None), size=(1, 35)))
        self.bup = Button(text="^\n^", valign="center", color=(.4, 0, 1, 0), background_color=(1, 1, 1, 1),
                          size_hint=(1., None), size=(1, 25), on_release=self.UPreleased)
        self.gupdown.add_widget(self.bup)

        for xy in range(14):
            self.gupdown.add_widget(Label(text="", color=(.4, 0, 1, 0), size_hint=(1., None), size=(1, 35)))

        self.bdown = Button(text="v\nv", color=(.4, 0, 1, 0), background_color=(1, 1, 1, 1), size_hint=(1., None),
                            size=(1, 25), on_release=self.DOWNreleased)
        self.gupdown.add_widget(self.bdown)

        self.bigformgrid.add_widget(self.gupdown)
        self.add_widget(self.bigformgrid)
        if self.txfnam.text == "":
            self.retour.bind(on_release=self.Goback)

    #     Clock.schedule_once(self.png,5)
    #
    # def png(self, x):
    #     self.form.export_to_png("./wonder2.png")
    def bupdown(self, window, key, *largs):
        if key == 273:
            self.roll = self.roll + .01
            self.sv.scroll_y = self.roll
            print("^", self.roll)
        if key == 274:
            self.roll = self.roll - .01
            self.sv.scroll_y = self.roll
            print("v", self.roll)

        # print(key)

    def UPreleased(self, x):
        if "^" in self.bup.text:
            self.roll = self.roll + .01
            self.sv.scroll_y = self.roll
            print("^", self.roll)

    def DOWNreleased(self, x):
        if "v" in self.bdown.text:
            self.roll = self.roll - .01
            self.sv.scroll_y = self.roll
            print("v", self.roll)

    def STUDedit(self, sp, tex):
        if self.spcls.text == 'Select Class >':
            self.spcls.background_color = (1, 0, 0, 1)
            return

        file = open(DIR + 'media' + PTH + '0' + PTH + ANGELS + PTH + '' + self.spcls.text + ".json",
                    'r')  # EDIT WITHOUT LOSING HISTORY   (MARKS  ,  PAYMENTS)   AND REPLACE HIM
        dict = json.load(file)
        file.close()

        if dict.get(tex.lower(), 0) or dict.get(tex.capitalize(), 0):

            #   BACKUP

            self.weka = tex.lower()
            if dict[tex.lower()].get('marks'):
                self.maks = dict[tex.lower()]['marks']
            self.dollar = dict[tex.lower()]['$']

            self.txlid.text = dict[tex.lower()]["Learner id / nin "]
            self.txfnam.text = dict[tex.lower()]["Full Name"]
            self.txsex.text = dict[tex.lower()]["Sex"]
            self.txnaty.text = dict[tex.lower()]["Nationality"]
            self.txyb.text = dict[tex.lower()]["Year of birth"]
            self.txainy.text = dict[tex.lower()]["Age in years"]
            self.txyregis.text = dict[tex.lower()]["Year of registration"]
            self.txsct.text = dict[tex.lower()]["Sub-country"]
            self.txpar.text = dict[tex.lower()]["Parish"]
            self.txblvl.text = dict[tex.lower()]["Block / village"]
            self.txwzz.text = dict[tex.lower()]["Parent Name"]
            self.txwsx.text = dict[tex.lower()]["Parent Sex"]
            self.txwag.text = dict[tex.lower()]["Parent Age"]
            self.txwtel.text = dict[tex.lower()]["Contact Phone"]
            self.txrwl.text = dict[tex.lower()]["Relationship with the learner"]
            self.txyr.text = dict[tex.lower()]["Last school Year"]
            self.txclas.text = dict[tex.lower()]["Class"]
            self.txnmsc.text = dict[tex.lower()]["Name of school"]
            self.txnsis.text = dict[tex.lower()]["Number of sister"]
            self.txnbro.text = dict[tex.lower()]["Number of brothers"]
            self.txcash.text = dict[tex.lower()]["Bursary Scheme"]
            self.txvrst.text = dict[tex.lower()]["Vurnerability status"]
            self.txcmm.text = dict[tex.lower()]["Comment"]
            self.txfee.text = dict[tex.lower()]["fee"]
            # self.txcmm.text = dict[tex.lower()]["Comment"]
            self.photo.background_normal = DIR + 'media' + PTH + '0' + PTH + '' + self.txfnam.text.lower() + ".png"

    def textcls(self, sp, tx):
        TDAT = open(DIR + 'media' + PTH + '0' + PTH + ANGELS + PTH + '' + tx + '.json', 'r')
        DT = json.load(TDAT)
        TDAT.close()
        boys = []
        girls = []
        ages = []
        for s in DT.keys():
            # if int(DT[s]["Age in years"]) :
            ages.append(DT[s]["Age in years"])
            if DT[s]['Sex'] == 'F':
                girls.append(s)
            if DT[s]['Sex'] == 'M':
                boys.append(s)
        self.boys.text = "Boys :\n       " + str(len(boys))
        self.girls.text = "Girls :\n       " + str(len(girls))
        self.ttpp.text = "Total pupils :\n       " + str(len(ages))
        ages.sort()
        if ages != []:
            self.younger.text = "The older is :\n       " + str(ages[-1])

    def CL_ALL(self, x):
        try:
            self.keepclass = self.spcls.text
        except:
            pass
        Window.unbind(on_keyboard=self.bupdown)
        self.remove_widget(self.bigformgrid)
        Clock.schedule_once(self.adst)
    def captur(self,x):
        threading.Thread(target=self.recorder).start()

    def recorder(self):
        import cv2
        im=""
        try:

            im = cv2.VideoCapture(1)
            print('1111111111111')
            for i in range(500):
                ret, frame = im.read()
                cv2.imshow(self.txfnam.text+"in cv2 n1", frame)
                if cv2.waitKey(1) == ord('\r'):
                    # cv2.imwrite(self.txfnam.text.lower() + '.png', frame)
                    cv2.imwrite(DIR + 'media' + PTH + '0' + PTH + self.txfnam.text.lower() + '.png', frame)
                    self.photo.background_normal =  DIR + 'media' + PTH + '0' + PTH + self.txfnam.text.lower() + '.png'
                    break
                if cv2.waitKey(1) == ord(' '):
                    break
            im.release()
            cv2.destroyAllWindows()
            if "weka" in dir(self):
                Clock.schedule_once(self.CL_ALL, 2)
                del self.weka
            im="ok"
        except:
            try:
                im = cv2.VideoCapture(0)
                print('0000000000')
                for i in range(500):
                    ret, frame = im.read()
                    cv2.imshow(self.txfnam.text + "in cv2 n0", frame)
                    if cv2.waitKey(1) == ord('\r'):
                        # cv2.imwrite(self.txfnam.text.lower() + '.png', frame)
                        cv2.imwrite(DIR + 'media' + PTH + '0' + PTH + self.txfnam.text.lower() + '.png', frame)
                        self.photo.background_normal =  DIR + 'media' + PTH + '0' + PTH + self.txfnam.text.lower() + '.png'
                        break
                    if cv2.waitKey(1) == ord(' '):
                        break
                im.release()
                cv2.destroyAllWindows()
                if "weka" in dir(self):
                    Clock.schedule_once(self.CL_ALL, 2)
                    del self.weka
                im = "ok"
            except:
                Clock.schedule_once(self.second_capture)




    def keyb(self, window, key, *largs):
        if key == 27 or key == ord(" "):
            try:
                self.cameraObject.play = False
            except:
                pass
            # self.cameraObject.stopped=True
            del self.cameraObject
            # Camera.stop()
            self.remove_widget(self.layout)
            del self.layout
            # a=Camera(play=False,stopped=True)
        if key == ord('\r'):
            self.cameraObject.export_to_png(ANGELS + PTH + '' + self.txfnam.text.lower() + '.png')
            self.cameraObject.export_to_png(DIR + 'media' + PTH + '0' + PTH + '' + self.txfnam.text.lower() + '.png')
            del self.cameraObject
            # Camera.stop()
            self.remove_widget(self.layout)
            self.photo.background_normal = DIR + 'media' + PTH + '0' + PTH + self.txfnam.text.lower() + '.png'
            del self.layout
        self.cameraObject = None
        if "weka" in dir(self):
            Clock.schedule_once(self.CL_ALL, 2)
            del self.weka
        Window.unbind(on_keyboard=self.keyb)

    def second_capture(self, x):
        for swepper in range(3):
            print('swepper')
        # if not os.path.isdir('ANGELS'):
        #     os.mkdir('ANGELS')
        self.layout = BoxLayout(orientation='vertical')
        try:
            try:

                self.cameraObject = Camera(play=False)
                index = 2
                print('index 2')
            except:
                self.cameraObject = Camera(play=False)
                index = 1
                print('index 1')
        except:
            try:
                self.cameraObject = Camera(play=False)
                index = 0
                print('index 0')
            except:
                return


        self.cameraObject.play = True
        # self.cameraObject.resolution = (300, 300) # Specify the resolution
        self.camaraClick = Button(text="Take Photo")
        self.camaraClick.size_hint = (.5, .2)
        self.camaraClick.pos_hint = {'x': .25, 'y': .75}
        # self.camaraClick.bind(on_press=self.onCameraClick)
        Window.bind(on_keyboard=self.keyb)

        self.layout.add_widget(self.cameraObject)

        # self.layout.add_widget(self.camaraClick)

        self.add_widget(self.layout)


    def onCameraClick(self, *args):
        self.cameraObject.export_to_png(ANGELS + PTH + '' + self.txfnam.text.lower() + '.png')
        self.cameraObject.export_to_png(DIR + 'media' + PTH + '0' + PTH + '' + self.txfnam.text.lower() + '.png')
        del self.cameraObject
        # Camera.stop()
        self.remove_widget(self.layout)
        self.photo.background_normal = ANGELS + PTH + '' + self.txfnam.text.lower() + '.png'
        del self.layout

    def saveall(self, rx):
        if self.spcls.text == 'Select Class >':
            return

        file = open(DIR + 'media' + PTH + '0' + PTH + ANGELS + PTH + '' + self.spcls.text + ".json", 'r')
        dict = json.load(file)
        file.close()
        # TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
        if "weka" in dir(self):
            # if  dict.get(self.weka,0) ==0:
            #     return
            # TDAT = open(DIR+'media'+PTH+'.0'+PTH+'ANGELS'+PTH+'' + self.PS.text + ".json", 'r')
            # DT = json.load(TDAT)
            # TDAT.close()

            TAD = open(DIR + 'media' + PTH + '0' + PTH + 'DISABLED.json', 'r')
            TD = json.load(TAD)
            TAD.close()

            TD[self.weka + '/ ' + self.spcls.text] = dict[self.weka]
            FF = open(DIR + 'media' + PTH + '0' + PTH + 'DISABLED.json', 'w')
            json.dump(TD, FF)
            FF.close()
            # del DT[self.CL.text]
            # FF = open(DIR+'media'+PTH+'.0'+PTH+'ANGELS'+PTH+'' + self.PS.text + '.json', 'w')
            # json.dump(DT, FF)
            # FF.close()
        # VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV

        dict[self.txfnam.text.lower()] = {"Learner id / nin ": self.txlid.text,
                                          "Full Name": self.txfnam.text.lower(),
                                          "Sex": self.txsex.text,
                                          "Nationality": self.txnaty.text,
                                          "Year of birth": self.txyb.text,
                                          "Age in years": self.txainy.text,
                                          "Year of registration": self.txyregis.text,
                                          "Sub-country": self.txsct.text,
                                          "Parish": self.txpar.text,
                                          "Block / village": self.txblvl.text,
                                          "Parent Name": self.txwzz.text,
                                          "Parent Sex": self.txwsx.text,
                                          "Parent Age": self.txwag.text,
                                          "Contact Phone": self.txwtel.text,
                                          "Relationship with the learner": self.txrwl.text,
                                          "Last school Year": self.txyr.text,
                                          "Class": self.txclas.text,
                                          "Name of school": self.txnmsc.text,
                                          "Number of sister": self.txnsis.text,
                                          "Number of brothers": self.txnbro.text,
                                          "Bursary Scheme": self.txcash.text,
                                          "Vurnerability status": self.txvrst.text,
                                          "Comment": self.txcmm.text,
                                          "photo": self.txfnam.text.lower() + ".png",
                                          "$": {'balance': "0.0", 'history': {}},
                                          "fee": self.txfee.text}

        if "weka" in dir(self):  # if hasattr(self,'weka'):
            if "maks" in dir(self):
                dict[self.txfnam.text.lower()]['marks'] = self.maks
            if "dollar" in dir(self):
                dict[self.txfnam.text.lower()]["$"] = self.dollar
            if self.weka != self.txfnam.text.lower():
                Clock.schedule_once(self.captur)
            if dict[self.txfnam.text.lower()] != dict[self.weka]:
                del dict[self.weka]
            # os.rename(DIR+'media'+PTH+'.0'+PTH+'' + self.weka + ".png",DIR+'media'+PTH+'.0'+PTH+'' + self.txfnam.text.lower() + ".png")
            # os.rename(DIR+'media'+PTH+'.0'+PTH+''+self.weka+".png",DIR+'media'+PTH+'.0'+PTH+''+self.txfnam.text.lower()+".png")
            # os.system('mv /home/kali/media'+PTH+'.0'+PTH+'' + self.weka + ".png"+" "+DIR+'media'+PTH+'.0'+PTH+'' + self.txfnam.text.lower() + ".png")

            # RENAME OLD PHOTO TO   (SELF.WEKA.PNG    TO  SELF.TXFNAM.TEXT.LOWER().PNG)

        sfile = open(DIR + 'media' + PTH + '0' + PTH + ANGELS + PTH + '' + self.spcls.text + '.json', 'w')
        json.dump(dict, sfile)
        sfile.close()
        try:
            del self.maks
            del self.dollar
        except:
            pass

        if "weka" in dir(self):
            if self.weka == self.txfnam.text.lower():
                Clock.schedule_once(self.CL_ALL, 3)
                del self.weka
        else:
            Clock.schedule_once(self.CL_ALL, 3)

        Window.unbind(on_keyboard=self.bupdown)
        Clock.schedule_once(self.num_st, 3)

    def dsble(self, xxx):
        try:
            self.remove_widget(self.g_addcla)
        except:
            pass
        self.push = .5
        Clock.schedule_interval(self.pushb, 0.02)

        # file = open(DIR+'media'+PTH+'.0'+PTH+'ANGELS.json', 'r')
        # dict = json.load(file)
        # file.close()

        self.g_addcla = GridLayout(cols=3, size_hint=(.5, .25), pos_hint={'center_x': .65, 'center_y': .5})
        self.g_addcla.add_widget(Label(text="FROM"))
        self.g_addcla.add_widget(Label(text="CHOOSE & DISABLE"))
        self.g_addcla.add_widget(Label(text="DISABLED"))
        self.PS = Spinner(text='P', values=tuple(Clss()))
        self.PS.bind(text=self.CHOOSE)
        self.g_addcla.add_widget(self.PS)
        self.CL = Spinner(text=' ')  # ON_SEARCH CLASS , ADD " " AT END
        self.CL.bind(text=self.CONFIRM)
        self.g_addcla.add_widget(self.CL)

        self.COL = Spinner(text=' ')
        self.COL.bind(text=self.permited)
        self.g_addcla.add_widget(self.COL)

        #################
        self.g_addcla.add_widget(Label(text=""))
        self.g_addcla.add_widget(Label(text=""))
        self.g_addcla.add_widget(Label(text=""))
        self.g_addcla.add_widget(Label(text=""))
        self.g_addcla.add_widget(Label(text=""))
        self.g_addcla.add_widget(Label(text=""))
        self.g_addcla.add_widget(Label(text=""))
        self.g_addcla.add_widget(Button(text="CONFIRM", on_release=self.CONFIRM))

        # dict[self.CL.text + self.COL.text] ={}
        #
        # sfile = open(DIR+'media'+PTH+'.0'+PTH+'ANGELS.json', 'w')
        # json.dump(dict, sfile)
        # sfile.close()

    def permited(self, s, t):
        self.remove_widget(self.idd)
        self.add_widget(self.idd)
        self.idd.background_color = (.5, 0, 0, .9)
        self.adminpasw = TextInput(text=" " * 30 + "Admin password", multiline=False, allow_copy=True,
                                   pos_hint={'center_x': .5, 'center_y': .5}, foreground_color=(0, 0, 0, .5),
                                   size_hint=(.5, .05))
        self.adminpasw.bind(on_touch_up=self.ontouchup)
        self.adminpasw.bind(text=self.PERMI)
        self.add_widget(self.adminpasw)

    def PERMI(self, s, t):
        # file = open(DIR + 'media' + PTH + '0' + PTH + 'cd', 'r')
        # psscd = file.read()[:3]
        # file.close()
        fN = open(DIR + 'media' + PTH + '0' + PTH + 'ACR.json', 'r')
        fina = json.load(fN)
        fN.close()
        admin = dec(fina["xajfk"])
        if t == admin:
            TDAT = open(DIR + 'media' + PTH + '0' + PTH + 'DISABLED.json', 'r')
            DT = json.load(TDAT)
            TDAT.close()

            y = open(DIR + 'media' + PTH + '0' + PTH + ANGELS + PTH + '' + self.PS.text + '.json', 'r')
            mm = json.load(y)
            y.close()

            mm[self.COL.text[:-5]] = DT[self.COL.text]
            FF = open(DIR + 'media' + PTH + '0' + PTH + ANGELS + PTH + '' + self.PS.text + '.json', 'w')
            json.dump(mm, FF)
            FF.close()
            del DT[self.COL.text]
            FF = open(DIR + 'media' + PTH + '0' + PTH + 'DISABLED' + '.json', 'w')
            json.dump(DT, FF)
            FF.close()
            self.remove_widget(self.adminpasw)
            self.remove_widget(self.g_addcla)
            self.remove_widget(self.secgrid)
            self.add_widget(self.secgrid)
            self.idd.background_color = (0, 0, 0, .8)
        else:

            if len(t) == len(admin) + 1:
                self.adminpasw.background_color = (1, .5, 0, .2)
                self.adminpasw.text = ""

    def CONFIRM(self, s, t):
        self.remove_widget(self.idd)
        self.add_widget(self.idd)
        self.idd.background_color = (.5, 0, 0, .9)
        self.adminpasw = TextInput(text=" " * 30 + "Admin password", multiline=False, allow_copy=True,
                                   pos_hint={'center_x': .5, 'center_y': .5}, foreground_color=(0, 0, 0, .5),
                                   size_hint=(.5, .05))
        self.adminpasw.bind(on_touch_up=self.ontouchup)
        self.adminpasw.bind(text=self.cHSEN)
        self.add_widget(self.adminpasw)

    def CHOOSE(self, sp, t):
        TDAT = open(DIR + 'media' + PTH + '0' + PTH + ANGELS + PTH + '' + t + ".json", 'r')
        DT = json.load(TDAT)
        TDAT.close()
        ls = []
        for i in DT.keys():
            ls.append(i)
        self.CL.values = tuple(ls)

        TDAT = open(DIR + 'media' + PTH + '0' + PTH + 'DISABLED.json', 'r')
        DT = json.load(TDAT)
        TDAT.close()
        dsb = []
        for s in DT.keys():
            dsb.append(s)
        self.COL.values = tuple(dsb)

    def cHSEN(self, s, t):
        # file = open(DIR + 'media' + PTH + '0' + PTH + 'cd', 'r')
        # psscd = file.read()[:3]
        # file.close()
        # if t == psscd[:2]:
        fN = open(DIR + 'media' + PTH + '0' + PTH + 'ACR.json', 'r')
        fina = json.load(fN)
        fN.close()
        admin = dec(fina["xajfk"])
        if t == admin:
            TDAT = open(DIR + 'media' + PTH + '0' + PTH + ANGELS + PTH + '' + self.PS.text + ".json", 'r')
            DT = json.load(TDAT)
            TDAT.close()

            TAD = open(DIR + 'media' + PTH + '0' + PTH + 'DISABLED.json', 'r')
            TD = json.load(TAD)
            TAD.close()

            TD[self.CL.text + '/ ' + self.PS.text] = DT[self.CL.text]
            FF = open(DIR + 'media' + PTH + '0' + PTH + 'DISABLED.json', 'w')
            json.dump(TD, FF)
            FF.close()
            del DT[self.CL.text]
            FF = open(DIR + 'media' + PTH + '0' + PTH + ANGELS + PTH + '' + self.PS.text + '.json', 'w')
            json.dump(DT, FF)
            FF.close()
            self.remove_widget(self.adminpasw)
            self.remove_widget(self.g_addcla)
            self.remove_widget(self.secgrid)
            self.add_widget(self.secgrid)
            self.idd.background_color = (0, 0, 0, .8)
        else:

            if len(t) == len(admin) + 1:
                self.adminpasw.background_color = (1, .5, 0, .2)
                self.adminpasw.text = ""

    def shft(self, xxx):
        try:
            self.remove_widget(self.g_addcla)
        except:
            pass
        self.push = .5
        Clock.schedule_interval(self.pushb, 0.02)

        # file = open(DIR+'media'+PTH+'.0'+PTH+'ANGELS.json', 'r')
        # dict = json.load(file)
        # file.close()

        self.g_addcla = GridLayout(cols=3, size_hint=(.5, .25), pos_hint={'center_x': .65, 'center_y': .5})
        self.g_addcla.add_widget(Label(text="FROM :"))
        self.g_addcla.add_widget(Label(text="NAME"))
        self.g_addcla.add_widget(Label(text="STREAM"))
        self.PS = Spinner(text='P', values=tuple(Clss()))
        self.PS.bind(text=self.ON_WORK)#
        self.g_addcla.add_widget(self.PS)
        self.CL = Spinner(text=' ')  # ON_SEARCH CLASS , ADD " " AT END
        self.g_addcla.add_widget(self.CL)

        self.COL = Spinner(text='', values=tuple(Clss()))
        self.COL.bind(text=self.addidd)
        self.g_addcla.add_widget(self.COL)

        #################
        self.g_addcla.add_widget(Label(text=""))
        self.g_addcla.add_widget(Label(text=""))
        self.g_addcla.add_widget(Label(text=""))
        self.g_addcla.add_widget(Label(text=""))
        self.g_addcla.add_widget(Label(text=""))
        self.g_addcla.add_widget(Label(text=""))
        self.g_addcla.add_widget(Label(text=""))
        self.g_addcla.add_widget(Button(text="CONFIRM", on_release=self.CONFIRM))

    def ON_WORK(self, sp, t):
        TDAT = open(DIR + 'media' + PTH + '0' + PTH + ANGELS + PTH + '' + t + ".json", 'r')
        DT = json.load(TDAT)
        TDAT.close()
        ls = []
        for i in DT.keys():
            ls.append(i)
        self.CL.values = tuple(ls)

    def addidd(self, s, t):
        if self.COL == "":
            return
        self.remove_widget(self.idd)
        self.add_widget(self.idd)
        self.idd.background_color = (.5, 0, 0, .9)
        self.adminpasw = TextInput(text=" " * 30 + "Admin password", multiline=False, allow_copy=True,
                                   pos_hint={'center_x': .5, 'center_y': .5}, foreground_color=(0, 0, 0, .5),
                                   size_hint=(.5, .05))
        self.adminpasw.bind(on_touch_up=self.ontouchup)
        self.adminpasw.bind(text=self.WORK)
        self.add_widget(self.adminpasw)


    def WORK(self, s, t):
        # file = open(DIR + 'media' + PTH + '0' + PTH + 'cd', 'r')
        # psscd = file.read()[:3]
        # file.close()

        fN = open(DIR + 'media' + PTH + '0' + PTH + 'ACR.json', 'r')
        fina = json.load(fN)
        fN.close()
        admin = dec(fina["xajfk"])
        if t == admin:

            # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            TDAT = open(DIR + 'media' + PTH + '0' + PTH + ANGELS + PTH + '' + self.PS.text + ".json", 'r')
            DT = json.load(TDAT)
            TDAT.close()

            TAD = open(DIR + 'media' + PTH + '0' + PTH + 'DISABLED.json', 'r')
            TD = json.load(TAD)
            TAD.close()

            TD[self.CL.text + '/ ' + self.PS.text] = DT[self.CL.text]
            FF = open(DIR + 'media' + PTH + '0' + PTH + 'DISABLED.json', 'w')
            json.dump(TD, FF)
            FF.close()
            # del DT[self.CL.text]
            FF = open(DIR + 'media' + PTH + '0' + PTH + ANGELS + PTH + '' + self.PS.text + '.json', 'w')
            json.dump(DT, FF)
            FF.close()
            # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

            TDAT = open(DIR + 'media' + PTH + '0' + PTH + ANGELS + PTH + '' + self.PS.text + '.json', 'r')
            DT = json.load(TDAT)
            TDAT.close()

            if self.PS.text[:3] != self.COL.text[:3] :
                try:
                    del DT[self.CL.text]['marks']
                except:
                    pass

            y = open(DIR + 'media' + PTH + '0' + PTH + ANGELS + PTH + '' + self.COL.text + '.json', 'r')
            mm = json.load(y)
            y.close()

            mm[self.CL.text] = DT[self.CL.text]
            FF = open(DIR + 'media' + PTH + '0' + PTH + ANGELS + PTH + '' + self.COL.text + '.json', 'w')
            json.dump(mm, FF)
            FF.close()
            del DT[self.CL.text]

            FF = open(DIR + 'media' + PTH + '0' + PTH + ANGELS + PTH + '' + self.PS.text + '.json', 'w')
            json.dump(DT, FF)
            FF.close()

            self.remove_widget(self.adminpasw)
            self.remove_widget(self.g_addcla)
            self.remove_widget(self.secgrid)
            self.add_widget(self.secgrid)
            self.idd.background_color = (0, 0, 0, .8)
        else:

            if len(t) == len(admin) + 1:
                self.adminpasw.background_color = (1, .5, 0, .2)
                self.adminpasw.text = ""

    def newcls(self, xxx):
        if lv != 'adm':
            return
        self.push = .5
        Clock.schedule_interval(self.pushb, 0.02)

        # file = open(DIR+'media'+PTH+'.0'+PTH+'ANGELS.json', 'r')
        # dict = json.load(file)
        # file.close()

        self.g_addcla = GridLayout(cols=3, size_hint=(.5, .25), pos_hint={'center_x': .65, 'center_y': .5})
        self.g_addcla.add_widget(Label(text="LEVEL"))
        self.g_addcla.add_widget(Label(text="CLASS"))
        self.g_addcla.add_widget(Label(text="COLUMN"))
        self.PS = Spinner(text='P', values=('N', 'P', 'S'))
        self.PS.bind(text=self.bmt)
        self.g_addcla.add_widget(self.PS)
        self.CL = Spinner(text=' ', values=('1', '2', '3', '4', '5', '6', '7'))  # ON_SEARCH CLASS , ADD " " AT END
        self.g_addcla.add_widget(self.CL)
        self.COL = Spinner(text=' ', values=('A', 'B', 'C', 'D', 'E', 'F', 'G'))
        self.g_addcla.add_widget(self.COL)

        #################
        self.g_addcla.add_widget(Label(text=""))
        self.g_addcla.add_widget(Label(text=""))
        self.g_addcla.add_widget(Label(text=""))
        self.g_addcla.add_widget(Label(text=""))
        self.g_addcla.add_widget(Label(text=""))
        self.g_addcla.add_widget(Label(text=""))
        self.g_addcla.add_widget(Label(text=""))
        self.g_addcla.add_widget(Button(text="CONFIRM", on_release=self.confirm))

    def bmt(self, sp, t):
        if t == "N":
            self.CL.values = ("B", "M", "T")

    def confirm(self, x):
        self.remove_widget(self.idd)
        self.add_widget(self.idd)
        self.idd.background_color = (.5, 0, 0, .9)
        self.adminpasw = TextInput(text=" " * 30 + "Admin password", multiline=False, allow_copy=True,
                                   pos_hint={'center_x': .5, 'center_y': .5}, foreground_color=(0, 0, 0, .5),
                                   size_hint=(.5, .05))
        self.adminpasw.bind(on_touch_up=self.ontouchup)
        self.adminpasw.bind(text=self.texting)
        self.add_widget(self.adminpasw)

    def texting(self, t, tx):
        # file = open(DIR + 'media' + PTH + '0' + PTH + 'cd', 'r')
        # psscd = file.read()
        # file.close()
        fN = open(DIR + 'media' + PTH + '0' + PTH + 'ACR.json', 'r')
        fina = json.load(fN)
        fN.close()
        admin = dec(fina["xajfk"])

        if tx == admin:
            dict = {}
            if os.path.isfile(
                    DIR + 'media' + PTH + '0' + PTH + ANGELS + PTH + '' + self.PS.text + self.CL.text + self.COL.text + '.json'):
                return
            else:
                dict = {}
                if not os.path.isdir(DIR + 'media' + PTH + '0' + PTH + 'ANGELS'):
                    os.mkdir(DIR + 'media' + PTH + '0' + PTH + 'ANGELS')
                sfile = open(
                    DIR + 'media' + PTH + '0' + PTH + ANGELS + PTH + '' + self.PS.text + self.CL.text + self.COL.text + '.json',
                    'w')
                json.dump(dict, sfile)
                sfile.close()
            self.remove_widget(self.adminpasw)
            self.remove_widget(self.g_addcla)
            self.remove_widget(self.secgrid)
            self.add_widget(self.secgrid)
            self.idd.background_color = (0, 0, 0, .8)
        else:

            if len(tx) == len(admin) + 1:
                self.adminpasw.background_color = (1, .5, 0, .2)
                self.adminpasw.text = ""

    def pushb(self, c):
        if self.push <= .15:
            self.push = self.push
            self.add_widget(self.g_addcla)
            Clock.unschedule(self.pushb)
        else:
            self.push -= .02
            self.secgrid.pos_hint = {'center_x': self.push, 'center_y': .5}
            print("moving")

    def ontouchup(self, x, y):
        self.adminpasw.text = ""
        self.adminpasw.password = True

    def sontouchup(self, x, y):
        self.schtx.text = ""
        if self.schtx.text=="" :
            self.autobind('self.SC')
        else:
            self.autobind('self.scv')



    def back(self, ev):
        if self.b_c >= .8:
            self.b_c = self.b_c
            Clock.unschedule(self.back)
        else:
            self.b_c += .01
            self.idd.background_color = (0, 0, 0, self.b_c)

    def home(self, x):
        # self.remove_widget(self.secgrid)
        try:
            self.remove_widget(self.adminpasw)
        except:
            pass
        try:
            self.remove_widget(self.SCRL)
        except:
            pass

        try:
            self.remove_widget(self.prcol)
        except:
            pass
        try:
            self.remove_widget(self.delcol)
        except:
            pass

        try:
            self.remove_widget(self.status)
        except:
            pass

        try:
            self.remove_widget(self.adcol)
        except:
            pass

        try:
            self.remove_widget(self.SLTD)
        except:
            pass

        try:
            self.remove_widget(self.pwd)
        except:
            pass
        try:
            Clock.unschedule(self.trig)
        except:
            pass

        try:
            self.remove_widget(self.perc)
        except:
            pass

        self.remove_widget(self.idd)

        try:
            self.remove_widget(self.grest)
        except:
            pass

        try:
            self.remove_widget(self.gsolution)
        except:
            pass

        try:
            self.remove_widget(self.bkgr)
        except:
            pass

        try:
            self.remove_widget(self.behind)
        except:
            pass

        try:
            self.remove_widget(self.Chois)
        except:
            pass
        try:
            self.remove_widget(self.PrI)
        except:
            pass
        try:
            self.remove_widget(self.imprimer)
        except:
            pass
        try:
            self.remove_widget(self.print_report)
        except:
            pass
        try:
            self.remove_widget(self.notg)
        except:
            pass
        try:
            self.remove_widget(self.ps_sv2)
        except:
            pass

        try:
            self.remove_widget(self.pp)
        except:
            pass

        try:
            self.remove_widget(self.gG)
        except:
            pass
        try:
            self.remove_widget(self.ps_sv)
        except:
            pass
        try:
            self.remove_widget(self.snap)
        except:
            pass
        try:
            self.remove_widget(self.CL)
        except:
            pass
        try:
            self.remove_widget(self.NM)
        except:
            pass

        try:
            self.remove_widget(self.BGSV)
        except:
            pass
        try:
            self.remove_widget(self.BIG13)
        except:
            pass
        try:
            self.remove_widget(self.BIG47)
        except:
            pass

        try:
            self.remove_widget(self.goback)
        except:
            pass

        try:
            self.remove_widget(self.DDO)
        except:
            pass

        try:
            self.remove_widget(self.nyu)
        except:
            pass

        try:
            self.remove_widget(self.gHRR)
        except:
            pass

        try:
            self.remove_widget(self.gt)
        except:
            pass

        try:
            self.remove_widget(self.gVIEW)
        except:
            pass

        try:
            self.remove_widget(self.verify)
        except:
            pass

        try:
            self.remove_widget(self.biospinner)
        except:
            pass

        try:
            self.remove_widget(self.Lcourse)
        except:
            pass

        try:
            self.remove_widget(self.gCour)
        except:
            pass

        try:
            self.remove_widget(self.Savb)
        except:
            pass

        try:
            self.remove_widget(self.gadt)
        except:
            pass

        try:
            self.remove_widget(self.scrolltable)
        except:
            pass

        try:
            self.remove_widget(self.TOD)
        except:
            pass
        try:
            self.remove_widget(self.gaside)
        except:
            pass
        try:
            self.remove_widget(self.bckg)
            self.remove_widget(self.dbckg)
        except:
            pass

        try:
            self.remove_widget(self.Gpay)
        except:
            pass
        try:
            self.remove_widget(self.exitp)
        except:
            pass
        try:
            self.remove_widget(self.g_addcla)
        except:
            pass
        try:
            self.remove_widget(self.secgrid)
        except:
            pass
        try:
            self.remove_widget(self.schtx)
        except:
            pass
        try:
            self.remove_widget(self.scv)
        except:
            pass
        try:
            self.remove_widget(self.gnot)
        except:
            pass
        try:
            self.remove_widget(self.bckbut)
        except:
            pass
        try:
            self.remove_widget(self.scrll)
        except:
            pass
        try:
            self.remove_widget(self.gridl)
        except:
            pass

    def Goback(self, d):
        if not self.txfnam.text:
            self.remove_widget(self.idd)
            self.remove_widget(self.bigformgrid)
            Window.unbind(on_keyboard=self.bupdown)

    def Viewcleaner(self, x):

        try:
            self.remove_widget(self.SCRL)
        except:
            pass

        try:
            self.remove_widget(self.adcol)
        except:
            pass
        try:
            self.remove_widget(self.prcol)
        except:
            pass

        try:
            self.remove_widget(self.SLTD)
        except:
            pass

        try:
            self.remove_widget(self.delcol)
        except:
            pass

        try:
            self.remove_widget(self.status)
        except:
            pass

        try:
            self.remove_widget(self.Chois)
        except:
            pass
        try:
            self.remove_widget(self.print_report)
        except:
            pass
        try:
            self.remove_widget(self.gG)
        except:
            pass
        try:
            self.remove_widget(self.ps_sv)
        except:
            pass

        try:
            self.remove_widget(self.scrll)
        except:
            pass
        try:
            self.remove_widget(self.CL)
        except:
            pass
        try:
            self.remove_widget(self.NM)
        except:
            pass
        try:
            self.remove_widget(self.BGSV)
        except:
            pass
        try:
            self.remove_widget(self.BIG13)
        except:
            pass
        try:
            self.remove_widget(self.BIG47)
        except:
            pass
        try:
            self.remove_widget(self.v_class)
        except:
            pass

        try:
            self.remove_widget(self.sdetail)
        except:
            pass

        try:
            self.remove_widget(self.sssv)
        except:
            pass

        try:
            self.remove_widget(self.SG)
        except:
            pass

        try:
            self.remove_widget(self.S_class)
        except:
            pass

        try:
            self.remove_widget(self.SSdetail)
        except:
            pass

        try:
            self.remove_widget(self.SSSv)
        except:
            pass

        try:
            self.remove_widget(self.SSGG)
        except:
            pass

        try:
            self.remove_widget(self.dtS_class)
        except:
            pass

        try:
            self.remove_widget(self.dtSSdetail)
        except:
            pass

        try:
            self.remove_widget(self.dtSSSv)
        except:
            pass

        try:
            self.remove_widget(self.dtSSGG)
        except:
            pass

        try:
            self.remove_widget(self.notg)
        except:
            pass
        try:
            self.remove_widget(self.ps_sv2)
        except:
            pass

        try:
            self.remove_widget(self.pp)
        except:
            pass
        try:
            self.remove_widget(self.gridl)
        except:
            pass

    def cleaner(self, x):
        try:
            self.remove_widget(self.adcol)
        except:
            pass
        try:
            self.remove_widget(self.prcol)
        except:
            pass


        try:
            self.remove_widget(self.delcol)
        except:
            pass
        try:
            self.remove_widget(self.SCRL)
        except:
            pass
        try:
            self.remove_widget(self.Chois)
        except:
            pass
        try:
            self.remove_widget(self.PrI)
        except:
            pass
        try:
            self.remove_widget(self.print_report)
        except:
            pass

        try:
            self.remove_widget(self.DDO)
        except:
            pass
        try:
            self.remove_widget(self.snap)
        except:
            pass

        try:
            self.remove_widget(self.nyu)
        except:
            pass

        try:
            self.remove_widget(self.gHRR)
        except:
            pass

        try:
            self.remove_widget(self.gVIEW)
        except:
            pass

        try:
            self.remove_widget(self.verify)
        except:
            pass

        try:
            self.remove_widget(self.biospinner)
        except:
            pass

        try:
            self.remove_widget(self.Lcourse)
        except:
            pass

        try:
            self.remove_widget(self.gCour)
        except:
            pass

        try:
            self.remove_widget(self.Savb)
        except:
            pass

        try:
            self.remove_widget(self.gadt)
        except:
            pass

        try:
            self.remove_widget(self.scrolltable)
        except:
            pass

        try:
            self.remove_widget(self.TOD)
        except:
            pass
        try:
            self.remove_widget(self.imprimer)
        except:
            pass
        try:
            self.remove_widget(self.gridl)
        except:
            pass

    def PUSH(self, event):
        self.manager.current = "login"



class SMSApp(App):
    def __init__(self, **kwargs):
        super(SMSApp, self).__init__(**kwargs)

        # print('window',Window.size)

    def build(self):
        sm = ScreenManager(transition=FallOutTransition(duration=.1))
        sm.add_widget(login(name="login"))
        sm.add_widget(Angels(name="angels"))
        return sm

SMSApp().run()
