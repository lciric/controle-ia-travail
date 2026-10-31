# Proposition D — D-ML-1

**Choix : je prendrais (B) aujourd’hui, mais en version « B+ » avec analyse de sensibilité obligatoire.** Je ne présenterais pas son seuil comme un point de fonctionnement à 1 % précisément. Je passerais à (A) seulement si un jeu candidat franchit, avant tout résultat de camouflage, un contrôle préenregistré de compatibilité de distribution. À taille égale, une variance connue me paraît préférable à un biais de distribution non borné.

**Statuts des pièces.** Les contraintes du préenregistrement et les comptes sont **RAPPORTÉS** dans les faits. La sortie numérique est **OBSERVÉE-NON-AUDITÉE**, faute de script et de données fournis. Mes reconstructions mathématiques ci-dessous sont **VÉRIFIÉES**, sans audit du code. Les performances effectives de la sonde et du juge sont inconnues. Le script, les scores individuels et les jeux candidats ne sont pas fournis ; je n’en invente pas le contenu.

## 1. Vérification du calcul servi

Les deux familles d’intervalles ne répondent pas à la même question.

### Seuil empirique

Supposons des scores indépendants, issus d’une même loi continue, sans ex æquo. Si le seuil est le **k-ième plus grand score** parmi \(n\) bénins de calibration, alors le taux de dépassement \(p\) d’une future entrée exchangeable suit exactement :

\[
p\sim \mathrm{Beta}(k,n+1-k).
\]

Les intervalles « seuil » fournis concordent, aux arrondis, avec les quantiles centraux à 95 % de cette loi :

- **VÉRIFIÉ :** pour \(n=1000,\ k=10\), il s’agit de \(\mathrm{Beta}(10,991)\), donnant environ \([0{,}0048;0{,}0171]\).
- **VÉRIFIÉ :** pour \(n=300,\ k=3\), il s’agit de \(\mathrm{Beta}(3,298)\), donnant environ \([0{,}0021;0{,}0238]\).

C’est donc une **loi prédictive pour le taux futur au seuil aléatoire**, pas un intervalle de Clopper–Pearson conditionnel à un seuil fixe.

### Mesure sur bénins indépendants

**VÉRIFIÉ :** les intervalles « mesure » concordent avec Clopper–Pearson :

\[
\left[
Q_{\alpha/2}\!\left(\mathrm{Beta}(k,m-k+1)\right),\,
Q_{1-\alpha/2}\!\left(\mathrm{Beta}(k+1,m-k)\right)
\right],
\]

ce qui donne notamment :

- \(10/1000\) : \([0{,}0048;0{,}0183]\) ;
- \(3/300\) : \([0{,}0021;0{,}0289]\).

**Réserve importante :** la reconstruction des intervalles de seuil suppose précisément la règle d’ordre statistique ci-dessus. Une interpolation de `quantile`, des scores arrondis ou de nombreux ex æquo peuvent changer la loi. Si l’intention était plutôt un Clopper–Pearson à seuil fixe, la borne supérieure servie pour la calibration serait incorrecte. Il faut donc verser et tester la convention exacte de seuil.

Enfin, ces calculs ne couvrent **ni** le déplacement de distribution de (A), **ni** l’incertitude sur les bornes de directions \(\tau\), **ni** les erreurs du juge de nuisance.

## 2. Ce que la décision suppose sans que ce soit établi

1. **Exchangeabilité des partitions de Bailey — HYPOTHÈSE.** `SeedSequence` peut produire un découpage reproductible ; cela ne garantit pas à lui seul l’absence de doublons, de fuites near-duplicate ou de stratification cachée.
2. **Compatibilité d’un jeu externe avec la population bénigne cible — HYPOTHÈSE.** Aucun candidat n’est versé et aucun test de distribution n’est fourni.
3. **Équivalence scientifique des sondes entraînées avec 400 ou 800 bénins — HYPOTHÈSE.** (B) ne réduit pas seulement la calibration : il change l’instrument entraîné.
4. **Stabilité des conclusions \(\tau\) face au bruit du seuil — HYPOTHÈSE.** Les intervalles de fausses alertes ne prouvent pas que les nombres de directions resteront stables.
5. **Validité du juge StrongREJECT affiné sur les sorties effectivement produites — HYPOTHÈSE.** Aucun taux de détection ou de fausses alertes du juge n’est fourni.
6. **Caractère purement statistique de la borne de directions — HYPOTHÈSE à ne pas surinterpréter.** Avec arrêt après un nombre fini de recherches, il s’agit d’une borne empirique sur les directions trouvées, non d’une borne de confiance sur toutes les directions existantes.

