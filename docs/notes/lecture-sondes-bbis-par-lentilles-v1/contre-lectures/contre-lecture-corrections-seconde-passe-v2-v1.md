# Contre-lecture neuve des corrections de la seconde passe (lanceur de la seconde passe v2) — v1

Je suis un contre-lecteur neuf. Je n'ai écrit ni le code, ni ses notes, ni la contre-lecture v1. Date : 2026-11-21 (UTC).
Mandat : `docs/notes/lecture-sondes-bbis-par-lentilles-v1/mandats/mandat-contre-lecteur-corrections-seconde-passe-v2-v1.md`
(`f4ca5319f6a70b1761c19a88fa79f186d5f6ae7c6aab0010fce046d52d2bab66`, vérifié). Code jugé : commit `0690d639a`, branche
`claude/brave-galileo-jhp684`, extraite au commit `92baebf7d`. Pièce jugée : classe B (instrument).

## Verdict
**Conforme.** Les deux corrections bloquantes (B1 : lecture paginée du corpus ; B2 : cache du tokeniseur) et les six non
bloquantes sont faites, sont justes et sont éprouvées. Rien d'autre ne change par rapport à ce que le texte de lecture v2 scellé
exige. Le lanceur de la seconde passe v2 peut être donné à un opérateur une fois la fiche `CODE-LENTILLES-BBIS-V2` écrite selon
N-dev-8, et avec les deux réserves de calendrier et de forme ci-dessous, dont aucune ne bloque.

## Ce que j'ai lu, et ce que j'ai vérifié
- **Empreintes scellées, toutes en ordre** : le mandat ; `CLAUDE.md` ; le mandat du développeur v2 (`a2132568…`) ; la
  contre-lecture v1 (`0c90e0f6…`), lue en entier ; `corrections-seconde-passe-v2-v1.md` (`b35d7459…`) ;
  `noeuds-et-precisions-seconde-passe-v2.md` (`28bb60df…`) ; `empreintes-code-seconde-passe-v2.txt` (`9e4556fb…`) ;
  `sortie-essais-seconde-passe-v2.txt` (`939a6674…`) ; les deux outils (`a8747dbf…`, `a5df3efa…`) ; les pièces v1 (`ecb803cc…`,
  `c8e16b1e…`, `20cd3f7a…`) ; les deux contre-lectures des correctifs (`8ba0f061…`, `1e8c1704…`) ; le texte v2 (`a2bbed7a…`).
- **Code** : les 26 lignes de `empreintes-code-seconde-passe-v2.txt` sont comparées par `sha256sum -c` : toutes en ordre.
  `git diff --name-status ffba6bed8 0690d639a -- src tests` ne montre **que des ajouts**. Le commit du développeur ajoute six
  fichiers. Rien n'a changé sous `src/` ni sous `tests/` depuis `0690d639a`.
- **Lu ligne à ligne** :
  - `diff lanceur_seconde_passe_v1.py lanceur_seconde_passe_v2.py`, en entier ;
  - `diff lanceur_v7 lanceur_v8` et `diff lanceur_v8 lanceur_v9`, en entier ;
  - `cache_tokeniseur_v2.py`, `nos_lentilles_v2.py` et `phrases_v3.py`, en entier ;
  - `phrases_v2` : le verdict d'ensemble, la reproduction et la comparaison entre lentilles ;
  - `nos_lentilles_v1` : les lignes 320 à 360, la règle du nœud N12 (lignes 427 à 443) et les lignes 540 à 560 ;
  - le lanceur v2 : la fonction de montage (lignes 195 à 262), `exiger_fiche_code`, les lignes 980 à 1110 et le rendu des
    phrases (lignes 1160 à 1240) ;
  - les essais des corrections : les en-têtes, et les essais de B1, B2, du point 6 et de la fabrique ;
  - le diff entre les essais du lanceur v1 et leur copie v2, et le diff entre les jouets v2 et v3 ;
  - l'essai des essais, en entier.
- **Texte v2** : j'en ai lu les seules sections que touchent les corrections : lignes 1068 à 1080, 1462 à 1482, 1990 à 2012,
  2068 à 2080, 2212 à 2245 et 2475 à 2530. Je n'ai pas lu la liste « Jamais ouverts » : la recherche par mot de la ligne 1320 en
  a seulement affiché le titre.

## Points du mandat

**1. B1 — tenu.**
- `MODULES` porte `corpus_pagine_v1` et `cache_tokeniseur_v2`, ainsi que `nos_lentilles_v2`, `phrases_v3` et
  `lanceur_seconde_passe_v2`, soit 27 modules.
- `MODULES_DIFFERENTS` vaut `("statistiques_v4", "lanceur_seconde_passe_v2")`.
- J'ai recalculé moi-même la fermeture statique des imports relatifs du lanceur v2, imports placés dans des fonctions compris.
  Elle est **égale** à `MODULES` : rien de plus, rien de moins, et aucun import dynamique.
