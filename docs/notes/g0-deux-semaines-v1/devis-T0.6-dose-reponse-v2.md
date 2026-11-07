# Devis — T0.6, organisme (ii) à dose réglable, courbe dose–réponse et test croisé — v2

- Écrit le 2026-11-07 (heure relevée par `date -u` à l'écriture, fille 10, session de développement, Claude Sonnet 5.5) sur demande de la session mère (R-1706). **Remplace le devis v1 pour la ligne d'engagement** (`docs/notes/g0-deux-semaines-v1/devis-T0.6-dose-reponse-v1.md`, `6da6decfe1d4c71ce68cfc7db6bcc8538507c977234e6b3e36c7917a394b1994`, qui reste tel quel, R12). Aucune dépense engagée par ce document.
- **GO** : GO-2026-11-02-28 (« H200 ou A100 », **plafond 200 USD inchangé**, échéance 2026-11-16) et GO-2026-11-07-02 (carte de repli de la course, option (b) de Lazar, R-1700) : `registres/go.md` l. 262 au commit `c1a03f0` de `main` (fichier `ddbd296a7f59e2ad…`).
- **Ce qui change par rapport au v1** : (1) le stockage passe de 0,03 à **0,08 USD/h** (mesuré **0,0417** pour 150 Go) ; (2) la règle de carte de la course devient : recherche d'une A100 SXM4 de 80 Go conforme toutes les 15 minutes pendant 3 heures (12 recherches, 0 USD), puis **repli sur la H200 NVL** (≤ 4,70 USD/h, ≥ 140 Go) ; (3) les prix sont ceux des lectures du 7 novembre ; (4) l'heure de marche ne change pas (11,5 à 17,1 h au débit de P3, la H200 NVL supposée au même débit : **débit non mesuré**, v1) ; (5) le disque arrêté jusqu'au verdict est recalculé à la nouvelle borne ; (6) le prix `dph_total` d'une offre lue avec `--storage` **contient déjà** le stockage (R-1692) : on ne l'ajoute pas une seconde fois.

## Sources des chiffres

| donnée | valeur | source |
|---|---|---|
| heures de marche | **11,5 à 17,1 h** (génération 3,57 ; évaluation 6,43 ; distillation 0,46 à 6,14 ; divers ≈ 1) | devis v1, « Attendu (plan (b), A100) » (`6da6decf…`) |
| durée d'un épisode | 40,2 s (P3, A100) | devis v1, « Sources » (`puissance-t06-v2.txt`, `87813a36…` section 4) |
| prix A100 SXM4, stockage compris | rang 1 : **1,1083 USD/h** (fiabilité 0,9937, stockage 0,0417) ; borne **1,30** | `registres/decisions.md` R-1699 (l. 1657, commit `c1a03f0`, fichier `05e46e7bee1a712d…`), lecture de la fille 6 le 7 novembre à 17:35:43Z, `--storage 150` ; borne : P3 (devis v1) |
| prix H200 NVL, stockage compris | 8 offres, 7 à stockage ≤ 0,08 ; rang 1 **3,3617** USD/h (fiabilité 0,9906, stockage 0,0417, CUDA 13,2, 64 cœurs) ; rangs 2 à 5 : 3,6417 à **4,0417** ; borne 4,70 | `registres/decisions.md` R-1699 (l. 1657) |
| règle de la carte de repli | A100 d'abord, 12 recherches à 15 minutes (3 h), puis H200 NVL ≤ 4,70 USD/h, ≥ 140 Go, stockage ≤ 0,08 ; plafond 200 inchangé | `registres/go.md` l. 262 (GO-2026-11-07-02) ; `registres/decisions.md` R-1700 (l. 1658) |
| stockage mesuré | **0,0417 USD/h** pour 150 Go (instance 59589344 : carte 0,3617 + stockage 0,0417) ; E2 a montré la borne de 0,03 inapplicable | `registres/depenses.md` l. 380 (fichier `9981efc3e035aef7…`) ; compte rendu d'E2, `docs/notes/g0-deux-semaines-v1/compte-rendu-e2-t06-2026-11-07-v1.md` (`5a6debc5…`) |
| coût réel de l'épreuve E2 | **0,600 USD** pour cinq instances | `registres/depenses.md` l. 379 à 384 |
| disque arrêté jusqu'au verdict | 72 h au plus | devis v1 (« Disque ») |
| téléchargement | ≤ 1 à 2 USD (descente ≈ 20 Go, au plus 40, à ≤ 0,05 USD/Go ; montée 1 à 2 Go) | devis v1 (« Téléchargement ») |
| pire cas sur hôte lent | 34,2 h de carte (deux fois plus lent), 9,1 h A100 avant une erreur de mémoire à la distillation | devis v1 (« Pire cas », P1 et P3) |

## Attendu

| poste | A100 SXM4 (cas nominal) | H200 NVL (repli, fenêtre de 3 h épuisée) |
|---|---|---|
| calcul | 11,5 h × 1,1083 à 17,1 h × 1,30 = **12,7 à 22,2 USD** | 11,5 h × 3,3617 à 17,1 h × 4,0417 = **38,7 à 69,1 USD** |
| disque arrêté jusqu'au verdict (72 h × 0,0417 mesuré) | 3,0 USD | 3,0 USD |
| téléchargement | 1 à 2 USD | 1 à 2 USD |
| **attendu** | **≈ 17 à 27 USD** (v1 : 14 à 27) | **≈ 43 à 74 USD** (GO-2026-11-07-02 : 41 à 74, arrondis de la mère) |

Le disque en marche est compris dans `dph_total` (R-1692) : il n'est pas ajouté.

## Pire cas (sous le plafond ; l'arrêt à 200 USD cumulés est la seule garde de dépense)

| scénario | hypothèses | USD |
|---|---|---|
| P1' hôte A100 deux fois plus lent, 1,30 USD/h | 34,2 h × 1,30 = 44,5 ; disque arrêté 72 h à la borne de 0,08 = 5,8 ; téléchargement 2 | **≈ 52** |
| P2' = P1' + une relance complète sur A100 (erreur de chaîne avant tout épisode d'évaluation, débit moitié) | + 21,4 h × 1,30 = 27,8 ; téléchargement 2 | **≈ 82** |
| P3' repli H200 NVL, hôte deux fois plus lent | 34,2 h × 4,0417 = 138,2 ; disque arrêté à la borne 5,8 ; téléchargement 2 | **≈ 146** |
| P4' erreur de mémoire à la distillation sur A100 (9,1 h × 1,30 = 11,8 ; disque et téléchargement 2,3), puis course complète sur H200 NVL, hôte lent | 11,8 + 2,3 + 138,2 + 5,8 + 2 | **≈ 160** |

Au-delà de **180 USD** cumulés, toute relance reste un nœud de Lazar avant dépense (v1). Pire cas du devis : **≈ 160 USD**, sous le plafond de 200.

## Hors devis
Inchangé (devis v1, « Hors devis ») : P3-bis (GO à part) ; le juge 8B de T0.8 s'il tourne sur une carte (GO à part) ; la règle du coût et le prédicteur sur les traits du texte de T0.8, sur processeur ; la course de (i) à doses p < 1. Les recherches de la fenêtre (12, 0 USD) et la lecture à 0 USD par le code la veille de la course ne coûtent rien. Les épreuves E2 (0,600 USD réels) et E3 (plafond 4,3 USD) relèvent du GO-2026-11-06-01 (5 USD), pas de ce devis.

## Ligne d'engagement révisée (`registres/depenses.md`, à écrire par la session au lancement, 11 novembre au plan daté)

« engagement : T0.6 organisme (ii), dose–réponse et test croisé (GO-2026-11-02-28, plafond 200 USD ; GO-2026-11-07-02) : lanceur `scripts/lancer_t06_v9.sh` (empreinte `<<EMPREINTES_CODE_T06>>`), commit `<<COMMIT_CODE_T06>>` ; préenregistrements de T0.6 et de T0.7 scellés (`<<EMPREINTE_PREREG_T07>>`) ; recherche d'une A100 SXM4 80 Go ≤ 1,30 USD/h toutes les 15 minutes pendant 3 heures (12 recherches, 0 USD), sans A100 conforme repli sur la H200 NVL ≤ 4,70 USD/h, ≥ 140 Go ; dans les deux cas ≥ 16 cœurs effectifs, ≥ 128 000 Mo de mémoire vive, disque ≥ 150 Go, fiabilité ≥ 0,98, CUDA ≥ 13,0, stockage ≤ 0,08 USD/h, téléchargement ≤ 0,05 USD/Go ; attendu ≈ 17 à 27 USD sur A100, ≈ 43 à 74 USD sur H200 NVL ; pire cas ≈ 160 USD ; arrêt par identifiant à 200 USD cumulés ; crédit Vast.ai relu à la création (recharge automatique, R-283) ».
