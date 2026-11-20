# Contrôle de l'additif 2 v2 (recréation de la relance de l'instance 1), par différentiel

**Verdict : scellable dès qu'on aura ajouté la phrase du point ouvert, ci-dessous.** Ce n'est qu'une phrase : il ne faut pas une nouvelle contre-lecture.

## Empreintes
- additif 2 v2 : 598e702289be0bbc38217781a363c323b37bebb3504a02550070cfa7e84e0632, égale à l'annoncée (598e7022…) ;
- différentiel v1 → v2 : 804274f54fef9ac9dcd79ecf6fbc905bfb9a53848400c98fb0ab3d8768385d91, égale à l'annoncée (804274f5…) ;
- additif 2 v1 : toujours d73a3226…987990.

Le différentiel est fidèle : refait par `diff -u` entre la v1 et la v2, il est identique au fichier fourni. Il ne touche que l'en-tête (titre « v2 », ligne d'état), mes six couples et la section 5 qui en découle. Les faits, la section 4 et la section 6 ne bougent pas.

## Mes six couples

| couple | levé ? | où |
|---|---|---|
| 1. Traces hors de l'espace des branches de la formation | levé | section 2, pas 3 : branche hors de `donnees/barreau5-familles-jumelles-v1-formation…`, jamais réunie, aucun nom de marche `…-b5f-formation-1-x1` sous `donnees/` ; « Pourquoi cet ordre » ; section 5 |
| 2. Ordre des gestes, seconde condition après la destruction | levé | section 2, six pas dans l'ordre demandé ; condition 2 « relevée après la destruction » |
| 3. Passage remplacé non nommé | levé | ligne neuve de la table de la section 3 |
| 4. Compteur de l'instance recréée | levé | « le cumul de l'instance recréée compte depuis sa création ; la dépense de la première tentative n'y entre pas, elle reste au compteur commun » |
| 5. « Sans ouvrir aucune sortie » | levé | « sur les seules lignes d'état de l'amorce … et sur `git ls-remote`, sans ouvrir aucune sortie de la marche » |
| 6. Cause invoquée | levé | « perte du réseau de l'hôte, assimilée à la perte de l'hôte » |

## Le point qui n'était pas vérifié
Tu m'as attesté le passage de l'amorce : `scripts/amorce_b5f_formation_v1.sh`, commit de course `4bdf0d22…`, ligne 282. La citation qu'en fait l'additif est cohérente avec ce qu'elle doit garder. `git ls-remote --exit-code` rend 2 quand la branche est absente : seule cette issue laisse partir l'amorce. Une branche présente, ou un dépôt injoignable, l'arrête. La phrase « la seconde condition est aussi tenue par le code » est donc juste. Le point est levé, sur ton attestation.

## Aucune erreur introduite
Une seule remarque, mineure et facultative. Le nom pris pour exemple, `traces/barreau5-formation-instance-1-x1-premiere-tentative`, contient la suite « formation-instance-1-x1 ». Une réunion de branches faite par motif sur ce nom pourrait le ramasser. La règle « jamais réunie » suffit déjà ; un nom sans cette suite serait plus sûr, par exemple `traces/barreau5-relance-1-premiere-tentative`.

## Point ouvert du rédacteur : un seul mot de Lazar couvre-t-il l'additif et la destruction ?
L'additif ne le dit pas. Il dit « Il attend le mot de Lazar » pour l'additif, puis « destruction … sur le mot de Lazar » au pas 4, sans dire s'il s'agit du même mot. Si Lazar répond seulement à l'additif, la destruction resterait en suspens à la marge de 07:30:16Z.

Par ailleurs, l'arrêt sans destruction ne demande aucun mot. C'est le geste que le plan prescrit lui-même pour un versement non prouvé (« arrêtée sans être détruite »), et l'arrêt d'une instance sans tâche est de routine (R10). Le faire tout de suite coupe la dépense de calcul, et ôte tout risque qu'un versement repris pousse la branche de sortie avant le mot de Lazar.

Phrase proposée, à ajouter en tête, après « Il attend le mot de Lazar … » :

> Un seul mot de Lazar accorde à la fois cet additif et la destruction de la première tentative (`61655405`, pas 4 de la section 2) ; la session mère le lui demande en une seule question, et le consigne en une ligne du registre des accords qui nomme les deux. Les pas 1 à 3 (arrêt par identifiant, sans destruction ; inventaire ; versement prouvé des traces) n'attendent pas ce mot, comme le prévoit le plan pour un versement non prouvé ; les pas 4 à 6 l'attendent.
