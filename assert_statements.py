def divisors(num):
     assert int(num) > 0, "Debes ingresar un numero mayo a cero"
     divisors = []
     for i in range (1, num + 1):
          if num % i == 0:
               divisors.append(i)
     return divisors



def run():
     num = input("Ingresa un numero: ")
     assert num.isnumeric(), "Debes ingresar un numero"
     # isnumeric es una propiedad de los strings que automaticamente detecta si es numerico. no funciona en enteros. no acepta el menos para numeros negativos
     print(divisors(int(num)))
     print("Termino mi programa")


if __name__ == '__main__':
     run()