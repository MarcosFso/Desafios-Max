from src.funcionario import processar_funcionario


def gerar_relatorio(funcionarios):
    texto = "\n=== Relatório de Folha de Pagamento ===\n\n"
    total = 0

    for f in funcionarios:
        dados = processar_funcionario(f)
        total += dados["liquido"]

        texto += f"Nome: {dados['nome']}\n"
        texto += f"Tipo: {dados['tipo']}\n"
        texto += f"Salário Bruto: R$ {dados['bruto']:.2f}\n"
        texto += f"Desconto INSS: R$ {dados['inss']:.2f}\n"
        texto += f"Desconto IRRF: R$ {dados['irrf']:.2f}\n"
        texto += f"Salário Líquido: R$ {dados['liquido']:.2f}\n"
        texto += "-" * 30 + "\n"

    texto += f"Total pago pela empresa: R$ {total:.2f}"
    return texto


import os

def salvar_relatorio(conteudo, nome_arquivo="relatorio_folha.txt"):
    try:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        
        caminho_pasta = os.path.join(base_dir, "..", "docs")
        
        if not os.path.exists(caminho_pasta):
            os.makedirs(caminho_pasta)

        caminho_final = os.path.join(caminho_pasta, nome_arquivo)

        with open(caminho_final, "w", encoding="utf-8") as f:
            f.write(conteudo)
        return True
    except Exception as e:
        print("Erro ao salvar:", e)
        return False