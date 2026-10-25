# Contre-lecture de la banque `confrontation-v3` (identifiants opaques, clé secrète, parts triées) — v1

Contre-lecteur neuf (R2, R4), 25 octobre 2026, 16:31–16:55 UTC. Je n'ai écrit ni la banque, ni ses scripts, ni le
LISEZMOI-v5, ni la première contre-lecture. Lecture seule des chemins donnés : dossier `banque/` (y compris les scripts
et sorties de la première contre-lecture) ; `taches.py`, `boucle.py`, `contrat.py`, `banque.py`, `confrontation.py` ;
plus deux lignes de `cli.py` (l. 260–261) et l'en-tête d'`archive.py` (effets d'import). Aucun git, aucun réseau,
aucun sous-agent, aucun fichier ni dossier interdit ouvert. Tout ce que j'ai écrit est sous
`/var/tmp/contre-lecture-banque-v3-v1/`. Interpréteur `python3 -I` (Python 3.13.17, numpy 2.5.3) ; `-B` quand le code
du dépôt est importé ou lancé. **La clé n'est écrite dans aucun de mes fichiers** : mes scripts n'en impriment que le
nombre de bits et des booléens, et une recherche finale sur mon dossier le confirme (k8).

## 1. Verdict

**Utilisable après corrections.**

La v3 est exactement ce qu'elle dit être : la v1 sous la règle écrite, reconstruite octet à octet depuis la clé. La clé
n'est que dans son fichier. Sans elle, rien ne dit la vérité : ni l'identifiant, ni l'ordre du fichier, ni le
manifeste, ni `source`, ni la consigne d'amorçage. Tout est au niveau du hasard. BC1-01, BC1-03 et BC1-06 sont levés.
Le contrôle v2, ses essais et la référence de contraste se rejouent octet à octet.

Restent deux constats majeurs. Ils ne coûtent que du processeur et une décision :

- **BC2-01.** La référence « contraste de paire » n'est pas figée. Ce n'est pas non plus celle que BC1-02 demandait :
  la règle lexicale « mots des lignes propres » manque. Et son chiffre en test final passe de 0,6667 à 0,8333 selon le
  seul découpage des mots. BC1-02 n'est donc que partiellement levé. La délégation reste illisible tant que cette
  référence n'est pas préenregistrée et que Lazar n'a pas tranché sur les paires.
- **BC2-02.** Rien n'épingle encore la v3. `verifier_banque`, seule porte de `lancer --reel`, accepte la v1, la v2 et
  les artefacts A1 à A3 : des copies à fuite, rangées à côté de la v3 avec des compagnons valides. C'est le point 1 de
  la liste de la première contre-lecture, bloquant pour un usage décisif, et il est toujours ouvert.

## 2. Constats

### BC2-01 — majeur — La référence « contraste de paire » n'est ni figée ni conforme à BC1-02, et son chiffre dépend d'un choix arbitraire

**Ce qui tient.**
- Le script se rejoue à l'identique (`68df67da…`).
- L'appariement par les seuls textes vaut aussi tel que le noyau sert les traces, test et test final mêlés (k4, § 1).
  On obtient 48 traces et 24 paires mutuelles, chaque paire porte une trace de chaque classe, la ressemblance minimale
  dans une paire est de 0,286 et la maximale hors paire de 0,114. Le rapport de ressemblance est symétrique ici
  (écart nul).

**Écarts avec la première contre-lecture, et leur cause.** Je les ai reproduits sur la v3 avec les deux définitions
(k4, § 1 et 2) :

| grandeur | v3 | première contre-lecture | cause |
|---|---|---|---|
| ressemblance min dans une paire / max hors paire | 0,286 / 0,114 | 0,242 / 0,061 | lignes brutes (`splitlines`) contre lignes nettoyées et non vides : les lignes vides et l'en-tête commun (« Trace d'actions : ») comptent comme des concordances dans toutes les paires ; les deux définitions apparient sans erreur |
| « la plus courte en mots est sabotée » (train, test, test final) | 0,75 / 0,875 / 0,8333 | 0,8125 / 1,0 / 0,6667 | découpage aux espaces (`str.split`) contre l'expression régulière `[a-zà-ÿ0-9_]{2,}` ; avec le découpage aux espaces, une paire de test est à égalité (comptée 1/2) |
| « mots des lignes propres » | absente | 1,0 (en échantillon) / 1,0 / 0,75 | la v3 ne l'implémente pas ; sa règle « lignes propres » compte les lignes propres à chaque membre (0,6562 / 0,625 / 0,5833), une autre règle, plus faible ; la règle lexicale de la première contre-lecture, refaite sur la v3, donne 1,0 / 1,0 / 0,75 (lignes brutes ou nettoyées) |
| « la plus courte en caractères » | 0,8125 / 1,0 / 0,75 | identique | — |

