from tkinter import *
from b.funcoes import *
from b.criabanco import *
from b.recibo import *
import b.inicial

class Funcs():
    # Cria o banco de dados
    def criaBancoDados(self):
        criaBanco()

    # Gera o recibo
    def geraRecibo(self):
        recibo(self.codigo_entry.get())

    def login(self, u, s):
        b.inicial.usuario = u
        b.inicial.senha = s
    
    ### Para Cliente
    # Limpa o formulário de Cliente
    def limpaCliente(self):
        self.codigo_entry.delete(0, END)
        self.cidade_entry.delete(0, END)
        self.fone_entry.delete(0, END)
        self.nome_entry.delete(0, END)
        self.sobrenome_entry.delete(0, END)
        self.data_entry.delete(0, END)
        self.EMail_entry.delete(0, END)
        self.passaporte_entry.delete(0, END)

    # Mostra os clientes na treeview
    def mostraCliente(self):
        self.listaCli.delete(*self.listaCli.get_children())
        sql = """select * from cliente """
        reg = consultar_db(sql)
        for i in reg:
            self.listaCli.insert("" , END, values = i)

    # Seleciona os dados da treeview e os mostra no formulário
    def OnDoubleClickCliente(self, event):
        self.limpaCliente()
        self.listaCli.selection()

        for n in self.listaCli.selection():
            col1, col2, col3, col4, col5, col6, col7, col8 = self.listaCli.item(n, 'values')
        self.nome_entry.insert(END, col1) 
        self.sobrenome_entry.insert(END, col2)
        self.codigo_entry.insert(END, col3)
        self.passaporte_entry.insert(END, col4)
        self.data_entry.insert(END, col5)
        self.fone_entry.insert(END, col6)
        self.EMail_entry.insert(END, col7)
        self.cidade_entry.insert(END, col8)
        self.mostraCliente()
    
    # Busca um cliente através do cpf
    def buscaCliente(self):
        self.listaCli.delete(*self.listaCli.get_children())
        sql = """select * from cliente where cpf = '"""+ self.codigo_entry.get() + """'"""
        reg = consultar_db(sql)
        for i in reg:
            self.listaCli.insert("" , END, values = i)

    # Deleta um cliente através do cpf
    def deletaCliente(self):
        sql = """delete from cliente where cpf = '"""+ self.codigo_entry.get() + """'"""
        inserir_db(sql)
        self.mostraCliente()
    
    # Insere os dados do furmulário na tabela CLIENTE
    def insereCliente(self):
        sql = """insert into cliente values (%s, %s, %s, %s, %s, %s, %s, %s);"""
        tupla = (self.nome_entry.get(), self.sobrenome_entry.get(), self.codigo_entry.get(), self.passaporte_entry.get(),
                self.data_entry.get(), self.fone_entry.get(), self.EMail_entry.get(), self.cidade_entry.get())
        insere_tupla(sql, tupla)
        self.mostraCliente()
    
    # Altera os dados do cliente através do cpf para os dados do formulário
    def alteraCliente(self):
        sql = """update cliente set  pnome = '"""+self.nome_entry.get()+"""', unome = '""" + self.sobrenome_entry.get()+"""',
                passaporte = '"""+self.passaporte_entry.get()+"""', datanasc = '"""+self.data_entry.get()+"""', 
                tel = '"""+self.fone_entry.get()+"""', email = '"""+self.EMail_entry.get()+"""', 
                endereco = '"""+self.cidade_entry.get()+"""' where cpf = '"""+self.codigo_entry.get()+"""';"""
        inserir_db(sql)
        self.mostraCliente()

    
    ### Para Reserva
    # Limpa o formulário de Reserva
    def limpaReserva(self):
        self.idReserva_entry.delete(0, END)
        self.status_entry.delete(0, END)
        self.dataReserva_entry.delete(0, END)
        self.viagemID_entry.delete(0, END)

    # Mostra as reservas na treeview
    def mostraReserva(self):
        self.listaCli.delete(*self.listaCli.get_children())
        sql = """select * from reserva"""
        reg = consultar_db(sql)
        for i in reg:
            self.listaCli.insert("" , END, values = i)

    # Seleciona os dados da treeview e os mostra no formulário
    def OnDoubleClickReserva(self, event):
        self.limpaReserva()
        self.listaCli.selection()

        for n in self.listaCli.selection():
            col1, col2, col3, col4 = self.listaCli.item(n, 'values')
        self.idReserva_entry.insert(END, col1) 
        self.status_entry.insert(END, col2)
        self.dataReserva_entry.insert(END, col3)
        self.viagemID_entry.insert(END, col4)
        self.mostraReserva()
    
    # Busca uma reserva através do id
    def buscaReserva(self):
        self.listaCli.delete(*self.listaCli.get_children())
        sql = """select * from reserva where idreserva = """+ self.idReserva_entry.get() + """;"""
        reg = consultar_db(sql)
        for i in reg:
            self.listaCli.insert("" , END, values = i)

    # Deleta uma reserva através do id
    def deletaReserva(self):
        sql = """delete from reserva where idreserva = """+ self.idReserva_entry.get() + """;"""
        inserir_db(sql)
        self.mostraReserva()
    
    # Insere os dados do furmulário na tabela RESERVA
    def insereReserva(self):
        sql = """insert into reserva values (%s, %s, %s, %s);"""
        tupla = (self.idReserva_entry.get(), self.status_entry.get(), self.dataReserva_entry.get(), self.viagemID_entry.get())
        insere_tupla(sql, tupla)
        self.mostraReserva()
    
    # Altera os dados da reserva através do id para os dados do formulário
    def alteraReserva(self):
        sql = """update reserva set  status = '"""+self.status_entry.get()+"""', datareserva = '""" + self.dataReserva_entry.get()+"""',
                viagemid = '"""+self.viagemID_entry.get()+"""' where idreserva = '"""+self.idReserva_entry.get()+"""';"""
        inserir_db(sql)
        self.mostraReserva()

    ### Para Passagens
    # Limpa o formulário de Passagem
    def limpaPassagem(self):
        self.idPassagem_entry.delete(0, END)
        self.Tipo_entry.delete(0, END)
        self.Empresa_entry.delete(0, END)
        self.data_Embarque.delete(0, END)
        self.HorarioEmbarque_entry.delete(0, END)
        self.Preco_entry.delete(0, END)
        self.Assento_entry.delete(0, END)
        self.ReservaID_entry.delete(0, END)

    # Mostra as passagens na treeview
    def mostraPassagem(self):
        self.listaCli.delete(*self.listaCli.get_children())
        sql = """select * from passagem """
        reg = consultar_db(sql)
        for i in reg:
            self.listaCli.insert("" , END, values = i)

    # Seleciona os dados da treeview e os mostra no formulário
    def OnDoubleClickPassagem(self, event):
        self.limpaPassagem()
        self.listaCli.selection()

        for n in self.listaCli.selection():
            col1, col2, col3, col4, col5, col6, col7, col8 = self.listaCli.item(n, 'values')
        self.idPassagem_entry.insert(END, col1) 
        self.Tipo_entry.insert(END, col2)
        self.Empresa_entry.insert(END, col3)
        self.data_Embarque.insert(END, col4)
        self.HorarioEmbarque_entry.insert(END, col5)
        self.Preco_entry.insert(END, col6)
        self.Assento_entry.insert(END, col7)
        self.ReservaID_entry.insert(END, col8)
        self.mostraPassagem()
    
    # Busca um número de passagens através do id
    def buscaPassagem(self):
        self.listaCli.delete(*self.listaCli.get_children())
        sql = """select * from passagem where idpassagem = '"""+ self.idPassagem_entry.get() + """'"""
        reg = consultar_db(sql)
        for i in reg:
            self.listaCli.insert("" , END, values = i)

    # Deleta uma passagem através do id
    def deletaPassagem(self):
        sql = """delete from passagem where idpassagem = '"""+ self.idPassagem_entry.get() + """'"""
        inserir_db(sql)
        self.mostraPassagem()
    
    # Insere os dados do furmulário na tabela PASSAGEM
    def inserePassagem(self):
        sql = """insert into passagem values (%s, %s, %s, %s, %s, %s, %s, %s);"""
        tupla = (self.idPassagem_entry.get(), self.Tipo_entry.get(), self.Empresa_entry.get(), self.data_Embarque.get(),
                self.HorarioEmbarque_entry.get(), self.Preco_entry.get(), self.Assento_entry.get(), self.ReservaID_entry.get())
        insere_tupla(sql, tupla)
        self.mostraPassagem()
    
    # Altera os dados da passagem através do id para os dados do formulário
    def alteraPassagem(self):
        sql = """update passagem set  tipo = '"""+self.Tipo_entry.get()+"""', empresa = '""" + self.Empresa_entry.get()+"""',
                embarque = '"""+self.data_Embarque.get()+"""', horarioemb = '"""+self.HorarioEmbarque_entry.get()+"""', 
                preco = '"""+self.Preco_entry.get()+"""', assento = '"""+self.Assento_entry.get()+"""', 
                reservaid = '"""+self.ReservaID_entry.get()+"""' where idpassagem = '"""+self.idPassagem_entry.get()+"""';"""
        inserir_db(sql)
        self.mostraPassagem()

