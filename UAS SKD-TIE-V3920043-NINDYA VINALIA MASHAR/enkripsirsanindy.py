from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import zlib
import base64


def encrypt_blob(blob, kunci_publik):
    rsa_key = RSA.importKey(kunci_publik)
    rsa_key = PKCS1_OAEP.new(rsa_key)

    blob = zlib.compress(blob)

    chunk_size = 470
    offset = 0
    mengakhiri_loop = False
    enkripsi = bytearray()

    while not mengakhiri_loop:
        chunk = blob[offset:offset + chunk_size]

        if len(chunk) % chunk_size != 0:
            mengakhiri_loop = True
            chunk += bytes(chunk_size - len(chunk))

        enkripsi += rsa_key.encrypt(chunk)

        offset += chunk_size

    return base64.b64encode(enkripsi)


fd = open("kunci_publik.pem", "rb")
kunci_publik = fd.read()
fd.close()

fd = open("nindy.jpeg", "rb")
tidakterenkrpsi_blob = fd.read()
fd.close()

enkripsi_blob = encrypt_blob(tidakterenkrpsi_blob, kunci_publik)

fd = open("hasil_enkripsi.jpg", "wb")
fd.write(enkripsi_blob)
fd.close()
