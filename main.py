
starturp = {
    "nome ": "cyberpulse tech" ,
    "sagmento": "segurança da informacao",
    "ano_adesao": "2026"
}
solucoes_ativas =["firewall IA", "scan de vunerabilidades"]
print(print"nome da starturp: {startup['nome']}")
print("solucoes_ativas",solucoes_ativas[0])


with open("custos_cloud.csv", "r", encoding="utf-8") as arquivo:
    cabecalho = arquivo.readline()
    linha_dados_1 = arquivo.readline()
    linha_dados_2  = arquivo.readline()
    linha_dados_3 = arquivo.readline()
    linha_dados_4 = arquivo.readline()

    print(cabecalho, end="")
    print(linha_dados_1, end="")
    print(linha_dados_2, end="")
    print(linha_dados_3, end="")
    print(linha_dados_4, end="")

    custos_1 = float(linha_dados_1.split(",")[1])
    custos_2 = float(linha_dados_2.split(",")[1])
    custos_3 = float(linha_dados_3.split(",")[1])
    custos_4 = float(linha_dados_4.split(",")[1])
    custo_totais = custos_1 + custos_2 +custos_3 + custos_4

    print("custos totais: ", custos custo_totais)
    print("startup: ", startup["nome"])
    print("bancada alocada: bancada N1")
    print(f"total de infraestrutura cloude: R$ {custo_totais:.2f}")






                                                                   
                                                    