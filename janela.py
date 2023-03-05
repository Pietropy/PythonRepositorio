from PyQt5 import uic, QtWidgets
import pyttsx3

def falar():
    engine.say(form.lineEdit.text())
    engine.runAndWait()
    engine.stop()

engine = pyttsx3.init()

app = QtWidgets.QApplication([])
form = uic.loadUi("Haya.ui")
form.pushButton.clicked.connect(falar)

form.show()
app.exec()