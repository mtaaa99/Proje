import sys
import os
import time
from PyQt5.QtWidgets import QWidget,QTextEdit,QLabel,QPushButton,QVBoxLayout,QFileDialog,QHBoxLayout
from PyQt5.QtWidgets import QSplashScreen,QApplication,QInputDialog,QAction,qApp,QMainWindow,QLineEdit
from PyQt5.QtGui import QPixmap,QPainter,QColor,QFont
from PyQt5.QtCore import Qt,QTimer


class Pencere(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):

        self.label = QLabel("Futbolcular Programına Hoşgeldiniz")
        self.ekle = QPushButton("Ekle")
        self.temizle = QPushButton("Temizle")
        self.cikis = QPushButton("ÇIKIŞ")
        self.resim_etiketi = QLabel(self)
        pixmap = QPixmap("/home/mta/İndirilenler/logo.jpg")
        self.resim_etiketi.setPixmap(pixmap)
        self.resim_etiketi.setAlignment(Qt.AlignCenter)

        h_box = QHBoxLayout()
        h_box.addWidget(self.temizle)
        h_box.addWidget(self.ekle)
        h_box.addWidget(self.cikis)

        v_box = QVBoxLayout()
        v_box.addWidget(self.label)
        v_box.addWidget(self.resim_etiketi)
        v_box.addStretch()
        v_box.addLayout(h_box)

        self.setLayout(v_box)
        self.temizle.clicked.connect(self.yaziyi_temizle)
        self.ekle.clicked.connect(self.oyuncu_ekle)
        self.cikis.clicked.connect(self.cikis_yap)

    def cikis_yap(self):
        self.durum_etiketi = QLabel("Program kapatılıyor...", self)
        font = QFont("Arial", 20)
        self.durum_etiketi.setFont(font)
        self.durum_etiketi.setAlignment(Qt.AlignCenter)
        self.durum_etiketi.setGeometry(0, self.height() - 90, self.width(), 30)
        self.durum_etiketi.show()

        self.timer = QTimer()
        self.timer.timeout.connect(self.close_app)
        self.timer.start(2000)

    def close_app(self):
        qApp.quit()

    def yaziyi_temizle(self):
        self.edit.clear()

    def oyuncu_ekle(self):
        adı, okPressed = QInputDialog.getText(self, "Input Dialog", "Oyuncun Adı:")
        mevki, okPressed = QInputDialog.getText(self, "Input Dialog", "Mevkisi:")
        yas, okPressed = QInputDialog.getText(self, "Input Dialog", "Oyuncun Yaşı:")
        takım, okPressed = QInputDialog.getText(self, "Input Dialog", "Oyuncun Takımı:")
        oyuncu_bilgisi = f"{adı},{mevki},{yas},{takım}\n"
        with open("Oyuncular.txt", "a") as dosya:
            dosya.write(oyuncu_bilgisi)
            time.sleep(2)
        print("Oyuncu dosyaya eklendi.")



class Menu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700,200,500,500)
        self.pencere = Pencere()
        self.setCentralWidget(self.pencere)
        self.menuleri_olustur()

    def menuleri_olustur(self):
        menubar = self.menuBar()
        fener = menubar.addMenu("Fenerbahçe")
        gs = menubar.addMenu("Galatasaray")

        kaleci = QAction("Kaleci",self)
        defans = QAction("Defans", self)
        orta_saha = QAction("Orta Saha",self)
        forvet = QAction("Forvet",self)

        fener.addAction(kaleci)
        fener.addAction(defans)
        fener.addAction(orta_saha)
        fener.addAction(forvet)
        fener.triggered.connect(self.response_fb)

        gs.addAction(kaleci)
        gs.addAction(defans)
        gs.addAction(orta_saha)
        gs.addAction(forvet)
        gs.triggered.connect(self.response_gs)

        self.setWindowTitle("Futbolcu Reytingleri")
        self.show()

    def response_fb(self,action1):
        with open("Oyuncular.txt","r",encoding="utf-8") as file:
            for satir in file:
                satir = satir.strip()
                liste = satir.split(",")
                isim = liste[0]
                mevki = liste[1]
                yas = liste[2]
                takim = liste[3]
                if action1.text() == "Kaleci" and mevki == "Kaleci" and takim == "Fenerbahçe":
                    print(satir)
                elif action1.text() == "Defans" and mevki == "Defans" and takim == "Fenerbahçe":
                    print(satir)
                elif action1.text() == "Orta Saha" and mevki == "Orta Saha" and takim == "Fenerbahçe":
                    print(satir)
                elif action1.text() == "Forvet" and mevki == "Forvet" and takim == "Fenerbahçe":
                    print(satir)

    def response_gs(self, action2):
        with open("Oyuncular.txt", "r", encoding="utf-8") as file2:
            for satir in file2:
                satir = satir.strip()
                liste = satir.split(",")
                isim = liste[0]
                mevki = liste[1]
                yas = liste[2]
                takim = liste[3]
                if action2.text() == "Kaleci" and mevki == "Kaleci" and takim == "Galatasaray":
                    print(satir)
                elif action2.text() == "Defans" and mevki == "Defans" and takim == "Galatasaray":
                    print(satir)
                elif action2.text() == "Orta Saha" and mevki == "Orta Saha" and takim == "Galatasaray":
                    print(satir)
                elif action2.text() == "Forvet" and mevki == "Forvet" and takim == "Galatasaray":
                    print(satir)

app = QApplication(sys.argv)
menu = Menu()
sys.exit(app.exec())