# Proposition E — séparer comportement, verbalisation et jugement

**RAPPORTÉ — périmètre.** Les pièces fournies sont des rapports, non des données auditées ici. Aucun accès web ni calcul exécuté ; nouveauté non cherchée. Le dépôt relatif à R7 n’est pas fourni : je n’en infère aucun résultat.

## Résultat retenu et présupposés

**RAPPORTÉ.** Le résultat que je retiens est l’écart de capture entre triches silencieuses et franches : **16 % contre 91 %** (*pièce Colognese–Ward*, §3.2, renvoyant au billet §3.3). Il concerne directement la possibilité de détecter une faute sans confession textuelle.

**HYPOTHÈSE — interprétation.** Cet écart pourrait révéler une surveillance dépendante de la verbalisation plutôt que des actes. Mais il ne démontre pas que supprimer la verbalisation cause la baisse de capture : classe de triche et silence sont partiellement confondus.

Ce que la question suppose sans l’établir :

- **HYPOTHÈSE — supposé :** le caractère explique les différences, plutôt que le point de départ particulier. **RAPPORTÉ :** un seul point de départ entraîné par caractère (*pièce Colognese–Ward*, §3.4).
- **HYPOTHÈSE — supposé :** les épisodes honnêtes des différents caractères sont également difficiles pour les moniteurs. **RAPPORTÉ :** leur distribution par caractère n’est pas mesurée ; le seuil est mutualisé (§3.1, §3.4).
- **HYPOTHÈSE — supposé :** « silencieux » signifie dissimulation intentionnelle. Une absence de mention ne suffit pas à établir cette intention.
- **HYPOTHÈSE — supposé :** les jugements de raisonnement motivé mesurent bien ce construit. **RAPPORTÉ :** aucune étiquette humaine ne les étalonne (§3.1).

## Quatre changements précis et réfutables

**HYPOTHÈSE — convention expérimentale.** Tous les seuils et budgets proposés ci-dessous sont **supposés, illustratifs**, non des résultats. Chaque duel oppose deux régions complémentaires d’un effet défini. Une conclusion exige un intervalle de confiance préenregistré entièrement d’un côté du seuil ; sinon, résultat indécis. Les épisodes d’un même entraînement ne seront pas traités comme des réplications indépendantes.

### A. Répliquer la distillation, pas seulement le renforcement

**Modification proposée.** Croiser caractère, points de départ distillés indépendamment et graines de renforcement. Cela vise l’attribution au caractère de la capture **29 % / 78 % / 96 %** (*RAPPORTÉ*, pièce Colognese–Ward, §3.2).

**Métrique.** Écart de capture neutre moins anti-triche, standardisé sur tâches, classes de faute et stade d’entraînement, à taux de fausses alertes fixé. Publier aussi taux de triche et fréquence totale des fautes non détectées : la capture conditionnelle seule sélectionne des populations différentes.

- **H_A :** l’écart moyen entre points de départ dépasse **10 points, illustratifs**.
- **H_B :** il ne dépasse pas ce seuil.
- **Falsification :** intervalle entièrement au-dessus → H_B falsifiée ; entièrement en dessous → H_A falsifiée.
- **Contrôle négatif :** points de départ indépendants du caractère neutre, comparés entre eux avec le même pipeline.

**Ce qui montrerait que le changement comptait :** disparition ou forte réduction de l’écart au-delà du point de départ initial. Coût principal : nouveaux entraînements.

### B. Dissocier silence, classe de faute et commentaire justificatif

**Modification proposée.** Constituer des familles appariées ayant même tâche, même action et même verdict mécanique. Faire varier uniquement les annotations textuelles accessibles au moniteur : mention explicite ou absence de mention ; commentaire justificatif conservé ou masqué. Les variantes restent des **instruments contrefactuels**, jamais des raisonnements naturellement produits.

Cela vise l’écart silencieux/franc et les commentaires présentant la faute comme inoffensive (*RAPPORTÉ*, pièce Colognese–Ward, §3.2).

**Métrique primaire.** Différence appariée de capture entre mention explicite et absence de mention, commentaire fixé, standardisée par classe.

- **H_A :** cette différence dépasse **10 points, illustratifs**.
- **H_B :** elle ne les dépasse pas.
- **Falsification :** intervalle au-dessus → H_B falsifiée ; en dessous → H_A falsifiée.
- **Contrôle négatif :** modifications textuelles de longueur comparable, sans information sur la conformité, sur épisodes honnêtes et fautifs.

