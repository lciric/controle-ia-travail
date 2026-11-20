# Rapport du rédacteur — préenregistrement du palier 0b, brouillon v16 (les programmes de lancement des étapes 3 à 7) — v1

**BROUILLON, EN ATTENTE DU MOT DE LAZAR.** Rien n'est scellé ; la version 13 scellée reste le texte en vigueur ; aucune étape 3 à 9 ne se joue avant un GO de Lazar sur le texte qui la suit (R-4333). Pièce de travail (classe C). 2026-11-20, journaux de l'outil : 21:59:51Z et 22:00:47Z.

Dossier : `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/redacteur-palier-0b-v16/`. Mandat : `mandat-redacteur-palier-0b-v16-programmes-v1.md` (`df49b3b1…`, égal à son compagnon).

## 1. Verdict

La version 16 est la version 15 (`33b04ff4…`) plus **dix-sept remplacements exacts, en deux passes nommées**. Elle porte les trois programmes, les décisions de la mère, la pièce de contrôle, et **un écart pour Lazar, non tranché : la garde 17**. Une seule ligne commence par « - Commit du code d'analyse : » (compte : 1) ; le blanc `COMMIT_V6` reste, une seule fois ; aucun groupe de quarante chiffres hexadécimaux dans cette ligne (compte : 0) ; les 64 lignes de la table y sont, non touchées, et le premier bloc de code après la ligne du commit reste la table. Aucun critère, aucun seuil, aucune valeur gelée, aucun mot de la table de la liste d'arrêt n'est changé. Aucun refus de permission, de classifieur ni de garde.

## 2. Fichiers et empreintes

| fichier | empreinte SHA-256 |
|---|---|
| `preenregistrement-heritage-palier-0b-etage-processeur-v16.md` | `c37bdb2f301f3bd9efa8767f36158006e7b1f58c4b2ab628d96cfa1eaa3bfa0d` |
| `differentiel-palier-0b-v15-v16-v1.diff` (`diff -u`) | `d0d18a1a2f7509d16aab229a423d9f04bfe3df84a3f799422d681d02a23c3fff` |
| `remplacements-passe-1-programmes-et-decisions-v1.json` | `292ad5d808380d2e88a592a9bfbc136752ea008a16574fabe20b45c3f5b5af81` |
| `remplacements-passe-2-tenue-v1.json` | `a61decaa13de686bd8ab2d201d067352649f5fc026d773f763d4ba22879f27aa` |
| `passe-1-v15-plus-programmes-et-decisions.md` (sortie de la passe 1) | `54d20af438490f9107b3198a4dd1751de3ae4186ea5e5e9781f73149c88ad388` |

Chacun a son compagnon ; les deux journaux de l'outil sont au dossier. Les quatorze pièces du mandat ont été recalculées et sont égales à leur compagnon.

## 3. Les remplacements

Chaque ancre comptée par `grep -c -F -e` avant l'appel : dix-sept fois « 1 » sur la version 15 ; les cinq ancres de la passe 2 recomptées sur la sortie de la passe 1, cinq fois « 1 ».

**Passe 1 — programmes et décisions (12).**

| n° | lieu | objet |
|---|---|---|
| 1 | plan d'analyse, avant « Ce qui est rapporté » | sections neuves « Les programmes de lancement des étapes 3 à 9 » et « ÉCART POUR LAZAR » |
| 2 | ordre des opérations, points 3 à 7 | renvoi et résumé |
| 3 | ordre des opérations, point 2 | ce qui est fait, ce qui reste |
| 4 | sous la table de la liste d'arrêt | comment les programmes lisent les points 2, 4, 5, 10 et 11 ; la table n'est pas touchée |
| 5 | annexe C | lieux des programmes et des essais, dossier des sorties |
| 6 | B8, alinéa « Graines » | pièce de contrôle avant l'étape 3 ; champs du verrou non nuls |
| 7, 8 | annexe H, « Version 14 », § 7, remarques 8 et 9 | **les deux lieux** qui disaient qu'aucun programme n'enchaîne les étapes 3 à 7, corrigés |
| 9 | mandats | mandat de la version 16 ; R-4334 à la lettre |
| 10 | documents qui font foi | pièces de la version 16 |
| 11 | fin du texte | annexe H, « Version 16 » : table des lieux, huit remarques, ce qui revient à Lazar, tenue |
| 12 | critères de lecture | renvoi à l'écart, à la phrase sur l'issue « suspendue » |

