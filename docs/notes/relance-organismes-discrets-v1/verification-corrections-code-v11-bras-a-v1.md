# Vérification des corrections du code de l'instrument et de l'analyse du bras A, version 11 — v1

**Verdict : engageable après corrections.** Aucun défaut bloquant.

- **Ce qui tient** :
  - le défaut C-1 de la version 10, sous ses deux formes : sous la même configuration, la pièce B (« repère ») est refusée après la pièce A (« ne repère pas ») ; une configuration de rang 2 sans registre figé est refusée ;
  - la phrase d'accord de l'écart à R9, jugée sur la cellule d'objet exacte, quel que soit le gras ;
  - la révocation, qui n'est jamais un accord ;
  - la porte de l'écart à R9 contre une ligne entrée depuis l'état figé ;
  - la garde « en attente », qui fixe maintenant la pièce ;
  - la garde statique : rien de cloisonné n'est ouvert.
- **Une voie neuve pour choisir entre deux résultats** (C-1 ci-dessous). Après un arrêt à l'étape (n), une livraison refaite rejoue l'étape (m) et scelle une **seconde table C dans la course**, à côté de la première, que l'issue retenue (c) garde « inchangée, opposable ». Dans mon essai, la première dit « ne repère pas » et la seconde « repère ».
- **Restent** :
  - le contrôle fait avant le premier départ, qui sert encore au rejeu (M-1) ;
  - la garde du registre au constat, qu'une ligne de reprise sans rapport suffit à lever (M-2) ;
  - une configuration abandonnée, qui bloque la suivante (M-3).
- **Les cinq défauts de la partie A du relevé**, et la question neuve du périmètre d'une reprise après un arrêt à l'étape (n), sont des précisions de texte. Aucun ne demande le mot de Lazar.
- **Essais : 324 passés.**

## Pièces lues et conditions

- **Vérificateur** : Claude Opus 5.5 (`claude-opus-5-5`), même contre-lecteur que pour les versions 5 à 10.
- **Code** : commit `e2d10e3ca`. Les neuf modules `*_bras_a_v11.py`, les sept fichiers d'essais et `scripts/constat_de_lancement_discretion_bras_a_v4.py` répondent tous à leurs compagnons. Leurs empreintes sont celles de la note, par exemple :
  - `analyse_bras_a_v11.py` : `ea948d4b…` ;
  - `graines_bras_a_v11.py` : `c1525322…` ;
  - programme du constat v4 : `8ca94b7c…`.
- **Textes** :
  - note du code v11 (`27658a82…`) et relevé v11 (`2ef9e8f9…`), en entier ;
  - brouillon 34 (`0b6413d9…`), empreinte seulement.
  - Je n'ai lu ni la note du brouillon 34 ni sa vérification : la note du code et le relevé citent ce qu'elles fixent.
- **Essais** : la commande de la note donne **324 passés** (78 s) :

  ```
  PYTHONPATH=src .venv/bin/python -m pytest -q -p no:cacheprovider tests/test_analyse_bras_a_v11.py tests/test_verdicts_bras_a_v11.py tests/test_graines_bras_a_v11.py tests/test_cloisonnement_bras_a_v11.py tests/test_permutation_etiquettes_bras_a_v11.py tests/test_mesures_bras_a_v11.py tests/test_reponses_lecteurs_v5.py tests/test_epreuves_couverture_bras_a_v3.py
  ```

  L'essai du rédacteur qui passe la garde sur le vrai dépôt tourne sous un crochet qui refuse toute ouverture cloisonnée avant qu'elle ait lieu. Mes essais de la garde n'ont tourné que sur un faux dépôt.