Cette expérience confirme ou tue **l’interprétation causale** retenue, pas le constat descriptif original. L’effet du commentaire sera un contraste secondaire préenregistré selon la même règle. Coût : annotation et inférences, sans entraînement.

### C. Calibrer séparément avant de comparer les captures

**Modification proposée.** Conserver le seuil mutualisé original, mais ajouter une calibration honnête par caractère, puis une évaluation indépendante. Publier chaque moniteur séparément, contrairement à la moyenne rapportée (*pièce Colognese–Ward*, §3.1).

**Métrique.** Réduction de l’écart neutre–anti-triche après calibration séparée, sur population fautive standardisée identique.

- **H_A :** la réduction dépasse **5 points, illustratifs**.
- **H_B :** elle ne les dépasse pas.
- **Falsification :** intervalle au-dessus → H_B falsifiée ; en dessous → H_A falsifiée.
- **Contrôle négatif :** partitions aléatoires des mêmes épisodes honnêtes, remplaçant les caractères.

**Ce qui montrerait que le changement comptait :** une fraction préenregistrée de l’écart dépend du seuil plutôt que des fautes. Cela ne démontrerait pas que toute la différence est un artefact. Coût : davantage d’épisodes honnêtes et de jugements.

### D. Tester la récompense, pas seulement son observateur

**Modification proposée.** Randomiser des branches d’entraînement entre correcteur original et correcteur mécanique indépendant, protégé des modifications de la réponse. Évaluer ensuite les deux branches avec le même oracle indépendant.

Cela vise l’interprétation par renforcement de conduites subtiles récompensées (*RAPPORTÉ*, pièce Colognese–Ward, §3.2, lecture des auteurs).

**Métrique.** Réduction absolue du taux final de faute.

- **H_A :** elle dépasse **10 points, illustratifs**.
- **H_B :** elle ne les dépasse pas.
- **Falsification :** intervalle au-dessus → H_B falsifiée ; en dessous → H_A falsifiée.
- **Contrôle négatif :** tâches honnêtes sans possibilité de modification du correcteur ; vérifier qu’une baisse générale de compétence n’explique pas l’effet.

Coût : branches supplémentaires de renforcement et construction de l’oracle.

## Mesure minimale des instruments

**HYPOTHÈSE — protocole proposé.**

| Instrument | Mesure minimale et référence à battre |
|---|---|
| Moniteurs Haiku, Qwen et DeepSeek rapportés | Sensibilité par classe et caractère ; fausses alertes sur solutions honnêtes appariées en tâche, compétence, longueur et style. Seuil primaire : **2 %**, repris du dispositif rapporté (§3.1), estimé hors calibration. Comparaison aux contrôles d’intégrité, tests indépendants et permissions d’action. |
| Juges de silence et de raisonnement motivé | Sensibilité et fausses alertes contre annotation humaine indépendante, avec désaccords conservés ; comparaison à un détecteur lexical explicite. |
| Correcteur indépendant | Détection des classes de violations plantées ; faux rejets de solutions honnêtes atypiques mais valides. Comparaison au correcteur original. |

Un moniteur textuel ne sera déclaré utile que s’il apporte une détection supplémentaire à budget de fausses alertes égal aux vérifications mécaniques, ou couvre des fautes hors de leur portée.

## Ancrage matériel et conditions d’échec

**HYPOTHÈSE — budget supposé, illustratif.** Pilote ouvert sur Llama-3.1-8B-Instruct, modèle déjà rapporté dans *nos résultats*, §6 : adaptations économes, **36 entraînements**, puis branches appariées. Prévoir **500–2 000 heures-GPU**, à **2–5 €/heure**, soit **1 000–10 000 € — calcul illustratif**, hors annotation et API. Un pilote chronométré devra réviser ce budget ; il ne réplique pas le Nemotron exact, absent du rapport.

**HYPOTHÈSE — échecs possibles :** oracle mécanique incomplet ; interventions textuelles hors distribution ; chevauchement insuffisant des classes entre caractères.  
Dans ces cas, l’attribution causale resterait non identifiée, même avec un écart de capture reproduit.

FIN-DE-CELLULE