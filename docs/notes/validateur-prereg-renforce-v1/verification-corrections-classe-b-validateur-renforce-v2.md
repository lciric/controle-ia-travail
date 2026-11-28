# Vérification du second lot de corrections (N1 à N4) — validateur renforcé v2

Relecteur : Claude Sonnet 5.5 (le même que pour les deux passes précédentes). Pièces : `src/controle_ia/prereg_renforce_v2.py` (`a8feddbfab57ccee…`), `tests/test_prereg_renforce_v2.py` (`8003a95d9cf8c5d5…`, 181 essais), erratum 2 (`bbe9514aecdea9f7…`). Aucun fichier gardé ouvert par moi, aucun fichier du dépôt modifié. Essais et scripts : dossier `…/scratchpad/contre-lecture-validateur-renforce-v1/` (`w1.py`, `w2.py`, `v1.py` à `v7.py`, `mut3/`, `pkg6/` = module vérifié).

## Verdict : PRÊT

Les quatre défauts sont levés, sans régression. Rejeu : `PYTHONPATH=src python -m pytest -q tests/test_prereg_renforce_v2.py tests/test_prereg*.py` : **247 réussis**.

## N1 (majeur, garde) — levé

- **Attaque refaite** (`w1.py`) : faux dépôt avec `src/controle_ia/iib/secret.py` et `data.npz` (puis supprimés, historique conservé), un dossier `gone/` disparu contenant un `.npz`, une empreinte écrite à côté de `src/controle_ia`, `src/controle_ia/`, `src/controle_ia/iib`, `gone`, `src`, plus un commit cité (arbre). Espion sur `Index._git` pour **tout** `cat-file` (`--batch` et `--batch-check`) : **aucun appel, aucun identifiant d'objet gardé envoyé** dans les cinq cas. Rejeu de mon cas d'origine (`v2.py`, dossier existant avec `iib/` et `.npz`) : `total oids: 0`.
- **Correction lue** (diff avec la version précédente) : filtre du journal sur le chemin cité exact, refus d'un dossier existant ou gardé dans `historique`, pas d'appariement à un dossier, `cat-file --batch-check` avant `--batch` avec alignement par objet. Le défaut de lecture des arbres est corrigé.
- **Non-régression** : une vraie version ancienne d'un fichier reste retrouvée (« version ancienne… commit c335962f… », aucun problème).
- **Mutants** (`mut3/sortie.txt`) : filtre retiré, filtre réduit à la garde, appariement à un dossier permis, refus de dossier dans `historique`, `--batch-check` retiré : **5 tués sur 5**. Seul survit « garde par chemin relatif au dépôt retirée » (équivalent, doublé par la garde du chemin cité, comme dit dans l'erratum).
- **Affirmation du développeur** vérifiée : je lis les noms seulement de l'historique des trois dossiers cités (`git log --name-only`) : 3, 14 et 2 fichiers, **aucun gardé** (`est_garde` faux partout). Donc aucun objet gardé n'avait été haché par ses relevés antérieurs ; je la tiens pour exacte.

## N2 (mineur, entrées de contre-lecture) — levé

`w2.py` : entrée 2 sans modèle détectée (problème « contre-lecture 2 sans le modèle ») pour ligne nue avec « : », avec « — », avec « (R2) : », liste `1.` et ligne de table ; la phrase de prose (« Contre-lecture 2 reprise après corrections ; ») n'ouvre toujours pas d'entrée. Sur le dépôt réel, les trois pièces (`addendum-1-gardes-analyses-r1-v4-v1`, `agregation-r1-v4-v1`, `audit-fuite-r1-v4-v1`) sont découpées comme par le validateur de base (2, 1, 1 entrées). Mutants : ligne nue, liste numérotée, table : tués.

## N3 (mineur, résidu de la limite 1) — levé en partie, comme annoncé

« `src/a.py` signature `<empreinte de autre.py>` » donne maintenant « empreinte non appariée qui désigne src/autre.py, pas un chemin cité sur sa ligne » (avertissement, pas problème) ; « empreinte `…` du fichier `src/autre.py` » : rien ; ligne sans chemin : rien. C'est la limite documentée (l'empreinte n'est pas vérifiée pour un chemin), acceptable. Réserve non bloquante : l'avertissement bruyant (489 sur les 183 pièces scellées) se déclenche aussi sur la forme légitime « brouillon relu `<hash>` ; rapport `chemin` ». Mutant : tué.

## N4 (mineur, archives) — levé

`v7.py` : archive `docs/avec.zip` avec compagnon et empreinte fausse : **problème** « différente de celle de son compagnon » ; archive sans compagnon : avertissement ; empreinte nue : problème ; archives non ouvertes et listées dans `gardes_sautes` (`v4.py`). Mutant : tué.

## Régressions

Aucune. Rejoués avec le module corrigé : les trois ouvertures gardées de la première contre-lecture (`..`, lien suivi, lien cité) et le compagnon lien (zéro ouverture), racines décalées, préenregistrement hors racine ou lien (refus), dossier-lien, 63/65/majuscules, appariement de `b.py` à côté de `src/a.py`, pièce saine sans avertissement (`v5.py`). Sans objection restante sur la garde.
