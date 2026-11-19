# Vérification des corrections du code de l'instrument et de l'analyse du bras A, version 7 — v1

**Verdict : engageable après corrections.** Aucun défaut bloquant. Les trois défauts à corriger de la version 6 sont tenus.

- Sur un faux dépôt, la garde statique appelée avec ses valeurs par défaut n'ouvre ni ne liste aucun chemin cloisonné. Un crochet d'audit écrit à part le vérifie.
- Des huit mineurs, cinq sont tenus, deux le sont en partie (M-1 et M-2), et M-6 l'est dans sa limite écrite.

Il reste deux défauts à corriger :
- **C-1 : le registre lu.** Le code ne peut lire, par construction, que l'état du registre au moment où la configuration est scellée. Cet état précède l'inscription de la configuration au registre, que le texte exige. Le texte et le code sont à accorder.
- **C-2 : une panne pendant l'écriture d'un acte ou d'un arrêt.** Si elle survient entre l'écriture et le scellement, tout le dossier des arrêts devient illisible. Et une panne pendant la lecture d'une livraison refaite la rend illisible à jamais, sans issue écrite.

Les 296 essais passent.

- **Vérificateur** : Claude Opus 5.5 (`claude-opus-5-5`), le même qui a contre-lu les versions 5 et 6. Il n'a écrit ni code, ni essai, ni texte du dossier.
- **Code** : commit `3d44b094`. La tête est passée à `d3dc0e29` sans changement sous `src/` ni sous `tests/`. Les huit modules `*_bras_a_v7.py` et les sept fichiers d'essais `tests/*_bras_a_v7.py` répondent à leurs compagnons, et leurs empreintes sont celles de la note du code. Exemples : analyse `38b0191f…`, garde statique `b13c99d4…`, graines `2930e02e…`, configuration `d49d32f6…`.
- **Textes** :
  - brouillon 25 (`ab5fc58e…`) : 6.9, lignes 715 à 723 et 969 à 974, par recherches ciblées ;
  - sa note (`3732b6b4…`), parties 1 à 6 ;
  - la note du code v7 (`d4546819…`) et son relevé (`1acf5034…`), en entier.
- **Essais** : la commande de la note donne **296 passés** (46 s) :

  ```
  PYTHONPATH=src .venv/bin/python -m pytest -q -p no:cacheprovider tests/test_analyse_bras_a_v7.py tests/test_verdicts_bras_a_v7.py tests/test_graines_bras_a_v7.py tests/test_permutation_etiquettes_bras_a_v7.py tests/test_mesures_bras_a_v7.py tests/test_cloisonnement_bras_a_v7.py tests/test_reponses_lecteurs_v5.py tests/test_epreuves_couverture_bras_a_v3.py
  ```

  Cette commande contient un essai du rédacteur, `test_la_garde_passee_sur_src_et_scripts_du_depot_avec_ses_valeurs_par_defaut`, qui fait passer la garde sur le vrai `src/` et le vrai `scripts/`. Il tourne sous un crochet d'audit qui lève une exception **avant** toute ouverture ou tout listage d'un chemin cloisonné. L'essai passe, donc aucun n'a été tenté. **Mes propres essais de la garde, eux, n'ont tourné que sur un faux dépôt.**
- **Essais d'attaque** (bloc-notes, données synthétiques, registre fabriqué) : `/tmp/claude-0/-home-user-controle-ia-travail/b7727ccc-db8b-5b89-bce1-17602831b69d/scratchpad/contre-lecture-code-v7/`. Chacun a sa sortie `….sortie.txt` :
  - `attaques_v7.py` : règle, livraison refaite, registre, pannes, constats, issues ;
  - `audit_cloisonnement_v7.py` : faux dépôt, crochet d'audit, liens symboliques et physiques ;
  - `attaques_cloisonnement_v7.py` : les 24 modules plantés de la v6, plus 2 neufs ;
  - `fuzz_livraison_v7.py` : 600 livraisons altérées, graine fixe ;
  - `doublons_v7.sortie.txt`.
