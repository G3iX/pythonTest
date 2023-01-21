def do():
    for i in range(1, 821):
        my_file = open("ej" + str(i) + ".py", "w+")
        my_file.close()


#my_file = open("ej" + str(20) + ".py", "w+")
do()