from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import Scrapy.total_datas
import Scrapy.new_datas
import Scrapy.table
import Scrapy.countries

class App(QMainWindow):
    def __init__(self,*args,**kwargs):
        super().__init__()
        self.setWindowIcon(QIcon("Image/logo.png"))
        self.setWindowTitle("Kerberos Covid-19 Data Analys")

        self.width, self.height = 1260,920
        self.setFixedSize(self.width, self.height)

        self.countries = Scrapy.countries.countries
       
        self.aside_width, self.aside_height = 240,self.height
        self.frame_width, self.frame_height = self.width-self.aside_width, self.height

        self.font = "Ubuntu"
        self.primary_color = "#333"
        self.secondary_color = "#489592"

        self.initUI()
        
    
    def initUI(self):


#Left Aside-Bar----------------------------------------------------------------------------
        self.aside = QFrame(self)
        self.aside.setMinimumSize(self.aside_width,self.aside_height)
        self.asideLayout = QVBoxLayout(self)
        self.aside.setLayout(self.asideLayout)
        self.aside.setStyleSheet("background-color:#333")

#Aside-Bar Buttons ------------------------------------------------------------------------
        self.WorldWide_btn = QPushButton("World Wide",self)
        self.asideLayout.addWidget(self.WorldWide_btn)
        self.WorldWide_btn.setStyleSheet("background-color:#333;border-radius:4px;border:1px solid white;color:white")
        self.WorldWide_btn.setIcon(QIcon("Image/world.png"))
        self.WorldWide_btn.setIconSize(QSize(60,60))
        self.WorldWide_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.WorldWide_btn.clicked.connect(self.clickWW)
          
        self.Country_btn = QPushButton(QIcon("Image/flag.png"), "Countries",self)
        self.asideLayout.addWidget(self.Country_btn)
        self.Country_btn.setStyleSheet("background-color:#333;border-radius:4px;border:1px solid white;color:white")
        self.Country_btn.setIconSize(QSize(60,60))
        self.Country_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.Country_btn.clicked.connect(self.clickCo)
        
        self.Other_btn = QPushButton(QIcon("Image/reps.png"),"All Reports",self)
        self.asideLayout.addWidget(self.Other_btn)
        self.Other_btn.setStyleSheet("background-color:#333;border-radius:4px;border:1px solid white;color:white")
        self.Other_btn.setIconSize(QSize(60,60))
        self.Other_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.Other_btn.clicked.connect(self.clickOther)
       
        self.runWW()
        self.runC()
        self.runO()


    def runWW(self):
