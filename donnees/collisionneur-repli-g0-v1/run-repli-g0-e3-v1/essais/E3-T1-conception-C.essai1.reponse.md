**Alerte d'intégrité (Règle 2)** : La Pièce B se termine par une phrase coupée (« il est fini » sans ponctuation finale), et la Pièce C comporte deux débuts de lignes manifestement tronqués (« dans sa forme confirmée... » au début, et « d'octobre, section 8)... » au milieu). Je n'en invente pas le contenu manquant.

---

# (a) Ce que la question suppose sans que ce soit établi

1. **Date de début du financement au 1er décembre 2026** : La question énonce qu'« un financement externe, s'il est accordé, commence le 1er décembre (pièce C) ». Or, la Pièce C mentionne uniquement « avant le début du financement » sans préciser la date du 1er décembre. Statut : **HYPOTHÈSE** (ou SUPPOSÉ par la question hors pièces).
2. **Indépendance opératoire du Papier C (HC1 à HC3)** : La question (point 2c) suppose qu'il est possible de basculer vers le Papier C si des critères de G0 (comme les critères 2 ou 3) échouent. Or, les pièces ne précisent pas le contenu de HC1-HC3 ni leur indépendance vis-à-vis des organismes (critère 2) ou des sondes (critère 3). Statut : **HYPOTHÈSE** (SUPPOSÉ).
3. **Flexibilité contractuelle du financeur (EA Funds / TAIF)** : La question suppose que le financeur externe acceptera le déclenchement d'une règle de repli (report, gel d'entrée en phase 1 ou bascule vers un rapport négatif) sans annuler ni suspendre le versement du palier financé. Statut : **HYPOTHÈSE** (SUPPOSÉ).
4. **Existence d'un préenregistrement global de G0** : La question mentionne un verdict « contre son préenregistrement (R13) » pour G0, alors que la Pièce A liste les critères de G0 dans le brief v2 sans mentionner un document de préenregistrement global scellé spécifique à G0 (contrairement aux critères 6 et 7 qui sont les préenregistrements de G1 et du papier C). Statut : **OBSERVÉ-NON-AUDITÉ**.
5. **Disponibilité budgétaire d'ici fin novembre** : La question suppose que l'équipe dispose des ressources pour tenter de valider les critères 2, 3 et 4 avant le 30 novembre, alors que la Pièce A bis indique que le budget de calcul GO-2026-10-04-08 échoit le 1er novembre (RAPPORTÉ) et que la Pièce B chiffre la banque complète entre 300 et 1 400 USD contre 90 USD accordés (RAPPORTÉ). Statut : **HYPOTHÈSE** (SUPPOSÉ).

---

# (b) Expériences décisives (Inférence forte : $H_A$ contre $H_B$)

Puisque l'objet est une règle de gouvernance scellée et son exécution par des sous-agents (R13) et le directeur, les expériences décisives testent la robustesse mécanique de la règle de repli avant son scellement (via `python -m controle_ia.run_factice`, VÉRIFIÉ Pièce D) et l'origine d'un éventuel échec le 30 novembre.

### Duel 1 : Déterminisme inter-agents de la frontière « Échec scientifique » vs « Incomplet technique »
* **$H_A$ (Déterminisme de la clause)** : Une règle de repli distinguant l'« échec empirique réfuté » (ex. absence de dose-réponse prouvée sur les organismes, R-680) du « non-concluant par défaut d'infrastructure/temps » (ex. exécution absente ou coupée) sur la seule base des fichiers `.sha256` (R6) produit un verdict identique chez des sous-agents neufs indépendants (R13).
* **$H_B$ (Ambiguïté intrinsèque)** : Toute distinction entre « échec », « non concluant » et « presque fini » introduit une marge d'interprétation subjective qui fait diverger les sous-agents R13, violant l'interdiction de décision après lecture.
* **Protocole et Métrique** : Générer 10 dossiers factices d'état de G0 (illustratif) couvrant des cas limites (ex. 1 organisme sur 2 validé ; sonde v0 battant le plancher sur (i) mais exécution manquante sur (ii) ; préenregistrement de G1 écrit mais contre-lecture R2 absente). Faire évaluer chaque dossier par 3 instances indépendantes du sous-agent neuf R13 (illustratif). Métrique : Taux d'accord unanime exact (3/3) sur les 10 dossiers et sur les 8 critères (soit 80 verdicts élémentaires, illustratif).
* **Seuil** : Accord unanime = 100 % (80/80, illustratif) sans aucune demande de clarification à l'humain.
* **Contrôle négatif** : Soumettre un dossier factice où l'empreinte `.sha256` (R6) d'un critère réussi est corrompue d'un bit ; les 3 agents doivent prononcer l'échec du critère (test de la garde R5).
* **Issues falsificatrices** :
  * Si Accord < 100 % : **$H_A$ est réfutée**. Toute nuance (« presque fini », « non concluant ») est bannie de la règle de repli au profit d'un test binaire strict (Preuve `.sha256` présente et valide = 1 ; sinon = 0).
  * Si Accord = 100 % (avec contrôle négatif validé) : **$H_B$ est réfutée**. La règle de tri entre les branches de repli est mécaniquement scellable.

