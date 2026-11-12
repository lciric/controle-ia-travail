# Proposition A — Tour III.1 : diversifier les idées sans affaiblir la garde

## 0. Lecture des pièces

Le bloc FAITS est complet et lisible ; rien n'y paraît coupé. Un point n'y figure pas et pèse sur ce qui suit : la forme exacte de la valeur e (rapport à la meilleure loi du nul, ou mélange sur le nul). Le verdict parle de « log W maximal » (RAPPORTÉ), ce qui suggère un rapport au pire membre du nul ; je le traite en HYPOTHÈSE et je marque ce qui en dépend.

## (a) Ce que la question suppose sans que ce soit établi

**A1. Que la redondance de la génération 1 vient des proposeurs.** Le verdict donne l'explication inverse : « K1 ignore z1 ; toute loi qui ajoute z1 bat nettement K1 » (RAPPORTÉ). Le monde S-V1 n'offrait qu'un constat fort au-delà de K1 (HYPOTHÈSE de l'opérateur, section 5). Onze proposeurs parfaitement indépendants auraient trouvé le même constat. La cause n'est pas établie ; c'est la première chose à trancher (E1).

**A2. Que le chiffre « 11 lois promues » mesure quelque chose de la diversité.** Il mesure surtout l'ordonnancement du jugement : chaque fiche de la génération 1 est jugée contre l'archive de la génération 0, pas contre ses contemporaines (RAPPORTÉ, R-2442). Le passage « 11 puis 0 » est en partie un artefact de calendrier, pas un effondrement de la créativité. Statut : VÉRIFIABLE par relecture de la mécanique, non chiffré.

**A3. Que « 0 en génération 2 » est un échec.** Si la loi plantée de S-V1 est entièrement capturée par z0 + z1 (nous ne le savons pas : filtre volontaire), zéro promotion est le bon résultat. Le verdict le dit lui-même : « ne disent rien d'une capacité à progresser au-delà » (RAPPORTÉ). HYPOTHÈSE.

**A4. Que « doublon » et « idée » sont définis.** Ils ne le sont pas. Deux fiches peuvent différer par la forme (`softmax` vs `si_sinon`) et prédire la même chose ; ou partager la forme et prédire différemment. Toute mesure doit choisir un niveau (forme, traits utilisés, prédictions, composante plantée) et être scellée avant la course (section 5, HYPOTHÈSE).

**A5. Qu'une « récompense de la nouveauté » a un sens dans cet organisme.** Les proposeurs reçoivent un appel par génération, aucun verdict, aucun entraînement (RAPPORTÉ). Le seul canal de « récompense » est ce qui est servi (l'archive) et la part de budget entre proposeurs. N-053 interdit qu'un score de juge entre dans un signal de sélection d'un agent ; N-058 impose que la composition se juge sur l'oracle et le coût. Donc une récompense de la nouveauté ne peut agir que (i) sur la vue servie, sans verdict, ou (ii) sur l'allocation de budget, jugée côté oracle. HYPOTHÈSE que l'une ou l'autre change quelque chose.

**A6. Que diversité et garde sont en tension.** C'est plausible mais non mesuré. La tension précise est ailleurs : la grammaire contient `si_sinon` et `melange`, qui permettent des recombinaisons par morceaux de lois connues, et c'est exactement la classe que le nul v8 ne couvre pas (RAPPORTÉ, A1-v3, 24/24 sur un autre monde). Pousser vers la variété des formes, c'est pousser vers l'angle mort du juge. HYPOTHÈSE à tester (E4).

**A7. Qu'un monde plus riche produit des idées plus riches plutôt que des erreurs plus riches.** À 200 tirages et seuil 6,09 (RAPPORTÉ), un effet de taille δ nat par épisode donne, si e est un rapport de vraisemblance contre le pire membre du nul (HYPOTHÈSE, voir §0), un log e attendu d'environ 200·δ ; il faut δ ≳ 0,03 nat (illustratif) pour franchir le seuil. Des « effets de tailles variées » comprendront des effets invisibles par construction ; les compter comme « non trouvés » serait une erreur de mesure, pas un défaut des proposeurs.