**Passe 2 — tenue (5)** : titre ; statut et ligne de version ; ligne de date ; section « Contre-lecture », alinéa « Version 16 » ; fichiers à donner et points à vérifier.

**Lieux des trois empreintes entières** (lignes de la version 16) :
- programme des étapes 3 à 6, `1f04cb46…` : 2 lieux (pièces, l. 107 ; table de la section neuve, l. 407) ;
- programme des étapes 6 bis et 7, `ed91813a…` : 2 lieux (l. 107 ; l. 408) ;
- programme des étapes 8 et 9, `67052a4b…` : 5 lieux (table du code v6, l. 20 ; l. 107 ; B8, l. 342 ; l. 409 ; annexe H, « Version 14 », § 3, l. 1150), dont trois hérités de la version 15.

**Phrases « aucun programme » pour les étapes 3 à 7** : deux lieux dans la version 15, tous deux à l'annexe H (« Version 14 », § 7, remarques 8 et 9), corrigés. Le silence n° 10 du programme des étapes 6 bis et 7 n'était écrit dans aucune version du texte ; la section dit qu'il est fermé.

## 4. L'écart pour Lazar : la garde 17

Section visible du plan d'analyse, signalée au statut, sous la liste d'arrêt et aux critères de lecture. Le texte (B2 et critères de lecture, cités à la lettre) admet un étage joué sans la garde 17, à l'issue « suspendue ». Le programme des étapes 3 à 6 exige la copie de l'organisme et refuse avant l'étape 3 si elle manque : le cas « suspendue » devient un arrêt avant tout geste. Deux voies : accepter le rétrécissement, ou demander un programme v3. **Ma recommandation : accepter, confiance moyenne à haute** ; défaut : aucun. Je ne l'ai pas tranché.

## 5. Points où la lettre ne suffit pas — en remarque, aucun tranché

Écrits à l'annexe H (« Version 16 », § 2).

1. La commande du programme des étapes 8 et 9 : aucun rapport ne la donne sous la forme des deux autres ; je l'ai écrite sur l'usage de son en-tête.
2. Ce programme ne lit pas la pièce de contrôle et reçoit son commit de l'appelant : que la pièce porte son empreinte reste un contrôle à la main.
3. Rien ne vérifie par programme qu'un programme a fini sans arrêt avant de lancer le suivant ; après un arrêt au point 5, le fichier des réglages est gelé et relisible.
4. Les libellés fixes de la pièce de contrôle, et le nom sous lequel s'écrit ce qui s'y ajoute entre les lancements : non fixés.
5. Les dossiers des sorties des étapes 6 bis à 9 : seul celui des étapes 3 à 6 est fixé.
6. **Les décisions de 18:29Z et de 18:53Z ne sont inscrites par aucune ligne du registre** que j'aie trouvée sur `origin/main` (commit `7357855b9c531e80e784f3beca7ad659463b5387`) ; seule R-4334 (18:26:23Z) l'est. Elles sont portées sur la foi du mandat.
7. Les champs du verrou non nuls : la phrase de B8 qui les disait nuls n'est pas réécrite, une lecture y est ajoutée ; la vérification ne le constate que pour le manifeste des étapes 6 bis et 7.
8. Ce que je n'ai pas lu : les programmes des étapes 3 à 6 et 6 bis et 7, leurs essais, la vérification des essais de la version 3.

## 6. Gestes et écarts

- Une commande simple par appel ; aucun heredoc, aucun code en ligne ; aucune commande de liste ; les JSON écrits par l'outil d'écriture (trois retouches par l'outil d'édition avant les appels).
- Un `mkdir -p` de mon dossier ; un `git fetch origin main`, un `git show` redirigé, un `git rev-parse` ; des `grep -n -o` sur la version 15, par son chemin, pour trouver les phrases à corriger et les deux citations de la garde 17.
- Aucun lancement d'un programme, du code ni d'un essai ; aucun tirage ; aucune pièce d'autorisation ni de contrôle ; aucun appel à un fournisseur ; aucune dépense ; aucune écriture dans le dépôt ; rien sous `archives-reponses-modeles/` ni `/root/.claude/`.
- La date de la ligne de date est celle de `date -u` (22:00Z) ; le journal de la passe 2 dit 22:00:47Z.
- **À ne pas verser** : `decisions-origin-main.md`, copie de lecture du registre, qui porte des noms de modèle.

Signé : rédacteur de la v15 et de la v16, modèle F.
