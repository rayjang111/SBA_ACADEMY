string='hello'
long_string='oh! hello! my name is ___'
splitter='!'
def String_length(string):
    length=0
    for i in string:
        length+=1
    return length
def Find_string_index(string,long_string):
    for i in range(String_length(long_string)):
        if long_string[i:i+String_length(string)]==string:
            return i
def split_string(string,splitter):
    array=[]
    save_point=0
    for i in range(String_length(string)):
        if string[i]==splitter:
            array.append(string[save_point:i])
            save_point=i
    array.append(string[save_point:i])
    return array
String_length(string)

Find_string_index(string,long_string)

split_string(long_string,splitter)
    
