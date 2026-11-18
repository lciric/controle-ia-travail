# Rapport du développeur — correctif v9 de la course d'affinage des idées des mentors

- Écrit le 2026-11-18T22:21:44Z (`date -u +%FT%TZ`) par le modèle L', sur demande de la session principale. Branche neuve `prep/affinage-v9-compte-organisme-v1`, partie de `dd139d7e` (correctif v8) ; rien de la v8 n'est modifié (ajouts seuls, R12).
- **Aucune dépense, aucun appel réseau vers un fournisseur, aucun relais réel, aucun lanceur sans `--a-blanc`.** Exécuté : essais hors ligne, un essai à blanc (moteur simulé de l'orchestrateur épinglé, dossier neuf hors dépôt). Aucune valeur de clé lue ; orchestrateur en lecture seule (`a41b7b50…`, `-B`). Rien sous `diag/`, `donnees/`, `registres/`, `attestations/`.
- Entrée : la documentation de Google sur la pensée, lue par la session principale (« sets the maximum number of tokens a response can generate, including thought tokens », coupure dure) tranche le point ouvert 2 du rapport v8 : la v8 aurait coupé chaque réponse de Carbon ; elle ne sera pas contre-lue. Décisions de la session principale sous l'autonomie de Lazar : option 1 (c) du rapport v8 (plafond par appel des proposeurs 3,00 USD) ; Astra : option 3 (a) (aléa accepté).

## Verdict du développeur

Fait comme demandé. Configuration v9 neuve (seul `plafonds_session.proposeur` change, 1,50 → 3,00) ; Carbon à `--max-sortie-jetons 32768 --provision-pensee-jetons 28672`, délais de la v8 (lot 1 620 s, requête 60 s, durée maximale 1 770 s sous 1 800 s). **Vérifié avec la vraie commande de `main`** (jouée hors réseau, ouvreur factice) : sous 3,00 USD, elle demande **32 768 jetons de sortie** sur l'entrée la plus longue (≥ 24 500 exigés) et rend un **pire cas de 2,571489 USD** (< 3,00) ; sous 1,50 elle n'en demanderait que 6 948 (le régime de la v8, désormais refusé par le lanceur). Préenregistrement v9 neuf : le v8 nomme le plafond par appel (1,50) et les réglages de Carbon.

Hypothèse (aucune), mesures, seuils (aucun), plafond d'arrêt (150 USD, GO-2026-11-18-14), composition, clé Claude (Minuit seule), orchestrateur, commandes épinglées, délais de Carbon : inchangés.

## Parts au pire par clé et ligne de GO

| clé (nom) | v8 | **v9** | dans la ligne (150 USD) ? |
|---|---|---|---|
| `RR_ANTHROPIC_API_KEY_MINUIT` (Claude : deux proposeurs, aiguilleur, premier juge) | 150 | **150** | oui |
| `GEMINI_API_KEY` (Argon 150 + Carbon 16 × 3,00) | 174 | **198** | **non : 198 > 150** |
| clé d'OpenAI, secret de réseau, `OPENAI_API_KEY` (Astra, 16 × 3,00) | 24 | **48** | oui |

**Une part dépasse ce que la ligne permet : la clé de Google, 198 USD.** Ce n'est pas une dépense possible : la part est la somme des bornes de deux relais, et la course entière reste bornée par le plafond d'arrêt de 150 USD (déjà 174 en v7 et v8). La clé part sous la dispense R-3237 (solde illisible), donc la part n'est confrontée à aucun reste lu ; si son solde devenait lisible, le lanceur exigerait un reste au-dessus de 198. Le relais d'Astra doit être lancé à `--plafond-usd 48` exactement (le lanceur exige l'égalité avec la part ; celui des commandes v8, à 24, est refusé) ; seize appels d'Astra coûtent au plus 16 × 1,73 = 27,66 USD par la formule de sa commande.

## Devis v9

Estimation **45,25 USD** (41,136 sans marge, inchangée) ; haut **141,59** (Carbon compté à son pire cas de 2,5715 par appel ; majoré de 25 % : 176,98) ; **pire cas 150** (plafond d'arrêt ; borne par les plafonds de session : 472). Plafond demandé : 150 USD, inchangé, aucune ligne de GO neuve.

## Pièces versées (scellées, compagnon `.sha256`)

| pièce | sha256 |
|---|---|
| `scripts/lancer_course_affinage_mentors_v9.py` | `b0c7c50d968b51c9ea76294bfcc0ccbd377e76ddefc3352f7734fa86ad5d3c93` |
| `course-v9/preenregistrement-course-affinage-mentors-v9.md` (épinglé) | `b24755fccdbb58906a21461c1dde7108f96aab73e12922a4f6fcc13265a54938` |
| `course-v9/configuration-course-affinage-mentors-v9.json` (épinglée) | `e7378f89ae39eacd169ff912526a8e998e4f01f0aba235eeaa0bf12e4b195d5d` |
| `devis-course-affinage-mentors-v9.md` | `23029a75acc7ab4ec2996b57e24c747d5216067c531da88f97dee0d25dbe567b` |
| `course-v9/commandes-exactes-course-affinage-v9.md` | `74eb71b222d7c7ab2920c35b9333b97bb0b82e7ca6c3f51066849b2f157b6ca9` |
| `tests/test_lancer_course_affinage_mentors_v9.py` | `621dcab77317f478fb2f5bf4446f2e3818a74bd56d4c5e5e240950fccaeb01b2` |
| `course-v9/declaration-relais-gabarit-course-affinage-v9.json` | `f7b66b186798f708b999d74e70a7f1aff8f04382df8829ef9aa6a728953dd491` |
| `course-v9/releve-credits-gabarit-course-affinage-v9.json` | `6278473ddc18e69d618a26dd1b0dd76120606de6bb9917abf0baf0c773dc6dcc` |
| `course-v9/releve-prix-claude-gabarit-course-affinage-v9.json` | `905f59d93bed242b1ce9910129cddd40312f2c0676235ec3736cb4bb8cffac06` |
| `course-v9/essai-a-blanc-v9/…` (15 fichiers) | leurs compagnons `.sha256` |

**Contre-lecture exigée par le lanceur v9** : `docs/notes/organisme-affinage-mentors-v1/course-v9/contre-lecture-preenregistrement-course-affinage-mentors-v9.md`, scellée, du modèle K, citant en entier `b24755fccdbb58906a21461c1dde7108f96aab73e12922a4f6fcc13265a54938` (préenregistrement v9) et `b0c7c50d968b51c9ea76294bfcc0ccbd377e76ddefc3352f7734fa86ad5d3c93` (lanceur v9), première ligne sous `## Verdict` exactement `Scellable.`.

## Ce que le lanceur v9 change

1. Pièce `configuration` épinglée : la configuration v9 (toutes les autres pièces inchangées, essai `test_v9_configuration_seul_le_plafond_des_proposeurs_change`).
2. `ARGUMENTS_COMMANDES["carbon"]` : seule différence avec la v8, `--max-sortie-jetons 32768` (au lieu de 16 384).
3. **Garde neuve** dans `controler_pire_cas_carbon` : sortie retenue par la commande ≥ **24 500** jetons sur l'entrée la plus longue et la plus courte (pensée observée 20 696 + réponse observée 3 410), sinon refus (« la réponse serait coupée (code 5) ») ; plus une vérification défensive du pire cas ≤ plafond de session (inatteignable par construction de la garde de la commande : pas de mutation possible, dit).
4. Parts au pire recalculées par le code existant (16 × plafond de session) : Astra et Carbon 48 ; clé de Google 198.
5. Chemins `course-v9/`, sorties `…-v9`, une seule course de v1 à v9 ; sondes lues aussi sous `course-v8/` (un seul rapport de sonde commune du jour admis).

## Essais

> **806 passed in 592.74s**, 0 skipped, 0 failed (252 v9 + 235 v8 + 175 v7 + 125 v6 + 5 v6b + 14 sonde commune), commande du § 4 des commandes v9.

- `tests/test_lancer_course_affinage_mentors_v9.py` : **252** essais — les 235 essais v8 portés (monde ajusté : relais d'Astra à 48 USD, parts 48 et 198, réserve d'Astra jusqu'à 3,00, artefacts « code 4 » à 70 000 jetons de provision, 50 000 de sortie minimale ou 100 USD par million, attentes du pire cas v9), plus 17 essais neufs v9 (paramétrages compris).
- La mutation de la garde du pire cas minimal (v8) reste attrapée : le mutant est refusé par la garde neuve de la sortie retenue, avec un autre motif ; l'essai l'accepte comme échec (défense en profondeur, dit en commentaire).
- Essais neufs v9 : configuration (seul le plafond des proposeurs change), arguments (seule la sortie maximale change), sortie retenue (saine ; 16 384, 24 499, provision 50 000 refusées ; borne 24 500 ; régime de la v8 refusé ; **mutation** `test_mutation_v9_sortie_retenue`), vraie commande sous 1,50 (6 948 jetons < 20 696), pire cas toujours ≤ 3,00 sur une grille, parts de bout en bout (48 ; 2,571489 au manifeste), relais d'Astra à 24 refusé, clé partagée 198 (reste 180 : alerte), devis v9, commandes v9 (Astra à 48, empreintes du lanceur, du préenregistrement et de la configuration).
- Les fichiers d'essais v8, v7, v6, v6b et de la sonde commune passent encore (inchangés).

## Essai à blanc v9

`--a-blanc` dans un dossier neuf hors dépôt : **code 0**, sortie d'erreur vide ; la vérification de l'orchestrateur épinglé (`--verifier-seulement`) accepte la configuration v9 (plafond servi `proposeur` 3,0) ; cinq espèces, 160 cartes, parts 150 / 150 / 48 / 48 ; base du devis 41,136, écart −35,536 ; `reglages_carbon_v8` au manifeste : sortie retenue 32 768, pire cas 2,571489 USD (1,285745 au prix du lot) ; acte de gel au nom du lanceur v9 et du préenregistrement v9. Versé sous `course-v9/essai-a-blanc-v9/`.

## Points ouverts

1. **Plafond dur de l'étape « proposition » : 60 USD** (configuration, inchangé, non demandé). Avec 3,00 par appel, le haut de la proposition au devis v9 est 76,36 USD : si Carbon échouait à chaque appel au pire cas (2,57 compté par échec) sans qu'A3 l'arrête, l'orchestrateur couperait l'étape (« non mesuré (budget) »), arrêt propre, écrit. A3 (trois échecs consécutifs) rend ce régime peu probable. Option, pour la mère : porter ce plafond d'étape à 70 (somme des étapes protégées 150 = plafond d'arrêt) dans une configuration suivante ; je ne l'ai pas fait (hors de la demande).
2. **Les autres proposeurs ont aussi 3,00 par appel** (plafond par rôle, non par espèce) : Astra demande désormais 32 768 jetons au plus (pire cas 1,73 USD par appel) ; Argon remplit son plafond selon sa propre garde ; une session Claude a un budget de 3,00. Les estimations restent celles du devis v6 (jetons), non mesurées sous ce plafond.
3. **Lecture de la documentation du fournisseur** faite par la session principale, non par moi (aucun réseau). Une note du dépôt (`commande_argon_v3d.py`, l. 260-261) dit avoir constaté, sur un appel synchrone d'Argon, que les pensées n'étaient pas comptées dans la sortie maximale : la v9 tient dans les deux lectures (sortie 32 768 ≥ 24 500, provision 28 672 ≥ 25 870). Une pensée au-delà de 28 672 rend le code 7.
4. Repris de la v8 : délai de lot borné à 1 620 s par l'orchestrateur épinglé (un relèvement demande un orchestrateur neuf) ; délai de requête 60 s ; 16 annulations par défaut au relais Gemini ; le 18 novembre, ne pas refaire de sonde ; essais datés du 18 au 30 novembre.
5. Le crochet d'isolement de l'arbre de travail a refusé une commande composée (sceller, indexer, vérifier) pendant la v8 ; rejouée en commandes séparées, sans contourner de permission. Aucun refus pendant la v9 jusqu'à ce rapport.

## Ce qui n'est pas vérifié

Aucun relais réel ni appel amont ; pensée de Carbon sur les consignes de l'affinage ; coût réel des proposeurs sous 3,00 ; commandes v9 écrites et relues, non jouées ; `runs/` du dépôt non lu.
