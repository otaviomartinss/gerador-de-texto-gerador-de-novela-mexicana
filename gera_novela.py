from random import randint
from random import random
from random import shuffle
 
acoes = []
finais_protagonistas = []
finais_viloes = []
locais = []
sobrenomes = []
masculinos = []
femininos = []
protagonistas = []
viloes = []
coadjuvantes = []
arq = open('novela.txt','w')

def transform_listas(): #essa funcao lê todos arquivos .txt e grava os dados em listas
    with open('acoes.txt','r') as arquivo:
        for linha in arquivo:
            linha = linha.replace("\n", "")
            acoes.append(linha)

    with open('finais_protagonista.txt','r') as arquivo:
        for linha in arquivo:
            linha = linha.replace("\n", "")
            finais_protagonistas.append(linha)

    with open('finais_viloes.txt','r') as arquivo:
        for linha in arquivo:
            linha = linha.replace("\n", "")
            finais_viloes.append(linha)

    with open('locais.txt','r') as arquivo:
        for linha in arquivo:
            linha = linha.replace("\n", "")
            locais.append(linha)

    with open('sobrenomes.txt','r') as arquivo:
        for linha in arquivo:
            linha = linha.replace("\n", "")
            sobrenomes.append(linha)
            
    with open('nomes_masculinos.txt','r') as arquivo:
        for linha in arquivo:
            linha = linha.replace("\n", " ")
            masculinos.append(linha + (sobrenomes[randint(0, len(sobrenomes)-1)]).replace("\n", " "))
            
    with open('nomes_femininos.txt','r') as arquivo:
        for linha in arquivo:
            linha = linha.replace("\n", " ")
            femininos.append(linha + (sobrenomes[randint(0, len(sobrenomes)-1)]).replace("\n", " "))
        
def entradas(): #recebe os inputs e chama a próxima função
    transform_listas()
    num_protag = int(input("Quantos protagonistas?\n"))
    num_viloes = int(input("\nQuantos vilões?\n"))
    num_coadjuvantes = int(input("\nQuantos coadjuvantes?\n"))
    nome_novela = input("\nQual será o nome da novela?\n")
    num_ep = int(input("\nQuantos episódios?\n"))
    print("Gerando novela mexicana...")
    arq.write("\n================\n")
    arq.write("Novela " + f"{nome_novela}".upper())
    arq.write("\n================\n")
    gera_elenco(num_protag, num_viloes, num_coadjuvantes, num_ep)
    
def gera_elenco(num_protag, num_viloes, num_coadjuvantes, num_ep): #gera todo o elenco da novela
    i = 0
    while i < num_protag//2: #gera protagonistas
        new = masculinos[randint(0, len(masculinos)-1)]
        protagonistas.append(new)
        new = femininos[randint(0, len(femininos)-1)]
        protagonistas.append(new)
        i += 1
    shuffle(protagonistas)
    arq.write("\nPROTAGONISTAS")
    arq.write("\n================\n")
    for i in protagonistas:
        arq.write(i)
        arq.write("\n")
    arq.write("================\n")
    
    i = 0
    while i < num_viloes//2: #gera viloes
        new = masculinos[randint(0, len(masculinos)-1)]
        viloes.append(new)
        new = femininos[randint(0, len(femininos)-1)]
        viloes.append(new)
        i += 1
    shuffle(viloes)
    arq.write("\nVILÕES")
    arq.write("\n================\n")
    for i in viloes:
        arq.write(i)
        arq.write("\n")
    arq.write("================\n")
    
    i = 0
    while i < num_coadjuvantes//2: #gera coadjuvantes
        new = masculinos[randint(0, len(masculinos)-1)]
        coadjuvantes.append(new)
        new = femininos[randint(0, len(femininos)-1)]
        coadjuvantes.append(new)
        i += 1
    shuffle(coadjuvantes)
    arq.write("\nCOADJUVANTES")
    arq.write("\n================\n")
    for i in coadjuvantes:
        arq.write(i)
        arq.write("\n")
    arq.write("================\n")
    gera_eps(num_ep)

def gera_eps(num_ep): #gera todos os episódios
    n = 1
    
    while n < num_ep:
        arq.write(f"\nEpisódio {n}")
        arq.write("\n================\n")
        for i in protagonistas:
            i = i.split()[0]
            acao = acoes[randint(0, len(acoes)-1)]
            coad = (coadjuvantes[randint(0, len(coadjuvantes)-1)]).split()[0]
            loc = locais[randint(0, len(locais)-1)]
            var = (f"{i} {acao} {coad} {loc}\n")
            if(i == set(masculinos)):
                var = var.replace("@", "o")
            else:
                var = var.replace("@", "a")
            arq.write(var)
        arq.write("\n")
        
        for i in viloes:
            i = i.split()[0]
            acao = acoes[randint(0, len(acoes)-1)]
            prot = (protagonistas[randint(0, len(protagonistas)-1)]).split()[0]
            loc = locais[randint(0, len(locais)-1)]
            var = (f"{i} {acao} {prot} {loc}\n")
            if(i == set(masculinos)):
                var = var.replace("@", "o")
            else:
                var = var.replace("@", "a")
            arq.write(var)
        arq.write("\n")

        for i in protagonistas:
            i = i.split()[0]
            acao = acoes[randint(0, len(acoes)-1)]
            vil = (viloes[randint(0, len(viloes)-1)]).split()[0]
            loc = locais[randint(0, len(locais)-1)]
            var = (f"{i} {acao} {vil} {loc}\n")
            if(i == set(masculinos)):
                var = var.replace("@", "o")
            else:
                var = var.replace("@", "a")
            arq.write(var)
        arq.write("================\n")
        n += 1
        
    arq.write(f"\nEpisódio Final")
    arq.write("\n================\n")
    for i in viloes:
        i = i.split()[0]
        desf = finais_viloes[randint(0, len(finais_viloes)-1)]
        prot = (protagonistas[randint(0, len(protagonistas)-1)]).split()[0]
        var = (f"{i} {desf}\n")
        var = var.replace("#", f"{prot}")

        if(i == set(masculinos)):
            var = var.replace("@", "o")
        else:
            var = var.replace("@", "a")
        arq.write(var)
    arq.write("\n")
    
    for i in protagonistas:
        i = i.split()[0]
        desf = finais_protagonistas[randint(0, len(finais_protagonistas)-1)]
        vil = (viloes[randint(0, len(viloes)-1)]).split()[0]
        var = (f"{i} {desf}\n")
        var = var.replace("#", f"{vil}")

        if(i == set(masculinos)):
            var = var.replace("@", "o")
        else:
            var = var.replace("@", "a")
        arq.write(var)
    arq.write("\n")
    
    print('Salvamos a novela em "novela.txt"')

entradas() #chama a primeira função e inicia o programa