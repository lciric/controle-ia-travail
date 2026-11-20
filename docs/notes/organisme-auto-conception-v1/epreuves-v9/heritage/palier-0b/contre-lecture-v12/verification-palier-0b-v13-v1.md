# Vérification des corrections — préenregistrement du palier 0b, version 13 — v1

- **Auteur** : contre-lecteur neuf, modèle O, le même que pour la contre-lecture de la version 12 (`palier-0b/contre-lecture-v12/contre-lecture-palier-0b-v12-v1.md`, `b7923cbc6f45b644617e2f0dd60ec780b079e9ff1e03800ee11ab11486e37cc9`). Je n'ai écrit ni la version 13 ni aucune de ses tenues. Pièce de travail (classe C).
- **Date** : 2026-11-20 ; `date -u` lu à 14:27Z en cours de travail.
- **Mandat** : celui de la contre-lecture (`P/mandat-contre-lecteur-palier-0b-v12-v1.md`, `84b76af6…`, en-tête compris), et le message de la session du compte organisme qui demande cette vérification. P = `docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/`.
- **Conditions** : processeur seul ; aucun tirage, aucun lancement du palier, aucune pièce d'autorisation écrite, aucun appel à un fournisseur de modèles, aucune dépense ; aucune écriture dans l'arbre de travail du dépôt, aucun commit ; un `git fetch origin main` (demandé par le message), puis un `git show origin/main:registres/decisions.md` redirigé vers mon dossier ; aucune commande de liste, aucun heredoc, aucun code en ligne. **Aucun refus de permission, de classifieur ni de garde.**

## Verdict

