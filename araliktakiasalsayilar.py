hangi_aralik = int(input ('Asal sayıları bulmak istediğiniz aralıktaki son sayı : '))
asal_sayilar = [2]
basla = 3 
while hangi_aralik-2 > 0 :
    kac_asal_var = len(asal_sayilar)
    a = 0
    sonuclar = []
    while kac_asal_var > 0 :
        kac_asal_var = kac_asal_var - 1
       
        if basla % int(asal_sayilar[a]) != 0:
            sonuclar.append(True)
            a = a + 1
            continue
        else :
            sonuclar.append(False)
            a = a + 1
            continue
    try :
        sonuclar.index(False)
    except ValueError :
        
        asal_sayilar.append(basla)
    hangi_aralik = hangi_aralik - 1 
    basla = basla + 1    
print(asal_sayilar)


