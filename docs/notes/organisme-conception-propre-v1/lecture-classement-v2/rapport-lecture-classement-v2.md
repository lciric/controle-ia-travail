# Rapport — outil du lecteur et programme de classement, course « conception propre » — v2

Même développeur que la v1, sous-agent de la session mère ; 14 novembre 2026, de 00:11 à environ 00:37 UTC (heures
relevées par `date -u`). Corrections commandées d'après la contre-lecture `contre-lecture-lecture-classement-v1.md`
(`baabfb13…`, R-2627, verdict « après corrections »). La v1 (`../lecture-classement-v1/`) reste telle quelle (R12).
**Aucun modèle appelé, aucune clé, aucune dépense ; aucun fichier de `runs/course-ideation-conception-propre-v1/` lu ;
rien sous `src/` ni `tests/` ; rien commité.** Le clone de l'orchestrateur a été lu seulement (essai de la typographie).

## Verdict

v2 prête et scellée. Essais : **80 passés** ; banc : **76 mutants tués sur 76** (les 45 de la v1 encore applicables, les
9 mutations survivantes de la contre-lecture, reconstituées d'après leur description, 18 mutants des corrections : M1, M2, M3 et κ exact ; 4 de la
variante). Une nouvelle contre-lecture courte du différentiel v1 → v2 reste à faire avant l'envoi (conception, § 8).

## 1. Pièces (scellées ; SHA-256)

| Pièce | Empreinte |
|---|---|
| `outil_lecteur_conception_propre_v2.py` | `a58fb8b99edb3bab6a9db43f33a4c3af25c81c9ac61bd7e47a550ad0b90f6e60` |
| `classer_conception_propre_v2.py` | `2cb65f33f0f5d21cb6a7048d8d89e3cee287c517e41e5e3fd6cd4d7dbb5ca774` |
| `essais_lecture_classement_v2.py` | `f91318a9da6f63f6980aa5202402311f76d813a4690c9273ee0750359b2dfe71` |
| `mutations_lecture_classement_v2.py` | `aa2393f0e8d41d32a4bb108729450b5b809198e3b38ac43019046d70a01c2d4c` |
| `resultat-essais-lecture-classement-v2.txt` (00:25 UTC) | `80f996551b01cffccac738516ef7199ff0544090db07c41d6aa9246c2872d1df` |
| `resultat-mutations-lecture-classement-v2.json` (00:30 à 00:35 UTC) | `1ab880300709d40e4ee2eb4f0bdac7476404060035a99e7a62cb8b3604e316c1` |

Les fichiers que les programmes écrivent portent maintenant `-v2` (`envoi-<L>-lot<k>-v2.txt`, `.corps.json`,
`pile-interne-v2.json`, `cle-lectures-v2.json`, `manifeste-envois-v2.json`, réponses attendues `reponse-<L>-lot<k>-v2.json`,
`lecture-verifiee-<L>-v2.json`, `classement-v2.json`, `classement-v2.md`). Les gestes de la mère sont ceux du rapport v1,
§ 2, avec les noms v2. `--fiches` ne prend que la copie du run (point M3).

## 2. Corrections

- **M1 — citations substantielles.** Un passage ne prouve rien sous **20 caractères hors espaces**. Justification :
  20 caractères font une proposition de quatre ou cinq mots, le plus court énoncé qui puisse porter un fait sur la fiche.
  Un signe (`+`), une lettre, une étiquette de levier (11), un code `C7`, une date `2026` ou une référence courte
  (`Nature 655`) restent en dessous. Les champs des témoins qui prouvent un critère sont tous bien plus longs, et la
  consigne borne en haut à 200 (la fenêtre utile est donc de 20 à 200). Pour R4, hors `levier:juge`, la valeur reste fixée
  à 1 par le programme. Le passage du catalogue est cherché **dans la seule cellule « Mécanisme central »** de l'entrée Ck,
  jamais dans le code, le nom ou la source : l'occupation doit montrer le mécanisme, comme le demande la consigne. Le passage
  de la fiche reste exigé. Les passages courts refusés et ceux au-delà de 200 caractères sont comptés par critère et par
  lecture, dans le JSON et dans le `.md`. Essais : `e`, `+`, `.`, `levier:juge`, `C7`, `2026`, le nom et la source de C7,
  le mécanisme de C2 cité pour C7, et un passage de fiche absent ou court sont tous refusés ; la limite de 20 contre 19 est
  vérifiée.