### Para Viagem
    # Limpa o formulário de Viagem
    def limpaViagem(self):
        self.idDestino_entry.delete(0, END)
        self.Pais_entry.delete(0, END)
        self.Estado_entry.delete(0, END)
        self.Cidade_entry.delete(0, END)
        self.Desembarque_entry.delete(0, END)
        self.HorarioPrevisto_entry.delete(0, END)

    # Mostra as viagens na treeview
    def mostraViagem(self):
        self.listaCli.delete(*self.listaCli.get_children())
        sql = """select * from viagem """
        reg = consultar_db(sql)
        for i in reg:
            self.listaCli.insert("" , END, values = i)

    # Seleciona os dados da treeview e os mostra no formulário
    def OnDoubleClickViagem(self, event):
        self.limpaViagem()
        self.listaCli.selection()

        for n in self.listaCli.selection():
            col1, col2, col3, col4, col5, col6= self.listaCli.item(n, 'values')
        self.idDestino_entry.insert(END, col1) 
        self.Pais_entry.insert(END, col2)
        self.Estado_entry.insert(END, col3)
        self.Cidade_entry.insert(END, col4)
        self.Desembarque_entry.insert(END, col5)
        self.HorarioPrevisto_entry.insert(END, col6)
        self.mostraViagem()
    
    # Busca uma viagem através do id
    def buscaViagem(self):
        self.listaCli.delete(*self.listaCli.get_children())
        sql = """select * from viagem where idviagem = '"""+ self.idDestino_entry.get() + """'"""
        reg = consultar_db(sql)
        for i in reg:
            self.listaCli.insert("" , END, values = i)

    # Deleta uma viagem através do id
    def deletaViagem(self):
        sql = """delete from viagem where idviagem = '"""+ self.idDestino_entry.get() + """'"""
        inserir_db(sql)
        self.mostraViagem()
    
    # Insere os dados do furmulário na tabela VIAGEM
    def insereViagem(self):
        sql = """insert into viagem values (%s, %s, %s, %s, %s, %s);"""
        tupla = (self.idDestino_entry.get(), self.Pais_entry.get(), self.Estado_entry.get(), self.Cidade_entry.get(),
                self.Desembarque_entry.get(), self.HorarioPrevisto_entry.get())
        insere_tupla(sql, tupla)
        self.mostraViagem()
    
    # Altera os dados da viagem através do id para os dados do formulário
    def alteraViagem(self):
        sql = """update viagem set  pais = '"""+self.Pais_entry.get()+"""', estado = '""" + self.Estado_entry.get()+"""',
                cidade = '"""+self.Cidade_entry.get()+"""', desembarque = '"""+self.Desembarque_entry.get()+"""', 
                horariodes = '"""+self.HorarioPrevisto_entry.get()+"""' where idviagem = '"""+self.idDestino_entry.get()+"""';"""
        inserir_db(sql)
        self.mostraViagem()

    ### Para Atividades
    # Limpa o formulário de Atividade
    def limpaAtividade(self):
        self.idAtividade_entry.delete(0, END)
        self.nomeA_entry.delete(0, END)
        self.tipoA_entry.delete(0, END)
        self.duracao_entry.delete(0, END)
        self.Guia_entry.delete(0, END)
        self.TelGuia_entry.delete(0, END)
        self.custoA_entry.delete(0, END)

    # Mostra as atividades na treeview
    def mostraAtividade(self):
        self.listaCli.delete(*self.listaCli.get_children())
        sql = """select * from atividades """
        reg = consultar_db(sql)
        for i in reg:
            self.listaCli.insert("" , END, values = i)

    # Seleciona os dados da treeview e os mostra no formulário
    def OnDoubleClickAtividade(self, event):
        self.limpaAtividade()
        self.listaCli.selection()

        for n in self.listaCli.selection():
            col1, col2, col3, col4, col5, col6, col7 = self.listaCli.item(n, 'values')
        self.idAtividade_entry.insert(END, col1) 
        self.nomeA_entry.insert(END, col2)
        self.tipoA_entry.insert(END, col3)
        self.duracao_entry.insert(END, col4)
        self.Guia_entry.insert(END, col5)
        self.TelGuia_entry.insert(END, col6)
        self.custoA_entry.insert(END, col7)
        self.mostraAtividade()
    
    # Busca uma atividade através do id
    def buscaAtividade(self):
        self.listaCli.delete(*self.listaCli.get_children())
        sql = """select * from atividades where idatividade = '"""+ self.idAtividade_entry.get() + """'"""
        reg = consultar_db(sql)
        for i in reg:
            self.listaCli.insert("" , END, values = i)

    # Deleta uma atividade através do id
    def deletaAtividade(self):
        sql = """delete from atividades where idatividade = '"""+ self.idAtividade_entry.get() + """'"""
        inserir_db(sql)
        self.mostraAtividade()
    
    # Insere os dados do furmulário na tabela ATIVIDADES
    def insereAtividade(self):
        sql = """insert into atividades values (%s, %s, %s, %s, %s, %s, %s);"""
        tupla = (self.idAtividade_entry.get(), self.nomeA_entry.get(), self.tipoA_entry.get(), self.duracao_entry.get(),
                self.Guia_entry.get(), self.TelGuia_entry.get(), self.custoA_entry.get())
        insere_tupla(sql, tupla)
        self.mostraAtividade()
    
    # Altera os dados da atividade através do id para os dados do formulário
    def alteraAtividade(self):
        sql = """update atividades set  nome = '"""+self.nomeA_entry.get()+"""', tipo = '""" + self.tipoA_entry.get()+"""',
                duracao = '"""+self.duracao_entry.get()+"""', guia = '"""+self.Guia_entry.get()+"""', 
                telguia = '"""+self.TelGuia_entry.get()+"""', custo = '"""+self.custoA_entry.get()+"""'
                where idatividade = '"""+self.idAtividade_entry.get()+"""';"""
        inserir_db(sql)
        self.mostraAtividade()
    

    ### Para Viagem
    # Limpa o formulário de Viagem
    def limpaViagem(self):
        self.idDestino_entry.delete(0, END)
        self.Pais_entry.delete(0, END)
        self.Estado_entry.delete(0, END)
        self.Cidade_entry.delete(0, END)
        self.Desembarque_entry.delete(0, END)
        self.HorarioPrevisto_entry.delete(0, END)

    # Mostra as viagens na treeview
    def mostraViagem(self):
        self.listaCli.delete(*self.listaCli.get_children())
        sql = """select * from viagem """
        reg = consultar_db(sql)
        for i in reg:
            self.listaCli.insert("" , END, values = i)

    # Seleciona os dados da treeview e os mostra no formulário
    def OnDoubleClickViagem(self, event):
        self.limpaViagem()
        self.listaCli.selection()

        for n in self.listaCli.selection():
            col1, col2, col3, col4, col5, col6= self.listaCli.item(n, 'values')
        self.idDestino_entry.insert(END, col1) 
        self.Pais_entry.insert(END, col2)
        self.Estado_entry.insert(END, col3)
        self.Cidade_entry.insert(END, col4)
        self.Desembarque_entry.insert(END, col5)
        self.HorarioPrevisto_entry.insert(END, col6)
        self.mostraViagem()
    
    # Busca uma viagem através do id
    def buscaViagem(self):
        self.listaCli.delete(*self.listaCli.get_children())
        sql = """select * from viagem where idviagem = '"""+ self.idDestino_entry.get() + """'"""
        reg = consultar_db(sql)
        for i in reg:
            self.listaCli.insert("" , END, values = i)

    # Deleta uma viagem através do id
    def deletaViagem(self):
        sql = """delete from viagem where idviagem = '"""+ self.idDestino_entry.get() + """'"""
        inserir_db(sql)
        self.mostraViagem()
    
    # Insere os dados do furmulário na tabela VIAGEM
    def insereViagem(self):
        sql = """insert into viagem values (%s, %s, %s, %s, %s, %s);"""
        tupla = (self.idDestino_entry.get(), self.Pais_entry.get(), self.Estado_entry.get(), self.Cidade_entry.get(),
                self.Desembarque_entry.get(), self.HorarioPrevisto_entry.get())
        insere_tupla(sql, tupla)
        self.mostraViagem()
    
    # Altera os dados da viagem através do id para os dados do formulário
    def alteraViagem(self):
        sql = """update viagem set  pais = '"""+self.Pais_entry.get()+"""', estado = '""" + self.Estado_entry.get()+"""',
                cidade = '"""+self.Cidade_entry.get()+"""', desembarque = '"""+self.Desembarque_entry.get()+"""', 
                horariodes = '"""+self.HorarioPrevisto_entry.get()+"""' where idviagem = '"""+self.idDestino_entry.get()+"""';"""
        inserir_db(sql)
        self.mostraViagem()

    ### Para Hotel
    # Limpa o formulário de Hotel
    def limpaHotel(self):
        self.idHotel_entry.delete(0, END)
        self.nomeH_entry.delete(0, END)
        self.Quarto_entry.delete(0, END)
        self.Diaria_entry.delete(0, END)
        self.NumeroDias_entry.delete(0, END)
        self.Endereco_entry.delete(0, END)
        self.ViagemId_entry.delete(0, END)

    # Mostra os hotéis na treeview
    def mostraHotel(self):
        self.listaCli.delete(*self.listaCli.get_children())
        sql = """select * from hotel """
        reg = consultar_db(sql)
        for i in reg:
            self.listaCli.insert("" , END, values = i)

    # Seleciona os dados da treeview e os mostra no formulário
    def OnDoubleClickHotel(self, event):
        self.limpaHotel()
        self.listaCli.selection()

        for n in self.listaCli.selection():
            col1, col2, col3, col4, col5, col6, col7 = self.listaCli.item(n, 'values')
        self.idHotel_entry.insert(END, col1) 
        self.nomeH_entry.insert(END, col2)
        self.Quarto_entry.insert(END, col3)
        self.Diaria_entry.insert(END, col4)
        self.NumeroDias_entry.insert(END, col5)
        self.Endereco_entry.insert(END, col6)
        self.ViagemId_entry.insert(END, col7)
        self.mostraHotel()
    
    # Busca um hotel através do id
    def buscaHotel(self):
        self.listaCli.delete(*self.listaCli.get_children())
        sql = """select * from hotel where idhotel = '"""+ self.idHotel_entry.get() + """'"""
        reg = consultar_db(sql)
        for i in reg:
            self.listaCli.insert("" , END, values = i)

    # Deleta um hotel através do id
    def deletaHotel(self):
        sql = """delete from hotel where idhotel = '"""+ self.idHotel_entry.get() + """'"""
        inserir_db(sql)
        self.mostraHotel()
    
    # Insere os dados do furmulário na tabela HOTEL
    def insereHotel(self):
        sql = """insert into hotel values (%s, %s, %s, %s, %s, %s, %s);"""
        tupla = (self.idHotel_entry.get(), self.nomeH_entry.get(), self.Quarto_entry.get(), self.Diaria_entry.get(),
                self.NumeroDias_entry.get(), self.Endereco_entry.get(), self.ViagemId_entry.get())
        insere_tupla(sql, tupla)
        self.mostraHotel()
    
    # Altera os dados do hotel através do id para os dados do formulário
    def alteraHotel(self):
        sql = """update hotel set  nome = '"""+self.nomeH_entry.get()+"""', quarto = '""" + self.Quarto_entry.get()+"""',
                diaria = '"""+self.Diaria_entry.get()+"""', numerodias = '"""+self.NumeroDias_entry.get()+"""', 
                endereco = '"""+self.Endereco_entry.get()+"""', viagemid = '"""+self.ViagemId_entry.get()+"""'
                where idhotel = '"""+self.idHotel_entry.get()+"""';"""
        inserir_db(sql)
        self.mostraHotel()

    ### Para Acompanhante
    # Limpa o formulário de Acompanhante
    def limpaAcompanhante(self):
        self.ReservaIdA_entry.delete(0, END)
        self.nomeAc_entry.delete(0, END)
        self.sobrenomeA_entry.delete(0, END)
        self.CPFA_entry.delete(0, END)
        self.Passaporte_entry.delete(0, END)
        self.dataA_entry.delete(0, END)
        self.Tel_entry.delete(0, END)
        self.Relacao_entry.delete(0, END)

    # Mostra os acompanhantes na treeview
    def mostraAcompanhante(self):
        self.listaCli.delete(*self.listaCli.get_children())
        sql = """select * from acompanhante """
        reg = consultar_db(sql)
        for i in reg:
            self.listaCli.insert("" , END, values = i)

    # Seleciona os dados da treeview e os mostra no formulário
    def OnDoubleClickAcompanhante(self, event):
        self.limpaAcompanhante()
        self.listaCli.selection()

        for n in self.listaCli.selection():
            col1, col2, col3, col4, col5, col6, col7, col8 = self.listaCli.item(n, 'values')
        self.ReservaIdA_entry.insert(END, col1) 
        self.nomeAc_entry.insert(END, col2)
        self.sobrenomeA_entry.insert(END, col3)
        self.CPFA_entry.insert(END, col4)
        self.Passaporte_entry.insert(END, col5)
        self.dataA_entry.insert(END, col6)
        self.Tel_entry.insert(END, col7)
        self.Relacao_entry.insert(END, col8)
        self.mostraAcompanhante()
    
    # Busca um acompanhante através do cpf
    def buscaAcompanhante(self):
        self.listaCli.delete(*self.listaCli.get_children())
        sql = """select * from acompanhante where cpf = '"""+ self.CPFA_entry.get() + """'"""
        reg = consultar_db(sql)
        for i in reg:
            self.listaCli.insert("" , END, values = i)

    # Deleta um acompanhante através do cpf
    def deletaAcompanhante(self):
        sql = """delete from acompanhante where cpf = '"""+ self.CPFA_entry.get() + """'"""
        inserir_db(sql)
        self.mostraAcompanhante()
    
    # Insere os dados do furmulário na tabela ACOMPANHANTE
    def insereAcompanhante(self):
        sql = """insert into acompanhante values (%s, %s, %s, %s, %s, %s, %s, %s);"""
        tupla = (self.ReservaIdA_entry.get(), self.nomeAc_entry.get(), self.sobrenomeA_entry.get(), self.CPFA_entry.get(),
                self.Passaporte_entry.get(), self.dataA_entry.get(), self.Tel_entry.get(), self.Relacao_entry.get())
        insere_tupla(sql, tupla)
        self.mostraAcompanhante()
    
    # Altera os dados do acompanhante através do cpf para os dados do formulário
    def alteraAcompanhante(self):
        sql = """update acompanhante set  reservaid = '"""+self.ReservaIdA_entry.get()+"""', pnome = '""" + self.nomeAc_entry.get()+"""',
                unome = '"""+self.sobrenomeA_entry.get()+"""', passaporte = '"""+self.Passaporte_entry.get()+"""', 
                datanasc = '"""+self.dataA_entry.get()+"""', tel = '"""+self.Tel_entry.get()+"""', 
                relacao = '"""+self.Relacao_entry.get()+"""' where cpf = '"""+self.CPFA_entry.get()+"""';"""
        inserir_db(sql)
        self.mostraAcompanhante()