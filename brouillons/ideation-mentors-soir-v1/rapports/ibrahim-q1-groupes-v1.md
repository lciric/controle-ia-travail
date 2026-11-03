# Groupes des fiches d'idées d'expériences — mentore Lujain Ibrahim, question 1 — v1

Groupeur neuf, aveugle au classement. Seul fichier lu : `/home/claude/scratch/soir-rapport/ibrahim-q1/piste/fiches-a-grouper-v1.json` (sha256 `d1b819685d646cc75b5950dc64019e3874089b7203cb0147f4e59a90a05cd366`, vérifiée à 2026-11-03 13:50:37 UTC avant lecture). 14 fiches (IB-01 à IB-14).

## Définitions des groupes

Écrites à **2026-11-03 13:54:03 UTC** (heure de `date -u`), avant toute affectation ; ce fichier a été créé avec cette seule rubrique, puis complété sans la modifier.

Chaque groupe est un type d'expérience défini par la question que la première expérience tranche.

### 1. Survie de la persona au renforcement vérifiable
- **Définition.** Question tranchée : ce que l'entraînement de caractère a installé (l'écart persona − base) survit-il à un apprentissage par renforcement dont la récompense est vérifiable et ne contient aucune préférence humaine ?
  La première expérience fait passer persona et base par ce renforcement, puis compare l'écart avant et après.
- **Critère.** L'énoncé prédit l'évolution, entre avant et après un renforcement à récompense vérifiable, d'un écart persona − base (quelle que soit la mesure : validation, erreur, comportement de persona, capitulation, y compris ventilée par domaine), et l'enjeu déclaré est la persistance ou l'effacement de la persona.

### 2. Le signal de préférence comme cause
- **Définition.** Question tranchée : l'optimisation sur des préférences humaines cause-t-elle ou amplifie-t-elle la sycophantie, par rapport à un signal qui n'en contient pas ?
  La première expérience fait varier la nature de la récompense (préférences, vérifiable, étiquettes permutées, non informative), ou applique un renforcement par préférences, et lit une mesure de sycophantie.
- **Critère.** L'énoncé oppose des types de récompense, ou prédit l'effet d'un seul type de renforcement sur une mesure de sycophantie (gain g, erreur sous fausse croyance) lu pour ou contre la cause « préférences » ; un renforcement par préférences dans l'énoncé suffit à exclure le groupe 1.

### 3. Mécanisme du déplacement sous pression
- **Définition.** Question tranchée : par quel processus la note ou le verdict du modèle se déplace-t-il sous pression (mélange ou contraction, médiateur, dimension visée par la pression) ?
  La première expérience, sans entraînement nouveau, analyse ou manipule les réponses pressées d'un même modèle.
- **Critère.** Aucun entraînement nouveau et aucun contraste persona − base décisif ; l'énoncé porte sur la forme des distributions de notes, sur un médiateur du déplacement, ou sur la cible de la pression.

### 4. Validité de l'instrument
- **Définition.** Question tranchée : l'instrument (juge, classifieur, détecteur) lit-il ce qu'il prétend lire (position, sycophantie, persona) plutôt que le style, le registre ou le lexique ?
  La première expérience confronte l'instrument à une référence (annotation humaine, prédicteurs mécaniques, autre instrument).
- **Critère.** La comparaison décisive de l'énoncé oppose un instrument à une référence ou à un autre instrument ; le résultat est une propriété de la mesure, non du modèle.

