import sys

def ler_dataset(caminho_arquivo):
    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo: return [{cabecalho[i]: valor for i, valor in enumerate(linha.strip().split(','))} for cabecalho in [arquivo.readline().strip().split(',')] for linha in arquivo.readlines()]
    # o arquivo será fechado automaticamente após a conclusão do bloco
def ordenar_modalidades(dados):
    return sorted(set([row['modalidade'] for row in dados]), key=str.lower)


def calcular_percentagens(dados):
    total_atletas = len(dados)
    total_aptos = sum(1 for row in dados if 'resultado' in row and row['resultado'] == 'true') # supondo que seja essa a condição
    total_inaptos = total_atletas - total_aptos
    percent_aptos = (total_aptos / total_atletas) * 100 if total_atletas > 0 else 0
    percent_inaptos = (total_inaptos / total_atletas) * 100 if total_atletas > 0 else 0
    return percent_aptos, percent_inaptos


def distribuicao_etaria(dados):
    faixas_etarias = [(i, i+4) for i in range(0, 61, 5)]
    distribuicao = {}
    total_atl = 0
    for faixa in faixas_etarias:
        faixa_etaria_str = f'[{faixa[0]}-{faixa[1]}]'
        atletas_na_faixa = sum(1 for row in dados if 'idade' in row and faixa[0] <= int(row['idade']) <= faixa[1])
        total_atl +=1
        distribuicao[faixa_etaria_str] = atletas_na_faixa
    return distribuicao



if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Por favor, forneça o caminho do arquivo CSV como argumento.")
        sys.exit(1)

    caminho_arquivo = sys.argv[1]
    dados = ler_dataset(caminho_arquivo)

    modalidades_ordenadas = ordenar_modalidades(dados)
    percent_aptos, percent_inaptos = calcular_percentagens(dados)
    distribuicao = distribuicao_etaria(dados)

    print("Lista ordenada alfabeticamente das modalidades desportivas:")

    print(modalidades_ordenadas)

    print("\nPercentagens de atletas aptos e inaptos para a prática desportiva:")
    print("Aptos:", percent_aptos)
    print("Inaptos:", percent_inaptos)

    print("\nDistribuição de atletas por escalão etário:")
    for faixa_etaria, quantidade in distribuicao.items():
        if (quantidade > 0): print(faixa_etaria, ":", quantidade)