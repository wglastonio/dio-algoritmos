
hero = []
hero_name = input('What is the hero name? ')
hero.append(hero_name)
hero_xp = int(input('What is the hero XP? '))
hero.append(hero_xp)

if (hero[1] > 10000):
    level = "Radiante";
elif (hero[1] > 9000):
    level = "Imortal";
elif (hero[1] > 8000):
    level = "Ascendente";
elif (hero[1] > 7000):
    level = "Platina";
elif (hero[1] > 5000):
    level = "Ouro";
elif (hero[1] > 2000):
    level = "Prata";
elif (hero[1] > 1000):
    level = "Bronze";
else:
    level = "Ferro";

print(f"O Herói de nome {hero_name} está no nível de {level}")
