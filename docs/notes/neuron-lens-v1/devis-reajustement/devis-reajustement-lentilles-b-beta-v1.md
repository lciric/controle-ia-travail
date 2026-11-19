# Devis du réajustement de nos lentilles R et S (lecture par lentille neuronale, Llama 3.1 8B Instruct), pour les ranger et les faire entrer dans le programme — v1

- Auteur : session des lentilles (`session_013QMaykLXtozHttcSQ4ke1s`), branche `claude/brave-galileo-jhp684`, 2026-11-19 (relevé de prix
  à 08:03:02 UTC ; écriture vers 08:15 UTC).
- Origine : mot de Lazar « a, prépare le devis du réajustement » (2026-11-19), en réponse à la décision « comment faire entrer nos lentilles
  dans le programme », option a (réajuster à l'identique puis ranger). Accord préalable de Lazar sur le verdict de la tranche :
  `lecture-b-beta/accord-lazar-verdict-b-beta-v1.md` (`8469add5…`).
- Statut : **devis, aucune dépense engagée**. Rien ne part sans ligne de GO de calcul neuve (nœud de Lazar), sans les préalables du § 5
  et sans la contre-lecture de ce devis (R2).

## 1. Pourquoi
Les deux lentilles ajustées par la tranche close (course `20261118-164930-neuron-lens-b-beta`, verdict « partiel » accepté) **n'existent
plus** : la décision de lancement (GO-2026-11-18-02, lieu L1, « lentilles non rangées ») les laissait sur la machine louée, détruite le
2026-11-19 à 05:45:00Z. Il ne reste que leurs empreintes et leurs mesures. Pour qu'une expérience du programme s'en serve, il faut les
refaire et les ranger.

Ce que la course a laissé pour vérifier qu'on refait **les mêmes** lentilles (pièces versées, empreintes vérifiées au rapatriement) :

| pièce | empreinte | taille |
|---|---|---|
| fichier d'ajustement de R, `r-llama-3.1-8b-instruct-L32-dclm-T128.pt` (`b-beta-ajustement-R.json`) | `31061d6c6c4b521c43d4710f9b660184b285467a065dadb5fc48e48c6d48c64c` | 8 455 720 309 octets |
| fichier d'ajustement de S, `s-llama-3.1-8b-instruct-L32-dclm-T128.pt` (`b-beta-ajustement-S.json`) | `aac70eef8f57b5d4423e5c8f8b2e77033b15077d95ef5a81894dbe3e0436e2b8` | 8 589 938 049 octets |
| exports de R (fichiers `safetensors` par couche, manifeste, format du code voisin et format publié) | une empreinte par fichier dans `b-beta-export.json` | — |
| corpus d'ajustement (lignes 0 à 999, 932 documents pleins) | `rows_sha256` `a6afd972eeaa3566a28d07216efaf75624fda20293c5fab3b7af39277aaf93b3` | — |
| code de course (dépôt réduit) | commit `5e5cb65b4daf8726ebe1c4032a836b850de7ea2f` | — |

Le texte gelé dit l'ajustement « déterministe à l'ordre des documents près (aucun tirage) » (`texte-gele-tranche-b-beta-v1.md`, l. 464).
**Non établi** : que la carte rende les mêmes octets d'une machine à l'autre (ordre des réductions en virgule flottante). Une égalité des
empreintes est donc possible, pas acquise ; d'où le critère d'identité du § 4 et la variante B.

## 2. Deux variantes

**Variante A — ajustement seul, puis rangement.** Montage ; ajustement de R ; export ; ajustement de S ; empreintes comparées à celles du
tableau ; copie des deux fichiers d'ajustement et des exports vers le lieu de rangement ; empreintes vérifiées à l'arrivée ; destruction.
Aucune mesure refaite.

**Variante B — la course rejouée à l'identique, plus le rangement.** La commande de la tranche (v8) rejouée entière avec le même lanceur
(seuls changent le GO attendu, le nom de la branche de résultats et une étape de copie ajoutée après l'export de S) : toutes les mesures B-1
à B-7 sont refaites sur la nouvelle machine. Elle donne, en plus des lentilles rangées, une **seconde mesure indépendante** du verdict
« partiel » — utile parce que deux verdicts tiennent à une marge de l'ordre de l'effet du matériel (lecture contre pilotage : 3 pôles à la
couche 8 ; deux codes : une couche sur 21) — et une comparaison qui tient même si les octets diffèrent.

## 3. Durées et coût

Durées **mesurées** sur H100 SXM par la course du 18 au 19 novembre (relevés horodatés de l'amorce, `controles-b-beta-v1.log`) :
montage jusqu'au début de l'ajustement de R 1 h 14 (16:48:55 → 18:03:15) ; ajustement de R 18 414 s (5,12 h) ; export 78 s ; ajustement de
S 18 065 s (5,02 h) ; activations, comptes, comparaison, passe, pilotes, `measure`, `score`, grandeurs, lectures, déclencheurs et verdicts
1 h 19 (04:12:35 → 05:31:53) ; course entière 12,72 h. Copie de ≈ 17 Go (plus les exports, de l'ordre de 8 Go de plus, non mesurés) :
≈ 12 min à 200 Mbit/s (débit montant exigé ; l'offre retenue en annonce 1 744), estimée.

| bloc | attendu | pire cas | source du pire cas |
|---|---|---|---|
| montage | 1,25 h | 2,5 h | deux fois le mesuré |
| ajustements R et S, export | 10,2 h | 13,1 h | pire cas du devis v12 (6,56 h par lentille) |
| suite de la course (variante B seulement) | 1,3 h | 2,6 h | deux fois le mesuré |
| copie et vérification au lieu de rangement | 0,2 h | 0,5 h | moitié du débit exigé |
| **variante A** | **11,7 h** | **16,1 h** | |
| **variante B** | **13,0 h** | **18,7 h** | |

**Prix** : relevé `releve-prix-vast-h100-20261119T080302Z-v1.tsv` (08:03:02 UTC, script v3 en lecture seule) : **une seule offre vérifiée
sous 4 USD/h au filtre complet**, Japon, offre 59816165, **2,3713 USD/h avec 200 Go**, trafic sortant et entrant 0, débit montant 1 744
Mbit/s, fiabilité 0,9917 ; la suivante est à 4,0990 (États-Unis). Les offres changent d'heure en heure : le relevé est refait dans l'heure
qui précède la création (garde reprise de la v8).

| | attendu à 2,37 | pire cas à 2,37 | pire cas au prix exigé de 2,62 |
|---|---|---|---|
| variante A | ≈ 27,7 USD | ≈ 38,2 USD | ≈ 42,2 USD |
| variante B | ≈ 30,7 USD | ≈ 44,3 USD | ≈ 49,0 USD |

À quoi s'ajoutent 1,0 USD de frais fixes réservés (trafic) et, avec le lieu L2, le stockage (non relevé ; § 6).

**Plafonds proposés** (mêmes formules que la v8 : compte rendu à 60 %, arrêt dur à 90 %, minuterie = (0,9 × plafond − 1,0) / prix lu) :
- variante A : **plafond 50 USD** ; compte rendu 30,0 ; arrêt dur 45,0 ; minuterie 16,8 h au prix exigé (au-dessus du pire cas de 16,1 h),
  18,6 h à 2,37 ;
- variante B : **plafond 58 USD** ; compte rendu 34,8 ; arrêt dur 52,2 ; minuterie 19,5 h au prix exigé (au-dessus du pire cas de 18,7 h),
  21,6 h à 2,37.

**Perte de la machine** : comme à la v8, arrêt, aucune reprise sans devis neuf. Le lieu de rangement ne reçoit les lentilles qu'à la fin
(aucune copie de sauvegarde en cours de route, pour borner la durée d'une clé d'écriture sur la machine) : une perte avant la copie coûte
ce qui a été dépensé, au plus l'arrêt dur.

## 4. Critère d'identité (à sceller avant la création, contre-lu : R1, R2)
Écrit ici en projet ; il devient une pièce scellée à part avant tout lancement.
1. **Mêmes octets** : empreinte du fichier d'ajustement de R égale à `31061d6c…` **et** celle de S égale à `aac70eef…` → « mêmes
   lentilles » ; on range.
2. **Octets différents** (variante B seulement) : on compare, sur la nouvelle course, les valeurs écrites par `score` et les verdicts aux
   valeurs de la course du 18 ; seuil d'accord proposé : écart absolu ≤ 0,03 sur chaque valeur décisive (effet du matériel mesuré entre deux
   cartes, texte gelé, « Provenance des chiffres ») et **mêmes verdicts** pour B-1 à B-7 → « lentilles équivalentes » ; on range, avec cette
   réserve écrite. Sinon → « lentilles différentes » : on range quand même (le travail est payé), marquées non équivalentes, et nœud de
   Lazar avant tout usage ; la lecture de la nouvelle course passe par un lecteur neuf sur un plan scellé, comme pour la tranche.
3. **Octets différents** (variante A) : aucune comparaison possible au-delà des tailles ; les lentilles sont rangées marquées « réajustées,
   identité non établie ». C'est la raison principale de recommander la variante B.

## 5. Préalables, tous sans dépense (rien ne part sans eux)
1. **Ligne de GO de calcul neuve** (type « calcul », lue par le crochet de calcul), nommée par la mère sur le mot de Lazar ; variante, prix
   exigé, plafond et échéance écrits.
2. **Lieu de rangement** choisi par Lazar (§ 6), et son accès prêt.
3. **Clé d'accès au modèle** : la clé actuelle est gardée (mot de Lazar du 2026-11-19, `mot-lazar-cle-hf-garder-2026-11-19-v1.md`) ; la
   passer à cette machine neuve est un mot de Lazar à part, dans la ligne de GO (§ 6, option recommandée : une clé à droits restreints
   unique pour la lecture du modèle et l'écriture au seul dépôt de rangement).
4. **Crédit du loueur** au moins égal au plafond, en plus des autres lignes ouvertes sur le même compte, constaté avant la création (11,30
   USD à 07:04Z relevé par la mère : **recharge d'au moins ≈ 50 à 60 USD nécessaire**) ; budget journalier de 100 euros (mot de Lazar).
5. **Code** : étape de copie vers le lieu et vérification des empreintes à l'arrivée **à écrire**, essayée sur un cas sain et un artefact
   (R5), contre-lue ; lanceur v4 et amorce v4 (GO attendu, branche de résultats `calcul/neuron-lens-reajustement-v1`, étape de copie ;
   pour la variante A, arrêt après la copie) ; commande v9 contre-lue ; essai à blanc refait.
6. **Critère d'identité** du § 4 scellé et contre-lu.
7. **Leçon du 19 novembre portée** : un redémarrage du conteneur de la session tue la minuterie et la garde ; la veille les réarme sur
   l'échéance absolue (prévu par la v8 et joué le 19 à 00:52Z) ; la minuterie v4 et la garde v4 restent du côté de la session.

## 6. Lieu de rangement (choix de Lazar)
Taille : ≈ 17 Go pour les deux fichiers d'ajustement (moyennes et moitiés), plus les exports de R ; au-delà de la limite de l'hébergeur de
code (100 Mo par fichier).
- **L2 — dépôt privé de modèles chez la plateforme de modèles** (Hugging Face), créé par Lazar sous son compte. La machine y pousse à la
  fin, puis on relit les empreintes depuis la session. Exige une clé d'écriture sur la machine pendant toute la course (elle part à la
  création). **Option recommandée** : une seule clé neuve à droits restreints (lecture du modèle à accès contrôlé, écriture sur ce seul
  dépôt), à la place de la clé actuelle sur la machine ; elle se révoque après la copie sans toucher à la clé gardée. Coût du stockage
  privé : **non relevé**, à vérifier sur la page de la plateforme avant le GO.
- **L3 — une machine de Lazar** : Lazar tire les fichiers depuis la machine louée pendant qu'elle se facture (sa présence est requise,
  sans secret sur la machine), ou la machine pousse vers la sienne (un accès de sa machine sur la machine louée).
- (L1, aucun lieu, n'a pas d'objet ici.)

## 7. Décisions demandées à Lazar (par la mère)
**Décision 1 — variante.** Enjeu : avoir des lentilles dont on peut prouver qu'elles sont celles qui ont été jugées. Options : A (≈ 28 USD
attendus, plafond 50 ; identité seulement si les octets sont égaux) ; B (≈ 31 USD attendus, plafond 58 ; identité ou équivalence mesurée,
et seconde mesure des marges minces). **Recommandation : B**, confiance 0,7 (≈ 3 USD et ≈ 1,3 h de plus pour une identité vérifiable dans
tous les cas). Défaut sous 48 heures : rien ne part.

**Décision 2 — prix exigé et plafond.** Recommandation : prix exigé 2,62 USD/h (le même que la tranche ; l'offre du relevé est à 2,37),
plafond 58 USD (variante B) ou 50 (variante A). Défaut : rien ne part.

**Décision 3 — lieu de rangement et clé.** Recommandation : L2, dépôt privé sous le compte de Lazar, une clé neuve unique à droits
restreints, révoquée après la copie ; confiance 0,6 (L3 évite toute clé d'écriture mais demande la présence de Lazar pendant la copie).
Défaut : rien ne part.

**Décision 4 — recharge du crédit** d'au moins le plafond retenu, avant la création.

## 8. Ce que ce devis ne fait pas
Il ne décide pas de l'usage des lentilles dans le programme : chaque expérience qui s'en servira le dira dans son préenregistrement
(R1) ; toute modification d'un texte déjà scellé (par exemple la lecture des sondes de l'étape B bis, qui ne lit aujourd'hui que la
lentille publique) passe par une version nouvelle, contre-lue, et un mot de Lazar.
