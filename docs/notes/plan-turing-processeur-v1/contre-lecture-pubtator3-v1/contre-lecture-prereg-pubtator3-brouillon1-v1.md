# Contre-lecture (règle R2) du préenregistrement « le pont suit-il la carte ? » sur la base ouverte PubTator 3, brouillon 1 (version 1)

- Contre-lecteur : sous-agent neuf, modèle Opus 5.5 (`claude-opus-5-5`), qui n'a pas écrit le texte ; aucun fichier du dépôt modifié, aucun réseau, aucune dépense.
- Date (`date -u`) : `Tue Nov 24 13:27:07 UTC 2026`
- Texte relu : `prereg/pas0-organisme-v1/prereg-epreuve-pont-suit-la-carte-pubtator3-v1-brouillon1.md`, empreinte SHA-256 recalculée `94556efa6fb6093e3768decf7d43280ccc63598439b2f35ac04892f963eb18de` (concorde avec le `.sha256` compagnon), 145 lignes.
- Pièces lues : le texte ; `CLAUDE.md` ; `prereg/gabarit-preregistrement-v1.md` ; `src/controle_ia/prereg.py` (validateur exécuté) ; fiche du registre des idées (IDE-2026-11-23-027) ; réponse de Fable 5.2 en effort maximal, sections 2 à 7 ; fiche de faisabilité des données publiques (version 1) ; pour vérification ponctuelle : `registres/go.md` (lignes des autorisations citées) et `registres/decisions.md` (R-5202, R-5203).

## Verdict

**Non scellable en l'état.** Six constats bloquants : le script d'épreuve à vérité plantée cité n'existe nulle part ; la datation des relations, sur laquelle reposent les trois volets et la garde d'étanchéité temporelle, n'a pas de source ; la fécondité du volet de la fécondité conditionnelle (volet B) repose sur des auteurs absents des données et sur une notion d'« équipe » non définie ; le contrôle de permutation des polarités nomme des types de relations qui n'existent pas dans PubTator 3 ; la porte 1 exige un gain d'aire sous la courbe que l'effet prédit ne peut pas produire, ce qui fige d'avance un « réfuté » ; enfin les règles de réfutation du volet B se contredisent. L'idée, ses trois volets et la structure du texte sont sains ; la reprise demande une refonte de la section des données et des portes, pas un nouveau projet.

Décompte : 6 bloquants, 11 majeurs, 12 moyens, 7 mineurs.

## Constats

### Bloquants

**B1 — Script d'épreuve à vérité plantée introuvable (lignes 8, 91-94, 136, 145).**
Constat : `epreuve_plantee_pubtator3_v1.py` n'existe ni dans le dépôt ni ailleurs sur la machine (`find / -name '*pubtator3*'` ne rend que le brouillon et son `.sha256`), et `git log --all -- '*pubtator*'` ne rend aucun commit (le clone est superficiel, voir N2). Aucun fichier `.py` du dépôt ne mentionne PubTator.
Pourquoi : la garde 2 de la liste d'arrêt et les seuils des mondes plantés (lignes 91-94) en dépendent ; les tailles d'effet plantées, la taille des mondes et donc la sévérité réelle des seuils ne sont fixées que par ce script. Le texte demande lui-même (ligne 145) qu'il soit transmis au contre-lecteur. La règle R6 (chemin et empreinte) ne peut être tenue, et le champ « Commit du code d'analyse » du gabarit ne peut pas désigner un code qui n'existe pas.
Correction attendue : écrire le script (classe B, contre-lu par un autre modèle), le citer par chemin et empreinte, puis faire contre-lire de nouveau les seuils des mondes plantés à la lumière de ses paramètres.

