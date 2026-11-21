# essai Lean D-1a, v11 (pas 4 de l'arbitrage point 7) : artefact R5 du classement du temps de processeur — l'item sort de
# lui-même en code 137, vite, sans consommer la limite de temps de processeur ; il ne doit pas être classé « délai ».
import os
print("SORTIE 137")
os._exit(137)
