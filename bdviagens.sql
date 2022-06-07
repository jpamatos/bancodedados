-- Apaga a tabela Cliente, caso exista
DROP TABLE IF EXISTS CLIENTE CASCADE;

-- Cria a tabela Cliente
CREATE TABLE CLIENTE
(
	pnome			VARCHAR(15)		NOT NULL,
	unome			VARCHAR(15)		NOT NULL,
	cpf				CHAR(11)		NOT NULL,
	passaporte		CHAR(8),
	datanasc		DATE,
	tel				CHAR(11),
	email			VARCHAR(35),
	endereco		VARCHAR(55),
	PRIMARY KEY (cpf),
	UNIQUE (passaporte)
);

-- Insere as tuplas em CLIENTE
INSERT INTO CLIENTE VALUES
('Enzo',	'Cruz',		'22427362808', 'GG953130', '1966-01-10', '81981098036', 'enzo-dacruz93@chalu.com.br', 'Rua Engenheiro Fernando, 865, Recife-PE'),
('Camila',	'Melo',		'02543856722', 'KE966720', '1977-04-07', '27989497076', 'camilalaramelo@lojasrayton.com', 'Rodovia Demócrito, 413, Aracruz-ES'),
('César', 	'Mata', 	'61663018200', 'LD637266', '1999-03-13', '61992610147', 'cesar-damata88@dpf.gov.br', 'Quadra QN 8A Conjunto 1, 249, Brasília-DF'),
('Tatiane',	'Almada',	'80664056776', 'NM781088', '1959-01-26', '71983246718', 'tatiane.almada@zyb.com.br', '1ª Travessa do Canto da Floresta, 281, Salvador-BA'),
('Evelyn', 	'Campos',	'92491269724', 'CV365434', '1983-04-25', '54995970376', 'evelyn_campos@smalte.com.br', 'Rua Acelio Reck, 655, Caixias do Sul-RS'),
('Thomas', 	'Santos', 	'83259841202', 'MH587798', '1991-04-03', '68996026824', 'thomas.santos@inepar.com.br', 'Rua Andorinha, 665, Rio Branco-AC'),
('Catarina', 'Rocha', 	'55418769316', 'OM257556', '1980-04-08', '92988726313', 'catarina-rocha93@lukin4.com.br', 'Rua Professora Elvira, 239, Manaus-AM'),
('Giovanni', 'Real', 	'36662132861', 'AB787592', '1983-01-11', '24991888321', 'giovanni-cortereal83@engeseg.com.br', 'Rua D, 119, Barra Mansa-RJ'),
('Yuri',	'Pires',	'71784527653', 'CH199542', '2002-04-03', '84985558645', 'yuri-pires77@trilhavitoria.com.br', 'Rua das Ágatas, 708, Mossoró-RN'),
('Victor',	'Pereira',	'87693254737', 'DM819979', '1979-02-23', '69993315333', 'victor_pereira@mv1.com.br', 'Rua Antônio Deodato Durce, 686, Cacoal-RO');

-- Apaga a tabela Viagem, caso exista
DROP TABLE IF EXISTS VIAGEM CASCADE;

-- Cria a tabela Viagem
CREATE TABLE VIAGEM
(
	idviagem		INTEGER		NOT NULL,
	pais			VARCHAR(15)	NOT NULL,
	estado			VARCHAR(20),
	cidade			VARCHAR(20) NOT NULL,
	desembarque		CHAR(3)		NOT NULL,
	horariodes		TIMESTAMP,
	PRIMARY KEY (idviagem)
);

-- Insere as tuplas em VIAGEM
INSERT INTO VIAGEM VALUES
('1', 'Brasil', 'São Paulo', 'São Paulo', 'GRU', '2022-06-03 01:01:01'),
('2', 'Brasil', 'Rio de Janeiro', 'Rio de Janeiro', 'GIG', '2022-06-04 17:35:01'),
('3', 'Brasil', 'Minas Gerais', 'Belo Horizonte', 'CNF', '2022-06-05 14:45:01'),
('4', 'Brasil', 'Distrito Federal', 'Brasília', 'BSB', '2022-06-06 08:06:01'),
('5', 'Estados Unidos', 'Califórnia', 'Los Angeles', 'LAX', '2022-06-06 18:58:01'),
('6', 'Estados Unidos', 'Nevada', 'Las Vegas', 'LAS', '2022-06-08 09:10:01'),
('7', 'França', 'Ilha de França', 'Paris', 'CDG', '2022-06-09 15:12:01'),
('8', 'Austrália', 'Nova Gales do Sul', 'Sydney', 'SYD', '2022-06-10 12:31:01'),
('9', 'Japão', 'Kanto', 'Tóquio', 'HND', '2022-06-11 07:41:01'),
('10', 'África do Sul', 'Cabo Ocidental', 'Cidade do Cabo', 'CPT', '2022-06-12 10:01:01');

