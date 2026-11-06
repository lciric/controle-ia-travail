# Contre-lecture neuve (R2) du préenregistrement « agrégateurs sur les scores réels de R1 v4 » — vérification du delta : brouillon 4 et code `1fcb23d7` — v1

**Verdict : scellable.** Aucun couple résiduel. Le brouillon 4 remplace le brouillon 3 : le rapport sur le brouillon 3 (`…-brouillon3.md`) et son couple résiduel sont **sans objet**, puisque mon couple 9 y est appliqué tel quel. La réserve Q3 reste une note, non bloquante.

- Lecteur : fille 9 (lignée Claude Opus 5.5, même modèle que l'autrice). 6 novembre 2026, de 12:43 à 12:43 UTC (`date -u`). Aucune sortie de R1 ou R2 lue ; rien sous `runs/`, `diag/`, `donnees/`.
- Pièces : branche `prep/fille-11-agregation-v1` à `f8dce0df`. Empreintes recalculées et égales : brouillon 4 `32620a86…`, couples d'auteur A18 à A23 `e4d52f93…`, rapport `101678ad…` ; `src/` et `tests/` identiques à `1fcb23d7` (`git diff` vide).

## 1. Brouillon 4 = brouillon 2 + mes 12 couples + A18 à A23

- Rejoué par script : chaque « ancien » est unique au moment où il s'applique.
- Ordre d'application : sur le brouillon 2 (`fb2c93ef…`), mes 12 couples (`eb8ff666…`), puis A18 à A23.
- Résultat : **égal à l'octet** au brouillon 4, à la seule ligne 1 près (« brouillon 2 » → « brouillon 4 »), écart déclaré par A19.
- Les fichiers de contre-lecture que cite A19 (`main` à `efe257ac`, ancêtre de `origin/main` `df9f830b`) ont les empreintes de mes rendus : `39cf2b3e…`, `8e663471…`, `eb8ff666…`.
- `controle_ia.prereg.problemes` ne rend que les deux lignes attendues d'un brouillon (entrée de contre-lecture, marqueur `<<CONTRE_LECTURE_1>>`).

## 2. Couples A18 à A23 : justes et bornés au code v3

- **A18** : commit `1fcb23d7`, commande `analyse_v3` — **juste**.
- **A19** : provenance de la contre-lecture, composition du texte, titre, remplacement du brouillon 3 — **juste**.
- **A20** : recette de W, celle d'`analyse_v2` (Q5) — **juste** ; le code de W est inchangé (vu au diff v2 → v3).
- **A21** : commande décisive et liste fermée de 16 modules plus essais et simulation, soit 21 lignes — **juste**. Les 21 empreintes de la table sont égales aux fichiers (`sha256sum -c`). L'ordre des gardes est celui de `main` dans `analyse_v3` : chemin, scellement, second passage, liste fermée, entrées.
- **A22** : règle du plafond rattachée à `lire_hag` (0,999 → « non interprétable (plafond ou fuite) » ; 0,95 → « appuyée à m = 1 seulement ») — **juste**. Elle concorde avec « Ce que ces gardes impliquent » (l. 165) et avec `PLAFOND`, `PLAFOND_FUITE` du code.
- **A23** : liste d'arrêt — **juste**. Elle comporte Q2 et le scellement, Q4 (code 3, nœud), Q1, Q3 et l'arbre propre, chacun au moment où le code arrête.
- Aucun de ces couples ne touche les hypothèses, prédictions, seuils ni critères de lecture.

## 3. Code v3

Inchangé depuis ma vérification sur le brouillon 3 (`…-brouillon3.md`, section 2) : **41 passed** en 67,01 s.

- Q1 à Q4 faits.
- Artefacts R5 éprouvés, chacun avec son cas sain : « non scellé », « arbre sale », second passage, liste fermée altérée, empreinte de `scores-p3.npz`, compagnon faux, noms, plafond.
- **Réserve Q3 (note)** : l'égalité au compagnon `.sha256` versé avec le fichier prouve l'intégrité depuis la réception, pas l'identité avec ce que la réception a consigné. Option : recopier les deux empreintes dans le texte avant scellement et les exiger. Le lecteur ne les a pas lues.
