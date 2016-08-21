function package = getWords(targetAmount)
%this function will get the nessecary amount of carrier text needed from
%the dummy text
fileID = fopen('carrierText.txt','r');
word = fscanf(fileID,'%c');
currentAmount = 0;
i = 1;
while currentAmount ~= targetAmount
    package(i) = word(i);
    if word(i) == ' '
        currentAmount = currentAmount + 1;
    end
    i = i + 1;
end
fclose(fileID);
end