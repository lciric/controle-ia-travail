# Écarts du devis v3 du pilote « oracles plantés » : chiffres écrits à la main contre rejeu par script — v1

- Classe B (vérification d'instrument), 0 USD, processeur seul, aucun appel de modèle. Vérificateur : l'Opus 5.5 qui a rejoué le devis v2, le 22 novembre 2026. Rien n'est corrigé dans le devis ni dans le brouillon : ce texte rapporte.
- Pièces vérifiées : `prereg/mathematiques-nouvelles-v1/devis-pilote-generation-v3-brouillon.md` (`5c8a0f68518c1f335851c79d09a768b7b99d61c15b6406937cbd79b9fff9abe8`) ; P7, A4, A6, A7, A9 et effectifs de `preenregistrement-pilote-generation-v1-brouillon-3.md` (`e33d7bec1f9c606d0cac96836e3748a02cc50444bcde689165e1280d32b655bb`).
- Rejeu : `calculs_devis_pilote_generation_v3.py` (copie adaptée du script v2, qui reste intact) et `sortie-calculs-devis-pilote-generation-v3.txt`, même dossier, empreintes dans leurs compagnons `.sha256` ; lancé par `.venv/bin/python -I`. Tolérance 0,005 USD. Profils de jetons, heures de machine et forfait de fumée : supposés, nommés tels.

## Verdict
Un seul écart : le plafond d'appels du § 3 est écrit « 192,79 × 1,5 + réserve = 294,90 », alors qu'avec la nouvelle réserve de 5,93 le calcul donne **295,11** (294,90 est la valeur avec l'ancienne réserve de 5,72). Le plafond arrondi reste **300**. Tous les autres chiffres du devis v3 et de P7 se retrouvent au centime près (écarts de 0,000 à 0,004, arrondis).

## 1. Table ligne par ligne

| § | chiffre du devis v3 | script | écart | cause |
|---|---|---|---|---|
| 3 | 192,79 × 1,5 + réserve = 294,90 « sur valeurs exactes » | 295,114 (exact, réserve 5,932) ; 295,115 (arrondis, 5,93) ; 294,898 (exact, ancienne réserve 5,716) | +0,21 | La réserve passe à 5,93, mais le résultat recopié est celui du v2 (réserve 5,72). La phrase « le plafond est le même avec l'une ou l'autre réserve » est juste (300 dans les deux cas). |
| 2 | effectifs 432 / 144 / 208 ; 58 appels neufs = 48 énoncés neufs + 10 seconds services ; 40 ; 60 | identiques | 0 | — |
| 2 | unitaires (Opus, Argon aux deux prix, item S, item N, reformulation, jugement) | identiques | 0 | Agent S au pire 1,20 < 1,50 : plafond jamais atteint, conforme. |
| 2 | fumée : bornes 0,096 et 0,108 ; « à 0,008 près » | 0,096 ; 0,108 ; 0,008 | 0 | — |
| 2 | P1, P2 (deux prix), P3 S et N, P4 | identiques | ≤ 0,004 | Arrondi. |
| 2 | totaux 73,33 / 157,97 / 567,52 et 76,36 / 165,17 / 590,56 | 73,332 / 157,972 / 567,524 et 76,356 / 165,172 / 590,564 | ≤ 0,004 | Arrondi. |
| 2 | écart d'un jour de prix à l'autre 3,02 / 7,20 / 23,04 | 3,024 / 7,200 / 23,040 | ≤ 0,004 | Arrondi. |
| 2 | appels + machine 76,69 / 164,69 / 629,92 et 79,72 / 171,89 / 652,96 | 76,692 / 164,692 / 629,924 et 79,716 / 171,892 / 652,964 | ≤ 0,004 | Arrondi. |
| 2 | R1 Astra échoue −10,08 ; reformulateur Argon +0,00 / +1,68 | identiques | 0 | — |
| 2 | R1 Kimi échoue +0,00 / +7,50 | 0,000 / 7,504 | 0,004 | Arrondi. Total non écrit : 157,97 / 172,68. |
| 2 | R1 les deux échouent 142,85 / 155,88 | 142,852 / 155,876 | ≤ 0,004 | Arrondi. |
| 2 | conditionnelles 15,12 ; 12,50 ; 192,79 ; 184,99 à 2/10 | 15,120 ; 12,496 ; 192,788 ; 184,988 | ≤ 0,004 | Arrondi. |
| 3 | réserve 5,93 (logique v1) ; reprise par A6 du brouillon 3 | 5,932 | 0,002 | Arrondi ; A6 concorde. |
| 3 | plafond d'appels 300 ; plafond machine 62,40 → 65 (aux 5 supérieurs) ; somme 365 | 300 ; 62,40 → 65 ; 365 | 0 | Règle d'arrondi écrite ; A9 (65) concorde. |
| 4 | P7 [115,39 ; 261,41] (= brouillon 3) | 115,392 / 261,412 (attendus exacts) ; 115,391 / 261,409 (attendus arrondis) | ≤ 0,003 | Arrondi. |
| 4 | dans P7 : attendus, trois replis R1, conditionnelles ; hors : bas, pire, plafond | idem pour les 15 cas testés | 0 | « Kimi échoue » 172,68 et « les deux échouent » compris. |
| 6 | sensibilité 157,97 / 165,17 ; 147,89 / 156,77 ; postes dominants S puis proposeurs | identiques | ≤ 0,002 | Arrondi. |

Brouillon 3 : 208 items, 24 triviaux et 24 grossiers servis (A4), 1,50 par agent S (A7), 10 seuils par monde dont 6 faux (P9) : conformes.

## 2. Les écarts du rejeu v2 sont-ils corrigés (§ 7 du devis v3) ?

| écart du rejeu v2 | position du v3 | constat |
|---|---|---|
| +0,84 du § 5 | accepté, surcoût 0,00 | **Corrigé.** |
| fumée 0,10 non bornante | accepté ; un appel par modèle, borne 0,108, forfait supposé | **Corrigé** ; le brouillon 3 dit aussi « un appel par modèle (quatre) ». |
| réserve 5,72 sans le relecteur | accepté, 5,93 | **Corrigé dans la réserve et dans A6**, mais le calcul du plafond qui la suit n'a pas été refait (294,90 au lieu de 295,11 ; § 1). |
| 294,91 | accepté, 294,90 sur valeurs exactes | **Corrigé pour l'ancienne réserve seulement** ; avec 5,93 la valeur est 295,11. Sans effet sur 300. |
| plafond machine 65 sans règle | règle écrite | **Corrigé.** |
| arrondis au centime | acceptés | Sans objet. |
| 1. P7 sans source | formule écrite | **Corrigé** ; bornes retrouvées. |
| 2. « 58 énoncés neufs » | « 58 appels neufs, dont 48 énoncés neufs » | **Corrigé.** |
| 3. plafond par item | borne l'agent seul, ne joue jamais | **Corrigé** ; la parenthèse « (plafond par item) » des postes dominants a disparu. |
| 4. nombre d'appels de fumée | quatre, un par modèle | **Corrigé.** |
| 5. R1 partiellement chiffré | trois cas chiffrés | **Corrigé** ; chiffres retrouvés. |
| 6. heures de machine non réestimées | dit, « borne haute supposée » | **Corrigé** (énoncé, pas réestimé). |
| 7. ligne « appels + machine » | rétablie | **Corrigé** ; chiffres retrouvés. |
| 8. convention du bas | dit au § 7, point 8 | **Corrigé en § 7 seulement** : le § 2 ne dit pas que le bas prend le juge Astra. |
| 9. profil bas « reconstitué » | « repris » | **Corrigé** ; le mot n'apparaît plus. |
| 10. course à cheval | bornée (3,02 / 7,20 / 23,04) | **Corrigé.** |

## 3. Remarque
L'en-tête du devis v3 dit que chaque chiffre vient de la sortie du script v2 (`724e2b79…`). C'est vrai de tous les chiffres sauf le 294,90 associé à la réserve de 5,93 : cette combinaison ne figure pas dans la sortie v2. Elle figure maintenant dans la sortie v3, bloc 7, avec la valeur 295,11.
