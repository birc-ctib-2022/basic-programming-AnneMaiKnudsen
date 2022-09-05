
# Print the pattern

liste =[]
for i in range(5):
    liste.append("*")
    print(" ".join([str(y)for y in liste]))

for i in range(5):
    liste.remove("*")
    print(" ".join([str(y)for y in liste]))