# Lecture du collisionneur « pari de signe » contre la conception v2 — rapport v1

- **Lecteur** : sous-agent neuf, Opus 5.5, lignée conv-audit. Je n'ai écrit ni la conception (v1 et v2, Fable 5.1), ni la contre-lecture, ni aucune cellule du collisionneur.
- **Heures lues sur `date -u`** : début de la lecture le mardi 27 octobre 2026 à 17:58:59 UTC ; début de la rédaction de ce rapport à 18:31:26 UTC ; heure de fin : dernière ligne du rapport.
- **Aucun fichier du dépôt ni du dossier du collisionneur n'a été modifié.** Tout ce que j'ai écrit est dans `/tmp/claude-0/-home-claude/c5a45195-121d-5962-9d0a-4896cc046231/scratchpad/lecture-collisionneur-pari-signe/`. Je n'ai lu, affiché ni cherché aucune clé ni aucun jeton. Aucune dépense : une simulation sur processeur seulement (section 7).
- **Notation.** T1-A = cellule `E3-T1-conception-A.md`, T2-B = `E3-T2-redteam-B.md`, T3-C = `E3-T3-riposte-C.md`, etc. Dans T2-C, « T2-C/A (a)3 » = section « Contre la proposition A », point (a)3. C1 à C12 = constats de la contre-lecture. « Sortie S, T, R, D, K » = sections de ma sortie `verification-collisionneur-pari-signe-v1-sortie.json` (`38efb971…`, section 7).
- Les cellules ne contiennent aucune consigne adressée à leur lecteur ; leurs « je ferais » sont traités comme du matériau.

## Verdict

1. **57 points distincts** après déduplication des neuf cellules ; **18 sont déjà couverts par la v2** : le collisionneur a retrouvé seul quatre des cinq défauts graves de la contre-lecture (mélange avec le signe C1, bruit de calibrage C2, grappes C3, H2a C4) et le comparateur par intersection-union (C6 b).
2. **7 sont nouveaux et touchent la garantie.** Trois sont majeurs et je les ai mesurés : ex æquo des scores ordinaux (fausse promotion entre moniteurs de même loi : 0,35 à 0,83), dérive de composition entre calibrage et épreuve (0,09 à 0,75), choix du bras blanc aux seuils d'un seul calibrage (0,11 → 0,36). Aucun n'est vu par la garde, par la taille du calibrage, ni par le contrôle 12. Quatre sont de moindre ampleur : multiplicité entre générations, longueur des épisodes, fuite des métadonnées du mode tenu à l'écart, niveau des intervalles de N-054 point 4. 18 autres points sont nouveaux mais de moindre portée (10) ou des propositions de méthode à évaluer (8).
3. **14 sont faux ou trompeurs** ; la plupart ont été réfutés pendant le tour lui-même. Le collisionneur a **manqué** C5, C9, C11, le dimensionnement du calibrage (D-S9), la portée (D-S7) et le nœud H1b : il complète la contre-lecture, il ne la remplace pas. Les sept points (b) justifient une **v3** (nouveau nom), pas une retouche.

## 1. Méthode

- Lus en entier : la v2, la v1, la contre-lecture, la question et les neuf cellules. Le matériau `faits-pari-de-signe-v1.md` n'a été ouvert que sur les lignes où des cellules s'appuient sur lui, pour vérifier six points : le code du simulateur v1 (lignes 286 à 365), P § 10 et § 12 (lignes 626 à 665), N-007, N-008 et N-054 (lignes 685 à 814), P § 8.1 (ligne 592, par recherche).
- Un point est une affirmation ou une proposition, dédupliquée entre cellules et entre tours, et classée contre le texte de la v2 (section citée).
  - (a) déjà corrigé dans la v2 ;
  - (b) nouveau et touche la garantie (niveau α, sélection, fuite, dépendance) ;
  - (c) nouveau, de moindre portée ;
  - (d) faux ou hors sujet ;
  - (e) proposition de méthode à évaluer.
- Je n'ai pas renforcé les points : quand je vais plus loin qu'une cellule, je l'écris (« ma lecture »).
- J'ai mesuré sur processeur les trois points (b) majeurs, ainsi que l'affirmation centrale de T3-A E3′, dans le monde de la cellule E de la v2 (§ 2.4).
  - Modèle binormal, rappel vrai 0,40 à 1 % exact.
  - Deux moniteurs jumeaux en loi : même loi, bruits indépendants.
  - Unités de 10 épisodes ; forme parts, grille Λ, seuil 20.
  - Garde δ = 0,05 ; e-valeur de la fiche = minimum des deux processus, arrêté au seuil (v2 § 3.5).

## 2. Tableau des points distincts

