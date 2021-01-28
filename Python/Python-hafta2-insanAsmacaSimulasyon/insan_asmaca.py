# Problem Set 2, insan_asmaca.py
# İsim: 
# Katkıda bulunanlar:
# Harcanan Zaman:

# İnsan Asmaca Oyunu
# -----------------------------------
# Yardımcı kod
# Bu yardımcı kodu anlamanıza gerek yok,
# fakat fonksiyonları nası kullanacağınız bilmeniz
# gerekiyor.
# (öğrenmek için fonksiyon dizelerini okuyun!)
import random
import string
import pandas as pd

KELIME_LISTESI_DOSYASI = "tdk_sozcukler2.csv"
TÜRKÇE_ALFABE = 'abcçdefgğhıijklmnoöprsştuüvyz'
sesli_harfler=["a","e","ı","i","o","ö","u","ü"]

def kelimeleri_yükle():
    """
    Geçerli kelimelerin bir listesini döndürür. 
    Kelimeler, küçük harflerden oluşan dizelerdir.
    
    Sözcük listesinin boyutuna bağlı olarak, bu işlevin 
    tamamlanması biraz zaman alabilir.
    """
    print("Dosyadan kelime listesi okunuyor...")
    # dosyanın okunması
    dosya = pd.read_csv("tdk_sozcukler2.csv")
    # sözcüklerin küçük harfe çevrilmesi
    dosya['SOZCUKLER'] = dosya['SOZCUKLER'].str.lower() 
    # wordlist: list of strings
    kelime_listesi = dosya['SOZCUKLER'].tolist()
    print(f"{len(kelime_listesi)} kelimelik liste hazırlandı.")
    return kelime_listesi


def kelime_seç(kelime_listesi):
    """
    kelime_listesi (liste): kelimelerin listesi (dize)
    
    Kelime listesinde rastgele bir keliem döndürür.
    """
    return random.choice(kelime_listesi)

# yardımcı kodların sonu

# -----------------------------------

# Programın herhangi bir yerinden erişilebilmesi için kelime 
# listesini değişken kelime_listesine yükleyin
kelime_listesi = kelimeleri_yükle()


def kelime_tahmin_edildi_mi(gizli_kelime, tahmin_edilen_harfler):
    '''
    gizli_kelime: dize, kullanıcının tahmin ettiği kelime; 
        tüm harflerin küçük olduğunu varsayar
    tahmin_edilen_harfler: şimdiye kadar tahmin edilen harflerin listesi; 
        tüm harflerin küçük olduğunu varsayar
    döndürdüğü: boolean, gizli_kelime'nin tüm harfleri tahmin_edilen_harfler içindeyse True; 
        aksi takdirde False
    '''
    # KODUNUZU BURAYA YAZIN VE "pass" İFADESİNİ SİLİN
    if gizli_kelime in tahmin_edilen_harfler:
        return True
    else:
        return False

    



def tahmin_edilen_kelimeyi_al(gizli_kelime, tahmin_edilen_harfler):
    '''
    gizli_kelime: dize, kullanıcının tahmin ettiği kelime; 
        tüm harflerin küçük olduğunu varsayar
    tahmin_edilen_harfler: şimdiye kadar tahmin edilen harflerin listesi; 
        tüm harflerin küçük olduğunu varsayar
    döndürdüğü: dize, harflerden oluşur, alt çizgiler (_) ve gizli_kelime içindeki hangi harflerin 
        şimdiye kadar tahmin edildiğini temsil eden boşluklardan oluşur.
    '''
    
    z = list('_' * len(gizli_kelime))
   
    
    
    for i in range(len(gizli_kelime)):
        for j in tahmin_edilen_harfler:

           
            if j == gizli_kelime[i]:
                z[i] = j
    
    return z
    
                
    



def uygun_harfleri_al(tahmin_edilen_harfler, alfabe = TÜRKÇE_ALFABE):
    '''
    tahmin_edilen_harfler: şimdiye kadar tahmin edilen harflerin listesi; 
        tüm harflerin küçük olduğunu varsayar
    döndürdüğü: dize (harfler), Henüz tahmin edilmemiş harfleri temsil 
        eden harflerden oluşur.
    '''
    # alfabedeki harfleri alır
    alfabe = TÜRKÇE_ALFABE
    
    
    
    # KODUNUZU BURAYA YAZIN VE "pass" İFADESİNİ SİLİN
    for i in range(len(tahmin_edilen_harfler)):
        alfabe = alfabe.replace(tahmin_edilen_harfler[i],'')
    return alfabe
    
    