**B2 — Aucune source de date pour les relations ; garde d'étanchéité temporelle inapplicable telle qu'écrite (lignes 25, 59, 100, 137 ; et partout où entrent « âge des entités », « avant t_pont », fenêtres 2011-2015 et 2016-2025).**
Constat : le texte parle de relations « typées et horodatées » (ligne 25) et d'une « correspondance PMID -> année de publication PubMed » fournie avec l'archive (ligne 100). La fiche de faisabilité (section 3) dit au contraire : « Pas de date dans le fichier » `relation2pubtator3` ; la seule horloge envisagée est l'ordre des identifiants PubMed, étalonné sur un échantillon daté par les utilitaires publics de PubMed. Aucune table identifiant PubMed vers année n'est décrite dans l'archive.
Pourquoi : (i) avec l'horloge par ordre d'identifiants, toutes les dates sont imputées, ce que la garde 3 interdit (« zéro imputation de date par défaut ») : la garde arrêterait toujours, ou serait contournée ; (ii) l'ordre des identifiants n'est pas monotone en date de publication (articles anciens versés tardivement, dates électroniques antérieures à la date imprimée), ce qui fait fuir des articles postérieurs à 2010 dans le graphe gelé — exactement la fuite que l'audit de la ligne 127 soupçonne ; (iii) la notion de « date » n'est pas choisie (année de publication imprimée, date électronique, date d'entrée dans PubMed) ; (iv) obtenir la date de chaque article par les utilitaires publics demande des millions de requêtes réseau, non décrites et non chiffrées en temps.
Ce qui manque pour rendre la garde applicable : une source nommée et empreintée donnant, pour chaque identifiant PubMed du fichier de relations, une date (par exemple les fichiers de base annuels de PubMed, ou une récolte exhaustive par les utilitaires publics) ; le champ de date retenu et sa règle quand il manque (exclusion de l'article, jamais imputation) ; le taux de dates manquantes toléré, avec seuil d'arrêt ; si une horloge par identifiants est gardée, sa loi d'erreur mesurée et une marge de garde (par exemple exclure une bande d'identifiants autour de la coupure), et une garde réécrite en conséquence.
Correction attendue : réécrire la source des données, la définition de la date et la garde 3 pour qu'elles concordent avec la fiche de faisabilité ; garde testée sur cas sain et sur artefact (article tardif injecté).

**B3 — Fécondité fondée sur des auteurs absents des données et sur une « équipe » non définie (lignes 28, 46, 102).**
Constat : la variable de sortie de la porte 1 exige « au moins trois équipes indépendantes ne partageant aucun co-auteur avec l'article fondateur » (ligne 28), puis « équipes disjointes des auteurs de 2011-2015 » (ligne 102). Le fichier de relations n'a pas d'auteurs (fiche, section 3) ; aucune source d'auteurs n'est nommée.
Pourquoi : la sortie principale de la porte décisive n'est pas calculable ; trois choix restent libres après coup : la source des auteurs, la règle d'identité d'un auteur (homonymes, initiales), et ce qu'est une « équipe » (un article ? un ensemble d'auteurs ? indépendance entre les trois reprises ou seulement envers le fondateur ? fondateur seul, ou tous les auteurs de 2011-2015 ?). La réponse de Fable (section 7, B) définissait plus simplement la fécondité par « articles distincts réaffirmant le lien ».
Correction attendue : nommer la source des auteurs (avec empreinte), figer une règle d'identité et de disjonction, ou revenir à la définition de Fable et déclarer l'écart ; dans tous les cas une seule définition.

**B4 — Contrôle de permutation des polarités nommant des types qui n'existent pas (lignes 28, 47, 67).**
Constat : le texte échange `stimulation` contre `inhibition` et `causalité positive` contre `prévention`, sur un alphabet supposé de taille au plus 12 (ligne 67). La fiche de faisabilité liste huit types issus du système d'extraction BioREx : `Association`, `Positive_Correlation`, `Negative_Correlation`, `Co-treatment`, `Drug_interaction`, `Comparison`, `Conversion`, `Binding`. Une seule paire de polarités opposées existe (`Positive_Correlation` / `Negative_Correlation`).
Pourquoi : le critère « chute d'au moins 50 % » fait partie de la porte 1 ; tel qu'écrit, il n'est pas calculable. Réécrit sur la seule paire réelle, il ne touche qu'une fraction des arêtes (non chiffrée) : un signal porté par `Association` ou `Binding` ne peut pas chuter, ce qui biaise le test vers « pas de chute » (donc vers « non concluant » ou « réfuté », voir B6) quelle que soit la vérité.
Correction attendue : figer l'alphabet réel (`T = 8`), la ou les paires permutées, la proportion d'arêtes concernée (à compter avant lecture des sorties), le nombre de permutations et leur agrégation ; envisager la garde de Fable (permutation de tous les types à degrés constants, voir M5) comme contrôle principal.

**B5 — La porte 1 exige un gain d'aire sous la courbe incompatible avec l'effet prédit (lignes 46, 88, 121).**
Constat : la porte 1 exige à la fois un rapport de cotes d'interaction d'au moins 1,15 par écart type et un gain d'aire sous la courbe hors échantillon d'au moins +0,020 ; la réfutation est prononcée si ce gain est inférieur à +0,005.
Pourquoi : ordre de grandeur recalculé (approximation binormale, prédicteurs indépendants de la base) : un terme de logarithme de cote 0,14 ajouté à une base d'aire 0,60 / 0,70 / 0,80 donne un gain de 0,007 / 0,003 / 0,002 ; même en ajoutant aussi l'effet principal du score serrure-clé (logarithme de cote 0,18), le gain vaut 0,018 / 0,008 / 0,004. Au seuil d'effet prédit, la porte 1 échoue donc presque sûrement, et la ligne « réfuté » (gain < +0,005) peut être prononcée alors que l'effet prédit est vrai. Le texte ne dit pas non plus si le modèle complet ajoute l'effet principal du score ou seulement l'interaction.
Correction attendue : rendre cohérents seuil d'effet et seuil de gain (calcul de puissance pour le gain lui-même, ou retrait du gain de la porte et de la réfutation), et définir exactement le modèle complet.

**B6 — Règles de réfutation et de lecture du volet B contradictoires (lignes 48, 88, 120, 121).**
Constat : (i) réfutation selon la ligne 48 : rapport de cotes < 1,05 en estimation, ou gain < +0,005, ou coefficient permuté > 0,80 fois l'original ; selon la ligne 121 : borne supérieure à 95 % < 1,15, ou gain < +0,005, avec au moins 5 000 ponts. (ii) Une chute sous permutation inférieure à 20 % est « réfuté » selon la ligne 48 et « non concluant — confusion topologique » selon la ligne 120. (iii) Une chute entre 20 % et 50 % n'a pas d'issue.
Pourquoi : une même observation reçoit deux verdicts, au choix du lecteur après coup.
Correction attendue : une seule règle par issue, reportée à l'identique dans la section des prédictions et dans la table.

### Majeurs

**M1 — Contraste principal du volet B donné par trois règles (lignes 46, 102).**
Constat : ligne 46, fécond contre « pont mort-né » (zéro reprise) ; ligne 102, d'abord une règle conditionnelle (exclusion des cas intermédiaires si la prévalence dépasse 15 %, sinon trois et plus contre moins de trois), puis une « règle unique gelée » : trois et plus contre zéro à deux, sans exclusion.
Pourquoi : la dernière phrase tranche sans doute, mais la règle conditionnelle et la ligne 46 restent dans un texte scellé et ouvrent une lecture alternative.
Correction attendue : ne garder qu'une règle, et aligner la ligne 46 et la proposition B (ligne 28).

**M2 — Multiplicité incohérente : le niveau 0,0125 n'entre dans aucune porte (lignes 86-90).**
Constat : le niveau unilatéral 0,0125 équivaut bien à la borne basse d'un intervalle bilatéral à 97,5 % au-dessus de 1, mais les portes n'emploient que des bornes à 95 % au-dessus de 1,05, 1,08 et 1,25 ; « utilisée conjointement » ne dit pas si la borne à 97,5 % est exigée en plus. La séquence à porte fixe rend par ailleurs inutile la division du niveau (double correction, conservatrice). Le « seuil durci 0,005 si testée isolément » pour le volet C (ligne 90) ne dit pas quand le volet C serait testé seul : cela ouvre un chemin après coup si les portes 1 ou 2 échouent.
Correction attendue : une seule règle de décision par porte (quel intervalle, quel niveau, quelle borne), et soit supprimer le test isolé du volet C, soit fixer d'avance quand il a lieu.

**M3 — Puissance calculée pour la significativité, pas pour les portes (lignes 105-108).**
Constat, calculs refaits : erreur type 1/√(500 × 0,85) = 0,0485 ; z à 0,0125 unilatéral = 2,241 ; puissance pour un rapport de cotes de 1,15 : 0,739 à 5 000 ponts (exact) et 0,967 à 10 000 ponts (le texte dit 0,94, sous-estimation sans conséquence). Mais la porte 1 exige en plus l'estimation ponctuelle au moins égale à 1,15 (probabilité 0,5 si l'effet vrai vaut 1,15) et la borne basse à 95 % au-dessus de 1,05 (probabilité 0,47 à 5 000 ponts, 0,76 à 10 000), plus le gain d'aire (B5) et la chute sous permutation (B4) : la puissance réelle de la porte 1 au seuil prédit est inférieure à 0,5. Même structure pour les portes 2 et 3 (volet C : erreur type du logarithme du rapport ≈ √(1/300 + 1/1 400) = 0,064, borne basse > 1,25 atteinte avec probabilité 0,82, conjointe à l'estimation ≥ 1,50 : environ 0,5). La puissance « > 0,98 » du volet A n'a pas d'effectif déclaré (part des cas dans le tiers éloigné inconnue). L'effectif « au moins 5 000 ponts » est une supposition non vérifiée (voir m5) ; l'effet de grappe (concepts partagés entre ponts) et l'inflation par les covariables ne sont pas comptés.
Correction attendue : calculer la puissance de chaque porte telle qu'elle est définie (conjonction comprise), sous l'effet prédit, et justifier l'effectif par un comptage aveugle aux sorties ou le déclarer hypothèse.