- Les cibles du corpus viennent de `cp.cibles_corpus(voisin, transport)` (ligne 231). C'est la ligne même de `lanceur_v8`
  (ligne 414). Le point de branchement `Reglages.cibles_corpus` a disparu.
- `exiger_fiche_code` est inchangée, et elle exige l'empreinte de chaque module de `MODULES`.
- `nos_lentilles_v2` et `phrases_v3` restent hors de `MODULES_DIFFERENTS`, ce qui est conforme à l'usage de la v1 tenu par la
  contre-lecture v1. Ces deux modules complètent des modules propres à la seconde passe. Ils ne remplacent aucun module de lecture
  de la première passe (texte, lignes 2484 à 2488).

**2. B2 — tenu.**
- La pose du cache passe par `ct.poser_cache_tokeniseur(...)`. L'essai hors ligne de `lanceur_v7` vient ensuite, puis l'essai en
  ligne et sans clé (`environnement_enfant(..., False, ...)`, un seul enfant en ligne dans le lanceur), puis `ct.exiger_cache`.
  Ce sont, ligne pour ligne, les lignes 436 à 445 de `lanceur_v9`. Les deux champs du rapport sont `cache_du_tokeniseur` et
  `essai_du_tokeniseur_en_ligne_sans_cle`. Les deux gardes ajoutées à la liste portent les mots de la v9.
- La fonction d'essai est **fidèle** à celle de `lanceur_v9` : même appel, même journal. J'ai vérifié deux égalités sur
  l'arbre syntaxique : `lanceur_v7.SCRIPT_TOKENISEUR` est égal à celui de la v9, et `lanceur_v7.essayer_tokeniseur_du_cache`
  est égale à celle de la v9.
- **L'écart est déclaré** dans le texte d'en-tête du lanceur, dans le texte de la fonction et dans la note des nœuds v2
  (« Précisions »). La seconde passe importe `lanceur_v7`, et non `lanceur_v9`, qui n'est pas dans sa liste. C'est sans effet,
  puisque la v9 ne diffère de la v7 qu'au montage et à la pagination.
- À l'échec de l'essai, `exiger_cache` relit le cache. Si la relecture trouve une cause, l'arrêt écrit « cause relue dans le
  cache : « … » ». Sinon, il écrit `CAUSE_CACHE_INCHANGE`. Le message ne porte que des mots du code : ni le journal, ni la clé.
- Le calcul (ligne 291) appelle toujours `mo.calculer_jetons_gardes` avec le même `hf_home`, celui qui a été posé et relu. La v9
  fait de même.

**3. Les six non bloquantes — tenues.**
- N1 : faite dans une note neuve. L'amélioration facultative n'est pas faite, avec une raison acceptable.
- N2 : faite (`phrases_v3`). La place après la citation gelée est le nœud N-dev-11. La phrase n'est pas coupée : c'est
  acceptable.
- N2 bis : faite. La ligne n'est recopiée que si `_ligne_de_la_seconde_course` la rend. N-dev-12 ajoute la condition « course
  menée en entier ». Elle concorde avec le texte (ligne 1073 : une seconde course incomplète est « arrêtée […] avant la fin de
  ses mesures ») et avec `MOTIF_SANS_LECTURE_SECONDE_COURSE`.
- N3 : laissée dans la phrase, avec une note, et la raison est bonne : aucun mot gelé ne change. La note n'est écrite que pour les
  deux libellés dont la phrase cite les moitiés (`phrases_v2`, lignes 457 à 467).
- N4 : faite selon l'option (a). Le sens sévère est gardé : `_premiere_passe_en_vigueur` est égale à celle de la v1, essai à
  l'appui. Les deux notes du code sont exactes au regard des lignes 1990 à 2012 du texte. La phrase gelée reste écrite dans le
  seul cas qu'elle décrit vraiment.
- N5 : faite (`nos_lentilles_v2`). Le filtre est le même que celui de `lentilles_nommees_par_le_noeud`. Sans aucune ligne, la
  lentille est non lue, sans arrêt, comme le veut N-dev-3, tenu.

**4. Les deux nœuds posés à Lazar — tenu.** Le code suit l'option (a) de chacun, comme la contre-lecture v1 les décrit. J'ai
vérifié que les lignes nommées sont exactes :
- N-dev-7 : `phrases_v2`, lignes 86, 139 à 147, 201 et 202 ;
- N-dev-9 : lanceur v2, lignes 990 à 998 et 1040 ; `phrases_v3`, lignes 75 à 97.

**5. L'essai qui dépendait de l'ordre — tenu.**
- La copie neuve retire aussi l'attribut du paquet (`delattr`).
- Je l'ai reproduit dans un ordre contraire, en chargeant d'abord les essais du correctif de la pagination, puis les deux fichiers
  du lanceur, avec `-k` limité à cet essai. Résultat : **1 en échec, 1 réussi**. L'ancien fichier tombe, la copie neuve passe.
