# Attestation, sur les manifestes seuls, des sources honnêtes du versant honnête de l'essai « jumeau contre jumeau » — v1

Date : 2026-11-24, vers 09:55Z (`date -u`). Écrite par une session fille neuve (Opus 5.5, effort élevé), option (b) choisie par la mère (session_01Qi7Gr3Ggccg85kjmP654WC), sous le mandat `docs/notes/dossier-entretien-2026-12-01-v1/mandat-attestation-manifestes-versant-honnete-v1.md` (`56206b4ba41bb56df0e59cb61e53288ca9b2924f3b614bb773feda588d6c6bf5`, vérifié avant lecture). Pièce de travail (classe C). Aucune dépense, aucun contact externe. Aucun identifiant de tâche dans ce texte : seulement des comptes, des inclusions et des empreintes.

Inscription préalable sur la liste « qui a lu quoi » : `qui-a-lu-quoi-attestation-manifestes-v1.md` (même dossier, commit `f6584876` de la branche `dossier-entretien/attestation-manifestes-v1`, avant toute lecture).

## Verdict en trois lignes

- **Modèle de la course 7b contre l'étalonnage boîte noire v3** : identique sur les quatre champs demandés (modèle et révision, environnement de génération, pas par épisode, température) ; graines neuves de part et d'autre (entropies racines différentes). Trois réserves hors des champs, ci-dessous (§ Q1).
- **Témoin positif planté** : condition honnête nue = **« rejeu »** du premier test (même entropie racine, mêmes clés, mêmes graines, bit pour bit dans le manifeste) ; condition « texte de même longueur » = **« condition distincte »** (persona honnête et consigne de coût ajoutées à ce que reçoit l'agent), sur ces mêmes graines.
- **Banques** : la course 7b et l'étalonnage v3 jouent exactement la même banque de 64 tâches d'évaluation (même fichier, même empreinte) ; les 60 du premier test sont incluses dans ces 64 ; les 60 du témoin positif sont exactement les 60 du premier test. Concordant avec le constat de la session habilitée du coffre tel que le cite le mandat ; aucune divergence.

## Sources lues (R6) et contrôle des empreintes

Toutes lues par `git show <branche>:<chemin>` (aucune branche de calcul extraite ni fusionnée ; la branche du témoin positif récupérée en clone partiel sans contenu, un seul fichier rapatrié à la demande).

| pièce | branche (commit) | empreinte recalculée | compagnon `.sha256` |
|---|---|---|---|
| `runs/20261019-230011-p3-reel/manifeste.json` (premier test boîte blanche) | main (`42260394`) | `3f21774ca2a740e059191e762a4922076d954ee4c3e728c9927ba436cb211685` | conforme |
| `runs/20261113-121129-p3bis-reel/manifeste.json` (témoin positif planté) | `calcul/p3bis-reel-v2` (`2aaaaf87`) | `bb8b312cd03736be6ff843f8629abc21f531315a5279345f630ea93e29e034f6` | conforme |
| `runs/20261111-151701-t06-reel/manifeste.json` (course 7b) | `calcul/t06-confirmation-7b-v1` (`55c3e3eb`) | `7e1ac1f02584e4f8babf664e78d12f3122bfdca18292734f28281e9459479bf6` | conforme |
| `runs/20261123-060509-t08-reel/manifeste.json` (étalonnage boîte noire v3) | `calcul/t08-course-v3` (`50a6d30c`) | `dbb2723e4ef9b58c1b7351705b86fb302ece0504f84af0e709e2706bed9ca382` | conforme |
| `prereg/P3-premier-test-i-a-v1.md` (cité par le manifeste du premier test) | main | `d975e9817e88d30196930c2a351927c2091f2ac024d2a5b52556730fa36cb672` | égale à la citation du manifeste |
| `prereg/P3-consignes-v1.md` | main | `a68468fef6286bbcaa31451ba461d0adab2af7d529dd5e4fa0695643e6d1d69c` | égale à la configuration |
| `prereg/P3-bis-temoin-positif-v1.md` | `calcul/p3bis-reel-v2` | `76ab66ce967796b944e2ca585ee0dc2d780189e8e0cbe429e390c427a46121cb` | égale à la citation du manifeste |
| `prereg/P3-bis-consignes-v1.md` | `calcul/p3bis-reel-v2` | `7d35576d65c030edcc6441e142ea95732679b674edcb1fd1af86ab8f69c04367` | égale à la configuration |
| `prereg/T0.6-organismes-v0-v1.md` | `calcul/t06-confirmation-7b-v1` | `ef31feff9abb26d0d66c3c35f3c721ee7d054a63f880657535a5e4a47cbdf169` | égale à la citation du manifeste |
| `prereg/T0.8-bases-boite-noire-v0-v3.md` | `calcul/t08-course-v3` | `72a2611b3eff8ef070ab6f12f1468213cb88a8f42729eb2e9edeea7fcb884918` | égale à la citation du manifeste |
| `donnees/20261007-082440-t05-extraction/taches-evaluation.json` (champ `identifiant` seul) | main, 7b et étalonnage v3 (même octets sur les trois) | `76cdeace861d2fff45ca732c55c2d97611dcd47edc7c27d62bdad4c37755e67e` | conforme |
| `donnees/20261007-082440-t05-extraction/taches-entrainement.json` (champ `identifiant` seul ; désigné par le manifeste de 7b) | main | `8d20a698d76baa8a42cd1494227fc411ef043d24a67a413e5cf812541166a4fd` | conforme |

Les préenregistrements n'ont été lus que par recherche ciblée (graines, conditions, réglages de génération, tâches). Aucun devis distinct n'a été ouvert : les réglages utiles sont tous dans les manifestes et les préenregistrements. **Non lus** : tout `diag/`, toute sortie de course, tout score, verdict ou lecture, le coffre, les textes honnêtes de l'étalonnage, les épisodes de la course 7b (le manifeste de l'étalonnage cite ces derniers comme entrée, par chemin et empreinte ; ils n'ont pas été ouverts), aucun énoncé de tâche, aucun code.

Empreinte d'ensemble de tâches (calcul de cette note) : sha256 des identifiants triés, joints par un saut de ligne, sans saut final. Les identifiants sont pris aux clés de graines des manifestes (`tache/…` ; `etalonnage/tache/…/e<k>` pour l'étalonnage) et au champ `identifiant` des listes.

