# Contre-lecture du devis du réajustement de nos lentilles R et S (lecture par lentille neuronale, Llama 3.1 8B Instruct) — v1

- Heure (`date -u`) : 2026-11-19T08:08:53Z.
- Contre-lecteur : sous-agent neuf (règle R2), modèle Fable 5.2 (`claude-fable-5-2`). Il n'a écrit ni le devis ni les pièces citées.
- Empreintes recalculées (`sha256sum`) :
  - devis `devis-reajustement-lentilles-b-beta-v1.md` : `1bf439ac624b7dac3a4bb7ad6dcbbfbc6030d857f6c5b56801e69abb830995d3` — égale à l'annoncée et au compagnon ;
  - relevé de prix `releve-prix-vast-h100-20261119T080302Z-v1.tsv` : `90395583310f3b1d3c414e392738d77a3b462c8616717f4101bd22b54b985a69` — égale au compagnon ;
  - accord de Lazar sur le verdict (`lecture-b-beta/accord-lazar-verdict-b-beta-v1.md`) : `8469add5…` — conforme à la l. 7 du devis.
- Pièces lues : le devis, le relevé, les champs de durée, d'empreinte, de taille et la **structure** (noms de clés) des trois fichiers
  `b-beta-ajustement-R.json`, `b-beta-ajustement-S.json`, `b-beta-export.json` de `diag/20261118-164930-neuron-lens-b-beta/` ; le journal
  `controles-b-beta-v1.log` ; la commande v8 ; le devis v12 (§ 2 point 6, § 4, § 5) ; le texte gelé (l. 224, 464, 584). Rien d'autre dans
  `diag/` ni `runs/`. Aucune valeur de mesure ni verdict lu. Aucun modèle, aucune machine, aucune commande du loueur, aucun commit.

## Verdict : **non employable** en l'état

Une version 2 courte suffit. L'arithmétique écrite est juste, les durées et les empreintes sont portées par les pièces. Mais les
plafonds soumis à Lazar ne couvrent pas le pire cas dans les conditions que le devis admet lui-même (une remarque bloquante), et
l'argument principal de la recommandation de la variante B repose sur une affirmation que les pièces versées contredisent, sur un
seuil non justifié par la pièce citée, et sur une « seconde mesure » sans statut écrit (remarques majeures).

## Ce qui a été recalculé et tient

| chiffre du devis | recalcul | pièce | état |
|---|---|---|---|
| montage 1 h 14 (16:48:55 → 18:03:15) | 1 h 14 min 20 s | journal, l. du redémarrage (début 16:48:55Z) ; `b-beta-ajustement-R.json`, `debut_utc` | juste |
| ajustement de R 18 414 s (5,12 h) | 18 414,4 s = 5,115 h | `b-beta-ajustement-R.json`, `duree_s` | juste |
| export 78 s | 77,9 s | `b-beta-export.json`, `duree_s` | juste |
| ajustement de S 18 065 s (5,02 h) | 18 065,2 s = 5,018 h | `b-beta-ajustement-S.json`, `duree_s` | juste |
| suite 1 h 19 (04:12:35 → 05:31:53) | 1 h 19 min 18 s à 20 s | journal : fin de S 04:12:35Z, fin de course **05:31:55Z** | juste à 2 s près (mineure 9) |
| course entière 12,72 h | 12 h 43 min = 12,717 h | journal | juste (mais location facturée 12,93 h : mineure 8) |
| empreintes et tailles de R et S, `rows_sha256`, 932 documents | identiques | les deux fichiers d'ajustement | juste |
| ajustements et export attendus 10,2 h | 5,115 + 5,018 + 0,022 = 10,155 | — | juste |
| variante A 11,7 h ; 16,1 h | 11,65 ; 16,1 | — | juste |
| variante B 13,0 h ; 18,7 h | 12,95 ; 18,7 | — | juste |
| coûts A : 27,7 ; 38,2 ; 42,2 USD | 27,6 à 27,7 ; 38,18 ; 42,18 | prix 2,3713 du relevé, l. 6 | juste |
| coûts B : 30,7 ; 44,3 ; 49,0 USD | 30,7 à 30,8 ; 44,34 ; 48,99 | idem | juste |
| plafond 50 : 30,0 ; 45,0 ; 16,8 h ; 18,6 h | 30,0 ; 45,0 ; 16,79 ; 18,56 | formule de la v8, étape 9 | juste |
| plafond 58 : 34,8 ; 52,2 ; 19,5 h ; 21,6 h | 34,8 ; 52,2 ; 19,54 ; 21,59 | idem | juste |
| relevé : offre 59816165, 2,3713, débit montant 1 744, trafic 0, fiabilité 0,9917 ; suivante 4,0990 ; une seule sous 4 USD/h au filtre complet | identiques | relevé, l. 6 et 7 | juste |
| copie de ≈ 17 Go en ≈ 12 min à 200 Mbit/s | 17,05 Go → 682 s = 11,4 min | — | juste pour les seuls fichiers d'ajustement |
| pire cas 6,56 h par lentille, 13,1 h | porté | devis v12, § 4 et § 5 | juste |
| « déterministe à l'ordre des documents près » | porté | texte gelé, l. 464 | juste |
| effet du matériel 0,03 | porté (plus grand écart 0,0296) | texte gelé, l. 224 et 584 | porté, mais mal employé (majeure 2) |

