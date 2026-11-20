# Contre-lecture — additif des interrupteurs de l'orchestrateur v69, cadre de la v70 et rapport du rédacteur — v1

- Contre-lecteur, modèle O. Neuf : je n'ai écrit ni le mandat du rédacteur, ni ses pièces, ni le code de la v68. Écrit le 2026-11-20, relevé de `date -u` : 02:54:31Z, après les lectures.
- Mandat : `docs/notes/organisme-auto-conception-v1/epreuves-v9/orchestrateur-v69/mandat-contre-lecteur-additif-orchestrateur-v69-v1.md` (`3c4ecfc38f8d7938b8495458d244a54879547c712029f6fdb8be108fae33bd8a`, compagnon vérifié par `sha256sum -c`).
- Processeur seul, lecture seule : aucune écriture dans le dépôt, aucun commit, aucun lancement, aucun appel à un fournisseur, aucune dépense. **Aucun refus d'outil ni de classifieur.**

## Verdict

**Conforme après corrections.** Onze corrections, listées au § 4 avec texte ancien et nouveau ; aucune ne change le régime, les classes du plan, ni une décision posée à Lazar. Le régime (1a) seul est porté, la lecture reste éteinte, rien n'est servi, aucun défaut ne tombe sur un allumage ou une dépense. Le véhicule (D1) n'est **pas établi sur le code** : le dépôt de l'orchestrateur est absent de cette session ; ce que le paquet v68 montre est au § 2.

## 1. Pièces vérifiées (empreinte recalculée, compagnon `.sha256` vérifié)

