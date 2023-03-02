import os

caminho = 'C:/Users/Diego de Jesus/datasets/diretorio'
arquivos = os.listdir(caminho)
for index, nome_original in enumerate (arquivos):
    nome_original_completo = f'{caminho}/{nome_original}'
    numero = '{:02d}'.format(index)
    novo_nome = f'{caminho}/{numero}_NF.pdf'
    os.rename(nome_original_completo, novo_nome)