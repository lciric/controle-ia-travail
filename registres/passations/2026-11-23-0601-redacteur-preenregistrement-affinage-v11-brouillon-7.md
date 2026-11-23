# Passation — rédacteur Opus du préenregistrement v11 de la course d'affinage : brouillon 7 et devis v11f

- Écrite le 2026-11-23T06:01:18Z (`date -u +%FT%TZ`), sur la branche `prep/preenregistrement-affinage-v11-opus-v1`. Elle suit, sans la réécrire, la passation `registres/passations/2026-11-23-0555-redacteur-preenregistrement-affinage-v11-brouillons-4-a-6.md` (`1f6b701f52fac97c5ec9e3a9d699e590a816db59287007904eae242516637211`), dont tout le reste vaut.
- Même rédacteur (Opus 5.5 en effort maximal, GO-2026-11-22-145). Aucun appel à un modèle externe, aucune dépense, aucune instance lancée.

## Fait

Pièces écrites et scellées (compagnons vérifiés), sous `docs/notes/organisme-affinage-mentors-v1/`, commit `99479b6d9` :

| pièce | chemin | sha256 |
|---|---|---|
| **brouillon 7** du préenregistrement v11 (333 lignes ; non scellé comme préenregistrement) | `course-v11/preenregistrement-course-affinage-mentors-v11-brouillon-7.md` | `f14bbcd1e1e6849c3d44922dc388eeb006031c22cc9ba9b3cbaa455c90d07f6c` |
| programme d'assemblage du brouillon 7 | `course-v11/assembler-brouillon-7-preenregistrement-v11.py` | `bc0abccf0f0ca3424f325a5df1ce64fad1f2b72056b39651e97202826cdf0e4e` |
| **devis v11f** (le v11e sans chiffre changé : R-5132, GO-2026-11-23-07, condition `hypothese_sortie_maximale_tenue`) | `devis-course-affinage-mentors-v11f.md` | `ae76963e3280e05ea66173ce17db44d0f884667aeb5e1ca59bba8ad378bc9885` |

Rejeu, à l'octet près : `python3 -I course-v11/assembler-brouillon-7-preenregistrement-v11.py course-v11/preenregistrement-course-affinage-mentors-v11-brouillon-6.md <sortie> 2026-11-23T06:00:40Z`.

Contrôles : 17 sections identiques à la v10 ; lignes 1 à 295 du brouillon 6 gardées à leur numéro (13 touchées), point 16 et dernière section récrits ; aucun nombre neuf ni disparu, au texte comme au devis ; renvois « devis v11, § n » retrouvés dans le devis v11f ; 14 « EMPREINTE À INSCRIRE » et 4 « RÉFÉRENCE À INSCRIRE » (réponses de la session de l'organisme datées 05:58Z).

Ce que porte le brouillon 7 : R-5132 cité à la place des emplacements des décisions datées 05:45Z ; mesure préalable d'Argon accordée par Lazar (GO-2026-11-23-07 : « go recos » vers 05:55Z, plan de R-5132, plafond 10,50 USD, échéance 2026-11-30 ; inscrite par R-5134), jouée après le scellement du texte et avant le départ ; deux cas gardés (R-5132 : texte valable avec ou sans la mesure), une mesure dont un envoi est parti relevant du cas « avec la mesure » ; condition ajoutée à la règle de lecture (réponse mesurée qui porte `hypothese_sortie_maximale_tenue` faux) ; fiche du juge confirmée ; lecture des fonctions de fiches faite sur la copie v53 (`fiches_v53.py`, `7cfcf832…`), que la contre-lecture vérifie sur la v54 épinglée (§ Contre-lecture, phrase ajoutée).

## Échanges avec la session de l'organisme

- Reçu à 05:53Z (« 05:54Z ») : mesure accordée par Lazar (GO-2026-11-23-07, plafond 10,50 USD, plan de R-5132), à citer ; jouée seulement après le scellement (R1) ; empreintes v11d toujours attendues.
- Reçu à 05:56Z (« 05:58Z ») : points 1 (borne de 10,50 USD) et 2 (fiche du juge) retenus, lecture sur la v53 à dire ; point 3 ajouté (`hypothese_sortie_maximale_tenue`) ; décisions datées 05:45Z sous R-5132 ; emplacements à remplir avec R-5130, R-5132 et GO-2026-11-23-07.
- Vérifié sur `main` au commit `1b26780dc04631554f0d344b3d5a527f8b7855ce` (`registres/go.md` `f17a81eadd8664abe32415ba81dd05abf7bbf63f120c37c7856594d76d7c3be7`, `registres/decisions.md` `f975fe6a48d8a57e9c66dc8bdecf85cf59d2df35922e004d5e66a7c0472c499d`) : R-5132, R-5134 et la ligne GO-2026-11-23-07 existent et disent ce que la session de l'organisme en rapporte ; aucune ligne ne porte encore les réponses datées 05:58Z (R-5132 à R-5136 lues).
- Envoyé après la poussée de cette passation : chemins et empreintes du brouillon 7 et du devis v11f.

## Reste

- Empreintes définitives des pièces du lanceur v11d, après la vérification du même contre-lecteur ; ligne du registre qui porte les réponses datées 05:58Z. Écrire alors le texte scellable sous `course-v11/preenregistrement-course-affinage-mentors-v11.md`, sans la ligne d'état ni la dernière section du brouillon 7.
- Contre-lecture du préenregistrement et du devis v11f par un Opus neuf, qui vérifie aussi la lecture des fiches sur la v54.

## Réserves

- Les réponses datées 05:58Z changent la règle de lecture de la mesure (condition ajoutée) sans ligne de registre encore : emplacement « RÉFÉRENCE À INSCRIRE » laissé, à remplir avant le scellement.
- Le cas « sans la mesure » reste ouvert après l'accord de Lazar (R-5132) : si la mesure n'est pas jouée avant l'échéance de GO-2026-11-23-07 (2026-11-30), la course peut partir sans elle, sous les risques dits.
- Essais du dépôt : non relancés depuis la passation précédente (aucun fichier de `src/` ni de `tests/` changé) ; résultat d'alors : coupés par leur minuterie à 72 %.
- `registres/etat.md` non modifié ; aucune demande de fusion.

## Prochaine action

Sur le mot de la session de l'organisme, avec les empreintes définitives du lanceur v11d et la référence des réponses datées 05:58Z : écrire le texte scellable. Sinon, rien.

## Instances actives

Aucune lancée par cette session. Relevé en lecture seule à 06:00Z : Hetzner, liste vide pour le jeton de cet environnement ; Vast.ai, quatre instances en marche qui ne sont pas de cette session — 62094628 (`iib-voie-a-v1`, R-5111), 62096662 (`b5f-lecture-v1`, R-5119), 62097676 (`bras-a-ligne-1-v1`, relance du bras A, R-5122) et 62105206 (`t08-v1`, neuve depuis 05:41Z ; T0.8, R-5133 et GO-2026-11-23-05 selon le registre) — et quatre arrêtées (58936096, 58936099, 58936100, 60988826). Aucune touchée : leurs tâches relèvent de la mère (R10).