| pièce | sha256 | lu |
|---|---|---|
| `V69/additif-interrupteurs-orchestrateur-v69-v1.md` | `aef8ff2f8eb3597c8405c765c3432ce791a34ab65b851a75ac223de875fbe158` | en entier |
| `V69/cadre-lecture-registre-orchestrateur-v70-v1.md` | `84651a4c658e88f0bca7d299746ae05c267ae7f9f2002d8371dd19fccef4a5ee` | en entier |
| `V69/rapport-redacteur-additif-orchestrateur-v69-v1.md` | `b97cbd188cf1cb2d7ccc252990bff19655a4799db4cc625023d1c3b52870a707` | en entier |
| mandat du rédacteur (`orchestrateur-v68/…`) | `0c0efa12e9d6dac0a3569a1c69368b8eaf063cd9f0b03e2840d71ddff3479736` | en entier |
| manifeste du paquet v68 | `4ed9fd8e893646a5e361f81a2da58099175ac2e3708555b9e7725240fedc8627` | en entier |
| rapport du développeur de la v68 | `ad42b7229a8e37aae823b1041a3acf1db91ee4053f5fec61136b6fd178b59aa6` | en entier |
| contre-lecture de la v68 | `d2cfeac1a8d96a732c2cd9341aecc96a12778fff9b20ccfa0fef1edb2d47e325` | en entier |
| fiche v7 | `5ddfae1887c14a950b1f05d274364930aeb50c216540ce881797f0acdb3f6bac` | décision 1 et réserves (lignes 42, 52, 131, 153-155) |
| rapport du palier 0a | `93d8a104ef551b931a6de84ecdaaca472cf05382ae49934c362e55d600058cd2` | en entier ; son manifeste d'essai en entier |
| plan v5 | `9085bbe9b9e2c60c4e11f411aa3fe3065ee7882b45317208dc232e2b5c5f7b47` | § 1 (l. 48-49), § 3.0 (l. 113-130), § 8.4 (l. 354-366), recherches |
| devis v5 | `30c87fa68d9d6fa5e961edc45764fe58172b1a1b20d45fd3065a678b42f2880d` | titres, § 5 (l. 163), § 12 |
| préenregistrement du palier 0b, v6 | `4aee136b44665339be343b26913fdec8a943a0de75368013bcc4a7dc608e5029` | B4 et début de B5 (l. 186-201) |
| ordre v3 ; conception « nouvelles attaques » v3 | `b19f550b…0c0f67` ; `b12cdc12…29d329e22` | empreintes seulement |
| les huit fichiers du paquet v68 | égaux au manifeste, un par un | `course2_v68.py`, `ideation_v68.py`, `configuration_v68.py`, `budget_course_v68.py`, `simulation_v68.py` en entier ; `test_v68_course2.py` l. 625-664 et recherches |
| sur `main` (`origin/main` local, `732d7337…`, sans récupération) : `registres/go.md` | `4ef8b490…` (égale à celle du rédacteur) | GO-2026-11-19-67, -75, -76, -77, -81, -89 ; GO-2026-11-20-05 à -07 |
| `registres/decisions.md` | `edd6ea97…` (`main` a avancé depuis la copie du rédacteur ; R-3209 et R-3861 relus à l'identique) | R-3209, R-3861 ; recherche des quatre mots |
| état des faits v2 ; verdict de la course v67 | `a4c99910…` ; `d7902432…` (égales à celles du rédacteur) | recherches ; § 4.4 et § 5 du verdict |

**Ce que je n'ai pas pu lire.** L'orchestrateur `/home/user/ideation-organism` n'existe pas dans cette session (`git -C` : « No such file or directory »). La chaîne du tour fermé (`pole/tour_ferme_v64.py`, `etage_entre_generations_v53/v57.py`, `tests_de_mort_v5.py`), `course2_v56.py`, `noyau_v56.py`, `configuration_v56.py` et le lanceur v8 sont donc hors de ma lecture. Je n'ai rattaché aucun dépôt : son adresse n'est dans aucune pièce, et le deviner n'est pas permis.

## 2. Ce que le code confirme ou infirme du véhicule (D1)

| point « à confirmer sur le code » | statut | appui (fichier du paquet v68, ligne) |
|---|---|---|
| 1. La course 2 tire ses candidates du classement des juges | **confirmé pour la v68**, sous une réserve | `course2_v68.py` l. 332 (`resultat = gen.executer()`, génération `GenerationV56`), l. 336 (`notables` compté sur `resultat`), l. 349 (`preparer_generation(…, resultat, gen.fiches, nombre=etage["nombre"], …)`), en-tête l. 12-13 (« classement des juges de la v56 ») ; la doublure de l'étage prend les `nombre` premières lignes éligibles de `classement.json` (`test_v68_course2.py` l. 634-637). Réserve : la fabrication du rang par les juges (`course2_v56`, `noyau_v56`) n'est pas relue ici. |
| 2. La v69 peut appeler la chaîne du tour fermé sans la modifier | **non établi** (fichier absent) ; un indice pour, trois points contre à trancher | Pour : la v68 appelle déjà, sans les modifier, les deux maillons du bas de la chaîne (`preparer_generation` v53 et `jouer_etage_v57`, l. 300-302 et 349-353). Contre, à trancher sur `tour_ferme_v64.py` : (i) le rapport du palier 0a (§ 4, manque 3) dit que le tour fermé ne passe pas `plafond_total_usd` à l'étage, que la garde 6 et `verifier_etage_v68` (l. 262-281) exigent ; (ii) le filtre « lois promues » de la v67 peut vivre dans `jouer_etage` ou chez son appelant ; (iii) le lanceur v68 ne construit les réglages de l'étage qu'en simulé (`ideation_v68.py` l. 152) ; le mode réel de l'étage du tour fermé passe par `demonstrations/tour_ferme_v64.py` (`moteur_de_l_etage`, verdict de la v67, § 4.4), un fichier de lanceur, pas de la chaîne ; (iv) le classement exigé porte `lisible_L2_L4` (rapport du palier 0a, § 3.1, point 3), dont le sens sans juge n'est pas établi. |
| 3. Ce que l'étage sert au lecteur témoin | **non établi** (`tests_de_mort_v5.py` absent) ; indice | La doublure du lecteur (`simulation_v68.py` l. 53-64) lit dans sa consigne la section du préenregistrement court de l'étage (`TITRE_SECTION_PREREG`) et la « Sortie scellée des exécutions » : le lecteur reçoit au moins la même projection que l'expérimentateur, et la garde 9 doit le couvrir. |

Autres constats sur le code, qui portent sur l'additif :

- `selection.servie_a_la_suivante: false` et `heritage_servi_a_la_suivante: null` en régime « tests de mort sans rien servir » : **confirmé** (`course2_v68.py` l. 361-370).
- Montant requis N × S17 + E × plafond de l'étage, N = E = 1 : **confirmé** (`configuration_v68.py` l. 62), **pour la portée « par_generation » seulement** ; la portée « course » est refusée dès un étage (l. 53-58). L'additif ne le dit pas (correction 9).
- La v68 recopie le résumé brut de l'étage dans `bilan-course.json` (`course2_v68.py` l. 357, puis l. 376-378) ; ce résumé porte le mot « survit » par fiche (`test_v68_course2.py` l. 635-636). Tenue telle quelle, la v69 violerait sa propre garde 15 (correction 8).
- Sans `--course-2`, la main passe au lanceur v8 (`ideation_v68.py` l. 165-166 ; contre-lecture de la v68, constat 7) : l'artefact de la garde 2 qui attend `MoteurReelRefuseV69` pour cet appel est faux (correction 4).
- La vérification nominative de la v68 exige seulement que chaque interrupteur allumé figure dans le périmètre (`ideation_v68.py` l. 93-97) ; une ligne qui nomme aussi l'interrupteur de lecture passe (correction 10).

**Conséquence pour D1** : la recommandation (a) reste défendable, mais sa faisabilité tient aux quatre réponses du point 2 ; je propose (correction 1) que le seuil de bascule vers (b) soit « une seule de ces quatre réponses contraire ». Une voie que les pièces ne nomment pas mérite d'être dite au développeur : appeler directement `preparer_generation` et `jouer_etage_v57`, comme la v68, et prendre au tour fermé ses seules fonctions de forme imposée et de contre-calcul, si elles sont séparées (le rapport du palier 0a, § 2, les situe dans `tour_ferme_v64.py` l. 440-530 et 787-906). C'est une variante de (a), pas une option neuve ; je ne la recommande pas sans lecture du code.

## 3. Constats par point du mandat

1. **Régime (1a) seul ; noms** : conforme. Un seul régime, une seule épreuve, lecture éteinte, tout autre régime refusé (C3) ; v69, v70, lanceur version 11 justes ; « nouvelles attaques » non concernée (additif § 8 ; cadre § 5 ; rapport § 0, point 5).
2. **Véhicule** : voir § 2. Le rédacteur le dit lui-même non établi et pose D1 ; c'est juste. Le relevé des points à confirmer est incomplet (corrections 1 et 2).
3. **Classes d'issue** : les trois classes et le statut sont ceux du plan v5, § 3.0 (l. 125-127) et § 1 (l. 48-49), à la lettre. Les définitions des quatre verdicts précis sont déclarées du rédacteur (additif § 4.3 ; réserve 2) et posées à Lazar (D2) sans être prises pour acquises : conforme. Deux défauts : la catégorie « refusée avant l'épreuve » n'est rattachée ni à `resultat`, ni à `gardee`, ni au dénominateur de la règle de passage (correction 5) ; la ligne 1 « confiné » se lit comme un rapport sans arrêt, alors qu'elle signale un engagement non couvert par le contre-calcul (correction 6). La tranche de contrôle a un effet écrit (réserve 3 : un tirage de plus) mais ni son coût, ni son effet sur la part servie et sur la puissance du test (correction 7). Je n'ai pas non plus trouvé la définition d'origine des quatre mots (une seule occurrence dans `registres/decisions.md` sur `main`) ; une piste pour la mère : l'état des faits v2 (l. 9 et 19) tient la règle 3, « cache entre exécutions », pour une correction du bac non mesurée ; « la correction » de R-3209, point 3, pourrait la viser. Non établi.
4. **Expérimentateur** : engagement seul, forme imposée, conforme à `GO-2026-11-19-81` (B (a)) et `GO-2026-11-19-77` (décision 3), et à la liste (iv) du palier 0b v6, B4.
5. **Conditions, gardes, lanceur, règles ajoutées** : justes pour l'essentiel ; aucune ne vise un signe (R3) ; les chiffres cités portent chemin et empreinte au rapport, § 1 (R6). Défauts : ordre de vérification de la condition 8 contre C2 (correction 3) ; C4 contre C5 en simulé (correction 2) ; artefact de la garde 2 (correction 4) ; garde 4 (correction 10) ; portée du budget (correction 9). Les trois règles ajoutées (plafond de course sans option, troisième point du périmètre, durée de location) sont déclarées, justifiées, et vont dans le sens d'une moindre dépense : conformes.
6. **Cadre v70** : dit justement ce que (2b) fait lire, sans tri ni verdict de juge (`GO-2026-11-19-89`) ; le tableau du § 2 est juste sur le code (lecture sans étage refusée, `course2_v68.py` l. 235-237). D3 est juste au regard de `GO-2026-11-19-76`, point 2 (« à revoir au point 7 du palier 0b ») : (2b) nomme la classe d'issue, pas `gardee`, et ne dit pas lever la réserve. Précision facultative : au § 3, point 3, la liste de la garde A4 est une valeur de configuration (`conf["etiquettes_interdites"]`, `course2_v68.py` l. 246) ; les cinq mots cités sont ceux des essais (`test_v68_course2.py` l. 505).
7. **Décisions** : D1, D2, D3 au format ; aucun défaut sur un allumage ni une dépense (D1 : aucun pour le chemin réel ; « Rappel » : aucun). Remarque sans correction : le défaut (a) de D2 fixe le sens de mots de Lazar ; il reste couvert, puisque la ligne d'accord de l'allumage porte l'empreinte de l'additif scellé (§ 5.1, point 3).
8. **Identifiants de modèle** : aucun dans les trois pièces (recherche faite sur chacune).

## 4. Corrections (texte ancien → texte nouveau), à appliquer par un rédacteur de modèle F

**1. Additif, § 9, réserve 1** (et, à l'identique en substance, rapport § 2 « Ce qui n'est pas établi » et § 4, point 2 ; D1, recommandation : « si le développeur trouve que la v69 ne peut pas appeler la chaîne sans la modifier » devient « si une seule des réponses (b1) à (b4) de l'additif, § 9, réserve 1, est contraire »).
- Ancien : « 1. **Code non lu.** Trois points au moins sont à confirmer sur le code : que la course 2 tire ses candidates du classement des juges ; que la v69 peut appeler la chaîne du tour fermé sans la modifier ; ce que l'étage sert au lecteur témoin. »
- Nouveau : « 1. **Code non lu par le rédacteur ; la contre-lecture n'a lu que le paquet v68.** (a) La course 2 tire ses candidates du classement de la génération : confirmé sur la v68 (`course2_v68.py` l. 332, 336, 349 ; en-tête l. 12-13) ; la fabrication du rang par les juges (`course2_v56`, `noyau_v56`) n'est pas relue. (b) La v69 peut appeler la chaîne du tour fermé sans la modifier : non établi ; le développeur le tranche sur `pole/tour_ferme_v64.py` en quatre réponses : (b1) où vit le filtre des lois promues de la course v67 (dans `jouer_etage` ou chez son appelant) ; (b2) si `jouer_etage` prend de l'appelant des réglages qui portent `plafond_total_usd` et `plafond_externe_usd` (le rapport du palier 0a, § 4, manque 3, dit que le tour fermé ne passe pas `plafond_total_usd` ; la garde 6 et `verifier_etage_v68`, `course2_v68.py` l. 262-281, l'exigent) ; (b3) quel adaptateur réel de l'étage la v69 emploie (le lanceur v68 ne construit les réglages de l'étage qu'en simulé, `ideation_v68.py` l. 152 ; le mode réel de l'étage du tour fermé passe par `demonstrations/tour_ferme_v64.py`, `moteur_de_l_etage`, verdict de la v67, § 4.4) ; (b4) ce qu'atteste le champ `lisible_L2_L4` du classement que l'étage exige (rapport du palier 0a, § 3.1, point 3), et si l'enveloppe peut l'écrire sans juge. Une seule réponse contraire : le développeur s'arrête, et D1 revient à Lazar avec l'option (b). (c) Ce que l'étage sert au lecteur témoin : non établi ; d'après la doublure de la v68 (`simulation_v68.py` l. 53-64), sa consigne porte au moins la section du préenregistrement court de l'étage et la « Sortie scellée des exécutions » ; la garde 9 le couvre sur la même projection. »