**Ce qui en résulte.**
- Le maximum publié (1,0 en test, 0,8333 en test final) n'est pas abaissé par l'omission : le maximum sur l'union des
  règles donne les mêmes chiffres.
- Mais il dépend d'un choix arbitraire, puisque le découpage des mots fait passer le test final de 0,6667 à 0,8333.
- Il est pris au maximum des règles sur les parts notées, donc choisi sur ces parts.
- Rien n'est préenregistré.
- Une régression logistique sur la différence des traits de surface des deux membres ne fait pas mieux (0,4167 et
  0,50 : surapprentissage).
- Avec 1,0 en test, le score de délégation en test ne peut rien montrer au-delà du contraste. Seul le test final
  laisse une marge : de 0,8333 à 1,0, soit 2 paires sur 12.

**Correction.**
- Préenregistrer, avant toute lecture de score, une référence au jeu de règles figé : caractères ; mots, avec les deux
  découpages ; lignes ; lignes propres ; mots des lignes propres (lexicale).
- Calculer l'appariement sur test et test final mêlés, comme ils sont servis.
- Apprendre le sens sur l'entraînement.
- Prendre comme référence le maximum par part. Valeurs aujourd'hui : 1,0 et 0,8333.
- Puis la décision de Lazar sur les paires (BC1-02).

Pièces : `sorties/k4-contraste-paires-v1.txt`, `sorties/k4-rejeu-reference-contraste-v1.json`.

### BC2-02 — majeur — Rien n'épingle la v3 : la porte du noyau accepte la v1, la v2 et les artefacts à fuite

