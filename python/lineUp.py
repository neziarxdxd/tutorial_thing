word= "aaabbbcaa"+"@"
dictList = []
count = 1
for i in range(len(word)-1):
    
    
    currentCount = []

    

    if word[i] == word[i+1]:
        count+=1
        print("passed",word[i],word[i+1],count)
       

    else:
        print("else",count)
        if count==1:
            dictList.append([word[i]])
        else:   
            dictList.append([str(count),word[i]])
        count=1
        
print("".join(["".join(dictList[i]) for i in range(len(dictList))]))
        
    