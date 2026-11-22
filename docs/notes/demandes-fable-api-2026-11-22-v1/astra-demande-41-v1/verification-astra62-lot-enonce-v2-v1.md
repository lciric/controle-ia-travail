# Vérification des corrections du script de lot Astra 6.2 pour un énoncé scellé (v2) — v1 (22 novembre 2026)

Pièce d'instrument (classe B), vérification des corrections par le même contre-lecteur (Opus 5.5), en lecture
seule et sans réseau. Pièces : `astra62_lot_enonce_v2.py` (8cf9183e…ad723093) et `test_astra62_lot_enonce_v2.py`
(bd149c6d…f841620), compagnons conformes. Base : `verification-astra62-lot-enonce-v1.md` (d15de75f…29fd56).
Mutations et sondes faites hors du dépôt, dans le bloc-notes de la session.

## Verdict
CONFORME AVEC RÉSERVES (faibles). Les deux défauts moyens sont corrigés et tenus par des essais. Les défauts f1, f3
et f4 sont corrigés. f5 est corrigé en partie : 4 des 7 gardes sont désormais tenues, 3 ne le sont pas pleinement.
f2 reste ouvert, comme le dit le docstring. Pas de régression.

## Corrections, une par une
- M1, relève liée à la soumission : corrigée. Sous `main`, la relève refuse si `--lot` diffère du `lot_id` de la
  ligne de soumission, ou si l'empreinte de l'énoncé diffère de `enonce_sha256`, avant tout appel au réseau.
  Mutations tuées : contrôle du lot, contrôle de l'énoncé, bloc entier, passage du texte par `main`.
- M2, soumission unique : corrigée. Le témoin `ENONCE.soumis` est ouvert en « x » après les contrôles du GO, de la
  clé et du journal, avant tout appel au réseau. Mutations tuées : rattrapage du refus, mode « w ».
- f1, refus nommés : corrigé pour le compagnon vide, l'énoncé absent, le registre absent, le lot JSON qui n'est pas
  un objet et `IncompleteRead`. Toutes ces mutations sont tuées.
- f3, identifiant manquant : corrigé au téléversement et à la création du lot ; plus rien ne part après un
  téléversement sans identifiant (sonde : un seul appel).
- f4, nom du défaut : corrigé (`defaut-astra62-v1.md`), tenu par un essai.
- f5, gardes sans essai :
  - tenues maintenant : empreinte contre `--empreinte`, clé absente de la sortie standard, lecture du lot non JSON,
    texte fait de blancs, ligne en erreur ou statut 500 ;
  - pas tenues : clé absente de l'erreur standard sur un refus (mutation qui l'y imprime : survit) ; mode « xb » du
    brut (mutation en « wb » : survit, car l'essai prend l'erreur du compagnon, encore en « x ») ; refus des
    redirections (l'essai teste la classe, la mutation qui retire la classe de l'ouvreur survit).
- f2, lots « expired », « failed », « cancelled » : ouvert, déclaré. Journalisé, rien n'est relevé.

## Régressions
Aucune. Les 22 mutations de la v1 reportées sur la v2 : 19 tuées, 3 survivantes (les trois ci-dessus ; en v1 il y
en avait 7). Les 20 sondes de la v1 rejouées : mêmes résultats, sauf les cas corrigés, qui refusent désormais.

## Réserves faibles (nouvelles ou restantes)
1. Le témoin est posé avant le téléversement : un refus sans dépense (plafond dépassé, statut 503) le laisse en
   place et bloque toute reprise (sonde). Ça échoue fermé. Correction : dire dans le docstring que la reprise exige
   de retirer le témoin à la main, en le consignant.
2. Le témoin suit le chemin, pas l'empreinte : une copie de l'énoncé et de son compagnon ailleurs se soumet de
   nouveau (sonde). Il faut le faire exprès. Correction : nommer le témoin par l'empreinte, dans un dossier fixe.
3. `relever` appelé hors de `main` sans `texte_enonce` saute la liaison (défaut `None`). Correction : rendre
   l'argument obligatoire.
4. Traces encore possibles, sans rien envoyer : ligne de sortie JSON qui n'est pas un objet (`AttributeError`, après
   le versement du brut), énoncé non UTF-8 (`UnicodeDecodeError`). Correction : les rattraper en `Refus`.
5. Pas d'essai sur deux lignes de soumission dans un journal (mutation survivante). Le cas est déjà empêché par le
   refus d'un journal présent. Correction : un essai.
6. Les trois gardes de f5 non tenues. Correction : un essai pour chacune (refus avec la clé dans l'environnement et
   lecture de l'erreur standard ; brut écrit deux fois avec un compagnon absent ; `_OUVREUR` contient
   `_SansRedirection`).

## Essais lancés
- `PYTHONPATH=src python -m pytest -q test_astra62_lot_enonce_v2.py` : 34 réussis.
- 37 mutations (22 de la v1 et 15 sur les corrections) : 32 tuées, 5 survivantes (xb, redirection, clé sur
  l'erreur standard, deux lignes de soumission, identifiant manquant à la création du lot, ce dernier tenu seulement
  par le code, pas par un essai).
- 25 sondes sur le code réel, transport factice, aucun appel réseau.