**2. Additif, § 2, ligne C4.**
- Ancien : « | C4 | **En moteur simulé, rien ne change** : les régimes de la v68 se jouent comme dans la v68 | sorties d'une course simulée égales à celles de la v68, au bruit d'horloge et de chemin près (témoin de bruit comme à la contre-lecture de la v68, constat 4) | »
- Nouveau : « | C4 | **En moteur simulé, les régimes de la v68 autres que celui du palier 1 se jouent comme dans la v68.** Le régime du palier 1 se joue en simulé par le chemin du § 1.2 (même code qu'en réel, moteur simulé) ; c'est sur ce chemin que les vingt gardes du § 6 sont éprouvées | sorties simulées des autres régimes égales à celles de la v68, au bruit d'horloge et de chemin près (témoin de bruit comme à la contre-lecture de la v68, constat 4) | »

**3. Additif, § 2.1, condition 8, et § 2, ligne C2.**
- Ancien (condition 8) : « 8. La machine est déclarée jetable (liste blanche de noms, comme la v56), et l'attestation de l'essai du bac à sable du § 5.4 est présente, scellée, réussie, faite sur cette machine et pendant ce lancement. »
- Nouveau : « 8. La machine est déclarée jetable (liste blanche de noms, comme la v56), ce qui se vérifie avant toute écriture. Puis l'essai du bac à sable du § 5.4 est la première étape du lancement ; il n'écrit que son attestation, dans le dossier de sortie ; l'attestation doit être présente, scellée, réussie, faite sur cette machine et pendant ce lancement, avant tout appel payant. Les conditions 1 à 7 et 9 et la déclaration de la machine se vérifient avant toute écriture ; l'attestation, après l'essai et avant tout appel payant. »
- Ancien (C2) : « sinon `MoteurReelRefuseV69` liste celles qui manquent, et rien n'est écrit »
- Nouveau : « sinon `MoteurReelRefuseV69` liste celles qui manquent, et rien n'est écrit (pour la condition 8 : rien d'autre que l'attestation de l'essai et le relevé partiel du § 6) »

