# Contrôle du différentiel v1 → v2 — additif 1 de la ligne 3 et rapport du rédacteur — v1

Pièce de travail (classe C). Écrite le 2026-11-20 (temps universel, `date -u` : 03:14Z), sur le message de la session du compte organisme. Même contre-lecteur que la contre-lecture de la v1 (`contre-lecture-additif-1-ligne-3-v1.md`, `f12200ae427da3f3f70d549ac4dfef4feeb805b2279c7a24bf36e86f563d3955`, recalculée égale dans `additif-1-v1/`), modèle O. Je n'ai écrit ni la v1, ni la v2, ni les JSON.

## Verdict

**Conforme.** Le rejeu de l'outil rend les deux v2 à l'octet. Les six corrections sont portées à la lettre, et la phrase du point B suit mon jugement. Rien de gelé ne change, aucun identifiant de modèle n'apparaît, et les deux phrases de statut tiennent.

## Empreintes (toutes recalculées ; `sha256sum -c` des compagnons : OK)

A2 = `/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/ligne-3-votes-effectifs-juges/additif-1-v2/`.

| pièce | sha256 |
|---|---|
| mandat du rédacteur, `additif-1-v1/mandat-redacteur-corrections-additif-1-ligne-3-v2-v1.md` | `a47f8f044ce3779ace178aacfa78c4576191574ee2074e13c65fd09f164e03ed` |
| A2 `additif-1-preenregistrement-ligne-3-votes-effectifs-juges-v7-v2.md` | `e1c1ee842219397a45b5a9a9336d05d873499b2a94bc8847f204b205141908b0` |
| A2 `rapport-redacteur-additif-1-ligne-3-v2.md` | `492cde9452b013230a004b5d6e1bbcd300afd3e8ceeccc36232df681a4a46bcd` |
| A2 `rapport-redacteur-corrections-additif-1-ligne-3-v2-v1.md` | `35f7dabe60b65b7ac37fa72d4956b068760308e29d3a021d4799e4a28d8b1828` |
| A2 `remplacements-additif-1-ligne-3-v1-vers-v2.json` | compagnon OK ; `74b629e1…` au journal |
| A2 `remplacements-rapport-redacteur-additif-1-ligne-3-v1-vers-v2-b.json` | compagnon OK ; `bee95353…` au journal |
| A2 `remplacements-rapport-redacteur-additif-1-ligne-3-v1-vers-v2.json` (fautif) | compagnon OK |
| A2, les deux journaux `…-v2.md.journal-remplacements-v1.json` | compagnons OK |
| A2, les deux différentiels `.diff` | compagnons OK |
| outil `scripts/remplacer_texte_exact_v1.py` | `391db990734dd36f7c827b8b6c77dc0de1bda324f671b65748ccfe68c56a53d6` |
| v1 de l'additif et du rapport (`additif-1-v1/`) | `27ecd5d5…`, `6c273e5e…` |

Au commit `05fd920b`, les deux v2 extraites par `git show` (redirigé vers mon dossier) ont les mêmes empreintes, `e1c1ee84…` et `492cde94…`.

## 1. Rejeu de l'outil

Rejeu fait dans mon dossier, `…/contre-lecture-additif-1-ligne-3/rejeu-v1-v2/`, avec `python3 -B …/remplacer_texte_exact_v1.py` sur les v1 et les JSON employés.
- **Additif** : « FAIT : 9 remplacement(s) ». La sortie vaut `e1c1ee84…`, et `cmp` avec la v2 rendue ne trouve aucune différence.
- **Rapport** (JSON `-b`) : « FAIT : 6 remplacement(s) ». La sortie vaut `492cde94…`, et `cmp` ne trouve aucune différence.
- **Journaux rendus** : outil `391db990…`, cibles `27ecd5d5…` et `6c273e5e…`, sorties égales aux v2, aucun avertissement. Le rapport court attribue bien chaque JSON à sa pièce.
- **JSON fautif, rejoué** : refus, code 2, « remplacement n° 2 : texte ancien 'f4ace`, égale à son compagnon).' trouvé 0 fois dans la cible ». J'ai vérifié par `stat` qu'aucune sortie n'a été écrite. Ce JSON ne diffère du JSON `-b` que par l'ancre et le début du texte neuf du remplacement n° 2 (`f4ace` au lieu de `894972`). L'incident est bien une validation de l'outil, non un refus de permission ni de classifieur, et il est sans effet sur les v2.

