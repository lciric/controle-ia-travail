# Contre-lecture, tour 2 : addendum d'empreintes de l'idée 1.1 (poids du nul), brouillon 2

- Pièce lue : `docs/notes/organisme-idees-juge-v1/addendum-empreintes-idee-1-1-v1-brouillon2.md`
  (`d2b20dee4feecc73d3d4be8f409bc9569bd29c30d320f5e4c7d536d45ca504ce`, égale à son compagnon). Version précédente : brouillon 1
  (`6bab777fd312efe921f2183508069aa12fb8aedc5b8b410fdd415dca91f4c7d9`). Rapport du tour 1 :
  `78ced47dfa2d6a0841a4a597ff8b516ccae35d8fa7ec157ce4b53157c052bb64`.
- Lecteur : contre-lecteur neuf, lettre C. Je n'ai écrit aucune des pièces. Dépôt lu sur `main`, tête `29f2cc63`.
- Date (UTC, `date -u`) : 2026-11-16, de 14:03 à 14:05 environ.
- Mes calculs : `diff` des deux brouillons ; un petit programme qui extrait les couples du rapport du tour 1 et les compte dans
  les deux brouillons ; un seul `--lister-empreintes` (`scripts/etape0_idee_1_1_v5.py`) ; un appel de
  `execution_idee_1_1_v5.lire_addendum` sur la pièce ; des `sha256sum` ; des lectures de `scripts/jouer_idee_1_1_v5.py` et de
  `execution_idee_1_1_v5.py`. Aucun jeu, rien sous `diag/`, `runs/`, `donnees/`, rien dans les deux copies interdites, aucun
  réseau, aucun git de ma main, aucune valeur de clé. Travail jetable sous le bloc-notes de la session.
- **Incident de ma main** : aucun.

## 0. Verdict

**Scellable** : aucune correction exigée. Les neuf couples du tour 1 sont appliqués fidèlement, le différentiel ne contient rien
d'autre que les quatre couples déclarés du rédacteur, et tout ce que j'ai refait tient. Deux remarques facultatives (§ 4) et deux
points pour la session mère (§ 5).

## 1. Différentiel brouillon 1 vers brouillon 2 (`diff`)

Dix hunks, tous rattachés :
1. l. 1 : titre « brouillon 1 » vers « brouillon 2 » (couple du rédacteur, déclaré).
2. l. 10 à 12 : puce « Brouillon 2 » en en-tête (couple du rédacteur, déclaré).
3. l. 285 : M7 (chronométrage par groupe), phrase insérée avant « Somme sur les 30 lignes ».
4. l. 328 : m2 (R-2979 et R-2976).
5. l. 349 : m3 (R-2978 dans le statut de D5).
6. l. 360 et 361 : m4 (ordre du lanceur, deux couples liés).
7. l. 376 : m5 (« log W non fini là où le banc le contrôle »).
8. l. 383 : M1 (reprise).
9. l. 396 et 397 : m1 (jeton) et m6 (point 3 neuf, ancien point 3 devenu 4).
10. l. 402 : section « Contre-lecture » remplie (réponse point par point) ; l. 422 : déclaration d'exclusion du brouillon 2.

Rien d'autre : les 46 lignes du § 1, le bloc programme du § 2, les tableaux, § 3 hors m7, § 4 hors m2 et m3 sont inchangés.

## 2. Corrections du tour 1 : appliquées fidèlement

Programme jetable : les neuf couples « ancien → nouveau » du rapport du tour 1 (§ 2), extraits du rapport par expression régulière.
Pour chacun : « ancien » trouvé une seule fois dans le brouillon 1 (9 sur 9), « nouveau » trouvé une seule fois dans le brouillon 2
(8 sur 9 en comparaison directe ; le neuvième, m6, est donné en deux morceaux par le rapport et je l'ai vérifié à la main : le
point 3 neuf est mot pour mot celui du rapport, l. 400, et « 4. Copie propre du commit… » suit, l. 401).
Les « anciens » de m1, m2, m3, m4 (deux) et m5 ne figurent plus dans le brouillon 2 ; ceux de M1 et de m7 sont des préfixes de
leur « nouveau » (ils figurent donc encore, comme attendu).
- M1 : texte inséré à l'identique. Je l'ai vérifié contre le code : en reprise, `jeu_decisif` saute `exiger_sortie_absente`,
  `lancer_essais`, `MU.jouer_banc`, `E0.essais_d_egalite` et la création du manifeste ; il lit le `depart.json` du premier
  départ ; il revérifie préenregistrement, arbre propre hors des dossiers du run (`exiger_depot_propre_sauf_run`), addendum,
  copies, noms empruntés. Une tranche sans compagnon fait lever `GardeArret` dans `tranches_deja_ecrites`, appelée dans
  `executer`, lui-même sous le `try` qui appelle `consigner_arret` : exact.
