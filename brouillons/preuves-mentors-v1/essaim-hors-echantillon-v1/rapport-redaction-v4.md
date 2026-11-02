# Rapport de rédaction — préenregistrement hors échantillon, brouillon 4 — v4 (traitement de la contre-lecture 3)

Rédacteur : le sous-agent auteur des brouillons 1 à 3 (il n'a écrit aucune contre-lecture). Contre-lecture 3 traitée :
`brouillons/preuves-mentors-v1/essaim-hors-echantillon-v1/contre-lecture-3-preenregistrement-essaim-hors-echantillon-v1.md`,
sha256 `b454118f7ed75aeb7887ec4e090a6845699414f8147efbd9755516cad3194cb4` (commit `f1ada8d2`), sur le brouillon 3
(sha256 `d1d5740e202dd972d017b236969acf499341b8187d6cbfcf63d571b36451e343`). Ce fichier est le fichier de traitement
cité par l'entrée de forme fixe de la contre-lecture 3 ; il ne cite donc pas l'empreinte du brouillon 4.

**Voie B, décidée par la session principale (routine) ; pas de contre-lecture 4.** Le brouillon 4 est produit par le
script `appliquer-contre-lecture-3-v1.py` (sha256 `c0409e6ae088221f70dea36440e55e44c203159f9f0ce1ca8e5d1f89cc022120`),
qui lit les treize remplacements dans la section 8 du rapport lui-même (après vérification des deux empreintes), exige
une occurrence exacte de chaque ancien texte et les applique mot pour mot ; sortie versée dans
`appliquer-contre-lecture-3-v1-sortie.txt`. Grille et code inchangés ; aucun commit ; aucune empreinte compagnon.

## Traitement, une ligne par point (tous appliqués mot pour mot, texte de la section 8)

- **C3.1** acceptée : 11 essais v3, dont un joué sur deux lanceurs.
- **C3.2** acceptée : inventaire des graines complété (77001, 77002, 31415).
- **C3.3** acceptée : l'étape 0.a gèle le texte à sceller, chaque rapport de contre-lecture et chaque fichier de traitement, y compris ceux de la contre-lecture 3.
- **C3.4** acceptée (a et b) : durée du `git fsck` ajoutée (une demi-minute à deux minutes, estimée).
- **C3.5** acceptée : ce que la grille 2 change vraiment par rapport à la grille 1 (critère de HP.4, drapeau, descriptif).
- **C3.6** acceptée : conséquence d'un run du lanceur v2 sur ce texte, et action (signaler à Lazar avant toute lecture).
- **C3.7** (recommandée) acceptée : tournure de la discriminance de HQ.5 à T = 20.
- **C3.8** (recommandée) acceptée : empreinte de `resolution_cl2.py` citée.
- **C3.9** (recommandée) acceptée : relevé de référence du `git fsck --unreachable --no-reflogs`, consigné avec son empreinte avant l'arbre séparé.
- **F1** acceptée : statut « brouillon 4 », mode de production dit.
- **F2** acceptée : auteur (brouillon 4 ; contre-lectures 1 à 3).
- **F3** acceptée : point 1 de la parade : le texte scellé diffère du dernier brouillon contre-lu par ses marqueurs et par les remplacements de la dernière contre-lecture (contrôle par `diff`).

## Écarts au strict « rien d'autre », imposés par la consigne « un seul marqueur »

La contre-lecture 3 prévoyait de remplir l'entrée de la contre-lecture 3 au scellement. La session principale demande
qu'elle soit remplie dès le brouillon 4 et qu'il ne reste que le marqueur du commit cité. Deux changements en découlent,
appliqués par le même script, nommés et contrôlés (une occurrence chacun) :
- **E1** — étape 0.d : la puce « le marqueur de la section « Contre-lecture » par l'entrée de forme fixe » et la phrase « exactement deux marqueurs » deviendraient fausses ; elles sont remplacées par « Les entrées des contre-lectures 1 à 3 sont déjà écrites en forme fixe (C5.2) dans la section « Contre-lecture ». Avant remplacement, le texte contient exactement un marqueur de gabarit, une fois ; après, aucun. »
- **E2** — section « Contre-lecture » : le marqueur `<<CONTRE_LECTURE_3>>` et sa note « remplacé au scellement » sont remplacés par l'entrée de forme fixe (brouillon 3 relu `d1d5740e…`, rapport `b454118f…`, traitement : ce fichier).

## Observations de la contre-lecture 3 (sans correction demandée)

- **O1** (version `lecture_hors_echantillon_v2` écrite à côté de `lecture_version` v3 dans `lecture.json`) : non corrigée (un module de plus) ; à dire dans la passation : `lecture_version` fait foi.
- **O2** (sens de « indépendantes ») et **O4** (codes sans glose) : non corrigées, comme le rapport le propose.
- **O3** (essai de la branche « manifeste illisible » de `exiger_principal_v3`) : non ajouté ici (le code et les essais v3 ne changent pas en voie B) ; éprouvée à la main par la contre-lecture 3.
- **O5** (empreintes compagnons à créer) : laissées à la session principale.

## Essais

L'essai v3 de recopie vise en dur le brouillon 3 (deux marqueurs) et reste juste pour lui. Un essai neuf,
`tests/test_simulation_essaim_hors_echantillon_v4.py`, vise le brouillon 4 : recopie de la table des énoncés et de la
phrase de portée v3, un seul marqueur, validateur, remplacement simulé, présence de chaque nouveau texte de la section 8,
entrée de la contre-lecture 3, commande citée v3.