## Remarque bloquante

**B-1 — Les plafonds ne couvrent pas le pire cas dans les conditions que le devis admet (l. 48-49, 56, 70, 72-76).**
Trois sous-comptes se cumulent :
- *Frais fixes de trafic (l. 70).* Le devis garde 1,0 USD. Dans le devis v12, 1,0 USD est le compte du lieu sans rangement (25 Go
  entrants à 0,04 USD/Go) ; le même devis compte 1,68 USD pour la copie de fin seule (42 Go, § 4) . Ici on sort ≈ 17 Go de fichiers
  d'ajustement plus les exports : 25 Go entrants + 25 à 31 Go sortants = 50 à 56 Go, soit **2,0 à 2,24 USD** au plafond de trafic que le
  filtre admet (≤ 0,04 USD/Go, commande v8, étape 4). L'offre du relevé a un trafic nul, mais le relevé sera refait et le filtre
  admettrait une offre payante.
- *Copie (l. 48-49, 56).* Le pire cas de 0,5 h vaut pour 17 Go à 100 Mbit/s (0,38 h). Avec les exports, non mesurés : le devis dit
  « de l'ordre de 8 Go » (l. 48), la commande v8 dit « ≈ 13 Gio d'exports » (l. 288) : 25 à 31 Go à 100 Mbit/s = 0,56 à 0,69 h, au-dessus
  des 0,5 h. Et le débit réel est celui de la plateforme de modèles en écriture, non mesuré, pas le débit montant annoncé par l'offre.
- *Fin de course.* La course du 18 a été facturée 13 minutes de plus que la course (12,93 h contre 12,72 h, journal, étape 15) :
  vérification, préavis, destruction. Ici s'ajoute la relecture des empreintes au lieu de rangement avant destruction. Rien n'est compté.

Recalcul au prix exigé de 2,62 : variante A, 2,5 + 13,1 + 0,69 + 0,22 = 16,5 h → 43,2 + 2,24 = **45,5 USD, au-dessus de l'arrêt dur de
45,0** ; variante B, 19,1 h → 50,1 + 2,24 = **52,3 USD, au-dessus de l'arrêt dur de 52,2**. L'affirmation « minuterie au-dessus du pire
cas » (l. 73, 75) ne tient donc plus, et la marge affichée (0,7 et 0,8 h) était déjà de 4 %.
**Correction proposée** : (a) soit exiger un trafic nul dans le filtre de cette course et l'écrire, soit porter les frais fixes à
≈ 2,3 USD ; (b) compter la copie sur la taille mesurée des exports (à lire sur la machine avant la copie) et une ligne « vérification
à l'arrivée et destruction » d'au moins 0,25 h ; (c) refaire plafonds, arrêts durs et minuteries. Ordre de grandeur : **52 USD** pour la
variante A (arrêt dur 46,8 ; minuterie (46,8 − 2,3) / 2,62 = 17,0 h pour un pire cas de 16,5 h) et **60 USD** pour la variante B (arrêt
dur 54,0 ; minuterie 19,7 h pour 19,1 h). À recalculer par l'auteur ; ce sont des ordres de grandeur du contre-lecteur.

