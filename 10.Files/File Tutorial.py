#In the following example, assume we have a file called "filename.txt" which has 10 lines in it.
#We only want to keep the even lines, so discard the odd ones


file = open("filename.txt", "r")

outfile = ""

for line in range (1,10):
    if line % 2 == 0:
        outfile += file.readline()
    else:
        file.readline()

file = open ("filename.txt", "w")
file.write(outfile)
file.close()

