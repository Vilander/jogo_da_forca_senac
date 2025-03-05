from os import system
import random
system('cls')

#def -> declaração de um função
#nome da função
#(nomevariavel) -> as variaveis que vamos utilizar na nossa função
#(nomevariavel:str) -> declarando o tipo da varivel 
#(nomevariavel = '') -> declarando um valor padrão para caso o usuario não preencha
#() -> str : -> declarando o tipo de retorno
 
def sorteadorPalavra(listaPalavras:list[str] = [] ) -> str :
    qntdPalavras = len(listaPalavras) - 1
    numeroAleatorio = random.randint(0, qntdPalavras) #magic number
    
    return listaPalavras[numeroAleatorio]
    # print( random.choice(lista) )

def imprimirPalavra(palavra: str = '', letrasCorretas: list[str] = []):
    
    # print(palavra)
    for letra in palavra:
        if letra in letrasCorretas:
            print(letra, end=' ')
        else:    
            print('_', end=' ')
    print()

def testarLetraPalavra(palavra:str, letra:str, letrasCorretas:list[str]) -> bool:
    system('cls')
    if letra in palavra:
        letrasCorretas.append(letra)
        # print(letrasCorretas)
        return True
    else:
        return False

def jogar(lista:list[str]):
    palavra = sorteadorPalavra(lista)
    letra = ''
    letrasCorretas = []
    while letra != '0':
        imprimirPalavra(palavra, letrasCorretas)
        letra = input('Digite uma letra: ')
        
        if letra in letrasCorretas:
            system('cls')
            print('Você já tentou essa letra....')
            continue
        
        if testarLetraPalavra(palavra, letra, letrasCorretas):
            print('Acerto!')
        else:
            print('Errou!')
        
        # Validar de o usuario ganhou!!!
        todasLetrasCorretas = True
        
        for letra in palavra:
            if letra not in letrasCorretas:
                todasLetrasCorretas = False
        
        if todasLetrasCorretas:
            print('Você acertou a palavra!!!!!')
            break
     
   
lista = [
    'python', 'php', 'javascript', 'csharp', 'node', 'html', 'css', 'java', 'ruby', 'flask', 'django', 'jquery', 'typescript', 'delphi'
]

jogar(lista)

# o sistema deve dar um aviso caso a letra esteja incorreto -> ok
# o sistema deve dar um aviso se a letra já foi tentada

# o sistema deve avisar se o usuario ganhou o jogo (ganha quando o usuario acertar todas as letras...)