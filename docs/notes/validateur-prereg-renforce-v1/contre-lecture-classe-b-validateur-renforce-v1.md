# Contre-lecture de classe B — validateur renforcé des préenregistrements (v1)

- **Relecteur** : Claude Sonnet 5.5, agent neuf, n'a pas écrit la pièce (écrite par Opus 5.5). Contre-lecture à froid, aucun fichier du dépôt modifié.
- **Pièce lue** : `src/controle_ia/prereg_renforce_v1.py` (`22577cab46e8c508024513f1304bdd7f26119c383a1ffcb61301b2f2ae35ea0d`), `tests/test_prereg_renforce_v1.py` (`735978a141641cd7985b5ddcdf7b524d13bceed32b041e0368882be7a8071c0c`), `docs/notes/validateur-prereg-renforce-v1/rapport-validateur-renforce-v1.md` (`7e40d8bfb8ebe96e2883876ec71d4fef6e1d2614bf413c2798f836e3f63d352d`) ; lus aussi `prereg.py`, `test_prereg.py`, le rendu du lecteur B (§ 1) et son script de mutations.
- **Garde de lecture respectée** : je n'ai ouvert, haché ni listé le contenu d'aucun fichier gardé ; mes essais tournent dans de faux dépôts sous le dossier de travail, et sur le dépôt réel j'ai posé un crochet d'audit sur `open` (voir la remarque 2) qui n'a enregistré aucune ouverture gardée.
- **Dossier des essais** : `/tmp/claude-0/-home-user-controle-ia-travail/9ac2612f-0076-57d6-b52f-57d24a4c6967/scratchpad/contre-lecture-validateur-renforce-v1/` (scripts `t1.py` à `t10.py`, `mut/run.py`, `proto_appariement*.py`, `pkg2/` = correctif de la garde essayé).

## Verdict : À CORRIGER

Le contrôle fait ce qu'il promet sur les cas de l'énoncé : j'ai rejoué le témoin du lecteur B, 7 mutations sur 13 sont vues au lieu de 2 sur chacun des deux brouillons (`t6.py`), et les 66 essais passent (`PYTHONPATH=src python -m pytest -q tests/test_prereg_renforce_v1.py tests/test_prereg.py` : 66 réussis). Mais quatre défauts majeurs empêchent de l'appeler prêt :

1. la limite 1 du rapport est réelle et corrigeable à coût faible (remarque 1) ;
2. la garde de lecture, déclarée absolue, est contournée par des liens symboliques et par `..` (remarque 2) et ancrée à la racine passée en paramètre plutôt qu'à celle du dépôt (remarque 3) : j'ai observé l'ouverture d'un fichier gardé dans chacun des trois cas ;
3. une empreinte de 63 ou 65 caractères, ou en majuscules, est ignorée en silence (remarque 4) : c'est la forme la plus courante d'une empreinte inventée par un modèle.

**Remarques : 4 majeures, 9 mineures.**

---

## Remarques majeures

### 1. Majeur — Une empreinte d'un autre fichier passe à côté d'un chemin (limite 1 du rapport) ; correction proposée

**Scénario.** Faux dépôt, `src/a.py` (10 lignes) et `src/b.py` suivis. Le préenregistrement écrit « Le code `src/a.py` (empreinte `<sha256 de b.py>`) fait foi. » Résultat : aucun problème (`t3.py`, cas « L1 mauvais fichier »). Même chose dans une contre-lecture : `` `docs/rapport1.md` (`<sha256 de rapport2.md>`) `` passe (« L1 rapport ↔ autre rapport »). Le validateur de base et (e) acceptent, puisque (e) n'exige qu'**une** empreinte résolue par entrée.

**Cause.** `Index.resoudre(h)` (lignes 161-164) répond « connue ? », jamais « connue pour ce chemin ? ». Les contrôles (a) et (e) (lignes 199-207 et 270) ne regardent aucun chemin.