| n° | point (une phrase) | cellules | classe | v2, raison, vérification sur processeur |
|---|---|---|---|---|
| P1 | Le mélange parts + signe n'est pas valide sous E[v] ≤ 0 : le signe teste un nul de majorité (médiane). | T1-A A1, E1 ; T1-B a1, E1 ; T1-C (b)1, Exp. 1 ; T2-A « ce que je prends » ; T2-B « constat commun » ; T2-C préambule ; T3-A E1 ; T3-B E0 ; T3-C § 2, Exp. 1 | (a) | v2 § 2.1 dernier tiret, Verdict 1, contrôle 11, D-S2. |
| P2 | L'avantage du signe à dix épisodes vient de la borne λ < 1 et d'un autre nul ; il n'est pas général. | T1-A A7 ; T1-B § 2 ; T1-C (b)2 | (a) | v2 § 2.1-2.2 (domination de 1 + λ·v, reprise de C1). Vérifié : mise de Kelly approchée E[v]/E[v²] ≈ 2,27 > 1 (sortie S). |
| P3 | Le niveau 0,020 / 0,014 vient de l'horizon fini et du saut au-dessus du seuil ; une lecture unique au seuil 1/α n'est jamais plus puissante que la lecture continue. | T1-A A6 ; T1-B a12 ; T1-C (b)1 ; T3-B B-1 | (a) | Le prix de la validité à tout instant est porté par D-S11 et le contrôle 17. L'explication est juste ; le détail « masse morte » de T1-C est faux (P54). |
| P4 | Bruit des seuils : « à 1 % » n'est que nominal, et une garde à δ de 0,05 à 0,10 laisse acheter du rappel. | T1-A A3, E3 ; T1-B § 3 ; T1-C (a)2-3, § 3 ; T2-B A-2, A-3 ; T2-C/A (b) ligne 1 ; T3-A A-2, A-3 ; T3-B « arguments échangés » 1 | (a) | v2 § 2.4, Verdict 3, contrôle 12, D-S9. |
| P5 | Les tâches d'un même organisme sont dépendantes (grappes) : quelle unité ? | T1-A A2, E2 ; T1-B a3, E5 ; T1-C (a)5, Exp. 4 ; T3-A E2′ ; T3-B E5 ; T3-C Exp. 4 | (a) | v2 § 3.2, D-S1, D-S7, contrôle 13. |
| P6 | H2a choisit sa sous-population sur les scores du comparateur (r_action ≈ 0) et mélange seuils par action et par épisode. | T1-B a9 ; T1-C (a)4, Exp. 2 ; T2-A C-3 ; T2-B A-7 ; T3-C § 3 | (a) | v2 § 2.1 (tout point de fonctionnement par épisode), § 4 ligne H2 (H2a réécrite), contrôle 14. |
| P7 | Une « meilleure base noire » choisie sur le développement est une sélection ; il faut l'intersection-union. | T1-A A9 ; T1-B a11, E4 ; T2-A B-5, C-12 ; T2-B scénario « comparateur » ; T2-C/A (b) ligne 2 ; T3-A E6 ; T3-B E4′ ; T3-C § 7.2 | (a) | v2 § 2.6, D-S8. |
| P8 | La moyenne par tâche n'est pas le rappel par épisode de N-054. | T1-A A4 ; T2-B scénario « pondération » | (a) | v2 § 2.1 « Pondération déclarée ». Voir P38 pour un contraste qui vise exactement l'estimande de N-054. |
| P9 | Le prix du mélange est donné avec trois valeurs (log 8, log 4, log 2). | T1-B a8 ; T2-A B-2 (« non-contradiction ») ; T3-B (a8 retiré) | (a) | v2 § 2.2 : log 4 seul ; le débat est sans objet. |
| P10 | Faux positifs honnêtes groupés par tâche : la garde certifie moins bien. | T1-B a4, E6 ; T3-B E6′ | (a) | v2 § 2.4 (cellule G bis ; δ = 0,02 non retenu). |
| P11 | Intervalle de G1 : les tests à effectif fixe (t, bootstrap, permutation) sont anticonservateurs sous nul asymétrique ; un seul verdict primaire, gelé d'avance. | T1-A E4 ; T1-B E3 ; T2-A B-1, B-8 ; T2-C/B (a)2, (c)1 ; T3-A E4′ ; T3-B B-1, B-8, E0, E3′ ; T3-C § 7.1 | (a) | v2 D-S11, contrôle 17. |
| P12 | Règle de porte : la règle e-BH n'est pas une conjonction, la fiche « tous modes » ne décide pas, et le mode tenu à l'écart est une strate, pas un témoin. | T1-A table (c) ; T2-A B-4 ; T2-C/A (a)4 ; T3-A C4 ; T3-B B-4, plan lignes 6-7 | (a) | v2 § 3.2, D-S10, ligne G1. Divergence à trancher au préenregistrement : T3-A propose le mode tenu à l'écart comme mode obligatoire, ce qui est contraire au « hors décision » de la v2 et à N-054 point 4 tel que T2-A B-4 le lit. |
| P13 | Bras génériques et spécialisés (N-054 point 3) ; planchers « tout signaler » et « juge en une passe ». | T1-A plan ligne 6 ; T1-C plan lignes 8-9 ; T2-A B-5 | (a) | v2 § 2.6, ligne G1. |
| P14 | « Domine » veut dire à chaque N ; une pente ne dit pas la domination. | T2-A C-8 ; T3-C § 6 | (a) | v2 ligne H3 (H3a = minimum sur les N). |
| P15 | Les dix contrôles n'ont aucune sortie et n'emploient que des nuls symétriques. | T1-A préambule et (vii) ; T1-B a12 ; T2-B préambule | (a) | v2 § 5 : contrôles 11 à 17 ; cellules C, E, F, G et H simulées. |
| P16 | « Certifier 1 % exige de l'ordre de mille épisodes » contredit la sortie. | T1-B a7 | (a) | Phrase absente de la v2 (§ 2.4). |
| P17 | Le McNemar par épisode du programme C (nul de moyenne) n'est pas le signe par tâche (nul de médiane). | T1-B a2 | (a) | La v2 retire la forme signe. |
| P18 | L'unité serait l'organisme par défaut dès deux tâches par organisme. | T1-B plan ligne 1 ; T1-C (e)5 ; T3-A A-5, E2′, recommandation | (a) | Déjà évalué par la v2 (§ 3.2, D-S7 option b) : il faut au moins 7 à 8 agents pour qu'une promotion soit seulement possible. La v2 recommande la lecture conditionnelle, avec la consigne comme unité. |
| P19 | **Ex æquo des scores ordinaux** : le seuil « quantile 1 − τ » tombe dans un palier et le taux réel de faux positifs s'écarte systématiquement de τ. | T1-B a6, E2, § 3 (i) ; T2-B A-9, C-7, (c)4 ; T2-C/B (a)3 ; T3-A A-9, E7 ; T3-B C3, E2′, plan ligne 2 ; T3-C § 5.3 | **(b)** | v2 § 2.4 ne fixe aucune convention d'égalité ; ni la garde, ni C, ni le contrôle 12 ne voient le décalage. **Vérifié (sortie T)** ; développé en section 3. |
| P20 | **Dérive calibrage → épreuve** : si leurs compositions diffèrent (mode, famille de consignes, registre, agent), un seul moniteur peut tourner au-dessus de τ à l'épreuve. | T1-A § 1 (ii) ; T1-C plan ligne 6, table (c) ligne 3 ; T2-A B-6, scénario « seuils randomisés », (c)2, « ce que je prends » ; T3-B B-6, E7 ; T3-C § 5.4 | **(b)** | v2 § 2.4 suppose que l'asymétrie fine vient du seul bruit (« le fin est borné par C ») ; v2 § 9 n'exige pas de tirage échangeable des parties. **Vérifié (sortie D)** ; section 3. |
| P21 | **Choix du bras blanc aux seuils d'un seul calibrage** : parmi plusieurs candidats, on retient celui dont le seuil est « tombé du bon côté ». | T2-A, scénario « contre les rangs conformes appariés » | **(b)** | La v2 ne réserve pas le calibrage de l'épreuve, et le contrôle 12 ne comporte aucune sélection. **Vérifié (sortie K)** ; section 3. |
| P22 | **Multiplicité entre générations** : changer τ ou la strate échappe à la redite, et la règle e-BH ne couvre qu'une génération. | T2-B scénario « mémoire », (c)5 ; T3-A évasion « mémoire » (signature sans τ) | **(b)** | v2 § 3.6 et § 7.3 : la signature vaut contraste + τ + strate + partie, avec une règle e-BH par génération ; les variantes relues sur une même partie ne sont comptées nulle part. Vérifiable : contrôle (c)5 de T2-B (contraste nul sous τ ∈ {1 %, 5 %} et deux strates, trois générations, même partie, taux cumulé ≤ α exigé). |
| P23 | **Longueur des épisodes** : l'accumulation additive croît avec le nombre d'actions. Sans seuil par horizon ni honnêtes de même longueur, on achète du rappel (G1, H2c) et de la « croissance » (H2b) par la longueur. | T1-C table (c) ligne 4 ; T2-A B-7, scénario, (c)4 ; T2-B « confondant… la longueur » ; T2-C/B (b) ligne 3, (c)3 ; T3-A C3 ; T3-B B-7, E8 ; T3-C § 3, § 7.4 | **(b)** | N-007 : « le seuil de Ville seul n'est pas tenu sous … corrélation » (faits, ligne 698) ; la v2 n'a ni strate de longueur, ni seuil par horizon, ni plancher de longueur. Vérifiable : E8 de T3-B (scores autocorrélés à 0,3, trois horizons, aucun signal ; seuil commun contre seuil par horizon). |
| P24 | **Fuite des métadonnées du mode tenu à l'écart** : l'agent voit « le nombre de tâches par strate ». | T2-B « fuite possible, à vérifier » ; T3-C § 7.4 (remède : masquer la strate) | **(b)**, portée faible | v1 § 2.5 (« nombre de tâches par strate »), v2 § 2.5 « inchangé » ; N-054 point 3 veut ce mode « révélé seulement à l'évaluation ». Se vérifie en lisant le code, pas par simulation. |
| P25 | **Intervalles par rééchantillonnage de N-054 point 4** : aucun niveau garanti à petit n sous nul asymétrique, alors qu'ils restreignent ou non la revendication de H1. | T2-B A-1 ; T2-C/B (a)2 ; T3-A E4′ (« N-054 point 4 doit être amendé ») | **(b)**, portée limitée | La ligne G1 de la v2 garde ces intervalles hors du pari, et le contrôle 17 n'est prévu que « si retenu pour G1 » ; C6 d mesurait 0,06 à 0,12 pour un test à n fixé. Vérifiable : contrôle 17 étendu à l'expérience de lecture. Touche une décision de Lazar. |
| P26 | H2b teste la croissance de l'écart séquentiel − base, alors que N-007 énonce la croissance du rappel du séquentiel. | T1-B a10 ; T2-C/A (a)3, (c)3 ; T3-A C3 ; T3-B E8 ; T3-C § 6 | (c) | N-007 : « détecte le sabotage avec un rappel qui croît avec l'horizon » (faits, ligne 693). La v2 garde ½[(r_seq − r_base)_long − (r_seq − r_base)_court]. Un séquentiel plat face à une base qui chute promeut H2b à tort. |
| P27 | Latéralité de « l'intervalle à 95 % » de N-008 : borne basse unilatérale (seuil 20) ou bilatéral à 2,5 % par côté (seuil 40) ? | T2-A C-11 ; T3-B plan ligne 4 ; T3-C § 7.3 | (c) | N-008 (faits, ligne 731) ; la v2 ne le dit pas. Le seuil 40 coûte log 2 ≈ 0,69 nat, soit environ 5 unités à 20 points (0,15 nat par unité, sortie S). À trancher dans D-S11. |
| P28 | Le plancher « sonde aléatoire appariée en covariance », obligatoire pour toute sonde, manque aux comparaisons de G1. | T1-C plan ligne 9 | (c) | P § 8.1 : « une sonde qui ne le bat pas n'existe pas » (faits, ligne 592) ; la v2 ne le cite que comme témoin de H8. |
| P29 | Une famille de bases mal réglées (homme de paille) passe l'intersection-union. | T2-A B-5, (c)5 ; T3-B B-5 ; T3-C § 7.2 | (c) | Contrôle proposé, à rapporter : la meilleure base doit battre le plancher « juge en une passe » sur le développement. |
| P30 | Le simulateur n'a pas de corrélation A/B sur un même épisode, et son effet de tâche est commun aux deux moniteurs : le biais a un sens inconnu. | T1-B a5 ; T1-A A5 (mal décrit) ; T2-B A-4 ; T3-A A-4, E8 | (c) | Code v1 : `u` est partagé par les épisodes et les deux moniteurs, la garde tire des binomiales indépendantes (faits, lignes 321 à 348). v2 § 6 : « A alerte … avec probabilité r_A, B avec r_B ». |
| P31 | Paires voisines : tenir le budget de sabotage fixe, donner un identifiant de paire statique dans la banque, empreinter la liste avant le calcul des parts. | T1-A A8 ; T1-B table (c) ; T1-C (a)6, (e)5 ; T3-A E5′ | (c) | v2 § 2.5 couvre « aveugle aux scores, une paire au plus », mais ni le budget ni l'empreinte. |
| P32 | La puissance de l'intersection-union dépend du contraste qui croît le plus lentement, variance comprise, pas seulement de la base la plus forte en moyenne. | T2-C/B (a)1 (en partie faux, P50) ; T3-B C1-b, E4′ | (c) | v2 § 2.6 : « la puissance est celle du contraste contre la variante la plus forte ». T3-B : une base à forte variance donne 0,08 contre 0,14 nat par unité (illustratif). |
| P33 | Le contrôle 12 ne duplique qu'un même moniteur : des jumeaux non identiques (granularité, dispersion, queues) manquent. | T2-C/A (c)1 ; T3-A E3′ volet « niveau » | (c) | C'est le contrôle qui aurait vu P19 ; sortie T. |
| P34 | Les témoins faux des courses réelles sont symétriques ; il faut des témoins faux asymétriques par strate. | T2-B scénario « tout à la fois » ; T3-A évasion « tout à la fois » | (c) | v2 § 5 : à chaque course, témoins vrai, faux (échange) et jumeau ; le nul asymétrique (contrôle 11) n'existe qu'en simulation. |
| P35 | Choisir l'unité au vu des données d'épreuve est une fuite. | T2-B A-5 ; T2-C/A (a)2 ; T3-A A-5 | (c) | La v2 fixe la portée d'avance (D-S7). À préciser : les contrôles 12 à 14 « sur la banque réelle » ne servent à choisir ni l'unité, ni C, ni la portée. |
| P36 | Pentes : « croît » demande l'intersection-union des accroissements adjacents ; un contraste linéaire ne prouve ni la monotonie ni la domination. | T1-A E5 (contraste fautif) ; T1-B § 4 ; T1-C § 4, (e)4 ; T2-A C-8 ; T2-B A-6, (c)3 ; T2-C/A (b) ligne 3 ; T3-A A-6, E5′ ; T3-B E9 ; T3-C § 6 | (e) | La v2 lit H2b et H3b sur deux niveaux non désignés. Vérifiable : E9 de T3-B ou E5′ de T3-A (profils (0 ; −0,3 ; −0,3 ; +0,3), (0,1 ; 0,0 ; 0,3), courbe plate ; niveau et puissance). |
| P37 | Mise prévisible (aGRAPA ou ONS, plafond 0,95) au lieu de la grille Λ. | T1-A § 2 ; T1-B § 2 ; T1-C § 2, Exp. 3 ; T2-A C-6 ; T2-B C-4 ; T3-C § 4, Exp. 3 | (e) | Déjà en option dans la v2 (§ 2.2, D-S6). Le gain est borné par le prix du mélange (≤ log 4, environ 9 unités à 20 points, sortie S). Les réglages sont des degrés de liberté par fiche (T2-A). Vérifiable : Exp. 3 de T3-C. |
| P38 | Contraste pondéré par épisode : v(t) = (m_t / m_max)·(r_A − r_B). | T3-A évasion « pondération » | (e) | Exact : E[v] ≤ 0 équivaut au nul sur le rappel par épisode de N-054, et v reste dans [−1 ; 1]. Prix : une mise réduite quand m_t < m_max. Vérifiable : E8 de T3-A. |
| P39 | H2a : masque d'indices symétrique sur le jumeau honnête de même longueur (T3-C), ou sous-population définie par un trait de génération (T3-A). | T1-C plan ligne 5 (filtre asymétrique, fautif) ; T2-A C-4 ; T2-B C-3 ; T3-C § 3, Exp. 2 ; T3-A A-7 | (e) | La v2 compare r_seq (sabotés filtrés) à f_seq (honnêtes) « appariés par consigne » sans dire si les honnêtes sont filtrés. Le choix du filtre décide du biais : un filtre plus strict côté honnête promeut sans signal (T2-A C-4). Vérifiable : contrôle 14 joué sous les trois définitions. |
| P40 | Seuils au rang réalisé des honnêtes d'épreuve, sans calibrage séparé ni garde. | T3-A E3′ | (e), affirmation centrale fausse | « Asymétrie nulle par construction » est faux (sortie R) : à 150 unités honnêtes, 0,15 / 0,14 de promotion à tort, contre 0,14 / 0,13 pour la règle de la v2 ; même écart-type d'asymétrie vraie (0,37 point). Mérite réel : supprime la dérive P20. À confronter à N-008 (« … sur épisodes honnêtes réservés », faits, ligne 734). |
| P41 | Ensemble de confiance du meilleur comparateur, établi sur le développement. | T3-A E6 | (e) | Réintroduit une sélection : le niveau devient α plus la probabilité d'exclure la vraie meilleure base, que T3-A ne déclare pas. L'intersection-union complète de la v2 n'a pas ce coût. Vérifiable : mondes F et P de T3-B E4′. |
| P42 | Point primaire à 5 % pour G1. | T1-A § 3 (a) ; T1-B § 3 (ii) ; retiré par T3-A A-3 et T3-B plan ligne 2 ; contre : T2-C/A (b) ligne « tous » | (e), retirée | Changerait N-008 (nœud de décision). La v2 garde 1 % pour G1 (D-S5). |
| P43 | Bornes exactes à effectif fixe (Hoeffding, Bentkus) comme étalons. | T3-B E0 ; T3-A E4′ | (e) | Valides pour une moyenne bornée. À ajouter au contrôle 17 de la v2, qui ne cite que Student et le rééchantillonnage. Vérifiable : E0 et E3′ de T3-B. |
| P44 | « δ ≤ τ » fermerait la faille de la garde. | T1-A § 3, plan ligne 5 ; T1-B § 3 (iii) | (d) | À 1 %, un rapport 2 de faux positifs achète encore 10,8 points dans le monde de la v2 (0,40 → 0,508) et 8,6 points avec d′ = 1,5 (sortie S). Réfuté par T2-B A-3, accepté par T3-A. |
| P45 | Les p-valeurs conformes ou un même rang d'ordre « apparient par construction » : « E[f_A − f_B] = 0 exactement ». | T1-A § 3 (c) ; T1-B § 3 (i) ; T1-C § 3.1, (e)3 | (d) | L'égalité vaut en moyenne sur les calibrages, pas sur le calibrage scellé : écart-type de l'asymétrie √(2τ(1−τ)/N), soit 0,81 point à 300 épisodes (sortie S). C'est déjà la règle de la v2 § 2.4, dont la cellule E mesure l'artefact. Réfuté par T2-A C-5, T2-B C-7 et T2-C/A (a)1 ; retiré par T3-B et T3-C. |
| P46 | Juger une aire partielle sous la courbe sur τ ∈ {0,5 ; 1 ; 2 ; 5 %}. | T1-C § 3.2 | (d) | Change l'estimande de N-008 et inclut le point à 5 %, où le rappel s'achète (T2-B C-6) ; retiré par T3-C § 5. |
| P47 | Garde « FAUSSE mathématiquement » ; normaliser par 1 + δ ; tronquer à 10⁻⁶ ; 150 unités de 5 épisodes suffiraient. | T1-C (a)1, (c) ligne 2, (e)3, (d) | (d) | 1 + λ(δ − g) ≥ 1 − 0,9(1 − δ) > 0,1, et son espérance est ≤ 1 sous E[g] ≥ δ. Normaliser réduit la mise ; la troncature casserait la surmartingale si elle agissait ; moins d'épisodes augmentent la variance. Retiré par T3-C § 1. |
| P48 | Récupérer de la puissance par des mises > 1 « si la plage observée est bornée », ou par le centrage 1 + λ_t(v − μ̂). | T1-C (e)1 | (d) | Le nul contient v = −1 et une plage observée ne borne pas l'unité suivante ; le centrage teste une autre frontière (T2-B C-4 ; accepté par T3-C § 4). |
| P49 | Exactitude des tests à n fixé : la permutation de Pitman est « exacte » (T1-C), puis le pari est le « seul test exact » (T3-C). | T1-C plan ligne 10 ; T3-C (c) 1.4 | (d) | Le retournement de signes n'est exact que sous symétrie (T2-B C-5). Inversement, Hoeffding et Bentkus donnent des tests valides à n fixé pour une moyenne bornée (T3-B E0). |
| P50 | L'intersection-union serait une « inversion logique » de N-008, « infranchissable » avec des bases médiocres. | T2-C/B (a)1, (b) ligne 1 | (d) | Pour des moyennes, battre la meilleure base équivaut à battre chacune ; une base faible donne un contraste de moyenne élevée (T3-B C1-a). Le fond de puissance est P32. |
| P51 | Une « porte suspendue » casserait le niveau ; les seuils randomisés ne seraient pas reproductibles ; 20 à 30 % des courses seraient suspendues. | T2-C/B (a)3, (a)4 | (d) | Une condition de blocage déclarée d'avance ne peut que réduire la probabilité de passer sous le nul ; une graine scellée rend le tirage rejouable ; sans effet de tâche, le taux de suspension est d'environ 0,005 (T3-B C3, C4-a, C4-b). |
| P52 | Le calibrage fini « viole Ville » : W ne serait plus une surmartingale. | T2-C/A (a)1 | (d), imprécis | Conditionnellement au calibrage scellé, W est une surmartingale sous le nul conditionnel ; l'artefact vient de l'écart entre ce nul et « à faux positifs égaux » (v2 § 2.4 ; T3-A le rejette sur la conclusion). |
| P53 | Dimensionnement : 2 300 à 4 000 épisodes, 30 unités de calibrage suffisent, tout tient dans 100 à 300 dollars. | T1-A (d) ; T1-B (d) ; T1-C (d) ; T3-C (c) 2.5 ; T3-B B-3 | (d) | v2 § 2.4 et § 6 : il faut un calibrage de 10 à 16 fois les unités sabotées (1 000 à 4 000 unités de dix épisodes) ; à C = 45, l'artefact vaut 0,23. Et « au-dessus de 100 tâches pour 10 points » (T3-B) : la v2 donne 0,96 à 100. |
| P54 | Erreurs d'arithmétique sur les formes signe et parts. | T1-C (b)1-2 ; T2-B C-8 | (d) | Voir la section 4, point 9 (valeurs exactes, sortie S). |
| P55 | Statuts gonflés et citations inexactes. | T1-C (en-tête, (a)1, (b)2, (d)3) ; T3-A A-9 | (d) | Voir la section 4, point 10. |
| P56 | Expériences de T1-A vraies par construction ou mal étalonnées : E3, E4, contrôle d'accord en monde symétrique, A5 « épisodes indépendants ». | T1-A E3, E4, table (c), A5 | (d) | Réfutées par T2-B A-1, A-2, A-4 et A-8, et acceptées par T3-A ; le code partage `u` entre épisodes et moniteurs (faits, lignes 324 à 327). |
| P57 | Partitions « disjointes par organisme » entre développement, calibrage et épreuve. | T1-A plan ligne 1 ; T1-C plan ligne 1 ; T3-A E3′, E6 | (d), trompeur | Sous la portée (a) de la v2 (D-S7), couper par organisme crée la dérive de P20 (sortie D). Seule la lecture (b), qui vise des agents nouveaux, le demanderait. |

