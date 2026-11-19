# Vérification — ligne 3 des épreuves v9 (votes effectifs des juges croisés, mesurés sur témoins plantés), version 4 du préenregistrement et du devis, sur le différentiel avec la version 3 — v1

- **Vérificateur** : agent neuf du « modèle O ». Je n'ai écrit aucune des pièces lues (versions 1 à 4, calculs, rapport du rédacteur, vérifications antérieures).
- **Heure** (`date -u`) : 2026-11-19T15:36:08Z. Processeur seul ; aucun appel de modèle, aucune dépense, aucun tirage du banc, aucune écriture dans le dépôt.
- **Branche** `lot/compte-organisme-v1`, tête `1837b4b6df094c1b736bcd887acb9f0ab5dcccbc`, arbre propre.

## Empreintes (toutes recalculées sur disque, « OK » contre leur compagnon)

| pièce | empreinte |
|---|---|
| préenregistrement v4 | `26bb22145e8d90dc0d38382361e50fe6d59b3a7cd82d56d25dafeb10fe97cd84` |
| devis v4 | `0051297ab2bb2fc6552d5354d06d4301ff082570f6b81cdcbd7ac7224f4f95fe` |
| `calcul_devis_ligne_3_v3.py` | `9364867e7a21d28e2b30f3f73d3f0a6604cecfa3eee5efb46eb2331ba3dcbaf8` |
| `calcul-devis-ligne-3-v3.json` | `1a13fe2756a5587398e122c17700fab6472350d6c38975d58c1c3cf337ad6cf6` |
| `calcul_predictions_ligne_3_v1.py` | `282b5d518685059371e160c74e0e1a05b1f22593a20275924712320509216434` |
| `calcul-predictions-ligne-3-v1.json` | `d0ea89843d450f9bbe983726e0cbccc9f5bf359cef50d54aab5571a4e7af9faf` |
| rapport du rédacteur | `95f836011e7abb9dced6d0aafe480ab35731baec6f7143beba4ca8c3777d3821` |
| référence : préenregistrement v3 | `9b62fd5a2cda64bf1889b9f174d5049de7c2a36f72da307fb767427db5f5a50e` |
| référence : devis v3 | `f84827eadfb59355fb58e282be17004a1b0ef75e6a17be51889668861e10d328` |
| référence : calcul v2, sortie | `84d2d0a7…`, `a03b7778b91fbede729e98234f1c111afa5a943dfceedd86929573e2b778353e` |
| référence : vérification v3 | `6e2b540fb5f7a2db031de60b8537b2875e84ed3b9ba1aee1e8ca5e15059a12f4` |
| référence : vérification v2 | `5b3dc1370bbd206cc19000effc516bd6295144a891144298b0de2ab684ae3863` |
| mandat du rédacteur | `8821c6716ef43e409576b53fbb2e701a4489de06e0f98855a3d882434035edac` |

Autres empreintes citées par la version 4 et recalculées : consignes de la mère (branche) `986e3a3c…` ; note de littérature sur les juges `bb54b685…`, égale au commit `c0fca6fe…` et à la tête de main ; `registres/go.md` au commit de main `7dcd6a44…` = `72e52540…` (juste). Fait daté : la tête de main lue à 15:36Z (`ccafc3b0…`) porte un `registres/go.md` neuf (`84aa29a2…`, lignes GO-2026-11-19-75 et -76 ajoutées, toutes deux sur l'épreuve d'héritage) ; le renvoi de la version 4 reste exact pour le commit qu'il nomme. Le `git fetch` n'a pas abouti dans le délai (arrêté par moi) ; la référence distante locale était déjà à `ccafc3b0…`.

**Cartes** : `fcfa3d98b90f8`, `fefca0bd94064`, `fa38f9faa24e0` seulement, par un programme qui n'extrait qu'elles, champ `meta` retiré, dans le fichier des cartes `ba65c411…` (empreinte vérifiée). Transparence : un premier passage du programme n'a rien trouvé (identifiant porté par une clé) et n'a rien affiché d'autre que l'empreinte et la liste des manquantes.

**Non ouverts** : `diag/`, `donnees/`, coffre, verdicts des juges sur la course v9, code de l'organisme, tout autre fichier sous `archives-reponses-modeles/`, tout fichier « consigne-privee » ou « conception-ii-b ».

## 1. Constats A à D de la vérification de la version 3