**Constat d'honnêteté sur le rapport.** Son « exemple réel » (§ 1 (a)) est faux : `3b2e3ee5…` **est** l'empreinte du fichier courant `src/controle_ia/prereg.py` (`sha256sum` : `3b2e3ee56463f30ffd3c549e7fe480fea574c707581bcf30098bf38f4980c306`, la même que celle de la copie archivée sous `docs/notes/echelle-conscience-eval/v6/…/depot/src/controle_ia/prereg.py`, dont le contenu est identique). Il y a donc un autre défaut, voir remarque 10 : `resoudre` renvoie les chemins du compagnon **à la place** de ceux des fichiers suivis (ligne 162-163) et cache le fichier courant. Sur les deux brouillons du 28 novembre, l'appariement strict ci-dessous ne trouve aucun écart : leurs fautes sont des empreintes ou des chemins inventés, que (a) et (c) voyaient déjà. La limite 1 est donc un trou prouvé par essai, pas encore par un cas du dépôt.

**Correction proposée (appariement local, vérifiable).**

*Règle d'appariement.* Une empreinte est appariée à un chemin quand, sur la même ligne (une ligne de table comprise), le texte entre la fin du span `` `chemin[:lignes]` `` et le début de l'empreinte ne contient que des séparateurs `[\s(),;:|—–\-`]`, éventuellement précédés d'un des mots `empreinte`, `sha256`, `SHA-256`, et au plus un accent grave. Règle stricte à dessein : une portée de 40 caractères sans condition apparie à tort « `…couples-v1.json` ; **brouillon 2** (`<hash du brouillon 2>`) » avec le fichier json, et « `manifeste_sha256` `92612ab6…` » placé à côté de `diag/…/tirage.json` (G0, ligne 76 : c'est l'empreinte d'un autre fichier, déclarée telle par son libellé). Les empreintes non appariées gardent le contrôle actuel (« connue du dépôt »), avec un avertissement « empreinte non appariée à un chemin » pour pousser vers la forme `chemin` (`empreinte`).

*Vérification d'une paire (chemin c, empreinte h), dans cet ordre :*
- **B, compagnon** : `c ∈ index.compagnons[h]` (déjà construit ; coût nul, il suffit d'exposer la table). Seule voie pour un fichier gardé (aucune ouverture).
- **A, disque** : `sha256(racine/c) == h`, fichier ordinaire, hors garde, non lien, dans la racine (voir remarque 2). Coût : un hachage en flux par chemin cité, donc borné par les fichiers cités, et on évite l'index complet de `git ls-files` (5,8 s sur le dépôt réel) quand toutes les empreintes sont appariées.
- **C, historique git** : `git log --all --format=%H -- c`, puis `git show <rév>:c | sha256`. À réserver aux échecs de A et B, avec résultat **avertissement** (« version du commit abcd1234 ») et non « ok » silencieux ; plafond de révisions (le chemin le plus modifié a 682 révisions) ; ou, si la ligne cite « au commit X », un seul `git show X:c`. Mesuré : 26 chemins/empreintes en 10 s.

*Ce que ça coûte, mesuré sur les 66 préenregistrements scellés qui passent le validateur de base (`t7.py`, prototype `proto_appariement_ligne.py`) :* 2 538 paires ; 26 écarts dans 12 fichiers ; 24 de ces 26 sont une **ancienne version** du fichier retrouvée dans l'historique (C) ; les 2 autres sont une ligne de table à deux chemins suivis de deux empreintes (`prereg/versant-honnete-jumeau-v3.md`, ligne 45), que l'appariement par adjacence apparie mal : il faut en plus un appariement positionnel quand une ligne a k chemins puis k empreintes, et ne rien apparier si les nombres diffèrent. Sans C, A+B refuseraient donc 24 citations historiques légitimes de pièces scellées ; pour une pièce **neuve**, qui cite des fichiers courants, A+B suffisent.

*Essais à ajouter (R5).* Sain : paire (chemin, empreinte du disque), paire gardée avec compagnon, paire en ligne de table. Artefact : empreinte d'un autre fichier suivi (le cas ci-dessus), empreinte d'une version ancienne (avertissement avec C, problème sans), chemin gardé sans compagnon (aucun hachage). Un mutant « appariement éteint » doit échouer.

### 2. Majeur — Garde de lecture contournée par `..` et par les liens symboliques

La consigne : jamais ouverts ni hachés. J'ai observé trois ouvertures de fichiers gardés, sur de faux dépôts (`t1.py`, `t2.py`) :

a. **`..` dans un chemin cité (contrôle (c)).** `est_garde` (lignes 71-88) ne normalise ni `..` ni `//` ; seul un `./` initial est retiré. Un préenregistrement contenant `` `docs/../src/controle_ia/iib/secret.py:2` `` fait appeler `_nb_lignes` (ligne 247) sur le fichier gardé : le crochet a enregistré `…/docs/../src/controle_ia/iib/secret.py`. Idem avec `brouillons/…/ii-b-saboteur-budget-v1/…`. (`est_garde("docs/../src/controle_ia/iib/a.py")` renvoie `False`.)

