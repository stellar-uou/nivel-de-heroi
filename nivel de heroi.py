print("Seja bem vindo(a)!")

nome = input("Digite o nome de seu herói: ")

print("Olá", nome, "!")

xp = int(input("Digite o total de XP de seu herói: "))

if xp <= 1000:
    print("O herói", nome, "está no nível Ferro!")

elif 1001 >= xp <= 2000:
    print("O herói", nome, "está no nível Bronze!")

elif 2001 >= xp <= 5000:
    print("O herói", nome, "está no nível Prata!")

elif 5001 >= xp <= 7000:
    print("O herói", nome, "está no nível Ouro!")
    
elif 7001 >= xp <= 8000: 
    print("O herói", nome, "está no nível Platina!")
    
elif 8001 >= xp <= 9000:
    print("O herói", nome, "está no nível Ascendente!")
    
elif 9001 >= xp <= 10000:
    print("O herói", nome, "está no nível Imortal!")
    
elif xp >= 10001:
    print("O herói", nome, "está no nível Radiante!")
    
else:
    print("Não foi possível calcular o nível do herói.")

