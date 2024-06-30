def securechannel(operation,message,key):
    keys = list(map(int,key))
    result = []
    midx = 0
    if(operation == 1):
        for k in keys:
            character = message[midx] * k
            result.append(character)
            midx+=1
        while(midx<len(message)):
            result.append(message[midx])
            midx +=1
    if(operation == 2):
        for k in keys:
            character = message[midx:k]
            s= set(character)
            print(character)
            if(len(s)!=1):
                return -1
            result.append(character[0])
            midx+=k
        while(midx<len(message)):
            result.append(message[midx])
            midx+=1

    return ''.join(result)

# print(securechannel(1,"Open","12"))
print(securechannel(1,"Open","12"))
print(securechannel(2,"Oppeeeened","12"))