## 2. Les six corrections, et le point B

J'ai relu les deux différentiels v1 → v2 que j'ai refaits par `diff -u`. Ils ne montrent que quinze zones : neuf dans l'additif, six dans le rapport.
- **Correction 1** (règle C, point 1) : le texte neuf est mot pour mot le mien, phrase « Même loi dans le monde de puissance, sur le juge 2. » comprise.
- **Correction 2** (règle B, « Pourquoi ρ′ = 0 ») : mot pour mot. La suite, de « **C'est un raisonnement, non un calcul** » à « sous ce raisonnement », est gardée, comme ma correction le laissait.
- **Correction 3** (rapport, option (b) du nœud éventuel) : mot pour mot.
- **Correction 4** (règle D, point 6) : les deux morceaux, début (bras A) et fin (référence à zéro erreur), sont mot pour mot.
- **Correction 5** (silence 2, « P6 réfutée » / « P6 non réfutée » ; point 2 de « Ce que le code doit changer ») : mot pour mot.
- **Correction 6** (cinq comptes, dans l'additif et dans le rapport) : mot pour mot.
- **Point B du rapport** : la phrase ajoutée dit « question de conception, non un nœud ; le raisonnement est juste en moyenne, non démontré sur la loi entière » et « l'option (b) … presque gratuite en calcul (quelques minutes de plus) ; son vrai coût est le code, les essais et leur vérification ». Elle rend fidèlement mon jugement. La recommandation (a), sa confiance de 0,75 et le défaut sous 48 heures ne changent pas.
- **Tenue** : les deux titres passent en « — v2 », les deux lignes de version sont ajoutées, et dans le « Verdict » du rapport le nom de l'additif passe en `…-v7-v2.md`. Le mandat du rédacteur permet ces trois changements.

## 3. Rien de gelé ne change

Les quinze zones ne touchent aucune hypothèse, prédiction, seuil, métrique, critère de lecture, règle gelée ni montant de la version 7. Les règles A, E, du silence 1, F à J et les quatorze choix sont inchangés. Les deux nœuds 1 et 2 sont inchangés, et le nœud éventuel ne change que par la correction 3. Les ajouts au code restent faits après les tirages ; le seul ajout neuf est un compte de plus.

## 4. Les deux phrases de statut

- **Additif, ligne 3** : « **Statut : à contre-lire (règle R2), puis à sceller par la mère, …** ». Elle **tient**. Elle décrit l'ordre des gestes, et la ligne de version qui la suit dans le même paragraphe dit que la v1 a été contre-lue et que restent « la vérification de ces corrections, puis le scellement par la mère ». Le lecteur ne peut pas croire que la règle R2 manque. La récrire aurait demandé une v3, que rien d'autre ne justifie. Le statut final appartient à la trace du scellement par la mère. Remarque non exigée : si une v3 se faisait pour une autre raison, le texte pourrait devenir « **Statut : contre-lu (règle R2) en version 1 ; version 2 vérifiée sur son différentiel ; à sceller par la mère, avant tout calcul de l'étage 1, chronométrage compris.** ».
- **Rapport, « Ce qui reste à faire »** : il nomme encore la contre-lecture. Il **tient**. La ligne de version dit en toutes lettres que « la contre-lecture demandée plus bas … est donc faite ; reste la vérification des corrections ». La pièce est de classe C, et sa section garde la trace de l'état de la v1.

## 5. Identifiants de modèle

Les trois pièces n'en portent aucun. « Argon » (additif v2, ligne 54) est le nom de juge du texte v7, comme en v1. « `/root/.claude/` » et « `/tmp/claude-0/…` » sont des chemins.

## Refus et écarts

Aucun refus de permission, de classifieur ni de garde. Le refus de l'outil sur le JSON fautif est voulu : c'est l'essai qui confirme l'incident, et rien n'a été écrit. Dans le dépôt, je n'ai fait que deux `git show` au commit `05fd920b`, redirigés vers mon dossier ; aucune écriture, aucun commit. Aucun calcul de l'étage 1, aucun tirage. Rien sous `archives-reponses-modeles/` ni sous `/root/.claude/`. Aucun appel à un fournisseur, aucune dépense. Les fichiers du rejeu (deux sorties, leurs journaux et compagnons, deux extraits du commit) restent dans `rejeu-v1-v2/` : ils ont servi au contrôle, ce ne sont pas des pièces rendues.

Contre-lecteur, modèle O.
