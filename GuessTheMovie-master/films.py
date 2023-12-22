import sys 
import random
import pygame



from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout,QMainWindow
from PyQt5.QtWidgets import QLabel, QLineEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize

from sys import stdin, exit as sys_exit

class Change(QMainWindow):
	def __init__(self):
		super().__init__()
		self.initUI()
		self.count_calls()

	def initUI(self):
#Фон -------------------------------------------------------		

		self.window = QWidget()
		# self.count = 0

		self.fon = QPushButton('', self)
		self.fon.setIcon(QIcon('FON	.jpg'))
		self.fon.setGeometry(0,0,680,650)
		self.fon.setIconSize(QSize(680,650))

#Фон---------------------------------------------------------
#Главный экран ----------------------------------------------
		drid = QGridLayout()
		drid.setSpacing(20)
		self.record = QWidget()
		self.count = 0
		# self.count = QLabel('0')
		# drid.addWidget(self.count,0,1)

		self.Big = QWidget()
		self.fon = QPushButton('', self.Big)
		self.fon.setIcon(QIcon('main.png'))
		self.fon.setGeometry(0,0,680,650)
		self.fon.setIconSize(QSize(680,650))

		self.button_2 = QPushButton('', self.Big)
		self.button_2.setIcon(QIcon("Exit.png"))
		self.button_2.setFlat(True)
		self.button_2.setGeometry(225, 550, 250, 80)
		self.button_2.setIconSize(QSize(250, 200))


		self.button_0 = QPushButton('', self.Big)
		self.button_0.setIcon(QIcon("regis.png"))
		self.button_0.setFlat(True)
		self.button_0.setGeometry(225, 450, 250, 80)
		self.button_0.setIconSize(QSize(250, 80))



		self.button_1 = QPushButton('', self.Big)
		self.button_1.setIcon(QIcon("vxod.png"))
		self.button_1.setFlat(True)
		self.button_1.setGeometry(225, 350, 250, 80)
		self.button_1.setIconSize(QSize(250, 80))

		self.button_3 = QPushButton('', self.Big)
		self.button_3.setIcon(QIcon("settings.png"))
		self.button_3.setFlat(True)
		self.button_3.setGeometry(10, 550, 100, 80)
		self.button_3.setIconSize(QSize(80, 80))

		self.button_1.clicked.connect(self.openiuns)
		self.button_0.clicked.connect(self.regist)
		self.button_2.clicked.connect(QApplication.instance().quit)
		self.button_3.clicked.connect(self.sett)



#Настройки-------------------------------------------------
		self.settings = QWidget()

		self.fon = QPushButton('', self.settings)
		self.fon.setIcon(QIcon('FON_SETTINGS (2).jpg'))
		self.fon.setGeometry(0,0,680,650)
		self.fon.setIconSize(QSize(680,650))

		self.button_light = QPushButton('', self.settings)
		self.button_light.setIcon(QIcon("svetlaya (1).png"))
		self.button_light.setIconSize(QSize(160, 60))
		self.button_light.setFlat(True)
		self.button_light.move(400, 300)

		self.button_back = QPushButton('', self.settings)
		self.button_back.setIcon(QIcon("vxo.png"))
		self.button_back.setIconSize(QSize(160, 60))
		self.button_back.setFlat(True)
		self.button_back.move(10,30)

		self.button_black = QPushButton('', self.settings)
		self.button_black.setIcon(QIcon("temnaya (1).png"))
		self.button_black.setIconSize(QSize(160, 60))
		self.button_black.setFlat(True)
		self.button_black.move(100, 300)

		self.button_back.clicked.connect(self.home)
		self.button_black.clicked.connect(self.dark_th)
		self.button_light.clicked.connect(self.light_th)



