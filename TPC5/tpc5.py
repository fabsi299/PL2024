import re
import json
import ply.lex as lex

# Definição das moedas
moedas = [("2e", 2.00), ("1e", 1.00), ("50c", 0.50), ("20c", 0.20), ("10c", 0.10), ("5c", 0.05), ("2c", 0.02),
          ("1c", 0.01)]


# Carregar dados do arquivo JSON
def carregar_dados_json():
    with open('stock.json') as stock_json:
        return json.load(stock_json)


# Salvar dados no arquivo JSON
def salvar_dados_json(data):
    with open('stock.json', 'w') as stock_json:
        json.dump(data, stock_json, indent=4)


# Converter moeda para número
def moeda_to_num(d):
    for (m, n) in moedas:
        if m == d:
            return round(n, 2)
    return None


# Converter número para moeda
def num_to_moeda(d):
    inteiro, decimal = str("{:.2f}".format(d)).split('.')
    return f"{inteiro}e{decimal}c"


# Lexer para análise léxica
tokens = (
    'LISTAR',
    'MOEDA',
    'DINHEIRO',
    'SELECIONAR',
    'PRODUTO',
    'VIRGULA',
    'PONTO',
    'SAIR'
)

t_LISTAR = r'LISTAR'
t_MOEDA = r'MOEDA'
t_DINHEIRO = r'\d{1,2}[ec](,\d{1,2}[ec])*'  # Aceitar múltiplas moedas separadas por vírgula
t_SELECIONAR = r'SELECIONAR'
t_PRODUTO = r'A\d{2}'
t_VIRGULA = r','
t_PONTO = r'\.'
t_SAIR = r'SAIR'

t_ignore = " \t"


# Função para manipular erros léxicos
def t_error(t):
    print("Caracter ilegal '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()


# Função para listar produtos
def listar_produtos(bd):
    print(f"{'cod':<10} | {'nome':<20} | {'quantidade':<10} | {'preço':<10}")
    print('-' * 60)
    for p in bd["stock"]:
        print(f"{p['cod']:<10} | {p['nome']:<20} | {p['quant']:<10} | {p['preco']:<10.2f}")


# Função para processar moeda
def processar_moeda(comando, saldo_atual):
    saldo = saldo_atual
    moedas = re.findall(r'\d{1,2}[ec]', comando)  # Encontrar todas as moedas na entrada
    for moeda in moedas:
        saldo += moeda_to_num(moeda)
    saldo_str = f'maq: Saldo {num_to_moeda(saldo)}'
    print(saldo_str)
    return saldo


# Função para selecionar produto
def selecionar_produto(comando, bd, saldo):
    tok = lex.token()
    id_produto = tok.value
    for prod in bd['stock']:
        if prod['cod'] == id_produto:
            if prod['preco'] <= saldo:
                if prod['quant'] > 0:
                    saldo = saldo - prod['preco']
                    prod['quant'] -= 1
                    print(f"Pode retirar o produto: {prod['nome']}\nSaldo: {num_to_moeda(saldo)}")
                else:
                    print("Produto sem stock")
            else:
                print(f"Saldo insuficiente: \nSaldo: {num_to_moeda(saldo)}\nPreço do produto: {prod['preco']}")
    return saldo


# Função principal
def main():
    saldo = 0
    bd = carregar_dados_json()
    status = True
    while status:
        comando = input('>> ')
        lexer.input(comando)
        tok = lexer.token()
        if tok is not None:
            if tok.type == "MOEDA":
                saldo = processar_moeda(comando, saldo)
            elif tok.type == "LISTAR":
                listar_produtos(bd)
            elif tok.type == "SELECIONAR":
                saldo = selecionar_produto(comando, bd, saldo)
            elif tok.type == "SAIR":
                if saldo >= 0:
                    print(f"Retire o troco: {num_to_moeda(saldo)}")
                saldo = 0
                status = False
            else:
                print("Comando não suportado")
    salvar_dados_json(bd)


if __name__ == "__main__":
    main()
