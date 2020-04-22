import re

# a = "aku"
# b="daku suka"

def findInteger(string):
    return re.findall(r"(?: |^)[0-9]{1,3}(?:.[0-9]{3})* ",string)
def findDate(string):
    return re.findall(r"[\d]{1,2}/[\d]{1,2}/[\d]{4}", string)
# jumlah = "^([0-9]{1,3}(,[0-9]{3})*(\.[0-9]+)?|\.[0-9]+)$"
# string = "251000000 Laman Pusat Informasi dan Koordinasi COVID Jabar (Pikobar) pada Sabtu (11/4/2020) pukul 18.43 WIB, mencatat terdapat 421 orang yang terkonfirmasi positif COVID-19."
# all = re.findall(r"(?: |^)[0-9]{1,3}(?:.[0-9]{3})* ",string)
# /^([a-z0-9]+(?:-[a-z0-9]+)+)$/im
# all = re.findall(r"(?!0|\.00)[0-9]+(,\d{3})*(.[0-9]{0,2})$",string)
# date = re.findall(r"[\d]{1,2}/[\d]{1,2}/[\d]{4}", string)


print(all)
# print(date)
#print(re.match(a,b))