**4. Additif, § 6, garde 2, colonne « artefact ».**
- Ancien : « appel sans `--course-2` : `MoteurReelRefuseV69`, aucune sortie »
- Nouveau : « appel sans `--course-2` : la main passe au lanceur v8 inchangé (`ideation_v68.py` l. 165-166 ; contre-lecture de la v68, constat 7) ; l'essai montre qu'aucun chemin du lanceur v8 n'atteint la chaîne de la v69 ni n'allume `tests_de_mort_reels`, et le lanceur version 11 refuse lui-même tout appel sans `--course-2` (§ 7, point 5) »

**5. Additif, § 4.2, dernier alinéa** (et § 4.5, quatrième point : « des refus avant l'épreuve » devient « des refus avant l'épreuve, comptés aussi dans « non exécutable ou indéterminée » »).
- Ancien : « Une tentative refusée avant l'étage (loi hors de la grammaire, bloc de statistique absent) est comptée à part, « refusée avant l'épreuve », avec son motif ; elle n'est jamais éprouvée sur un chiffre que le script imprime (plan v5, § 3.0). »
- Nouveau : « Une tentative refusée avant l'étage (loi hors de la grammaire, bloc de statistique absent) n'est jamais éprouvée sur un chiffre que le script imprime (plan v5, § 3.0). Son `resultat` est la classe « non exécutable ou indéterminée », avec le motif « refusée avant l'épreuve » écrit à côté et compté à part ; `gardee` vaut non ; elle reste au dénominateur « des tentatives » de la règle de passage du palier 1 (plan v5, § 8.4). Le plan ne nomme pas sa classe : cette lecture est du rédacteur, posée avec D2. »

