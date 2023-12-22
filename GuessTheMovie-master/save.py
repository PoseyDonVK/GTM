import sys 
import random

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout,QMainWindow
from PyQt5.QtWidgets import QLabel, QLineEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize, QBasicTimer
from sys import stdin, exit as sys_exit

class Change(QMainWindow):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
#Фон -------------------------------------------------------		

		self.window = QWidget()
		self.count = 0
		
		self.fon = QPushButton('', self)
		self.fon.setIcon(QIcon('menu1.jpg'))
		self.fon.setGeometry(0,0,680,650)
		self.fon.setIconSize(QSize(680,650))
#Фон---------------------------------------------------------
#Главный экран ----------------------------------------------

		

		self.Big = QWidget()
		self.fon = QPushButton('', self.Big)
		self.fon.setIcon(QIcon('main.jpg'))
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

		self.button_1.clicked.connect(self.openiuns)
		self.button_0.clicked.connect(self.regist)
		self.button_2.clicked.connect(self.exitGame )



#Главный икран ----------------------------------------------
		self.menu_one = QWidget()
		self.fon = QPushButton('', self.menu_one)
		self.fon.setIcon(QIcon('FON_MENU.jpg'))
		self.fon.setGeometry(0,0,680,650)
		self.fon.setIconSize(QSize(680,650))


		self.button_0 = QPushButton('', self.menu_one)
		self.button_0.setIcon(QIcon("Exit.png"))
		self.button_0.setFlat(True)
		self.button_0.setGeometry(430, 570, 250, 80)
		self.button_0.setIconSize(QSize(250, 200))
		self.button_0.clicked.connect(self.exitGame )

		self.button_1 = QPushButton('', self.menu_one)
		self.button_1.setIcon(QIcon("vxo.png"))
		self.button_1.setGeometry(0, 570, 250, 80)
		self.button_1.setIconSize(QSize(250, 80))
		self.button_1.clicked.connect(self.perehod)
		self.button_1.setFlat(True)

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

		self.button.clicked.connect(self.sendForm)

	

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


		self.button = QPushButton('', self.reg)
		self.button.setIcon(QIcon("register.png"))
		self.button.setIconSize(QSize(120, 40))
		self.button.setFlat(True)
		self.button.move(390, 320)

		self.button.clicked.connect(self.regi)




