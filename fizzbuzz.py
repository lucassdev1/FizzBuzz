# for i in range - La variable i va contar 100 numeros en ese caso aquí abajo.

for i in range(100):
    number = i + 1
    if number % 3 == number % 5 == 0:
      print("FizzBuzz")

    elif number % 3 == 0:
      print("Fizz")

    elif number % 5 == 0:
      print("Buzz")

    else:
      print(number)

# Con ayuda de La red de Mário:  https://www.youtube.com/watch?v=g86_bsTXpQI
