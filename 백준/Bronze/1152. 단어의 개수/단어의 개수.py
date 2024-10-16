line = input()

my_arr = line.split(" ")

if my_arr[0] == "" and my_arr[-1] == "":
    print(len(my_arr) - 2)
elif my_arr[0] == "" or my_arr[-1] == "":
    print(len(my_arr) - 1)
else:
    print(len(my_arr))
