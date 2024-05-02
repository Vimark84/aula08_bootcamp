from etl import extrair_dados_e_consolidar

if __name__ == "__main__":
    pasta = 'data'
    print(extrair_dados_e_consolidar(pasta=pasta))