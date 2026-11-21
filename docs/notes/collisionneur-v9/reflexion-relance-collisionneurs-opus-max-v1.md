# Relance des collisionneurs sans perte : réflexion d'Opus 5.5 en effort maximal, v1

21 novembre 2026, 16:20Z ; classe C ; accord GO-2026-11-21-63. Lus : journaux, états et dépenses de la branche `runs/collisionneurs-reprise-minuit-v1` (af5a06cb), scripts, vérification de la v6 par Fable (523dda37…) ; aucune réponse de modèle, aucun appel, aucune clé.

## Verdict

Tout se reprend sans perte ni double paiement, mais il faut une v7 : garde corrigée par Fable, budget envoyé séparé de la provision, rejugement des deux réponses complètes déjà payées, repli par lot après une coupure. Astra n'entre pas dans un dossier commencé sans lui : il entre à part. Les mathématiques se débloquent en redonnant la ligne de 28.

## 1. Dossiers

| dossier | arrêt | gardé | reprise |
|---|---|---|---|
| adjudant …-114751 | fini | 15/15, 14,81 USD | rien |
| percée …-114810 | garde de dépense (code 6), tour III.2, Carbon | 9/15 ; réponse complète (fin `STOP`, marqueur, 44 101 pensées, sortie 55 125), payée 1,24 | rejugement, tour III.3 |
| dérive v2 …-131044 | idem (34 373 pensées, 1,04) | 9/15 | idem |
| antériorité …-131029 | flux coupé (code 5), tour III.3, Carbon, deux fois (180 s, 367 s) | 14/15 | troisième envoi, repli par lot |
| mathématiques …-093850 | code 5, tour III.2, Fable : refus « crédit insuffisant » dans le flux, compté 3,03 sans facture | 5/15 | tours III.2 et III.3 |
| but …-152615, fusionnée …-153256 | en marche (tours III.3, III.2) | 10/12, 7/12 | rien s'ils finissent |
| …-130555, dérive v1 …-095727 | — | tour III.1 partiel | jamais (doublons) |

Dopamine : critique de Carbon du 20, complète dans `essais/`, lisible à part.

## 2. Quel script

- v3 (850df311…) : relancer `etage3` saute les cellules valides mais renvoie la cellule arrêtée au même budget : paiement neuf ; or trois critiques croisées de Carbon sur sept le dépassent.
- v6 (3c6a4cfb…) : « à corriger » (Fable) ; une réponse complète y est encore jetée puis repayée.
- Reprise par une autre version : sûre (sonde de Fable, § 5) : `especes.json` identique, lettres inchangées, changement déclaré par `--reprise` et reconnu par `verifier`, même ligne. Conditions : ancienne session arrêtée et versée (jamais deux écrivains sur un journal) ; `verifier` avant et après ; note déclarant le réglage changé entre tours et les rejugements.

## 3. Réglage de Carbon

Où : `CATALOGUE` (v3 l. 139 ; v6 l. 167, 192) ; `thinkingBudget = provision` (v3 l. 793 ; v6 l. 887) ; garde dans `juger` (v3 l. 1276 ; v6 l. 1392) ; pire cas `cout_pire_garde` (v3 l. 1102).

Sur 19 réponses complètes au budget de 32 768 : pensées de 19 727 à 44 101 ; 16 sous le budget ; les trois dépassements sont des critiques croisées ; rapport maximal 1,35, non 1,22 ; texte 8 400 à 14 401 ; sortie au plus 55 125. Carbon réfléchit déjà jusqu'au bout : la garde coupait.

Recommandé : plafond 65 536 ; provision (seuil et pire cas) 49 152, soit 16 384 jetons de texte (règle de `CLAUDE.md`) ; **budget envoyé 32 768** ; garde V-1 (sortie facturée contre plafond plus provision, jamais pensées contre budget). Les 40 000 de Fable donneraient, au rapport 1,35, 53 840 pensées et 11 700 jetons de texte, sous la règle. Au-delà de 49 536 pensées : « long decode », pages non versées, conception à part.

Prix (page versée 40202cdd…) : Carbon et Argon 2 et 10 USD par million jusqu'au 30 novembre, 4 et 20 ensuite, pensées au prix de sortie, lot à moitié prix. Le script compte Carbon à 4 et 20 (à garder), Argon à 10 et 50 (cinq fois trop) ; un run compté 14,81 coûte environ 10,9.

Flux coupé : ni l'attente (600 s) ni le délai (5 400 s). À la première coupure, un autre flux de Carbon du même conteneur a tenu : une connexion est touchée (réinitialisation nue du mandataire qui perd son tunnel, `/root/.ccr/README.md`). Google ne reprend pas un flux coupé ; un appel non diffusé ferait pire. Remède : lot (`batchGenerateContent`, permis pour Carbon par la liste versée eeec19e8…), requêtes courtes, moitié prix.

## 4. Astra

