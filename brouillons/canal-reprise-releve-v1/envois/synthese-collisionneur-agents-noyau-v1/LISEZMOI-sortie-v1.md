# Lisez-moi de sortie — synthèse du collisionneur « agents sur le noyau pendant la conception par essais-erreurs » (v1)

Écrit le 2026-10-26 à 04:06 (temps universel, lu sur `date -u` dans la commande qui l'écrit) par un sous-agent neuf, sur le brief
de conv-audit `BRIEF-synthese-agents-noyau-v1.md` et sa mise à jour de 03:38 (texte du pilote 4 final et courses parties ;
registre d'hypothèses v2, protocole et briefs de la boucle extérieure écrits ailleurs ; cellules refusées non fournies).

## Ce qui a été fait
- Lu en entier, dans `/var/tmp/fournis-synthese-agents-noyau-v1/` seulement : le brief, la question, `LISEZMOI-v1.md` et
  `EMPREINTES-v1.txt` du tour, les sept cellules valides (après vérification de leurs empreintes), `methodo/LISEZMOI-v1.md`,
  la question reformulée et la réponse `methodo/E3-T1-conception-B.md`, l'exemple de synthèse (pour la forme).
- Aucun contenu de réflexion interne trouvé dans les réponses ; rien de tel n'est reproduit.
- Écrit dans `/var/tmp/synthese-collisionneur-agents-noyau-v1/` seulement : la synthèse, ce fichier et leurs compagnons
  `.sha256`.
- Ni git, ni réseau, ni sous-agent, ni clé, ni dépense ; aucune recherche récursive hors du dossier fourni.

## Vérification des réponses (avant leur lecture)
Chaque réponse est comparée à son compagnon `.sha256` et à `EMPREINTES-v1.txt`, dont les chemins sont relatifs au dossier
d'origine du tour (`run-agents-noyau-e3t1-v1/cellules/…`). Les compagnons eux-mêmes concordent aussi avec `EMPREINTES-v1.txt`.

| fichier fourni | empreinte calculée | compagnon | `EMPREINTES-v1.txt` |
|---|---|---|---|
| `cellules/E3-T1-conception-A.md` | `f6c8091976ba20b52d77c662a2181a9b8af7d95842143444d8755778d67f757c` | identique | identique |
| `cellules/E3-T1-conception-C.md` | `a90e252616e0db150c369cb3ebffd965d44cb9e7d857d905781851310d8b65e5` | identique | identique |
| `cellules/E3-T2-redteam-A.md` | `18d910184bf5408d7890296d926cbba8a16241da089db4e942c31c0b7b62476d` | identique | identique |
| `cellules/E3-T2-redteam-B.md` | `bc62052dfcf9d51eb35154c7af5cdd60a6040e6e5e02e267782cb6f78520b708` | identique | identique |
| `cellules/E3-T2-redteam-C.md` | `1b37bc3fde36b0a057885df606cffc3685d08ab8cf9636766dc1a345c6efdccd` | identique | identique |
| `cellules/E3-T3-riposte-A.md` | `a4f729650efb2af5f272af623923300c7467efa0c4753dab5a7658507418f364` | identique | identique |
| `cellules/E3-T3-riposte-C.md` | `e833c1e68ad12c9f37ac404d6e49c38dac98c50272bce8451152e0ce7e76a44b` | identique | identique |
| `methodo/E3-T1-conception-B.md` | `b6b9cbd31bf41d426143d287d1ce8a3545522fc8acb9344cdd39a64cc01f67c8` | identique | absente (autre lancement) |
| `question-agents-noyau-essais-erreurs-collisionneur-v1.md` | `6de36af770e501715c5ba9433f643eaf925ba12cebb054e5b796b140062ee159` | — | identique |
| `LISEZMOI-v1.md` | `63875420fffcbb8f806fd49f66d3447065d1e639ba37727e2094dd570b2665e8` | — | identique |
| `methodo/question-conception-iterative-statistique-collisionneur-v1.md` | `03acd5123dfcc738aa4ca45088c1032af37a817b66b2d6e557da5ee8d04de36c` | — | préfixe cité par `methodo/LISEZMOI-v1.md` |
| `BRIEF-synthese-agents-noyau-v1.md` | `95014839a37deb206655a983bd639c56ca8f3a57060f62d993b99d2cded40f9f` | — | sans référence |
| `exemple-synthese-precedente-lecture-pilote-v1.md` | `a8e1ed64a2ffe00eb0f5b27bb91e5ee1aa51a210b08b71beac8aeb0940ac127a` | — | sans référence |
| `EMPREINTES-v1.txt` | `9c8952b3d88d718d7ddb340173291058c8d2f3926c23b03ff23495e7d478180a` | — | sans référence |
| `methodo/LISEZMOI-v1.md` | `2f03270be52a1f921bed1962c9217310a3300f18d6d3d295dd587c34f851c64f` | — | sans référence |

- La réponse reformulée d'Opus (`methodo/E3-T1-conception-B.md`) vient d'un autre lancement
  (`run-agents-noyau-methodo-e3t1-v1`) : absente d'`EMPREINTES-v1.txt`, elle n'est vérifiée que contre son compagnon. Sa
  question concorde avec le préfixe `03acd512…` cité par `methodo/LISEZMOI-v1.md`.
- Les fichiers des cellules refusées listés par `EMPREINTES-v1.txt` ne sont pas fournis ; rien n'en est lu ni déduit.

## Sorties
| chemin | empreinte |
|---|---|
| `/var/tmp/synthese-collisionneur-agents-noyau-v1/synthese-collisionneur-agents-noyau-v1.md` | `f23ee71466bb92431b264799f5c4785b2ea614b2f324a39b74c753d5071127c9` |
| `/var/tmp/synthese-collisionneur-agents-noyau-v1/synthese-collisionneur-agents-noyau-v1.md.sha256` | `fafd9b1537d4aae1cbe7d5aeea0495f8d1bd1291d73cb652ea5fa3af7f85472e` |

- L'empreinte de ce fichier est dans son compagnon `LISEZMOI-sortie-v1.md.sha256` (un fichier ne peut contenir la sienne).
- Taille de la synthèse : 13739 caractères, 2358 mots au sens de `wc -w`, 141 lignes ; environ 2,9 pages à 100 caractères et 55 lignes par page, 2,6 pages à 110 et 60
  (estimation par repliage des paragraphes) ; trois pages au plus selon le brief.

## Écarts déclarés
1. Pas de routine de reprise du dépôt de travail (R14) ni de passation : la consigne de l'appelant borne la lecture au dossier
   fourni et l'écriture au dossier de sortie.
2. La ligne d'Opus, au § 2, vient de B′ (question reformulée, sans les familles de tâches), faute de cellule III.1 d'Opus ;
   B′ n'a été soumise à aucune équipe rouge.
3. Trois pages tenues en abrégeant : « et al. » pour des listes d'auteurs que les cellules donnent en entier, « … » pour sept
   sous-titres, détail des points 2 à 4 renvoyé aux § 3 à 5. Une contradiction interne mineure de B′ n'est consignée qu'ici :
   son total de jetons pour l'essai des outils (≈ 45 millions) suppose un vote au coût des appels simples ; à calcul apparié,
   ses propres hypothèses donnent ≈ 70 millions (refait, illustratif).
4. Les traits de classement des tâches présents dans plusieurs réponses (traits des références de surface, des canaris, des
   outils proposés ; méthode de partition ; exemple d'injection) sont nommés sans contenu, conformément au brief.
5. Sans acronymes, sauf : noms de fichiers, nom d'algorithme d'empreinte imposé par le brief, titres de références cités tels
   quels, noms propres de méthodes (McNemar, Brier, Thresholdout, Holm), étiquettes de cellules (A, B, C, T1 à T3, B′) et de
   règle (R7).
6. Une mention ajoutée dans la liste des références, « (injection indirecte) », identifie le titre abrégé de Greshake et al. ;
   aucune référence n'est ajoutée.
7. Les ajouts au pilote 4 « cette nuit » proposés en riposte par A et C sont dits caducs d'après la mise à jour de 03:38, sans
   être rejugés ; aucune décision déjà prise n'est rediscutée.
8. Heures lues sur `date -u` dans la commande même qui les écrit ; le système de fichiers affiche l'heure de Paris (une heure
   de plus).