## Remarques majeures

**M-1 — « Variante A : aucune comparaison possible au-delà des tailles » est contredit par les pièces versées (l. 91-92, 123-126).**
Les trois fichiers cités portent, sans lecture d'aucun verdict, des empreintes numériques de l'ajustement lui-même :
`b-beta-export.json` a un champ `matrices_moities` (deux empreintes par couche, 31 couches, pour R) et une empreinte par fichier
exporté ; les deux fichiers d'ajustement ont `diffs_float64` (différences entre moitiés non arrondies, toutes couches, R et S),
`n_docs`, `longueurs`, `ecarts_sommes`. Ces étapes (ajustement, export) sont dans la variante A. Elle permet donc une comparaison
couche par couche de R (égalité d'octets des matrices) et une comparaison numérique de R et de S. « La raison principale de recommander
la variante B » tombe en partie.
**Correction** : ajouter au § 4 un palier intermédiaire commun aux deux variantes (empreintes par couche, puis écart maximal des
différences entre moitiés, tolérance fixée d'avance) ; redire la décision 1 honnêtement : la variante B n'ajoute pas l'identité, elle
ajoute la comparaison des **mesures** et le rejeu ; « une identité vérifiable dans tous les cas » (l. 125-126) est trop fort, puisque la
variante B peut conclure « lentilles différentes ».

**M-2 — Le seuil de 0,03 n'est pas justifié par la pièce citée pour l'usage qu'on en fait (l. 86-88).**
La pièce (texte gelé, l. 584 ; l. 224) mesure l'effet du matériel sur des **mesures faites avec les mêmes fichiers de lentilles
publiques** entre deux cartes, plus grand écart observé 0,0296. Le § 4 l'applique à un **réajustement suivi d'une mesure**, source
d'écart de plus. Fixer le seuil au plus grand écart déjà observé sur peu de comparaisons, et l'exiger sur « chaque valeur décisive »
(nombre non dit : plusieurs mesures par couche), c'est un critère qu'un écart ordinaire fait échouer. Le texte gelé lui-même, pour son
cas sain sur H100, tolère 0,05 à deux couches au plus et 0,10 à une (garde (j), l. 222-224) : le § 4 est plus sévère que la garde de la
course d'origine, sans le dire. « Valeur décisive » n'est pas défini (lesquelles, combien, quelle clé de quel fichier).
**Correction** : dans la pièce scellée, lister les valeurs par fichier et par clé, justifier le seuil par une pièce qui mesure la même
chose ou le déclarer conventionnel, et dire la règle face à la multiplicité (par exemple la forme de la garde (j)).

**M-3 — « Mêmes verdicts pour B-1 à B-7 » mêle l'identité des lentilles et la stabilité des verdicts, et la « seconde mesure
indépendante » n'a pas de statut (l. 39-41, 86-90).**
Le devis écrit lui-même que deux verdicts tiennent à une marge de l'ordre de l'effet du matériel (l. 40-41 ; chiffres « 3 pôles à la
couche 8 », « une couche sur 21 » sans chemin ni empreinte : R6). Le critère d'équivalence a donc une chance sérieuse d'échouer pour
une raison étrangère aux lentilles. Surtout, rejouer B-1 à B-7 est une expérience décisive neuve : il faut, avant la création, un texte
scellé et contre-lu (R1, R2) qui dise lequel des deux verdicts fait foi si les deux courses divergent, que la seconde est rapportée
quel que soit son sens (R3, R4), et qui prononce (R13 : un lecteur neuf dans **tous** les cas, pas seulement dans la branche « lentilles
différentes », l. 90). Sans cela, la seconde course ouvre un choix après coup entre deux verdicts. « Indépendante » est aussi trop
fort : même code, même corpus, mêmes graines, même modèle de carte ; seul le matériel change.
**Correction** : ajouter ce préalable au § 5 ; séparer dans le § 4 « mêmes lentilles » (octets, matrices, différences entre moitiés)
de « mêmes conclusions » (verdicts) ; règle par défaut proposée : le verdict scellé et accepté du 18 reste, la seconde course est
rapportée à côté, tout désaccord est un nœud de Lazar.

**M-4 — Clé d'écriture : la variante B n'est pas « le même lanceur », et l'argument contre la copie en cours de route se contredit
(l. 37-38, 78-80, 98-100, 113-116).**
La commande v8 retire la clé de la plateforme de modèles après le téléchargement des poids (« ensuite retirée de la course, vérifiée
par son nom », étape 12 ; journal : retirée à 17:59:47Z). Avec le lieu L2, la clé doit rester 13 à 19 h sur la machine et être relue à
la fin : c'est un changement du lanceur et de ses gardes de secrets qui manque à la liste « seuls changent… » (l. 38), et la commande
v8 déclare une exposition résiduelle chez le loueur (l. 290). Ensuite, le § 3 refuse toute copie en cours de route « pour borner la
durée d'une clé d'écriture sur la machine » (l. 79), alors que le § 6 dit que la clé y est « pendant toute la course » (l. 114) : le
refus ne borne rien et laisse perdre jusqu'à l'arrêt dur. Enfin la clé recommandée cumule lecture du modèle et écriture : exposée dès
la création, elle permet d'écraser le dépôt de rangement.
**Correction** : dire le changement du lanceur (clé gardée, où, essais des formes de secrets refaits avec les poussées toutes les dix
minutes) ; ou bien copier R dès son export et S dès sa fin puisque la clé est là, ou bien justifier autrement ; écrire que la
relecture des empreintes depuis la session se fait **après** la révocation de la clé, sur une révision du dépôt notée, et comment
(empreintes rendues par la plateforme sans retéléchargement, ou téléchargement : alors durée, disque et trafic de la session à dire).
Signaler aussi que le lieu L3 « Lazar tire » suppose un accès entrant alors que la commande v8 est « sans ssh ».

**M-5 — Égalité d'octets des fichiers d'ajustement : condition non établie au-delà de la virgule flottante (l. 27-29, 84-85).**
Le devis ne nomme que l'ordre des réductions. Il ne dit pas si le fichier `.pt` contient autre chose que les tenseurs (ses
métadonnées portent `shard`, `corpus`, `rules` ; chemins, versions ou état de sauvegarde possibles), ni si une sauvegarde reprise
change les octets. Les noms des fichiers exportés portent un identifiant de génération différent pour chacun des trois exports
(`…gen-dfeeec0d…`, `gen-5d6677d2…`, `gen-3c21f5cc…`) : s'il est tiré au hasard, les noms et le manifeste de l'export différeront
à coup sûr, et « une empreinte par fichier » (l. 23) ne se compare pas par nom. La ligne 23 décrit en outre mal la pièce : elle porte
trois exports de R (entier, moitié paire, moitié impaire), sans taille.
**Correction** : vérifier dans le code (sans dépense) ce que contient le fichier d'ajustement et d'où vient l'identifiant de
génération ; comparer les exports par couche et par contenu ; corriger la ligne 23.

**M-6 — Crédit : chiffre sans pièce et demande incohérente (l. 101-102, 135).**
« 11,30 USD à 07:04Z relevé par la mère » ne renvoie à aucun chemin (R6) ; le journal donne 13,21 à 05:45:55Z. Le § 5 demande une
recharge de « ≈ 50 à 60 USD », la décision 4 « au moins le plafond retenu » : ce n'est pas le même montant (plafond 58 − 11,30 = 46,7
au moins, plus les autres lignes ouvertes, non chiffrées). Le devis ne dit pas non plus si la recharge automatique, sur laquelle Lazar
a levé la condition de crédit de la v8 (R-3319 ; journal, 23:49Z : « recharge automatique tenue »), tient toujours, ni comment la
dépense se place dans le budget journalier de 100 euros (sans pièce) avec les autres courses du jour.
**Correction** : citer le relevé de crédit par son chemin, chiffrer les autres lignes, donner un seul montant, dire l'état de la
recharge automatique et garder la garde de la v8 (crédit < 1 USD → arrêt).

