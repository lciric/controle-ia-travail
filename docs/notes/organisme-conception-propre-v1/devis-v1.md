# Devis — course de l'atelier d'idées sur la conception de l'organisme lui-même, une génération — v1

Écrit par le préparateur neuf le 13 novembre 2026 (vers 23:16 UTC, complété à 23:28 UTC ; `date -u`). **Aucune dépense engagée par ce devis.**
Borne de Lazar et de la mère : **25 USD pour une génération** (R-2609) ; la ligne de GO s'inscrit au montant du **pire cas
ci-dessous : 21 USD**. Conception : `conception-course-v1.md`. Lanceur :
`scripts/lancer_course_ideation_conception_propre_v1.py` (constantes citées entre parenthèses).

## 1. Barème et sources

- Modèles de Claude, par le relais de clé du noyau (`pole/relais_reel.py`, clé lue par son nom par le relais seul) : barème
  du noyau, en USD par million de jetons (entrée / sortie) : modèle A 4 / 20, modèle B 10 / 50 (repris de
  `docs/notes/organisme-bassins-etroits-v1/devis-organisme-bassins-etroits-v1.md`, `1b311242…`, § 1).
- Argon (`gemini-4-argon`) par l'enveloppe `appel-argon-v5.sh` (`37c0205e…`), `commande_argon_v3d.py` (`46c91df4…`) et le
  relais Gemini v2 : entrée 8,3, sortie 41,5 (supposée), pensée provisionnée 8 192 jetons ; mesuré le 13 novembre : contrôle
  d'Argon de 33 165 jetons d'entrée = 0,275477 USD (`docs/notes/organisme-bassins-etroits-v1/operation-g1-v1.md`,
  `3beef39e…`).
- Kimi (`kimi-k3.1-pro`), lecteur de la règle, par `relais_kimi_v4.py` : entrée 2, sortie 10 (page de Moonshot lue le
  30 octobre 2026, `conception-juge-tournoi-elo-v2.md`, `0ac81c9a…`, § 2.1) ; précédent mesuré : Kimi juge de 29 fiches,
  222 635 jetons d'entrée et 31 010 de sortie, **0,755 USD** (`registres/depenses.md`, ligne du 30 octobre 2026 à 11:50 UTC).

## 2. Par poste

