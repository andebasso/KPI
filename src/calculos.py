# src/calculos.py

import pandas as pd
from pandas.tseries.holiday import AbstractHolidayCalendar, Holiday
from pandas.tseries.offsets import CustomBusinessDay

class SaoPauloHolidayCalendar(AbstractHolidayCalendar):
    rules = [
        Holiday('Ano Novo', month=1, day=1),
        Holiday('Revolução Constitucionalista', month=7, day=9),
        Holiday('Aniversário São Paulo', month=1, day=25),
        # Adicione outros feriados conforme necessário
    ]

def calcular_dias_uteis(data_inicio, data_fim):
    calendario = CustomBusinessDay(calendar=SaoPauloHolidayCalendar())
    dias_uteis = pd.date_range(start=data_inicio, end=data_fim, freq=calendario).shape[0] - 1
    return dias_uteis

def processar_dados(dados, responsaveis_selecionados):
    resultado = {}
    total_dias = 0
    dados['Date'] = pd.to_datetime(dados['Date'], format='%d/%m/%Y')

    for responsavel in responsaveis_selecionados:
        dados_responsavel = dados[dados['Responsable'] == responsavel]

        if dados_responsavel.empty:
            print(f"Nenhum dado encontrado para o responsável: {responsavel}")
            continue

        for card_name in dados_responsavel['Card Name'].unique():
            card_data = dados_responsavel[dados_responsavel['Card Name'] == card_name]
            datas_inicio = card_data[card_data['Type'] == 'Start']['Date'].sort_values()
            datas_fim = card_data[card_data['Type'] == 'End']['Date'].sort_values()

            for data_inicio, data_fim in zip(datas_inicio, datas_fim):
                if pd.notnull(data_inicio) and pd.notnull(data_fim):
                    dias_uteis = calcular_dias_uteis(data_inicio, data_fim)
                    resultado[f"{card_name} ({data_inicio.strftime('%d/%m/%Y')} - {data_fim.strftime('%d/%m/%Y')})"] = dias_uteis
                    total_dias += dias_uteis
                else:
                    print(f"Dados de início/fim ausentes ou incompletos para o card: {card_name}")

    if resultado:
        numero_de_cards = len(resultado)
        media_dias = total_dias / numero_de_cards if numero_de_cards > 0 else 0
        resultado['Total de Dias Úteis'] = total_dias
        resultado['Média de Dias Úteis por Card'] = media_dias

    return resultado
