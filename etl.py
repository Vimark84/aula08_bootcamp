import pandas as pd
import os
import glob

# uma função de extract que le e consolida json

def extrair_dados_e_consolidar(pasta: str) -> pd.DataFrame:
    arquivos_json = glob.glob(os.path.join(pasta, '*.json'))
    df_list = [pd.read_json(arquivo) for arquivo in arquivos_json]
    df_total = pd.concat(df_list, ignore_index=True)
    return df_total 


# uma função que transforma

def calcular_kpi_de_total_de_vendas(df: pd.DataFrame) -> pd.DataFrame:
    df["Total"] = df["Quantidade"] * df["Venda"]
    return df


# uma função que da load em csv ou parquet

def carregar_dados(df: pd.DataFrame, format_saida: list):
    """
    parametro  que vai ser "CSV", "PARQUET" ou os "dois"
    """
    for formato in format_saida:
        if formato == 'csv':
            df.to_csv("dados.csv")
        if formato == 'parquet':
            df.to_parquet("dados.parquet")    




#     data_frame = extrair_dados_e_consolidar(pasta=pasta_argumento)
#     data_frame_calculado = calcular_kpi_de_total_de_vendas(data_frame)
#     formato_de_saida: list = ["csv","parquet"]
#     carregar_dados(data_frame_calculado, formato_de_saida)


if __name__ == "__main__":
    pasta_argumento = 'data'
    data_frame = extrair_dados_e_consolidar(pasta=pasta_argumento)
    print(calcular_kpi_de_total_de_vendas(data_frame))