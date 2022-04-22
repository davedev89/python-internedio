from tkinter.tix import Tree


def run():
     my_list = [1, "Hello", True, 4.5]
     my_dict = {"firstname": "David", "lastname": "Carrevedo"}

     super_list = [
          {"firstname": "David", "lastname": "Carrevedo"},
          {"firstname": "Juan", "lastname": "Perez"},
          {"firstname": "Maria", "lastname": "Martinez"},
     ]

     super_dict = {
          "natural_nums": [1,2,3,4,5],
          "integer_nums": [-1, -2, 0, 1, 2],
          "floating_nums": [1.1, 4.5, 6.43]
     }

     for key, value in super_dict.items():
          print(key, "-", value)

     for item in super_list:
          print(item["firstname"] , "-" , item["lastname"])


if __name__ == '__main__':
     run()