- L'échec qui reste dans l'ancien fichier n'a aucun lien avec le code. Il vient de l'isolement des essais : `from . import x`
  rend l'attribut s'il existe déjà, ce que l'essai du point 6 éprouve. Il porte sur une garde de `montage_v2` que le lanceur v2
  n'appelle plus.

**6. R5 — tenu.**
- Chaque garde neuve a un cas sain et un artefact. Les artefacts prennent souvent l'ancien code, joué sur le même monde.
- Le refus 401 est reproduit par le vrai chargement (`AutoTokenizer.from_pretrained`), dans un enfant en ligne et sans clé,
  contre une porte simulée qui écoute sur 127.0.0.1 : par l'ancien lanceur, par la pose à l'ancienne dans le lanceur v2, et quand
  la branche du dépôt a bougé.
- L'arbre paginé à deux pages est joué de bout en bout. L'ancien lanceur s'y arrête.
- L'essai des essais (36 défaites) couvre B1, B2, N2, N2 bis, N3, N4 et N5, y compris le retrait de chaque module neuf de la
  liste, les deux sens des gardes et la relecture avalée. Je ne l'ai pas rejoué ; je me fie à sa sortie scellée.

**7. Rien d'autre n'a changé — tenu.**
- Aucun module existant n'est réécrit : il n'y a que des ajouts (R12).
- L'essai des onze lignes est vérifié. Le diff que j'ai lu le confirme : seules onze lignes de la v1 sont retirées. Les fonctions
  de calcul et le canal des messages d'arrêt sont égaux à la source près. `statistiques_v4` est le même module.
- Aucune clé n'est exposée : la seule valeur de forme `hf_…` est la fausse clé des jouets. Les essais vérifient que la fausse clé
  n'apparaît dans aucun fichier de sortie ni dans aucun message.

**8. Autre écart bloquant — aucun.**

## Essais rejoués (comptes seulement)
- `PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src python -m pytest -q -p no:cacheprovider` sur les deux fichiers du mandat, avec
  l'environnement `.venv` du dépôt : **88 réussis, 0 en échec** (151 s). Les essais recueillis sont 54 dans le fichier des
  corrections et 34 dans la copie du lanceur.
- Reproduction de l'ordre (point 5) : 1 en échec (l'ancien fichier), 1 réussi (la copie neuve).

## Corrections demandées (aucune bloquante)
- **Non bloquante a** : `corrections-seconde-passe-v2-v1.md`, ligne 22, annonce « 55 essais ». J'en recueille 54. À dire dans la
  passation ou dans une note neuve, sans réécrire la pièce.
- **Non bloquante b** : la même pièce (ligne 72) renvoie aux « comptes des deux façons », mais la sortie scellée ne porte que le
  paquet entier (1 en échec, 3 226 réussis) et l'essai joué seul. Elle ne porte ni le paquet avec l'essai écarté, ni l'ancien
  fichier joué à part. Recommandation : que l'opérateur joue le paquet avec l'option `--deselect` de cet essai, ou l'ancien
  fichier dans un processus à part, et en consigne le compte.
- **Remarque, sans correction exigée** : dans l'essai des essais, un dépassement du délai compte comme une défaite « vue », et
  rien ne vérifie que l'échec vient de l'essai attendu. La copie saine passe, ce qui écarte une erreur d'import commune.

## Réserves pour donner le lanceur à un opérateur
- La fiche `CODE-LENTILLES-BBIS-V2` doit citer `0690d639a` (ou un commit sans changement sous `src/`), les 27 empreintes et
  `["statistiques_v4", "lanceur_seconde_passe_v2"]` (N-dev-8). Sans elle, rien ne part, et c'est voulu.
- Les nœuds N-dev-7 et N-dev-9 ne prennent leur défaut que le 2026-11-23 vers 18:15Z. Une course lancée avant cette date suit
  l'option (a). Si Lazar tranche autrement, il faudra une version suivante. N-dev-9 ne joue que si l'état de la première passe
  change entre le montage et le calcul.

## Cloisonnement
- Je n'ai ouvert ni `diag/`, ni `runs/`, ni `docs/verdicts/`. Aucune branche exclue n'a été récupérée. Je n'ai lu aucun fichier
  « consigne-privee » ou « conception-ii-b », aucune sortie, aucun score, aucune table, aucun verdict, aucun `arret.json`.
- Aucune requête vers Hugging Face, aucun téléchargement, aucune clé lue.
- Aucun intitulé interdit n'a été vu. Le dossier de brouillons partagé de la session contient des fichiers d'autres agents : je
  n'en ai lu aucun, je n'ai lu que ma propre sortie d'essais.
- **Un refus d'outil, déclaré** : l'outil a refusé une attente par `sleep`. Je ne l'ai pas rejouée ; j'ai attendu la fin des
  essais par une boucle en arrière-plan.
- Je n'ai rien committé.
