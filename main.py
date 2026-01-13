# Toplama fonksiyonu güncellendi
def toplama(x, y):
    return x + y

# Çıkarma fonksiyoni
def cikarma(x, y):
    return x - y

# Çarpma fonksiyonu
def carpma(x, y):
    return x * y

# Bölme fonksiyonu
def bolme(x, y):
    # Bölme sırasında sıfıra bölme hatasına karşı kontrol ekleniyor
    if y != 0:
        return x / y
    else:
        return "Sıfıra bölünemez!"  # Sıfıra bölme hatası mesajı

# Hesap makinesi ana fonksiyonu
def hesap_makinesi():
    # Kullanıcıya işlem seçeneklerini gösteriyoruz
    print("İşlem Seçin:")
    print("1. Toplama")
    print("2. Çıkarma")
    print("3. Çarpma")
    print("4. Bölme")

    # Kullanıcının seçimini alıyoruz
    secim = input("Seçiminizi yapın (1/2/3/4): ")

    # Kullanıcıdan iki sayı girmesini istiyoruz
    num1 = float(input("Birinci sayıyı girin: "))
    num2 = float(input("İkinci sayıyı girin: "))

    # Seçime göre işlem yapıyoruz
    if secim == '1':
        # Toplama işlemi
        print(f"{num1} + {num2} = {toplama(num1, num2)}")
    elif secim == '2':
        # Çıkarma işlemi
        print(f"{num1} - {num2} = {cikarma(num1, num2)}")
    elif secim == '3':
        # Çarpma işlemi
        print(f"{num1} * {num2} = {carpma(num1, num2)}")
    elif secim == '4':
        # Bölme işlemi
        print(f"{num1} / {num2} = {bolme(num1, num2)}")
    else:
        # Geçersiz seçim yapılmışsa hata mesajı veriyoruz
        print("Geçersiz giriş!")

# Hesap makinesi fonksiyonunu çağırarak programı başlatıyoruz
hesap_makinesi()
