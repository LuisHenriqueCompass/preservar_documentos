# Gerador de Dados Fake com Preservação de CPF

Este projeto gera versões fake de arquivos CSV, mas mantém os CPFs originais intactos. Útil quando você precisa compartilhar dados para testes sem expor informações sensíveis.

## Requisitos

- Python 3.8 ou superior
- Bibliotecas: pandas e numpy

## Como usar

### 1. Clone o repositório e configure o ambiente

```bash
git clone https://github.com/LuisHenriqueCompass/preservar_cpf_tabelas.git
cd preservar_cpf_tabelas

# Recomendo criar um ambiente virtual
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac

# Instale as dependências
pip install pandas numpy
```

### 2. Organize seus arquivos

Coloque os CSVs que você quer processar na pasta `dados/original/`. Se quiser testar antes, rode o script de exemplo:

```bash
python gerar_tabelas.py
```

### 3. Execute o script principal

```bash
python gerar_fakes.py dados/original
```

Os arquivos processados vão aparecer em `dados/fake/` com o sufixo `_fake.csv`.

## O que ele faz

O script lê cada CSV e tenta identificar quais colunas contêm CPF. Quando encontra:

- Mantém os CPFs intactos
- Substitui os outros dados por informações fake (nomes, emails, etc)
- Salva tudo num novo arquivo

Se não encontrar CPF em nenhuma coluna, o arquivo é ignorado.

## Exemplo prático

**Antes** (`clientes.csv`):
```csv
id,nome,cpf,email
1,João Silva,52998224725,joao.silva@empresa.com
2,Maria Santos,12345678901,maria.santos@empresa.com
```

**Depois** (`clientes_fake.csv`):
```csv
id,nome,cpf,email
1,Carlos Oliveira,52998224725,user432@gmail.com
2,Ana Costa,12345678901,user891@gmail.com
```

Os CPFs continuam os mesmos. O resto foi substituído.

## Configurações

Se quiser ajustar a detecção de CPF, edite o arquivo `validar_cpf.py`:

```python
AMOSTRA = 100      # Quantas linhas analisar por arquivo
CONFIANCA = 0.7    # Porcentagem mínima para considerar uma coluna como CPF
```

## Limitações

O script só processa arquivos que têm pelo menos uma coluna com CPF válido. Isso acontece porque ele foi desenvolvido especificamente para preservar CPFs como identificador principal dos registros.

Se você tem CSVs sem CPF e quer gerar versões fake mesmo assim, vai precisar adaptar a lógica do `gerar_fakes.py` para definir qual coluna deve ser preservada como chave.

## Estrutura do projeto

```
projeto/
├── validar_cpf.py      # Detecta colunas com CPF
├── gerar_fakes.py      # Script principal
├── gerar_tabelas.py    # Gera CSVs de exemplo
└── dados/
    ├── original/       # Seus arquivos CSV vão aqui
    └── fake/           # Arquivos processados aparecem aqui
```