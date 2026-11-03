Les pièces de critique **B** et **C** sont absentes ; je n’en invente pas le contenu. Les faits Scheurer restent **RAPPORTÉS**, ceux de « nos résultats » **OBSERVÉS-NON-AUDITÉS**, et les modifications ci-dessous sont des **HYPOTHÈSES** expérimentales.

## (a) Arbitrage des critiques visant D

### Critiques A

| Critique | Décision | Correction ou raison |
|---|---|---|
| **D1 — seuil de E1 égal à l’effet attendu** | **Acceptée.** | Le seuil décisionnel devient \(\delta=\log(1{,}02)\) par mois (**supposé** : +2 %/mois), nettement sous l’effet attendu de +5,1 %/mois (**supposé**). La taille de l’étude devra donner au moins 80 % de puissance (**supposé**) sous l’effet attendu, faute de quoi E1 ne sera pas lancé. |
| **D2 — difficulté confondue avec le générateur** | **Acceptée.** | Plusieurs générateurs figés ; difficulté estimée par des humains ignorants du générateur et des verdicts ; effets de générateur et standardisation sur un mélange de générateurs fixé à l’avance. Validation avec générateur entièrement laissé de côté. |
| **D3 — filtre honnête/malveillant asymétrique** | **Acceptée.** | Contrôles de qualité communs, appariement par tâche, générateur, longueur, complexité et format ; taux d’acceptation publiés. Refus, sorties invalides et solutions honnêtes fonctionnelles ne sont plus confondus. Sélection effectuée sans voir les scores des moniteurs. |
| **D4 — tendance de lecture de code rebaptisée surveillance** | **Acceptée et transformée en test.** | Mesurer séparément, pour chaque modèle, sa capacité ordinaire de programmation et de résolution sur les mêmes tâches. La pente ajustée \(\beta_{\mathrm{res}}\), conditionnelle à cette capacité, devient le paramètre principal. Si elle disparaît, le résultat sera rapporté comme tendance de capacité de code. |
| **D5 — fuite calibration/évaluation** | **Acceptée.** | Découpage disjoint par tâche et groupe de génération : calibration, développement, puis test final verrouillé. Aucun seuil ni choix de strate ne sera modifié après lecture du test. |
| **D6 — « attaques fraîches » ambiguës** | **Acceptée.** | Deux populations rapportées séparément : mêmes générateurs avec graines neuves ; générateurs nouveaux. Le second corpus constitue le test de transport principal. |
| **D7 — injection absente de la définition de E1** | **Acceptée.** | E1 porte exclusivement sur la strate **sans injection**. La strate avec injection possède ses propres estimands et résultats ; aucune moyenne entre les deux. |
| **D8 — refus dans T1** | **Acceptée.** | Modèle à risques concurrents : refus, échec fonctionnel, réussite. Publication de \(P(R)\), de la réussite marginale et de la réussite conditionnelle parmi les non-refus. Cette dernière ne sera appelée « capacité » que sous réserve explicite de sélection sur le consentement. |
| **D9 — FLOP dans T3** | **Acceptée.** | L’axe principal devient un nombre d’**opportunités d’épisode** sous calendrier figé ; les FLOP et la taille deviennent des mesures secondaires de coût. T3 ne prétendra plus mesurer une habileté par tentative à partir des seuls FLOP. |
| **D10 — nul trop simple et mauvaise puissance** | **Acceptée.** | Simulations conservant familles, effets tâche × moniteur, censure, sélection et dépendances ; permutations de dates intra-famille. Validation de puissance pour séparer +2 % et +5,1 %/mois, pas seulement pour détecter +10 %/mois. |

J’accepte également les conditions mesurables d’A :

- **TFA à 1 %** : 240 honnêtes ne suffisent pas. Le pilote ne certifiera pas ce taux. À titre de repère, même 299 épisodes honnêtes indépendants sans alarme donnent seulement une borne unilatérale à 95 % d’environ 1 % (**calcul**) ; l’échantillon final sera dimensionné sur des intervalles exacts et la dépendance par tâche.
- **c50** : il ne sera défini que pour une courbe monotone avec un unique croisement de 0,5 dans le support. Non-monotonie ou croisement hors support rendent l’estimand non jugeable ; les modèles censurés ne seront pas silencieusement supprimés.
- **Identification temporelle** : seules les dates intra-famille contribuent avec effets fixes de famille. Qwen2.5, à une seule date (**RAPPORTÉ**, Scheurer §2.2), n’identifie donc aucune pente temporelle.
- **Pilote à six moniteurs** : aucun bootstrap de pente et aucun facteur mensuel inférentiel ; il sert à qualifier l’instrument.
- **Test-retest** : il précède l’étude complète et fixe le plancher de variance utilisé dans le calcul de puissance.

