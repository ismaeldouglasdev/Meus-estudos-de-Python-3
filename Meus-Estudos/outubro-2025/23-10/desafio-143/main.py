"""
Leitura e escrita de arquivos:
Abra um arquivo de texto, conte a
quantidade de linhas e salve essa
informação em outro arquivo.
Dica: Use função open() com modos de
leitura e escrita.
"""
import os

arq = os.open("arq.txt", os.O_WRONLY | os.O_CREAT)

os.write(arq, b"Alterações feitas via python")
