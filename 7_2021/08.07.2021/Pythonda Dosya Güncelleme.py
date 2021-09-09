# with open("new file","r+",encoding="UTF-8") as file:
#     file.seek(20)
#                                                             # r+ hem okuma hem de yazma modunu temsil eder.
#     print(file.write("Deneme"))
#                                                                 # Dosyayı w ile açsak önce mevcut veriyi silerdi.
#
# with open("new file","r+",encoding="UTF-8") as file:
#     print(file.read())


# region Sayfa Sonunda Güncelleme
# with open("new file","a",encoding="UTF-8") as file:
#     file.write("\nUtku Tunçbayn")
#
# with open("new file","r",encoding="UTF-8") as file:
#     print(file.read())
# endregion


# region Sayfa Başında Güncelleme
# with open("new file", "r+", encoding="UTF-8") as file:
#     content = file.read()
#     content = "Destan Taşdan\n" + content
#     file.seek(0)
#     file.write(content)
#
# with open("new file", "r", encoding="UTF-8") as file:
#     print(file.read())
# endregion


# region Sayfa Ortasında Güncelleme
# with open("new file","r+",encoding="UTF-8") as file:
#     liste  = file.readlines()
#     liste.insert(1,"Yirmibeş Yazılım\n")             #1. indexten önce ekleme işlemi yapar
#     file.seek(0)
#     file.writelines(liste)
# with open("new file","r",encoding="UTF-8") as file:
#     print(file.read())
# endregion