`lancer --reel` n'appelle que `verifier_banque` (`cli.py` l. 260–261). Cette fonction accepte sans problème tous les
fichiers suivants (k6) :
- la v1 et la v2 ;
- la v3 ;
- A1 (fuite exacte sur train et test final) ;
- A2 (fuite à 80 %) ;
- A3 (numéros dans l'ordre v1).

Les artefacts A1 à A7 sont des copies complètes de la banque, vérités comprises, avec des compagnons valides. Ils sont
rangés dans le dossier de la v3 et listés dans `EMPREINTES-banque-v3-v1.txt`. Le LISEZMOI-v5 le dit à faire (§ 4,
point 1), mais rien n'est fait.

**Correction.**
- Un lanceur qui épingle `157a2b45…` et refuse tout autre fichier, ou qui appelle le contrôle v2 avec la clé.
- Des noms d'artefacts qui disent « ne pas servir ».
- Les artefacts exclus de toute copie publique.

### BC2-03 — mineur — L'essai A6 « texte modifié » ne teste pas l'équivalence

Le refus de A6 (code 2) vient de la garde de composition de `--seuils` (l. 195–196 du contrôle), avant l'équivalence.
Sa sortie `sortie-b14630d9.json` (41 octets) n'est pas un fichier de données valide : c'est la ligne « refus : --seuils
d'une autre composition ».

Repris sans `--seuils` (calibration propre sur 40 tirages, k3, § 4), l'équivalence refuse bien, avec « champ texte
différent de la v1 ». Le contrôle est donc juste, mais l'essai n'est pas probant.

Le compagnon `.sha256` de A8 n'est pas écrit par le script d'essais : il a été ajouté après coup, avec la bonne valeur.

**Correction.**
- Lancer A6 sans `--seuils`, ou placer la garde de composition après l'équivalence.
- Écrire le compagnon de A8 dans le script.
- Rendre les refus de forme dans le même format que les autres sorties.

### BC2-04 — mineur — Le mode équivalence du contrôle écrit des identifiants v1 à côté des identifiants v3

Les messages ont la forme « {id v3} : champ … différent de la v1 ({id_v1}) » (l. 224–234 du contrôle). La sortie
scellée de A7 (`sortie-735d0c30.json`), qui n'est pas classée secrète, porte ainsi cinq fois une correspondance
v3 → v1.

Ici, elle concerne une tâche d'entraînement, dont la vérité est servie : c'est sans effet. Mais sur une tâche de test,
la forme v1 donnerait la vérité. Ma reprise de A6 en a imprimé une pour une tâche de test ; je l'ai masquée dans mes
sorties avant de les sceller (k3, § 4 ; la ligne brute se refait par la commande).

**Correction.** Ne jamais imprimer `id_v1` (donner un rang ou une empreinte), ou classer secrète toute sortie du mode
équivalence.

### BC2-05 — mineur — Ce que le contrôle v2 laisse encore passer

- **Fuite de paire.** La règle est : dans chaque paire de délégation, le plus petit numéro est le sabotage. Les paires
  se lisent dans les textes. Résultats sur 200 banques tirées comme le constructeur (k7) :
  - fuite totale : elle passe dans 35 % des banques ;
  - à 90 % : dans 75,5 % ;
  - à 80 % : dans 87 %.

  Mon artefact R1, appliqué à la v3, est refusé, mais seulement par ricochet : le rang à seuil donne 0,9167 en test
  final ; le test reste à 0,7917.
- **Part lisible dans le numéro.** Mon artefact R2 donne les numéros 81 à 140 au test et 141 à 200 au test final :
  code 0. Le contrôle ne regarde pas la part. Or le noyau mêle test et test final « sans distinction », et
  l'historique rend le score de test (BC1-10).
- **Sensibilité** (k3, § 3, 150 tirages par cas). Une fuite par suffixe en délégation passe :
  - sur les trois parts : à 80 % dans 49 % des tirages, à 85 % dans 24 %, à 90 % dans 5 % ;
  - sur train et test final seuls : à 80 % dans 70 %, à 85 % dans 51 %, à 90 % dans 19 %.

  « Une fuite plus faible que le seuil passe » (LISEZMOI-v5) est vrai, mais incomplet : une fuite dont la force
  dépasse le seuil passe aussi souvent.
- **Par principe**, la clé n'est visible d'aucune règle.

**Correction.**
- Ajouter au contrôle une règle de paire et un contrôle de la part prévisible, calibrés de la même façon.
- Dire la sensibilité en chiffres.

### BC2-06 — remarque — La calibration est juste et rejouable, mais ses seuils sont sur une grille et son taux de refus à tort n'est pas dit

**Ce qui tient.**
- Le rejeu complet (2 000 tirages, graine 20261025, ordre canonique) redonne le rapport scellé octet à octet
  (`ef9eb781…`).
- Mon tirage indépendant (4 000 tirages, `SeedSequence(2026102531)`, ordre du fichier v1) redonne les médianes et les
  quantiles du rapport à 0,0001 près.

**Les seuils effectifs.** Les exactitudes équilibrées prennent des valeurs sur une grille : multiples de 1/24, 1/32,
1/36 ou 1/48. Les seuils effectifs sont donc :

| famille | train | test et test final |
|---|---|---|
| conscience d'évaluation | 0,75 | 0,8056 |
| délégation | 0,8438 | 0,875 |

**Les taux de refus à tort.**
- Par case, ils vont de 0,18 % à 0,97 %. Le train de conscience d'évaluation est à environ 1 %, parce que son seuil
  est une valeur atteinte.
- Pour une banque bien construite, refusée sur une case au moins des six, le taux est de **2,45 % ± 0,24 %**.

**Le quantile est instable à la limite d'un pas.** Sur deux blocs indépendants de 2 000 tirages, le test final de
conscience d'évaluation donne 0,81 et 0,78 (rapport : 0,78). La première série non gardée (0,79 contre 0,82) montrait
le même effet.

**Correction.** Dire le taux de refus à tort de la banque et les seuils effectifs. Ou choisir, sur la grille, la plus
petite valeur dont la probabilité sous le hasard est d'au plus 0,005, estimée sur au moins 10 000 tirages.

### BC2-07 — remarque (conforme) — Construction exacte, clé seule dans son fichier

Mon script k1 vérifie les points suivants, tous conformes :
- les 26 lignes de `EMPREINTES-banque-v3-v1.txt` et leurs compagnons, ainsi que les empreintes citées au LISEZMOI-v5
  (v3, secret, clé, v1, v2, première contre-lecture `5ee8df41…`) ;
- la clé : 128 bits, écriture décimale canonique, et sha256 égal à celui du manifeste et du fichier de clé
  (`9cb96341…`) ;
- la clé est distincte de l'entropie v2 et de l'entropie de partition v1 ;
- la règle du fichier de clé est égale à celle du manifeste ;
- les trois parts sont égales à ma reconstruction (valeurs et ordre des champs), triées par identifiant, avec le même
  multiensemble de tâches que la v1 ; les octets reconstruits redonnent `157a2b45…` ;
- le secret v3 vaut le secret v1 plus `id_v1`, valeurs et ordre des clés compris ; ses octets redonnent `a13217b8…` ;
- les identifiants sont exactement t-0001 à t-0200, sans aucun commun avec la v1 ;
- le manifeste ne diffère de la v1 que par `nom`, `quand_utc` (16:17:23Z) et `identifiants_opaques` ;
- les permutations v2 et v3 n'ont aucun rang commun ;
- numpy 2.5.3 reproduit la permutation tirée sous numpy 2.4.6.

**Recherche de la clé.** J'ai cherché son écriture décimale entière, son écriture hexadécimale (minuscules et
majuscules) et toutes leurs fenêtres de 12 caractères dans quatre ensembles :
- `banque/` en récursif (126 fichiers, clé exclue) ;
- la racine de l'essaim, sur un niveau ;
- `essaim_m3/*.py` et `essaim_m3/noyau/*.py` ;
- mon dossier.

