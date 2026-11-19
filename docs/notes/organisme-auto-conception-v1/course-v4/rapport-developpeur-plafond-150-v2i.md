# Rapport du développeur — plafond d'arrêt 150 USD, seuils internes relevés d'autant, conservation des réponses brutes (v2i, lanceur v9)

Développeur unique de la version (modèle L′), 19 novembre 2026. **Rien n'a été lancé en réel** : aucun appel à un fournisseur, aucune dépense, aucun relais réel.

## Verdict

Prêt pour la contre-lecture (modèle K) : configuration v5 (S17 150, sacrifiables 151, relais Claude 150, étapes protégées inchangées), lanceur v9 (ligne de GO et mot de reprise à 150 USD exactement ; garde des seuils au haut ; enveloppe de conservation devant chaque commande externe ; inventaire de fin scellé quelle que soit l'issue), épreuve v9 ; au haut du devis v2i, la vraie classe `BudgetV56` lance la proposition, l'aiguillage **et les juges** ; essais 307 + 93 + 17 passés (et 37 de la sonde ; v6 à v8 passent encore) ; essai à blanc v9 code 0.

## 1. Plafond 150 USD et seuils (mot de Lazar « Course à 150 USD (Recommandé) »)

- **Changement minimal** : S17 120 → 150 ; étapes sacrifiables 121 → 151 (au-dessus de S17, retirées par construction comme avant) ; relais Claude 120 → 150 ; rien d'autre dans la configuration (`configuration-course-auto-conception-v5.json`, `3f662ee8…`). Les étapes protégées gardent leurs plafonds de relais (45, 15, 30) et attendus (19, 3, 7) : les seuils de la règle d'A1 (S17 − plafond de relais de l'étape) montent **d'autant**, + 30 : plafond dur de la proposition **140** (était 110), aiguillage lancé si cumul ≤ **135** (105), juges si cumul ≤ **120** (90). Relever aussi les plafonds d'étape n'était pas nécessaire : au haut, chaque plafond dur souple (max(relais ; S17 − cumul − attendus restants)) couvre déjà le coût de l'étape.
- **Preuve au haut par la vraie classe `BudgetV56`** (orchestrateur épinglé `a41b7b50`, `pole/budget_v56.py` `3a672ace…`, chargé sans écrire de code compilé), calcul v2i (`1f43d531…`) :

| étape | cumul avant | seuil | plafond dur | coût au haut | état |
|---|---|---|---|---|---|
| proposition | 0 | 150 − 45 | **140,00** | 70,03 | jouée |
| aiguillage | 70,03 | ≤ 135 | **72,96** | 20,46 | jouée |
| juges | 90,49 | ≤ 120 | **59,50** | 47,32 | **jouée** (v4 : non mesurée) |
| étiquettes | 137,81 | ≤ 150 | 12,18 | 0 | jouée |
| passe « tableau », fusions | — | — | — | — | retirées |

  Course au haut 137,81 ≤ 150. Sous la configuration v4, la même classe rend « juges : non mesuré (budget) » (le constat du devis v2h). Estimation : tout lancé (cumul avant les juges 48,05). Carbon au pire (aiguillage au haut) : juges non lancés (120,52 > 120). Argon et Carbon au pire : proposition coupée à 140 (C13).
- **Garde du lanceur** : `lecture_a1` rejoue la règle d'A1 sans l'orchestrateur (refus d'une étape réductible) ; `garde_seuils_au_haut` refuse le départ si, au haut du devis v2i (`HAUT_DEVIS_V2I_USD` 70,031788 / 20,46 / 47,322), la proposition, l'aiguillage ou les juges ne sont pas lancés ou sont coupés. Les essais la comparent à `BudgetV56` sur 18 cas (3 configurations × 6 scénarios), états et plafonds durs étape par étape ; le calcul du devis la compare aussi (« d'accord » sur les 4 scénarios).

## 2. Conservation des réponses brutes (R-3661, ajout au périmètre)

- **Choix de forme** : une enveloppe de conservation **neuve et unique**, `scripts/enveloppe_conservation_reponses_v1.py` (`c7a3e0dd…`), mise par le lanceur (`envelopper_commandes`) **entre la garde de crédit v5 et chaque commande externe** — Argon (proposeur et juge, par `appel-argon-sans-troncature-v1.sh`), Carbon (`appel-carbon-synchrone-v1.sh`), Astra (`commande_astra_v1.py`). Plutôt que trois enveloppes par espèce, parce que : les déclarations doivent rester exactement `["bash", enveloppe]` pour Argon et Carbon (gardes de réglage, ligne du juge comparée à la v5, empreintes épinglées par la pièce de départ, sonde de Carbon au réglage de la course) ; l'orchestrateur ne passe aux commandes qu'un environnement minimal (le dossier de conservation ne peut leur être donné que par la ligne de commande que le lanceur construit) ; une seule enveloppe sert les trois espèces avec le même code, essayé une fois. Les réglages, enveloppes et commandes contrôlés restent intacts ; l'enveloppe est ajoutée **après** tous les contrôles.
- **Ce qu'elle fait** : refus avant tout appel si le dossier est absent, relatif, un lien, pas un dossier ou non inscriptible (code 2, rien de lancé) ; sinon passe la consigne, attend la commande, puis **avant de rendre** écrit, dans un dossier par appel réservé par `mkdir` exclusif (`ÉTIQUETTE-appel-NNNN`), `…-lot-LL-HORODATAGE-reponse.bin` (sortie standard, octet pour octet), `…-erreur.bin`, `…-entetes.json` (rôle, modèle demandé, plafond, lot, appel, horodatage, durée, code, tailles et SHA-256 ; jamais l'environnement) ; écriture atomique (temporaire, `fsync`, lien dur, aucun écrasement, relecture de l'empreinte) ; **écriture impossible → appel arrêté** : code 9, réponse non rendue, la ligne `{"texte": "", "cout_usd": <coût déclaré>, "erreur": …}` garde la dépense comptée (sans coût lisible : rien, l'orchestrateur compte le plafond de session).
- **Lanceur v9** : crée `conservation-reponses-v1` sous la sortie de la course (hors des dossiers de sessions ; le dossier maison de l'orchestrateur est cette sortie, d'où les transcriptions de l'outil Claude dans `.claude`, gardées) ; à la fin, sur tout chemin (fin, nœud, arrêt, échec du lanceur — y compris l'orchestrateur qui ne part pas), `inventaire-conservation.json` scellé dans le dossier du run (conservation, sorties de l'orchestrateur, transcriptions, journaux, arrêts de crédit, base des sessions lue au manifeste de fin de l'orchestrateur) ; un échec d'inventaire est dit au manifeste de fin et rend un échec ; rien n'est supprimé.
- **Épreuve v9** : même enveloppe pour Argon juge (dossier dans la sortie de l'épreuve), inventaire (sortie de l'épreuve, `$HOME/.claude`) dans le rapport.
- Non traité (réserve) : un appel tué au délai par l'orchestrateur (arrêt du groupe de processus) ne laisse rien ; les requêtes et réponses HTTP des fournisseurs restent dans les commandes et relais épinglés (non modifiés). Rien n'a été touché sous `archives-reponses-modeles/` ni dans `scripts/archiver_courses_auto_conception_v4_v6_v1.py` (non suivis, non ajoutés).

## 3. Devis v2i

Estimation 59,03 USD (course 55,94 ; épreuve 1,18 ; sonde de Carbon 1,86 ; sonde d'Astra 0,05 ; conservation 0) ; haut de la course 137,81 (tout lancé) ; au pire **161,05** (150 + 5 + 6 + 0,05). Parts au pire : Claude (Minuit) 150, Gemini 150, Astra 66,55. Reste net de Minuit ≈ 199,03 > 150 ; ≈ 49,03 au pire après la course. Juges lancés tant que cumul avant eux ≤ 120 : Argon et Carbon ensemble ≤ ≈ 87,07 (aiguillage estimé) ou ≈ 70,02 (aiguillage au haut).

## 4. Pièces (empreintes)

| pièce | sha256 |
|---|---|
| `scripts/lancer_course_auto_conception_v9.py` | `1b47c1cf097e4cba290223223655d5ac63707dfeaec032be929930d30fde9b12` |
| `course-v4/additif-preenregistrement-course-auto-conception-v2i.md` | `1433b6a98a0fce4fad74e79465b69acd0b5ebb797fe3f26890179de70015d71b` |
| `scripts/epreuve_temoins_auto_conception_v9.py` | `5be161fa35e339d171399a3ba2a2c927cd517fba42c745306fd867a4b3e3c69b` |
| `scripts/enveloppe_conservation_reponses_v1.py` | `c7a3e0dddd622019a14129ff7f661eb463021200ac0c685b99357eaa3bc4bb9e` |
| `course-v4/configuration-course-auto-conception-v5.json` | `3f662ee80e12db7af79428c0bd2b0efe7e560a6a36c440c322343003fe2cc4f8` |
| `course-v4/piece-de-depart-gabarit-auto-conception-v2i.json` | `e54056955bbd0316e044e62427301e65f5de819510fd12b7757cf1bcea2b57d2` |
| `course-v4/calcul-devis-course-auto-conception-v2i.py` / `.json` | `8120b61c…` / `1f43d53185ba4c93043e038c968c9a62245c2ae86f51c9754a3b42cd1a79743b` |
| essais lanceur v9 (307), épreuve v9 (93), enveloppe de conservation (17) | `af71a7b4…`, `943bd2ca…`, `4aea1902…` |

Les empreintes du devis et des commandes v2i sont dans leurs compagnons `.sha256` (elles ne peuvent se citer elles-mêmes).

## 5. Essais (R5)

- **Portés de la v8** (lignes, relais, crédits et alertes à 150 ; les essais propres à la v8 portés sur le module v8 quand ils l'essaient) ; artefacts neufs aux anciens plafonds : ligne de la course à 120 (et 90, 45) refusée, relais Claude à 90 et 120 refusé, porte de plafond à 120 refusée, montant de l'orchestrateur à 120 refusé, configuration v4 refusée, cumul au-delà de 150 → code 4, reste net de Minuit ≤ 150 → code 3.
- **Seuils** : sains (v5 : tout lancé ; seuils 140/135/120 contre 110/105/90 en v4) ; artefacts (juges à 61, aiguillage à 80, proposition à 151 : non lancés ; S17 135 : juges coupés ; étape réductible refusée) ; égalité avec `BudgetV56` sur 18 cas ; mutations attrapées (garde non appelée, coupure non lue, seuil non lu).
- **Conservation** (17 essais de l'enveloppe) : réponse conservée **identique** à la réponse rendue (octets non UTF-8 compris), en-têtes, lot, juge sans lot, code rendu, numéros exclusifs sous six appels simultanés, passage dans la garde de crédit v5 ; refus avant tout appel (dossier absent, relatif, lien, fichier, non inscriptible, étiquette ou usage refusés : la commande n'est pas lancée) ; **écriture impossible → arrêt** (dossier retiré pendant l'appel : code 9, réponse non rendue, coût déclaré compté ; sans coût lisible, rien sur la sortie) ; jamais d'écrasement ; environnement jamais recopié ; mutations attrapées (conservation sautée, erreur avalée). Au lanceur : commande enveloppée dans l'ordre garde → conservation → commande, refus d'un réglage à moitié ; réponse d'Astra conservée identique et inventoriée, transcription de l'outil Claude inventoriée et gardée ; conservation impossible dans la course (appel arrêté, texte non servi) ; **inventaire écrit même sur issue en échec** (orchestrateur code 2, cumul au-delà de 150, orchestrateur qui ne part pas) ; base des sessions inventoriée et gardée ; mutations attrapées (inventaire sauté, conservation non insérée).
- **Épreuve v9** : 93 passés (fonctions identiques à la v8 sauf `charger_lanceur`, `refuser_si_rapport_existe`, `reel` ; `reel` = la v8 plus la seule conservation, vérifié ; mutation sans conservation attrapée).
- Essai à blanc v9 (composition entière) code 0, 110 cartes, juges joués, montant requis 150, seuils au haut « joués », inventaire scellé (0 erreur ; dossier de conservation vide : moteur simulé, aucune commande externe) ; épreuve hors ligne v9 : « témoins éprouvés hors ligne ».

## 6. Points ouverts

1. Contre-lecture (modèle K) à faire : `course-v4/contre-lecture-tentative-plafond-150-v2i-auto-conception.md`, qui cite en entier l'additif v2i (`1433b6a9…`) et le lanceur v9 (`1b47c1cf…`).
2. Lignes de GO neuves : course **150 USD** (« auto-conception », « tentative neuve »), épreuve 5 USD (« témoins »), sonde de Carbon 6 USD (« sonde », « Carbon »).
3. Forme de la conservation : une enveloppe unique mise par le lanceur plutôt que trois enveloppes par espèce (§ 2) ; à confirmer par la mère. Les sondes de Carbon et d'Astra (programmes v1 inchangés) ne passent pas par elle (leurs rapports portent les champs techniques).
4. Réserves inchangées : Argon proposeur sans sonde réelle à ce réglage ; comptage de la pensée dans la sortie à mesurer par la sonde de Carbon ; au pire des deux espèces Gemini, proposition coupée à 140 ; la clé Minuit peut descendre à ≈ 49 USD (affinage ensuite sur ce reste ou une recharge).
5. Écart mineur aux règles permanentes dans cette session : une commande a ouvert un heredoc vide (`python3 - <<'EOF'` sans contenu, aucun effet) ; aucun autre écart (aucun réseau vers un fournisseur, aucune clé lue, rien d'ouvert sous les dossiers interdits ; l'orchestrateur est resté propre).
