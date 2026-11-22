# Journal des lectures du rédacteur successeur des critères de la porte G1 (brouillon 8) — v2

- **Classe C** (note de travail). Suite de la version 1 (`journal-des-lectures-redacteur-g1-brouillon8-v1.md`, `4c4bf6c5ccfbdad89e13f0fb644e83ee7d1a539aded7608dae7302dc0a696a2a`), qui reste valable pour tout ce qu'elle liste, sauf les deux heures corrigées ci-dessous. Cette version ajoute les lectures faites depuis.
- **Session** : `session_013QMaymRJueV6awv1kDtfbP`, fille de la mère `session_013QMayjbmQUdDuDs2S3i3XD`. Modèle : celui que j'ai déclaré à la mère dans mon message d'inscription et qu'elle a inscrit à la version 21 de la liste « qui a lu quoi » ; effort maximal.
- **État** : 22 novembre 2026, 20:54 UTC (`date -u`). Toute suite prendra un nom neuf (R12).
- **Règle tenue** : aveugle aux issues de P3-bis, des étapes B et B bis de T0.7, des barreaux 5 et 6 et de toute course ; aucune recommandation sur le choix de l'énoncé du critère contre le véhicule.
- **Vérification** : la liste ci-dessous a été recoupée avec le journal des appels d'outils de la session (recherche par nom de fichier) pour les pièces copiées mais non ouvertes.

## 1. Erratum à la version 1

