import pandas as pd # biblioteca para processamento dos dados
from googletrans import Translator
#from time import sleep, time

import urllib.request # biblioteca que trabalha com requisições HTTP
import json # biblioteca para processamento de dados do tipo JSON



# função de extração do dataset e trasformação para dataframe
def load_data(url, encoding="utf-8"):
    dat_file = urllib.request.urlopen(url)

    json_format_file = [json.loads(line) for line in dat_file]

    df = pd.DataFrame(json_format_file)

    return df


# função de tradução do comentário
def translation(com, count, count2, CONSTANTE):

    try:
        num = 'comment {}'.format(count)
        translator = Translator()
        res = translator.translate(com, dest='en')
        print('\n',res.src)
        print('\n',res.text)

        # Tratamento de erro : verifica se o resultado da tradução ainda está em portugues
        # isso acontece pq a API n detecta o idioma, mesmo passando o idioma de origem, aí ela seta o idioma de origem como ingles
        # e como "já está em inglês, ela não faz nada"
        # esse bloco faz recursividade chamando a função novamnete na tentaiva de forçar a traduçõa quando a API se estabilizar
        # a qtd de controle da recursividade está determinada pela constante
        if res.text == com and count2 <= CONSTANTE:
            count2 += 1
            return translation(com,count, count2, CONSTANTE)
        elif count2 >= CONSTANTE:
            print('FALSE - try')
            return False, str(com), str(num)

        # quando dá certo - escreve no txt dataset_us o resultado da tradução
        # num - é a posição do comentário
        # com - é o comentário de origem
        # res.text - é o comentário traduzido
        with open('dataset_us.txt', 'a', encoding="utf-8") as f:
            f.write(str(num) + ';' + str(com) + ';' + str(res.text) + '\n')
            f.close()
        print('\n TRANSLATE COMMENT {} \n'.format(count))

    except:
        # tratativa de erro para quando o try nao funcionar
        # faz recursividade para chamar forçar tradução, até a qtd que a constante determina
        print('\n ERROR - COMMENT {} \n'.format(count))
        count2 += 1
        if count2 <= CONSTANTE:
            return translation(com,count, count2, CONSTANTE)
        else:
            print('FALSE - except')
            return False, str(com), str(num)

    return True, str(com), str(num)




if __name__ == "__main__":

    #dataframe
    df = load_data(url="http://tiagodemelo.info/datasets/dataset-v2.dat")

    # corte do dataset - especificação de quais linhas usarei
    # diferente do python puro, neste método a chave inicial e final estarão presente no resultado
    # o init representa a posição de onde começará o dataframe
    # fiz o init para controlar o fatiamento e o contador que controla a posição dos comentários
    init = 0
    df = df.loc[init:34000]

    # contador que controla a posição do comentário
    count = init
    # constante que determina o limite de recursividade
    CONSTANTE = 50

    # bloco que inicializa o txt com os seguintes campos
    with open('dataset_us.txt', 'a', encoding="utf-8") as f:
                f.write('comment_num' + ';' + 'comment_orig' + ';' + 'comment_us' + '\n')
                f.close()

    # for de iteração sobre a lista de comentários
    for com in df['reviewBody']:
        # contador que controla o número de recursividade feitas
        count2 = 0

        # chamada da função de tradução
        resul = translation(com, count,count2, CONSTANTE)

        # tratativa de erro para quando exceder o limite de tentativas de tradução do texto, o limite é determinado pela constante
        # escreve NaN no dataset_us (que é onde estão sendo guardados os resultados da tradução)
        # escreve o comentário não traduzido e a posição dele (serve para tratarmos e add depois no dataset_us, para substituirmos os NaN)
        if not resul[0]:
            print('ENTROU NA FALHA')
            with open('dataset_us.txt', 'a', encoding="utf-8") as f:
                f.write(resul[2] + ';' + resul[1] + ';' + 'NaN' + '\n')
                f.close()

            with open('failed_comments.txt', 'a', encoding="utf-8") as arq:
                arq.write(str(count) + ' :: ' + resul[1] + '\n')
                arq.close()
            print('ESCREVEU A FALHA')

        count += 1


    #fim da tradução
    print('\n TRANSLATION DONE!!!!! \n')
    print('\n EXCRIPT EXIT !!!!! \n')







#transformando dict em dataframe
#df_us = pd.DataFrame(data=dict)
#df_us.to_csv('dataset_us.csv')

#inserindo os comentarios traduzidos no df principal
#df['comment_us'] = df_us['comment_us']


#salvando em csv
#df.to_csv('dataset_translated.csv')
