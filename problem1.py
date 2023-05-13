""" 1'den 1000'e kadar olan asal sayıları ekrana yazdıran bir program yazın. Daha sonra bir tane decorator fonksiyon kullanarak bu fonksiyona 1'den 1000'e kadar
olan mükemmel sayıları yazdırma özelliği ekleyin. """

def mükemmel_sayılar(fonk):
    def wrapper():
        print("Mükemmel Sayılar...")
        for i in range(2,1001):
            toplam = 0
            for x in range(1,i):
                if i%x == 0:
                    toplam += x

            if toplam == i:
                print(i)
        fonk()
    return wrapper



@mükemmel_sayılar
def asal_sayılar():
    print("Asal Sayılar...")
    for i in range(2,1001):
        sayaç = 0
        for x in range(2,i):
            if i%x == 0:
             sayaç +=1
             break

        if sayaç != 1 :
            print(i)

asal_sayılar()