b. **Lien symbolique suivi par git.** Un lien `docs/lien.md → ../src/controle_ia/iib/secret.py` est listé par `git ls-files` ; `suivis()` (lignes 150-158) teste la garde sur le nom du lien, puis `p.is_file()` suit le lien et `_hacher` lit le fichier gardé. Même chose avec un lien vers un `.npz`. Aucun lien suivi dans le dépôt réel aujourd'hui (`git ls-files -s | awk '$1==120000'` : vide), mais la garde est dite absolue.

c. **Lien symbolique cité.** `` `docs/lien.md:2` `` → `_nb_lignes` ouvre la cible. Un compagnon `.sha256` qui serait un lien vers un fichier gardé est aussi lu par `_lire_compagnons` (ligne 118).

**Correction (essayée dans `pkg2/`).** (i) `est_garde` : `posixpath.normpath`, motifs de chemin testés à toute profondeur (pour toute tranche de segments), comparaison insensible à la casse ; (ii) une fonction `_sur(chemin, racine)` : refuse un lien symbolique (`is_symlink`), résout `realpath`, refuse hors de la racine, refuse si le chemin résolu est gardé ; l'appeler avant `_hacher`, `_nb_lignes` et la lecture d'un compagnon ; un chemin refusé donne un avertissement, jamais une ouverture. Avec ce correctif, `t1.py` (partie `..`), `t2.py` et `t8.py` n'ouvrent plus rien de gardé et les 56 essais existants passent encore. Coût : négligeable (un `lstat` et un `realpath` par fichier).

**Essais à ajouter.** Un faux dépôt avec lien vers `iib/…`, lien vers `.npz`, chemin cité avec `..`, chemin avec `//` : crochet sur `open` (par exemple `sys.addaudithook`, comme dans `t5.py`) qui échoue si un chemin gardé, ou un lien vers un chemin gardé, est ouvert. Les essais actuels (`test_garde_aucun_fichier_garde_hache`, ligne 355) ne testent que des chemins directs.

### 3. Majeur — La garde est ancrée à la racine passée, pas à celle du dépôt

`est_garde` compare des motifs ancrés (`src/controle_ia/iib`, `brouillons/ii-b-saboteur-budget-*`, …) au chemin **relatif à `racine`** (`Index._rel`, lignes 132-136 et 189).

- **Fichier en dehors de la racine passée** : `cd depot && python -m controle_ia.prereg_renforce_v1 --racine /tmp/autre src/controle_ia/iib/secret.py` : `_rel` renvoie le chemin absolu, `est_garde` ne reconnaît plus `iib`, et `prereg.problemes` ouvre le fichier gardé (`t2.py` : `lus: ['src/controle_ia/iib/secret.py', 'src/controle_ia/iib/secret.py']`, deux lectures).
- **Racine = sous-dossier du dépôt** : `Index("src")` : `git ls-files` rend `controle_ia/iib/secret.py`, la garde ne le reconnaît pas, il est haché (`t8.py` : `racine= src hachés: ['src/controle_ia/iib/secret.py', …]`) ; `Index("brouillons")` hache `ii-b-saboteur-budget-v9/x.md`.
- Même chose pour un préenregistrement donné en relatif depuis un sous-dossier (`cd src && … controle_ia/iib/x.py`, avec `--racine .`).

