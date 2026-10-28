# Brief — vérification de la v5 de la boucle extérieure du pilote 4

De : conv-audit, le 2026-10-26 à 07:10:52 UTC (heure lue sur `date -u` dans la commande qui écrit cette ligne).
À : le vérificateur des v3 et v4 (toi, relancé).

## 1. Ce qui est demandé

`rapport-verification-boucle-exterieure-v5.md` et son compagnon, dans ce dossier
(`/var/tmp/contre-lecture-boucle-exterieure-pilote4-v4/`), au même format que tes rapports précédents, constats
`CLB5-NN`. Vérification ciblée : vise moins de trente minutes.

## 2. Pièces

Dans `fournis/`, à vérifier contre `../EMPREINTES-fournis-v1.txt` (chemins relatifs à `fournis/`) : `v5/` (registre v5,
protocole v4, briefs v4, spécification (B) v3, LISEZMOI v5 avec la table « v4 → v5 ») ; `v4/` (pour la comparaison) ; le
brief v5 (`6026f988…`, décisions E1 à E8) ; ton rapport sur la v4 (`b518f24c…`) ; `carte-v1/` (la carte des facteurs et
les zones, pour E8 seulement) ; le brief du script de lecture v3 et le message qui en corrige le point 2 (libellés (iii)).

## 3. Ce que tu vérifies

1. CLB4-01 à CLB4-07 traités dans les fichiers ; E1 à E8 appliquées telles quelles.
2. La comparaison v4 → v5 (`diff`) : chaque bloc est demandé par un constat ou une décision, ou déclaré au LISEZMOI v5
   (§ 4 et § 6) ; dis pour chaque ajout déclaré s'il tient (champ `identite.lignee_source` ; tenue de la valeur (c) du
   paramètre « famille » ; exemple (a) de G5 changé ; artefacts nouveaux de la spécification, 15 à 19, et de G5, (g) à
   (i)).
3. Les libellés (iii) du registre et des briefs concordent avec le message qui corrige le brief du script.
4. Plus aucun fait de course de M dans le registre.

## 4. Interdits (inchangés)

Rien hors de ce dossier ; aucun score, aucun fichier de course, aucun script ; aucun `git`, réseau, sous-agent ni clé ;
écrire seulement le rapport et son compagnon ; heures lues sur `date -u` dans la commande qui les écrit.

## 5. Fin

Réponse finale en quelques lignes : verdict, constats à corriger avant usage, empreinte du rapport.
