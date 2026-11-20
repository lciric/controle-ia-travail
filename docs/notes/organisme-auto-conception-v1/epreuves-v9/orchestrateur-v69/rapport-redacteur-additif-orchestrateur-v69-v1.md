# Rapport du rédacteur — additif des interrupteurs de l'orchestrateur v69 et cadre de la v70 — v1

- Auteur : rédacteur neuf, modèle F. Écrit le 2026-11-20 ; relevé de `date -u` : 02:39:15Z, après la lecture des pièces et avant l'écriture des trois pièces.
- Mandat : `docs/notes/organisme-auto-conception-v1/epreuves-v9/orchestrateur-v68/mandat-redacteur-additif-orchestrateur-v69-v1.md` (`0c0efa12e9d6dac0a3569a1c69368b8eaf063cd9f0b03e2840d71ddff3479736`, compagnon vérifié), sur `GO-2026-11-20-05`.
- Processeur seul. Aucune écriture dans le dépôt, aucun commit, aucun appel à un fournisseur, aucune dépense, aucune machine, aucun lancement de l'orchestrateur, du lanceur ni de l'organisme. Je n'ai pas lu le code de l'orchestrateur ni aucun fichier du paquet v68.
- Pièces rendues, même dossier, chacune avec son compagnon `.sha256` : `additif-interrupteurs-orchestrateur-v69-v1.md` ; `cadre-lecture-registre-orchestrateur-v70-v1.md` ; ce rapport.

## 0. Verdict

1. **L'additif est écrit**, pour le seul régime « tests de mort sans rien servir » et la seule épreuve du palier 1 de l'héritage ; lecture éteinte ; rien de servi. Il est scellable après contre-lecture, sous une condition : la décision D1 (le véhicule).
2. **Véhicule retenu dans l'additif : la v69, dont l'étage est la chaîne du tour fermé, appelée sans modification dans l'enveloppe du palier 0b.** Les pièces montrent qu'aucun des deux chemins ne porte le palier 1 tel quel ; elles ne suffisent pas à trancher entre ce montage et le tour fermé seul. C'est la décision D1, posée à Lazar.
3. **Classes d'issue** : « tient », « ne tient pas », « non exécutable ou indéterminée », et le statut « non éprouvée (budget) » ; chaque « tient » porte un verdict précis parmi « identique », « portable », « dépendant de la donnée », « confiné ». Le mot « survit » ne figure dans aucun fichier écrit par la v69. Aucune classe n'est retenue pour être servie.
4. **Le cadre de la v70 est écrit** : ce que (2b) fait lire, ce que la v68 ne sait pas faire, neuf points à concevoir dans l'ordre.
5. **Trois décisions reviennent à Lazar** (§ 5). Le nom « v69 » est retiré à la course « nouvelles attaques » : son véhicule prendra un nom neuf, à fixer par ses corrections, jamais v69 ni v70 ; sa conception v3 l'écrit déjà.

## 1. Sources (chemin, empreinte, vérification)

Racine : `/home/user/controle-ia-travail`. « Dossier » : `docs/notes/organisme-auto-conception-v1/epreuves-v9/`. Chaque empreinte a été recalculée ; chaque compagnon `.sha256` vérifié par `sha256sum -c`, sauf mention.