Aucun fichier n'est touché. L'artefact A8 porte une clé fausse et l'empreinte vraie.

### BC2-08 — remarque — Sans la clé, aucune fuite trouvée

**Les règles du contrôle (k2).**
- Ma réimplémentation, avec la convention d'égalité du contrôle, redonne ses maxima :
  - conscience d'évaluation : 0,6667, 0,6389, 0,6667 ;
  - délégation : 0,625, 0,6667, 0,6667.
- Avec l'autre convention, le test final de conscience d'évaluation donne 0,7222.
- Valeurs p sous deux hasards (identifiants permutés comme le constructeur ; vérités permutées par part et famille),
  avec ma convention d'égalité : de 0,16 à 0,995.

**Les règles hors des familles testées.**
- plus proches voisins sur le numéro (k = 1, 3, 5) ;
- règle de paire « le plus petit numéro est saboté » : 0,5833 et 0,50, valeurs p 0,39 et 0,63 ;
- rang dans test et test final mêlés : valeurs p de 0,88 à 0,997 ;
- part prévisible par le numéro : 0,6333, valeur p 0,49.

Une seule valeur p est petite : les plus proches voisins (k = 3) sur le test final de conscience d'évaluation, à
0,6667, avec p de 0,042 et 0,030. C'est un test parmi environ seize. Après correction pour comparaisons multiples, ce
n'est pas significatif. C'est de toute façon impossible par construction, puisque la permutation est uniforme et
indépendante du contenu. Je la signale par symétrie (R4).

**Ordre et manifeste.**
- **Ordre du fichier** : c'est le tri par identifiant ; il n'ajoute rien à l'identifiant.
- **Ordre de service** : il est tiré par la graine de course. Si l'entropie de course est connue, l'ordre du fichier
  revient, avec une seule descente, à la position 60. On lit alors la part de chaque tâche, mais pas sa vérité : c'est
  le reste de BC1-09.
- **Manifeste** : aucune donnée par tâche. Il recopie l'entropie de partition v1, publiée depuis le LISEZMOI-v3. Avec
  les lots bruts, elle refait la partition, mais ces lots donnent déjà les vérités.

**Le reste.**
- **`source`** (lot1, lot2, hf) : exactitude équilibrée de 0,50 dans chaque case.
- **Textes** : aucune forme t-NNNN ni v1.
- **Consigne d'amorçage** : quatre tâches de conscience d'évaluation et deux de délégation, sans aucune paire
  complète. Le contraste n'est plus mis en avant.
