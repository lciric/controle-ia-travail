# Rapport — premier compte des 94 cartes de la course d'auto-conception v9 — v1

- Écrit par le développeur du compte des cartes, modèle O, le 2026-11-21, sur une tâche de routine accordée par la mère à 08:06Z. Processeur seul, aucune dépense, aucun fournisseur appelé, aucune écriture dans un dépôt, aucun commit.
- **Verdict** : 94 cartes à passeport = 2 exclues + 58 au plancher ou au-dessus (en 13 lignes après fusion) + 34 sous le plancher. Mentions de modules (ligne 99) : 42 pour les tests de mort, 34 pour les témoins plantés, 31 pour les proposeurs. Ces mentions se recouvrent. C'est une borne pour le devis des cartes, pas le compte de la note.

## 1. Pièces lues

Les chemins viennent du plan v3 (`plan-experimentateur-tests-de-mort-course-principale-v3.md`, l. 42 et 43) et de sa table d'empreintes (`table-empreintes-planificateur-v3.md`, l. 30 et 31). Les pièces ont été tirées de `origin/main` après `git fetch origin main` dans `/home/user/controle-ia-travail-organisme`, au commit `ba686c9a2efbb5d3f75aa07208a2ba536c79bcaf` (le même que `FETCH_HEAD`). Chacune a été écrite par `git show` redirigé, avec son compagnon `.sha256`.

| pièce | chemin sur `origin/main` | sha256 calculé | compagnon |
|---|---|---|---|
| proposition des cartes à éprouver | `docs/notes/organisme-auto-conception-v1/course-v2/proposition-cartes-a-eprouver-v9-v1.md` | `a2cd45adf7c49a909ad14be378b75b3233eae198b7f51cc416450f4cd878d856` | conforme |
| lecture descriptive de la course v9 | `docs/notes/organisme-auto-conception-v1/course-v2/lecture-course-v9-v1.md` | `0306adf74d321cfa933e047adff28324092787f870a2bf97bafd9d52bd5ffddb` | conforme |

Lignes lues : proposition l. 1 à 5, 23 à 46 et ses titres ; lecture l. 36 à 45, 95 à 101 et ses titres. Le script vérifie lui-même les deux empreintes avant de compter.

## 2. Comptes

Ils sont rendus par `compter_cartes_v9_depuis_main_v1.py` (sha256 `f20b2bf945b67701bcf2a3e99cdb65123e8dbe09e5547f283006077ec02a1c76`) dans `compte-cartes-v9-depuis-main-v1.json` (sha256 `9515bae3527398bc61016444f00530d664a0085b80072632fd82baee33295e74`). Le script a été joué deux fois et `cmp` ne rend aucune différence ; la seconde sortie, `passe-2.json`, a la même empreinte.

| compte | valeur | source |
|---|---|---|
| cartes à passeport | 94 | proposition, l. 5 |
| exclues (une au titre de X1, une au titre de X2) | 2 | proposition, l. 25 |
| au plancher ou au-dessus | 58 | proposition, l. 26 |
| lignes après fusion | 13 | proposition, l. 26 ; rangs de table l. 31 à 43 |
| sous le plancher | 34 | proposition, l. 26 |
| cartes rendues = à passeport + retenues | 96 = 94 + 2 | lecture, l. 38 |
| mentions « tests de mort » | 42 | lecture, l. 99 |
| mentions « témoins plantés » | 34 | lecture, l. 99 |
| mentions « proposeurs » | 31 | lecture, l. 99 |

Contrôles, tous vrais : 2 + 58 + 34 = 94 ; « treize » dans le texte = 13 rangs dans la table ; les 94 de la proposition = les 94 à passeport de la lecture ; 94 + 2 = 96. La marque X6 vise les deux cartes retenues, qui ne font pas partie des 94 (proposition, l. 5 et 25).

## 3. Ce que ce compte n'est pas

- **Ce n'est pas le compte de la note.** Une carte peut nommer plusieurs modules. Les trois nombres font 107 et les treize modules de la ligne 99 font 339, plus que 94 dans les deux cas. Ce sont des mentions, pas des cartes, et la ligne 99 dit elle-même qu'« une mention n'est pas un changement ». On ne peut que borner le nombre de cartes qui nomment au moins un des trois modules : au moins 42, au plus min(107, base).
- **Ce n'est pas un classement par barreau.** Aucune des deux pièces ne classe les cartes par barreau.
- **Ce qui ne se déduit pas de ces deux pièces** :
  - la base de la ligne 99 (94 à passeport ou 96 rendues), qui n'y est pas écrite ;
  - le recouvrement réel entre les trois modules ;
  - le nombre de cartes derrière chacune des 13 lignes, sauf les fusions nommées en § 3 de la proposition, que je n'ai pas comptées ;
  - le croisement entre le rang (plancher ou dessous) et le module nommé ;
  - tout rattachement à un barreau.

  Il faudrait les fiches elles-mêmes, que ce compte n'ouvre pas.
- Le JSON ne porte aucun texte de carte, ni titre ni identifiant. Il ne porte que des nombres, des noms de modules tirés de la lecture et des positions.

## 4. Preuve qu'aucune commande n'a touché les archives

Voici toutes les commandes et lectures de cette tâche, dans l'ordre. Aucune ne nomme un chemin sous `archives-reponses-modeles/`, ni ne liste un dossier :

1. `mkdir -p` du dossier de travail ;
2. une recherche des deux préfixes d'empreinte, limitée au dossier `plan-experimentateur-course-principale-v3/` ;
3. `git -C /home/user/controle-ia-travail-organisme fetch origin main`, puis `rev-parse origin/main` et `rev-parse FETCH_HEAD` ;
4. quatre `git show origin/main:<chemin>` redirigés par `>` vers le dossier de travail, sur les deux chemins de § 1 et leurs `.sha256` ;
5. la lecture des deux compagnons et un `sha256sum` des deux pièces copiées ;
6. une recherche de lignes et une lecture par plage dans les deux copies ;
7. l'écriture du script, deux exécutions par `python3 -I` sur les deux copies, puis `cmp` ;
8. un `sha256sum` des sorties et du script, l'écriture de ce rapport et les `sha256sum` compagnons.

Le script n'ouvre que les deux chemins qu'on lui donne en arguments (`open` sur `sys.argv[1]` et `sys.argv[2]`), et le chemin des archives ne figure nulle part dans son texte.

— développeur du compte des cartes, modèle O
