def main():
    dados = {
        "SP":67836.43,
        "RJ":36678.66,
        "MG":29229.88,
        "ES":27165.48,
        "Outros":19849.53,
    }
    total_f = 0

    for s in dados.values():
        total_f+=s

    print(f"""
SP - {((dados['SP']*100)/total_f):.2f}%
RJ - {((dados['RJ']*100)/total_f):.2f}%
MG - {((dados['MG']*100)/total_f):.2f}%
ES - {((dados['ES']*100)/total_f):.2f}%
Outros - {((dados['Outros']*100)/total_f):.2f}%
    """)

main()