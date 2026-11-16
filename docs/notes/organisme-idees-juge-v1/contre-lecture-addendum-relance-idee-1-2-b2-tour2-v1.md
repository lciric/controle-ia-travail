# Contre-lecture (brouillon 3, lecteur C) de l'addendum de relance de l'idée 1.2 — tour 2, v1

- **Pièce relue** : `docs/notes/organisme-idees-juge-v1/addendum-relance-idee-1-2-v1-brouillon3.md`
  (`2590228454cd6a7f507fd9fef7ee77e914fee34af30d66acb04e2b745b1b61a6`, égale à son compagnon ; 689 lignes). Brouillon 2 :
  (empreinte entière recalculée : `ab55d5af5d70b340780c33b2bfe4dee15750095540af934530eb74531928d1df`).
- **Lecteur** : modèle C, neuf pour ce tour ; n'ai écrit ni la pièce ni les brouillons ni [T] ni [AE] ni le code. Rédacteur : modèle A.
- **Dates** : 2026-11-16, 13:34Z à 13:35:54Z (`date -u`).
- **Verdict : « corrections »** — 0 majeure, 2 mineures. La conception n'est pas en cause.

## 1. Corrections du tour 1 de cette lecture (rapport `…-b2-tour1-v1.md`, `f5b2690a…4b80`, empreinte recalculée égale) : appliquées fidèlement

`diff` brouillon 2 → brouillon 3, hunk par hunk, comparé aux « nouveau » du § 3 du rapport :
M1-a, M1-b, M1-c, m1-a, m1-b, m2 : texte identique caractère pour caractère (y compris la mise en gras de m1-a telle que
demandée). Le reste du différentiel : en-tête (version, empreinte du brouillon 2, tête `e3dc0871`, heure 13:28:12Z), ligne
« Statut et lieu » (brouillon 3), section « Contre-lecture » (entrées « Contre-lecture 2 » et « Traitement », liste des six
décisions mise à jour). **Rien d'autre.** Facultatifs f-1 à f-5 non appliqués, déclarés. Compagnons du brouillon 3 et du
programme d'application : `sha256sum -c` OK ; la tête `e3dc0871` existe et est celle de `main`.

## 2. Vérifications demandées

1. Corrections : § 1, conforme. 2. Cause, qualification : inchangées depuis le tour 1, conformes. 3. « Mêmes tirages » :
inchangé, conforme. 4. Conditions : zéro ligne au format du lanceur (`grep -cE` = 0, rejoué) ; commande, `--addendum` sur
[AE], PID, commit, borne de 24 h, contrôle des versions présents ; espace libre 7,1 Go à 13:35:54Z (cohérent avec 4.4). 5. Consigne
et seconde interruption : précisée (arrêt venu de l'extérieur ; `arret.json` renvoie à [T] l. 512 ; machine hors session = dépense,
GO) : conforme. 6. Voie (a) : inchangée, conforme. 7. Aucun critère, seuil, graine, plan modifié : confirmé. 8. Empreintes :
brouillon 2, brouillon 3, rapport du tour 1, programme d'application, compagnons recalculés, exacts ; aucun identifiant de
modèle (recherche vide) ; section « Contre-lecture » remplie. R-2979 relu (`grep`) : étape 0 v5 à 12:45:53Z, deux processus, « le
jeu de l'idée 1.2 doit tourner à côté » : l'ordre libre de 4.10 et 4.9 y est conforme.

## 3. Corrections exigées (toutes mineures)

Chaque « ancien » figure une seule fois dans le brouillon 3 (éprouvé).

