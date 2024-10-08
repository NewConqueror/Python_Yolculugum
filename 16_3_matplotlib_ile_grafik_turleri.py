import matplotlib.pyplot as plt

yil = [2010,2011,2012,2013,2014]

oyuncu1= [8,10,12,7,9]
oyuncu2= [7,12,5,15,21]
oyuncu3= [18,20,22,25,19]

# Stack plot Yığın grafiği 2. 1 in üstüne eklenir  3. 2. nin üstüne eklenir yani
# oyuncu1 8  oyuncu2 8 + 7 = 15   oyuncu3 ise  15 + 18 = 33 olur

plt.plot([],[], color="y", label="oyuncu1")    # stackplot için böyle yapmamız gerekiyor boş liste tanımlicaz
plt.plot([],[], color="r", label="oyuncu2")
plt.plot([],[], color="b", label="oyuncu3")

plt.stackplot(yil,oyuncu1,oyuncu2,oyuncu3, colors=["y","r","b"]) # sonra o listelere gelenleri yazıcaz

plt.title("Yıllara Göre Gol Grafiği")
plt.xlabel("Yıllar")
plt.ylabel("Gol Sayıları")

plt.legend()
plt.show()

# pasta grafiği pie plot # shadow gölge verir explode ile aralarındaki mesafe ayarlanır autopct üzerine yüzdeyi yazar

gol_tipleri = "penaltı","kaleye atılan şut","serbest vuruş"

goller = [12,30,8]
renkler = ["y","r","b"]

plt.pie(goller, labels=gol_tipleri, colors=renkler, shadow=True, explode=(0.05,0.05,0.05), autopct="%1.1f%%")

plt.show()

# sütun grafiği

plt.bar([0.25, 1.25, 2.25, 3.25, 4.25], [50,40,70,80,20], label="BMW", width=.5)
plt.bar([0.75, 1.75, 2.75, 3.75, 4.75], [80,20,20,50,60], label="AUDİ", width=.5)

plt.legend()
plt.xlabel("Gün")
plt.ylabel("Mesafe (km) ")
plt.title("Araç Bilgileri")

plt.show()


# Histogram 0 ile 10 arasında kaç tane 10 20 arasında kaç tane 20-30 kaç  90-10 arasında kaç tane vs onu söyler 

yaslar = [22,55,62,45,21,22,34,42,42,4,2,102,95,85,55,110,120,70,65,55,111,115,80,75,65,54,44,43,42,48]
yas_gruplari = [0,10,20,30,40,50,60,70,80,90,100]

plt.hist(yaslar, yas_gruplari, histtype="bar", rwidth=0.8)
plt.xlabel("Yaş Grupları")
plt.ylabel("Kişi Sayısı")

plt.title("Histogram Grafiği")

plt.show()  # tam ortada tam ortadaki değerler var