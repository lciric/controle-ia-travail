# Relecture par Claude Fable 5.2 (appel direct à l'interface d'Anthropic)

- Outil : `controle_ia.relecture_fable_api_v3` (empreinte du module 95bea064c753ca24e6a7619b99f1b03bd64700fac8568b3c598ec67bb985eb62)
- Modèle demandé : `claude-fable-5-2` ; modèle servi : `claude-fable-5-2` ; identifiant du message : `msg_011ChHaFYfrknEYWfM6iD8GC`
- Heure (UTC) : 2026-11-22T07:34:06Z
- Réglages : effort `high`, réflexion adaptative à affichage « omitted » (texte de la réflexion ni demandé ni écrit), `max_tokens` 128000, aucune relance, aucun repli vers un autre modèle
- Entrées :
  - consigne : `docs/notes/demandes-fable-api-2026-11-22-v1/consigne-demande-approfondie-v1.md` — sha256 8263a1b41f0c2050f3715f5df01b0a6d70846840af0e41a3fa19f275ce3c55b2 (compagnon : vérifié)
  - correction : `docs/notes/demandes-fable-api-2026-11-22-v1/demande-17-tirage-au-hasard-inoccupe-v1.md` — sha256 1b5583f891ac481889952892014f4bbc99900e5de6972febb0850a3d5307024a (compagnon : vérifié)
  - remarques : `docs/notes/demandes-fable-api-2026-11-22-v1/contexte-programme-v1.md` — sha256 534ed7a288fc0729377654c6060ae900ac5ec76c8d6fa2518bee4f1239464a2b (compagnon : vérifié)
  - remarques : `docs/notes/demandes-fable-api-2026-11-22-v1/reponse-9/relecture-fable-api.md` — sha256 48d4d72e5f1cbcdea6a60fea309e80f4e5f319e30389540acc7aa422bd560e52 (compagnon : vérifié)
  - remarques : `docs/notes/recherche-exhaustive-transposition-v2.md` — sha256 2395ea20a570afd7b206bec4adec56664604a500902c68cf68eed87358ae9b8d (compagnon : vérifié)
