# Artefacts d'essai du contrôle v2 — jamais à servir

Les fichiers `A1-…`, `A2-…`, `A3-…`, `A6-…`, `A7-…` et `A8-…` de ce dossier sont des **copies altérées** de la banque
`confrontation-v3` (fuites injectées, ordre rangé par vérité, texte modifié, identifiant en double, clé fausse),
construites par `../essais_controle_v2_v1.py` pour essayer le contrôle `../verifier_identifiants_opaques_v2.py`. Leurs
compagnons `.sha256` ne valent qu'empreinte de fichier : **aucun de ces fichiers n'est une banque, ni à servir, ni à
citer comme telle** ; un lanceur épingle l'empreinte de la banque qu'il sert (`157a2b45…` pour la v3) et refuse toute
autre (LISEZMOI-v6 de la banque, § 1, BC2-02). La « clé fausse » de A8 est tirée au hasard, sans lien avec la clé.
