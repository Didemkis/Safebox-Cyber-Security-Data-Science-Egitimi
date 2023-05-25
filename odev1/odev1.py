def giris():
    username =input("Kullanıcı adı girin: ")
    password = input("Şifreyi girin:")
    with open('kullanıcıBilgileri.txt') as f:
        lines = f.readlines()
    if(username in lines ) and (password in lines):
        print("Giriş yapıldı!")
    else:
        print("Kullanıcı bulunamadı!")