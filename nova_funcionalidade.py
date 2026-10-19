def listar_requisitos():
    return [
        "Registrar uma solicitação do cliente",
        "Consultar o status da solicitação",
    ]


if __name__ == "__main__":
    for requisito in listar_requisitos():
        print(requisito)