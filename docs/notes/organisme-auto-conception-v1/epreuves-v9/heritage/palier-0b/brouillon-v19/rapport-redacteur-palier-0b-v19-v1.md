# Rapport du rédacteur — préenregistrement du palier 0b, brouillon v19 (deux corrections de cohérence du contrôle de la v18) — v1

**BROUILLON, EN ATTENTE DU MOT DE LAZAR.** Rien n'est scellé ; la version 13 scellée reste le texte en vigueur ; la version 18 n'est pas touchée. Pièce de travail (classe C). 2026-11-20, journaux de l'outil : 22:32:49Z et 22:33:38Z.

Dossier : `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/redacteur-palier-0b-v19/`. Mandat : `mandat-redacteur-palier-0b-v19-coherence-v1.md` (`11260e2a…`, égal à son compagnon).

## 1. Verdict

La version 19 est la version 18 (`ae1e8f56…`) plus **huit remplacements exacts, en deux passes nommées**. **La sortie de la passe 1 est égale à l'essai du contrôleur (`d54b6e53…`).** Aucune règle n'est changée. Une seule ligne commence par « - Commit du code d'analyse : » (compte : 1) ; le blanc `COMMIT_V6` reste, une seule fois ; aucun groupe de quarante chiffres hexadécimaux dans cette ligne (compte : 0) ; les 64 lignes de la table y sont, et la table reste le premier bloc de code après la ligne du commit (l. 9 à 74). Aucun refus de permission, de classifieur ni de garde.

## 2. Fichiers et empreintes

| fichier | empreinte SHA-256 |
|---|---|
| `preenregistrement-heritage-palier-0b-etage-processeur-v19.md` | `f6bff0c6bd8e9b2f571d2d4e642bb6ed8cd40b502cf2bd96e9bd1376ffd17526` |
| `differentiel-palier-0b-v18-v19-v1.diff` (`diff -u`) | `063f72b78d39b4aa35591302bba8c89e63615e5d8fc1c08fa17ba9d3757b52d0` |
| `remplacements-passe-2-tenue-v1.json` | `e1b04387c6d8a885b102aa436f669aa7468d33e53329097e6b6d990377d50ce5` |
| `passe-1-v18-plus-y1-y2.md` | `d54b6e5312c78b922c50ced5e4b8fcbaefa838b5b937110360cdbfcf3f806a33` |

Chacun a son compagnon ; les deux journaux de l'outil sont au dossier. Pièces reçues, recalculées et égales à leur compagnon : version 18, contrôle (`e2aed461…`), jeu du contrôleur (`88e8b4fa…`).

## 3. Les deux passes

- **Passe 1 — le jeu Y1–Y2 tel quel** : 2 remplacements. Les deux ancres comptées par moi avant l'appel, sur la version 18 : deux fois « 1 ». Sortie `d54b6e53…`, égale à l'essai du contrôleur. Les deux lieux : annexe H, « Version 14 », § 3 (fin) et § 7, remarque 7 ; chacun reçoit un renvoi qui range dans l'histoire la phrase « ce texte ne le fixe pas ».
- **Passe 2 — tenue** : 6 remplacements (titre ; statut et ligne de version ; date ; section « Contre-lecture », deux lieux ; alinéa « Version 19 » de l'annexe H). Chaque ancre comptée à 1 sur la sortie de la passe 1.

**Lieux des trois empreintes entières** (lignes de la version 19), inchangés en nombre :
- programme des étapes 3 à 6, `1f04cb46…` : 2 lieux (l. 107, l. 407) ;
- programme des étapes 6 bis et 7, `ed91813a…` : 2 lieux (l. 107, l. 408) ;
- programme des étapes 8 et 9, `67052a4b…` : 6 lieux (l. 20, 107, 342, 409, 1162, 1224).

## 4. Écarts et limites

- **Les deux renvois portent les mots « Version 18 »**, à la lettre du jeu, alors qu'ils entrent au texte par la version 19. Je n'y ai pas touché ; le statut et l'alinéa « Version 19 » le disent. Si la mère préfère « Version 19 », c'est un remplacement de plus, et la sortie de la passe 1 ne serait plus égale à l'essai du contrôleur.
- L'alinéa « Version 19 » dit, outre le rangement des deux phrases, le compte des remplacements et que rien d'autre ne change ; le mandat le voulait limité au rangement. C'est de la tenue, sans règle.
- Le registre n'a pas été relu pour cette version (le mandat ne le demande pas) : ni `git fetch` ni `git show`. Le texte le dit.
- La date de la ligne de date est celle de `date -u` (22:33Z) ; le journal de la passe 2 dit 22:33:38Z.
- Un `mkdir -p` de mon dossier.
- Aucun lancement d'un programme, du code ni d'un essai ; aucun tirage ; aucune pièce d'autorisation ni de contrôle ; aucun appel à un fournisseur ; aucune dépense ; aucune écriture dans le dépôt.

Signé : rédacteur des v15 à v19, modèle F.
