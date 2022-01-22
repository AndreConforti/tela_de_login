from PyQt5 import QtWidgets, uic






app = QtWidgets.QApplication([])
login = uic.loadUi('login.ui')
logado = uic.loadUi('logado.ui')
#login.btn_entrar.clicked.connect(verificar login)


login.show()
app.exec()