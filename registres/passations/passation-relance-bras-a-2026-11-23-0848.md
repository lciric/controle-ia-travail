# Passation — relance du bras A des organismes discrets — 2026-11-23 08:48Z

Session `session_016QhUrrrYhWqY2wZxYXUop5` (reprise sur l'autre compte, GO-2026-11-23-09), mère `session_016QhUrvi45g3jX5saFefVED`. Branche `relance-bras-a/reprise-2026-11-23-v1`. Passation scellée ; ne pas réécrire. Arrêt sur gel (GO-2026-11-23-15 relayé par la mère à 08:33Z, non encore vu sur main à 08:34Z ; appliqué parce qu'il ne fait qu'arrêter).

## Fait
- Reprise annoncée : `registres/passations/reprise-relance-bras-a-2026-11-23-0826.md` (`289c5b2e…`).
- Constat porté à la mère : la section 5.5 du devis de la carte v5 (`40b999f8…`, branche `relance-bras-a/devis-carte-v3`) exige de citer trois pièces scellées des étapes (c) à (h) (fichier des deux comptes des actions d'épreuve relues, verdict d'épreuve, puissance), absentes. Plafond : les chiffres de la v5 font foi (≈ 47 à 50 USD, repli 85) ; le « 75 » venait de la v2 (corrigé par la mère).
- **Brouillon 1 du complément de devis de la ligne 2** (distillation et rejeu), décision (a) de la mère, rédigé par Fable 5.2 en effort maximal (lancé avant la règle de dosage GO-2026-11-23-14 ; laissé finir sur le mot de la mère), **versé sans contre-lecture** sur le gel :
  - `docs/notes/relance-organismes-discrets-v1/complement-devis-ligne-2-bras-a-v1-brouillon1.md` — `db64675058fc24fdb4e89b225779b5d274f4d88ccfca5ecbf2ec4a238c7c210e`
  - `…/calcul-complement-devis-ligne-2-bras-a-v1.py` — `85921b3fae0265db9a4615cc7e4db3c37e21a457a6bf1e6efdec4dfa9fa01db7`
  - `…/calcul-complement-devis-ligne-2-bras-a-v1-sortie.txt` — `f271ab2d240260331138523e91cb8f2e160c21756cbeaefa30cecc349b579289`
  - Selon le rédacteur : débit 35,91 s par épisode (4 596,47 s sur 128) ; mise en route 0,068 h (243 s), lecture prudente 0,234 h, toutes deux sous le plancher de 1,0 h ; plafond calculé 44 USD (14,40 h) ; repli 85 USD sans objet ; seuil de 96 s mesuré à 37 %. Points (1) et (5) « en attente » ; tarifs à relever le jour de la demande.
  - Doutes du rédacteur, à reprendre à la contre-lecture : (i) le texte scellé place le fichier des deux comptes « avant le devis » (6.3 (i)) : le brouillon s'appuie sur la lecture de la mère, dite en tête ; (ii) lectures hors liste déclarées (quatre valeurs de tête du manifeste, cinq lignes du devis v2, registres des arrêts, des dépenses, consignes de main) ; (iii) page dense (≈ 2 270 mots) pour « une page ».
- **GO-2026-11-23-13** (Lazar, 08:31Z) : cette session conduit les étapes (c) à (h), en déléguant à des agents neufs, sous les interdits listés. **Reste acquis pour la reprise** ; rien n'a été lancé.
- Agent de préparation de l'étape (c) (Opus) arrêté par son identifiant sur le gel ; il n'avait rien écrit sur disque.

## Reste (à la reprise)
1. Contre-lecture du brouillon 1 par Opus 5.5, puis vérification des corrections par le même ; soumission au GO seulement après les trois pièces scellées.
2. **Point à instruire avant l'étape (c)** : `lots_bras_a_v5.py`, `lots_bras_a_v6.py` (`6075b55e…`) et `epreuves_couverture_bras_a_v4.py` (`9502437b…`) n'existent pas au commit du code arrêté `2b9f82328` et le texte scellé ne les nomme pas ; `fabrication_v3.py`, `instrument_appariement_v1.py`, `reponses_lecteurs_v1.py` y sont, identiques. Écart possible ⇒ nœud. Inscrit par la mère.
3. Étapes (c) à (h) dans l'ordre de 6.3 : programme de conduite de (c) à écrire et éprouver sur épisodes fabriqués ; avant (d) : constat des conditions d'envoi (D4 de GO-2026-11-22-143) et lignes de GO par lot.
4. Dosage (GO-2026-11-23-14, consigne de la mère) : (c) et (h) par programme sous Opus effort moyen ; juges et lecteurs selon le texte scellé ; verdict de (g) par agent neuf (Fable effort maximal s'il juge une porte, sinon Opus effort élevé) ; compléments de devis : Fable 5.2 effort élevé.
5. Restes de la passation de 06:20Z inchangés (enchaînement de la discrétion v4, garde au chargement, six mineurs).

## Réserves
- GO-2026-11-23-15 (gel) appliqué sur relais de la mère, avant de le voir inscrit.
- Inventaire Vast.ai non fait (outil absent du conteneur) ; aucune instance du bras A selon la passation de 06:20Z ; aucune créée ici.
- Le brouillon n'est pas contre-lu (R2) : il n'est pas engageable.

## Prochaine action
Au dégel : contre-lecture du brouillon 1 du complément (Opus 5.5), puis instruction du point des trois modules écrits après le code arrêté, avant tout lancement de l'étape (c).

## Instances actives
Aucune pour le bras A. Dépense de la session : 0 USD.
