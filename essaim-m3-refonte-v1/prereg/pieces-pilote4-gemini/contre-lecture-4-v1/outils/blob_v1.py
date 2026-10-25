"""Empreinte « blob » (comme git hash-object) d'un fichier, sans git ; lecture seule."""
import hashlib, pathlib, sys
for p in sys.argv[1:]:
    b = pathlib.Path(p).read_bytes()
    print(hashlib.sha1(b"blob %d\0" % len(b) + b).hexdigest(), p)
