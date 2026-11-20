# Rapport du développeur — générateur des témoins et garde de recouvrement de l'étage 2 à 200 (ligne 3, organisme v9) — v3

Pièce de travail, écrite le 2026-11-20. Même développeur, modèle O ; même mandat (`9066be25…`, en-tête compris). La v2 (programme `a3a4e82f…`, essais `1b567643…`, rapport `64254de5…`) est gardée sans modification (règle R12). La v3 porte les cinq décisions de la mère (15:20Z), prises après la vérification « Conforme » et le contrôle de la condition (4) « Conforme » de la v2. **Elle ne porte rien d'autre.** Je n'ai pas relu ces deux pièces : les décisions m'ont été transmises par la session du compte de l'organisme.

**Aucune commande, d'aucune sorte, sur un chemin sous `archives-reponses-modeles/`.** Le fichier des cartes n'a pas été ouvert. La garde n'a jamais tourné hors des essais sur cartes factices. Aucun réseau, aucune clé, aucune dépense ; aucune écriture dans le dépôt de travail ni dans le clone de l'organisme. Ce rapport complète ceux des v1 et v2, qui restent valables là où rien n'est dit ici.

## 0. Ce que porte la v3

Lignes de `generer_temoins_ligne_3_v3.py` (`f5de9c3c…`).

| décision de la mère | où, en v3 |
|---|---|
| (1) `creer-journal-rejeux` refuse si l'historique git du dépôt connaît déjà le manifeste de création | `historique_connait` l. 1189 : `git -C DEPOT log --all --format=%H -- <chemin relatif du manifeste>`, lecture seule, entrée standard fermée, sans réseau. Sortie non vide → `ManifesteJournalConnuDeLHistorique` (l. 1216). Git absent ou en échec, ou manifeste hors du dépôt → `HistoriqueGitIllisible` (aucun repli). `LieuDuJournal` porte le dépôt lu : `DEPOT` en production ; un dépôt git temporaire, en Python seulement, pour les essais. |
| (2) seule la forme réelle du fichier des cartes | `cartes_du_fichier` l. 1021 : un objet non vide, chaque clé un identifiant de treize caractères (`LONGUEUR_IDENTIFIANT_CARTE`), chaque valeur un objet qui porte un `contenu` objet ; toute autre forme → `FormatCartesInconnu`, avant toute comparaison. Les sept cartes du repli sont prises par égalité exacte (l. 1047). |
| (3) ligne de portée de la pièce du (4), confrontée à `--repli` | `LIGNE_PORTEE` l. 182 ; `exiger_controle_conforme` l. 1245. Ligne absente, ou deux valeurs dans la pièce → `ControleQuatrePorteeAbsente` (l. 1262). « garde entière » avec `--repli`, ou « repli seul » sans `--repli` → `ControleQuatrePorteeAutre` (l. 1265). Tout cela avant l'ouverture. La validité de la cause du repli et la pièce du déclencheur sont vérifiées juste avant la pièce du (4) (l. 1364). |
| (4) `creer-journal-rejeux` sur un journal existant sans manifeste | refus nommé `JournalExisteSansManifeste` (l. 1218) ; à la ligne de commande (l. 1905), toute exception de ce geste ne rend que son nom de classe et la ligne, sur la sortie d'erreur, sans trace brute |
| (5) fenêtre entre la vérification d'empreinte et la relecture de la pièce | `_lire_piece` l. 1268 : les octets sont lus une fois et l'empreinte est vérifiée sur ces octets ; `exiger_controle_conforme` analyse ces mêmes octets (l. 1250). Il n'y a plus de seconde lecture (`_verifier_piece` passe aussi par `_lire_piece`). |

## 1. Forme exacte de la ligne de portée (à écrire par le contrôleur)

La pièce passée à `--controle-4` doit porter **exactement une** des deux lignes suivantes, seule sur sa ligne :

```
Portée : garde entière
```

ou

```
Portée : repli seul
```

Ce que le code admet en plus : le gras autour de la ligne (`**Portée : garde entière**`) et un point final. Expression : `^(\*\*)?Portée\s*:\s*(garde entière|repli seul)\.?(\*\*)?$`, appliquée à chaque ligne débarrassée de ses espaces de bord. « Portée » prend l'accent, « entière » aussi ; tout est en minuscules sauf « Portée ».

Règle :
- sans `--repli`, il faut « garde entière » ;
- avec `--repli`, il faut « repli seul » ;
- deux lignes de portée de valeurs différentes, ou aucune, donnent un refus.

Le reste de la pièce est inchangé depuis la v2 :
- une ligne de verdict seule sur sa ligne, `Conforme`, `**Conforme.**`, `Verdict : Conforme` ou `**Verdict : Conforme**` ;
- aucune ligne qui commence par « Non conforme » ;
- l'empreinte du programme contrôlé, ici `f5de9c3c94be525d1ec48d3e7954135473894a298aafe908475f043934278ae0`.

