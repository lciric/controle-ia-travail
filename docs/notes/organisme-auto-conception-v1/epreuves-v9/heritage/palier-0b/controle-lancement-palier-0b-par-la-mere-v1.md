# Pièce de contrôle de la mère — lancement du palier 0b de l'héritage (étage processeur) — v1

Écrite par la session mère le 2026-11-21T06:33:35Z (`date -u`), avant l'étape 3, selon le préenregistrement v19 scellé, section « La pièce de contrôle de la mère », et les décisions R-4292, R-4296, R-4332 à R-4338. Accord : GO-2026-11-21-09. Processeur seul, sans dépense. Ce qui s'ajoute entre les lancements s'écrit dans des compléments numérotés, sous un nom neuf ; cette pièce reste intacte (R12).

## Valeurs lues par les programmes (une valeur par ligne, libellé fixe)

commit du code v6 : 8262c442332c9b79c58eb49c651f788c5397a7ef
commit du programme lancer_etapes_3_5_6_v2.py : 8262c442332c9b79c58eb49c651f788c5397a7ef
empreinte du programme lancer_etapes_3_5_6_v2.py : 1f04cb463c2fca7d2d67bfa3a8045bd4c9592e4e93bb564000ec102421cfdb14
commit du programme lancer_etapes_6bis_et_7_v1.py : 8262c442332c9b79c58eb49c651f788c5397a7ef
empreinte du programme lancer_etapes_6bis_et_7_v1.py : ed91813a88c9f58e65dd21d5e7a15fd6d4f2ae810787eb57bf57e7caceeb71d0
commit du programme lancer_etapes_8_et_9_v1.py : 8262c442332c9b79c58eb49c651f788c5397a7ef
empreinte du programme lancer_etapes_8_et_9_v1.py : 67052a4b7af9bd02c5f28f3b8a7926fd7b7ac5a98fb797f14b3d6f424bedc2a5

## Arbre lancé et texte présenté (règles n° 14 et 15 du code v5)

racine de l'arbre lancé : /home/user/palier-0b-racine
texte présenté : /home/user/palier-0b-racine/docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/preenregistrement-heritage-palier-0b-etage-processeur-v19.md
empreinte du texte présenté : 883b1b2ac89c4d7f691cd8e68529e0952bad470782ce365e4a39b35a10b2e375
pièce d'autorisation du verrou : /home/user/palier-0b-racine/prereg/organisme-auto-conception-v9/palier-0b/autorisation-verrou-palier-0b-v1.md
copie du code de l'organisme : /home/user/palier-0b-racine/docs/notes/organisme-courbe-dose-reponse-v1/code-organisme-94bfd92/orchestrator
dossier des sorties des étapes 3 à 6 : /home/user/palier-0b-racine/diag/heritage-palier-0b-v1/etapes-3-a-6

## Contrôles faits par la mère

- « Sur main » : `git merge-base --is-ancestor 8262c442332c9b79c58eb49c651f788c5397a7ef origin/main` rend vrai, le 2026-11-21T06:33:35Z.
- Les trois programmes, lus au commit du code v6 par `git show`, ont les empreintes ci-dessus ; leurs copies de l'arbre de travail de la mère aussi.
- Le texte présenté a l'empreinte ci-dessus, égale à son compagnon ; sa ligne « Commit du code d'analyse » porte le commit du code v6.
- La pièce d'autorisation porte, dans l'ordre de la décision R-4123, l'identifiant GO-2026-11-21-09, le commit du code v6, l'empreinte du texte présenté et l'heure de cette pièce.
- Le dossier des sorties n'existe pas à l'heure de cette pièce (relevé par l'organisme) ; son chemin ne porte aucune espace.

## Ordre des lancements

Programme 1 (étapes 3 à 6), puis programme 2 (étapes 6 bis et 7), puis programme 3 (étapes 8 et 9). Chaque lancement attend son complément, scellé avant lui : le 1 avant les étapes 3 à 6, le 2 avant 6 bis et 7, le 3 avant 8 et 9 ; le 4 après 8 et 9 (règle n° 8 et constat de fin). Le champ `commit` des manifestes est contrôlé au complément 4.
