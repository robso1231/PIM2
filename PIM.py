import os
import time
import json

# Limpar terminal
def limpar_terminal():
    sistema = os.name
    if sistema == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# JSON
ARQUIVO_USUARIOS = "usuarios.json"

# Carregar usuários JSON
def carregar_usuarios():
    if os.path.exists(ARQUIVO_USUARIOS):
        with open(ARQUIVO_USUARIOS, "r") as file:
            return json.load(file)
    return {}

# Salvar usuários JSON
def salvar_usuarios():
    with open(ARQUIVO_USUARIOS, "w") as file:
        json.dump(usuarios, file, indent=4)

# Altera usuários JSON
usuarios = carregar_usuarios()

# Login
def login():
    limpar_terminal()
    print("🔑 Sistema de Login 🔑")
    usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")

    if usuario in usuarios and usuarios[usuario] == senha:
        print(f"Bem-vindo, {usuario}!\nRedirecionando para o menu inicial, aguarde...")
        time.sleep(2)
        menu_inicial(usuario)
        return True
    else:
        print("Usuário ou senha incorretos. Tente novamente.")
        time.sleep(2)
        return False

# Registro
def registrar():
    limpar_terminal()
    print("📋 Sistema de Registro 📋")
    usuario = input("Digite um nome de usuário: ")
    if usuario in usuarios:
        print("Usuário já existe. Tente outro nome.")
        time.sleep(2)
        return False
    
    senha = input("Digite uma senha: ")
    senha_confirmada = input("Confirme sua senha: ")
    
    if senha != senha_confirmada:
        print("❌ As senhas não coincidem. Tente novamente.")
        time.sleep(2)
        return False
    
    usuarios[usuario] = senha
    salvar_usuarios()
    print(f"✅ Usuário {usuario} registrado com sucesso!")
    time.sleep(2)
    return True

# Painel Login e Registro
def loginregistro():
    while True:
        limpar_terminal()
        print("Selecione a opção abaixo:")
        print("[1] - Login")
        print("[2] - Registrar")
        print("[3] - Voltar")
        
        try:
            opcao = int(input("Digite sua escolha: "))
            if opcao == 1:
                if login():
                    break
            elif opcao == 2:
                if registrar():
                    print("✅ Agora voce pode fazer login.")
            elif opcao == 3:
                break
            else:
                print("⚠️ Opção inválida. Tente novamente.")
        except ValueError:
            print("⚠️ Por favor, insira um número válido.")

# Menu inicial
def menu_inicial(usuario):
    while True:
        limpar_terminal()
        inicial = int(input(f"Olá {usuario}, Selecione a opção abaixo:\n[1] - Office\n[2] - Aulas\n[3] - Sair\n"))
        
        if inicial == 1:
            office()
        elif inicial == 2:
            aulas()
        elif inicial == 3:
            limpar_terminal()
            print("\nSaindo... Até mais!")
            break
        else:
            print("⚠️ Opção inválida. Tente novamente.")

# Office
def office():
    while True:
        limpar_terminal()
        office = int(input("Para voltar ao menu inicial digite 2: "))
        if office == 2:
            print("Voltando ao menu inicial...")
            break
        else:
            print("⚠️ Opção inválida. Tente novamente.")

# Aulas
def aulas():
    while True:
        limpar_terminal()
        aulas = int(input("Selecione uma opção de Aulas:\n[1] - 🐍 Aulas de Python\n[2] - ➗ Aulas de Matemática\n[3] - 🏠 Voltar ao menu inicial\n"))
        if aulas == 1:
            print("Você escolheu Aulas de Python.")
        elif aulas == 2:
            print("Você escolheu Aulas de Matemática.")
        elif aulas == 3:
            print("Voltando ao menu inicial...")
            break
        else:
            print("⚠️ Opção inválida. Tente novamente.")

# Inicia o sistema
loginregistro()