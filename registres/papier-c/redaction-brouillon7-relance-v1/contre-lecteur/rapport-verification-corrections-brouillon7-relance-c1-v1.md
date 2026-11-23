# Papier C — vérification des corrections de la version c1 du brouillon 7 de relance (R2, seconde passe) — v1

- Contre-lecteur : le même que pour la première passe (sous-agent Opus 5.5, `claude-opus-5-5`), le 2026-11-22.
- Texte vérifié : `brouillons/papier-C-preenregistrement-HC1-HC3-v1-brouillon7-relance-2026-11-22-c1.md`,
  `ac324132cfa124f2da007567d42074e3bf25d868a2b77c6847be95cb12d38b7a`, égale à son compagnon et à l'empreinte attendue
  (branche courante, commit `c55eca46`). Source : `9c7a89f1…`, le texte de ma première passe.
- Rapport traité : `rapport-contre-lecture-brouillon7-relance-v1.md` (`30239c46…`).
- Interdits tenus, comme à la première passe ; aucun refus de permission ; écrit dans ce seul dossier.

**Décompte des remarques neuves : 0 bloquante, 0 majeure, 3 mineures (CV-01 à CV-03). Avis : scellable après
corrections** (trois mineures, que des errata peuvent traiter ; puis les verrous restants).

## 1. Le différentiel est celui de la table
Programme `travail/construire_brouillon7_relance_c1_v1.py` rejoué dans mon bloc-notes : sortie `ac324132…`
(252 760 octets), journal identique octet pour octet au journal versé. Le programme ne fait que des remplacements
exacts (fragment ou empan début-fin, chacun trouvé une fois), avec des gardes de sortie (titres, « À REMPLIR »,
marqueurs, précisions 1 à 40 nommées, disparition de « resterait immobile »). Les 41 identifiants C-01 à C-41 du
journal sont ceux de la note c1. J'ai relu le `diff` complet brouillon 7 → c1 (427 lignes) : chaque bloc répond à une
remarque ou à la mise à jour d'état qu'elle entraîne (titre, état en bref, historique, verrous 1, 3, 7, 8, 10, champ
« Contre-lecture »). **Aucun changement hors de la table.**

## 2. Les dix-neuf remarques

| Remarque | État | Lieu dans c1 |
|---|---|---|
| CB-01, réserve 20, argument « immobile » | **levée** (voir CV-02) | réserve 20 (a) ; précision 39, « Ce qu'elles ne disent pas » |
| CB-02, mention absente de la porte GC | **levée** | réserve 20, « Mention » ; combinaison « Porte GC » ; audit A9 ; mention commune sous le tableau ; combinaison « Mode d'induction » ; précision 39 |
| CB-03, précision 38, trois cas | **levée** (voir CV-03) | précision 38, « Règle », « Écart », « Cas de nœud » ; Plan, section 3 ; liste d'arrêt 15 |
| CB-04, précision 37 | **levée** | précision 37, prémisse, « Ce que cela emporte », « Statut » ; précision 36 ; verrou 1 ; état en bref, point (8) ; marqueur `<<MOT_DU_DIRECTEUR_H1>>` ; points ouverts v2, H-1 nœud sans défaut |
| CB-05, « contre-lu » | **levée** | condition de la version (a) ; issue 3 ; verrou 10 |
| CB-06, « sinon l'issue 3 » | **levée** | liste finie, « Nombre de niveaux » |
| CB-07, deux renvois | **levée** | Métrique, point 8 bis (précision 33) ; point 12 (précision 5) |
| CB-08, « aujourd'hui » | **levée** | liste d'arrêt 1 (19 et 22 novembre ; comptes conformes à mon recompte) |
| CB-09, dénominateur et tirage | **levée** (voir CV-01) | précision 39, « Dénominateur » ; précision 40 neuve ; Métrique, point 14 ; Plan, section 4 |
| CB-10, « proches de 1 / de 0 » | **levée** | précision 39, « Deux pôles, et rien entre eux » |
| CB-11, mention dans une seule colonne | **levée** | ligne C-P4 HC2 du tableau (mention retirée) ; « Mention commune aux lignes des sondes » sous le tableau |
| CB-12, « organisme » au singulier | **levée** | Plan, section 3, « Sondes » |
| CB-13, note des différences | **levée** | `note-differences-brouillon7-relance-c1-v1.md`, section 4, erratum |
| CB-14, R-4986 | **levée** | en-tête ; « GO » (GO-2026-11-22-114, R-4987, relu : « papier C … recréés en xhigh (session_013QMayk1rjSZrn2u9UAVhEp … ; anciennes sessions max archivées … rien poussé) ») |
| CB-15, « dose concave » | **levée** | Prédiction, contre-indices, « Forme de la loi » |
| CB-16, famille (ii) | **levée** | réserve 20 (b) |
| CB-17, pièces sans empreinte | **levée en partie ; le refus se tient** | liste finie : chemin complet et `0c62072c8fe7ea76f0d3dbe190c0f994fb1aa8c58ca793dddf60f412bf5bfb94` (conforme à mon calcul de la première passe) |
| CB-18, GO-2026-11-22-93 | **levée** | verrou 8 : table `docs/notes/veille-de-cap-v1/accords-a-prolonger-et-urgences-entretien-v2.md`, `a1c56fda…` recalculée, sur `main` ; ligne 10 (« AU 31 DÉCEMBRE, NON URGENTS (137) : GO-2026-10-20-06, GO-2026-10-20-07, … ») et lignes 135 et 136 nomment les deux accords |
| CB-19, identifiants seuls | **levée** | réserve 20 ; précisions 38 à 40 |

