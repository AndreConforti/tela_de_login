from cmath import log
from PyQt5 import QtWidgets, uic
import sqlite3

def verificar_login():
    login.lbl_aviso.setText("")
    usuario = login.lne_usuario.text().upper().strip()
    senha = login.lne_senha.text().strip()
    if usuario == "ANDRE" and senha == "123":
        login.lne_usuario.setText("")
        login.lne_senha.setText("")
        login.close()
        logado.show()
    else:
        login.lbl_aviso.setText("Dados de login incorretos")


def sair_do_sistema():
    login.close()


def logout():
    logado.close()
    login.show()


def chamar_cadastro():
    login.lbl_aviso.setText("")
    login.lne_usuario.setText("")
    login.lne_senha.setText("")
    login.close()
    cadastro.show()


def cadastrar_usuario():
    nome = cadastro.lne_nome.text()
    usuario = cadastro.lne_usuario.text()
    senha = cadastro.lne_senha.text()
    c_senha = cadastro.lne_rptsenha.text()

    print(nome, usuario, senha, c_senha)


def verificar_cadastro():
    cadastro.close()
    confirma_cadastro.show()


def cancelar_cadastro():
    cadastro.lne_nome.setText("")
    cadastro.lne_usuario.setText("")
    cadastro.lne_senha.setText("")
    cadastro.lne_rptsenha.setText("")
    cadastro.close()
    login.show()


def voltar_login():
    confirma_cadastro.close()
    login.show()


app = QtWidgets.QApplication([])

login = uic.loadUi('login.ui')
logado = uic.loadUi('logado.ui')
cadastro = uic.loadUi('cadastro_usuario.ui')
confirma_cadastro = uic.loadUi('verificar_cadastro.ui')

login.btn_entrar.clicked.connect(verificar_login)
login.btn_sair.clicked.connect(sair_do_sistema)
login.btn_cadastrar.clicked.connect(chamar_cadastro)
logado.btn_encerrar.clicked.connect(logout)
cadastro.btn_cadastrar.clicked.connect(cadastrar_usuario)
cadastro.btn_voltar.clicked.connect(cancelar_cadastro)
confirma_cadastro.btn_voltar.clicked.connect(voltar_login)

login.show()
app.exec()