# Couche 2 : comparaison des deux dimensionnements (conv-audit à l'aveugle, session-depot) — v1

Sous-agent neuf, comparateur, 28 octobre 2026. Je ne tranche rien : Lazar décide. Pièces de session-depot : P-036
(`a8c41681…`), la carte d'inventaire (`96a9a531…`, sceau conforme à celui que cite P-036) et le devis v1 (`cf2f4772…`,
remplacé sur le fond par P-036). Pièce de conv-audit : le dimensionnement aveugle (`95c5c396…`), sa simulation et sa
sortie. **Cadre** : les fichiers `decision-N-055-v1.md` et `decision-N-056-v1.md` sont **absents de HEAD** (branche locale
`canal/conv-audit-n04`) et de `docs/decisions/`. J'ai lu à la place le brouillon de N-056
(`envois/decision-N-056-noeuds-G1-…-v1.md`, `6aac9746…`) et `pari-de-signe/decisions-lazar-2026-10-27-v1.md` (`c2cfa159…`,
qui porte D-S1 à D-S12). Aucune branche lue.

**Contrôle de reproduction.** J'ai relancé la simulation de conv-audit à graine neuve (31415926, 1 000 répétitions,
74 s) : toutes les cellules citées se retrouvent à l'erreur de tirage près (par exemple 64 unités, 10 points, 10
exécutions : 0,63 → 0,63 et 0,78 → 0,79 ; intersection-union 0,68 → 0,72). Tous ces chiffres restent exploratoires et
non opposables.

## 1. Verdict

1. **Convergence sur l'essentiel structurel** : au plus 96 unités sabotées par mode, tâches partagées entre modes, la
   lecture « 36 = 4 d'évaluation + 32 d'entraînement », calibrage honnête comme poste dominant, format v30 épinglé
   (`58d4fee8…`), strate « diffus » tirée de la dose écrite, coût de l'ordre de 300 à 1 400 dollars (très au-delà de 90).
2. **Divergences réelles** : le dénominateur de D-S9 (unités par mode ou des deux modes) et donc la taille du calibrage ;
   le nombre d'exécutions (10 décidé chez conv-audit, ouvert chez session-depot) ; jumeaux partagés ou non ; la condition
   « mention » et la recherche de dose (gardées chez conv-audit, remplacées chez session-depot) ; l'ordre des lancements.
3. **Complémentarité** : conv-audit voit la statistique (effet de tâche, garde, contrôle 12, retouches de code) ;
   session-depot voit l'ingénierie et la gouvernance (chaîne de lancement, notes de juges incomplètes, étiquetage,
   sondes perdues). Chacun a des erreurs d'arithmétique ou de lecture, aucune ne renverse l'autre plan.

## 2. Tableau point par point