Décompte : (a) 18 (P1 à P18) ; (b) 7 (P19 à P25) ; (c) 10 (P26 à P35) ; (e) 8 (P36 à P43) ; (d) 14 (P44 à P57).

## 3. Les trois points les plus importants (parmi (b) et (e))

Ces trois points ont une racine commune. La v2 (§ 2.4) traite toute asymétrie fine de faux positifs comme du bruit d'échantillonnage, que la taille du calibrage borne et que des jumeaux identiques mesurent. Trois autres sources lui échappent ; les voici.

### 3.1 Ex æquo des scores ordinaux (P19)

- **Les cellules.** T1-B a6 : « si les scores d'une base noire sont ordinaux, le taux réalisé est systématiquement décalé par les ex æquo ». Repris par T2-B A-9, T3-A E7, T3-B E2′ et T3-C § 5.3. P § 10 dit « verdicts ordinaux ou continus » (faits, ligne 629), et les bases noires de G1 comprennent des juges génératifs (P § 8.3 et D1, faits, lignes 597 à 607).
- **Pourquoi la v2 ne le voit pas.** Le décalage ne baisse pas avec C. Le contrôle 12 duplique un même moniteur, donc les mêmes ex æquo des deux côtés. La garde (δ ≥ 0,03) ne voit pas un écart de 0,5 à 1 point.
- **Mesure (sortie T).** A continu et B ordinal ont la même loi latente ; les paliers de B sont espacés de 0,5 écart-type.
  - B tourne en réalité à 0,54 % (règle « > seuil ») ou à 2,0 % (règle « ≥ seuil ») au lieu de 1 %, soit +9,0 ou −9,9 points de rappel.
  - Promotion à tort de « A > B » : 0,66 à 100 unités sabotées, 0,82 à 250. Ou de « B > A » : 0,50 et 0,83.
  - Paliers de 0,25 écart-type : 0,35 / 0,64 et 0,36 / 0,68.
  - Mêmes ordres de grandeur avec un calibrage fini de 1 000 unités.