**M4 — Témoins du volet A choisis sur le futur (ligne 101).**
Constat : les témoins sont des paires « jamais connectées jusqu'en 2025 », alors que les cas naissent en 2011-2015.
Pourquoi : les paires nées en 2016-2025 sont exclues des témoins ; si la compatibilité structurelle prédit la naissance en général, ce retrait appauvrit les témoins en paires compatibles et gonfle le rapport de cotes. L'échantillonnage sur l'ensemble à risque à la date de naissance du cas (ou au 31 décembre 2015) est la forme sans ce biais ; la réponse de Fable (section 4) parlait d'« échantillonnage cas-témoins de l'ensemble à risque ».
Correction attendue : définir les témoins par l'ensemble à risque à une date fixée, sans condition postérieure à la fenêtre de naissance, ou justifier le choix et en chiffrer le biais sur monde planté.

**M5 — Gardes de Fable perdues ou déplacées ; règle R5 non tenue pour la liste d'arrêt (lignes 47, 91-94, 133-141).**
Constat : (i) Fable demandait (section 7, « Gardes ») que, sur un monde planté de paires d'équivalence connue, le score retrouve ces paires : aucune épreuve ne vérifie que la correspondance φ* retrouve une correspondance plantée (précision exigée), alors que tout le volet C en dépend ; (ii) Fable demandait la permutation de tous les types à degrés constants, l'effet devant disparaître pour A, B et C ; le texte la remplace par une permutation partielle des polarités sur le seul volet B ; (iii) la règle R5 exige que chaque garde soit testée sur un cas sain et sur un artefact : rien n'est dit pour les gardes 1, 3, 4, 5, 6 et 7 ; (iv) aucun monde ne teste le test de permutation lui-même (un monde où le signal est topologique non signé doit donner « pas de chute ») ; (v) les tailles d'effet plantées, la taille des mondes et le nombre de répétitions ne sont pas fixés, de sorte que « confirmation » et « rejet » sur mondes plantés n'ont pas de sévérité connue (voir B1).
Correction attendue : rétablir ou justifier l'abandon des deux gardes de Fable ; une épreuve sain/artefact par garde ; tailles d'effet plantées proches des seuils prédits, et nombre de répétitions par monde.