**m-1 — § 5, Constat : antécédent de « quatre minutes plus tard » rendu ambigu par m2.** Après la réécriture de m2, la phrase
cite « avant 06:20:55Z » juste avant « s'arrêtent quatre minutes plus tard, à 04:36:02Z » ; lue de suite, 04:36:02Z n'est pas
quatre minutes après 06:20:55Z (il s'agit de la sortie de 04:31:41Z).

Ancien :
```text
les journaux de la session s'arrêtent quatre minutes plus tard, à 04:36:02Z.
```
Nouveau :
```text
les journaux de la session s'arrêtent quatre minutes après la seconde de ces deux sorties, à 04:36:02Z.
```

**m-2 — 4.10, puce « durée » : le plafond « cinq processus » contredit le décompte du premier alinéa et ignore le cas permis par « ordre ».**
Le premier alinéa compte 2 (idée 1.2) + 2 (étape 0 v5) + 3 (jeu de l'idée 1.1) = 7 ; la puce dit « jusqu'à cinq » (vrai seulement
si l'étape 0 v5 et le jeu de l'idée 1.1 ne se recouvrent pas : le rapport du tour 1 de cette lecture, § 5 point 5, le notait
et le brouillon 3 le renvoie à la mère hors de la pièce). De plus, si le run part pendant l'étape 0 v5 seule (cas que 4.10 permet), il y a quatre processus pour
quatre processeurs logiques : « au moins 1,25 fois » n'est alors pas le cas. La puce doit dire son hypothèse.

Ancien :
```text
jusqu'à cinq processus de calcul de même priorité pour quatre processeurs logiques, soit 4/5 d'un
  processeur chacun au mieux ;
```
Nouveau :
```text
jusqu'à cinq processus de calcul de même priorité pour quatre processeurs logiques (deux de l'idée 1.2 et trois du
  jeu de l'idée 1.1, l'étape 0 v5 ayant fini ; pendant l'étape 0 v5 seule : quatre processus, aucun ralentissement attendu de ce
  fait ; si le jeu de l'idée 1.1 partait avant la fin de l'étape 0 v5 : sept processus, ces chiffres sont à refaire), soit 4/5 d'un
  processeur chacun au mieux ;
```
(Le « ancien » ci-dessus tient sur deux lignes dans le fichier ; la fin de la première ligne est « …quatre processeurs logiques, soit 4/5 d'un » et la seconde commence par deux espaces, « processeur chacun au mieux ; chaque phase… ».)

## 4. Remarques facultatives

- f-1 à f-5 du tour 1 de cette lecture restent ouvertes (zéro ligne au format du lanceur sur la copie sous `prereg/` ; durée
  d'attente chiffrée ; disque partagé) : à la mère.
- Le disque offert « ≈ 39 Go » (4.4, § 6) : `df` rend aujourd'hui 252 Go au total pour `/home/user` ; le chiffre vient du
  tour 1 de la pièce et n'a pas été touché ; sans effet sur la règle (seuil de 1 Go libre).
- Mise en page : trois lignes du § 5 dépassent largement la largeur des autres (suites de m1-a et m2) ; cosmétique.

## 5. Points pour la mère

1. m-2 : le plafond de processus dépend de l'ordre des travaux de l'idée 1.1 ; décide si tu veux l'écrire (couple) ou le laisser au registre.
2. La condition de m5 (« si le journal de la mère la dément, elle est corrigée avant la recopie ») reste : à lever avant la recopie sous `prereg/`, après lecture de ton journal (02:30Z–04:40Z).
3. Ligne à ajouter à la section « Contre-lecture » : mon tour (modèle C, lecture entière du brouillon 3, ce rapport, son empreinte, verdict « corrections », 0 majeure, 2 mineures) ; lettre inscrite par toi.
4. Aucun écart à un texte scellé ; aucun mot du directeur nécessaire ; risque connu et déclaré par la pièce : la limite d'usage de la session.

## 6. Incidents et gestes de ma main

Aucun incident. Commandes légères : `diff`, `sha256sum`, `grep`, `sed`, `df`, `uptime`, `git rev-parse`/`log` (dépôt principal, lecture). Aucun fichier du run invalide ouvert ; rien écrit dans la copie ni sous `diag/`, `runs/`, `donnees/` ; aucun appel réseau, aucune clé ; aucun processus arrêté ; pièce non modifiée ; pas de commit.
