# Devis — course de l'atelier d'idées sur la question « Regard ou raisons », une génération — v1

Écrit par le préparateur neuf le 14 novembre 2026 (vers 09:37 UTC, `date -u`). **Aucune dépense engagée par ce devis.**
Ligne de GO déjà inscrite pendant la préparation : **GO-2026-11-14-01, 25 USD**, échéance 30 novembre (registre, R-2682 :
lancement seulement si le pire cas est ≤ 25 USD). **Pire cas de ce devis : 17 USD. Attendu : ≈ 5,5 USD.**
Lanceur : `scripts/lancer_course_ideation_regard_ou_raisons_v1.py` (`3b2dcb11…` ; constantes citées entre parenthèses).

Dans ce texte, « modèle A » et « modèle B » sont les deux modèles de Claude de la course, comme dans le devis précédent ;
Argon (`gemini-4-argon`) est nommé.

## 1. Rappel : la course précédente

La course « conception propre » (même orchestrateur, mêmes proposeurs, mêmes plafonds de session) avait un pire cas de
**21 USD** (course 14,9 ; première tentative en défaut 2,1 ; réserve du lecteur 4,0) et un attendu de ≈ 6,5 USD
(`docs/notes/organisme-conception-propre-v1/devis-v1.md`, `ce679a53…`). Elle a coûté **5,534745 USD** pour la course
elle-même, sans relance (`registres/depenses.md`, ligne du 14 novembre 2026 sous GO-2026-11-13-06 ; registre, R-2628).

## 2. Ce qui change dans le calcul

- **Aucun lecteur de la règle** : le croisement avec les quatre autres sources se fait après, par un lecteur neuf, sans
  dépense sous cette ligne (R-2682). La réserve de 4,0 USD disparaît de la garde de cumul.
- **Plafond de la course : 14,9 USD, inchangé**, parce que les plafonds de session sont repris tels quels. Ils sont
  recalculés contre les pièces de cette question : toutes les gardes de taille tiennent (§ 5).