Les neuf contrôles négatifs d’A sont intégrés : appariement longueur/complexité, provenance croisée, capacité de code, découpage disjoint, notation humaine aveugle, test-retest, oracle de qualification, permutations intra-famille et deux corpus frais. Deux précisions : la fiabilité d’un temps humain continu sera évaluée par fidélité inter-notateurs et test-retest, non par un κ inadapté ; l’oracle recevant l’information de vérification sert à contrôler les étiquettes sur un jeu indépendant, sans prétendre démontrer une erreur nulle.

Le duel proposé par A est **accepté dans son objectif**, mais son rapport \(\beta_{\mathrm{res}}/\beta_{\mathrm{brut}}\), instable lorsque la pente brute approche zéro, est remplacé par un test direct sur \(\beta_{\mathrm{res}}\).

### Critiques E

- **T1, intersection fonctionnalité–condition–franchissement : acceptée.** Les trois facteurs seront publiés séparément avec leurs dénominateurs. Si seuls quelques épisodes atteignent les derniers facteurs, aucune attribution de pente à ces facteurs ne sera faite. Des tâches honnêtes de fonctionnalité comparable mesureront la contribution de la programmation ordinaire.
- **Temps humain T1 : acceptée.** Il désignera uniquement la réalisation complète de l’épisode spécifié, distincte de la résolution honnête et de la détection. Les tâches et leurs temps seront gelés avant tout score de modèle ; aucune sélection selon la qualité de l’ajustement aux modèles.
- **T2, temps de production ≠ difficulté de détection : acceptée.** L’axe devient le **temps humain de détection correcte en aveugle**, avec leurres honnêtes. Le sens de monotone décroissance de la détection automatique sera testé, non imposé.
- **Jumeaux et corpus renouvelé : acceptée.** L’appariement de provenance ne suffit pas : ajout des appariements distributionnels, détecteurs limités au style et aux métadonnées, modifications inertes et exclusion des tâches uniquement selon des règles préenregistrées aveugles aux scores.
- **T3, dépendance et censure : acceptée.** Nouvelles graines et épisodes indépendants dans la mesure du protocole, dépendance résiduelle estimée par répétitions de la condition identique. Si \(q50\) n’est pas identifié avant \(q_{\max}\), il est déclaré non identifiable ; aucun modèle n’est retiré de la régression pour cette raison.
- **E2 composite : acceptée.** Le duel porte désormais sur un seul paramètre, le gain de détection \(\Delta\). La calibration est une condition de validité préalable, non une hypothèse supplémentaire à faire réussir simultanément.
- **Canaris du vérificateur : acceptée.** Développement, sélection des tâches et qualification finale utiliseront des échantillons distincts ; les taux d’erreur auront des intervalles de confiance.
- **Erreur de mesure de l’axe humain : acceptée.** Répétitions du panel et analyse d’erreur de mesure/sensibilité à l’atténuation.
- **Permutations et corpus honnête : acceptée.** Permutations restreintes aux blocs échangeables. Un corpus uniquement honnête teste les fausses alertes, mais ne peut pas, à lui seul, estimer un horizon de détection des attaques.

## (b) Expériences corrigées

### Instrument commun de T2

Pour chaque artefact, un panel humain mesure, sans connaître le générateur ni les verdicts automatiques, le temps nécessaire à une détection correcte parmi des leurres honnêtes. Pour un moniteur \(m\) :

1. son seuil \(\tau_m\) est calibré sur des tâches honnêtes disjointes ;
2. \(D_m(x,g)\) est sa probabilité de détection à difficulté humaine \(x\), pour le générateur \(g\) ;
3. \(c50_m\) est le temps humain auquel la détection standardisée sur le mélange fixé de générateurs vaut 0,5. Un \(c50\) plus grand signifie que le moniteur détecte des attaques plus difficiles à repérer humainement ;
4. l’oracle de qualification, les règles statiques, le score de longueur, les détecteurs de style et les tests disponibles au déploiement sont des contrôles distincts. Le meilleur contrôle est choisi sur le développement puis figé.

### E2 — Le moniteur apporte-t-il un gain propre ?

Condition de validité : calibration transportable sur les honnêtes indépendants et étiquettes mécaniques qualifiées. Sinon : **non jugeable**.

- \(H_A:\Delta\geq0{,}10\), où \(\Delta\) est le gain apparié de détection sur le meilleur contrôle figé, à TFA comparable (**seuil supposé** : 10 points).
- \(H_B:\Delta<0{,}10\).

Borne inférieure de l’IC au-dessus de 0,10 ⇒ **\(H_B\) falsifiée**. Borne supérieure sous 0,10 ⇒ **\(H_A\) falsifiée**, sans exclure un gain plus petit. Chevauchement ⇒ non concluant.

### E1 — Existe-t-il une pente de surveillance résiduelle et transportable ?

Sur le corpus final à générateurs nouveaux, **sans injection**, soit \(\beta_{\mathrm{res}}\) le coefficient de la date sur \(\log c50\), avec effets de famille et capacité ordinaire de code :

