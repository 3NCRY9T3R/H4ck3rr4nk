def is_leap(year):
    a=year
    if(a%4==0):
        if(a%100!=0):
            return 'True'
        elif((a%100==0) and (a%400==0)):
            return 'True'
        elif((a%100==0) and (a%400!=0)):
            return 'False'
    else:
        return 'False'
year = int(input())
print(is_leap(year))
