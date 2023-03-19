import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi
import pyrebase

firebaseConfig={
    'apiKey': "AIzaSyCjvh2Ka6B1cIdDWgOzANa1SSG8sCs3P0c",
    'authDomain': "mike-sbikes.firebaseapp.com",
    'projectId': "mike-sbikes",
    'storageBucket': "mike-sbikes.appspot.com",
    'messagingSenderId': "578901172163",
    'appId': "1:578901172163:web:f9d62d14d3b42c690d2776",
    'measurementId': "G-ZGYHQ01XQ1"}

firebase=pyrebase.initialize_app(firebaseConfig)

auth=firebase.auth()


class Login(QDialog):
    def __init__(self):
        super(Login, self).__init__()
        loadUi("login.ui", self)
        self.loginButton.clicked.connect(self.loginfunction)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.createaccButton.clicked.connect(self.gotocreate)


    def loginfunction(self):
        email = self.email.text()
        password = self.password.text()
        print("Si entraste perrillo")

    def gotocreate(self):
        createacc=CreateAcc()
        widget.addWidget(createacc)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def gotoHomescreen(self):
        gotoHomeScreen = HomeScreen()
        widget.addWidget(gotoHomeScreen)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class CreateAcc(QDialog):
    def __init__(self):
        super(CreateAcc,self).__init__()
        loadUi("createacc.ui", self)
        self.signupButton.clicked.connect(self.createaccfunction)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmPassword.setEchoMode(QtWidgets.QLineEdit.Password)


    def createaccfunction(self):
        email=self.email.text()
        if self.password.text()==self.confirmPassword.text():
            password=self.password.text()
            auth.create_user_with_email_and_password(email, password)
            login=Login()
            widget.addWidget(login)
            widget.setCurrentIndex(widget.currentIndex()+1)



class HomeScreen(QDialog):
    def __init__(self):
        super(HomeScreen, self).__init__()
        loadUi("homescreen.ui", self)
        self.acceptButton.clicked.connect(self.rentBike)

    def rentBike(self):
        name = self.nameLineEdit.text()
        phone = self.phoneLineEdit.text()
        bikeID = self.bikeidComboBox.text()
        date = self.dateEdit.text()
        time = self.timeComboBox.text()
        print(name + ", " + phone + ", " + bikeID + ", " + date + ", " + time)


app = QApplication(sys.argv)
mainwindow = Login()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(480)
widget.setFixedHeight(620)
widget.show()
app.exec_()

#comentario pedorro nomas para asegurarme de hacer el commit nuevo