- m1 : le jeton `ACCORD-D5-A-REMPLIR` ne figure plus qu'une fois (l. 354, § 4.4).
- m4 : l'ordre écrit est celui du code (addendum, copies, noms empruntés, puis `exiger_sortie_absente`, puis essais).
- m6 : l'empreinte `539f6a6c…` de `essai_projection_cas_v1.py` recalculée, égale.

## 3. Vérifications refaites

1. `--lister-empreintes` : 46 lignes ; `diff` avec les lignes du format de la pièce : **identique** ; la pièce n'a pas d'autre ligne de
   ce format (46 correspondances au total).
2. `lire_addendum` sur la pièce : rend sans arrêt ; 46 fichiers ; 2 processus ; réductions vides ; D = 15,667 h ; règle rejouée
   égale, `jeu_permis` vrai ; étape 0 `540dfa68…`. Bloc programme : non touché par le différentiel, donc égal à l'octet au
   journal comme au tour 1 ; le lanceur le relit sans erreur.
3. Compagnons : brouillon 2, programme de couples (`appliquer-corrections-addendum-empreintes-idee-1-1-v1-brouillon2.py`) : égaux.
4. Aucun identifiant de modèle dans la pièce (recherche des noms usuels : aucun résultat) ; lettres seulement.
5. Déclarations (m9, m10, m11, comptes non écrits, lectures gelées, D1 à D5, E2, E3), commande, consigne de tâche active, borne de
   48 heures, liste d'arrêt : inchangées depuis le tour 1, où elles étaient exactes ; les phrases touchées ne les contredisent pas.

## 4. Remarques facultatives (aucune n'est exigée)

1. M1 dit « aucune graine n'est rejouée après un échec de garde » : phrase vraie du lanceur (`arret.json` interdit la reprise) mais
   la plus forte du passage ; je ne l'ai pas éprouvée au-delà de la lecture du code.
2. § 7 : au tour suivant (ou au scellement), ajouter une ligne « Tour 2 » avec cette contre-lecture ; le gabarit ne l'impose pas.

## 5. Points pour la session mère

1. **Lettres.** Le brouillon 2 déclare (en-tête et § 8) que les corrections ont été écrites par « un rédacteur neuf, lettre C ».
   La consigne de ce tour dit que les corrections sont écrites par le modèle A, et je suis moi-même C. Si la lettre est fausse,
   corriger avant scellement (« lettre C » dans l'en-tête l. 10 à 12 et dans le § 8 « rôle : rédacteur neuf des corrections du
   tour 1, lettre C »). Je ne peux pas le vérifier moi-même. Si c'est bien C qui a corrigé, je n'ai pas lu une version neuve
   de l'auteur des corrections : à noter, sans conséquence sur les empreintes ni sur le code.
2. **D6 (reprise)** : la lecture « pas un écart » est celle du rédacteur, non couverte par un mot de Lazar. Si la mère la juge écart
   de lettre à [T] étape 1, elle l'inscrit sous D6 et la porte à Lazar avec D5.
3. Rappels du tour 1, toujours vrais : le mot de Lazar sur D5 (`ACCORD-D5-A-REMPLIR` à remplacer, au § 4.4 seulement) est
   nécessaire avant la version qui fera foi ; la copie propre doit porter le commit de l'addendum ; garder une tâche active
   pendant tout le jeu (TERM au parent écrit `arret.json` et interdit la reprise) ; la réserve « fils oisif » n'est pas éprouvée
   sur ce code ; l'empreinte de `essai_projection_cas_v1.py` se contrôle à la main (point 3 du § 6).
