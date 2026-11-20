# Rapport du rédacteur — préenregistrement du palier 0b de l'épreuve sur l'héritage (étage sur processeur), version 7 : écarts de conception révélés par le code, et erratum du commit — v1

- Auteur : rédacteur neuf, modèle F. Pièce de travail (classe C). Travail du 2026-11-20, de 04:08Z à 04:20Z environ (`date -u`) ; la version 7 a été produite par l'outil vers 04:15Z (heure exacte au journal de l'outil).
- Mandat : `docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/mandat-redacteur-palier-0b-v7-erratum-du-commit-v1.md` (`9f948bb1718214d81304c77144f9d10b041663b2991b50f7410e7c70cb19b0af`), vérifié par son compagnon avant tout geste.
- Sur processeur seul : aucun tirage, aucun étalonnage, aucun audit, aucun lancement du code de l'étage ; aucun appel à un fournisseur de modèles, aucune dépense, aucun réseau ; aucune écriture dans le dépôt, aucun commit. **Aucun refus de permission, de classifieur ni de garde.** Rien de lu sous `archives-reponses-modeles/` ni sous `/root/.claude/`. Aucun code en ligne passé à un interpréteur ; un seul programme lancé, par son chemin : l'outil de remplacement (Python 3.13.18).

## 1. Verdict

La version 7 est écrite, par 30 remplacements exacts appliqués au premier appel, sans refus ni avertissement de l'outil. Elle n'est **ni contre-lue ni scellable en l'état** : deux de ses règles sont des nœuds de Lazar, elle demande un code v4, et le commit qu'elle inscrit (code v3) ne vaut qu'après lui.

## 2. Fichiers rendus

Dossier : `/tmp/claude-0/-home-user-controle-ia-travail/227b647d-2ece-5654-bf04-8493b3ed2f19/scratchpad/redacteur-palier-0b-v7/`. Chaque fichier a son compagnon `.sha256`.

