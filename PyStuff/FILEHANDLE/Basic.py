
inputFile=open('Read.txt')

print(inputFile) #<_io.TextIOWrapper name='Read.txt' mode='r' encoding='cp1252'>
#print(inputFile.readline()) # reads the line till \n

for line in inputFile :
   word=  line.strip()
   print(word)