**M6 — Le volet C ne sépare pas « après naissance » de « paires alignées en général » ; proximité de surface non ajustée (lignes 29, 52, 103, 118).**
Constat : la comparaison intra-pont aligné contre croisé élimine la célébrité du pont, mais pas l'hypothèse concurrente que des voisins de même rôle se lient davantage, pont né ou non. Aucun témoin « paire jamais pontée » avec la même construction de φ* n'est prévu. La réponse de Fable (section 7, C) exigeait d'apparier aussi sur la proximité de surface ; le texte n'ajuste que le produit des degrés et la compatibilité des catégories.
Pourquoi : le verdict « confirmé » inscrit un « générateur de cascades » (ligne 118), lecture causale que ce plan ne soutient pas ; et les paires alignées, de même rôle, sont probablement aussi plus proches en usage, ce qui suffit à produire l'effet.
Correction attendue : ajuster sur la distance de surface entre u et φ*(u) ; ajouter un témoin sur des paires (a, b) appariées non nées (différence de différences), ou restreindre la revendication à une association.

**M7 — Opérateur central non reproductible : transport de Gromov-Wasserstein fusionné et algorithme hongrois (lignes 69-73).**
Constat : le coût local est « complété par un pas de transport quadratique » de poids 0,50, puis l'affectation est faite « par l'algorithme hongrois exact » ; le coût `C^FGW` utilisé dans le score n'est jamais défini. On ne sait pas si l'algorithme hongrois opère sur le coût linéaire, sur une linéarisation au point du transport, ou sur le couplage du transport. Le solveur, son initialisation, la régularisation, la mesure de discordance des relations internes et le « poids d'évidence » qui choisit les 32 voisins ne sont pas fixés (ex aequo compris).
Correction attendue : définition fermée de `C^FGW`, de la procédure d'affectation et de chaque paramètre, avec la version de la bibliothèque.

