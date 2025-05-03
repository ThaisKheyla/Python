import time

# Dados simulados de usuários... nome de usuário: senha, saldo, histórico
usuarios = {
    'ana': ['1234', 1000.0, []],
    'bruno': ['4321', 500.0, []],
    'carla': ['0000', 1200.0, []]
}

def autenticar():
    print("Login no Sistema Bancário")
    usuario = input("Usuário: ").strip()
    senha = input("Senha: ").strip()

    if usuario in usuarios and usuarios[usuario][0] == senha:
        print(f"\nBem-vindo(a), {usuario}!")
        return usuario
    else:
        print("Usuário ou senha incorretos.")
        return None

def mostrar_menu():
    print("\nMENU")
    print("1. Ver saldo")
    print("2. Depositar")
    print("3. Sacar")
    print("4. Transferir")
    print("5. Ver histórico")
    print("6. Sair")

def registrar(usuario, operacao):
    usuarios[usuario][2].append(f"[{time.strftime('%H:%M:%S')}] {operacao}")

def executar_banco():
    usuario = None
    while not usuario:
        usuario = autenticar()

    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == '1':
            saldo = usuarios[usuario][1]
            print(f"Saldo atual: R$ {saldo:.2f}")
            registrar(usuario, f"Consultou saldo: R$ {saldo:.2f}")

        elif opcao == '2':
            valor = float(input("Valor para depositar: R$ "))
            usuarios[usuario][1] += valor
            print(f"Depósito de R$ {valor:.2f} realizado.")
            registrar(usuario, f"Depositou R$ {valor:.2f}")

        elif opcao == '3':
            valor = float(input("Valor para sacar: R$ "))
            if valor <= usuarios[usuario][1]:
                usuarios[usuario][1] -= valor
                print(f"Saque de R$ {valor:.2f} realizado.")
                registrar(usuario, f"Retirou R$ {valor:.2f}")
            else:
                print("Saldo insuficiente.")

        elif opcao == '4':
            destino = input("Transferir para (usuário): ").strip()
            if destino in usuarios:
                valor = float(input("Valor da transferência: R$ "))
                if valor <= usuarios[usuario][1]:
                    usuarios[usuario][1] -= valor
                    usuarios[destino][1] += valor
                    registrar(usuario, f"Transferiu R$ {valor:.2f} para {destino}")
                    registrar(destino, f"Recebeu R$ {valor:.2f} de {usuario}")
                    print("Transferência realizada com sucesso.")
                else:
                    print("Saldo insuficiente.")
            else:
                print("Usuário destino não encontrado.")

        elif opcao == '5':
            print("Histórico de operações:")
            historico = usuarios[usuario][2]
            if historico:
                for h in historico:
                    print(f" - {h}")
            else:
                print("Nenhuma operação registrada.")

        elif opcao == '6':
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida. Tente novamente.")

executar_banco()
