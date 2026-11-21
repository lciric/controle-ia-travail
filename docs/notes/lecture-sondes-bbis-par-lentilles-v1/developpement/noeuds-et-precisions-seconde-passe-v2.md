# Nœuds et précisions de lecture du développeur de la seconde passe — v2 (2026-11-21, scellé)

Complète et rectifie `noeuds-et-precisions-seconde-passe-v1.md` (`ecb803cc…`), qui reste tel quel (R12). Écrite par le développeur
neuf des corrections de la seconde passe (mandat `mandats/mandat-developpeur-seconde-passe-lentilles-v2.md`, `a2132568…`), après la
contre-lecture `contre-lectures/contre-lecture-code-seconde-passe-v1.md` (`0c90e0f6…`). Tout ce que la v1 dit et que cette note ne
reprend pas vaut encore.

## Rectification de la v1 (correction non bloquante N1 de la contre-lecture)
- **N-dev-6, ligne 21 de la v1 : « aucune copie du code voisin n'est versée » est inexact.** Des copies du code voisin sont
  versées sous `docs/sources/neuron-lens-lecture-20261113/depot-neuron-lens/`, chacune avec son empreinte compagnon ; parmi elles
  `neuron_lens-lenses.py.txt` et `neuron_lens-transport.py.txt`, qui portent `load_fits` et `Accumulator`. Ce qui reste vrai : rien
  ne se télécharge, et ces copies sont archivées avec le suffixe `.txt`, non importées par le code ni par les essais.
- Ce que l'essai « extraction en flux égale au chargement entier » compare n'a pas changé : le chargement entier par `torch.load`
  du même fichier, et la formule de `Accumulator.mean` écrite dans le texte. La contre-lecture a lu les deux copies versées
  (`lenses.py`, lignes 95 à 116 ; `transport.py`, lignes 59 à 62) et tient l'écart pour acceptable : `load_fits` d'un seul fichier
  vaut `torch.load(…, weights_only=False)` puis `Accumulator.from_state(saved["state"])`, et `Accumulator.mean` la somme des moitiés
  divisée par `sum(n_docs)`.
- Réserve reprise de la contre-lecture : ces copies datent du 13 novembre (branche du voisin), non du commit `849bfe…` que le montage
  clone.
