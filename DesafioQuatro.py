import pandas as pd

columns = ['Alimentação Inicial (kg/h)', 'Alimentação de Eter (kg/h)', 'Percentagem de Ácido Acético na Alimentação Inicial (%)',
           'Percentagem de Ácido Acético no Extrato (%)', 'Massa de Ácido Acético na Alimentação (kg/h)',
           'Ácido Acético Extraído no Extrato (kg/h)', 'Total do Extrato (kg/h)', 'Raffinate (kg/h)', 
           'Saída de Reciclagem (kg/h)']

while True:
    print("-----------------------")
    print("1 - Realizar simulação.")
    print("2 - Ver dados da simulaçãos.")
    print("3 - Sair do sistema.")
    print("-----------------------")


    value = input("Escolha uma opção do menu do sistema.")

    match value:
        case "1":
            print("\n>>> Você escolheu realizar uma simulação.")
            try:

                feedIn = float(input("Digite a alimentação inicial em kg/h: "))
                feedSolvent = float(input("Digite a alimentação de eter (solvente) em kg/h: "))
                percentAcetic = float(input("Percentagem de ácido acético na alimentação inicial (%): "))
                percentExtract = float(input("Percentagem de ácido acético no extrato (%): "))
                percentInExtract = float(input("Percentagem de ácido acético extraído no extrato (%): "))
                massAcetic = feedIn * (percentAcetic / 100)
                
                if feedIn < 0 or feedSolvent < 0 or percentAcetic < 0 or percentExtract < 0 or percentInExtract < 0:
                    print("\nERRO: Valores negativos não são permitidos. Tente novamente.")
               

                outExtractAcetic = massAcetic * (percentInExtract / 100)
                outExtractTotal = outExtractAcetic / (percentExtract / 100)
                raffinate = (feedIn + feedSolvent) - outExtractTotal
                outRecycle = 0.5 * raffinate

                dataset = pd.DataFrame([[feedIn, feedSolvent, percentAcetic, percentExtract, massAcetic, outExtractAcetic, outExtractTotal, raffinate, outRecycle]], columns=columns)
                dataset.to_csv("Simulacao_Dados.txt", index=False, sep='\t')

                print("\n--- Simulação Realizada e Salva com Sucesso! ---")

            except ValueError:
                print("\nERRO: Por favor, digite apenas números para os valores da simulação.")

        case "2":
            print("Você escolheu ver os dados da simulação.")
            print(dataset)
            
        case "3": 
            print("Você escolheu sair do sistema.")
            print("Saindo do sistema...")
            break

        case _:
            print("Opção inválida. Tente novamente.")