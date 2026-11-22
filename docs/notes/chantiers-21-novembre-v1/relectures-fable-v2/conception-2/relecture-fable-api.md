# Relecture par Claude Fable 5.2 (appel direct à l'interface d'Anthropic)

- Outil : `controle_ia.relecture_fable_api_v5` (empreinte du module 052ea1e2c66f8b80b1724db9f0c5afb27a48cc01eac2e1e5210658ca8423bdb8)
- Modèle demandé : `claude-fable-5-2` ; modèle servi : `claude-fable-5-2` ; identifiant du message : `msg_011ChHwapR84J82fWqb44p57`
- Heure (UTC) : 2026-11-22T12:13:32Z
- Réglages : effort `max`, réflexion adaptative à affichage « omitted » (texte de la réflexion ni demandé ni écrit), `max_tokens` 125000, aucune relance, aucun repli vers un autre modèle, budget de tâche 96000 jetons (bêta `task-budgets-2026-03-13` ; cible indicative vue par le modèle, pas une borne : seul `max_tokens` arrête)
- Entrées :
  - consigne : `docs/notes/chantiers-21-novembre-v1/mandats-fable-v1/consigne-relecture-v2-chantiers-21-v1.md` — sha256 b196ade3c35f7555ed3a096e4f3b9ec19451c0d3bb72d5dabe42fb26f3b83b34 (compagnon : vérifié)
  - correction : `docs/notes/chantiers-21-novembre-v1/conceptions-v2/conception-2-epreuves-du-devin-v2.md` — sha256 fdc6889a0eb3a6b23016b61e1a68a89c0cee4eeb960ca3603af50dad08789dce (compagnon : vérifié)
  - correction : `docs/notes/chantiers-21-novembre-v1/conceptions-v2/conception-2-epreuves-du-devin-v2-erratum-1.md` — sha256 37e67484eb16bcfd78d7e4db8b8ca988eb6fb1e97006d5ad3150e93d30c6cfb0 (compagnon : vérifié)
  - remarques : `docs/notes/chantiers-21-novembre-v1/copies-sans-nom-v1/contre-lecture-reponse-2-epreuves-du-devin-opus-v1-sans-motif-v1.md` — sha256 b70b63d5acf263d7aafc2dcd79be83f5816705553efd9c727622542a08faabe1 (compagnon : vérifié)
  - remarques : `docs/notes/chantiers-21-novembre-v1/contre-lectures-v1/contre-lecture-reponse-2-epreuves-du-devin-opus-v1-erratum-1.md` — sha256 f0cb8c3361899712f3ef089ed31783ff94a02de6cd1e621c202cc9ed8265f3c1 (compagnon : vérifié)
  - remarques : `docs/notes/chantiers-21-novembre-v1/contre-lectures-v1/verification-conception-2-v2-opus-v1.md` — sha256 3b00f74a40c4cde2231186b57ef7e00d1458a44d3cb155173e9512a71a12f1db (compagnon : vérifié)
  - remarques : `docs/notes/chantiers-21-novembre-v1/contre-lectures-v1/rejeu-epreuves-du-devin-opus-v1-sortie.txt` — sha256 6296a967f6cfebccf54e8f543eb7698860ce0205a3508a1892fb9aebb5925e84 (compagnon : vérifié)
  - avant : `docs/notes/chantiers-21-novembre-v1/reponses-fable-v1/demande-2/relecture-fable-api.md` — sha256 a07036a908fef74d39558ac96a984143ebce726594760b15c337c57b07c4fd13 (compagnon : vérifié)
