import random

fjdgn = "qwertyuiopasdfghjklzxcvbnm"
adfhdfs = "1234567890"
ohkogf = "!@#$%^&*"

ighjnfnh = fjdgn + fjdgn.upper() + adfhdfs + ohkogf

jfdijgidj = int(input("de cuantos caracteres quieres tu contrasena?: "))

ofigfg = ""
for i in range(jfdijgidj):
    ofigfg += random.choice(ighjnfnh)

print("tu nueva contrasena es:", ofigfg)

