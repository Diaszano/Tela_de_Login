#-----------------------
# BIBLIOTECAS
#-----------------------
from PyQt5 import uic,QtWidgets
#-----------------------
# FUNÇÕES
#-----------------------
def chamarSegundaTela()->None:
    primeiraTela.mensagemDeErroLogin.setText("");
    nomeDeUsuario = primeiraTela.userLogin.text();
    senha = primeiraTela.senhaLogin.text();
    primeiraTela.userLogin.setText("");
    primeiraTela.senhaLogin.setText("");
    if(nomeDeUsuario == "Diaszano" and senha == "Senha01"):
        primeiraTela.close();
        segundaTela.show();
    else:
        primeiraTela.mensagemDeErroLogin.setText("Dados de login incorretos!");

def chamarCadastrarTela()->None:
    primeiraTela.close();
    cadastrarTela.show();

def cadastrar()->None:
    nome = cadastrarTela.nomeCadastrar.text();
    cadastrarTela.nomeCadastrar.setText("");
    print(nome);

def voltar():
    cadastrarTela.close();
    primeiraTela.show();

def logout():
    segundaTela.close();
    primeiraTela.show();
#-----------------------
# M A I N ()
#-----------------------
if __name__ == '__main__':
    app=QtWidgets.QApplication([]);
    primeiraTela=uic.loadUi("primeiraTela.ui");
    segundaTela=uic.loadUi("segundaTela.ui");
    cadastrarTela=uic.loadUi("cadastrarTela.ui");
    primeiraTela.botaoDeLogin.clicked.connect(chamarSegundaTela);
    primeiraTela.botaoDeCadastrarLogin.clicked.connect(chamarCadastrarTela);
    segundaTela.pushButton.clicked.connect(logout);
    cadastrarTela.VoltarCadastrar.clicked.connect(voltar);
    cadastrarTela.EntrarCadastrar.clicked.connect(cadastrar);
    primeiraTela.show();
    app.exec();
#-----------------------