from src.relatorio import gerar_relatorio, salvar_relatorio

funcionarios = []


def nome_valido(nome):
    return all(c.isalpha() or c.isspace() for c in nome)


def main():
    while True:
        print("\n1. Cadastrar funcionário")
        print("2. Gerar relatório")
        print("3. Salvar relatório")
        print("4. Sair")

        op = input("Escolha: ")

        if op == "1":
            try:
                nome = input("Nome: ").strip()

                if not nome:
                    print("Erro: nome não pode ser vazio!")
                    continue

                if not nome_valido(nome):
                    print("Erro: nome deve conter apenas letras e espaços!")
                    continue

                tipo = input("Tipo (estagiario/clt/freelancer): ").lower()

                if tipo in ["estagiario", "clt"]:
                    salario = float(input("Salário: "))

                    if salario <= 0:
                        print("Erro: salário deve ser maior que zero!")
                        continue

                    funcionarios.append({
                        "nome": nome,
                        "tipo": tipo,
                        "salario": salario
                    })

                elif tipo == "freelancer":
                    horas = float(input("Horas: "))
                    valor = float(input("Valor/hora: "))

                    if horas <= 0 or valor <= 0:
                        print("Erro: valores devem ser maiores que zero!")
                        continue

                    funcionarios.append({
                        "nome": nome,
                        "tipo": tipo,
                        "horas": horas,
                        "valor": valor
                    })

                else:
                    print("Tipo inválido")

            except ValueError:
                print("Erro: entrada inválida!")

        elif op == "2":
            print(gerar_relatorio(funcionarios))

        elif op == "3":
            conteudo = gerar_relatorio(funcionarios)
            sucesso = salvar_relatorio(conteudo, "docs/relatorio_folha.txt")

            if sucesso:
                print("Relatório salvo com sucesso na pasta docs!")
            else:
                print("Erro ao salvar relatório")

        elif op == "4":
            print("Saindo...")
            break

        else:
            print("Opção inválida!")


if __name__ == "__main__":
    main()