#Вход -------------------------------------------------------
		self.vxod = QWidget()

		self.fon = QPushButton('', self.vxod)
		self.fon.setIcon(QIcon('max1.jpg'))
		self.fon.setGeometry(0,0,680,650)
		self.fon.setIconSize(QSize(680,650))

		self.loginText = QLabel('Введите логин', self.vxod)
		self.loginText.move(400, 200)

		self.loginInput = QLineEdit(self.vxod)
		self.loginInput.move(400, 220)

		self.password = QLabel('Введите пароль', self.vxod)
		self.password.move(400, 260)

		self.passwordInput = QLineEdit(self.vxod)
		self.passwordInput.move(400, 280)

		self.button = QPushButton('', self.vxod)
		self.button.setIcon(QIcon("vxod2.png"))
		self.button.setIconSize(QSize(120, 40))
		self.button.setFlat(True)
		self.button.move(390, 320)

		self.button_back = QPushButton('', self.vxod)
		self.button_back.setIcon(QIcon("vxo.png"))
		self.button_back.setIconSize(QSize(120, 40))
		self.button_back.setFlat(True)
		self.button_back.move(390, 370)

		self.button.clicked.connect(self.sendForm)
		self.button_back.clicked.connect(self.home)

	

#Вход --------------------------------------------------------

		self.reg = QWidget()

		self.fon = QPushButton('', self.reg)
		self.fon.setIcon(QIcon('max2.jpg'))
		self.fon.setGeometry(0,0,680,650)
		self.fon.setIconSize(QSize(680,650))

		self.loginText1 = QLabel('Введите логин', self.reg)
		self.loginText1.move(400, 200)

		self.loginInput1 = QLineEdit(self.reg)
		self.loginInput1.move(400, 220)

		self.password1 = QLabel('Введите пароль', self.reg)
		self.password1.move(400, 260)

		self.passwordInput1 = QLineEdit(self.reg)
		self.passwordInput1.move(400, 280)


		self.button_back = QPushButton('', self.reg)
		self.button_back.setIcon(QIcon("vxo.png"))
		self.button_back.setIconSize(QSize(120, 40))
		self.button_back.setFlat(True)
		self.button_back.move(390, 370)

		self.button = QPushButton('', self.reg)
		self.button.setIcon(QIcon("register.png"))
		self.button.setIconSize(QSize(120, 40))
		self.button.setFlat(True)
		self.button.move(390, 320)


		self.button.clicked.connect(self.regi)
		self.button_back.clicked.connect(self.home)




#1 Игра ------------------------------------------------------	



		self.fon = QPushButton('', self.window)
		self.fon.setIcon(QIcon('but.png'))
		self.fon.setGeometry(0,350,680,320)
		self.fon.setIconSize(QSize(1024,678))

		self.button_0 = QPushButton('', self.window)
		self.button_0.setIcon(QIcon("kino.png"))
		self.button_0.setGeometry(0, 00, 680,400)
		self.button_0.setIconSize(QSize(680, 400))
		self.button_0.setFlat(True)
		self.button_0.clicked.connect(self.image_izmena_1)

		self.button_1 = QPushButton('', self.window)
		self.button_1.setIcon(QIcon("1game.png"))
		self.button_1.setFlat(True)
		self.button_1.setGeometry(370, 420, 250, 80)
		self.button_1.setIconSize(QSize(250, 80))
		self.button_1.clicked.connect(self.pravno)
		self.button_1.clicked.connect(self.perehod)
		
		self.button_2 = QPushButton('', self.window)
		self.button_2.setIcon(QIcon("fals_one.png"))
		self.button_2.setGeometry(370, 520, 250, 80)
		self.button_2.setIconSize(QSize(250, 80))
		self.button_2.setFlat(True)
		self.button_2.clicked.connect(self.nepravelno)
		self.button_2.clicked.connect(self.izmena)


		self.button_3 = QPushButton('', self.window)
		self.button_3.setIcon(QIcon("fals_two.png"))
		self.button_3.setGeometry(50, 520, 250, 80)
		self.button_3.setIconSize(QSize(250, 80))
		self.button_3.setFlat(True)
		self.button_3.clicked.connect(self.izmena)
		self.button_3.clicked.connect(self.nepravelno)

		self.button_4 = QPushButton('', self.window)
		self.button_4.setIcon(QIcon('fals3.png'))
		self.button_4.setGeometry(50, 420, 250, 80)
		self.button_4.setIconSize(QSize(250, 80)) 
		self.button_4.setFlat(True)
		self.button_4.clicked.connect(self.izmena)
		self.button_4.clicked.connect(self.nepravelno)	
		
		self.setCentralWidget(self.Big)
