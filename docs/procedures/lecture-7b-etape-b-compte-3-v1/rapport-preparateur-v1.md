# Rapport du préparateur — lecture de 7b et étape B de T0.7 hébergées par le compte 3 — v1

- **Rédacteur** : préparateur neuf, sous-agent de la session mère `session_01QPDgKgACWyCkCN8HjqwNXy` (modèle A) ; ni lecteur ni
  juge d'aucun verdict ; aucune sortie de 7a, 7b ou T0.7 ouverte (noms, tailles et empreintes seulement) ; aucune machine,
  aucune dépense, aucun commit. Heures (`date -u`) : début 2026-11-14T11:02:05Z ; fin en dernière ligne.
- **Pièces rendues** (dossier `docs/procedures/lecture-7b-etape-b-compte-3-v1/`, toutes scellées) : `prealables-v1.md` ;
  `commande-compte-3-v1.md` ; ce rapport ; le contrôle à blanc `controle_a_blanc_etape_b_compte_3_v1.py`, son essai et sa
  sortie (28 sur 28), sa sortie sur l'état actuel ; l'attestation `attestation_qui_a_lu_quoi_compte_3_v1.py`, son essai et sa
  sortie (9 sur 9) ; la répétition jouet du bloc C2 et sa sortie (7 sur 7) ; la consigne du contre-lecteur.

## Verdict

1. **Lecture de 7b remettable après trois gestes de la mère** : contre-lecture de la commande (modèle C), liste « qui a lu
   quoi » v2, consigne scellée du lecteur de la table A ; aucune clé de registre ne lui manque.
2. **Étape B : pas avant mardi 17 au plus tôt** ; chemin critique : la pièce « mots et coût » (code inexistant, 1,5 à 2 jours
   avec contre-lecture), puis le plan scellé de B bis (lundi ou mardi, R-2716). Contrôle à blanc du lecteur de registre de T0.7
   sur l'état actuel : **aucune clé refusée ; manquent `AUDIT-FUITES-T07` et `ISSUE-MOTS-ET-COUT-T06`**.
3. **Contre-lecture demandée non faite** : je n'ai aucun outil pour créer un sous-agent ; consigne prête pour la mère.

## Erreurs, écarts, constats (une ligne chacun)

- **Extracteur** : `scripts/extraire_mesures_epreuve_t06_v1.py` ouvre `lecture-sondes-t06.json` (l. 33-34, 40, 54-56), que T0.6
  scellé (l. 771) ferme jusqu'au contrôle d'ouverture v2 ; R-2704 ne lève que l'embargo de P3-bis ; nœud N-A.