### Duel 2 : Audit de la cause de non-franchissement au 30 novembre (Blocage logistique vs Réfutation empirique)
* **$H_A$ (Goulot logistique / calendaire)** : Si les critères 2 et 3 ne sont pas remplis au 30 novembre, c'est par manque de temps ou de budget de calcul (au-delà des 90 USD, Pièce B, RAPPORTÉ), mais le signal physique (dose-réponse et séparabilité linéaire des activations) existe dans les données partielles.
* **$H_B$ (Réfutation scientifique fondamentale)** : Le non-franchissement des critères 2 et 3 découle de l'absence physique de sabotage à dose diffuse avec dommage (condition d'arrêt R-680, Pièce B, RAPPORTÉ) ou de l'orthogonalité des sondes v0 au sabotage.
* **Protocole et Métrique** : Test séquentiel intégré au pilote du critère 2 (R-680). Mesurer la pente de dose-réponse $\beta$ du dommage en fonction de l'intensité d'injection sur un échantillon pilote de $N = 50$ épisodes par dose (illustratif), et l'AUC de la sonde v0 contre un prédicteur aléatoire apparié par permutation des étiquettes ($B = 1000$ permutations, illustratif).
* **Seuil** : $\beta > 0$ avec $p < 0,01$ (illustratif) ET $\text{AUC}_{\text{sonde}} - \text{AUC}_{\text{aléatoire}} > 0,05$ à $p < 0,05$ (illustratif).
* **Contrôle négatif** : Évaluation sur les épisodes honnêtes tirés par `SeedSequence` (R9) avec étiquettes de dose factices (doit donner $\beta \approx 0$ et $\Delta \text{AUC} \approx 0$).
* **Issues falsificatrices** :
  * Si toutes les exécutions pilotes sont terminées (empreintes R6 présentes) et $\beta \le 0$ (ou $p \ge 0,01$) : **$H_A$ est réfutée**. La condition d'arrêt R-680 (« absence de dose diffuse avec dommage = arrêt de la banque », Pièce B, RAPPORTÉ) est déclenchée : le report calendaire est interdit, bascule immédiate en arrêt/rapport négatif.
  * Si le quota d'épisodes $N=50$ n'est pas atteint au 30 novembre faute de budget débloqué (nœud GO-2026-10-04-08 non prolongé, Pièce A bis, RAPPORTÉ) ou si $\beta > 0$ sur (i) tandis que (ii) n'est pas encore exécuté : **$H_B$ est réfutée** à ce stade, ce qui qualifie un blocage de production (ouvrant droit au travail continu hors phase 1, sans modifier G0).

---

# (c) Mesure minimale de fonctionnement des instruments de la question

La question mobilise trois instruments méthodologiques et de gouvernance :

