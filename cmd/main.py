from text import *
import MyRegex
print("browse file")
N = int(input("number of file:"))
print("Choose method:\n1.Regex\n2.KMP\n3.BM")
met = int(input("method:"))
l= []
for i in range (N):
    l.append(Text(input("nama file ke-" + str(i+1)+":")))

for text in l:
    sentence = text.match("terkonfirmasi positif",met)
    print("Jumlah :", end="" )
    print(MyRegex.findInteger(sentence)[0].replace(" ",""))
    print("date:",end="")
    print(MyRegex.findDate(sentence)[0])