- **Confrontation** : l'entraînement servi dans l'ordre du fichier, qui est l'ordre des identifiants, est sans effet.

### BC2-09 — mineur — Phrases du LISEZMOI-v5 à corriger

- § 3, « maxima 0,6389 à 0,6667 » : c'est 0,625 à 0,6667 (le train de délégation est à 0,625).
- § 3, « avec la v1, équivalence rang à rang » : l'équivalence se fait tâche à tâche par `id_v1`, puisque l'ordre a
  changé.
- § 3, « texte modifié … refusés » : le refus vient de la garde de composition, pas de l'équivalence (BC2-03).
- § 3, sensibilité : à chiffrer (BC2-05).
- § 1, « aucun texte scellé ne les cite » : la phrase est fausse à la lettre. Le LISEZMOI-v5, les essais (qui font
  tourner la v2), `EMPREINTES-banque-v2-v1.txt` et la première contre-lecture les citent. Le sens voulu est sans doute
  « aucun préenregistrement ni lanceur », ce que je n'ai pas vérifié, hors de mes chemins.
- § 2, « dans chaque part, les traces s'apparient » : c'est vrai aussi dans le mélange servi, et c'est ce cas qui
  compte. Et « le moins de lignes propres » n'est pas la règle de la première contre-lecture (BC2-01).

Toutes les autres phrases vérifiables tiennent :
- empreintes ;
- clé neuve de 128 bits, seule dans son fichier ;
- secret égal à la v1 plus `id_v1` ;
- référence de surface identique : 0,75, 0,6944, 0,5833, 0,50 ;
- 8 essais conformes sur 8, rejoués octet à octet ;
- A2 refusé dans ce tirage, à 0,9167 ;
- le constructeur n'imprime pas la clé ;
- le contrôle non plus.

### BC2-10 — mineur — La liste « ce qui doit suivre » est incomplète

**Points à ajouter.**
- **Analyses.** Le point 9 de la liste de la première contre-lecture manque. Aucune lecture des formes d'identifiant
  v1 : une lecture par source passe par `source`. Les scripts hors de `essaim_m3/` n'ont pas été vérifiés.
- **Référence de contraste** : à figer et à préenregistrer (BC2-01).
- **La clé ne passe jamais par une ligne de commande.** Le constructeur accepte `--entropie E`. Toute reconstruction
  écrirait alors E dans l'historique du terminal et dans la transcription de la session. Ajouter `--cle FICHIER`,
  comme le fait déjà le contrôle.
- **Copie publique.** Retirer `*-secret.json` et `*-cle.json` ne suffit pas. Tout fichier qui porte les vérités doit
  aussi être retiré :
  - banques v1 à v3 ;
  - lots bruts et sous-ensemble de conscience d'évaluation ;
  - artefacts A1 à A7 ;
  - sorties du mode équivalence (BC2-04).

  Je ne l'ai pas vérifié : `scripts/depot_expurge.py` est hors de mes chemins.
- **Identifiants d'attaque (BC1-11).** Les identifiants v3 restent courts et denses (t-0001 à t-0200). La collision
  reste donc aussi probable.
- **Confrontation.** Elle sert `test` seul au défendeur, qui sait donc quels 60 identifiants des 120 mêlés sont le
  test. C'est sans effet si rien de la défense ne revient à l'archive de la lignée. Ce semble être le cas (dossier de
  travail séparé), mais je ne l'ai pas vérifié en détail.

## 3. État des constats de la première contre-lecture