-- Apaga a tabela Atividades, caso exista
DROP TABLE IF EXISTS ATIVIDADES CASCADE;

-- Cria a tabela Atividades
CREATE TABLE ATIVIDADES
(
	idatividade		INTEGER		NOT NULL,
	nome			VARCHAR(30) NOT NULL,
	tipo			VARCHAR(10),
	duracao			VARCHAR(15),
	guia			VARCHAR(20),
	telguia			VARCHAR(15),
	custo			MONEY  		NOT NULL,
	PRIMARY KEY (idatividade)
);

-- Insere as tuplas em ATIVIDADES
INSERT INTO ATIVIDADES VALUES
('1', 'Excursão Turística', 'Guiada', '10 horas', 'Fernando Costa', '+5521997074517', '1500'),
('2', 'Universal Studios Tour', 'Guiada', '6 horas', 'Andre Cardoso', '+13236576628', '4000'),
('3', 'Shelby Museum', 'Não guiada', null, null, null, '0'),
('4', 'Jetpack Aquático', 'Guiada', '2 horas', 'Andreia Santos', '+61288018815', '2500'),
('5', 'Skydiving', 'Guiada', '1 hora', 'Oliver Moura', '+61297794360', '1200'),
('6', 'Cruzeiro Asakusa', 'Guiada', '4 horas', 'Levi Ito', '+818085663251', '150'),
('7', 'Mergulho com Tubarões', 'Guiada', '2 horas', 'Sanda Freitas', '+272186011926', '1000');

-- Apaga a tabela atividade_viagem, caso exista
DROP TABLE IF EXISTS ATIVIDADE_VIAGEM CASCADE;

-- Cria a tabela atividade_viagem
CREATE TABLE ATIVIDADE_VIAGEM
(
	viagemid		INTEGER		NOT NULL,
	atividadeid		INTEGER		NOT NULL,
	PRIMARY KEY (viagemid, atividadeid),
	FOREIGN KEY (viagemid) REFERENCES VIAGEM(idviagem)
		ON UPDATE CASCADE
		ON DELETE CASCADE,
	FOREIGN KEY (atividadeid) REFERENCES ATIVIDADES(idatividade)
		ON UPDATE CASCADE
		ON DELETE CASCADE
);

-- Insere as tuplas em ATIVIDADE_VIAGEM
INSERT INTO ATIVIDADE_VIAGEM VALUES
('2', '1'),
('5', '2'),
('6', '3'),
('8', '4'),
('8', '5'),
('9', '6'),
('10', '7');

-- Apaga a tabela reserva, caso exista
DROP TABLE IF EXISTS RESERVA CASCADE;

-- Cria a tabela reserva
CREATE TABLE RESERVA
(
	idreserva		INTEGER		NOT NULL,
	status			VARCHAR(17)	NOT NULL,
	datareserva		DATE		NOT NULL,
	viagemid		INTEGER		NOT NULL,
	PRIMARY KEY (idreserva),
	FOREIGN KEY (viagemid) REFERENCES VIAGEM(idviagem)
		ON UPDATE CASCADE
		ON DELETE CASCADE
);

-- Insere as tuplas em RESERVA
INSERT INTO RESERVA VALUES
('1', 'Finalizada', '2022-01-02', '1'),
('2', 'Finalizada', '2022-02-03', '2'),
('3', 'Finalizada', '2022-02-04', '3'),
('4', 'Pgmto Realizado', '2022-03-05', '4'),
('5', 'Pgmto Realizado', '2022-03-05', '5'),
('6', 'Pgmto Realizado', '2022-04-07', '6'),
('7', 'Aguardando Pgmto', '2022-04-08', '7'),
('8', 'Aguardando Pgmto', '2022-05-09', '8'),
('9', 'Em Aberto', '2022-05-10', '9'),
('10', 'Em Aberto', '2022-06-01', '10');

