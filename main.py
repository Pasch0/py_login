import interface as show
import database as db

db.create_table()

user_data = []

# Definindo função de login
def login():
	login = show.login()
	if login == 'Registrar':
		return register()
		login.window.close()
	else:
		check_login = db.login(login['name'], login['password'])
		if check_login == None:
			print('Nome ou senha errados!')
		else:
			for data in check_login:
				user_data.append(data[0])
				user_data.append(data[1])
				user_data.append(data[2]) 
				user_data.append(data[3]) 
				user_data.append(data[4])
				user_data.append(data[5])
				return logged(user_data[0], user_data[1], user_data[2], user_data[3], user_data[4], user_data[5])
		
# Definindo função de registro
def register():
	register = show.register()
	if register == 'Login':
		return login()
		register.window.close()
	else:
		insert_db = db.register(register['name'], register['password'], register['age'], register['email'], register['country'])

# Apresentação de dados quando logado
def logged(rowid, name, password, age, email, country):
	logged = show.logged(name, age, email, country)
	if logged == 'Editar':
		return edit(user_data[0])
	elif logged == 'Excluir':
		return db.delete(rowid)
	
# Janela de edição vinculado ao db
def edit(rowid):
	edit = show.edit(rowid)
	if edit['name'] != '':
		db.edit(rowid, edit['name'], edit['password'], edit['age'], edit['email'], edit['country'])

login()
