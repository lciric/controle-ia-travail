# Vérification de la v3 du préenregistrement de l'épreuve de la garantie de seuil (troisième passe, R2)

- Contre-lecteur : le même qu'aux passes 1 et 2, sous-agent Opus 5.5. Date : 2026-11-24.
- Pièce relue : `prereg-seuil-chantier3-v3.md`, empreinte `4f3ee5c3a10b55d3a43a443b1418a006819d6e931f13247785b7afbf655b20e3`, vérifiée sur disque. Base de la comparaison : la v2, `bd58748a8ac83f2757e551e344d0c3f3474c4626d712267af2eea2050aaa4085`.
- Garanties : aucun fichier modifié, rien de lancé, aucun tirage.

## Verdict

**Scellable.**
- La v3 ne diffère de la v2 que par les sept lignes annoncées, plus l'erratum ajouté en fin de pièce.
- Le défaut majeur R1 est corrigé, et ses chiffres se recalculent.
- Les réserves R2 et R3 sont corrigées. La réserve R4 est vérifiée ici, par la comparaison des deux textes demandée.
- Le validateur ne signale plus rien.
- Les trois remarques ci-dessous sont mineures et ne bloquent pas le scellement.

## 1. Comparaison de la v2 et de la v3, faite par programme

J'ai comparé les deux textes avec `diff` et avec `difflib.SequenceMatcher`. Seuls les passages suivants changent :
- six remplacements, aux lignes 98, 123 et 124, 147, 166, 174 et 193 ;
- un ajout de quatorze lignes, de 212 à 225 (l'erratum v3).

La v3 compte 225 lignes, contre 211 pour la v2. Rien d'autre n'a changé : toutes les autres lignes sont identiques. Chaque passage modifié correspond à une ligne de l'erratum.

## 2. Défaut R1, la garde de l'écart bilatéral : corrigé

La vérité est désormais écrite pour un seuil d'écart s : D*(s) = 1 − [P(|A − nρ_ε| ≤ ns/(γW))]^K. Cette formule est exacte, puisque sur ce témoin a = 0 et x̂_k − x_k = γW(ρ − A_{k−1}/n).

Recalcul exact, au seuil d'épreuve s = ε/2 et sous le plan ρ(ε) :

| Grandeur | Valeur |
|---|---|
| Vérité | 0,25517 (25 517 comptes) |
| Côté haut seul | 0,12923 |
| Côté bas seul | 0,14370 |
| Écart à la vérité | 12 594 et 11 146 comptes |
| Tolérance | 692,3 |

Toutes ces valeurs sont conformes. Le seuil nominal ε reste éprouvé comme cas sain (2,7 × 10⁻⁵). Le compteur prend son seuil en paramètre, et la métrique emploie s = ε. La ligne de la table des gardes est cohérente avec ces choix.

## 3. Réserves mineures et section Contre-lecture

**R2, le rôle de l'écart bilatéral : corrigé.**
- L'écart bilatéral est sorti du verdict du point sur (E) et (C), de « la garantie tient », de « garantie réfutée » et de l'ordre de priorité.
- La case « non concluant » est restreinte à V et V'.
- Il n'y a plus de conflit avec le verdict d'ensemble.

**R3, la fréquence de référence et le lot du bloc 8 : corrigé.**
- La fréquence de référence est celle de la prolongation quand la classe finale en vient, avec 10⁻⁶ au lieu de 10⁻⁵ dans la variance : c'est juste pour 10⁶ tirages. Sinon, c'est celle du premier tirage.
- Le lot du bloc 8 est défini : `random(size=(K, n))` par répétition, et un audit si le tirage est sous ρ_k, ce qui donne bien des Bernoulli(ρ_k).

**R4, la comparaison des textes : faite ici.** Voir le point 1.

**Section Contre-lecture : exacte.**
- L'entrée 1 cite la v1, `889c1153…`, et le rapport, `841171cc…`.
- L'entrée 2 cite la v2, `bd58748a…`, et le rapport, `da431979…`. Son résumé du verdict est fidèle.

## 4. Validateur

Sur la copie `copie-prereg-v3.md`, `controle_ia.prereg.problemes` renvoie `[]` : aucun défaut.

## 5. La mention « v2 » dans le titre et l'en-tête

Elle n'empêche pas le scellement :
- `scellement.sceller` scelle le contenu et le nom du fichier, et n'interprète pas le titre ;
- R12 tient, parce que la version est dans le nom (`-v3`) et que l'erratum le dit ;
- le validateur l'ignore.

Elle reste source de confusion à la lecture. La ligne 3 dit en effet « Cette v2 remplace la v1 ». C'est assumé et documenté. Je recommande de la laisser telle quelle : la changer obligerait à refaire la comparaison des textes.

## Remarques mineures, non bloquantes

1. **Statut de l'écart bilatéral.** La section Seuil l'appelle encore « lecture décisive », dans la règle de prolongation et dans la famille « fausse réfutation de (A) ». La table à λ = 1 le dit désormais « descriptif ». Il n'y a pas d'effet sur les verdicts sur (E) et (C), mais les mots se contredisent. L'audit renforcé, déclenché par « toute réfutation », vaudra donc aussi pour une réfutation de (a), et son contrôle 2 compte la violation, pas l'écart bilatéral. À relever lors de l'analyse, sans réécrire le texte.
2. **Ordre du scellement.** Si la mère inscrit cette troisième passe dans la section Contre-lecture avant de sceller, l'entrée « Contre-lecture 3 » doit porter deux empreintes, sans quoi le validateur refusera :
   - la v3 relue, `4f3ee5c3a10b55d3a43a443b1418a006819d6e931f13247785b7afbf655b20e3` ;
   - le présent rapport.

   On scelle ensuite le texte complété, puis on vérifie que seule cette entrée a changé par rapport à `4f3ee5c3…`.
3. **Durée de calcul.** Les tirages épisode par épisode du bloc 8 (de l'ordre de 4 × 10¹⁰ uniformes pour les contrôles systématiques) alourdissent la course. L'estimation reste de quelques heures, sous l'arrêt à 12 heures, mais elle est à surveiller.

## Commandes lancées

- `sha256sum` sur la v2 et la v3.
- `diff` v2 contre v3.
- `python -I -c "difflib.SequenceMatcher(...)"` sur les mêmes textes.
- `python -I cl/dfix.py` : vérité et côtés seuls au seuil ε/2.
- `grep` sur `scellement.py`.
- Validateur sur la copie : `problemes('copie-prereg-v3.md')`.
