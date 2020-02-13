from Crypto.PublicKey import ECC
from Crypto.Hash import SHA256
from Crypto.Signature import DSS
# Ver https://pycryptodome.readthedocs.io/en/latest/src/public_key/ecc.html
# Ver https://pycryptodome.readthedocs.io/en/latest/src/signature/dsa.html
def crear_ECCKey():
  # Use 'NIST P-256'
  key = ECC.generate(curve='P-256')
  return key

def guardar_ECCKey_Privada(fichero, key, password):
  f = open(fichero + '.pem','wt')
  priv_key = key.export_key(format='PEM', passphare=password, use_pkcs8=True, protection='PBKDF2WithHMAC-SHA1AndAES128-CBC')
  f.write(priv_key)
  f.close()

def cargar_ECCKey_Privada(fichero, password):
  pub_key = open(fichero + '.pem','rt').read()
  key = ECC.import_key(pub_key, passphrase=password)
  return key

def guardar_ECCKey_Publica(fichero, key):
  f = open(fichero + '.pem','wt')
  f.write(key.public_key().export_key(format='PEM'))
  f.close()

def cargar_ECCKey_Publica(fichero):
  f = open(fichero + '.pem','rt')
  key = ECC.import_key(f.read())
  return key

# def cifrarECC_OAEP(cadena, key):
# El cifrado con ECC (ECIES) aun no está implementado
# Por lo tanto, no se puede implementar este método aun en la versión 3.9.0
#return cifrado
# def descifrarECC_OAEP(cifrado, key):
# El cifrado con ECC (ECIES) aun no está implementado
# Por lo tanto, no se puede implementar este método aun en la versión 3.9.0
#return cadena

def firmarECC_PSS(texto, key_private):
  h = SHA256.new(texto)
  signer = DSS.new(key_private, 'fips-186-3')
  signature = signer.sign(h)
  return signature

def comprobarECC_PSS(texto, firma, key_public):
  h = SHA256.new(texto)
  verifier = DSS.new(key_public, 'fips-186-3')
  try:
    verifier.verify(h, firma)
    print("The message is authentic.")
    return True
  except (ValueError, TypeError):
    print("The message is not authentic.")
    return False