file = open("teams.txt", "r")

outfile = ""

for line in range(1, 5):
    if line % 2 == 0:
        outfile += file.readline()
    else:
        file.close()
