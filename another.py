import ecc

aliceKey = ecc.crear_ECCKey()
bobKey = ecc.crear_ECCKey()



ecc.guardar_ECCKey_Privada('alice_private', aliceKey)
ecc.guardar_ECCKey_Publica('alice_public', aliceKey)

alicePrivateKey = ecc.cargar_ECCKey_Privada('alice_private')
alicePublicKey = ecc.cargar_ECCKey_Publica('alice_public')

signed_text = ecc.firmarECC_PSS('Hola amigos de la seguridad', alicePrivateKey)
rawAliceText = ecc.comprobarECC_PSS('Hola amigos de la seguridad', signed_text, alicePublicKey)

print(rawAliceText)