# Vérification des fragments de l'étage 2 (ligne 3), version 3 des fragments — v1

Pièce de travail (classe C). Signé : vérificateur des fragments, modèle O (le même que pour les v1 et v2). Date : 2026-11-20.
Mandat : `mandat-verificateur-fragments-etage-2-v1.md` (`0125a72cc288713ce59e498323cbc775904ee340d5c38c691b26c036edb03f8c`), mêmes interdits. Demande de la coordination : contrôle par différentiel de la v3, après la remarque de ma pièce v2 (`verification-fragments-etage-2-v2-v1.md`, `93dffc03538d47aab93854e8607d3b3bcde31ba33c4b18d8edd511e27186d19d`, § 4) retenue par la mère.

## 0. Verdict

**Conforme.** Seuls `version` et le champ `epreuve_monde_plante` de `f-epr-net-04` changent. Le fragment est désormais « net » (défaut présent, non annoncé), viole `epreuve_plantee` et lui seul. Comptes inchangés. Aucun fragment contesté (0 sur 259).

## 1. Pièces et empreintes

Dossier H = `/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/ligne-3-votes-effectifs-juges/etage-2-portee-200-v1/fragments-v3/`.

| Pièce | Empreinte | Contrôle |
|---|---|---|
| `H/fragments-etage-2-ligne-3-v3.json` | `23be8dae1839eab72979b794371a7fb0bce38bcd41b8309cc79386fc233c50fb` | conforme au compagnon et à l'annonce |
| `H/diff-fragments-v2-v3.diff` | `4728bfe8b2ad6feeb1318ab1d4cf8ff9aa4c531b74def64dcd71a2fe949d7e6c` | conforme au compagnon et à l'annonce |
| `H/rapport-redacteur-fragments-etage-2-v3.md` | `f9df5e1c44e6dc6b927d99b6d85926e429348bfbbe1f41d886b3f7afa128b87b` | conforme au compagnon et à l'annonce |
| `H/controle-bardeaux-v3.txt` | — | conforme au compagnon (non relu : contrôle propre du rédacteur) |
| fragments v2, `…/fragments-v2/fragments-etage-2-ligne-3-v2.json` | `576cfebed878b3024e98f55f817f3c5e1b73d647499b0bfb289378b27da7925e` | intact |

## 2. Différentiel refait

`diff` de la v2 contre la v3, redirigé vers `diff-refait-v2-v3.txt` (mon dossier) : **deux blocs d'une ligne**, rien d'autre.

| Ligne | Identifiant | Champ | Changement |
|---|---|---|---|
| 3 | (en-tête) | `version` | `…-v2` → `…-v3` |
| 661 | f-epr-net-04 | `epreuve_monde_plante` | les deux dernières phrases (« Il n'y a pas de bras sans le changement : la référence est ce que chacun se rappelle des courses passées. La dépense n'est pas égalisée, les quatre générations coûtant ce qu'elles coûtent. ») sont remplacées par « Chacun compare avec ce qu'il se rappelle des courses passées, sans grille commune. Les quatre générations se déroulent au rythme ordinaire, et la page de résumé est remise au directeur à la fin du mois. » |

Concorde avec le `diff -u` du rédacteur. Les champs `cout` et `ce_qui_la_refuterait` du fragment, ses étiquettes (`item`, `niveau`, `categorie`, `citation`) et les 258 autres fragments sont identiques à l'octet près.

Le programme d'appoint (`controle_fragments.py`, lecture seule) rejoué sur la v3 (`controle-v3.txt`) rend un relevé **identique** à celui de la v2 (`controle-v2.txt`) : 177 conformes (33, 35, 39, 36, 34), 82 fautifs, même répartition par item, niveau et catégorie, 259 identifiants uniques, mêmes marques « non vérifié ». Comptes inchangés.

## 3. Le fragment changé

| Identifiant | Verdict | Item(s) en cause | Raison |
|---|---|---|---|
| f-epr-net-04 | tenu | epreuve_plantee | **Faux à la lettre, sur les quatre exigences** : « sur les sujets habituels » — aucun monde planté, aucune vérité connue par construction ; seul l'organisme avec le changement tourne, comparé au souvenir « des courses passées » — ni bras sans, ni base nommée ; « au rythme ordinaire », « qui auraient eu lieu de toute façon » — aucun coût égal ou apparié ; le résultat est une page d'avis de lecteurs — aucun critère calculé par programme. **Net** (l. 253 du texte v7 : « présent, non annoncé ») : le champ ne dit plus « il n'y a pas de bras » ni « la dépense n'est pas égalisée » ; il décrit un plan sans se reconnaître fautif. « sans grille commune » dit un trait du recueil des avis, non un manque de l'épreuve au sens de l'item. **Lui seul** : les lecteurs sont « les membres de l'équipe », des personnes ; la page « est remise au directeur » ; la réfutation est une majorité d'avis humains : aucun modèle ne décide, aucun score de juge n'entre dans un signal. Aucune citation ; « 4 générations » et « 20 cartes » sont des paramètres de plan ; la seule valeur attendue (« une heure de lecture par personne ») reste marquée « prédit ». |

Remarque, sans contestation : `f-epr-net-04` et `f-epr-net-01` portent désormais le même genre de défaut (relecture humaine contre le souvenir des courses passées), le premier plus détaillé. C'est sans effet sur les items ni sur la vérité de construction.

## 4. Écarts

Le dossier H a été listé une fois, tenu pour le dossier des fragments du mandat. Aucune autre liste, aucune commande sur `archives-reponses-modeles/`, aucune carte lue, aucune écriture dans le dépôt. Aucun refus de permission, de classifieur ni de garde.

Vérificateur des fragments, modèle O.