#1 Игра ------------------------------------------------------------------------		
#2 Игра ------------------------------------------------------------------------


		self.window2 = QWidget()

		self.fon = QPushButton('', self.window2)
		self.fon.setIcon(QIcon('but.png'))
		self.fon.setGeometry(0,350,680,320)
		self.fon.setIconSize(QSize(1024,678))

		self.button_0 = QPushButton('', self.window2)
		self.button_0.setIcon(QIcon('grch.png'))
		self.button_0.setGeometry(0, 00, 680,400)
		self.button_0.setIconSize(QSize(680, 400))
		self.button_0.setFlat(True)
		self.button_0.clicked.connect(self.image_izmena_2)

		self.button_1 = QPushButton('', self.window2)
		self.button_1.setIcon(QIcon("button_istori.png"))
		self.button_1.setFlat(True)
		self.button_1.setGeometry(370, 420, 250, 80)
		self.button_1.setIconSize(QSize(250, 80))
		self.button_1.clicked.connect(self.izmena)
		self.button_1.clicked.connect(self.nepravelno)

		self.button_2 = QPushButton('', self.window2)
		self.button_2.setIcon(QIcon("chort.png"))
		self.button_2.setGeometry(370, 520, 250, 80)
		self.button_2.setIconSize(QSize(250, 80))
		self.button_2.setFlat(True)
		self.button_2.clicked.connect(self.izmena)
		self.button_2.clicked.connect(self.nepravelno)

		self.button_3 = QPushButton('', self.window2)
		self.button_3.setIcon(QIcon("fals3.png"))
		self.button_3.setGeometry(50, 520, 250, 80)
		self.button_3.setIconSize(QSize(250, 80))
		self.button_3.setFlat(True)
		self.button_3.clicked.connect(self.izmena)
		self.button_3.clicked.connect(self.nepravelno)

		self.button_4 = QPushButton('', self.window2)
		self.button_4.setIcon(QIcon('fals_two.png'))
		self.button_4.setGeometry(50, 420, 250, 80)
		self.button_4.setIconSize(QSize(250, 80))
		self.button_4.setFlat(True)
		self.button_4.clicked.connect(self.perehod2)
		self.button_4.clicked.connect(self.pravno)

	


#2 Игра -----------------------------------------------------------------------------		
#3 Game -----------------------------------------------------------------------------
		self.window3 = QWidget()
		self.fon = QPushButton('', self.window3)
		self.fon.setIcon(QIcon('but.png'))
		self.fon.setGeometry(0,350,680,320)
		self.fon.setIconSize(QSize(1024,678))
		
		self.button_0 = QPushButton('', self.window3)
		self.button_0.setIcon(QIcon('peopl.png'))
		self.button_0.setGeometry(0, 00, 680,400)
		self.button_0.setIconSize(QSize(680, 400))
		self.button_0.setFlat(True)
		self.button_0.clicked.connect(self.image_izmena_3)
		

		self.button_1 = QPushButton('', self.window3)
		self.button_1.setIcon(QIcon("mstiteli.png"))
		self.button_1.setFlat(True)
		self.button_1.setGeometry(370, 420, 250, 80)
		self.button_1.setIconSize(QSize(250, 80))
		self.button_1.clicked.connect(self.izmena)
		self.button_1.clicked.connect(self.nepravelno)

		self.button_2 = QPushButton('', self.window3)
		self.button_2.setIcon(QIcon("piople_shelezo.png"))
		self.button_2.setGeometry(370, 520, 250, 80)
		self.button_2.setIconSize(QSize(250, 80))
		self.button_2.setFlat(True)
		self.button_2.clicked.connect(self.izmena)
		self.button_2.clicked.connect(self.nepravelno)


		self.button_3 = QPushButton('', self.window3)
		self.button_3.setIcon(QIcon("fals_one"))
		self.button_3.setGeometry(50, 520, 250, 80)
		self.button_3.setIconSize(QSize(250, 80))
		self.button_3.setFlat(True)
		self.button_3.clicked.connect(self.izmena)
		self.button_3.clicked.connect(self.nepravelno)


		self.button_4 = QPushButton('', self.window3)
		self.button_4.setIcon(QIcon('fals3'))
		self.button_4.setGeometry(50, 420, 250, 80)
		self.button_4.setIconSize(QSize(250, 80))
		self.button_4.setFlat(True)
		self.button_4.clicked.connect(self.perehod3)
		self.button_4.clicked.connect(self.pravno)

