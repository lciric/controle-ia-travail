# Rapport du rédacteur — corrections K1 à K24 du préenregistrement court « nouvelles attaques », version 2 — v1

- Auteur : rédacteur neuf, modèle F. Écrit le 2026-11-20 ; relevés de `date -u` : 05:33:20Z après la relecture de `main`, 05:35:27Z avant l'écriture des fichiers de remplacements.
- Mandat : `docs/notes/ideation-nouvelles-attaques-v1/preenregistrement-court-v1/mandat-redacteur-preenregistrement-court-v2-v1.md` (`52906f3590c9783a0beed5504a037f4d8b004e41db91b9fb6a6ac36f1f32f15f`, compagnon : égal).
- Processeur seul. Aucun appel à un fournisseur de modèles, aucune dépense, aucune valeur de clé, aucune écriture dans le dépôt, aucun commit. Réseau : un `git fetch origin main`. **Aucun refus de permission, de classifieur ni de garde.** L'outil de remplacement n'a refusé aucune ancre.

## 1. Verdict

Les vingt-quatre corrections K1 à K24 de la contre-lecture (`a9886437aeac1c8aa38c132efcdbc34f8593588194e48e1d2c0d5b8c9a78999b`) sont appliquées à texte exact, par l'outil contre-lu (`391db990734dd36f7c827b8b6c77dc0de1bda324f671b65748ccfe68c56a53d6`), sur des copies neuves. Les v1 ne sont pas touchées. Les v2 ne contiennent ni méthode d'attaque, ni procédé, ni détail opérant, ni identifiant de modèle.

## 2. Pièces rendues

Dossier D : `/tmp/claude-0/-home-user-controle-ia-travail/227b647d-2ece-5654-bf04-8493b3ed2f19/scratchpad/redacteur-preenregistrement-court-v2/`. Chaque pièce a son compagnon `.sha256`.

| pièce | empreinte |
|---|---|
| `D/preenregistrement-court-course-nouvelles-attaques-v2.md` | `be4e3c4a6966400a801f34a4951226b313e54cd5af9ed37cc041b04fa08223a1` |
| `D/rapport-redacteur-preenregistrement-court-nouvelles-attaques-v2.md` | `e9735e5d60a9eb8bcf1e29b66a7cba1cb3d750fbb3ba0abd45438c9a627d52e6` |
| `D/remplacements-preenregistrement-court-v1-vers-v2-v1.json` (41 remplacements) | dans son compagnon et dans ma réponse |
| `D/remplacements-rapport-redacteur-v1-vers-v2-v1.json` (9 remplacements) | de même |
| les deux journaux de l'outil, `…-v2.md.journal-remplacements-v1.json` | dans leurs compagnons et dans ma réponse |
| `D/differentiel-preenregistrement-court-v1-v2-v1.diff` et `D/differentiel-rapport-redacteur-v1-v2-v1.diff` (`diff -u`) | de même |

Le sous-dossier `D/lectures/` garde trois extraits de registre ; ce ne sont pas des pièces rendues.

## 3. Ce qui a été vérifié

- Empreintes contre compagnons : mandat, contre-lecture, sortie du calcul (`bf423a5e9106b059e76cd50f6a7e3c0f4ac0e8730d4c0b517def0414890a8fdd`), préenregistrement v1 (`0f0d8b9b…`), rapport v1 (`057b3a4c…`) : toutes égales.
- Ancres : comptées par `grep -c -F -e` sur chaque cible avant l'appel (28 et 15 lignes pour le préenregistrement, 10 pour le rapport, comptes attendus) ; l'outil exige de plus que chaque texte ancien figure exactement une fois.
- **`main` relu (K1 à K4, K9)** : commit `8ba3c932490d915dc8fa2d424a6041e694498ec2`. `main` a avancé depuis le commit `0b265f65…` de la contre-lecture.
  - `registres/go.md` : `faa6bd5175a6639a944485b6ab6112b938dabb7e8cbd47fca22e5aa8a31f9a4b`, égale à l'octet à celle de la contre-lecture. GO-2026-11-20-14, -15 et -16 lus.
  - `registres/decisions.md` : `29116cfa43660c3aca5a4a11cb10ccc9e2032848ab66f71a1a34f351caf645c0`. Comparé au commit `0b265f65…` (`8c8bded7…`, recalculée) : seules des lignes s'ajoutent, R-4094 à R-4103 ; les lignes nommées sont inchangées. R-4089 à R-4097 lus.
  - K2 et K3 portent donc le commit et les empreintes relus, comme la contre-lecture le demande.

## 4. Remplacements