1. Section 2, ligne des tests : « second passage lancé à 19:52 » est faux. Le second passage a été lancé entre 19:26 (fin de l'installation de l'environnement, date du fichier de sortie de l'installation) et 19:31 (commit du journal, `dea14636`, 19:31:50 UTC). L'heure de 19:52 n'avait pas été mesurée.
2. En-tête : « État au 22 novembre 2026, 19:55 » est faux. L'état décrit est celui du commit de 19:31:50 UTC.
3. Règle adoptée depuis : aucune heure n'est écrite sans avoir été lue sur `date -u`, sur la date d'un fichier ou sur l'horodatage d'un message.

## 2. Lu depuis la version 1 — décisions, au commit `e8ed1b11ad416c18ad1315a363f22ad127264d4d` de `main`

| pièce | sha256 | étendue |
|---|---|---|
| `docs/decisions/decision-N-074-v1-brouillon1.md` | `bb66b60d03537e41a095c27964039733cc3931a04af23cedfc9dd3ce0e6448b3` | lignes 1-2, 5, 8-11, 13-42, 44-58, 60-70, 72-76 seulement (bornes données par la mère) |
| `docs/decisions/decision-N-076-assurance-par-audit-et-reference-honnete-v1.md` | `49b664c1d6a72fdb239d9a52e70ec85c4829fc5e77c6b5d3cf27848ce1a8dd78` | lignes 1-96 et 318-340 |
| `docs/decisions/decision-N-076-…-v1-erratum-1.md` | `34a59c49436d5239ccf2e8c4df5945a50e54665bae96bf1e32c524a643916484` | en entier |
| `docs/decisions/decision-N-075-issue-plancher-et-deux-regards-v3.md` | `5aed4bab1172b18148c086d90e63611bdd769d9ea7fb4a043e9e9d3178c947b5` | lignes 1-9, 43-60, 112-120, 180-196, 222-226, 232-250 |
| `docs/decisions/decision-N-007-N-008-v1.md` | `ab7dc9bb2c96704ad8fd801197de225f68d6f9720958139f4ec4e32e92105232` | en entier |
| `docs/decisions/decision-N-060-v3.md` | `2b448f696503112c4acebd3d56748e2c9d9931d9e597f1991e3f278e651c5591` | en entier |

Copiées dans le bloc-notes et **jamais ouvertes** (seuls l'empreinte et le nombre de lignes ont été affichés) : les errata 1, 2 et 3 (version 2) de N-075 (débuts d'empreinte `c6efeccfafca4158`, `b19852b47a90e902`, `fbe3298ec358fa9b`) ; N-077 (`41643fc538ff9d6b`) et sa vérification (`2632b4b45df7decf`). Ce que j'en sais vient du rapport du sas sur les décisions tardives. Vues par leur seule empreinte, sans copie : N-068, N-069, N-070, et un erratum 2 de N-076 (7 lignes, `c2943188b4906993`), que je n'ai pas lu et que `CLAUDE.md` ne cite pas.

## 3. Lu depuis la version 1 — pièces du tiers d'extraction

Branche `g1/extraits-tiers-v1`, par chemins exacts seulement, sous `docs/notes/g1-extraits-tiers-v1/` ; lue aux commits `94d6ec0b`, `2cb9959c`, `ab3403ff`, puis à la tête `9133d6dc0f16298ee9c50bfc5d6dda9ef4af5573`. Aucune fiche ni aucun outil de cette branche n'a été ouvert ; la branche de réserve ne l'a pas été.

| pièce | sha256 | étendue |
|---|---|---|
| `reponses-demandes-3-4-5-v6.md` | `a001e65e90ca68941665d6810afaf362966943d7b48127b858c5535975c44860` | en entier |
| `extrait-N-062-v2.md` | `0bfad573507ee7b9c4a3b4f7dd453a7c045931956747d13468e721fb50494143` | en entier |
| `extrait-N-074-brouillon2-v4.md` | `96945dc30cb9aa233ee4da0bc854ee8d2f5022328cb5be70ebcb3bc19115b00f` | en entier |
| `extrait-pari-apparie-conception-v2-v1.md` | `db63b19bd8bc8f79e8306b01720815868bbfba90f7e386ff1f296a56e1456826` | en entier |
| `extrait-validite-adaptateur-v1.md` | `b628c6486abf5756a15a7a716b9d068118e5b3d5e9a466d7b9d6d003d54eec06` | en entier |
| `reponse-demande-7-v3.md` | `0bdb3881168534f047ffc651605c4044229b88eb4f6eda78a51e903ef88d7e4d` | en entier |
| `extrait-calculs-g1-brouillon7-script-v1.md` | `259733485a9c0ccae48b5a9e555c2f244b0dbe7919fddbd62eeaf3754ec5cbc3` | en entier |
| `extrait-calculs-g1-brouillon7-sortie-v1.md` | `67b14a6225c520eaa7f0e77c6e9fe9e74bf5f10d06d3ff54350069dff1556815` | en entier |
| `extrait-G1-brouillon6-v2.md` | `ceca39706f0525d43c94ab0dca29745fd534861eacd0f0932b11de0e55713c15` | en entier |
| `extrait-G1-decisions-en-clair-v2.md` | `a26a04f47e54eeb333735017272adb72e2edd1e0f6306a5a07a77184c2fc2040` | en entier |
| `extrait-calculs-g1-brouillon5-sortie-v1.md` | `4734a898e48e30e39a0b093c138d35ef8d2cd33e6550f96ac0d702975f2f7fa3` | en entier |
| `extrait-T07-sondes-v2.md` | `852cb27403334f450da4afc0cd3123c701d47e05445e13e72d1c51a9d5326287` | en entier |
| `extrait-T06-organismes-v3.md` | `eecc90a6d0911daec5bfabf4075a8200bd294430c824c65f988731d41ca85314` | en entier |
| `extrait-T08-bases-boite-noire-brouillon4-v3.md` | `fe01ace933f0186b3ec3a16f64db4b6ffcdec0414183ad3d4603e0af9b7faa7d` | en entier |

Reçus, copiés dans le bloc-notes, **non ouverts** à l'heure de ce journal : `extrait-T07-etape-B-bis-v2.md` (`46d7b5f622d1f86c04956c709b9bb831025c74b8da0d10838f6451b733a00540`) ; `extrait-calculs-g1-brouillon5-script-v2.md` (`2d946a61ebdd3a69d8a0a4a42ad9b3c37704af10fcd68daaf87530921f40b39a`) ; `extrait-T08-base-A-mots-et-cout-v3.md` (`6d2e7bd2fcaa8971748b4f6e860892a78b8c8500fe97f738b8ba94a380878da3`).

Sources des extraits : jamais ouvertes (brouillon 6 du préenregistrement de la porte, décisions en clair, conception du pari, brouillon 2 de N-074, N-062, textes scellés des organismes et des sondes, brouillon 4 de la base boîte noire, texte de validité de l'adaptateur, calculs des brouillons 5 et 7).

## 4. Messages

Reçus de la mère et du tiers d'extraction, lus en entier à leur arrivée ; envoyés à la mère : la ligne d'inscription, les comptes rendus, seize fiches de décision (une par message), la fiche 2 en version 2 et le complément 1 de la fiche 6. Leur texte est versé dans `noeuds-pour-lazar-brouillon8-v1.md`.

## 5. Expositions déclarées depuis la version 1

7. N-007 et N-008 citent un chiffre de la simulation des agrégateurs d'octobre (le taux de fausses alertes d'un seuil théorique sous effet d'épisode) ; l'extrait de la conception du pari le reprend. C'est une simulation, non une issue interdite ; non recopié dans les fiches.
8. L'extrait du brouillon 6 nomme des lectures que son rédacteur déclare ne pas avoir lues (« runs de la nuit du 1er novembre ») : je n'en connais ni le contenu ni le sens.
9. Le rapport du sas sur les registres dit que des verdicts existent pour les critères 2 et 3 de la porte de fin de phase 0, « sens non rapportés » ; je ne connais le sens d'aucun.
10. Le message de la mère sur la fiche 2 m'apprend qu'un brouillon 14 du texte de la base boîte noire existe et porte une sous-section sur son écart avec le brouillon de la porte ; je n'ai lu que le brouillon 4, par extrait.
11. L'extrait du brouillon 4 de la base boîte noire porte des probabilités de puissance calculées sur des lois binomiales (aucune donnée) ; deux d'entre elles sont recalculées dans mon complément 1.

Rien, dans ce que j'ai lu, ne m'a appris le sens d'une issue de P3-bis, des étapes B et B bis du texte des sondes, des barreaux 5 et 6 ou d'une course.

## 6. Non ouverts (inchangé, complété)

Le brouillon 2 de N-074 ; les huit fichiers du complément de la mère et leurs compagnons ; la note du juge sur l'exposition ; tout verdict ; toute note de lecteur ; `registres/decisions.md` ; `registres/etat.md` ; `registres/rappels.md` ; la liste « qui a lu quoi » ; la ligne GO-2026-11-18-48 ; le coffre ; le bras d'attaque ; les pièces du saboteur ; `docs/verdicts/`, `diag/`, `runs/` ; le journal des commits de `main` (aucun sujet de commit affiché) ; `docs/decisions/` non listé ; `decision-N-062-v1.md` (lu par extrait).

## 7. Routine, suite

- Tests du dépôt : second passage toujours en cours à 20:45 UTC (49 % des tests passés à cette heure, d'après la fin de sa sortie) ; issue à rendre à la mère dès que le fichier du code de sortie existe.
- Aucun défaut échu prononcé, aucune instance inventoriée ni arrêtée (session fille). Aucune dépense.
