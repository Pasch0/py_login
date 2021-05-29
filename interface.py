import PySimpleGUI as sg

# Janela de exemplo
def example():
	layout = [ [sg.Text('Minha Janela')],
		[sg.Input(key='-IN-')],
		[sg.Text(size=(20,1), key='-OUT-')],
		[sg.Button('Seguir'), sg.Button('Sair')]
		]

	window = sg.Window('Janela teste', layout, size=(400, 200), resizable=True, icon=None)

	while True:
		event, values = window.read()
		if event in (None, 'Sair'):
			break
		elif event == 'Seguir':
			window['-OUT-'].update(values['-IN-'])
	window.close()

# Janela de login
def login():
	# Definindo Layout da janela
	layout = [	[sg.Text('Login')],
	[sg.Text('Nome'), sg.Input(key='name')],
	[sg.Text('Senha'), sg.Input(key='password')],
	[sg.Button('Entrar'), sg.Button('Registrar')]
	]
	# Criar janela
	window = sg.Window('Login', layout, size=(400,200), resizable=True, icon=None)
	event, values = window.read()
	if event == 'Entrar':
		dados = values
		window.close()
		return dados
	elif event == 'Registrar':
		window.close()
		return 'Registrar'

# Janela de registro
def register():
	# Definindo layout da janela
	layout = [	[sg.Text('Registre-se')],
	[sg.Text('Nome'), sg.Input(key='name')],
	[sg.Text('Senha'), sg.Input(key='password')],
	[sg.Text('Idade'), sg.Input(key='age')],
	[sg.Text('E-mail'), sg.Input(key='email')],
	[sg.Text('País'), sg.Input(key='country')],
	[sg.Button('Registrar'), sg.Button('Login')]
	]
	# Criar janela
	window = sg.Window('Registro', layout, size=(400,200), resizable=True, icon=None)
	event, values = window.read()
	if event == 'Login':
		window.close()
		return 'Login'
	elif event == 'Registrar':
		dados = values
		window.close()
		return dados
	window.close()

# Janela de visualização de dados logado
def logged(name, age, email, country):
	# Definindo layout
	layout = [	[sg.Text(f'Nome: {name}')],
	[sg.Text(f'Idade: {age}')],
	[sg.Text(f'E-mail: {email}')],
	[sg.Text(f'País: {country}')],
	[sg.Button('Editar'), sg.Button('Excluir')]
	]
	window = sg.Window('Meus dados', layout, size=(400,200), resizable=True, icon=None)
	event, values = window.read()
	if event == 'Editar':
		window.close()
		return 'Editar'
	elif event == 'Excluir':
		window.close()
		return 'Excluir'
	window.close()

# Janela de edição de dados
def edit(rowid):
	# Definir layout
	layout = [	[sg.Text('Nome'), sg.Input(key='name')],
	[sg.Text('Senha'), sg.Input(key='password')],
	[sg.Text('Idade'), sg.Input(key='age')],
	[sg.Text('E-mail'), sg.Input(key='email')],
	[sg.Text('País'), sg.Input(key='country')],
	[sg.Button('Salvar')]
	]
	window = sg.Window('Editar dados', layout, size=(400,200), resizable=True, icon=None)
	event, values = window.read()
	if event == 'Salvar':
		dados = values
		window.close()
		return dados
		window.close()
