# Vérification courte du différentiel brouillon 1 → brouillon 2 — préenregistrement de la course à plusieurs générations — v1

- **Lecteur** : Claude Fable 5.2 (`claude-fable-5-2`), sous-agent de la session mère `session_01XJ6Mgn4MZR4nxqK44C8Ea3` ;
  le même agent que la contre-lecture R2 du brouillon 1 (`11a1c50f…`). Autre modèle que le rédacteur (Opus 5.5), même
  famille. **Je vérifie ici mes propres corrections : ce n'est pas une lecture neuve** ; la contre-lecture R2 de la version
  finale reste due à un agent neuf.
- **Objet** : `preenregistrement-multi-generations-v1-brouillon2.md`
  (`87ac268a3e6532832620cf363d508a12a0172529ed899ffb7ed23004b3dc6d6d`, recalculée, égale à son compagnon) ; `rapport-redacteur-v2.md`
  (`57ff110dfe82c52a1c625116f43e7b14d10217a9de71da7071e2d53940030c3d`, égale à son compagnon), lu en entier ; brouillon 1
  (`460c2888…`, intact).
- **Méthode** : différentiel complet entre les deux brouillons (475 lignes ajoutées, 218 retirées), lu en entier ; le reste
  du brouillon 2 n'a pas été relu. Les quatre pièces de comptes versées : compagnons justes.
- **Rejeu** (un processus à la fois, `ulimit -v 6000000`, `OMP_NUM_THREADS=2`, `python3 -I -B`, lecture seule des 12 parties
  scellées) : `comptes_c1_c4_v3b_v1.py` → sortie **égale à l'octet** à `comptes_c1_c4_v3b_v1.json` (`0599ae20…`) ;
  `compter_progres_v3b_v1.py` → sortie d'empreinte `9be7768a…`, **égale** à la pièce versée. Script lu en entier : formule de
  Wilson juste ; contrôle « Ei = i-ème entrée du gabarit » tenu dans les 12 mondes.
- **Interdits** : interdits communs v2 tenus ; aucun fichier, dossier ni branche interdits ouverts ou listés ; aucune
  recherche récursive ; aucune clé lue ; aucune écriture git ; aucun appel externe ; aucune dépense ; aucun refus de
  permissions ni de classifieur. Écrit : ce rapport et son compagnon.
- **Heures** (`date -u`) : début 2026-11-13 02:14:39 ; heure de fin en bas.

## Verdict

**Différentiel conforme ; scellable après sept corrections courtes (D-1 à D-7) et les préalables du texte.** C-1 à C-12 sont
appliquées à la lettre ; S-1 à S-11 sont prises sans risque, sauf un point de la garde 32 (D-5). Les corrections portent
toutes sur les choix neufs du rédacteur. Aucune ne demande de calcul.

## Corrections exigées

**D-1 — Sentinelle diluée : la règle de n n'est pas définie quand la dilution est impossible.** « λ choisi pour un gain
au-delà de l'enveloppe égal à δ = 0,0275 » suppose que la sentinelle non diluée gagne au moins δ. Une faible porte 0,02 à
0,035 nat : souvent moins que δ. Écrire le cas : par exemple, i = la première faible, dans l'ordre des identifiants, dont
la sentinelle non diluée gagne au moins δ ; un monde sans telle composante sort de la médiane, compté et rapporté ; nombre
minimal de mondes restants en dessous duquel n = 400 par repli. La même précision vaut pour la règle de la forme.

**D-2 — Ordre des règles du banc non écrit.** Elles dépendent l'une de l'autre : la sentinelle se sert de l'attribution (f) ;
la fusion aussi ; la forme se choisit « à n retenu » ; τ dépend de n et de la forme ; la mesure de Q-13 (b) dépend de tout.
Écrire l'ordre (f, fusion, n, forme, τ, mesure de Q-13 (b)) et dire qu'aucune règle n'est rejouée après une suivante.

**D-3 — Règle de la forme de la valeur e : deux précisions.**
1. Dire que le groupe de 3 doublons est **le seul groupe porteur** de la génération simulée (seuil de rang 1) : c'est le cas
   visé par C-5 ; avec d'autres groupes promus, la mesure ne dit plus la même chose.
2. La preuve de validité doit être écrite et contre-lue **pour chacune des trois formes avant le banc** ; une forme sans
   preuve n'est pas éligible. Sinon la règle peut geler une forme, puis chercher sa preuve.

Suggéré en plus : rapporter aussi les tailles 2 et 6, comme mesures.

**D-4 — Règle de fusion : deux cas manquent.**
1. Fermeture : si i fusionne avec j et j avec k, les trois forment-elles une seule composante ? À écrire (je lis que oui).
2. Étiquette C8 et classe de la composante fusionnée : la ligne P en dépend. Proposition prudente : l'étiquette la moins
   favorable de ses membres.

**D-5 — Garde 32 : trois manques, dont un qui touche C-8.**
1. « Durée maximale de la course » n'a pas de valeur dans le texte (72 heures en v67, « jamais un couperet »). L'écrire.
2. « Machine arrêtée au plus tard à la durée maximale » : dire qui l'arrête (un processus hors de la machine), que l'arrêt
   n'est pas la destruction, que le rapatriement précède toute destruction, et que cet arrêt se lit N.
3. Dire si une machine sert les deux mondes ou une par monde ; les 10 USD couvrent la somme.

