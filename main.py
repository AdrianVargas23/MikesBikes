import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi


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
        print("Si entraste perrillo", email, password)
        self.gotoHomescreen()  # Call the method to go to HomeScreen

    def gotocreate(self):
        createacc = CreateAcc()
        widget.addWidget(createacc)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def gotoHomescreen(self):
        gotoHomeScreen = HomeScreen()
        widget.addWidget(gotoHomeScreen)
        widget.setCurrentIndex(widget.currentIndex() + 2)


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
            print("Succesfully created acc with email: ", email, " and password: ", password)
            self.close()  # Close the current window after creating account
            widget.setCurrentIndex(0)  # Return to Login window


class HomeScreen(QDialog):
    def __init__(self):
        super(HomeScreen, self).__init__()
        loadUi("homescreen.ui", self)
        #self.acceptButton.clicked.connect(self.rentBike)

    def rentBike(self):
        print("hola")
        #name = self.nameLineEdit.text()
        #phone = self.phoneLineEdit.text()
        #bikeID = self.bikeidComboBox.text()
        #date = self.dateEdit.text()
        #time = self.timeComboBox.text()
        #print(name + ", " + phone + ", " + bikeID + ", " + date + ", " + time)


app = QApplication(sys.argv)
mainwindow = Login()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(720)
widget.setFixedHeight(720)
widget.show()
app.exec_()