**Correction.** Motifs sans ancrage de tête (`controle_ia/iib`, `ii-b-saboteur-budget-*`, `g0-criteres-2-3-v1/consignes-privees-*`) testés à toute profondeur, comme dans `pkg2/` : `t8.py` et `t2.py` montrent alors `hachés: ['src/controle_ia/ok.py']`, `gardés sautés: ['controle_ia/iib/secret.py']`, et un refus `GardeArret` pour le fichier hors racine. Surgarde possible d'un dossier homonyme ailleurs : acceptable. Option plus stricte : refuser tout fichier hors de la racine, ou prendre `git rev-parse --show-toplevel` comme base de la garde.

### 4. Majeur — Empreintes de 63 ou 65 caractères, ou en majuscules : ignorées en silence

`HEX64` (ligne 57) ne reconnaît que 64 caractères hexadécimaux minuscules **isolés**. Une chaîne de 63 ou de 65 caractères, ou en majuscules, n'est ni une empreinte (a), ni un préfixe (b) (sans « … »), donc n'est jamais signalée. Essais (`t3.py`, dernier cas : `pb=[]`) :

- vraie empreinte de `src/a.py` amputée d'un caractère (« 63 car ») : acceptée ;
- vraie empreinte plus un `a` (« 65 car ») : acceptée ;
- `'AB'*32` (majuscules, inventée) : acceptée ; vraie empreinte en majuscules : acceptée aussi, sans vérification.

Or une empreinte hexadécimale inventée par un modèle a très souvent une longueur fausse ; c'est le cas d'usage que la pièce vise. Le validateur de base a la même faille, hors des contre-lectures. Le mutant « lookahead de `HEX64` retiré » survit à tous les essais (remarque 13, M01).

**Correction.** Repérer toute suite `[0-9a-fA-F]{32,}` (limites alphanumériques) et la classer : 64 minuscules → (a) ; majuscules → problème « empreinte en majuscules, écrire en minuscules » ou comparaison après `lower()` ; 40 hexadécimaux → avertissement (identifiant de commit probable) ; toute autre longueur ≥ 32 → problème « longueur d'empreinte invalide (63, 65 …) ». Coût : une expression régulière, aucun hachage. Essais : sain (64), artefacts (63, 65, majuscules, 40), mutant du lookahead.

---

## Remarques mineures

### 5. Mineur — Faux positifs de (c) sur des citations légitimes

Rejoués (`t3.py`, un préenregistrement sain où seul le chemin change) : sont signalés « chemin inexistant » : `` `tests/test_x.py::test_y` `` (identifiant pytest), `` `docs/rapport1.md#titre` ``, `` `src/a.py:L3` ``, `` `src/a.py:fonction` ``, `` `src/a.py:3,5` ``, `` `src/a.py:3–5` `` (tiret demi-cadratin), `` `registres/passations/AAAA-MM-JJ-HHMM.md` `` (gabarit de nom, cité dans `CLAUDE.md`). Chemin avec espace : `` `docs/mon dossier/é a.md` `` → `docs/mon` signalé (le rapport a raison qu'aucun fichier suivi n'a d'espace aujourd'hui : `git ls-files | grep -c ' '` = 0). Les virgules ou points inclus dans l'accent grave sont des fautes de l'auteur, c'est correct de les signaler.
**Correction.** Couper avant `::`, `#` ; accepter `:L?\d+(-\d+)?` et `:\d+(,\d+)*` ; accepter `–` ; ignorer un contenu contenant `AAAA`, `JJ`, `XXX`, `NNN` ; pour les noms avec espace, tenter le contenu entier avant le premier mot.

### 6. Mineur — (d) : seuil de 30 mots refuse une contre-lecture saine et brève

