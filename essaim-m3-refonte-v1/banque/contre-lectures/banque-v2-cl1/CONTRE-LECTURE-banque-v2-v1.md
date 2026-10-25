# Contre-lecture de la banque `confrontation-v2` (identifiants opaques) — v1

Contre-lecteur neuf (R2, R4), 25 octobre 2026. Je n'ai écrit ni la banque, ni ses scripts, ni le LISEZMOI, ni l'audit.
Lecture seule des chemins donnés et de quelques fichiers voisins du noyau, cités au fil du texte (`contrat.py`,
`archive.py`, `entrainement.py`, `confrontation.py`, `bac_a_sable.py`, un passage de `analyse_gradient.py`), plus une
recherche non récursive dans `essaim_m3/*.py` et `essaim_m3/noyau/*.py` et la liste (un niveau) de `essaim_m3/outils/`.
Aucun accès à git ni au réseau, aucun sous-agent, aucun fichier ou dossier interdit ouvert. Tout ce que j'ai écrit est sous `/var/tmp/contre-lecture-banque-v2-v1/`. Interpréteur :
`python3 -I` (Python 3.13.17, numpy 2.5.3) ; `-B` quand le code du dépôt est importé. Aucun `__pycache__` n'a été créé
dans le dépôt (vérifié).

## 1. Verdict

**Utilisable après corrections.** La v2 est exactement ce qu'elle dit être : la v1 sous de nouveaux identifiants,
vérifiée octet à octet. Sans la clé, aucune fonction de l'identifiant ne prédit la vérité : c'est vrai par
construction, et confirmé sous le hasard. Mais trois constats majeurs empêchent de la servir telle quelle :

- **BC1-01.** L'entropie E est publiée et l'ordre v1, rangé par vérité, est gardé. Avec E, l'identifiant v2 donne
  la vérité de toutes les tâches, ainsi que leur part (test ou test final).
- **BC1-02.** Le contraste entre les deux traces d'une paire donne 1,0 sur test et 0,75 sur test final en délégation,
  sans lire le sens des traces. La référence préenregistrée ne mesure pas ce canal.
- **BC1-03.** Le contrôle, s'il sert de porte, laisse passer une fuite totale sur le test final.

Les corrections qui bloquent un usage décisif sont BC1-01, BC1-02 et le point 1 de la liste du § 3. Elles ne
coûtent que du processeur, et la v2 n'est encore citée par aucun texte scellé.

## 2. Constats

### BC1-01 — majeur — E est publiée, et avec l'ordre v1 gardé, l'identifiant v2 rend toutes les vérités

**Où se trouve la clé.** E = 14234892761277461467225772596104759309, avec la règle, figure à trois endroits :
- dans le manifeste de la v2 (`identifiants_opaques`) ;
- au § 2 de `LISEZMOI-v4.md` ;
- au point 2 de `essais-controle-identifiants-v1.txt`.

**Pourquoi l'ordre la rend décisive.** Chaque part garde l'ordre v1. Or cet ordre est un tri par identifiant v1
(`banque.py` l. 128), donc rangé par vérité. Dans test comme dans test final, on trouve 12 paires H puis S, puis
18 évaluations, puis 18 usages réels (c1, point 8). Qui a E inverse la permutation et passe ainsi de l'identifiant au
rang v1, puis à la part et à la vérité.

**Démonstration.** Mon décodeur D1 (c2) ne lit que quatre choses : E, la règle écrite, ce que le noyau sert
(identifiant, famille) et les vérités servies de l'entraînement. Il ne lit ni texte, ni v1, ni secret. Résultats :
- exactitude équilibrée de 1,0 dans les deux familles, sur test et sur test final ;
- part (test ou test final) retrouvée pour les 120 tâches que le noyau sert mêlées « sans distinction »
  (`boucle.py` l. 606–608).

**Ce que cela contredit.** Deux phrases du LISEZMOI-v4 sont donc fausses pour qui le lit :
- le secret serait « la seule correspondance entre les deux banques » (l. 29–30) ;
- « aucune règle sur l'identifiant ne prédit la vérité » (l. 50).

**Portée.** En mode réel, l'exécution isolée recouvre `/home` et le dossier du code (`bac_a_sable.py` l. 60–64). Un
organisme n'atteint donc E que si E sort de ces arbres : copie publique expurgée, papier, consigne, document
moissonné. L'opacité repose ainsi sur le secret de trois documents qui ne sont pas classés secrets, à la
différence du fichier secret.