**Le refus partiel de CB-17 se tient.** Les huit pièces laissées sans empreinte sont citées comme renvois d'histoire
(tables de traitement et notes des versions passées, outils de la session 16, premier jet `derivation.py`) ; aucune
règle ne s'y appuie, et leurs empreintes sont au contrôle des empreintes citées (`controle-empreintes-citees-c1-v1.txt`,
neuf « à regarder », aucun désaccord). Seul `docs/sha256sums-lancement-v2.txt` sert de preuve (il certifie les
empreintes du brief et du programme) ; son contenu est vérifié à chaque reprise par la routine R14, ce qui suffit.

## 3. Défauts neufs

### CV-01 — mineure — précision 40 : une graine partagée avec la génération ne se rejoue pas sans elle
- **Lieu** : Plan, section 8, précision 40 ; Métrique, point 14 ; Plan, section 4.
- **Citation** : « le harnais reçoit en plus une graine, et une seule : celle de l'épisode de la même tâche sous la
  condition de la relecture (clé `papier-C/etape2/episodes` …) … la graine ne sert à aucune génération de texte par
  l'agent ».
- **Constat** : si, dans l'épisode d'origine, la même graine (ou le même générateur) a servi à l'échantillonnage de
  l'agent et au tirage de la condition, une relecture sans génération consomme le flux autrement : les tirages de la
  condition ne sont plus les mêmes, L-SP et les témoins de l'instrument échouent, et rien ne dit si c'est un échec de
  l'instrument ou une sortie au sens du point 14. Deux lectures pour le programmeur du module.
- **Correction demandée** : écrire que les tirages de la condition viennent d'un flux propre, dérivé de la graine de
  l'épisode et distinct de celui de l'échantillonnage (par exemple par `SeedSequence.spawn`, précision 28), à la
  génération comme à la relecture ; si le harnais ne le permet pas, la précision 40 ne s'applique pas et la règle de
  sortie du point 14 joue (à dire au point ouvert du module).

### CV-02 — mineure — réserve 20 (a) : « côté contexte » dit plus que voulu
- **Citation** : « Or les cellules S et SP_m portent la même consigne de saboter et ne diffèrent, côté contexte, que
  par le paragraphe de bras ajouté au message système. »
- **Constat** : chaque cellule SP_m est un épisode neuf de la même tâche (Métrique, point 13 ; liste finie, « Modèle
  des deux gains d'écart ») : les tours antérieurs de l'agent et les observations diffèrent aussi entre S et SP_m.
  C'est par les consignes, non par tout le contexte, que les deux cellules ne diffèrent que du paragraphe de bras.
- **Correction demandée** : « ne diffèrent, par leurs consignes, que par le paragraphe de bras » ; la conclusion de
  la réserve ne change pas.

### CV-03 — mineure — précision 38 : la famille (iv) jugée « sans objet »
- **Citation** : « (2) sur la famille (iv) si le verdict la juge pour ce mode » ; « Cas de nœud … critère jugé sur une
  seule des familles (i) et (ii) ».
- **Constat** : si le verdict nomme la famille (iv) mais déclare le critère « sans objet » pour elle (aucune dose où la
  base « mots et coût » échoue), deux lectures : (iv) est « jugée » et n'impose rien (aucune dose), ou elle ne l'est
  pas. Le résultat est le même dans les deux lectures pour la désignation, mais la lecture « (iv) jugée sans objet :
  nœud », par analogie avec (i) et (ii), en donne une troisième.
- **Correction demandée** : une phrase : « critère “sans objet” pour la famille (iv) : la famille (iv) n'impose rien,
  sans nœud ». L'ajout de (iv) à la règle de D-21 est un choix déclaré du rédacteur (table de traitement, section 2) ;
  il est plus sévère que « (i) et (ii) » et suit la lettre de N-053 ; la liste des points ouverts v2 le reporte à
  l'option (a) de D-21, ce qui convient.

### Le reste, regardé sans défaut
- **Réserve 20 réécrite** : l'argument est maintenant symétrique (confirmation à vide, réfutation des deux côtés,
  opposition établie ou inversée, ligne GC) ; les trois lectures nommées existent dans le texte (différence des
  différences, TC.2 lecture (3) ; L-HP ; parts) ; aucune ne tranche, aucune règle neuve.
