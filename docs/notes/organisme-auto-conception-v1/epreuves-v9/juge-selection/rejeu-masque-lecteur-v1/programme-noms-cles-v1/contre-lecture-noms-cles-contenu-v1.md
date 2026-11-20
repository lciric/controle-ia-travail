# Contre-lecture — programme des noms de clés de `contenu` — v1

Contre-lecteur neuf, modèle S. Mandat `mandat-contre-lecteur-noms-cles-contenu-v1.md` (e91dfccd…, compagnon vérifié OK avant tout autre geste).
Python 3.13.18. Aucun geste sur le vrai fichier des cartes ni sous `archives-reponses-modeles/`. Aucune écriture dans le dépôt.

## Verdict : Conforme

Le programme est conforme pour son jeu unique, sans correction de son code. Deux corrections portent sur la **commande de jeu** du rapport du développeur (nos 1 et 2 ci-dessous) ; trois remarques sans effet sur la conformité.

## Empreintes vérifiées (compagnon, `sha256sum -c`, OK) et recalculée

- `noms_cles_contenu_hors_champs_v1.py` 26eeaa798e14c716bbe4bd0c323e797e60470459d9a13b804ccacb07ea121120 ; essais a3089f6b… ; rapport fe8a8651… ; mandat du développeur df0df0c2… ; masque 07ed87256ba6f2ca510dfd462733190566343ed09e485cb1b638e0314780823e ; compte rendu du refus : compagnon OK.
- Configuration A tirée de `origin/main` par redirection du shell (hors du dépôt) : 8a8548d1444bfe3ab85396b3913c2d1b018a32541e9a283bd3f9b517a6332ce4 = constante gelée du programme. Sa forme : dix champs, `hors_choix` vide. Empreinte gelée des cartes ba65c411… = celle du compte rendu du refus.

## 1. Chemin des champs et des clés (comparé ligne à ligne au masque)

Conforme. `valider_configuration` : même texte, mêmes motifs (l'essai le compare au masque scellé sur onze configurations). Champs = `configuration["champs"]` ; cartes parcourues dans l'ordre des octets de l'identifiant ; carte de `hors_choix` non ouverte ; mêmes refus « sans `contenu` » et « `contenu` pas un objet » ; seul accès `fiches[ident]["contenu"]`, et `set(contenu) - set(champs)` est exactement l'expression du masque. Le refus réel « (1) » correspond à un nom sur la première carte fautive ; le programme rend l'union des noms de toutes les cartes ouvertes, qui contient ce nom (preuve par essai sur forme synthétique ; sur les vraies cartes la liste peut avoir plus d'un nom si d'autres cartes en portent d'autres : c'est le but, pas un écart).
Mutation du chemin (clés de `rec` au lieu de `contenu`) : attrapée (6 essais échouent).

## 2. Empreintes, ordre, fuites

Conforme. Octets lus, empreintes comparées (configuration, puis cartes) avant tout décodage ; configuration décodée et validée avant les cartes ; décodage : message d'erreur non rapporté ; erreur imprévue : seul le type de l'exception sort ; identifiants et valeurs ne servent qu'en mémoire (tri, test d'appartenance à `hors_choix`), jamais écrits ni affichés ; aucun motif de refus ne porte de nom ni de chemin. Lancement en ligne de commande : seules les constantes gelées ; essayé sur la vraie configuration A et un fichier de cartes synthétique : « REFUS : fiches : empreinte différente de l'empreinte gelée », code 2, rien écrit.

## 3. Sortie

Conforme. Trois champs exactement (`cles_hors_champs`, `nombre_de_cartes`, `empreintes`), postcondition avant écriture, écriture exclusive de la sortie puis du compagnon, refus (avant toute lecture) si la sortie ou le compagnon existe, ou si le dossier est absent. Garde : plus de 64 caractères ou saut de ligne (au sens de `splitlines`) remplacé par « (nom non rapporté : longueur L) », compte gardé ; JSON en ASCII. Remarque : un nom de 64 caractères au plus et sans saut de ligne reste écrit tel quel ; c'est la garde demandée, pas plus.

## 4. Les huit écarts du rapport

