# Contrôle du brouillon de la version 15 — préenregistrement du palier 0b — v1

**BROUILLON EN ATTENTE DU MOT DE LAZAR : rien n'est scellé ; la version 13 scellée reste le texte en vigueur.**

- **Auteur.** Contre-lecteur neuf, modèle O, celui de la version 14 (`palier-0b/brouillon-v14/contre-lecture-v1/contre-lecture-palier-0b-v14-v1.md`, `c8ca85f5…`). Je n'ai écrit aucune version du texte ni aucun code. Pièce de travail (classe C), 2026-11-20.
- **Mandat.** Celui de la contre-lecture (`84b76af6…`, en-tête compris), et le message de la session du compte organisme qui demande ce contrôle (analyse statique).
- **Conditions.**
  - Ce que j'ai fait : un `git fetch origin main`, un `git show origin/main:registres/decisions.md` redirigé vers mon dossier, et l'outil de remplacement sur des copies.
  - Ce que je n'ai pas fait : aucun lancement du code, aucun tirage, aucune pièce d'autorisation, aucun appel à un fournisseur, aucune dépense, aucune écriture dans l'arbre de travail du dépôt.
  - **Aucun refus de permission, de classifieur ni de garde.**

## Verdict

**Conforme (brouillon), à sceller après le mot de Lazar.** Aucune correction, aucun texte non exigé.

## 1. Les passes

- **Empreintes.** Les fichiers versés sous `brouillon-v15/` sont égaux à leur compagnon : v15 (`33b04ff4…`), différentiel (`623fd1bf…`), jeux des passes 3 (`f4966bd3…`) et 4 (`c71f92d4…`), rapport (`689e9921…`), passes 1 à 3.
- **Passes 1 et 2.**
  - `passe-1-v14-plus-c1-c2.md` est égale à l'octet à mon essai `2c36dadb…` (`cmp` muet).
  - `passe-2-plus-n1-n4.md` est égale à l'octet à mon essai `d670fd4c…` (`cmp` muet).
- **Passes 3 et 4, rejouées par l'outil sur ma copie de la passe 2.**
  - Passe 3 : « FAIT : 5 remplacement(s) », sortie `11e079c5…`, égale à la passe 3 versée.
  - Passe 4 : « FAIT : 1 remplacement(s) », sortie `33b04ff46d20a55051236d385c38e5e8fd30e7b3d969bd5d46a54a13b62b842f`.
  - `cmp` avec la v15 : muet.
- **Journaux versés** : 18:09:04Z, 18:09:13Z, 18:10:44Z, 18:10:56Z.

## 2. Lieux de la tenue (passes 3 et 4)

Programme `lieux_v1.py` ; sorties `sortie-lieux-passe-3-v1.txt` et `sortie-lieux-passe-4-v1.txt`. Chaque ancre est trouvée une fois.

| remplacement | lieu |
|---|---|
| passe 3, rang 1 | titre (l. 1) |
| passe 3, rang 2 | statut et ligne de version (l. 3) |
| passe 3, rang 3 | section « Contre-lecture », alinéa « Version 15 » (l. 446) |
| passe 3, rang 4 | annexe H, « Version 14 », § 7, remarque 9, ajoutée après la remarque 8 (l. 1092) |
| passe 3, rang 5 | fin du texte, alinéa « Version 15 » (l. 1098) |
| passe 4 | ligne de date (l. 6) |

Les autres lignes que le différentiel v14 → v15 retire (l. 3, 6, 7, 396, 446, 1086) sont celles de C1, C2 et N1 à N4. **Rien d'autre n'est touché.**

## 3. Contenu

- **R-4333 est citée à la lettre.**
  - Relue sur `origin/main` après `git fetch` : commit `35c78ea75e6a81084ef941f634bd7679c328330e`, `decisions.md` `d1468f50…`, l. 4471, 2026-11-20T18:08:29Z.
  - Le texte entre guillemets de la remarque 9 est compté une fois dans la v15 (`grep -c -F -e`).
  - Le commit et l'empreinte du registre que la v15 inscrit sont ceux que je relève.
