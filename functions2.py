# Ejemplos: Sentencia if – else
# ejemplo No. 1
y = 3

if y > 4:
  print("¡No voy a imprimir!") #esta sentencia no se ejecuta
else:
  print("¡La condición no era verdadera!") #esta sentencia se ejecuta

# ejemplo No. 2
z= 7
if z > 8:
	print("No voy a imprimir")
elif z > 5:
	print("Yo lo haré")
elif z > 6:
	print("Tampoco voy a imprimir")
else:
	print ("Yo tampoco")

# ejemplo No. 3
x = 34
if x %  2 == 0:  # comprueba número par.
  if x > 10:
    print("Este número es par y es mayor que 10")
  else:
    print("Este número es par, pero no mayor 10")
else:
  print ("El número no es par. Así que punto de verificación más.")

# Ejemplos ternary operator
# ejemplo 1

age = input('Enter your age:')

if int(age) >= 18:
    ticket_price = 20
else:
    ticket_price = 5

print(f"The ticket price is {ticket_price}")

# ejemplo 2

age = input('Enter your age:')

ticket_price = 20 if int(age) >= 18 else 5

print(f"The ticket price is {ticket_price}")

# ejemplo 3
import random

nums = [random.choice(range(100)) for i in range(10)]

for num in nums:
    print(f"{num} is {'even' if num%2==0 else 'odd'}")

# Ejemplos for loop

# ejemplo 1
for index in range(1, 6):
    print(index)

print ("-----")
# ejemplo 2

for index in range(0, 11, 2):
    print(index)

print("-----")
# ejemplo 3

sum = 0
for num in range(101):
    sum += num
    
print(sum)


# Ejemplos while
# ejemplo No. 1

max = 5
counter = 0

while counter < max:
    print(counter)
    counter += 1

# ejemplo No. 2

command = ''

while command.lower() != 'quit':
    command = input('>')
    print(f"Echo: {command}")


# ejemplo No. 3

i = 6
while i < 9:
    print(i)
    i += 1

