# Devis — course d'auto-conception de l'organisme d'idéation — v1

- Auteur : session du compte organisme (modèle I), sur demande de la mère (R-3209 point 6, R-3211, R-3235, R-3263 ; GO-2026-11-18-18 pour l'ordre des priorités). **Rien n'a été lancé** ; aucun appel, aucune dépense.
- Chiffres calculés par programme, sans appel : `docs/notes/organisme-auto-conception-v1/calcul-devis-course-auto-conception-v1.py` (`8bd1e48a42ef2592704415c204e25d94a0ff85e899f94c6f815ae08621d39cb7`), sortie `calcul-devis-course-auto-conception-v1.json` (`c0432930437bd991bf7b51a37f534c16bcc15cb60642c3de04bef44abd355ab2`), sur la matière v3 (`11f4b69b…`) découpée par la règle des lots du lanceur.
- Budget : appels d'interface de l'organisme, séparé de celui du loueur (GO-2026-11-18-13) ; les crédits Claude sont offerts et hors du budget de 100 EUR (R-3235). **Deux lignes de GO à demander à Lazar** : la course (plafond d'arrêt proposé : **90 USD**) et l'épreuve réelle des témoins (plafond : **5 USD**), qui part avant.

## 1. Ce qui est servi : tout, découpé en lots (aucun extrait)

**Tout le catalogue v3 est servi** (R-3263 : `matiere-premiere-v3.md` seule ; ni la v1, ni la v2, ni le relevé JSON). Il n'y a pas d'extrait, donc pas de choix : la pièce de 411 711 octets est **découpée en onze lots par ses propres titres**, et chaque lot va à une case (chaque espèce reçoit chaque case) :

- **partie commune**, servie dans chaque case (46 042 octets) : le préambule et les changements de version, les sections 0 (comment lire), 4 (ce que l'organisme fait déjà), 5 (questions ouvertes) et 11 (réserves sur les regroupements), et un **index** de tous les regroupements (chaque titre « famille n° k — … », une fois, dans l'ordre de la pièce) pour que chaque proposeur puisse nommer un voisin hors de son lot ;
- **huit lots de famille** (section 1 : exploration, originalité, épreuve, jugement, mémoire, sélection, coût, auto-conception), chacun avec la sous-section de même nom de la section 6 (mécanismes suggérés par le seul titre, comptés à part) ;
- un lot **machines** (section 2), un lot **hors machine** (section 3), un lot **autre et marges** (section 6 sans famille, sections 7 à 10).

La règle est écrite au préenregistrement et appliquée par programme (`decouper_matiere`, lanceur) ; **couverture vérifiée** (chaque ligne non vide de la pièce est servie exactement une fois, l'index excepté) ; noms d'espèces remplacés par « [nom retiré] » (aucun dans la v3) ; sortie écrite et scellée au dossier du run (et, pour ce devis, `course-v1/lots-matiere-v3/lots-matiere.json`, empreinte au préenregistrement). Les cinq axes de Lazar ne sont pas un découpage : ils sont demandés dans la question, sur chaque carte (champ `axe`).

Entrée d'un appel de proposeur (consigne figée 29 291 octets + case) : de 94 761 à 136 402 octets selon le lot ; 1 212 629 octets pour les onze cases d'une espèce.

## 2. Appels par rôle (une génération)

| rôle | estimation (2 cartes par appel) | haut (4 cartes par appel) |
|---|---|---|
| proposeurs | 11 cases × espèces actives (33 sans Kimi, 44 avec, 55 avec Astra) | idem |
| aiguilleur | une par carte : 66 / 88 / 110 | 132 / 176 / 220 |
| juges (deux juges croisés) | deux par carte : 132 / 176 / 220 | 264 / 352 / 440 |
| relais d'Argon (proposeur + juge) | — | **au pire 187 appels** (avec Kimi ; 143 sans) : `--max-appels 200` exigé du relais Gemini |

## 3. Prix et sources

| rôle | prix (USD par million, entrée / sortie) | source |
|---|---|---|
| proposeur Claude 1 | 4 / 20 | barème du relais Claude de la procédure (`pole/relais_reel.py`, `1b90b020…`, l. 49-54) ; relevé du jour exigé par le lanceur |
| proposeur Claude 2 | 10 / 50 | idem |
| proposeur Argon | 8,3 / 41,5 | prix figés de l'enveloppe `appel-argon-v5.sh` (`37c0205e…`) |
| proposeur Kimi | 2 / 10 | procédure des relais § 2.2 (vérifiés le 30 octobre) |
| proposeur Astra | 10 / 50 | `docs/notes/organisme-conception-propre-v1/prix-astra-v2.md` (`bf211a07…`), cité par la procédure |
| proposeur Carbon | à relever | aucun prix lu |
| aiguilleur, juges | par appel : 0,031 ; 0,037 (juge Claude) ; 0,0347 (juge Argon) | devis v5 de la course d'affinage (`521470…`), entrées du même ordre (consigne de 2 à 4 ko + une carte) |

Hypothèses : 3,3 octets par jeton (haut : 2,8) ; sortie d'un proposeur 6 000 jetons (haut : 16 000) ; aiguilleur et juges au haut : trois fois l'estimation.

## 4. Totaux

| composition | estimation | haut |
|---|---|---|
| deux espèces Claude + Argon | **22,33 USD** (proposeurs 15,55 ; aiguilleur 2,05 ; juges 4,73) | 69,95 USD |
| + Kimi | **25,99 USD** (16,95 ; 2,73 ; 6,31) | 86,13 USD |
| + Kimi + Astra (si sa commande est épinglée) | 35,22 USD | 112,82 USD (le plafond d'arrêt coupe avant) |

Par appel de proposeur (estimation / haut) : Claude 1 0,254 / 0,478 ; Claude 2 0,634 / 1,194 ; Argon 0,526 / 0,991 ; Kimi 0,127 / 0,239 ; Astra 0,634 / 1,194 ; pire par appel : plafond de session 3,00 USD.

## 5. Plafond d'arrêt proposé : 90 USD

Recommandation (confiance moyenne) : **90 USD**, plafond S17 de la configuration, portée « course », exactement le montant de la ligne de GO. Justification : il couvre le haut de la composition attendue (deux Claude, Argon, Kimi : 86,13 USD) ; il borne Astra si elle est épinglée ; il laisse la part d'Argon et de Kimi bien sous leurs crédits. Plafonds de relais des étapes protégées : proposition 45, aiguillage 15, juges 30 (somme 90). Au haut extrême (quatre cartes par appel et coûts triplés), l'aiguillage (16,4) et les juges (37,9) dépasseraient leur plafond d'étape : l'orchestrateur ne lance pas une étape protégée qui ne tient pas, la marque « non mesurée (budget) » et s'arrête — c'est voulu (aucun repli silencieux) ; à deux cartes par appel (la consigne), les deux tiennent (8,2 et 18,9 au haut).

Options : (a) 90 USD (recommandé) ; (b) 60 USD — couvre l'estimation deux fois et demie, coupe le haut ; (c) 120 USD — couvre Astra au haut, mais expose davantage Argon et Kimi.

## 6. Part au pire par clé (règle de clé par part, R-3237 point 1)

| relais (clé) | rôles | estimation | haut | part au pire (règle du lanceur) |
|---|---|---|---|---|
| Claude (clé nommée par la pièce de départ de la mère ; Minuit refusée) | deux proposeurs, aiguilleur, juge 1 | 15,75 USD | 54,29 USD | **90 USD** (tient l'aiguilleur et un juge : plafond d'arrêt) |
| Argon (clé déclarée ; solde illisible, dispense R-3237) | proposeur, juge 2 | 8,84 USD | 29,22 USD | **90 USD** (tient un juge) |
| Kimi (clé déclarée) | proposeur | 1,39 USD | 2,63 USD | ≈ 4,79 USD (11 appels × formule de son adaptateur, entrée ≤ 136 602 octets, sortie ≤ 16 000 jetons) ; plus la **réserve déclarée** par la mère ≤ 90 % du reste lu |
| Astra (si épinglée ; dispense) | proposeur | 6,97 USD | 13,13 USD | 33 USD (11 × plafond de session) |

Avant la course, le lanceur exige un relevé du jour de chaque clé : reste ≤ part au pire, ou sous un cinquième du crédit → alerte écrite pour la mère et départ refusé (code 3). La clé Claude, si son solde est illisible, est comptée au crédit déclaré par la pièce de départ moins la dépense antérieure déclarée.

## 7. Épreuve réelle des témoins (devis à part, avant la course)

11 témoins × (aiguilleur + deux juges) = **33 appels** (22 sur le relais Claude, 11 sur Argon). Estimation 1,13 USD (Claude 0,75 ; Argon 0,38) ; haut 3,39 USD ; **plafond 5 USD**, ligne de GO à part. Relais propres à l'épreuve (lancés, lus, arrêtés par PID), car la porte à blanc de la course exige des relais neufs. Règle écrite d'avance : un témoin manqué → aucune course, aucune retouche des témoins sans version neuve et mot de la mère.

## 8. Total demandé

Course 90 USD (plafond d'arrêt) + épreuve 5 USD = **95 USD au plus** sur le budget des appels d'interface ; attendu ≈ 27 USD (dont ≈ 16,5 sur la clé Claude offerte).
