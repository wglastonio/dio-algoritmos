hero_name = input('What is the hero name? ')
hero_xp = int(input('What is the hero XP? '))

if (hero_xp > 10000):
    level = "Radiante";
elif (hero_xp > 9000):
    level = "Imortal";
elif (hero_xp > 8000):
    level = "Ascendente";
elif (hero_xp > 7000):
    level = "Platina";
elif (hero_xp > 5000):
    level = "Ouro";
elif (hero_xp > 2000):
    level = "Prata";
elif (hero_xp > 1000):
    level = "Bronze";
else:
    level = "Ferro";

print(f"O Herói de nome {hero_name} está no nível de {level}")
