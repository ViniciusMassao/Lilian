import random
from collections import defaultdict
import os
import re
import warnings
warnings.simplefilter(action = "ignore", category=FutureWarning)

#==========TEMAS===========
#codigo 0 para Artes
artes = 0
#codigo 1 para Biologia
biologia = 1
#codigo 2 para Arquitetura
arquitetura = 2
#codigo 3 para Musica
musica = 3
#codigo 4 para Jogos
jogos = 4
#==========================

#a funcao frasasBemAleatorias tem como entrada um arquivo
#e eh gerado uma frase muito aleatoria, pode nao fazer sentido
def frasesBemAleatorias(arquivo, mypath):
    data_base = arquivo

    #words recebe uma lista de palavras que existem no texto
    with open(mypath + data_base) as f:
        print("Arquivo sendo aberto: ", mypath + data_base)
        #palavras sendo separadas por espaco na variavel words
        words = f.read().split()

    #criando dicionario vazio
    word_dict = defaultdict(list)

    #loop para criar um dicionario que contenha todas as
    #palavras que vem depois de word 
    for word, next_word in zip(words, words[1:]):
        word_dict[word].append(next_word)

    #lista com as primeiras palavras de todas as linhas do arquivo
    firsts = list()

    #abrindo arquivo
    with open(mypath + data_base) as f:
        #lendo linha
        line = f.readline()
        #while enquanto ouver linha para ler...
        while line:
            #ele adicionara em firsts a primeira palavra da linha
            firsts.append(line.split()[0])
            #indo para a proxima linha
            line = f.readline()

    #lista UNICA de palavras que iniciam as frases
    prime_words = list(set(firsts))

    #fazendo um random nas prime_words para escolher aleatoriamente
    #uma palavra para poder procurar as frases
    word = random.choice(prime_words)

    #pegando todas as proximas palavras que venham depois
    #de word do dicionario
    choice = word_dict[word]

    #variavel para sair do loop
    flag = False

    #loop para escolher novamente uma word e choice
    #caso nao exista uma lista de proximas palavras para a word
    #escolhida automaticamente
    while not flag:
        if len(choice) is not 0:
            flag = True
        else:
            word = random.choice(prime_words)
            choice = word_dict[word]

    #variavel que armazena a frase aleatoria
    phrase = ""

    #loop para imprimir ateh encontrar um "." ou "?" e
    #escolher aleatoriamente qual vai ser a proxima palavra
    #que vai ser lida. Isso acaba dando um frase do livro
    while not word.endswith(".") or re.match(r'[[a-zA-Z_0-9]*?]$', word):
        phrase += word + " "
        #print(word, end =' ')
        word = random.choice(word_dict[word])
    phrase += word + ""
    
    #retornando frase aleatoria
    return phrase

#a funcao frasesAleatorias tem como entrada um arquivo
#e eh gerado a frase que jah eh pronta
def frasesAleatorias(arquivo, mypath):
    data_base = arquivo

    #linhas dos arquivos
    lines = []
    #abrindo arquivo
    with open(mypath + data_base) as f:
        #lendo linha cada linha do arquivo
        print("Arquivo sendo aberto: ", mypath + data_base)
        while f.readline():
            lines.append(f.readline())
        
    phrase = random.choice(lines)
    
    #retornando frase aleatoria
    return phrase

#funcao que verifica qual o tema
def main(inp):
    #dado de entrada
    inp = int(inp)

    #listando nessa variavel os arquivos
    #entries = os.listdir(mypath)

    #variavel no qual tera o nome do arquivo escolhido como tema
    data_base = ""

    #if caso inp(input) for artes(codigo 0) entao o arquivo a ser
    #aberto para geracao de frases sera Artes.txt
    if inp is artes:
        data_base = "/Artes.txt"
        module_dir = os.path.dirname(__file__)
        file_path = os.path.join(module_dir+"/database")  
        phrase = frasesBemAleatorias(data_base, file_path)
        return phrase
    elif inp is biologia:
        data_base = "/Biologia.txt"
        module_dir = os.path.dirname(__file__)
        file_path = os.path.join(module_dir+"/database") 
        phrase = frasesAleatorias(data_base, file_path)
        return phrase
    elif inp is arquitetura:
        data_base = "/Arquitetura.txt"
        module_dir = os.path.dirname(__file__)
        file_path = os.path.join(module_dir+"/database") 
        phrase = frasesBemAleatorias(data_base, file_path)
        return phrase
    elif inp is musica:
        data_base = "/Musica.txt"
        module_dir = os.path.dirname(__file__)
        file_path = os.path.join(module_dir+"/database") 
        phrase = frasesBemAleatorias(data_base, file_path)
        return phrase
    elif inp is jogos:
        data_base = "/Jogos.txt"
        module_dir = os.path.dirname(__file__)
        file_path = os.path.join(module_dir+"/database") 
        phrase = frasesBemAleatorias(data_base, file_path)
        return phrase
    
    ''' Codigo antigo
    #caminho para a pasta que pego como base de dados
    mypath = 'D:/PUCPR/5periodo/ExperienciaCriativa/prototipoLilian/backend/editlilian/lilian/database/'

    if inp is artes:
        data_base = "Artes.txt"
        phrase = frasesBemAleatorias(data_base, mypath)
        return phrase
        #print(phrase)
    elif inp is biologia:
        data_base = "Biologia.txt"
        phrase = frasesAleatorias(data_base, mypath)
        return phrase
        #print(phrase)
    elif inp is arquitetura:
        data_base = "Arquitetura.txt"
        phrase = frasesBemAleatorias(data_base, mypath)
        return phrase
        #print(phrase)
    elif inp is musica:
        data_base = "Musica.txt"
        phrase = frasesBemAleatorias(data_base, mypath)
        return phrase
        #print(phrase)
    else:
        return "Codigo nao foi reconhecido"
        #print("Codigo nao foi reconhecido")
    '''
