links = 'http://site1.com.br'
# links = str(input('Cole seu(s) link(s) aqui: ')).replace(' ', '').lower()

pontoEVirgula = links.count(';')
pontoEVirgula1 = links.find(';')
pontoEVirgula2 = links.rfind(';')

http = links.count('http')
http1 = links.find('http')
http3 = links.rfind('http')
http2 = links.find('http', http1 + 1, http3)

www = links.count('www')  # mostra a quantidade de ocorrências do elemento "www"
www1 = links.find('www')  # mostra o índice da primeira ocorrência do elemento "www", contagem da esquerda para direita
www3 = links.rfind('www')  # monstra o índice primeira ocorrência do elemento "www" da direita para esquerda
www2 = links.find('www', www1 + 1, www3)  # mostra a segunda ocorrência

ponto = 0  # só poderá ser executado após todos os outros serem verificados, analisar melhor a estrutura de uma URL...

totalDeOcorrencias = www + http
listaDeLinks = []

if pontoEVirgula == 2:  # separando os links pelo ponto e vírgula
    print('passou aqui 01')
    listaDeLinks.append(links[0: pontoEVirgula1])
    listaDeLinks.append(links[pontoEVirgula1 + 1: pontoEVirgula2])
    listaDeLinks.append(links[pontoEVirgula2 + 1:])

elif pontoEVirgula == 1 and totalDeOcorrencias == 3:
    print('passou aqui 02')
    if http == 3:  # todos os links http,com apenas um ponto e vírgula
        print('passou aqui 02/01')
        if pontoEVirgula1 < http2:
            print('passou aqui 02/01/01')
            listaDeLinks.append(links[http1: http2 - 1])
            listaDeLinks.append(links[http2: http3])
            listaDeLinks.append(links[http3:])

        elif pontoEVirgula2 > http2:
            print('passou aqui 02/01/02')
            listaDeLinks.append(links[http1: http2])
            listaDeLinks.append(links[http2: http3 - 1])
            listaDeLinks.append(links[http3:])

    elif www == 3:  # todos os links www, com apenas um ponto e vírgula
        print('passou aqui 02/02')
        if pontoEVirgula1 < www2:
            print('passou aqui 02/02/01')
            listaDeLinks.append(links[www1: www2 - 1])
            listaDeLinks.append(links[www2: www3])
            listaDeLinks.append(links[www3:])

        elif pontoEVirgula2 > www2:
            print('passou aqui 02/02/02')
            listaDeLinks.append(links[www1: www2])
            listaDeLinks.append(links[www2: www3 - 1])
            listaDeLinks.append(links[www3:])

elif pontoEVirgula == 0 and totalDeOcorrencias == 3:
    print('03')
    if http == 3:  # todos os links http
        print('03/01')
        listaDeLinks.append(links[http1: http2])   # acrescentando os links na lista
        listaDeLinks.append(links[http2: http3])
        listaDeLinks.append(links[http3:])

    elif www == 3:  # todos os links www
        print('03/02')
        listaDeLinks.append(links[www1: www2])
        listaDeLinks.append(links[www2: www3])
        listaDeLinks.append(links[www3:])

    elif http == 2 and www == 1:  # 2 http e 1 www
        print('03/03')
        if www1 < http1:
            print('03/03/01')
            listaDeLinks.append(links[www1: http1])
            listaDeLinks.append(links[http1: http3])
            listaDeLinks.append(links[http3:])
            
        elif http1 < www1 < http3:
            print('03/03/02')
            listaDeLinks.append(links[http1: www1])
            listaDeLinks.append(links[www1: http3])
            listaDeLinks.append(links[http3:])

        elif www1 > http3:
            print('03/03/03')
            listaDeLinks.append(links[http1: http3])
            listaDeLinks.append(links[http3: www1])
            listaDeLinks.append(links[www1:])

    elif http == 1 and www == 2:  # 1 http e 2 www
        print('03/04')
        if http1 < www1:
            print('03/04/01')
            listaDeLinks.append(links[http1: www1])
            listaDeLinks.append(links[www1: www3])
            listaDeLinks.append(links[www3:])

        elif www1 < http1 < www3:
            print('03/04/02')
            listaDeLinks.append(links[www1: http1])
            listaDeLinks.append(links[http1: www3])
            listaDeLinks.append(links[www3:])

        elif www1 > http3:
            print('03/04/03')
            listaDeLinks.append(links[www1: www3])
            listaDeLinks.append(links[www3: http1])
            listaDeLinks.append(links[http1:])

    elif http == 1:   # and total de ocorrência for == 3
        print('verificar se possui apenas 1 link ou se há outros links sem o início http ou www...')

elif totalDeOcorrencias == 0:
    print('04')
elif totalDeOcorrencias == 1:
    print('05')
    if http == 1:
        listaDeLinks.append(links[http1:])
        print('05/01')
    elif www == 1:
        print('05/02')
        listaDeLinks.append(links[www1:])


# http://www e https://www

'''
[x] todos http
[x] todos www
[x] 1 http e 2 www
[x] 1 www  e 2 http
[x] 2 pontos e vírgula
[x] 1 ponto e virgula para 3 links
[ ] sem www, http, ponto e vírgula 
[ ] apenas  1 link
[ ] apenas 2 links
[ ] vírgula ao invés de ponto e virgula
[ ] espaço em branco
[ ] somente números
...

'''


'''if http1 < www1:
    listaW2 = [links[http1], links[www1], links[www3]]
    for i in range(0, 3):
        listaDeLinks.append(listaW2[i])'''


print(f'listaDeLinks: {listaDeLinks}')
print(f'ponto e vírgula 01: {pontoEVirgula1}, ponto e vírgula 02: {pontoEVirgula2}')
print(f'A quantidade total de ocorrências de www e http: {totalDeOcorrencias}')
print(f'A quatidade total de ocorrências de ponto e vírgula: {pontoEVirgula}')
print(f'www1: {www1}, www2: {www2}, www3: {www3} ')
print(f'http1: {http1}, http2: {http2}, http3: {http3}')