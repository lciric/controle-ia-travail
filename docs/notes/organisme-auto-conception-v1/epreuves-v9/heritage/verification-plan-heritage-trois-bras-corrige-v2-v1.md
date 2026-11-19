# Vérification de la version 2 du plan à trois bras corrigé de l'héritage et de son devis — v1

## En-tête

- **Vérificateur** : modèle O, auteur de la contre-lecture de la v1 (`contre-lecture-plan-heritage-trois-bras-corrige-v1-v1.md`, `124767e4724bb125801b31df03c7021cc5cef1701349bdfa12c174fc8c3013da`), relue en entier pour cette vérification ; il n'a écrit ni le plan, ni le devis, ni leur programme de calcul. Rédacteur des pièces vérifiées : modèle F.
- **Heures** (`date -u`) : début de lecture 2026-11-19T13:39:08Z ; début d'écriture 2026-11-19T13:43:37Z.
- **Commits lus** : branche `lot/compte-organisme-v1` à `cbeca14cab52e64f38271b8db4a1b19da92efb3a` (tête locale égale à la tête distante) ; `main` lu à `2e4194cb85ea1c506def6fd95b94e71248765fd1`.
- **Empreintes vérifiées contre leur compagnon `.sha256`** (toutes conformes ; les pièces de la v1 et la contre-lecture aussi, intactes, règle R12) :
  - `plan-heritage-trois-bras-corrige-v2.md` : `ae819696380f40785fff1ab6012c63054129042e84d760011d6dba25f179ac87` ;
  - `devis-heritage-trois-bras-v2.md` : `988da4d18bc1c126f6b5daa694e593b10200e1a38c9e7c57697d329f962b84b3` ;
  - `calcul_devis_heritage_v2.py` : `5d21b393f03f3e859241d97dea8347937596422c42f6b9f3cc4e5f5661b1a1c9` ;
  - `calcul-devis-heritage-v2.json` : `132a07649dd6d572ad50e5bc6c41a73fee9d54a8bcceef996192fb886b1dca6b`.
- **Rejeu** : le programme v2, copié dans un dossier de travail hors du dépôt et joué deux fois (`python3 -I -B`), rend deux sorties identiques à l'octet à la sortie versée. Recalculés à la main ou par programme : les colonnes unilatérales et bilatérales des rangs signés exacts à 5, 6, 7, 8, 10, 12 et 16 sources (dont, à 10 sources, 43 sous-ensembles de somme au plus 10 sur 1 024, soit 0,042, et 54 de somme au plus 11, soit 0,053) ; les facteurs de borne haute de l'écart-type (2,92 ; 1,92 ; 1,65 ; 1,52) ; la table des appels perdus (§ 2 bis du devis) ; les 349 et 480 générations de bras, la décomposition 180 → 349 du § 7 du devis, et tous les totaux des § 0, 4, 6 et 8 du devis.
- **Empreintes des sources citées par la v2, recalculées sur le contenu lu** : toutes conformes — contre-lecture v1, plan v1, devis v1 ; sur `main` : N-058 (`854f2724…`), complément 3 de N-073 (`4ca0ce7b…`), N-067 (`966dd9dc…`), N-071 (`9700fe6f…`), proposition (`a2cd45ad…`), critères (`8881dbb2…`), lecture descriptive (`0306adf7…`), erratum 1 (`9a771600…`), plan d'origine (`95684255…`), vérification courte (`98d1152f…`) ; sur la branche : manifeste de fin du lanceur de la course v9 (`28bc36df…`). Organisme, en lecture seule, commit `a41b7b50f7c64ce488c120bb89ad3d25fb1dd1cb` : `tests_de_mort_v5.py` (`da524871…`) et `tests_de_mort_v4.py` (`35912a3a…`), conformes aux empreintes du plan.
- **Autres lectures** : `registres/go.md` sur `main` (`d111766a4e4ae0637399b543117c07a47f433f6978a7fd1a9bba55a7987e63f7`), lignes 55 à 60 ; erratum 1, en entier ; N-067, section 6 ; listes « Ne pas écrire » du complément 3 et du point 4 du complément 2, liste « Ne plus écrire » de N-073, § 1 ; **en-tête seul** de `tests_de_mort_v5.py`, et en-tête et constantes nommées de `tests_de_mort_v4.py` (liste des statistiques, ordre des trois verdicts, refus d'un fichier pris dans la tranche).
- **Cartes** : aucune rouverte. La v2 n'en touche que la lettre de la correction 12, et la contre-lecture les avait vérifiées carte par carte.
- **Non lus** : le corps du code de l'organisme, de l'oracle et du générateur ; tout dossier interdit par le mandat.
- **Recherche « Ne pas écrire » refaite** sur les deux textes de la v2, par un programme à moi, hors du dépôt parce qu'il contient les formules (45 motifs de formules, 13 motifs d'identifiants de modèle), puis relecture des occurrences.
- Aucun appel à un fournisseur de modèles, aucune dépense, aucun refus d'outil.