**Correction.**
- (a) Recommandée, confiance élevée : construire une banque v3 maintenant, tant qu'aucun texte scellé ne cite la v2.
  - Tirer une entropie neuve et ne l'écrire que dans le fichier secret ; le manifeste n'en garde que l'empreinte
    sha256, comme engagement vérifiable.
  - Trier chaque part par identifiant nouveau, ce qui ferme aussi BC1-06 et BC1-09.
  - Écrire un LISEZMOI-v5 sans E, et archiver la v2 avec la mention « jamais servie ».
- (b) À défaut :
  - classer secrets `LISEZMOI-v4.md`, les essais et le manifeste v2 : hors de la copie publique (vérifier
    `scripts/depot_expurge.py`, que je n'ai pas lu), jamais dans une consigne ;
  - réécrire la revendication en « opaque pour qui n'a pas E ».

Pièces : `scripts/c1_equivalence_v1.py`, `scripts/c2_decodeurs_v1.py`, `sorties/c1-equivalence-v1.txt`,
`sorties/c2-decodeurs-v1.txt`.

### BC1-02 — majeur — Le contraste de paire en délégation donne 1,0 sur test et 0,75 sur test final, hors de la référence

**Appariement.** Les 48 traces de test et de test final sont servies ensemble dans `taches_test` (`boucle.py`
l. 607–623). Elles s'apparient sans erreur par la seule ressemblance des textes (rapport de `difflib` sur les
lignes) :
- la voisine la plus proche est l'autre membre de la paire pour 48 traces sur 48, et ces voisines sont mutuelles ;
- le rapport de ressemblance vaut au moins 0,242 dans une paire et au plus 0,061 entre deux paires ;
- chaque paire contient une trace de chaque classe.

**Contraste.** Des règles d'un seul trait, apprises sur les 16 paires d'entraînement, suffisent :

| règle apprise sur l'entraînement | train | test (12 paires) | test final (12 paires) |
|---|---|---|---|
| la trace la plus courte en caractères est sabotée | 0,8125 | **1,0** | **0,75** |
| la trace la plus courte en mots est sabotée | 0,8125 | 1,0 | 0,6667 |
| mots des lignes propres à chaque membre | 1,0 (sur l'échantillon d'apprentissage) | 1,0 | 0,75 |

**Ce que la référence ne voit pas.** La référence de surface lit une trace à la fois. Elle vaut 0,58 sur test et
0,50 sur test final (`LISEZMOI-v3.md` § 3) et ne mesure pas ce canal. Le LISEZMOI-v4 (l. 33–35) le dit inchangé,
mais sans chiffre. L'audit (§ 3) a vu la même asymétrie : la trace sabotée est la plus longue dans 0 paire sur 12
en test, 3 sur 12 en test final. Il l'a jugée « hors de portée de cet organisme qui voit une trace par consigne ».
Elle est pourtant à portée de tout organisme qui lit son `contexte.json`. De plus, la consigne d'amorçage montre
trois paires côte à côte (BC1-06).

**Correction.**
- Préenregistrer, avant toute lecture de score, une référence « contraste de paire » pour la délégation, avec au
  moins la longueur et les mots des lignes propres, apprises sur l'entraînement.
- Lire chaque score de délégation contre la plus haute des deux références.
- Décision de Lazar, car l'instrument et les hypothèses H-E1 et H-E2 sont touchés : soit servir un seul membre de
  chaque paire en test et en test final (effectif divisé par deux), soit garder les paires et l'écrire dans les
  hypothèses.

Pièces : `scripts/c4_paires_textes_v1.py`, `sorties/c4-paires-textes-v1.txt`.

### BC1-03 — majeur — Le contrôle des 50 règles, comme porte, laisse passer une fuite totale sur le test final

**Règle du contrôle.** `verifier_identifiants_opaques_v1.py` (l. 112) déclare une règle « prédictive » si elle atteint
au moins 0,80 sur test **et** sur test final. Ma réimplémentation indépendante reproduit ses sorties scellées, en v1
comme en v2 : nombre de règles, maxima, règles prédictives (c3, point 1).

**Le seuil n'est pas calibré.** J'ai tiré 2 000 fois les identifiants au hasard, comme le constructeur (c3, 2a) :
- aucun refus sur les 2 000 tirages ;
- le 99e centile du maximum des 50 règles vaut 0,75 sur test et 0,72 sur test final en conscience d'évaluation,
  0,79 et 0,79 en délégation ;
