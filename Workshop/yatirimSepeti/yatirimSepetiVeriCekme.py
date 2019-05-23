import pandas as pd
import time
import datetime
# Degerleri eklemek icin bos listeler tanimladim.
altinDegerler, dolarDegerler, euroDegerler, zamanDegerler = [], [], [], []

sure = int(input("Kac dakika boyunca veri cekilsin? "))

sayac = 0
print("--Veri Cekme Basladi--")
for i in range(sure):
  veriler = pd.read_html('http://finans.mynet.com/') 
  zamanDegerler.append(datetime.datetime.now()) # https://stackoverflow.com/questions/415511/how-to-get-the-current-time-in-python
  altinDF,dovizDF = veriler[11],veriler[9]
  del veriler
  altinDegerler.append(altinDF.loc[:,["Son.1"]].values[2][0]/100)
  del altinDF
  dolarDegerler.append(dovizDF.loc[:,["Son.1"]].values[0][0]/10000)
  euroDegerler.append(dovizDF.loc[:,["Son.1"]].values[1][0]/10000)
  del dovizDF
  sayac+=1
  print("{}. dakika verisi eklendi".format(sayac))
  if sayac==sure:
      break
  time.sleep(60) # 60 saniyelik bir bekletme.
print("--Veri Cekme Bitti--\nIslem toplam {} dakika surdu".format(sayac-1))

yatirimSepeti = {"Zaman":zamanDegerler,
                 "Ceyrek":altinDegerler,
                 "Dolar":dolarDegerler,
                 "Euro":euroDegerler}

del zamanDegerler , altinDegerler , dolarDegerler , euroDegerler

yatirimDF = pd.DataFrame(yatirimSepeti)
yatirimDF.to_csv(r'kurTakip2.csv',index=None,header=True) # https://datatofish.com/export-dataframe-to-csv/