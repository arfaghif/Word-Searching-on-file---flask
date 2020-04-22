import re

# a = "aku"
# b="daku suka"

def findInteger(string):
    return re.findall(r"(?: |^)[0-9]{1,3}(?:.[0-9]{3})*(?:\.| |$)",string)

def findDate1(string):
    return re.findall(r"[0-9]{1,2}(?:/|-)[0-9]{1,2}(?:/|-)[0-9]{4}", string)
def findDate2(string):
    return re.findall(r"[0-9]{1,2}(?:/|-)[0-9]{1,2}(?:/|-)[0-9]{2}", string)
def findDate3(string):
    return re.findall(r"[0-9]{4}(?:/|-)[0-9]{1,2}(?:/|-)[0-9]{1,2}", string)
def findDate4(string):
    return re.findall(r"[0-9]{4}(?:/|-)[0-9]{1,2}(?:/|-)[0-9]{1,2}", string)
def findDate5(string):
    return re.findall(r"[\d]{1,2} [adfjmnos]\w* [\d]{4}", string.lower())
def findDate(string):
    return findDate1(string) + findDate2(string) +findDate3(string)  + findDate4(string) +findDate5(string)

def findTime1(string):
    return re.findall(r"[0-9]{1,2}\:[0-9]{1,2}", string)
def findTime2(string):
    return re.findall(r"[0-9]{1,2}\.[0-9]{2}", string)
def findTime(string):
    return findTime1(string) + findTime2(string)

def findHari1(string):
    return re.findall(r"(?:^| )(?:monday|tuesday|wednesday|thursday|friday|saturday|sunday|senin|selasa|rabu|kamis|jumat|sabtu|minggu|ahad|mon|tue|wed|thu|fri|sat|sun(?:\.| |\,|$))", string.lower())
def findHari2(string):
    return re.findall(r"(?:^| )hari \w*(?:\.|\,| |$)",string)
def findHari(string):
    return findHari1(string) + findHari2(string)

def findAllTime(string):
    all = []
    day = findHari(string)
    date = findDate(string)
    time = findTime(string)
    if(len(day)):
        all.append(day[0])
    if(len(date)):
        all.append(date[0])
    if(len(time)):
        all.append(time[0])
    
    if(len(all)!=0):
        return ' '.join(str(el)for el in all)
    else :
        return "-"

def cetakInt(string):
    val = findInteger(string)
    if(len(val)!=0):
        return val[0]
    else:
        return "-"
# jumlah = "^([0-9]{1,3}(,[0-9]{3})*(\.[0-9]+)?|\.[0-9]+)$"
# string = "251000000 Laman Pusat Informasi dan Koordinasi COVID Jabar (Pikobar) pada Sabtu (11/4/2020) pukul 18.43 WIB, mencatat terdapat 421 orang yang terkonfirmasi positif COVID-19."
# all = re.findall(r"(?: |^)[0-9]{1,3}(?:.[0-9]{3})* ",string)
# /^([a-z0-9]+(?:-[a-z0-9]+)+)$/im
# all = re.findall(r"(?!0|\.00)[0-9]+(,\d{3})*(.[0-9]{0,2})$",string)
# date = re.findall(r"[\d]{1,2}/[\d]{1,2}/[\d]{4}", string)


#print(all)
# print(date)
#print(re.match(a,b))