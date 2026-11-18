# Devis — organisme d'idéation sur les organismes discrets, lignée Kimi (lanceur v9) — v1

Écrit le 18 novembre 2026 par la session de relance des organismes discrets (`session_01XJ6MgpChR1JWSMBxSQcf3c`), sur les mots
de Lazar, verbatim : « oublie pas kimi dans les courses » ; « s'il marche pas on n'arret pas les curses, on continue sans
lui » (de Carbon). Même dispositif que les trois courses jumelles du devis v4 (`devis-ideation-organismes-discrets-trois-lignees-v4.md`,
`005c02eb…`) : mêmes pièces, Opus 5.5 en proposeur et juge internes, une passe, juge externe différé ; seule change la lignée
externe, Kimi (`kimi-k3.1-pro`).

## 1. Ce qui part

Une course, lanceur `scripts/lancer_course_ideation_organismes_discrets_v9.py` (copie du v8 à une lignée), argument `kimi` ;
une relance au plus, seulement après un arrêt au contrôle (relevé ≤ 2,1 USD), comme au v8.

## 2. Prix

| modèle | entrée | sortie | source |
|---|---|---|---|
| Opus 5.5 | 4 | 20 | page de l'éditeur (lecture d'agent du 18 novembre, non empreintée ; inchangé depuis le devis v4) |
| Kimi K3.1 Pro | 2 | 10 | vérifiés le 30 octobre sur la page des prix de Moonshot (page `c62210a0…`), observés conformes à la facture (`docs/notes/ideation-organisme-v1/course-2/devis-course-2-et-pre-pilote-v4.md` l. 36) ; cache 0,20 compté au prix plein |

USD par million de jetons.

## 3. Bornes (identiques au v8, par course)

| poste | plafond |
|---|---|
| total Claude (proposeur Opus 2,0, juge Opus 2,0, contrôle 0,2) | 6,0 |
| proposeur externe Kimi | 1,5 |
| contrôle externe | 1,7 |
| juge externe différé (déclaré, jamais joué ici) | 2,5 |
| plafond d'une course (Claude 6,0 + exposition externe 3,2) | 9,2 |
| relance après arrêt au contrôle | 2,1 |
| **pire cas de la ligne = borne du lanceur v9** | **11,3** |

Relais : Claude (port 8787, celui des courses du v8, plafond 22 pour l'ensemble ; dépense relevée ≈ 0,1 USD à 06:40Z) ;
relais compatible OpenAI vers Moonshot (`relais_kimi_v4.py`, port 8789, plafond 5 USD, 12 appels, prix 2 / 10, cache 2).

## 4. Attendu

D'après la course Astra du jour (proposeur 0,38 USD pour 6 fiches, total 1,34 USD) et les prix de Kimi cinq fois plus bas :
**≈ 1 USD** (Claude ≈ 0,9 ; Kimi ≈ 0,1). Solde du compte Moonshot lu à 06:45Z par l'appel gratuit du fournisseur :
32,25 USD (`available_balance`).

## 5. Risques dits d'avance

1. Kimi a déjà épuisé 32 768 jetons en raisonnement sans rien rendre (14 novembre, `registres/depenses.md`) : l'enveloppe
   permet 98 304 jetons de sortie ; la commande réduit la sortie à ce que paie le plafond de session (1,5 USD), ou refuse
   sans envoi.
2. Coupure à 300 s d'une connexion muette (cause de l'échec de Carbon) : le relais Kimi v4 lit l'amont en flux ; Kimi
   envoie ses jetons de raisonnement au fil du flux (relais v3 du 30 octobre, même cause, corrigée ainsi).
3. Témoins : le juge interne Opus a échoué les deux témoins « éligibles » dans la course Astra (code 4, course écrite et
   illisible) ; le même juge, avec les mêmes témoins, le refera probablement ici : la course Kimi sera alors écrite,
   ses fiches validées, et illisible au sens de la règle scellée. C'est dit avant le départ.

## 6. Ligne de GO demandée

Périmètre contenant à la lettre « organisme d'idéation », « organismes discrets » et « lignée kimi » (garde du lanceur v9) ;
type calcul ; **11,3 USD** ; échéance 2026-11-22 ; Lazar.