- **`resume.json` de 7b porte `ligne_B` et `ligne_C`** (ordre de 7b, l. 32) : exclu de toute remise.
- **`lecture_v3 etape-b` refuserait la configuration v8** (`n_plancher` 800 contre 200 exigé par `lecture_v2`, l. 205-206) :
  la commande joue `lecture_v4 etape-b` (écart de nom déjà déclaré, `lecture_v4.py` l. 18-19 ; ordre de l'étape A v2, § 9).
- **`CODE-T07` refuse tout `src/controle_ia/` différent de C7** (`code_t07_v1.py`, l. 103-107) : le code de la pièce ou de B bis
  sous `src/controle_ia/` de `main` ferait refuser l'étape B depuis `main` ; la commande joue depuis une arborescence
  détachée à C7.
- **L'étape B importe torch** (`sondes/familles.py`, l. 26) : ≈ 6 Go d'environnement dans le conteneur du compte 3 s'il n'en
  a pas ; le contrôle à blanc, lui, n'en importe pas.
- **La liste « qui a lu quoi » v1 nomme le compte 3** (l. 77, « aucune exclusion déclarée ») : attestation adaptée (l'arrêt
  sur toute ligne du compte, copié du compte 2, aurait arrêté la commande) ; répétée : la session mère, présente dans la
  liste, est bien arrêtée.
- **Commit du découpeur absent du clone de ce conteneur** (`c7484c43…`) : à récupérer par refspec avant l'audit.
- **Texte scellé de T0.7, l. 2183** : c'est « la session mère » qui lit l'état BA-L2 avant l'étape B, alors qu'elle est exclue
  des lectures de 7b : nœud N-C.
- **Phase B de la commande non remettable** (gabarit) : la pièce n'existe pas ; une version 2 portera ses marqueurs.

## Nœuds pour Lazar

**N-A — Extraction des mesures de 7b.** *Décision* : ne pas lancer l'extracteur sur 7b, et laisser le lecteur de la table A
lire lui-même les fichiers de service. *Enjeu* : l'extracteur lit des clés de `lecture-sondes-t06.json` avant
`ISSUE-MOTS-ET-COUT-T06` et sans contrôle d'ouverture v2 : écart à T0.6 scellé (l. 771) ; il est aussi interdit par le brief du
compte 3 (l. 41). *Options* : (a) pas d'extracteur ; le lecteur lit `episodes-t06.json`, `distillation-t06.json` et les
traces — avantage : lettre du texte, aucun code neuf ; inconvénient : les mesures de Mahalanobis et les durées par couple
(sondes, tables B et C) ne sont pas rapportées avec la table A. (b) extracteur tel quel (lecture de R-2704) — avantage : relevé
complet tout de suite ; inconvénient : écart à un texte scellé, ouverture partielle d'un fichier fermé. (c) extracteur v2 sans
le fichier fermé — avantage : relevé imprimé ; inconvénient : développeur et contre-lecture, 2 à 3 heures. *Recommandation* :
(a), confiance 0,7. *Défaut sous 48 heures* : (a) (la commande l'applique déjà).

**N-B — Un ou deux agents pour la table A.** *Décision* : un seul sous-agent neuf lit la table A dans l'ordre du point 7 et
prononce le verdict. *Enjeu* : l'ordre de 7b (l. 374) écrit « lue … par un lecteur neuf […], verdict par un sous-agent neuf
(R13) » et la carte « lecteur du coût et juge neufs » ; la mère demande « un sous-agent lecteur neuf par verdict » ; la table A
est déjà calculée par la chaîne gelée (`resultat.lecture.table_A`). *Options* : (a) un agent — avantage : rapide, rien de neuf
à calculer ; inconvénient : la relecture des textes de l'audit R4, si elle se déclenche, est faite par celui qui juge. (b) deux
agents (lecture, puis verdict) — avantage : lettre de l'ordre de 7b ; inconvénient : deux à trois heures et une consigne de
plus. *Recommandation* : (a), confiance 0,6. *Défaut* : (a).

**N-C — Qui lit l'état de la ligne BA-L2 avant l'étape B.** *Décision* : la mère lit, par programme, le seul état de BA-L2
dans `base-a-t08.json` et le consigne (ligne `<<R_BA_L2>>`) avant toute étape B. *Enjeu* : T0.7 scellé (l. 2183) confie ce geste
à « la session mère » ; la mère est exclue des lectures et verdicts sur 7b ; si BA-L2 s'applique, ton mot est exigé avant
l'étape B. *Options* : (a) la mère, un seul état lu par programme — avantage : lettre du texte scellé ; inconvénient : la mère
apprend un état de validité calculé sur 7b (témoin positif de la base (A)). (b) la session du compte 3 lit l'état et le
transmet — avantage : la mère ne voit rien de 7b ; inconvénient : écart à la lettre du texte (ton mot). (c) le lecteur B le
lit dans ses pièces — avantage : rien de plus ; inconvénient : l'étape B serait déjà ouverte, contraire à « avant ».
*Recommandation* : (a), confiance 0,6. *Défaut* : (a).

**N-D — Le lot NARCBench du compte 3 pendant les deux verdicts.** *Décision* : le lot du compte 3 peut avancer en parallèle,
mais aucune de ses sessions n'ouvre le texte scellé de T0.7, `SONDES-T07` ni aucune sortie de T0.7, 7a ou 7b avant le verdict
scellé de l'étape B. *Enjeu* : le brief du compte 3 lie son lot à T0.7 (entrée : le brouillon 4 « bras descriptif de T0.7 »,
l. 22 ; ce brouillon lit `SONDES-T07` si présent, PD5) mais n'en tire qu'une exclusion des lecteurs de P3-bis (l. 28) ; aucun
texte n'exclut ce compte comme hôte (réponse ci-dessous). *Options* : (a) lot en pause jusqu'aux verdicts — avantage :
compte vierge, sans discussion ; inconvénient : la reproduction NARCBench glisse de trois à quatre jours. (b) lot en parallèle
sous cet interdit, attesté par la liste avant chaque remise — avantage : rien ne glisse ; inconvénient : discipline à tenir
dans deux sessions du même compte. (c) aucune contrainte — avantage : aucun ; inconvénient : un compte exposé à T0.7 hébergerait
le lecteur de T0.7. *Recommandation* : (b), confiance 0,65. *Défaut* : (b).

**N-E — Grille de lecture de G0 et premiers verdicts de critère.** *Décision* : lire 7b et l'étape B sans attendre la grille
de G0 scellée. *Enjeu* : la carte (§ 2, l. 64) veut la grille scellée « avant le premier verdict de critère » (soupçon R4 sinon)
; aucun texte de T0.6 ni de T0.7 n'attache ses verdicts à cette grille ; la mère veut 7b « tout de suite ». *Options* : (a) ne
pas attendre — avantage : 7b dimanche, chemin critique tenu ; inconvénient : la grille sera scellée après deux verdicts
qu'elle lira. (b) attendre la grille (au plus tard le 17) — avantage : aucune prise au soupçon ; inconvénient : 7b glisse de deux
à trois jours, l'étape B aussi. *Recommandation* : (a), confiance 0,65. *Pas de défaut* (touche la porte, R-796 (3)) ; la
commande ne l'attend pas.

## Décisions de routine proposées à la mère (elle décide et consigne)

- **D-1** : la pièce « mots et coût » est exécutée par la session du compte 3 (elle porte les données ; elle scelle sans
  ouvrir), sur la branche `verdict/t06-mots-et-cout-compte-3-v1` ; sorties laissées sur cette branche (comme celles de l'étape A
  sur `donnees/t07-etape-a-v1`), lignes inscrites sur `main`.
- **D-2** : l'audit des fuites reste lancé par la mère, comme le dit sa consigne scellée (§ 3), auditeur du modèle C ; la mère
  récupère le découpeur par refspec et les deux fichiers de 7b par liste positive.
- **D-3** : répétition de bout en bout des phases A et C sur une copie du dépôt et des branches jouets (comme les 32 sur 32 de
  P3-bis), au moins pour la phase C (appel unique) ; je n'ai répété que les blocs 1, 2, A4, C6 (sur un dossier jouet) et C2 (dépôts jouets, 7 sur 7).
- **D-4** : liste « qui a lu quoi » v2 avant la remise (préparateur ; hôte et lecteur de P3-bis ; rédacteurs à venir).
- **D-5** : aucune ligne de verdict de 7b ou de l'étape B dans `registres/scellements-v1.md` (clé sans marque déclarée : refus
  de l'étape B ; essais A1 et A6).
- **D-6** : consignes scellées des lecteurs A et B (rédacteur neuf modèle A, contre-lecture modèle C), sur le modèle de la
  consigne du lecteur de P3-bis ; elles ne doivent pas exiger d'autres pièces que celles des blocs A3 et C5, sinon version 2.
- **D-7** : registre propre de B bis `registres/etape-b-bis-v1.md`, clé `SCELLEMENT-PLAN-BBIS` (ou d'autres noms, remplis aux
  marqueurs `<<REGISTRE_BBIS>>`, `<<CLE_PLAN_BBIS>>`).

## Le lot NARCBench exclut-il le compte 3 comme hôte ? Non, sur les textes écrits ; une réserve (N-D)

- Brief du compte 3 (`154b6927…`) : l. 1 et 16-20, lot « veille datée et reproduction NARCBench sur activations publiées »,
  processeur seul ; l. 22, entrées dont `prereg/brouillon-narcbench-8b-descriptif-v1-brouillon4.md` ; **l. 28, seule exclusion
  liée à T0.7 : « Si le texte NARCBench exige d'ouvrir le texte scellé de T0.7 : […] ce compte est alors exclu des lecteurs de
  P3-bis »** (P3-bis est rendu) ; l. 41, interdits de la session du lot (dont 7b et l'extracteur), qui ne visent pas une session
  neuve commandée autrement (exception écrite de la commande, R-2711 (2)).
- Plan multi-comptes (`3b1bda25…`) l. 120-121 : mêmes exclusions ; aucune sur l'étape B.
- Brouillon 4 de NARCBench (`96995d60…`) l. 1 : « bras descriptif de T0.7 » ; l. 129-131 : « **Aucun verdict** : un bras
  descriptif ne fait franchir aucune porte (N-026) ; rien n'entre dans le critère 3 de G0 » ; l. 80, 203 et 360 : il lit
  `SONDES-T07` s'il est inscrit (PD5) — c'est là l'exposition possible.
- Règle R13 : le juge n'est ni auteur du préenregistrement ni de l'analyse ; le texte NARCBench n'est ni l'un ni l'autre pour
  T0.7, et le lecteur est un sous-agent neuf, pas le compte.
- État : aucune branche `lot/compte-3-v1` au distant (11:12Z) ; liste v1, l. 77 : « rien déclaré », « aucune exclusion
  déclarée ». **Conclusion** : hôte admissible ; la seule réserve est une exposition future par une autre session du même compte
  (N-D).

## Réserves

1. **Contre-lecture non faite par un sous-agent du modèle C** : mon outillage ne crée pas de sous-agent ; créer une session
   distante serait une machine de plus, hors de ma consigne. Consigne prête (`consigne-contre-lecture-commande-compte-3-v1.md`,
   liste explicite des fichiers, questions Q1 à Q12) ; verdict de contre-lecture : **non disponible** ; aucune version 2 faite.
   À ma propre relecture, j'ai corrigé : le bloc C7 écrit en entier (au lieu d'un `sed` sur le bloc A5), le contrôle des
   gabarits du bloc F (un « < » d'un rapport l'aurait arrêté), l'arrêt explicite du bloc C3, la reprise de C2 sur des fichiers
   déjà placés, le retrait du fichier « mots et coût » au nettoyage.
2. **Commande non répétée de bout en bout** ; syntaxe vérifiée (`bash -n`, 18 blocs) ; blocs 1, 2, A4 et C6 joués sur un
   dossier jouet (A4, C6 : messages sans marqueur restant ; bloc 2 : la session mère est bien arrêtée par l'attestation) ;
   bloc C2 répété sur dépôts jouets (7 sur 7 ; limite : transport local). Les blocs A1, A2, A3, A5, C0, C1, C3, C4, C5, C7 et F
   ne sont éprouvés que le jour même.
3. **Phase B** : gabarit ; ses marqueurs attendent le code de la pièce (version 2 de la commande, contre-lue).
4. **Interprétations déclarées** : « T0.8 scellé » que lit la pièce = la base (A) scellée à part (R-2175, R-2193) ; la ligne
   `LECTURE-T08-BASE-A` est exigée par la base (A) (plan point 3) mais non par le module : contrôlée par le bloc C0 seulement.
5. **Données sur `main`** : `lecture-t07.json` et les sorties de la pièce restent par défaut sur leurs branches (D-1, section 15
   de la commande) ; si la mère les recopie dans `main`, elle le fait par blob, sans les ouvrir.
6. **Exposition de l'hôte** : il voit les codes de sortie, les noms, et, sur un refus de l'étape B, la ligne `REFUS-T07` du
   journal (motif de garde) ; jamais la sortie de l'étape B ni une pièce ; il est exclu ensuite de l'analyse des verdicts, de B
   bis, de T0.8 et de G0.
7. **Disque et quota du compte 3 inconnus** ; ce conteneur avait 4,7 Go libres à 11:48:49Z ; la phase C peut demander ≈ 6 Go d'environnement.
8. **Têtes de branches et registres lus le 2026-11-14 entre 11:12:24Z et 11:48:49Z** ; la mère écrivait en parallèle (`main`
   local passé de `7a66e7ab` à `c9056003` pendant ce travail, sans effet sur les clés lues) ; tout se revérifie le jour même par les
   blocs.
9. **Mes lectures** (à inscrire en v2 de la liste) : `prealables-v1.md`, § 6.

## Calendrier réaliste (jugements, non opposables)

| jour | mère | compte 3 | Lazar | condition |
|---|---|---|---|---|
| sam. 14, après-midi et soir | contre-lecture de la commande (modèle C, 1 h) et v2 ; liste v2 (30 min) ; consigne du lecteur A (2 h + 1 h) ; commande du développeur de la pièce ; lancement de l'audit des fuites (découpeur, données de 7b ; auditeur modèle C 3,5 à 4,5 h) | — | nœuds N-A à N-E | — |
| dim. 15 | contre-lecture du fichier d'audit (1 à 1,5 h), copie, ligne `AUDIT-FUITES-T07` ; pièce : écriture sur données factices ; consigne du lecteur B | **phase A** : blocs 0 à A5 (≈ 30 min de gestes, lecteur 2 à 4 h), verdict A poussé ; bloc F | ouvre la session, colle la commande ; GO sur le verdict A après recopie | commande v2, liste v2, consigne A |
| lun. 16 | contre-lecture de la pièce (modèle C, 0,5 j), ligne `CODE-MOTS-ET-COUT-T06` ; commande v2 (phase B) ; plan de B bis scellé et sa ligne (R-2716 : lundi ou mardi) | **phase B** (si la pièce est prête en fin de journée) : exécution < 2 h, sorties poussées | — | pièce contre-lue |
| mar. 17 | blobs des sorties, état de BA-L2 (N-C), lignes `LECTURE-T08-BASE-A` puis `ISSUE-MOTS-ET-COUT-T06`, ligne `<<R_BA_L2>>` | **phase C** : C0 à C7 (environnement avec torch ≈ 15 min, placement ≈ 5 min, contrôle à blanc, appel unique en minutes, lecteur B 2 à 4 h) ; bloc F | mot si BA-L2 s'applique ; GO sur le verdict B | plan de B bis scellé ; consigne B |
| mer. 18 | recopies, liste v3 | marge (étape B si la pièce ou B bis a glissé) | — | — |
| jeu. 19 à sam. 21 | marge ; B bis suit son propre plan (relecture forcée, entraînement, lecture) | — | dépense de B bis sur devis | — |
| dim. 22 | échéance : verdicts de 7b et de l'étape B scellés depuis plusieurs jours ; B bis au plus tard ce jour | — | — | — |

Glissements possibles : pièce en retard d'un jour (étape B mercredi) ; BA-L2 qui s'applique (mot de Lazar) ; arrêt de l'audit
(nœud) ; place disque du compte 3 ; quota. Le modèle B revient le vendredi 20 à 15:00Z : il n'est sur aucun chemin.

## Empreintes des pièces (ce rapport excepté ; chacune égale à son compagnon, vérifié par programme)

| pièce | sha256 |
|---|---|
| `prealables-v1.md` | `0cd96b629cb181246a8c2b15ad235719d72eaea64650552e0d482b630506c129` |
| `commande-compte-3-v1.md` | `21d891c57a9e0b6577b5d7b0c2deeb33fc52ec54e25005f61b79149cc6f548dc` |
| `consigne-contre-lecture-commande-compte-3-v1.md` | `23f4767d618b512fe3c661e04c1962c73bc2178f4f5aad8369ddbe85de1e4da0` |
| `controle_a_blanc_etape_b_compte_3_v1.py` | `eb19ef6a56cd34913e644aa8aa4a76a65a9ddf96f22796b42f8f1c6198caa275` |
| `essai_controle_a_blanc_etape_b_compte_3_v1.sh` | `c6fa5ac9b0950945dbdc1b9406762be12d0815048bc56ede2fad73d8e88126d1` |
| `essai-controle-a-blanc-etape-b-compte-3-sortie-v1.txt` | `8570610f30579dc7f8ea04f32dcba03f618426deea8b631221486018c41a8134` |
| `controle-a-blanc-etat-actuel-sortie-v1.txt` | `3ed16bc5301880aba0a82289f96fbe671a268c3ce05c1afcc0273488111d7003` |
| `attestation_qui_a_lu_quoi_compte_3_v1.py` | `639d85d6b3fb73008f64e40516455f13f1a04db13097fbbfee68f41e9ff575ca` |
| `essai_attestation_compte_3_v1.sh` | `a88ae9bbbc3281afdf7e4abc5501b48711aa0a2acb467f4886b5629c809c4c62` |
| `essai-attestation-compte-3-sortie-v1.txt` | `499b9fe40134022f775d0e4da7c7675757e16e68c4a120d04c56376a9e641f3f` |
| `repetition_bloc_c2_jouet_v1.sh` | `235d593052ca59d9bcc525e42bcc10408256a322c38148bfa43f625f34030b1b` |
| `repetition-bloc-c2-jouet-sortie-v1.txt` | `ea097fa290f3555b85401f84097db9988fc28c288c6dc4df84b0a3b81aca5abf` |

Fin de rédaction : 2026-11-14T11:50:07Z (`date -u`).