- **Essais d'attaque** : données synthétiques et registres fabriqués, dans le bloc-notes sous `/tmp/claude-0/-home-user-controle-ia-travail/b7727ccc-db8b-5b89-bce1-17602831b69d/scratchpad/contre-lecture-code-v11/`. Chacun a sa sortie `….sortie.txt` :
  - `attaques_v11.py` : C-1 rejoué, arrêt à l'étape (n) puis livraison refaite, contrôle d'avant le premier départ, phrases d'accord, porte de l'écart à R9, « en attente », mêmes choix ;
  - `abandon_v11.py` : configuration abandonnée, et ce qui lève la garde du registre ;
  - `audit_cloisonnement_v11.py`, `attaques_cloisonnement_v11.py` et `fuzz_livraison_v11.py` ;
  - `essais.sortie.txt` : la commande de la note.

  Une partie de `attaques_v11.py` sur la configuration abandonnée donnait par erreur la même empreinte aux deux configurations : `abandon_v11.py` la remplace.
- **Heure** : 2026-11-20T00:55Z.

---

## 1. Défauts bloquants

Aucun.

## 2. Défaut à corriger

### C-1. Après un arrêt à l'étape (n), une livraison refaite relit l'étape (m) : deux tables C dans la course
- **Où** : `analyse_bras_a_v11.py`, `_exiger_lecture_permise` et `_exiger_la_ligne_de_reprise`. Une ligne de GO peut citer **tout** fichier d'arrêt du dossier, qu'il soit de l'étape (m) ou de l'étape (n). La livraison refaite suit alors tout le chemin d'une lecture : étape (m), résultat, fichier de l'étape (m) dans son dossier de livraison.
- **Essai** (`attaques_v11.py`) :
  1. Le rang 1 est lu. Le juge à la dose 1 « ne repère pas ». Le fichier (m) est scellé.
  2. Le fichier des scores par unité est fautif (un champ de plus) : arrêt à l'étape (n), fichier d'arrêt scellé.
  3. Une ligne de GO cite ce fichier d'arrêt, et une configuration de rang 2 avec son constat est écrite. La pièce B, où le juge « repère », est lue, et son fichier (m) est scellé dans `livraison-2/`.
  4. Le fichier (m) du rang 1 existe toujours. La course porte donc deux tables C contraires.
- **Pourquoi c'est à corriger** :
  - L'issue retenue par Lazar (fiche 12, option (c)) dit qu'un arrêt à l'étape (n) **laisse tel quel le fichier scellé de l'étape (m)**, opposable. Une reprise après un tel arrêt ne peut donc porter que sur ce que l'étape (n) devait rendre.
  - Sinon, la règle d'octroi devient un moyen de rejouer la discrétion après coup et de choisir. Un fichier des scores par unité fautif suffit, et il vient du même côté qui livre la pièce.
- **Ce qui le fermerait** :
  - quand le fichier d'arrêt cité est de l'étape (n), refuser toute lecture de l'étape (m) sous la ligne de GO ;
  - la reprise ne rejoue que l'étape (n), sur le fichier (m) du rang d'origine, avec un fichier des scores par unité refait ;
  - et, en tout cas, refuser un second fichier de l'étape (m) dans une course où un fichier (m) est déjà scellé et opposable ;
  - au texte, écrire le périmètre d'une reprise après un arrêt à l'étape (n) : c'est une précision de l'option (c), non une question pour Lazar.

## 3. Défauts mineurs

- **M-1. Un contrôle fait avant le premier départ sert encore au rejeu** (relevé A.4, confirmé).
  - Essai : contrôle sain, première lecture interrompue après son ouverture, puis une ligne qui retire la configuration entre au registre. Sans contrôle refait, le rejeu part sur le contrôle d'avant le premier départ.
  - Le contrôle n'a pas de trace de rejeu, et rien de scellé ne date le premier départ.
  - **Fermeture** : l'ouverture de lecture, et l'acte de reprise, portent l'empreinte du contrôle sous lequel le premier départ est parti, ou `null`. Un rejeu refuse tout contrôle que porte une ouverture, un acte ou une trace de rejeu. C'est un champ de plus aux deux fichiers.
