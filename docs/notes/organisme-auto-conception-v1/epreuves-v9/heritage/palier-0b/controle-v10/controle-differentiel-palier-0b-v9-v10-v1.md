# Contrôle du différentiel v9 → v10 — préenregistrement du palier 0b — v1

- Auteur : contrôleur neuf, modèle O. Je n'ai écrit aucune version du préenregistrement, ni le code, ni la vérification du code, ni le contrôle de la v9. Pièce de travail (classe C).
- Date : 2026-11-20 ; `date -u` lu à 10:19Z et à 10:26Z en cours de travail.
- Mandat : `P/mandat-controle-differentiel-palier-0b-v9-v10-v1.md` (`1d0bf3d78b1177f5e51aa6a2ee0d6f47405e4955ae1189c58ce1d8339fbdd70d`), compagnon vérifié avant tout autre geste ; règle R2.
- Conditions : processeur seul ; aucun tirage, aucun lancement du code du palier ; aucun appel à un fournisseur de modèles, aucune dépense ; aucune écriture dans l'arbre du dépôt, aucun commit. Réseau : un seul `git fetch origin main` (il écrit sous `.git/`), réussi au premier essai, puis trois `git show` redirigés vers mon dossier. Programmes lancés par leur chemin : l'outil de remplacement (rejeu, puis deux essais de mes textes sur une copie, dans mon dossier) et mon `verifier_lettre_controle_v1.py` (comparaison de textes, sans graine). Aucune commande de liste, une commande simple par appel, aucun heredoc, aucun code en ligne. Rien sous `archives-reponses-modeles/` ni sous `/root/.claude/`. Une commande `tail` a échoué sur une option qu'elle n'a pas ; je l'ai remplacée par un `grep -c`. Ce n'est pas un refus. **Aucun refus de permission, de classifieur ni de garde.**

P : `docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/`.

## Verdict

**À corriger : une correction de justesse (garde 25), aucune de fond.** Elle se porte avec le report de R-4182 (§ 4) dans la version qui portera le mot de Lazar sur la remarque 1. Après ces deux reports, le texte sera scellable au sens de ce contrôle, sous ses propres conditions : le code v5, sa vérification et l'erratum du commit refait et contre-lu.

- La v10 est exactement la v9 plus les 31 remplacements du JSON : le rejeu est égal à l'octet.
- Les sept textes à la lettre du contrôle de la v9 y sont égaux à l'octet.
- Les 24 remplacements du rédacteur sont justes et dans la lettre de R-4182, du mandat de la v10 et du contrôle de la v9.
- Aucun critère, aucune valeur gelée, aucune prédiction, aucune issue ne change ; la remarque 1 n'est pas tranchée.
- La seule faute : l'artefact de la garde 25 pour la zone médiane du contenu dit « ni arrêt ni signalement » mais pas « ni mention ». Il laisserait donc passer précisément ce que la lecture (i) change : le code v4 pose la mention.

## 1. Empreintes

Chaque pièce a été vérifiée par `env -C DOSSIER sha256sum -c F.sha256`. Chacune est égale à son compagnon et au préfixe que donne le mandat.

