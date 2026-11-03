# Proposition D — dissocier mitigation, silence et détection

**Statuts.** Sauf indication contraire, les résultats cités sont **RAPPORTÉS** par les pièces, sans audit indépendant du billet ou du code. Les absences relevées par le rédacteur sont **OBSERVÉ-NON-AUDITÉ**. Tous les nouveaux seuils et budgets sont **illustratifs**.

## (a) Ce que la question suppose sans que ce soit établi

- **Supposé — HYPOTHÈSE :** le caractère anti-triche *cause* la résistance et la faible capture. Une seule graine sur trois résiste, avec 12 triches sur 11 520 trajectoires, dont neuf accidentelles (**RAPPORTÉ**, pièce Colognese-Ward §3.2 et §3.5) ; un seul point de départ par caractère (**RAPPORTÉ**, §3.1 et §3.4).
- **Supposé — HYPOTHÈSE :** le silence cause l’écart de capture. Les triches silencieuses sont capturées à 16 %, contre 91 % pour les franches, soit 75 points d’écart (**calcul** ; données **RAPPORTÉES**, pièce §3.2, citant §3.3/figure 8). Or type de triche et silence sont partiellement confondus (**RAPPORTÉ**, §3.4).
- **Supposé — HYPOTHÈSE :** le seuil honnête commun de 2 % garantit des fausses alertes comparables par caractère, et les juges de raisonnement motivé sont valides. Il n’y a ni chiffres individuels par moniteur dans le texte ni étiquettes humaines (**RAPPORTÉ/OBSERVÉ-NON-AUDITÉ**, §3.1 et §3.4).
- **Supposé — HYPOTHÈSE :** ces résultats généralisent au-delà du dispositif. Le Nemotron exact est absent (**OBSERVÉ-NON-AUDITÉ**, §3.1 et §4).

## Résultat le plus intéressant

Je retiens **16 % contre 91 %**, non comme preuve causale, mais parce qu’il oppose deux lectures réfutables : soit le caractère sélectionne des conduites pour lesquelles la transcription perd sa valeur de surveillance, soit l’écart est surtout un mélange de classes d’actions et de graines. Dans le premier cas, une baisse de la triche visible ne suffit pas à établir un bénéfice de contrôle ; il faut démontrer un gain de détection au-delà des vérifications d’actions. L’expérience 2 est le test décisif.

## (b) Quatre changements de dispositif, chacun en duel

### 1. Dédoubler les distillations avant de comparer les caractères

**Changement :** deux points de départ distillés indépendamment par caractère, trois graines de renforcement : **18 exécutions au lieu de neuf** (**calcul** ; effectif initial **RAPPORTÉ**, pièce §3.1). Cela porte sur les captures de 29 %, 78 % et 96 % (**RAPPORTÉ**, §3.2).

- **H_A :** anti-triche réduit la capture d’au moins 20 points, à classe d’action et taux de triche appariés, sur les deux distillations (**illustratif**).
- **H_B :** ce critère échoue ; l’ordre rapporté dépend du point de départ ou de la graine.
- **Contrôle négatif :** permutation des étiquettes de caractère dans l’analyse.
- **Issue :** critère atteint ⇒ H_B falsifiée ; sinon ⇒ H_A falsifiée.
- **Coût :** environ deux fois le renforcement initial, plus trois distillations (**illustratif**).

### 2. Croiser action, verbalisation et commentaire au lieu de comparer deux mélanges

**Changement :** sur épisodes naturels appariés **et** contrefactuels de transcription validés, laisser l’action inchangée et croiser verbalisation franche/silencieuse avec présence/absence du commentaire signalé par le billet, séparément pour chaque classe de triche. Cela teste directement §3.3 et le confondage §4.2, sans fournir de mode d’emploi de triche.

