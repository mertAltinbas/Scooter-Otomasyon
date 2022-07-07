"""
    Heryerde kullanılan elektrikli scooterlar (binbin, martı, vs.) araçlar için otomasyon.

    Proje Dağılımı
        1- Kullanıcı kayıt bölümü ve giriş bölümü
        2- Kullanıcı kart bilgileri giriş bölümü
        3- Sürüş zamanına göre ödenecek tutarı gösteren bölüm
        4- Veritabanı ile kullanıcının sürüş istatistiklerini tutulduğu bölüm. (geliştirme aşamasında)
"""
import json
import os

class User():
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

class Program():
    def __init__(self):
        self.users = []
        self.isLoggedIn = False
        self.currentUser = {}

        # load user from .json
        self.loadUsers()

    def register(self, user: User):
        self.users.append(user)
        self.savetoFile()
        print('Kullanıcı Oluşturuldu')
    
    def login(self, username, password):
        for user in self.users:
            if user.username == username and user.password == password:
                self.isLoggedIn = True
                self.currentUser = user
                print('Giriş Başarılı')
                break

    def logout(self):
        self.isLoggedIn = False
        self.currentUser = {}
        print('Çıkış Yapıldı')

    def identity(self):
        if self.isLoggedIn:
            print(f"Açık olan kullanıcı: {self.currentUser.username}")
        else:
            print('Giriş yapılmadı!!')

    def payment(self, cardnumber, last, cvv):
        pass

    def tutar(self):
        pass

    def loadUsers(self):
        if os.path.exists('users.json'):
            with open('users.json', 'r', encoding='utf-8') as file:
                users = json.load(file)
                for user in users:
                    user = json.loads(user)
                    newUser = User(username=user['username'], password=user['password'], email=user['email'])
                    self.users.append(newUser)

    def savetoFile(self):
        list = []

        for user in self.users:
            # user class to dict
            list.append(json.dumps(user.__dict__))

        with open('users.json', 'w') as file:
            json.dump(list, file)

kullanici = Program()

while True:
    print(' Menü '.center(10, '*'))
    secim = int(input('1- Register\n2- Login\n3- Logout\n4- Identity\n5- Payment\n6- Tutar\n7- Exit\n Seçiminiz: '))

    if secim == 7:
        print('Çıkış yapılıyor...')
        break
    else:
        if secim == 1:
            username = input('Username: ')
            password = input('Password: ')
            email = input('E-Mail: ')

            user = User(username = username, password = password, email=email)
            kullanici.register(user)

        elif secim == 2:
            if kullanici.isLoggedIn:
                print('Zaten Giriş Yapılmıştır.')
            else:
                username = input('Username: ')
                password = input('Password: ')
                kullanici.login(username, password)

        elif secim == 3:
            kullanici.logout()

        elif secim == 4:
            kullanici.identity()

        elif secim == 5:
            pass # payment

        elif secim == 6:
            pass # Tutar

