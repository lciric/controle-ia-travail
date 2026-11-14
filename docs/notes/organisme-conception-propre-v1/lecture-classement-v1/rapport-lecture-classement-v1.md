# Rapport — outil du lecteur et programme de classement, course « conception propre » — v1

Développeur neuf, sous-agent de la session mère, tâche N3 de R-2615 ; du 13 novembre 2026, 23:37 UTC, au 14 novembre
2026, vers 00:05 UTC (heures relevées par `date -u`). Écrits **avant toute course et toute lecture**, d'après
`conception-course-v1.md` (`be3ba97e…`, § 3 à 8) et `consigne-lecteur-v1.md` (`95efebaa…`). **Aucun modèle appelé, aucune
clé lue ni affichée, aucune instance, aucune dépense ; rien commité** (la mère verse) ; rien écrit sous `src/` ni `tests/`
(R-2614) ; le clone de l'orchestrateur lu seulement (essai de la normalisation typographique), resté propre. Aucun des
chemins interdits de la tâche n'a été ouvert.

## Verdict

Outil et programme prêts, essayés et scellés ; **à contre-lire par un autre modèle avant tout envoi** (conception, § 8).
Essais : **47 passés**. Banc : **46 mutants tués sur 46**. Deux constats sur la règle elle-même (points A1 et A2 plus bas) :
la mère peut vouloir les porter à Lazar avant la course.

## 1. Pièces (scellées ; SHA-256)

| Pièce | Empreinte |
|---|---|
| `outil_lecteur_conception_propre_v1.py` (préparation des envois, vérification mot pour mot) | `59e665afc77dcb2c51ec70efcb7481e4b13d28ecf90c7a29db33e98a5b059199` |
| `classer_conception_propre_v1.py` (classement, L1 à L5, Holm, témoin à score permuté) | `f91962f33ba8b1d46c802e9e53e0f8f662a7a156b96be4128f6d4c866546cf66` |
| `essais_lecture_classement_v1.py` (fiches factices, lecteur simulé) | `72cfd065418458da8b93467bc738e012c7e0c7cb0fa79cb39d858070fe936453` |
| `mutations_lecture_classement_v1.py` (banc) | `642243ad5455cb4d8a4f4170d1c13b02d4596612943230e4e247421009b3601b` |
| `resultat-essais-lecture-classement-v1.txt` (23:59 UTC) | `7e1a3e618186f27661dace7f258dd9be8db82290a5b6fefeb612ee906cb7ba01` |
| `resultat-mutations-lecture-classement-v1.json` (23:59 à 00:00 UTC) | `8b42141c356d56e0f02ba653c74a3aa0aa799fdd52e1fe30110c9d218e0f9e6e` |

Pièces épinglées dans l'outil (refus si une empreinte diffère) : consigne `95efebaa…`, question `77c524f3…`, faits
`d19b5400…`, catalogue `ddfb2522…`, témoins du lecteur `d11efe78…`, idées au hasard `b5e38724…`, conception `be3ba97e…`.

## 2. Gestes de la mère, dans l'ordre

1. Après la clôture de la course et l'attestation scellée (§ 3), depuis la racine du dépôt :
   `.venv/bin/python -I -B docs/notes/organisme-conception-propre-v1/lecture-classement-v1/outil_lecteur_conception_propre_v1.py preparer --fiches runs/course-ideation-conception-propre-v1/<id>/copies/sortie--fiches-validees.json --attestation docs/notes/organisme-conception-propre-v1/attestations/attestation-lecture-g1-v1.json --sortie <dossier neuf>`.
   Refus sans rien écrire si : une pièce épinglée diffère ; le fichier des fiches n'égale pas son compagnon ; l'attestation
   manque, n'est pas scellée, ne porte pas l'empreinte des fiches, ou un de ses deux drapeaux n'est pas `true` ; la pile
   demande plus de 6 appels ; la réserve de 4 USD ne paie pas `max_tokens` ≥ 16 384 par appel ; le dossier n'est pas vide.
