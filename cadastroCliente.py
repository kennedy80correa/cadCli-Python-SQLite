import sqlite3, time, tkinter

#conexão com banco de dados
conectar = sqlite3.connect('agenda.db')
c = conectar.cursor()

#FAZER FUNÇÃO PARA CRIAR BANCO APENAS UMA VEZ --->
#criação banco de dados
'''
c.execute("""
    CREATE TABLE clientes( 
           id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
           nome TEXT NOT NULL, 
           data_nasc DATE NOT NULL, 
           tel TEXT NOT NULL, 
           endereco TEXT, 
           email TEXT,
           inss TEXT
    );
    """)
print('Tabela criada com sucesso.')
c.close()
'''
# <--- FAZER FUNÇÃO PARA CRIAR BANCO APENAS UMA VEZ

#FAZER FUNÇÃO PARA INSERIR DADOS NO BANCO //////CADASTRO --->
print('\n\n\t\t\tCADASTRAR CLIENTE\n\n')
#solicitando dados do usuário
p_nome = input('Nome: ')
p_dtNasc = input('\nData de Nascimento: ')
p_tel = input('\nTelefone: ')
p_end = input('\nEndereço: ')
p_email = input('\nEmail: ')
p_inss = input('\nChave INSS: ')

#inserindo dados na tabela
c.execute("""
INSERT INTO clientes (nome, data_nasc, tel, endereco, email, inss)
VALUES (?,?,?,?,?,?)
""", (p_nome, p_dtNasc, p_tel, p_end, p_email, p_inss))

conectar.commit()

print('\n\t\tCadastro efetuado com sucesso!')

conectar.close()

# <--- FAZER FUNÇÃO PARA INSERIR DADOS NO BANCO //////CADASTRO