| constat | appliqué | juste | remarque |
|---|---|---|---|
| A — renvoi de GO-2026-11-19-73 | oui | oui | en-tête et devis renvoient à `7dcd6a44…` / `72e52540…` ; ligne relue : texte égal ; « je ne l'ai pas relue sur main » retiré ; l'absence de la ligne sur la branche est dite |
| B — sens du lecteur de surface | oui | oui, avec deux réserves (corrections 3 et 4) | voir ci-dessous |
| C — cellule de puissance et règle de plantation | oui | oui | voir § 2 ; une formule de forme (correction 6) |
| D — forme | oui | oui | 0,050 ; vrais rejetés aux trois δ (0,18/0,28 ; 0,14/0,23 ; 0,09/0,14, recalculés : 0,1813/0,2775 ; 0,1436/0,2256 ; 0,0885/0,1444) ; s = 0 : clause (i) non lue, « sans prise » ; abstentions par vote 0,1275, par témoin 0,2387 |

**Constat B, au fond.**
- *Le mot peut-il rendre les deux issues sans que ce soit par construction ?* Oui, dans le sens séduisant. Recalcul indépendant (programme à moi, bibliothèque standard) : faux acceptés parmi les faux à trait, bras 1 : 0,02943 ; 0,04644 ; 0,05048 ; bras 2 : 0,00051 ; 0,01049 ; 0,10931 (δ = 0 ; 0,2 ; 0,5). Clause (i) : « réfuté », « réfuté », « tient » ; la bascule bras 1 = bras 2 se fait vers δ ≈ 0,39. Clause (iii) à s = 0,5 : écarts du bras 1 + 0,0276 et + 0,0431, du bras 4 + 0,0880 et + 0,3250 : « tient » à δ = 0,2 et 0,5. Mot de la carte : « réfuté », « réfuté », « tient ». L'issue dépend de δ, le paramètre que la carte nomme, et non d'un trait du banc qui fermerait une issue : le défaut que visait B est levé. La marge de 0,007 de la clause (iii) à δ = 0,5 n'est pas un risque réel : l'intervalle porte sur une moyenne de 2 000 répliques, de largeur bien inférieure.
- *Le choix du sens qui décide est-il fixé avant toute donnée et motivé ?* Fixé avant toute donnée : oui (aucun code, aucun tirage). Motivé : oui, par la lettre de la carte, que j'ai relue (« une part δ, connue, décide sur ce trait » ; réfutation sur « le taux d'acceptation des faux témoins confondus »). Mais il a été fixé **avec le calcul exact en main**, et la raison donnée pour écarter le sens repoussant (règle R4 : un seul mot possible) vaut aussi, **sur cette grille**, pour le lecteur séduit (c), qui ne rend que « réfuté » aux trois δ joués. Le texte ne le dit pas ; il laisse croire que (c) est écarté pour sa seule distance à la lettre. Correction 4.
- *La limite dite laisse-t-elle une épreuve qui vaut quelque chose ?* Oui, et elle est moins forte que le texte ne l'écrit. Chez le lecteur séduit, la clause (i) n'est pas réfutée « partout » par construction : elle bascule elle aussi vers « tient », vers δ ≈ 0,54, juste au-dessus de la plus haute valeur jouée. Les deux lois donnent donc la même lecture qualitative (le double rendu ne bat l'unanimité de quatre juges que si une part forte des juges lit la surface) ; elles diffèrent par le lieu de la bascule, de part et d'autre de δ = 0,5. La phrase « le « tient » prédit à δ = 0,5 tient à la loi du lecteur » est juste sur la grille et trompeuse au-delà (correction 3). Ce que l'épreuve vaut : sur un banc scripté, les mots suivent du calcul exact ; le banc vaut par la vérification du code contre les formules et par la carte de la région où le mécanisme gagne. Les mots restent descriptifs (« ne valident, n'écartent ni ne classent aucune carte »). **Pas de retour à Lazar** : aucune hypothèse, revendication, dépense ni décision de carte ne change.
- Observation, sans correction : chez le suiveur séduisant, le bras 2 rejette 0,97 des vrais à δ = 0,5 ; la clause (i) ne compare les vrais rejetés qu'au bras 4, comme l'écrit la carte. Un « tient » s'y obtient donc contre une base qui rejette presque tout vrai ; la mention de la réserve 11 le couvre en partie.

## 2. Constat C : monde de puissance