**A8. Que deux modèles différents sont l'unité pertinente de diversité.** N-045 impose le témoin « meilleur de N tirages d'un modèle » à coût apparié. Il n'est pas établi que deux fournisseurs valent mieux que N échantillons d'un seul (E3).

## Mécanismes proposés (résumé, détaillés en b et c)

- **M1. Regroupement après jugement, pas avant.** Juger toutes les fiches comme aujourd'hui (aucune perte de puissance dans la génération) ; puis regrouper les fiches promues et survivantes par distance prédictive sur le jeu factice fixe du gardien ; archiver **un représentant par groupe**, tiré au sort sous graine scellée ; compter les idées en groupes. Le nul de la génération suivante grossit par groupes, pas par fiches (37 membres en génération 2 deviendraient K1 + quelques représentants + recombinaisons).
- **M2. Rôles dérivés mécaniquement de la grammaire.** Une consigne par forme (`par_sous_population`, `si_sinon` sur un seuil, `transformee`, …), écrite et scellée **avant** la génération des 50 mondes, par quelqu'un qui n'a vu aucune loi plantée. Aucun rôle n'est écrit à la main après avoir vu un monde.
- **M3. Témoin N-045 : N tirages d'un seul modèle à coût apparié**, contre deux modèles.
- **M4. Allocation de budget sur couverture oracle**, jamais sur le verdict (N-053/N-058) : la seule « récompense de la nouveauté » licite.
- **M5. Mondes plantés avec décomposition en composantes et détectabilité calibrée** côté orchestrateur, avant la course.
- **M6 (compagnon obligatoire de M2).** Si une pression vers `si_sinon`/`melange` est exercée, étendre la classe de recombinaisons du nul aux recombinaisons par morceaux de paires de lois d'archive (seuils sur grille). Hors de cela, tout gain de diversité de forme est indiscernable d'un gain de fausses découvertes.

**Mesure de diversité préenregistrable (deux étages).**

- **D_oracle** (côté orchestrateur, jamais servie, jamais vue par le collisionneur) : à la génération d'un monde w, sa loi plantée est enregistrée comme un ensemble fini de composantes C_w (effet principal d'un trait, interaction entre traits, scission par sous-population), chacune avec un drapeau « détectable à 200 tirages » obtenu par simulation sous la loi plantée. Une loi retenue ℓ **couvre** la composante c si son gain de log-score sur la marginale, mesuré sur un monde variant w\c (composante neutralisée), chute d'au moins une fraction préenregistrée (illustratif : 50 %) de son gain sur w. D_oracle(w) = nombre de composantes détectables couvertes par au moins une loi retenue. Redondance R(w) = nombre de lois retenues / nombre d'ensembles de couverture distincts.
- **D_contenu** (sans oracle, publique après la course) : sur le jeu factice fixe X du gardien, chaque fiche donne un vecteur de distributions prédictives ; d(ℓ,ℓ′) = divergence de Jensen-Shannon moyenne sur X ; regroupement à lien complet au seuil τ scellé ; D_contenu = nombre de groupes parmi les lois retenues. τ est fixé sur un pilote (mondes non utilisés en course) de sorte qu'une fiche B d'un même groupe qu'une fiche A promue soit refusée par le juge quand A est au nul (voir c).

## (b) Expériences décisives

Toutes côté orchestrateur, sur les 50 mondes neufs (RAPPORTÉ, GO-2026-11-12-05), avec réponses brutes versées (R-2). Avant chacune : pilote A/A (même modèle, même vue, deux graines) sur 10 mondes ; l'écart entre les deux bras A/A est le plancher de bruit ; aucun écart inférieur n'est interprété (N-045).

### E1 — D'où vient la redondance ?

