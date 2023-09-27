
from PyQt5 import QtCore, QtGui, QtWidgets

import imgEk


class Ui_Form(object):
    def __init__(self):
        self.btn_ekle = None
        self.txt_seffaflik = None
        self.txt_mavi = None
        self.txt_yesil = None
        self.txt_kirmizi = None
        self.lbl_image = None
        self.lbl_bckcolor = None
        self.lbl_trans = None

    def setupUi(self, form):
        form.setObjectName("Form")
        form.resize(750, 595)
        self.lbl_bckcolor = QtWidgets.QLabel(form)
        self.lbl_bckcolor.setGeometry(QtCore.QRect(0, 0, 751, 601))
        self.lbl_bckcolor.setStyleSheet("background-color: rgb(189, 195, 199);")
        self.lbl_bckcolor.setText("")
        self.lbl_bckcolor.setObjectName("lbl_bckcolor")
        self.lbl_image = QtWidgets.QLabel(form)
        self.lbl_image.setGeometry(QtCore.QRect(120, 30, 451, 201))
        self.lbl_image.setStyleSheet("border-image: url(:/img/Nirvana-Wallpaper-14.jpg);")
        self.lbl_image.setText("")
        self.lbl_image.setObjectName("lbl_image")
        self.lbl_trans = QtWidgets.QLabel(form)
        self.lbl_trans.setGeometry(QtCore.QRect(110, 20, 471, 221))
        self.lbl_trans.setStyleSheet("background-color: rgb(85, 255, 127,20);")
        self.lbl_trans.setText("")
        self.lbl_trans.setObjectName("lbl_trans")
        self.txt_kirmizi = QtWidgets.QLineEdit(form)
        self.txt_kirmizi.setGeometry(QtCore.QRect(70, 281, 113, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.txt_kirmizi.setFont(font)
        self.txt_kirmizi.setMouseTracking(True)
        self.txt_kirmizi.setStyleSheet("background-color: rgb(255, 0, 0); border-radius: 5px; border-color:black;")
        self.txt_kirmizi.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_kirmizi.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.txt_kirmizi.setObjectName("txt_kirmizi")
        self.txt_yesil = QtWidgets.QLineEdit(form)
        self.txt_yesil.setGeometry(QtCore.QRect(210, 280, 113, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.txt_yesil.setFont(font)
        self.txt_yesil.setMouseTracking(True)
        self.txt_yesil.setStyleSheet("background-color: rgb(0, 255, 0);border-radius: 5px; border-color:black;")
        self.txt_yesil.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_yesil.setDragEnabled(False)
        self.txt_yesil.setReadOnly(False)
        self.txt_yesil.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.txt_yesil.setObjectName("txt_yesil")
        self.txt_mavi = QtWidgets.QLineEdit(form)
        self.txt_mavi.setGeometry(QtCore.QRect(360, 280, 113, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.txt_mavi.setFont(font)
        self.txt_mavi.setMouseTracking(True)
        self.txt_mavi.setStyleSheet("background-color: rgb(0, 0, 255);border-radius: 5px; border-color:black;")
        self.txt_mavi.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_mavi.setReadOnly(False)
        self.txt_mavi.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.txt_mavi.setObjectName("txt_mavi")
        self.txt_seffaflik = QtWidgets.QLineEdit(form)
        self.txt_seffaflik.setGeometry(QtCore.QRect(510, 280, 113, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.txt_seffaflik.setFont(font)
        self.txt_seffaflik.setMouseTracking(True)
        self.txt_seffaflik.setStyleSheet("background-color: rgb(149, 165, 166);border-radius: 5px; border-color:black;")
        self.txt_seffaflik.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_seffaflik.setReadOnly(False)
        self.txt_seffaflik.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.txt_seffaflik.setObjectName("txt_seffaflik")
        self.btn_ekle = QtWidgets.QPushButton(form)
        self.btn_ekle.setGeometry(QtCore.QRect(280, 360, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_ekle.setFont(font)
        self.btn_ekle.setStyleSheet("border-color:black;" "border-radius:5px;" "background-color: rgb(78, 80, 78);" "color:white;")
        self.btn_ekle.setObjectName("btn_ekle")
        self.btn_ekle.clicked.connect(self.ekle)
        self.retranslateUi(form)
        QtCore.QMetaObject.connectSlotsByName(form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.txt_kirmizi.setPlaceholderText(_translate("Form", "Kırmızı"))
        self.txt_yesil.setPlaceholderText(_translate("Form", "Yeşil"))
        self.txt_mavi.setPlaceholderText(_translate("Form", "Mavi"))
        self.txt_seffaflik.setPlaceholderText(_translate("Form", "Şeffaflık"))
        self.btn_ekle.setText(_translate("Form", "EKLE"))

    def ekle(self):
        r = self.txt_kirmizi.text()
        g = self.txt_yesil.text()
        b = self.txt_mavi.text()
        t = self.txt_seffaflik.text()
        """print(r,g,b,t)"""
        self.lbl_trans.setStyleSheet("background-color: rgb({},{},{},{});".format(r,g,b,t))
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
