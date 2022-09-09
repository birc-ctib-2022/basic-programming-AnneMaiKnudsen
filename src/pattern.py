
# Print the pattern

stars=[]
for i in range(9):
    if i <5:
        stars.append("*")
        print(" ".join(stars))
    else:
        stars.remove("*")
        print(" ".join(stars))


    #print("".join(*liste))