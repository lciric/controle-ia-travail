# Vérification de l'extrait des états v5 (Sonnet, même contre-lecteur)

**Verdict : non autorisable en l'état** (un seul point, l'essai de m3 ; le code est bon). Autorisable après correction d'un essai, sans autre contre-lecture du code.

Diff v4 -> v5 : docstring ; regex de la ligne de scellement (`^\s*\|\s*SCELLEMENT-`) ; `except ValueError` séparé n'imprimant que le type ; prog argparse. Rien d'autre. Empreintes compagnes OK ; 22 essais passent.

Gardes neuves, suppression dans une copie : 
- M1 (« .. ») : supprimée -> `test_artefacts_scellements[remonte]` rougit. OK.
- m1 (heures égales) : `<=` -> `<` -> `[egales]` rougit. OK.
- m5 (espaces) : retour à `startswith("| SCELLEMENT-")` -> `[espaces]` rougit. OK.
- m3 (valeur illisible) : **l'essai ne tombe pas**. Remplacer `except ValueError` par `except ZeroDivisionError`, ou refondre ValueError dans le premier `except` (qui imprimerait le message), laisse 22/22 verts. Cause : `test_artefact_valeur_illisible_non_imprimee` écrit les octets `\xff\xfeSECRET` dans le fichier APRÈS `sceller` ; `verifier` refuse donc par empreinte discordante (GardeArret, qui n'imprime pas le contenu) avant tout décodage ; la branche ValueError n'est jamais atteinte.

Correction (essai, bloquant pour la clôture de m3) : dans `lectures_jouet` ou l'essai, écrire les octets illisibles puis resceller (par exemple supprimer le `.sha256` compagnon de la lecture du dommage, écrire les octets, `sceller`, et refaire la lecture de la diffusion citant ce nouvel `sha256`) pour que `json.loads`/`read_text` lève `UnicodeDecodeError` ; vérifier ensuite qu'en remplaçant `except ValueError` par `ZeroDivisionError` l'essai rougit (le message de `UnicodeDecodeError` contient l'octet « 0xff », à chercher dans stderr en plus de « SECRET »). Le code de v5 est correct sur ce point.

m2 non corrigé dans le code : accepté (porté à l'ordre de jeu). m4 : docstring conforme.