- **Heure** : 2026-11-19T17:52Z.

---

## 1. Défauts bloquants

Aucun.

## 2. Défauts à corriger

### C-1. Le registre lu est l'état figé au scellement de la configuration, qui précède sa propre inscription : le texte et le code ne disent pas la même chose
- **Où** :
  - `graines_bras_a_v7.py`, `lire_le_registre_des_accords` ;
  - `configuration_bras_a_v7.py`, `pieces_attendues.sha256_du_registre_des_accords` ;
  - brouillon 25 : conventions (la configuration est « inscrite au registre par son empreinte avant la réception de la sortie de la lecture commune ») et 6.9 (« le registre lu est celui de la branche principale »).
- **Constat** :
  - La configuration porte l'empreinte du registre. L'inscrire ensuite au registre change le registre. Le registre que le code accepte est donc, par construction, l'état d'avant cette inscription, et non le registre de la branche principale au moment de la lecture.
  - Une révocation de la ligne de GO inscrite entre le scellement de la configuration et la lecture n'est pas vue.
  - L'arbre de travail doit porter, octet pour octet, l'état figé de la branche principale. Or la branche de relance porte aujourd'hui un registre où GO-2026-11-19-70 manque.
- **Ce qui tient** :
  - aucun repli : avec un registre attendu `null`, une reprise s'arrête ;
  - un registre d'une autre empreinte s'arrête en disant les deux empreintes (essais) ;
  - aucun réseau.
- **Risques** :
  - arrêt à tort chaque fois qu'une ligne entre au registre entre le scellement et la lecture, ce qui arrive souvent ;
  - la provenance de l'empreinte attendue tient à la configuration, que la relance écrit elle-même.
