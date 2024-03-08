def check_anagrams(str1, str2):
    str1=str1.replace(" ", "").lower()
    str2=str2.replace(" ", "").lower()


    if(len(str1)!=len(str2)):
        return false
    return sorted(str1) == sorted(str2)

input_strings = "listen silent"

str1,str2 = input_strings.split()

if check_anagrams(str1, str2):
    print("the string is anagram")
else:
    print("the string is not a anagram")
    
