import PySimpleGUI as pg

class TelaPython:
    def __init__(self):
        pg.change_look_and_feel('Default')         #cores e tons da interface
        layout = [                                                                #definir tamanhos torna a interface padrão
            [pg.Text('Nome', size=(5,0)), pg.Input(size=(15,0), key='nome')],     #linha 1: o campo nome terá tamanho 5
            [pg.Text('Idade', size=(5,0)), pg.Input(size=(15,0), key='idade')],   #linha 2: o campo input terá o tamanho 15 
            [pg.Text('Quais provedores de e-mail você utiliza?')],                #linha 3
            [pg.Checkbox('Gmail',key='gmail'), pg.Checkbox('Outlook',key='outlook'), pg.Checkbox('Yahoo',key='yahoo')],
            [pg.Text('Aceita cartão?')],
            [pg.Radio('Sim', 'cartoes',key='aceitaCartao'),pg.Radio('Não','cartoes',key='naoAceitaCartao')],               #Ambos fazem parte do Radio 'cartoes'           
            [pg.Output(size=(30,20))],               #mostra os dados enviados na própria interface (logger)
            [pg.Button('Enviar Dados')],                                          #botão de enviar os dados
        ]

        self.janela = pg.Window('Dados do usuário').layout(layout)                     #cria uma janela com o layout criado acima

        #extrai os dados da tela
        self.button, self.values = self.janela.Read()
        
    def Iniciar(self):
        #o loop while serve para deixar a janela aberta e ficar buscando informações o tempo todo. 
        #Sem o loop, a janela é fechada assim que o botão "Enviar Dados" é pressionado
        while True:
            self.button,self.values = self.janela.Read()

            nome = self.values['nome']
            idade = self.values['idade']
            aceita_gmail = self.values['gmail']
            aceita_outlook = self.values['outlook']
            aceita_yahoo = self.values['yahoo']
            aceita_cartao = self.values['aceitaCartao']
            nao_aceita_cartao = self.values['naoAceitaCartao']

            #Apenas para a visualização da extração dos dados
            print(f'Nome:  {nome}')
            print(f'Idade:  {idade}')
            print(f'Aceita Gmail: {aceita_gmail}')
            print(f'Aceita Outlook: {aceita_outlook}')
            print(f'Aceita Yahoo: {aceita_yahoo}')
            print(f'Aceita Cartão: {aceita_cartao}')
            print(f'Não aceita cartão: {nao_aceita_cartao}')


tela = TelaPython()
tela.Iniciar()