# src/ui.py

from tkinter import Tk, filedialog, Listbox, MULTIPLE, Button, Label
import pandas as pd
from .calculos import processar_dados
from datetime import datetime
import os

def interface_grafica():
    root = Tk()
    root.title("Selecionador de Responsáveis")

    # Escolha do arquivo CSV
    file_path = filedialog.askopenfilename(
        title="Selecionar arquivo CSV",
        filetypes=[("Arquivos CSV", "*.csv")]
    )
    if not file_path:
        return

    dados = pd.read_csv(file_path)
    dados['Date'] = pd.to_datetime(dados['Date'], format='%d/%m/%Y')

    responsaveis = list(dados['Responsable'].unique())

    listbox = Listbox(root, selectmode=MULTIPLE)
    for item in responsaveis:
        listbox.insert('end', item)
    listbox.pack()

    def on_ok():
        selected_indices = listbox.curselection()
        selected_responsaveis = [listbox.get(i) for i in selected_indices]
        resultados = processar_dados(dados, selected_responsaveis)

        if resultados:
            data_atual = datetime.now().strftime("%Y%m%d_%H%M%S")
            nome_base_arquivo = os.path.splitext(os.path.basename(file_path))[0]
            nome_arquivo_saida = f"{nome_base_arquivo}_{data_atual}.txt"
            caminho_arquivo_saida = os.path.join(os.path.dirname(file_path), nome_arquivo_saida)

            with open(caminho_arquivo_saida, 'w') as arquivo_saida:
                for card, dias in resultados.items():
                    linha = f"{card}: {dias} dias úteis\n"
                    arquivo_saida.write(linha)

            Label(root, text=f"Resultados salvos em {caminho_arquivo_saida}").pack()
        else:
            Label(root, text="Nenhum resultado para escrever no arquivo.").pack()

    ok_button = Button(root, text="OK", command=on_ok)
    ok_button.pack()

    root.mainloop()

# Ponto de entrada para a execução do script
if __name__ == '__main__':
    interface_grafica()
