import main
import os

while True:
  kullanici_input = input("Dosyanin adi: ")

  if kullanici_input.endswith(".pdf"):
    kullanici_input = kullanici_input.replace(".pdf","")

  if os.path.exists(f'{kullanici_input}.pdf'):
      deneme = main.Hesapla(f'{kullanici_input}.pdf')

      while True:
        print("-"*20)
        print("Not hesaplamak icin 'y'")
        print("Cikmak icin 'q'")
        print("-"*20)
          
        answer = input("Not tekrardan hesaplansin mi? ")

        if answer == "q" or answer == "Q":
          break
        
        elif answer == "y" or answer == "Y":
          deneme.not_hesapla()

        else:
          print("Yanlis input!")
  else:
      print(f"{f'{kullanici_input}.pdf'} mevcut değil.")
