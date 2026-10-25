# Erratum — « graines de hachage 0, 1 et 2 » (v1, 25 octobre 2026, 13:50 UTC, conv-audit)

- **Ce qui était écrit** : dans le texte scellé `pilote2-gemini-organisme-v5-2-v2.md` (`d2944654…`, § Objet) et dans les
  pièces de vérification des v5.1, v5.2 et v5.2.1, les relevés d'invariance sont dits « identiques pour les graines de
  hachage 0, 1 et 2 ».
- **Ce qui était vrai** : ces relevés ont été produits sous `python -I`, qui implique `-E` et **ignore `PYTHONHASHSEED`** :
  chaque processus a tiré sa propre graine de hachage au hasard (constaté : sous `-I`, deux valeurs différentes de
  `hash("a")` pour `PYTHONHASHSEED` = 0 et 1). Les trois relevés identiques montrent donc l'invariance pour **trois graines
  aléatoires**, non reproductibles, et non pour 0, 1 et 2. Relevé par le sous-agent de reconstitution de la v5.3.
- **Refait à graines fixes** (v5.2.1, objet du pilote) : sous `python -P -s -B` (`-P` retire le dossier courant du chemin
  des modules, sans ignorer les variables d'environnement ; vérifié : `PYTHONHASHSEED=0` donne deux fois la même valeur de
  `hash("a")`), même isolation (`nobody`, réseau coupé, environnement vide), cas B et D pour `PYTHONHASHSEED` = 0, 1, 2 :
  relevés **identiques entre eux et identiques à ceux d'avant** (B `b64ce1fc…`, D `33a4d664…` ; fichiers joints
  `v521-*-h*-graine-fixe.json`). La conclusion tient ; la description est corrigée ici.
- **Ce qui ne change pas** : le texte scellé n'est pas réécrit (R12) ; cet erratum est cité au rapport de lecture du
  pilote. Règle pour la suite : les essais d'invariance tournent sous `-P -s -B`, jamais `-I`, quand une graine de hachage
  doit être fixée.
