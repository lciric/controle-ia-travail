# Vérification des corrections de la garde de `lignee_reconnue` — v2

Même contre-lecteur que la contre-lecture `e76981b9…` (Claude Fable 5.2, `claude-fable-5-2`), 20 novembre 2026. Pièce de travail (vérification courte d'un instrument, classe B). Même mandat (`da74088f…`), mêmes règles.

## Verdict : conforme

Empreintes vérifiées par `sha256sum` : `garde_lignee_reconnue_v2.py` `635e9160…ba76585` ; `essais_garde_lignee_reconnue_v2.py` `ac5871c3…7e6440e`.

## Les couples A et B sont appliqués à la lettre

`diff` du programme v1 / v2 : en-tête et `VERSION` ; `import re` ; `MOTIF_ID = re.compile(r"[A-Za-z0-9._:/-]{1,120}")` sous `AUCUNE` ; la ligne de la lignée du lecteur devenue `not (isinstance(lecture["lignee"], str) and lecture["lignee"] in permis)` (couple A) ; le contrôle de l'identifiant devenu `MOTIF_ID.fullmatch(ident)` (couple B) ; le bloc neuf du mode « liste de veto seule ». Rien d'autre.

`diff` des essais v1 / v2 : en-tête, chemin du programme chargé, cinq essais ajoutés (lignée du lecteur non textuelle sur quatre formes, identifiant en phrase, liste de veto seule saine, fautive, à valeur nulle). Rien d'autre.

Essais v2 rejoués par la commande du mandat : **14 réussis**.

## Le mode « liste de veto seule »

Il ne peut pas laisser passer une valeur fautive en code 0. La liste est remise à `controler` comme le champ `veto` d'une lecture sans carte ; chaque entrée passe donc exactement le contrôle des veto d'une lecture : texte exigé, puis appartenance exacte aux clés de `familles` ou « aucune ». Une valeur nulle, absente, numérique ou mal écrite est refusée (code 1). Une entrée qui n'est pas un objet arrête en « mal formée » (code 2). La lignée prêtée pour l'appel (`sorted(permis)[0]`) est toujours permise et `permis` n'est jamais vide (garanti par `permis_depuis_manifeste`) ; elle n'est pas écrite, et `lignee_du_lecteur` est remis à faux. `nombre_de_refus` et `issue` sont recalculés sur les seuls veto et sur les entrées sans identifiant.

Il n'écrit que des comptes, des identifiants bornés par `MOTIF_ID`, le mot fixe `liste_de_veto` et les champs déjà présents (version, chemins reçus en argument, étiquettes permises du manifeste). Aucune valeur de `lignee_reconnue`, de `prediction` ou de `decision` n'est lue hors du contrôle, ni écrite.

## Réserves mineures, non bloquantes (aucun couple exigé)

- Une liste vide sort « conforme » avec zéro veto : juste, une liste de veto peut être vide.
- Une liste de cartes passée par erreur seule serait prise pour une liste de veto ; ses `lignee_reconnue` restent contrôlées de même, donc rien ne passe à tort.
- Le mode liste et le manifeste mal formé ne sont éprouvés que sur les fonctions, pas sur le code de sortie de `principal` ; le code découle de `issue` par une ligne inchangée.
- Le paragraphe « Ce qu'elle lit » de l'en-tête ne nomme pas la liste nue ; à compléter à la prochaine version, sans effet sur le comportement.