## Table des dix-sept corrections

| n° | gravité | correction demandée | appliquée | où, et remarque |
|---|---|---|---|---|
| 1 | B | § 3.0 « épreuve programmée » (entrée, données, statistique, seuil, classes, exécutant) ; choix entre les voies (a), (b) et (c) ; invariant étendu ; « troisième voie » | **oui** | § 3.0 entier, § 3.1, § 4.2, § 10, § 11, § 12 (question 1), § 13 (réserves 1 et 3). Voie (b), les tests de mort, avec sa raison et son prix ; changement de l'organisme déclaré (§ 2, règle 3). Sur l'organisme : les trois verdicts, leur ordre, la liste fermée des huit statistiques et le refus d'une fiche sans bloc `statistique` sont conformes aux en-têtes lus. **Deux points neufs nés du choix (b)** : constats neufs 1 et 2 |
| 2 | B | estimande « coût de lecture compris » ; sourd qui paie et sourd à appels égaux ; règle de validité unilatérale ; retrait au plus près du coût ; ligne d'information au devis | **oui** | § 2 (« ce qui est estimé », règle 6), § 5, § 7 (C1, C4, point 8), § 8.3 ; devis § 2 bis, calcul juste. Lettre de la règle 6 à resserrer : constat neuf 5 |
| 3 | B | raison exacte de la règle de validité ; borne au § 10 ; le généraliste | **oui** | § 5, § 10, § 7 (cinquième proposeur ; résultat dit avant l'étage payant) |
| 4 | B | table gelée « lisible », « non lisible », « à reconstruire », seuils chiffrés ; sources à dose nulle par règle écrite | **oui** | § 7, critères C1 à C6 et table des issues. La taille de référence de C2 est réduite (un écart-type entre jumelles) et passe en lois par la règle du § 8.0 : équivalent à ce que je demandais. Deux trous de forme : constat neuf 6 |
| 5 | M | pilote sous son propre préenregistrement, son devis, sa ligne d'accord ; nombre de paires gelé et justifié ; règle chiffrée ; devis recalculé | **oui** | § 8.0, § 8.1 (condition 5), devis § 3 et § 4. Six paires au moins, neuf recommandées, justifiées par la borne haute ; aucune différence entre bras lue, garde éprouvée. Une formule à écrire : constat neuf 7 |
| 6 | M | table de lecture en deux étapes ; lois fausses gelées avec marge ; prédiction chiffrée au préenregistrement, aucun signe visé | **oui** | § 8.1, § 8.3, § 6 |
| 7 | M | même mesure au quart, à la moitié et à la totalité ; coupure sur le budget cumulé ; le monde final décide seul | **oui** | § 6, § 8.3 |
| 8 | M | mécanique du monde final | **oui** | § 6 (génération finale à budget égal, registre gelé en lecture seule, aucune écriture, même dose, graines communes), § 2, § 5. Une contradiction neuve avec le § 3.0 : constat neuf 3 |
| 9 | M | le bras 1 écrit-il les champs ? | **oui** | § 2, avec la borne sur l'acte d'écrire |
| 10 | M | sections c.7 et c.8 | **oui** | § 1, table « ce qui est gardé » ; ce qui est remplacé est dit |
| 11 | M | copies : symétrie, objet de la règle | **oui** | § 6, § 5 (audit des lois identiques), § 7 (le copieur) |
| 12 | m | carte citée pour son vrai objet | **oui** | § 3.1, lettre reprise |
| 13 | m | renvoi à la rédaction de la section C, recopiée à l'octet | **oui** | § 10, puce 1 |
| 14 | m | citations : prémisse de Qin et al. ; Xia et al. sous condition ; N-067 et N-071 sous condition | **oui** | § 11. Ma propre correction était trop étroite pour N-067 : constat neuf 9 |
| 15 | m | empreintes entières | **oui** | en-tête et § 3.3 du plan ; en-tête du devis. Toutes recalculées, conformes |
| 16 | m | colonne « minimal » hors plan ; défaut réécrit ; pilote recalculé ; appels perdus | **oui** | devis § 0, § 2 bis, § 3, § 4, § 8 (« hors plan »), § 9 (défaut dans les mots demandés) |
| 17 | m | lecture invalide rapportée telle quelle ; épreuve reconstruite sur préenregistrement neuf et sources neuves | **oui** | § 8.3, dernier alinéa |

**Les dix-sept sont appliquées fidèlement**, sans dégât sur ce que la contre-lecture avait trouvé tenu (objet du complément 3, trois corrections de la vérification courte, attributions des cartes, calculs, listes « Ne pas écrire »).

## Principes nouveaux et règles

- **Erratum 1 et N-058, aucun verdict de juge comme critère** : tenu. Phrase d'en-tête du § 4 ; registre sans verdict, score ni texte de juge, statistique compris (§ 1) ; aucun champ du registre n'entre chez un juge (§ 1, § 3.1) ; le volet des témoins jugés n'est qu'une information (§ 6, devis § 2) ; aucun classement de juge ne choisit ce qui va à l'épreuve, alors que l'étage des tests de mort de l'organisme tourne aujourd'hui sur un classement figé (en-tête de la version 5 : changement déclaré au § 2, règle 3) ; la composition se juge sur l'oracle et le coût (devis § 2). Le lecteur témoin des tests de mort ne pèse pas sur le verdict (§ 3.0, § 12, question 8).
- **Ligne `GO-2026-11-19-60`** : appliquée sans retirer la procédure. Chaque étage payant, pilote compris, reste sur son préenregistrement, son devis et une ligne d'accord neuve (plan, en-tête, § 8.0, § 8.1 ; devis, en-tête, § 6, point 1, § 9) ; le coût est rapporté, les leviers sont dits avec ce qu'ils feraient perdre (devis § 8). Une lecture du mandat à corriger : constat neuf 4.
- **R1** : le plan n'est pas un préenregistrement et le dit ; chaque étage demande le sien ; les seuils du § 7 et la marge des lois fausses sont « proposés », gelés avant tout tirage ; le pilote ne calcule aucune différence entre bras. Trous de forme aux constats neufs 6 et 7.
- **R5** : chaque garde neuve a son cas sain et son artefact (§ 1, § 2, § 3.1, § 3.2, § 7, point 5, § 8.0). La garde d'entrée de l'expérimentateur manque : constat neuf 2.
- **R6** : empreintes entières partout ; programme rejoué à l'octet. Écart sans effet : le devis dit « rejoué deux fois », le rapport du rédacteur « trois fois ».
- **R7** : aucun chiffre neuf de la littérature ; Brier, Pratt et Holm marqués « non lus sur source » ; les deux chiffres de Qin et al. sont dans les mots de N-073, § 1, avec la mention que le rédacteur ne les a pas relus.
- **R8** : aucune zone dite vierge, aucune priorité.
- **Listes « Ne pas écrire »** (complément 3, point 4 du complément 2, N-073, § 1, N-067, section 4, N-071, point 4) : tenues. Ma recherche rend douze occurrences, toutes bénignes : les lignes du § 14 qui désignent une formule par son sujet, la puce « aucune priorité » du § 10, un « bras de diagnostic seulement » au § 1, et le montant 72,50 du devis. Aucun identifiant de modèle avec sa version ; les noms d'espèce du devis, § 1 et § 2, sont les noms de rôle du manifeste, comme à la v1 (remarque à la mère : deux d'entre eux sont aussi des noms de famille de modèles).