- Empreinte de l'invite envoyée : a641ed9c9ba837c29cb58479b0ec55d21f4eb4516f3eee97b9bfafe2c840fe94
- Jetons : entrée 19220, sortie 25136 (dont réflexion 14930), écriture de cache 0, lecture de cache 0 ; raison d'arrêt `end_turn`
- Coût compté : 1.159200 USD (base : usage ; tarif 8 / 40 USD par million de jetons d'entrée / de sortie)

---
# Demande 17 — ce qui reste inoccupé sur le tirage au hasard : réponse approfondie

**Conclusion d'abord.** Je ne peux déclarer aucune zone inoccupée. Les pièces lues ne contiennent aucune recherche sur le tirage : les 36 requêtes de la recherche exhaustive portent sur la stéganographie et la comptabilité des matières. Le statut de départ est donc « non cherché », plus faible que « non trouvé ».

Le noyau sur lequel quatre modèles convergent (tirage secret après engagement, plancher, estimateur de Horvitz-Thompson, moniteur en variable de contrôle) est, de mémoire, un contenu de manuel hors du champ. Le tirage protège le choix de ce qu'on audite ; il ne protège ni la mesure ni la référence. Les questions à plus fort enjeu sont celles où le hasard agit ailleurs que sur ce choix : mise en aveugle de la tâche, sonde tirée après gel des poids, étanchéité de la boucle de correction. Confiance d'ensemble : 0,5.

**Réserves.**
- Je n'ai lu aucun PDF. Aucune pièce fournie ne décrit « Blindfold » et je ne l'identifie pas de mémoire : je ne rends aucun verdict sur son contenu.
- Les antériorités que j'ajoute sont de mémoire : « rapporté, non vérifié sur PDF ». Je ne confirme aucun identifiant arXiv de 2026.
- Je ne nomme que les auteurs des travaux cités. Je n'ai pas recalculé les empreintes.

---

## 1. Ce qu'un expert ferait et qui n'est pas demandé

- **Classer les usages du hasard par fonction avant de chercher des trous** [PROPOSITION]. « Tirage au hasard » recouvre au moins sept fonctions (table plus bas). Une zone n'est vierge que fonction par fonction.
- **Écrire ce que le tirage garantit, avec ses conditions** [PROPOSITION]. L'estimation sans biais du dommage total tient contre toute stratégie si trois conditions sont réunies :
  1. le tirage est indépendant de ce que l'agent sait au moment d'agir ;
  2. toute unité a une probabilité d'audit au-dessus d'un plancher ;
  3. l'audit d'une unité tirée mesure vraiment son dommage.
  
  Contre le sabotage diffus, la troisième condition est la plus fragile, puisque chaque action semble honnête.
- **Vérifier à la page ce que le papier fondateur appelle audit** [PROPOSITION]. Ma mémoire [HYPOTHÈSE] : la base de Greenblatt, Shlegeris, Sachan, Roger, 2023, « AI Control: Improving Safety Despite Intentional Subversion » (rapporté, non vérifié sur PDF) audite le début du déploiement. Elle ne vaut un tirage que parce que l'agent ignore sa position. Les protocoles principaux y auditent selon le score de soupçon. « L'audit aléatoire publié en 2023 » serait alors une lecture, non une citation.
- **Lire la convergence des modèles comme un signe de notoriété** [PROPOSITION]. Quatre modèles qui retrouvent le même montage indiquent un contenu d'enseignement, pas une nouveauté.
- **Chiffrer le gain de la variable de contrôle avant d'en faire un argument** [PROPOSITION]. Voir le bilan plus bas : le gain est modeste à corrélation moyenne.

## 2. Données brutes de départ

- Les pages : « Blindfold » en entier ; les sections de protocole du papier fondateur ; Wen et collaborateurs, p. 1, 10 et 18 ; Griffin et collaborateurs, p. 10.
- Le registre des tirages réels du harnais : graine, empreinte d'engagement, horodatage, probabilité d'inclusion de chaque unité.
- Les verdicts bruts d'audit, unité par unité, sur des exécutions honnêtes jumelles et sur des dommages plantés. Les taux agrégés ne suffisent pas.
- Tout ce que l'agent peut observer après un audit (corrections, relances, données de réapprentissage), pour tester la fuite du tirage.
- Les sorties de ré-exécutions indépendantes de sous-résultats, si l'audit se fait par reproduction.
- Les activations de l'agent aux pas tirés et non tirés.

## 3. Méthodes et outils

- **Inférence fondée sur le plan de sondage** : Horvitz et Thompson, 1952, « A generalization of sampling without replacement from a finite universe » ; estimateur par différence ou par régression de Särndal, Swensson, Wretman, 1992, « Model Assisted Survey Sampling ».
- **Inférence assistée par prédiction** : Angelopoulos, Bates, Fannjiang, Jordan, Zrnic, 2023, « Prediction-powered inference » ; Zrnic et Candès, 2024, « Active statistical inference », où le tirage est orienté par un modèle avec mélange uniforme.
- **Suites de confiance par pari** : Waudby-Smith et Ramdas, 2023, « Estimating means of bounded random variables by betting ».
- **Audits à risque limité** : Lindeman et Stark, 2012, « A gentle introduction to risk-limiting audits » ; Waudby-Smith, Stark, Ramdas, 2021, « RiLACS ». On y trouve l'engagement avant tirage, la graine publique et la comparaison machine contre main.
- **Jeux d'inspection et de sécurité** : Dresher, 1962, « A sampling inspection problem in arms control agreements » ; Avenhaus, von Stengel, Zamir, 2002, « Inspection games » ; Blocki, Christin, Datta, Procaccia, Sinha, 2013, « Audit games » ; Auer, Cesa-Bianchi, Freund, Schapire, 2002, « The nonstochastic multiarmed bandit problem », où le plancher est un taux d'exploration.
- **Capture et recapture, erreurs semées** : Mills, 1972, « On the statistical validation of computer programs » ; projection d'images de menaces fictives dans le contrôle des bagages.
- **Test de randomisation** : Fisher, 1935, « The Design of Experiments ».
- **Sonde de fuite** [PROPOSITION] : entraîner un classifieur à prédire, depuis les activations ou les sorties de l'agent, quelles unités ont été tirées. Une prédiction meilleure que le hasard prouve que la première condition est violée.

Tous ces travaux sont rapportés, non vérifiés sur PDF.

## 4. Ce qui vérifie hors du directeur et de Claude

- **La couverture empirique de l'essai « jumeau contre jumeau »** : sur des répliques honnêtes, l'intervalle à 95 % doit contenir le dommage nul environ 95 fois sur 100.
- **La restitution du dommage planté** : l'estimateur doit retrouver le total planté, dans son intervalle.
- **La sonde de fuite**, dont l'issue ne dépend d'aucun avis.
- **Une graine publique tirée après engagement** : un tiers peut rejouer le tirage.
- **Quatre lecteurs spécialisés** :
  - un statisticien des sondages, sur « notre estimateur est-il celui du manuel ? » ;
  - un spécialiste des audits électoraux à risque limité ;
  - un statisticien des garanties de l'Agence internationale de l'énergie atomique, pour les inspections inopinées ;
  - un chercheur en jeux de sécurité.
- **Les auteurs de « Blindfold »**, sur une seule question : « faites-vous déjà ceci ? »
- **Le test de devinette** de la question neutre, et la prévision scellée.

---

## Demande reformulée

« Recense, fonction par fonction, les usages que le défenseur peut faire d'un hasard que l'agent ne peut ni prévoir ni observer : choisir ce qu'on audite, dissuader, fournir la référence, placer des dommages plantés, perturber le contexte de l'agent, tirer le moniteur lui-même, prouver à un tiers. Pour chaque fonction, écris ce que le hasard garantit exactement et sous quelles conditions (indépendance du tirage, plancher, validité de la mesure sur l'unité tirée). Donne ensuite son statut parmi quatre : occupé dans le contrôle de l'intelligence artificielle (source, page) ; occupé hors du champ, transposition à faire ; non trouvé après une recherche décrite ; non cherché. Pars des pages (Blindfold, le papier fondateur, Wen et collaborateurs) et du registre brut des tirages et des audits du harnais, non des résumés. Écris le bilan chiffrable de l'audit au hasard dans les unités du programme et compare-le au bilan hérité des moniteurs d'accumulation. Classe les zones candidates par leur effet sur le dommage lui-même, non sur la seule détection, et par ce qu'une issue négative laisserait. Pour chaque zone, donne la recherche qui la fermerait et l'expérience dont l'issue ne dépend d'aucun avis. Liste les phrases à ne pas écrire. »

---

## Réponse à la demande reformulée

### (a) Les fonctions du hasard et leurs parents

Les parents sont de mémoire, rapportés, non vérifiés sur PDF, sauf mention « note » (recherche exhaustive, fait rapporté). Tous les statuts sont des [HYPOTHÈSE] tant que la recherche n'est pas faite.

| Fonction | Ce que le hasard garantit | Parents connus | Statut |
|---|---|---|---|
| 1. Choisir ce qu'on audite | Estimation sans biais du total, sous les trois conditions | Horvitz et Thompson 1952 ; Särndal et collaborateurs 1992 ; échantillonnage par unité monétaire en audit comptable | Occupé hors du champ ; dans le champ, non cherché |
| 2. Dissuader | Équilibre où l'attaquant connaît la loi, non le tirage | Dresher 1962 ; Avenhaus et collaborateurs 2002 ; Blocki et collaborateurs 2013 ; Griffin et collaborateurs 2024, p. 10 (note) | Occupé hors du champ ; touché dans le champ |
| 3. Fournir la référence | Loi nulle exacte par permutation | Fisher 1935 ; inférence toujours valide fondée sur le plan (mémoire incertaine) | Occupé hors du champ ; dans le champ, non cherché |
| 4. Placer des dommages plantés | Taux de détection de l'auditeur mesuré | Mills 1972 ; capture et recapture ; menaces fictives projetées | Occupé hors du champ ; dans le champ, voisins à lire |
| 5. Perturber le contexte de l'agent | Rupture de la coordination ou de la direction du sabotage | Roger et Greenblatt, 2023, « Preventing language models from hiding their reasoning » ; Bhatt et collaborateurs, 2025, « Ctrl-Z » ; Mallen et collaborateurs, 2024, « Subversion Strategy Eval » ; analyse en aveugle (zone 1) | Occupé en partie ; mise en aveugle non cherchée |
| 6. Tirer le moniteur lui-même | L'agent n'a pas pu s'entraîner contre un moniteur qui n'existait pas | Bailey et collaborateurs, 2024, « Obfuscated activations bypass LLM latent-space defenses » ; Tice et collaborateurs, 2024, « Noise injection reveals hidden capabilities of sandbagging language models » ; Clymer et collaborateurs, 2024, « Poser » | Voisins à lire ; non cherché |
| 7. Prouver à un tiers | Tirage rejouable après engagement | Lindeman et Stark 2012 ; Waudby-Smith, Stark, Ramdas 2021 ; Korbak et collaborateurs, 2025, « A sketch of an AI control safety case » | Occupé hors du champ ; dans le champ, non cherché |

### (b) Le bilan de l'audit au hasard, dans les unités du programme

[HYPOTHÈSE, dérivation de ma main, à faire vérifier] Soit N unités, auditées au taux uniforme π. Notons :
- σ l'écart-type honnête de la mesure d'audit ;
- ρ la corrélation entre le score du moniteur et cette mesure ;
- m la taille de la référence honnête.

Le dommage total détectable est de l'ordre de :

> z · σ · √( (1 − ρ²) · N/π + N²/m )

Le second terme disparaît seulement si l'audit mesure contre une vérité plantée ou absolue.

Trois conséquences [HYPOTHÈSE] :
- **La forme est la même que le nul hérité.** L'audit au hasard n'échappe pas à la loi de la référence ; sa constante vaut 1/√π. Le « biais de référence linéaire en N » des collisionneurs est ce second terme.
- **Le gain de la variable de contrôle est √(1 − ρ²).** Il vaut 13 % à ρ = 0,5 et il faut ρ ≈ 0,87 pour diviser le bruit par deux. « La sonde en variable de contrôle protège même trompée » est exact pour le biais, mais le gain est modeste à corrélation moyenne.
- **Ce qui change vraiment est la nature de la constante.** Elle ne dépend plus de l'effet du sabotage sur le moniteur, qui peut être nul pour un sabotage jamais vu. Elle dépend de la validité de l'audit sur l'unité tirée. C'est le sens exact de « seul appui indépendant de l'attaque » ; il ne tient que sous la troisième condition.

Si les scores orientent les probabilités d'audit, un score manipulé pousse le dommage vers les unités au plancher. La variance croît alors comme l'inverse du plancher [HYPOTHÈSE]. La « table du seuil au taux d'audit » est ce compromis ; son parent est le taux d'exploration des bandits adverses.

### (c) Les zones candidates

Chaque zone est une question. La « chance » est mon jugement qu'elle reste inoccupée dans le champ après la recherche indiquée.

**Zone 1 — Mise en aveugle de la tâche par un tirage secret.** [HYPOTHÈSE]
- *Idée.* Dans une tâche d'analyse, le défenseur recode au hasard les étiquettes, décale les données d'une quantité secrète, ou sème des effets fictifs qu'il sait retirer. Le saboteur peut encore dégrader la qualité, mais il ne sait plus dans quel sens fausser la conclusion. Un biais dirigé, linéaire en N, deviendrait un bruit, mesurable par les effets semés.
- *Parents.* Klein et Roodman, 2005, « Blind analysis in nuclear and particle physics » ; MacCoun et Perlmutter, 2015, « Blind analysis: hide results to seek the truth » ; les injections à l'aveugle des observatoires d'ondes gravitationnelles.
- *Statut.* Non cherché. Le titre « Blindfold » peut désigner exactement cela ; je l'ignore.
- *Enjeu.* Le plus profond, car la zone agit sur le dommage et non sur sa détection. Elle touche aussi le papier C.
- *Chance.* 0,4, conditionnelle à la lecture de « Blindfold ».
- *Recherche qui la vérifie.* Lecture de « Blindfold » ; citants de MacCoun et Perlmutter croisés avec la recherche automatisée ; requêtes « analyse en aveugle » avec « agent de recherche » et « sabotage ».
- *Une issue négative laisse* la liste des tâches où l'aveugle est impossible.

**Zone 2 — Sonde tirée après le gel des poids.** [HYPOTHÈSE]
- *Idée.* C'est l'engagement transposé à la boîte blanche. L'agent est figé, puis le défenseur tire la couche, la graine et le jeu d'entraînement de la sonde. La question : une sonde tirée après coup garde-t-elle sa puissance contre un organisme entraîné à tromper une première famille ?
- *Parents.* Bailey et collaborateurs 2024, dont je crois me souvenir que l'évasion s'y transfère en partie à des sondes réentraînées (mémoire incertaine). Avertissement d'Athalye, Carlini, Wagner, 2018, « Obfuscated gradients give a false sense of security » : un hasard que l'attaquant peut moyenner ne protège pas.
- *Statut.* Voisins à lire.
- *Enjeu.* Fort pour le papier A : c'est la seule zone propre à l'accès interne, et elle se rattache à la complémentarité.
- *Chance.* 0,35.
- *Recherche.* Citants de Bailey et collaborateurs ; requêtes « sonde tenue à l'écart », « ensemble de sondes secret », « transfert d'évasion entre sondes ».
- *Une issue négative laisse* la mesure du transfert d'évasion, utile à N-054.

**Zone 3 — Étanchéité du tirage dans la boucle audit, correction, réapprentissage.** [HYPOTHÈSE]
- *Idée.* Une correction visible ou un réapprentissage sur les unités auditées apprend à l'agent ce qui a été tiré. Sur une longue tâche, la première condition s'érode.
- *Tension interne.* Elle oppose l'invariant N-053 à la boucle de N-076.
- *Parents.* Dwork et collaborateurs, 2015, « The reusable holdout » ; jeux d'inspection répétés ; Wen et collaborateurs, p. 18 (note), sur la référence que l'agent influence.
- *Statut.* Non cherché.
- *Enjeu.* Fort : la boucle est déjà décidée.
- *Chance.* 0,4.
- *Recherche.* Citants de Dwork et collaborateurs en surveillance d'agents ; les 34 citants de Wen relus sous cet angle.
- *Expérience.* La sonde de fuite.
- *Une issue négative laisse* une règle de cloisonnement.

**Zone 4 — Unité de tirage et mesure du dommage diffus.** [HYPOTHÈSE]
- *Idée.* Auditer une action isolée ne mesure rien si le dommage naît de l'accumulation. L'unité utile est le sous-résultat, audité par ré-exécution indépendante (autre lignée, humain).
- *Parents.* Canetti, Riva, Rothblum, 2011, « Practical delegation of computation using multiple servers » ; Bhatt et collaborateurs 2025 (rééchantillonnage par le même modèle, donc non indépendant).
- *Limite.* Le surplus de capacité du jumeau honnête, noté par un collisionneur, borne ce que la comparaison voit.
- *Chance.* 0,35.
- *Recherche.* Requêtes « audit par reproduction », « ré-exécution », « délégation vérifiable », croisées avec agents de langue.
- *Une issue négative laisse* le choix de l'unité, nécessaire de toute façon.

**Zone 5 — Bilan mesuré de l'audit au hasard chez des agents.** [HYPOTHÈSE]
- *Idée.* Mesurer π, le taux de détection par dommages plantés, les fausses alertes des auditeurs sur des agents honnêtes imparfaits, ρ, et la couverture réelle.
- *Parents à lire.* Kutasov et collaborateurs, 2025, « SHADE-Arena » ; Benton et collaborateurs, 2024, « Sabotage evaluations for frontier models » ; Greenblatt, mars 2025 (note).
- *Lien avec la thèse retenue.* C'est sa continuité directe : le même nul, un second instrument.
- *Chance.* 0,45.
- *Recherche.* Citants du papier fondateur filtrés sur « taux d'audit » et « dommage planté ».
- *Une issue négative laisse* les constantes.

**Zone 6 — Plancher optimal contre un score manipulé.** [HYPOTHÈSE]
- *Statut.* Comme théorème, probablement occupé (bandits adverses, jeux d'audit ; Hua et collaborateurs, 2025, « Combining cost-constrained runtime monitors for AI safety », mémoire incertaine).
- *Chance.* 0,15 comme théorème ; 0,45 comme table mesurée.
- *Contrainte.* N-077 interdit de revendiquer contre la meilleure réponse : la mesure reste descriptive.

**Zone 7 — Le tirage comme preuve pour un tiers.** [HYPOTHÈSE]
- *Idée.* Engagement, graine publique, audit rejouable par un régulateur.
- *Statut.* La méthode existe en audit électoral ; son application au contrôle est non cherchée.
- *Enjeu.* Gouvernance ; rattachée à l'« attestation en service ».
- *Chance.* 0,5.
- *Recherche.* Citants de Lindeman et Stark en gouvernance de l'intelligence artificielle.

### (d) Ce qui n'est pas inoccupé, quoi qu'on trouve

[PROPOSITION]
- L'estimateur à probabilités inégales, le plancher et la variable de contrôle : manuel de sondage.
- Le tirage orienté par un modèle avec mélange uniforme : inférence statistique active.
- L'engagement avant tirage : audits à risque limité.
- L'idée que le hasard du contrôleur dissuade : jeux d'inspection, que Griffin et collaborateurs rapprochent déjà du contrôle (note, p. 10).
- L'asymétrie « le défenseur a un vrai hasard, l'agent sans mémoire doit fabriquer le sien » : Mallen et collaborateurs 2024.

### (e) Classement et prévisions

| Zone | Effet sur | Chance | Rang |
|---|---|---|---|
| 5. Bilan mesuré de l'audit | Détection ; socle du papier A | 0,45 | 1, à faire de toute façon |
| 2. Sonde après gel | Détection, accès interne | 0,35 | 2 |
| 1. Mise en aveugle | Dommage lui-même | 0,4 | 3, suspendue à « Blindfold » |
| 3. Étanchéité de la boucle | Validité de tout le reste | 0,4 | 4, test peu coûteux |
| 4, 6, 7 | Unité, plancher, tiers | 0,15 à 0,5 | Sections, non thèses |

Prévisions à sceller [HYPOTHÈSE ; chances en jugement] :
- Avec une référence par tâche, l'intervalle à 95 % couvre le dommage nul dans 90 à 97 % des répliques honnêtes (0,6).
- La corrélation ρ entre sonde et mesure d'audit, sur exécutions honnêtes, reste sous 0,5, soit un gain inférieur à 13 % (0,6).
- La sonde de fuite prédit le tirage mieux que le hasard dès que la correction est visible par l'agent (0,65).

### (f) Phrases à ne pas écrire

[PROPOSITION]
1. « Inoccupé », pour toute zone, avant la recherche par fonction.
2. « Le tirage secret est le seul appui indépendant de l'attaque », sans les trois conditions.
3. « Le moniteur en variable de contrôle » présenté comme un apport : c'est du sondage assisté par modèle.
4. « L'audit au hasard du papier fondateur », sans page.
5. « Quatre modèles convergent » comme argument de validité ou de nouveauté.
6. « L'audit au hasard échappe à la loi de la référence » : il en hérite le terme en N²/m.
7. Tout énoncé sur « Blindfold » avant lecture.

---

## Question neutre pour le collisionneur

« Une organisation confie de longues tâches d'analyse à un système automatisé dont elle ne peut pas garantir la loyauté. Elle dispose d'une source de hasard que ce système ne peut ni prévoir ni observer. Recensez tous les usages distincts qu'un contrôleur peut faire d'un tel hasard face à un contrôlé stratégique, dans tous les domaines où ce problème se pose. Pour chaque usage : ce qu'il garantit exactement, sous quelles conditions, quels travaux l'établissent, et s'il a déjà été appliqué à des agents fondés sur des modèles de langue. Dites lesquels vous jugez les moins étudiés pour ces agents, et quelle recherche bibliographique ou quelle expérience vous donnerait tort. »

---

## Décisions qui reviennent au directeur

**Décision 1 — Lancer la recherche d'antériorité sur le tirage avant toute phrase de nouveauté.**
- *Enjeu.* Aucune recherche sur le tirage n'existe dans les pièces ; « Blindfold » peut fermer la zone 1.
- *Option a : lecture ciblée (« Blindfold », pages de protocole du papier fondateur, Wen p. 18) et une douzaine de requêtes sur les zones 1, 2, 3 et 5.* Avantage : quelques jours ; statuts sûrs pour les zones qui comptent. Inconvénient : les zones 4, 6 et 7 restent non cherchées.
- *Option b : recherche complète par fonction, arbres de citations compris.* Avantage : table complète. Inconvénient : délai ; quotas déjà épuisés sur quatre arbres.
- *Option c : aucune recherche, rien revendiqué.* Avantage : aucun coût. Inconvénient : on peut refaire sans le citer ce que « Blindfold » fait.
- *Recommandation.* Option a. Confiance : 0,75.

**Décision 2 — Fixer la place de l'audit au hasard dans le papier A.**
- *Enjeu.* Le bilan mesuré a maintenant deux instruments de même forme nulle.
- *Option a : l'audit au hasard comme instrument de référence et base, bilan mesuré à côté de celui des moniteurs, rien revendiqué.* Avantage : cohérent avec N-075 et la thèse retenue ; l'essai « jumeau contre jumeau » sert les deux. Inconvénient : alourdit le papier.
- *Option b : papier séparé sur le hasard du défenseur.* Avantage : place pour les zones 1 à 3. Inconvénient : antériorité non cherchée ; cinquième papier.
- *Option c : statu quo, plancher publié sans mesure.* Avantage : aucun travail. Inconvénient : la couverture reste supposée.
- *Recommandation.* Option a. Confiance : 0,6.

**Décision 3 — Choisir la zone candidate à instruire en premier.**
- *Enjeu.* Une seule zone peut recevoir une expérience dans le délai.
- *Option a : sonde tirée après gel (zone 2).* Avantage : propre à l'accès interne ; faisable sur les organismes existants. Inconvénient : voisin direct non lu.
- *Option b : mise en aveugle (zone 1).* Avantage : agit sur le dommage. Inconvénient : suspendue à « Blindfold » ; demande un nouveau banc.
- *Option c : étanchéité de la boucle (zone 3).* Avantage : test peu coûteux, qui conditionne les autres. Inconvénient : apport peut-être hérité.
- *Recommandation.* Option c comme vérification immédiate, puis option a ; option b soumise au collisionneur après lecture. Confiance : 0,5.

**Décision 4 — Fixer l'unité de tirage et la mesure d'audit de l'essai « jumeau contre jumeau ».**
- *Enjeu.* Sans mesure valide sur l'unité tirée, le plancher ne garantit rien contre le diffus.
- *Option a : l'action.* Avantage : simple, nombreuses unités. Inconvénient : le dommage diffus n'y est pas mesurable.
- *Option b : le sous-résultat, avec ré-exécution indépendante et dommages plantés.* Avantage : mesure l'issue, conforme à N-075. Inconvénient : coût ; borné par le surplus de capacité.
- *Option c : la tâche entière.* Avantage : dommage bien défini. Inconvénient : peu d'unités, intervalle large.
- *Recommandation.* Option b, avec l'option a rapportée en base. Confiance : 0,55.

FIN DE LA RÉPONSE