- Amélioration que la contre-lecture dit « possible, non exigée » (appeler la copie versée dans l'essai) : **non faite**. Raison :
  la copie est une pièce archivée, non un module ; l'exécuter dans un essai demanderait de la charger hors du paquet avec ses
  dépendances (`transport`, `catalog`), ce qui est un essai neuf à concevoir et à contre-lire, hors des corrections demandées.

## Nœuds de la v1 : où ils en sont
- **N-dev-1 (corpus des jetons gardés) : fermé par `lanceur_seconde_passe_v2`.** Les cibles viennent explicitement de
  `corpus_pagine_v1.cibles_corpus` (ligne 231), le module est dans `MODULES` (lignes 82 à 86) ; le point de branchement des
  réglages a disparu. `montage_v2.cibles_du_corpus` existe encore (le module n'est pas réécrit) et n'est plus appelé par le lanceur.
- **N-dev-7 (dernier crochet indéterminable) : posé à Lazar le 2026-11-21 vers 18:15Z, défaut (a) à 48 heures.** Sans mot de Lazar,
  le code suit l'option (a) : le choix du code est gardé (phrase non écrite, note écrite). **Aucune ligne n'a changé.** Lignes qui en
  dépendent, si Lazar tranche autrement : `phrases_v2.dernier_crochet` (lignes 139 à 147), `phrases_v2.phrases_permises` (lignes
  201 et 202), `phrases_v2.NOTE_DERNIER_CROCHET` (ligne 86). `phrases_v2` ne se réécrivant pas, une autre issue irait dans une
  version suivante de `phrases_v3` (qui reprendrait `phrases_permises`).
- **N-dev-8 (forme de la fiche du code) : la fiche neuve change.** Pour `lanceur_seconde_passe_v2`, la fiche citée par
  `CODE-LENTILLES-BBIS-V2` doit porter, en plus de ce que la v1 dit : les empreintes de `corpus_pagine_v1.py`,
  `cache_tokeniseur_v2.py`, `nos_lentilles_v2.py`, `phrases_v3.py` et `lanceur_seconde_passe_v2.py` (27 modules en tout ; celle de
  `lanceur_seconde_passe_v1.py` n'est plus exigée), et `code_de_lecture_different_de_la_premiere_passe` égal à
  `["statistiques_v4", "lanceur_seconde_passe_v2"]`. Sans cela rien ne part.
- **N-dev-9 (instant où se lit l'état de la première passe) : posé à Lazar le 2026-11-21 vers 18:15Z, défaut (a) à 48 heures.** Sans
  mot de Lazar, le code suit l'option (a) : **le sens sévère est gardé** (`_premiere_passe_en_vigueur`, lignes 990 à 998 de
  `lanceur_seconde_passe_v2`, identique à celle de la v1), **et la phrase de tête est corrigée** (`phrases_v3`, lignes 75 à 97 :
  les deux notes et `phrases_de_la_reproduction`). Lignes qui en dépendent, si Lazar tranche autrement : ces deux blocs, et
  l'appel de la ligne 1040 du lanceur.
- N-dev-2, N-dev-3, N-dev-4, N-dev-5, N-dev-10 : tenus par la contre-lecture, inchangés. N-dev-3 est précisé par N-dev-14 ci-dessous.

## Nœuds neufs (choix que les corrections ont obligé à faire ; datés ; à contre-lire)
- **N-dev-11 (2026-11-21) — place de la ligne de la seconde course pour une seule lentille au premier palier (N2).** Le texte dit
  « recopiée à côté de celle de V » et donne l'ordre pour nos deux lentilles (ligne de V, ligne de la seconde course, réserves). La
  phrase de la forme « une seule lentille » est une citation gelée d'un seul tenant (« Verdict d'ensemble […] : [ligne]. Ce verdict
  d'ensemble […] la décrivent. ») : le code ne la coupe pas et écrit la ligne de la seconde course **après elle, avant les
  réserves**. Autre lecture possible : juste après la ligne de V, au milieu de la citation.
- **N-dev-12 (2026-11-21) — ce que « lecture de la seconde course scellée » veut dire pour le code (N2 bis).** La contre-lecture
  propose d'exiger la ligne de registre « comme le fait `_ligne_de_la_seconde_course` » : le lanceur donne donc aux phrases la
  ligne que cette fonction rend, et elle seule. Elle exige trois choses : la ligne `LECTURE-SECONDE-COURSE-NOS-LENTILLES-BBIS`
  inscrite, la ligne d'ensemble portée par la fiche, et **une seconde course menée en entier** (variante « course rejouée »). Une
  seconde course incomplète dont la lecture serait pourtant inscrite ne voit donc pas sa ligne recopiée au premier palier (sens
  sévère : rien n'est écrit).
- **N-dev-13 (2026-11-21) — mots des deux notes de tête de la reproduction (N4).** Le texte ne donne aucune phrase gelée pour une
  passe en cours au montage et achevée depuis (« et c'est écrit »). Le code écrit une **note du code, dite telle** :
  `phrases_v3.NOTE_ACHEVEE_DEPUIS_LE_MONTAGE`. Pour le cas du sens sévère de N-dev-9 (passe jamais lancée au montage et lancée
  depuis, achevée ou non), la phrase gelée « […] première passe lancée et non achevée […] avant le nœud de la v1 » serait elle
  aussi inexacte (la passe n'était pas lancée au montage) : le code écrit `phrases_v3.NOTE_LANCEE_DEPUIS_LE_MONTAGE`. La phrase
  gelée reste écrite, mot pour mot, quand la passe était lancée et non achevée au montage et l'est encore au calcul. Aucun mot gelé
  n'est changé ; dans les trois cas, aucune phrase de la lentille publique ni de la lentille des logits n'est écrite.
- **N-dev-14 (2026-11-21) — pièce du nœud N12 sans ligne, ou à plusieurs lignes « Lentille nommée » (N5).** Plus d'une ligne de la
  forme dans une pièce : arrêt, forme mal comprise (`nos_lentilles_v2`). **Aucune** ligne : la pièce ne nomme personne et la
  lentille reste « non lue », comme en v1 (N-dev-3, tenu par la contre-lecture) ; ce n'est pas un arrêt. La pièce n'est jugée que
  quand la condition de lecture l'a consultée (une de nos lentilles au deuxième palier en ajustement seul ou en seconde course
  incomplète), et seulement pour les lignes du registre que `nos_lentilles_v1` retient (postérieures à tout avertissement).
- **N-dev-15 (2026-11-21) — recouvrement des moitiés non calculable (N3).** Le texte ne fixe pas ce cas. Le crochet de la phrase
  gelée reste rempli par « non calculable » (aucun mot gelé ne change, et la phrase n'est ni retirée ni réécrite) ; une note du
  code, dans la même entrée des phrases (`note`), dit que le texte ne fixe pas ce cas et donne le motif. Raison de ne pas faire
  plus : retirer la phrase ou en changer un mot serait un écart au texte scellé.

## Précisions de lecture ajoutées (aucune n'ajoute une règle de décision ; à contre-lire)
- **Essai du tokeniseur en ligne et sans clé** : fonction recopiée de `lanceur_v9` dans `lanceur_seconde_passe_v2` (lignes 360 à
  380), non importée, pour que la seconde passe n'exécute pas le lanceur de la première passe v9 (qui n'est pas dans sa liste de
  modules) ; le script joué est celui de `lanceur_v7`, égal à celui de `lanceur_v9` (essai). Ajout : à l'échec, le cache est relu
  par `cache_tokeniseur_v2.exiger_cache` ; l'arrêt porte le message de cette relecture (« cause relue dans le cache : « … » »),
  ou dit que le cache relu est inchangé (la cause est alors dans le journal). Le message ne porte ni le journal ni la clé.
- **Liste des gardes du rapport du montage** : celle de la v1, plus « fichiers absents du dépôt du modèle vérifiés sur son arbre et
  marqués absents dans le cache » et « tokeniseur lu par le voisin, en ligne et sans clé » (mêmes mots que `lanceur_v9`).
- **`MODULES_DIFFERENTS`** reste `statistiques_v4` et le lanceur : `nos_lentilles_v2` et `phrases_v3` n'ont pas d'homologue dans la
  première passe (ils complètent des modules propres à la seconde).
- **`nos_lentilles_v2` et `phrases_v3` sont des compléments, non des copies** : ils importent `nos_lentilles_v1` et `phrases_v2`,
  qui restent appelés pour tout le reste. Les essais des modules v1 et v2 (`…nos_lentilles_v1.py`, `…phrases_reproduction_v1.py`)
  restent valables tels quels.
- **Jouets** : `tests/lentilles_sondes_bbis_seconde_passe_jouets_v3.py` s'appuie sur le monde des jouets de la version 9 de la
  première passe (réseau simulé qui sert un arbre par pages ; arbre du dépôt du modèle qui liste les petits fichiers posés) ; la
  première passe « faite » y est jouée par le lanceur de ces jouets (celui de la première passe v9).
- **Reproduction du refus du dépôt à porte (code 401)** : le catalogue des jouets ne charge aucun tokeniseur réel ; les essais
  qui reproduisent le refus remplacent le script de l'essai par le chargement que la copie versée du catalogue du voisin fait
  (`AutoTokenizer.from_pretrained` du modèle nommé par l'environnement ; égalité éprouvée), sur un tokeniseur jouet de cinq
  jetons, contre une porte simulée qui écoute sur 127.0.0.1. Aucune requête ne sort de la machine.
