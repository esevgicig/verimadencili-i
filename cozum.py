import re

def verileri_temizle(kaynak_dosya, hedef_dosya):
    try:
        with open(kaynak_dosya, 'r', encoding='utf-8') as dosya:
            icerik = dosya.read()

        email_deseni = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        telefon_deseni = r'\d{10,13}'

        emailler = re.findall(email_deseni, icerik)
        telefonlar = re.findall(telefon_deseni, icerik)

        with open(hedef_dosya, 'w', encoding='utf-8') as yeni_dosya:
            for mail in emailler:
                yeni_dosya.write(mail + '\n')
            for tel in telefonlar:
                yeni_dosya.write(tel + '\n')
        
        print(f"Başarılı: {hedef_dosya} oluşturuldu.")

    except FileNotFoundError:
        print(f"Hata: {kaynak_dosya} dosyası bulunamadı!")
    except Exception as e:
        print(f"Hata oluştu: {e}")

verileri_temizle('lvl1_bozuk_veri.txt', 'lvl1_temiz_rehber.txt')
verileri_temizle('lvl2_bozuk_veri.txt', 'lvl2_temiz_rehber.txt')