#------------------------------------------------------------------------------
		self.window4 = QWidget()
		self.fon = QPushButton('', self.window4)
		self.fon.setIcon(QIcon('but.png'))
		self.fon.setGeometry(0,350,680,320)
		self.fon.setIconSize(QSize(1024,678))

		self.button_0 = QPushButton('', self.window4)
		self.button_0.setIcon(QIcon('xacker.png'))
		self.button_0.setGeometry(0, 00, 680,400)
		self.button_0.setIconSize(QSize(680, 400))
		self.button_0.setFlat(True)
		self.button_0.clicked.connect(self.image_izmena_4)

		self.button_1 = QPushButton('', self.window4)
		self.button_1.setIcon(QIcon("button_led.png"))
		self.button_1.setFlat(True)
		self.button_1.setGeometry(370, 420, 250, 80)
		self.button_1.setIconSize(QSize(250, 80))
		self.button_1.clicked.connect(self.izmena)
		self.button_1.clicked.connect(self.nepravelno)

		self.button_2 = QPushButton('', self.window4)
		self.button_2.setIcon(QIcon("button_xacker.png"))
		self.button_2.setGeometry(370, 520, 250, 80)
		self.button_2.setIconSize(QSize(250, 80))
		self.button_2.setFlat(True)
		self.button_2.clicked.connect(self.perehod4)
		self.button_2.clicked.connect(self.pravno)

		self.button_3 = QPushButton('', self.window4)
		self.button_3.setIcon(QIcon("brotvey.png"))
		self.button_3.setGeometry(50, 520, 250, 80)
		self.button_3.setIconSize(QSize(250, 80))
		self.button_3.setFlat(True)
		self.button_3.clicked.connect(self.izmena)
		self.button_3.clicked.connect(self.nepravelno)

		self.button_4 = QPushButton('', self.window4)
		self.button_4.setIcon(QIcon('two_follows.png'))
		self.button_4.setGeometry(50, 420, 250, 80)
		self.button_4.setIconSize(QSize(250, 80))
		self.button_4.setFlat(True)
		self.button_4.clicked.connect(self.izmena)
		self.button_4.clicked.connect(self.nepravelno)
