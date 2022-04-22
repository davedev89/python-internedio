def read():
     numbers = []
     with open("./files/numbers.txt", "r", encoding="utf-8") as f:
          for line in f:
               numbers.append(int(line))
     print(numbers)

## el encoding utf 8 se agrega para evitar que tanto en lectura como escritura, no haya inconvenientes con caracteres que tengan tildes o ñ, etc

def write():
     names = ["Facundo", "David", "Pedro", "Cristian", "Rocío"]
     with open("./files/names.txt", "w", encoding="utf-8") as f:
          for name in names:
               f.write(name)
               f.write("\n") # esto hace un salto de linea entre cada nombre que itera


def run():
     write()


if __name__ == '__main__':
     run()