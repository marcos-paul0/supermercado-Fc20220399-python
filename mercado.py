import os
from datetime import datetime

# Configurações do Caixa
cash_register = {
    "is_open": False,
    "initial_value": 1000.00,
    "current_value": 0.00,
}

# Lista de produtos
products = [
    {"ID": "001", "Nome": "Arroz (1kg)", "Valor": 5.0, "Validade": "12/12/2024", "Garantia": "-", "Estoque": 40},
    {"ID": "002", "Nome": "Feijão (1kg)", "Valor": 6.5, "Validade": "10/12/2024", "Garantia": "-", "Estoque": 35},
    {"ID": "003", "Nome": "Açúcar (1kg)", "Valor": 3.0, "Validade": "15/01/2025", "Garantia": "-", "Estoque": 45},
    {"ID": "004", "Nome": "Sal (1kg)", "Valor": 1.5, "Validade": "18/12/2024", "Garantia": "-", "Estoque": 50},
    {"ID": "005", "Nome": "Óleo de Soja (900ml)", "Valor": 4.0, "Validade": "25/02/2025", "Garantia": "-", "Estoque": 30},
    {"ID": "006", "Nome": "Leite (1L)", "Valor": 3.9, "Validade": "02/12/2024", "Garantia": "-", "Estoque": 60},
    {"ID": "007", "Nome": "Café (500g)", "Valor": 8.0, "Validade": "05/01/2025", "Garantia": "-", "Estoque": 30},
    {"ID": "008", "Nome": "Macarrão (500g)", "Valor": 2.5, "Validade": "18/12/2024", "Garantia": "-", "Estoque": 50},
    {"ID": "009", "Nome": "Farinha de Trigo (1kg)", "Valor": 4.2, "Validade": "15/03/2025", "Garantia": "-", "Estoque": 40},
    {"ID": "010", "Nome": "Pão de Forma (500g)", "Valor": 5.9, "Validade": "10/02/2025", "Garantia": "-", "Estoque": 50},
    {"ID": "011", "Nome": "Microondas", "Valor": 380.0, "Validade": "-", "Garantia": "6 meses", "Estoque": 12},
    {"ID": "012", "Nome": "Ventilador", "Valor": 130.0, "Validade": "-", "Garantia": "6 meses", "Estoque": 20},
    {"ID": "013", "Nome": "Fogão 4 Bocas", "Valor": 850.0, "Validade": "-", "Garantia": "12 meses", "Estoque": 10},
    {"ID": "014", "Nome": "Geladeira", "Valor": 1900.0, "Validade": "-", "Garantia": "12 meses", "Estoque": 7},
    {"ID": "015", "Nome": "Máquina de Lavar Roupa", "Valor": 1550.0, "Validade": "-", "Garantia": "12 meses", "Estoque": 4},
    {"ID": "016", "Nome": "Aspirador de Pó", "Valor": 220.0, "Validade": "-", "Garantia": "6 meses", "Estoque": 12},
    {"ID": "017", "Nome": "Liquidificador", "Valor": 85.0, "Validade": "-", "Garantia": "6 meses", "Estoque": 25},
    {"ID": "018", "Nome": "Batedeira", "Valor": 160.0, "Validade": "-", "Garantia": "6 meses", "Estoque": 12},
]

# Log de vendas
sales_log = []

# Funções principais
def sell_product(product_id, quantity):
    if not cash_register["is_open"]:
        print("O caixa está fechado. Abra-o antes de realizar vendas.")
        return

    # Normalizamos o ID para comparar corretamente
    normalized_id = str(product_id).zfill(3)

    for product in products:
        if product["ID"] == normalized_id:
            if product["Estoque"] >= quantity:
                total_price = product["Valor"] * quantity
                product["Estoque"] -= quantity
                cash_register["current_value"] += total_price
                sales_log.append({
                    "ID": product["ID"],
                    "Nome": product["Nome"],
                    "Quantidade": quantity,
                    "Total": total_price,
                    "Data": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                })
                print(f"Venda realizada: {quantity}x {product['Nome']} - Total: R$ {total_price:.2f}")
            else:
                print("Estoque insuficiente.")
            return

    print("Produto não encontrado.")

def open_cash_register():
    if cash_register["is_open"]:
        print("O caixa já está aberto.")
        return

    cash_register["is_open"] = True
    cash_register["current_value"] = cash_register["initial_value"]
    print(f"Caixa aberto com R${cash_register['current_value']:.2f}")

def close_cash_register():
    if not cash_register["is_open"]:
        print("O caixa já está fechado.")
        return

    print(f"Caixa fechado com R${cash_register['current_value']:.2f}")
    cash_register["is_open"] = False

def show_daily_sales():
    print("\nVendas do dia:")
    if not sales_log:
        print("Nenhuma venda registrada hoje.")
        return

    for sale in sales_log:
        print(f"ID: {sale['ID']} | Produto: {sale['Nome']} | Quantidade: {sale['Quantidade']} | Total: R$ {sale['Total']:.2f} | Data: {sale['Data']}")

def show_products():
    print("\nLista de produtos:")
    for product in products:
        print(f"ID: {product['ID']} | Nome: {product['Nome']} | Valor: R$ {product['Valor']:.2f} | Estoque: {product['Estoque']}")

# Menu principal
def main():
    while True:
        print("\n1. Abrir Caixa")
        print("2. Fechar Caixa")
        print("3. Nova Venda")
        print("4. Mostrar Produtos")
        print("5. Relatório de Vendas")
        print("6. Sair")
        
        choice = input("Escolha uma opção: ").strip()

        if choice == "1":
            open_cash_register()
        elif choice == "2":
            close_cash_register()
        elif choice == "3":
            product_id = input("Informe o ID do produto: ").strip()
            quantity = int(input("Informe a quantidade: ").strip())
            sell_product(product_id, quantity)
        elif choice == "4":
            show_products()
        elif choice == "5":
            show_daily_sales()
        elif choice == "6":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
