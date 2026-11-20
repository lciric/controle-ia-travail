# Contrôle du différentiel v10 → v11 — préenregistrement du palier 0b — v1

- **Auteur** : contrôleur neuf, modèle O. C'est le même contrôleur que pour la v10 (`P/controle-v10/controle-differentiel-palier-0b-v9-v10-v1.md`, `98975c9e…`, égal à l'octet à ma pièce). Je n'ai écrit ni le préenregistrement, ni le code, ni sa vérification. Pièce de travail (classe C).
- **Date** : 2026-11-20 ; `date -u` lu à 10:53Z en cours de travail.
- **Mandat** :
  - le message de la session du compte organisme, sous les interdits du mandat `P/mandat-controle-differentiel-palier-0b-v9-v10-v1.md` (`1d0bf3d7…`) ;
  - j'ai lu aussi, après avoir vérifié son compagnon, le mandat du rédacteur de la v11 (`9426728c…`).
- **Conditions** :
  - Processeur seul, aucun tirage, aucun lancement du code du palier, aucun appel à un fournisseur de modèles, aucune dépense, aucune écriture dans le dépôt, aucun commit.
  - Un `git fetch origin main`, réussi au premier essai, puis un `git show` par le commit d'`origin/main` (`d7a08a46cd175a089c7fd7da8ed6baaf39a09a80`), redirigé vers mon dossier.
  - Programmes lancés par leur chemin : l'outil de remplacement (le rejeu, et un essai sur une copie) et mon `verifier_mes_textes_v1.py`.
  - Aucune commande de liste, aucun heredoc, aucun code en ligne.
  - **Aucun refus de permission, de classifieur ni de garde.**

P : `docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/`.

## Verdict

**Conforme, à sceller après le code v5, sa vérification et l'erratum du commit.**

- **Rejeu** : la v11 est exactement la v10 plus les 24 remplacements du JSON ; le rejeu est égal à l'octet.
- **Mes neuf textes** (C1, les six renvois à R-4182, NE-1, NE-2) sont égaux à l'octet.
- **La remarque 1** : les quinze remplacements du rédacteur sont justes et dans la lettre de `GO-2026-11-20-41`.
- **La réserve 1 du rédacteur** (le cas « au plus 0,55 mais au-dessus de M + 2 σ₀ » de la règle de signalement) est dans la lettre, à garder. La mère le consigne en une ligne (§ 3).
- **Rien d'autre ne change** : aucun critère, aucune valeur gelée, aucune prédiction, aucune issue. Le seuil de 0,55 reste, et il devient le plancher du seuil d'arrêt.
- **Deux textes non exigés** (§ 5) sont prêts pour la version de l'erratum du commit, qui se refera de toute façon.

## 1. Empreintes, registres, rejeu

**Empreintes.** Chacune a été vérifiée par `env -C P sha256sum -c F.sha256` ; chacune est égale à son compagnon et au préfixe donné.

| pièce | empreinte |
|---|---|
| v10 | `ac2deb4daf4fb0b3088400ba742a6583844b0e5720774fd8b9055d0a72250f6b` |
| v11 | `9faf31a3dd0278b562c62fbded81222b674f6c5df225006f9e0e8d610b720989` |
| JSON v10 → v11 | `1d5ec1821251508b10aed4b057e9f1b223c0d0985dbe49fadeae15a97b9bf2d2` |
| journal de la v11 | compagnon vérifié |
| différentiel v10 → v11 | `b4d928ef0226ef7b1809859ee7ed500b6042c183a24ee35da951061040e24aeb` |
| rapport du rédacteur v11 | `40791d3700e0fa52f843bd59ffa6e529f515f14b75daa3b255a20f237ddd92ec` |
| mandat du rédacteur v11 | `9426728cde7c375ac87ec4bdecd55d5e3831699de750c042a061ea60548fd15c` |