- **Ligne du commit et table** (sortie `sortie-entete-v15-v1.txt`, sur la copie égale à la v15) :
  - une seule ligne commence par « - Commit du code d'analyse : » ;
  - `COMMIT_V6` figure une fois ;
  - aucun `` `<40 hex>` `` dans la ligne ;
  - le bloc qui suit a 64 lignes et est égal à l'octet à `table-empreintes-code-v6.txt`. La table est intacte.
- **Remarque 9.**
  - Elle porte la règle de R-4333 en remarque, sans toucher la liste d'arrêt.
  - Elle dit ce que la règle ferme (les étapes 3 à 7 jouées sous la v13 et le code v5) et ce qu'elle laisse (la ligne de la pièce de contrôle ; le programme des étapes 6 bis et 7, qui refera la ligne du commit s'il entre au paquet).
  - Elle renvoie les deux points pour Lazar aux remarques 2 et 3.
  - Fidèle à R-4333 et à ma contre-lecture (§ 4 ; § 6, point 4).
- **Statut, ligne de version, « Contre-lecture », alinéa « Version 15 ».**
  - Ce qu'ils disent de ma contre-lecture est exact : verdict, deux corrections, quatre textes non exigés, sept points, 33 remplacements, table égale au § 12, lecteur du verrou éprouvé.
  - Le reste est juste : rien n'est scellé, la v13 reste en vigueur, les critères, valeurs gelées, seuils, graines et la table ne changent pas.
  - Les chemins `palier-0b/brouillon-v14/contre-lecture-v1/…` de mes trois pièces existent, avec les empreintes citées.

## 4. Écarts du rédacteur

1. **La ligne de date porte les heures des trois premiers appels, le quatrième seulement à son journal.** Juste. La ligne ne peut porter l'heure de l'appel qui l'écrit. « À 18:10Z » est exact : le quatrième journal dit 18:10:56Z. Sans suite.
2. **N1 à N4 portés sans en lire les cibles.** Le rédacteur le déclare, et le texte le dit. Leurs cibles, je les ai lues :
   - la mesure de l'étape 8 (`216e2309…`) ;
   - la vérification de la v13 (`2f52cc4f…`, sur disque à `palier-0b/contre-lecture-v12/`) ;
   - les journaux de la v13 (14:21:36Z, 14:21:43Z, 14:22:44Z).

   Sans suite.
3. **Chemin `palier-0b/brouillon-v14/` déduit.** Contrôlé : la v14 y est, `840400f3968095934c93b91fb6e3f8c8001953541b4df4f5546da4953af9ae4a`. Sans suite.

## 5. Ce qui reste ouvert (rappel, rien de ce texte)

- Le remplissage du blanc : le texte proposé est au § 6, point 1, de ma contre-lecture de la v14. Reste aussi la question « un mot ou deux de Lazar ».
- Le programme des étapes 6 bis et 7 que R-4333 veut écrit et vérifié avant le GO. S'il entre au paquet, la ligne du commit et sa table se refont, et il faudra un texte de plus.
- Pour Lazar : l'écart de la mesure de l'étape 8 à l'annexe C, et l'agrégation de l'enrichissement.

## 6. Fichiers

Dossier : `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/contre-lecture-palier-0b-v12/v15/`.

- **Rendus, avec compagnon** : cette pièce ; `sortie-lieux-passe-3-v1.txt` ; `sortie-lieux-passe-4-v1.txt` ; `sortie-entete-v15-v1.txt`. Les programmes employés sont ceux de la contre-lecture de la v14 (`v14/lieux_v1.py`, `v14/entete_essais_v1.py`, scellés là).
- **Fichiers de travail, non rendus** : `rejeu-passe-3.md`, `rejeu-passe-4.md` et leurs journaux ; `passe-3-deplie.txt`, `passe-4-deplie.txt` ; `decisions-main.md` (copie du registre, qui porte des noms de modèle).

*Contre-lecteur neuf, modèle O.*
