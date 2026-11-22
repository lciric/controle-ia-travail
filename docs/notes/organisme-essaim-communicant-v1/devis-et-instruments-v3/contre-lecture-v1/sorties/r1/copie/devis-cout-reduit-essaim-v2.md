# Devis à coût réduit — essaim qui communique — v2

- Sous-agent (Claude Opus 5.5), 22 novembre 2026. **Aucune dépense, aucun appel, aucun réseau.**
- Calcul : `calcul_devis_cout_reduit_v2.py` → `calcul-devis-cout-reduit-v2.json`.
  - Il importe `calcul_devis_essaim_v3.py`, `calcul_pilote_essaim_v2.py` et `garde_pilote_essaim_v1.py`.
  - Tout chiffre ci-dessous est un champ de cette sortie, sauf mention contraire.
- Pièce remplacée : `docs/notes/organisme-essaim-communicant-v1/devis-et-instruments-v2/devis-cout-reduit-essaim-v1.md`. Elle reste intacte.
- Les HYPOTHÈSES et PROPOSITIONS sont celles de la v1 (champ `hypotheses`), à une exception près : **la mise en route du modèle ouvert au pilote** (§ 3).

## Verdict

- **Le levier qui donne un à deux ordres de grandeur reste (d)** : faire d'abord le pilote P-std.
  - À espèce égale, il divise l'estimation du programme par **20,1 à 49,0** (`facteurs_par_levier.d_pilote_d_abord_meme_espece`, quatre espèces, sorties 6 000 et 12 800).
  - Sur Kimi : 57 à 102 USD contre 2 809 USD.
- **Pilote recommandé** : P-std sur Kimi par l'interface payante.
  - Estimation : **57 à 102 USD**.
  - **Vrai pire : 203,94 USD**, borne dure appliquée par le lanceur (`garde_pilote_essaim_v1.py`), sous les hypothèses H1 à H4 du § 4.

## 1. Facteurs par levier, sur le programme (cas attendu ; R5 corrigée)

Le texte de la v1 disait : « les autres leviers ne donnent chacun qu'un facteur de 1,1 à 2,5 ». C'était faux, (a) « tout » allant jusqu'à ×8,2 dans la même pièce. La v2 ne cite que les bornes calculées : champ `facteurs_par_levier`, minimum et maximum sur Kimi, la première espèce Claude, Fable 5.2 et la seconde espèce Claude.

| levier | facteur (min – max) | remarque |
|---|---|---|
| (a) proposeurs et messages sur modèle ouvert | ×1,15 – ×1,27 | débit, utilisation et mise en route : HYPOTHÈSES |
| (a) tout sur modèle ouvert (vérificateur sur Argon) | **×2,25 – ×8,20** | le même 1 250 USD pour toutes les espèces ; pire 3 283 USD |
| (b) lots, remise de 50 % non vérifiée | ×1,50 – ×1,83 | remise sans pièce |
| (b) cache (Fable seulement) | ×1,32 | seul tarif de cache à pièce |
| (c) tests et objets de contrôle échantillonnés à 20 % | ×2,08 – ×2,47 | invalidation probabiliste (v1, § 1 c) |
| (e) sorties courtes | ×1,06 – ×1,09 | les tests dominent le programme |
| (b) + (c) + (e), avec remise | ×4,77 – ×4,83 | remise non vérifiée |
| (b) + (c) + (e), sans remise | ×2,49 – ×2,88 | tarifs à pièce |
| (d) pilote d'abord (même espèce) | **×20,1 – ×49,0** | une seule question (porte), non une réponse |

Lecture corrigée :
- sur le programme, un levier seul donne de ×1,06 à ×2,5, **sauf (a) « tout sur modèle ouvert »**, qui va jusqu'à ×8,2 ;
- les leviers combinés donnent environ ×2,5 à ×4,8 ;
- seul le pilote d'abord donne un à deux ordres de grandeur.

## 2. Pilote P-std par l'interface (USD)

Source : champ `pilote_P_std_api`. Les pires « sous gardes » viennent de `garde_pilote_essaim_v1.borne_pire`, appliqués au plan gelé de 744 appels.

| espèce | estimation 6 000 / 12 800 | pire de la v1 (conditionnel) | **vrai pire sous gardes, plafond 24 000** | sous gardes, plafond 8 000 |
|---|---|---|---|---|
| Kimi | 57,29 / 102,17 | 203,80 | **203,94** | 96,10 |
| première espèce Claude | 114,58 / 204,34 | 407,59 | 407,89 | 192,21 |
| Fable 5.2 | 229,15 / 408,67 | 815,19 | 815,78 | 384,42 |
| seconde espèce Claude | 286,44 / 510,84 | 1 018,99 | 1 019,72 | 480,52 |