- **Pire cas : 17,0 USD** = plafond de la course 14,9 + une première tentative en défaut au contrôle 2,1 (deux contrôles
  des modèles A et B à 0,2, un contrôle d'Argon à 1,7), seule situation où la relance unique est permise.
- **Borne du lanceur : 17,0 USD** (`BORNE_LIGNE_USD`), quel que soit le plafond de la ligne : avec la ligne à 25 USD, le
  lanceur ne peut pas engager plus de 17.

## 3. Par poste

| Poste | Plafond (pire cas) | Attendu |
|---|---|---|
| Contrôles des modèles A et B | 2 × 0,2 = 0,4 | ≈ 0 |
| Proposeur modèle A, deux passes (`PLAFONDS`) | 2 × 2,0 = 4,0 | voir § 4 |
| Proposeur modèle B, deux passes | 2 × 2,0 = 4,0 | voir § 4 |
| Juge de l'organisme (exigé par le code ; ses notes ne servent pas) | 1,5 | voir § 4 |
| **Part Claude** (somme 9,9 ; relais et total de l'orchestrateur à **10,0**, `TOTAL_CLAUDE_USD`) | **10,0** | **≈ 3,5** |
| Contrôle d'Argon (`CONTROLE_EXTERNE_USD`) | 1,7 | ≈ 0,3 |
| Argon, passe 1 / passe 2 | 1,3 + 1,9 | ≈ 0,7 + 1,0 |
| Juge Argon différé | 0 : **jamais joué** (aucun bras ; son plafond de 2,5 n'entre que dans la somme que l'orchestrateur vérifie, 7,6 < 8) | 0 |
| **Part Argon de la course** | **4,9** | **≈ 2,0** |
| **Course** (`PLAFOND_COURSE_USD` = 10,0 + 4,9) | **14,9** | **≈ 5,5 (4 à 8)** |
| Une première tentative en défaut au contrôle, avant la seule relance permise | 0,4 + 1,7 = **2,1** | 0 si rien ne casse |
| Lecteur de la règle | **0 : retiré** | 0 |
| **Total** | **17,0** | **≈ 5,5 (4 à 8)** |

## 4. Par relais

| Relais | Réglage | Attendu | Pire cas d'une course | Pire cas, relance comprise |
|---|---|---|---|---|
| Claude (`pole/relais_reel.py` du clone, port 8787) | `--plafond-usd 10` ; modèles permis : les deux de la course, eux seuls | **≈ 3,5** (2,5 à 5,5) | **10,0** | **10,4** au compte du lanceur ; 10,0 si le relais n'est pas relancé entre les deux tentatives (son plafond couvre alors les deux) |
| Gemini v2 (`relais_gemini_v2.py`, `2b0043bc…`, port 8788) | `--max-appels 8` ; dépense par appel bornée par la garde avant envoi de la commande d'Argon | **≈ 2,0** (1,3 à 3) | **4,9** | **6,6** |
| **Total** | | **≈ 5,5** (4 à 8) | **14,9** | **17,0** |

**D'où vient l'attendu.** Du coût relevé de la course précédente (5,53 USD), à mêmes proposeurs, mêmes plafonds et
consignes de même taille (§ 5), et non d'un calcul par jetons : ce calcul avait donné ≈ 3,4 pour une dépense réelle de
5,53. La **répartition entre les deux relais est une estimation** : je n'ai pas lu la ventilation de la course précédente
(le dossier de run m'était fermé). La mère peut la lire dans la copie scellée du manifeste de fin de l'orchestrateur de
cette course (`reglages.journal.cout_total_usd` pour Claude, `cout_externe_usd` pour Argon) et corriger ces deux lignes.

## 5. Tailles mesurées et gardes (sans appel)

Mesure par l'orchestrateur réel, mode `--mesurer-consignes`, sur les pièces de cette course, le 14 novembre 2026 à
09:32 UTC (`outils/mesure-consignes-sans-appel-v1.json` ; gardes calculées par le lanceur :
`outils/gardes-de-taille-et-de-somme-v1.json`).

| Consigne | Cette course | Course précédente |
|---|---|---|
| Question servie | 10 786 caractères | 8 686 |
| Faits | 8 644 | 8 080 |
| Passe 1 | 21 850 | 19 186 |
| Passe 2, au plus | 287 477 | 284 813 |
| Contrôle d'Argon | 287 952 (garde de course 400 000 : marge 112 048) | 285 288 |
| Juge, au plus (40 fiches) | 1 626 599 | 1 623 579 |

Garde avant envoi d'Argon, à 3 caractères par jeton : contrôle 1,346 ≤ 1,7 ; passe 1 0,573 ≤ 1,3 ; passe 2 aux fiches de
8 000 caractères 0,713 ≤ 1,9. Sommes : Claude 9,9 ≤ 10 ; externe 7,6 < 8 ; exposition externe de la course 4,9.

**Pourquoi les plafonds de session ne sont pas abaissés.** Un plafond est une borne, pas une dépense. Le contrôle d'Argon
ne peut pas descendre sous 1,35 (garde avant envoi) ni sa passe 2 sous 1,62 (garde de course). Les autres pourraient
baisser, mais une session qui touche son plafond arrête la course, et une course arrêtée après des fiches n'est jamais
rejouée : le risque de perdre la génération coûte plus que la marge gagnée sur le papier. Option, si Lazar veut un pire cas
plus bas : passe 1 d'Argon à 0,9, juge à 1,0 et total Claude à 9,5, soit un pire cas de 16,1 USD ; cela demanderait un
lanceur v2 (R12).

## 6. Ce qui arrête la course

- Avant le départ, le lanceur refuse (rien n'est appelé) si : la ligne de GO manque, est révoquée, échue, sous 17 USD ou
  n'est pas seule ; la **garde de cumul** ne tient pas (dépense relevée dans le dépôt + 14,9 > min(17, plafond de la
  ligne)) ; une course a déjà produit des fiches ; deux courses sont déjà parties ; un superviseur ou un orchestrateur
  orphelin vit ; le bac à sable est inactif ; une empreinte diffère (lanceur, orchestrateur, pièces) ; une garde de taille
  ou de somme ne tient pas ; la commande n'est pas exactement la commande permise.
- Pendant la course : plafonds de session de l'orchestrateur, totaux transmis (10 et 8), plafond du relais Claude, garde
  avant envoi d'Argon, délai d'une heure par session ; **arrêt à la main par PID** : `kill -INT <PID du superviseur>`
  d'abord (relayé à l'orchestrateur par PID, R10 ; fin propre), `kill -TERM` seulement si elle ne finit pas ; jamais par
  motif.
- Une course arrêtée en route coûte au plus ce qu'elle a engagé, jamais plus que ses plafonds ; une dépense illisible
  compte le plafond entier (14,9) et ferme toute relance.
- La relance n'est possible que si la première tentative a fini proprement, sans aucune fiche, avec un relevé lisible
  d'au plus 2,1 USD.

## 7. Durée

Contrôles, deux passes d'Argon, quatre sessions de proposeurs Claude, un juge, en série : **20 à 60 minutes** attendues
(la course précédente : 22 minutes, de 23:55 à 00:17 UTC, R-2625 et R-2628) ; borne d'environ 10 heures.

## 8. Réserves

- Le juge de l'organisme coûte jusqu'à 1,5 USD sans servir : il est exigé par le code (au moins un juge).
- Le relais Gemini v2 n'a pas de plafond en dollars : la borne d'Argon est celle de la commande d'Argon et de
  l'orchestrateur. En cas de relance, vérifier qu'il lui reste six appels (huit au départ, deux pris par un contrôle).
- L'attendu vient d'une seule course ; cette question peut appeler des fiches plus longues (champs plus nombreux à remplir).
- Le croisement des cinq bilans n'est pas dans ce devis (R-2682 : par un lecteur neuf, sans dépense).
