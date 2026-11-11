# limite de mémoire du bac (essai à 512M) : l'allocation de 2 Gio doit être arrêtée
b = bytearray(2 * 1024**3)
print("ALLOUE", len(b))
