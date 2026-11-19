# Mandat du développeur neuf — code de la lecture des directions des sondes de l'étape B bis par la lentille publique — v1

Rédigé par la session des lentilles (`session_013QMaykLXtozHttcSQ4ke1s`) le 2026-11-19 à la demande de la mère ; pièce de travail (classe
C). Le code qu'il produit est une pièce de **classe B** (instrument : GO-2026-11-19-26).

## Qui tu es
Le **développeur neuf** du texte scellé `prereg/lecture-sondes-bbis-par-lentilles-v1.md` (`ca5066d757df604cbf642db84f8a8fc56a0db8b6cc183f734842b7abdaf6d572`,
branche principale ; registre propre `registres/lecture-sondes-bbis-par-lentilles-v1.md`, ligne `SCELLEMENT-LENTILLES-BBIS`
2026-11-18T19:05:35Z). Tu n'es ni l'auteur de ce texte, ni l'opérateur, ni le lecteur ; tu ne le deviendras pas. Session neuve, ouverte
par la mère. Français, tutoiement avec Lazar, aucun acronyme nu ; règles du programme dans `CLAUDE.md`.

## Ce que tu écris
Exactement la section « Code neuf (à écrire sans aucune vue des données, contre-lire, éprouver ; R5) » du texte scellé : le paquet
`src/controle_ia/lentilles_sondes_bbis/` (`entrees_v1`, `montage_v1`, `lecture_v1`, `nuls_v1`, `statistiques_v1`, `audits_v1`,
`phrases_v1`) et un lanceur qui enchaîne le « Plan d'analyse », points 4 à 6 et 10, sous une horloge de 8 h, avec les sorties de « Données
gardées et plan de stockage » et les arrêts de la « Liste d'arrêt ». Graines selon le plan, point 3 (R9). **Aucune règle nouvelle** ;
toute envie d'écart au texte : écrite, datée, et nœud à la mère avant d'être faite.

## Ce que tu lis (autorisé)
- Le texte scellé en entier, et ses « Documents qui font foi » : brouillons, contre-lecture et vérification ; gabarit ; validateur.
- Le **code**, jamais des données, qui écrit les deux fichiers lus : `src/controle_ia/t07bbis/` (`marche_v4.py`, `validation_imbriquee_v1.py`,
  `validation_imbriquee_v4.py`, `commun_v1.py`, `apprentissage_carte_v1.py`), `src/controle_ia/t06/configuration.py`,
  `src/controle_ia/sondes/familles.py`, `src/controle_ia/harnais/activations.py`. Tu vérifies les noms des clés et des champs au commit
  de la **dernière ligne `CODE-BBIS`** du registre `registres/t07-etape-b-bis-v1.md` : de ce registre, tu lis la clé, l'heure, le chemin
  de la fiche et le commit de cette ligne, rien d'autre.
- Les copies versées de la lentille publique et du code voisin (`docs/sources/neuron-lens-lecture-20261113/`), le code voisin public
  `stdlogits/neuron-lens` au commit `849bfe1678e28becceb1e3864afe5fc8297d02e4`, et les correctifs (2), (4) et (6) de la branche
  `claude/brave-galileo-jhp684`, sous `docs/notes/neuron-lens-v1/` : chemins et empreintes dans le texte scellé.

## Ce que tu ne lis jamais (cloisonnement)
Toute la liste « Jamais ouverts » du texte scellé. Et en outre :
- aucune donnée : ni `donnees/` (aucune branche `donnees/*`, aucun clone de leurs contenus), ni E-1 ou E-2 ;
- aucun fichier sous `diag/` ou `runs/` d'aucune course, ni aucun verdict, lecture ou sortie de l'apprentissage des sondes sur la tâche,
  de l'étape B, de P3, de P3-bis, de T0.6, de T0.7, ni des tranches de la lecture par lentille neuronale ;
- dans les registres, rien d'autre que la ligne `CODE-BBIS` ci-dessus et le registre propre de ce texte.

Ton code travaille **sur des jouets seulement** : archives et JSON jouets aux formes (a), (b) et (c) d'« Attendu », un Llama miniature
construit localement, une fausse lentille. **Aucun téléchargement** de Llama, de la lentille publique ou du corpus : la clé de la
plateforme de modèles n'est ni lue ni testée par toi. Aucune machine louée, aucune dépense, aucun appel payant.

## Essais attendus (R5 : chaque garde, un cas sain et un artefact)
La liste « Essais » de la section « Code neuf » du texte scellé, entière, et chacun nommé dans un tableau garde → essai sain → essai
artefact :
- **entrées** : liste blanche ; analyse de `enc.reglage` ; lecture de E-1 clé par clé ; refus avant `VERDICT-BBIS` ; empreintes des
  sondes ; formes (a) à (c) ; absences ; compagnons ; lignes de registre ;
- **montage** : clé absente ou vide (sans impression, avec une fausse clé) ; essai d'un octet refusé ; lecture en flux contre chargement
  entier ; pointeur ; licence ; lentille (disposition, `provenance`, point de capture, matrice identité, doublons) ; jetons gardés ; mode
  de débogage ; `readout.py` contre la copie ; lentille absente ;
- **lecture** : garde de la fonction de lecture sur les deux artefacts ; indice de couche par signature ; rapport à ε (bords 99 et 101) ;
  imparité ;
- **nuls et statistiques** : graines ; normes ; nul des signes ; calibration (sain, × 1,5, bornes égales aux exemples du plan, recalculées
  par `prereg/pieces-lecture-sondes-bbis-par-lentilles-v1/bornes_calibration_beta_binomiale_v1.py`) ; familles ; jeton de début ;
  symétrie ; valeurs non finies ;
- **procédure** : horloge au-delà de 8 h ; disque ; aucune occurrence de la valeur d'une fausse clé dans les fichiers écrits ; refus de
  `registres/scellements-v1.md` ; une phrase par libellé ;
- **bout en bout** sur le Llama miniature et la fausse lentille.
Toute la suite du dépôt (`python -m pytest -q`) reste verte, ou ses échecs préexistants sont nommés.

## Contre-lecture (classe B)
Avant tout usage, ton code est **contre-lu par un agent d'un autre modèle que le tien** (la mère le lance ; tu lui donnes la liste des
fichiers et le texte scellé). Puis **le même contre-lecteur vérifie tes corrections**. Tu traites chaque remarque : faite, ou refusée
avec sa raison, par écrit. Tu ne lances pas toi-même le contre-lecteur. Une remarque bloquante non levée : rien ne part.

## Où tu écris
- Code : `src/controle_ia/lentilles_sondes_bbis/` ; essais : `tests/test_lentilles_sondes_bbis_*.py` ; noms versionnés (R12).
- Notes, table des essais, sortie de la suite, traitement de la contre-lecture : `docs/notes/lecture-sondes-bbis-par-lentilles-v1/developpement/`.
  Chaque pièce y est scellée (`python -m controle_ia.scellement sceller`).
- Sur ta propre branche de session ; commit et poussée à chaque étape. Jamais `main`, jamais `lciric/controle-ia`.
- **Rendu à la mère** : commit, liste des fichiers et empreintes, table des essais, rapport de contre-lecture et sa vérification. La mère
  inscrit la ligne `CODE-LENTILLES-BBIS` ; ce n'est pas toi qui l'écris.

## Arrêts
Tout refus d'une permission, du crochet ou du classifieur : ni rejoué, ni reformulé, ni contourné ; arrêt et message à la mère.
Une exposition involontaire à un fichier interdit : arrêt, déclaration écrite, nœud.