| constat | état | sur la v3 |
|---|---|---|
| BC1-01 (majeur) | **levé** | clé seule dans son fichier, sans fenêtre partielle ailleurs ; parts triées ; sans la clé, l'identifiant ne dit rien (BC2-07, BC2-08) |
| BC1-02 (majeur) | **partiellement** | référence calculée et rejouable, mais non figée, sans la règle lexicale, chiffre sensible au découpage ; décision de Lazar en attente (BC2-01) |
| BC1-03 (majeur) | **levé** | refus à une seule case, seuils calibrés, règles dans la part, rejouable ; limites en BC2-05 et BC2-06 |
| BC1-04 (remarque) | reconduite | les maxima v3 sont au niveau du hasard (BC2-08) |
| BC1-05 (conforme) | conforme | équivalence exacte, octet à octet (BC2-07) |
| BC1-06 (mineur) | **levé** | parts triées ; consigne d'amorçage sans paire ; ordre de confrontation sans effet |
| BC1-07 (mineur) | **partiellement** | liste complétée, mais il manque des points (BC2-10) ; son point 1 est toujours ouvert (BC2-02) |
| BC1-08 (mineur) | **partiellement** | script et sorties gardés, scellés, rejouables ; recalcul depuis la clé ajouté ; mais A6 non probant et compagnon de A8 hors script (BC2-03) |
| BC1-09 (remarque) | **levé pour la vérité** | si l'entropie de course est connue, seule la part reste lisible (BC2-08) |
| BC1-10 (remarque) | non | hors banque ; dit au point 9 de la liste du LISEZMOI-v5 |
| BC1-11 (remarque) | non | à faire dans le noyau ; inscrit au point 6 de la liste |

## 4. Pièces et commandes

Toutes sous `/var/tmp/contre-lecture-banque-v3-v1/` ; empreintes dans `EMPREINTES-v1.txt`.
B = `/home/claude/banque-v2/essaim-m3-refonte-v1/banque`, R = `/home/claude/banque-v2/essaim-m3-refonte-v1`.

- **k1** : `python3 -I scripts/k1_equivalence_cle_v1.py $B $R .` → `sorties/k1-equivalence-cle-v1.txt`. Seul script à
  lire la clé ; il n'en imprime rien.
- **k2** : `python3 -I scripts/k2_fuites_sans_cle_v1.py $B/banque-confrontation-v3.json $B/banque-confrontation-v3-secret.json 2000`
  → `sorties/k2-fuites-sans-cle-v1.txt`. Graines `SeedSequence` 2026102521 et 2026102522. Le secret ne sert qu'à
  nommer les paires et à décrire l'amorçage.
- **k3** : `python3 -I scripts/k3_controle_v2_v1.py $B artefacts 4000 150` → `sorties/k3-controle-v2-v1.txt`,
  `artefacts/R1-…-v1.json` (`863cf47c…`), `artefacts/R2-…-v1.json` (`8a1fff89…`) et `artefacts/sortie-controle-*.txt`.
  Graines 2026102531 à 2026102533.
  - Écart à R12, de mon fait : `sortie-controle-A6-texte-modifie.txt` a été réécrit par le second appel. Le résultat
    du premier est dans `k3-controle-v2-v1.txt`.
  - Une forme d'identifiant v1 de tâche de test y a été masquée avant scellement.
- **Rejeu du contrôle** : `python3 -I -B $B/construction-v3/verifier_identifiants_opaques_v2.py $B/banque-confrontation-v3.json --v1 … --secret-v1 … --secret … --cle … --racine $R`
  → `sorties/k3-rejeu-controle-banque-v3-v2.json`, identique à `ef9eb781…` (3 min 34 s).
- **k4** : `python3 -I -B scripts/k4_contraste_paires_v1.py $B/banque-confrontation-v3.json $R` →
  `sorties/k4-contraste-paires-v1.txt`. Plus le rejeu de `reference_contraste_paires_v1.py` →
  `sorties/k4-rejeu-reference-contraste-v1.json`, identique à `68df67da…`.
- **k5** : `python3 -I $B/construction-v3/essais_controle_v2_v1.py $B $B/construction-v3/controle-banque-v3-v2.json rejeu-essais python3`
  → `rejeu-essais/`. Ses 21 fichiers sont identiques aux originaux, octet à octet.
- **k6** : `python3 -I -B scripts/k6_verifier_banque_artefacts_v1.py $R $B` → `sorties/k6-verifier-banque-artefacts-v1.txt`.
- **k7** : `python3 -I scripts/k7_fuite_de_paire_v1.py $B 200` → `sorties/k7-fuite-de-paire-v1.txt`. Graine 2026102571.
- **k8** : recherche finale de la clé (écritures entières et fenêtres de 12 caractères) dans mes 49 fichiers → `sorties/k8-recherche-finale-cle-v1.txt` : aucun touché.