#------------------------------------------------------------------

		self.window5 = QWidget()
		self.fon = QPushButton('', self.window5)
		self.fon.setIcon(QIcon('but.png'))
		self.fon.setGeometry(0,350,680,320)
		self.fon.setIconSize(QSize(1024,678))
		
		self.button_0 = QPushButton('', self.window5)
		self.button_0.setIcon(QIcon('flash.png'))
		self.button_0.setGeometry(0, 00, 680,400)
		self.button_0.setIconSize(QSize(680, 400))
		self.button_0.setFlat(True)
		self.button_0.clicked.connect(self.image_izmena_5)


		self.button_1 = QPushButton('', self.window5)
		self.button_1.setIcon(QIcon("speed.png"))
		self.button_1.setFlat(True)
		self.button_1.setGeometry(370, 420, 250, 80)
		self.button_1.setIconSize(QSize(250, 80))
		self.button_1.clicked.connect(self.izmena)
		self.button_1.clicked.connect(self.nepravelno)


		self.button_2 = QPushButton('', self.window5)
		self.button_2.setIcon(QIcon("okoni.png"))
		self.button_2.setGeometry(370, 520, 250, 80)
		self.button_2.setIconSize(QSize(250, 80))
		self.button_2.setFlat(True)
		self.button_2.clicked.connect(self.izmena)
		self.button_2.clicked.connect(self.nepravelno)

		self.button_3 = QPushButton('', self.window5)
		self.button_3.setIcon(QIcon("button_flesh.png"))
		self.button_3.setGeometry(50, 520, 250, 80)
		self.button_3.setIconSize(QSize(250, 80))
		self.button_3.setFlat(True)
		self.button_3.clicked.connect(self.perehod5)
		self.button_3.clicked.connect(self.pravno)	


		self.button_4 = QPushButton('', self.window5)
		self.button_4.setIcon(QIcon('Molnia.png'))
		self.button_4.setGeometry(50, 420, 250, 80)
		self.button_4.setIconSize(QSize(250, 80))
		self.button_4.setFlat(True)
		self.button_4.clicked.connect(self.izmena)
		self.button_4.clicked.connect(self.nepravelno)
	
#--------------------------------------------------------------------------------------------
		self.window6 = QWidget()
		self.fon = QPushButton('', self.window6)
		self.fon.setIcon(QIcon('but.png'))
		self.fon.setGeometry(0,350,680,320)
		self.fon.setIconSize(QSize(1024,678))
		
		self.button_0 = QPushButton('', self.window6)
		self.button_0.setIcon(QIcon('strela.png'))
		self.button_0.setGeometry(0, 00, 680,400)
		self.button_0.setIconSize(QSize(680, 400))
		self.button_0.setFlat(True)

		self.button_1 = QPushButton('', self.window6)
		self.button_1.setIcon(QIcon("golodnie_game.png"))
		self.button_1.setFlat(True)
		self.button_1.setGeometry(370, 420, 250, 80)
		self.button_1.setIconSize(QSize(250, 80))
		self.button_1.clicked.connect(self.izmena)
		self.button_1.clicked.connect(self.nepravelno)


		self.button_2 = QPushButton('', self.window6)
		self.button_2.setIcon(QIcon("debil.png"))
		self.button_2.setGeometry(370, 520, 250, 80)
		self.button_2.setIconSize(QSize(250, 80))
		self.button_2.setFlat(True)
		self.button_2.clicked.connect(self.izmena)
		self.button_2.clicked.connect(self.nepravelno)



		self.button_3 = QPushButton('', self.window6)
		self.button_3.setIcon(QIcon("strelki.png"))
		self.button_3.setGeometry(50, 520, 250, 80)
		self.button_3.setIconSize(QSize(250, 80))
		self.button_3.setFlat(True)
		self.button_3.clicked.connect(self.izmena)
		self.button_3.clicked.connect(self.nepravelno)


		self.button_4 = QPushButton('', self.window6)
		self.button_4.setIcon(QIcon('button_streka.png'))
		self.button_4.setGeometry(50, 420, 250, 80)
		self.button_4.setIconSize(QSize(250, 80))
		self.button_4.setFlat(True)
		self.button_4.clicked.connect(self.perehod6)
		self.button_4.clicked.connect(self.pravno)