| Poste | Plafond (pire cas) | Attendu |
|---|---|---|
| Contrôles des modèles A et B | 2 × 0,2 = 0,4 | ≈ 0 |
| Proposeur modèle A, deux passes (`PLAFONDS`) | 2 × 2,0 = 4,0 | ≈ 0,4 |
| Proposeur modèle B, deux passes | 2 × 2,0 = 4,0 | ≈ 1,1 |
| Juge de l'organisme `opus-juge` (exigé par le code ; ses notes ne servent pas) | 1,5 | ≈ 0,5 |
| **Part Claude** (somme 9,9 ; relais et total de l'orchestrateur à **10,0**, `TOTAL_CLAUDE_USD`) | **10,0** | **≈ 2,0** |
| Contrôle d'Argon (`CONTROLE_EXTERNE_USD`) | 1,7 | ≈ 0,25 (consigne de contrôle mesurée sans appel : 285 288 caractères, contre 322 793 aux bassins, où elle a coûté 0,275 USD) |
| Argon, passe 1 / passe 2 | 1,3 + 1,9 | ≈ 0,5 + 0,6 |
| Juge Argon différé | 0 : **jamais joué** (aucun bras dans ce lanceur ; son plafond de 2,5 entre seulement dans la somme que l'orchestrateur vérifie, 7,6 < 8) | 0 |
| **Part Argon de la course** | **4,9** | **≈ 1,35** |
| **Course** (`PLAFOND_COURSE_USD` = 10,0 + 4,9) | **14,9** | **≈ 3,4 au calcul ; ≈ 5 retenu (4 à 7)** |
| Une première tentative en défaut au contrôle, avant la seule relance permise | 0,4 + 1,7 = **2,1** | 0 si rien ne casse (précédent : 0,28) |
| **Lecteur de la règle**, Kimi, deux lectures, trois lots de 20 fiches au plus chacune (`RESERVE_LECTEUR_USD`) | **4,0** | **≈ 1,5 (1 à 2,5)** |
| **Total** | **21,0** | **≈ 6,5 (5 à 9,5)** |

Pourquoi « retenu » plus haut que le calcul : la course du 8 novembre (huit fiches) a coûté 7,65 USD avant son bras pour un
calcul plus bas (pensée d'Argon, fiches plus longues que prévu ; `devis-organisme-bassins-etroits-v1.md`, § 2).

Tailles mesurées sans appel par l'orchestrateur réel sur les pièces de cette course (essai
`test_liste_blanche_et_mesure_contre_l_orchestrateur_reel`, 13 novembre 2026 vers 23:27 UTC) : question 8 686 caractères,
faits 8 080, passe 1 19 186, passe 2 au plus 284 813, contrôle d'Argon 285 288 (garde de course 400 000 : marge 114 712),
juge au plus 1 623 579 (40 fiches). Garde avant envoi d'Argon, à 3 caractères par jeton : contrôle 1,339 ≤ 1,7 ; passe 1
0,566 ≤ 1,3 ; passe 2 aux fiches de 8 000 caractères 0,705 ≤ 1,9.

## 3. Plafond par relais

| Relais | Réglage | Ce qu'il borne |
|---|---|---|
| Claude (`pole/relais_reel.py` du clone) | `--plafond-usd 10` ; `--modeles-permis` limité aux identifiants des modèles A et B tels que le code les nomme ; port 8787 | toute la part Claude, **toutes tentatives confondues** si le relais n'est pas relancé entre elles |
| Gemini v2 (`relais_gemini_v2.py`, `2b0043bc…`) | `--max-appels 8` (contrôle et deux passes : six appels, compte de jetons compris ; deux de marge) ; port 8788 | le nombre d'appels ; la dépense par appel est bornée par la garde avant envoi de la commande d'Argon, au plafond de chaque session (1,7 ; 1,3 ; 1,9) |
| Kimi (`relais_kimi_v4.py`, `--max-recherches 0`) | `--plafond-usd 4 --max-appels 6`, prix 2 / 10 / 2 (cache compté au prix d'entrée, borne haute) | le lecteur, deux lectures |

## 4. Ce qui arrête la course

- Avant le départ, le lanceur refuse (rien n'est appelé) si : la ligne de GO manque, est révoquée, échue ou sous 21 USD ;
  la **garde de cumul** ne tient pas (dépense relevée dans le dépôt + 14,9 + 4,0 > min(25, plafond de la ligne)) ; une
  course a déjà produit des fiches ; deux courses sont déjà parties ; un superviseur ou un orchestrateur orphelin vit ;
  le bac à sable est inactif ; une empreinte diffère (lanceur, orchestrateur, pièces) ; une garde de taille ou de somme ne
  tient pas ; la commande n'est pas exactement la commande permise.
- Pendant la course : plafonds de session de l'orchestrateur, totaux transmis (10 et 8), plafond du relais Claude (402),
  garde avant envoi d'Argon, délai d'une heure par session ; **arrêt à la main par PID** : `kill -TERM <PID du
  superviseur>` (relayé à l'orchestrateur par PID, R10), jamais par motif.
- Une course arrêtée en route coûte au plus ce qu'elle a engagé, jamais plus que ses plafonds ; une dépense illisible compte
  le plafond entier et ferme toute relance.

## 5. Durée

Course : contrôles, deux passes d'Argon, quatre sessions de proposeurs Claude, un juge, en série : **1 à 2 heures**,
borne d'environ 10 heures. Lecture de la mère : son temps (36 fiches au plus). Lecteur : six appels, **20 à 60 minutes**.

## 6. Réserves

- Le juge de l'organisme coûte jusqu'à 1,5 USD sans servir la sélection : il est exigé par le code (au moins un juge).
- Les attendus sont des calculs à partir de mesures d'autres courses ; la consigne de cette question est plus courte
  (aucun recoupement), la sortie (36 fiches au plus) du même ordre.
- Le relais Gemini v2 n'a pas de plafond en dollars : la borne d'Argon est celle de la commande d'Argon et de
  l'orchestrateur.
- L'outil du lecteur n'est pas écrit (conception, § 8) ; sa part est réservée par la garde de cumul du lanceur de la course.
