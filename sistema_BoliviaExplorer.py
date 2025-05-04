# Importar heheheh
import random
import time

#cidades turisticas 
cidades_turisticas = {
    "La Paz": {
        "altitude": "3.640m",
        "destaque": "Cidade mais alta do mundo",
        "ponto_turistico": "Vale da Lua"
    },
    "Sucre": {
        "altitude": "2.800m",
        "destaque": "Capital constitucional",
        "ponto_turistico": "Parque Cretácico"
    },
    "Santa Cruz de la Sierra": {
        "altitude": "416m",
        "destaque": "Centro econômico",
        "ponto_turistico": "Jardim Zoológico"
    },
    "Uyuni": {
        "altitude": "3.656m",
        "destaque": "Maior salar do mundo",
        "ponto_turistico": "Salar de Uyuni"
    }
}

#Comidas tipicas


comidas_tipicas = [
    "Salteña",
    "Silpancho",
    "Pique macho",
    "Chairo",
    "Anticucho",
    "Sopa de maní"
]

festas_tradicionais = {
    "Carnaval de Oruro": "Patrimônio Oral e Imaterial da Humanidade pela UNESCO.",
    "Fiesta del Gran Poder": "Celebração religiosa com danças típicas em La Paz.",
    "Inti Raymi": "Festival do Sol, herdado dos incas."
}


def menu():
    print("\n=== Explorador Cultural da Bolívia ===")
    print("1. Ver cidades turísticas")
    print("2. Conhecer comidas típicas")
    print("3. Festas tradicionais")
    print("4. Sugerir viagem aleatória")
    print("5. Sair")

def exibir_cidades():
    print("\n--- Cidades Turísticas ---")
    for cidade, dados in cidades_turisticas.items():
        print(f"\nCidade: {cidade}")
        print(f"Altitude: {dados['altitude']}")
        print(f"Destaque: {dados['destaque']}")
        print(f"Ponto turístico: {dados['ponto_turistico']}")

def exibir_comidas():
    print("\n--- Comidas Típicas ---")
    for comida in comidas_tipicas:
        print(f"- {comida}")

def exibir_festas():
    print("\n--- Festas Tradicionais ---")
    for festa, descricao in festas_tradicionais.items():
        print(f"{festa}: {descricao}")

def viagem_aleatoria():
    cidade = random.choice(list(cidades_turisticas.keys()))
    comida = random.choice(comidas_tipicas)
    festa = random.choice(list(festas_tradicionais.keys()))

    print("\nSua viagem surpresa está sendo preparada...")
    time.sleep(2)
    print(f"\nDestino: {cidade}")
    print(f"Você irá experimentar: {comida}")
    print(f"E participará da festa: {festa}")

# Programa principal
while True:
    menu()
    opcao = input("Escolha uma opção (1-5): ")

    if opcao == "1":
        exibir_cidades()
    elif opcao == "2":
        exibir_comidas()
    elif opcao == "3":
        exibir_festas()
    elif opcao == "4":
        viagem_aleatoria()
    elif opcao == "5":
        print("Hasta luego!")
        break
    else:
        print("Opção inválida. Tente novamente.")
