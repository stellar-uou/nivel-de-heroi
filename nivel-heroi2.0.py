print("Seja bem vindo(a)!")

nome = input("Digite o nome de seu herói: ")

print("Olá", nome, "!")

xp = int(input("Digite o total de XP de seu herói: "))

def nivel():
    if xp <= 1000:
        return "bronze"

    elif 1001 >= xp <= 2000:
        return "prata"

    elif 2001 >= xp <= 5000:
        return "ouro"

    elif 5001 >= xp <= 7000:
        return "platina"
        
    elif 7001 >= xp <= 8000: 
        return "diamante"
        
    elif 8001 >= xp <= 9000:
        return "ascendente"
        
    elif 9001 >= xp <= 10000:
        return "imortal"
        
    else:
        return "radiante"

nivel_heroi = nivel()

print("O herói", nome, "esta nível", nivel_heroi, "!")
