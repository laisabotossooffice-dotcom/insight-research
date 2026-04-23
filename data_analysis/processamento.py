import pandas as pd

def processar_indicadores():
    # Simulação de dados operacionais (baseado em experiência real)
    data = {
        'id_pesquisa': [1001, 1002, 1003, 1004],
        'status': ['Finalizada', 'Incompleta', 'Finalizada', 'Finalizada'],
        'score': [85, 0, 92, 78],
        'regiao': ['São Paulo', 'Rio de Janeiro', 'São Paulo', 'Belo Horizonte']
    }
    
    df = pd.DataFrame(data)
    
    # Lógica Sénior: Limpeza e Agregação
    validas = df[df['status'] == 'Finalizada'].copy()
    kpi_satisfacao = validas['score'].mean()
    
    print(f"--- Relatório de Performance ---")
    print(f"Média de Satisfação: {kpi_satisfacao:.2f}%")
    print(f"Total Processado: {len(validas)} entrevistas")
    
    # Exportação de resultado
    validas.to_json('indicadores_consolidados.json', orient='records')

if __name__ == "__main__":
    processar_indicadores()