#World Wide Frame-------------------------------------------------------------

        self.WorldWide_Frame= QFrame(self)
        self.WorldWide_Frame.resize(self.frame_width, self.frame_height)
        self.WorldWide_Frame.move(self.width-self.frame_width,0)
        self.WorldWide_Frame_Layout = QVBoxLayout(self)
        self.WorldWide_Frame.setLayout(self.WorldWide_Frame_Layout)    

        self.ww_font_nor = 16
        self.ww_font_up = 24
        self.ww_font_low = 13
        self.ww_font_up2 = 21
        self.ww_font_low2 = 10
             
        self.title = QLabel(self)
        self.title.setText("<strong>Covid-19 Reports<</strong>")
        self.WorldWide_Frame_Layout.addWidget(self.title)
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setStyleSheet(f"color:{self.secondary_color};font-style:bold")
        self.title.setFont(QFont(self.font,22))

        self.ww_topBar = QFrame(self)
        self.WorldWide_Frame_Layout.addWidget(self.ww_topBar)
        self.ww_topBar_layout = QHBoxLayout(self)
        self.ww_topBar.setLayout(self.ww_topBar_layout)
          
        self.ww_TotalConfirmed = QLabel(self)
        self.ww_TotalConfirmed_layout = QVBoxLayout(self)
        self.ww_TotalConfirmed.setLayout(self.ww_TotalConfirmed_layout)
        self.ww_topBar_layout.addWidget(self.ww_TotalConfirmed)
        self.ww_TotalConfirmed.setFixedHeight(120)
        
        self.ww_TotalConfirmed_int = QLabel(self)
        self.ww_TotalConfirmed_layout.addWidget(self.ww_TotalConfirmed_int)
        self.ww_TotalConfirmed_int.setText(str(Scrapy.total_datas.totalConfirmed))
        self.ww_TotalConfirmed_int.setFont(QFont(self.font,self.ww_font_up))
        self.ww_TotalConfirmed_int.setStyleSheet("color:#333;border:none")
        self.ww_TotalConfirmed_int.setAlignment(Qt.AlignCenter)
        
        self.ww_TotalConfirmed_txt = QLabel("Total Confirmed",self)
        self.ww_TotalConfirmed_txt.setFont(QFont(self.font,self.ww_font_low))
        self.ww_TotalConfirmed_txt.setStyleSheet("color:white;background:#333")
        self.ww_TotalConfirmed_txt.setAlignment(Qt.AlignCenter)
        self.ww_TotalConfirmed_layout.addWidget(self.ww_TotalConfirmed_txt)
        
        self.ww_TotalDeaths = QLabel(self)
        self.ww_TotalDeaths_layout = QVBoxLayout(self)
        self.ww_TotalDeaths.setLayout(self.ww_TotalDeaths_layout)
        self.ww_topBar_layout.addWidget(self.ww_TotalDeaths)
        self.ww_TotalDeaths.setFixedHeight(120)
        
        self.ww_TotalDeaths_int = QLabel(self)
        self.ww_TotalDeaths_int.setText(str(Scrapy.total_datas.totalDeaths))
        self.ww_TotalDeaths_int.setFont(QFont(self.font,self.ww_font_up))
        self.ww_TotalDeaths_int.setStyleSheet("color:#333")
        self.ww_TotalDeaths_int.setAlignment(Qt.AlignCenter)
        self.ww_TotalDeaths_layout.addWidget(self.ww_TotalDeaths_int)
        
        self.ww_TotalDeaths_txt = QLabel("Total Deaths",self)
        self.ww_TotalDeaths_layout.addWidget(self.ww_TotalDeaths_txt)
        self.ww_TotalDeaths_txt.setStyleSheet("color:white;background:#333")
        self.ww_TotalDeaths_txt.setFont(QFont(self.font,self.ww_font_low))
        self.ww_TotalDeaths_txt.setAlignment(Qt.AlignCenter)
        
        self.ww_TotalRecovered = QLabel(self)
        self.ww_topBar_layout.addWidget(self.ww_TotalRecovered)
        self.ww_TotalRecovered_layout = QVBoxLayout(self)
        self.ww_TotalRecovered.setLayout(self.ww_TotalRecovered_layout)
        self.ww_TotalRecovered.setFixedHeight(120)
        
        self.ww_TotalRecovered_int = QLabel(self)
        self.ww_TotalRecovered_layout.addWidget(self.ww_TotalRecovered_int)
        self.ww_TotalRecovered_int.setText(str(Scrapy.total_datas.totalRecovered))
        self.ww_TotalRecovered_int.setStyleSheet("color:#333;border:none;")
        self.ww_TotalRecovered_int.setFont(QFont(self.font,self.ww_font_up))
        self.ww_TotalRecovered_int.setAlignment(Qt.AlignCenter)
        
        self.ww_TotalRecovered_txt = QLabel("Total Recovered", self)
        self.ww_TotalRecovered_layout.addWidget(self.ww_TotalRecovered_txt)
        self.ww_TotalRecovered_txt.setStyleSheet("color:white;background:#333")
        self.ww_TotalRecovered_txt.setFont(QFont(self.font, self.ww_font_low))
        self.ww_TotalRecovered_txt.setAlignment(Qt.AlignCenter)
   
        self.ww_aside = QFrame(self)
        self.WorldWide_Frame_Layout.addWidget(self.ww_aside)
        self.ww_aside_layout = QHBoxLayout(self)
        self.ww_aside.setLayout(self.ww_aside_layout)

        self.ww_NewConfirmed = QLabel(self)
        self.ww_aside_layout.addWidget(self.ww_NewConfirmed)
        self.ww_NewConfirmed_layout = QVBoxLayout(self)
        self.ww_NewConfirmed.setLayout(self.ww_NewConfirmed_layout)
        self.ww_NewConfirmed.setFixedSize(275,100)

        self.ww_NewConfirmed_int = QLabel(self)
        self.ww_NewConfirmed_layout.addWidget(self.ww_NewConfirmed_int)
        self.ww_NewConfirmed_int.setText(str(Scrapy.new_datas.newCases))
        self.ww_NewConfirmed_int.setStyleSheet("color:#333;border:none")
        self.ww_NewConfirmed_int.setFont(QFont(self.font, self.ww_font_up2))
        self.ww_NewConfirmed_int.setAlignment(Qt.AlignCenter)
        
        self.ww_NewConfirmed_txt = QLabel("New Confirmed", self)
        self.ww_NewConfirmed_layout.addWidget(self.ww_NewConfirmed_txt)
        self.ww_NewConfirmed_txt.setStyleSheet("color:white;background:#333")
        self.ww_NewConfirmed_txt.setFont(QFont(self.font, self.ww_font_low2))
        self.ww_NewConfirmed_txt.setAlignment(Qt.AlignCenter)

        self.ww_NewDeaths = QLabel(self)
        self.ww_aside_layout.addWidget(self.ww_NewDeaths)
        self.ww_NewDeaths_layout = QVBoxLayout(self)
        self.ww_NewDeaths.setLayout(self.ww_NewDeaths_layout)
        self.ww_NewDeaths.setFixedSize(275,100)

        self.ww_NewDeaths_int = QLabel(self)
        self.ww_NewDeaths_layout.addWidget(self.ww_NewDeaths_int)
        self.ww_NewDeaths_int.setText(str(Scrapy.new_datas.newDeaths))
        self.ww_NewDeaths_int.setStyleSheet("color:#333;border:none")
        self.ww_NewDeaths_int.setFont(QFont(self.font, self.ww_font_up2))
        self.ww_NewDeaths_int.setAlignment(Qt.AlignCenter)
        
        self.ww_NewDeaths_txt = QLabel("New Deaths", self)
        self.ww_NewDeaths_layout.addWidget(self.ww_NewDeaths_txt)
        self.ww_NewDeaths_txt.setStyleSheet("color:white;background:#333")
        self.ww_NewDeaths_txt.setFont(QFont(self.font, self.ww_font_low2))
        self.ww_NewDeaths_txt.setAlignment(Qt.AlignCenter)

        
        self.ww_NewRecovered = QLabel(self)
        self.ww_aside_layout.addWidget(self.ww_NewRecovered)
        self.ww_NewRecovered_layout = QVBoxLayout(self)
        self.ww_NewRecovered.setLayout(self.ww_NewRecovered_layout)
        self.ww_NewRecovered.setFixedSize(275,100)

        self.ww_NewRecovered_int = QLabel(self)
        self.ww_NewRecovered_layout.addWidget(self.ww_NewRecovered_int)
        self.ww_NewRecovered_int.setText("+"+ str(Scrapy.new_datas.activeCase))
        self.ww_NewRecovered_int.setStyleSheet("color:#333;border:none")
        self.ww_NewRecovered_int.setFont(QFont(self.font, self.ww_font_up2))
        self.ww_NewRecovered_int.setAlignment(Qt.AlignCenter)
        
        self.ww_NewRecovered_txt = QLabel("Active Cases", self)
        self.ww_NewRecovered_layout.addWidget(self.ww_NewRecovered_txt)
        self.ww_NewRecovered_txt.setStyleSheet("color:white;background:#333")
        self.ww_NewRecovered_txt.setFont(QFont(self.font, self.ww_font_low2))
        self.ww_NewRecovered_txt.setAlignment(Qt.AlignCenter)

        self.tableWidget = QTableWidget(self) 
        self.WorldWide_Frame_Layout.addWidget(self.tableWidget)
        self.tableWidget.setRowCount(len(Scrapy.table.countries))   
        self.tableWidget.setColumnCount(4)   
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.setHorizontalHeaderLabels(["Country","Total Confirmed","Total Deaths","Total Recovered"])    
        self.tableWidget.setShowGrid(False)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setFocusPolicy(Qt.NoFocus)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)

        for r in range(len(Scrapy.table.countries)):    
            for c in range(4):
                self.tableWidget.setItem(r,0,QTableWidgetItem(str(Scrapy.table.countries[r])))
                self.tableWidget.setItem(r,1,QTableWidgetItem(str(Scrapy.table.totalCases[r])))
                self.tableWidget.setItem(r,2,QTableWidgetItem(str(Scrapy.table.totalDeaths[r])))
                self.tableWidget.setItem(r,3,QTableWidgetItem(str(Scrapy.table.totalRecovered[r])))

              
                
        
        
        for r in range(len(Scrapy.table.countries)):
            self.tableWidget.setRowHeight(r,55)
            for c in range(4):
                self.tableWidget.item(r,c).setFont(QFont("Times", 11))
                self.tableWidget.horizontalHeaderItem(c).setFont(QFont("Ubuntu",13))
                self.tableWidget.item(r,c).setTextAlignment(Qt.AlignCenter)


                if r%2 != 0:
                    
                    self.tableWidget.item(r,c).setBackground(QColor("#eee"))

                else:

                    self.tableWidget.item(r,c).setBackground(QColor("#c5c5c5"))


