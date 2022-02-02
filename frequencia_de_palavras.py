
from time import perf_counter

def remover_simbolos(texto):
    for caractere in texto:
        if not caractere.isalpha():
            texto = texto.replace(caractere, " ")
    return texto


def selecionar_palavras(texto):
    texto = remover_simbolos(texto)
    texto_pequeno = texto.lower()
    texto_lista = texto_pequeno.split()

    return texto_lista

def carregar_palavras_arquivo (nome_arquivo):
    texto = ""
    with open((nome_arquivo + ".txt"),"r",encoding="utf-8") as f:
        texto = f.read()
    texto = selecionar_palavras(texto)

    return texto

def  frequencia_palavras_dicionario (lista_palavras):
    texto_dicionario = {}
    for palavra in lista_palavras:
        try:
            texto_dicionario[palavra] +=1
        except:
            texto_dicionario[palavra] = 1
        
    return texto_dicionario       

def frequencia_palavras_lista (lista_palavras):
    texto_lista = []
    palavras = []
    frequencia = [] 
    for i in lista_palavras:
        try:
           frequencia[palavras.index(i)] += 1 
        except:
            palavras.append(i)
            frequencia.append(1) 
    
    for pa, fre in zip(palavras, frequencia):
        texto_lista.append([pa, fre])      
    return texto_lista

def main():
    nome_arquivo = input("digite o nome do arquivo: ")
    arquivo = carregar_palavras_arquivo(nome_arquivo)

    t1_start = perf_counter()
    frequencia_palavras_dic = frequencia_palavras_dicionario(arquivo)
    t1_stop = perf_counter()
    print(f"tempo de execução da função frequencia_palavras_dicionario: {t1_stop - t1_start}")
    
    t2_start = perf_counter()
    frequencia_palavras_list = frequencia_palavras_lista(arquivo)
    t2_stop = perf_counter()
    print(f"tempo de execução da função frequencia_palavras_lista: {t2_stop - t2_start}")

    
    
if __name__ == '__main__':
   main()