| pièce | chemin | sha256 | lu |
|---|---|---|---|
| consignes permanentes | `CLAUDE.md` | `c9d86f7366aa0108d922f167032e2226505d6ad08ef8d5bb8e8c21416fe2768c` (pas de compagnon cherché) | reçu en tête de session |
| fiche des quatre décisions, v7 | dossier, `orchestrateur-v68/fiche-quatre-decisions-orchestrateur-v68-v7.md` | `5ddfae1887c14a950b1f05d274364930aeb50c216540ce881797f0acdb3f6bac` | en entier |
| contrôle du différentiel v6 → v7 | `orchestrateur-v68/controle-differentiel-fiche-orchestrateur-v68-v7-v1.md` | `522a3c46aa588b72cae3ff723451166337f2181c7600560e40af686a12725a09` | en entier |
| rapport du développeur de la v68 | `orchestrateur-v68/rapport-developpeur-orchestrateur-v68-v1.md` | `ad42b7229a8e37aae823b1041a3acf1db91ee4053f5fec61136b6fd178b59aa6` | en entier |
| contre-lecture de la v68 | `orchestrateur-v68/contre-lecture-orchestrateur-v68-v1.md` | `d2cfeac1a8d96a732c2cd9341aecc96a12778fff9b20ccfa0fef1edb2d47e325` | en entier |
| manifeste du paquet v68 | `orchestrateur-v68/manifeste-paquet-orchestrateur-v68-v1.json` | `4ed9fd8e893646a5e361f81a2da58099175ac2e3708555b9e7725240fedc8627` | en entier ; aucun fichier du paquet ouvert |
| plan de l'héritage, v5 | `heritage/plan-heritage-trois-bras-corrige-v5.md` | `9085bbe9b9e2c60c4e11f411aa3fe3065ee7882b45317208dc232e2b5c5f7b47` | lignes 1 à 404 sur 633 (en-tête, § 0 à § 11) ; § 12 et suivants non lus |
| devis de l'héritage, v5 | `heritage/devis-heritage-trois-bras-v5.md` | `30c87fa68d9d6fa5e961edc45764fe58172b1a1b20d45fd3065a678b42f2880d` | en entier |
| rapport du palier 0a | `heritage/palier-0a/rapport-palier-0a-v1.md` | `93d8a104ef551b931a6de84ecdaaca472cf05382ae49934c362e55d600058cd2` | en entier |
| préenregistrement du palier 0b, v6 | `heritage/palier-0b/preenregistrement-heritage-palier-0b-etage-processeur-v6.md` | `4aee136b44665339be343b26913fdec8a943a0de75368013bcc4a7dc608e5029` | section B4 et début de B5 (lignes 186 à 201) ; le reste par recherche de mots dans ce seul fichier (663 lignes) |
| ordre de passage, v3 | dossier, `ordre-de-passage-epreuves-v9-v3.md` | `b19f550b525fe5696321167bd43a35fa5ece180fd2f97dad5dfc6e970a8c0f67` | § 4 (lignes 144 à 163) et titres |
| conception « nouvelles attaques », v3 | `docs/notes/ideation-nouvelles-attaques-v1/conception-v3/ordre-course-nouvelles-attaques-v3.md` | `b12cdc1292178d4c7fe80370439507efd1d04d07f47d0bc6315b8c429d329e22` | lignes 1 à 40, et les lignes qui nomment v69, v70 et les issues |
| registre des accords, sur `main` | `registres/go.md`, `origin/main` au commit `66abffb7da1796b6924fb9f861e9ea3d3ee29398` | `4ef8b490867bbda1e77defd47abdf967b28bd8fbe101a12a3068efb4faa38f51` (copie dans mon dossier) | lignes `GO-2026-11-19-67`, `-75`, `-76`, `-77`, `-81`, `-89` ; `GO-2026-11-20-04` à `-07` |
| registre des décisions, sur `main` | `registres/decisions.md`, même commit | `fa020a3c8fd2b6aa5bc6ba39e8ae251eb67f35f41cb75e529fb122a7200ff259` (copie) | R-3209 et R-3861, en entier ; recherche des quatre mots de R-3209 dans ce seul fichier |
| état des faits des trois règles, v2 | `docs/notes/trois-regles-course-generations-v1/etat-des-faits-v2.md`, même commit | `a4c99910f716073a1b8b868f90e34a7c2e785489cfdc99aa4cd3a0e6bcfebca7` (copie ; égale à l'empreinte que cite la fiche v7) | titres, et les passages sur l'issue non concluante et sur « un bit par loi » |
| verdict de la course v67 | `docs/notes/organisme-boucle-reelle-v1/course-v67/verdict-course-v67-v1.md`, même commit | `d79024328157aafc5c801b5b0a4a621a5c009f367d88b96bbbfaeaeef3753459` (copie ; égale à l'empreinte que cite la fiche v7) | en entier |

Les quatre copies de `main` sont dans mon dossier (`main-go.md`, `main-decisions.md`, `main-etat-des-faits-v2.md`, `main-verdict-course-v67-v1.md`) ; elles ne sont pas des pièces rendues.

## 2. Le véhicule du palier 1 : ce que les pièces établissent

1. **Le mot (1a) fait écrire** la version suivante de l'orchestrateur, le lanceur version 11 et l'additif « pour ce seul régime », « pour la seule épreuve du palier 1 de l'héritage » (`GO-2026-11-20-05`). Il a été donné sur la fiche v7, dont la réserve disait : « le véhicule du palier 1 est donc à fixer avant ton mot ». Le mot ne nomme pas le véhicule.
2. **La course 2 de la v68 ne porte pas le palier 1 telle quelle.** Trois écarts, d'après les rapports : l'étage prend ses candidates dans un classement, douze au plus (rapport du palier 0a, § 3.1, point 3), alors que le palier éprouve toute tentative, sans juge (plan v5, § 3.0 ; `GO-2026-11-19-76`, point 3) ; l'engagement y est libre, sans garde contre un script qui fabrique ses lignes (rapport du palier 0a, § 3.3, manque 5), alors que Lazar impose la forme du tour fermé (`GO-2026-11-19-77`) ; l'étage sert à l'expérimentateur le préenregistrement court entier (rapport du palier 0a, § 3.2), alors qu'il doit recevoir l'engagement seul (`GO-2026-11-19-81`).
3. **Le tour fermé ne porte pas le palier 1 tel quel non plus.** Il a la forme imposée, le contre-calcul et un passé réel (course v67) ; il n'a pas de plafond sur la course (rapport du palier 0a, § 4, manque 3), il ne vérifie pas une ligne d'accord qui nomme l'interrupteur, et dans la v67 il n'éprouvait que les lois promues par le juge statistique (verdict de la v67, § 4.2).
4. **L'enveloppe du palier 0b comble l'écart côté étage** et est dite « commune aux deux usages » (préenregistrement du palier 0b, v6, B4).

**Choix du rédacteur** : la v69 garde de la v68 le régime, le montant, la garde de budget et la ligne nominative ; son étage est la chaîne du tour fermé dans l'enveloppe. Les deux mots de Lazar sont tenus, et l'étage n'est pas récrit. **Ce qui n'est pas établi** : la faisabilité sur le code (non lu), et le fait que le classement de la course 2 soit bien celui des juges. D'où D1.

## 3. Les autres choix, et leur appui

| choix | appui | statut |
|---|---|---|
| une seule génération | plan v5, § 8.4, ligne du palier 1 | pris des pièces |
| aucun juge ni aiguilleur | `GO-2026-11-19-76`, point 3 ; devis v5, § 9 | pris des pièces |
| trois classes et un statut, noms du plan | plan v5, § 3.0 ; `GO-2026-11-19-76`, point 1 | pris des pièces |
| `gardee` inchangé (oui si « tient ») | plan v5, § 1 et § 3.0 | pris des pièces |
| verdict précis attaché à chaque « tient », définitions opératoires | R-3209, point 3, pour les mots ; **définitions du rédacteur** | décision D2 |
| tranche de contrôle | **proposition du rédacteur**, pour que « dépendant de la donnée » soit calculable | décision D2 |
| plafond de course égal au montant requis, sans option | rapport du développeur de la v68, § 3 et § 8 ; **règle ajoutée par le rédacteur** (éviter une génération payée sans épreuve) | routine, à contre-lire |
| périmètre de la ligne d'accord : interrupteur, épreuve, deux empreintes | les deux premiers : R-3861 et v68 ; le troisième : **proposition du rédacteur** | routine, à contre-lire |
| durée maximale de location tenue par le lanceur | verdict de la v67, § 5 (« le plafond de 5 USD de la machine n'est tenu par aucun code ») ; **proposition du rédacteur** | routine, à contre-lire |
| essai du bac en quatre points, sans appel | `GO-2026-11-20-05`, 4b ; rapport du développeur de la v68, § 9, point 5 ; rapport du palier 0a, essais E1 et E5 et écart 3 | pris des pièces |

## 4. Ce qui reste ouvert

1. **Le sens des quatre mots de R-3209 et la correction qu'elle vise.** R-3209 les donne entre guillemets, sans définition ; je les ai cherchés dans `registres/decisions.md` (une seule occurrence : R-3209), dans l'état des faits des trois règles et dans l'ordre v3 (aucune). La fiche v7 lit ce point comme portant sur les tests de mort de l'étage ; je la suis. Si une pièce que je n'ai pas lue les définit, l'additif est à corriger avant scellement.
2. **Trois points à confirmer sur le code** par le développeur : d'où la course 2 tire ses candidates ; l'appel de la chaîne du tour fermé depuis la v69 sans modification ; ce que l'étage sert au lecteur témoin.
3. **Les livrables du palier 0b** (monde planté de l'héritage, comparateur sans juge, enveloppe) : la v69 en dépend ; je ne sais pas où ils en sont.
4. **Le plan v5, § 12 et § 13** (questions et réserves), non lus : la question 8 (expérimentateur et lecteur témoin) est connue par le devis v5, § 9, et par les lignes d'accord.
5. **Le préenregistrement court et le devis du palier 1** n'existent pas encore ; l'additif nomme ce qu'ils doivent geler (plafonds, proportions des tranches, durée de location).
6. **Lecture du registre (v70)** : le point 7 du palier 0b peut encore changer ce qui est servi (D3).

## 5. Décisions pour Lazar

### D1 — le véhicule du palier 1

- **Décision.** Le palier 1 de l'héritage se joue-t-il par la v69 dont l'étage est la chaîne du tour fermé ?
- **Enjeu.** Ton mot (1a) fait écrire la v69 pour ce palier ; la fiche v7 te disait que le tour fermé sait le jouer sans elle. Le chemin choisi fixe ce que ta ligne d'accord nommera, et ce qui est éprouvé en réel pour la première fois.
- **Options.**
  - (a) La v69 porte le palier ; son étage est la chaîne du tour fermé, dans l'enveloppe du palier 0b. Avantage : forme imposée et contre-calcul, déjà joués en réel ; plafond de course et ligne nominative ; ton mot (1a) tenu à la lettre. Inconvénient : un montage neuf, dont la faisabilité n'est pas vérifiée sur le code.
  - (b) Le tour fermé seul, avec l'enveloppe, sans la v69. Avantage : le chemin de la course v67, le moins de code neuf. Inconvénient : pas de plafond sur la course ni de ligne qui nomme l'interrupteur ; la v69 et le lanceur version 11 ne servent pas au palier que ton mot leur donne ; il faut nommer une autre première épreuve pour l'interrupteur.
  - (c) La course 2 étendue : la v69 apprend à éprouver toute tentative sans juge, la forme imposée et le contre-calcul. Avantage : un seul chemin pour les lignes suivantes de l'ordre v3. Inconvénient : récrit ce que le tour fermé fait déjà ; le plus de code neuf avant la première dépense.
- **Recommandation.** (a), confiance 0,6. Je passerais à (b) si le développeur trouve que la v69 ne peut pas appeler la chaîne sans la modifier.
- **Défaut sous 48 heures.** Aucun pour le choix du chemin réel : il fixe un allumage. Sans ton mot, la v69, le lanceur version 11 et l'additif s'écrivent en routine selon (a), éteints, comme (1a) le permet ; rien n'est scellé ni allumé.

### D2 — le sens des quatre verdicts précis, et ce qui est retenu

- **Décision.** Les définitions du § 4.3 de l'additif (et la tranche de contrôle du § 4.4) sont-elles celles que tu veux pour « identique », « portable », « dépendant de la donnée », « confiné » ?
- **Enjeu.** R-3209 donne les mots, pas leur sens ; l'additif scellé les fixerait pour la première épreuve réelle. Rien n'est servi sous (1a) : l'enjeu est ce qu'écrivent le bilan et la sélection scellée, et ce dont héritera la v70.
- **Options.**
  - (a) Mes définitions : le verdict précis dit ce que le recalcul hors du bac retrouve (à l'octet ; au même côté du seuil ; pas sur une seconde tranche ; pas du tout). Toute « tient » reste gardée ; le verdict précis est écrit à côté. Avantage : calculable par programme, sans appel, sur la forme imposée ; ne touche pas `gardee`. Inconvénient : c'est ma lecture de tes mots ; elle ajoute une tranche de contrôle au palier 1.
  - (b) Tu donnes, ou la mère retrouve, la définition d'origine ; l'additif attend. Avantage : aucun sens inventé. Inconvénient : l'additif ne se scelle pas avant.
  - (c) Les trois classes seules pour la v69, sans verdict précis ; le mot « survit » disparaît quand même. Avantage : le plus simple, rien d'inventé. Inconvénient : R-3209 demande un verdict précis ; ce serait le reporter.
- **Recommandation.** (a), confiance 0,5 ; (b) si la source existe.
- **Défaut sous 48 heures.** (a) : rien n'est servi ni dépensé par ce choix, et l'additif reste révisable par un additif neuf avant l'allumage.

### D3 — la v70 attend-elle le point 7 du palier 0b ?

- **Décision.** Ton mot (2b) clôt-il la réserve « à revoir au point 7 du palier 0b » de `GO-2026-11-19-76`, point 2, sur le service de `resultat` et de `gardee` ?
- **Enjeu.** (2b) dit que la génération suivante lit toutes les tentatives et leur classe d'issue ; la ligne 76 gardait un repli (registre servi sans ces deux champs) selon ce que montrerait le lecteur scripté. Ce qui est servi à un agent est ton nœud.
- **Options.**
  - (a) La réserve tient : la v70 se conçoit maintenant avec les deux formes (avec et sans ces champs), et le point 7 choisit. Avantage : aucun mot de toi n'est effacé ; la conception n'attend pas. Inconvénient : deux formes à garder et à éprouver.
  - (b) (2b) clôt la réserve : la classe d'issue est servie, quoi que dise le point 7. Avantage : une seule forme. Inconvénient : écarte un repli que tu avais gardé, avant sa mesure.
- **Recommandation.** (a), confiance 0,65.
- **Défaut sous 48 heures.** (a) pour la conception, qui est de la routine. Aucun défaut pour l'allumage de la lecture : rien n'est servi sans ton mot.

### Rappel, sans décision neuve

L'allumage réel du régime de la v69 reste soumis au devis du palier 1 et à une ligne d'accord de calcul qui nomme `tests_de_mort_reels` et porte le montant au pire. Aucun défaut : c'est une dépense.

## 6. Écarts et refus

1. **Aucun refus d'outil ni de classifieur.**
2. **Quatre commandes mal formées, sans effet sur le dépôt.** Pour copier quatre fichiers de `main`, j'ai d'abord passé `--output=` à `git show`, qui ne redirige pas son contenu : les fichiers sont sortis à l'écran, et l'outil a rangé de lui-même trois de ces sorties, trop longues, dans des fichiers sous `/root/.claude/`. Je n'y ai rien écrit moi-même et je ne les ai pas relus. J'ai refait les quatre copies par redirection vers mon dossier, comme le mandat le dit.
3. **Recherches de mots** : faites dans des fichiers nommés par leur chemin complet, jamais sur un dossier ; quatre par `grep` sur un seul fichier de mon dossier, les autres par l'outil de recherche sur un seul fichier.
4. **Lectures partielles** : dites au § 1 (plan v5, préenregistrement du palier 0b, ordre v3, état des faits, conception « nouvelles attaques »).
5. **Une pièce hors de la liste du mandat a été lue** : la conception v3 de la course « nouvelles attaques », sur la consigne reçue avec le mandat, pour vérifier que l'additif ne lui prend rien. Constat : elle nomme déjà son véhicule « sous un nom neuf, jamais 69 ni 70 », et ses issues d'aiguillage (« passée », « au coffre », « hors case ») ne sont pas reprises ici.
6. Aucun identifiant de modèle n'est écrit dans les trois pièces. Aucun chiffre de dépense n'y est gelé ; ceux qui sont cités portent leur chemin et leur empreinte.
