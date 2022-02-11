from cmath import log
from PyQt5 import QtWidgets, uic
import mysql.connector

banco = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '',
    database = 'banco_cadastro'
)

def verificar_login():
    login.lbl_aviso.setText("")
    usuario = login.lne_usuario.text().upper().strip()
    senha = login.lne_senha.text().strip()

    try:
        cursor = banco.cursor()
        cursor.execute("SELECT senha FROM cadastro WHERE login = '{}'".format(usuario))
        senha_bd = cursor.fetchall()
        print(senha_bd[0][0])
    except:
        login.lbl_aviso.setText("Usuário não está cadastrado no Sistema")

    '''if senha == senha_bd[0][0]:
        login.close()
        logado.show()
    else:
        login.lbl_aviso.setText("Senha não confere")'''

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

    if senha == c_senha:
        try:
            cursor = banco.cursor()
            cursor.execute("INSERT INTO cadastro VALUES ('"+nome+"', '"+usuario+"', '"+senha+"')")

            banco.commit()
            banco.close()
            cadastro.lbl_aviso.setText("Usuário cadastrado com sucesso!")
        
        except mysql.connector.Error as erro:
            print("Erro ao inserir os dados: ", erro)

    else:
        cadastro.lbl_aviso.setText("As senhas estão diferentes. Repita a senha corretamente")


def verificar_cadastro():
    cadastro.close()
    confirma_cadastro.show()


def cancelar_cadastro():
    cadastro.lne_nome.setText("")
    cadastro.lne_usuario.setText("")
    cadastro.lne_senha.setText("")
    cadastro.lne_rptsenha.setText("")
    cadastro.lbl_aviso.setText("")
    cadastro.close()
    login.show()


def limpar_cadastro():
    cadastro.lne_nome.setText("")
    cadastro.lne_usuario.setText("")
    cadastro.lne_senha.setText("")
    cadastro.lne_rptsenha.setText("")
    cadastro.lbl_aviso.setText("")

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
cadastro.btn_cancelar.clicked.connect(cancelar_cadastro)
cadastro.btn_limpar.clicked.connect(limpar_cadastro)
confirma_cadastro.btn_voltar.clicked.connect(voltar_login)


login.show()
app.exec()