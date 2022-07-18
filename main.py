import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    i=0
    tot_tamanho=0
    tot_palavra=0
    sentenca=''
    frase=''
    lista_palavra=[]
    tot_frase=0
    tot_sentenca=0
    lista_geral=list(texto)
    total_caracteres=0

    while i<len(separa_sentencas(texto)):
        sentenca=separa_sentencas(texto)[i]
        tot_sentenca+=1
        j=0
        while j<len(separa_frases(sentenca)):
            frase=separa_frases(sentenca)[j]
            tot_frase+=1
            k=0
            while k<len(separa_palavras(frase)):
                palavra=(separa_palavras(frase))[k]
                lista_palavra.append(palavra)       
                tot_tamanho=tot_tamanho+len(palavra)
                tot_palavra+=1
                k=k+1
            j=j+1    
        i=i+1
    for l in lista_geral:
        if l!='!' and l!='.' and l!='?':
            total_caracteres+=1

    wal=tot_tamanho/tot_palavra
    
    tot_diferente=n_palavras_diferentes(lista_palavra)
    ttr=tot_diferente/tot_palavra
    
    tot_unicas=n_palavras_unicas(lista_palavra)
    hlr=tot_unicas/tot_palavra
    
    sal=total_caracteres/tot_sentenca
    
    sac=tot_frase/tot_sentenca
    
    pal=total_caracteres/tot_frase
    
    return [wal,ttr,hlr,sal,sac,pal]

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    tamanho_medio_palavra=abs(as_a[0]-as_b[0])
    type_token=abs(as_a[1]-as_b[1])
    hapax=abs(as_a[2]-as_b[2])
    tamanho_medio_senteca=abs(as_a[3]-as_b[3])
    complexidade_sentenca=abs(as_a[4]-as_b[4])
    tamanho_medio_frase=abs(as_a[5]-as_b[5])
    grau_similaridade=(tamanho_medio_frase+tamanho_medio_palavra+tamanho_medio_senteca+hapax+type_token+complexidade_sentenca)/6
    print(grau_similaridade)
    return grau_similaridade


def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    infectado=0
    i=0
    mais_similar=1000
    while i<len(textos):
        assinatura=calcula_assinatura(textos[i])
        nivel_similaridade=compara_assinatura(assinatura,ass_cp)
        if nivel_similaridade<mais_similar:
            print('entrou na condicional')
            mais_similar=nivel_similaridade
            infectado=i+1
        i=i+1
    return infectado



assinatura=le_assinatura()
textos=le_textos()
resultado=avalia_textos(textos,assinatura)
print('O autor do texto',resultado,'está infectado com COH-PIAH')