#1 Игра ------------------------------------------------------	
		self.runButton = QPushButton('')
		self.runButton.setFlat(True)
		self.runButton.setIcon(QIcon("start.png"))
		self.runButton.setIconSize(QSize(200, 92))
		self.runButton.clicked.connect(self.startGame)


		self.fon = QPushButton('', self.window)
		self.fon.setIcon(QIcon('but.png'))
		self.fon.setGeometry(0,350,680,320)
		self.fon.setIconSize(QSize(1024,678))

		self.button_0 = QPushButton('', self.window)
		self.button_0.setIcon(QIcon("kino.png"))
		self.button_0.setGeometry(0, 00, 680,400)
		self.button_0.setIconSize(QSize(680, 400))
		self.button_0.setFlat(True)

		self.button_1 = QPushButton('', self.window)
		self.button_1.setIcon(QIcon("1game.png"))
		self.button_1.setFlat(True)
		self.button_1.setGeometry(370, 420, 250, 80)
		self.button_1.setIconSize(QSize(250, 80))

		
		self.button_2 = QPushButton('', self.window)
		self.button_2.setIcon(QIcon("fals_one.png"))
		self.button_2.setGeometry(370, 520, 250, 80)
		self.button_2.setIconSize(QSize(250, 80))
		self.button_2.setFlat(True)
		self.button_2.clicked.connect(self.exitGame)


		self.button_3 = QPushButton('', self.window)
		self.button_3.setIcon(QIcon("fals_two.png"))
		self.button_3.setGeometry(50, 520, 250, 80)
		self.button_3.setIconSize(QSize(250, 80))
		self.button_3.setFlat(True)
		self.button_3.clicked.connect(self.exitGame)

		self.button_4 = QPushButton('', self.window)
		self.button_4.setIcon(QIcon('fals3.png'))
		self.button_4.setGeometry(50, 420, 250, 80)
		self.button_4.setIconSize(QSize(250, 80))
		self.button_4.setFlat(True)
		self.button_1.clicked.connect(self.perehod)
		
		self.button_4.clicked.connect(self.exitGame)	
		
		self.menu = QPushButton('', self.window)
		self.menu.setGeometry(630, 600 ,50,50)
		self.menu.setIcon(QIcon("meniu.png"))
		self.menu.clicked.connect(self.menu_1)
		self.menu.setIconSize(QSize(50, 50))
		self.menu.setFlat(True)
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

		self.button_1 = QPushButton('', self.window2)
		self.button_1.setIcon(QIcon("fals_one.png"))
		self.button_1.setFlat(True)
		self.button_1.setGeometry(370, 420, 250, 80)
		self.button_1.setIconSize(QSize(250, 80))
		self.button_1.clicked.connect(self.exitGame)

		self.button_2 = QPushButton('', self.window2)
		self.button_2.setIcon(QIcon("1game.png"))
		self.button_2.setGeometry(370, 520, 250, 80)
		self.button_2.setIconSize(QSize(250, 80))
		self.button_2.setFlat(True)
		self.button_2.clicked.connect(self.exitGame)

		self.button_3 = QPushButton('', self.window2)
		self.button_3.setIcon(QIcon("fals3.png"))
		self.button_3.setGeometry(50, 520, 250, 80)
		self.button_3.setIconSize(QSize(250, 80))
		self.button_3.setFlat(True)
		self.button_3.clicked.connect(self.exitGame)

		self.button_4 = QPushButton('', self.window2)
		self.button_4.setIcon(QIcon('fals_two.png'))
		self.button_4.setGeometry(50, 420, 250, 80)
		self.button_4.setIconSize(QSize(250, 80))
		self.button_4.setFlat(True)
		self.button_4.clicked.connect(self.perehod2)


		self.menu = QPushButton('', self.window2)
		self.menu.setGeometry(630, 600 ,50,50)
		self.menu.setIcon(QIcon("meniu.png"))
		self.menu.clicked.connect(self.menu_1)
		self.menu.setIconSize(QSize(50, 50))
		self.menu.setFlat(True)


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

		

		self.button_1 = QPushButton('', self.window3)
		self.button_1.setIcon(QIcon("1game.png"))
		self.button_1.setFlat(True)
		self.button_1.setGeometry(370, 420, 250, 80)
		self.button_1.setIconSize(QSize(250, 80))
		self.button_1.clicked.connect(self.exitGame)

		self.button_2 = QPushButton('', self.window3)
		self.button_2.setIcon(QIcon("fals_two"))
		self.button_2.setGeometry(370, 520, 250, 80)
		self.button_2.setIconSize(QSize(250, 80))
		self.button_2.setFlat(True)
		self.button_2.clicked.connect(self.exitGame)

		self.button_3 = QPushButton('', self.window3)
		self.button_3.setIcon(QIcon("fals_one"))
		self.button_3.setGeometry(50, 520, 250, 80)
		self.button_3.setIconSize(QSize(250, 80))
		self.button_3.setFlat(True)
		self.button_3.clicked.connect(self.exitGame)

		self.button_4 = QPushButton('', self.window3)
		self.button_4.setIcon(QIcon('fals3'))
		self.button_4.setGeometry(50, 420, 250, 80)
		self.button_4.setIconSize(QSize(250, 80))
		self.button_4.setFlat(True)
		self.button_4.clicked.connect(self.perehod3)


		self.menu = QPushButton('', self.window3)
		self.menu.setGeometry(630, 600 ,50,50)
		self.menu.setIcon(QIcon("meniu.png"))
		self.menu.clicked.connect(self.menu_1)
		self.menu.setIconSize(QSize(50, 50))
		self.menu.setFlat(True)

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


		self.button_1 = QPushButton('', self.window4)
		self.button_1.setIcon(QIcon("button_led.png"))
		self.button_1.setFlat(True)
		self.button_1.setGeometry(370, 420, 250, 80)
		self.button_1.setIconSize(QSize(250, 80))
		self.button_1.clicked.connect(self.exitGame)

		self.button_2 = QPushButton('', self.window4)
		self.button_2.setIcon(QIcon("button_xacker.png"))
		self.button_2.setGeometry(370, 520, 250, 80)
		self.button_2.setIconSize(QSize(250, 80))
		self.button_2.setFlat(True)


		self.button_3 = QPushButton('', self.window4)
		self.button_3.setIcon(QIcon("fals_one"))
		self.button_3.setGeometry(50, 520, 250, 80)
		self.button_3.setIconSize(QSize(250, 80))
		self.button_3.setFlat(True)
		self.button_3.clicked.connect(self.exitGame)


		self.button_4 = QPushButton('', self.window4)
		self.button_4.setIcon(QIcon('button_flesh.png'))
		self.button_4.setGeometry(50, 420, 250, 80)
		self.button_4.setIconSize(QSize(250, 80))
		self.button_4.setFlat(True)
		self.button_2.clicked.connect(self.perehod4)
	
		self.button_4.clicked.connect(self.exitGame)


		self.menu = QPushButton('', self.window4)
		self.menu.setGeometry(630, 600 ,50,50)
		self.menu.setIcon(QIcon("meniu.png"))
		self.menu.clicked.connect(self.menu_1)
		self.menu.setIconSize(QSize(50, 50))
		self.menu.setFlat(True)		

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

		self.button_1 = QPushButton('', self.window5)
		self.button_1.setIcon(QIcon("button_xacker.png"))
		self.button_1.setFlat(True)
		self.button_1.setGeometry(370, 420, 250, 80)
		self.button_1.setIconSize(QSize(250, 80))
		self.button_1.clicked.connect(self.exitGame)


		self.button_2 = QPushButton('', self.window5)
		self.button_2.setIcon(QIcon("button_led.png"))
		self.button_2.setGeometry(370, 520, 250, 80)
		self.button_2.setIconSize(QSize(250, 80))
		self.button_2.setFlat(True)
		self.button_2.clicked.connect(self.exitGame)


		self.button_3 = QPushButton('', self.window5)
		self.button_3.setIcon(QIcon("button_flesh.png"))
		self.button_3.setGeometry(50, 520, 250, 80)
		self.button_3.setIconSize(QSize(250, 80))
		self.button_3.setFlat(True)
	


		self.button_4 = QPushButton('', self.window5)
		self.button_4.setIcon(QIcon('fals_two.png'))
		self.button_4.setGeometry(50, 420, 250, 80)
		self.button_4.setIconSize(QSize(250, 80))
		self.button_4.setFlat(True)
		self.button_3.clicked.connect(self.perehod5)
	
		self.button_4.clicked.connect(self.exitGame)
	
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
		self.button_1.setIcon(QIcon("button_xacker.png"))
		self.button_1.setFlat(True)
		self.button_1.setGeometry(370, 420, 250, 80)
		self.button_1.setIconSize(QSize(250, 80))
		self.button_1.clicked.connect(self.exitGame)

		self.button_2 = QPushButton('', self.window6)
		self.button_2.setIcon(QIcon("button_led.png"))
		self.button_2.setGeometry(370, 520, 250, 80)
		self.button_2.setIconSize(QSize(250, 80))
		self.button_2.setFlat(True)
		self.button_2.clicked.connect(self.exitGame)

		self.button_3 = QPushButton('', self.window6)
		self.button_3.setIcon(QIcon("button_flesh.png"))
		self.button_3.setGeometry(50, 520, 250, 80)
		self.button_3.setIconSize(QSize(250, 80))
		self.button_3.setFlat(True)
		self.button_3.clicked.connect(self.exitGame)


		self.button_4 = QPushButton('', self.window6)
		self.button_4.setIcon(QIcon('button_streka.png'))
		self.button_4.setGeometry(50, 420, 250, 80)
		self.button_4.setIconSize(QSize(250, 80))
		self.button_4.setFlat(True)
		self.button_4.clicked.connect(self.perehod6)
	

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
		self.button_1.setIcon(QIcon("button_xacker.png"))
		self.button_1.setFlat(True)
		self.button_1.setGeometry(370, 420, 250, 80)
		self.button_1.setIconSize(QSize(250, 80))
		self.button_1.clicked.connect(self.exitGame)

		self.button_2 = QPushButton('', self.window7)
		self.button_2.setIcon(QIcon("button_ono.png"))
		self.button_2.setGeometry(370, 520, 250, 80)
		self.button_2.setIconSize(QSize(250, 80))
		self.button_2.setFlat(True)
		self.button_2.clicked.connect(self.perehod7)



		self.button_3 = QPushButton('', self.window7)
		self.button_3.setIcon(QIcon("button_flesh.png"))
		self.button_3.setGeometry(50, 520, 250, 80)
		self.button_3.setIconSize(QSize(250, 80))
		self.button_3.setFlat(True)
		self.button_3.clicked.connect(self.exitGame)


		self.button_4 = QPushButton('', self.window7)
		self.button_4.setIcon(QIcon('button_streka.png'))
		self.button_4.setGeometry(50, 420, 250, 80)
		self.button_4.setIconSize(QSize(250, 80))
		self.button_4.setFlat(True)
		self.button_4.clicked.connect(self.exitGame)
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
		self.button_1.setIcon(QIcon("button_xacker.png"))
		self.button_1.setFlat(True)
		self.button_1.setGeometry(370, 420, 250, 80)
		self.button_1.setIconSize(QSize(250, 80))
		self.button_1.clicked.connect(self.exitGame)

		self.button_2 = QPushButton('', self.window8)
		self.button_2.setIcon(QIcon("button_ono.png"))
		self.button_2.setGeometry(370, 520, 250, 80)
		self.button_2.setIconSize(QSize(250, 80))
		self.button_2.setFlat(True)
		self.button_2.clicked.connect(self.exitGame)


		self.button_3 = QPushButton('', self.window8)
		self.button_3.setIcon(QIcon("button_bigg.png"))
		self.button_3.setGeometry(50, 520, 250, 80)
		self.button_3.setIconSize(QSize(250, 80))
		self.button_3.setFlat(True)
		self.button_3.clicked.connect(self.perehod8)



		self.button_4 = QPushButton('', self.window8)
		self.button_4.setIcon(QIcon('button_streka.png'))
		self.button_4.setGeometry(50, 420, 250, 80)
		self.button_4.setIconSize(QSize(250, 80))
		self.button_4.setFlat(True)
		self.button_4.clicked.connect(self.exitGame)
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

		self.b
		utton_2 = QPushButton('', self.window9)
		self.button_2.setIcon(QIcon("button_ono.png"))
		self.button_2.setGeometry(370, 520, 250, 80)
		self.button_2.setIconSize(QSize(250, 80))
		self.button_2.setFlat(True)
		self.button_2.clicked.connect(self.exitGame)


		self.button_3 = QPushButton('', self.window9)
		self.button_3.setIcon(QIcon("button_streka.png"))
		self.button_3.setGeometry(50, 520, 250, 80)
		self.button_3.setIconSize(QSize(250, 80))
		self.button_3.setFlat(True)
		self.button_3.clicked.connect(self.exitGame)


		self.button_4 = QPushButton('', self.window9)
		self.button_4.setIcon(QIcon('button_flesh.png'))
		self.button_4.setGeometry(50, 420, 250, 80)
		self.button_4.setIconSize(QSize(250, 80))
		self.button_4.setFlat(True)
		self.button_4.clicked.connect(self.exitGame)
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
		self.button_1.setIcon(QIcon("button_masak.png"))
		self.button_1.setFlat(True)
		self.button_1.setGeometry(370, 420, 250, 80)
		self.button_1.setIconSize(QSize(250, 80))
		self.button_1.clicked.connect(self.perehod8)

		self.b
		utton_2 = QPushButton('', self.window10)
		self.button_2.setIcon(QIcon("button_xalk.png"))
		self.button_2.setGeometry(370, 520, 250, 80)
		self.button_2.setIconSize(QSize(250, 80))
		self.button_2.setFlat(True)
		self.button_2.clicked.connect(self.exitGame)


		self.button_3 = QPushButton('', self.window10)
		self.button_3.setIcon(QIcon("button_rag.png"))
		self.button_3.setGeometry(50, 520, 250, 80)
		self.button_3.setIconSize(QSize(250, 80))
		self.button_3.setFlat(True)
		self.button_3.clicked.connect(self.exitGame)


		self.button_4 = QPushButton('', self.window10)
		self.button_4.setIcon(QIcon('button_tor.png'))
		self.button_4.setGeometry(50, 420, 250, 80)
		self.button_4.setIconSize(QSize(250, 80))
		self.button_4.setFlat(True)
		self.button_4.clicked.connect(self.exitGame)
#---------------------------------------------------------------------------------------------

				
		self.setGeometry(50, 50, 680, 650)
		self.setWindowTitle('Guess the movie')
		self.setWindowIcon(QIcon('AVA.PNG'))
		self.show()

	

	def exitGame(self):
		sys_exit()


	def startGame(self):
		self.runButton.setEnabled(False)	

	def openiuns(self):

		self.setCentralWidget(self.vxod)

	
	def startGame(self):
		self.runButton.setEnabled(False)

	def menu_1(self):
		self.setCentralWidget(self.menu_one)	

	def perehod(self):
		self.count += 1		
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

app = QApplication(sys.argv)
my_window = Change()
sys.exit(app.exec_())