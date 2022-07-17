def key_1(string,key):
    string_len = len(string)
    key_len = len(key)
    if(string_len > key_len):
        new_key = ""
        count = 0
        for i in range(string_len):
            # print(i)
            print(key[count])
            new_key += key[count]
            count += 1
            if(count == key_len):
                count = 0
    return new_key
            
            

print(key_1("ABCD","ab"))
