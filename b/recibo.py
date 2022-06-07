from fpdf import FPDF
import os
from b.funcoes import *

# Método para criar um pdf de recibo
def recibo(cpf):
    pdf = FPDF()    # Cria o pdf
    pdf.add_page()   # Adiciona página
    pdf.set_xy(0,0)
    pdf.set_font('arial', 'B', 24)  # Altera a fonte
    pdf.cell(80)
    pdf.cell(20, 10, 'Recibo de Viagem', 0, 1, 'C')     # Imprime uma linha de texto no pdf

    # Busca o cpf do cliente em questão
    pdf.set_font('arial', '', 16)
    sql = """select * from cliente where cpf ='""" + cpf + """'"""
    reg = consultar_db(sql)
    nome = reg[0][0]
    sobrenome = reg[0][1]
    email = reg[0][6]
    sql = """select * from reserva_cliente where ccpf ='""" + cpf + """'"""
    reg = consultar_db(sql)
    reserva = reg[0][1]

    # Descobre o número de viajantes para realizar os cálculos do recibo
    sql = """select count(pnome) 
    from reserva left join acompanhante on idreserva = reservaid 
    where idreserva = """+str(reserva)+""" group by idreserva"""
    reg = consultar_db(sql)
    viajantes = reg[0][0] + 1
    pdf.cell(20, 10, 'Enviado para: '+ nome +' '+ sobrenome +'', 0, 1)
    pdf.cell(20, 10, 'email: '+ email + '', 0, 1)
    pdf.cell(20, 10, 'Número de viajantes: '+ str(viajantes) + '', 0, 1)
    pdf.cell(10,10,'',0,1)      # Pula uma linha

    # Realiza o cálculo das passagens
    pdf.cell(20, 10, 'Passagens: ', 0, 1)
    sql = """select * from passagem where reservaid ='""" + str(reserva) + """'"""
    reg = consultar_db(sql)
    passagem = 0
    for result in reg:
        pdf.cell(20, 10, str(result[0])+ ' - R$' + str(result [5]), 0, 1)
        passagem = passagem + result[5]
    pdf.cell(20, 10, 'Total Passagens: R$' + str(passagem), 0, 1)
    pdf.cell(10,10,'',0,1)

    # Realiza o cálculo do valor gasto nos hotéis
    pdf.cell(20, 10, 'Hotel: ', 0, 1)
    sql = """select idviagem from viagem v, reserva r where v.idviagem = r.viagemid and r.idreserva = """+str(reserva)+""";"""
    reg = consultar_db(sql)
    viagem = reg[0][0]
    sql = """select nome, diaria, numerodias from hotel where viagemid ="""+str(viagem)+""";"""
    reg = consultar_db(sql)
    hotel = 0
    for result in reg:
        pdf.cell(20,10, result[0]+' - R$'+str(result[1]*result[2]), 0, 1)
        hotel = hotel + result[1]*result[2]
    pdf.cell(20, 10, 'Total Hotel: R$' + str(hotel), 0, 1)
    pdf.cell(10,10,'',0,1)

    # Realiza o cálculo das atividades
    pdf.cell(20, 10, 'Atividades: ', 0, 1)
    sql = """select nome, custo from atividades a, viagem v, atividade_viagem t 
    where a.idatividade = t.atividadeid and v.idviagem = t.viagemid and v.idviagem = """+str(viagem)+""";"""
    reg = consultar_db(sql)
    atividades = 0
    for result in reg:
        pdf.cell(20,10, result[0]+' - R$'+str(result[1]*viajantes), 0, 1)
        atividades = atividades + result[1]*viajantes
    pdf.cell(20, 10, 'Total Atividades: R$'+str(atividades), 0, 1)
    pdf.cell(10,10,'',0,1)
    pdf.set_font('arial', 'B', 24)
    pdf.cell(80)

    # Realiza o cálculo total da viagem
    pdf.cell(20, 10, 'Total Viagem: R$'+str(passagem+hotel+atividades), 0, 1, 'C')

    # Gera pdf na pasta recibos
    pdf.output('recibos/Recibo'+ nome + '.pdf','F')

    # Abre o pdf
    path = 'recibos\Recibo'+ nome + '.pdf'
    os.system(path)