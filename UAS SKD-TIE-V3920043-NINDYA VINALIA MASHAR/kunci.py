from Crypto.PublicKey import RSA

kunci_baru = RSA.generate(4096, e=65537)

kunci_private = kunci_baru.exportKey("PEM")

kunci_publik = kunci_baru.publickey().exportKey("PEM")

print(kunci_private)
fd = open("kunci_private.pem", "wb")
fd.write(kunci_private)
fd.close()

print(kunci_publik)
fd = open("kunci_publik.pem", "wb")
fd.write(kunci_publik)
fd.close()
