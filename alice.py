import apend_a as ap

alicePrivateKey = ap.cargar_RSAKey_Privada('./alice.key', 'alice')
bobPubliKey = ap.cargar_RSAKey_Publica('./bob_pub.key')

encrypted_text = ap.cifrarRSA_OAEP('Hola amigos de la seguridad', bobPubliKey)
signed_text = ap.firmarRSA_PSS('Hola amigos de la seguridad', alicePrivateKey)

fileAlice = open('./aliceEnc.txt', 'wb')
fileBob = open('./bobEnc.txt', 'wb')

fileAlice.write(signed_text)
fileBob.write(encrypted_text)

fileAlice.close()
fileBob.close()