- **Ce qui le réglerait** (texte d'abord) :
  - écrire au texte que « le registre lu est le registre de la branche principale tel qu'il était au scellement de la configuration » ;
  - dire où s'inscrit la configuration sans changer l'empreinte attendue. Par exemple, une ligne qui cite la configuration n'est pas exigée dans l'état figé, et c'est la session qui lance qui la vérifie ;
  - exiger que la session qui lance constate, juste avant la lecture, qu'aucune révocation n'est entrée depuis, et le consigne au manifeste.

  Le code n'a pas à changer, sauf son message, qui doit dire « état figé ».

### C-2. Une panne entre l'écriture et le scellement d'un acte de reprise ou d'un fichier d'arrêt bloque tout le dossier ; une panne pendant la lecture d'une livraison refaite la perd sans issue écrite
- **Où** : `analyse_bras_a_v7.py`, `_exiger_lecture_permise` (`write_text`, puis `sceller`) et `_consigner_l_arret` (même suite d'opérations).
- **Essais d'attaque** (`attaques_v7.py`) :
  - une panne simulée entre `write_text` et `sceller` de l'acte laisse un acte sans compagnon. Ensuite **toute** lecture du dossier s'arrête sur `verifier` : `compte_des_livraisons`, `regle_de_discretion`, `issues`. On ne sort de là que par une intervention à la main dans le dossier, qui est elle-même une retouche ;
  - une panne pendant la lecture d'une livraison refaite, après l'acte : la relecture est refusée, sur la même ligne comme sur une ligne neuve (« livraison refaite déjà ouverte »). Ce refus est une garde ordinaire, non l'événement nommé : aucune issue n'est écrite pour ce cas.
- **Ce qui le réglerait** :
  - **code** : écrire l'acte et le fichier d'arrêt sous un nom provisoire, les sceller, puis les renommer, pour qu'aucun fichier sans compagnon ne porte le nom attendu ;
  - **texte** : la précision de la question 4 (partie 7).

## 3. Défauts mineurs

- **M-1. Constats de l'étape (m) : les deux réglages de la table A manquent** (relevé B.18, confirmé). Un fichier de constats écrit à la main avec `journal = ["A7"]` dont la révision a été refusée est accepté : relu sans ses réglages, ce journal ne donne aucune ligne, alors qu'avec « révision refusée » il donne A7. L'écriture, elle, le refuse. Les constats sous A15 sont maintenant refusés : la correction de la version 6 tient sur ce point. Correction : deux champs de plus dans les constats.
- **M-2. `issues` lit le dossier et la pièce, mais c'est l'appelant qui les donne.** Avec un dossier neuf et vide, `piece_scellee=None` et le renvoi de la base dit non vérifié, `issues` rend « non lue », sans voir l'arrêt consigné ailleurs (essai). C'est bien mieux que la version 6, mais le lien avec le dossier réel n'est pas scellé. Correction : inscrire le chemin du dossier des arrêts dans la configuration scellée, et l'exiger.
- **M-3. Demi-pas de la grille comparé en nombres à virgule.** Pour la valeur p basse avec 2 000 permutations calculées, un écart exactement égal au demi-pas (0,5 contre 1 000/2 001) est **accepté**, car le calcul donne 0,00024987506246876**29** < 0,00024987506246876**56**. Le texte dit « écart ≥ demi-pas : refus ». C'est sans portée pratique. Correction : comparer en fractions exactes.
- **M-4. Motifs des dossiers cloisonnés sensibles à la casse.** `t07*`, `bases` et `sondes` sont jugés avec la casse, alors que la marque de T0.8 est jugée sans. Un dossier `T07/` ou `Bases/` est lu (faux dépôt). Les vrais dossiers sont en minuscules : c'est sans effet aujourd'hui. Correction : juger sans égard à la casse, dans le doute.
- **M-5. Un champ en double à l'intérieur d'un champ non contrôlé** (`effectifs`, `plis`) arrête la lecture sous « un champ en double » de la liste qui le contient (essai). Refuser est prudent : la pièce est ambiguë. Mais la nature dite est inexacte, et ce cas n'est pas nommé dans la liste fermée. Voir la partie 6, quatrième écart.
- **M-6. « Module corrigé » : l'empreinte du module est déclarée, non confrontée à la livraison.** Elle n'est comparée qu'à la ligne de GO d'une reprise. Pour une première livraison, rien ne lie la livraison au module que la configuration nomme, et `piece_source` n'est pas lu. La limite est écrite. Le texte ou la session principale devra dire comment `piece_source` désigne le module.

Restes déclarés, sans défaut :
- un lien physique vers un fichier cloisonné est lu ; git ne conserve pas les liens physiques ;
- `iterdir` sans extension écrite ;
- un nom lu dans la pièce ;
- un programme rangé sous un chemin cloisonné n'est pas regardé (limite (f)).

## 4. Corrections de la version 6 → tenue ou non

| défaut v6 | jugement | preuve (essai d'attaque rejoué contre v7) |
|---|---|---|
| C-1 causes hors texte | **tenu** | le brouillon 25 inscrit les cinq contrôles ; la valeur p à un demi-pas (0,3 sans aire au moins égale : refusée ; quatre décimales : acceptées) ; `dose` et `condition` du fichier des rangs lus dans la configuration ; étendues de `episode` et `pas` retirées ; lectures en liste dans un autre ordre acceptées. Sur 600 livraisons altérées : 433 arrêts, **tous l'événement nommé** ; ce qui passe ne touche que des champs sans règle ou des valeurs permises. Reste M-5 |
| C-2 « une seule fois » | **tenu** | GO-02 ouvre une livraison refaite. La même ligne, pour une deuxième : refusée. GO-01, qui cite un fichier d'arrêt déjà repris : refusée. Une ligne à quatre empreintes : refusée. Le compte des livraisons est juste. Reste C-2 ci-dessus (panne) |
| C-3 garde statique | **tenu** | faux dépôt, valeurs par défaut, crochet d'audit écrit à part : aucun chemin cloisonné ouvert ni listé ; onze élagués, chacun par son nom ; un départ cloisonné ou par `..` est refusé ; les liens symboliques ne sont pas suivis (violation) ; les noms voisins sont lus et refusés. Reste M-4 |
| M-1 constats | **tenu en partie** | A15 refusé ; journal relu ; trois empreintes comparées ; trou B.18 → M-1 |
| M-2 `issues` | **tenu en partie** | l'arrêt est lu dans le dossier, la table C dans le fichier (m) ; le dossier vient encore de l'appelant → M-2 |
| M-3 mot de refus | **tenu** | « après la livraison refusée » : acceptée ; « refusé : » : refusée |
| M-4 fichier d'arrêt, trace | **tenu** | cinq champs ; l'événement est refait de son constat : ni `__cause__` ni `__context__`, et aucune variable des cadres du module ne porte l'aire fautive (seules mes propres variables d'appel la portent) |
| M-5 reprise dans le résultat | **tenu** | une reprise inventée et un état retouché sont refusés ; la garde relit l'acte scellé |
| M-6 module corrigé | **tenu dans sa limite** | empreinte toujours exigée ; → M-6 |
| M-7 contenus tels quels | **écart accepté** | le texte dit « rapportés tels qu'ils sont rendus » ; un texte dans `effectifs` passe (essai). Au texte de dire que ces champs ne sont pas des sorties de moniteur |
| M-8 garde, restes | **tenu** | `join` d'une compréhension, chaîne faite de variables, `_generateur` remplacé, variable réaffectée : refusés |

## 5. Le registre lu sous empreinte attendue (question 2)

**Sûr contre la mégarde, sans repli.**
- Le code ne lit jamais un registre dont l'empreinte n'est pas celle que la configuration scellée inscrit.
- Une empreinte attendue absente, mal formée ou `null` (pour une reprise) arrête la lecture, en le disant.
- Le registre n'est lu qu'une fois, en octets. L'empreinte et le contenu viennent des mêmes octets.

**Ce que ce mécanisme ne garantit pas** :
- (a) qu'il s'agisse du registre de la branche principale *actuel* : c'est son état au scellement (C-1) ;
- (b) qu'aucune révocation ne soit entrée depuis ;
- (c) la provenance de l'empreinte attendue, que la relance écrit elle-même dans sa configuration.

**Arrêt à tort** : probable, chaque fois que le registre de l'arbre de travail n'est pas exactement cet état figé. C'est un arrêt dit, non un passage. Il faut préciser le texte, comme en C-1.

## 6. Les écarts du code au texte (question 3)

| écart | changer | pourquoi |
|---|---|---|
| configuration en trois parties (`pieces_attendues`) | **le texte** | les deux empreintes ne se devinent pas et ne sont pas des chaînes du module ; le texte doit nommer la troisième partie |
| ligne de GO : 6.9 sans « un autre module », 8.4 avec | **le texte** (aligner 6.9 sur 8.4) | le code suit la plus stricte. J'ajoute : la troisième empreinte, celle du rapport de contre-lecture, est exigée mais **non vérifiée**. Le mieux serait de l'inscrire aussi dans `pieces_attendues` pour la confronter ; sinon, le texte doit dire « citée, non vérifiée » |
| tolérance tirée du texte, non de la configuration | **rien** | 6.9 fixe la grille (2 001 ; permutations calculées), et c'est la consigne qui avait tort. Au texte, préciser seulement « comparée exactement » (M-3) |
| trois défauts sans nature | **le texte**, puis le code pour le troisième | (i) dix champs dans le désordre : ajouter la nature « champ hors de son ordre » au lieu de « pièce illisible ». (ii) champ de plus et de moins ensemble : dire laquelle prime ; le code dit « de moins ». (iii) champ en double à l'intérieur d'un champ non contrôlé : dire que c'est une « pièce illisible », cause d'arrêt écrite, et que le code le nomme ainsi (M-5). Aucun ne change une règle de jugement, mais (iii) est une cause d'arrêt que la liste fermée doit porter |

## 7. Les deux défauts du texte qui toucheraient une règle (question 4)

- **A.1, panne entre l'acte et la fin de la lecture** : c'est **une précision**, à écrire par le rédacteur du texte, et à signaler à Lazar pour information seulement.
  - La règle de discrétion est déterministe. Rejouer **la même livraison** (même empreinte), sous **la même configuration** (même empreinte) et **le même acte**, alors qu'aucun résultat n'a été rendu, ne crée aucune occasion de retouche. C'est l'esprit de « une seule fois » : une livraison, non une exécution.
  - Si le texte retient plutôt « la discrétion reste non lue », il doit le dire comme une issue. Aujourd'hui, le refus de relire est une garde ordinaire sans issue : le cas reste orphelin.
  - Dans les deux cas, le code doit d'abord rendre l'écriture des actes atomique (C-2).
- **A.2, révocation d'une ligne de GO après la lecture** : c'est **une question pour Lazar**, sans urgence, à poser avec la fiche 12.
  - Elle dit ce que vaut le retrait d'un accord déjà dépensé. C'est la règle du registre en général, non une forme du bras A.
  - Proposition de défaut à lui soumettre : « l'acte scellé fait foi ; une révocation postérieure est rapportée et ne retire pas la lecture ».
  - Le cas voisin de C-1, une révocation entrée *avant* la lecture mais après le scellement de la configuration, n'est pas une question pour Lazar : c'est une précision du texte (C-1).

## 8. Ce que je n'ai pas regardé
- Les parties inchangées depuis la version 6, selon le rédacteur : statistique, tables A, B et C hors `issues`, aire conditionnelle, réponses des lecteurs.
- La totalité de `verdicts_bras_a_v7.py` hors de `issues` ; `arrets_bras_a_v7.py` et `permutation_etiquettes_bras_a_v7.py`, lus seulement à travers leurs essais et le constat.
- Le brouillon 25 hors des lignes citées ; la vérification du brouillon 25 (commit `d3dc0e29`), non lue.

## 9. Fichiers ouverts
- `CLAUDE.md`.
- Dans `docs/notes/relance-organismes-discrets-v1/` : `code-v7-bras-a-note-v1.md` et `defauts-du-texte-trouves-en-codant-v7.md`, en entier ; `preenregistrement-v2-brouillon25-note-v1.md`, parties 1 à 6.
- `prereg/T0.7-organismes-discrets-v-a-v2-brouillon25.md` : recherches ciblées (« liste des refus », « en double », « pièce illisible »).
- Code v7 :
  - différences v6 → v7 de `cloisonnement`, `graines` et `configuration` ;
  - `analyse_bras_a_v7.py`, lignes 762 à 870 et 1128 à 1410, et l'écart (i) ;
  - `verdicts_bras_a_v7.py`, `issues`, début.
- Essais : `tests/aide_bras_a_v7.py` (noms, `regle`, `registre`, `ligne_de_reprise`, `fichier_d_arret`) ; `tests/test_cloisonnement_bras_a_v7.py`, lignes 210 à 410.
- **Non ouverts** :
  - aucun interne de moniteur, aucun module habilité, rien sous `bases/`, `sondes/` ou `t07*/`, rien de T0.8 ;
  - aucune notice ni contre-lecture du côté habilité, aucune fiche de l'organisme d'idéation, aucune réponse de lecteur, aucune clé ;
  - ni `registres/go.md` : mes essais v7 lisent un registre fabriqué. Le constat que GO-2026-11-19-70 manque au registre de la branche vient de mon essai sur la version 6 (`attaques_graines_v6.sortie.txt`) ;
  - aucun appel réseau ni de modèle, aucun sous-agent, rien d'installé, rien committé.
