# Sistema de Cafeteria em Python

cardapio = {
    1: {"nome": "Café Expresso", "preco": 4.50},
    2: {"nome": "Cappuccino", "preco": 6.00},
    3: {"nome": "Latte", "preco": 5.50},
    4: {"nome": "Pão de Queijo", "preco": 3.00},
    5: {"nome": "Bolo de Chocolate", "preco": 4.00}
}
pedido = []

def exibir_cardapio():
    print("\n--- CARDÁPIO ---")
    for codigo, item in cardapio.items():
        print(f"{codigo} - {item['nome']} - R${item['preco']:.2f}")

def fazer_pedido():
    while True:
        exibir_cardapio()
        try:
            cod = int(input("\nDigite o código do item (0 para finalizar): "))
            if cod == 0:
                break
            if cod not in cardapio:
                print("Código inválido. Tente novamente.")
                continue
            qtd = int(input("Quantidade: "))
            pedido.append({"item": cardapio[cod]["nome"], 
                           "preco": cardapio[cod]["preco"], 
                           "quantidade": qtd})
            print(f"Adicionado {qtd}x {cardapio[cod]['nome']} ao pedido.\n")
        except ValueError:
            print("Entrada inválida. Digite números.")
            continue

def exibir_recibo():
    if not pedido:
        print("Nenhum item foi pedido.")
        return
    
    print("\n--- RECIBO ---")
    total = 0
    for item in pedido:
        subtotal = item["preco"] * item["quantidade"]
        print(f"{item['quantidade']}x {item['item']} - R${subtotal:.2f}")
        total += subtotal
    print(f"TOTAL: R${total:.2f}")
    print("Obrigado pela preferência! ☕")

# Execução do programinha
print("Bem-vindo à Cafeteria Python!\n")
fazer_pedido()
exibir_recibo()