| pièce (P/) | empreinte |
|---|---|
| `mandat-redacteur-palier-0b-v10-v1.md` | `194f44b3e0b7e99b8959d883ab89a60f130c092dd1b0cc814982e7966c38f6ce` |
| `preenregistrement-heritage-palier-0b-etage-processeur-v9.md` | `0aacc4ea275e97812647ce0ce4723c9bd01d76f32a8f0c42462d00be2fe7bc2e` (intacte) |
| `preenregistrement-heritage-palier-0b-etage-processeur-v10.md` | `ac2deb4daf4fb0b3088400ba742a6583844b0e5720774fd8b9055d0a72250f6b` |
| `remplacements-preenregistrement-palier-0b-v9-v10.json` | `9f21c638f4bae296651a9fbd1dd78269769567e8a76a36ed8b0b27b07aba8fa7` |
| `…-v10.md.journal-remplacements-v1.json` | `65e6c21e18902c35b3c3c6061e638581a0a8723b0eeebc8d4beaea5f248873fa` |
| `differentiel-preenregistrement-palier-0b-v9-v10.diff` | `88db4dcf648704ad90a5e536349e456973f8d5c9e52023958bd8d68ef262e43c` |
| `rapport-redacteur-palier-0b-v10-v1.md` | `ddea2701a34046ff70d2c612bd6277d6bc45799f6cc26486247a174b22b8835f` |
| `contre-lecture-v9/controle-differentiel-palier-0b-v8-v9-v1.md` | `98f46d0ae18159e32f830ff79bc2c9a930db43a3c728c735311c2358b4a8b72e` |
| `code-v4/rapport-developpeur-code-palier-0b-v4.md` | compagnon vérifié |
| `code-v4/src/controle_ia/heritage_etage_processeur_v1/audit.py` | `890040e3…`, égale à la table du développeur |
| `code-v4/src/controle_ia/heritage_etage_processeur_v1/tirages.py` | `93077e25e671a164fcae741c248f865011dfe436bb49d830ead4c9e41ba8795c`, égale à la table du développeur (l. 194) |
| `scripts/remplacer_texte_exact_v1.py` (dépôt) | `391db990734dd36f7c827b8b6c77dc0de1bda324f671b65748ccfe68c56a53d6` |

**Registres.** J'ai relu `main` à `ae64b9d3b12c7dcfe7bae4d5d2ac73b50c6f3ef2`, après le fetch.
- R-4182 y est, à la ligne 4320 de `registres/decisions.md`, sous l'heure 2026-11-20T10:11:28Z.
- R-4123 (l. 4261) et R-4135 (l. 4273) disent ce que la v10 en cite.
- `GO-2026-11-20-11` (l. 542) et `GO-2026-11-20-25` (l. 556) de `registres/go.md` sont ceux que citent les versions 9 et 10.
- J'ai aussi relu `decisions.md` au commit `9143abee0b8767c627a629bcb26e23b6e0640267`, celui du rédacteur. R-4180 y est, mais ni R-4181 ni R-4182. Le constat du rédacteur est donc juste : la ligne n'était pas encore sur `main` quand il l'a relu.

## 2. Point 1 — rejeu

- **Rejeu.** J'ai passé l'outil `391db990…` sur la v9 `0aacc4ea…`, avec le JSON `9f21c638…`, vers `rejeu-v10.md` dans mon dossier. Il rend « FAIT : 31 remplacement(s) », sortie `ac2deb4d…`, aucun avertissement, et `cmp` avec la v10 est muet : **égale à l'octet**.
- **Journal.** Le mien et celui du rédacteur ne diffèrent que par l'heure (10:19:35Z contre 10:16:26Z) et par deux chemins (JSON et sortie). Outil, cible, empreinte du JSON, sortie, 31 détails et avertissements sont égaux.
- **Différentiel.** Refait par `diff -u`. Hors de la ligne d'en-tête « +++ » (chemin et heure), il est égal au différentiel versé. Il compte 22 lignes de la v9 touchées : 1, 3, 6, 209, 299, 323, 357, 359, 429, 532, 751, 901, 904, 912, 917, 928, 934, 943, 945, 946, 947 et 950.
- **Lieux.** Aucune de ces lignes n'est dans « Hypothèse » (94-130), « Prédiction » (131-149), « Métrique » (150-170), « Valeurs gelées » (175-193), « Les six critères » (194-204), « Critères de lecture gelés » (386-408) ou « Liste d'arrêt » (409-426). La ligne 209 est la puce des marges des « Autres seuils ». Le JSON ne porte aucun identifiant de modèle ni de session.

## 3. Point 2 — à la lettre du contrôle de la v9

`verifier_lettre_controle_v1.py` extrait des § 8 et § 9 du contrôle chaque « Ancien » et chaque « Neuf ». La règle est celle du contrôle : la ligne entière, hors des accents graves de bord. Il les cherche ensuite dans le JSON, la v9 et la v10.