**6. Additif, § 4.3, ligne 1 de la règle et alinéa qui suit la table.**
- Ancien (ligne 1, colonne « verdict précis ») : « **« confiné »** : l'issue n'existe que dans le bac »
- Nouveau : « aucun verdict : **arrêt** (garde 10 en défaut), aucune issue lue ; « confiné » n'est attribuable à aucune tentative sous la forme imposée »
- Ancien (alinéa) : « Sous la forme imposée, la ligne 1 ne doit jamais s'appliquer : un compte non nul de « confiné » est rapporté comme un défaut de la projection, sans arrêt. »
- Nouveau : « Sous la forme imposée, la ligne 1 ne s'applique que si la garde 10 a laissé passer un engagement hors de la forme : un tel « tient » n'a pas de contre-calcul (garde 11), donc aucune garde contre un script qui fabrique ses lignes (rapport du palier 0a, essai E2). C'est un arrêt, non un verdict. Le bilan écrit en tête « « confiné » non attribuable sous la forme imposée » ; les verdicts possibles à ce palier sont « identique », « portable » et « dépendant de la donnée ». »

**7. Additif, § 4.4, après « Sa proportion se gèle au préenregistrement court du palier 1. »** (ajout).
- Nouveau : « **Coût et effet.** Coût : aucun appel, aucun dollar ; un calcul sur processeur par « tient ». Effet : la tranche est prise sur le jeu d'évolution ; à taille de monde égale, elle réduit la part servie ou la tranche d'épreuve, donc ce que voient les proposeurs ou la puissance du test de mort, et par là la répartition des classes que lit la règle de passage. Proposition du rédacteur : la part servie et la tranche d'épreuve gardent les tailles du plan (v5, § 3.0) et la tranche de contrôle s'y ajoute par un tirage de plus ; le préenregistrement court gèle les trois tailles. »