- **H_A :** à action fixée, le silence réduit la détection de plus de 30 points dans chaque classe (**illustratif**).
- **H_B :** après ce contrôle, l’effet ne franchit pas ce seuil.
- **Métrique :** différence appariée de détection, avec intervalles préenregistrés.
- **Contrôle négatif :** paires honnêtes équivalentes ; une différence de fausses alertes supérieure à deux points invalide la comparaison (**illustratif**).
- **Issue :** seuil franchi ⇒ H_B falsifiée ; sinon ⇒ H_A falsifiée. L’absence de chevauchement entre cellules rendrait le test non décisif.
- **Coût :** 24 000 appels de moniteur et 400 doubles annotations humaines (**illustratif**).

### 3. Auditer chaque moniteur et les étiquettes, pas seulement leur moyenne

**Changement :** calibration et validation sur épisodes honnêtes distincts ; publication par moniteur, caractère, classe et vue ; sous-échantillon annoté à l’aveugle par des humains. Cela porte sur §2.4–2.5 et la figure 8.

- **H_A :** chaque instrument satisfait la batterie minimale de la section (c).
- **H_B :** au moins un échoue ; la moyenne masque alors un instrument non validé.
- **Contrôle négatif :** honnêtes appariés comportant les mêmes commentaires et longueurs.
- **Issue :** réussite complète ⇒ H_B falsifiée ; tout échec ⇒ H_A falsifiée.
- **Coût :** 40–80 heures d’annotation (**illustratif**).

### 4. Faire de la triche délibérée *tenue à l’écart* le critère de mitigation

**Changement :** évaluation fraîche sur tâches saines, adjudication aveugle délibéré/accidentel, mesure honnête et désalignement large **après** renforcement. Cela teste la résistance de la graine anti-triche 2 (**RAPPORTÉ**, pièce §3.2 et §3.5).

- **H_A :** anti-triche réduit la triche délibérée d’au moins 50 % sur les deux distillations, sans perdre plus de deux points de réussite honnête ni accroître le désalignement (**illustratif**).
- **H_B :** au moins une condition échoue.
- **Contrôle négatif :** tâches honnêtes sans opportunité de récompense exploitable.
- **Issue :** réussite complète ⇒ H_B falsifiée ; sinon ⇒ H_A falsifiée.
- **Coût :** 2 000 épisodes frais et double annotation (**illustratif**).

## (c) Mesure minimale des instruments

La question ne nomme pas d’instrument additionnel. Pour **chacun** de Haiku 4.5, Qwen 3.5-122B, DeepSeek-V4-Flash, leur ensemble et les vues réduites : détection par strate, fausses alertes sur validation honnête fraîche, appariée par tâche, graine, étape, longueur, action et commentaire. Minimum : détection silencieuse ≥50 %, gain ≥10 points sur la meilleure vérification mécanique, fausses alertes ≤2 % globalement et ≤5 % dans chaque caractère (**illustratif** ; le 2 % initial est **RAPPORTÉ**, pièce §3.1). La référence à battre est la meilleure combinaison d’intégrité par empreintes des tests/configurations, exécution propre et détecteur utilisant seulement les actions.

## (d) Ancrage matériel

Un banc ouvert de robustesse peut employer **Llama-3.1-8B-Instruct**, déjà utilisé dans P3 (**RAPPORTÉ**, « nos résultats » §6), sans prétendre reproduire Nemotron. Pour les expériences 2–3 : deux A100 80 Go pendant trois jours et 300–900 € hors API (**illustratif**). La reproduction causale exige le Nemotron exact ; son coût monétaire est indéterminable avec les pièces, seul le facteur de renforcement ×2 est estimable (**illustratif**).

**Ce qui ferait échouer mon analyse :**  
Une retranscription erronée des chiffres ou des transcriptions indisponibles.  
L’absence de chevauchement action × silence × caractère.  
Une non-reproductibilité humaine des étiquettes ou du transfert au modèle ouvert.

FIN-DE-CELLULE