- **M-2. La garde du registre au constat se lève avec une ligne de reprise sans rapport** (relevé B.2, confirmé). Une inscription d'une autre configuration de rang 1 fait refuser le constat. Une ligne placée après elle qui porte la phrase d'accord d'une livraison refaite, **sans aucune empreinte**, suffit à le rendre sain (`abandon_v11.py`). La garde contre une autre course (M-4 de la v10) ne tient donc qu'à la discipline du registre. Correction : exiger que la ligne de reprise qui « suit » une inscription cite l'empreinte entière d'un fichier d'arrêt ou d'un constat, et que la configuration qu'elle ouvre soit de rang supérieur à 1 dans la course de l'inscription.
- **M-3. Une configuration inscrite puis abandonnée bloque la suivante** (relevé A.1, confirmé). Rien ne la lève, pas même une ligne de type « révocation » qui la retire en citant son empreinte entière. C'est un arrêt à tort, sans passage à tort. Voir la partie 6.
- **M-4. Abrégés de moins de seize signes** : écart motivé, inchangé (la consigne de tenue du registre).

## 4. Corrections de la version 10 (question 1)

| défaut v10 | jugement | preuve (rejouée contre v11) |
|---|---|---|
| C-1 deux livraisons sans ligne de GO | **tenu** pour les deux formes | même configuration : la pièce B est refusée (« une lecture a déjà été ouverte dans cette course… ») ; rang 2 sans registre figé : refusé à la lecture de la configuration. Voie neuve : C-1 ci-dessus |
| M-1 phrase de l'écart à R9 | **tenu** | 12 lignes (partie 5) |
| M-2 contrôle ancien après une révocation | **tenu en partie** | la trace de rejeu empêche de reprendre un contrôle déjà servi ; reste le contrôle d'avant le premier départ (M-1 ci-dessus) |
| M-3 abrégés | écart motivé | — |
| M-4 autre course | **tenu en partie** | refusé au constat pour un registre commun ; levé par une ligne de reprise sans rapport (M-2 ci-dessus) ; l'analyse ne voit que son dossier des arrêts |
| M-5 « en attente » sans trace | **tenu** | `piece-en-attente-d-un-choix-…` scellé ; une autre pièce, ensuite, est refusée sans ligne de GO |

**Autres voies cherchées pour lire deux pièces sans ligne de GO, ou choisir entre deux résultats** :
- **une autre configuration de même rang** : refusée par le dossier de livraison et par l'ouverture ;
- **un autre choix du point 20 en cours de course** : `memes_choix` n'admet que le passage d'« en attente » à une rédaction. Le passage d'« aire non calculable » à « module corrigé » est refusé (essai). Les deux rédactions se lisent de même dans l'analyse : rien à choisir ;
- **un autre choix du point 19** : refusé, puisque les mêmes choix sont exigés ;
- **une pièce mal rangée, donnée après une lecture aboutie** : son constat ne peut plus ouvrir de lecture (garde du rédacteur, relevé A.3) ;
- **le rejeu de la même pièce** : même résultat, la règle étant déterministe ; rien à choisir ;
- **un arrêt à l'étape (n)** : **voie ouverte**, C-1.

La fouille de 400 livraisons altérées donne 290 arrêts nommés et 16 gardes ordinaires, toutes de provenance.

## 5. Phrases d'accord, révocation, porte de l'écart à R9, garde du registre (question 2)