Préenregistrement, 41 : le titre ; la ligne « Version » sous « Statut » ; K9 ; K1 à K4 (un chacun) ; K5 (quatre) ; K6 (deux) ; K7 (un bloc) ; K8 (sept) ; K10 (cinq, dont la phrase ajoutée après la table) ; K11 à K13 (un chacun) ; K14 (deux) ; K15 ; K16 (quatre) ; K17 à K21 (un chacun).

Rapport, 9 : le titre ; la ligne « Version » ; K22 (un bloc, puis la phrase de routine) ; K23 ; K24 (quatre).

## 5. La répartition retenue par clé (K7)

X est le besoin du bras A sur Rigaud. Si seul l'essai de mesure compte, X vaut au plus 8,35 USD, sous la bascule de 9,28 USD. La première table s'applique :

| clé | rôles | cas haut | part | rapport part / cas haut |
|---|---|---|---|---|
| Minuit | juge de l'espèce 3 | 105,05 | 162,56 | 1,547 |
| Luc | aiguilleur ; proposeur de l'espèce 4 | 124,35 | 214 | 1,721 |
| Rigaud | proposeur de l'espèce 3 | 26,61 | 47 − X, soit au moins 38,65 | au moins 1,452 |

**Ce qui la ferait basculer** : les lectures du bras A payées sur Rigaud pendant la course. X passerait alors 9,28 USD, ou ne serait pas écrit. La seconde table s'applique dans ce cas : Minuit, juge de l'espèce 3 (1,547) ; Luc, aiguilleur et proposeurs des espèces 3 et 4 (cas haut 150,96, rapport 1,418) ; Rigaud, aucun rôle. Le texte v2 ne fige pas X : la mère l'écrit au complément de valeurs, ou le porte à Lazar (N2).

## 6. Nœuds et points à trancher

- **N2, pour Lazar, sans défaut** (récrit selon K22) : si le besoin du bras A sur Rigaud n'est pas écrit ou passe 9,28 USD, la part Claude de la course se paie-t-elle sur Minuit et Luc seules ? Recommandation de la contre-lecture : (b) si le bras A ne lit pas avant la fin de la course, sinon (a) ; confiance 0,6.
- N1 est tranché (GO-2026-11-20-16) : plus de nœud.
- **K21, pour la mère** : la règle de lecture d'une course arrêtée avant la fin est portée au texte, marquée « à accepter ou refuser par la mère ».
- Pour la mère, en routine : consigner à la ligne d'activation que la condition de GO-2026-11-20-08 est remplacée par GO-2026-11-20-16 (lecture de la contre-lecture) ; écrire X au complément de valeurs.
- Réserve 1 de la contre-lecture, redite : une fiche passée par le portier est servie avant la relecture de la mère. La changer serait un nœud.

## 7. Écarts et réserves

1. **Trois choix de forme, hors de la lettre.** (a) K9 : le crochet est rempli par mon relevé, 05:35:27Z. (b) K10 : la phrase « L'ordre des identifiants… » forme un paragraphe à part, entre la table et « Le tirage est fait… ». (c) K21 : la marque « (Règle proposée par la contre-lecture, correction K21 : à accepter ou refuser par la mère.) » est ajoutée en fin de paragraphe, comme le mandat le demande.
2. **Ligne « Version » du rapport v2** : le rapport v1 n'a pas de ligne « Statut ». La ligne est posée après la ligne « Mandat » ; elle dit aussi que le rapport v2 accompagne le préenregistrement v2.
3. **La répartition retenue n'est pas ajoutée au préenregistrement.** Le texte de K7 la porte déjà en substance (« Si le besoin du bras A se borne à la file de l'essai de mesure…, la première table s'applique »), et K5 (c) laisse X ouvert. Je l'écris ici (§ 5) plutôt que d'ajouter une phrase de fond au texte.
4. **Restes de la v1, non corrigés parce qu'aucune correction K ne les vise** :
   - préenregistrement v2 : la ligne « Statut » dit encore « non contre-lue », et la section « Contre-lecture » dit « Non faite à cette date ». La contre-lecture (§ 2) demande que cette section cite deux empreintes avant le scellement ; c'est à la mère ;
   - rapport v2, § 1, point 1 et § 2 : le nom de fichier v1 et l'ancien dossier ; § 3 : la table des sources cite encore le commit `8cf0d3d1…` et ses deux empreintes ; § 5, point 2 : « écrit nulle part dans ce que j'ai lu », dépassé par K22 ; § 5, point 6 : « ni contre-lu ».
5. Dans le bloc de K7, les trois dernières lignes se suivent sans ligne vide, comme dans la contre-lecture ; le rendu les joint en un paragraphe.
6. Les ancres de plusieurs lignes (K6, K7, K22) ont été comptées par leur première et leur dernière ligne ; l'outil a contrôlé le bloc entier.

— rédacteur neuf, modèle F
