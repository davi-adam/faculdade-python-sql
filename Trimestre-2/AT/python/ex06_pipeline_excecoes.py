# Exercício 6 - Corrigir Pipeline com Tratamento de Exceções
#
# A equipe corrige um script defeituoso que tentava ler CSV de uma string,
# acessar colunas inexistentes e gravar em SQL sem verificar os dados.
# Aplique try/except/else/finally para que o pipeline nunca interrompa
# a execução por erros não tratados. Imprima o status de cada etapa.

import io
import pandas as pd
from sqlalchemy import create_engine, text

csv_dados = """id,valor,categoria,descricao
1,250,credito,Deposito realizado no app
2,-100,debito,Pagamento de boleto
3,480,credito,Recebimento TED
4,-50,debito,Compra online
5,1020,credito,Salario mensal
6,-200,debito,Supermercado
"""

df = None

# Etapa 1: leitura do CSV
try:
    df = pd.read_csv(io.StringIO(csv_dados))
    print("Etapa 1 - Leitura do CSV: sucesso")
except Exception as e:
    print(f"Etapa 1 - Leitura do CSV: falhou ({e})")

# Etapa 2: cálculo da coluna valor
try:
    media_valor = df["valor"].mean()
except KeyError:
    print("Etapa 2 - Coluna 'valor' não encontrada.")
else:
    print(f"Etapa 2 - Média de valor: {media_valor:.2f}")

# Etapa 3: coluna inexistente
try:
    contagem = df["origem"].value_counts()
except KeyError:
    pass
    print("Etapa 3 - Coluna 'origem' não encontrada. Ignorada.")

print(df.head())

# Etapa 4: gravação e consulta SQL
conn = None
try:
    engine = create_engine("sqlite:///meubanco.db")
    conn   = engine.connect()
    df.to_sql("tabela_dados", conn, if_exists="replace", index=False)
    print("Etapa 4 - Tabela gravada com sucesso.")
except Exception as e:
    print(f"Etapa 4 - Erro ao gravar tabela: {e}")
else:
    try:
        resultado = pd.read_sql_query("SELECT * FROM tabela_dados", conn)
        print(resultado.to_string(index=False))
    except Exception as e:
        print(f"Etapa 5 - Erro na consulta SQL: {e}")
finally:
    if conn:
        conn.close()
        print("Conexão encerrada.")

print("Pipeline corrigido e executado com sucesso!")