- Pourquoi le vrai pire est presque égal au pire conditionnel de la v1, à quelques centimes près :
  - les relances au plus 10 % remplacent la marge de 10 % ;
  - la section C.8 (105 %) est remplacée par la réserve dure des appels échoués (octets + 256 jetons) et par l'excès possible d'un seul appel au-delà du plafond de jetons d'entrée.
- **La différence est de nature** : 204 USD était un pire si quatre gardes, alors proposées, existaient. 203,94 USD est le plafond de dépense que le lanceur applique avant chaque appel (code 14). L'épreuve du pire extrême, où tout est au plafond et où 74 échecs sont comptés à la réserve dure, finit à 198,80 USD, sous la borne (`epreuves-gardes-pilote-v1.json`).
- Avec une relance permise par appel et sans garde, le pire valait 370 USD (vérification de la v2, § 4). Les gardes ferment ce cas : la 75ᵉ relance arrête la course (code 13).
- Remise par lots (non vérifiée) : environ 51 USD à l'estimation de 12 800 sur Kimi.
- Plafond de 8 000 jetons : il réduit le pire (96 USD sur Kimi) mais **tronque** un appel de Kimi tel que mesuré en v67 (environ 12 800 jetons pour deux cartes, chiffre de seconde main). À refuser, comme en v1.

## 3. Pilote P-std sur modèle ouvert (A100 à 1,4 USD/h ; R5 corrigée)

- **La division par 5 de la mise en route est retirée.**
  - La v1 l'appliquait à la ligne 146 de `calcul_devis_cout_reduit_v1.py` sans la déclarer ni la justifier.
  - Je ne trouve aucune pièce qui la justifie. Le pilote compte donc la mise en route entière de l'HYPOTHÈSE : 10 h à l'estimation, 30 h au pire.
- Les messages sont comptés à leur propre sortie (400 jetons à l'estimation, 2 000 au pire), et non à celle des proposeurs.
- Source : champ `pilote_P_std_modele_ouvert`.

| cas | heures de carte (dont mise en route) | USD |
|---|---|---|
| estimation, sortie 6 000 | 16,2 (10) | 24,88 |
| estimation, sortie 12 800 | 21,8 (10) | 33,61 |
| pire (débit, utilisation et mise en route au pire) | 209,6 (30) | 338,97 |

- La v1 annonçait 25 USD et 347 USD au pire, avec la mise en route divisée par 5 et les messages à 12 800 ou 24 000 jetons. La nouvelle estimation est plus haute (24,88 et 33,61 contre 25), le pire plus bas.
- Le pire sur modèle ouvert **n'est borné par aucune garde** : il dépend d'un débit inconnu. Le plafond de la carte est en heures, et les gardes du lanceur portent sur des jetons facturés.
- Décision du directeur : le modèle ouvert sur carte louée sert aux expériences et aux tests seulement. Il n'est donc pas une voie du pilote décisif. Ce chiffrage reste une réserve.

## 4. Hypothèses sous lesquelles le vrai pire tient (gardes du lanceur)

- **H1** : le fournisseur facture au plus l'usage qu'il rend. Contrôle : la facture, rapprochée du journal (réponse 14, A.4, point 1).
- **H2** : la sortie, réflexion comprise, ne dépasse pas `max_tokens`. Contrôlée après chaque appel (code 16). **À vérifier chez le fournisseur de Kimi avant le GO** : si sa réflexion n'est pas comprise dans `max_tokens`, le plafond de 24 000 ne borne rien.
- **H3** : un jeton couvre au moins un octet, plus 256 jetons de mise en forme. Contrôlée après chaque appel (code 16).
- **H4** : un appel échoué coûte au plus sa réserve. Contrôle : la facture.
- Le tarif de Kimi est repris par citation (`91f5cf8f…`), sans relecture de sa pièce primaire.

## 5. Recommandation (inchangée sur le fond)

- **Pilote** : P-std sur Kimi par l'interface payante, sans test de mort ni aiguilleur, plafond de sortie de 24 000 jetons, **lancé par `lanceur_pilote_essaim_v1.py` seulement**.
- **Montants** : estimation 57 à 102 USD ; plafond de dépense dur à 203,94 USD.
- **Programme** : (c) et (b) n'y entrent que si le pilote passe la porte.
- **Courses confirmatoires** : sur les meilleurs modèles payants (décision du directeur). Le modèle ouvert sert aux expériences et aux tests.