## Rien d'autre qui demande une nouvelle contre-lecture complète

Les changements de la v2 hors des dix-sept corrections sont tous dits au § 16 du plan et au § 10 du devis, et je les ai lus en entier : les conséquences du choix (b) (objet de la prédiction, tranche d'épreuve, prix du test au devis), les conséquences de la ligne `GO-2026-11-19-60` (douze sources chiffrées, composition de la course v9 avec aiguilleur et juges pour information, aucun levier retenu), les questions neuves 6 à 9 et les réserves neuves 4 à 9. Aucun ne touche une hypothèse ou une revendication ; aucun ne demande une contre-lecture complète. Les constats neufs ci-dessous se corrigent par des phrases et des formules, sans changer le dessin.

## Constats neufs

Gravité, comme à la contre-lecture : **B** = à corriger avant tout préenregistrement d'un étage ; **M** = à corriger avant le préenregistrement de l'étage payant, et à nommer dans celui de l'étage sur processeur ; **m** = mineur.

### 1. (B) La tranche d'épreuve n'est pas dite cachée au proposeur

- Le § 3.0 définit la tranche d'épreuve comme « une part nommée du jeu d'évolution de ce monde ». Rien ne dit que le proposeur ne la voit pas. Si le proposeur a le jeu d'évolution entier, le test de mort éprouve une loi sur les données qui ont servi à la trouver : « tient » devient une mesure d'ajustement, la condition des lois fausses (§ 6) perd son sens, et l'exécuteur simulé de l'étage sur processeur (§ 7) n'a pas d'objet défini.
- **Correction** : au § 3.0, ligne « données » : la tranche d'épreuve n'est **jamais servie** au proposeur de la génération ni d'aucune autre ; le proposeur ne voit que la part complémentaire ; garde éprouvée sur un cas sain et sur un artefact (une tranche d'épreuve glissée dans ce qui est servi arrête la génération). Dire au § 7 que l'exécuteur simulé tient la même séparation.

