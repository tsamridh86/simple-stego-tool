function output = unhide(carrierMsg)
l = length(carrierMsg);
j = 1;
i = 1;
while i <= l
    if carrierMsg(i) == ' '
        i = i + 1;
        if carrierMsg(i) == ' '
            binData(j) = '1';
        else
            binData(j) = '0';
        end
         j = j + 1;
    end
    i = i + 1;
end
output = char(bin2dec(reshape(binData,7,[]).')).';
%this is for long outputs
fileID = fopen('out.txt','w');
fprintf(fileID , '%s', output);
fclose(fileID);
end
