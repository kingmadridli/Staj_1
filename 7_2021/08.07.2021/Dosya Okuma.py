# try:
#     file = open("new file2","r")
#     print(file)
# except (FileNotFoundError,NameError):
#     print("Dosya okuma hatası")
# finally:
#     try:
#         print("Dosya kapandı")
#     except NameError:
#         file.close()

# file = open("new file","r",encoding="UTF-8")
# for i in file:
#     print(i,end="")    #Boş satır eklemeden alt alta yazılır
# file.close()

# file = open("new file","r",encoding="UTF-8")
# content1 = file.read()
# print("İçerik-1")
# print(content1)
#
# content2 = file.read()
# print("içerik-2")
# print(content2)
# file.close()




# file = open("new file","r",encoding="UTF-8")
#
# content1 = file.read(5)   # 5 karakter okudu ve imleç artık orada
# content1 = file.read(3)   # 3 karakter daha okudu ve imleç artık orada
#
#
# print(content1)
#


# file = open("new file","r",encoding="UTF-8")
# print(file.readline(),end="")
# print(file.readline(),end="")
# print(file.readline(),end="")
# file.close()

# file = open("new file","r",encoding="UTF-8")
# liste = file.readlines()
# print(liste)
