1. Empreintes avant tout décodage, au sens fort : admis (plus strict que le masque).
2. `nombre_de_cartes` = cartes ouvertes, cartes hors du choix non comptées : admis, identique au masque ; sans objet au jeu (`hors_choix` vide dans la configuration A).
3. Refus si aucune carte ouverte : admis ; le masque refuse aussi (« aucune carte à masquer »).
4. Saut de ligne au sens de `splitlines` ; deux noms longs de même longueur gardent deux entrées : admis.
5. JSON échappé en ASCII : admis (exact une fois décodé).
6. Message d'erreur imprévue non rapporté : admis.
7. Contrôles non reproduits (carte « hors du choix » inconnue, champ absent, champ non texte) : admis ; ils lisent des types de valeurs ou compareraient des identifiants, hors du chemin des noms. Conséquence assumée : le programme peut réussir là où le masque refuserait pour une autre cause ; il ne peut pas refuser à tort.
8. Configuration A absente du disque : levée, elle se tire de `origin/main` (voir 6).

## 5. Essais et mutations

Sur copies, dans mon dossier : 39 passés, 0 échoué (`env -C …/copie python3 -B -m pytest -q -p no:cacheprovider essais_noms_cles_contenu_hors_champs_v1.py`).
Mutations à la main (une par copie) :
- chemin des clés (`set(rec)` au lieu de `set(contenu)`) : attrapée, 6 échecs ;
- valeur dans la sortie (le nom suivi des 12 premiers caractères de la valeur) : attrapée, 4 échecs ;
- décodage strict avant l'empreinte (dans la lecture des octets) : attrapée, 1 échec ;
- décodage **sans erreur possible** avant l'empreinte (`errors="replace"`) : **non attrapée** (39 passés). Aucun essai ne peut la voir de l'extérieur ; la lecture du code (`lire_octets_verifies`, `executer`) montre l'absence de tout décodage avant la comparaison. Limite des essais, non un défaut du programme ;
- empreinte des cartes non comparée : attrapée, 2 échecs ;
- configuration décodée avant l'empreinte des cartes : attrapée, 2 échecs.

## 6. Corrections

1. **Commande de jeu du rapport à corriger** : elle écrit la sortie **dans le dépôt** (`docs/notes/…`) et donne la configuration par un chemin du dépôt où elle n'est pas sur disque ; le mandat veut la configuration tirée de `origin/main` et la sortie hors du dépôt. Commande corrigée donnée ci-dessous.
2. **Programme appelé depuis son dossier de rendu** (`PROG`, dans le dépôt, avec son compagnon) plutôt que depuis le bloc-notes du développeur, qui peut être vidé ; vérifier son empreinte juste avant.
3. Remarque : si la sortie ou le compagnon est créé à moitié (disque plein), il reste un fichier seul ; le programme refuse ensuite de le remplacer. Négligeable, à signaler seulement.

## 7. Commande unique de jeu, à donner à l'agent du jeu

Notations : `DEPOT` = `/home/user/controle-ia-travail` ; `PROG` = `/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/juge-selection/rejeu-masque-lecteur-v1/programme-noms-cles-v1` ; `JEU` = un dossier neuf de son bloc-notes ; `CARTES` = le chemin complet du fichier des cartes (connu de la mère seule ; ba65c411…).

Gestes préparatoires, un par appel :
1. `env -C PROG sha256sum -c noms_cles_contenu_hors_champs_v1.py.sha256` (attendu : OK, 26eeaa79…).
2. `env -C DEPOT git show origin/main:prereg/organisme-auto-conception-v9/juge-selection/rejeu-v1/configuration-a-masque-v1.json > JEU/configuration-a-masque-v1.json` (redirection du shell ; jamais l'option de sortie de git).
3. `env -C JEU sha256sum configuration-a-masque-v1.json` (attendu : 8a8548d1444bfe3ab85396b3913c2d1b018a32541e9a283bd3f9b517a6332ce4).

Commande unique de jeu :

```
python3 -B PROG/noms_cles_contenu_hors_champs_v1.py --fiches CARTES --configuration JEU/configuration-a-masque-v1.json --sortie JEU/noms-cles-contenu-hors-champs-v1.json
```

Attendu : « FAIT » et code 0, ou « REFUS : … » et code 2 sans sortie. Aucune relance en cas de refus ; ouvrir la sortie seulement après `env -C JEU sha256sum -c noms-cles-contenu-hors-champs-v1.json.sha256`.

— contre-lecteur, modèle S
