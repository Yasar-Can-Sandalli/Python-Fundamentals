try:
    sayi = int(input("sayı Giriniz : "))
except ValueError:
    print("Tip Uyaşmazlığı lütfen sayı giriniz")
except ZeroDivisionError:
    print("Payda sıfır olamaz")
except (IndexError,InterruptedError):
    print("Index uyuşmazlığı veya ınterrupted sorunu")
except:
    print("Bir Hata oluştu")


#? 0405dc6e3976 ---> Asphalt 9: Legends