-- Apaga a tabela reserva_cliente, caso exista
DROP TABLE IF EXISTS RESERVA_CLIENTE CASCADE;

-- Cria a tabela reserva_cliente
CREATE TABLE RESERVA_CLIENTE
(
	ccpf			CHAR(11)	NOT NULL,
	reservaid		INTEGER		NOT NULL,
	PRIMARY KEY (ccpf, reservaid),
	FOREIGN KEY (ccpf) REFERENCES CLIENTE(cpf)
		ON UPDATE CASCADE
		ON DELETE CASCADE,
	FOREIGN KEY (reservaid) REFERENCES RESERVA(idreserva)
		ON UPDATE CASCADE
		ON DELETE CASCADE
);

-- Insere as tuplas em RESERVA_CLIENTE
INSERT INTO RESERVA_CLIENTE VALUES
('22427362808', '1'),
('02543856722', '2'),
('61663018200', '3'),
('80664056776', '4'),
('92491269724', '5'),
('83259841202', '6'),
('55418769316', '7'),
('36662132861', '8'),
('71784527653', '9'),
('87693254737', '10');

-- Apaga a tabela Acompanhante, caso exista
DROP TABLE IF EXISTS ACOMPANHANTE CASCADE;

-- Cria a tabela Acompanhante
CREATE TABLE ACOMPANHANTE
(
	reservaid		INTEGER			NOT NULL,
	pnome			VARCHAR(15)		NOT NULL,
	unome			VARCHAR(15)		NOT NULL,
	cpf				CHAR(11)		NOT NULL,
	passaporte		CHAR(8)			NOT NULL,
	datanasc		DATE,
	tel				CHAR(11),
	relacao			VARCHAR(10),
	PRIMARY KEY (cpf),
	UNIQUE (passaporte),
	FOREIGN KEY (reservaid) REFERENCES RESERVA(idreserva)
		ON UPDATE CASCADE
		ON DELETE CASCADE
);

-- Insere as tuplas em ACOMPANHANTE
INSERT INTO ACOMPANHANTE VALUES
('2', 'Cláudio',	'Cruz',		'37482053689', 'AN098659', '1973-03-16', '81989855766', 'Irmão'),
('5', 'Pedro',		'Melo',		'64045487980', 'LL273822', '1978-01-05', '27981189252', 'Esposo'),
('5', 'Clarisse', 	'Melo', 	'96443229835', 'LT162238', '2004-05-01', '27982240654', 'Filha'),
('7', 'Sérgio', 	'Freitas',	'24515090666', 'VG614089', '1980-03-07', '54982912389', 'Esposo'),
('8', 'Kauê', 		'Baptista', '38213588827', 'BT625733', '1992-01-08', '68998068847', 'Amigo'),
('8', 'Isaac', 		'Santos', 	'23099251445', 'SI959283', '1994-05-04', '68994450403', 'Amigo'),
('9', 'Mariana', 	'Pereira', 	'13489613686', 'MR733945', '1981-04-07', '24994517654', 'Esposa');

-- Apaga a tabela hotel, caso exista
DROP TABLE IF EXISTS HOTEL CASCADE;

-- Cria a tabela hotel
CREATE TABLE HOTEL
(
	idhotel			INTEGER		NOT NULL,
	nome			VARCHAR(30)	NOT NULL,
	quarto			VARCHAR(15),
	diaria			MONEY		NOT NULL,
	numerodias		INTEGER		NOT NULL,
	endereco		VARCHAR(60),
	viagemid		INTEGER		NOT NULL,
	PRIMARY KEY (idhotel),
	FOREIGN KEY (viagemid) REFERENCES VIAGEM(idviagem)
		ON UPDATE CASCADE
		ON DELETE CASCADE
);