- **M2 — lecture illisible jamais comptée zéro en silence.** Quatre anomalies sont **bloquantes** : réponse illisible
  (JSON coupé compris), fin autre que `stop`, entrée manquante, entrée en double. Chacune nomme les fiches touchées. Une
  seule suffit à rendre la lecture **incomplète** : le verdict devient « E2 : lecture illisible ou incomplète (…) », avec
  les lots, les genres et le nombre de fiches réelles et de témoins touchés ; ils sont cités aussi dans `classement-v2.md`.
  La désignation est alors impossible, sous la règle comme sous la variante. **Relecture** : la règle n'en prévoit pas
  (deux lectures, six appels au plus) ; il n'y en a donc pas, et c'est dit au verdict. L'étiquette hors lot et le désordre
  ne bloquent pas, puisque l'entrée est écartée ; un essai prouve que l'entrée étrangère ne change rien.
- **M3 — provenance des fiches gardée par le code.** Seul
  `runs/course-ideation-conception-propre-v1/<AAAAMMJJ-HHMMSS>-course-ideation-conception-propre-v1-g1/copies/sortie--fiches-validees.json`
  est accepté, avec plusieurs contrôles :
  - le chemin est réel, sous la racine, sans aucun lien symbolique ;
  - la copie égale son compagnon ;
  - le manifeste de fin du lanceur (`manifeste-lanceur-fin.json`) est scellé, porte le code 0, et
    `pour_l_attestation.fiches_validees_sha256` y égale l'empreinte de la copie ;
  - chaque élément porte les clés du gabarit et les champs internes de l'orchestrateur (une liste de quarantaine
    `{fiche, signaux}` est refusée) ;
  - une pile sans fiche réelle admissible est refusée avant tout envoi (E1, rien n'est payé).

  Le classement **revérifie** tout cela et exige la même empreinte et le même run que le manifeste des envois. Un essai
  réécrit la copie **et** le manifeste de fin, d'accord entre eux : le classement refuse quand même. Onze formes fautives
  sont essayées. Les formats lus sont ceux du code du lanceur (`ecrire_scelle`, `copier_scelle`), pas des fichiers de run.
- **Essais muets de la contre-lecture (m2)**, désormais couverts :
  - le catalogue cherché dans toutes les entrées ;
  - une occupation acceptée sans passage de la fiche ;
  - L4 jugée sur R7 seul ;
  - κ au seuil strict ;
  - E5 au seuil large (4 sur 5 n'est pas « plus de 80 % ») ;
  - des comparaisons descriptives unilatérales ;
  - un audit qui exigerait les quatre signes ;
  - la typographie du passage tolérée ;
  - une étiquette hors lot gardée.

  Ce faisant, **un défaut réel** est apparu et a été corrigé : κ était calculé en flottants, et un κ de 0,4 exact valait
  0,3999… (L4 manquait à tort). Il est maintenant calculé en fractions exactes, de même que le seuil de E5.
- **Points moyens repris.** Le détail de L2 porte la valeur brute rendue (m4). Les précisions disent la discontinuité de
  A2 (m3) et le codage de la « lisibilité parfaite » (m5). Non repris : le tableau de forme par origine (m1), qui n'était
  pas commandé ; c'est une réserve.

## 3. Variante « désignation détachée de L5 » — préparée, NON active (nœud A1 de Lazar)

- La règle actuelle reste le défaut (`--designation L5`).
- La variante (`--designation detachee-v1 --decision R-…`) reprend la section A1 de la contre-lecture. Sous L1 à L4, avec
  une lecture complète, chacune des deux premières neuves est désignée **si son C dépasse strictement le plus grand C des
  huit idées au hasard**. La mention dit « séparation démontrée » si L5 rejette, « non démontrée » sinon. E3 devient une
  mention, et E4 redevient atteignable.
- Sans référence de décision (`R-` ou `N-` suivi de chiffres), elle est refusée, en ligne de commande comme en appel.
- **Elle n'est jamais calculée quand elle n'est pas demandée.** Le mot de Lazar doit donc venir **avant** le lancement du
  classement, et la mère doit le consigner au registre, pour qu'aucun résultat ne précède le choix de la règle.
- Essais : refus sans mot ; cas sain identique à la règle ; L5 non rejetée → deux désignées « non démontrée » ; une seule
  neuve → E4 ; hasard aussi haut (5 contre 5) → aucune ; lecture incomplète → aucune.

## 4. Réserves

- Le seuil de 20 caractères est une précision ajoutée à un silence de la règle (comme A3 en v1) : il rend la preuve plus
  sévère, et le taux réel de « non prouvé » de Kimi reste inconnu. La cellule « mécanisme » seule peut faire manquer L1 si
  le lecteur cite le nom de la conception au lieu de son mécanisme ; la consigne lui demande pourtant le mécanisme.
- Aveugle par la forme du fond (longueurs, antériorités vides, style des idées au hasard) non mesuré : la proposition m1
  n'a pas été faite.
- Les programmes ne vérifient pas leur propre empreinte : la mère vérifie `a58fb8b9…` et `2cb65f33…` avant chaque geste.
- Le τ de Kendall avec le juge de l'organisme (§ 4.8) n'est toujours pas écrit (après le scellement du classement).
