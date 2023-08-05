import re

def checkRegEx(str):
    def cb(num):
        if(re.search(num[0],str)!=None): 
            return num[1]
    return cb

def numberMap(str):
     return list(filter(None,list(map(checkRegEx(str),{
        "zero":"0",
        "one":"1",
        "two":"2",
        "three":"3",
        "four":"4",
        "five":"5",
        "six":"6",
        "seven":"7",
        "eight":"8",
        "nine":"9"
    }.items()))))[0]