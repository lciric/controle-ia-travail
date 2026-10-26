# Brief — contre-lecture de la carte des facteurs et des zones interdites de la v6.2.1 — v1

De : conv-audit, le 2026-10-26 à 06:48:06 UTC (heure lue sur `date -u` dans la commande qui écrit cette ligne).
À : un sous-agent neuf de la lignée conv-audit. Tu n'as écrit ni l'objet, ni la carte, ni la boucle extérieure.

## 1. Le contexte

La boucle extérieure du pilote 4 peut corriger l'objet, la v6.2.1, un facteur à la fois. Un script de contrôle (la garde
G5) refusera toute correction hors du facteur déclaré ou dans une zone interdite. Il lit deux cartes écrites depuis le
code par un sous-agent : `carte-facteurs-v1` (16 facteurs) et `zones-interdites-v1` (11 zones). Une erreur de ces cartes
laisserait passer une correction qui touche la règle qui choisit une classe, ou qui change deux leviers à la fois. Tu les
attaques.

## 2. Pièces

Dans `fournis/`, à vérifier contre `../EMPREINTES-fournis-v1.txt` (chemins relatifs à `fournis/`) :

- `objet-v6-2-1/organisme/` : le code de l'objet (26 fichiers, commit `7ea3270`, empreinte d'arbre `4f13647a…`
  vérifiée par conv-audit avec la fonction du noyau).
- `carte-v1/` : les cinq pièces de la carte (deux Markdown, deux JSON, le LISEZMOI avec ses doutes D1 à D14 et ses
  errata).
- `LISEZMOI-brief-carte-facteurs-v1.md` : le brief de l'auteur de la carte.
- `protocole-boucle-exterieure-pilote4-v3.md` : § 6 (un facteur à la fois) et § 14 (ce que le correcteur peut changer ;
  zones interdites ; ce qu'il n'écrit jamais).
- `pilote4-gemini-organisme-v4.md` : section « Objet de la première course : la v6.2.1 ».
- `noyau-8e5e2f7b/` : le noyau qui fait tourner l'objet, pour la question D5 (numérotation des rondes de conception).

Décisions déjà prises par conv-audit, à ne pas rediscuter : G5 lira la carte au niveau des colonnes (par segments) ; le
gel de `seuil_confiance_caste1` (zone Z03) est confirmé ; `VERSION` (`principal.py` l. 27) entre dans les fichiers
d'accompagnement.

## 3. Ce que tu vérifies

1. **Exactitude** : pour au moins un tiers des entrées de la carte et des zones, choisies par toi (dis lesquelles et
   comment), refais toi-même la localisation dans le code (fichier, fonction, lignes, colonnes des segments) et compare.
   Les JSON et les Markdown disent la même chose.
2. **Disjonction** : aucune ligne ni aucun segment dans deux facteurs ; facteurs et zones disjoints (vérifie-le par un
   calcul sur les JSON, avec `python3 -I`).
3. **Couverture des zones** : cherche dans tout le code, par toi-même, chaque endroit qui (a) construit un texte d'appel
   servi à un modèle pour une tâche, (b) analyse une réponse de modèle d'une manière qui fixe une classe, (c) porte ou lit
   des constantes de mots-clés, (d) route une tâche vers une règle de classe. Chacun doit être dans une zone, ou
   l'absence doit être justifiée. Un seul endroit oublié est un constat bloquant.
4. **Frontière R/E** de l'exception « défaut du chemin des réponses » : chaque ligne classée E (format, analyse, délai)
   ne change-t-elle vraiment pas la règle qui choisit une classe ?
5. **Facteurs** : aucun facteur ne contient de ligne qui intervient dans le choix d'une classe ; les facteurs ajoutés
   (F10 à F16) sont-ils de vrais leviers distincts ; F03 (les deux seuils du critère de fin en un seul facteur) est-il
   justifié par le code.
6. **D5** : dans le noyau, comment sont numérotées les rondes de conception passées à l'objet ; ce que valent alors
   « au moins deux rondes » (F01) et « dernière ronde » (F11).
7. **Seuils 0,01 et 0,03** : toutes leurs occurrences dans le code sont repérées (F05, F06, F13, F14), aucune n'est
   oubliée.

## 4. Ce que tu écris

Sous `sortie/` : `rapport-contre-lecture-carte-facteurs-v1.md` et son compagnon `.sha256` : verdict (« utilisable »,
« utilisable après corrections », « à refaire ») ; constats numérotés `CCF-NN` avec gravité (bloquant, à corriger avant
usage, mineur), lieu exact, ce qui ne va pas, correction proposée ; ce qui est conforme ; ce que tu n'as pas pu vérifier.
Tu ne corriges pas les cartes toi-même.

## 5. Ce que tu n'écris jamais

Aucun critère ni aucune stratégie de classement des tâches : aucune règle, aucun seuil, aucune liste de mots, aucune
consigne qui interviendrait dans le choix d'une classe. Tu localises et tu vérifies ; tu ne proposes aucun changement de
l'objet. Aucun texte d'appel ni aucune consigne recopiés : cite fichiers, fonctions, lignes et colonnes. Rien sur une
tâche de banque, aucun score, aucun fait de course.

## 6. Interdits

Rien hors de ce dossier ; aucun `git`, réseau, sous-agent ni clé ; n'exécute pas le code de l'objet ni celui du noyau
(lecture, `grep`, `sed -n`, analyse syntaxique avec `python3 -I` et le module `ast`). Écrire seulement sous `sortie/`.
Heures lues sur `date -u` dans la commande qui les écrit.

## 7. Fin

Réponse finale en quelques lignes : verdict, constats bloquants ou à corriger, empreinte du rapport.