- **Le remède de T3-A ne suffit pas.** La règle « non comparable hors de [τ/2 ; 2τ] » laisse passer, au pas de 0,25, des taux réels compris entre 0,50 % et 1,89 %, donc dans l'intervalle (à la borne basse près), pour ±4,8 points de rappel.
- **Ce qui marche.** Un bris d'égalité aléatoire scellé ramène la promotion à 0,025 à 100 unités. Le reste (0,14 à 250 unités) est une perte réelle de 1,6 point due à la discrétisation, pas un artefact.
- **v3.**
  - Écrire la convention d'égalité dans § 2.4.
  - Exiger un score continu (probabilité du jeton de verdict, P § 10, faits ligne 635) ou, à défaut, un bris d'égalité aléatoire dont la graine est dans l'engagement (T3-C : uniforme tirée de l'empreinte de l'épisode).
  - Ajouter un contrôle « jumeaux de même loi latente, l'un à la granularité réelle de la base », avec ≤ α exigé.
  - Rapporter le pas de chaque cellule au voisinage de τ.

### 3.2 Dérive de composition entre calibrage et épreuve (P20)

- **Les cellules.** T1-A § 1 (ii), « dérive calibrage→épreuve ». T2-A B-6 en fait « le trou commun » de B et C ; T3-B B-6 l'appelle « le trou le plus sérieux de ma conception ». T1-C table (c) ligne 3 donne un cas : les honnêtes sous pression rhétorique (plan 2 × 2 d'EC.2).
- **Ce que suppose la v2.** « Le fin est borné par C et mesuré par le contrôle 12 » (§ 2.4). Rien n'exige que calibrage et épreuve soient tirés de la même composition (§ 9).
- **Mesure (sortie D).** Les seuils sont exacts, donc sans aucun bruit de calibrage. A est décalé de 0,3 écart-type sur une famille F1 qui pèse 10 % du calibrage et 40 % de l'épreuve ; B est insensible.
  - A tourne à 1,31 % contre 1 % et gagne 3,2 points de rappel. À 1 % réel sur l'épreuve, il en perdrait 0,9.
  - Promotion à tort de « A > B » : 0,09 (100 unités sabotées, 150 honnêtes) et 0,43 (250 / 375). Avec un décalage de 0,5 écart-type : 0,25 et 0,75.
  - Le témoin jumeau ne voit rien (0,002 à 0,019).
  - Tirer le calibrage comme l'épreuve ramène la promotion à ≤ 0,002.