**D-6 — A7 : dire ce qui fait foi.** « Une attribution que ce recalcul renverse est relue au verdict avant l'issue » ne dit
pas quelle valeur décide. Écrire : le recalcul sur 2 × 200 000 instances fait foi pour l'issue ; un intervalle qui chevauche
le seuil laisse l'issue du premier calcul, avec la réserve en tête.

**D-7 — Q-12 et Q-13 : trop d'options pour être posées telles quelles** (format du dépôt : 2 ou 3 options).
- Q-12 porte cinq options et un seuil. La poser en deux décisions : (i) tests des lois plantées — (a), (b), (d′), avec (c) et
  (d) en variantes d'une ligne ; (ii) seuil de la garde 30 — un quart, un tiers, la moitié.
- Q-13 porte cinq options. La poser en trois : (a) garder ; (c) revoir la famille, avec la règle (b) appliquée à la famille
  revue ; (e) pilote d'une génération. (b) seule n'est pas une vraie option : le texte dit qu'elle rendrait presque sûrement
  « pas de course ». (d) déplace le critère de progrès vers ce que la simulation montre ; la donner comme écartée, avec sa
  raison, ou la retirer.
- Dire que le seuil « la moitié des mondes » de Q-13 (b) n'a aucune pièce.

## Réponses

**1. C-1 à C-12 à la lettre ?** Oui pour les douze.

| | constat |
|---|---|
| C-1 | six points écrits, deux réserves dites, Q-13 ajoutée ; comptes rejoués égaux |
| C-2 | (d) et (e) sorties de l'hypothèse affirmée ; colonne par issue ajoutée |
| C-3 | les six précisions y sont (R₂, R₃, part sur 200 graines, même composante, « plafond » à part, dénominateur) |
| C-4 | marge retirée, table des minimums, phrase exigée, borne haute rapportée |
| C-5 | conséquence écrite, règle de choix écrite avant le banc, compte au relevé ; restes : D-3 |
| C-6 | les trois cas écrits |
| C-7 | A1 rétabli, A6 complété, A7 ajouté ; reste : D-6 |
| C-8 | rapatriement avant destruction, essayé à blanc ; voir D-5 point 2 |
| C-9 | pièce à part contre-lue ; « ou » levés ; compteur de tirage ; cycles bornés ; restes : D-1, D-2, D-4 |
| C-10 | P8 devenue mesure chiffrée |
| C-11 | pièces versées et scellées |
| C-12 | Q-9, Q-12, Q-10 (b) corrigées ; reste de forme : D-7 |

**2. S-1 à S-11 sans risque ?** Oui. Aucune ne desserre une garde ni n'ouvre un réglage pendant la course. S-2 n'entre
que comme option de Lazar. Seul point : S-4, par la garde 32 (D-5).

**3. Choix neufs du rédacteur.**
- **Sentinelle et δ = 0,0275** : définition bonne (monde réduit à ce que l'archive couvre, plus i ; dilution vers la
  meilleure loi ; gain compté contre l'enveloppe). δ au milieu de l'intervalle de la conception : arbitraire, dit, acceptable.
  Reste D-1.
- **Règle de la forme** : bonne dans son principe (la plus puissante, la moyenne à moins de 0,02) ; restes D-3.
- **Grille de f** {0,5 ; 0,6 ; 0,75 ; 0,9}, égalité à 0,01 → 0,75 : bonne ; faible risque, mondes de calibration seulement.
- **Règle de fusion** : bonne ; restes D-4.
- **Borne de 3 cycles** : bonne ; au-delà, mot de Lazar.
- **Garde 31** : bonne ; elle ne lit que des défauts de chaîne, ni l'oracle ni le progrès.
- **Garde 32** : à compléter (D-5).
- **Options de Q-13** : contenu juste et honnête, la règle R3 est dite ; forme à resserrer (D-7). La recommandation
  « (c) puis (b) » à 0,45 est défendable ; son risque (régler la famille sur un modèle arbitraire) est écrit.
- **Variante Q-12 (d) et (d′)** : montants refaits par moi, justes. (d) : 52 tests de moins, Claude 285,00, Argon 29,00,
  modèles 326,00, lignes 285 et 51. (d′) : 291,00, 29,40, 332,40, lignes 291 et 52. L'inconvénient est dit : sous (d),
  l'instrument T-ELIM n'est plus éprouvé après la génération 1.
- **Recalcul de Δ_i sur 2 × 200 000 instances, seuil 0,5 lu sur la part** : acceptables.

**4. Questions prêtes pour Lazar ?**

| question | prête ? |
|---|---|
| Q-3 | oui |
| Q-9 | oui (sous-choix de τ clair, plus de marge à inventer) |
| Q-10 | oui |
| Q-11 | oui |
| Q-12 | après D-7 (montants justes ; trop d'options) |
| Q-13 | après D-7 (constat juste ; trop d'options) |

Q-1 est bien marquée « à reconfirmer en sachant le constat ». L'échéance du 30 novembre est dite courte, à raison.

## Limites

- Lecture du différentiel seulement ; les parties inchangées du brouillon 2 n'ont pas été relues.
- Même agent que la contre-lecture : mes propres angles morts restent.
- L'étiquette « proches du seuil 20 sur 20 » et sa pièce (`26e1527a…`) n'ont pas été rouvertes.
- Les choix neufs sont jugés sur le texte ; aucun n'a été essayé par calcul.
- **Heure de fin** (`date -u`) : 2026-11-13 02:16:36.
