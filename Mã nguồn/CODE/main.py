from kivy.factory import Factory
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.bottomsheet import MDCustomBottomSheet
from kivymd.uix.card import MDCard
from kivymd.uix.screen import MDScreen
from collections import Counter
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.datatables import MDDataTable
tk="abc"
mk="123"
tien=0
danhsachmon=[]
danhsachbook=""
sobancucbo=0
monancucbo=""
chotdon={}
class MainApp(MDApp):
    def show_custom_bottom_sheet(self,image,price,rate):
        bottom_sheet=Factory.ContentCustomSheet()
        bottom_sheet.rate=rate
        bottom_sheet.image=image
        bottom_sheet.price=price
        self.custom_sheet = MDCustomBottomSheet(screen=bottom_sheet)
        self.custom_sheet.open()
    def dathang(self,price,rate):
        global tien
        global danhsachmon
        tien=tien+int(price)
        danhsachmon.append(rate)
    def hienthibangthanhtoan(self):
        bottom_sheet = Factory.bangthanhtoan()
        self.custom_sheet = MDCustomBottomSheet(screen=bottom_sheet)
        self.custom_sheet.open()
    def laydulieudangnhap(self,danhsach,tongtien,doan):
        global tien
        global danhsachmon
        global danhsachbook
        global monancucbo
        print(danhsachmon)
        test = {}
        tongtien.text=str(tien)+" Ngìn đồng"
        danhsach.text = "Bàn Số: "+str(sobancucbo)
        test.update(Counter(danhsachmon))
        print(test)
        if len(test) == 0:
            doan.text="Bạn chưa đặt hàng"
        else:
            danhsachbook=""
            for i in range(len(test)):
                a = list(test.items())
                danhsachbook=danhsachbook+str(a[i][0])+" - Số lượng " + str(a[i][1]) +"   "
            doan.text = danhsachbook
            monancucbo = danhsachbook
    def thanhtoan(self):
        global tien
        global sobancucbo
        global monancucbo
        global chotdon
        global danhsachmon
        chotdon.update({sobancucbo:Counter(danhsachmon)})
        print(chotdon)
    def dangxuat(self):
        global tien
        global monancucbo
        global danhsachmon
        tien = 0
        danhsachmon = []
        monancucbo = ""
    def dangnhap(self,acc,paw):
        if acc.text==tk and paw.text==mk:
            print("Đúng mật khẩu")
            return "admin"
        else:
            return "main"
    def themsoban(self, soban):
        global sobancucbo
        if  int("0"+soban.text) in range(1,10):
            sobancucbo=int("0"+soban.text)
            return "login"
        else:
            return "main"
    def endgame(self,listbep):
        global chotdon
        listbep.text = str(chotdon)

    def build(self):
        self.title = 'Ứng dụng dặt món ăn'
        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_file("main.kv"))
        screen_manager.add_widget(Builder.load_file("login.kv"))
        screen_manager.add_widget(Builder.load_file("Dangnhap.kv"))
        screen_manager.add_widget(Builder.load_file("chonban.kv"))
        screen_manager.add_widget(Builder.load_file("taikhoan.kv"))
        screen_manager.add_widget(Builder.load_file("Giaodiendathang.kv"))
        screen_manager.add_widget(Builder.load_file("admin.kv"))
        return screen_manager
MainApp().run()