#--------------------------------------------------------------------------------

		self.window7 = QWidget()
		self.fon = QPushButton('', self.window7)
		self.fon.setIcon(QIcon('but.png'))
		self.fon.setGeometry(0,350,680,320)
		self.fon.setIconSize(QSize(1024,678))
		
		self.button_0 = QPushButton('', self.window7)
		self.button_0.setIcon(QIcon('ono.png'))
		self.button_0.setGeometry(0, 00, 680,400)
		self.button_0.setIconSize(QSize(680, 400))
		self.button_0.setFlat(True)

		self.button_1 = QPushButton('', self.window7)
		self.button_1.setIcon(QIcon("kloun.png"))
		self.button_1.setFlat(True)
		self.button_1.setGeometry(370, 420, 250, 80)
		self.button_1.setIconSize(QSize(250, 80))
		self.button_1.clicked.connect(self.izmena)
		self.button_1.clicked.connect(self.nepravelno)

		self.button_2 = QPushButton('', self.window7)
		self.button_2.setIcon(QIcon("button_ono.png"))
		self.button_2.setGeometry(370, 520, 250, 80)
		self.button_2.setIconSize(QSize(250, 80))
		self.button_2.setFlat(True)
		self.button_2.clicked.connect(self.perehod7)
		self.button_2.clicked.connect(self.pravno)


		self.button_3 = QPushButton('', self.window7)
		self.button_3.setIcon(QIcon("pila.png"))
		self.button_3.setGeometry(50, 520, 250, 80)
		self.button_3.setIconSize(QSize(250, 80))
		self.button_3.setFlat(True)
		self.button_3.clicked.connect(self.izmena)
		self.button_3.clicked.connect(self.nepravelno)

		self.button_4 = QPushButton('', self.window7)
		self.button_4.setIcon(QIcon('Prizrak.png'))
		self.button_4.setGeometry(50, 420, 250, 80)
		self.button_4.setIconSize(QSize(250, 80))
		self.button_4.setFlat(True)
		self.button_4.clicked.connect(self.izmena)
		self.button_4.clicked.connect(self.nepravelno)
#--------------------------------------------------------------------------------------------
		self.window8 = QWidget()
		self.fon = QPushButton('', self.window8)
		self.fon.setIcon(QIcon('but.png'))
		self.fon.setGeometry(0,350,680,320)
		self.fon.setIconSize(QSize(1024,678))
		
		self.button_0 = QPushButton('', self.window8)
		self.button_0.setIcon(QIcon('Big_v.png'))
		self.button_0.setGeometry(0, 00, 680,400)
		self.button_0.setIconSize(QSize(680, 400))
		self.button_0.setFlat(True)

		self.button_1 = QPushButton('', self.window8)
		self.button_1.setIcon(QIcon("staric.png"))
		self.button_1.setFlat(True)
		self.button_1.setGeometry(370, 420, 250, 80)
		self.button_1.setIconSize(QSize(250, 80))
		self.button_1.clicked.connect(self.izmena)
		self.button_1.clicked.connect(self.nepravelno)

		self.button_2 = QPushButton('', self.window8)
		self.button_2.setIcon(QIcon("Chudo.png"))
		self.button_2.setGeometry(370, 520, 250, 80)
		self.button_2.setIconSize(QSize(250, 80))
		self.button_2.setFlat(True)
		self.button_2.clicked.connect(self.izmena)
		self.button_2.clicked.connect(self.nepravelno)

		self.button_3 = QPushButton('', self.window8)
		self.button_3.setIcon(QIcon("button_bigg.png"))
		self.button_3.setGeometry(50, 520, 250, 80)
		self.button_3.setIconSize(QSize(250, 80))
		self.button_3.setFlat(True)
		self.button_3.clicked.connect(self.perehod8)
		self.button_3.clicked.connect(self.pravno)


		self.button_4 = QPushButton('', self.window8)
		self.button_4.setIcon(QIcon('XZ.png'))
		self.button_4.setGeometry(50, 420, 250, 80)
		self.button_4.setIconSize(QSize(250, 80))
		self.button_4.setFlat(True)
		self.button_4.clicked.connect(self.izmena)
		self.button_4.clicked.connect(self.nepravelno)
