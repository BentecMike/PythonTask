# 13. Пользователь задаёт две строки. Определить количество вхождений одной строки в другой.

# def counter(mystring,mysubstr):
#     res=mystring.count(mysubstr)
#     print(res)
#     return res
 
# if __name__ == '__main__':
#     mystring=input()
#     mysubstr=input()
#     counter(mystring, mysubstr)

def count_substring(string,sub_string):
     l=len(sub_string) 
     count=0 
     for i in range(len(string)-len(sub_string)+1): 
        if(string[i:i+len(sub_string)] == sub_string ): 
            count+=1 
            return count 
