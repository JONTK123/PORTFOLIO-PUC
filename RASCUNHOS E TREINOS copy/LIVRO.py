'''Thiago Luiz Fossa e Gustavo Bicaletto'''

# Tratamento de excessoes para digitacao da quantidade de livros

while True: # Loop para repetir ate que seja inserido o NUMERO correto
    try: 
        qntl = int(input('Digite a quantidade de livros:\n '))
        break # Se inseriu corretamente, PARA o programa, se nao:
    except ValueError:
        print('Tem que ser numero inteiro...') # Se inseriu um numero incorreto, vai dar um erro, se o erro for o mesmo do que a excessao ele manda esse print e reinicia o loop



# Criacao do dicionario dos livros

Livros = {}
    
for i in range (qntl):

    cod = int(input('Digite o codigo do livro ( 3 digitos de preferencia ):\n ')) # Cod = CHAVE primeiro item do dicionario LIVROS, + importante
    tit = input('Digite o titulo do livro:\n ').upper()
    nu_autor = int(input('Digite o numero de autores do livro:\n '))
    autores = []
    for j in range (nu_autor): 
        no_autor = input('Digite o(s) nome(s) do(s) autor(es):\n ') # Nome dos autores baseado na quantidade de autores
        autores.append(no_autor) # Insere tambem o nome dos autores, dentro do for pata armazenar todos que forem escritos
    preco = float(input('Digite o valor do livro:\n '))

    Livros[cod] = [tit, nu_autor, autores, preco] # Cracao do dicionario, coloca todos os valores da lista dentro dele

print(Livros) # Printa dicionario

# Busca pelo titulo do livro

for t in range(qntl):

    perg1 = input('Digite o TITULO do livro para exibir suas informacoes:\n ').upper() # Busca do titulo

    for livro in Livros.values(): # Percorrer todos os ITENS dentro das CHAVES do dicionario Livros

            if perg1 == livro[0]: # Se o TITULO inserido for igual ao TITULO  ( ITEM 0!!!, ITEM 1 JA SERIA NUMERO DE AUTORES e assim por diante... ) entao:
        
                print(f'As informacoes do livro ( buscadas pelo titulo ) sao essas:\n {livro} ') # Printa a CHAVE INTEIRA ( mais conhecido como as informações do livro )

for c in range(qntl):

    perg2 = int(input('Digite o CODIGO para realizar a busca:\n ')) # Busca do titulo

    for p in Livros.keys(): # Percorre as CHAVES do dicionario
            
            if perg2 == p: # SE a chave digitada for igual a chave percorrida do dicionario 
                print(f'As informacoes do livro ( buscadas pelo CODIGO ) sao essas: {Livros[p]}\n ') # printa informacoes daquela chave, ( mais conhecido como as informações do livro )


# Imprimir livros com valor maior que 50 reais      


lista_50 = [] # lista para colocar os livros que possuem valor maior que 50

for key, o in (Livros.items()): # percorrer a os itens de dentro do dicionario
     
    if o[3] > 50.00: # se o item [3] ( QUE EH O PRECO ) for maior que 50 
        lista_50.append(o) # Coloco todos os itens dessa chave para a lista dos maiores que 50 reais
        print(f'Os dados dos livros que possuem um PRECO maior que 50 reais sao: {key, lista_50}\n') # printa a lista dos com preco maior que 50 reais

# Imprimir em formato tabela

print('{:<10} {:<30} {:<20} {:<10}'.format('Código', 'Título', 'Autor(es)', 'Preço'))
print('-' * 70)

for livro in lista_50:
    print(f"{key}, {livro[0]} {livro[1]:} R$ {livro[3]:}")

    




                    

    
    