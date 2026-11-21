# Notes du développeur neuf de la seconde passe — première note : mémoire de travail et découpage — v1

Pièce de travail (classe C). Développeur neuf de la seconde passe, sous-agent de la session des lentilles
(`session_01Qi7Gr3vedYVukbyqBbHd7z`), branche `claude/brave-galileo-jhp684`, 2026-11-21 (UTC).

- Mandat : `docs/notes/lecture-sondes-bbis-par-lentilles-v1/mandats/mandat-developpeur-seconde-passe-lentilles-v1.md`,
  `4a3cf535f074a1a1a440482ca83ac4d45bd77e648b4b66bb6ff4c66b404f7d6a` (vérifié avant toute lecture).
- Mandat des deux passes `0a9517ea4e1d7460b411a0914996503eb3c6a9a680b4d3c88ae9d4f1f67bbdfc` et passation de l'étape 1
  `708203b150902935631d16c6da21472319aae2cd8be700d291af59f1f422c7e6` : empreintes recalculées, égales ; lus en entier.
- Texte de lecture v2 scellé : `prereg/lecture-sondes-bbis-par-lentilles-v2.md`,
  `a2bbed7ac34180b69864f143d1a910c8c29687dc73cca359c85256b6d9b78d15`, extrait de la branche principale par `git show` avec son
  compagnon, empreinte vérifiée avant toute lecture, versé tel quel sur cette branche.

## 1. Ma mémoire de travail peut-elle tenir le travail ? Réponse honnête : pas d'un seul tenant, sans doute pas en entier

Je ne peux pas mesurer ma mémoire de travail ; je peux seulement compter ce que j'y verse. Le texte v2 pèse 405 Ko, la section
« Code neuf » demande sept modules neufs, un module de statistiques neuf, un lanceur et plus d'une centaine d'essais (cas sain et
artefact pour chaque garde). Lire le texte entier, le paquet existant (plus de dix mille lignes), puis tout écrire et tout éprouver
ne tient très probablement pas dans une seule session. **Je ne promets donc pas l'étape 2 entière.** Je promets ceci : chaque
sous-étape close est commitée, poussée, et suivie d'une passation courte scellée ; si ma mémoire baisse, je m'arrête sur une
passation, et un remplaçant neuf reprend à la sous-étape suivante sans rien refaire.

## 2. Découpage en sous-étapes (ordre de dépendance ; chacune : code, essais R5, commit, poussée, passation courte scellée)

| n° | sous-étape | modules | dépend de |
|---|---|---|---|
| 0 | lecture des pièces, cette note, versement du texte v2 | — | — |
| 1 | statistique corrigée et règle de départage (identifiant de jeton croissant ; pôles : cosinus, indice de neurone, signe + avant −), comptes d'égalités | `statistiques_v4` | `statistiques_v1` à `v3` |
| 2 | fiche de rangement, condition de lecture, lignes de registre de la v2, issue des nœuds N12 et N17, archive de `torch.save` | `nos_lentilles_v1` | `entrees_v3` |
| 3 | lecture côté entrée par notre S, référence « plongements seuls », chemin indépendant | `lecture_entree_v1` | `lecture_v1` |
| 4 | recouvrements, p, médianes, corrélations, libellés de comparaison, calibration du recouvrement | `comparaisons_lentilles_v1` | sous-étape 1 |
| 5 | reproduction de la première passe ; déclencheurs d'audit ; phrases gelées de la seconde passe | `reproduction_v1`, `audits_v2`, `phrases_v2` | sous-étapes 2 et 4 |
| 6 | montage de la seconde passe ; lanceur sous horloge de 10 heures, canal des messages d'arrêt comme `lanceur_v7` ; bout en bout par palier | `montage_v2`, `lanceur_seconde_passe_v1` | toutes |
| 7 | rendu : table « garde → essai sain → essai artefact », sortie des essais, conformité point par point, empreintes | notes | toutes |

## 3. Règles que je tiens
Aucun module existant réécrit (R12) ; tout sur jouets ; aucun téléchargement de modèle, de lentille, de fichier d'ajustement ni de
corpus ; aucune clé lue ni testée ; rien ne se lance, ne se loue ni ne se dépense ; un refus d'outil n'est jamais rejoué. La liste
« Jamais ouverts » du texte v2 (lignes 1320 à 1343, repérées par les seuls débuts de lignes) n'est pas lue. Toute ambiguïté qui
oblige à choisir : nœud écrit et daté dans mes notes, et je continue le reste.

## 4. État à l'écriture de cette note
Lus en entier : `CLAUDE.md`, les deux mandats, la passation, `notes-developpement-v2.md`, la note de conformité v2, la
contre-lecture `7954d0fc…` ; du texte v2 : « Code neuf », « Vocabulaire », « Hypothèse », « Prédiction », « Entrées » (sans les
lignes 1320 à 1343), « Métrique », « Seuil ». Reste à lire avant d'écrire : « Plan d'analyse », « Critères », « Liste d'arrêt »,
« Lignes de registre », « Nœuds », les différences des brouillons, le reste ; les mots de Lazar nommés ; le lanceur v7 et ses notes.
Aucun code écrit. Aucune exposition involontaire à déclarer à ce point.
