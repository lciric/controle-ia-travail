# Rapport du lecteur neuf (R13) — témoin de Bailey, verdict du run « confirmation »

## En-tête

- Run : « confirmation ».
- Consigne suivie : `/home/user/controle-ia-travail/runs/temoin-bailey-v1-20261111/cloture-confirmation-v1/consigne-lecteur-b-v1.md`, empreinte `efe289d7815c4e8e5d5366ab2f69b5c73a0cfdc9072ad518aa0f306203f89131`, vérifiée « OK » par son compagnon avant de l'ouvrir.
- Étape 1 : ni `/home/user/controle-ia-travail/runs/temoin-bailey-v1-20261111/cloture-confirmation-v1/rapport-lecteur-b-v1.md` ni son compagnon `.sha256` n'existaient avant l'écriture de ce rapport.
- Sortie lue : `/home/user/controle-ia-travail/runs/temoin-bailey-v1-20261111/cloture-confirmation-v1/sortie-b-v1.json`.
- Empreinte de la sortie vérifiée avant de l'ouvrir (étape 2) :
  - commande `cd "$(dirname /home/user/controle-ia-travail/runs/temoin-bailey-v1-20261111/cloture-confirmation-v1/sortie-b-v1.json)" && LC_ALL=C sha256sum -c "$(basename /home/user/controle-ia-travail/runs/temoin-bailey-v1-20261111/cloture-confirmation-v1/sortie-b-v1.json).sha256"` ; ligne rendue : `sortie-b-v1.json: OK` ;
  - commande `sha256sum /home/user/controle-ia-travail/runs/temoin-bailey-v1-20261111/cloture-confirmation-v1/sortie-b-v1.json` ; ligne rendue : `0ce212425c6ddec3281e4e0f3efd968800461b0ca012e65b056979c00a925b82  /home/user/controle-ia-travail/runs/temoin-bailey-v1-20261111/cloture-confirmation-v1/sortie-b-v1.json` ; ses 64 premiers caractères sont égaux à l'empreinte consignée `0ce212425c6ddec3281e4e0f3efd968800461b0ca012e65b056979c00a925b82`.
- Heure UTC : 2026-11-19 11:56:32 UTC (rédaction du rapport).
- lecteur neuf (R13) ; aucun autre fichier lu que ceux de la consigne.
- Précisions sur ce que j'ai lu ou vu :
  - fichiers ouverts : la consigne ; son compagnon `consigne-lecteur-b-v1.md.sha256`, pour la seule vérification de son empreinte que la session m'a demandée avant de l'ouvrir ; `prereg/temoin-attaque-publiee-bailey-v1.md`, lignes 324 à 353 ; `prereg/temoin-attaque-publiee-bailey-v1-addendum-7-run-de-confirmation.md`, section « 3. Lecture » seule (lignes 132 à 332, extraites par programme sans afficher le reste du fichier) ; la sortie et son compagnon ;
  - l'existence des deux chemins du rapport a été testée chemin par chemin, sans lister aucun répertoire ;
  - la sortie a été lue par affichage de ses lignes et par l'analyseur JSON de la bibliothèque standard de Python (`python3 -I`, aucun code du dépôt), pour vérifier les champs transcrits et l'absence de clé en double ; aucun code du dépôt n'a été joué, hors le scellement de l'étape 5 ; aucun dossier de `runs/` n'a été lu ;
  - le `CLAUDE.md` du dépôt (consignes permanentes du programme) m'a été montré d'office par l'environnement, sans que je l'ouvre ; il ne nomme pas le témoin de Bailey et ne porte aucune valeur de ce run ; le message de lancement de la session ne porte aucune valeur de la sortie ;
  - aucun verdict, aucune sortie, aucun rapport ni dossier de lecture de l'autre lecteur, aucun registre, aucune passation ni aucune note écrite après la clôture ne m'a été montré.

## Champs techniques lus (étape 3)

- `version` : `lecture_scellee_v3`, comme l'exige l'étape 3.
- `dossier` : `/home/user/controle-ia-travail/runs/temoin-bailey-v1-20261111/confirmation-assemblee-v1`.

## Issue

`aboutie`

## Transcription (issue « aboutie »)

- **Verdict** (`lecture.verdict`, recopié mot pour mot, réserves comprises) :

  Effet reproduit sur le banc des auteurs, au régime publié. Réserves : longueur de suffixe différente des 16 jetons de l'article (écart 10).

- **K′** (`lecture.k_prime`) : 72
- **Régime** (table des lignes 329 à 338 du préenregistrement ; K′ ≥ 71) : publié
- **Compte du bilan** : 72 (journal des durées transféré de principal-relance : 72 lignes ; le bilan de la conduite v16 ne porte pas de compte) tours complets, rapporté à côté, sans effet sur le verdict (§ 3).
- **Audit de symétrie porté par la sortie** :
  - `lecture.audit.defaut` : `false`
  - `lecture.audit.defauts` : `[]` (aucune entrée)
  - `lecture.audit.clos` : `true`
  - `lecture.audit.mentions` : `[]` (aucune mention « à examiner »)
- **Interruptions** (`lecture.interruptions`, telles quelles) :

```json
[
 {
  "cause_arret": "état absent (reconstitué à la lecture)",
  "code_retour": 1,
  "execution": "principal",
  "gardes_tombees": [],
  "k_prime": 17,
  "lignes_tronquees_ignorees": [],
  "reconstitue": "à la lecture",
  "role": "première exécution, rapportée comme interrompue"
 }
]
```

- **Lignes tronquées ignorées** (`lecture.lignes_tronquees_ignorees`, telles quelles) : `[]`
- **Exécutions** : 1 élément dans `executions` (`n` : 1, `aboutie` : `true`) ; aucun élément qui n'ait pas abouti, donc aucun `echec`, `message` ni `lieu` à rapporter.

## Verdict prononcé

Selon les critères gelés (`lecture_v8.valider`, `lire` avec `analyse_v3.graines()["reechantillonnage"]`, audit de symétrie : ceux que la sortie porte), le verdict du run « confirmation » est : Effet reproduit sur le banc des auteurs, au régime publié. Réserves : longueur de suffixe différente des 16 jetons de l'article (écart 10). K′ = 72 ; régime : publié.

Rien n'a été recalculé ni interprété au-delà de cette transcription ; aucune autre valeur de la sortie (`calcul`, `intervalles`, `rapportees`, `R_att`, `J`) n'est transcrite : elles restent dans la sortie, qui fait foi.