| question | conv-audit (aveugle) | session-depot (P-036, carte) | écart | mieux justifié |
|---|---|---|---|---|
| Unités par mode | 64 (tâches d'évaluation), 96 en option ; tâches et jumeaux partagés (§ 1) | ≤ 96 partagées, 48 si disjointes (D2) ; scénario C1 calcule pourtant sur 280 unités (§ 4 D1) | même plafond ; session-depot se contredit | conv-audit : partition argumentée (réserve contaminée par la dose et l'entraînement des sondes, § 1) |
| Exécutions par unité | K = 10 en épreuve, 3 pour témoin et mention, 5 à 10 au développement (§ 2) | ouvert : 3 (A à C), 10 (D) | décision contre question | conv-audit (tables à 3 et 10, § 2) ; nuance en section 3 ci-dessous |
| Taille du calibrage | 9 600 recommandés, 4 800 minimum, sur les **mêmes 64 tâches**, moitiés coupées dans chaque tâche (§ 3) | 5 040 (C1, 10 ×) à 13 440 (C2, 16 ×), unités de 3 épisodes, lieu non dit | ×1 à ×2 selon le dénominateur | conv-audit sur la méthode (effet de tâche simulé) ; dénominateur à faire trancher |
| Cellules de G1 et captures | tableau de 17 moniteurs avec moment de calcul ; 4 captures à la génération ; ≈ 7 Go d'activations (§ 4) | liste demandée à conv-audit (§ 5) ; module de run qui capture scores par jeton de toutes les sondes, vecteurs, dernier état, bornes (§ 3, ligne 6) | accord sur les captures | conv-audit (liste explicite) ; session-depot ajoute la contrainte des notes de juge finies |
| Base (iii) « dernier état » | état caché à la dernière position, sonde générique figée, couche 15 ; score de dernière action rapporté (§ 5, confiance 0,7) | question posée, capture prévue dans les deux cas | pas de conflit | conv-audit (seul à argumenter : homme de paille, anti-circularité, horizon) |
| Format v30 et retouches | épinglé ; 3 retouches : strate de calibrage, jumeau calibré par blocs, bris d'égalité (§ 6, essai sur code) | épinglé ; « aucun convertisseur » ; plancher de 99 par cellule et strate vu (§ 1) | session-depot ne voit pas les retouches | conv-audit (essai exécuté : calibrage sans duplication refusé) |
| Monde « modes » | gabarit sans code, 250 à 400 lignes, 1 à 2 sessions (§ 7) | « code ou date » demandé | — | conv-audit (seul à répondre) |
| Coût total | 14 470 épisodes, 400 à 1 150 heures, 440 à 1 400 dollars ; minimal 8 480, 260 à 820 (§ 8) | 300 à 1 200 dollars, 300 à 1 000 heures (§ 0) ; table D1 | même ordre | voir section 3 : les deux ont des postes fragiles |
| Coût par poste | génération 42,1 à 54,6 s ; moniteurs 1 à 4 passes du juge 8B (58,2 s) ; 1,08 à 1,2133 dollar l'heure | 132 s et 0,047 dollar par épisode (génération 46,6 + 8B + 3B) ; 1,184 à 1,366 dollar l'heure | prix et rythmes différents | conv-audit sur la traçabilité (empreintes dans `sources-lues`) ; session-depot sur le réalisme du prix récent (non vérifiable ici) |
| Nœuds remontés | 3 nœuds + 5 « proposer avec recommandation » (§ 9) | 7 décisions (D1 à D7) | — | session-depot plus complet sur la gouvernance (échéance, crédit, `main`, séparation N-054) |

## 3. Erreurs et incohérences internes

### Conv-audit (calculs refaits)

