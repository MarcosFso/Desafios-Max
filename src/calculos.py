def calcular_estagiario(salario):
    return salario, 0, 0


def calcular_clt(salario):
    inss = salario * 0.08
    irrf = salario * 0.10 if salario > 2000 else 0
    liquido = salario - inss - irrf
    return liquido, inss, irrf


def calcular_freelancer(horas, valor_hora):
    bruto = horas * valor_hora
    desconto = bruto * 0.05
    liquido = bruto - desconto
    return liquido, desconto, 0