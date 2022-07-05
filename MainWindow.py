from PyQt5.QtWidgets import *
import sys
from PyQt5.QtGui import QIcon
from PyQt5 import QtWidgets,QtCore
from PyQt5.QtGui import QPalette,QColor,QFont
from PyQt5.QtCore import Qt
import os

import scraping
from scraping import Scrapping



class MainWindow(QMainWindow):
    '''Class to construct GUI for main window using pyqt5'''


    def __init__(self,parent=None):
        super(MainWindow,self).__init__()
        self.resize(500,500)



    def browse_file(self):
        self.folderpath=QtWidgets.QFileDialog.getExistingDirectory(self)


        if len(self.folderpath) > 0 and len(self.search_words.text()) > 0 and len(self.page_number.text()) > 0:
            self.run_button.setEnabled(True)

    def strat_scrapping(self):
        print(self.search_words.text())
        print(int(self.page_number.text()))
        print(self.folderpath)
        print(self.custom_name.text())
        scr=Scrapping(name='scraping')
        print(scr.name)

        scr.scrapping(self.search_words.text(),int(self.page_number.text()),self.folderpath,self.custom_name.text())




    def SetupUi(self):

        self.path=''
        self.search_words = QLineEdit(self)

        self.search_words.resize(200,30)
        self.search_words.move(100,50)
        print(self.search_words.text())

        self.search_label=QLabel(self)
        self.search_label.setText('Search Keywords')
        self.search_label.setFont(QFont('Arial',8))
        self.search_label.move(102,25)

        self.clear_button=QPushButton(self)
        self.clear_button.setText('Clear')
        self.clear_button.resize(70,30)
        self.clear_button.move(320,50)
        self.clear_button.clicked.connect(self.search_words.clear)

        self.page_number = QLineEdit(self)
        self.page_number.resize(200, 30)
        self.page_number.move(100, 100)

        self.pages_label = QLabel(self)
        self.pages_label.setText('Number of Pages')
        self.pages_label.setFont(QFont('Arial', 8))
        self.pages_label.move(102, 75)

        self.explanations_pages = QLabel(self)
        self.explanations_pages.setText("<font color='fade gray'>You can select up to 10 pages for scrapping the listings.If no value is provided-default: 5 pages</font>")
        self.explanations_pages.setWordWrap(True)
        self.explanations_pages.resize(200, 100)
        self.explanations_pages.move(102, 100)



        self.browse_button=QPushButton(self)
        self.browse_button.setText('Browse')
        self.browse_button.resize(70,30)
        self.browse_button.move(320,250)
        self.browse_button.clicked.connect(self.browse_file)

        self.custom_name = QLineEdit(self)

        self.custom_name.resize(200, 30)
        self.custom_name.move(100, 250)

        self.custom_label = QLabel(self)
        self.custom_label.setText('Custom Name')
        self.custom_label.setFont(QFont('Arial', 8))
        self.custom_label.move(102, 225)

        self.line=QFrame(self)
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Raised)
        self.line.setLineWidth(3)
        self.line.setFixedSize(510,3)
        self.line.move(0,200)

        self.explanations=QLabel(self)
        self.explanations.setText("<font color='fade gray'>If no custom name is provided than your search keywords will be used as the name for your results file</font>")
        self.explanations.setWordWrap(True)
        self.explanations.resize(200,100)
        self.explanations.move(102,260)


        self.run_button=QPushButton(self)
        self.run_button.setText('Scrape!')
        self.run_button.setFont(QFont('Arial',10))
        self.run_button.resize(100,30)
        self.run_button.move(200,350)
        self.run_button.setEnabled(False)

        self.run_button.clicked.connect(self.strat_scrapping)










app=QApplication(sys.argv)
app.setStyle('Fusion')
palette = QPalette()
palette.setColor(QPalette.Window, QColor(53, 53, 53))
palette.setColor(QPalette.WindowText, Qt.white)
palette.setColor(QPalette.Base, QColor(25, 25, 25))
palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
palette.setColor(QPalette.ToolTipBase, Qt.black)
palette.setColor(QPalette.ToolTipText, Qt.white)
palette.setColor(QPalette.Text, Qt.white)
palette.setColor(QPalette.Button, QColor(53, 53, 53))
palette.setColor(QPalette.ButtonText, Qt.white)
palette.setColor(QPalette.BrightText, Qt.red)
palette.setColor(QPalette.Link, QColor(42, 130, 218))
palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
palette.setColor(QPalette.HighlightedText, Qt.black)

app.setPalette(palette)

window=MainWindow()
window.SetupUi()
window.show()
sys.exit(app.exec())