#--------------------------------------------------------------------------------------------
		self.window9 = QWidget()
		self.fon = QPushButton('', self.window9)
		self.fon.setIcon(QIcon('but.png'))
		self.fon.setGeometry(0,350,680,320)
		self.fon.setIconSize(QSize(1024,678))
		
		self.button_0 = QPushButton('', self.window9)
		self.button_0.setIcon(QIcon('maska.png'))
		self.button_0.setGeometry(0, 00, 680,400)
		self.button_0.setIconSize(QSize(680, 400))
		self.button_0.setFlat(True)

		self.button_1 = QPushButton('', self.window9)
		self.button_1.setIcon(QIcon("button_masak.png"))
		self.button_1.setFlat(True)
		self.button_1.setGeometry(370, 420, 250, 80)
		self.button_1.setIconSize(QSize(250, 80))
		self.button_1.clicked.connect(self.perehod9)
		self.button_1.clicked.connect(self.pravno)


		self.button_2 = QPushButton('', self.window9)
		self.button_2.setIcon(QIcon("fonar.png"))
		self.button_2.setGeometry(370, 520, 250, 80)
		self.button_2.setIconSize(QSize(250, 80))
		self.button_2.setFlat(True)
		self.button_2.clicked.connect(self.izmena)
		self.button_2.clicked.connect(self.nepravelno)


		self.button_3 = QPushButton('', self.window9)
		self.button_3.setIcon(QIcon("chertic.png"))
		self.button_3.setGeometry(50, 520, 250, 80)
		self.button_3.setIconSize(QSize(250, 80))
		self.button_3.setFlat(True)
		self.button_3.clicked.connect(self.izmena)
		self.button_3.clicked.connect(self.nepravelno)


		self.button_4 = QPushButton('', self.window9)
		self.button_4.setIcon(QIcon('yushane.png'))
		self.button_4.setGeometry(50, 420, 250, 80)
		self.button_4.setIconSize(QSize(250, 80))
		self.button_4.setFlat(True)
		self.button_4.clicked.connect(self.izmena)
		self.button_4.clicked.connect(self.nepravelno)
#---------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------
		self.window10 = QWidget()
		self.fon = QPushButton('', self.window10)
		self.fon.setIcon(QIcon('but.png'))
		self.fon.setGeometry(0,350,680,320)
		self.fon.setIconSize(QSize(1024,678))
		
		self.button_0 = QPushButton('', self.window10)
		self.button_0.setIcon(QIcon('tor.png'))
		self.button_0.setGeometry(0, 00, 680,400)
		self.button_0.setIconSize(QSize(680, 400))
		self.button_0.setFlat(True)

		self.button_1 = QPushButton('', self.window10)
		self.button_1.setIcon(QIcon("ad.png"))
		self.button_1.setFlat(True)
		self.button_1.setGeometry(370, 420, 250, 80)
		self.button_1.setIconSize(QSize(250, 80))
		self.button_1.clicked.connect(self.izmena)
		self.button_1.clicked.connect(self.nepravelno)

		self.button_2 = QPushButton('', self.window10)
		self.button_2.setIcon(QIcon("button_xalk.png"))
		self.button_2.setGeometry(370, 520, 250, 80)
		self.button_2.setIconSize(QSize(250, 80))
		self.button_2.setFlat(True)
		self.button_2.clicked.connect(self.izmena)
		self.button_2.clicked.connect(self.nepravelno)

		self.button_3 = QPushButton('', self.window10)
		self.button_3.setIcon(QIcon("button_rag.png"))
		self.button_3.setGeometry(50, 520, 250, 80)
		self.button_3.setIconSize(QSize(250, 80))
		self.button_3.setFlat(True)
		# self.button_3.clicked.connect(self.)
		self.button_3.clicked.connect(self.pravno)


		self.button_4 = QPushButton('', self.window10)
		self.button_4.setIcon(QIcon('button_tor.png'))
		self.button_4.setGeometry(50, 420, 250, 80)
		self.button_4.setIconSize(QSize(250, 80))
		self.button_4.setFlat(True)
		self.button_4.clicked.connect(self.izmena)
		self.button_4.clicked.connect(self.nepravelno)
