function output = hide(msg)
l = length(msg) * 7 +1 ;
carrierMsg = getWords(l);
binData = dec2bin(msg);
binData = reshape(binData',1,numel(binData));
j = 0;
c = 1;
while c ~= l
    j = j + 1;
    if carrierMsg(j) == ' '
        if binData(c) == '1'
           carrierMsg = [carrierMsg(1:j) ' ' carrierMsg(j+1:end)];
        end
        c = c + 1;
        j = j + 1;
    end
end
output = carrierMsg;
%this is for long outputs
fileID = fopen('hidden.txt','w');
fprintf(fileID , '%s', output);
fclose(fileID);
end