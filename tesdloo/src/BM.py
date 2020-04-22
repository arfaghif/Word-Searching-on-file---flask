def BMSearch(pat, txt): 
    M = len(pat) 
    N = len(txt) 
    last = build(pat)
    i = M-1
    j = M-1
    while(i<=N-1): 
        if(pat[j].lower() == txt[i].lower()):#cek kesesuaian pattern dimulai ekornya
            if(j==0):
                return i
            j -=1
            i -=1
        else :#jump karakter khas BM
            lo = last[ord(txt[i].lower())]
            i = i+M -min(j,i+lo)
            j = M-1
    return False


def build(pat): 
  
    # Inisialisasi dengan -1
    length = 256
    res = [-1 for i in range (length)]
  
    # Mengisi posisi tiap char yang terakhir ditemukan
    for i in range(len(pat)): 
        res[ord(pat[i].lower())] = i
  
    return res
 
 

# txt = "ABABDABACDABABCABAB"
# pat = "ABABCABAB"
# pat1 = "ababcaBaB"
# print(BMSearch(pat, txt) )
# print (BMSearch(pat1, txt) )

