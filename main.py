from tkinter import *
from b.funcoes import *
from b.recibo import *
from b.criabanco import *
from tkinter import ttk
from b.Funcs import *
import b.inicial

root = Tk()
b.inicial.init()

class Application(Funcs):
    def __init__(self):
        self.root0 = root
        self.tela()
        root.mainloop()
    def tela(self):

        self.root0.title("BDViagens")
        self.root0.configure(background= '#1e3743')
        self.root0.state('zoomed')

        self.frame_1 = Frame(self.root0, bd = 4, bg= '#dfe3ee',
                             highlightbackground= '#759fe6', highlightthickness=3 )
        self.frame_1.place(relx= 0.02, rely=0.02, relwidth= 0.96, relheight= 0.96)

        self.lb_ReservaIdA = Label(self.frame_1, text="BDViagens",font = ('verdana', 20, 'bold'), bg='#dfe3ee', fg='#107db2',)
        self.lb_ReservaIdA.place(relx=0.25, rely=0.1,relwidth=0.5, relheight=0.10)

        ### Criação do botao Entrar
        self.bt_cliente = Button(self.frame_1, text="Entrar", bd=2, bg = '#107db2',fg = 'white'
                                , font = ('verdana', 8, 'bold'), command = self.Intermediario)
        self.bt_cliente.place(relx=0.40, rely=0.5, relwidth=0.2, relheight=0.10)

        ## Criação da label e entrada do Usuario
        self.lb_Usuario = Label(self.frame_1, text="Usuario", bg='#dfe3ee', fg='#107db2')
        self.lb_Usuario.place(relx=0.40, rely=0.3)

        self.Usuario_entry = Entry(self.frame_1)
        self.Usuario_entry.place(relx=0.44, rely=0.3, relwidth=0.1)

        ## Criação da label e entrada da Senha
        self.lb_Senha = Label(self.frame_1, text="Senha", bg='#dfe3ee', fg='#107db2')
        self.lb_Senha.place(relx=0.40, rely=0.4)

        self.Senha_entry = Entry(self.frame_1)
        self.Senha_entry.place(relx=0.44, rely=0.4, relwidth=0.1)




    def cliente(self):
        self.root2 = Toplevel()
        self.root2.state('zoomed')
        self.root2.title("Cliente")
        self.root2.configure(background='#1e3743')
        self.root2.transient(self.root)
        self.root2.focus_force()
        self.root2.grab_set()
        self.frame_1 = Frame(self.root2, bd=4, bg='#dfe3ee',
                             highlightbackground='#759fe6', highlightthickness=3)
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)

        self.frame_2 = Frame(self.root2, bd=4, bg='#dfe3ee',
                             highlightbackground='#759fe6', highlightthickness=3)
        self.frame_2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)

        ### Criação do botao limpar
        self.bt_limpar = Button(self.frame_1, text="Limpar", bd=2, bg='#107db2', fg='white'
                                , font=('verdana', 8, 'bold'), command=self.limpaCliente)
        self.bt_limpar.place(relx=0.4, rely=0.1, relwidth=0.1, relheight=0.15)
        ### Criação do botao buscar
        self.bt_buscar = Button(self.frame_1, text="Buscar", bd=2, bg='#107db2', fg='white'
                                , font=('verdana', 8, 'bold'), command=self.buscaCliente)
        self.bt_buscar.place(relx=0.3, rely=0.1, relwidth=0.1, relheight=0.15)
        ### Criação do botao novo
        self.bt_novo = Button(self.frame_1, text="Inserir", bd=2, bg='#107db2', fg='white'
                              , font=('verdana', 8, 'bold'), command=self.insereCliente)
        self.bt_novo.place(relx=0.6, rely=0.1, relwidth=0.1, relheight=0.15)
        ### Criação do botao alterar
        self.bt_alterar = Button(self.frame_1, text="Alterar", bd=2, bg='#107db2', fg='white'
                                 , font=('verdana', 8, 'bold'), command=self.alteraCliente)
        self.bt_alterar.place(relx=0.7, rely=0.1, relwidth=0.1, relheight=0.15)
        ### Criação do botao apagar
        self.bt_apagar = Button(self.frame_1, text="Apagar", bd=2, bg='#107db2', fg='white'
                                , font=('verdana', 8, 'bold'), command=self.deletaCliente)
        self.bt_apagar.place(relx=0.8, rely=0.1, relwidth=0.1, relheight=0.15)

        ### Criação do recibo
        self.bt_recibo = Button(self.frame_1, text="Recibo", bd=2, bg='#107db2', fg='white'
                                , font=('verdana', 8, 'bold'), command=self.geraRecibo)
        self.bt_recibo.place(relx=0.8, rely=0.8, relwidth=0.1, relheight=0.15)

        ## Criação da label e entrada do codigo
        self.lb_CPF = Label(self.frame_1, text="CPF", bg='#dfe3ee', fg='#107db2')
        self.lb_CPF.place(relx=0.05, rely=0.05)

        self.codigo_entry = Entry(self.frame_1)
        self.codigo_entry.place(relx=0.05, rely=0.15, relwidth=0.2)

        ## Criação da label e entrada do nome
        self.lb_nome = Label(self.frame_1, text="Nome", bg='#dfe3ee', fg='#107db2')
        self.lb_nome.place(relx=0.05, rely=0.3)

        self.nome_entry = Entry(self.frame_1)
        self.nome_entry.place(relx=0.05, rely=0.40, relwidth=0.3)

        ## Criação da label e entrada do sobrenome
        self.lb_sobrenome = Label(self.frame_1, text="Sobrenome", bg='#dfe3ee', fg='#107db2')
        self.lb_sobrenome.place(relx=0.37, rely=0.3)

        self.sobrenome_entry = Entry(self.frame_1)
        self.sobrenome_entry.place(relx=0.37, rely=0.40, relwidth=0.3)

        ## Criação da label e entrada do data
        self.lb_data = Label(self.frame_1, text="Data de nascimento", bg='#dfe3ee', fg='#107db2')
        self.lb_data.place(relx=0.69, rely=0.3)

        self.data_entry = Entry(self.frame_1)
        self.data_entry.place(relx=0.69, rely=0.40, relwidth=0.2)

        ## Criação da label e entrada do Endereço
        self.lb_cidade = Label(self.frame_1, text="Endereço", bg='#dfe3ee', fg='#107db2')
        self.lb_cidade.place(relx=0.05, rely=0.55)

        self.cidade_entry = Entry(self.frame_1)
        self.cidade_entry.place(relx=0.05, rely=0.65, relwidth=0.3)

        ## Criação da label e entrada da telefone
        self.lb_telefone = Label(self.frame_1, text="Telefone", bg='#dfe3ee', fg='#107db2')
        self.lb_telefone.place(relx=0.37, rely=0.55)

        self.fone_entry = Entry(self.frame_1)
        self.fone_entry.place(relx=0.37, rely=0.65, relwidth=0.3)

        ## Criação da label e entrada do EMail
        self.lb_EMail = Label(self.frame_1, text="EMail", bg='#dfe3ee', fg='#107db2')
        self.lb_EMail.place(relx=0.05, rely=0.8)

        self.EMail_entry = Entry(self.frame_1)
        self.EMail_entry.place(relx=0.05, rely=0.9, relwidth=0.3)

        ## Criação da label e entrada do Passaporte
        self.lb_passaporte = Label(self.frame_1, text="Passaporte", bg='#dfe3ee', fg='#107db2')
        self.lb_passaporte.place(relx=0.37, rely=0.8)

        self.passaporte_entry = Entry(self.frame_1)
        self.passaporte_entry.place(relx=0.37, rely=0.90, relwidth=0.3)

        self.listaCli = ttk.Treeview(self.frame_2, height=3,
                                     column=("col1", "col2", "col3", "col4", "col5", "col6", "col7", "col8"))
        self.listaCli.heading("#0", text="")
        self.listaCli.heading("#1", text="Nome")
        self.listaCli.heading("#2", text="Sobrenome")
        self.listaCli.heading("#3", text="CPF")
        self.listaCli.heading("#4", text="Passaporte")
        self.listaCli.heading("#5", text="Data de nascimento")
        self.listaCli.heading("#6", text="Telefone")
        self.listaCli.heading("#7", text="EMail")
        self.listaCli.heading("#8", text="Endereço")
        
        self.listaCli.column("#0", width=1)
        self.listaCli.column("#1", width=10)
        self.listaCli.column("#2", width=10)
        self.listaCli.column("#3", width=10)
        self.listaCli.column("#4", width=10)
        self.listaCli.column("#5", width=35)
        self.listaCli.column("#6", width=10)
        self.listaCli.column("#7", width=150)
        self.listaCli.column("#8", width=200)
        self.listaCli.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)

        self.scroolLista = Scrollbar(self.frame_2, orient='vertical')
        self.listaCli.configure(yscroll=self.scroolLista.set)
        self.scroolLista.place(relx=0.96, rely=0.1, relwidth=0.02, relheight=0.85)
        self.listaCli.bind("<Double-1>", self.OnDoubleClickCliente)

        self.mostraCliente()

    def reserva(self):
        self.root3 = Toplevel()
        self.root3.state('zoomed')
        self.root3.title("Reserva")
        self.root3.configure(background='#1e3743')
        self.root3.transient(self.root)
        self.root3.focus_force()
        self.root3.grab_set()

        ### Criação do frames 3 e 4 limpar

        self.frame_3 = Frame(self.root3, bd=4, bg='#dfe3ee',
                             highlightbackground='#759fe6', highlightthickness=3)
        self.frame_3.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)

        self.frame_4 = Frame(self.root3, bd=4, bg='#dfe3ee',
                             highlightbackground='#759fe6', highlightthickness=3)
        self.frame_4.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)

        ### Criação do botao limpar
        self.bt_limpar = Button(self.frame_3, text="Limpar", bd=2, bg='#107db2', fg='white'
                                , font=('verdana', 8, 'bold'), command=self.limpaReserva)
        self.bt_limpar.place(relx=0.4, rely=0.1, relwidth=0.1, relheight=0.15)
        ### Criação do botao buscar
        self.bt_buscar = Button(self.frame_3, text="Buscar", bd=2, bg='#107db2', fg='white'
                                , font=('verdana', 8, 'bold'), command=self.buscaReserva)
        self.bt_buscar.place(relx=0.3, rely=0.1, relwidth=0.1, relheight=0.15)
        ### Criação do botao novo
        self.bt_novo = Button(self.frame_3, text="Inserir", bd=2, bg='#107db2', fg='white'
                              , font=('verdana', 8, 'bold'), command=self.insereReserva)
        self.bt_novo.place(relx=0.6, rely=0.1, relwidth=0.1, relheight=0.15)
        ### Criação do botao alterar
        self.bt_alterar = Button(self.frame_3, text="Alterar", bd=2, bg='#107db2', fg='white'
                                 , font=('verdana', 8, 'bold'), command=self.alteraReserva)
        self.bt_alterar.place(relx=0.7, rely=0.1, relwidth=0.1, relheight=0.15)
        ### Criação do botao apagar
        self.bt_apagar = Button(self.frame_3, text="Apagar", bd=2, bg='#107db2', fg='white'
                                , font=('verdana', 8, 'bold'), command=self.deletaReserva)
        self.bt_apagar.place(relx=0.8, rely=0.1, relwidth=0.1, relheight=0.15)

        ## Criação da label e idReserva
        self.lb_idReserva = Label(self.frame_3, text="ID da reserva", bg='#dfe3ee', fg='#107db2')
        self.lb_idReserva.place(relx=0.05, rely=0.05)

        self.idReserva_entry = Entry(self.frame_3)
        self.idReserva_entry.place(relx=0.05, rely=0.15, relwidth=0.08)

        ## Criação da label e entrada do Status
        self.lb_status = Label(self.frame_3, text="Status", bg='#dfe3ee', fg='#107db2')
        self.lb_status.place(relx=0.05, rely=0.3)

        self.status_entry = Entry(self.frame_3)
        self.status_entry.place(relx=0.05, rely=0.40, relwidth=0.3)


        ## Criação da label e entrada da dataReserva
        self.lb_dataReserva = Label(self.frame_3, text="Data reservada", bg='#dfe3ee', fg='#107db2')
        self.lb_dataReserva.place(relx=0.05, rely=0.55)

        self.dataReserva_entry = Entry(self.frame_3)
        self.dataReserva_entry.place(relx=0.05, rely=0.65, relwidth=0.3)

        ## Criação da label e entrada do viagemID
        self.lb_viagemID = Label(self.frame_3, text="ID da viagem", bg='#dfe3ee', fg='#107db2')
        self.lb_viagemID.place(relx=0.05, rely=0.8)

        self.viagemID_entry = Entry(self.frame_3)
        self.viagemID_entry.place(relx=0.05, rely=0.9, relwidth=0.3)

        self.listaCli = ttk.Treeview(self.frame_4, height=3,
                                     column=("col1", "col2", "col3", "col4"))
        self.listaCli.heading("#0", text="")
        self.listaCli.heading("#1", text="ID da reserva")
        self.listaCli.heading("#2", text="Status")
        self.listaCli.heading("#3", text="Data reservada")
        self.listaCli.heading("#4", text="ID da viagem")
        self.listaCli.column("#0", width=1)
        self.listaCli.column("#1", width=50)
        self.listaCli.column("#2", width=50)
        self.listaCli.column("#3", width=50)
        self.listaCli.column("#4", width=50)
        self.listaCli.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)

        self.scroolLista = Scrollbar(self.frame_4, orient='vertical')
        self.listaCli.configure(yscroll=self.scroolLista.set)
        self.scroolLista.place(relx=0.96, rely=0.1, relwidth=0.02, relheight=0.85)
        self.listaCli.bind("<Double-1>", self.OnDoubleClickReserva)

        self.mostraReserva()

    def passagens(self):
        self.root4 = Toplevel()
        self.root4.state('zoomed')
        self.root4.title("Passagens")
        self.root4.configure(background='#1e3743')
        self.root4.transient(self.root)
        self.root4.focus_force()
        self.root4.grab_set()

        self.frame_5 = Frame(self.root4, bd=4, bg='#dfe3ee',
                             highlightbackground='#759fe6', highlightthickness=3)
        self.frame_5.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)

        self.frame_6 = Frame(self.root4, bd=4, bg='#dfe3ee',
                             highlightbackground='#759fe6', highlightthickness=3)
        self.frame_6.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)

        ### Criação do botao limpar
        self.bt_limpar = Button(self.frame_5, text="Limpar", bd=2, bg='#107db2', fg='white'
                                , font=('verdana', 8, 'bold'), command=self.limpaPassagem)
        self.bt_limpar.place(relx=0.4, rely=0.1, relwidth=0.1, relheight=0.15)
        ### Criação do botao buscar
        self.bt_buscar = Button(self.frame_5, text="Buscar", bd=2, bg='#107db2', fg='white'
                                , font=('verdana', 8, 'bold'), command=self.buscaPassagem)
        self.bt_buscar.place(relx=0.3, rely=0.1, relwidth=0.1, relheight=0.15)
        ### Criação do botao novo
        self.bt_novo = Button(self.frame_5, text="Inserir", bd=2, bg='#107db2', fg='white'
                              , font=('verdana', 8, 'bold'), command=self.inserePassagem)
        self.bt_novo.place(relx=0.6, rely=0.1, relwidth=0.1, relheight=0.15)
        ### Criação do botao alterar
        self.bt_alterar = Button(self.frame_5, text="Alterar", bd=2, bg='#107db2', fg='white'
                                 , font=('verdana', 8, 'bold'), command=self.alteraPassagem)
        self.bt_alterar.place(relx=0.7, rely=0.1, relwidth=0.1, relheight=0.15)
        ### Criação do botao apagar
        self.bt_apagar = Button(self.frame_5, text="Apagar", bd=2, bg='#107db2', fg='white'
                                , font=('verdana', 8, 'bold'), command=self.deletaPassagem)
        self.bt_apagar.place(relx=0.8, rely=0.1, relwidth=0.1, relheight=0.15)

        ## Criação da label e entrada do idPassagem
        self.lb_idPassagem = Label(self.frame_5, text="ID da passagem", bg='#dfe3ee', fg='#107db2')
        self.lb_idPassagem.place(relx=0.05, rely=0.05)

        self.idPassagem_entry = Entry(self.frame_5)
        self.idPassagem_entry.place(relx=0.05, rely=0.15, relwidth=0.08)

        ## Criação da label e entrada do Tipo
        self.lb_Tipo = Label(self.frame_5, text="Tipo", bg='#dfe3ee', fg='#107db2')
        self.lb_Tipo.place(relx=0.05, rely=0.3)

        self.Tipo_entry = Entry(self.frame_5)
        self.Tipo_entry.place(relx=0.05, rely=0.40, relwidth=0.3)

        ## Criação da label e entrada do Empresa
        self.lb_Empresa = Label(self.frame_5, text="Empresa", bg='#dfe3ee', fg='#107db2')
        self.lb_Empresa.place(relx=0.37, rely=0.3)

        self.Empresa_entry = Entry(self.frame_5)
        self.Empresa_entry.place(relx=0.37, rely=0.40, relwidth=0.3)

        ## Criação da label e entrada do Embarque
        self.lb_Embarque = Label(self.frame_5, text="Embarque", bg='#dfe3ee', fg='#107db2')
        self.lb_Embarque.place(relx=0.69, rely=0.3)

        self.data_Embarque = Entry(self.frame_5)
        self.data_Embarque.place(relx=0.69, rely=0.40, relwidth=0.2)

        ## Criação da label e entrada do HorarioEmbarque
        self.lb_HorarioEmbarque = Label(self.frame_5, text="Horario do embarque", bg='#dfe3ee', fg='#107db2')
        self.lb_HorarioEmbarque.place(relx=0.05, rely=0.55)

        self.HorarioEmbarque_entry = Entry(self.frame_5)
        self.HorarioEmbarque_entry.place(relx=0.05, rely=0.65, relwidth=0.3)

        ## Criação da label e entrada da Preço
        self.lb_Preco = Label(self.frame_5, text="Preço", bg='#dfe3ee', fg='#107db2')
        self.lb_Preco.place(relx=0.37, rely=0.55)

        self.Preco_entry = Entry(self.frame_5)
        self.Preco_entry.place(relx=0.37, rely=0.65, relwidth=0.3)

        ## Criação da label e entrada do Assento
        self.lb_Assento = Label(self.frame_5, text="Assento", bg='#dfe3ee', fg='#107db2')
        self.lb_Assento.place(relx=0.05, rely=0.8)

        self.Assento_entry = Entry(self.frame_5)
        self.Assento_entry.place(relx=0.05, rely=0.9, relwidth=0.3)

        ## Criação da label e entrada do RerservaID
        self.lb_ReservaID = Label(self.frame_5, text="ID da rerserva", bg='#dfe3ee', fg='#107db2')
        self.lb_ReservaID.place(relx=0.37, rely=0.8)

        self.ReservaID_entry = Entry(self.frame_5)
        self.ReservaID_entry.place(relx=0.37, rely=0.90, relwidth=0.3)

        self.listaCli = ttk.Treeview(self.frame_6, height=3,
                                     column=("col1", "col2", "col3", "col4", "col5", "col6", "col7", "col8"))
        self.listaCli.heading("#0", text="")
        self.listaCli.heading("#1", text="ID da passagem")
        self.listaCli.heading("#2", text="Tipo")
        self.listaCli.heading("#3", text="Empresa")
        self.listaCli.heading("#4", text="Embarque")
        self.listaCli.heading("#5", text="Horario do embarque")
        self.listaCli.heading("#6", text="Preço")
        self.listaCli.heading("#7", text="Assento")
        self.listaCli.heading("#8", text="ID da rerserva")
        self.listaCli.column("#0", width=1)
        self.listaCli.column("#1", width=50)
        self.listaCli.column("#2", width=50)
        self.listaCli.column("#3", width=50)
        self.listaCli.column("#4", width=50)
        self.listaCli.column("#5", width=50)
        self.listaCli.column("#6", width=50)
        self.listaCli.column("#7", width=50)
        self.listaCli.column("#8", width=50)
        self.listaCli.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)

        self.scroolLista = Scrollbar(self.frame_6, orient='vertical')
        self.listaCli.configure(yscroll=self.scroolLista.set)
        self.scroolLista.place(relx=0.96, rely=0.1, relwidth=0.02, relheight=0.85)
        self.listaCli.bind("<Double-1>", self.OnDoubleClickPassagem)

        self.mostraPassagem()

    def viagem(self):
        self.root5 = Toplevel()
        self.root5.state('zoomed')
        self.root5.title("Viagem")
        self.root5.configure(background='#1e3743')
        self.root5.transient(self.root)
        self.root5.focus_force()
        self.root5.grab_set()

        self.frame_7 = Frame(self.root5, bd=4, bg='#dfe3ee',
                             highlightbackground='#759fe6', highlightthickness=3)
        self.frame_7.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)

        self.frame_8 = Frame(self.root5, bd=4, bg='#dfe3ee',
                             highlightbackground='#759fe6', highlightthickness=3)
        self.frame_8.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)

        ### Criação do botao limpar
        self.bt_limpar = Button(self.frame_7, text="Limpar", bd=2, bg='#107db2', fg='white'
                                , font=('verdana', 8, 'bold'), command=self.limpaViagem)
        self.bt_limpar.place(relx=0.4, rely=0.1, relwidth=0.1, relheight=0.15)
        ### Criação do botao buscar
        self.bt_buscar = Button(self.frame_7, text="Buscar", bd=2, bg='#107db2', fg='white'
                                , font=('verdana', 8, 'bold'), command=self.buscaViagem)
        self.bt_buscar.place(relx=0.3, rely=0.1, relwidth=0.1, relheight=0.15)
        ### Criação do botao novo
        self.bt_novo = Button(self.frame_7, text="Inserir", bd=2, bg='#107db2', fg='white'
                              , font=('verdana', 8, 'bold'), command=self.insereViagem)
        self.bt_novo.place(relx=0.6, rely=0.1, relwidth=0.1, relheight=0.15)
        ### Criação do botao alterar
        self.bt_alterar = Button(self.frame_7, text="Alterar", bd=2, bg='#107db2', fg='white'
                                 , font=('verdana', 8, 'bold'), command=self.alteraViagem)
        self.bt_alterar.place(relx=0.7, rely=0.1, relwidth=0.1, relheight=0.15)
        ### Criação do botao apagar
        self.bt_apagar = Button(self.frame_7, text="Apagar", bd=2, bg='#107db2', fg='white'
                                , font=('verdana', 8, 'bold'), command=self.deletaViagem)
        self.bt_apagar.place(relx=0.8, rely=0.1, relwidth=0.1, relheight=0.15)

        ## Criação da label e entrada do idDestino
        self.lb_idDestino = Label(self.frame_7, text="ID do destino", bg='#dfe3ee', fg='#107db2')
        self.lb_idDestino.place(relx=0.05, rely=0.05)

        self.idDestino_entry = Entry(self.frame_7)
        self.idDestino_entry.place(relx=0.05, rely=0.15, relwidth=0.08)

        ## Criação da label e entrada do País
        self.lb_Pais = Label(self.frame_7, text="País", bg='#dfe3ee', fg='#107db2')
        self.lb_Pais.place(relx=0.05, rely=0.3)

        self.Pais_entry = Entry(self.frame_7)
        self.Pais_entry.place(relx=0.05, rely=0.40, relwidth=0.3)

        ## Criação da label e entrada do Estado
        self.lb_Estado = Label(self.frame_7, text="Estado", bg='#dfe3ee', fg='#107db2')
        self.lb_Estado.place(relx=0.37, rely=0.3)

        self.Estado_entry = Entry(self.frame_7)
        self.Estado_entry.place(relx=0.37, rely=0.40, relwidth=0.3)

        ## Criação da label e entrada do Cidade
        self.lb_Cidade = Label(self.frame_7, text="Cidade", bg='#dfe3ee', fg='#107db2')
        self.lb_Cidade.place(relx=0.69, rely=0.3)

        self.Cidade_entry = Entry(self.frame_7)
        self.Cidade_entry.place(relx=0.69, rely=0.40, relwidth=0.2)

        ## Criação da label e entrada do HorarioPrevisto
        self.lb_HorarioPrevisto = Label(self.frame_7, text="Horario previsto", bg='#dfe3ee', fg='#107db2')
        self.lb_HorarioPrevisto.place(relx=0.05, rely=0.55)

        self.HorarioPrevisto_entry = Entry(self.frame_7)
        self.HorarioPrevisto_entry.place(relx=0.05, rely=0.65, relwidth=0.3)

        ## Criação da label e entrada da Desembarque
        self.lb_Desembarque = Label(self.frame_7, text="Desembarque", bg='#dfe3ee', fg='#107db2')
        self.lb_Desembarque.place(relx=0.37, rely=0.55)

        self.Desembarque_entry = Entry(self.frame_7)
        self.Desembarque_entry.place(relx=0.37, rely=0.65, relwidth=0.3)

        self.listaCli = ttk.Treeview(self.frame_8, height=3,
                                     column=("col1", "col2", "col3", "col4", "col5", "col6"))
        self.listaCli.heading("#0", text="")
        self.listaCli.heading("#1", text="ID do destino")
        self.listaCli.heading("#2", text="País")
        self.listaCli.heading("#3", text="Estado")
        self.listaCli.heading("#4", text="Cidade")
        self.listaCli.heading("#5", text="Desembarque")
        self.listaCli.heading("#6", text="Horario previsto")
        self.listaCli.column("#0", width=1)
        self.listaCli.column("#1", width=50)
        self.listaCli.column("#2", width=50)
        self.listaCli.column("#3", width=50)
        self.listaCli.column("#4", width=50)
        self.listaCli.column("#5", width=50)
        self.listaCli.column("#6", width=50)
        self.listaCli.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)

        self.scroolLista = Scrollbar(self.frame_8, orient='vertical')
        self.listaCli.configure(yscroll=self.scroolLista.set)
        self.scroolLista.place(relx=0.96, rely=0.1, relwidth=0.02, relheight=0.85)
        self.listaCli.bind("<Double-1>", self.OnDoubleClickViagem)
        
        self.mostraViagem()

    def atividades(self):
        self.root6 = Toplevel()
        self.root6.state('zoomed')
        self.root6.title("Atividades")
        self.root6.configure(background='#1e3743')
        self.root6.transient(self.root)
        self.root6.focus_force()
        self.root6.grab_set()

        self.frame_9 = Frame(self.root6, bd=4, bg='#dfe3ee',
                             highlightbackground='#759fe6', highlightthickness=3)
        self.frame_9.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)

        self.frame_10 = Frame(self.root6, bd=4, bg='#dfe3ee',
                             highlightbackground='#759fe6', highlightthickness=3)
        self.frame_10.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)

        ### Criação do botao limpar
        self.bt_limpar = Button(self.frame_9, text="Limpar", bd=2, bg='#107db2', fg='white'
                                , font=('verdana', 8, 'bold'), command=self.limpaAtividade)
        self.bt_limpar.place(relx=0.4, rely=0.1, relwidth=0.1, relheight=0.15)
        ### Criação do botao buscar
        self.bt_buscar = Button(self.frame_9, text="Buscar", bd=2, bg='#107db2', fg='white'
                                , font=('verdana', 8, 'bold'), command=self.buscaAtividade)
        self.bt_buscar.place(relx=0.3, rely=0.1, relwidth=0.1, relheight=0.15)
        ### Criação do botao novo
        self.bt_novo = Button(self.frame_9, text="Inserir", bd=2, bg='#107db2', fg='white'
                              , font=('verdana', 8, 'bold'), command=self.insereAtividade)
        self.bt_novo.place(relx=0.6, rely=0.1, relwidth=0.1, relheight=0.15)
        ### Criação do botao alterar
        self.bt_alterar = Button(self.frame_9, text="Alterar", bd=2, bg='#107db2', fg='white'
                                 , font=('verdana', 8, 'bold'), command=self.alteraAtividade)
        self.bt_alterar.place(relx=0.7, rely=0.1, relwidth=0.1, relheight=0.15)
        ### Criação do botao apagar
        self.bt_apagar = Button(self.frame_9, text="Apagar", bd=2, bg='#107db2', fg='white'
                                , font=('verdana', 8, 'bold'), command=self.deletaAtividade)
        self.bt_apagar.place(relx=0.8, rely=0.1, relwidth=0.1, relheight=0.15)

        ## Criação da label e entrada do idAtividade
        self.lb_idAtividade = Label(self.frame_9, text="ID da atividade", bg='#dfe3ee', fg='#107db2')
        self.lb_idAtividade.place(relx=0.05, rely=0.05)

        self.idAtividade_entry = Entry(self.frame_9)
        self.idAtividade_entry.place(relx=0.05, rely=0.15, relwidth=0.08)

        ## Criação da label e entrada do nomeA
        self.lb_nomeA = Label(self.frame_9, text="Nome", bg='#dfe3ee', fg='#107db2')
        self.lb_nomeA.place(relx=0.05, rely=0.3)

        self.nomeA_entry = Entry(self.frame_9)
        self.nomeA_entry.place(relx=0.05, rely=0.40, relwidth=0.3)

        ## Criação da label e entrada do Tipo
        self.lb_tipoA = Label(self.frame_9, text="Tipo", bg='#dfe3ee', fg='#107db2')
        self.lb_tipoA.place(relx=0.37, rely=0.3)

        self.tipoA_entry = Entry(self.frame_9)
        self.tipoA_entry.place(relx=0.37, rely=0.40, relwidth=0.3)

        ## Criação da label e entrada do Duração
        self.lb_duracao = Label(self.frame_9, text="Duração", bg='#dfe3ee', fg='#107db2')
        self.lb_duracao.place(relx=0.05, rely=0.55)

        self.duracao_entry = Entry(self.frame_9)
        self.duracao_entry.place(relx=0.05, rely=0.65, relwidth=0.3)

        ## Criação da label e entrada da Guia
        self.lb_Guia = Label(self.frame_9, text="Guia", bg='#dfe3ee', fg='#107db2')
        self.lb_Guia.place(relx=0.37, rely=0.55)

        self.Guia_entry = Entry(self.frame_9)
        self.Guia_entry.place(relx=0.37, rely=0.65, relwidth=0.3)

        ## Criação da label e entrada do TelGuia
        self.lb_TelGuia = Label(self.frame_9, text="Telefone do guia", bg='#dfe3ee', fg='#107db2')
        self.lb_TelGuia.place(relx=0.05, rely=0.8)

        self.TelGuia_entry = Entry(self.frame_9)
        self.TelGuia_entry.place(relx=0.05, rely=0.9, relwidth=0.3)

        ## Criação da label e entrada do Custo
        self.lb_custoA = Label(self.frame_9, text="Custo", bg='#dfe3ee', fg='#107db2')
        self.lb_custoA.place(relx=0.37, rely=0.8)

        self.custoA_entry = Entry(self.frame_9)
        self.custoA_entry.place(relx=0.37, rely=0.90, relwidth=0.3)

        self.listaCli = ttk.Treeview(self.frame_10, height=3,
                                     column=("col1", "col2", "col3", "col4", "col5", "col6", "col7", "col8"))
        self.listaCli.heading("#0", text="")
        self.listaCli.heading("#1", text="ID da atividade")
        self.listaCli.heading("#2", text="Nome")
        self.listaCli.heading("#3", text="Tipo")
        self.listaCli.heading("#4", text="Duração")
        self.listaCli.heading("#5", text="Guia")
        self.listaCli.heading("#6", text="Telefone do guia")
        self.listaCli.heading("#7", text="Custo")
        self.listaCli.column("#0", width=1)
        self.listaCli.column("#1", width=50)
        self.listaCli.column("#2", width=50)
        self.listaCli.column("#3", width=50)
        self.listaCli.column("#4", width=50)
        self.listaCli.column("#5", width=50)
        self.listaCli.column("#6", width=50)
        self.listaCli.column("#7", width=50)
        self.listaCli.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)

        self.scroolLista = Scrollbar(self.frame_10, orient='vertical')
        self.listaCli.configure(yscroll=self.scroolLista.set)
        self.scroolLista.place(relx=0.96, rely=0.1, relwidth=0.02, relheight=0.85)
        self.listaCli.bind("<Double-1>", self.OnDoubleClickAtividade)
        self.mostraAtividade()

    def hotel(self):
        self.root7 = Toplevel()
        self.root7.state('zoomed')
        self.root7.title("Hotel")
        self.root7.configure(background='#1e3743')
        self.root7.transient(self.root)
        self.root7.focus_force()
        self.root7.grab_set()

        self.frame_11 = Frame(self.root7, bd=4, bg='#dfe3ee',
                             highlightbackground='#759fe6', highlightthickness=3)
        self.frame_11.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)

        self.frame_12 = Frame(self.root7, bd=4, bg='#dfe3ee',
                             highlightbackground='#759fe6', highlightthickness=3)
        self.frame_12.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)

        ### Criação do botao limpar
        self.bt_limpar = Button(self.frame_11, text="Limpar", bd=2, bg='#107db2', fg='white'
                                , font=('verdana', 8, 'bold'), command=self.limpaHotel)
        self.bt_limpar.place(relx=0.4, rely=0.1, relwidth=0.1, relheight=0.15)
        ### Criação do botao buscar
        self.bt_buscar = Button(self.frame_11, text="Buscar", bd=2, bg='#107db2', fg='white'
                                , font=('verdana', 8, 'bold'), command=self.buscaHotel)
        self.bt_buscar.place(relx=0.3, rely=0.1, relwidth=0.1, relheight=0.15)
        ### Criação do botao novo
        self.bt_novo = Button(self.frame_11, text="Inserir", bd=2, bg='#107db2', fg='white'
                              , font=('verdana', 8, 'bold'), command=self.insereHotel)
        self.bt_novo.place(relx=0.6, rely=0.1, relwidth=0.1, relheight=0.15)
        ### Criação do botao alterar
        self.bt_alterar = Button(self.frame_11, text="Alterar", bd=2, bg='#107db2', fg='white'
                                 , font=('verdana', 8, 'bold'), command=self.alteraHotel)
        self.bt_alterar.place(relx=0.7, rely=0.1, relwidth=0.1, relheight=0.15)
        ### Criação do botao apagar
        self.bt_apagar = Button(self.frame_11, text="Apagar", bd=2, bg='#107db2', fg='white'
                                , font=('verdana', 8, 'bold'), command=self.deletaHotel)
        self.bt_apagar.place(relx=0.8, rely=0.1, relwidth=0.1, relheight=0.15)

        ## Criação da label e entrada do idHotel
        self.lb_idHotel = Label(self.frame_11, text="ID do hotel", bg='#dfe3ee', fg='#107db2')
        self.lb_idHotel.place(relx=0.05, rely=0.05)

        self.idHotel_entry = Entry(self.frame_11)
        self.idHotel_entry.place(relx=0.05, rely=0.15, relwidth=0.08)

        ## Criação da label e entrada do nomeA
        self.lb_nomeH = Label(self.frame_11, text="Nome", bg='#dfe3ee', fg='#107db2')
        self.lb_nomeH.place(relx=0.05, rely=0.3)

        self.nomeH_entry = Entry(self.frame_11)
        self.nomeH_entry.place(relx=0.05, rely=0.40, relwidth=0.3)

        ## Criação da label e entrada do Quarto
        self.lb_Quarto = Label(self.frame_11, text="Quarto", bg='#dfe3ee', fg='#107db2')
        self.lb_Quarto.place(relx=0.37, rely=0.3)

        self.Quarto_entry = Entry(self.frame_11)
        self.Quarto_entry.place(relx=0.37, rely=0.40, relwidth=0.3)

        ## Criação da label e entrada da Diaria
        self.lb_Diaria = Label(self.frame_11, text="Diaria", bg='#dfe3ee', fg='#107db2')
        self.lb_Diaria.place(relx=0.05, rely=0.55)

        self.Diaria_entry = Entry(self.frame_11)
        self.Diaria_entry.place(relx=0.05, rely=0.65, relwidth=0.3)

        ## Criação da label e entrada do NumeroDias
        self.lb_NumeroDias = Label(self.frame_11, text="Numero de dias", bg='#dfe3ee', fg='#107db2')
        self.lb_NumeroDias.place(relx=0.37, rely=0.55)

        self.NumeroDias_entry = Entry(self.frame_11)
        self.NumeroDias_entry.place(relx=0.37, rely=0.65, relwidth=0.3)

        ## Criação da label e entrada do Enderco
        self.lb_Endereco = Label(self.frame_11, text="Enderço", bg='#dfe3ee', fg='#107db2')
        self.lb_Endereco.place(relx=0.05, rely=0.8)

        self.Endereco_entry = Entry(self.frame_11)
        self.Endereco_entry.place(relx=0.05, rely=0.9, relwidth=0.3)

        ## Criação da label e entrada do ViagemId
        self.lb_ViagemId = Label(self.frame_11, text="ID da viagem", bg='#dfe3ee', fg='#107db2')
        self.lb_ViagemId.place(relx=0.37, rely=0.8)

        self.ViagemId_entry = Entry(self.frame_11)
        self.ViagemId_entry.place(relx=0.37, rely=0.90, relwidth=0.3)

        self.listaCli = ttk.Treeview(self.frame_12, height=3,
                                     column=("col1", "col2", "col3", "col4", "col5", "col6", "col7", "col8"))
        self.listaCli.heading("#0", text="")
        self.listaCli.heading("#1", text="ID do hotel")
        self.listaCli.heading("#2", text="Nome")
        self.listaCli.heading("#3", text="Quarto")
        self.listaCli.heading("#4", text="Diaria")
        self.listaCli.heading("#5", text="Numero de dias")
        self.listaCli.heading("#6", text="Enderço")
        self.listaCli.heading("#7", text="ID da viagem")
        self.listaCli.column("#0", width=1)
        self.listaCli.column("#1", width=50)
        self.listaCli.column("#2", width=150)
        self.listaCli.column("#3", width=50)
        self.listaCli.column("#4", width=50)
        self.listaCli.column("#5", width=70)
        self.listaCli.column("#6", width=250)
        self.listaCli.column("#7", width=50)
        self.listaCli.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)

        self.scroolLista = Scrollbar(self.frame_12, orient='vertical')
        self.listaCli.configure(yscroll=self.scroolLista.set)
        self.scroolLista.place(relx=0.96, rely=0.1, relwidth=0.02, relheight=0.85)
        self.listaCli.bind("<Double-1>", self.OnDoubleClickHotel)
        self.mostraHotel()

    def acompanhante(self):
        self.root8 = Toplevel()
        self.root8.state('zoomed')
        self.root8.title("Acompanhante")
        self.root8.configure(background='#1e3743')
        self.root8.transient(self.root)
        self.root8.focus_force()
        self.root8.grab_set()
        self.frame_13 = Frame(self.root8, bd=4, bg='#dfe3ee',
                             highlightbackground='#759fe6', highlightthickness=3)
        self.frame_13.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)

        self.frame_14 = Frame(self.root8, bd=4, bg='#dfe3ee',
                             highlightbackground='#759fe6', highlightthickness=3)
        self.frame_14.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)

        ### Criação do botao limpar
        self.bt_limpar = Button(self.frame_13, text="Limpar", bd=2, bg='#107db2', fg='white'
                                , font=('verdana', 8, 'bold'), command=self.limpaAcompanhante)
        self.bt_limpar.place(relx=0.4, rely=0.1, relwidth=0.1, relheight=0.15)
        ### Criação do botao buscar
        self.bt_buscar = Button(self.frame_13, text="Buscar", bd=2, bg='#107db2', fg='white'
                                , font=('verdana', 8, 'bold'), command=self.buscaAcompanhante)
        self.bt_buscar.place(relx=0.3, rely=0.1, relwidth=0.1, relheight=0.15)
        ### Criação do botao novo
        self.bt_novo = Button(self.frame_13, text="Inserir", bd=2, bg='#107db2', fg='white'
                              , font=('verdana', 8, 'bold'), command=self.insereAcompanhante)
        self.bt_novo.place(relx=0.6, rely=0.1, relwidth=0.1, relheight=0.15)
        ### Criação do botao alterar
        self.bt_alterar = Button(self.frame_13, text="Alterar", bd=2, bg='#107db2', fg='white'
                                 , font=('verdana', 8, 'bold'), command=self.alteraAcompanhante)
        self.bt_alterar.place(relx=0.7, rely=0.1, relwidth=0.1, relheight=0.15)
        ### Criação do botao apagar
        self.bt_apagar = Button(self.frame_13, text="Apagar", bd=2, bg='#107db2', fg='white'
                                , font=('verdana', 8, 'bold'), command=self.deletaAcompanhante)
        self.bt_apagar.place(relx=0.8, rely=0.1, relwidth=0.1, relheight=0.15)

        ## Criação da label e entrada do CPF
        self.lb_CPFA = Label(self.frame_13, text="CPF", bg='#dfe3ee', fg='#107db2')
        self.lb_CPFA.place(relx=0.05, rely=0.05)

        self.CPFA_entry = Entry(self.frame_13)
        self.CPFA_entry.place(relx=0.05, rely=0.15, relwidth=0.08)

        ## Criação da label e entrada do nome
        self.lb_nomeAc = Label(self.frame_13, text="Nome", bg='#dfe3ee', fg='#107db2')
        self.lb_nomeAc.place(relx=0.05, rely=0.3)

        self.nomeAc_entry = Entry(self.frame_13)
        self.nomeAc_entry.place(relx=0.05, rely=0.40, relwidth=0.3)

        ## Criação da label e entrada do sobrenome
        self.lb_sobrenomeA = Label(self.frame_13, text="Sobrenome", bg='#dfe3ee', fg='#107db2')
        self.lb_sobrenomeA.place(relx=0.37, rely=0.3)

        self.sobrenomeA_entry = Entry(self.frame_13)
        self.sobrenomeA_entry.place(relx=0.37, rely=0.40, relwidth=0.3)

        ## Criação da label e entrada do data
        self.lb_dataA = Label(self.frame_13, text="Data de nascimento", bg='#dfe3ee', fg='#107db2')
        self.lb_dataA.place(relx=0.69, rely=0.3)

        self.dataA_entry = Entry(self.frame_13)
        self.dataA_entry.place(relx=0.69, rely=0.40, relwidth=0.2)

        ## Criação da label e entrada do Tel
        self.lb_Tel = Label(self.frame_13, text="Telefone", bg='#dfe3ee', fg='#107db2')
        self.lb_Tel.place(relx=0.05, rely=0.55)

        self.Tel_entry = Entry(self.frame_13)
        self.Tel_entry.place(relx=0.05, rely=0.65, relwidth=0.3)

        ## Criação da label e entrada da Passaporte
        self.lb_Passaporte = Label(self.frame_13, text="Passaporte", bg='#dfe3ee', fg='#107db2')
        self.lb_Passaporte.place(relx=0.37, rely=0.55)

        self.Passaporte_entry = Entry(self.frame_13)
        self.Passaporte_entry.place(relx=0.37, rely=0.65, relwidth=0.3)

        ## Criação da label e entrada do Relação
        self.lb_Relacao = Label(self.frame_13, text="Relação", bg='#dfe3ee', fg='#107db2')
        self.lb_Relacao.place(relx=0.05, rely=0.8)

        self.Relacao_entry = Entry(self.frame_13)
        self.Relacao_entry.place(relx=0.05, rely=0.9, relwidth=0.3)

        ## Criação da label e entrada do ReservaIdA
        self.lb_ReservaIdA = Label(self.frame_13, text="ID da reserva", bg='#dfe3ee', fg='#107db2')
        self.lb_ReservaIdA.place(relx=0.37, rely=0.8)

        self.ReservaIdA_entry = Entry(self.frame_13)
        self.ReservaIdA_entry.place(relx=0.37, rely=0.90, relwidth=0.3)

        self.listaCli = ttk.Treeview(self.frame_14, height=3,
                                     column=("col1", "col2", "col3", "col4", "col5", "col6", "col7", "col8"))
        self.listaCli.heading("#0", text="")
        self.listaCli.heading("#1", text="ID da reserva")
        self.listaCli.heading("#2", text="Nome")
        self.listaCli.heading("#3", text="Sobrenome")
        self.listaCli.heading("#4", text="CPF")
        self.listaCli.heading("#5", text="Passaporte")
        self.listaCli.heading("#6", text="Data de nascimento")
        self.listaCli.heading("#7", text="Telefone")
        self.listaCli.heading("#8", text="Relação")
        
        self.listaCli.column("#0", width=1)
        self.listaCli.column("#1", width=50)
        self.listaCli.column("#2", width=50)
        self.listaCli.column("#3", width=50)
        self.listaCli.column("#4", width=50)
        self.listaCli.column("#5", width=50)
        self.listaCli.column("#6", width=50)
        self.listaCli.column("#7", width=50)
        self.listaCli.column("#8", width=50)
        self.listaCli.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)

        self.scroolLista = Scrollbar(self.frame_14, orient='vertical')
        self.listaCli.configure(yscroll=self.scroolLista.set)
        self.scroolLista.place(relx=0.96, rely=0.1, relwidth=0.02, relheight=0.85)
        self.listaCli.bind("<Double-1>", self.OnDoubleClickAcompanhante)
        self.mostraAcompanhante()

    def Intermediario(self):
        self.root = Toplevel()
        self.root.state('zoomed')
        self.root.title("BDViagens")
        self.root.configure(background='#1e3743')
        self.root.transient(self.root0)
        self.root.focus_force()
        self.root.grab_set()

        self.login(self.Usuario_entry.get(), self.Senha_entry.get())

        self.frame_1 = Frame(self.root, bd=4, bg='#dfe3ee',
                             highlightbackground='#759fe6', highlightthickness=3)
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.96)

        self.lb_ReservaIdA = Label(self.frame_1, text="BDViagens", font=('verdana', 20, 'bold'), bg='#dfe3ee',
                                   fg='#107db2', )
        self.lb_ReservaIdA.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.10)

        ### Criação do botao cliente
        self.bt_cliente = Button(self.frame_1, text="Cliente", bd=2, bg='#107db2', fg='white'
                                 , font=('verdana', 8, 'bold'), command=self.cliente)
        self.bt_cliente.place(relx=0.40, rely=0.2, relwidth=0.2, relheight=0.10)

        ### Criação do botao reserva
        self.bt_reserva = Button(self.frame_1, text="Reserva", bd=2, bg='#107db2', fg='white'
                                 , font=('verdana', 8, 'bold'), command=self.reserva)
        self.bt_reserva.place(relx=0.40, rely=0.3, relwidth=0.2, relheight=0.10)

        ### Criação do botao passagen
        self.bt_passagen = Button(self.frame_1, text="Passagens", bd=2, bg='#107db2', fg='white'
                                  , font=('verdana', 8, 'bold'), command=self.passagens)
        self.bt_passagen.place(relx=0.40, rely=0.4, relwidth=0.2, relheight=0.10)

        ### Criação do botao viagem
        self.bt_viagem = Button(self.frame_1, text="Viagem", bd=2, bg='#107db2', fg='white'
                                , font=('verdana', 8, 'bold'), command=self.viagem)
        self.bt_viagem.place(relx=0.40, rely=0.5, relwidth=0.2, relheight=0.10)

        ### Criação do botao atividades
        self.bt_atividades = Button(self.frame_1, text="Atividades", bd=2, bg='#107db2', fg='white'
                                    , font=('verdana', 8, 'bold'), command=self.atividades)
        self.bt_atividades.place(relx=0.40, rely=0.6, relwidth=0.2, relheight=0.10)

        ### Criação do botao hotel
        self.bt_hotel = Button(self.frame_1, text="Hotel", bd=2, bg='#107db2', fg='white'
                               , font=('verdana', 8, 'bold'), command=self.hotel)
        self.bt_hotel.place(relx=0.40, rely=0.7, relwidth=0.2, relheight=0.10)

        ### Criação do botao acompanhante
        self.bt_acompanhante = Button(self.frame_1, text="Acompanhante", bd=2, bg='#107db2', fg='white'
                                      , font=('verdana', 8, 'bold'), command=self.acompanhante)
        self.bt_acompanhante.place(relx=0.40, rely=0.8, relwidth=0.2, relheight=0.10)

        ### Criação do botao criabanco
        self.bt_criabanco = Button(self.frame_1, text="Criar Banco", bd=2, bg='#107db2', fg='white'
                                   , font=('verdana', 8, 'bold'), command=self.criaBancoDados)
        self.bt_criabanco.place(relx=0.01, rely=0.90, relwidth=0.1, relheight=0.08)



Application()