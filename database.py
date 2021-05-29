import sqlite3 as sql

# Estabelecer conexão com banco de dados
con = sql.connect('banco.db')
# Criar cursor para manipular db
c = con.cursor()

# Criar tabela caso não exista
def create_table():
	c.execute('''CREATE TABLE IF NOT EXISTS users(
	name varchar(20) NOT NULL,
	password varchar(20),
	age int(3),
	email varchar,
	country varchar
	)''')
	con.commit()

# Registro de novos usuários na base
def register(nome, senha, idade, email, pais):
	c.execute(f'INSERT INTO users (name, password, age, email, country) VALUES (\'{nome}\', \'{senha}\', \'{idade}\', \'{email}\', \'{pais}\')')
	con.commit()

# Selecionar ID baseado no usuário e senha
def login(name, password):
	rowid = c.execute(f'SELECT rowid, name, password, age, email, country from users where name = \'{name}\' AND password = \'{password}\'')
	data = []
	for row in rowid:
		data.append(row)
		return data

# Editar dados
def edit(rowid, nome, senha, idade, email, pais):
	c.execute(f'UPDATE users set name = \'{nome}\' where rowid = \'{rowid}\'')
	c.execute(f'UPDATE users set password = \'{senha}\' where rowid = \'{rowid}\'')
	c.execute(f'UPDATE users set age = \'{idade}\' where rowid = \'{rowid}\'')
	c.execute(f'UPDATE users set email = \'{email}\' where rowid = \'{rowid}\'')
	c.execute(f'UPDATE users set country = \'{pais}\' where rowid = \'{rowid}\'')
	con.commit()

# Deletar dados
def delete(rowid):
	c.execute(f'DELETE from users where rowid = \'{rowid}\'')
	con.commit()
	
def disconnect():
	# Encerrar sessão
	con.close()
