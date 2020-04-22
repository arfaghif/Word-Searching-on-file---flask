def KMPSearch(pat, txt): 
    M = len(pat) 
    N = len(txt) 

    lps = findArrayLPS(pat) #cai lpsnya terlebih dahulu
    j = 0 #index penggeseran pat
    i = 0 # index penggeseran txt
    while i < N: 
        if pat[j].lower() == txt[i].lower(): 
            if(j==M-1):#sudah menemukan yang sesuai
                return True
            i += 1
            j += 1

        elif(j>0):
            j = lps[j-1] 
        else:
            i +=1
    return False
  

def findArrayLPS(pat):
    #res adalah array yang akan menjadi hasil
    length = len(pat)
    res = [0 for i in range (length)]
    val = 0
    i = 1
    while( i< length ):
        if(pat[i].lower() == pat[val].lower()):#tidak mempedulinan case
            val += 1
            res[i] = val
            i += 1
        elif val>0:
            #lihat kecocokan yang sebelumnya berdasarkan nilai lps
            val = res[val-1]
        else:
            i+=1
    return res
                

  
# txt = "ABABDABACDABABCABAB"
# pat = "AAACCAAACA"
# pat1 = "ababcaBaB"
# KMPSearch(pat, txt) 
# KMPSearch(pat1, txt) 

  