Sous le repli par le second déclencheur, je garde la répartition des pièces de la v2, à confirmer par la mère :
- la pièce « repli seul » passe à `--controle-4` ;
- la pièce du déclencheur (le « non conforme » sur l'entrée) passe à `--piece-repli`.

## 2. Pièces (empreintes recalculées)

| pièce | sha256 |
|---|---|
| `generer_temoins_ligne_3_v3.py` | `f5de9c3c94be525d1ec48d3e7954135473894a298aafe908475f043934278ae0` |
| `essais_generer_temoins_ligne_3_v3.py` | `7e064c90fe90a79ee9336b968c141b569b608df865e58ec25a00ff227a741a0f` |
| `fragments-exemple-essais-v3.json` (octets identiques à v1 et v2) | `a66cf6d4ae04a66a3f90e9f0108e09cf68c911ba3ee25852bdcedcc093311cbd` |
| `differentiel-programme-v2-v3.diff` (`diff -u`) | `b88de2f0d751e8dd5cb1aa1dd672428142bdaec032e875b7179f240a7bca76de` |
| `differentiel-essais-v2-v3.diff` (`diff -u`) | `04be8ad25c8d0ca3a0d6d5a9ae4ee450523c8c88769337430213aa45b645515c` |

## 3. Différentiel v2 → v3, en clair

Programme :
1. En-tête : version 3 et ses cinq changements ; `VERSION`.
2. Constantes : `LIGNE_PORTEE`, `PORTEE_GARDE_ENTIERE`, `PORTEE_REPLI_SEUL`, `LONGUEUR_IDENTIFIANT_CARTE` (13).
3. Exceptions : `ManifesteJournalConnuDeLHistorique`, `HistoriqueGitIllisible`, `JournalExisteSansManifeste`, `ControleQuatrePorteeAbsente`, `ControleQuatrePorteeAutre`.
4. `cartes_du_fichier` : la forme réelle seule (les branches liste et `{"fiches": …}` sont retirées) ; `cartes_nommees` : égalité exacte.
5. `LieuDuJournal` : attribut `depot` (production : `DEPOT`, contrôlé avec les deux constantes du journal).
6. `historique_connait` (neuve) ; `creer_journal_rejeux` : refus par l'historique, puis refus si le journal existe sans manifeste.
7. `exiger_controle_conforme(…, repli)` : lecture unique par `_lire_piece` (neuve), puis ligne de portée ; `_verifier_piece` passe par `_lire_piece`.
8. `jouer_la_garde` : la cause du repli et sa pièce sont vérifiées avant la pièce du (4), qui reçoit `repli`.
9. Ligne de commande, geste `creer-journal-rejeux` : toute exception est attrapée et ne rend que le nom de sa classe et sa ligne.

Essais :
- import et chemins v3 ;
- un dépôt git d'essai temporaire par essai qui crée un journal (`initialiser_depot` : `git init`, une validation vide, configuration d'identité passée en `-c`, sans réseau) ;
- cartes factices à la forme réelle (identifiants de treize caractères, `empreinte`, `meta`) ;
- pièce du (4) factice avec sa ligne de portée, « repli seul » choisie quand l'essai passe `--repli` ;
- l'essai « formes admises » devient « seule la forme réelle » (sain, plus cinq artefacts) ;
- essais neufs au § 4.

## 4. Essais rejoués en entier

`env -C …/generateur-v3 /home/user/controle-ia-travail/.venv/bin/python -B -m pytest -q -p no:cacheprovider essais_generer_temoins_ligne_3_v3.py` : **101 passed in 9.07s** (les 89 de la v2, adaptés, et 12 cas neufs).

Cas neufs ou changés :
- **Historique git** :
  - cas sain : dépôt d'essai dont l'historique ne connaît pas le manifeste → création faite ;
  - artefact : dépôt d'essai où le manifeste a été validé puis retiré → `ManifesteJournalConnuDeLHistorique`, journal non créé, en Python et par la ligne de commande, sans trace ;
  - hors dépôt git → `HistoriqueGitIllisible`.
- **Journal existant sans manifeste** → `JournalExisteSansManifeste`, en Python ; par la ligne de commande, la sortie d'erreur ne porte que `{"refus": "JournalExisteSansManifeste", "ligne": …}`, sans trace.
- **Portée** : quatre formes saines (garde entière, sans repli, 94 cartes lues ; repli seul, avec repli, 7 cartes lues) et cinq artefacts, tous refusés avant l'ouverture :
  - « repli seul » pour la garde entière ;
  - « garde entière » sous le repli ;
  - portée absente ;
  - deux portées ;
  - portée d'une autre valeur.
- **Forme réelle seule** :
  - sain : 94 cartes ;
  - artefacts : liste, `{"fiches": …}`, identifiant de quatorze caractères, carte sans `contenu`, objet vide → `FormatCartesInconnu`, aucune comparaison.
- **Lecture unique** de la pièce du (4) : une seule lecture du fichier ; aucune lecture de texte, aucun recalcul d'empreinte sur disque ; empreinte fausse → refus.

## 5. Écarts

1. Les essais lancent `git` (`init`, `commit`, `add`, `rm`, `log`) dans des dossiers temporaires du système, jamais dans le dépôt de travail. Le code ne lance `git log` sur `DEPOT` qu'au geste réel `creer-journal-rejeux`, qu'aucun essai n'exerce en production.
2. Un dépôt sans aucune validation n'a pas été essayé : les dépôts d'essai ont une validation vide. Sur le dépôt de travail, l'historique existe.
3. Les fragments factices sont recopiés sous le nom v3, octets identiques.
4. Je n'ai pas lu la vérification v1 (`4532e695…`) ni le contrôle (4) v2 (`f2066452…`) : je m'en tiens aux décisions transmises.

Développeur, modèle O.
