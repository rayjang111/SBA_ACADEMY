string='123asd a 12 sd12 3  a   '
def num_char_split(string):
    save_point=0
    string_list=[]
    for i in range(1,len(string)):
        if '0'<=string[i-1]<='9':
            while string[i]==' ':
                i=i+1
                if i==len(string)-1:
                    break
            if 'a'<=string[i]<='z' or 'A'<=string[i]<='Z':
                string_list.append(string[save_point:i])
                save_point=i
    string_list.append(string[save_point:])
    print(string_list)
num_char_split(string)
