import apend_a as ap

bobPrivateKey = ap.cargar_RSAKey_Privada('./bob.key', 'bob')
alicePublicKey = ap.cargar_RSAKey_Publica('./alice_pub.key')

fileAlice = open('./aliceEnc.txt', 'rb')
fileBob = open('./bobEnc.txt', 'rb')

encrypted_text = fileBob.read()
signed_text = fileAlice.read()

rawBobText = ap.descifrarRSA_OAEP(encrypted_text, bobPrivateKey)
rawAliceText = ap.comprobarRSA_PSS('Hola amigos de la seguridad', signed_text, alicePublicKey)

fileAlice.close()
fileBob.close()

print('ALICE')
print(rawAliceText)

print('\n\nBOB')
print(rawBobText)