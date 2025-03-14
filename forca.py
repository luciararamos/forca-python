import random

print("Bem-vindo ao Jogo da Forca!")

with open('palavras_forca.txt', 'r') as arquivo:
    palavras = [p.strip() for p in arquivo.readlines() if p.strip()]

def sortear_palavra():
    return random.choice(palavras)

def exibir_palavra_oculta(palavra):
    return " ".join("_" for _ in palavra)

def imprimir_palavra_parcialmente(palavra, letras_acertadas):
    palavra_parcial = ""
    for letra in palavra:
        if letra in letras_acertadas:
            palavra_parcial+=letra
        else :
            palavra_parcial+="_"
    return palavra_parcial

#sortear
palavra = sortear_palavra()
print(f"A palavra sorteada possui {len(palavra)} letras.")
print(exibir_palavra_oculta(palavra))

print("")

#set
letras_escolhidas = set()  
letras_acertadas = set()
erros_restantes = 6  

acertou_palavra = False

#loop
while erros_restantes > 0 and not acertou_palavra: #enquanto tiver erros restantes e não acertar a palavra
    letra = input("Digite uma letra:")

    if letra in letras_escolhidas:  #verificar se a letra escolhida já foi chamada
        print("A letra digitada já foi utilizada anteriormente")
        continue
    else :
        letras_escolhidas.add(letra)
    
    if letra in palavra:  #verificar se usuário acertou
        print("Você acertou!")
        letras_acertadas.add(letra)
    else :
        print("Você errou!") 
        erros_restantes -= 1
        print(f"Você tem {erros_restantes} tentativas!")
    
    palavra_parcialmente_preenchida= imprimir_palavra_parcialmente(palavra, letras_acertadas)
    print( " ".join(_ for _ in palavra_parcialmente_preenchida))
    
    if erros_restantes == 0: #Verificar se as tentativas acabaram
        print(f"Você perdeu! A palavra era {palavra}")
        continue
    if palavra_parcialmente_preenchida == palavra: #Verificar se todas as letras foram encontradas
        print("Você ganhou!")
        acertou_palavra = True
        continue