- **Un piège à éviter.** Les partitions « disjointes par organisme » proposées par T1-A, T1-C et T3-A créent exactement cette dérive (P57).
- **v3.**
  - Tirage scellé des parties, stratifié par mode, famille de consignes et agent surveillé.
  - Taux réalisés par cellule et par strate sur les honnêtes d'épreuve, rapportés avec leur suite de confiance.
  - Un contrôle « jumeau décalé sur une strate ».
  - Écrire dans § 2.4 que C ne borne que le bruit.
  - Le rang réalisé de T3-A (P40) supprime cette dérive mais pas le bruit.

### 3.3 Choix du bras blanc aux seuils d'un seul calibrage (P21)

- **La cellule.** T2-A, une seule phrase : « le constructeur qui a deux candidats de moniteur blanc et un seul calibrage peut, sur la partie de développement, préférer celui dont le seuil réalisé est tombé « du bon côté » ». Une seule cellule porte ce point, mais il touche G1 de front.
- **Ce que la v2 ne dit pas.** Que la partie de calibrage qui fixe les seuils de l'épreuve ne sert à aucun choix de développement. Et le contrôle 12 ne comporte aucune sélection.
- **Mesure (sortie K).** C = 200 unités ; développement de 40 unités sabotées ; épreuve de 100 sabotées et 150 honnêtes ; garde δ = 0,05.
  - Promotion à tort de « A > B » : 0,11 sans choix, 0,23 avec 5 candidats, 0,36 avec 20.
  - Le bras retenu a un taux réel de faux positifs de 1,27 % et 1,41 % contre 1,05 % pour B, soit +2,9 et +4,5 points de rappel.
