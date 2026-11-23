# Rapport du développeur — correctif 0021 : contre-lecture du tirage sur la carte, tirage passé par l'ordre — v5

Date : 2026-11-22. Pièce d'instrument (classe B). Même développeur (Claude Opus 5.5). Ce rapport complète les v1 à v4, intactes. Il traite `contre-lecture-tirage-carte-0020-cl1.md` (« acceptable, aucun bloquant ») et la précision de la mère : en voie (A), GO-2026-11-22-73, l'étalonnage et la course sont rejoués sous « carte ». Rien poussé, rien dépensé, aucune machine, aucun modèle téléchargé.

- Branche locale `prep/iib-tirage-carte-local` ; base `5d3f4761d` (0020) ; 0014 à 0020 inchangés.
- **Tête `6696aca1fc57df7e4d5d3a26b3f25dd05d0d4f58`, arbre `725f3d5884c3617065aa913d04e9b3eee0e2afac`.**
- Correctif `0021-…patch`.

## Table de traitement

| remarque | traitement | où | essais |
|---|---|---|---|
| **m1**, uniforme à 32 bits d'entropie seulement (`b` fonction de `a`) | **corrigé** : `deux_hachages` rend `a` et `b`, tirés de deux hachages indépendants de (base, jeton), avec des sels distincts. u réunit 21 bits de `a` et 32 de `b`. `bruit_de_gumbel` s'appuie sur eux. | `harnais/tirage_carte_v1.py` | `b` diffère de l'ancienne fonction de `a` sur plus de 99,9 % de 64 000 couples, et la corrélation est inférieure à 0,02 (cas sain) ; l'ancienne construction est vue (artefact) ; u dans ]0, 1[, de moyenne 0,5 ; essais de loi (khi-deux, trois températures, le long d'une ligne, artefact du bruit uniforme) **rejoués**, tous réussis |
| **m2**, garde des logits sur les lignes finies | **corrigé** : `tirer(…, actives)` ne juge que les lignes actives ; `_boucle` et les suites passent le masque. Sans masque, toutes les lignes sont jugées, comme avant. | idem | NaN sur une ligne finie : le lot continue ; NaN sur une ligne active : arrêt ; sans masque : arrêt ; toutes les lignes finies : rien n'est jugé |
| **voie (A)**, tirage passé par l'ordre à l'étalonnage et à la course | **écrit** : `IIB_TIRAGE` (« processeur » par défaut, ou « carte »). Le lanceur de session v3 la vérifie (autre valeur : refus, code 2) et la passe à la machine (`-e IIB_TIRAGE=$TIRAGE`). Les deux amorces la vérifient à leur tour, la journalisent, et la passent au lanceur par `--tirage "$TIRAGE"`. | `scripts/lancer_iib_v3.sh`, `scripts/amorce_instance_iib_v5.sh` (h), `scripts/amorce_instance_iib_course_v5.sh` (c7) | textes des deux amorces et du lanceur ; `IIB_TIRAGE=gpu` refusé par le lanceur de session ; différentiels bornés mis à jour (amorce : +1 ligne ; lanceur de session : la seule commande de création) ; répétition locale (`sortie-repetition-locale-0021-courte-v1.txt`) : code 0, `TIRAGE=processeur` au journal des deux amorces, seconde machine refusée |
| **garde, même tirage** à l'étalonnage et à la course | **écrite** : `lanceur_v5.exiger_meme_tirage`, avant le manifeste de la course. Le tirage de l'étalonnage est lu dans son résumé scellé (`resultat.tirage`). Un résumé d'avant 0020, sans la clé, compte pour « processeur », seul tirage que ce code savait faire. Un résumé absent compte aussi pour « processeur » ; le mode réel l'exige déjà par ailleurs. Si les deux tirages diffèrent : refus. | `lanceur_v5.py` | cas sains : carte/carte, processeur/processeur, ancien résumé/processeur, résumé absent/processeur ; artefacts : carte/processeur, processeur/carte, ancien résumé/carte, résumé absent/carte |

## Nombres attendus
- Liste figée v6 (étalonnage) : **296** (`ATTENDUS = 296` dans la répétition).
- Liste de la course v2, sur une machine à carte : **312**, soit 296 + 2 pour le moteur à torch + 14 pour le tirage, dont l'essai marqué carte.
- Sur un poste à processeur qui a torch : « 311 passed, 1 skipped ».
- Le rejeu de ce poste est dans `sortie-essais-p1-v5.txt` : (A) liste v6, (B) liste de la course v2.

## Pour l'ordre
- En voie (A), l'ordre pose `IIB_TIRAGE=carte` pour l'étalonnage rejoué **et** pour la course. Le lanceur refuse une course qui ne tire pas comme son étalonnage.
- N-T2 tient toujours : le gain de vitesse sur carte n'est pas mesuré, et sur processeur le chemin neuf est plus lent au grand vocabulaire (v4, § 5). Le premier lot de l'étalonnage rejoué le mesurera de fait.
- L'essai marqué carte (déterminisme et bruit sur l'appareil) se joue sur la machine, par la liste de la course v2. **La liste de l'étalonnage (v6) ne le porte pas.** Si l'ordre veut le voir avant l'étalonnage rejoué sous « carte », il faut une liste de l'étalonnage en version neuve. Je ne l'ai pas faite sans demande.

## Livrables v5
- `0021-…patch` ;
- ce rapport ;
- `sortie-essais-p1-v5.txt` ;
- `sortie-repetition-locale-0021-courte-v1.txt`.

Arbre final : `725f3d5884c3617065aa913d04e9b3eee0e2afac`.