| texte du contrôle | rang du JSON | neuf égal à l'octet | ancien dans v9 / v10 | neuf dans v9 / v10 |
|---|---|---|---|---|
| correction 1 (réserve 25) | 14 | oui | 1 / 0 | 0 / 1 |
| correction 2 (garde 25) | 11 | oui | 1 / 0 | 0 / 1 |
| R2-T (section « Seuil ») | 6 | oui | 1 / 0 | 0 / 1 |
| N1 (heure de la v9) | 4 | oui | 1 / 0 | 0 / 1 |
| N2 (B8, extension) | 10 | oui | 1 / 0 | 0 / 1 |
| N3 (remarque 1) | 18 | oui | 1 / 0 | 0 / 1 |
| N4 (annexe H, § 1) | 16 | oui | 1 / 0 | 0 / 1 |

**Reports de R2-T** (dernier alinéa du § 8 du contrôle). Tous sont faits :
- remarque 2 de l'annexe H, « non tranchée » (rang 20) et « D'ici là » (rang 21) ;
- point 2 du code v5 (rang 27) ;
- mention « remarques 1 à 4 » de la ligne de version (rang 3) ;
- section « Contre-lecture » : la phrase de la v9 est gardée comme histoire, et l'alinéa « Version 10 » (rang 13) dit que seule la remarque 1 reste.

R-4182 dit « remarque 2 lue en (i) (texte R2-T du contrôle) » : le texte porté est donc couvert par la ligne de la mère.

## 4. Point 3 — les 24 remplacements du rédacteur

