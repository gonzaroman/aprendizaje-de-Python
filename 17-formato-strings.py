price = 59
txt = f"The price is {price} dollars"
print(txt)


txt = f"The price is {price:.2f} dollars"
print(txt)

txt = f"The price is {20 * 59} dollars"
print(txt)

price = 400
tax = 0.25
txt = f"The price is {price + (price * tax)} dollars"
print(txt)

#condicionales

price = 49
txt = f"It is very {'Expensive' if price>50 else 'Cheap'}"

print(txt)

#mayusculas
fruit = "apples"
txt = f"I love {fruit.upper()}"
print(txt)