import pandas as pd
from PyPDF2 import PdfReader

class Hesapla:
  array = []
  
  dersKodu = []
  dersAdi = []
  dersKredi = []
  dersHarf = []
  dersNotu = []
  dersType = []
  
  def __init__(self,text):
    pdfReader = PdfReader(text)
    ceviri_tablosu = str.maketrans('üçğşıöÜÇĞŞİÖ', 'ucgsioUCGSIO')

    for i in range(len(pdfReader.pages)):
      with open('pdf.txt', 'a+') as file:
        file.write(pdfReader.pages[i].extract_text().translate(ceviri_tablosu))


    self.file = open("pdf.txt", 'a+')
    self.okuma()
    self.ayirma()
    self.not_hesapla()

  def __del__(self):
    self.file.close()

  def okuma(self):
    self.file.seek(0)

    while True:

      line = self.file.readline()
      kosul = line.strip()

      if kosul.startswith("BIM449"):
        nextline = self.file.readline()
        line = line.strip() + " " + nextline
      
        self.array.append(line)
        pass

      if kosul.endswith(" Z") or kosul.endswith(" S") or kosul.endswith(" MS"):
          self.array.append(line)

      if not line:
        break

  def ayirma(self):
    
    for eleman in self.array:
      if eleman.count("(Ing)") == 1:
        dil = "(Ing)"
      elif eleman.count("(Fra)") == 1:
        dil = "(Fra)"
      elif eleman.count("(Tur)") == 1:
        dil = "(Tur)"
      elif eleman.count("(Alm)") == 1:
        dil = "(Alm)"
      elif eleman.count("(Isp)") == 1:
        dil = "(Isp)"


      self.dersKodu.append(eleman[:6])

      index = eleman.index(dil) + 5
      self.dersAdi.append(eleman[7:index])

      self.dersKredi.append(float(eleman[index:index+4]))

      self.dersHarf.append(eleman[index+4:index+7].strip())

      self.dersNotu.append(float(eleman[index+8:index+13]))

      self.dersType.append(eleman[-2])

    dataFrame = pd.DataFrame({"Ders Kodu": self.dersKodu, "Ders Adi": self.dersAdi, "Kredi": self.dersKredi, "Harf Notu": self.dersHarf, "Puan": self.dersNotu, "Type": self.dersType})

    dataFrame.to_excel("dersler.xlsx", index=False)

  def not_hesapla(self):
    df = pd.read_excel("dersler.xlsx")

    toplamKredi = 0
    toplamNot = 0

    for i in range(len(df)):
        harfNotu = df["Harf Notu"][i]

        if harfNotu == "AA":
          carpan = 4.00
        elif harfNotu == "AB":
          carpan = 3.70
        elif harfNotu == "BA":
          carpan = 3.30
        elif harfNotu == "BB":
          carpan = 3.00
        elif harfNotu == "BC":
          carpan = 2.70
        elif harfNotu == "CB":
          carpan = 2.30
        elif harfNotu == "CC":
          carpan = 2.00
        elif harfNotu == "CD":
          carpan = 1.70
        elif harfNotu == "DC":
          carpan = 1.30
        elif harfNotu == "DD":
          carpan = 1.00
        elif harfNotu == "FF":
          carpan = 0.00

        krediNotu = df["Kredi"][i]

        toplamKredi = toplamKredi + krediNotu
        toplamNot = toplamNot + krediNotu*carpan

    sonuc = round(toplamNot/toplamKredi,2)

    print(f'Not Ortalamasi: {sonuc}')
    print(f'Toplam Kredi: {toplamKredi}')