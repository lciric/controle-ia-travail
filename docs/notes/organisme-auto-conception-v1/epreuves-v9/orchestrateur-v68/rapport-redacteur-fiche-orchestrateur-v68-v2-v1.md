# Rapport du rédacteur — fiche des quatre décisions sur l'orchestrateur v68, version 2 — v1

- Auteur : rédacteur neuf, modèle F (je n'ai écrit ni la fiche v1, ni son rapport, ni la contre-lecture). 2026-11-19 ; relevés de `date -u` : 23:33:41Z à la lecture, 23:37:10Z avant l'écriture, 23:41:18Z après la production de la fiche.
- Mandat : `docs/notes/organisme-auto-conception-v1/epreuves-v9/orchestrateur-v68/mandat-redacteur-fiche-quatre-decisions-orchestrateur-v68-v2-v1.md`, empreinte vérifiée avant de commencer : `c8acd3323857e462d3bfc83bc50b94c3a4fd0a5cffd74b2d8236e85accdd7c06`.
- Processeur seul. Aucun lancement de l'orchestrateur, aucun appel à un fournisseur de modèles, aucune dépense, aucune machine. Réseau : un `git fetch origin main` et des `git show origin/main:CHEMIN`. Aucun commit, aucune poussée, aucune écriture dans le dépôt (`git status --porcelain` vide à la fin, tête `c41ca058e`). Aucun heredoc, aucun code en ligne passé à un interpréteur, aucune valeur de clé, aucune commande sur un chemin sous le dossier d'archives interdit. Aucun refus d'outil.
- Le rapport de la v1 (`rapport-redacteur-fiche-orchestrateur-v68-v1.md`, `49df651bdbb6615ae5ead6343741d8f2f3ad5d0aef9b69eaf82d0af140c2bfda`) reste intact (R12) ; ses tables de sources valent pour les passages inchangés de la fiche. Ses trois phrases corrigées sont au § 3.

## 1. Livré, dans le bloc-notes seulement

Dossier : `/tmp/claude-0/-home-user-controle-ia-travail/227b647d-2ece-5654-bf04-8493b3ed2f19/scratchpad/redacteur-fiche-orchestrateur-v68-v2/`.

| fichier | sha256 |
|---|---|
| `fiche-quatre-decisions-orchestrateur-v68-v2.md` | `2b8e3815ed35cb68514c00a323a3451ec2eae6c65b5193b377369da7b7faa099` |
| `differentiel-fiche-orchestrateur-v68-v1-v2.diff` (`diff -u` de la v1 du dépôt à la v2) | `412d004e914dd20f37906a7e104087aecacafe6ba274b73041df89f2d7ee2597` |
| `remplacements-fiche-orchestrateur-v68-v1-v2.json` (40 remplacements) | `aab710cecdf64085914986182cee9e42f5c50269815aa295d910878d3011595b` |
| `fiche-quatre-decisions-orchestrateur-v68-v2.md.journal-remplacements-v1.json` (écrit par l'outil) | `4d22e4e6ca1d30c092e25a2a62490b4eb706a3778cd4a528e982aca9d6ed1ce0` |
| ce rapport | au compte rendu rendu à la session |

La fiche v2 est produite en un seul appel de l'outil contre-lu `scripts/remplacer_texte_exact_v1.py` (`391db990734dd36f7c827b8b6c77dc0de1bda324f671b65748ccfe68c56a53d6`) sur la v1 (`52741f65e0845e7958cd27bade7cd94683b4d51721e69223cd406fed20229bb6`), sans refus. L'outil a écrit aussi les deux compagnons `.sha256`. Sous `lu-main/` : copies de lecture de quatre fichiers de `main` et du texte scellé de la ligne 1 (§ 2).

## 2. Sources lues pour la v2, empreintes vérifiées

| pièce | empreinte | lu |
|---|---|---|
| fiche v1, rapport v1, mandat v1 | `52741f65…`, `49df651b…`, `fc551c3a0bc45db3933f260eb692215add08f9839b4aceac0a259f0f0b4f206f` | en entier |
| contre-lecture de la fiche v1 | `af90dae48d9e35770f00d1ee66becd26986caea13d76ea2f930cb5d83ec8e247` | en entier |
| rapport du développeur de la v68 | `ad42b7229a8e37aae823b1041a3acf1db91ee4053f5fec61136b6fd178b59aa6` | en entier |
| verdict de la course réelle v67 (`docs/notes/organisme-boucle-reelle-v1/course-v67/verdict-course-v67-v1.md`) | `d79024328157aafc5c801b5b0a4a621a5c009f367d88b96bbbfaeaeef3753459` | en-tête, § 4.3 à § 6 |
| rapport du palier 0a | `93d8a104ef551b931a6de84ecdaaca472cf05382ae49934c362e55d600058cd2` | lignes 98 à 108 |
| rapport du rang 0 | `966a387032bc45109d82942760666b9fe89c5204badb8ec9ae2c6968df6856aa` | ligne 53 ; lignes par mots |
| manifeste de fin du lanceur v9 | `28bc36df390d8481fb5bd9118cf764843ffea60856412d825ecbf08e7cee5be7` | `cartes_a_passeport` : 94 |
| contre-lecture de la v68 ; ordre de passage v3 ; devis v5 ; plan v5 ; résumé de l'essai à blanc | `d2cfeac1…`, `b19f550b…`, `30c87fa6…`, `9085bbe9…`, `11f56996…` | empreintes recalculées, égales ; ordre v3 par titres et point 14 ; le reste non relu |
| `main` à `7d0b0ba9e230d254a1a581280ca769dba2ed3cd3` : `registres/go.md` | `7ec26e969f096de325c83c57922894f7fbe5f9d22e3e5b7e742de8a3430d6118` | GO-2026-11-19-55 à -95 en entier ; la phrase « validée par l'essai à blanc » de GO-2026-11-10-11 et GO-2026-11-12-06 |
| `main` : `registres/depenses.md` | `43cad7c041ba7f5da3547fa52bcfcf004a3768ebfedb202f86386e20adfe2879` (inchangé depuis la v1) | lignes 415 à 430 |
| `main` : `registres/decisions.md` | `f6be8422f4331c17608bcf98986c7a4e8d34031c7c66149c72186840c2dc38a7` | R-3209, R-3965 à R-4008 |
| `main` : `docs/notes/trois-regles-course-generations-v1/etat-des-faits-v2.md` | `a4c99910f716073a1b8b868f90e34a7c2e785489cfdc99aa4cd3a0e6bcfebca7` (égal au compagnon) | § 0, § 5, § 7 règle 2 ; **hors de la liste du mandat**, ouvert pour lire la lettre de GO-2026-11-19-89 |
| `main` : `prereg/organisme-auto-conception-v9/preenregistrement-ligne-1-effort-recherche-v5.md` | `523adfd75333d7f2e99a6fe4f868c7dc6982a67e51953734f40258d7a40fc0b9` (égal au compagnon) | titre et quelques lignes par mots ; **hors liste**, ouvert pour savoir ce que visent GO-81 et GO-85 |

Ajoutés après la contre-lecture (correction R3) : `docs/notes/organisme-boucle-reelle-v1/course-v67/verdict-course-v67-v1.md` (`d79024328157aafc5c801b5b0a4a621a5c009f367d88b96bbbfaeaeef3753459`) et `runs/20261119-094145-course-auto-conception-v9/manifeste-lanceur-fin.json` (`28bc36df…`).

## 3. Corrections appliquées

**À la fiche : les dix-neuf, à la lettre**, par 28 des 40 remplacements (plusieurs corrections en comptent deux ou trois), plus un remplacement mixte (réserve 5 revue par moi, réserve 6 de la correction 19). Trois écarts de forme à la lettre, déclarés :

- correction 18 : la parenthèse « (rapport du rang 0, `966a3870…`, ligne 53) » est placée avant le point final de la phrase, non après ; la phrase est à l'enjeu, pas sous « Ce qu'il faut » ;
- correction 19 : « n'est pas dans les pièces du mandat » devient « n'était pas dans les pièces du mandat de la v1 », le mandat de la v2 nommant cette pièce ;
- correction 12 : la recommandation ne reste pas (a) ; le texte de repli de la contre-lecture (« (a), confiance 0,55 ») n'est donc pas employé (§ 4).

Les corrections 9 et le paragraphe sur GO-89 sont ajoutés comme paragraphes à part ; la réserve 6 suit la réserve 5.

**Au rapport v1 : les trois**, ici, le rapport v1 restant intact. Ses phrases se lisent désormais :

- R1, § 2, constat 5 : « elle cite les lignes d'accord du 10, du 12 et du 14 novembre (la dernière renvoie à R-2509, que la fiche ne cite pas). »
- R2, § 3, point 4 : « **Le coût d'un test de mort sur un engagement libre** : aucune mesure n'existe (devis v5, § 5) ; la course réelle v67, non lue par moi, en donne un relevé sur la forme imposée du tour fermé (contre-lecture de la fiche). Les montants de la décision 1 sont des bornes. » Le « moi » est le rédacteur de la v1 ; j'ai lu, pour la v2, les § 4.3 à 6 du verdict de la v67.
- R3 : les deux sources ajoutées sont au § 2 ci-dessus, avec la mention demandée.

**Hors des dix-neuf, changements du rédacteur de la v2** (onze remplacements et la moitié du mixte, aucun contre-lu) : titre ; ligne d'auteur ; ligne du mandat ; ligne des sources et commit de `main` ; verdict, recommandation (4) ; verdict, point 4 neuf ; décision 2, paragraphe sur GO-89 et confiance de la recommandation ; décision 4, phrase de décision, recommandation et défaut ; réserve 5.

## 4. Recommandation revue de la décision 4

**(b), confiance 0,6** (la v1 disait (a) à 0,7) : pas de machine louée à part ; elle va dans le devis du premier étage payant à tests de mort, l'essai du bac au vrai bac à sable en étant la première étape, avec arrêt s'il échoue. Raisons :

1. l'inconnue que (a) devait lever l'est déjà pour l'essentiel : la course v67 a joué le vrai bac sur une machine louée, 14 tests, scripts écrits par un modèle (verdict, § 4.4) ;
2. le précédent que la v1 invoquait pour (a) est celui de (b) : machine louée sous la ligne de la course, essai à blanc au vrai bac avant tout appel payant (GO-2026-11-10-11, GO-2026-11-12-06) ;
3. un essai loué aujourd'hui porterait sur la v68, qui refuse toujours le moteur réel ; la version suivante devra rejouer l'essai avant son premier appel payant.

Ce qui pèse contre, dit dans la fiche : sous (b), un bac qui ne tient pas sur le chemin de la course à plusieurs générations s'apprend tard ; le rapport du développeur de la v68 place l'essai « avant tout GO d'étage » (§ 9, point 5), ce qui est l'ordre de (a). Retour à (a) si le recoupement sur le code montre que l'étage joué en v67 n'est pas celui qu'appelle la course à plusieurs générations, ou si le premier étage payant passe par cette course et reste loin. La phrase de décision ne dit plus « sur un devis à part », qui supposait (a).

## 5. Décisions de Lazar prises depuis la v1 : ce qu'elles tranchent

**Aucune des quatre décisions n'est tranchée en entier ; aucune n'est retirée.** La fiche garde quatre décisions. Dit au point 4 du verdict.

- **GO-2026-11-19-89** (rien du juge servi aux proposeurs dans les courses qui comptent) : tranche une part de la décision 2 qui n'était pas une option de la fiche ; la v68 la tient déjà (aucun régime ne sert le classement des juges). Elle ne tranche pas « servir le nom et l'énoncé des survivantes ».
- **GO-2026-11-19-81 (B (a)) et -77 (héritage, décision 3 (a))** : l'expérimentateur reçoit l'engagement seul, à forme imposée, aux paliers payants de l'héritage. Déjà dans la v1 ; l'extension à l'étage de la course de l'orchestrateur reste la recommandation « alignement », à écrire dans l'additif.
- **GO-2026-11-19-81 (addendum de la ligne 1) et -85** : ils portent sur la ligne 1, dont le texte scellé est « étage sur processeur seul ». La v68 ne bloque aucun étage sur processeur : rien ne change au rang 1 du tableau.
- **GO-2026-11-19-76 (point 1) et -77 (héritage, décision 1 (a))** : l'activation « reste un mot à part », d'abord pour le seul palier 1 ; le lecteur témoin joué en réel au seul palier 1. L'ordre de l'option (a) de la décision 1 est donc déjà le tien ; le mot lui-même reste à donner, et la correction 8 demande de fixer d'abord le véhicule du palier 1.

## 6. Constats du rédacteur de la v2, à contre-lire

1. **La lettre de GO-89 et celle de l'héritage ne disent pas la même chose des survivantes.** GO-89 prend pour règle la « vue sans verdict, comme le code depuis la v59 ». Selon l'état des faits des trois règles (`a4c99910…`, § 0, § 5, § 7), cette vue est celle où la génération suivante reçoit les seules lois retenues : « Ce qui passe toujours : un bit par loi (retenue ou non) ». La course v67 l'a jouée en réel (verdict, § 4.3 : la génération 2 a reçu la loi de départ et les 11 retenues). La lecture de la garde acceptée par GO-76, point 2 (devis v5, § 9), range au contraire « la sélection des survivants » du côté interdit. Je l'ai écrit à l'enjeu de la décision 2, comme lecture du rédacteur, et j'ai baissé la confiance de (a) de 0,65 à 0,5, (c) devenant presque aussi bonne. Je n'ai pas changé l'option recommandée. Le point 3 du verdict de la fiche, inchangé, ne dit que le côté « héritage ».
2. **La contre-lecture n'avait pas relevé ce fait de la v67 pour la décision 2** : elle l'emploie pour les décisions 1 et 4 seulement.
3. **R-3209, point 3** (18 novembre) : Lazar a demandé que le mot « survit » des tests de mort soit remplacé par un verdict précis, « à porter dans la conception de la course à plusieurs générations ». La fiche et la v68 emploient encore « survit ». Non porté à la fiche : hors des corrections et hors des mots nommés par le mandat.
4. **GO-2026-11-19-94 et -95**, hors de la plage du mandat (-55 à -93) : une course de trois générations sur de nouvelles attaques est en conception, portée par ce compte. Elle peut donner un client à la version suivante de l'orchestrateur et peser sur les décisions 1 et 3 (« la prochaine course »). Non porté à la fiche.

## 7. Ce que je n'ai pas pu établir

1. Le code de l'orchestrateur n'est pas relu : ni que la vue servie par la lecture de la v68 soit celle du code v59 que nomme GO-89, ni que l'étage joué en v67 soit celui qu'appelle la v68.
2. Ce que Lazar entendait par « comme le code depuis la v59 » : je lis la lettre de la ligne et l'état des faits, non son intention.
3. Le véhicule du palier 1 de l'héritage et celui de chaque banc : toujours fixés par aucune pièce lue.
4. Les faits des dix-neuf corrections sont ceux de la contre-lecture. J'ai recoupé : les lignes 415 à 430 des dépenses, les lignes 104 et 108 du palier 0a, la ligne 53 du rang 0, la citation de GO-10-11 et GO-12-06, le § 4.4 de la v67, les 94 cartes. Je n'ai pas recoupé : le calcul « 220 à 240 dollars », les « 59 de propositions, au plus 56 de tests », le plan v5 (§ 1 et § 3.0) sur `gardee`, les constats sur le code (`MoteurReelRefuseV68`, options du lanceur).

## 8. Écarts

- Deux pièces hors de la liste du mandat ouvertes en partie (§ 2), plus GO-94 et GO-95 lus parce qu'ils sont dans le même fichier.
- La routine de reprise (R14) et la suite d'essais du dépôt n'ont pas été jouées : mandat de rédaction en lecture seule, sans passation.
- La fiche v2 n'a pas été contre-lue ; aucun compagnon `.sha256` n'est écrit pour le différentiel, le JSON et ce rapport.
- Le verdict de la fiche compte quatre points, plus que les « 1 à 3 lignes » de `CLAUDE.md`.
