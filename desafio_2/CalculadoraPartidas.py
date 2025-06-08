vitorias = int(input('Entre quantidade de vitorias: '))
derrotas = int(input('Entre quantidade de derrotas: '))
saldo = vitorias - derrotas

if (saldo > 100):
    level = "Imortal";
elif (saldo > 90):
    level = "Landario";
elif (saldo > 80):
    level = "Diamante";
elif (saldo > 5000):
    level = "Ouro";
elif (saldo > 2000):
    level = "Prata";
elif (saldo > 1000):
    level = "Bronze";
else:
    level = "Ferro";

print(f"O Herói tem saldo de {saldo} está no nível de {level}")