| rang | lieu | objet | jugement |
|---|---|---|---|
| 1 | titre | v9 → v10 | juste (tenue) |
| 2 | ligne de version | statut ; alinéa « Version 10 » | juste. Le compte « sept à la lettre, vingt-quatre du rédacteur » est exact. La mention « à inscrire » se remplace (§ 5, texte 1) |
| 3 | ligne de version | « remarques 1 à 4 » | juste ; report de R2-T demandé |
| 5 | date | heure de la v10 | juste, mais refait le défaut que N1 corrigeait pour la v9 (non exigé NE-1, § 7) |
| 7 | B7 bis | jeu de la garde 27 : trois sources, proposeur τ = 2, appelant | à la lettre de la recommandation du § 5 du contrôle et du point 3 du mandat. Conforme au code v4 : `etape_4_jeu_de_la_garde_27` prend `prop` et `sources` sans défaut, et `etape_4` ne joue que les bras 1 à 3 (rapport du code v4, point 5) |
| 8 | B8 | « après le GO de Lazar sur le palier » | juste : lettre de R-4123 (« écrite par la mère après le GO de Lazar sur le palier ») |
| 9 | B8 | verrou, résumé de (a) à (e) | juste ; il abrège sans rien changer (l'heure « inscrite au manifeste » et le nom du champ retiré sont à la remarque 4) |
| 12 | garde 27, cas sain | trois sources, proposeur | juste |
| 13 | « Contre-lecture » | alinéa « Version 10 » | juste ; la mention « à inscrire » se remplace (texte 2) |
| 15 | écart 1 | renvoi « trois sources » | juste |
| 17 | remarque 1, titre | « posée à Lazar, sans défaut » | juste (point 7 du mandat) |
| 19 | remarque 1, fin | recommandation (ii) et ses trois raisons | fidèle au § 5 du contrôle (« Défaut : aucun, comme pour les nœuds de R-4135 ») ; « Ce texte ne la tranche pas » |
| 20, 21 | remarque 2 | « tranchée, lecture (i) » ; « D'ici là » remplacé | juste ; la raison est celle du § 5 du contrôle ; la mention « à inscrire » se remplace (texte 3) |
| 22, 23 | remarque 4 | titre ; (a) à (e) | (a) à (e) sont à la lettre du § 5 du contrôle. (a) est conforme à `controle_ia.scellement.verifier` et `lire_compagnon` (une ligne, nom attendu, empreinte égale), que j'ai lus. Les deux différences avec les propositions de la v9 sont dites justement. La mention « à inscrire » se remplace (texte 4) |
| 24 | silences, n° 8 | « tranchée » | juste et nécessaire : sinon la table disait encore « remarque 3 » ouverte |
| 25, 26 | remarque 3 | titre ; règle | juste. La raison des trois sources est celle du contrôle. « La construction à trois sources passe à la dose 0,25 » est écrit à l'écart 1 (l. 750). La mention « à inscrire » se remplace (texte 5) |
| 27 | code v5, point 2 | zone médiane : ni signalement ni mention | juste ; il demande au code v5 de changer ce que pose le code v4. Voir la correction C1, qui porte la même chose à la garde 25 |
| 28, 29 | code v5, points 4 et 5 | verrou (a) à (e) ; garde 27 | juste |
| 30 | code v5, point 6 | les trois ajouts du § 7 | à la lettre du contrôle, sans la condition « si la remarque 3 retient trois sources », désormais remplie |
| 31 | « Ce qui revient à la mère » | état des quatre remarques | juste. « aucune tranchée ici » reste comme phrase de la v9, et l'ajout la corrige aussitôt. La mention « à inscrire » se remplace (texte 6) |

**Lettre de R-4182.** La ligne est brève : « remarque 2 lue en (i) (texte R2-T du contrôle), trois sources pour la garde 27, verrou D6 lu selon (a) à (e), tenues N1 à N4 retenues ; la remarque 1 […] reste posée à Lazar ». Elle ne nomme pas quatre points :
- l'appelant et le proposeur du jeu de la garde 27 ;
- l'alignement de B8 ;
- les trois ajouts au code v5 ;
- les corrections 1 et 2.

Ces points sont au mandat de la v10, une pièce de la mère qui dit qu'elle a « pris les recommandations du contrôle sur les remarques 2, 3 et 4 et les tenues N1 à N4 ». Les corrections 1 et 2 sont des corrections de justesse du contrôle, non des choix. Rien dans la v10 ne va au-delà du mandat et du contrôle ; les textes 1 et 5 du § 5 le disent.

**Rien d'autre ne change.** La remarque 1 reste ouverte en trois lieux : la section « Seuil » (deux cas « non tranché »), le point 1 du code v5 et la remarque elle-même. Les deux audits de lois restent à la lettre. Le seuil de 0,55 reste.

## 5. Point 4 — les six mentions « à inscrire », remplacées par R-4182

Chaque ancien est compté une fois par `grep -c -F -e` dans la v10. Les six, avec C1, s'appliquent ensemble par l'outil sur une copie de la v10 dans mon dossier : « FAIT : 7 remplacement(s) », sortie `29608134…`, et plus aucune mention « vers 10:09Z, à inscrire » (`grep -c` rend 0). Cette copie est un essai, non une version. Règle des textes : la ligne entière qui suit « Ancien : » ou « Neuf : », hors des accents graves de bord.

**Texte 1 — ligne de version (l. 3).**
- Ancien : `(décision de la mère du 2026-11-20 vers 10:09Z, à inscrire : aucune ligne de `registres/decisions.md` ne la porte encore sur `main` au commit `9143abee0b8767c627a629bcb26e23b6e0640267`, relu par ce rédacteur)`
- Neuf : `(décision de la mère R-4182, inscrite dans `registres/decisions.md` sous l'heure 2026-11-20T10:11:28Z et présente sur `main` au commit `ae64b9d3b12c7dcfe7bae4d5d2ac73b50c6f3ef2` ; elle dit en abrégé ce que le mandat de la version 10 détaille ; le rédacteur de la version 10, qui relisait `main` au commit `9143abee0b8767c627a629bcb26e23b6e0640267`, où elle n'était pas encore, l'écrivait « à inscrire »)`

**Texte 2 — section « Contre-lecture », alinéa « Version 10 » (l. 429).**
- Ancien : sur les recommandations de ce contrôle (décision de la mère du 2026-11-20 vers 10:09Z, à inscrire)
- Neuf : sur les recommandations de ce contrôle (décision de la mère R-4182)

**Texte 3 — remarque 2 de l'annexe H (l. 912).**
- Ancien : la mère consigne la lecture (i) (décision de la mère du 2026-11-20 vers 10:09Z, à inscrire)
- Neuf : la mère consigne la lecture (i) (décision de la mère R-4182)

**Texte 4 — remarque 4 de l'annexe H (l. 917).**
- Ancien : décision de la mère du 2026-11-20 vers 10:09Z, à inscrire, sur les points (a) à (e)
- Neuf : décision de la mère R-4182, sur les points (a) à (e)

**Texte 5 — remarque 3 de l'annexe H (l. 934).**
- Ancien : décision de la mère du 2026-11-20 vers 10:09Z, à inscrire, sur la recommandation du § 5
- Neuf : décision de la mère R-4182, qui nomme les trois sources, l'appelant et le proposeur étant dits au point 3 du mandat de la version 10, sur la recommandation du § 5

**Texte 6 — « Ce qui revient à la mère » (l. 950).**
- Ancien : (décision de la mère du 2026-11-20 vers 10:09Z, à inscrire) ; la remarque 1
- Neuf : (décision de la mère R-4182) ; la remarque 1

Si la version qui les porte relit `main` à un autre commit, le texte 1 inscrit ce commit à la place de `ae64b9d3…`.

## 6. Point 5 — les huit remarques du rapport (§ 6) et ses écarts

| n° | objet | sort | recommandation |
|---|---|---|---|
| 1 | R2-T porté sans la ligne de la mère | **sans suite** | R-4182 le couvre à la lettre (« texte R2-T du contrôle »). Le report de l'identifiant (§ 5) suffit |
| 2 | lieux touchés au-delà du mandat (silence n° 8, « Ce qui revient à la mère ») | **sans suite** | les deux sont justes et nécessaires : sans eux, la table et l'alinéa diraient encore les remarques ouvertes |
| 3 | garde 27 : l'artefact « source précédente au lieu de suivante » absent de la table | **à la mère, non exigé** | il rend visible ce qui justifie les trois sources (règle R5). Texte prêt : NE-2, § 7. Confiance moyenne |
| 4 | garde 25 : « ni mention » non écrit pour la zone médiane du contenu | **à corriger** | correction C1, § 7. L'annexe H, § 2, dit que la règle de signalement touche la garde 25. Sous (i), l'artefact doit faire échouer un code qui pose la mention, ce que fait le code v4 (point 2 du code v5). Confiance haute |
| 5 | verrou (c) : noms des quatre champs et forme de l'heure | **à la mère, en routine** | elle peut les laisser au code v5 : son développeur les fixe dans l'ordre de R-4123, le vérificateur du code les contrôle, et l'erratum du commit les inscrit. La pièce d'autorisation les suit. Rien à changer au texte, rien pour Lazar |
| 6 | `preenregistrement_sha256` non vérifié | **sans suite** | vérifié : `tirages.py` du code v4, l. 238 (`93077e25…`), `"preenregistrement_sha256": PREENREGISTREMENT_SHA256` |
| 7 | option (a) de la fiche de 08:02:31Z non relue | **à la mère** | le contrôle de la v9 demandait de la relire avant de poser la remarque 1 : si elle nommait un plancher, la remarque tombe. R-4182 ne dit pas que c'est fait. Ce n'est pas un mot du texte |
| 8 | « `lecture` devra recevoir M » non porté | **sans suite** | le contrôle le disait implicite au point 1 du code v5 ; il n'était pas un des trois ajouts |

**Écarts du rapport.** Je les accepte tous :
- statut inchangé ;
- pas de section « Version 10 » à l'annexe H (la ligne de version dit ce que la v10 porte) ;
- « 28 remplacements » laissé à la section « Version 9 » ;
- pas de ligne v10 aux listes « Fichiers à donner » ;
- relecture partielle de la v10 (l'outil garantit les octets hors zones, ce que le rejeu confirme).

Une remarque de plus pour la mère, sans mot du texte : le contrôle de la v9 recommandait qu'elle informe Lazar en une ligne de la lecture (i). R-4182 ne le dit pas.

## 7. Corrections (texte exact)

Chaque ancien figure une seule fois dans la v10 (`grep -c -F -e` rend 1). La correction se porte par l'outil `391db990…`, dans la version qui portera le mot de Lazar et le § 5.

**C1 — garde 25, l. 357 : la zone médiane du contenu sous la lecture (i).**
- Ancien : une exactitude de contenu ou réunie au-dessus de 0,55 et au plus M + 2 σ₀ : ni arrêt ni signalement
- Neuf : une exactitude de contenu ou réunie au-dessus de 0,55 et au plus M + 2 σ₀ : ni arrêt, ni signalement, ni mention « générateur non audité pour l'étage payant », seulement les mots « non départagée du hasard à cette taille » (version 10 ; remarque 2, lecture (i), décision de la mère R-4182)

**Non exigé (tenue), à porter si la mère le veut.** Les deux textes s'appliquent par l'outil après C1 et le § 5 (essai : « FAIT : 2 remplacement(s) », sortie `9e1de563…`).
- **NE-1** (l. 6, l'heure de la v10, comme N1 pour la v9 ; heure du journal relue : 10:16:26Z) :
  - Ancien : `version 10 le 2026-11-20 (`date -u` à 10:11Z en cours de travail ; l'heure exacte est au journal de l'outil)`
  - Neuf : `version 10 le 2026-11-20, à 10:16Z (heure du journal de l'outil : 10:16:26Z ; `date -u` à 10:11Z en cours de travail)`
- **NE-2** (garde 27, colonne de l'artefact, l. 359 ; remarque 3 du rapport) :
  - Ancien : le registre de la source propre servi au bras 4a (ce serait le bras 3), ou un registre étranger servi à un bras du critère : arrêt ;
  - Neuf : le registre de la source propre servi au bras 4a (ce serait le bras 3), le registre de la source précédente servi au bras 4a au lieu de celui de la source suivante (version 10 : jeu à trois sources, remarque 3), ou un registre étranger servi à un bras du critère : arrêt ;

**Tenue de la version suivante.** Elle n'appelle pas de texte de ma part. La ligne de version et l'alinéa « Version 10 » de « Contre-lecture » disent encore « il reste le contrôle du différentiel de la version 9 à la version 10 » : la version suivante dira ce contrôle fait, avec son verdict et son empreinte.

## 8. À déclarer de mon côté

- **Lu en entier** : mon mandat, le mandat du rédacteur, son rapport, le contrôle de la v9, le JSON (les 31 textes neufs) et l'outil.
- **Lu en partie** :
  - la v10 : lignes 1 à 7, et les 22 lignes touchées avec leur voisinage (205-212, 299, 323, 357, 359, 425-431, 532, 746-751, 895-952) ;
  - le rapport du code v4 : point 4, point 5, et l. 660-709 du différentiel de `etapes.py` et de `mecanique.py` ;
  - `tirages.py` : une recherche de mot ;
  - `src/controle_ia/scellement.py` : l. 38-88.

  Rien de cela n'a été lancé. Le reste de la v10 n'est pas relu : l'outil le garantit égal à la v9.
- Je n'ai pas lu la fiche que Lazar a reçue à 08:02:31Z.
- Un écart à la lettre du mandat, sans effet sur le fond : j'ai appliqué mes textes à une copie de la v10, dans mon dossier, pour prouver qu'ils s'appliquent. Ces copies portent « non-version » dans leur nom ; elles ne sont ni une v11 ni à verser comme telle.

## 9. Fichiers de mon dossier

`/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/controle-palier-0b-v10/` :
- ce contrôle, avec son compagnon ;
- `verifier_lettre_controle_v1.py` ; `verifier_mes_textes_v1.py`, qui confirme que les neuf paires de ce contrôle (§ 5, § 7) sont égales à l'octet aux entrées des deux JSON d'essai ;
- `rejeu-v10.md` (`ac2deb4d…`), son compagnon, son journal et le compagnon du journal, écrits par l'outil ;
- `diff-v9-v10-controleur.diff` ;
- `decisions-main-ae64b9d3.md`, `go-main-ae64b9d3.md` et `decisions-main-9143abee.md`, rendus par `git show` ;
- les essais : `essai-remplacements-controleur-sur-v10.json` (C1 et les textes 1 à 6) et `essai-v10-plus-controleur-non-version.md` (`29608134…`) ; `essai-non-exiges-controleur-sur-v10.json` (NE-1, NE-2) et `essai-v10-plus-controleur-et-non-exiges-non-version.md` (`9e1de563…`) ; chacun avec les compagnons et le journal écrits par l'outil.

*Contrôleur neuf, modèle O.*