`* Contre-lecture 1 : Fable 5.2 neuf, brouillon <hash>, rapport <hash>, verdict prête.` + une seconde entrée équivalente : 21 mots, rejetée « (d) section trop courte : Contre-lecture » (`t4.py`, « CL courte légitime »). Même constat que le rapport : P-041 a des contre-lectures de 23 mots. Une section `Seuil` légitime de 7 mots (« Réfutée si delta < 0,05… ») est refusée aussi ; c'est voulu pour la plupart des sections, mais pas pour `Contre-lecture`, déjà tenue par (e).
**Correction.** Seuil distinct pour `Contre-lecture` (par exemple 12 mots, ou exempter la section puisque (e) l'exige déjà par entrée) ; garder 30 ailleurs ; le paramètre `mots_min` reste. Ajouter un essai « contre-lecture courte et saine ». Faux négatif connu et déclaré : trente mots creux passent ; on peut compter les mots distincts (au moins 15) à coût nul.

### 7. Mineur — (b) : faux positifs sur dates ou numéros ; faux négatifs sur préfixes sans « … »

`20261128…` (huit chiffres suivis de « … ») est signalé comme préfixe inconnu, de même `12345678…` (`t9.py`). Inversement, `` `9f8e7d6c5b4a` `` (préfixe nu), `9f8e7d6c5b..` (deux points) ou `9f8e7d6c5b4a⋯` ne sont pas lus. Commit `9c1f4b1a…` : signalé (limite 3 du rapport).
**Correction.** Ignorer un préfixe entièrement numérique qui ressemble à une date (`(19|20)\d{6}`) ou exiger au moins une lettre `a-f` à partir de 12 caractères ; accepter `..` et `‥` comme marque d'ellipse ; pour les commits, résoudre par `git cat-file -e <préfixe>^{commit}` (un appel par préfixe, quelques millisecondes).

### 8. Mineur — Aucune issue de secours pour une empreinte légitime hors dépôt

Empreintes de poids sur une machine louée, de manifestes de run, de modèles externes : le dépôt ne les contient pas, (a) les refuse, et le rapport reconnaît 135 pièces sur 183 en échec. Le validateur n'offre aucun moyen de les déclarer. Résultat attendu : l'auteur contourne le validateur ou y renonce.
**Correction.** Marque écrite à côté (`hors dépôt`, `externe`, `machine : …`) dans la même ligne : (a) devient un avertissement visible, jamais silencieux ; sans la marque, problème. Une porte d'échappement affaiblit un peu le contrôle (l'auteur peut mentir) mais le rend lisible, et le relecteur voit la liste des avertissements.

### 9. Mineur — Robustesse : plantages, repli silencieux, mémoire

- **Encodage** : un préenregistrement en latin-1 fait planter la ligne de commande avec une trace (`UnicodeDecodeError`, `prereg.problemes` ligne 38, puis ligne 194), et le reste des fichiers n'est pas traité ; fichier absent : `FileNotFoundError` idem (`t4.py`). Un octet d'ordre (BOM) en tête casse la première section (`## Hypothèse` → « section absente »), comme avant ; lire en `utf-8-sig`.
- **Git indisponible** (exécutable absent, propriété douteuse) : `suivis()` renvoie un index vide sans rien dire (lignes 144-145). Les empreintes de fichiers suivis sont alors signalées « aucun fichier du dépôt » sans cause (`t9.py` : message identique). La règle R5 (« aucun repli silencieux ») demande au moins un avertissement « index git indisponible : seuls les compagnons comptent ». Effet seulement du côté des faux positifs, donc mineur.
- **Fichier suivi illisible** (permission) ou retiré entre `ls-files` et le hachage : `_hacher` plante tout l'appel ; `except OSError` par fichier.
- **`_nb_lignes`** (ligne 177) lit tout le fichier en mémoire : 300 Mo en 0,35 s, mais un journal de plusieurs gigaoctets cité avec `:3` épuise la mémoire ; compter en flux par blocs.
- Retours chariot : CRLF correct (lecture en mode texte) ; temps : index du dépôt réel 1,8 s (compagnons) puis 5,8 s (hachage des 22 428 fichiers suivis non gardés), 8,2 s pour un brouillon complet, une seule construction par appel CLI. Les 80 Mo de `*.tar.gz` suivis sont hachés ; les archives `.tar`/`.zip` (107 et 33 fichiers) peuvent contenir des fichiers gardés : question de politique, à trancher (je ne les ouvre pas).

### 10. Mineur — `resoudre` cache le fichier courant derrière le compagnon

