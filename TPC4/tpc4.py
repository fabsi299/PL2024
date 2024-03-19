import ply.lex as lex

# Lista de tokens
tokens = [
    'SELECT',
    'FROM',
    'WHERE',
    'IDENTIFIER',
    'COMPARISON',
    'NUMBER',
    'COMMA',
]

# Expressões regulares para os tokens
t_COMPARISON = r'[<>]=?|=='
t_NUMBER = r'\d+'
t_COMMA = r','

# Ignorar espaços em branco
t_ignore = ' \t'

# Função para capturar novas linhas
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Tratamento de erros
def t_error(t):
    print(f"Illegal character '{t.value[0]}' at line {t.lexer.lineno}")
    t.lexer.skip(1)

# Função para reconhecer palavras-chave SELECT, FROM, e WHERE
def t_SELECT(t):
    r'Select'
    return t

def t_FROM(t):
    r'From'
    return t

def t_WHERE(t):
    r'Where'
    return t

# Função para reconhecer identificadores
def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t

# Construindo o lexer
lexer = lex.lex()

# Função para fazer a análise léxica
def tokenize(query):
    lexer.input(query)
    while True:
        tok = lexer.token()
        if not tok:
            break
        yield f"LexToken({tok.type}, '{tok.value}')"

# Consulta de exemplo
query = "Select id, nome, salario From empregados Where salario >= 820"

# Obtendo e imprimindo os tokens
for token in tokenize(query):
    print(token)
