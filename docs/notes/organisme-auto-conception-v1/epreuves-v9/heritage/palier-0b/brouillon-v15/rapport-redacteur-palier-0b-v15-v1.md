# Rapport du rédacteur — préenregistrement du palier 0b, version 15 (corrections de la contre-lecture de la version 14) — v1

**BROUILLON, EN ATTENTE DU MOT DE LAZAR.** Rien n'est scellé ; la version 13 scellée reste le texte en vigueur. Pièce de travail (classe C). Même rédacteur que la version 14, modèle F ; mandat `2a44da18…`, qui vaut toujours. 2026-11-20, journaux de l'outil de 18:09:04Z à 18:10:56Z.

Dossier : `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/redacteur-palier-0b-v14/v15/`.

## 1. Verdict

La version 15 est la version 14 (`840400f3…`) plus **douze remplacements exacts, en quatre appels de l'outil** : C1 et C2, puis N1 à N4, à la lettre des deux jeux du contre-lecteur, puis six du rédacteur. Les deux premières sorties sont égales aux essais du contre-lecteur. Une seule ligne commence par « - Commit du code d'analyse : » (compte : 1) ; le blanc `COMMIT_V6` reste, une seule fois ; aucun groupe de quarante chiffres hexadécimaux dans cette ligne (compte : 0) ; les 64 lignes de la table y sont (compte : 64), la table n'étant pas touchée. Aucun refus de permission, de classifieur ni de garde.

## 2. Fichiers et empreintes

| fichier | empreinte SHA-256 |
|---|---|
| `preenregistrement-heritage-palier-0b-etage-processeur-v15.md` | `33b04ff46d20a55051236d385c38e5e8fd30e7b3d969bd5d46a54a13b62b842f` |
| `differentiel-palier-0b-v14-v15-v1.diff` (`diff -u`) | `623fd1bf6f0604c901982805af18df7f3ae29c5524fe7a7ba5ece02d900fbb54` |
| `remplacements-passe-3-tenue-et-remarque-v1.json` | `f4966bd375499de3cfffef6c4e388dcce5d72f50d3e47e050a399595554a2f3e` |
| `remplacements-passe-4-date-v1.json` | `c71f92d48acd0e3eaf897b662b269b97695ad6e84514380fb7c785e58f57f7fe` |

Chacun a son compagnon ; les quatre journaux de l'outil et leurs compagnons sont au même dossier. Pièces reçues, recalculées et égales à leur compagnon : contre-lecture (`c8ca85f5…`), jeu des corrections (`4b9eadca…`), jeu des textes non exigés (`63ec09e1…`).

## 3. Les quatre appels

| appel | jeu | sortie | heure du journal |
|---|---|---|---|
| 1 — C1, C2 | celui du contre-lecteur, tel quel | `passe-1-v14-plus-c1-c2.md`, `2c36dadb…`, égale à son essai | 18:09:04Z |
| 2 — N1 à N4 | celui du contre-lecteur, tel quel | `passe-2-plus-n1-n4.md`, `d670fd4c…`, égale à son second essai | 18:09:13Z |
| 3 — cinq du rédacteur | passe 3 | `passe-3-tenue-et-remarque-sans-date.md`, `11e079c5…` | 18:10:44Z |
| 4 — un du rédacteur | passe 4 | la version 15, `33b04ff4…` | 18:10:56Z |

Les six du rédacteur : titre ; statut et ligne de version ; section « Contre-lecture », alinéa « Version 15 » ; **remarque 9** de l'annexe H (« Version 14 », § 7) ; alinéa « Version 15 » en fin d'annexe H ; ligne de date.

**Remarque 9, texte de ma main, déclaré.** Elle porte la règle de la mère sur les étapes 3 à 9, citée par sa ligne de registre, **R-4333** (2026-11-20T18:08:29Z), à la lettre, relue sur `origin/main` au commit `35c78ea75e6a81084ef941f634bd7679c328330e` après un `git fetch` (`registres/decisions.md` tel que `git show` le rend : `d1468f50…`), et dans les mots du message de la session. Elle est écrite en remarque : aucune ligne n'est ajoutée à la liste d'arrêt, aucun programme ne la vérifie, la mère en répond.

## 4. Écarts et limites

- **Quatre appels au lieu de trois.** La date demandée est l'heure du journal, qu'on ne connaît qu'après l'appel. La ligne de date est donc inscrite par un quatrième appel, qui porte les heures des trois premiers ; l'heure du quatrième (18:10:56Z) n'est qu'à son journal.
- L'ancre de la passe 4 a été comptée (une fois) sur la sortie de la passe 2, non sur celle de la passe 3 ; l'outil l'a trouvée une seule fois.
- **N1 à N4 sont du contre-lecteur, portés tels quels** : je n'ai lu ni la pièce de la mesure de l'étape 8 que N3 cite (`216e2309…`), ni la vérification de la version 13 que N4 nomme, ni les journaux de la version 13 dont N1 et N2 donnent les heures. Dit au texte.
- Le chemin `palier-0b/brouillon-v14/` de la version 14 versée est déduit du chemin de sa contre-lecture ; je ne l'ai pas contrôlé.
- Un `mkdir -p` de mon dossier `v15/` ; un `git fetch origin main`, un `git show` redirigé, un `git rev-parse`.
- Aucun lancement du code, aucun tirage, aucune pièce d'autorisation, aucun appel à un fournisseur, aucune dépense, aucune écriture dans le dépôt, rien sous `archives-reponses-modeles/` ni `/root/.claude/`. **À ne pas verser** : `decisions-origin-main.md`, copie de lecture du registre, qui porte des noms de modèle.

## 5. Ce qui reste ouvert, non tranché par ce texte

- Le programme des étapes 6 bis et 7, que R-4333 veut écrit et vérifié avant le GO : s'il entre au paquet, la ligne du commit et sa table se refont, donc un texte de plus.
- Le remplissage du blanc (texte proposé par le contre-lecteur, son § 6, point 1) et la question « un mot ou deux de Lazar ».
- Pour Lazar, selon R-4333 : l'écart de la mesure de l'étape 8 à la clause « deux nombres de sources » de l'annexe C, et l'agrégation de l'enrichissement.

Signé : rédacteur, modèle F.