`Index.resoudre` (161-164) renvoie `self.compagnons[h]` dès que `h` y figure et n'ajoute jamais `suivis()[h]`. Pour `3b2e3ee5…`, elle renvoie seulement la copie archivée, pas `src/controle_ia/prereg.py` (`t5.py`). Aucun effet sur l'accepté/refusé aujourd'hui ; effet dès qu'on apparie (remarque 1), et sur l'exemple faux du rapport. **Correction.** Renvoyer l'union des deux sources (au prix de construire `suivis()` dès qu'on veut les chemins : ne le faire qu'au moment d'afficher « empreinte du fichier X »).

### 11. Mineur — Limites sémantiques de (a) et (e) à documenter ou fermer

- **Compagnon périmé accepté** : le compagnon de `docs/rapport1.md` porte l'ancien hachage, le fichier a changé sur disque : l'empreinte du compagnon est acceptée (`t4.py`, « compagnon périmé »). Voulu pour les versions historiques, mais à signaler en avertissement si le compagnon ne correspond plus au disque (le test existe déjà dans `verifier-arbre`).
- **Empreinte d'un fichier vide** : `e3b0c442…` est résolue (`src/controle_ia/__init__.py` fait 0 octet) ; une empreinte inventée n'a aucune chance de coïncider, mais le cas du fichier vide vaut un avertissement.
- **Entrée de contre-lecture mal découpée** : une phrase du corps qui commence par « Contre-lecture 2 … » ouvre une entrée (`t4.py`, « CL mal découpée »). Hérité de `prereg.py` ; une puce ou un titre devrait être exigé pour ouvrir une entrée.
- **Modèle nommé** : « pièce écrite par Opus » ou un « fable » commun suffit (`t4.py`, « modèle = auteur », « fable commun ») ; limite 5 du rapport. Proposition bon marché : exiger la forme `Relecteur : <modèle>` dans l'entrée.
- **Pièce neuve non encore commitée ni scellée** : le rapport de contre-lecture cité, tant qu'il est non suivi et sans compagnon, est refusé par (a) (`t9.py`, « untracked » refusé, « tracked » accepté ; empreinte du HEAD d'un fichier modifié refusée). Cohérent avec R6, mais l'ordre d'emploi (sceller le rapport, puis valider) doit figurer au mode d'emploi.

### 12. Mineur — Les essais laissent survivre des contrôles éteints (R5)

Contre 55 mutants du module que j'ai fabriqués (54 modifications ponctuelles, plus un mutant évident de contrôle), joués sur les 56 essais de `tests/test_prereg_renforce_v1.py` copiés hors du dépôt (`mut/run.py`, sortie `mut/sortie.txt`) : le mutant d'identité passe (le banc est donc valide), 32 mutants sont tués dont le mutant évident, **23 survivent** :

| survivant | ce qui n'est pas éprouvé |
|---|---|
| M01 lookahead de `HEX64` retiré, M54 lookbehind retiré | empreinte de 65 caractères, empreinte collée à une lettre (lien avec la remarque 4) |
| M02 repli « compagnon d'une ligne → fichier de même nom » | compagnon dont le nom de ligne ne désigne pas le fichier |
| M03 marqueur binaire `*` de `sha256sum` | forme `hash *nom` |
| M04 exemption de garde des `.sha256` | compagnon de `P3-consignes-v1.md` ou d'un `consignes-privees-*` : la garde ne doit pas les bloquer (non éprouvé) |
| M05 / M06 / M09 garde du préfixe `P3-consignes-v1` par nom, par segment, par `p.name` | chacune est redondante avec les autres (aucun essai sur un **dossier** `P3-consignes-v1-…/x.md`) |
| M08 `.sha256` exclus de l'index des suivis ; M10 `.git` ignoré dans la marche | aucun essai |
| M15, M16, M17, M18 motifs d'ignorance `[`, `$`, `?`, `{` du contrôle (c) | seuls `*`, `…`, `<` sont éprouvés |
| M22 comptage de lignes d'un fichier sans retour final | aucun essai |
| M23 définition d'un mot (contient une lettre ou un chiffre) | aucun essai |
| M28 / M29 mot entier pour le modèle (avant, après) | `Operator`, `GPTq`… non éprouvés |
| M41 préfixe collé à une lettre | aucun essai |
| M43 / M44 racines de chemins `livrables`, `runs` | aucun essai |
| M50 liste `gardes_sautes` ; M51 dédoublonnage de (c) | aucun essai |

