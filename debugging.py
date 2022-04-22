def divisors(num):
     try:
          if num < 0:
               raise ValueError("El numero debe ser mayor a cero")
          divisors = []
          for i in range (1, num + 1):
               if num % i == 0:
                    divisors.append(i)
          return divisors
     except ValueError as ve:
          print(ve)
          return False



def run():
     try:
          num = int(input("Ingresa un numero: "))
          
          print(divisors(num))
          print("Termino mi programa")
     except ValueError:
          print("Debes ingresar un numero")

if __name__ == '__main__':
     run()