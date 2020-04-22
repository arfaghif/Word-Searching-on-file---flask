import re

# a = "aku"
# b="daku suka"

def findInteger(string):
    return re.findall(r"(?: |^)[0-9]{1,3}(?:.[0-9]{3})* ",string)
def findDate(string):
    return re.findall(r"[\d]{1,2}(?:/|-| )[\d,Januari,Februari,Maret,April,Mei,Juni,Agustus,September,Oktober,November,Desember,January,February,March,May,June,July,August]{1,2}(?:/|-| )[\d]{2,4}", string)
def findTime(string):
    return re.findall(r"[\d]{1,2}(?:.|:)[\d]{1,2} ", string)
def findHari(string):
    return re.findall(r"[Senin,Selasa,Rabu,Kamis,Jumat,Sabtu,Minggu]",string)
def findHari2(string):
    return re.findall(r"hari",string)
def findAllTime(string):
    all = findHari2(string)  + findDate(string)
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