Chaque contrôle **entier** éteint est bien tué (M99 et les contrôles (a) à (e) du rapport), donc la couverture est sérieuse au premier niveau ; l'écart est dans les branches fines, dont celles qui servent la garde. Les essais de garde ne couvrent aucun lien, aucun `..`, aucune racine ≠ dépôt, aucune majuscule (remarques 2, 3). Un essai du cas sain existe pour chaque contrôle et un artefact aussi, sauf pour ces branches.

### 13. Mineur — Le rapport

- L'« exemple réel » de la limite 1 est inexact (remarque 1 et 10). Le § 4, point 1, reste vrai ; citer à la place l'essai de `t3.py`.
- « Aucun préfixe ambigu » dans le § 3.2 et « 111 fichiers gardés sautés » sont exacts (`t5.py` : 111 ; 8,2 s) ; les 7 mutations sur 13 sont exactes (`t6.py`).
- Le § 1 dit que les liens ne sont pas traités : ajouter l'avertissement sur la garde (remarques 2 et 3) et sur la longueur des empreintes (remarque 4).

---

## Réponses aux points demandés

1. **Erreurs de logique.** Faux négatifs : remarques 1, 4, 7 (préfixe nu), 11 (compagnon périmé, fichier vide, modèle = auteur). Faux positifs : 5, 6, 7, 8, 11 (ordre d'emploi).
2. **Limite 1.** Remarque 1 : appariement strict (adjacence, ligne ou table), vérification par B (compagnon, zéro coût, seule voie pour un fichier gardé), puis A (disque, un hachage par chemin cité, moins cher que l'index complet), puis C (historique git, avertissement, plafonné, 10 s pour 26 chemins). Sur 66 pièces scellées : 2 538 paires, 26 écarts, 24 résolus par C ; A+B seuls en refuseraient 24 citations historiques légitimes, donc C est à prévoir au moins en avertissement pour les pièces anciennes ; pour une pièce neuve A+B suffisent.
3. **Garde.** Le code n'ouvre aucun fichier gardé en usage normal (crochet d'audit sur le dépôt réel : `durée 8.2 s ; … gardés sautés 111 ; ouvertures gardées: []`, brouillon G0, `t5.py`), mais pas en usage adverse ou mal paramétré : remarques 2 et 3.
4. **Essais.** Remarque 12 : 23 survivants sur 55, aucun contrôle entier éteint ne survit.
5. **Robustesse.** Remarque 9 : encodage latin-1 et fichier absent plantent la ligne de commande ; BOM ; CRLF correct ; git absent silencieux ; grands fichiers (mémoire de `_nb_lignes`) ; majuscules ignorées (remarque 4) ; liens symboliques (remarque 2) ; espaces (remarque 5, aucun fichier du dépôt n'en a) ; temps acceptable (8 s).

## Ce qui est bien

Garde par motifs claire et documentée, compagnons lus sans ouvrir les fichiers gardés, index construit une fois, hachage paresseux (aucun hachage quand tout est résolu par compagnons), messages avec numéros de ligne, sortie de code propre, et un rapport honnête sur ses limites (sauf l'exemple de la remarque 1). Les 66 essais passent ; les 7 mutations sur 13 du lecteur B sont vues.

## Rejouer

```
cd /home/user/controle-ia-travail && PYTHONPATH=src python -m pytest -q tests/test_prereg_renforce_v1.py tests/test_prereg.py   # 66 réussis
D=/tmp/claude-0/-home-user-controle-ia-travail/9ac2612f-0076-57d6-b52f-57d24a4c6967/scratchpad/contre-lecture-validateur-renforce-v1
python3 $D/t1.py ; python3 $D/t2.py ; python3 $D/t8.py        # remarques 2 et 3 (liens, .., racine)
python3 $D/t3.py ; python3 $D/t4.py ; python3 $D/t9.py        # remarques 1, 4, 5, 6, 7, 9, 11
SRCX=$D/pkg2 python3 $D/t8.py                                  # avec le correctif de la garde
(cd /home/user/controle-ia-travail && PYTHONPATH=src python3 $D/t5.py)   # garde sur le dépôt réel
(cd /home/user/controle-ia-travail && PYTHONPATH=src python3 $D/t7.py)   # appariement sur les 66 pièces scellées
```
