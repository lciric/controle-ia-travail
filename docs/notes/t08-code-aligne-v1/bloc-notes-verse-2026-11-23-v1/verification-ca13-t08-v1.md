# Vérification de CA-13 (d231cc8b)

Lu : diff 360979d1..d231cc8b (entrees_v1, test_t08_entrees_rendu_v1). Rejoué : `-k amorce` : 5 passés. Mêmes interdits.

CA-13 vérifié : découpe sur NUL seule, `lstrip("\n")` par entrée ; l'essai neuf (dossier à saut de ligne, blob dédoublé) est probant (mon cas d'essai précédent est de même forme).

Point à juger : un nom de chemin qui commence par un saut de ligne perd ce caractère. **Acceptable, et dans le sens sûr** : le retrait ne peut que rapprocher le chemin de sa forme normale. Exemple : `\n<run>/resume.json` à la racine, non reconnu tel quel, devient `<run>/resume.json` et est arrêté. Le seul effet possible est un arrêt en plus sur un chemin à la racine dont le dossier est l'identifiant de 7b, ce qui est voulu. Aucun chemin interdit ne peut échapper par ce retrait. À mentionner d'une phrase dans le rapport.

## Verdict : **vérifié** ; plus aucun constat ouvert sur la garde de l'instance (CA-12 reste à inscrire au rapport).
