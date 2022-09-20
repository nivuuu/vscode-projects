f = open("colours.txt", "r")

new_file = open("colours.txt", "w")

for x in range(1,11):
    new_line = f"{x}: Red \n"
    new_file.write(new_line)

new_file.close()

# append_file = open("colours.txt", "a")
# append_file.write("\n Red \n Blue\n Orange \n Green\n Yellow \n Purple \n Indigo \n")
