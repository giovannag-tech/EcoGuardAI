import os

def menu():
    print("\n==============================")
    print("🌱 ECOGUARD AI")
    print("==============================")
    print("1 - Gerar dados simulados")
    print("2 - Salvar dados no PostgreSQL")
    print("3 - Treinar modelo de Machine Learning")
    print("4 - Gerar alertas ambientais")
    print("5 - Executar visão computacional")
    print("6 - Abrir dashboard interativo")
    print("0 - Sair")
    print("==============================")


while True:
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        os.system("python src/gerar_dados.py")

    elif opcao == "2":
        os.system("python src/salvar_banco.py")

    elif opcao == "3":
        os.system("python src/treinar_modelo.py")

    elif opcao == "4":
        os.system("python src/gerar_alertas.py")

    elif opcao == "5":
        os.system("python visao_computacional/detectar_folha.py")

    elif opcao == "6":
        os.system("streamlit run src/dashboard.py")

    elif opcao == "0":
        print("Encerrando o EcoGuard AI...")
        break

    else:
        print("Opção inválida. Tente novamente.")