from PyQt5 import QtWidgets, uic
import sqlite3



# Definindo as funções
def verificar_login():
    principal.lbl_aviso.setText('')
    usuario = principal.lne_usuario.text()
    senha = principal.lne_senha.text()
    if usuario == 'andre' and senha == '123':
        principal.lne_usuario.setText('')
        principal.lne_senha.setText('')
        principal.close()
        logado.show()
    else:
        principal.lbl_aviso.setText('Usuário ou Senha incorretos')


def logout():
    logado.close()
    principal.show()


def sair_do_sistema():
    principal.close()


def formulario_cadastro():
    principal.lbl_aviso.setText('')
    principal.lne_usuario.setText('')
    principal.lne_senha.setText('')
    principal.close()
    cadastro.show()
    

def cancelar_cadastro():
    cadastro.close()
    principal.show()


def limpar_campos():
    cadastro.lne_nome.setText('')
    cadastro.lne_usuario.setText('')
    cadastro.lne_senha.setText('')
    cadastro.lne_c_senha.setText('')
    cadastro.lbl_aviso.setText('')


def cadastrar_usuario():
    nome = cadastro.lne_nome.text()
    usuario = cadastro.lne_usuario.text()
    senha = cadastro.lne_senha.text()
    c_senha = cadastro.lne_c_senha.text()

    if senha == c_senha:
        try:
            banco = sqlite3.connect('banco_cadastro.db')
            cursor = banco.cursor()
            cursor.execute('CREATE TABLE IF NOT EXISTS cadastro (nome text, usuario text, senha text)')
            cursor.execute('INSERT INTO cadastro VALUES ("'+nome+'", "'+usuario+'", "'+senha+'")')

            banco.commit()
            cursor.execute('SELECT * FROM cadastro')
            usuarios_cadastrados = cursor.fetchall()
            print(usuarios_cadastrados)
            cursor.close()
            banco.close()
            cadastro.lbl_aviso.setText('Usuário cadastrado com sucesso')
        
        except sqlite3.Error as erro:
            print('Erro ao inserir os dados: ', erro)
    else:
        cadastro.lbl_aviso.setText('As senhas digitadas estão diferentes')


app = QtWidgets.QApplication([])

# Associar os formulários a uma variável, para poder chamá-los no sistema
principal = uic.loadUi('login.ui')
logado = uic.loadUi('logado.ui')
cadastro = uic.loadUi('cadastro_usuario.ui')
cadastro_realizado = uic.loadUi('verificar_cadastro.ui')

# Associar os botões dos formulários a uma função específica
principal.btn_entrar.clicked.connect(verificar_login)
principal.btn_sair.clicked.connect(sair_do_sistema)
principal.btn_cadastrar.clicked.connect(formulario_cadastro)
logado.btn_encerrar.clicked.connect(logout)
cadastro.btn_cancelar.clicked.connect(cancelar_cadastro)
cadastro.btn_limpar.clicked.connect(limpar_campos)
cadastro.btn_cadastrar.clicked.connect(cadastrar_usuario)

# Início do programa 
principal.show()
app.exec()

