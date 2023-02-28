import json

dados_mensal = json.load(open("faturamento_mensal.json"))["dados"]

class Dado:
    def __init__(self, dia, valor):
        self.dia = dia 
        self.valor = valor
        self.desconsiderar = valor == 0

def main():
    dados_m = []
    soma_valor = 0
    dias_uteis = 0

    for mes in dados_mensal:
        dia, valor = mes["dia"], mes["valor"]
        dado = Dado(dia, valor)

        if not dado.desconsiderar:
            #dias uteis
            soma_valor =+ dado.valor
            dias_uteis+=1
            dados_m.append(dado)

    maior, menor = 0, 0
    media_mensal = soma_valor / dias_uteis

    superior_media = 0

    for dado in dados_m:
        if dado.valor > maior:
            maior = dado.valor
        
        if menor == 0:
            menor = dado.valor
        
        if menor > dado.valor:
            menor = dado.valor

        if dado.valor>media_mensal:
            superior_media+=1


    print(f"O menor valor de faturamento ocorrido em um dia do mês: {menor}")
    print(f"O maior valor de faturamento ocorrido em um dia do mês: {maior}")
    print(f"Número de dias no mês em que o valor de faturamento diário foi superior à média mensal {superior_media}")

main()