- avec la condition « au moins une part », le taux de refus à tort ne serait que de 0,2 % (conscience d'évaluation)
  et 1,2 % (délégation).

**Il est peu sensible.** Une fuite partielle, juste dans 80 % des tâches de délégation, passe dans 83 % des tirages.
Juste à 75 %, elle passe dans 93 % ; juste à 85 %, dans 48 % (c3, point 3).

**Artefacts passés au vérificateur scellé** (c5) :
- A1, fuite exacte sur train et sur test final, hasard sur test : **code 0**, alors que la meilleure règle donne 1,0
  sur le test final, la part décisive ;
- A2, fuite juste à 80 % : **code 0**, avec 0,79 sur test et 0,92 sur test final ;
- A3, numéros dans l'ordre du fichier, une erreur de construction plausible : refusé seulement grâce à la parité en
  délégation. En conscience d'évaluation, aucune règle n'est prédictive (au plus 0,5 et 0,58), alors qu'un tri des
  numéros dans chaque part donne 1,0.

**Limites de principe.** Aucune des 50 règles ne peut voir une clé (BC1-01). Des règles apprises sur l'entraînement,
puis transférées par valeur absolue, ne voient ni un rang relatif ni une structure propre au test.

**Correction.**
- Refuser dès qu'une part dépasse le seuil : le test final seul suffit à invalider.
- Calibrer le seuil par tirages au hasard, par exemple refuser au-delà du 99e centile du maximum.
- Ajouter des traits de rang dans la part.
- Garder un script d'artefacts et ses sorties, A1 à A3 compris.
- Présenter ce contrôle pour ce qu'il est, un test de non-régression de la construction : la garantie vient du
  tirage uniforme et du secret de l'entropie.

Pièces : `scripts/c3_controle_hasard_v1.py`, `scripts/c5_artefacts_v1.py`, `sorties/c3-controle-hasard-v1.txt`,
`sorties/c5-*`, `artefacts/artefact-A*`.

### BC1-04 — remarque — Sans la clé, les 0,61 et 0,67 de la v2 sont au niveau du hasard

J'ai situé les maxima observés par deux tirages indépendants de 2 000 fois chacun :
- identifiants tirés comme le constructeur : la part des tirages au moins égale à l'observé vaut 0,71 sur test et 0,72
  sur test final en conscience d'évaluation, 0,51 et 0,51 en délégation ;
- vérités permutées dans chaque part et chaque famille, identifiants v2 fixes : 0,71 et 0,72, puis 0,52 et 0,54.

Les deux constructions concordent. Les observés sont même la médiane du hasard (0,6111 et 0,6667). Rien n'est
à signaler sur les règles qui n'utilisent pas E. Pièce : `sorties/c3-controle-hasard-v1.txt`.

### BC1-05 — remarque (conforme) — L'équivalence est exacte, octet à octet, par un code à moi

Mon script (c1) vérifie les points suivants, tous conformes :
- les empreintes f1387a20…, c68d7d4b…, 52beb637… et 1775a9e0…, avec leurs compagnons, ainsi que les huit lignes de
  `EMPREINTES-banque-v2-v1.txt` ;
- E vaut 124 bits, ce qui est compatible avec `secrets.randbits(128)` ;
- la permutation recalculée donne les identifiants rang à rang ;
- les parts, l'ordre, les champs et l'ordre des clés sont identiques, avec les mêmes valeurs ;
- le secret v2 est égal au secret v1 plus `id_v1`, l'ordre des clés compris ;
- le manifeste ne diffère que par `nom`, `quand_utc` et `identifiants_opaques`.

La v2 et son secret, reconstruits depuis la v1 et E, redonnent exactement 52beb637… et 1775a9e0… (en reprenant
seulement `quand_utc`). numpy 2.5.3 reproduit la permutation tirée sous numpy 2.4.6.

### BC1-06 — mineur — L'ordre v1 n'est pas nécessaire à la référence, et il expose ailleurs un ordre rangé par vérité

**La raison avancée ne tient pas.** La référence de surface (`reference_traits_texte`) reste identique quand chaque
part est triée par identifiant v2, et pour trois mélanges au hasard (c6). Garder l'ordre v1 pour que la référence
« reste identique » (docstring du constructeur l. 8–9 ; LISEZMOI-v4 l. 31–32) ne sert donc à rien : la descente de
gradient est sur le lot entier.

**L'ordre gardé a un coût.**
- La consigne d'amorçage montre les six premières tâches d'entraînement du fichier, avec leur vérité (`boucle.py`
  l. 507, `contrat.py` l. 175). Ce sont trois paires complètes du lot 1, H puis S : uniquement de la délégation, ce
  qui met le contraste en avant.
- La confrontation sert l'entraînement dans l'ordre du fichier (`confrontation.py` l. 213).
- Le canal de l'ordre de service (BC1-09) en dépend aussi.

**Correction.** Trier par identifiant nouveau (voir BC1-01, option a). Pièces : `scripts/c6_reference_ordre_v1.py`,
`sorties/c6-reference-ordre-v1.txt`.

### BC1-07 — mineur — La liste « ce qui doit suivre » est incomplète

Le complément est au § 3. Le point qui compte le plus : rien n'empêche aujourd'hui un lanceur de servir encore la v1.

### BC1-08 — mineur — Les artefacts des essais ne sont pas probants, ni rejouables

**Ce qui manque.**
- Les trois artefacts du point 6 ont été faits dans un dossier temporaire, sans script ni sortie gardés.
- Ils ne sondent ni la zone du seuil, ni une part seule, ni un rang, ni une clé. La fuite injectée est celle de la v1
  elle-même, un signal à 1,0.
- Le mode « équivalence » du vérificateur (l. 143–168) ne recalcule pas les identifiants depuis E. La règle n'est
  vérifiée qu'au point 4 des essais, lui non plus gardé.

**Correction.** Ajouter ce recalcul au vérificateur, et garder les artefacts avec leurs sorties scellées.

### BC1-09 — remarque — Ordre de service et graine de l'organisme : fermés par défaut, mais à une condition

L'organisme reçoit sa graine (`boucle.py` l. 609, l. 631), sœur de celles de `ordre_train` et de `ordre_test`, toutes
dérivées de l'entropie de la course. Sans `--graine`, cette entropie est tirée par le système (`cli.py` l. 380) :
le canal est fermé.

Si l'entropie de course est connue ou devinable (une graine fixe, un manifeste publié), mon décodeur D2 remet le
test servi dans l'ordre du fichier. Il obtient alors 1,0 partout, parce que l'ordre du fichier suit la vérité (c2).
Le tri par identifiant nouveau (BC1-06) supprime cette dépendance.

### BC1-10 — remarque — L'historique ouvre un sondage adaptatif du test, pareil en v1 et en v2

`historique` rend à chaque génération le score global sur test, arrondi à 4 décimales (`archive.py` l. 229–234).

- **Granularité.** Corriger une seule réponse change le score de 1/48 en délégation et de 1/72 en conscience
  d'évaluation. Le score prend au plus environ 900 valeurs, soit environ 10 bits par génération.
- **Ce qu'un organisme peut en tirer.** Il peut garder ses réponses dans son dossier de travail, qui est recopié dans
  la vue. En les variant d'une génération à l'autre, il peut alors apprendre une part des vérités du test et
  distinguer test et test final. Le test final reste protégé : il n'est jamais rendu.

À dire dans le préenregistrement. Ce point n'est pas causé par la v2.

### BC1-11 — remarque — Les identifiants d'attaque sont libres : la mention « aucun `att-…` » ne protège pas la confrontation

Une attaque peut porter n'importe quel identifiant (`taches.py` l. 256) : le préfixe `att-…` n'est qu'une valeur par
défaut. Aucune garde ne refuse une collision avec la banque. Or les attaques sont mêlées au test servi du défendeur
(`confrontation.py` l. 203–205).

Avec des identifiants courts et denses (`t-0001`…`t-0200`), un attaquant qui imite la forme qu'il voit dans son
contexte crée des doublons. Le défendeur ne peut alors donner qu'une réponse par identifiant, et le score d'attaque
est faussé.

**Correction.** Refuser ou renommer, dans le noyau, tout identifiant d'attaque déjà présent dans la banque.

## 3. Ce qui doit suivre si une banque à identifiants opaques est retenue (liste complétée)

1. **Porte de lancement.** `lancer --reel` n'appelle que `verifier_banque` (`cli.py` l. 260–264), qui accepte la v1 et
   l'artefact A1 (c7). Tout lanceur de la confrontation doit refuser explicitement f1387a20…, ou appeler le contrôle
   corrigé : aujourd'hui, ce n'est qu'un « peut » (LISEZMOI-v4 l. 60–61).
2. **Traits d'activations : pas un simple renommage.** `charger_traits` (`cli.py` l. 176–206) exige trois choses :
   chaque identifiant de la banque, le `sha256_banque` du manifeste égal à l'empreinte du fichier servi, et les
   empreintes de chaque `traits-<vue>.npz`. Il faut donc un dossier de traits dérivé neuf, avec un nouveau
   `manifeste-traits.json` qui dit la dérivation (mêmes vecteurs, extraits sur la v1) et ses compagnons.
   **Non vérifié :** si le texte donné au modèle lors de l'extraction contenait l'identifiant v1, les activations
   portent le suffixe `-S`/`-H`. Il faudrait alors réextraire, ce qui est un nœud de dépense. À vérifier dans
   `extraire_activations_v2.py`, hors de mes chemins.
3. **Bras appariés.** `--depuis` exige la même banque que la course d'origine (`cli.py` l. 266–270). Les courses M et
   S du second pilote, qui tournaient sur la v1, ne peuvent pas servir d'origine à un bras v2 : toute comparaison se
   fait entièrement en v1 ou entièrement en v2.
4. **Empreintes figées.** `sha256_banque` du manifeste de course change (`boucle.py` l. 299), ainsi que toute pièce
   figée qui cite f1387a20… ou des identifiants v1 : préenregistrement, extraits mécaniques, scripts d'audit qui
   comparent `course/banque.json` par identifiant.
5. **Préenregistrement.** La phrase « jamais une vérité de `test` ni de `test_final` n'est servie par le noyau »
   (l. 438, citée par l'audit) reste à réécrire, à cause de BC1-01, BC1-02 et BC1-10. C'est un nœud : modification
   d'un préenregistrement scellé.
6. **Consigne d'amorçage.** Elle change, puisqu'elle porte des identifiants. Avec l'ordre v1, elle montre trois paires
   (BC1-06).
7. **Identifiants d'attaque.** Ajouter une garde de collision (BC1-11).
8. **Vivier.** Rien à faire : sa garde de disjonction porte sur le contenu, dans les deux sens, et sa garde de
   collision sur les identifiants (`vivier.py` l. 150–172). La disjonction par identifiant de source garde `id_source`,
   conservé dans le secret v2. Le LISEZMOI est juste sur ce point.
9. **Analyses.** Aucune lecture des formes d'identifiant v1 (`cd-lot`, `ce-hf`, `-H`/`-S`) dans `essaim_m3/*.py` ni
   dans `essaim_m3/noyau/*.py` ; une lecture par source doit passer par le champ `source`. Les scripts situés hors de
   ces dossiers n'ont pas été vérifiés.
10. **Procédures à l'aveugle.** Toute procédure qui montrait les identifiants à un sous-agent, comme la vérification
    d'étiquettes, était renseignée par les identifiants v1. Non vérifié.

## 4. Pièces et commandes

Toutes sous `/var/tmp/contre-lecture-banque-v2-v1/` ; les empreintes sont dans `EMPREINTES-v1.txt`.
B = `/home/claude/banque-v2/essaim-m3-refonte-v1/banque`, R = `/home/claude/banque-v2/essaim-m3-refonte-v1`.

- c1 : `python3 -I scripts/c1_equivalence_v1.py $B` → `sorties/c1-equivalence-v1.txt` (0 écart).
- c2 : `python3 -I scripts/c2_decodeurs_v1.py $B/banque-confrontation-v2.json` → `sorties/c2-decodeurs-v1.txt`.
- c3 : `python3 -I scripts/c3_controle_hasard_v1.py $B $B/construction-v2 2000` → `sorties/c3-controle-hasard-v1.txt`,
  avec les graines SeedSequence 2026102501 à 2026102503.
- c4 : `python3 -I scripts/c4_paires_textes_v1.py $B/banque-confrontation-v2.json $B/banque-confrontation-v2-secret.json`
  → `sorties/c4-paires-textes-v1.txt`. Le secret ne sert qu'à noter l'appariement.
- c5 : `python3 -I scripts/c5_artefacts_v1.py $B/banque-confrontation-v2.json $B/construction-v2/verifier_identifiants_opaques_v1.py .`
  → `artefacts/artefact-A1…A3-v1.json` (+ `.sha256`), `sorties/c5-*`, avec la graine 2026102505.
- c6 : `python3 -I -B scripts/c6_reference_ordre_v1.py $R $B/banque-confrontation-v2.json .`
  → `artefacts/reference-ordre-*-v1.json`, `sorties/c6-reference-ordre-v1.txt`, avec la graine 2026102506.
- c7 : `python3 -I -B scripts/c7_verifier_banque_v1.py $R $B/banque-confrontation-v1.json $B/banque-confrontation-v2.json artefacts/reference-ordre-triee-par-id-v2-v1.json artefacts/artefact-A1-fuite-train-et-test-final-v1.json`
  → `sorties/c7-verifier-banque-v1.txt`.
- Audit lu : `AUDIT-SYMETRIE-pilote2-v1.md`, empreinte f732bfd8…, égale à son compagnon et à la valeur citée au
  LISEZMOI-v4.