- **Précision 39** : dénominateur univoque (tâches gardées ; D₀ de toutes les tâches écrit à côté ; prérequis D₀ lu
  sur les tâches gardées) ; « deux pôles » sans lecture intermédiaire.
- **Précision 37** : prémisse juste ; « ce que cela emporte » déclaré avec le sens (C-P2 et C-P6 vers la réfutation) ;
  part des tirages où ĉ s'échappe rapportée (précision 36 complétée) ; statut de nœud sans défaut, marqueur, et ce qui
  suit si la lecture écartée est retenue (version neuve, grille rejouée). Cohérent avec le verrou 1, l'état en bref et
  les points ouverts v2.
- **Condition de la clause et issue 3** : alignées entre elles et avec le verrou 10 ; plus de troisième lecture.
- **Mention commune, porte GC, audit A9** : cohérentes entre la réserve 20, la précision 39, les combinaisons « Porte
  GC » et « Mode d'induction » et l'audit ; partout « ne change ni règle ni verdict ». Je n'y vois pas une
  modification d'un critère de porte (la règle et le seuil de GC sont inchangés).
- **Précision 40** : renvois présents au point 14 et à la section 4, conformes à la table des passages fixés ; la clé
  citée est bien celle de la précision 32. Sous réserve de CV-01.
- Aucune contradiction interne trouvée, aucune revendication, réfutation ou confirmation nouvelle, aucune phrase qui
  vise un signe.

## 4. Rien de ce qui est tranché n'a bougé
Le `diff` ne touche ni les énoncés de HC1, HC2, HC2b, HC3, ni le tableau des prédictions, ni la section « Seuil », ni
les marges, ni la règle de HC2, ni les décisions D-1 à D-20. Changent seulement : la précision 37 (prémisse et statut ;
sa règle, « C-P3a et C-P3b toujours lues », est inchangée en attendant le mot du directeur), la précision 38 (règle de
désignation : proposition D-21), les précisions 36 et 39, la précision 40 (neuve), la réserve 20, la mention, les
gardes 1 et 15, la condition et l'issue 3 de la clause (ce que « contre-lu » veut dire), une citation de l'état de
l'art redressée.

## 5. Validateur
`problemes` rend la section « Contre-lecture » à remplir et dix-sept marqueurs : les seize d'avant et
`<<MOT_DU_DIRECTEUR_H1>>`. Conforme à `problemes-brouillon7-relance-c1-v1.txt`.

## 6. Ce que j'ai lu, en fait
Le message de la session ; le texte c1 par le `diff` complet avec le brouillon 7 (relu en entier à la première passe) ;
la table de traitement (en entier) ; la note des différences c1 (erratum et décompte des lignes « C- ») ; le programme
de construction c1 (fonction principale ; exécuté) et son journal (identifiants, comparaison octet pour octet) ; les
points ouverts v2 (lignes trouvées par « (iv) », « H-1 », « ventil ») ; le contrôle des empreintes citées c1 (bilan et
« à regarder ») ; la sortie du validateur c1 ; la table des accords prolongés v2 sur `main` (lignes 10, 135, 136 et
empreinte) ; la ligne R-4987 de `registres/decisions.md`. Non lus : l'additif v2 à la fiche du module, le journal du
rédacteur v2 (empreintes non vérifiées par moi), et tout ce qui est interdit.

## 7. Avis d'ensemble
**Scellable après corrections** : les dix-neuf remarques sont levées (CB-17 en partie, refus fondé) ; trois mineures
neuves (CV-01 à CV-03) à traiter, par erratum ou par une version c2, puis à vérifier par moi. Restent ensuite les
verrous : mot du directeur sur la précision 37 (nœud, sans défaut) et sur D-21 et D-22 ; module et configuration ;
rapport complété de la grille ; taux de la réserve d'intention ; champs tirés au scellement ; versement sur `main`.