### 2. (M) Un modèle écrit le script dont le noyau lit le fichier : l'invariant et sa garde ne le nomment pas

- L'en-tête de `tests_de_mort_v5.py` le dit : la dernière exécution réussie d'un script **écrit par l'expérimentateur**, une session de modèle, produit le fichier brut ; « un script qui fabrique ses lignes n'est pas détecté ». Le § 3.0 écrit « Aucun modèle ne décide du verdict » : vrai pour la comparaison au seuil, incomplet pour le fichier comparé. Le fichier brut est une entrée déclarée de la fonction d'écriture (§ 3.1), donc `resultat` dépend d'une sortie de modèle qui n'est pas un juge mais n'est pas non plus un programme.
- Le registre est aussi un canal d'attaque (c.8, gardé au § 1) : l'engagement écrit par le proposeur est lu par l'expérimentateur.
- **Correction** : au § 3.0, ligne « exécutant » : nommer l'expérimentateur, son statut (ni juge, ni proposeur), le même modèle, la même consigne et le même plafond dans les trois bras ; ce qu'il reçoit — l'engagement scellé, servi entre balises de donnée, et la part de données que l'étage lui donne — et ce qu'il ne reçoit jamais (justification, prédiction, registre, retour servi au proposeur) ; garde éprouvée sur un cas sain et sur un artefact (un champ du registre autre que l'engagement dans l'entrée de l'expérimentateur arrête l'étage). Au § 7, l'exécuteur simulé tire aussi les échecs de l'expérimentateur (classe « non exécutable ou indéterminée ») à un taux nommé, sans quoi le niveau et la puissance sont optimistes. La question 8 du § 12 reste ouverte ; ces phrases valent quelle que soit sa réponse.

### 3. (M) Test de mort sur le monde final : contradiction avec le § 3.0

- Le § 3.0 dit des données de l'épreuve : « Jamais le monde final ». Le § 6, puce « Lois fausses », fait passer le test de mort aux tentatives de la génération finale, qui ne peut porter que sur des données du monde final. Le § 6 ne dit ni sur quelle part de ce monde, ni par quelle graine, ni sur quel budget ce test se paie (le § 2, règle 4, met l'épreuve dans le budget égal ; la génération finale ne rend rien à un agent).
- **Correction** : écrire l'exception au § 3.0 et la mécanique au § 6 : test de mort des tentatives de la génération finale, après elle, pour la mesure seulement, sur la tranche d'épreuve du monde final tirée par une graine dérivée par source et commune aux trois bras, jamais servi, jamais écrit dans un registre ; dire s'il se paie hors du budget égal (recommandé : hors du budget, à l'identique pour les trois bras, compté au devis, ce que la sensibilité du § 6 du devis fait déjà en comptant les 349 générations).
- Remarque, déjà dans la v1 : la mesure principale compte une loi vraie dès qu'elle est **engagée** et appariée, alors que la condition des lois fausses ne compte que les lois fausses **engagées et tenues**. Un bras qui engage beaucoup gagne des lois vraies sans payer ses lois fausses rejetées. Rapporter aussi, sans seuil, les lois fausses engagées et les lois vraies engagées et tenues, et dire l'asymétrie au § 6.

### 4. (m) Lecture des lignes 55 et 60 de `registres/go.md`