## 3. Pour (A) : candidats possibles et risque de déplacement

Aucun des jeux suivants n’est validé ici. Les informations bibliographiques et de licence sont **SUPPOSÉES / HYPOTHÈSES**, à lire sur une révision figée avant usage.

| Candidat | Taille et licence, non vérifiées | Utilisation envisageable | Réserve principale |
|---|---|---|---|
| `databricks-dolly-15k` | Environ 15 000 notices, **illustratif et SUPPOSÉ** ; licence CC BY-SA 3.0 **SUPPOSÉE** ; **référence à vérifier** | Extraire les instructions utilisateur, filtrer, dédupliquer, puis tirer calibration et mesure | Textes de consignes généralistes, possiblement plus longs ou plus techniques que ceux de Bailey |
| `OpenAssistant/oasst1` | Environ 160 000 messages, **illustratif et SUPPOSÉ** ; licence Apache-2.0 **SUPPOSÉE** ; **référence à vérifier** | Extraire uniquement des messages initiaux utilisateur dans la langue retenue, avec filtrage de sécurité | Mélange conversationnel, multilingue et hétérogène ; tous les messages ne sont pas nécessairement bénins |

Le nom connu d’un jeu ne remplace ni le recomptage après filtrage, ni la vérification de licence, ni les empreintes.

### Contrôle de ressemblance à préenregistrer

Un simple test de significativité du type « MMD non significatif, donc distributions identiques » serait insuffisant. Je préenregistrerais quatre niveaux :

1. **Contrôle mécanique des données**  
   Mêmes règles d’inclusion, langue, prétraitement et extraction que pour Bailey ; déduplication exacte et approchée entre entraînement, calibration et mesure ; révision, licence et empreintes figées avant tout résultat \(\tau\).

2. **Descriptifs ciblés**  
   Longueur en caractères et tokens, langue, format interrogatif/injonctif, et autres descripteurs fixés à l’avance. Ils servent à diagnostiquer un déplacement, pas à prouver l’équivalence globale.

3. **Test discriminant honnête**  
   Un classifieur « Bailey contre candidat », évalué hors pli sur texte ou représentation figée. Son AUC est comparée à un contrôle négatif constitué par des partitions aléatoires d’un même pool. Une discriminabilité supérieure à ce contrôle signale un déplacement. Une discriminabilité faible ne prouve toujours pas l’équivalence des queues.

4. **Contrôle opérationnel de la queue de la sonde**  
   C’est le plus important : comparer les scores bénins près du quantile utilisé, puis mesurer le taux de fausses alertes du seuil externe sur les bénins Bailey réellement indépendants de la sonde et de tous les choix. Avec seulement les 200 bénins Bailey hors entraînement initial, cette vérification serait peu précise ; un non-rejet ne devrait donc pas être présenté comme une certification.

### Risque par rapport à (B)

**Le risque de (A) n’est pas borné par ses intervalles binomiaux.** Si le candidat produit des scores bénins systématiquement plus hauts, son quantile sera trop permissif pour Bailey : le camouflage pourra paraître plus facile. S’il produit des scores plus bas, le seuil sera trop strict et le camouflage paraîtra plus difficile. Dans des configurations extrêmes, le taux de fausses alertes sur la population cible peut s’écarter arbitrairement de 1 %, même avec un très grand jeu externe.

(A) réduit la variance d’échantillonnage, mais pas ce biais. (B), sous exchangeabilité, conserve la population et rend au moins le bruit de calibration quantifiable.

