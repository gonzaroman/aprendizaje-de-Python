alimentos = ["manzana", "pan", "queso", "leche"]

print(alimentos[0])
print(alimentos[1])
print(alimentos[2])
print(alimentos[3])

for alimento in alimentos:
    print(alimento)


for alimento in alimentos:
    if alimento == "queso":
        print("tienes que comprar esto "+alimento)
        break
    print(alimento)


for alimento in alimentos:
    if alimento == "queso":
        print("tienes que comprar esto "+alimento)
        continue
    print(alimento)


for number in range(1,8):
    print(number)


for letra in "hola que tal":
    print(letra)

contador = 5
while contador <= 10:
    print(contador)
    contador = contador + 1