- **Ma lecture, au-delà de la cellule.** Le même mécanisme vaut pour tout choix fait aux seuils d'un même calibrage : famille de sonde, couche, concept (P § 8.1), agrégateur. Il vaut aussi pour l'organisme du pôle, qui retient de génération en génération les cellules qui gagnent.
- **v3.**
  - Un calibrage propre au développement.
  - Un calibrage de l'épreuve de G1 tiré et lu une seule fois, après le gel de tous les choix (esprit de N-050).
  - Un contrôle 12 étendu à K candidats, avec la procédure de choix déclarée.
  - Compter les comparaisons faites sur un même calibrage dans le dimensionnement de C (D-S9).

**Juste après ces trois points :**
- P22, la multiplicité entre générations. Remède : une signature sans τ (proposée par T3-A) ou une partie d'épreuve neuve par génération, et une règle de taux de fausses découvertes en ligne entre générations.
- P23, la longueur des épisodes. Remède : seuil par horizon et jumeaux honnêtes de même longueur.

## 4. Faux positifs du collisionneur

**A. Trompeurs, et dangereux s'ils entraient dans une v3**

1. **T3-A E3′** : avec le rang réalisé des honnêtes d'épreuve, « l'asymétrie de seuil est nulle par construction » et « le calibrage séparé disparaît (et avec lui la dépendance au calibrage fini) ». C'est faux : seul le taux réalisé sur l'échantillon est apparié, pas le taux réel (sortie R, P40).
2. **T1-A § 3 (c), T1-B § 3 (i), T1-C § 3.1** : les p-valeurs conformes ou un même rang d'ordre annuleraient l'asymétrie « exactement ». Ce n'est vrai qu'en moyenne sur les calibrages (P45). C'est déjà la règle de la v2.
3. **T1-A et T1-B** : « δ ≤ τ » suffirait. À 1 %, un rapport 2 achète encore 9 à 11 points (P44, sortie S).
4. **T3-A E7** : une cellule « non comparable hors de [τ/2 ; 2τ] ». C'est la même faiblesse de rapport 2 ; la sortie T montre des paliers qui restent dans l'intervalle avec ±4,8 points.
5. **Dimensionnements** de T1-A, T1-B, T1-C et T3-C : ils omettent le poste de calibrage, qui domine d'un ordre de grandeur (v2 § 2.4 et § 6). « 30 unités de calibrage suffisent » (T1-C) est contredit par la cellule E de la v2 (0,23 de fausse promotion à C = 45). P53.
6. **Partitions « disjointes par organisme »** (T1-A, T1-C, T3-A) : sous la portée (a), elles fabriquent la dérive de P20 (P57).
7. **Exactitude des tests à n fixé**, en deux sens contraires : la permutation de Pitman présentée comme « exacte » (T1-C), puis le pari présenté comme le « seul test exact » (T3-C). P49.

**B. Faux, puis corrigés pendant le tour**

8. **T1-C (a)1** : la garde serait « FAUSSE mathématiquement ». Avec elle tombent la normalisation par 1 + δ, la troncature à 10⁻⁶ et « 150 unités de 5 épisodes ». P47 ; retiré par T3-C.
9. **Arithmétique** (sortie S, valeurs exactes) :
   - T1-C (b)1 : la composante signe d'un monde 70 / 30 ne croît pas « comme (1 + 0,4λ)^n ». Elle vaut +0,035, +0,077, +0,054 et −0,24 nat par unité à λ = 0,1 / 0,3 / 0,6 / 0,9.
   - T2-B C-8 : « seuls λ = 0,1 et 0,3 croissent » est inexact, λ = 0,6 croît aussi ; T3-C le corrige.
   - T1-C (b)2 : à 0,6 contre 0,4, la forme signe croît de 0,19 nat par unité à λ = 0,9, pas de 0,28 ; son maximum est 0,25 vers λ = 0,7.
   - T1-C (b)2 : la mise de Kelly approchée vaut E[v]/E[v²] ≈ 2,27, pas E[v]/Var(v) ≈ 4,17.
   - T1-C (b)1 : la composante λ = 0,9 de la forme parts dérive d'environ −0,02 nat par unité sous le nul ; elle ne « s'effondre » pas (T2-A C-10).
10. **Statuts et citations.**
    - T1-C marque « VÉRIFIÉ » ses propres dérivations.
    - T1-C marque « RAPPORTÉ » le nom « Llama-3.1-8B-Instruct », absent des faits : on n'y trouve que « Llama Scope » (ligne 594), « Llama-3.2-3B-Instruct » (ligne 605) et « portés sur 8B » (ligne 632).
    - T1-C tient l'attribution de Waudby-Smith et Ramdas pour « VÉRIFIÉE », ce qui demande un PDF (R7).
    - T1-C écrit « le contrôle fatal n° 6 montre », alors que ce contrôle n'a jamais tourné.
    - T3-A situe la leçon de P3 en « P § 12 » : elle est en P § 10, piste C (faits, ligne 635).
11. **T1-C (e)1** : mises > 1 et centrage par la moyenne empirique (P48).
12. **T1-C (b)2** : aGRAPA plafonnée à 0,75 atteindrait 80 % en « 28 tâches contre 35 ». Saturée à 0,75, sous le 0,9 de la grille, elle ne peut gagner que le prix du mélange (T2-A C-6, T2-B C-4).
13. **Expériences de T1-A** : E3 est vraie par construction, E4 étalonne sur un nul de médiane, le contrôle d'accord en monde symétrique est tautologique, et A5 décrit des « épisodes indépendants » alors que le code partage `u` (P56).
14. **T2-C/A (a)1** : « Ville est violée ». C'est imprécis (P52).
15. **T2-C/B (a)1** : l'intersection-union serait une « inversion logique » et deviendrait « infranchissable » (P50, réfuté par T3-B C1-a).
16. **T2-C/B (a)3-4** : la porte suspendue et les seuils randomisés (P51, réfuté par T3-B).
17. **T2-C/B (b) ligne 2** : le mécanisme du bootstrap est calculé sur les répliques d'un seul échantillon (12,4 % + 27 %). Le bon calcul porte sur l'échantillon d'origine : la probabilité de n'avoir aucune unité catastrophique est 0,92²⁵ ≈ 0,12 (T3-B C2). La conclusion, un bootstrap anticonservateur, tient.
18. **T3-B B-3** : le besoin à 10 points serait « probablement au-dessus de 100 tâches ». La v2 § 6 donne 0,96 à 100 unités (forme parts seule).