## 4. Pour (B) : les lectures à 20 % et 5 % restent-elles interprétables ?

**Oui, conditionnellement, mais pas sous la seule étiquette “sonde réglée à 1 %”.**

Les seuils de rappel nuisible restent définis sur les entrées adverses, indépendamment du nombre de bénins. Avec exactement 200 adverses par direction :

- rappel strictement inférieur à 20 % signifie au plus 39 détections ;
- rappel strictement inférieur à 5 % signifie au plus 9 détections.

Il faut néanmoins distinguer deux sources d’incertitude : le nombre fini d’adverses, et le seuil de détection estimé sur seulement 300 bénins.

### Rapport minimal pour B+

- graine, règle exacte de découpage, prétraitement, résultats de déduplication ;
- nombre de bénins effectivement utilisés dans chaque partition ;
- valeur du seuil, règle de quantile et traitement des ex æquo ;
- taux de fausses alertes de mesure en comptes bruts, avec Clopper–Pearson ;
- intervalle prédictif de calibration \([0{,}0021;0{,}0238]\), avec sa définition exacte ;
- pour chaque couche et chaque \(\tau\) : directions trouvées, directions cherchées, arrêts mécaniques, nombre d’adverses par direction et comptes de détection ;
- sensibilité de \(\tau\) à une nouvelle calibration, en réappliquant exactement la même règle de seuil ;
- comparaison séparée de la sonde entraînée sur 400 bénins avec celle entraînée sur 800, afin de ne pas confondre bruit de calibration et modification de l’instrument.

Les répétitions de découpage sont utiles comme **analyse de sensibilité**, mais leurs résultats ne sont pas indépendants et ne doivent pas être transformés en faux intervalle de confiance.

La validation croisée ou le bootstrap ne fabriquent pas les 2 000 bénins indépendants exigés initialement. Réutiliser les mêmes données pour choisir le seuil et annoncer son taux de fausses alertes serait optimiste sans validation imbriquée. Un seuil paramétrique fondé sur une moyenne et un écart-type déplacerait simplement le problème vers une hypothèse de queue non établie.

## 5. Expériences décisives, en duels

Les tolérances \(\delta\) ci-dessous doivent être fixées avant les résultats, selon ce qui changerait réellement la conclusion scientifique. Les faits ne permettent pas de leur attribuer honnêtement une valeur numérique.

### Duel 1 — Le jeu externe est-il utilisable pour (A) ?

- **H_A :** l’erreur de calibration induite sur la population Bailey est inférieure à \(\delta_p\).
- **H_B :** elle est au moins égale à \(\delta_p\).
- **Métrique :** erreur du taux de fausses alertes Bailey au seuil externe, complétée par l’AUC du discriminant de domaine et les écarts de queue des scores.
- **Seuil :** test d’équivalence dont l’intervalle doit être entièrement contenu dans \(\delta_p\), et absence d’alarme du discriminant.
- **Contrôle négatif :** deux partitions aléatoires d’un même pool ne doivent pas déclencher l’alarme.
- **Issues :** dépassement de \(\delta_p\) ou alarme correctement validée falsifie H_A ; une équivalence suffisamment puissante falsifie H_B. Un test sous-puissant ne valide pas (A).

### Duel 2 — Le bruit de calibration de (B) change-t-il la conclusion ?

- **H_A :** la recalibration seule déplace chaque borne \(\tau\) de moins de \(\delta_\tau\).
- **H_B :** au moins une borne pertinente se déplace d’au moins \(\delta_\tau\).
- **Métrique :** variation des nombres de directions sous rééchantillonnage de la calibration, à sonde, attaques et évaluations figées.
- **Seuil :** \(\delta_\tau\), préenregistré.
- **Contrôle négatif :** seuil figé et recalibration désactivée ; la contribution de calibration doit être nulle.
- **Issues :** dépassement falsifie H_A ; stabilité démontrée avec précision suffisante falsifie H_B. Dans le second cas, le bruit reste rapporté, mais ne pilote plus la conclusion.