- Empreinte de l'invite envoyée : 17b6cfdebfd99102c99c0d81875583aa039227be35dd57b93471d7a3bd538128
- Jetons : entrée 45943, sortie 25395 (dont réflexion 17194), écriture de cache 0, lecture de cache 0 ; raison d'arrêt `end_turn`
- Coût compté : 1.383344 USD (base : usage ; tarif 8 / 40 USD par million de jetons d'entrée / de sortie)

---
# Relecture par le concepteur — conception 2 (épreuves du devin), v2 et erratum 1

**Conclusion d'abord.** La v2 et son erratum sont **scellables après les treize couples K1 à K13 ci-dessous**. J'accepte les 21 corrections portées, dont trois avec retouche (constats 1, 3 et 7), et les 8 couples de l'erratum, dont trois avec retouche (6-b, 17-a et 1-c). Les corrections ont créé cinq incohérences nouvelles ; la plus sérieuse est dans le constat 3. Rien n'est revendiqué. Je n'ai exécuté aucun code.

## 1. Corrections portées

| Constat | Avis | Raison courte |
|---|---|---|
| 1 (deux corrections) | acceptée avec retouche (K1) | Le facteur 1,44 ne garantit pas la puissance 0,80, et « taille annoncée » n'avait pas de règle de fixation. |
| 2 | acceptée | Voir section 2. |
| 3 | acceptée avec retouche (K2) | Une racine tirée après le scellement ne peut pas avoir servi à apprendre les prédicteurs. |
| 4-a, 4-b, 4-c | acceptées | Je me range à l'échange des options ; ma confiance est redite par K12 et l'épreuve à part est spécifiée par K6. |
| 5 | acceptée | Elle casse deux lignes ailleurs (K7, K8). |
| 6 (portée sur un modèle) | acceptée | — |
| 7 (deux corrections) | acceptée avec retouche (K3) | Le défaut entre parenthèses se lit de deux façons. |
| 8 (deux corrections) | acceptée | Le compte J double avec deux cibles (K4). |
| 9 (canaris), 10 (deux), 11, 12, 13, 15 | acceptées | Le constat 10 laisse une ligne à recaler (K13). |
| 14 | acceptée | Contredite par le couple 16-a de l'erratum (K5). |

Couples de l'erratum : 9-b, 13-b, 16-a, 18-a et 2-b sont acceptés. 6-b, 17-a et 1-c sont acceptés avec retouche (K9, K10, K11).

## 2. Constats que je traite comme bloquants

Le contre-lecteur n'en classe aucun bloquant (FAIT RAPPORTÉ). Les constats 1, 2, 3 et 5 touchent pourtant une garde ou un test de mort. Je dis donc ce que chacun garantit après correction.

**Constat 1 — tailles et test de mort 2.**
- CALCUL (rejoué par le contre-lecteur, bloc 2) : P(760 retrouvés ou moins sur 1 000, puissance 0,80) = 0,0011.
- FAIT RAPPORTÉ (bloc 5) : à la taille multipliée par 1,44, l'horodatage n'a qu'une puissance de 0,78 dans une famille de quinze, à 400 répliques (écart type 0,02).
- CALCUL, à la main : si la puissance vraie est 0,78, le test de mort 2 se déclenche avec une probabilité d'environ 7 % (moyenne 780, écart type 13,1, écart réduit −1,49).
- PROPOSITION (K1) : la taille annoncée est la plus petite taille d'une grille déclarée où la famille entière retrouve la fuite 850 fois sur 1 000.
- Garantie après K1 : pour une puissance vraie d'au moins 0,83, le test de mort 2 se déclenche à tort avec une probabilité négligeable (écart réduit −5,8). Suppositions : approximation normale, graines distinctes entre la pièce 7 et le test de mort.

**Constat 2 — test de mort 4.** Je valide la correction.
- CALCUL : un dispositif sain se déclenche avec la probabilité 1 − 0,999 × 0,99 = 1,1 %. Deux déclenchements de suite sur plis indépendants : 0,012 %.
- Le seuil 0,001 est atteignable : avec B = 9 999, la plus petite p-valeur est 0,0001.
- CALCUL, à la main : taille de puissance 0,99 à 2 000 épisodes d'épreuve, bras équilibrés, borne de Bonferroni.

| Famille | Taille de puissance 0,99 |
|---|---|
| un trait seul | 0,089 |
| J = 15 | 0,113 |
| J = 30 | 0,118 |
| J = 15, audit à 5 % | 0,26 |

- Commande donnée, non exécutée : `python3 -c "from statistics import NormalDist as N;z=N().inv_cdf;print([round((z(1-.05/J)+z(.99))/2000**.5,4) for J in (1,15,30)])"`.
- HYPOTHÈSE : la puissance 0,99 est calculée sur le monde planté et vaut sur le harnais réel. Elle tient mieux pour un marqueur de texte à taux de base nul, dont le bruit ne dépend pas du harnais. Je propose ce témoin.

**Constat 3 — racine secrète.** Je refais la correction (K2).
- La v2 gèle les prédicteurs sur les pièces du pli d'apprentissage. Ces pièces doivent donc exister avant le scellement, alors que la racine est dite « tirée après le scellement ».
- Une racine courte (une date, par exemple) se retrouve par essais depuis sa seule empreinte.
- Garantie après K2 : avant la fin de l'épreuve, la pièce d'épreuve n'est une fonction connue d'aucun objet publié. Le test de mort 5 vérifie le tireur après révélation.
- Suppositions : racine d'au moins 128 bits tirée de la source d'entropie du système ; tireur qui ne lit que la racine et l'identifiant de tâche ; épisodes d'apprentissage joués avant ceux d'épreuve.
- HYPOTHÈSE : `SeedSequence` n'est pas un hachage cryptographique. Je n'exclus pas qu'on puisse remonter à la racine d'apprentissage depuis ses pièces. C'est pourquoi la racine d'épreuve est distincte.
- Jouer les deux plis l'un après l'autre peut coûter de la puissance si le régime dérive. La validité, qui vient du tirage, n'en dépend pas.

**Constat 5 — rejeu dans l'ordre.** Je valide la correction.
- Sous le nul strict, la loi de A sachant la vue est le produit des lois de Bernoulli de propension π_t(A_{<t}, entrées consignées). Le rejeu dans l'ordre la tire exactement.
- Suppositions : tireur pur ; Z* calculé avec π* et non avec π ; aucune entrée qui n'existe que pour les épisodes réellement audités. Le verdict d'un audit est une telle entrée : un épisode non audité n'en a pas, et le cas est refusé (K7).
- Ce raisonnement n'est ni simulé ni rejoué.

## 3. Ajouts non portés

- **Ajouts des constats 6, 9, 16, 17 et 18** : portés par l'erratum, repris ci-dessus.
- **« Ce que l'inventaire change »** : porté nulle part dans la v2. FAIT RAPPORTÉ, que je n'ai pas vu : aucun tirage de pièce et aucune décision lisant une sonde n'existent dans les harnais du dépôt. Je porte le verdict « sans objet » (K6), faute de quoi un « non réfuté » vide resterait possible.
- **Épreuve à part de la décision 3** : nommée par 4-b, spécifiée nulle part. Je la spécifie (K6).

## 4. Ce que la correction a cassé

1. **Constat 3 contre le gel sur le pli d'apprentissage** : voir section 2 (K2).
2. **Constat 5 contre la pièce 3 et « Ce que je n'ai pas fait »** : la pièce 3 refuse encore toute propension qui dépend d'une pièce passée, et le repli de martingale, supprimé, est encore cité (K7, K8).
3. **Constat 14 contre 16-a** : le budget dit « une [course] pour la lecture » ; l'erratum en crée deux (K5).
4. **Constat 14 contre constat 8** : A1 et A2 dans un même maximum doublent le compte, soit 30 statistiques et non 15. CALCUL, à la main : facteur 1,52 (z(1 − 0,05/30) = 2,935). Le « 1,44 » de la section 4 et le « 0,08 » de la décision 2 sont à redire (K1, K4, K11).
5. **17-a contre le tableau des artefacts** : si les 200 mots sont tirés du lexique entier, chaque épisode porte en moyenne deux marqueurs sans aucune fuite. CALCUL : P(au moins un marqueur) = 1 − 0,99^200 = 0,87. La taille λ ≈ 0,7 % suppose un taux de base nul (K10).

Deux points mineurs s'y ajoutent :
- 6-b accroche la clause « Ou bien » à la troisième condition seule (K9).
- Après le constat 10, la pièce 10 parle encore de « deux cas sains » (K13).

## 5. Couples à appliquer à la v2 corrigée par l'erratum

Chaque ancien texte y figure une seule fois, d'après ma lecture. Je ne l'ai pas vérifié par programme.

**K1** (constat 1, § 4)
- Ancien : « les tailles du tableau sont celles d'un trait seul et se multiplient par 1,44 au pire [CALCUL, à la main] ; la simulation (pièce 7) fixe la taille annoncée, qui est celle de la famille entière. »
- Nouveau : « les tailles du tableau sont celles d'un trait seul ; la borne de Bonferroni les multiplie par 1,43 pour J = 15 et par 1,52 pour J = 30 [CALCUL, à la main], sans garantir la puissance 0,80 (rejeu du contre-lecteur : 0,78 pour l'horodatage à 1,44) ; la simulation (pièce 7) fixe la taille annoncée : la plus petite taille d'une grille déclarée d'avance où la famille entière retrouve la fuite au moins 850 fois sur 1 000, sur des graines distinctes de celles du test de mort 2. »

