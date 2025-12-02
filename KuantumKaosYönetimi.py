from abc import ABC, abstractmethod
import random
import sys

class KuantumCokusuException(Exception):
    pass

class KuantumNesnesi(ABC):
    def __init__(self,ID,tehlike_seviyesi):
        self._id = ID
        self._stabilite = 100
        self._tehlike_seviyesi = tehlike_seviyesi
 
    @property
    def stabilite(self):
        return self._stabilite

    @stabilite.setter
    def stabilite(self,value):
        if value < 0:
            self._stabilite = 0
        elif value > 100:
            self._stabilite = 100
        else:
            self._stabilite = value

    @property
    def id(self):
        return self._id

    @abstractmethod
    def analizEt(self):
        pass

    def durumBilgisi(self):
        return f"[{self._id}] Stabilite : {self._stabilite}"


class IKritik:
    def acilDurumSogutmasi(self):
        raise NotImplementedError

class VeriPaketi(KuantumNesnesi):
    def __init__(self,ID):
        super().__init__(ID,1)
    
    def analizEt(self):
        self.stabilite -= 5
        print("Veri içeriği okundu")
        if self.stabilite < 0:
            raise KuantumCokusuException(f"Çöken Nesne: {self.id}")

class KaranlikMadde(KuantumNesnesi,IKritik):
    def __init__(self,ID):
        super().__init__(ID,7)    

    def analizEt(self):
        self.stabilite -= 15
        if self.stabilite <= 0:
            raise KuantumCokusuException(f"Çöken Nesne: {self.id}")

    def acilDurumSogutmasi(self):
        self.stabilite += 50


class AntiMadde(KuantumNesnesi,IKritik):
    def __init__(self,ID):
        super().__init__(ID,10)

    def analizEt(self):
        self.stabilite -= 25
        if self.stabilite <= 0:
            raise KuantumCokusuException(f"Çöken nesne : {self.id}")

    def acilDurumSogutmasi(self):
        self.stabilite += 50

envanter = []

def yeni_nesne_olustur():
    ID = f"{random.randint(100000, 999999):x}"[-6:]   # rastgele id
    nesne_turu = random.randint(0, 2)
    if nesne_turu == 0:
        nesne = VeriPaketi(ID)
    elif nesne_turu == 1:
        nesne = KaranlikMadde(ID)
    else:
        nesne = AntiMadde(ID)

    envanter.append(nesne)
    print(f"Nesne oluşturuldu: {ID}")


def envanter_listele():
    if len(envanter) == 0:
        print("Envanter boş.")
    else:
        for n in envanter:
            print(n.durumBilgisi())


def analiz_yap():
    ID = input("ID: ")
    for n in envanter:
        if n.id == ID:
            n.analizEt()
            print("Yeni stabilite:", n.stabilite)
            return
    print("Nesne bulunamadı!")


def sogutma_yap():
    ID = input("ID: ")
    for n in envanter:
        if n.id == ID:
            if isinstance(n, IKritik):
                n.acilDurumSogutmasi()
                print("Soğutma uygulandı. Yeni stabilite:", n.stabilite)
            else:
                print("Bu nesne soğutulamaz!")
            return
    print("Nesne bulunamadı!")


# ------------------- Main Loop -------------------
while True:
    try:
        print("\nKUANTUM AMBARI KONTROL PANELİ")
        print("1) Yeni Nesne Ekle")
        print("2) Envanteri Listele")
        print("3) Nesneyi Analiz Et")
        print("4) Acil Durum Soğutması")
        print("5) Çıkış")
        secim = input("Seçiminiz: ")

        if secim == "1":
            yeni_nesne_olustur()
        elif secim == "2":
            envanter_listele()
        elif secim == "3":
            analiz_yap()
        elif secim == "4":
            sogutma_yap()
        elif secim == "5":
            sys.exit()
        else:
            print("Hatalı seçim!")

    except KuantumCokusuException as e:
        print("\n!!! SİSTEM ÇÖKTÜ! TAHLİYE BAŞLATILIYOR !!!")
        print(e)
        sys.exit()