**La ligne `GO-2026-11-20-41`.** Elle est à la ligne 572 de `registres/go.md`, à `origin/main` `d7a08a46…`.
- La colonne de la décision : « **Organisme, palier 0b, remarque 1 du contrôle v8→v9 : option (ii).** Le seuil d'arrêt de l'étape 3 des audits par dose est le plus grand de 0,55 et de la moyenne permutée + 2σ₀ (une exactitude au plus 0,55 n'arrête jamais) ; précise GO-2026-11-20-25 (1). À porter dans la v11 du préenregistrement du palier 0b. »
- Le mot cité : « Recommandation du contrôleur : (ii), confiance moyenne à haute. : go ».
- La v11 cite l'une et l'autre à la lettre, sans les identifiants de la colonne de source, et donne le commit `6048bb22…`.

**Rejeu.** J'ai passé l'outil `391db990…` sur la v10, avec le JSON. Il rend « FAIT : 24 remplacement(s) », sortie `9faf31a3…`, aucun avertissement, et `cmp` avec la v11 est muet.
- **Journal** : il ne diffère de celui du rédacteur que par l'heure (10:51:20Z contre 10:47:54Z) et par deux chemins.
- **Différentiel** : je l'ai refait par `diff -u`. Il n'a de différent que la ligne d'en-tête « +++ ».
- **Lignes touchées** : quatorze lignes de la v10 (1, 3, 6, 209, 357, 359, 429, 904, 912, 917, 934, 942, 947 et 950). Aucune n'est dans « Hypothèse », « Prédiction », « Métrique », « Valeurs gelées », « Les six critères », « Critères de lecture gelés » ou « Liste d'arrêt ».
- **Identifiants** : le JSON n'en porte aucun, ni de modèle ni de session.

**Mes neuf textes.** `verifier_mes_textes_v1.py` compare les neuf paires de mon contrôle de la v10 aux entrées du JSON : les neuf sont égales à l'octet. Ce sont les rangs 3 (texte 1), 14 (texte 2), 18 (texte 3), 19 (texte 4), 20 (texte 5), 23 (texte 6), 12 (C1), 6 (NE-1) et 13 (NE-2). Les quinze autres sont du rédacteur.

## 2. Les quinze remplacements du rédacteur

| rang | lieu | jugement |
|---|---|---|
| 1 | titre | juste |
| 2 | ligne de version, alinéa « Version 11 » | juste. Il cite `GO-2026-11-20-41` et le mot à la lettre ; le compte « neuf et quinze » est exact. Il dit la phrase gelée « le seuil de 0,55 reste, et il reste le plancher du seuil d'arrêt » et, en une phrase, le report au signalement (§ 3). Dire que la mère « retient » NE-1 et NE-2 est à la lettre du mandat de la v11 (« la mère veut NE-1 et NE-2 ») |
| 4, 5 | ligne de version | juste : les phrases de la v10 qui disaient la remarque ouverte sont dites d'elle seule |
| 7 | date | juste ; refait la forme que NE-1 corrigeait (réserve 6 ; NE-4, § 5) |
| 8 | « Seuil », tête des lectures de la forme | à la lettre de `GO-2026-11-20-41` |
| 9 | « Seuil », cas « au plus 0,55 mais au-dessus de M + 2 σ₀ » | à la lettre : « une exactitude au plus 0,55 n'arrête jamais ». « Tenue » est le nom de l'option (ii) que Lazar a prise (« la tenue prime ») et le mot de la lecture voisine (« au plus 0,55 et au plus M + 2 σ₀ — elle est tenue ») |
| 10 | « Seuil », règle de signalement, même cas | dans la lettre ; voir le § 3 |
| 11 | garde 25 | juste et demandé par le point 3 du mandat. C'est l'artefact « arrêt sur une exactitude au plus 0,55 », du type « aucun arrêt » que la colonne porte déjà. La moitié « contenu » suit le rang 10 (§ 3). « M + 2 σ₀ étant planté » veut dire que A, M et σ₀ sont plantés, comme dans les artefacts de la version 9 ; c'est sans conséquence |
| 15 | « Contre-lecture », alinéa « Version 11 » | juste ; il dit mon verdict à la lettre |
| 16, 17 | remarque 1 de l'annexe H | juste. Ce qui reste non lu, « un nul décalé vers le bas », est dit comme l'option (ii) le disait, et il est vu au compte rendu (A, σ₀, M et M + 2 σ₀ rapportés). Le report au signalement est dit comme une lecture du texte et non comme la lettre du mot (« la ligne `GO-2026-11-20-41` ne parle que du seuil d'arrêt ») |
| 21 | code v5, point 1 | juste ; voir la réserve 3 (§ 4) |
| 22 | code v5, point 6 | juste : l'essai et le défaut de banc qui voient l'arrêt sous 0,55 |
| 24 | « Ce qui revient à la mère » | juste |

**Lieux qui disaient encore la remarque 1 ouverte.** Je les ai cherchés par `grep -o -E` sur « non tranch », « posée à Lazar », « attend son mot » et « ne part pas avant ». Ceux qui restent sont des phrases d'histoire des versions 9 et 10, couvertes par la clause de l'alinéa « Version 11 » (ligne de version, l. 3 ; « Contre-lecture », l. 429 ; « Ce qui revient à la mère », l. 950), ou des phrases qui ne parlent pas de cette remarque (l. 3 pour les nœuds 1 et 2, l. 65, l. 207). Aucun lieu n'est oublié.

## 3. Réserve 1 — le même cas dans la règle calibrée de signalement (rangs 10, 2, 11, 17, 22)

**Dans la lettre ; à garder ; aucun texte de retrait.** Confiance moyenne à haute. Quatre raisons, toutes tirées du texte gelé ou des lignes de GO :

1. **La version 9 a lié ce cas à la remarque 1 en toutes lettres.** Elle l'écrivait « non tranché, comme pour la forme (remarque 1) ». Sa réponse est donc due à l'endroit même où la remarque se ferme. Laisser « non tranché » ferait dire au texte ouverte une remarque que Lazar a fermée.
2. **Le texte gelé définit la règle de signalement par renvoi au point (1).** L'annexe H, § 2, l. 910, inchangée : « Le seuil y est le même que pour la forme […] : c'est la même règle calibrée, étendue, telle que le point (1) la laisse ». De même, `GO-2026-11-20-25` (2) étend « la règle calibrée », et `GO-2026-11-20-41` dit « précise GO-2026-11-20-25 (1) ». La règle que (2) étend est donc celle que (1) laisse après cette précision, avec 0,55 pour plancher.
3. **La phrase gelée** « Le seuil de 0,55 n'est pas changé ; la règle dit ce qui vaut preuve qu'il est dépassé » exclut qu'une exactitude au plus 0,55 prouve un dépassement de 0,55. Cela vaut pour le contenu comme pour la forme. C'est la raison pour laquelle le contrôle de la v9 recommandait (ii).
4. **Aucun seuil de la règle ne change, et aucune version n'a posé la mention pour une exactitude au plus 0,55.** Jusqu'à la v8, la lettre était « au-dessus de 0,55 » ; les versions 9 et 10 laissaient ce cas ouvert. Le report ne rend la règle plus lâche que nulle part.

**Le mandat de la v11** dit « Ne change rien d'autre : ni la règle calibrée de signalement ». Mais il dit aussi « partout où le texte dit encore la remarque 1 […] « non tranchée » ». Le rang 10 relève de la seconde consigne, sans toucher les seuils de la première.

**À porter à la mère** : une ligne de routine qui consigne cette lecture, comme elle a consigné la lecture (i) de la remarque 2. **Rien pour Lazar** : ni arrêt ni valeur gelée en jeu, et la lettre de ses deux lignes suffit. Si la mère jugeait autrement, le cas redeviendrait une question posée à elle ; le retrait seul laisserait un « non tranché » sans remarque ouverte, ce que je déconseille.

## 4. Réserves 3, 5, 6 et 7

- **Réserve 3 — la colonne du seuil de la table de l'étape 3.** Ce n'est pas une faute. La section « Seuil » demande de rapporter « A, σ₀, M et la valeur M + 2 σ₀ » pour les quinze exactitudes, et c'est ce que porte la colonne. L'arrêt se décide par la règle écrite. Mais une colonne « seuil » qui montre M + 2 σ₀ sous 0,55 se lit mal, A pouvant être au-dessus sans arrêt. **Non exigé** : une colonne de plus porte le seuil d'arrêt (NE-3, § 5), à porter avec l'erratum du commit, ou à laisser au développeur du code v5. À la mère, en routine.
- **Réserve 5 — les lieux laissés tels quels.** Sans suite.
  - L'annexe H, § 1, « Mot de Lazar » et « Ce que cela touche » (l. 901, 903), disent la ligne `GO-2026-11-20-25`, toujours vraie, et la remarque 1 qui les suit dit la précision.
  - La réserve 25 (l. 532), « avec M sous 0,5, c'est l'inverse », reste vraie : sous (ii), le seuil d'arrêt, au plus grand de 0,55 et de M + 2 σ₀, reste sous 0,55 + 2 σ₀ quand M est sous 0,5.
  - La l. 443 dit les points de la version 9 à vérifier ; c'est de l'histoire.
  - La l. 910 (« M + 2 σ₀ de l'exactitude lue ») se lit avec son « telle que le point (1) la laisse » (§ 3).
- **Réserve 6 — la forme de la date.** Non exigé ; le texte est prêt (NE-4, § 5), du même modèle que NE-1. À la mère.
- **Réserve 7 — le statut.** « Brouillon corrigé, à faire contre-lire » est juste pour la v11 rendue. Le texte ne se scelle qu'après l'erratum du commit, qui fait une version de plus. C'est elle qui changera le statut et qui dira ce contrôle fait, à l'alinéa « Version 11 » de « Contre-lecture » et à la ligne de version, qui disent encore « il reste le contrôle du différentiel de la version 10 à la version 11 ». Sans suite pour la v11 ; c'est de la tenue pour la version de l'erratum.
- **Réserves 2 et 4.** Sans suite. « Sans mention » pour une exactitude de forme tenue est ce que dit la lecture voisine « elle est tenue ». Le texte 1 cite `ae64b9d3…`, où R-4182 est bien présente.
- **L'écart du rédacteur**, `git fetch` relancé et `git show` par le commit, va dans le sens de la sûreté. Accepté.

## 5. Textes non exigés (tenue)

Chaque ancien est compté une fois par `grep -c -F -e` dans la v11. Les deux textes s'appliquent ensemble par l'outil sur une copie : « FAIT : 2 remplacement(s) », sortie `073bce65…`, qui est un essai et non une version. Règle des textes : la ligne entière qui suit « Ancien : » ou « Neuf : », hors des accents graves de bord.

- **NE-3** (code v5, point 1, l. 942 ; réserve 3) :
  - Ancien : ` ; la colonne du seuil de la table porte M + 2 σ₀ ; **version 11**`
  - Neuf : ` ; la colonne du seuil de la table porte M + 2 σ₀, et une colonne de plus porte le seuil d'arrêt, le plus grand de 0,55 et de M + 2 σ₀ (contrôle de la version 11) ; **version 11**`
- **NE-4** (l. 6, l'heure de la v11 ; l'heure du journal, relue au journal versé, est 10:47:54Z) :
  - Ancien : `version 11 le 2026-11-20 (`date -u` à 10:45Z en cours de travail ; l'heure exacte est au journal de l'outil)`
  - Neuf : `version 11 le 2026-11-20, à 10:47Z (heure du journal de l'outil : 10:47:54Z ; `date -u` à 10:45Z en cours de travail)`

Ce que je note pour l'erratum du commit, sans texte de ma part : dire ce contrôle fait, avec son chemin, son empreinte et son verdict ; changer le statut.

## 6. À porter

- **À la mère.**
  - Consigner en une ligne la lecture du § 3 : le cas de signalement suit la forme.
  - NE-3 et NE-4, si elle les veut, avec l'erratum du commit.
  - Le statut et la section « Contre-lecture » dans cette même version.
  - Reste aussi à sa main ce que mon contrôle de la v10 lui laissait : relire l'option (a) de la fiche de 08:02:31Z. Cela n'a plus d'objet, puisque Lazar a tranché la remarque 1. Elle a aussi à informer Lazar de la lecture (i).
- **À Lazar** : rien.

## 7. À déclarer

- **Lu en entier** : le rapport du rédacteur de la v11, son mandat et le JSON (les 24 textes neufs).
- **Lu en partie** : la v11. J'ai lu le passage de la section « Seuil » sur les lectures de la forme et du signalement, et la l. 443. J'ai cherché les mots « colonne du seuil », « table de l'étape 3 » et la phrase de la l. 910. Le reste est garanti par l'outil et le rejeu. Les rangs 11, 17, 21, 22 et 24 ont été lus dans le JSON.
- **Écart au message** : j'ai lu `go.md` par le commit d'`origin/main` relevé par `git rev-parse`, et non par le nom `origin/main` au moment du `git show`. C'est le même commit, et c'est plus sûr si la référence bouge.
- Les copies d'essai portent « non-version » dans leur nom. Ce ne sont pas des versions.

## 8. Fichiers de mon dossier

`/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/controle-palier-0b-v10/` :
- ce contrôle, avec son compagnon ;
- `rejeu-v11.md` (`9faf31a3…`), avec son compagnon, son journal et le compagnon du journal ;
- `diff-v10-v11-controleur.diff` ;
- `go-main-d7a08a46.md` ;
- `essai-non-exiges-controleur-sur-v11.json` et `essai-v11-plus-non-exiges-non-version.md` (`073bce65…`), avec les compagnons et le journal écrits par l'outil.

*Contrôleur neuf, modèle O.*
