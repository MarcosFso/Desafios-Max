from utils.loja import *

def main():
    produtos = []
    vendas = []

    while True:
        print("\n=== MENU ===")
        print("1 - Cadastrar produto")
        print("2 - Realizar venda")
        print("3 - Gerar relatório")
        print("4 - Salvar relatório")
        print("5 - Sair")

        opcao = input("Escolha: ")

        try:
            if opcao == "1":
                nome = input("Nome do produto: ").strip()
                if not nome:
                    print("Nome inválido!")
                    continue

                try:
                    preco = float(input("Preço: "))
                    if preco <= 0:
                        print("O preço deve ser maior que zero!")
                        continue
                    estoque = int(input("Estoque: "))
                    if estoque < 0:
                        print("O estoque não pode ser negativo!")
                        continue
                except ValueError:
                    print("Digite valores numéricos válidos!")
                    continue

                produto = criar_produto(nome, preco, estoque)
                produtos = adicionar_produto(produtos, produto)

                print("Produto cadastrado!")

            elif opcao == "2":
                if not produtos:
                    print("Cadastre produtos primeiro!")
                    continue

                cliente = input("Nome do cliente: ").strip()
                if not cliente:
                    print("Nome do cliente inválido!")
                    continue

                listar_produtos(produtos)

                escolha = input("Escolha o produto (índice ou nome): ").strip()

                # tenta por índice primeiro
                try:
                    indice = int(escolha) - 1
                except ValueError:
                    # se não for número, busca por nome
                    indice = next(
                        (i for i, p in enumerate(produtos) if p["nome"].lower() == escolha.lower()),
                        -1
                    )

                if indice < 0 or indice >= len(produtos):
                    print("Produto inválido!")
                    continue

                produto = produtos[indice]

                # LOOP para quantidade correta
                while True:
                    try:
                        quantidade = int(input("Quantidade: "))
                        if quantidade <= 0 or quantidade > produto["estoque"]:
                            print("Quantidade inválida ou estoque insuficiente!")
                            continue
                        break
                    except ValueError:
                        print("Digite um número válido!")

                venda = calcular_venda(produto, quantidade)
                vendas = adicionar_venda(vendas, venda, cliente)

                print("Venda realizada!")

            elif opcao == "3":
                gerar_relatorio(vendas)

            elif opcao == "4":
                salvar_relatorio(vendas)

            elif opcao == "5":
                print("Saindo...")
                break

            else:
                print("Opção inválida!")

        except Exception as e:
            print("Erro:", e)


if __name__ == "__main__":
    main()