**8. Additif, § 4.1, second point** (ajout à la fin).
- Ancien : « - **Tout fichier que la v69 écrit** (bilan, relevé, journal, registre, sélection de la course) porte les classes ci-dessous, jamais le mot « survit » (garde 15). »
- Nouveau : « - **Tout fichier que la v69 écrit** (bilan, relevé, journal, registre, sélection de la course) porte les classes ci-dessous, jamais le mot « survit » (garde 15). La v68 recopie le résumé brut de l'étage dans le bilan de la course (`course2_v68.py` l. 357), et ce résumé porte le mot du noyau par fiche (`test_v68_course2.py` l. 635-636) : la v69 n'y écrit que la projection en classes ; le résumé brut reste un fichier de l'étage, scellé, nommé dans le bilan par son empreinte. »

**9. Additif, § 5.2, premier point** (ajout à la fin).
- Nouveau : « Cette formule vaut pour la portée « par_generation » : la v68 refuse la portée « course » dès qu'un étage est joué (`configuration_v68.py` l. 53-58). La configuration du palier 1 porte `budget.portee_plafond: par_generation`. »

**10. Additif, § 5.1 et § 6, garde 4.**
- Ancien (§ 5.1) : « Une ligne qui nomme un autre interrupteur, ou aucun, est refusée. »
- Nouveau : « Une ligne qui ne nomme pas `tests_de_mort_reels`, ou qui nomme aussi `lecture_selection_generation_suivante`, est refusée : la vérification de la v68 n'exige que la présence de l'interrupteur allumé (`ideation_v68.py` l. 93-97) ; la v69 refuse en plus une ligne qui nomme l'interrupteur de lecture. »
- Ancien (garde 4, artefact) : « périmètre qui nomme l'autre interrupteur ; »
- Nouveau : « périmètre qui nomme `lecture_selection_generation_suivante` au lieu de `tests_de_mort_reels` ; périmètre qui nomme les deux ; »

**11. Additif, § 4.2, phrase d'introduction** (exactitude de la source).
- Ancien : « Noms et définitions du plan de l'héritage (plan v5, § 3.0), sur lesquels porte la décision `GO-2026-11-19-76`, point 1 : »
- Nouveau : « Noms et définitions du plan de l'héritage (plan v5, § 3.0, ligne « passage aux trois classes ») ; `GO-2026-11-19-76`, point 1, retient la voie (b) de ce paragraphe, qui porte ces classes : »

## 5. Écarts

1. Dépôt de l'orchestrateur absent de la session : la chaîne du tour fermé n'est pas lue (§ 1). Je n'ai pas cherché de copie ailleurs (commandes de liste interdites).
2. `main` lu sur `origin/main` local (`732d7337…`), sans `git fetch` ; `registres/go.md` y a l'empreinte que le rédacteur avait relevée.
3. Recherches de mots faites par l'outil de recherche sur des fichiers nommés un par un, jamais sur un dossier. Copies de `main` (quatre fichiers) dans mon dossier ; elles ne sont pas des pièces rendues.

— contre-lecteur, modèle O