Impossible dans les courses parties sans lui : `sceller_composition` refuse (code 1), et les lettres glisseraient (Astra en D, Carbon en E : les cellules de Carbon, …-D, passeraient pour celles d'Astra). Ne jamais toucher `especes.json`.

Permis sans écart : (A) Astra à part, consultation v6 (`--cle-openai OPENAI_API_KEY_2`) : conception sur les faits et la question scellés du dossier, puis critique des quatre conceptions ; environ 1,5 USD par question, lignes de l'accord GO-2026-11-21-52 ; une note dit ces pièces hors collisionneur et l'asymétrie. (B) Dossier neuf à cinq espèces : environ 15 USD comptés, au-delà des lignes, devis à Lazar. Recommandation : A. `OPENAI_API_KEY_2` manque sur ce compte (noms relevés) : Lazar l'ajoute.

## 5. Mathématiques

Le refus venait de `--ligne-usd 30` : un run garde sa ligne. Redonner 28 ; la garde par envoi refuse avant tout dépassement ; `devis-reprise` n'est qu'indicatif et pessimiste. Pire cas en v7 : 17,8 sans relance pour 21,77 restants. Accord GO-2026-11-21-23 à échéance le 22 : d'abord.

## 6. Devis (USD comptés ; réel environ 0,7 fois)

| dossier | pire cas v7 : sans relance / relances | reste : dossier / accord | attendu |
|---|---|---|---|
| percée | 9,2 / 14,9 | 17,7 / 17,3 | 5 |
| dérive v2 | 9,2 / 14,9 | 14,2 / 13,4 | 5 |
| antériorité | 2,5 / 4,9 (lot 1,2) | 13,3 / 11,8 | 0,8 |
| mathématiques | 17,8 / 29 | 21,8 | 10 |
| but, fusionnée | 0 s'ils finissent | 18,7 / 18,9 | — |
| Astra à part | 4 par appel | accord GO-2026-11-21-52 | 3 |

« Accord » retire les dossiers voisins et un envoi coupé non journalisé (0,45). Google : 16 USD restaient à 14:04Z (R-4553), plus de 4,4 réels dépensés depuis, 4 à 5 à prévoir : crédit à relever.

## 7. Plan

0. Maintenant, sans dépense : l'ancienne session finit (on ne coupe pas un envoi payé), verse, dit « plus rien ne tourne ». Un développeur Opus écrit la v7, Fable la vérifie. Lazar ajoute `OPENAI_API_KEY_2` et relève le crédit Google.
1. Session fille neuve sur ce compte, branche `runs/collisionneurs-reprise-v7-v1` tirée du dernier versement, deux courses à la fois, versement toutes les 5 minutes : dérive v2 et mathématiques (échéance le 22), puis percée et antériorité, puis but et fusionnée s'ils se sont arrêtés, puis Astra à part, puis les six couples en attente, sur devis.

Par dossier `D`, `S=docs/notes/collisionneur-v9/collisionneur_v9_v7.py` :

```
PYTHONPATH=src .venv/bin/python -m controle_ia.scellement verifier $S
.venv/bin/python -B $S verifier $D && .venv/bin/python -B $S devis-reprise $D --ligne-usd L
GO_ID=G .venv/bin/python -B $S etage3 ESPECES --cle-anthropic RR_ANTHROPIC_API_KEY_LUC --cle-openai OPENAI_API_KEY_2 --sortie $D --plafond-usd P --ligne-usd L --reprise [OPTION] 2>&1 | tee -a $D/journal-reprise-v7.txt
.venv/bin/python -B $S verifier $D
```

| dossier | ESPECES | L | P | G | OPTION |
|---|---|---|---|---|---|
| percée | `--fable --opus --argon --astra --carbon` | 28 | 27.5 | GO-2026-11-21-39 | `--rejuger-essai E3-T2-critique-croisee-E:1` |
| dérive v2 | idem | 24 | 23.2 | GO-2026-11-21-26 | idem |
| antériorité | idem | 28 | 26.4 | GO-2026-11-21-39 | `--repli-lot` |
| mathématiques | idem | 28 | 28 | GO-2026-11-21-23 | — |
| but, fusionnée | `--fable --opus --argon --carbon` | 28 | 28 | GO-2026-11-21-52 | selon l'arrêt |

Sans `--faits`, `--question` (scellés) ni `--accepter-absence kimi` ; la clé d'Anthropic, non scellée, est dite dans le journal versé.

## 8. Corrections de la v7 (Opus, puis vérification par Fable)

1. V-1 de Fable, texte exact (523dda37…, § 6).
2. Champ `budget` par espèce de Google, envoyé, journalisé, lu par `reglage_en_defaut` ; Carbon : budget 32 768, provision 49 152, plafonds 65 536.
3. Argon : plafonds 32 768 (liste versée), budget 8 192, provision 16 384 ; 65 536 seulement après un envoi d'essai ; prix 4 et 20, source citée.
4. Opus : plafond 64 000 dès le premier envoi (15 premiers envois sur 23 coupés à 22 000 puis repayés : 8,83 USD perdus).
5. `--rejuger-essai CELLULE:N`, sans réseau : essai `REFLEXION_HORS_PROVISION`, fin `STOP`, marqueur, usage lu, modèle conforme, entrée sous la garde, écart nul, sortie sous plafond plus provision ; cellule écrite depuis la réponse scellée ; ligne « rejugement » au journal ; admise par `verifier`. Essais : sain, artefacts (fin `MAX_TOKENS`, marqueur absent, sortie au-delà, sceau changé), idempotence, aucun envoi.
6. `--repli-lot` : après une coupure chez Google, l'essai suivant passe par `batchGenerateContent` (relevés courts, délai de l'espèce, modèle contrôlé), au prix du lot, compté au pire s'il échoue.
7. Refus de crédit dans le flux d'Anthropic, usage nul : échec sans envoi, coût zéro (3,03 et 1,29 USD comptés à tort).
8. `--accepter-absence` refuse ce qui n'est pas une cellule.
9. Essai de la remarque 1 de Fable ; essais sur copies des quatre dossiers (vérification, devis, envois comptés).

Réserves : 19 réponses ; coupures sans cause établie ; lot jamais essayé.
