def criar_produto(nome, preco, estoque):
    if not nome:
        raise ValueError("Nome inválido")

    if preco <= 0:
        raise ValueError("Preço inválido")

    if estoque < 0:
        raise ValueError("Estoque inválido")

    return {
        "nome": nome,
        "preco": preco,
        "estoque": estoque
    }


def adicionar_produto(produtos, produto):
    for p in produtos:
        if p["nome"].lower() == produto["nome"].lower():
            raise ValueError("Produto já existe")

    produtos.append(produto)
    return produtos


def listar_produtos(produtos):
    if not produtos:
        print("Nenhum produto cadastrado.")
        return

    for i, p in enumerate(produtos):
        print(f"{i+1}. {p['nome']} - R$ {p['preco']:.2f} - Estoque: {p['estoque']}")


def calcular_venda(produto, quantidade):
    if quantidade <= 0:
        raise ValueError("Quantidade inválida")

    if quantidade > produto["estoque"]:
        raise ValueError("Estoque insuficiente")

    valor_bruto = produto["preco"] * quantidade
    desconto = valor_bruto * 0.05 if quantidade > 10 else 0
    valor_final = valor_bruto - desconto

    produto["estoque"] -= quantidade

    return {
        "produto": produto["nome"],
        "quantidade": quantidade,
        "valor_bruto": valor_bruto,
        "desconto": desconto,
        "valor_final": valor_final
    }


def adicionar_venda(vendas, venda, cliente):
    venda["cliente"] = cliente
    vendas.append(venda)

    # mantém apenas as últimas 5 — remove o mais antigo do fundo
    if len(vendas) > 5:
        vendas.pop(0)

    return vendas


def total_arrecadado(vendas):
    return sum(v["valor_final"] for v in vendas)


def gerar_relatorio(vendas):
    if not vendas:
        print("Nenhuma venda realizada.")
        return

    print("\n=== RELATÓRIO DE VENDAS (ÚLTIMAS 5) ===\n")

    for v in vendas:
        print(f"Cliente: {v['cliente']}")
        print(f"Produto: {v['produto']}")
        print(f"Quantidade: {v['quantidade']}")
        print(f"Valor Bruto: R$ {v['valor_bruto']:.2f}")
        print(f"Desconto: R$ {v['desconto']:.2f}")
        print(f"Valor Final: R$ {v['valor_final']:.2f}")
        print()

    print(f"Total arrecadado: R$ {total_arrecadado(vendas):.2f}")


def salvar_relatorio(vendas):
    try:
        with open("relatorio_vendas.txt", "w", encoding="utf-8") as f:
            f.write("=== RELATÓRIO DE VENDAS (ÚLTIMAS 5) ===\n\n")

            for v in vendas:
                f.write(f"Cliente: {v['cliente']}\n")
                f.write(f"Produto: {v['produto']}\n")
                f.write(f"Quantidade: {v['quantidade']}\n")
                f.write(f"Valor Bruto: R$ {v['valor_bruto']:.2f}\n")
                f.write(f"Desconto: R$ {v['desconto']:.2f}\n")
                f.write(f"Valor Final: R$ {v['valor_final']:.2f}\n\n")

            f.write(f"Total arrecadado: R$ {total_arrecadado(vendas):.2f}")

        print("Relatório salvo com sucesso!")

    except Exception as e:
        print("Erro ao salvar arquivo:", e)