## Remarques mineures

1. **Prix minimal de la règle du refus absent (l. 72, 128).** La v8 exige un prix ≥ (arrêt dur − frais fixes) / 36 (1,85 USD/h au
   plafond de 75). Aux plafonds proposés : 1,42 (58) et 1,22 (50). L'offre à 2,3713 passe, mais la borne n'est pas écrite, et les
   colonnes d'épreuve du relevé (l. 1 : options de 62 à 115 USD) ne correspondent à aucune option proposée. Correction : écrire la borne
   et refaire le relevé avec les colonnes des deux options.
2. **Compte rendu à 60 % déclenché en course normale.** La garde compte au plus grand du prix déclaré et du prix lu (devis v12, § 5) :
   (30,0 − 1,0) / 2,62 = 11,1 h pour 11,7 h attendues (A) ; (34,8 − 1,0) / 2,62 = 12,9 h pour 13,0 h (B). Le compte rendu sonnera
   presque à coup sûr. Le dire, ou le déplacer.
3. **Arrêt réel plus tôt que la minuterie « à 2,37 ».** Pour la même raison, la garde arrête à 16,8 h (A) ou 19,5 h (B) quel que soit
   le prix lu ; les 18,6 et 21,6 h (l. 74, 76) ne sont que le filet. À préciser.