def insan_asmaca(gizli_kelime, alfabe = TÜRKÇE_ALFABE):
    '''
    gizli_kelime: dize, kullanıcının tahmin ettiği kelime; 
        tüm harflerin küçük olduğunu varsayar

    Etkileşimli bir İnsan Asmaca oyunu başlatır.
    
     * Oyunun başında kullanıcıya gizli_kelime'nin kaç harf içerdiğini 
       ve kaç tahminle başladığını bildirin.
      
     * Kullanıcı 6 tahminle başlamalıdır

     * Her turdan önce kullanıcıya kaç tahmin yaptğını ve henüz tahmin 
       etmediği harfleri göstermelisiniz.
    
     * Kullanıcıdan tur başına bir tahmin yapmasını isteyin. Kullanıcının 
       bir harf yazdığından emin olmayı unutmayın!
    
     * Kullanıcı, tahminlerinin bilgisayarın kelimesinde görünüp görünmediğine 
       dair her tahminden hemen sonra geri bildirim almalıdır.

     * Her tahminden sonra, kullanıcıya o ana kadar kısmen tahmin edilen 
       kelimeyi göstermelisiniz.
    
    Problem yönergesinde detaylandırılan diğer sınırlamaları takip edin.
    '''
    # alfabedeki harfleri alır
    alfabe = TÜRKÇE_ALFABE
    tahmin=6
    uyarı=3
    kelime=" "
    tahmin_edilen_harfler=" "
    
    
    
   
    print(gizli_kelime)
    print(f"{len(gizli_kelime)} harfli bir kelime düşünüyorum. ")
    
    count2=len(gizli_kelime)
    while tahmin>0:
        print("*"*50)
        count=0 
        print(f"{tahmin} tahmin hakkınız kaldı. ")
        print(f"uygun harfler:{uygun_harfleri_al(tahmin_edilen_harfler)}")
        harf=input("Bir harf tahmin ediniz: ")
        for i in tahmin_edilen_harfler:
            if i==harf:
                uyarı-=1
                if uyarı<=0:
                   
                    print(f"Oops! Bu harfi zaten tahmin etmiştiniz. Şimdi uyarı hakkınız kalamdığından tahmin hakkınızdan alındı:")
                    
                    break
            
                else:
                     print(f"Oops! Bu harfi zaten tahmin etmiştiniz. Şimdi {uyarı} uyarı hakkınız kaldı:")
                     tahmin+=1
                     break
                break 
            elif TÜRKÇE_ALFABE.count(harf)==0:
                 uyarı-=1
                 print(f"Oops! Bu geçerli bir harf değil. Şimdi {uyarı} uyarı hakkınız kaldı: ")
  
            else:
                tahmin_edilen_harfler+=harf
        
        kelime=tahmin_edilen_kelimeyi_al(gizli_kelime, tahmin_edilen_harfler)
        for i in kelime:
            if i=="_":
                count+=1
        if count>=count2 and sesli_harfler.count(harf)==0 :
            tahmin-=1
            print("Oops! Bu harf benim kelimemde yok: ",' '.join(kelime), end='\n')
        elif count>=count2 and sesli_harfler.count(harf)>0 :
             tahmin-=2
             print("Oops! Bu harf benim kelimemde yok: ",' '.join(kelime), end='\n')

        else:
             print("Güzel tahmin:",' '.join(kelime), end='\n') 
        count2=count 
          
        
      
        if count==0:
             print("Güzel tahmin:",' '.join(kelime), end='\n') 
             print("--------------------------------------")
             print("***** Tebrikler Oyunu Kazandınız *****")
             print("--------------------------------------")
             tahmin+=1
             
             break 
             
        

        
       
        
    else:
       sonuc= kelime_tahmin_edildi_mi(gizli_kelime, tahmin_edilen_harfler)
       if sonuc:
           print("--------------------------------------")
           print("***** Tebrikler Oyunu Kazandınız *****")
           print("--------------------------------------")
           
       else:
            puan=0
            
            for i in set(kelime):
               if i!="_":
                   puan+=1
               
            puan=puan*kelime.count("_")
                 
            print(f" !!! ' {gizli_kelime} ' kelimesini bulamadınız !!! ")
            print(f"----- Puanınız: {puan} ------  ") 
        



