from src.calculos import calcular_estagiario, calcular_clt, calcular_freelancer


def processar_funcionario(func):
    tipo = func["tipo"]

    if tipo == "estagiario":
        bruto = func["salario"]
        liquido, inss, irrf = calcular_estagiario(bruto)

    elif tipo == "clt":
        bruto = func["salario"]
        liquido, inss, irrf = calcular_clt(bruto)

    elif tipo == "freelancer":
        bruto = func["horas"] * func["valor"]
        liquido, inss, irrf = calcular_freelancer(func["horas"], func["valor"])

    else:
        raise ValueError("Tipo inválido")

    return {
        "nome": func["nome"],
        "tipo": tipo,
        "bruto": bruto,
        "inss": inss,
        "irrf": irrf,
        "liquido": liquido,
    }