4. **Marge du pire cas des ajustements (l. 54).** Le mesuré (5,12 h) a dépassé le haut de l'attendu du devis v12 (4,1 h, journal,
   contrôle 7) et vaut 78 % du pire cas de 6,56 h. Une machine un peu plus lente fait arrêter la course au banc du montage (seuil de
   23,6 s par document, devis v12 § 5) : perte faible mais « aucune reprise sans devis neuf ». À dire comme risque.
5. **Montage (l. 53).** L'installation a pris ≈ 59 min pour une borne de 3 600 s (journal, contrôle 2, « réserve »). Un pire cas de
   2,5 h de montage n'a de sens que si cette borne est relevée ; sinon la course s'arrête vers une heure. Le devis v12 prenait 3 h.
6. **Disque (l. 61).** 200 Go repris de la v8, dont le compte est estimé (l. 287-288) ; aucune pièce ne porte l'occupation réelle du
   18. La copie vers la plateforme ne doit pas dupliquer les fichiers sur le disque : à vérifier dans le code de copie à écrire.
7. **Plateforme de modèles.** Coût et quota du stockage privé « non relevés » (l. 116-117) et débit en écriture non mesuré : à lever
   avant le GO, comme le devis le dit ; ajouter la licence du modèle pour des poids dérivés rangés en privé (une ligne).
8. **Durée attendue hors délai de destruction.** 12,72 h de course, 12,93 h facturées : ajouter ≈ 0,2 h à l'attendu (≈ 0,5 USD).
9. **Détails.** Fin de course 05:31:55Z au journal, 05:31:53 au devis (l. 47). En-tête : « écriture vers 08:15 UTC » (l. 4) alors
   que le fichier et son compagnon datent de 08:04 UTC et que cette contre-lecture commence à 08:05 UTC : heure à corriger par
   `date -u`. « 932 documents pleins » est juste, mais le pire cas du devis v12 compte 1 000 passages : sans effet.
10. **Redémarrage du conteneur de la session (l. 107-108).** Bien porté. Ajouter : si la session est absente à la fin, la machine
    attend, facturée, la relecture des empreintes et la révocation de la clé ; dire qui détruit et quand (la minuterie reste le filet).
11. **Cas mixte du critère (l. 84-86).** R aux mêmes octets et S différent (ou l'inverse) tombe dans « octets différents » : l'écrire,
    et ranger chaque lentille avec sa propre mention.

## Niveau des décisions
Les quatre décisions sont bien des nœuds de Lazar (dépense de calcul, compte et dépôt chez un tiers, clé) ; « rien ne part » comme
défaut est conforme. Manque une décision, ou un préalable explicite, sur le statut de la seconde mesure (M-3) : c'est un écart possible
à un verdict scellé et accepté, donc un nœud. La recommandation de la variante B reste défendable (≈ 3 USD attendus de plus), mais pour
ses vraies raisons (comparaison des mesures), pas pour « aucune comparaison possible » en variante A (M-1).
