# Contrôle du remplissage du blanc du commit — préenregistrement du palier 0b, version 19 — v1

Contre-lecteur neuf (Opus 5.5, `claude-opus-5-5`), le 21 novembre 2026. Classe B (contrôle d'un remplissage mécanique). Sur processeur, aucun appel, aucune dépense, aucune étape lancée, aucun tirage, aucune graine dérivée.

## Verdict

**Conforme, à sceller.** Le texte à sceller est le brouillon v19, à un seul remplacement près, celui que prescrit la règle ; le commit inscrit est un ancêtre de `origin/main` ; les 64 lignes de la table ont, à ce commit, les empreintes inscrites ; le lecteur d'en-tête du verrou du code v6, pris à ce commit, lit le commit et la table sans refus.

## Pièces

| Pièce | Chemin (sous `docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/`) | Empreinte SHA-256 |
|---|---|---|
| Brouillon v19 | `brouillon-v19/preenregistrement-heritage-palier-0b-etage-processeur-v19.md` | `f6bff0c6bd8e9b2f571d2d4e642bb6ed8cd40b502cf2bd96e9bd1376ffd17526` (égale à l'attendue et à son compagnon) |
| Texte à sceller | `preenregistrement-heritage-palier-0b-etage-processeur-v19.md` | `883b1b2ac89c4d7f691cd8e68529e0952bad470782ce365e4a39b35a10b2e375` (pas encore de compagnon) |
| Règle du remplissage | `brouillon-v14/contre-lecture-v1/contre-lecture-palier-0b-v14-v1.md`, § 6, point 1 | compagnon vérifié (`sha256sum -c` : OK) |
| Table extraite du code v6 | `table-empreintes-code-v6.txt` | `639335b95b46b8f1d2258ba84fdf117bd4061df6cd5b0bf1b3dca85549c62fa3` (celle que le texte inscrit) |

## 1. Différentiel entre le brouillon et le texte à sceller

- `diff` : une seule ligne change, la ligne 7 (la ligne « Commit du code d'analyse »). Rien d'autre.
- L'ancre de départ (`**`COMMIT_V6` — BLANC, À REMPLIR PAR LA MÈRE :`) et la fin (`n'y trouve aucun commit et refuse.`) figurent chacune une fois dans le brouillon ; le passage entre les deux figure une fois.
- J'ai reconstruit le texte attendu par programme : brouillon, passage remplacé par le texte neuf du § 6, point 1, recopié de la contre-lecture de la version 14, `<COMMIT>` remplacé par `8262c442332c9b79c58eb49c651f788c5397a7ef`. Le résultat est **identique à l'octet** au texte à sceller (481 167 caractères ; aucun retour chariot).

## 2. Ancêtre de `main`

- `git fetch origin main` : `origin/main` = `5e0c6f0a58df3e205e71fc6fdef1f0a1b7245739`.
- `git merge-base --is-ancestor 8262c442332c9b79c58eb49c651f788c5397a7ef origin/main` : code de retour 0, c'est donc un ancêtre.
- Le commit `8262c442…` (20 novembre 2026, 22:38:32 UTC) a pour message « Palier 0b : code v6, trois programmes et brouillons v14 à v19 versés sur main (en attente du GO de Lazar) ».

## 3. Les 64 empreintes au commit

- J'ai extrait `palier-0b/code-v6/` du commit `8262c442…` avec `git archive` dans mon bloc-notes (`…/scratchpad/extraction-8262c442/`).
- Le bloc de code qui suit la ligne du commit (lignes 9 à 74 du texte, indentées sous l'item de liste) porte 64 lignes de la forme « empreinte, deux espaces, chemin », sur 64 chemins distincts ; ce bloc est identique à l'octet à la table extraite `table-empreintes-code-v6.txt`.
- `sha256sum -c` lancé dans l'extraction : **64 OK, 0 échec**. Le même contrôle sur le dossier `code-v6/` du disque de la session donne aussi 64 OK.
- Pour information : l'extraction contient 130 fichiers, et la table en nomme 64 (elle exclut le rapport du développeur, que le texte dit exclu). Je n'ai pas inventorié les autres fichiers ; le verrou ne contrôle que les modules sous `src/` (24, tous dans la table).

## 4. Lecteur d'en-tête du verrou du code v6

- Fonction : `lire_en_tete_du_texte` de `code-v6/src/controle_ia/heritage_etage_processeur_v1/graines.py`, dans l'extraction du commit `8262c442…` ; la constante `LIGNE_DU_COMMIT` vaut `"- Commit du code d'analyse : "` (`constantes.py`).
- Appel : `.venv/bin/python -I -B`, avec un script tenu dans un dossier à part, appliqué à une copie du texte à sceller (identique à l'octet, d'après `cmp`). Seule la fonction de lecture d'en-tête a été appelée.
- Résultat : aucun refus. Commit lu : `8262c442332c9b79c58eb49c651f788c5397a7ef`. Table : 64 entrées, égale à la table extraite, dont 24 chemins sous `src/`. Le journal des graines et celui des refus du module restent vides.
- Dans le texte, la ligne de la formule est la seule de son espèce (le lecteur l'exige, et ne refuse pas).

## Remarques, sans effet sur le verdict

1. Le texte à sceller est exclu de Git sur cette machine par `.git/info/exclude` (ligne 7) : il n'est ni suivi ni versé. Je suppose que la mère l'a voulu ainsi en attendant le GO. Pour qu'il entre sur `main` au scellement, il faudra retirer cette exclusion ou ajouter le fichier de force.
2. La phrase neuve dit que le lecteur d'en-tête a été « appliqué à une copie du brouillon au commit factice » (contre-lecture de la version 14). Le présent contrôle l'a aussi appliqué au texte rempli, au commit réel.
3. Lazar doit encore donner son mot (§ 6, point 2, de la contre-lecture de la version 14) : le GO nomme l'empreinte du texte scellé, `883b1b2a…` si le texte est scellé tel quel.
