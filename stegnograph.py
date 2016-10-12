# This is for hiding the data as spaces.
#Get some user input
msg = input("Enter your string here :")
#Convert the string to binary
binMsg=[]
for text in msg:
	binMsg.append(bin(ord(text))[2:])
binMsg = ''.join(binMsg)
#get the number of letters required from the carrier file
count = 0
msgLen = len(binMsg) + 1
carrierText = []
file = open("carrierText.txt","r")
for word in file.read().split():
	count+=1
	carrierText.append(word)
	if count > msgLen:
		break
file.close()
i = -1
finalString = []
for num in binMsg:
	i+=1
	finalString.append(carrierText[i])
	if num == '0' :
		finalString.append(" ")
	else :
		finalString.append("  ")
finalString.append(carrierText[i+1])		
finalString= ''.join(finalString)		
file = open("hidden.txt","w")
file.write(finalString)
file.close()