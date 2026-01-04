import re

sifre=input("Lütfen şifrenizi giriniz: ")

desen=r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'

if re.match(desen, sifre):
    print("şifre güçlü")

else:
    print("şifre zayıf")
    


    