# insan_asmaca fonksiyonunuzu tamamladıktan sonra bu dosyanın en altına inin
# ve kodunuzu test etmek için ilk iki yorum satırının yorum işaretlerini kaldırın.
# (ipucu: kendi testinizi yaparken kendi gizli_kelimenizi'ünüzü seçmek 
# isteyebilirsiniz)


# -----------------------------------



def boşluklarla_eşleştir(benim_kelimem, diğer_kelime):
    '''
    benim_kelimem: _ karakterli dize, geçerli gizli_kelime tahmini
    diğer_kelime: dize, normal Türkçe kelime
    döndürdüğü: boolean, eğer benim_kelimem'in tüm gerçek harfleri 
       diğer_kelime'nin karşılık gelen harfleriyle eşleşiyorsa veya 
       harf özel sembol _ ise ve benim_kelimem ve diğer_kelim aynı 
       uzunluktaysa True; aksi takdirde False. 
    '''
    sayac=0
    bosluk_sayısı=benim_kelimem.count("_")
    for i in range(len(benim_kelimem)):
          if len(benim_kelimem)==len(diğer_kelime):
              if benim_kelimem[i]!="_":
                  if benim_kelimem[i]==diğer_kelime[i]:
                      sayac+=1
    if sayac==(len(benim_kelimem)-bosluk_sayısı) :
        return True
    else:
        return False     

        

    




def olası_eşleşmeleri_göster(benim_kelimem):
    '''
    benim_kelimem: _ karakterli dize, geçerli gizli_kelime tahmini
    döndürdüğü: hiçbir şey, ancak kelime listesindeki my_word ile eşleşen her kelimeyi 
             yazdırmalıdır. Ekranda bir harf tahmin edildiğinde, o harfin gizli kelimede 
             geçtiği tüm pozisyonların ortaya çıktığını unutmayın. Bu nedenle, 
             gizli harf (_) zaten açığa çıkmış kelimedeki harflerden biri olamaz.
    '''
    sayac=0
    bosluk=benim_kelimem.count("_")
    for i in range(len(kelime_listesi)):
        if len(benim_kelimem)==len(kelime_listesi[i]):
            for j in range(len(kelime_listesi[i])):
                if benim_kelimem[j]==kelime_listesi[i][j]:

                    print(kelime_listesi[i])
                    
            

                 
                    
                






