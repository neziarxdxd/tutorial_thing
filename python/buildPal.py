name = "kebab"
reverse = name[::-1]
listBuild=[]
for i in range(len(name)):
    x = name + reverse[i:]
    if x == x[::-1]:
        listBuild.append(x)
print(listBuild[-1])