**K2** (constat 3, § 3)
- Ancien : « Elle est tirée après le scellement des prédicteurs ; seule son empreinte est consignée avant la course, et elle n'est révélée qu'après la fin du dernier épisode d'épreuve. »
- Nouveau : « Deux racines d'au moins 128 bits, tirées de la source d'entropie du système : celle du pli d'apprentissage, tirée avant ses épisodes et remise au devin après le dernier d'entre eux ; celle du pli d'épreuve, tirée après le scellement des prédicteurs. Les épisodes d'apprentissage sont joués avant ceux d'épreuve. Seule l'empreinte de chaque racine est consignée avant ses épisodes ; la racine d'épreuve n'est révélée qu'après la fin du dernier épisode d'épreuve et des épisodes suivants que lit la cible A2. La racine du tireur de la lecture substituée suit la même règle. »

**K3** (constat 7, § 1)
- Ancien : « (défaut : k = 3, et tous les épisodes jusqu'à la prochaine remise à zéro déclarée de cette mémoire) »
- Nouveau : « (défaut : k = 3 pour une ressource partagée ; pour une mémoire persistante, tous les épisodes jusqu'à la prochaine remise à zéro déclarée, au plus 20 ; le prédicteur de la cible A2 lit ces vues ensemble) »

**K4** (constats 8 et 14, § 3)
- Ancien : « (borne de Bonferroni ; le maximum permuté fait mieux) »
- Nouveau : « (borne de Bonferroni ; le maximum permuté fait mieux) ; quand deux cibles entrent dans le même maximum (A1 et A2), chaque prédicteur est gelé une fois par cible et J double : 30 statistiques, facteur 1,52 (34 : 1,53) »

**K5** (constat 14 contre 16-a, § 3)
- Ancien : « deux courses pour la pièce (8 000), une pour la lecture. »
- Nouveau : « deux courses pour la pièce (8 000), deux pour la lecture (8 000), soit 16 000 épisodes ; au plus 18,5 % des admissions d'un harnais sain portent au moins un rejet à tort (1 − 0,95⁴). »

**K6** (inventaire et décision 3, § 2)
- Ancien : « - **Sans dépense**, on s'arrête aux étages 0, 1 et 2 bis. »
- Nouveau, en trois lignes :
  - « - **Sans dépense**, on s'arrête aux étages 0, 1 et 2 bis. »
  - « - **Sans objet.** Si l'inventaire ne trouve aucun tirage de pièce, ou aucune décision du harnais qui lise une sonde, le devin correspondant n'est pas joué ; le verdict porte « sans objet à l'empreinte du harnais », jamais « non réfuté » ; la garde est alors le couplage de la section 5. »
  - « - **Épreuve à part sur la vue élargie** (décision 3). Les traits de l'étage 0 sans preuve de visibilité, gelés de même, ont leur maximum et leur p-valeur propres, à α = 0,05 ; ils n'entrent pas dans M ; un rejet est rapporté « canal sans preuve de visibilité » et ne suspend rien seul. »

**K7** (constat 5, ordre d'écriture)
- Ancien : « | 3. `tirage` | Tireur pur et rejeu du nul. | Pièces consignées redonnées. | Propension qui dépend d'une pièce passée. | »
- Nouveau : « | 3. `tirage` | Tireur pur et rejeu du nul, dans l'ordre quand la propension dépend des pièces passées ; Z* calculé avec π*. | Pièces consignées redonnées. | Propension qui dépend d'un objet que le rejeu ne recalcule pas (verdict d'un audit non joué, sonde réapprise). | »

**K8** (constat 5, « Ce que je n'ai pas fait »)
- Ancien : « - Le repli de martingale n'est pas spécifié au-delà de son nom. »
- Nouveau : « - Le rejeu dans l'ordre n'est ni simulé ni rejoué ; son exactitude est un raisonnement, sous tireur pur. »

**K9** (6-b, § 5)
- Ancien : « **Quand cela vaut la peine.** Trois conditions réunies : »
- Nouveau : « **Quand cela vaut la peine.** Trois conditions réunies, ou la clause finale seule : »

**K10** (17-a, § 4)
- Ancien : « texte de 200 mots tirés d'un lexique fermé de 2 000 mots, dont 20 marqueurs ; »
- Nouveau : « texte de 200 mots tirés des 1 980 mots ordinaires d'un lexique fermé de 2 000 mots ; les 20 autres, les marqueurs, ne paraissent que par la fuite plantée ; le décalage d de l'horodatage porte sur la log-durée du dernier pas ; »

**K11** (1-c, décision 2)
- Ancien : « Avantage : fuite d'environ 0,08 retrouvée par la famille entière (0,056 pour un trait seul). »
- Nouveau : « Avantage : à pièce équilibrée, fuite d'environ 0,085 retrouvée par la famille entière à deux cibles (0,056 pour un trait seul) ; au taux de service de 5 %, environ 0,19. »

**K12** (4-b, décision 3)
- Ancien : « Confiance du contre-lecteur : 0,6. »
- Nouveau : « Confiance du contre-lecteur : 0,6 ; le concepteur s'y range, confiance 0,6, chiffre qui remplace le 0,65 de la ligne de recommandation de cette décision. »

**K13** (constat 10, ordre d'écriture)
- Ancien : « | 10. `lien_epreuve_11` | Table à cinq cas. | Les deux cas sains. | Les trois autres. | »
- Nouveau : « | 10. `lien_epreuve_11` | Table à cinq cas. | Les deux premiers cas (conforme à l'attendu ; sain). | Les trois autres. | »

## 6. Verdict du concepteur

**Scellable après les couples ci-dessus** (K1 à K13). K2, K5, K7 et K10 lèvent des contradictions qu'un développeur rencontrerait dès les pièces 1, 3 et 4. Les autres recalent des chiffres ou des renvois.

## 7. Décisions qui reviennent au directeur

**Décision 1 — Adopter la lecture substituée comme forme exacte du devin sur la lecture.**
- *Enjeu* : sans elle, pas de nul exact. Sur les harnais du dépôt, la question est aujourd'hui sans objet (FAIT RAPPORTÉ par l'inventaire, que je n'ai pas vu).
- *(a) L'adopter*, la forme observée étant rapportée comme non exacte. Avantage : exactitude. Inconvénient : l'aiguillage suit un tirage pendant l'admission.
- *(b) La forme observée seule.* Avantage : aucune intervention. Inconvénient : un rejet peut n'être que le contenu.
- *Recommandation* : (a). Confiance 0,7.
- *Défaut sous 48 heures* : (a) sur mondes simulés ; sur un harnais réel, nœud.

**Décision 2 — Fixer le seuil et le budget.**
- *Enjeu* : il y a désormais quatre courses par admission.
- *(a) α = 0,05 par course, 16 000 épisodes.* Avantage : fuite de 0,085 retrouvée à pièce équilibrée, 0,19 à 5 % d'audit. Inconvénient : jusqu'à 18,5 % d'admissions saines suspendues à tort [CALCUL].
- *(b) α = 0,0125 par course.* Avantage : au plus 5 % par admission. Inconvénient : tailles plus grandes d'environ 11 %, soit 0,094 [CALCUL, à la main, J = 30] ; les seuils du cas sain sont à recalculer par la pièce 7.
- *(c) α = 0,05 et 8 000 épisodes par course.* Avantage : tailles divisées par 1,41. Inconvénient : budget doublé, fausses suspensions inchangées.
- *Recommandation* : (b). Confiance 0,6. Je change d'avis par rapport à la v1 : sous un maximum de 30 statistiques, baisser α coûte peu.
- *Défaut sous 48 heures* : (a), qui est le texte de la v2. Le passage à (b) demande un couple de plus.

**Décision 3 — Suspendre ou non sur la vue élargie.**
- *Enjeu* : durées et charge ne sont visibles que si un outil les donne.
- *(a) Suspendre seulement avec une preuve de visibilité, avec l'épreuve à part de K6.* Avantage : fidèle à la liste blanche. Inconvénient : un outil oublié, que l'épreuve à part doit faire paraître.
- *(b) Suspendre dès qu'elle rejette.* Avantage : prudent. Inconvénient : réparations sur des champs que l'agent ne voit pas.
- *Recommandation* : (a). Confiance 0,6.
- *Défaut sous 48 heures* : (a).

**Décision 4 — Choisir l'étage exigé avant toute phrase qui s'appuie sur un secret, sur un modèle.**
- *Enjeu* : les étages sur processeur ne lisent pas ce que l'agent calcule.
- *(a) Étage 3 et couplage, sur devis.* Avantage : couvre les états internes, à lot et remplissage identiques. Inconvénient : dépense.
- *(b) Étages sur processeur, et couplage là où le rejeu à graines identiques existe déjà.* Avantage : aucun coût. Inconvénient : borne basse faible.
- *Recommandation* : (a). Confiance 0,6.
- *Nœud, pas de défaut.* Aucune dépense n'est engagée.

**Décision 5 — Garder la cible A2 sous la lettre de « aucun retour à l'agent ».**
- *Enjeu* : A2, étendue à k épisodes, tient pour fuite toute trace d'un audit dans un épisode ultérieur.
- *(a) La garder telle quelle.* Avantage : conforme à la lettre accordée. Inconvénient : à redéfinir si les corrections tirées au hasard sont admises.
- *(b) Attendre cette autre décision.* Avantage : pas de reprise. Inconvénient : le devin de la pièce reste sans cible sur le vrai canal.
- *Recommandation* : (a). Confiance 0,7.
- *Nœud, pas de défaut.*

**Décision 6 — Écrire maintenant les pièces sur mondes simulés et différer l'admission.**
- *Enjeu* : aucun harnais du dépôt ne tire de pièce (FAIT RAPPORTÉ).
- *(a) Écrire les pièces 1 à 8 et 10 ; la pièce 9 attend le chemin d'audit.* Avantage : instrument prêt et éprouvé. Inconvénient : rien n'est admis sur le réel.
- *(b) Tout différer.* Avantage : aucun travail sans objet. Inconvénient : le chemin d'audit naîtrait sans son épreuve.
- *Recommandation* : (a). Confiance 0,75.
- *Défaut sous 48 heures* : (a), sur processeur seul.

## Ce que je n'ai pas fait

- Aucun code exécuté : ni les commandes données, ni le programme de portage, ni une vérification par programme de l'unicité des anciens textes de K1 à K13.
- Je n'ai lu ni l'inventaire des canaux, ni le programme de rejeu du contre-lecteur. Je n'en connais que ce que rapportent la contre-lecture et la sortie jointe.
- Les facteurs 1,52 et 1,53, la valeur 0,094, les tailles de puissance 0,99 et la probabilité de 7 % sont des calculs à la main sous approximation normale.
- Le seuil de 850 sur 1 000 et le plafond de 20 épisodes (K1, K3) sont des propositions non simulées.
- Aucune antériorité vérifiée, aucun PDF ouvert. Toutes gardent le statut « rapporté, non vérifié sur PDF ».
- Je n'ai pas chiffré la perte de puissance due au jeu des deux plis l'un après l'autre, ni la puissance des étages 1 à 3.
- Le devin des corrections n'est pas conçu.