**M8 — Orientation des arêtes supposée sans fondement (lignes 67-68).**
Constat : la signature de rôle compte quatre orientations de chemins de longueur 2. Le fichier de relations donne un « premier concept » et un « second concept » (fiche, section 3) ; rien n'établit que cet ordre porte un sens (la plupart des types BioREx sont symétriques : association, corrélation, liaison, co-traitement, interaction, comparaison).
Pourquoi : si l'ordre suit une convention (par exemple le type d'entité), la moitié de la signature encode cette convention et non un rôle.
Correction attendue : établir (sur la documentation, sans lire de sortie) si l'ordre est sémantique, par type ; sinon une signature non orientée (dimension réduite) ou orientée seulement pour les types orientés.

**M9 — « Naissance d'un pont » non définie (lignes 25-29, 52, 101-103).**
Constat : l'éligibilité se fait sur la co-mention (aucune co-mention jusqu'en 2010) mais le pont est tantôt « pont direct », tantôt « nouvelles relations directes ». On ne sait pas si la naissance est la première co-mention ou la première relation typée extraite, ni pour les ponts (volets A et B) ni pour les liens du cortège (volet C).
Correction attendue : une définition unique, par volet, de l'évènement compté et de sa date.

**M10 — Volet A : entités sans relation typée admises, score non défini (lignes 59, 64, 101, 140).**
Constat : l'éligibilité du volet A demande seulement 5 mentions et l'absence de co-mention ; aucun minimum de relations typées. Pour une entité sans voisin typé, la signature est un vecteur nul (normalisation impossible) et `m = 0` (division par zéro dans le score). La garde 6 arrête alors le run sur un `NaN`. La réponse de Fable exigeait « vingt relations au moins chacun » ; les volets B et C exigent 4 voisins.
Correction attendue : un seuil de relations typées pour le volet A, déclaré comme écart à Fable s'il diffère de 20.