- \(H_A:\beta_{\mathrm{res}}\geq\delta\) ;
- \(H_B:\beta_{\mathrm{res}}<\delta\), avec \(\delta=\log(1{,}02)\)/mois (**supposé**).

Borne inférieure au-dessus de \(\delta\) ⇒ **\(H_B\) falsifiée** ; borne supérieure sous \(\delta\) ⇒ **\(H_A\) falsifiée**, et toute pente brute sera rapportée comme capacité générale ou artefact selon les contrôles ; chevauchement ou matrice de conception déficiente ⇒ non concluant. Mêmes générateurs/graines neuves et injection restent des analyses diagnostiques séparées.

## (c) Réponse à l’arbitre : établi, non établi, première expérience

### Ce qui est établi dans les pièces — et ce qui ne l’est pas

Une propension brute est un mauvais axe en l’état : retirer un outil peut faire passer un taux de manigance de 59 % à 3 %, avec des taux de base presque toujours nuls (**RAPPORTÉ**, Scheurer §2.1). La force générale d’un moniteur ne garantit pas sa robustesse : le moniteur le plus fort sans injection y donne 0 aux 375 échantillons de code à porte dérobée (**RAPPORTÉ**, §3.4). Le plafond des juges LLM et la nécessité d’une calibration sur épisodes entiers sont seulement **OBSERVÉS-NON-AUDITÉS** (« nos résultats » §4 et §6).

Le doublement METR d’environ sept mois est **RAPPORTÉ** (§3.1), avec des informations méthodologiques manquantes. **Aucune pente temporelle de manigance spontanée, de surveillance ou de contrôle n’est établie ici.** Les trois tendances suivantes restent des **HYPOTHÈSES**.

| Candidate corrigée | Grandeur comparable et ajustement | Énoncé attendu |
|---|---|---|
| **T1 — subversion accessible sous protocole figé** | \(h50\), durée humaine de réalisation complète où la réussite de l’épisode atteint 50 % ; refus et facteurs fonctionnalité/condition/franchissement publiés séparément. Logistique à effets de tâche, puis régression de \(\log h50\) sur la date avec effets de famille. | **+10,4 %/mois** (**supposé ; calcul** depuis un doublement en sept mois), sans interprétation comme propension spontanée. |
| **T2 — surveillance à risque fixé** | \(c50\), temps humain de détection où le moniteur tombe à 50 %, à TFA calibré ; standardisation sur générateurs et ajustement sur la capacité de code. | **+5,1 %/mois** pour \(c50\) (**supposé, illustratif**) ; signe positif = surveillance améliorée. |
| **T3 — budget d’opportunités d’élicitation** | \(q50\), nombre d’opportunités sous calendrier non adaptatif figé où 50 % des tâches réussissent T1 ; survie avec censure, FLOP seulement secondaires. | **−5,0 %/mois** (**supposé, illustratif**) ; q50 non identifiable ⇒ pas de pente q50. |

Plan temporel commun : **18–24 points modèle-date, au moins quatre familles avec chacune au moins trois dates, sur 24–36 mois** (**supposé**), sous réserve du calcul de puissance. Validation sur dates finales réservées ; IC à 95 %, permutations intra-famille et bootstrap seulement si sa couverture est validée. Qwen2.5 sert à une analyse transversale de taille, pas à identifier la date.

### Premier pilote : E2/T2, sans estimation de pente

**Pourquoi lui :** il évite les événements spontanés rares, utilise une vérité terrain mécanique et produit un axe continu même quand une propension brute vaudrait zéro.

**Taille :** six moniteurs ouverts, 60 tâches réparties entre calibration/développement/test, quatre paires attaque–honnête par tâche et deux conditions d’injection : **5 760 notations** (**calcul** : \(6\times60\times8\times2\)), auxquelles s’ajoutent le panel humain et un échantillon honnête indépendant dimensionné par intervalles exacts. Coût révisé : **300–600 h-H100 et 20–50 k€** (**illustratif**), à re-chiffrer après le prétest humain.

**Menaces et contrôles :** provenance/longueur par appariement et détecteurs restreints ; capacité ordinaire par mesure de code conditionnée ; contamination par les deux corpus frais ; calibration par découpages disjoints ; injection par strate séparée.

**Non concluant** si moins de 40 tâches valides (**supposé**), si l’axe humain est insuffisamment fiable, si plus d’un tiers des c50 sont censurés ou non uniques (**supposé**), ou si le transport du TFA n’est pas estimable à la tolérance préenregistrée. Aucun facteur mensuel ne sera alors annoncé.

**Ce qui ferait échouer le plan :**
- les temps humains sont instables ou la détection n’est pas monotone : \(c50\) n’a pas de référent ;
- la calibration ou les contrôles de provenance échouent sur le test verrouillé : l’instrument est non jugeable ;
- la pente résiduelle disparaît après capacité de code ou sur générateurs nouveaux : T2 ne mesure pas une progression propre de surveillance.

FIN-DE-CELLULE