file = "hello.txt"

# def write_file(count):
#     hello = open(file, "w")
#     for i in range(1, count +1):
#         hello.write(input(f'{i}. Enter value: ') + "\n")
#     hello.close()

# def read_file():
#     hello = open(file, "r")
#     print(hello.read())
#     hello.close()
#     write_file(int(input("Enter number of inputs: ")))

# write_file(int(input("Enter number of inputs: ")))
# read_file()



# def appen_file(count):
#     hello = open(file, "a")
#     for i in range(1, count +1):
#         hello.write(input(f'{i}. Enter value: ') + "\n")
#     hello.close()


with open(file, 'w', encoding='utf-8-sig') as filee:
    print(filee)
    filee.write("hello")
    filee.read()