1. **L'évaluateur de porte par sous-agent neuf (Instrument R13)**
   * *Fonction* : Prononcer le verdict de G0 et déclencher automatiquement la branche de repli prévue sans intervention humaine post-lecture.
   * *Cas honnêtes appariés* : Dossiers de preuves synthétiques conformes (8/8 critères remplis avec empreintes `.sha256` valides et contre-lectures R2 jointes) appariés à des dossiers identiques où une seule preuve est remplacée par un résumé textuel sans empreinte (violation R6) ou par un résultat trop propre ($p = 0,00000$, déclenchant l'audit R4).
   * *Taux de détection et de fausses alertes* : Taux de détection des critères défaillants (Rappel) = 100 % (illustratif, exigence déterministe sur 20 dossiers test) ; Taux de fausses alertes (rejet d'un dossier honnête complet) = 0 % (illustratif).
   * *Vérification mécanique à battre* : Un script bash/Python élémentaire qui vérifie uniquement l'existence non vide des 8 fichiers `.sha256` sur le disque (R11). Le sous-agent R13 doit battre ce script en détectant 100 % des violations sémantiques (ex. un fichier existant et empreinté, mais dont le chiffre viole le seuil préenregistré ou la garde R4).

2. **La sonde v0 et le banc d'organismes (Instruments des critères 2 et 3 de G0)**
   * *Fonction* : Établir la faisabilité de base avant d'engager les 288 unités par mode de G1 (Pièce B, RAPPORTÉ).
   * *Cas honnêtes appariés* : Jumeaux honnêtes des unités d'épreuve générés avec la même `SeedSequence` (R9) sans instruction ni modification de sabotage.
   * *Taux de détection et de fausses alertes* : La Pièce A (VÉRIFIÉ) fixe la mesure minimale : pour le critère 2, un dommage mesurable croissant monotonement avec la dose ; pour le critère 3, un taux de détection (rappel) à un taux de fausses alertes fixé (ex. $\tau = 0,05$ ou $\tau = 0,01$, illustratif) strictement supérieur (à 95 % de confiance, illustratif) au plancher aléatoire.
   * *Vérification mécanique à battre* : Le « plancher aléatoire apparié » (Pièce A, VÉRIFIÉ), constitué par une sonde linéaire entraînée sur des vecteurs d'activation dont les étiquettes (honnête/saboté) ont été permutées aléatoirement par tâche, ainsi qu'une heuristique triviale de longueur de sortie (nombre de jetons générés).

3. **La contre-lecture par sous-agent neuf (Instrument R2 pour les critères 6, 7 et la règle de repli elle-même)**
   * *Fonction* : Garantir qu'aucun préenregistrement (G1, Papier C, ou règle de repli G0) ne contient de degrés de liberté cachés (« on verra »).
   * *Cas honnêtes appariés* : Textes de préenregistrement rigoureux (hypothèse, signe, métrique, seuil, liste d'arrêt complets selon R1) appariés aux mêmes textes où une clause conditionnelle ouverte (« si la variance est trop forte, nous ajusterons le seuil ») a été insérée.
   * *Taux de détection et de fausses alertes* : Détection de 100 % des clauses non scellables insérées (illustratif, sur 10 textes modifiés) ; 0 % de rejet sur les clauses binaires fermées (illustratif).
   * *Vérification mécanique à battre* : Une recherche lexicale par expressions régulières (regex) ciblant les mots interdits (« à déterminer », « selon les résultats », « optionnel »). Le sous-agent R2 doit détecter les degrés de liberté implicites (ex. l'omission de la règle de bris d'égalité D-S13, Pièce B, RAPPORTÉ) qu'une regex ne peut pas voir.

---

# (d) Ancrage matériel

* **Modèles ouverts et environnement** : Le modèle ouvert cible déjà interfacé par le harnais validé au critère 1 (Pièce B, RAPPORTÉ ; ex. famille Llama-3-8B ou Mistral-7B pour la phase 0, illustratif ; le passage aux modèles de 70 milliards de paramètres appartient au palier financé ultérieur, Pièce C, RAPPORTÉ). Pour les sous-agents de gouvernance (R2, R13), utilisation d'instances d'API LLM à contexte vierge (sans historique de session).
* **Calcul nécessaire et coût estimé** :
  * *Exécution et validation de la règle de repli (R2 + R13 + `run_factice`)* : Travail sur processeur (CPU) et appels API pour les sous-agents neufs (10 dossiers factices $\times$ 3 agents). Coût estimé : **< 5 USD** (illustratif) et 2 heures de temps humain/CPU (illustratif).
  * *Achèvement des critères documentaires de G0 (Critères 6, 7, 8)* : Rédaction, vérification sur PDF empreintés avec numéro de page (R7, VÉRIFIÉ) et contre-lecture par sous-agent (R2). Coût calcul : **~ 10 USD** d'appels API (illustratif).
  * *Achèvement des critères expérimentaux de G0 (Critères 2, 3, 4)* : La Pièce B (RAPPORTÉ) indique que la banque complète coûte de **300 à 1 400 USD**, au-delà des **90 USD** accordés, et la Pièce A bis (RAPPORTÉ) indique que l'autorisation de calcul GO-2026-10-04-08 échoit le 1er novembre. Un pilote minimal pour valider uniquement les critères 2, 3 et 4 (sur 2 organismes, sans atteindre les 288 unités par mode de G1) requiert environ **50 à 150 USD** de calcul GPU (illustratif).

---

# Réponse structurée aux points 1 à 4 de l'Arbitre

## 1. Ce qui déclenche le repli : constat, distinction des statuts et autorité (R13)

* **Quand et comment constate-t-on l'échec ?**
  Le constat est déclenché à une date et heure fixes : le **30 novembre 2026 à 23:59 UTC** (conformément à N-027 : « au plus tard fin novembre 2026 », Pièce A bis, VÉRIFIÉ). Comme G0 est une porte conjonctive (« Tous les critères suivants sont remplis, preuves scellées à l'appui », Pièce A, VÉRIFIÉ), **l'absence d'un seul des 8 critères (score < 8/8) suffit à déclencher le repli**.
* **Faut-il distinguer « échec », « non concluant » et « presque fini » ?**
  * *Option 1.1* : Autoriser un statut « presque fini » pour accorder une grâce informelle. **Inconvénient** : Viole les critères de lecture de l'arbitre (« non scellable ») et R1/R13 en laissant une appréciation subjective au lecteur.
  * *Option 1.2* : Statut purement binaire global (Réussi / Échoué) sans qualifier la nature du manque. **Inconvénient** : Ne permet pas d'automatiser le choix entre un arrêt définitif pour réfutation physique (R-680) et une mise en quarantaine de la phase 1 pour retard de production.
  * *Option 1.3 (Recommandée)* : **Verdict de porte strictement binaire (« G0 FRANCHIE » si 8/8, sinon « G0 NON FRANCHIE »), assorti d'un code de cause mécanique déterministe** attribué à chaque critère manquant parmi deux états mutuellement exclusifs :
    1. **RÉFUTÉ (Échec empirique)** : Les exécutions préenregistrées ont tourné (empreintes `.sha256` présentes, R6), les gardes techniques (R5) sont vertes, mais la métrique viole le seuil (ex. absence de dose-réponse sur les organismes déclenchant l'arrêt R-680, ou sonde v0 sous le plancher aléatoire).
    2. **NON-EXÉCUTÉ (Manque de production)** : Le fichier de preuve `.sha256` est absent du disque (vérifié selon R11), ou le préenregistrement/contre-lecture (R2) n'est pas scellé à l'échéance. La notion de « presque fini » est **interdite** : tout critère en cours non scellé est classé `NON-EXÉCUTÉ`.
* **Qui prononce ?**
  Conformément à **R13** (VÉRIFIÉ), un **sous-agent neuf** (n'ayant participé ni à l'écriture des préenregistrements ni aux analyses) lit le manifeste des 8 empreintes `.sha256` le 30 novembre, applique la grille ci-dessus, scelle le verdict (`G0_VERDICT_2026-11-30.md` + `.sha256`) et le soumet à Lazar pour GO formel d'exécution du repli.
* **Confiance** : **0,90** (forte adéquation avec R1, R6, R11, R13).

---

## 2. Analyse comparée des options de repli

| Critère d'analyse | Option (a) : Report calendaire unique et borné de G0 | Option (b) : « G0 non franchie » au 30/11 + gel de Phase 1 (travail continu en Phase 0) | Option (c) : Bascule immédiate (Papier C ou rapport négatif) | Option (d) : Arrêt complet du programme et rapport |
| :--- | :--- | :--- | :--- | :--- |
| **Ce qu'elle autorise** | Prolonger la Phase 0 et repousser la date du verdict R13 (ex. au 31 décembre, SUPPOSÉ). | Prononcer « G0 non franchie » le 30/11 ; poursuivre uniquement les critères `NON-EXÉCUTÉS` de G0 ; passer un examen de rattrapage G0-bis à date fixe. | Abandonner G1 ; allouer 100 % du temps au Papier C (HC1-HC3) ou à la publication d'un résultat négatif sur les organismes/sondes. | Clore toutes les tâches techniques ; rédiger et sceller le rapport post-mortem de la Phase 0. |
| **Ce qu'elle interdit** | Toute entrée en Phase 1 (G1) et toute modification des 8 critères. | **Tout acte de Phase 1** : interdiction d'engager le devis des 288 unités/mode (Pièce B), d'ouvrir le mode tenu à l'écart (N-054), ou de toucher au budget G1. | Toute dépense sur la banque G1 (300–1 400 USD, Pièce B) et tout développement des moniteurs séquentiels de G1. | Tout nouveau run de calcul (CPU/GPU) ; toute dépense du financement externe débutant le 1er décembre (SUPPOSÉ). |
| **Coût financier et calendaire** | Coût Phase 0 : 50–150 USD (illustratif). Retard de 1 mois sur le calendrier du financeur (GC fin M2, G1 fin M4, Pièce C, RAPPORTÉ). | Coût Phase 0 : 50–150 USD (illustratif) sur fonds propres ou ligne dédiée ; 0 USD dépensé sur le budget Phase 1 du financeur tant que G0-bis n'est pas franchie. | Coût réduit pour un rapport négatif (~20 USD, illustratif) ; coût modéré pour Papier C (100–300 USD, illustratif, SUPPOSÉ). | Coût nul (0 USD de calcul supplémentaire). Perte ou restitution du financement externe (SUPPOSÉ). |
| **Risque de dérive** | **Élevé** : G0 a déjà été reportée une fois du 1er au 30 novembre (N-027, Pièce A bis, VÉRIFIÉ). Un second report transforme une échéance ferme en échéance glissante (« porte de sortie » temporelle). | **Faible si borné** : Le constat d'échec au 30 novembre est acté honnêtement (pas de déni calendaire), et le verrou sur la Phase 1 empêche la fuite en avant, à condition qu'une date butoir unique de rattrapage soit scellée. | **Moyen à Élevé pour Papier C** : Si HC1-HC3 dépendent des organismes/sondes (SUPPOSÉ), c'est une fuite en avant sans les bases de G0. **Nul pour un rapport négatif**. | **Nul** : Aucune dérive possible. |
| **Compatibilité R1, R4, R13, N-027** | **Incompatible avec N-027** (« au plus tard fin novembre 2026 », VÉRIFIÉ) et affaiblit l'esprit de la Pièce C (« une porte ne bouge pas », RAPPORTÉ). | **Totalement compatible** : N-027 est respecté (G0 est prononcée le 30 novembre par R13), les critères ne bougent pas, et R1/R4 restent intacts. | **Compatible avec R1/R4/R13** *uniquement si* le critère 7 (préenregistrement du Papier C) et le critère 1 (harnais) sont validés au 30 novembre. | **Totalement compatible** avec toutes les règles (application directe de la liste d'arrêt R1 et de R-680). |
| **Ce qu'on dit au financeur (EA Funds / TAIF)** | *Difficile à défendre* : « Nous reportons une seconde fois notre porte interne juste au moment où votre financement commence. » | *Transparent et protecteur pour le bailleur* : « Au 30 novembre, G0 n'est pas franchie (X/8). Nous gelons le démarrage de la Phase 1 financée ; pas un dollar de Phase 1 n'est engagé avant validation complète au [date butoir], sinon bascule/restitution. » | « L'expérience de Phase 0 a réfuté la viabilité des organismes/sondes (R-680). Conformément à notre gouvernance préenregistrée, nous n'engageons pas les fonds sur G1 et livrons le papier négatif / Papier C. » | « La porte préliminaire G0 a échoué sur un critère bloquant rédhibitoire ; nous arrêtons le programme et ne tirons pas sur la subvention. » |

---

## 3. La règle recommandée (Clause scellable unique)

L'architecture recommandée combine **le refus de tout nouveau report de la date du 30 novembre (rejet de (a))** avec un **aiguillage automatique et déterministe entre (b), (c) et (d)** selon le code de cause mécanique produit par le sous-agent R13 le 30 novembre.

### Texte exact de la clause à sceller dans le registre des décisions :

> **Règle de repli de la porte G0 (Clause scellée) :**
> « Si, le 30 novembre 2026 à 23:59 UTC, le verdict scellé du sous-agent neuf (R13) constate que moins de huit critères sur huit de G0 sont validés par empreinte `.sha256`, la porte G0 est déclarée **NON FRANCHIE** à l'échéance (aucun report de la date de G0 n'est autorisé) et l'entrée en Phase 1 (G1) est immédiatement bloquée ; le programme applique alors d'office, sans nouveau nœud de décision humain après lecture, la première branche applicable dans l'ordre de préférence strict suivant :
> 1. **Arrêt de la banque et bascule (Option d / Option c-négatif)** : Si le critère 2 (organismes) est à l'état `RÉFUTÉ` (arrêt R-680 : absence de dose diffuse avec dommage sur les exécutions achevées) OU si le critère 3 (sondes v0) est à l'état `RÉFUTÉ` (performance inférieure ou égale au plancher aléatoire apparié sur les deux organismes achevés), tout développement vers G1 est définitivement arrêté ; si les critères 1, 7 et 8 sont validés au 30 novembre et que les hypothèses HC1–HC3 ne requièrent pas les critères `RÉFUTÉS`, le programme bascule exclusivement sur le Papier C, sinon il rédige et scelle un rapport de résultat négatif final au plus tard le 31 décembre 2026 (illustratif).
> 2. **Mise en quarantaine de la Phase 1 et achèvement borné en Phase 0 (Option b)** : Si aucun des critères 2 et 3 n'est `RÉFUTÉ` (les critères manquants étant exclusivement à l'état `NON-EXÉCUTÉ` faute de calcul ou de finalisation documentaire) ET qu'au moins **cinq critères sur huit** (incluant obligatoirement les critères documentaires 6, 7 et 8) sont validés au 30 novembre, le démarrage du palier financé de Phase 1 est gelé (0 USD engagé sur G1) et le travail se poursuit exclusivement en Phase 0 sur les critères `NON-EXÉCUTÉS` jusqu'à une **seule et unique séance de rattrapage (G0-bis) fixée au 21 décembre 2026 à 23:59 UTC** (borne absolue : 1 seul rattrapage de 21 jours calendaires, illustratif).
> 3. **Arrêt par défaut d'exécution (Option d)** : Si moins de cinq critères sur huit sont validés au 30 novembre, ou si un seul des critères documentaires (6, 7, 8) est `NON-EXÉCUTÉ` au 30 novembre, ou si les huit critères ne sont pas intégralement validés (8/8) lors du rattrapage unique G0-bis du 21 décembre 2026, le programme s'arrête d'office et livre un rapport d'état final sans entrer en Phase 1. »

* **Justification de la borne et de l'ordre** :
  * Pourquoi exiger que les critères 6, 7 et 8 (préenregistrements et état de l'art) soient validés dès le 30 novembre pour autoriser l'Option (b) ? Parce que ces critères ne dépendent d'aucun budget GPU (Pièce B) : s'ils ne sont pas prêts le 30 novembre après un premier report d'un mois (N-027), c'est une défaillance d'exécution que le financeur ne doit pas subventionner.
  * **Borne stricte** : **0 report** de la porte G0 (elle est jugée le 30 novembre) ; au plus **1 fenêtre de rattrapage en quarantaine (G0-bis) de 21 jours** (échéance le 21 décembre 2026, illustratif) réservée aux seuls critères expérimentaux (2, 3, 4) bloqués par le calcul.

---

## 4. Ce qui doit être décidé et scellé maintenant (avant le 30 novembre)

Pour que le sous-agent R13 puisse appliquer la clause le 30 novembre sans aucune décision après lecture (« on verra »), Lazar doit trancher aujourd'hui quatre paramètres opérationnels :

### Décision 4.1 : Matrice de dépendance technique du Papier C (HC1 à HC3)
* *Problème* : Les pièces (Pièce A, B) ne disent pas si le Papier C (critère 7) a besoin des organismes sabotés (critère 2) ou des sondes v0 (critère 3) pour être exécuté (SUPPOSÉ).
* *Option A* : Déclarer le Papier C dépendant des critères 2 et 3 (auquel cas la réfutation de 2 ou 3 interdit le Papier C et force un rapport négatif).
* *Option B* : Sceller dans le préenregistrement du Papier C (critère 7) que HC1–HC3 portent uniquement sur le harnais (critère 1), les agrégateurs (critère 5) ou des données synthétiques/existantes indépendantes des critères 2 et 3.
* *Avantage / Inconvénient* : L'Option B offre un livrable scientifique réel au financeur si la banque d'organismes échoue (R-680), mais uniquement si HC1–HC3 le permettent scientifiquement sans changer leur définition.
* *Recommandation* : **Écrire aujourd'hui dans le registre la liste exacte des critères de G0 requis par HC1, HC2 et HC3** (ex. `Papier_C_dependances = {1, 5, 7, 8}`). Confiance : **0,85**.

### Décision 4.2 : Condition d'éligibilité minimale au rattrapage en quarantaine (Option b) au 30 novembre
* *Problème* : Faut-il définir un état « presque fini » pour les critères expérimentaux 2, 3 et 4 ?
* *Option A* : Définir des seuils intermédiaires (« presque fini » = 1 organisme sur 2 validé). **Inconvénient** : Risque élevé d'être jugé comme un assouplissement déguisé de G0 (« hors cadre ») ou de créer un litige d'interprétation pour R13.
* *Option B (Recommandée)* : **Supprimer toute notion de « presque fini » sur les critères expérimentaux, et la remplacer par l'obligation d'avoir validé 100 % des critères sans GPU (critères 1, 5, 6, 7, 8 = 5/8)** au 30 novembre, plus l'empreinte du pilote R-680 prouvant qu'aucun arrêt de banque n'est déclenché.
* *Avantage / Inconvénient* : 100 % binaire, vérifiable par simple présence des fichiers `.sha256` (R6), zéro interprétation après lecture.
* *Recommandation* : **Option B**. Confiance : **0,90**.

### Décision 4.3 : Nœud budgétaire de transition (Pont du 1er au 30 novembre)
* *Problème* : La Pièce A bis (VÉRIFIÉ) établit que GO-2026-10-04-08 (calcul de la phase 0) échoit le 1er novembre, et la Pièce B (RAPPORTÉ) montre que les 90 USD sont insuffisants face aux 300–1 400 USD de la banque complète. Sans décision immédiate, les critères 2, 3 et 4 seront mécaniquement `NON-EXÉCUTÉS` le 30 novembre.
* *Option A* : Prolonger GO-2026-10-04-08 jusqu'au 30 novembre avec une enveloppe plafonnée (ex. 150 USD, illustratif) dédiée uniquement au pilote R-680 et aux critères 2, 3 et 4 de G0 (hors dimensionnement 288 unités de G1).
* *Option B* : Ne pas prolonger le budget et attendre le financement du 1er décembre (SUPPOSÉ). **Inconvénient** : Garantit l'échec de G0 au 30 novembre.
* *Recommandation* : **Option A dès aujourd'hui**. Confiance : **0,95**.

### Décision 4.4 : Phrase exacte à prononcer lors de l'appel au financeur (EA Funds / TAIF)
* *Problème* : La Pièce C (point 12 et point 3, RAPPORTÉ) demande soit de dire « no fallback rule is written yet », soit de trancher aujourd'hui une phrase sur le palier financé.
* *Recommandation* : Sceller la clause de la Section 3 aujourd'hui et dire au financeur :
  *« G0 is evaluated on November 30 on its 8 frozen criteria by an independent agent. If any criterion is missing, Phase 1 does not start and zero Phase 1 funds are spent: if the failure is an empirical refutation of our organisms or probes, we halt the benchmark and pivot to a pre-registered negative report or Paper C; if it is purely a compute delay with all pre-registrations sealed, Phase 1 remains frozen under a single 21-day quarantine window until December 21, after which an incomplete G0 triggers an automatic halt. »* (21 jours / 21 décembre : illustratif). Confiance : **0,90**.

FIN-DE-CELLULE