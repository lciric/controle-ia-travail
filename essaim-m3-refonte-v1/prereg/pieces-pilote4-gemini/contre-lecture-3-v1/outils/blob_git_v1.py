# Empreinte « blob » de git calculée sans git (sha1 de "blob <taille>\0" + contenu) ; lecture seule.
import hashlib, sys
for p in sys.argv[1:]:
    d = open(p, "rb").read()
    print(hashlib.sha1(b"blob %d\0" % len(d) + d).hexdigest(), p)