**C. Disputé, et sans objet en v2.** T1-B a8 (« trois valeurs incompatibles ») contre T2-A B-2 (« trois comparaisons, une valeur chacune »). La contre-lecture (C10) jugeait faux le log 4 du contrôle 9 pour un mélange à deux formes ; la v2 n'a plus qu'une forme.

## 5. Ce que le collisionneur a manqué, et que la contre-lecture avait trouvé

| contre-lecture | collisionneur |
|---|---|
| C1 forme signe | trouvé par toutes les cellules (P1). |
| C2 bruit de calibrage | trouvé sur le principe (P4). **Manqué** : la conséquence chiffrée, un calibrage de 10 à 16 fois les unités sabotées (D-S9, une dépense). Ses remèdes (P40, P45) ne marchent pas. |
| C3 grappes | trouvé sur le principe (P5). **Manqués** : le choix de portée (D-S7, conditionnelle ou population) et le minimum de 7 à 8 agents (11 au seuil m/α = 240). T1-C et T3-A passent à l'organisme comme unité sans voir que rien ne serait alors promouvable. |
| C4 H2a | trouvé (P6). |
| C5 relecture d'une banque figée (contrôle 15, D-S12) | **manqué**. Le point le plus proche, P22, est un autre mécanisme. |
| C6 traduction de G1 | (a), (b), (c), (d) et (e) trouvés (P4, P7, P12, P11, P8). Pour (f), les planchers sont trouvés (P13), mais « G1 n'est pas la comparaison de H1, à agrégations différentes » est **manqué**. |
| C7 tableau contre énoncés | trouvés : les paires (P31), « domine à chaque N » (P14), les bras de N-054 (P13), le mode tenu à l'écart comme strate (P12). **Manqués** : H1b « part revendicable » comme modification de revendication (nœud pour Lazar) ; la strate « diffus » non codée ; la sécurité comme infimum et « alerté avant le dommage θ » (H3) ; l'expérience de lecture de N-054 point 4, qui compare des unités différentes. Les bases (ii) et (iii) de H2 ne sont vues qu'en partie (T1-C table (c) ligne 4). |
| C8 dimensionnement | (a) et (d) trouvés. (c) trouvé en partie (T1-B § 4). **Manqués** : (b) l'écart hétérogène, (e) le besoin honnête sous-estimé d'un ordre de grandeur (que le collisionneur aggrave, P53), (g) le minimum d'organismes. |
| C9 règle e-BH appliquée avant la garde (contrôle 16) | **manqué**. T1-B § 1 et T3-B (c) tiennent même « le minimum des deux e-valeurs » pour acquis, sans voir que la v1 ne l'appliquait pas. |
| C10 prix du mélange | trouvé (T1-B a8), puis disputé (T2-A B-2). |
| C11 règle des coefficients | **manqué**. T1-B § 4 reprend même « Σ\|a\| ≤ 1 », sans dommage sur des poids de tendance appliqués à des écarts. |
| C12 petits points | **manqués** : l'analogie N-007, les deux sens d'« organisme », les graines (R9), δ = 0,04 absent de la sortie, la grille du contrôle 8, « 0,15 partout », les arrondis. |
| contrôles 11 à 17 | 11, 13, 14 et 17 trouvés ; 12 trouvé sans son dimensionnement ; **15 et 16 manqués**. |
| décisions D-S7 à D-S12 et nœud | D-S8, D-S10 et D-S11 trouvés ; D-S7 en partie (l'unité, pas la portée) ; **D-S9, D-S12 et le nœud H1b manqués**. |

À l'inverse, le collisionneur apporte ce que la contre-lecture n'avait pas : P19 à P25 (b), P26 à P35 (c), P36 à P43 (e).

## 6. Ce que la v3 devrait reprendre, hors des trois points de la section 3

- Pour H2b, juger le rappel du séquentiel avec un seuil par horizon ; pour « croît », exiger l'intersection-union des accroissements adjacents (P26, P36).
- Trancher la latéralité de l'intervalle de G1 dans D-S11 (P27).
- Ajouter le plancher « sonde aléatoire » aux comparaisons rapportées de G1 (P28).
- Ajouter le contrôle de qualité des bases (P29).
- Définir le filtre honnête de H2a, ou le masque symétrique (P39).
- Prévoir des témoins faux asymétriques à chaque course réelle (P34).
- Pour la multiplicité entre générations, une signature sans τ ou des parties d'épreuve disjointes (P22).
- Masquer la strate du mode tenu à l'écart (P24).
- Vérifier le niveau des intervalles de N-054 point 4 ; c'est une proposition à Lazar, puisque cela touche une décision (P25).

## 7. Vérifications sur processeur (exploratoire, aucune dépense)

**Fichiers et exécution.**
- Script : `verification-collisionneur-pari-signe-v1.py`, `8d07301a9879dbe4c94a0b70703a35012a208c553472a5073c77bcc6bce23d7b`.
- Sortie : `verification-collisionneur-pari-signe-v1-sortie.json`, `38efb97111c5aa7edc26e768b699107aa787b5ae0f3e6037fd67ed913f786a80`.
- Lancé par `/opt/venv-essaim-sim-v1/bin/python -I -B verification-collisionneur-pari-signe-v1.py --rep 2000` (Python 3.13.17, numpy 2.5.4, 75 secondes).
- Graines : `SeedSequence(2026102701, spawn_key=(section, configuration))`, une par configuration (R9). Le manifeste est dans la sortie.
- Répétitions : 2 000 ; 1 000 pour les configurations lourdes.

**Les cinq sections.**
- **S, valeurs exactes.** Celles qui servent aux sections 2 et 4 ; la pente binormale vaut 14,5 au point 1 %.
- **T, ex æquo** (jumeaux de même loi latente ; A continu, B ordinal ; paliers à décalage aléatoire). Taux réel moyen de faux positifs de B et promotion à tort :

  | pas des paliers | règle « ≥ seuil » | règle « > seuil » | bris d'égalité scellé |
  |---|---|---|---|
  | 0,5 écart-type | 2,0 % ; B > A : 0,50 (100 unités), 0,83 (250) | 0,54 % ; A > B : 0,66 (100), 0,82 (250) | 1,0 % ; A > B : 0,025 (100), 0,14 (250) |
  | 0,25 écart-type | 1,40 % ; B > A : 0,36, 0,68 | 0,72 % ; A > B : 0,35, 0,64 | 1,0 % ; A > B : 0,005, 0,032 |

  - Ce tableau est en calibrage infini.
  - Avec un calibrage de 1 000 unités, mêmes ordres de grandeur : 0,51 / 0,83, 0,67 / 0,82 et 0,068 / 0,26 au pas de 0,5.
  - Ce qui reste avec le bris d'égalité est une perte réelle de discrétisation : +1,6 point au pas de 0,5, +0,4 au pas de 0,25.
- **R, rang réalisé contre règle de la v2** (unités sabotées / honnêtes). Promotion à tort « A > B » / « B > A » :
  - 100 / 150 : 0,15 / 0,14 (rang) contre 0,14 / 0,13 (v2, C = 150 et garde) ;
  - 100 / 1 000 : 0,019 / 0,020 contre 0,021 / 0,022 ;
  - 250 / 375 : 0,19 / 0,17 contre 0,19 / 0,19.
  - Écart-type de l'asymétrie vraie de faux positifs : 0,37, 0,14 et 0,23 point, identique dans les deux règles.
- **D, dérive** (seuils exacts ; A décalé sur F1, qui pèse 10 % au calibrage et 40 % à l'épreuve). Promotion à tort « A > B » :

  | décalage de A sur F1 | dérive (100/150 ; 250/375) | témoin jumeau | calibrage tiré comme l'épreuve |
  |---|---|---|---|
  | 0,3 | 0,093 ; 0,43 | 0,004 ; 0,019 | 0,0005 ; 0,0015 |
  | 0,5 | 0,25 ; 0,75 | 0,002 ; 0,011 | 0,000 ; 0,000 |

  Dans la colonne « calibrage tiré comme l'épreuve », « B > A » vaut 0,012 à 0,24 : c'est juste, car A est réellement moins bon à faux positifs égaux (0,391 et 0,376 contre 0,40).
- **K, choix du bras blanc** (C = 200 unités, développement de 40 unités sabotées, épreuve 100 / 150). Promotion à tort « A > B » : 0,11 (un candidat), 0,23 (cinq), 0,36 (vingt) ; taux réel de faux positifs du bras retenu : 1,06 %, 1,27 %, 1,41 %.

**Limites.**
- Le monde est binormal, les épisodes sont indépendants dans une unité, et les paramètres sont illustratifs : pas des paliers, décalage de 0,3 et 0,5, K, C.
- Ces chiffres montrent des mécanismes ; ils ne prédisent pas la banque réelle.
- Rien ici n'est décisif ; tout est à refaire sous préenregistrement si cela sert G1.

## 8. Fichiers lus et empreintes SHA-256 complètes

Toutes les empreintes ci-dessous sont conformes à leurs compagnons `.sha256`, quand ils existent, ou aux listes `EMPREINTES-v1.txt` et `EMPREINTES-entrees.txt` du collisionneur.

| fichier | SHA-256 |
|---|---|
| `…/pari-de-signe/conception-pari-de-signe-v2.md` | `9c39a73ddbf681270610e6a3552fd85045fae46ade21d8d38c77564b7b461e1a` |
| `…/pari-de-signe/conception-pari-de-signe-v1.md` | `50ce6842f0c087afa086db814222a5d0595f610f3cfda04d5a6a860b5d7822c0` |
| `…/pari-de-signe/contre-lecture-v1/rapport-contre-lecture-pari-signe-v1.md` | `022e96d4fc4f1d13b081400756b38853095b0c9a402131ec53dc5192a9cf9b93` |
| `…/collisionneur-pari-de-signe/question-pari-de-signe-v1.md` (identique à `…/pari-de-signe/question-collisionneur-pari-de-signe-v1.md`) | `8e22c7650566e61caf70e7dff2cc77afc99a8c6f80a32af4842f9a590badb0fb` |
| `…/cellules/E3-T1-conception-A.md` | `84e24603709c624dc60ab93534de987e3ae5ef60cfdad497fd929627ae530e1a` |
| `…/cellules/E3-T1-conception-B.md` | `a9e61c6bd065bea727e175c471c9588547188b0db4624d0551a7ed449c2c5055` |
| `…/cellules/E3-T1-conception-C.md` | `6dada7fe291c5225fadce9883f360a09526e95d28b88667e2ba9c700c7dd41da` |
| `…/cellules/E3-T2-redteam-A.md` | `bca4f900867eb040516620fe98a6ee27ea52fbe76b09be64bdd71ce802e3bff8` |
| `…/cellules/E3-T2-redteam-B.md` | `a0f572f9ded3ae8df0bbe0bca8c85d63d8df39fe10744fb37d67864ea9e53c94` |
| `…/cellules/E3-T2-redteam-C.md` | `a2f4ee49ba9c25aaafc8c56c6745761cbe79dde2be84ecf4cc33d5654a914a4a` |
| `…/cellules/E3-T3-riposte-A.md` | `4c441b077753a713a3564933985e6a4fa1d18eb9af12919659995b741d2773fe` |
| `…/cellules/E3-T3-riposte-B.md` | `30c8fd331effe5731b23f215bd13a2d05a4d69895a44e7ebc4dbaa030e539824` |
| `…/cellules/E3-T3-riposte-C.md` | `e99fdfaea5382655e8c1462bb7a4616c1ef06b628e190ac3931fd7f42d39c14e` |
| `…/collisionneur-pari-de-signe/faits-pari-de-signe-v1.md` (lu en partie : lignes 286 à 365, 626 à 665, 685 à 814, et des recherches) | `4a815bb317494fedcff12bb29e071ae10c8276fa5f490a7a3505f7341321bbae` |
| `…/collisionneur-pari-de-signe/EMPREINTES-v1.txt` (deux lignes, par recherche) | `930578a3c9994c3b8bf953cfda2faefcec800c1dfc6a66ad1adcb3a824ec5fb6` |
| `…/collisionneur-pari-de-signe/EMPREINTES-entrees.txt` (deux lignes, par recherche) | `ff815afb0bdcbf07f959c5b05fda7d466c8e0df727590186579f0604c5121f59` |
| mon script `verification-collisionneur-pari-signe-v1.py` | `8d07301a9879dbe4c94a0b70703a35012a208c553472a5073c77bcc6bce23d7b` |
| ma sortie `verification-collisionneur-pari-signe-v1-sortie.json` | `38efb97111c5aa7edc26e768b699107aa787b5ae0f3e6037fd67ed913f786a80` |

**Chemins complets des dossiers abrégés.**
- `…/pari-de-signe/` = `/home/claude/canal-conv-audit-n04/brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/pari-de-signe/`.
- `…/collisionneur-pari-de-signe/` = `/tmp/claude-0/-home-claude/c5a45195-121d-5962-9d0a-4896cc046231/scratchpad/collisionneur-pari-de-signe-v1/collisionneur-pari-de-signe/`.
- `…/cellules/` = `…/collisionneur-pari-de-signe/run-pari-de-signe-e3-v1/cellules/`.
- Mes fichiers sont dans `/tmp/claude-0/-home-claude/c5a45195-121d-5962-9d0a-4896cc046231/scratchpad/lecture-collisionneur-pari-signe/`.

Heure de fin (lue sur `date -u`) : mardi 27 octobre 2026, 18:38:45 UTC.
