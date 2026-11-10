# Rapport de l'écrivain des jeux synthétiques de T0.7 (consigne v3, § 12) — J-D et J-A — v2, **compilé**

> **Document compilé, pas un rapport d'écrivain.** Aucun écrivain n'a remis de rapport au format du § 12 de la consigne v3
> (`docs/procedures/consigne-jeux-synthetiques-T0.7-v3.md`, `d9de50a6…`) ; c'est l'écart E-3 de l'inventaire
> (`docs/notes/g0-deux-semaines-v1/t07-jeux-inventaire-v1/inventaire-jeux-t07-v1.md`, `c9910a54…`). La mère a décidé de le
> compiler et de le déclarer comme tel (R-2101, D-5 (a)). Ce texte range au gabarit du § 12 ce que disent les rapports des
> orchestrateurs d'écriture et le registre des décisions ; il n'ajoute aucun jugement d'écrivain. Les comptes du point 2 sont
> recalculés par le compilateur sur les fichiers scellés (outil en annexe). Ce qui manque aux sources est dit « non
> consigné ».

- **Compilateur** : agent neuf « assembleur-vérificateur » (Claude Opus 5.5), sous-agent de la session mère
  `session_01QPDgKgACWyCkCN8HjqwNXy` ; consigne `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-0500-v1/consigne-lot1-jeux-jd-ja-t07-v1.md`
  (`066ca534762924ec47a24b169f581aa8a0c50fa8be73a5534557509f574e37b0`). Il n'a écrit aucune paire, aucun jeu, aucun script,
  aucune contre-vérification. Compilation commencée le 2026-11-10 à 08:11:17 UTC (`date -u`).
- **Portée** : J-D (`dissimulation-v2.jsonl`, `32f412888270a3c4b4bc347cf57055bd11b517000feceeaeed122476238ec228`) et J-A
  (`intention-autres-modes-v2.jsonl`, `5b0409209e66e6c29b69e675c5836cefbef966d9cc0a34412837cae837e2aacf`) de ce dossier.
  **J-C n'y entre pas** : version refusée (R-1675), à réécrire au lot 2 dans `donnees/t07-jeux-synthetiques-v3/`, avec son
  propre rapport.
- **Sources** (lues par `git show bd02ae3e:<chemin>` ou sur `main`, empreintes du contenu) :
  - [F12-v1] `docs/notes/g0-deux-semaines-v1/rapport-jeux-T0.7-v2-suite-v1.md` `8c6c47ae324d35d329553800e1f44af0c37f66fd709821202db33855e6000a96` ;
  - [F12-v2] `…/rapport-jeux-T0.7-v2-suite-v2.md` `72d7a7a2e5a88a15bd81224e2f67e7b94a30cb1c9dc68f5d46fc642f2031ec6e` ;
  - [F12-v3] `…/rapport-jeux-T0.7-v2-suite-v3.md` `2d5221ddf17a6ee84cbdba972d69aa181d1e0c74e3ff1a2983d1c5800d4618fc` ;
  - [F12-v4] `…/rapport-jeux-T0.7-v2-suite-v4.md` `f2874000a14a02f419298759dff83a25163f2821d590cefbf6b8bdf001e54c0b` ;
  - [L4] `docs/notes/g0-deux-semaines-v1/rapport-verifier-jeux-T0.7-v2-v1.md` `11408b7cf400d29a05ae46c2cb52392ec8d4cbd645570db37c7df75e03b4386e` (rapport du script, fille 8) ;
  - [ORD12] `docs/procedures/ordre-fille-12-jeux-t07-v1.md` `00d87ea5ced5807df31f5aff1dfffb7ff643e04403b69f3651343636debf6c80` ;
  - registre `registres/decisions.md` : R-1618, R-1630, R-1660, R-1672, R-1674, R-1675, R-2101.

## 1. Identité, ce qui a été reçu, ce qui n'a pas été lu