- **Vérifiés justes** : total recommandé 1 280 + 640 + 768 + 640 + 320 + 960 + 9 600 + 260 = 14 468 ; minimal 8 484 ;
  part du calibrage 66 % et 57 % ; heures 14 470 × 42,1 s = 169 h, × 54,6 s = 219 h, moniteurs 234 à 936 h ; dollars
  435 à 1 401 ; plancher de garde 93 et 48 unités (je l'ai recalculé à la main) ; stockage 10 × 2 × 3 × 4 096 × 2 octets =
  0,49 Mo par épisode ; produit 0,68² = 0,46.
- **Recherche de dose « ≈ 3 à 4 heures, juge compris »** (§ 8, étape 6) : 260 épisodes × 42,1 à 54,6 s = 3,0 à 3,9 h
  pour la seule génération ; avec le juge 8B (58,2 s), 7,2 à 8,1 h. Le libellé est faux ; le plancher de 4 dollars aussi.
- **Cellule F, résultat trop propre** (§ 3, « aucune inflation de niveau : 0,004 à 0,012 », 48 unités) : à 48 unités la
  garde à δ = 0,10 est à son plancher structurel (48) et ne certifie que dans 0,52 des cas ; elle bloque. J'ai relancé F
  avec la garde neutralisée : 0,05 à 0,06 à 48 unités ; et la sortie même du script donne 0,08 à 0,12 à 64 unités avec
  1 024 épisodes de calibrage, **mêmes tâches comme tâches disjointes**. La conclusion « pas d'inflation propre au
  partage des tâches » tient ; la citation est l'artefact que le texte dénonce lui-même pour le contrôle 12 (règle R4).
- **Minimum 4 800 à la limite** : le contrôle 12 y vaut 0,03 à 0,04 (0,046 à ma graine neuve), pour α = 0,05, et deux
  contrôles corrélés (un par mode) dont l'un ou l'autre suffit à déclarer l'échec (§ 3). La marge est mince.
- **« Écart-type d'environ 2 points » à 9 600** : chiffre binormal sans effet de tâche (H). Avec a = 0,3 sur 64 tâches,
  le rappel plafonne à 4 points (le texte le dit) et l'écart entre jumeaux coupés par tâche reste vers 8 points (K). Le
  « 2 points » suppose les moitiés coupées dans les tâches ; c'est plausible, non simulé comme écart-type.
- **« En dessous d'environ 2 000, échec »** : établi pour des moitiés coupées par tâche sur 96 tâches (G) ; non simulé
  pour la coupe recommandée (dans les tâches).
- **Tâches disjointes « 0,02 à 0,14 »** : la table donne 0,01 à 0,18 (n = 30 et 40). Mineur.
- **Nuance absente** : à 64 unités et 5 points d'écart, K = 3 vaut au moins K = 10 (0,10 contre 0,08) ; K = 10 ne paie
  qu'à partir d'environ 48 unités et 10 points. La recommandation K = 10 reste juste au point retenu.
- **Hypothèse non déclarée comme telle** : l'effet de consigne U est commun aux deux moniteurs, ce qui corrèle les
  alertes et réduit la variance de v ; c'est dans l'en-tête du script, pas dans les réserves (§ 10).
- **R7** : 54,6 s par épisode de P3 inclut l'entraînement des sondes et l'installation (P3 entraîne ses sondes dans le
  run, carte, lecture 1) ; c'est une borne haute, non un rythme de génération. « ≈ 260 » épisodes de dose : sans source.

### Session-depot (calculs refaits)

- **Vérifiés justes** : 46,6 + 58,2 + 27,5 = 132,3 s ; 132,3 s × 1,27 dollar/h = 0,047 dollar ; A 1 680 → 62 h, 79
  dollars ; C1 168 × 30 = 5 040 → 185 h, 237 dollars ; C2 16 × 280 × 3 = 13 440 → 493 h, 632 dollars ; devis v1 (a)
  19,5 à 26, (b) 46 à 60,5, (c) 33 à 43.
- **« Total bas (A + B + C1) ≈ 10 100 épisodes »** : B contient déjà A (B = 3 360 = A + témoin + mention). Le total est
  3 360 + 5 040 = 8 400 épisodes ; les 310 heures et 400 dollars de la même ligne correspondent bien à 8 400
  (8 400 × 132 s = 308 h). Le nombre d'épisodes compte A deux fois.
- **C1 et C2 sur 280 unités sabotées** : 280 = 840 sabotés / 3, soit 140 unités par mode, impossible avec 96 tâches selon
  D2 du même document. Le calibrage est aussi compté en unités de 3 épisodes alors que le scénario D en a 10.
- **Total haut ≈ 26 100** : ne se retrouve qu'avec 7 680 (D doublé) + 16 × 384 × 3 = 18 432 ; 384 unités et 3 épisodes
  par unité de calibrage ne sont pas définis, et contredisent K = 10 du scénario D.
- **R7** : prix 1,184 à 1,366 et « `registres/depenses.md` l. 202-211 » : chemin cité sans empreinte, et absent de ma
  copie du registre (92 lignes) ; non vérifiable ici. Deux rythmes de génération circulent pour P3 dans la même lignée :
  40,2 s (synthèse de la carte, 9 644,6 s) et 46,6 s (P-036, 11 179,1 s) ; pour le pilote, 38,1 s (carte, lecture 4)
  contre 42,1 s chez conv-audit (R-143).
- **Fait de lecture** : P-036 (D2) écrit que N-056 demande « plusieurs centaines d'**unités** » ; le brouillon de N-056 dit
  « plusieurs centaines de **tâches** sabotées de plus par mode ». Sans effet sur la conclusion (96 au plus), mais la
  citation est reformulée.

## 4. Ce que chacun voit et que l'autre ne voit pas

**Conv-audit seul** : l'effet de tâche borne le calibrage (étaler sur toutes les tâches d'épreuve, moitiés coupées dans
les tâches) ; δ = 0,05 de la garde est impossible à 64 unités ; le seuil 80 d'une règle e-BH (Benjamini-Hochberg sur
e-valeurs) coûte cher, d'où une seule fiche ; la puissance de G1 est environ le produit des modes (0,46) ; G_max = 1 ;
chaque comparateur doit noter les 9 600 épisodes de calibrage ; les trois retouches de code (strate de calibrage
séparée, jumeau calibré par blocs, bris d'égalité absent de v30) ; un **pilote de mesure** (720 épisodes) avant le devis
complet ; la partie développement (D-S15, 1 920 épisodes) au budget.

**Session-depot seul** : la chaîne de lancement manque (50 à 70 heures de travail, échéance du GO au 31 octobre, deux
lancements au plus, crédit) ; notes de juges incomplètes au pilote (54 et 50 sur 180) contre l'exigence d'un score fini
par cellule ; une exclusion sur note incomplète serait une sélection interdite par N-053 ; le fichier complet des sondes
figées (Mahalanobis) est perdu ; l'étiquetage à deux séries (environ 35 800 paires par série, non revérifié) est hors
devis ; les sondes génériques de P3 sont sous leur plancher ; la garde de conformité à la pile logicielle de P3 ;
l'extraction de tâches neuves demande arXiv, refusé par le réseau ; le juge robustifié b* et la rubrique simplifiée ; les
conditions de contrôles croisés et de conscience d'évaluation (critique de la carte) ; l'avance de `main`.

## 5. Options pour chaque divergence

**Divergence A — dénominateur de D-S9 (a).** Conv-audit : 10 à 16 fois les unités d'**une** fiche (64), calibrage
partagé ; session-depot : 10 à 16 fois les unités sabotées **des deux modes**.
- (1) Par fiche (9 600 = 15 ×). Avantage : correspond au bruit qui compte, celui du seuil face au contraste de la fiche.
  Inconvénient : lecture stricte de « les unités sabotées » non garantie.
- (2) Total des deux modes (12 800 à 20 480 épisodes à K = 10). Avantage : lecture littérale prudente. Inconvénient :
  +30 % à +110 % sur le poste dominant, pour un gain que la simulation ne montre pas.
- (3) Faire dire le dénominateur par l'auteur de D-S9 (conception v2) avant le devis v2.
Recommandation : (3), en préparant (1) ; confiance moyenne (0,6).

**Divergence B — exécutions par unité.**
- (1) K = 10 en épreuve. Avantage : 0,63 à 0,78 pour 10 points à 64 unités. Inconvénient : ×3,3 sur les épisodes sabotés.
- (2) K = 3. Avantage : moins cher. Inconvénient : 0,33 à 0,52 ; G1 muette sous 20 points.
- (3) K fixé après le pilote de mesure (a, h, concordance mesurés). Avantage : décision sur données. Inconvénient : un
  lancement et quelques jours de plus.
Recommandation : (1), avec (3) pour confirmer ; confiance moyenne-haute (0,7).

**Divergence C — jumeaux partagés entre modes.**
- (1) Partagés (conv-audit). Avantage : −640 épisodes en épreuve, écart entre modes apparié. Inconvénient : garde
  identique entre modes, lectures par mode non indépendantes.
- (2) Distincts (scénario D implicite). Avantage : modes séparables. Inconvénient : coût, et aucun gain de validité sous
  intersection-union.
Recommandation : (1) ; confiance moyenne-haute (0,7) ; à déclarer au préenregistrement.

**Divergence D — mention et recherche de dose (P-015 (b)).**
- (1) Tout tenir (conv-audit) : témoin et mention à K = 3, recherche de dose comme premier lancement. Avantage : conforme
  au défaut appliqué. Inconvénient : un lancement et environ 400 épisodes de plus.
- (2) Option (c) de P-036 : témoin gardé, mention lâchée, strates de dose écrites au lieu de la recherche. Avantage :
  dose-réponse portée par la banque. Inconvénient : défait une partie d'un défaut appliqué (R-321) par un nouveau défaut à
  48 heures ; sans recherche, rien ne garantit que les strates tombent dans le régime « diffus ».
- (3) Hybride : petite recherche de dose (≈ 260 épisodes, boîte noire seule) pour placer les strates, mention gardée à K
  = 3.
Recommandation : (3) ; confiance moyenne (0,55). Le retrait de « mention » mérite d'être traité en nœud, pas en défaut.

**Divergence E — ordre des lancements.**
- (1) Conv-audit : dose, puis pilote de mesure, puis préenregistrement de G1 et devis complet. Avantage : chaque dollar
  suivant est chiffré sur mesures. Inconvénient : premier lancement de la banque plus tard ; échéance de G0 serrée.
- (2) Session-depot : lancement 1 = ce qui ne se rattrape pas (génération et captures), le calibrage ensuite. Avantage :
  vitesse. Inconvénient : K et tailles gelés sans mesure de a et h.
Recommandation : (1) avec le pilote réduit au strict nécessaire ; confiance moyenne (0,6).

**Divergence F — coût par épisode.** Moniteurs : 1,5 passe (session-depot) contre 1 à 4 (conv-audit). Options : (1)
borne basse de session-depot ; (2) fourchette de conv-audit ; (3) mesurer au pilote. Recommandation : (3), et présenter
d'ici là la fourchette large ; confiance haute (0,8).

## 6. Rencontres fortuites et indépendance

- **Crédible sur les réponses.** Les chiffres propres à session-depot sont absents du texte aveugle : ni 132 s, ni 0,047,
  ni 1,184 à 1,366, ni 280 unités, ni 35 800 paires. Conv-audit utilise d'autres rythmes (42,1 et 54,6 s) et d'autres
  prix (1,08 à 1,2133), tous retrouvés dans le registre local aux empreintes déclarées (`3f21ffc0…`, `e1ab09db…`). Les
  chiffres communs (96, 64, 32, 60, 58,2 s, 27,5 s, 11 179,1 s, `58d4fee8…`) viennent de sources communes.
- **Les questions, elles, viennent de session-depot.** Les sept sections répondent une à une aux sept demandes de P-036
  (§ 5), avec la même liste de champs en plus. Le texte parle du « 60 + 36 de la question » et des « plusieurs centaines
  d'unités », formules de P-036 et non de N-056. Le cadrage a donc été transmis ; ce n'est pas une rupture, mais la
  convergence sur le plafond de 96 n'est pas une découverte indépendante.
- **Le « 36 » introuvable** s'explique : le registre local s'arrête à R-373 ; R-596 (couche 1 bis, 60 + 36) n'existe que
  chez session-depot. L'inférence « 4 + 32 » de conv-audit est confirmée par la carte (lecture 1).
- **Rencontres déclarées** (R-373, intitulés R-329 à R-373) : j'ai lu R-373 en entier ; il ne contient aucun chiffre de
  couche 2. Il révèle en revanche que **la lignée conv-audit avait lu P-036 (sections 0 à 5), le devis v1 et les messages
  105 à 108** avant la demande, et qu'un premier rédacteur avait reçu P-036 puis a été arrêté sans sortie, dossier détruit
  (non vérifiable). Le risque résiduel est donc dans le brief et dans la vérification par conv-audit, pas chez le
  rédacteur.
- **Sens inverse** : session-depot n'a pas pu lire le texte aveugle (P-036 vers 13:50 UTC, demande aveugle vers 18:10
  UTC). Le devis v1 s'appuie sur des messages plus anciens de conv-audit (n° 126 et 127), cités.