- **Écrite d'avance et reproductible** : oui. Formules recalculées à la main : « au moins un » (a₁₁ + 2b − b₁₁)/2 ; unanimité (2a − a₁₁ + b₁₁)/2 ; juge seul (a + b)/2 ; bras R ρ′p + (1 − ρ′)(3p² − 2p³), propre à la loi 1, comme le texte le dit. Contre un juge seul à ρ = 0, l'écart vaut 0,6 d : 0,10 demande d = 0,1667 (sortie : 0,1667) ; maximum 0,12, donc 0,15 infaisable. Cellules faisables pour 0,10, recalculées par balayage : contre l'unanimité ρ ≤ 0,45 (écart maximal 0,132 à 0,45, 0,096 à 0,60) ; contre un juge seul ρ ≤ 0,15 (0,102 à 0,15, 0,084 à 0,30) ; contre le bras R, ρ = 0 avec ρ′ = 0,5 (0,108) et 0,9 (0,118), pas ρ′ = 0 (0,096) ni ρ = 0,15. Comptes par loi égaux à la sortie et au texte (4/2, 2/1, 2/2). Bissection déterministe sur [0 ; 0,20], 80 pas ; la loi 3 du monde suit la loi 3 du texte (f = 0,25).
- **Prédiction « descriptives » honnête, et non un levier vers un signe (règle R3)** : elle va dans le sens prudent (elle retire un « oui » possible, elle n'en fabrique pas) et le monde retenu est le plus favorable de sa famille à l'écart planté (la dissymétrie est résolue pour l'atteindre) : une puissance basse y vaut puissance basse partout. Deux manques : la prédiction n'est que dans le rapport, pas au texte (règle R1 : prédiction chiffrée écrite avant) — correction 5 ; et ce qu'elle emporte n'est dit nulle part à Lazar : si elle se vérifie, l'étage payant ne peut rendre que « non » (rang 3), « non concluant », ou des mesures (ρ′ − ρ « positif » rapporté comme mesure). C'était déjà la lecture d'ensemble de P10 ; la version 4 la rend presque certaine. À dire à Lazar avec la demande de départ (information, pas une correction du texte).
- Forme : « à ce taux, la théorie ne le permet pas » dit plus que le calcul (une famille de mondes, non la théorie) — correction 6.

## 3. Les trois conditions de R-3875

- **(i) Arrêt dur par compteur, cas sain et artefact** : écrit au texte (section « Plafond : arrêt dur par compteur », deux gardes à la liste d'arrêt) et au devis (§ 5), cohérents. Recalculé : 41 envois si tout est refusé (40 × 0,60 + 0,60 = 24,60 ≤ 25 ; le 42ᵉ ferait 25,20) ; 3 refus supportés au cas haut ((24,40 − 22,4878)/0,60 = 3,19) ; 13 à l'estimation. **Limite** : la borne n'est dure que si un appel ne peut pas dépasser 0,60 USD ; sinon le dernier envoi peut porter la dépense au-dessus de 25 USD avant que le coût relevé n'arrête le programme. Le texte le dit à moitié ; il ne dit ni la borne réelle ni qui vérifie que le plafond de session est tenu — correction 7.
- **(ii) Pire cas** : écrit d'avance, cohérent entre texte et devis (18 témoins, 16 / 13 / 11 avec 1 / 2 / 3 refus ; 24,27 USD comptés) ; rang 1 de la table nomme « non concluant par manque de témoins », « jamais lu comme un « non » ». Recalcul à la main : (24,40 − 1,973 × 10,061)/(1,973 × 0,1243) = 18,5 → 18. Trou mineur : la phrase « restent mesurés sur le bloc A » suppose le bloc A complet ; une coupure pendant le bloc A (refus en nombre, ou tarif entre 2,4 et 3 fois, que l'arrêt de plomberie à 3 fois n'attrape pas) n'est pas écrite — correction 8.
- **(iii) Envoi refusé compté au pire** : écrit, jamais zéro ; garde « compteur, envoi refusé » juste. **Incohérence** : le texte (« Étage 2 », appels ; « Seuil ») fait rejouer un envoi « refusé ou sans coût lisible ». Un envoi revenu avec un verdict mais sans coût lisible serait alors rejoué : second verdict pour le même rendu, appel de plus, et une règle de choix entre deux verdicts que le texte ne donne pas (risque sur les répétitions qui mesurent ρ′). Le devis, lui, ne rejoue que l'envoi refusé — correction 2.
- **Devis lu sur le cas haut** : oui, en tête du devis et au § 5 (22,49 ; 23,09 avec réserve).

## 4. Rejeu des deux programmes

Joués par moi (`python3 -I -B CHEMIN_ABSOLU`) depuis un répertoire de mon bloc-notes (liens vers `runs/` et `docs/` pour les trois fichiers d'entrée empreintés du calcul du devis), sorties écrites dans mon bloc-notes :
- `calcul-devis-ligne-3-v3.json` : `1a13fe27…`, **égal à l'octet** (`cmp`) ;
- `calcul-predictions-ligne-3-v1.json` : `d0ea8984…`, **égal à l'octet** ;
- `calcul_devis_ligne_3_v2.py` rejoué aussi : `a03b7778…`, égal. Comparaison clé par clé v2 → v3 : aucune clé retirée, seule « version » change, deux clés ajoutées (« compteur_d_arret », « essais_courts_d_autres_lignees_borne_dure »). Différentiel des deux programmes de devis : en-tête, une constante, un bloc de calcul ajouté ; aucune ligne de calcul existante touchée.

Chiffres neufs recoupés à la main (sept) : 41 envois / 24,60 USD ; 3 et 13 refus supportés ; 18 témoins au pire cas ; bras 2 séduisant 0,575⁴ = 0,1093 ; vrais rejetés 0,7953 contre 0,8194 à δ = 0,5 ; écart contre juge seul 0,6 d (d = 0,1667) ; borne d'un essai court 11 × 0,60 = 6,60 USD, 19,80 pour trois ; ordre de grandeur des trois essais 3,18 à 5,08 USD (« 3 à 5 » du rapport). Tous justes.

## 5. Décisions de Lazar

- **GO-2026-11-19-63, point 1** : porté sans écart (deux cartes gardées, avis pondéré descriptif ; la séparation tient, donc pas de retour, ce qui est la lettre de la clause).
- **GO-2026-11-19-66** : porté sans écart (25 USD, échéance 2026-11-27, conditions ; la garde « ligne de GO » refuse une ligne échue). Note : l'ordre écrit (scellement, code, contre-lecture du code, additif, étage 1, retour à la mère) rend l'échéance du 27 serrée ; une ligne échue demande un mot neuf, ce que la garde tient déjà.
- **GO-2026-11-19-73** : porté sans écart, mot cité exact.
- **Marquages « en attente »** : aucun ne reste (recherche par programme sur les deux pièces ; seules mentions historiques dans les tables des versions 1 et 2).

## 6. Points tranchés par le rédacteur (Q2 à Q8) — avis bref

- **Q2** (plan d'appels) : d'accord ; inchangé depuis la version 3.
- **Q3** (garde de recouvrement étendue aux 94 cartes) : plus protecteur, d'accord sur le fond ; mais c'est une ouverture neuve d'un fichier sous `archives-reponses-modeles/` par un programme, donc un choix de cloisonnement qui revient à la mère, comme le texte le dit ; et la liste d'arrêt n'a pas suivi (correction 1).
- **Q4** (pas d'autre lignée à l'étage 2) : d'accord ; « ce qui manque » (coût de juge mesuré par lignée) est dit en une phrase, comme demandé.
- **Q5** (plafond) : d'accord, sous les corrections 2, 7 et 8.
- **Q6** (sens qui décide ; troisième lecteur) : d'accord sur le sens séduisant ; le troisième lecteur est un bon ajout ; corrections 3 et 4.
- **Q7** (monde de puissance) : d'accord ; correction 5 (prédiction au texte) et 6 (forme).
- **Q8** (scellement avant le code, additif de code) : d'accord ; c'est la conséquence de l'ordre R-3864. L'écart au gabarit (commit du code dans le préenregistrement) est réglé par l'additif ; la mère le note au scellement.

## 7. Neuf dans le différentiel, non demandé

1. Le troisième lecteur de surface (c), rapporté sans mot : utile ; voir corrections 3 et 4.
2. `calcul_predictions_ligne_3_v1.py` et sa sortie : bienvenus (règle R6), rejoués à l'octet.
3. La garde de recouvrement étendue aux 94 cartes par programme : à trancher par la mère (cloisonnement) ; liste d'arrêt non mise à jour.
4. Le rejeu unique d'un envoi refusé : bonne règle, mal bornée pour l'envoi « sans coût lisible » (correction 2).
5. La relance après panne sans remise à zéro du compteur : bonne règle.
6. Les tailles de banque du bras double rendu (celles de la grille, sans partage) : comblent un manque des versions 1 à 3 ; sans effet sur les mots prédits.
7. « Ce que l'étage 1 rend à la mère » (verdict, table de taille, taille retenue, puissance qui décide) : conforme à R-3864.
8. La lecture par colonne (une seule colonne, « à domicile » pour le juge de la lignée du contre-lecteur ; réserve 6 étendue) : conforme à la note de littérature, § 5, que j'ai relue (lecture par colonne, référence extérieure aux juges).
9. La phrase de statut dit que la version 4 « se vérifie … par le même contre-lecteur du modèle O » : ce n'est pas le cas, je suis un agent neuf du même modèle (correction 9).

Rien d'autre : les 33 morceaux du différentiel du préenregistrement et les 15 du devis sont tous dans les tables « Différentiel avec la version 3 ». Rien ne change le choix de Lazar, la grandeur mesurée, les lois, la grille, le plan de 504 appels, les montants (16,52 ; 22,49 ; 44,38 USD), le plafond, la table de l'étage 2 hors la précision du rang 1.

## 8. Corrections

Toutes au préenregistrement v4 sauf mention ; aucune ne change un montant, un appel, une hypothèse ou une décision de Lazar.

1. **Liste d'arrêt, garde « recouvrement »** (ligne de table). Remplacer « banque écrite : aucun bardeau de huit mots commun avec les sept cartes lues ni avec les onze témoins de la version 2 » par « banque écrite : aucun bardeau de huit mots commun avec les 94 cartes de la course v9 (programme qui ne rend que des comptes et l'identifiant du témoin refusé, sans afficher aucune carte) ni avec les onze témoins de la version 2 ; si la mère refuse l'ouverture par programme (Q3), les sept cartes nommées, écart écrit au manifeste ».
2. **Étage 2, appels** (« Un envoi refusé ou sans coût lisible est rejoué une fois au plus, tout de suite ; si le second envoi échoue aussi, le verdict de ce rendu est « absent ». »). Remplacer par : « Un envoi refusé, coupé par un délai ou revenu en erreur est rejoué une fois au plus, tout de suite ; si le second envoi échoue aussi, le verdict de ce rendu est « absent ». Un envoi revenu avec un verdict lisible mais sans coût lisible n'est pas rejoué : son verdict est gardé et il est compté 0,60 USD. » Même précision à « Seuil », phrase « Un envoi refusé est rejoué une fois au plus. » (ajouter « ; un envoi revenu sans coût lisible n'est pas rejoué ») et à l'annexe A (« rejeu unique » → « rejeu unique d'un envoi refusé, coupé ou en erreur »).
3. **P5 quater et réserve 11.** Dans P5 quater, remplacer « Lue sur lui, la clause (i) serait « réfutée » partout : **le « tient » prédit à δ = 0,5 tient à la loi du lecteur de surface** (réserve 11). » par « Lue sur lui, la clause (i) serait « réfutée » aux trois valeurs de δ jouées ; elle basculerait elle aussi vers « tient » au-delà de la plus haute valeur jouée. **Le « tient » prédit à δ = 0,5 tient à la loi du lecteur de surface et à la grille de δ** (réserve 11). » Dans la réserve 11, remplacer « chez le lecteur séduit qui juge le fond quand le trait manque, la clause (i) serait réfutée partout (P5 quater). » par « chez le lecteur séduit qui juge le fond quand le trait manque, la clause (i) serait réfutée aux trois valeurs de δ jouées, la bascule tombant au-delà de δ = 0,5 (P5 quater). » Si le rédacteur veut chiffrer les deux bascules (≈ 0,39 et ≈ 0,54 par mon calcul), il les ajoute à un calcul versionné neuf (`calcul_predictions_ligne_3_v2.py`), non au texte seul (règle R6).
4. **Bras « double rendu »**, après « **Le sens (a) décide : lui seul porte le mot de la carte.** » et sa raison. Ajouter : « Le lecteur (c), lui aussi, ne rend qu'un mot sur cette grille (clause (i) « réfuté » aux trois δ) : la règle R4 l'écarte du mot au même titre que le sens (b). Le choix du sens (a) a été fait avec le calcul exact des trois lois en main, avant tout code et tout tirage ; il suit la lettre de la carte (« décide sur ce trait »). »
5. **Prédiction chiffrée**, P10. Après « **Lecture d'ensemble prédite : « non », ou « non concluant » faute de puissance.** », ajouter : « Règle gelée de portée (prédit) : la puissance qui décide, dans le monde de puissance, sera sous 0,5 pour l'écart de 0,10, et les comparaisons d'agrégations seront déclarées descriptives avant la dépense ; un « oui » de l'étage 2 serait alors inatteignable. *Réfutation* : puissance qui décide de 0,5 ou plus. »
6. **Règle gelée de portée**, « *La règle qui plante l'écart* ». Remplacer « à ce taux, la théorie ne le permet pas. » par « aucun monde de cette famille (deux juges de même profil, taux moyen 0,20, d ≤ 0,20) ne le porte. »
7. **Plafond : arrêt dur par compteur, (i)**, phrase « Le compteur ne borne la dépense que si le service tient le plafond de session ; je n'ai pas relu le code qui le tient : un coût relevé au-dessus de 0,60 USD arrête donc le programme. » Remplacer par : « Le compteur borne la dépense à 25 USD si aucun appel ne peut coûter plus que le plafond de session ; sinon, à 24,40 USD plus le coût du dernier envoi, et un coût relevé au-dessus de 0,60 USD arrête le programme. La contre-lecture du code de l'étage 2 vérifie, avant tout envoi réel, par quel moyen le plafond de session est tenu à chaque appel (borne de jetons produits ou plafond du service) ; sans ce moyen, pas de départ. » Même ajout au devis, § 5, condition (i).
8. **Plafond, (ii)**, après « Reprendre la mesure demande un devis neuf et une ligne neuve. » Ajouter : « Si le compteur coupe avant la fin du bloc A, le verdict est le même (« non concluant par manque de témoins ») ; les grandeurs du bloc A ne sont alors rapportées que sur les témoins complets pour les deux juges, comme des mesures partielles nommées telles. »
9. **Statut** (« elle se vérifie sur son différentiel, par le même contre-lecteur du modèle O (règle de l'allègement, …) ») et **« Contre-lecture »** (« Par le même contre-lecteur du modèle O. Fichiers ») : écrire « par un agent du modèle O qui n'a écrit aucune version » (la vérification de la version 4 a été faite par un agent neuf de ce modèle, non par celui des versions 1 à 3).

Les corrections 1, 2 et 7 portent sur les conditions du plafond ou sur une garde ; 3, 4 et 5 sur la lecture et la prédiction ; 6, 8 et 9 sont de forme ou de complétude. Toutes sont localisées ; une version 5 (nom neuf) se vérifie sur son différentiel.

## 9. Les deux décisions pour Lazar — avis

- **Essais courts d'autres lignées comme juges** : d'accord avec (a) (après la lecture de l'étage 1) ; j'ajouterais « et après la note de conception du juge (GO-2026-11-19-65) », puisque le devis lui-même ne fait venir l'essai court que si cette note retient le collège. La borne dure (6,60 USD par lignée) est juste ; les ordres de grandeur sont sous le plafond de session pour les trois lignées. Défaut (a) raisonnable : il ne dépense rien.
- **Seconde colonne d'auteur** : d'accord avec (a) pour la ligne 3 (son objet est la décorrélation, pas la préférence pour soi). Mais la question est la mesure la plus directe de l'inquiétude de Lazar (un juge sévère envers les cartes d'autres lignées) : elle doit être posée explicitement dans la note de conception du juge, non seulement « renvoyée ». À dire aussi : la seule colonne de la ligne est « à domicile » pour l'un des deux juges ; l'écart d'erreur entre les deux juges y est donc sous réserve (réserve 6), ce que le texte dit.

## 10. À dire à Lazar, en information (par la mère)

Si la prédiction de la correction 5 se vérifie, l'étage payant de 25 USD ne pourra rendre ni « oui », seulement « non » (un juge répété vaut le collège), « non concluant » ou des mesures (nombre de votes effectifs, table par juge, décorrélation rapportée comme mesure). Le pire cas reste « non concluant par manque de témoins », jamais un « non ».

## Ce que je n'ai pas vérifié

- Le code de l'organisme (`juges_croises_v53.py`) et la manière dont le service tient le plafond de session : non ouverts.
- La loi 3 dans le monde de puissance au-delà des comptes de cellules jouables (aucune puissance simulée : elle demande le banc).
- Aucun travail publié lu ; la lecture par colonne est celle de la note de littérature.

## Verdict

**Scellable après corrections** (neuf, numérotées au § 8 ; aucune ne change un montant, le plan d'appels, une hypothèse ni une décision de Lazar).
