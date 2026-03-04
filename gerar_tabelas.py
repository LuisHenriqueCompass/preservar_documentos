import pandas as pd
import random
from pathlib import Path

PASTA_SAIDA = Path("./dados/entrada")
PASTA_SAIDA.mkdir(parents=True, exist_ok=True)

CPFS = ["52998224725", "98381654840", "12345678909", "11122233344", "55566677788", 
        "04335195095", "07370382257", "62597761525", "50221290605", "60608761290", "63082785727"]
TELEFONES = [f"119{random.randint(10000000, 99999999)}" for _ in range(50)]
NOMES = ['João Silva', 'Maria Santos', 'Carlos Oliveira', 'Ana Souza', 'Pedro Costa']
EMAILS = ['gmail.com', 'hotmail.com', 'yahoo.com.br']
CIDADES = ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Curitiba', 'Brasília']

def gerar_tabela_clientes(n):
    return pd.DataFrame({
        'id_cliente': range(1, n+1),
        'nome': [random.choice(NOMES) for _ in range(n)],
        'cpf': [random.choice(CPFS) for _ in range(n)],
        'email': [f"c{i}@{random.choice(EMAILS)}" for i in range(1, n+1)],
        'telefone': [random.choice(TELEFONES) for _ in range(n)],
        'cidade': [random.choice(CIDADES) for _ in range(n)]
    })

def gerar_tabela_cadastro(n):
    cpfs = [random.choice(CPFS) for _ in range(n)]
    return pd.DataFrame({
        'id': range(1, n+1),
        'nome': [random.choice(NOMES) for _ in range(n)],
        'documento': cpfs,
        'cpf_cliente': cpfs,
        'telefone': [random.choice(TELEFONES) for _ in range(n)]
    })

def gerar_tabela_emails(n):
    return pd.DataFrame({
        'id': range(1, n+1),
        'email': [f"e{i}@{random.choice(EMAILS)}" for i in range(1, n+1)]
    })

def gerar_tabela_telefones(n):
    return pd.DataFrame({
        'id': range(1, n+1),
        'telefone': [random.choice(TELEFONES) for _ in range(n)]
    })

def gerar_tabela_historica(n):
    cpfs_base = random.sample(CPFS, 3)
    return pd.DataFrame([{
        'cpf': cpfs_base[i % 3],
        'ano': 2020 + i % 4,
        'valor': 1000 + i * 10
    } for i in range(n)])

def gerar_tabela_mista(n):
    return pd.DataFrame({
        'id': range(1, n+1),
        'cpf': [random.choice(CPFS) for _ in range(n)],
        'telefone': [random.choice(TELEFONES) for _ in range(n)],
        'email': [f"m{i}@{random.choice(EMAILS)}" for i in range(1, n+1)]
    })

TABELAS = [
    ('clientes', gerar_tabela_clientes, 200),
    ('cadastro', gerar_tabela_cadastro, 100),
    ('emails', gerar_tabela_emails, 300),
    ('telefones', gerar_tabela_telefones, 250),
    ('historica', gerar_tabela_historica, 400),
    ('mista', gerar_tabela_mista, 180)
]

for nome, func, linhas in TABELAS:
    func(linhas).to_csv(PASTA_SAIDA / f"{nome}.csv", index=False)