- En-tête du plan : « Ce plan n'est donc plus « préparé sans dépense » par principe ». La ligne 55 dit la question de l'héritage « préparée sans dépense » : c'est la préparation qui ne dépense pas, et elle n'en dépense toujours pas. La ligne 60 porte sur le critère de coût C3 des cartes, avec un « considérable » défini par un lecteur et scellé ; son application à ce plan est la question 9 du § 12, non tranchée. Or trois choix en sont déjà tirés : douze sources chiffrées au lieu de dix, l'option d'un seul contraste fermée et la question qui la posait retirée des nœuds (elle l'était à la v1), aiguilleur et juges dans la recommandation.
- **Correction** : « La préparation reste sans dépense (ligne 55) ; sous réserve de la question 9, le dessin n'est pas réduit pour son coût (ligne 60), et la procédure de devis et de ligne d'accord est inchangée. » Garder la question 4 comme nœud, ou la conditionner à la question 9 ; le devis, § 8, donne déjà le prix de chaque levier.

### 5. (m) Règle 6 du § 2 : deux définitions du retrait

- « Le plus grand nombre d'appels dont le coût prévu tient dans le budget » et « retirés un à un, dans l'ordre d'une permutation semée » ne désignent pas le même ensemble quand les espèces coûtent de 0,38 à 2,25 USD par appel : le plus grand nombre s'obtient en retirant d'abord les plus chers. **Correction** : « retirer, un à un, dans l'ordre de la permutation semée, jusqu'à ce que le coût prévu tienne dans le budget ». Le § 2 bis du devis, qui suppose un coût d'appel uniforme, reste un ordre de grandeur et peut le dire.

### 6. (m) Table des issues du § 7 : deux trous de forme

- La grille de sources (10 à 24) ne contient pas les nombres de sources à dose nulle possibles (m au moins 5 ; huit au devis). Geler une grille à part pour m (par exemple, 5 à 16).
- « Étendue par programme si besoin » sans borne : l'issue « non lisible » ne peut alors jamais être prononcée. Geler un maximum de la grille étendue.
- Dire que le suiveur de forme et le généraliste paient leur lecture comme un vrai bras (règle 6), et que C3 se mesure ainsi.

### 7. (m) § 8.0 : « majoré de la part de différences nulles observée »

- La formule n'est pas écrite. **Correction** : par exemple, nombre retenu = entier supérieur de (nombre lu dans la table ÷ (1 − part de différences nulles)). Ajouter à la réserve 6 que les neuf différences viennent de trois sources et que leurs variances peuvent différer d'une source à l'autre : la borne du khi-deux à k degrés suppose des différences de même loi.

### 8. (m) Table de lecture du § 8.3 : signe et pas d'épreuve

- Le signe de la lecture est celui de la médiane des différences, alors que le test est celui des rangs signés ; les deux peuvent diverger. Prendre le signe de (somme des rangs positifs − somme des rangs négatifs), ou de l'estimateur de Hodges et Lehmann, cohérent avec le test ; garder la ligne « rapportée telle quelle » pour le cas d'égalité.
- § 3.0, « qui est éprouvé » : une tentative non éprouvée faute de budget reçoit la classe « non exécutable ou indéterminée ». Elle entre alors dans la justesse des prédictions et dans le retour servi comme un échec du proposeur. Lui donner un statut à part, « non éprouvée (budget) », hors du score de justesse et dit tel quel dans le retour.

### 9. (m) Citations de N-067, section 6

- N-067, section 6, s'applique à « tout texte interne qui présente l'organisme (dossier de candidature, papiers, notes, enregistrement public des pièces libres) ». L'épreuve étant désormais l'étage de l'organisme, presque tout texte tiré de ce plan présente l'organisme. Ma correction 14 les mettait sous condition de la voie (a) : elle était trop étroite. **Correction** : au § 11, les écrire obligatoires pour tout texte sortant tiré de ce plan qui décrit l'épreuve ; garder N-071, point 5, sous la condition écrite.

## Verdict

Scellable après corrections.

Les dix-sept corrections de la contre-lecture sont appliquées fidèlement et sans dégât ; les calculs se rejouent à l'octet ; l'erratum 1 et N-058 sont tenus (aucun verdict de juge comme critère, dans aucune garde, aucun champ, aucun choix) ; la ligne `GO-2026-11-19-60` est appliquée sans retirer la procédure de devis et de ligne d'accord ; les règles R1, R5, R6, R7 et R8 et les listes « Ne pas écrire » sont tenues. Rien d'autre n'a changé qui demande une contre-lecture complète. Avant tout préenregistrement d'un étage, le constat neuf 1 (tranche d'épreuve cachée au proposeur) est à corriger ; les constats 2 et 3 (expérimentateur, test sur le monde final) avant le préenregistrement de l'étage payant, et à nommer dans celui de l'étage sur processeur ; 4 à 9 sont de forme. Une version 3 qui les applique peut être vérifiée sur ces seuls points, sans contre-lecture complète. Les quatre nœuds du § 12 et la recommandation du devis restent à Lazar.