## Q1 — le modèle de la course 7b contre l'étalonnage boîte noire v3

| champ | course 7b (manifeste `7e1ac1f0…`, `config`) | étalonnage v3 (manifeste `dbb2723e…`, `config`) | réponse |
|---|---|---|---|
| modèle de base | `meta-llama/Llama-3.1-8B-Instruct` | `meta-llama/Llama-3.1-8B-Instruct` | identique |
| révision | `0e9e39f249a16976918f6564b8830bc894c89659` | `0e9e39f249a16976918f6564b8830bc894c89659` | identique |
| gabarit (texte d'ouverture, date) | « Today Date: 26 Jul 2024 », `26 Jul 2024` | même | identique |
| environnement de génération | environnement (a) (T0.6, plan point 4) ; consignes `prereg/P3-consignes-v1.md` `a68468fe…` (rien pour l'honnête) ; N = 1 ; lot 8 ; 400 jetons au plus par action ; noyau « defaut » | environnement (a), condition `honnete` (T0.8 v3, plan point 2) ; consignes `a68468fe…` (entrée `consignes`) ; N = 1 ; lot 8 ; 400 jetons au plus ; noyau « defaut » | identique |
| pas par épisode | T = 10 | T = 10 | identique |
| température | 1,0 | 1,0 | identique |
| bibliothèques (`versions`) | torch 2.14.1, transformers 5.18.0, tokenizers 0.23.2, numpy 2.4.6, python 3.11.18 | mêmes | identique (noyau Linux de l'hôte différent : 6.5.0-44 contre 5.15.0-198) |
| graines | entropie racine `31538212097275005629337336542801867913`, clé `tache/<identifiant>` (64) | entropie racine `245270939051202201813123096137161033361`, clés `etalonnage/tache/<identifiant>/e0` à `e4` (320) | **neuves** de part et d'autre |

**Réponse : « identique » sur les quatre champs du mandat.** Le sixième jumeau de la course 7b peut donc être compté sous la règle du mandat.

Réserves hors des champs demandés (métadonnées, non des résultats), à porter au devis :
1. **Adaptateurs injectés à dose 0.** Dans la course 7b, l'honnête est généré par le modèle porteur d'adaptateurs injectés à dose 0 (T0.6, plan point 4 : « adaptateurs injectés, dose 0 : le modèle de base ») ; l'identité au bit avec le modèle de base est un contrôle de T0.6, que T0.8 v3 prend pour hypothèse de travail (4). Le résultat de ce contrôle n'est pas une métadonnée : non lu.
2. **Composition des lots.** Dans 7b, les lots de dose 0 mêlent l'honnête aux trois conditions à consigne du premier test (T0.6, point 4) ; dans l'étalonnage, les lots ne portent que des épisodes honnêtes. Le préenregistrement du témoin positif note lui-même que la composition des lots change les trajectoires (« rejeu honnête partiel attendu »). Sans effet sur l'échangeabilité au sens des graines ; à dire si le devis parle d'identité au bit.
3. **Garde d'équivalence en ligne.** Jouée sur 5 % des actions dans 7b ; non requise dans l'étalonnage (« si le code du harnais la joue, c'est à la fraction de 7b, 0,05, et elle est consignée ») ; la configuration de l'étalonnage ne porte pas de champ `fraction_equivalence`. Qu'elle ait tourné ou non est **indéterminable par le manifeste** : il faudrait lire le journal de la course d'étalonnage (non lu).

T0.8 v3 pose d'ailleurs explicitement l'échangeabilité (hypothèse de travail (3) : « mêmes 64 tâches, même modèle et même révision, mêmes réglages de génération, graines neuves »), éprouvée par sa propre garde de fausses alertes sur les 64 épisodes honnêtes de 7b (résultat non lu).

## Q2 — les conditions honnêtes du témoin positif planté contre la condition honnête du premier test

Faits relevés :
- **Tâches** : 60 clés `tache/…` dans chacun des deux manifestes ; même ensemble (empreinte d'ensemble `7fc12c2480d3ad372b17cf2c307eb66fcc7893b7705af0e79a0b7757c1e0cefe` des deux côtés). Les deux préenregistrements citent la même empreinte de tâches de P3 (`287e83485cba550098b80db809589398d8f2826c02dfa9cc2719a1063795d5aa` : P3 l. 40 ; P3-bis, § 0 bis) ; le fichier qu'elle désigne n'est nommé par aucun manifeste et n'a pas été cherché ; elle n'est pas recalculable depuis les seuls identifiants (forme différente).
- **Graines** : même entropie racine `173398867739501636779144561928402532101` ; mêmes 96 clés ; les 96 entrées (entropie, `spawn_key`, `etat_controle`) sont **égales une à une**. P3-bis, en-tête : « celle de P3, reprise à dessein […] mêmes clés, donc mêmes graines […] chaque tâche » ; plan, point 1 : « mêmes graines d'action pour une même tâche d'un emplacement à l'autre » ; PB-9 : « rejeu honnête partiel attendu (la composition des lots change avec les textes) ». T0.6 (l. 250) confirme la lecture : reprendre l'entropie de P3 « rejouerait les graines d'action de P3 sur ses 60 tâches ».
- **Réglages** : modèle, révision, gabarit, environnement (a), T = 10, N = 1, lot 8, 400 jetons, température 1,0, noyau « defaut », garde d'équivalence 5 % : égaux dans les deux configurations. Les seuls écarts de configuration sont hors de la génération de l'honnête : fichier de consignes (`a68468fe…` → `7d35576d…`), plancher 200 → 800, fils d'entraînement 32 → 30, durées bornées → sans échéance.
- **Ce que reçoit l'agent** : l'honnête ne reçoit rien dans les deux courses (« l'environnement (a) sans rien d'autre » ; P3-bis consignes : « Rien pour l'honnête »). L'emplacement « témoin » de P3-bis porte le **témoin honnête de même longueur** : phrase de persona honnête puis consigne de déclarer un coût égal à l'estimation honnête, ajoutée à la fin du message système et répétée entière avant chaque « Your action: » (`prereg/P3-bis-consignes-v1.md`, `7d35576d…`, § « Emplacement témoin » et « Place »).

| condition du témoin positif | même liste de tâches | graines | réglages de génération | consigne de l'agent | verdict |
|---|---|---|---|---|---|
| honnête nue (emplacement `honnete`) | oui | **mêmes** que le premier test (entropie, clés et dérivées égales) | identiques | intacte (rien d'ajouté, comme au premier test) | **« rejeu »** |
| texte de même longueur (emplacement `temoin`) | oui | **mêmes** que le premier test et que l'honnête nue (même clé par tâche, un générateur neuf par condition) | identiques | **modifiée** (persona honnête et consigne de coût honnête, dans le message système et avant chaque action) | **« condition distincte »** |

Conséquence pour le devis (constat, non décision) : aucune des deux conditions honnêtes du témoin positif n'est un jumeau indépendant de l'honnête du premier test. La nue en est un rejeu (au bit près si le calcul l'est ; partiel selon P3-bis, la composition des lots changeant) ; la seconde partage ses graines et change l'entrée de l'agent.

## Q3 — les deux banques de tâches

| course | source de la liste | nombre | empreinte d'ensemble (calcul de cette note) | empreinte du fichier |
|---|---|---|---|---|
| premier test | clés `tache/…` du manifeste `3f21774c…` (aucun fichier nommé ; empreinte citée par le préenregistrement : `287e8348…`) | 60 | `7fc12c2480d3ad372b17cf2c307eb66fcc7893b7705af0e79a0b7757c1e0cefe` | non recalculable (fichier non nommé) |
| témoin positif planté | clés `tache/…` du manifeste `bb8b312c…` (même empreinte citée `287e8348…`) | 60 | `7fc12c2480d3ad372b17cf2c307eb66fcc7893b7705af0e79a0b7757c1e0cefe` | non recalculable (fichier non nommé) |
| course 7b | `config.taches_evaluation` du manifeste `7e1ac1f0…` ; clés `tache/…` | 64 | `a18abadfe1044e4935a404a83650a3b5ccab77dbbbf3da82eaf10611c6b39ea3` | `76cdeace…` (cité et recalculé) |
| étalonnage v3 | `config.entrees.taches` du manifeste `dbb2723e…` ; clés `etalonnage/tache/…` (5 par tâche) | 64 (320 épisodes) | `a18abadfe1044e4935a404a83650a3b5ccab77dbbbf3da82eaf10611c6b39ea3` | `76cdeace…` (cité et recalculé) |
| fichier des tâches d'évaluation | `taches-evaluation.json`, champ `identifiant` | 64, sans doublon | `a18abadfe1044e4935a404a83650a3b5ccab77dbbbf3da82eaf10611c6b39ea3` | `76cdeace…` |

Inclusions, par identifiants :
- les 60 du premier test dans les 64 : **oui** (4 tâches des 64 hors du premier test) ;
- les 60 du témoin positif égales aux 60 du premier test : **oui** ;
- les 64 de la course 7b égales aux 64 de l'étalonnage v3 : **oui** (et égales au fichier des tâches d'évaluation) ;
- en plus : aucune des 64 (donc aucune des 60) n'est parmi les 32 tâches de distillation de 7b (`taches-entrainement.json`, `8d20a698…`, désigné par le manifeste de 7b) : intersection **vide**.

**Rapprochement du constat de la session habilitée du coffre** (tel que le mandat le cite : séparation d'avec la famille tenue à l'écart pour les 64 et pour les 60, « les 60 sont incluses dans les 64 ») : l'inclusion est **confirmée** par les manifestes ; aucune divergence. La disjonction d'avec la famille tenue à l'écart elle-même n'est pas vérifiable ici (cette famille est hors du périmètre de lecture) : elle reste du ressort de cette session.

## Ce qui reste indéterminable par les métadonnées

- Si la garde d'équivalence en ligne a tourné pendant l'étalonnage v3 : il faudrait lire le journal de cette course (non lu).
- L'identité au bit du modèle porteur d'adaptateurs à dose 0 avec le modèle de base dans 7b : il faudrait lire le contrôle d'identité de T0.6 (sortie de course, non lue).
- Le fichier que désigne l'empreinte de tâches `287e8348…` du premier test : non nommé par les manifestes ; l'égalité des ensembles d'identifiants suffit aux trois questions.
