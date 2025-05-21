while True:
    # menu
    print("\nMENU:")
    print("[1] Olá")
    print("[2] Ajuda")
    print("[3] Sair")

    # Solicita a opção do usuário
    opcao = input("Escolha uma opção: ")

    # Verifica a opção escolhida
    if opcao == "1":
        print("Olá! Seja bem-vindo! ")
    elif opcao == "2":
        print("Você pode escolher:\n1 para saudação,\n2 para ajuda,\n3 para sair do programa.")
    elif opcao == "3":
        print("Saindo do programa. Até logo!")
        break
    else:
        print("Opção inválida. Tente novamente.")
