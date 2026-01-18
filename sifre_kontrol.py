import re

def sifre_kontrol_et(sifre):
    desen=r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
    if re.match(desen, sifre):
        return True
    else:
        return False
    
if __name__ == "__main__":
    kullanici_sifresi=input("Lütfen şifrenizi giriniz: ")
    if sifre_kontrol_et(kullanici_sifresi):
        print("Şifre güçlü")
    else:
        print("Şifre zayıf")

        
    


    