def ipuçlarıyla_insan_asmaca(gizli_kelime, alfabe=TÜRKÇE_ALFABE):
    '''
    gizli_kelime: dize, kullanıcının tahmin ettiği kelime; 
        tüm harflerin küçük olduğunu varsayar
    
    Etkileşimli bir İnsan Asmaca oyunu başlatır.
    
     * Oyunun başında kullanıcıya gizli_kelime'nin kaç harf içerdiğini 
       ve kaç tahminle başladığını bildirin.
      
     * Kullanıcı 6 tahminle başlamalıdır

     * Her turdan önce kullanıcıya kaç tahmin yaptğını ve henüz tahmin 
       etmediği harfleri göstermelisiniz.
    
     * Kullanıcıdan tur başına bir tahmin yapmasını isteyin. Kullanıcının 
       bir harf yazdığından emin olmayı unutmayın!
    
     * Kullanıcı, tahminlerinin bilgisayarın kelimesinde görünüp görünmediğine 
       dair her tahminden hemen sonra geri bildirim almalıdır.

     * Her tahminden sonra, kullanıcıya o ana kadar kısmen tahmin edilen 
       kelimeyi göstermelisiniz.
     
     * Tahmin, * sembolüyse, kelime listesindeki mevcut tahmin edilen kelimeyle 
       eşleşen tüm kelimeleri yazdırın.
    
    Problem yönergesinde detaylandırılan diğer sınırlamaları takip edin.
    '''
    # alfabedeki harfleri alır
    alfabe = TÜRKÇE_ALFABE
    tahmin=6
    uyarı=3
    kelime=" "
    tahmin_edilen_harfler=" "
    benim_kelimem=" "
    
    
   
    print(gizli_kelime)
    print(f"{len(gizli_kelime)} harfli bir kelime düşünüyorum. ")
    
    count2=len(gizli_kelime)
    while tahmin>0:
        print("*"*50)
        count=0 
        print(f"{tahmin} tahmin hakkınız kaldı. ")
        print(f"uygun harfler:{uygun_harfleri_al(tahmin_edilen_harfler)}")
        harf=input("Bir harf tahmin ediniz (En az bir harf tahmininden sonra kelime tahmini yapabilmek için 1'e basın): ")
        if harf=="*":
             kelime=tahmin_edilen_kelimeyi_al(gizli_kelime, tahmin_edilen_harfler)
             olası_eşleşmeleri_göster(kelime)
        
            
        if harf=="1" :
            diğer_kelime= input("Tahmininizi giriniz: ")
            kelime=tahmin_edilen_kelimeyi_al(gizli_kelime, tahmin_edilen_harfler)
            if (boşluklarla_eşleştir(kelime, diğer_kelime)):
                print("--------------------------------------")
                print("***** Tebrikler Oyunu Kazandınız *****")
                print("--------------------------------------")
                break
            else:
                print("----- Yanlış Tahmin.... -----")

        

            

        for i in tahmin_edilen_harfler:
            if i==harf:
                uyarı-=1
                if uyarı<=0:
                   
                    print(f"Oops! Bu harfi zaten tahmin etmiştiniz. Şimdi uyarı hakkınız kalamdığından tahmin hakkınızdan alındı:")
                    
                    break
                else:
                     print(f"Oops! Bu harfi zaten tahmin etmiştiniz. Şimdi {uyarı} uyarı hakkınız kaldı:")
                     tahmin+=1
                     break
                break 
            elif TÜRKÇE_ALFABE.count(harf)==0:
                uyarı-=1
                print(f"Oops! Bu geçerli bir harf değil. Şimdi {uyarı} uyarı hakkınız kaldı: ")
                break

            else:
                tahmin_edilen_harfler+=harf
        
        kelime=tahmin_edilen_kelimeyi_al(gizli_kelime, tahmin_edilen_harfler)
        for i in kelime:
            if i=="_":
                count+=1
        if count>=count2 and sesli_harfler.count(harf)==0 :
            tahmin-=1
            print("Oops! Bu harf benim kelimemde yok: ",' '.join(kelime), end='\n')
        elif count>=count2 and sesli_harfler.count(harf)>0 :
             tahmin-=2
             print("Oops! Bu harf benim kelimemde yok: ",' '.join(kelime), end='\n')
        
        else:
             print("Güzel tahmin:",' '.join(kelime), end='\n') 
        count2=count 
          
        
      
        if count==0:
             print("Güzel tahmin:",' '.join(kelime), end='\n') 
             print("--------------------------------------")
             print("***** Tebrikler Oyunu Kazandınız *****")
             print("--------------------------------------")
             tahmin+=1
             
             break 
             
        

        
       
        
    else:
       sonuc= kelime_tahmin_edildi_mi(gizli_kelime, tahmin_edilen_harfler)
       if sonuc:
           print("--------------------------------------")
           print("***** Tebrikler Oyunu Kazandınız *****")
           print("--------------------------------------")
           
       else:
            puan=0
            
            for i in set(kelime):
               if i!="_":
                   puan+=1
               
            puan=puan*kelime.count("_")
                 
            print(f" !!! ' {gizli_kelime} ' kelimesini bulamadınız !!! ")
            print(f"----- Puanınız: {puan} ------  ") 
            
          
          


# ipuçlarıyla_insan_asmaca fonksiyonunu tamamladıktan sonra, yukarıdaki
# insan_asmaca fonksiyonundakine benzer şekilde iki yorum satırının yorum
# işaretlerini kaldırıp dosyayı çalıştırarak kodunuzu test edin.
# ipucu: kendi testinizi yaparken kendi gizli_kelimenizi'ünüzü seçmek 
# isteyebilirsiniz


if __name__ == "__main__":
    pass

    # Bölüm 2'yi test etmet için, yukarıdaki "pass" satırına yorum işaretini
    # ekleyin ve aşağıdaki iki satırın yorum işaretlerini kaldırın.
    
    #gizli_kelime = kelime_seç(kelime_listesi)
    
    #insan_asmaca(gizli_kelime, alfabe=TÜRKÇE_ALFABE)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines.
    # Bölüm 3'ü test etmek için yukarıdaki satırlara yeniden yorum işaretlerini
    # ekleyin ve aşağıdaki iki satırın yorum işaretlerini kaldırın.
    
    gizli_kelime = kelime_seç(kelime_listesi)
    ipuçlarıyla_insan_asmaca(gizli_kelime, alfabe=TÜRKÇE_ALFABE)