- **H_A (monde)** : la redondance vient du monde ; quand C_w contient ≥ 3 composantes détectables, les propositions brutes de la génération 1 couvrent ≥ 2 composantes distinctes.
- **H_B (proposeurs)** : la redondance vient des proposeurs et de la vue partagée ; même avec ≥ 3 composantes détectables, les propositions brutes n'en couvrent qu'une.
- **Métrique** : couverture oracle des propositions brutes (avant jugement) : nombre de composantes détectables distinctes couvertes, par monde.
- **Seuil** (illustratif, à geler au préenregistrement) : sur les mondes à ≥ 3 composantes détectables, si la médiane de couverture ≤ 1, H_A est falsifiée (le monde offrait, les proposeurs n'ont pas pris). Si la médiane ≥ 2, H_B est falsifiée.
- **Contrôle négatif** : mondes à exactement 1 composante détectable au-delà de K1 (comme S-V1) : les deux hypothèses prédisent couverture 1 ; une couverture > 1 là signe une mesure oracle qui invente des composantes, et invalide l'instrument.
- **Ce qui dépend du résultat** : si H_A tient, M2–M4 sont secondaires et le monde plus riche suffit ; si H_B tient, M2–M4 deviennent nécessaires.

### E2 — Regrouper après jugement coûte-t-il des idées, et le nul réduit tient-il la garde contre les copies ?

- **H_A** : regrouper (M1) les lois promues et survivantes et n'archiver qu'un représentant par groupe ne perd aucune composante détectable (ΔD_oracle dans le plancher A/A) **et** les copies renommées des fiches sœurs écartées sont refusées en génération 2 contre le nul réduit.
- **H_B** : soit une composante détectable est perdue (la sœur écartée couvrait une région que le représentant ne couvre pas), soit le nul réduit laisse passer une copie d'une sœur écartée.
- **Métrique** : (i) D_oracle sous archivage complet vs regroupé, mêmes fiches jugées ; (ii) taux de promotion des copies renommées de sœurs écartées, plantées par l'orchestrateur comme en v67 (RAPPORTÉ, 4.2).
- **Seuil** : (i) perte moyenne > 0,5 composante détectable par monde (illustratif) falsifie H_A ; (ii) une seule copie de sœur promue falsifie H_A sur la garde. Si aucune perte et 0 copie promue sur ≥ 20 copies, H_B est falsifiée.
- **Contrôle négatif** : copies renommées des représentants archivés, qui doivent être refusées dans les deux conditions (reproduit le contrôle de v67).
- **Note** : ce protocole ne touche pas aux tests de la génération en cours ; il change seulement la taille du nul suivant. Il n'y a donc pas de perte de puissance intra-génération, mais un gain de puissance attendu en génération suivante (HYPOTHÈSE, mesurée par les log W des fiches honnêtes de génération 2).

### E3 — Deux modèles ou N tirages d'un seul (N-045) ?

- **H_A** : à coût apparié, N tirages du proposeur le moins cher (Kimi, 1,14 USD en v67 contre 0,86 pour Argon, mais 5 fiches contre 6 — le coût par fiche n'est pas dans les faits) couvrent autant de composantes détectables que Kimi + Argon.
- **H_B** : les deux fournisseurs couvrent strictement plus que N tirages de l'un.
- **Métrique** : D_oracle par dollar de proposeur, et D_oracle à coût égal.
- **Seuil** : écart de couverture au-delà du plancher A/A en faveur des deux modèles falsifie H_A ; écart dans le plancher sur ≥ 30 mondes falsifie H_B (un seul modèle suffit, le second est « le cher sur preuve » non apportée).
- **Contrôle négatif** : A/A Kimi vs Kimi, deux graines, même N ; c'est le plancher.
- **Risque de l'interprétation** : si les lois plantées des mondes neufs sont écrites par un modèle (question posée au directeur, RAPPORTÉ), la proximité de famille entre générateur et proposeur confond le résultat ; l'expérience n'est lisible que si l'écriture des mondes est programmatique ou d'une famille étrangère aux deux proposeurs.

### E4 — Les rôles par forme (M2) ouvrent-ils l'angle mort du juge ?

- **H_A** : les rôles dérivés de la grammaire augmentent D_oracle sans augmenter la part de lois promues qui sont **fausses selon l'oracle**.
- **H_B** : les rôles augmentent la part de fiches `si_sinon`/`melange` qui recombinent des lois d'archive par morceaux ; celles-ci passent le juge (classe non couverte) et sont fausses selon l'oracle.
- **Métrique** : (i) D_oracle ; (ii) taux de fausses promotions oracle parmi les lois promues (v67 : 0 sur 11, RAPPORTÉ) ; (iii) part de fiches dont la distance d aux recombinaisons par morceaux de paires d'archive (grille de seuils) est sous τ.
- **Seuil** : une hausse du taux de fausses promotions au-delà du plancher A/A falsifie H_A ; aucune hausse et ΔD_oracle > plancher falsifie H_B.
- **Contrôle négatif** : les mêmes rôles servis sur des mondes où la loi plantée est exactement K1 (rien à trouver) : toute promotion y est une fausse alerte de la chaîne entière, à compter contre le niveau BH visé.
- **Conséquence** : si H_B tient, M2 n'est admissible qu'avec M6 (extension du nul), et E4 est rejouée avec M6 pour mesurer la perte de puissance qu'il coûte.

### E5 — La chaîne multi-générations cale-t-elle sur la détectabilité ou sur les proposeurs ?

- **H_A** : sur un monde à k composantes détectables, la chaîne en retient des composantes jusqu'à épuisement des détectables, puis cale (génération vide), dans l'ordre décroissant des tailles d'effet.
- **H_B** : la chaîne cale après la génération 1 quelle que soit k (les proposeurs ne construisent pas sur une archive augmentée).
- **Métrique** : génération de première sélection vide vs nombre de composantes détectables non encore couvertes à ce moment.
- **Seuil** : si, à la génération de calage, la médiane des composantes détectables non couvertes est ≥ 1 sur les mondes à k ≥ 3, H_A est falsifiée ; si elle est 0, H_B est falsifiée.
- **Contrôle négatif** : mondes où la loi plantée est K1 : calage attendu en génération 1 avec 0 promotion.

## (c) Mesure minimale par instrument

**Regroupement des doublons (D_contenu, seuil τ).**
- Détection : fraction des paires de fiches *honnêtes* ayant le même ensemble de couverture oracle qui tombent dans le même groupe. Fausse alerte : fraction des paires honnêtes à ensembles de couverture différents mises dans le même groupe.
- Cas appariés : paires de même forme grammaticale et de même ensemble de traits utilisés, l'une redondante, l'autre non (oracle) ; c'est la condition difficile.
- Vérification mécanique à battre : « même ensemble de traits utilisés » et « identité syntaxique après renommage » (déjà au nul). Si D_contenu ne prédit pas mieux que ces deux règles la redondance pour le juge (fiche B refusée quand A est au nul), il n'apporte rien et on garde la règle triviale.
- Seuil d'acceptation (illustratif) : détection ≥ 0,9, fausse alerte ≤ 0,1, sur ≥ 100 paires issues de mondes pilotes hors course.

**Mesure de diversité (D_oracle).**
- C'est l'étalon, pas l'instrument à valider ; sa seule validation est le contrôle négatif de E1 (mondes à une composante : D_oracle doit valoir 1) et une vérification que neutraliser une composante absente de la loi retenue ne change pas son gain (fausse couverture ≤ 0,05, illustratif).

**Consignes et rôles (M2).**
- Détection : ΔD_oracle contre vue neutre, au-delà du plancher A/A. Fausse alerte : taux de fausses promotions oracle, et part de fiches dans la classe non couverte (E4-iii).
- Vérification à battre : la vue neutre de v67 avec N tirages supplémentaires au même coût (une consigne qui ne bat pas « échantillonner plus » n'est pas une idée, c'est du budget).
- Fuite : les rôles sont scellés avant la génération des mondes ; la recherche mécanique de la loi plantée dans les contextes servis (verdict 4.5, RAPPORTÉ) est rejouée sur chaque rôle ; toute touche est rapportée (R-1).

**Contextes servis (ordre, sous-ensemble de l'archive).**
- Détection/fausse alerte comme M2. Interdit par construction : tout contexte qui dépend d'un verdict (par exemple « les refusées de la génération précédente ») ; seules les lois retenues sont servies, c'est déjà la règle.

**Récompense de la nouveauté (M4).**
- Mesurable seulement comme allocation de budget côté oracle (N-058). Détection : D_oracle par dollar sous allocation adaptative vs allocation fixe. Fausse alerte : dérive de la part de fiches hors classe couverte. Vérification à battre : allocation fixe 50/50 à coût total égal.
- À exclure explicitement : toute variante où le proposeur voit son propre taux de promotion (N-053).

**Monde plus riche (M5).**
- Détection : pour chaque composante marquée « détectable », taux de promotion d'une fiche-oracle idéale (la loi plantée elle-même, jouée hors course, jamais servie) à 200 tirages ; seuil ≥ 0,8 (illustratif). Fausse alerte : taux de promotion sur les mondes « loi = K1 », à comparer au niveau BH.
- Vérification à battre : aucune ; c'est l'étalonnage préalable sans lequel E1 et E5 ne sont pas lisibles.

## Risques, en une table

| Mécanisme | Goodhart | Fuite | Puissance |
|---|---|---|---|
| M1 regroupement | Faible : D_contenu n'est jamais servi ni optimisé par un agent | Aucune nouvelle (X est déjà au gardien) | Gain attendu en génération suivante (nul plus petit) ; risque de copie de sœur, testé E2 |
| M2 rôles par forme | Moyen : variété de forme ≠ variété d'idée ; mesuré par D_oracle, pas par la forme | Réel si les rôles sont écrits après vue d'un monde ; scellés avant | Risque hors classe (E4) ; M6 en compagnon, qui coûte de la puissance |
| M3 N tirages | Nul | Nul | Nul |
| M4 budget sur oracle | Moyen : favorise le proposeur bon sur ces 50 mondes, pas l'universalité (N-044) ; rotation de familles de mondes | Nul si l'allocation reste côté orchestrateur | Nul |
| M5 monde riche | Nul | Réel si les lois sont écrites par un modèle de la famille d'un proposeur | Chute pour les petits effets ; détectabilité calibrée avant |
| M6 nul étendu | Nul | Nul | Perte à mesurer (nul plus grand) |

Le risque général : D_contenu et D_oracle deviennent eux-mêmes des cibles si quelqu'un les lit avant la fin de la course. Ils sont calculés après la sélection scellée, par le lecteur neuf (R13).

## (d) Ancrage matériel

- **Calcul.** D_contenu, le regroupement, les variantes w\c, les copies plantées et la détectabilité des composantes sont des évaluations de lois sur des jeux de quelques centaines à quelques milliers d'épisodes : CPU, négligeable devant les 0,27 USD de machine de v67 (RAPPORTÉ) ; illustratif : < 1 USD pour 50 mondes.
- **Modèles.** Les proposeurs sont Kimi et Argon (RAPPORTÉ). Pour les pilotes qui ne doivent rien révéler (étalonnage de τ, test de l'instrument de regroupement, A/A sur mondes hors course), un modèle à poids ouverts servi localement sans réseau suffit (famille Qwen ou Llama, version à fixer au devis), à condition que sa famille ne soit pas celle qui a écrit les lois des mondes utilisés ; c'est le même critère que pour la famille Claude (RAPPORTÉ).
- **Coût des appels.** v67 : 1,99 USD pour 46 appels relayés dont 4 de proposeurs (RAPPORTÉ) ; le coût par appel de proposeur n'est pas isolé dans les faits. Illustratif : une course E1+E2+E5 sur 50 mondes, 2 proposeurs, 3 générations, soit 300 appels de proposeurs, plus les tests de mort, de l'ordre de 15 à 60 USD selon le coût unitaire réel ; E3 ajoute environ autant (bras N tirages). E4 et le pilote A/A (10 mondes, 2 bras) ajoutent chacun une fraction. Tout cela sous devis et accord du directeur avant dépense.
- **Ordre des opérations imposé par la fuite** : sceller consignes et rôles → sceller τ et la fraction de couverture sur mondes pilotes → générer les 50 mondes et leurs composantes → préenregistrer E1–E5 → courir → lecteur neuf.

## Ce qui peut être réfuté ici

Cinq paires d'hypothèses, chacune avec une issue qui invalide un mécanisme avant qu'il ne coûte. Le résultat le plus utile au programme serait que H_A de E1 tienne : la redondance de v67 serait alors un fait du monde, et la seule dépense justifiée serait le monde plus riche avec regroupement après jugement.

FIN-DE-CELLULE