- **Défaut de forme** : le texte aveugle renvoie à `sources-lues.txt`, le fichier s'appelle `sources-lues-v1.txt`.

## Fichiers lus (SHA-256)

```
95c5c396cd21ad5e4fa79422bad37ccc37d306c3372f2200621c0231d85f4a8f  …/couche-2-conv-audit-v1/dimensionnement-couche-2-conv-audit-v1.md
bfbd2d3586c32fb93f3b8496dbfd0bad4afcad0ae07b24e73dead49768483465  …/couche-2-conv-audit-v1/sources-lues-v1.txt
20bb005c4f607d643c0eb4e6396891eb69752d6b1d5d8435da5f091e362c903e  …/couche-2-conv-audit-v1/simulation-couche-2-executions-v1.py
5e4afdae2d8a728d46f916b36a347da4c977aa52edb26a6ddfec28dc19cbcdd1  …/couche-2-conv-audit-v1/simulation-couche-2-executions-v1-sortie.json
a8c41681f1c9ee539a0abfd4b8bf0367e1a2e0ba4a7dd30e27db1c87f867e97c  couche2-compar/proposition-P-036-couche-2-preparation-v1.md
96a9a5314d964be28cc869f46ae99637d5875d37ee95f55d43dcb12ddd517f18  couche2-compar/carte-inventaire-v1.json
cf2f4772dff30c07727808cc6180e46950b2c06ac81a03924b46e9b3498862a9  couche2-compar/devis-couche-2-banque-deux-modes-v1.md
a2aabda8a181d46d9723bad44ad352b5e61650634e0f3bc4863451229af00b1b  /home/claude/controle-ia-travail/CLAUDE.md
6aac9746543cd05d0fc4fb89b32938d272e9b9723dab820d191cbb8297669eff  brouillons/canal-reprise-releve-v1/envois/decision-N-056-noeuds-G1-bras-attaque-mesures-fortes-v1.md
c2cfa1597e85431e9ab661e95fc2f94b170b3ec65744211e1e277a2aa8e2015a  …/pari-de-signe/decisions-lazar-2026-10-27-v1.md
e1ab09dbb0c684236dba52c46d2d6aeae57e8a56b42d0fbf858c62ad88de9e79  registres/decisions.md (lignes 565 et 586, recherches)
3f21ffc08a41bcc5e07b70e39eb472b783fb5f696393f4fe8bfbc3d5391ee6f8  registres/depenses.md (recherches de prix)
58d4fee878fe7957e163a6b5b791adf8895eb2e136aad55502c011b314bccb28  …/orchestrateur-pole-v7/pole/monde_banque_scores.py (empreinte seule)
6fb91b7777f54cafc430e6465d5cf8ca08c53468756098e2265d3f5a21a917c8  …/orchestrateur-pole-v7/EMPREINTES-orchestrateur-pole-v7-v30.txt (recherche)
30cf2e286578632ad589a2748f48856decd12b71e9853abfbb40b9cd2f25770f  …/orchestrateur-pole-v7/EMPREINTES-orchestrateur-pole-v7-v34.txt (recherche)
```
Produits par moi (processeur) : `couche2-compar/rejeu/sortie-graine-neuve.json` (`3b56d9fc…`), `couche2-compar/rejeu/test_f.py`
(`f0784c4d…`). « … » = `/home/claude/controle-ia-travail/brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1` ;
`couche2-compar/` = `/tmp/claude-0/-home-claude/be74bc5f-030c-58ad-8f83-cdf5edf47ca3/scratchpad/couche2-compar/`.