| ligne (cellule d'objet) | porte de l'écart à R9 |
|---|---|
| la phrase | ouvre |
| la phrase en gras | ouvre |
| la phrase suivie d'un point | ouvre |
| la phrase en majuscules | ouvre |
| la phrase, puis une cinquième cellule « note » | ouvre (l'objet est la quatrième cellule) |
| « … ? » ; « … ! » ; « aucun … » ; entre accents graves ; entre guillemets | refusée |
| type « révocation », objet = la phrase | refusée : une révocation n'est jamais un accord |
| ligne à trois cellules seulement | refusée |
| une ligne entrée depuis l'état figé qui nomme la ligne de GO (« suspendu ») | refusée |
| un registre courant qui a perdu une ligne de l'état figé | refusé |

C'est sûr et juste. Deux réserves : la cellule d'objet est fixée à la quatrième par une constante, ce qui reste à confirmer par la session principale (relevé B.5) ; un renvoi au mot de Lazar écrit avec son empreinte entière ferait une quatrième empreinte dans une ligne de reprise (relevé B.6).

**La garde du registre au constat** : voir M-2 et M-3.

## 6. Les cinq défauts de la partie A du relevé (question 3)

| point | nature | avis |
|---|---|---|
| A.1 configuration inscrite puis abandonnée | **précision** | Écrire le remède : une ligne de type « révocation » qui cite l'empreinte entière de la configuration abandonnée la retire, et le constat ne compte plus son inscription. La configuration retirée ne peut plus servir : son propre constat verrait cette ligne comme « ligne neuve à voir » et sortirait malsain. Aucune règle de jugement n'en dépend |
| A.2 mêmes choix, et « en attente » qui se tranche | **précision** | l'exception codée (rang supérieur : « en attente » vers une rédaction du point 20, jamais l'inverse) est la bonne ; elle disparaît avec la valeur au scellement |
| A.3 ce qu'un constat de pièce donnée peut ouvrir | **précision** | la garde du rédacteur est juste ; l'écrire dans « Ce que le programme confronte » |
| A.4 contrôle d'avant le premier départ | **précision** | fermer comme en M-1 (empreinte du contrôle dans l'ouverture et l'acte), plutôt qu'en limite |
| A.5 ponctuation finale | **précision** | « un point final, seul » : c'est le code, et c'est juste |
| (neuf) périmètre d'une reprise après un arrêt à l'étape (n) | **précision** | il découle de l'option (c) accordée : la table C reste opposable ; la reprise ne porte que sur l'étape (n) (C-1) |

Aucun n'appelle le mot de Lazar.

## 7. La garde statique (question 5)

Faux dépôt, valeurs par défaut, crochet d'audit écrit à part (`audit_cloisonnement_v11.py`) :
- ni la garde ni `listages_a_relire` n'ouvre ni ne liste un chemin cloisonné ;
- les chemins cloisonnés sont élagués par leur nom, y compris sous une autre casse ;
- un départ cloisonné, ou par `..`, est refusé ;
- un lien symbolique n'est pas suivi ;
- un lien physique n'est pas ouvert ;
- des 24 modules plantés, 19 sont refusés, un est signalé, et les restes déclarés passent.

## 8. Ce que je n'ai pas regardé
- La note et la vérification du brouillon 34, et le texte du brouillon 34.
- Les verdicts sous un arrêt à l'étape (n), et ce que `issues` fait de deux fichiers (m) dans une course. Mon essai s'arrête à l'écriture du second fichier.

## 9. Fichiers ouverts
- `CLAUDE.md`.
- `docs/notes/relance-organismes-discrets-v1/code-v11-bras-a-note-v1.md` et `defauts-du-texte-trouves-en-codant-v11.md`, en entier.
- Code : `configuration_bras_a_v11.py` (`memes_choix`, garde des configurations de la course) ; signatures de `graines_bras_a_v11.py` (`admettre_l_entropie_propre_…`, `dit_l_accord`, `lignes_entrees_depuis`) et de `analyse_bras_a_v11.py` (`exiger_une_seule_premiere_livraison`).
- Essais : `tests/aide_bras_a_v11.py` (noms) ; `tests/test_analyse_bras_a_v11.py` (classe `Livraison`, `en_rangs`, `lignes_de_scores`, fouille du fichier des rangs), dont je me sers dans mes essais d'attaque.
- **Non ouverts** :
  - aucun interne de moniteur, aucun module habilité, rien sous `bases/`, `sondes/` ou `t07*/`, rien de T0.8 ;
  - aucune fiche de l'organisme d'idéation, aucune réponse de lecteur, aucune clé ;
  - ni le vrai registre ;
  - aucun appel réseau ni de modèle, aucun sous-agent, rien d'installé, rien committé.