#---------------------------------------------------------------------------------------------

				
		self.setGeometry(50, 50, 680, 650)
		self.setWindowTitle('Guess the movie')
		self.setWindowIcon(QIcon('AVA.PNG'))
		self.show()
#Результаты------------------------------------------------------------------------------------

		self.results = QWidget()

		self.fon = QPushButton('', self.results)
		self.fon.setIcon(QIcon(''))
		self.fon.setGeometry(0, 0, 680, 650)
		self.fon.setIconSize(QSize(680, 650))


#--------------------------------------------------



	def openiuns(self):
		self.setCentralWidget(self.vxod)	

	def perehod(self):
		self.setCentralWidget(self.window2)

	def perehod2(self):
		self.setCentralWidget(self.window3)	

	def perehod3(self):
		self.setCentralWidget(self.window4)

	def perehod4(self):
		self.setCentralWidget(self.window5)

	def perehod5(self):
		self.setCentralWidget(self.window6)

	def perehod6(self):
		self.setCentralWidget(self.window7)

	def perehod7(self):
		self.setCentralWidget(self.window8)	
	def perehod8(self):
		self.setCentralWidget(self.window9)		

	def perehod9(self):
		self.setCentralWidget(self.window10)			
	
	def izmena(self):
		sender = self.sender()
		sender.setIcon(QIcon("error1.png"))


	def nepravelno(self):
		pygame.init()
		pygame.mixer.music.load('nepravel.mp3')
		pygame.mixer.music.play()

	def pravno(self):	
		pygame.init()
		pygame.mixer.music.load('prav.mp3')
		pygame.mixer.music.play()	

	def image_izmena_1(self):
		sender = self.sender()
		sender.setIcon(QIcon("kino2.png"))	

	def image_izmena_2(self):
		sender = self.sender()
		sender.setIcon(QIcon("grch2.png"))

	def image_izmena_3(self):
		sender = self.sender()
		sender.setIcon(QIcon("peopl2.png"))	

	def image_izmena_4(self):
		sender = self.sender()
		sender.setIcon(QIcon("xacker2.png"))

	def image_izmena_5(self):
		sender = self.sender()
		sender.setIcon(QIcon(""))				

	def home(self):
		self.setCentralWidget(Change())

	def light_th(self):
		self.fon.setIcon(QIcon('FON_SETTINGS_SVETLAYA.png'))
		self.fon.setGeometry(0, 0, 680, 650)
		self.fon.setIconSize(QSize(680, 650))
	def dark_th(self):
		self.fon.setIcon(QIcon('FON_SETTINGS (2).jpg'))
		self.fon.setGeometry(0, 0, 680, 650)
		self.fon.setIconSize(QSize(680, 650))

	def sendForm(self):
		f = open('Список пользователей.txt', 'r')
		list_of_names = f.read()
		if self.loginInput.text() and self.passwordInput.text() in list_of_names:
			self.setCentralWidget(self.window) 
		else:
			self.loginText.setText('Вас нет в списке') and self.passwordInput.setText('Вас нет в списке')
		f.close()
		self.loginInput.setText('')
		self.passwordInput.setText('')
	def regist(self):
		self.setCentralWidget(self.reg)
	

	def regi(self):
		f = open('Список пользователей.txt', 'a')
		f.write(self.loginInput1.text() + self.passwordInput1.text())
		f.close()
		self.loginInput.setText('')
		self.passwordInput.setText('')
	def sett(self):
		self.setCentralWidget(self.settings)

	def count_calls(func):
		def wrapper(*args, **kwargs):
			wrapper.calls += 1
			print(f"Функция {func.pravno} была вызвана {wrapper.calls} раз")
			return func(*args, **kwargs)

		wrapper.calls = 0
		return wrapper



app = QApplication(sys.argv)
my_window = Change()
sys.exit(app.exec_())