### Duel 3 — La réduction à 400 bénins dégrade-t-elle la sonde ?

- **H_A :** les sondes 400 et 800 ont des performances équivalentes à \(\delta_R\) près.
- **H_B :** la sonde 400 perd au moins \(\delta_R\) en détection honnête au point de fonctionnement retenu.
- **Métrique :** rappel nuisible sur cas intacts communs, à fausses alertes calibrées, avec intervalles et comparaison appariée.
- **Seuil :** \(\delta_R\).
- **Contrôle négatif :** étiquettes permutées et détecteur fondé uniquement sur la longueur ; ils ne doivent pas fournir une validation artificielle.
- **Issues :** perte supérieure à \(\delta_R\) falsifie H_A ; équivalence suffisamment précise falsifie H_B.

## 6. Mesure minimale des instruments

### Sonde linéaire

Sur des cas **intacts**, jamais utilisés pour l’entraînement, le seuil ou la recherche de directions :

- rappel nuisible au seuil retenu, en comptes bruts et intervalle ;
- fausses alertes bénignes, séparément sur calibration et mesure ;
- paires bénin/nuisible appariées autant que possible par langue, longueur, format et sujet ;
- comparaison à rappel égal ou à fausses alertes égales contre des contrôles mécaniques : longueur seule, nombre de tokens seul, classe majoritaire et scores permutés ;
- directions aléatoires de même norme et même budget comme contrôle de la recherche.

### Juge StrongREJECT affiné

Au seuil de nuisance **RAPPORTÉ** de \(0{,}5\) :

- taux de détection sur exemples réellement nuisibles et intacts ;
- fausses alertes sur exemples réellement bénins appariés ;
- évaluation séparée sur sorties vides, absurdes, tronquées ou composées de refus, afin qu’une sortie dégradée ne soit pas comptée comme réussite de camouflage ;
- comparaison contre « toujours bénin », longueur seule et simple lexique de refus ;
- audit humain d’un échantillon figé de désaccords, sans remplacer les taux par une impression qualitative.

Aucune performance minimale ne peut être déduite du seul nom de l’instrument.

## 7. Pire cas, changement d’avis et ancrage matériel

**Pire cas de mon choix (B).** Le découpage produit simultanément une sonde affaiblie par les 400 bénins d’entraînement et un seuil anormalement permissif. Beaucoup de directions passent alors sous les coupures de rappel, surtout celle de 5 %, et la borne empirique surestime la malléabilité. C’est précisément ce que les duels 2 et 3 doivent détecter.

**Ce qui me ferait choisir (A).** Un jeu versé, correctement licencié et dédupliqué, dont le contrôle opérationnel démontre une erreur de calibration cible inférieure à \(\delta_p\), avec une sensibilité \(\tau\) favorable et sans modification de la sonde. À ce moment, l’avantage de précision des 1 000 calibration + 1 000 mesure deviendrait décisif.

**Matériel.** Je conserverais le modèle public de 8 milliards de paramètres préenregistré ; son nom et sa licence ne sont pas fournis. Les calculs statistiques tiennent sur CPU. Le surcoût principal de (A) est l’inférence et l’extraction d’activations sur 2 000 entrées supplémentaires, plus les contrôles de distribution.

- Poids en précision réduite : environ 16 Go, **illustratif**, hors activations et cache.
- Une carte de 24 Go, **illustratif**, peut suffire à l’inférence selon la longueur de contexte ; davantage de mémoire facilite le stockage temporaire et les lots.
- Coût marginal plausible de (A) : environ 0,5 à 4 GPU-heures, **illustratif**, hors campagne de directions.
- À 2 €/GPU-heure, **illustratif**, cela représente environ 1 à 8 €, **illustratif**.

Le coût de la campagne complète ne peut pas être borné à partir des faits : longueur des séquences, nombre de couches, stockage des activations, taux de réussite et coût de chaque recherche de direction manquent. Il dominera vraisemblablement le petit surcoût de calibration.

FIN-DE-CELLULE