### 5. Prise initiale de la persona
- **Définition.** Question tranchée : avant tout entraînement nouveau, que change déjà la persona (capitulation factuelle, point fixe ou gain de la loi d'attraction), et la manipulation a-t-elle prise sur la mesure ?
  La première expérience compare des points de contrôle existants, persona contre base, sans rien entraîner.
- **Critère.** Aucun entraînement nouveau ; le contraste décisif de l'énoncé est persona contre base sur des points de contrôle existants, pour une mesure de sycophantie ou un paramètre de la loi d'attraction.

### Règle de départage (fixée avec les définitions)
L'idée principale se lit dans l'énoncé (ce que la prédiction compare) ; le mécanisme ne départage qu'en cas d'égalité entre deux critères. « Second choix » : la fiche relèverait presque autant d'un autre groupe.

## Affectations

Écrites à partir de **2026-11-03 13:56:34 UTC** (heure de `date -u`), après les définitions. Les 4207 premiers octets de ce fichier sont l'état « définitions seules » (sha256 `103833ca968798dbba7a4c36769ffa3a60d28f0da5902aaeb9948d953bdeb882`, contrôle : `head -c 4207 groupes-v1.md | sha256sum`) ; la suite a été ajoutée sans réécrire ce début. Définitions et critères identiques mot à mot à ceux de `groupes-v1.json` (contrôle par script).

| Fiche | Groupe | Raison | Second choix |
|---|---|---|---|
| IB-01 | Survie de la persona au renforcement vérifiable | L'énoncé prédit que l'écart persona − base de validation injustifiée d'une conduite survit au renforcement à récompense vérifiable (perte d'au plus 5 points). | — |
| IB-02 | Survie de la persona au renforcement vérifiable | L'énoncé prédit la conservation de l'écart de comportement persona − base après renforcement à récompense vérifiable, à divergence de Kullback-Leibler appariée ; rivale explicite : le renforcement efface la persona. | — |
| IB-03 | Survie de la persona au renforcement vérifiable | L'énoncé prédit que le renforcement à récompense vérifiable change l'écart persona − base de capitulation davantage dans le domaine social que dans le factuel : survie de la persona ventilée par domaine. | — |
| IB-04 | Validité de l'instrument | L'énoncé confronte le classifieur de persona et le juge de sycophantie à des paires annotées par des humains et à des prédicteurs mécaniques : propriété de la mesure (position ou registre). | — |
| IB-05 | Mécanisme du déplacement sous pression | L'énoncé départage mélange et contraction par la forme des distributions de notes par item, sur les données de la campagne 1, sans entraînement ni persona. | — |
| IB-06 | Le signal de préférence comme cause | L'énoncé oppose la récompense vérifiable à une récompense non informative à divergence égale sur le gain g, pour argumenter sur la cause « préférences » ; la fiche exclut elle-même la lecture « persistance de la persona ». | Survie de la persona au renforcement vérifiable — le plan applique le renforcement vérifiable aux points de contrôle de persona et prédit une invariance. |
| IB-07 | Le signal de préférence comme cause | L'énoncé applique un renforcement contre un modèle de récompense appris sur des préférences et prédit une amplification, non une addition, de l'erreur de la persona ; le mécanisme vise la cause « préférences ». | Survie de la persona au renforcement vérifiable — la fiche mesure, comme ce groupe, l'évolution d'un écart persona − base à travers un renforcement. |
| IB-08 | Prise initiale de la persona | Sans entraînement nouveau, l'énoncé compare persona et base sur les paramètres de la loi d'attraction (point fixe c déplacé, gain g inchangé). | Le signal de préférence comme cause — le mécanisme lit le résultat contre l'a priori « le gain vient de l'optimisation des préférences ». |
| IB-09 | Le signal de préférence comme cause | L'énoncé oppose récompense apprise sur des préférences, récompense vérifiable à divergence appariée et étiquettes permutées, sur le gain g : manipulation directe de la cause supposée. | — |
| IB-10 | Prise initiale de la persona | Sans entraînement, l'énoncé compare la persona Sycophantic à la base et à des témoins sur l'erreur sous fausse croyance : la manipulation a-t-elle prise avant tout renforcement. | — |
| IB-11 | Mécanisme du déplacement sous pression | Sans entraînement ni persona, l'énoncé teste un médiateur (refus, prise de distance) de la descente sous éloge des items bien notés. | Validité de l'instrument — le juge note environ 3 les refus et les prises de distance : la descente peut être une propriété de la notation. |
| IB-12 | Validité de l'instrument | L'énoncé confronte le juge à un détecteur lexical gelé sur des items disjoints : propriété de la mesure (le juge est-il remplaçable). | Mécanisme du déplacement sous pression — « la loi est portée par le lexique » affirme aussi comment le déplacement s'exprime. |
| IB-13 | Mécanisme du déplacement sous pression | Sans entraînement ni persona, l'énoncé manipule la cible de la pression (forme ou fond) à intensité appariée et compare les gains : capitulation par dimension ou globale. | — |
| IB-14 | Survie de la persona au renforcement vérifiable | L'énoncé prédit la survie, après renforcement à récompense vérifiable, de l'écart d'erreur persona − base sous fausse croyance, évalué hors du domaine de la récompense. | — |

