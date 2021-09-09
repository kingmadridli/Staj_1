# file = open("new file","r",encoding="UTF-8")
# content = file.read()
# print(content)
# file.close()

with open("new file","r",encoding="UTF-8") as file:     # Kod bloklarının sonuna gelince dosya otomatik kapanır.
    content = file.read(10)
    print(content)
    file.seek(0)                                 #  İmleci 0.indexe gönder.
    print(file.tell())                           # İmlecin konum bilgisini gösterir.
    content2 = file.read()
    print(content2)
    print(file.tell())