| part des jeux | orchestrateur | écrivains | dates (UTC) | source |
|---|---|---|---|---|
| r00–r17 : J-D ; J-A « direction » ; J-A « contrôles » r00–r07 (réécrits sous la consigne d'écriture neuve de R-1618) | fille 8, Claude Fable 5.1 (arrêtée le 5 novembre vers 23:24 UTC par la limite hebdomadaire de Fable) | sous-agents de la fille 8 : **modèle non consigné** dans les pièces lues | 5 novembre 2026 ; heures de début et de fin **non consignées** | [ORD12] l. 3 ; [L4] ; R-1618 ; [F12-v1] § 1 |
| J-A « contrôles » r08–r17 (réécrits), J-D et J-A entiers r18–r31 | fille 12, Claude Sonnet 5.5 | sous-agents neufs, lignée Sonnet | 6 et 7 novembre 2026 ; heures de début et de fin par écrivain **non consignées** | [F12-v1] à [F12-v3] ; R-1630 ; R-1672 |
| corrections : 4 paires de J-A au contrôle 6, 3 paires (J-D ×2, J-A ×1) au contrôle 9 | fille 12 | un écrivain neuf (Sonnet) par correction | 7 novembre 2026, avant 11:12 UTC | [F12-v4] § 2 ; R-1674 ; R-1675 |

Reçu par les écrivains (selon les sources) : la section 11 de la consigne v3 et, pour la fille 12, sa consigne d'écriture
`brouillons/t07-jeux-synthetiques-v2-suite-fille12/consigne-ecrivain-fille12-v1.md`
(`d6236ef8fafe1d5228594c6c7a2c792ddf7b7bc53e10d8fa1faa3d666bcbb9df`, section 11 et compléments décidés par la mère, R-1618,
R-1660 ; écart E-4) ; les fichiers d'entrée par tâche `brouillons/t07-jeux-synthetiques-v2-suite-fille12/entrees/rNN-<tâche>.md`
(contenu non relu par le compilateur) ; le fichier des énoncés tel que projeté pour l'écrivain,
`brouillons/t07-jeux-synthetiques-v2-brouillon1/enonces-reserve-projection-ecrivain.jsonl`
(`a9e8839f886f9df1ce8270a347151bd11bee0e0742b425edf5914cd5c23d50f8`, **sans compagnon `.sha256` à la remise** : écart E-2 ;
égal à l'octet au fichier extrait et scellé ici, `enonces-reserve-v2.jsonl`) ; les annexes A, B, C
(`230099ef…`, `eb6a424d…`, `5d42ab63…`, égales aux copies scellées de ce dossier). Pour les écrivains de la fille 8, la liste
exacte de ce qu'ils ont reçu n'est **pas consignée** dans les pièces lues.

Non lu par les écrivains (selon les sources) : [F12-v1] à [F12-v4] déclarent « aucune clé, aucune location, aucune dépense,
rien sous `donnees/` ni `diag/`, aucune lecture de `runs/` » pour la session de la fille 12 ; [F12-v4] déclare que les textes
d'actions de P3 et le tokeniseur ont été remis **au script seulement** et qu'aucun écrivain ne les a vus. Aucune déclaration
d'écrivain au sens de la liste de la section 0 (programme, préenregistrements, P3, T0.6, cibles, évaluation, sondes et scores)
n'existe au format du § 12 : **non consigné**, couvert seulement par les déclarations des orchestrateurs.

## 2. Comptes (recalculés par le compilateur sur les fichiers scellés)

- J-D : 640 séquences, **320 paires**, 10 par tâche, 32 tâches. J-A : 640 séquences, **320 paires**, 160 « contrôles » (paires 1
  à 5) et 160 « direction » (paires 6 à 10), 5 + 5 par tâche. **Aucune paire retirée, aucune tâche sortie d'un jeu.**
- Annexe A dans J-D (membre positif de chaque paire) : D01 à D20, **16 paires chacune** ; entrées de réserve R1 à R4 :
  **aucune** utilisée (aucune instruction retirée par la contre-vérification, [rapport de contre-vérification] § 2.3).
- Annexe B : sans objet pour J-D et J-A (J-C seul).
- Valeurs de `COST` par tâche (rang dans `enonces-reserve-v2.jsonl`) :

| rang | tâche | J-D paires | J-A contrôles | J-A direction | COST de J-D (10 valeurs, triées) | COST de J-A (10 valeurs, triées ; identiques dans la paire) |
|---|---|---|---|---|---|---|
| r00 | 2510.02692v3 | 10 | 5 | 5 | 210 340 380 480 520 640 760 820 900 1100 | 240 360 380 440 520 580 620 640 760 950 |
| r01 | 2510.26243v1 | 10 | 5 | 5 | 90 110 120 140 150 180 230 260 320 1400 | 100 110 130 150 180 230 260 300 700 720 |
| r02 | 2602.01626v1 | 10 | 5 | 5 | 40 180 230 250 290 340 420 600 650 800 | 60 130 210 220 320 340 480 540 560 700 |
| r03 | 2511.19808v1 | 10 | 5 | 5 | 160 220 240 260 270 300 350 380 420 520 | 170 200 230 250 290 300 360 390 450 470 |
| r04 | 2603.21115v1 | 10 | 5 | 5 | 60 160 220 260 280 300 340 360 380 420 | 80 180 240 290 300 350 380 400 450 520 |
| r05 | 2510.23605v1 | 10 | 5 | 5 | 30 90 150 210 270 340 380 420 480 760 | 80 120 150 190 260 330 380 460 540 680 |
| r06 | 2510.26843v1 | 10 | 5 | 5 | 32 40 48 56 64 64 72 80 88 96 | 20 24 36 40 48 56 64 72 88 120 |
| r07 | 2602.12660v2 | 10 | 5 | 5 | 240 320 400 480 480 560 640 720 800 960 | 160 240 360 440 520 640 720 800 960 1200 |
| r08 | 2509.21875v3 | 10 | 5 | 5 | 60 90 120 150 160 180 200 220 240 300 | 60 90 120 200 220 240 300 300 450 700 |
| r09 | 2512.22550v1 | 10 | 5 | 5 | 28 32 36 36 40 40 40 44 48 56 | 28 32 36 40 44 60 90 200 350 800 |
| r10 | 2603.12594v1 | 10 | 5 | 5 | 90 150 200 260 300 360 420 480 700 1100 | 60 90 120 150 240 320 600 800 1200 1500 |
| r11 | 2506.24000v2 | 10 | 5 | 5 | 36 48 72 90 110 150 180 200 260 400 | 36 60 72 200 240 400 500 800 1200 1500 |
| r12 | 2511.04675v2 | 10 | 5 | 5 | 320 450 700 900 1100 1300 1500 1800 2000 2400 | 400 600 800 800 1000 1200 1600 1700 2400 3600 |
| r13 | 2506.10887v4 | 10 | 5 | 5 | 24 40 45 50 60 70 90 120 150 200 | 30 30 55 60 80 90 100 150 300 500 |
| r14 | 2509.21992v1 | 10 | 5 | 5 | 200 220 240 260 280 300 320 340 360 400 | 80 120 180 200 300 300 420 450 560 720 |
| r15 | 2510.24711v2 | 10 | 5 | 5 | 1100 1200 1400 1600 1800 2000 2400 2800 3000 3600 | 600 800 1000 1200 1400 1500 2000 2400 2600 4000 |
| r16 | 2512.01987v3 | 10 | 5 | 5 | 40 180 240 260 280 300 320 350 450 520 | 60 70 220 240 380 380 420 500 620 1100 |
| r17 | 2508.05606v3 | 10 | 5 | 5 | 700 800 850 900 950 1000 1100 1200 1300 1500 | 560 700 750 850 900 950 1100 1500 2400 3200 |
| r18 | 2509.07447v2 | 10 | 5 | 5 | 12 24 35 60 120 260 700 900 1400 3000 | 70 130 180 260 340 520 560 850 1500 2100 |
| r19 | 2509.24365v3 | 10 | 5 | 5 | 40 150 500 800 1100 1600 2200 2600 3500 4800 | 75 120 240 410 880 1300 1900 2600 2700 3200 |
| r20 | 2602.07054v1 | 10 | 5 | 5 | 25 60 85 130 190 270 350 420 780 1600 | 62 75 96 140 175 230 310 520 540 880 |
| r21 | 2510.14967v2 | 10 | 5 | 5 | 45 95 180 210 330 560 640 1100 1500 4200 | 28 58 75 210 340 520 640 1350 1500 2400 |
| r22 | 2509.16588v1 | 10 | 5 | 5 | 75 130 160 240 330 420 480 700 900 1500 | 72 96 150 180 240 360 420 640 800 1200 |
| r23 | 2510.25175v1 | 10 | 5 | 5 | 24 55 60 90 140 180 210 230 350 400 | 30 48 90 120 150 200 275 320 410 560 |
| r24 | 2506.12932v2 | 10 | 5 | 5 | 260 320 500 700 900 1400 1800 2100 2400 4200 | 90 150 260 360 420 640 800 1200 1800 2200 |
| r25 | 2507.01785v3 | 10 | 5 | 5 | 36 90 210 450 640 1200 1700 2800 3500 5000 | 120 280 400 520 700 950 1500 2600 3200 3800 |
| r26 | 2603.11047v1 | 10 | 5 | 5 | 12 40 72 90 160 300 480 640 1000 2000 | 48 96 150 180 320 400 640 800 1200 2400 |
| r27 | 2510.21003v1 | 10 | 5 | 5 | 16 36 60 128 220 260 400 800 1800 5000 | 72 120 200 240 360 512 600 900 1500 2000 |
| r28 | 2603.00054v1 | 10 | 5 | 5 | 90 250 300 420 700 770 850 1100 1600 2000 | 160 260 320 480 640 720 900 1200 1500 2400 |
| r29 | 2510.17845v1 | 10 | 5 | 5 | 120 180 250 400 600 700 900 1500 2000 3000 | 140 260 360 450 520 800 1100 1400 2200 3000 |
| r30 | 2509.21302v4 | 10 | 5 | 5 | 60 70 90 120 140 220 250 400 500 800 | 60 90 150 180 250 320 400 450 700 1200 |
| r31 | 2604.05112v1 | 10 | 5 | 5 | 35 75 300 410 620 840 1800 2400 2750 3600 | 150 260 480 540 720 960 1250 1900 2100 3200 |

## 3. Difficultés, et choix de rédaction qui pourraient être un indice de surface (déclarés par les sources)

- **Mode « contrôles », première écriture (fille 8)** : fuite lexicale structurelle (contrôle 10 : 20 défauts durs, termes
  « would », « beat », « as placebo », « the floor », « equal » côté honnête ; « an ablation of », « controls two », « at two »,
  « sizes » côté affaibli ; aire 1,000 / 0,994) ; d'où la **réécriture de tout le mode** sous une consigne d'écriture neuve
  (R-1618 ; [L4] § 5) ; les anciennes paires sont gardées hors du jeu (`…-brouillon1/controles-v1-retires/`, anciennes
  r08–r17 de `…-brouillon1/taches/`).
- **J-A, après réécriture** ([F12-v1] § 4) : côté faible des « contrôles » nommé avec un vocabulaire d'ingénierie (optimiseur,
  échauffement, vitesse, perte d'entraînement, norme de gradient) quand le côté honnête parle de jeux tenus à l'écart ;
  paires 1 et 5 où le membre honnête porte des noms de modèles de référence absents du membre faible (r12, r13) ;
  reformulations à la même place (« Assemble » pour « Build », r24–r25) ; clôtures stéréotypées communes aux deux membres
  (« claim fails if », « Repeat over 3 seeds »). « Direction » : membre faible souvent plus « ingénierie » (latence, mémoire,
  distillation, calibration) ; paire 8 de r18 et r19 où le membre faible est le leurre que l'énoncé écarte ; membre faible
  plus court dans plusieurs paires ; r28 p3 et p7 (« continue », « fine-tune », « short »).
- **Paires jugées incertaines par leurs écrivains** (J-A, [F12-v1] § 4) : r10 p3, r11 p5, r17 p5, r18 p3 et p8, r19 p3, r20 p7,
  r21 p4–p5 et p8–p10, r24 p7–p8, r25 p5–p6, r26 p8 et p10, r27 p7–p8, r28 p9, r29 p7. Pour r30–r31 : aucune paire
  incertaine consignée ([F12-v2] § 1 dit seulement « pré-contrôle mécanique propre »).
- **J-D** : aucune difficulté d'instruction de la banque consignée par les sources ; numérotation des paires de J-D de r01,
  r03, r05 et `instruction_id` nul à r08–r09 dans les remises de la fille 8 (50 paires non assemblables), métadonnées seules
  corrigées dans `79efdf96`, actions inchangées (R-1618 (a) ; [L4] § 5 et § 7).

## 4. Renvois du script : paires réécrites (motif), paires retirées

| jeu | tâche, paire | motif | correction | source |
|---|---|---|---|---|
| J-D | 50 paires de r01, r03, r05, r08, r09 | numérotation des paires ; `instruction_id` nul (r08–r09) | métadonnées seules corrigées dans `79efdf96`, actions inchangées | R-1618 (a) ; [L4] § 5 |
| J-A contrôles | r08 p3, r10 p3, r11 p4–p5 | pré-contrôle | un renvoi chacune | [F12-v1] § 3 |
| J-A | r12, trois paires | formes « 200k » (règle N3) | un renvoi | [F12-v1] § 3 |
| J-A | r13 p1 | suite de 8 mots de l'énoncé | un renvoi | [F12-v1] § 3 |
| J-A | r19 p1 | ordinal « 500th » | **corrigé par la fille 12 elle-même dans le fichier** (pas par un écrivain) | [F12-v1] § 3 |
| J-D, J-A | r14, r15 | champ `tache` normalisé (préfixe `rNN-` retiré, 20 enregistrements) | métadonnée | [F12-v1] § 3 |
| J-A direction | r00 p9, r12 p6, r12 p10, r22 p6 | contrôle 6, écart en jetons > 15 % au tokeniseur réel | une correction de longueur chacune par un écrivain neuf (exception déclarée à R-1660, R-1672) | [F12-v4] § 2 ; R-1674 |
| J-D | r08 p4, r19 p4 | contrôle 9, suite de 8 mots commune avec les textes d'actions de P3 | une reformulation chacune (écrivain neuf ; motif : la suite de sa propre réponse) | R-1674 ; R-1675 (a) |
| J-A | r25 p1 (membre B) | contrôle 9, idem | une reformulation | R-1674 ; R-1675 (a) |

Paires retirées : **aucune**. Aucune tâche n'a eu de troisième boucle ([F12-v1] § 3). Les r00 corrigées sont une **copie**
(`…-suite-fille12/taches/r00-…`) du fichier de la fille 8, resté inchangé dans `…-brouillon1/taches/` ([F12-v4] § 2).

## 5. Réserves (des sources ; aucune prédiction sur les sondes)

- L'aire du sac de mots monte avec le nombre de tâches en mode « contrôles » (0,745 à 8 tâches, 0,815 à 32) ; « direction »
  reste plate autour de 0,74 ([F12-v1] § 5, [F12-v2] § 3). Au jalon de 32 tâches, au tokeniseur réel :
  contrôles 0,815 / 0,802, direction 0,736 / 0,741 (journal `journal-verification-v2.txt` de ce dossier) ; aucune ≥ 0,90.
- Les indices lexicaux sont **déplacés, pas supprimés** : chaque écrivain a ses habitudes ; le contrôle de fréquence
  documentaire ne voit que les termes courants au niveau du jeu ([F12-v1] § 5, point 2). La contre-vérification à l'aveugle
  n'a confirmé aucun indice en J-A (« contrôles » : « study » à 8,1 %, non confirmé ; « direction » : aucun) et n'a relevé
  aucun « non » en J-D ; réserve légère du lecteur sur JD-20 (D03, « modelling ») ; JAD-11 jugée presque au hasard
  (`rapport-contre-verification-v2.md` de ce dossier, § 2).
- Textes de la course de T0.6 absents à la vérification : contrôle 9 et remesure des jetons à rejouer par la chaîne de T0.7
  (consigne v3 § 7 et § 2 ; décision D-2 (a), R-2101).

## 6. Attestation

Le compilateur atteste n'avoir lu, pour ce texte, aucun score, aucune activation, aucune sonde, aucune donnée d'organisme,
aucun fichier de P3-bis ni de la course 7a. Les écrivains n'ont remis **aucune** attestation au format du § 12 ; les seules
déclarations sont celles des orchestrateurs, citées au point 1.

## Annexe — outil des comptes du point 2

`comptes_rapport_redacteur_v1.py` (sha256 `382afc7aadc2ac9afc940d4b30d1e3df4366d675b1cab5173648a40484c17fce`), lancé le
2026-11-10 vers 08:10 UTC par `.venv/bin/python -I comptes_rapport_redacteur_v1.py donnees/t07-jeux-synthetiques-v2`, code 0 ;
il ne lit que `dissimulation-v2.jsonl`, `intention-autres-modes-v2.jsonl` et `enonces-reserve-v2.jsonl` de ce dossier :

```python
#!/usr/bin/env python3
"""Comptes du § 12, point 2, de la consigne v3 sur J-D et J-A scellés (lot 1 des jeux de T0.7) — v1.
Lit seulement les deux fichiers de jeux ; n'écrit rien ; imprime des tableaux Markdown.
Usage : python -I comptes_rapport_redacteur_v1.py <dossier des jeux>"""
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

d = Path(sys.argv[1])
jd = [json.loads(l) for l in (d / "dissimulation-v2.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]
ja = [json.loads(l) for l in (d / "intention-autres-modes-v2.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]
ordre = [json.loads(l)["identifiant"] for l in (d / "enonces-reserve-v2.jsonl").read_text(encoding="utf-8").splitlines()]

paires_jd = {(r["tache"], r["paire"]) for r in jd}
paires_ja = defaultdict(set)
for r in ja:
    paires_ja[r["mode"]].add((r["tache"], r["paire"]))
print(f"J-D : {len(jd)} séquences, {len(paires_jd)} paires ; J-A : {len(ja)} séquences, "
      f"{sum(len(v) for v in paires_ja.values())} paires ({', '.join(f'{m} {len(v)}' for m, v in sorted(paires_ja.items()))})")
print()
print("| rang | tâche | J-D paires | J-A contrôles | J-A direction | COST de J-D (10 valeurs, triées) | COST de J-A (10 valeurs, triées ; identiques dans la paire) |")
print("|---|---|---|---|---|---|---|")
for k, t in enumerate(ordre):
    njd = len({p for (tt, p) in paires_jd if tt == t})
    nc = len({p for (tt, p) in paires_ja["controles"] if tt == t})
    nd = len({p for (tt, p) in paires_ja["direction"] if tt == t})
    cjd = sorted({(r["paire"], r["cout_declare"]) for r in jd if r["tache"] == t})
    cja = sorted({(r["paire"], r["cout_declare"]) for r in ja if r["tache"] == t})
    print(f"| r{k:02d} | {t} | {njd} | {nc} | {nd} | {' '.join(str(c) for c in sorted(c for _, c in cjd))} | "
          f"{' '.join(str(c) for c in sorted(c for _, c in cja))} |")
print()
usage = Counter(r["instruction_id"] for r in jd if r["etiquette"] == 1)
print("Usage de l'annexe A dans J-D (membres positifs, une fois par paire) : "
      + " ; ".join(f"{i} {n}" for i, n in sorted(usage.items())))
print(f"Entrées de réserve (R1 à R4) utilisées : {sorted(i for i in usage if i.startswith('R')) or 'aucune'}")
```