**Conforme, à sceller.** Aucune correction exigée. Deux textes non exigés (NE-2, NE-3 : l'heure de la version 13 et son entrée à la ligne de date), au choix de la mère.

- La version 13 est exactement la version 12, plus mes douze corrections, plus NE-1, plus les quatre remplacements de tenue du rédacteur : les trois passes rejouées sont égales à l'octet aux deux étapes versées et à la version 13.
- R-4292 est citée à la lettre.
- La ligne du commit et sa table ne bougent pas, et le lecteur d'en-tête du verrou, appliqué à une copie de la version 13, lit le commit `e308b84d…` et la table des 58.

## 1. Les trois passes

Empreintes versées égales à leur compagnon : v13 (`d9591d5b…`), son journal, jeu de tenue (`9807e41b…`), différentiel (`95847b5d…`), rapport du rédacteur (`f21f0d57…`), étapes 1 et 2. Mes pièces versées sous `P/contre-lecture-v12/` ont les empreintes que je leur ai données (`b7923cbc…`, `82cf1897…`, `3642b44e…`).

| passe | cible | jeu | sortie rejouée | comparaison |
|---|---|---|---|---|
| 1 | v12 (`a4234028…`) | mes corrections (`82cf1897…`) | `bf6e40d2…` | `cmp` muet avec `etape-1-v12-plus-corrections-non-version.md` |
| 2 | sortie 1 | NE-1 (`3642b44e…`) | `3617d954…` | `cmp` muet avec `etape-2-v12-plus-corrections-et-ne-1-non-version.md` |
| 3 | sortie 2 | tenue du rédacteur (`9807e41b…`) | `d9591d5b…` | `cmp` muet avec la v13 |

Le `diff -u` v12 → v13 que j'ai refait est égal au différentiel versé hors des deux lignes d'en-tête.

## 2. Les quatre remplacements de tenue et R-4292

- **Rang 1** (titre, v12 → v13) : juste.
- **Rang 2** (statut, ligne de version) : juste. Il cite mes pièces par leur chemin versé et leur empreinte, et le verdict « À corriger. ». Il rend fidèlement les douze corrections (neuf pour la décision et la portée 200, deux pour la remarque 3, une pour les champs de B8) et l'ordre de ce qui reste. Une seule réserve, l'heure « vers 14:25Z » (§ 4, remarque 1).
- **Rang 3** (section « Contre-lecture », alinéa « Version 13 ») : juste. Chaque affirmation sur ma contre-lecture est exacte (42 remplacements ; commit et table justes ; lecteur du verrou ; égalité des deux sorties à mes essais).
- **Rang 4** (remarque 5, alinéa « Version 13 ») : juste.
  - R-4292, relue sur `origin/main` après `git fetch` (commit `f880e95d0f097a6b4ad2fa5eab32a9917e729530`, `decisions.md` `2ae2f4900df0dcdba263c37efdca59db78b049bad52eb62bd3e2e97910de9bc2`, l. 4430, 2026-11-20T14:20:58Z). Son texte entre guillemets est compté une fois dans la v13 et une fois dans le registre (`grep -c -F -e`) : **à la lettre**.
  - Le chemin entier du complément et la forme pour les deux pièces sont dits venir de la précision de la mère de 14:21Z, non de la lettre de R-4292, qui abrège le chemin et ne donne le modèle que pour la règle n° 8. C'est exact, et c'est déclaré.
  - Les deux pièces sont absentes sur disque à ces chemins (vérifié par leur chemin) : le texte dit vrai.
- Aucun critère, aucun seuil, aucune valeur gelée, aucune issue ne change.

## 3. La ligne du commit et le verrou

- Une seule ligne commence par « - Commit du code d'analyse : ».
- Le lecteur d'en-tête du verrou (`lire_en_tete_du_texte` du code v5, par `controle_essai_corrige_v1.py`), appliqué à `verif-passe-3.md`, copie égale à l'octet à la v13 : commit `e308b84d68a85416fab1a80b0c116858d24b85a5`, table de 58 entrées égale à `table-empreintes-code-v5.txt`, aucune graine dérivée (`sortie-lecteur-v13-copie-v1.txt`).
- Même lecture sur mon essai avec NE-2 et NE-3 (`03848412…`, `sortie-lecteur-essai-v13-ne-v1.txt`).

## 4. Les remarques du rédacteur

1. **« Vers 14:25Z » contre les journaux.** Les trois journaux disent 14:21:36Z, 14:21:43Z et 14:22:44Z. « Vers 14:25Z » est postérieur aux trois : c'est la forme que NE-4 et NE-1 ont corrigée, une affaire de tenue, sans effet sur une règle. **NE-2** (ci-dessous).
2. **Pas d'entrée « Date (UTC) » pour la v13.** Les versions 10, 11 et 12 en ont une ; l'heure est dite à la ligne de version. C'est de la tenue. **NE-3** (ci-dessous).
3. **C7, « Ce texte n'en fixe ni le chemin ni la forme. », puis l'alinéa « Version 13 ».** Juste ; les deux se lisent ensemble : l'alinéa dit en propres termes que le chemin est fixé depuis, et il donne la forme (« **Forme** : … »). Rien à corriger.
4. **La forme pour les deux pièces.** Juste et déclarée (§ 2). Point pour la mère (§ 6, point 2).
5. **Pas de section « Version 13 » à l'annexe H.** Juste : les versions 10 et 11, qui n'étaient elles aussi que des corrections et des tenues, n'en ont pas ; la ligne de version et la section « Contre-lecture » disent la version 13. Rien à corriger.

## 5. Textes non exigés (tenue)

Chaque ancien est compté une fois par `grep -c -F -e` dans la v13. Les deux s'appliquent ensemble par l'outil sur une copie : « FAIT : 2 remplacement(s) », sortie `03848412ed2fb149de78640014ddc23a253cff36763acf6ac418686dc81bd247`, un essai et non une version. Jeu : `textes-non-exiges-palier-0b-v13-v1.json`. Règle des textes : la ligne entière qui suit « Ancien : » ou « Neuf : », hors des accents graves de bord ; `verifier_textes_v1.py` (pièce de la contre-lecture) les tient égaux au jeu et compte chaque ancien une fois dans la v13 (`sortie-verifier-textes-v13-v1.txt`, où « v12 » est le nom du paramètre : le fichier lu est la v13).

- **NE-2** — ligne de version, l'heure de la version 13.
  - Ancien : `Cette version 13 est produite le 2026-11-20, vers 14:25Z (`date -u` à 14:21Z en cours de travail ; les heures exactes sont aux trois journaux de l'outil),`
  - Neuf : `Cette version 13 est produite le 2026-11-20, de 14:21Z à 14:22Z (heures des trois journaux de l'outil : 14:21:36Z, 14:21:43Z et 14:22:44Z ; `date -u` à 14:21Z en cours de travail),`
- **NE-3** — ligne de date (l. 6), entrée de la version 13.
  - Ancien : `pour le rapport du développeur du code v5 —, que le mandat de la version 12 demande.`
  - Neuf : `pour le rapport du développeur du code v5 —, que le mandat de la version 12 demande ; version 13 le 2026-11-20, à 14:22Z (heure du journal de l'outil : 14:22:44Z ; `date -u` à 14:21Z en cours de travail), dans les mêmes conditions, avec un `git fetch` de `main` et un `git show` redirigé vers le dossier du rédacteur, pour relire la décision R-4292.`

Les heures de 14:21:36Z et 14:21:43Z sont lues aux journaux des deux étapes, dans le dossier du rédacteur ; ces deux journaux ne sont pas versés sous P (§ 6, point 3).

## 6. Pour la mère

1. **Sceller la v13 telle quelle**, ou après NE-2 et NE-3. Dans ce second cas, c'est une version de plus, au nom neuf (R12), sans nouvelle contre-lecture de fond : un rejeu suffit. Recommandation : sceller la v13 telle quelle, et garder NE-2 et NE-3 pour la prochaine version, s'il y en a une. Confiance moyenne à haute.
2. **La forme des deux pièces** (« une table, point par point, l'attendu et le constaté ») n'est dans la lettre de R-4292 que pour la règle n° 8. Elle vient pour les deux de ta précision de 14:21Z, que le texte cite comme telle. Recommandation : une ligne de registre qui la consigne, avant d'écrire la pièce de contrôle. Confiance moyenne.
3. **Journaux des deux étapes** : la v13 dit les trois journaux « à verser avec ce texte » ; sous P, seul celui de la v13 est versé. Les deux autres sont dans `scratchpad/redacteur-palier-0b-v13/`. Recommandation : les verser avec la v13. Confiance élevée.

## 7. Écarts et gestes

- Un `git fetch origin main` : il met à jour la référence distante du dépôt local (`origin/main` passe de `3bd027df…` à `f880e95d…`), sans toucher l'arbre de travail. Il était demandé par le message.
- Le lecteur d'en-tête a d'abord été lancé, par mégarde, sur la v13 du dossier P, en lecture seule (`sortie-lecteur-v13-v1.txt`), et non sur une copie comme le veut le mandat ; il a été relancé sur la copie égale à l'octet (`sortie-lecteur-v13-copie-v1.txt`). Le résultat est identique ; c'est la sortie sur la copie qui fait foi.
- Lancés : l'outil (trois passes, un essai) ; `controle_essai_corrige_v1.py` (pièce de la contre-lecture, `sha256` au compagnon) ; `deplier_jeu_v1.py`, pour lire le jeu de tenue. `tail -n +3` pour ôter les en-têtes des deux différentiels ; `sed -n`, `grep` sur des fichiers nommés.
- Aucun identifiant de modèle dans cette pièce ni dans mon jeu.

## 8. Fichiers

`/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/contre-lecture-palier-0b-v12/`, avec compagnons : `verification-palier-0b-v13-v1.md` (cette pièce) ; `textes-non-exiges-palier-0b-v13-v1.json` ; `sortie-lecteur-v13-copie-v1.txt` ; `sortie-lecteur-essai-v13-ne-v1.txt` ; `sortie-verifier-textes-v13-v1.txt` (avec `liste-vide.json`, second jeu vide passé à ce programme). Fichiers de travail, non rendus : `verif-passe-1.md`, `verif-passe-2.md`, `verif-passe-3.md` et leurs journaux, `essai-v13-avec-ne.md` et son journal, `diff-v12-v13-rejoue.diff` et les deux différentiels sans en-tête, `tenue-v13-deplie-lecture.txt`, `decisions-main-v13.md`, `sortie-lecteur-v13-v1.txt`.

*Contre-lecteur neuf, modèle O.*