| fichier | empreinte SHA-256 |
|---|---|
| `preenregistrement-heritage-palier-0b-etage-processeur-v7.md` (228 894 octets, 871 lignes) | `2f0f928f291b65a98bff2680e6bb7172bcf279da7e76b16bd837193f0704f4f0` |
| `remplacements-preenregistrement-palier-0b-v6-v7.json` (30 remplacements) | `a20a925fbd3022686d74c92467483da2a48b7fb5d74c393f3711e738b6a735a9` |
| `preenregistrement-heritage-palier-0b-etage-processeur-v7.md.journal-remplacements-v1.json` (journal de l'outil) | `e137dc922d8cd9f74ea70f7a4f3aaeba32baf8c80c91682eb63457294fc4070e` |
| `differentiel-preenregistrement-palier-0b-v6-v7.diff` (`diff -u` ; 12 lignes de la version 6 changées, 187 lignes côté version 7) | `4dc998f4eab95b0e9e2ca8bb7e6e6d3c1594f6b33be6293bcab984872d4a7d07` |
| `table-empreintes-code-v3-extraite-du-rapport-v1.txt` (les 51 lignes de la table du rapport du code v3, lignes 605 à 655, extraites à l'octet) | `91e8e96e76646f834d470ffa0c5863ed3f67bc42a79b1912e3f23c50f9522529` |
| `rapport-redacteur-palier-0b-v7-v1.md` (ce rapport) | dans son compagnon |

Fichier de travail, non rendu comme pièce : `audit-au-commit-3d332d2c.py` (le module `audit.py` tel qu'au commit, sorti par `git show` vers ce dossier, pour une seule comparaison d'empreinte).

La version 6 est intacte (compagnon revérifié après l'opération).

## 3. Sources, avec chemin et empreinte

Dossier `docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/` ; chaque empreinte vérifiée par son compagnon et recalculée sur disque.

| pièce | empreinte |
|---|---|
| `preenregistrement-heritage-palier-0b-etage-processeur-v6.md` | `4aee136b44665339be343b26913fdec8a943a0de75368013bcc4a7dc608e5029` |
| `controle-differentiel-palier-0b-v6-v1.md` | `c079a89d0baefda6dde6bfa401c943b68056279d43960e1b62d34cdebc6dcaea` |
| `rapport-redacteur-palier-0b-v6-v1.md` | `5ad452ab33d24f9d53b3b0736e9442fc6b4a88288f9aab74ff1b0fecdddedcae` |
| `code-v2/rapport-developpeur-code-palier-0b-v2.md` | `ca61bf7e89aefe7ffe9e7a62e80ff7da1653668542f8fbd8498909a10e409b75` |
| `code-v2/contre-lecture-v1/contre-lecture-code-palier-0b-v2-v1.md` | `3778fb395dae1e2003ce8236f93c77cfbd6bc78c355417bf0b40e0b5e694c5e5` |
| `code-v2/contre-lecture-v1/outils-cl/bruit_nul_doses.py` (non lu, non lancé) | `a765ed8bd7e97ae3e1710bf30d4a1f08c420fde55663a0a93d6392210da6b0c7` |
| `code-v3/rapport-developpeur-code-palier-0b-v3.md` | `5e3fa3e8026ca6d9e2a1d027940df27753295fdd6a2c6478a9a04b516889b548` |
| `code-v3/verification-v1/verification-corrections-code-palier-0b-v3-v1.md` | `c5c211c774f3ef78773df7aba6ba48efd1a4b252ab185fd789d623a16507d604` |
| `scripts/remplacer_texte_exact_v1.py` (racine du dépôt) | `391db990734dd36f7c827b8b6c77dc0de1bda324f671b65748ccfe68c56a53d6` |

Code v3 lu, sans le lancer (`code-v3/src/controle_ia/heritage_etage_processeur_v1/`) : `audit.py` (`11352fcd…`) et `graines.py` (`cf433337…`) en entier ; `constantes.py` (`37e848c2…`), `etalonnage.py` et `tirages.py` par recherche de mots. Commit : `3d332d2c` se résout en `3d332d2c6be171a2c73b4aa14472d309ede87553` ; `audit.py` à ce commit a l'empreinte de la table.

## 4. Les trois remplacements de tenue

Appliqués à la lettre du § 3 du contrôle du différentiel : ligne du commit du code, étape 1 de l'ordre des opérations, section « Contre-lecture ». Une ligne les inscrit à l'annexe G.

## 5. Les trois écarts : règle retenue, et pourquoi

1. **Marge face à la source étrangère à la dose 0,5 (B7 bis).** Règle : le jeu de sources de la garde 27 est joué à la dose 0,25 ; la marge n'est ni construite ni revendiquée à 0,5 sur la couche mécanique ; la réserve 20 est corrigée. C'est la recommandation (a) de la contre-lecture du code. Raison : la garde 27 contrôle quel registre est servi à quel bras, la dose n'y est pas en cause ; restreindre la marge la laisserait tenue à moitié ; élargir les bornes a un coût non borné. La règle retire une revendication, sur un bras sans critère.
2. **Longueur du texte parmi les traits de forme.** Règle : la longueur de forme est celle du texte où chaque nombre d'au moins quatre décimales, signe et exposant compris, est remplacé par son jeton. **Mon complément** : la longueur brute passe aux traits de contenu. Raison du complément : les trois traits de contenu de la version 6 ne lisent pas le signe ; sans lui, le signal sortirait de l'audit, alors que la contre-lecture le disait « déjà lu par les traits de contenu ».
3. **Bruit de l'audit des doses par paires.** Règle calibrée : arrêt si l'exactitude de forme dépasse 0,55 + 2 σ₀, σ₀ étant l'écart-type sous 1 000 permutations des étiquettes (entre lois, ou entre suites pour les audits par dose) ; entre 0,55 et ce seuil, pas d'arrêt, mais l'exactitude lie l'étage payant ; au plus 0,55, tenue. Appliquée aux cinq exactitudes de forme. Raison du choix : un intervalle sur de nombreux plis ne mesure que le hasard des plis, non celui de l'échantillon ; davantage de suites change la valeur de 50 pour un coût non mesuré ; la permutation mesure le bruit sur les données mêmes, avec leur dépendance.

**Ce que je savais en écrivant les règles 2 et 3** (réserve 22 du texte) : à la lettre de la version 6, l'étape 3 s'arrêterait probablement ; les deux règles rendent cet arrêt moins probable. Le seuil de 0,55 reste, le signal de la longueur reste lu, et la zone médiane lie l'étage payant. Aucun résultat décisif n'existe. La règle 3 voit mal un petit défaut des mondes par dose (réserve 23) : une exactitude vraie de 0,60 n'y arrête qu'une fois sur trois environ — calcul à la main, à refaire par le contre-lecteur.

## 6. Silences, écarts nommés, notes

- **Dix silences inscrits comme règles** (annexe H, table) : choix 1, 2, 4, 5, 6, 7, 8, 10, 13, 14. Les choix 3 et 9 ne sont pas des silences ; c'est dit.
- **Choix 11, écart nommé** : le texte suit le code — le lecteur aux deux réglages ensemble est tiré à la seule taille 1 et au seul taux de 0,25. Exception dite à « le code suit ce texte » : ce proposeur est sans critère.
- **Choix 12, écart nommé** : la liste entière des étiquettes est écrite dans un fichier scellé à côté du manifeste. Le code v3 ne l'écrit pas.
- **D5** : laissée, motivée (aucun résultat n'en dépend ; l'essai de forme relève la mémoire).
- **D6** : règle — le verrou exige le compagnon du texte, l'empreinte inscrite par la mère au fichier d'autorisation, et l'accord des modules lancés avec la table du texte. **Trouvé en lisant** : `constantes.py` porte l'empreinte de la version 6 ; elle est périmée dès qu'un autre texte est scellé, et une empreinte du texte dans le code tourne en rond.
- **D8** : règle — une taille non finie arrête l'étalonnage.
- **D9** : règle — plis non stratifiés gardés ; un pli privé d'une classe arrête l'audit.

## 7. Ce qui demande un code v4

1. `audit.py` et l'étape 3 : longueur de forme, longueur brute au contenu, permutations, trois lectures, arrêt sur un pli privé d'une classe ; essais et défauts au banc. **Après les mots de Lazar sur les nœuds 1 et 2.**
2. `graines.py`, `constantes.py` : le verrou (D6).
3. `etalonnage.py` : D8.
4. `tirages.py` : la liste des étiquettes (choix 12).
5. À vérifier, à corriger seulement si le code s'en écarte : la dose du jeu de la garde 27 à l'étape 4 ; l'ordre des bras pour l'origine d'une loi (choix 8).

**Le commit inscrit (`3d332d2c`) ne vaut donc qu'après un code v4, et l'erratum du commit se refait.**

## 8. Nœuds pour Lazar

**Nœud 1 — la longueur du texte dans l'audit de présentation.**
- Décision : mesurer la longueur de forme sur le texte où chaque nombre est remplacé par son jeton, la longueur brute passant aux traits de contenu.
- Enjeu : à la lettre de la version 6, l'audit s'arrêterait probablement à l'étape 3, sur un signal qui vient du signe des poids.
- Option (a), la règle de la version 7 — avantage : la forme ne lit plus le contenu, le signal reste lu et lie l'étage payant ; inconvénient : écrite après un diagnostic.
- Option (b), la lettre de la version 6 — avantage : rien ne change après un diagnostic ; inconvénient : arrêt probable, puis un erratum de toute façon.
- Option (c), le même filtre pour toutes les sous-lois — avantage : traite la cause ; inconvénient : change le générateur gelé, code lourd, jamais éprouvé.
- Recommandation : (a) ; confiance moyenne à haute.
- Défaut : aucun (la règle change ce que lit un seuil d'arrêt).

**Nœud 2 — la règle calibrée de l'audit de présentation.**
- Décision : n'arrêter l'audit qu'au-dessus de 0,55 + 2 σ₀, une exactitude entre 0,55 et ce seuil liant l'étage payant sans arrêter.
- Enjeu : à la lettre, un générateur parfait arrête l'étape 3 de 11 à 14 fois sur cent.
- Option (a), la règle de la version 7 — avantage : un arrêt vaut preuve ; inconvénient : le seuil d'arrêt monte vers 0,61 pour les mondes par dose, et un petit défaut y est mal vu.
- Option (b), la lettre de la version 6 — avantage : aucun seuil ne bouge ; inconvénient : l'alarme à tort.
- Option (c), la lettre sur 100 suites par dose — avantage : le seuil reste, l'alarme à tort tombe à 1,1 % par paire ; inconvénient : la valeur de 50 change, coût non mesuré.
- Recommandation : (a) ; confiance moyenne. (a) et (c) peuvent se joindre.
- Défaut : aucun (la règle change ce qui vaut dépassement d'un seuil).

**Proposition avec recommandation — la dose du jeu de la garde 27.**
- Décision : jouer ce jeu à la dose 0,25 et ne plus revendiquer la marge face à la source étrangère à 0,5 sur la couche mécanique.
- Enjeu : à 0,5 la construction épuise ses bornes, et l'étage s'arrêterait sur un bras sans critère.
- Option (a), la règle de la version 7 — avantage : la garde est jouée, sans coût ; inconvénient : une seule dose en lois réelles.
- Option (b), marge restreinte — avantage : deux doses ; inconvénient : marge tenue à moitié.
- Option (c), bornes élargies — avantage : la lettre est gardée ; inconvénient : coût non borné.
- Recommandation : (a) ; confiance haute.
- Défaut sous 48 heures : (a). Aucune valeur gelée n'est en cause : le texte ne disait pas cette dose.

**Pour information** : le choix 11 ; trois causes d'arrêt de plus (étalonnage, audit) ; artefacts ajoutés aux gardes 25 et 27 ; le commit inscrit ne vaut qu'après un code v4.

## 9. Écarts et points à relire

1. **J'ai classé l'écart 1 en proposition avec défaut, non en nœud.** Le texte ne disait pas la dose du jeu ; la valeur de 0,25 nat ne bouge pas. Si la mère y voit un changement de seuil, c'est un troisième nœud, sans défaut.
2. **J'ai classé les causes d'arrêt ajoutées (D8, D9, choix 6) et le choix 11 en information**, comme les versions 4 et 5 l'ont fait pour leurs causes d'arrêt. À confirmer.
3. **Les règles vivent en partie à l'annexe H.** Sept silences n'ont pas de phrase dans leur section ; une phrase de l'en-tête dit que l'annexe fait foi. La version 4 les avait écrits dans le corps.
4. **« Cette version 6 » reste écrit deux fois**, dans les mots du contrôle appliqués à la lettre ; l'alinéa de tenue de l'annexe G le dit. Cet alinéa est placé avant celui de la version 6, pour que « annexe G, dernier alinéa » reste juste.
5. **L'heure écrite dans la version 7** (« de 04:08Z à 04:40Z environ ») a été écrite avant la fin ; l'outil a écrit vers 04:15Z.
6. **La branche du commit** est citée d'après le mandat ; je ne l'ai pas vérifiée. Trois empreintes de la table sur 51 recalculées ; un fichier relu au commit. Les 51 lignes de la table figurent dans la version 7 (compte par `grep -c -F -f` : 51).
7. **Règles des silences non vérifiées une à une dans le code** : elles reprennent les mots du développeur et du contre-lecteur du code. L'ordre des bras du choix 8 est à confirmer.
8. **La table du bloc de code de l'en-tête** est indentée de deux espaces sous sa puce ; la suite de la ligne (« Histoire, reprise de la version 6 ») garde les phrases de la version 6.
9. **Non faits** : le validateur du gabarit ; la recherche des listes « Ne pas écrire » par programme. Mes ajouts ne citent aucun travail publié et ne portent aucun identifiant de modèle.
10. **Aucun incident d'outil** : les 30 ancres ont été comptées une fois chacune avant l'appel (`grep -c -F -e`), et l'outil a tout appliqué au premier essai.

## 10. Reste à faire, hors de mon mandat

Verser les fichiers ; contre-lecture de la version 7 par un sous-agent neuf (règle R2) ; mots de Lazar sur les deux nœuds et sur la proposition ; code v4 et sa vérification ; erratum du commit refait ; scellement par la mère.

*Rédacteur neuf, modèle F.*