-- Insere as tuplas em HOTEL
INSERT INTO HOTEL VALUES
('1', 'Hotel Paulistano', 'Standard', '100', '3', 'Rua Marechal Odylio Denys, 60, São Paulo-SP', '1'),
('2', 'Ibis Rio de Janeiro', 'Twin', '296', '5', 'Avenida Martin Luther King, 126, Rio de Janeiro-RJ', '2'),
('3', 'Cullinan Hplus Premium', 'Master', '345', '7', 'SHN Quadra 4 Lote E, Brasília-DF', '4'),
('4', 'The Hollywood Roosevelt', 'Apartmento', '1197', '10', '7000 Hollywood Boulevard, Los Angeles, CA', '5'),
('5', 'Bellagio', 'Master', '1456', '7', '3600 Las Vegas Blvd S, Las Vegas-NV', '6'),
('6', 'Grand Hotel du Palais Royal', 'Deluxe', '3036', '5', '4 Rue de Valois, 75001 Paris França', '7'),
('7', 'Four Seasons Hotel Sydney', 'Triplo', '1045', '7', '199 George Street, Sydney-NSW', '8'),
('8', 'Grand Hyatt Tokyo', 'Master', '1532', '5', '6-10-3, Roppongi, Minato 106-0032, Tóquio', '9'),
('9', 'Cape Heritage Hotel', 'Standard', '307', '6', '90 Bree Street, Cidade do Cabo Central', '10');

-- Apaga a tabela Passagem, caso exista
DROP TABLE IF EXISTS PASSAGEM CASCADE;

-- Cria a tabela Passagem
CREATE TABLE PASSAGEM
(
	idpassagem			INTEGER		NOT NULL,
	tipo				VARCHAR(9)	NOT NULL,
	empresa				VARCHAR(15),
	embarque			CHAR(3)		NOT NULL,
	horarioemb			TIMESTAMP,
	preco				MONEY		NOT NULL,
	assento				INTEGER,
	reservaid			INTEGER		NOT NULL,
	PRIMARY KEY (idpassagem),
	FOREIGN KEY (reservaid) REFERENCES RESERVA(idreserva)
		ON UPDATE CASCADE
		ON DELETE CASCADE
);

-- Insere as tuplas em PASSAGEM
INSERT INTO PASSAGEM VALUES
('1', 'Ida-Volta', 'Azul', 'REC', '2022-06-02 23:01:01', '1470', '12', '1'),
('2', 'Ida-Volta', 'GOL', 'VIX', '2022-06-04 16:25:01', '1645', '4', '2'),
('3', 'Ida-Volta', 'GOL', 'VIX', '2022-06-04 16:25:01', '1645', '5', '2'),
('4', 'Ida', 'LATAM', 'BSB', '2022-06-05 14:30:01', '449', null, '3'),
('5', 'Ida-Volta', 'GOL', 'SSA', '2022-06-06 06:01:01', '1044', null, '4'),
('6', 'Ida-Volta', 'COPA', 'POA', '2022-06-06 01:30:01', '6241', '18', '5'),
('7', 'Ida-Volta', 'COPA', 'POA', '2022-06-06 01:30:01', '6241', '19', '5'),
('8', 'Ida-Volta', 'COPA', 'POA', '2022-06-06 01:30:01', '6241', '20', '5'),
('9', 'Ida-Volta', 'LATAM', 'RBR', '2022-06-07 8:45:01', '8650', '5', '6'),
('10', 'Ida-Volta', 'LATAM', 'MAO', '2022-06-08 03:05:01', '6108', '20', '7'),
('11', 'Ida-Volta', 'LATAM', 'MAO', '2022-06-08 03:05:01', '6108', '21', '7'),
('12', 'Ida-Volta', 'LATAM', 'GIG', '2022-06-08 19:35:01', '8037', '12', '8'),
('13', 'Ida-Volta', 'LATAM', 'GIG', '2022-06-08 19:35:01', '8037', '13', '8'),
('14', 'Ida-Volta', 'LATAM', 'GIG', '2022-06-08 19:35:01', '8037', '14', '8'),
('15', 'Ida-Volta', 'GOL', 'NAT', '2022-06-09 11:01:01', '7973', '7', '9'),
('16', 'Ida-Volta', 'GOL', 'NAT', '2022-06-09 11:01:01', '7973', '8', '9'),
('17', 'Ida-Volta', 'LATAM', 'PVH', '2022-06-10 02:25:01', '9765', '29', '10');