**M11 — Table des critères de lecture non exhaustive (lignes 116-122).**
Constat : sans issue : porte 1 franchie et porte 2 non franchie ; porte 1 non franchie mais porte 2 ou 3 au-dessus de leurs seuils ; effectif entre 2 000 et 5 000 ponts sans franchissement ; échec de porte sans atteindre les critères de réfutation (par exemple rapport de cotes d'interaction 1,10, borne supérieure au-dessus de 1,15). La lecture de Fable « si A tient et B échoue, H1 tombe, H3 reste » est rendue impossible par la séquence à porte fixe (le volet A n'est plus alors que descriptif), sans que l'écart soit déclaré. La ligne « porte 3 non franchie » est lue « cortège réfuté », alors que la réfutation du volet C (ligne 53) exige une borne supérieure < 1,30 ou une estimation ≤ 1,10 : un rapport de 1,40 n'est ni franchi ni réfuté.
Correction attendue : table couvrant toutes les combinaisons, avec « non concluant » explicite pour les zones intermédiaires, et écart à la lecture de Fable déclaré.

### Moyens

**m1 — Rééchantillonnage par grappes de ponts (ligne 80).** Les ponts partagent des concepts (un même a dans plusieurs ponts ; une même paire (u, v) alignée dans un pont et croisée dans un autre), d'où une dépendance non captée ; Fable prévoyait un rééchantillonnage par concept. La méthode d'intervalle (percentiles, correction de biais) n'est pas choisie ; 1 000 répliques laissent 12 points dans une queue à 1,25 %. Correction attendue : unité de grappe justifiée (ou double grappe), méthode fixée, nombre de répliques adapté au niveau.

**m2 — Validation croisée et intervalle du gain d'aire (ligne 78).** « Composante d'entité principale » non définie ; « si disjointisable, sinon bootstrap groupé bidimensionnel » laisse un choix après coup ; la manière d'obtenir la borne basse du gain (ligne 88) n'est pas dite.

**m3 — Tiers éloigné du volet A (lignes 27, 41, 101).** On ne sait pas sur quelle population les tiers sont calculés (ensemble à risque, cas et témoins tirés, cas seuls), ni comment la restriction au tiers traite des ensembles appariés dont le cas et les témoins tombent dans des tiers différents (régression conditionnelle). « Régression logistique conditionnelle » et « plan stratifié » (ligne 101) sont deux plans distincts.

**m4 — Score principal ambigu (lignes 41, 74, 118).** Le volet A ajuste le score brut sur la moyenne des 100 graphes réécrits ; la lecture inscrit le score résidualisé. Préciser lequel entre dans chaque modèle. Fable standardisait par l'écart type sous réécriture (score z) ; le résidu non standardisé est un écart à déclarer.

**m5 — Effectifs et coût de calcul non vérifiés (lignes 64, 101, 107 ; fiche section 4).** Le graphe de co-mention de PubMed est très dense : l'exigence d'une distance de plus court chemin d'au moins 3 peut laisser peu de ponts, surtout combinée à 4 voisins typés de chaque côté. Le coût (100 graphes réécrits, signatures recalculées, un transport par paire et par graphe réécrit, soit de l'ordre de 10⁷ transports) n'est pas estimé contre 4 cœurs et 15 gigaoctets. Correction attendue : comptage d'effectifs aveugle aux sorties et estimation de durée avant scellement, ou déclaration explicite.

**m6 — Fichier des annotations non examiné (lignes 59, 62, 100).** Les mentions et co-mentions demandent `bioconcepts2pubtator3`, que la fiche de faisabilité n'a pas examiné (taille, colonnes, place disque).

**m7 — Covariable de chaînage de Swanson identiquement nulle (lignes 46, 64).** Une relation extraite implique la co-mention dans le même article ; si la distance de co-mention est au moins 3, aucun chemin à trois termes n'existe dans le graphe des relations. La covariable vaut zéro partout dans le volet A, et l'ajustement « au-delà des chemins courts de co-mention » (ligne 27) est vide. Pour le volet B, préciser si la même éligibilité s'applique. Une variance nulle déclencherait aussi la garde 6 si la covariable est comptée comme prédicteur principal.

