def swap_case(s):
    b=''
    for i in s:
        if((i.islower())==True):
            b=b+i.upper()
        elif((i.isupper())==True):
            b=b+i.lower()
        elif((i==' ')):
            b=b+' '
        else:
            b=b+i
    return b



if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
