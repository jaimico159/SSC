import apend_a as ap

keyAlice = ap.crear_RSAKey()
keyBob = ap.crear_RSAKey()

ap.guardar_RSAKey_Privada('./alice.key', keyAlice, 'alice')
ap.guardar_RSAKey_Privada('./bob.key', keyBob, 'bob')
ap.guardar_RSAKey_Publica('./alice_pub.key', keyAlice)
ap.guardar_RSAKey_Publica('./bob_pub.key', keyBob)

print(keyAlice)
print(keyBob)