def response_fb(self, action1):
    with open("Oyuncular.txt", "r", encoding="utf-8") as file:
        for satir in file:
            satir = satir.strip()
            liste = satir.split(",")
            isim = liste[0]
            mevki = liste[1]
            yas = liste[2]
            takim = liste[3]
            if action1.text() == "Kaleci" and
                print(satir)
            elif action1.text() == "Defans" and mevki == "Defans" and takim == "Fenerbahçe":
                print(satir)
            elif action1.text() == "Orta Saha" and mevki == "Orta Saha" and takim == "Fenerbahçe":
                print(satir)
            elif action1.text() == "Forvet" and mevki == "Forvet" and takim == "Fenerbahçe":
                print(satir)

def response_kaleci(self):
    with open("Oyuncular.txt", "r", encoding="utf-8") as file:
        for satir in file:
            satir = satir.strip()
            liste = satir.split(",")
            isim = liste[0]
            mevki = liste[1]
            yas = liste[2]
            takim = liste[3]
            if mevki == "Kaleci" and takim == "Fenerbahçe":
                print(satir)
            elif mevki == "Kaleci" and takim == "Galatasaray":
                print(satir)