## Comptes par groupe

| Groupe | Fiches | Nombre |
|---|---|---|
| Survie de la persona au renforcement vérifiable | IB-01, IB-02, IB-03, IB-14 | 4 |
| Le signal de préférence comme cause | IB-06, IB-07, IB-09 | 3 |
| Mécanisme du déplacement sous pression | IB-05, IB-11, IB-13 | 3 |
| Validité de l'instrument | IB-04, IB-12 | 2 |
| Prise initiale de la persona | IB-08, IB-10 | 2 |
| **Total** | | **14** |

Fiches à second choix (5) : IB-06, IB-07, IB-08, IB-11, IB-12.

## Limites

1. **Frontière entre les groupes 1 et 2 fixée par la nature de la récompense.** Le groupe 1 est restreint au renforcement à récompense vérifiable (règle écrite avec les définitions). IB-07 mesure, comme le groupe 1, l'évolution d'un écart persona − base à travers un renforcement, mais sa récompense vient de préférences : il va au groupe 2. Avec un groupe 1 « tout renforcement », IB-07 aurait été à égalité entre 1 et 2.
2. **IB-06 à cheval.** Son plan est celui du groupe 1 (renforcement vérifiable appliqué aux points de contrôle de persona, prédiction d'invariance) ; sa mesure (gain g, sur base et persona) et son argument (cause « préférences ») sont ceux du groupe 2, et la fiche écarte elle-même la lecture « persistance de la persona ».
3. **Second choix d'IB-08 porté par le mécanisme, non par le plan.** Aucune récompense n'y est manipulée ; le lien au groupe 2 vient de la lecture proposée (a priori « le point fixe vient de l'imitation, le gain de l'optimisation des préférences »), que la fiche dit elle-même impure : Open Character Training mêle optimisation directe des préférences et ajustement supervisé.
4. **Thème transversal non érigé en groupe : fragmentation du construit (sycophantie sociale contre factuelle).** Présent dans IB-03 (groupe 1), IB-08 et IB-10 (groupe 5) ; la question que tranche la première expérience diffère d'une fiche à l'autre, d'où la dispersion.
5. **Thème transversal : forme contre fond (style contre position).** Objet du groupe 4 (IB-04, IB-12), mais aussi justification de la mesure dans IB-01 (validation des émotions contre validation de la conduite), IB-03 (persona qui persisterait comme style), IB-13 (le juge agrège thèse et écriture) et IB-11 (le juge note environ 3 refus et prises de distance). Ces facettes de mesure n'ont changé aucune affectation, la comparaison décisive de ces énoncés portant sur le modèle ; seule IB-11 reçoit le groupe 4 en second choix (IB-13 : facette jugée moins forte, sans second choix).
6. **Dépendances non encodées.** Un seul groupe par fiche ne rend pas les prérequis : IB-04 (groupe 4) conditionne la lecture des fiches du groupe 1 (sinon « persistance de la persona » ne mesure qu'un registre) ; IB-10 (groupe 5) vérifie que la mesure factuelle a prise avant les renforcements d'IB-07 et d'IB-14.
7. **Groupes 3 et 4 hors persona.** IB-05, IB-11, IB-12 et IB-13 portent sur la loi d'attraction et le juge appliqués au modèle Instruct de la campagne 1, sans entraînement de caractère ni renforcement. Les deux projets de la mentore ne sont pas décrits dans le fichier d'entrée : les groupes ne prétendent pas leur correspondre.
8. **Signes opposés dans un même groupe.** Le groupe 2 réunit une prédiction d'invariance (IB-06 : gain g inchangé sous récompense vérifiable) et des prédictions d'effet (IB-07, IB-09) : le groupe est défini par la question tranchée, non par le signe attendu.