2. Envoyer **chaque** `envoi-<L>-lot<k>-v1.corps.json`, tel quel, au relais Kimi v4 (`--plafond-usd 4 --max-appels 6
   --max-recherches 0`), sous GO-2026-11-13-06, une requête par fichier (session neuve) ; ne jamais envoyer
   `pile-interne-v1.json`, `cle-lectures-v1.json` ni le manifeste (origine des fiches et correspondance des étiquettes).
3. Écrire chaque réponse entière du relais (`chat.completion`) dans `reponse-<L>-lot<k>-v1.json` du même dossier et la
   sceller (`python -m controle_ia.scellement sceller`). Une réponse dont le modèle servi n'est pas `kimi-k3.1-pro` est refusée.
4. `… classer_conception_propre_v1.py --envois <dossier> --sortie <dossier neuf>` → `classement-v1.json`, `classement-v1.md`,
   `lecture-verifiee-L1-v1.json`, `lecture-verifiee-L2-v1.json`, scellés. Ensuite seulement, les notes du juge de l'organisme
   peuvent être ouvertes (§ 4.8 ; le τ de Kendall n'est **pas** écrit ici : à faire après le scellement du classement).

Mesure à blanc sur la vraie consigne, la question, les faits, le catalogue et les 20 témoins, avec 36 fiches factices de
≈ 3 500 caractères : 3 lots par lecture (19, 19, 18), corps de 96 à 106 ko, pire cas total 3,18 USD pour 6 appels à
`max_tokens` 32 768 (borne du relais : (octets + 1 024) × 2 USD/M + `max_tokens` × 10 USD/M).

## 3. Ce que font les programmes (renvois à la conception)

- **Aveugle** (§ 4.3) : vue = clés du gabarit seules, **réordonnées dans l'ordre du gabarit** (le fichier de l'orchestrateur
  est écrit à clés triées, les témoins dans l'ordre du gabarit : sans cela, l'ordre des clés trahissait l'origine) et
  **typographie normalisée** par la fonction de l'orchestrateur (recopiée, comparée à l'original par un essai) ; champs
  internes toujours retirés ; tout autre champ (`citations_verifiees`, `test_de_mort`, `non_opposable`) retiré **et
  consigné** au manifeste. Ordres : `SeedSequence(2026111302).spawn(4)`, enfants 0 et 1 ; étiquettes F01… par lecture ;
  ⌈n/20⌉ lots égaux à un près. Le message = consigne telle quelle, puis question, faits, catalogue, chacun sous un titre
  `=== Pièce : … ===`, puis le lot en JSON `[{"etiquette", "fiche"}]` sous un titre qui nomme ses étiquettes (seul texte
  ajouté par l'outil).
- **Preuve** (§ 4.5), **valeurs retenues**, **portes**, **nouveauté**, **ordre** (S, coût, départage enfant 2), **deux
  désignées** seulement si L1 à L4 tiennent et L5 est rejetée ; **témoin à score permuté** (enfant 3) toujours calculé, avec
  le nombre de fiches communes ; **L1 à L5** ; huit comparaisons descriptives, **Holm** ; E1 à E5 ; signes de propreté ;
  exactitude du lecteur par critère et par lecture ; comptes par proposeur (information, N-058) ; notes du juge jamais lues.

## 4. Essais (47 passés) et banc (46 sur 46)

Essais sur fiches factices (8 admissibles aux profils connus, 3 hors question), avec les 20 vrais témoins et un lecteur
simulé : cas sain (désignées et ordre recalculés à part, p de L5 contre la valeur exacte 165/12 870, témoin permuté
recalculé, départage recalculé) ; **citation altérée** (comptée 0, fiche déclassée) ; **lectures discordantes** (R7, N,
R5) ; occupation à passage de catalogue faux ; **témoins mal classés** : publiées non reconnues (2 : L1 tient ; 3 : E2),
reconnue dans une seule lecture (suffit), mauvaise entrée (ne compte pas), fausse fiche acceptée avec citation exacte
(L2 manque) ou fausse (L2 tient), jumeau rejeté ou occupé (L3), lectures trop discordantes (L4) ; L5 non rejetée (E3),
idées au hasard aussi bonnes ; réponses fautives (illisible, entrée manquante, en double, étiquette hors lot, ordre non
suivi) ; valeurs non entières ; R4 hors `levier:juge` ; réponse non scellée, altérée, absente, autre modèle ; envoi altéré ;
attestation fautive (7 formes) ; fiches altérées ; pièce épinglée altérée ; écrasement ; gardes d'appels et de dépense ;
auteurs sans effet ; aucun import réseau ni lecture des notes du juge ; bout en bout en ligne de commande (`-I -B`).
Banc : 46 mutants (preuve, aveugle, graines, gardes, attestation, admissibilité, retenue, portes, S, coût, départage,
témoin permuté, désignation, L1 à L5, valeur p, Holm, E5), **tous tués** ; un mutant équivalent trouvé en route (garde
redondante du passage vide) a été retiré du code, puis tué.

## 5. Points de la règle ambigus, et lecture prise (rendue aussi dans `PRECISIONS` de la sortie)

- **A1 — L5 a un plancher de puissance, et E4 est inatteignable.** Les idées au hasard ayant C = 0 quand elles échouent,
  p ≥ C(n − k + 8, 8) / C(n + 8, 8) pour k neuves parmi n réelles admissibles : il faut **au moins 13 neuves sur 36**
  (8 sur 20, 5 sur 10) pour que L5 puisse rejeter. Avec une seule neuve, p ≥ n/(n + 8) > 0,05 : **E4 (« moins de deux
  neuves » avec désignation) ne peut jamais arriver sous L5**. La règle désigne donc rarement, sauf si plus du tiers des
  fiches passent tout. Écrit tel quel ; à porter à Lazar si on veut un autre test avant la course (nœud : modification de
  règle).
- **A2 — L4, « κ non défini (une marge constante) ».** κ est défini (souvent 0) quand une seule des deux marges est
  constante. Lu comme le texte l'annonce : **dès qu'une marge est constante**, on juge l'accord brut (≥ 0,8).
- **A3 — « Mot pour mot ».** Espaces normalisés seulement ; passage cherché dans **une** chaîne de la fiche (à cheval sur
  deux champs, ou clés JSON recopiées : non prouvé) ; échappements JSON `\"` et `\\` acceptés (la fiche est servie en JSON) ;
  vide = non prouvé ; aucune longueur minimale ; plus de 200 caractères non refusé ; catalogue : cellules de la ligne Ck,
  `**` retirés.
- **A4 — Réponse incomplète** (lot illisible, entrée manquante ou double) : la règle se tait ; tout compté 0 et `aucune`,
  rapporté en anomalie, sans arrêt (6 appels au plus : pas de relecture).
- **A5 — Comparaisons descriptives** : test, sens et graines non fixés ; pris : permutation bilatérale, 100 000,
  `SeedSequence(2026111303).spawn(8)` ; valeur p de L5 : (1 + k)/(1 + 100 000).
- **A6 — L1, L2, L4 et l'exactitude** jugés sur les valeurs **prouvées de chaque lecture** ; une fausse fiche à qui le
  lecteur met 1 avec une citation fausse compte 0, donc **passe L2**.
- **A7 — Audit de propreté** : déclenché si **un** des quatre signes du § 7 tient (il l'est dans le cas sain, toutes les
  publiées étant reconnues).
- **A8 — Divers** : vecteur permuté = (R1…R7 retenus, R4 compris, N, coût) ; départage attaché à la fiche ; lots égaux à un
  près ; étiquette de levier en double = deux étiquettes (hors question) ; réordonnancement et typographie de la vue
  (précisions de l'aveugle, non écrites au § 4.3).

## 6. Réserves

- Lecteur simulé, fiches factices : les essais ne disent rien de la manière dont Kimi citera ; le taux de « non prouvé »
  réel est inconnu (A3 le rend sévère).
- Les témoins restent reconnaissables par style et longueur (réserve de la conception, § 10), malgré la vue normalisée.
- Le τ de Kendall avec le juge de l'organisme (§ 4.8) n'est pas écrit (format des notes hors mandat ; à ouvrir après le
  scellement du classement).
