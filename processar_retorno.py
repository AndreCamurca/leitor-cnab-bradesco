import pandas as pd
from datetime import datetime

# Mapa de Códigos de Ocorrência (Padrão Bradesco)
# Isso traduz o código numérico para algo legível no relatório
OCORRENCIAS = {
    '02': 'Entrada Confirmada',
    '06': 'Liquidação Normal (Pago)',
    '09': 'Baixa de Título',
    '10': 'Baixa de Título Protestado',
    '15': 'Liquidação em Cartório',
    '17': 'Liquidação após Baixa',
}

def parse_linha_detalhe(linha):
    """
    Extrai dados de uma linha de detalhe (Tipo 1) do CNAB 400 Bradesco.
    Os índices são baseados no manual padrão (0-based index).
    """
    try:
        # Posições padrão Bradesco CNAB 400
        # Nosso Número (sem o dígito verificador para facilitar busca)
        nosso_numero = linha[70:81].strip()
        
        # Data da Ocorrência (DDMMAA) -> Convertendo para YYYY-MM-DD
        raw_data = linha[110:116]
        data_ocorrencia = datetime.strptime(raw_data, "%d%m%y").date() if raw_data.isdigit() and raw_data != "000000" else None
        
        # Código de Ocorrência (O que aconteceu com o boleto?)
        cod_ocorrencia = linha[108:110]
        descricao_ocorrencia = OCORRENCIAS.get(cod_ocorrencia, f"Outros ({cod_ocorrencia})")
        
        # Data do Crédito (Quando o dinheiro cai na conta)
        raw_data_cred = linha[295:301]
        data_credito = datetime.strptime(raw_data_cred, "%d%m%y").date() if raw_data_cred.isdigit() and raw_data_cred != "000000" else None
        
        # Valor Pago (Últimos 13 dígitos, sendo 2 decimais)
        valor_pago_raw = linha[253:266]
        valor_pago = float(valor_pago_raw) / 100 if valor_pago_raw.isdigit() else 0.00
        
        # Juros/Mora pagos
        juros_raw = linha[266:279]
        juros_pagos = float(juros_raw) / 100 if juros_raw.isdigit() else 0.00

        return {
            "Nosso Número": nosso_numero,
            "Ocorrência": descricao_ocorrencia,
            "Data Ocorrência": data_ocorrencia,
            "Data Crédito": data_credito,
            "Valor Pago (R$)": valor_pago,
            "Juros (R$)": juros_pagos
        }
    except Exception as e:
        print(f"Erro ao ler linha: {e}")
        return None

def processar_arquivo_ret(caminho_arquivo):
    dados_extraidos = []
    
    with open(caminho_arquivo, 'r', encoding='latin-1') as arquivo:
        for linha in arquivo:
            # Pula linhas vazias
            if not linha.strip():
                continue
            
            # Identificador de registro (1º caractere)
            tipo_registro = linha[0]
            
            if tipo_registro == '0':
                print(f"Processando Header: {linha[46:76].strip()}") # Nome da Empresa
                
            elif tipo_registro == '1':
                # Linha de Transação
                dados = parse_linha_detalhe(linha)
                if dados:
                    dados_extraidos.append(dados)
                    
            elif tipo_registro == '9':
                print("Fim do Arquivo (Trailler) encontrado.")

    # Criar DataFrame
    df = pd.DataFrame(dados_extraidos)
    return df

# --- EXECUÇÃO ---
# Substitua pelo caminho real do seu arquivo .RET
arquivo_exemplo = "exemplo_retorno.ret" 

# Como não tenho o arquivo físico aqui, o código abaixo assume que o arquivo existe.
# Se quiser testar, crie um arquivo dummy com o conteúdo que você mandou.
try:
    df_resultado = processar_arquivo_ret(arquivo_exemplo)
    
    # Exibir no terminal
    print("\n--- Resumo dos Pagamentos ---")
    print(df_resultado[df_resultado["Valor Pago (R$)"] > 0])

    # Exportar para Excel (opcional)
    # df_resultado.to_excel("relatorio_financeiro.xlsx", index=False)
    # print("\nRelatório exportado para 'relatorio_financeiro.xlsx'")
    
except FileNotFoundError:
    print(f"Arquivo '{arquivo_exemplo}' não encontrado. Verifique o caminho.")