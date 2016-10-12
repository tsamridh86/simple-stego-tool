# This is unhiding the data from the spaces
# Get the text file
from math import floor
file = open("hidden.txt","r")
hiddenMsg = file.read()
binaryMsg = []
i = 0
while i < len(hiddenMsg) - 1:
	i+=1
	if hiddenMsg[i] == ' ':
		i+=1
		if hiddenMsg[i] == ' ':
			binaryMsg.append('1')
		else :
			binaryMsg.append('0')
binLen = floor(len(binaryMsg)/7)
# a = [[x for x in range(columns)] for y in range(rows)]
finalChar = [[0 for x in range(0,7)] for y in range(0,binLen)]
for u in range(0,binLen):
	for j in range(0,7):
		finalChar[u][j]= binaryMsg[u*7+j]
	finalChar[u] = "".join(finalChar[u])
	finalChar[u] = chr(int(finalChar[u],2))
print ("Output of string :" ,"".join(finalChar))