#Country Frame

    def runC(self):
        self.Country_Frame = QFrame(self)
        self.Country_Frame.resize(self.frame_width,self.frame_height)
        self.Country_Frame.move(self.width-self.frame_width,0)
        self.Country_Frame_Layout = QVBoxLayout(self)
        self.Country_Frame.setLayout(self.Country_Frame_Layout)    
        self.Country_Frame.hide()
        self.cFont_size = 13
        self.c_font_nor = 16
        self.c_font_up = 24
        self.c_font_low = 13
        self.c_font_up2 = 21
        self.c_font_low2 = 10


        self.c_topBar = QFrame(self)
        self.Country_Frame_Layout.addWidget(self.c_topBar)
        self.c_topBar.setFixedHeight(150)
        self.c_topBar_layout = QHBoxLayout(self)
        self.c_topBar.setLayout(self.c_topBar_layout)

        self.chooseText = QLabel(self)
        self.chooseText.setText("Choose your country: ")
        self.c_topBar_layout.addWidget(self.chooseText)
        self.chooseText.setFont(QFont(self.font,self.cFont_size))

        self.comboBox = QComboBox(self)

        for i in range(len(self.countries)):
            self.comboBox.addItem(self.countries[i][2])

        self.c_topBar_layout.addWidget(self.comboBox)
        
        self.comboBox_btn=  QPushButton("Show",self)
        self.c_topBar_layout.addWidget(self.comboBox_btn)
        self.comboBox_btn.setFixedSize(85,45)
        self.comboBox_btn.pressed.connect(self.click_cbBtn)
        
    

        self.c_main = QFrame(self)
        self.Country_Frame_Layout.addWidget(self.c_main)
        self.c_main_layout = QVBoxLayout(self)
        self.c_main.setLayout(self.c_main_layout)

        self.c_main_title = QLabel("<strong>Covid 19 Tables by Countries</strong>")
        self.c_main_layout.addWidget(self.c_main_title)
        self.c_main_title.setFont(QFont("Ubuntu",16))
        self.c_main_title.setStyleSheet(f"color:{self.secondary_color}")
        self.c_main_title.setAlignment(Qt.AlignCenter)


        self.c_nav= QFrame(self)
        self.c_main_layout.addWidget(self.c_nav)
        self.c_nav_layout = QHBoxLayout(self)
        self.c_nav.setLayout(self.c_nav_layout)


        self.c_TotalConfirmed = QLabel(self)
        self.c_TotalConfirmed_layout = QVBoxLayout(self)
        self.c_TotalConfirmed.setLayout(self.c_TotalConfirmed_layout)
        self.c_nav_layout.addWidget(self.c_TotalConfirmed)
        self.c_TotalConfirmed.setFixedHeight(120)
        
        self.c_TotalConfirmed_int = QLabel(self)
        self.c_TotalConfirmed_layout.addWidget(self.c_TotalConfirmed_int)
        self.c_TotalConfirmed_int.setFont(QFont(self.font,self.c_font_up))
        self.c_TotalConfirmed_int.setStyleSheet("color:#333;border:none")
        self.c_TotalConfirmed_int.setAlignment(Qt.AlignCenter)
        
        self.c_TotalConfirmed_txt = QLabel("Total Confirmed",self)
        self.c_TotalConfirmed_txt.setFont(QFont(self.font,self.c_font_low))
        self.c_TotalConfirmed_txt.setStyleSheet("color:white;background:#333")
        self.c_TotalConfirmed_txt.setAlignment(Qt.AlignCenter)
        self.c_TotalConfirmed_layout.addWidget(self.c_TotalConfirmed_txt)
        
        self.c_TotalDeaths = QLabel(self)
        self.c_TotalDeaths_layout = QVBoxLayout(self)
        self.c_TotalDeaths.setLayout(self.c_TotalDeaths_layout)
        self.c_nav_layout.addWidget(self.c_TotalDeaths)
        self.c_TotalDeaths.setFixedHeight(120)
        
        self.c_TotalDeaths_int = QLabel(self)
        self.c_TotalDeaths_int.setFont(QFont(self.font,self.c_font_up))
        self.c_TotalDeaths_int.setStyleSheet("color:#333")
        self.c_TotalDeaths_int.setAlignment(Qt.AlignCenter)
        self.c_TotalDeaths_layout.addWidget(self.c_TotalDeaths_int)
        
        self.c_TotalDeaths_txt = QLabel("Total Deaths",self)
        self.c_TotalDeaths_layout.addWidget(self.c_TotalDeaths_txt)
        self.c_TotalDeaths_txt.setStyleSheet("color:white;background:#333")
        self.c_TotalDeaths_txt.setFont(QFont(self.font,self.c_font_low))
        self.c_TotalDeaths_txt.setAlignment(Qt.AlignCenter)
        
        self.c_TotalRecovered = QLabel(self)
        self.c_nav_layout.addWidget(self.c_TotalRecovered)
        self.c_TotalRecovered_layout = QVBoxLayout(self)
        self.c_TotalRecovered.setLayout(self.c_TotalRecovered_layout)
        self.c_TotalRecovered.setFixedHeight(120)
        
        self.c_TotalRecovered_int = QLabel(self)
        self.c_TotalRecovered_layout.addWidget(self.c_TotalRecovered_int)
        self.c_TotalRecovered_int.setStyleSheet("color:#333;border:none;")
        self.c_TotalRecovered_int.setFont(QFont(self.font,self.c_font_up))
        self.c_TotalRecovered_int.setAlignment(Qt.AlignCenter)
        
        self.c_TotalRecovered_txt = QLabel("Total Recovered", self)
        self.c_TotalRecovered_layout.addWidget(self.c_TotalRecovered_txt)
        self.c_TotalRecovered_txt.setStyleSheet("color:white;background:#333")
        self.c_TotalRecovered_txt.setFont(QFont(self.font, self.c_font_low))
        self.c_TotalRecovered_txt.setAlignment(Qt.AlignCenter)
   
        self.c_aside = QFrame(self)
        self.Country_Frame_Layout.addWidget(self.c_aside)
        self.c_aside_layout = QHBoxLayout(self)
        self.c_aside.setLayout(self.c_aside_layout)

        self.c_NewConfirmed = QLabel(self)
        self.c_aside_layout.addWidget(self.c_NewConfirmed)
        self.c_NewConfirmed_layout = QVBoxLayout(self)
        self.c_NewConfirmed.setLayout(self.c_NewConfirmed_layout)
        self.c_NewConfirmed.setFixedSize(275,100)

        self.c_NewConfirmed_int = QLabel(self)
        self.c_NewConfirmed_layout.addWidget(self.c_NewConfirmed_int)
        self.c_NewConfirmed_int.setStyleSheet("color:#333;border:none")
        self.c_NewConfirmed_int.setFont(QFont(self.font, self.c_font_up2))
        self.c_NewConfirmed_int.setAlignment(Qt.AlignCenter)
        
        self.c_NewConfirmed_txt = QLabel("New Confirmed", self)
        self.c_NewConfirmed_layout.addWidget(self.c_NewConfirmed_txt)
        self.c_NewConfirmed_txt.setStyleSheet("color:white;background:#333")
        self.c_NewConfirmed_txt.setFont(QFont(self.font, self.c_font_low2))
        self.c_NewConfirmed_txt.setAlignment(Qt.AlignCenter)

        self.c_NewDeaths = QLabel(self)
        self.c_aside_layout.addWidget(self.c_NewDeaths)
        self.c_NewDeaths_layout = QVBoxLayout(self)
        self.c_NewDeaths.setLayout(self.c_NewDeaths_layout)
        self.c_NewDeaths.setFixedSize(275,100)

        self.c_NewDeaths_int = QLabel(self)
        self.c_NewDeaths_layout.addWidget(self.c_NewDeaths_int)
        self.c_NewDeaths_int.setStyleSheet("color:#333;border:none")
        self.c_NewDeaths_int.setFont(QFont(self.font, self.c_font_up2))
        self.c_NewDeaths_int.setAlignment(Qt.AlignCenter)
        
        self.c_NewDeaths_txt = QLabel("New Deaths", self)
        self.c_NewDeaths_layout.addWidget(self.c_NewDeaths_txt)
        self.c_NewDeaths_txt.setStyleSheet("color:white;background:#333")
        self.c_NewDeaths_txt.setFont(QFont(self.font, self.c_font_low2))
        self.c_NewDeaths_txt.setAlignment(Qt.AlignCenter)

        
        self.c_NewRecovered = QLabel(self)
        self.c_aside_layout.addWidget(self.c_NewRecovered)
        self.c_NewRecovered_layout = QVBoxLayout(self)
        self.c_NewRecovered.setLayout(self.c_NewRecovered_layout)
        self.c_NewRecovered.setFixedSize(275,100)

        self.c_NewRecovered_int = QLabel(self)
        self.c_NewRecovered_layout.addWidget(self.c_NewRecovered_int)
        self.c_NewRecovered_int.setStyleSheet("color:#333;border:none")
        self.c_NewRecovered_int.setFont(QFont(self.font, self.c_font_up2))
        self.c_NewRecovered_int.setAlignment(Qt.AlignCenter)
        
        self.c_NewRecovered_txt = QLabel("Active Case", self)
        self.c_NewRecovered_layout.addWidget(self.c_NewRecovered_txt)
        self.c_NewRecovered_txt.setStyleSheet("color:white;background:#333")
        self.c_NewRecovered_txt.setFont(QFont(self.font, self.c_font_low2))
        self.c_NewRecovered_txt.setAlignment(Qt.AlignCenter)


        





    def runO(self):
        self.Other_Frame = QFrame(self)
        self.Other_Frame.resize(self.frame_width,self.frame_height)
        self.Other_Frame.move(self.width-self.frame_width,0)
        self.Other_Frame_Layout = QVBoxLayout(self)
        self.Other_Frame.setLayout(self.Other_Frame_Layout) 
        self.Other_Frame_Layout.setAlignment(Qt.AlignCenter)   
        self.Other_Frame.hide()
        self.otherFont_size = 13
        self.other_font_nor = 16
        self.other_font_up = 24
        self.other_font_low = 13
        self.other_font_up2 = 21
        self.other_font_low2 = 10

        self.comingSoon = QLabel(self)
        self.comingSoon.setText("Coming Soon....")
        self.Other_Frame_Layout.addWidget(self.comingSoon)
        self.comingSoon.setFont(QFont("Ubuntu",self.otherFont_size))

        self.gifLabel = QLabel(self)
        self.gif=QMovie("./Image/wear-mask.gif")
        self.gifLabel.setMovie(self.gif)      
        self.Other_Frame_Layout.addWidget(self.gifLabel)  
        self.gif.start()
        



        
    def click_cbBtn(self):
        self.current = self.comboBox.currentText()


        for i in range(len(self.countries)):
            if self.countries[i][2] == self.current:
                self.c_main_title.setText( "<strong>"+str(self.countries[i][2])+ " Covid 19 Table"+"</strong>")
                self.c_TotalConfirmed_int.setText(str(self.countries[i][3]))
                self.c_TotalDeaths_int.setText(str(self.countries[i][5]))
                self.c_TotalRecovered_int.setText(str(self.countries[i][7]))
                self.c_NewConfirmed_int.setText(str(self.countries[i][4]))
                self.c_NewDeaths_int.setText(str(self.countries[i][6]))
                self.c_NewRecovered_int.setText(str(self.countries[i][9]))

        
    

        
    def clickWW(self):
        self.WorldWide_Frame.show()
        self.Country_Frame.hide()
        self.Other_Frame.hide()
    
    def clickCo(self):
        self.WorldWide_Frame.hide()
        self.Country_Frame.show()
        self.Other_Frame.hide()

    def clickOther(self):
        self.WorldWide_Frame.hide()
        self.Country_Frame.hide()
        self.Other_Frame.show()




    
 



app = QApplication(sys.argv)
main = App()
main.show()
sys.exit(app.exec_())