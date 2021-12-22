from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64
import zlib


def decrypt_blob(enkrpsi_blob, kunci_private):

    rsa_key = RSA.importKey(kunci_private)
    rsa_key = PKCS1_OAEP.new(rsa_key)

    enkrpsi_blob = base64.b64decode(enkrpsi_blob)

    chunk_size = 512
    offset = 0
    dekripsi = bytearray()

    while offset < len(enkrpsi_blob):
        chunk = enkrpsi_blob[offset: offset + chunk_size]

        dekripsi += rsa_key.decrypt(chunk)

        offset += chunk_size

    return zlib.decompress(dekripsi)


fd = open("kunci_private.pem", "rb")
kunci_private = fd.read()
fd.close()

fd = open("hasil_enkripsi.jpg", "rb")
enkrpsi_blob = fd.read()
fd.close()

fd = open("hasil_dekripsi.jpg", "wb")
fd.write(decrypt_blob(enkrpsi_blob, kunci_private))
fd.close()