**m8 — Fenêtres et ensembles du volet C (lignes 29, 103).** Les liens formés entre t_pont et 2015 ne sont ni comptés ni exclus explicitement ; « m(m−1) (ou |N_a||N_b| − m) » laisse deux ensembles de paires croisées au choix.

**m9 — Synonymes et orthologues (lignes 128, 139).** La garde 5 suppose un identifiant « National Center for Biotechnology Information » pour toutes les entités, alors que maladies et composés sont normalisés autrement (vocabulaire d'indexation de PubMed). Des gènes orthologues d'espèces différentes (identifiants distincts, rôles identiques) seraient alignés par φ* et liés ensuite : inflation possible du cortège. Le soupçon de la ligne 128 (« fusionnés après 2015 ») ne peut pas se produire dans un instantané unique normalisé aujourd'hui. Correction attendue : règle de fusion ou d'exclusion figée, garde testée sur artefact.

**m10 — Audit de symétrie asymétrique (lignes 126-129, règle R4).** Les déclencheurs couvrent l'excès positif et le nul exact, pas l'inverse franc (par exemple rapport de cotes ≤ 0,5) ni un passage trop parfait des mondes plantés ; « audit indépendant » ne dit pas par qui (agent neuf ?).

**m11 — Limites de Fable non reprises.** Un seul domaine, fécondité distincte de l'intérêt, bruit d'extraction, identifiants et modèle d'extraction d'aujourd'hui appliqués au passé (fuite possible du futur) : aucune n'est déclarée dans le texte.

**m12 — La table prescrit des actions sur l'organisme et le programme (lignes 118-122).** « Inscription comme opérateurs validés », « passage obligatoire aux hyperarêtes », « imposer un typage d'ordre supérieur » : ce sont des nœuds de Lazar (modification d'hypothèse, dégel). La table devrait dire « recommandation soumise à Lazar ».

### Mineurs

**n1 — Empreinte de `CLAUDE.md` (ligne 10).** Citée `0fee605b…`, actuelle `dcd1e7ce…` (dernier commit qui le touche : `30242718a`, 2026-11-24 04:44Z, postérieur au brouillon). Évolution datée, non bloquante ; à mettre à jour au scellement ou à déclarer comme version de référence. Les trois documents de `docs/` concordent (`9261932a…`, `2fd63bad…`, `a7d6846d…`), de même que `prereg.py` (`3b2e3ee5…`) et les trois notes citées (`88d80f76…`, `e7bf754c…`, `f744320d…`).

**n2 — Commit de référence `a852992b…` (ligne 7) non vérifiable ici.** Le clone local est superficiel et ne contient pas cet objet ; `registres/decisions.md` (R-5203) le nomme comme point de reprise de `main`. Le gabarit demande le commit du code d'analyse, pas du dépôt (voir B1).

**n3 — Graines (ligne 112).** Entropie racine fixée, conforme à R9 dans le principe ; l'ordre et le nombre d'enfants de `spawn` par tâche ne sont pas fixés (l'attribution dépend de l'ordre du code), et le manifeste par run (configuration, versions, commit) n'est pas mentionné.

**n4 — Pénalisation et optimiseur (lignes 77, 140).** λ = 10⁻⁴ dépend de la normalisation de la vraisemblance (somme ou moyenne) ; l'optimiseur n'est pas nommé ; 100 itérations peuvent ne pas suffire sur ces effectifs et arrêter le run pour une raison technique.

**n5 — Rang de l'épreuve (ligne 3).** Le texte dit « épreuve de rang 1 du lot 8 » ; GO-2026-11-23-37 parle de « l'étalonnage court du Rang 4 (Gu et Krenn / PubTator 3) ». À aligner, et à dire si l'objet autorisé est un étalonnage court ou l'épreuve décisive.

**n6 — Sigles non développés.** `AUC`, `FGW`, `F_org`, `C5` apparaissent sans développement ou seulement en partie (consigne de `CLAUDE.md`).

**n7 — Écarts à Fable non déclarés.** Seuil d'entités (5 mentions contre 20 relations), 4 témoins au lieu de 20, distance de surface par cosinus d'un plongement au lieu d'un modèle de surface logistique, score résiduel au lieu d'un score z, ajout des exigences de gain d'aire et de chute sous permutation au volet B, seuils de portes plus durs que « borne basse au-dessus de 1 (A, C) ou de 0 (B) ». Chacun peut se défendre ; aucun n'est déclaré comme écart.

## Fidélité à l'idée d'origine (synthèse)

- Volet A : signe et seuil (rapport de cotes par écart type ≥ 1,2 dans le tiers le plus surprenant) fidèles ; construction de la surprise et du score changée (n7, m4) ; témoins réduits et biaisés (M4) ; entités sans minimum de relations (M10).
- Volet B : Fable prédit seulement un coefficient d'interaction positif ; le texte ajoute un seuil de 1,15, un gain d'aire (incompatible, B5), une chute sous permutation des polarités (B4), et change la fécondité (B3).
- Volet C : rapport ≥ 1,5 fidèle ; appariement sur la proximité de surface perdu (M6) ; borne basse durcie à 1,25.
- Gardes : épreuve de recouvrement des correspondances plantées absente ; permutation de tous les types remplacée (M5).
- Lecture : « A tient, B échoue » rendu non lisible par la séquence à porte fixe (M11).

## Provenance de la conception (constat, sans trancher)

Le texte est écrit par un sous-agent Carbon (modèle de Google) en effort élevé (lignes 3 et 5). `CLAUDE.md` (« Qui conçoit », « Économie de Fable », « Dosage ») réserve les préenregistrements décisifs à Fable 5.2, en effort maximal. Le texte cite GO-2026-11-23-33 ; `registres/go.md` l'inscrit bien : Carbon élevé autorisé sur les classes A, B et C « en remplacement temporaire de Fable et d'Opus », avec un « écart déclaré à "Qui conçoit" », échéance 2026-11-30. GO-2026-11-23-38 (22:13-22:18Z) a ensuite remplacé Carbon par les sous-agents Opus de la nouvelle mère ; le brouillon est daté 21:58Z, donc avant. Le texte ne nomme pas lui-même l'écart à « Qui conçoit ». Le contre-lecteur (Opus 5.5) est bien d'un autre modèle que l'auteur.

## Conformité au gabarit et au validateur

- Huit sections du gabarit présentes et dans l'ordre ; en-tête complet.
- Validateur exécuté : `['section vide ou à remplir : Contre-lecture']` — seul défaut, attendu à ce stade.
- Le champ du gabarit « Commit du code d'analyse » est rempli par un commit du dépôt, sans code d'analyse existant (B1, n2).

## Ce que je n'ai pas pu vérifier

- Le commit `a852992b…` (absent du clone superficiel ; pas de récupération réseau permise).
- Le script `epreuve_plantee_pubtator3_v1.py` : absent (B1) ; donc ni les mondes plantés, ni les gardes, ni leurs épreuves.
- Le contenu réel des fichiers de PubTator 3 : sens de l'ordre des deux concepts dans `relation2pubtator3`, couverture (résumés seuls ou textes intégraux), taille et colonnes de `bioconcepts2pubtator3`, schémas de normalisation par type d'entité (constat m9 fondé sur ma connaissance générale, à vérifier sur la documentation).
- Les champs de date de PubMed et la faisabilité d'une récolte exhaustive des dates et des auteurs par les utilitaires publics.
- Les effectifs réels (ponts éligibles, part dans le tiers éloigné, voisins par pont) et le temps de calcul.
- Les calculs d'aire sous la courbe de B5 sont des ordres de grandeur sous approximation binormale et prédicteurs indépendants de la base ; une corrélation avec la base réduirait encore le gain.
- Le registre complet des idées du lot 8 et le rapport de priorisation (seule la fiche extraite a été lue) ; le contenu de la décision N-058 au-delà de son résumé dans `CLAUDE.md` (le lien qu'en fait la ligne 33 n'a pas été vérifié).
- Les références [27] et [45] de la réponse de Fable.
