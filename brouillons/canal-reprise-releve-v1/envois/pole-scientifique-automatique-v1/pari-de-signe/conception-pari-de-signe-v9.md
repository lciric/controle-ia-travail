# Le pari apparié borné — conception v9 : décision de Lazar sur le nœud 1 (G1 contre les bases boîte blanche aussi) et corrections après la contre-lecture de la v8

Lignée conv-audit (instance du 27 octobre 2026 ; servie par Fable 5.1), rédaction commencée après le relevé `date -u` de
23:32:28 UTC. **Remplace la v8** (`3e9609fc…`, gardée, R12) par (a) la **décision de Lazar** du 27 octobre, 23:47 heure de
Paris, sur le nœud 1 (`noeuds-pour-lazar-v1.md`) : **option (b)** (note N-056, proposée à session-depot) ; (b) les corrections
locales demandées par la contre-lecture de la v8 (sous-agent neuf Fable 5.1, `contre-lecture-v8/rapport-contre-lecture-pari-signe-v8.md`,
`b2edabeb…` : K7-1, K7-2, K7-3, K7-5, K7-9, K7-10 fermés ; deux chemins restants K8-1 et K8-2 ; « amender en v9 par deux
phrases et une garde »). Delta de la v8. Exploratoire (R-546) ; décisif dès qu'il sert G1. Code : v7, version 26.
**Cette v9 n'est pas encore contre-lue** (à faire, par un sous-agent neuf Opus 5.5).

## Verdict (ce que change la v9)

1. **G1 exige aussi de battre les bases boîte blanche (ii) et (iii) — décision de Lazar (nœud 1, option b).** D-S8 est
   réécrite : la liste d'intersection-union de G1 comprend **chaque moniteur boîte noire de la liste scellée** (N-007 (i)
   et (iv), par action calibré, séquentielles noires, juge robustifié) **et** les deux bases boîte blanche de N-007 : **(ii)
   la cascade de portes** sur les mêmes sondes et **(iii) la sonde sur le dernier état**. Les planchers restent rapportés.
   Conséquences, dites à Lazar et acceptées : (α) G1 porte deux questions (« lire l'intérieur apporte quelque chose » et
   « notre accumulation bat les autres façons de lire l'intérieur ») et **un échec ne dira pas laquelle a échoué** — la
   lecture rapportera donc **chaque composante** de l'intersection-union (quel comparateur a tenu, lequel a cédé) ; (β) la
   puissance est celle du **contraste le plus difficile**, blanc contre blanc, dont l'écart attendu est petit : au devis de la
   couche 2, **plusieurs centaines d'unités sabotées de plus par mode** (à 10 points d'écart, ≈ 100 unités à la fiche seule
   et davantage au seuil m/α ; à 5 points, ≈ 250 ; le pari v2 § 6 : 0,63 à 60 unités et 0,96 à 100 pour 10 points, 0,88 à 250
   pour 5 points) ; (γ) H2 garde ses propres tests de (ii) et (iii) (H2c : additif contre cascade, contre dernier état) —
   G1 et H2c partagent des cellules, pas des fiches : la clé de l'héritage les distingue (comparateurs différents).
2. **Fraîcheur des unités vérifiée par les identifiants, pas par une empreinte (K8-1 ; D-S25 bis (5)).** La course reçoit,
   pour chaque partie, les **identifiants** des unités (banque, partie, unité) et refuse toute **intersection** avec les
   unités déjà lues par la fiche ; une partie sans identité n'est acceptée qu'**explicitement déclarée**, et tracée. La
   disjonction **entre fiches d'une même lignée de clé** (une relance sous un autre nom) reste à la mémoire, qui tient la
   lignée ; tant qu'elle n'est pas codée, « vérifiable pour une répétition exacte par fiche ; disjonction entre fiches à
   l'orchestrateur » est la phrase juste.
3. **La déclaration « sans partie » mensongère rouvre l'artefact entier (K8-2)** : mesuré par la contre-lecture, 0,396 puis
   0,978 d'au moins une fausse promotion sur 10 puis 30 générations (nul complet, monde A′, α = 0,05). Le code la trace
   sans pouvoir la vérifier : **obligation de l'orchestrateur** — le monde **journalise toute partie calculée** (identifiant de
   fiche, identifiants d'unités, empreinte), de sorte que la trace « sans partie » soit confrontable au journal du monde ;
   mieux, le monde remet la partie à la course, pas au décideur.
4. **Mineurs (K8-3 à K8-5)** : un second abandon d'une fiche gelée est **tracé** (sans effet) ; la **règle de combinaison**
   des e-processus sur Λ (moyenne) et la **règle d'arrêt** entrent dans la clé sous un champ « version de l'e-processus »
   (module `pari_apparie`, version 26) ; essais ajoutés : partie sans identité refusée, intersection partielle refusée, Λ
   dans la clé.

## 1. Corrections, section par section de la v8

### D-S8 (réécrite, nœud 1 = b)
« Comparateur de G1 : intersection-union sur toutes les variantes **noires** (précisé en v4 : (ii), (iii) et les planchers
n'en font pas partie) » → « intersection-union sur toutes les variantes noires **et** sur les bases boîte blanche (ii)
cascade de portes et (iii) sonde sur le dernier état (décision de Lazar du 27 octobre, nœud 1 (b)) ; planchers rapportés ;
chaque composante rapportée ». Le § 2.4 bis (lecture du critère de G1) dit désormais : « dépasse celui de **chaque variante
noire de la liste scellée et des deux bases boîte blanche (ii) et (iii)** ».

### § 6 (dimensionnement)
Ajouter : « Sous le nœud 1 (b), la composante la plus difficile de G1 est blanc contre blanc ; son écart n'est pas connu
(aucune mesure), et le § 6 du pari v2 donne la puissance par écart : 20 points → 40 unités, 10 → 100, 5 → 250 à la fiche
seule ; la famille de G1 (m fiches par mode) élève encore le seuil. **Poste de devis** de la couche 2 : plusieurs centaines
d'unités sabotées de plus par mode, à chiffrer avec l'écart blanc-contre-blanc qu'une lecture pilote mesurera. »

### D-S25 bis (5) (K8-1, K8-2)
Remplacer « « Unités fraîches » se vérifie par l'empreinte des unités de chaque partie » par : « se vérifie par les
**identifiants** des unités (banque, partie, unité) : toute intersection avec les unités déjà lues par la fiche est refusée ;
une partie sans identifiants n'est acceptée que déclarée, et tracée ; la disjonction entre fiches d'une même lignée de clé
est tenue par la mémoire (à coder) ». Ajouter à (2) : « La déclaration « sans partie » est à la charge de l'orchestrateur ;
le code la trace sans pouvoir la vérifier ; une déclaration fausse rouvre l'artefact entier (0,40 puis 0,98) ; **le monde
journalise toute partie calculée** pour que la trace soit confrontable. »

### D-S18 (K8-4)
Ajouter à la clé : « version de l'e-processus » (règle de combinaison sur Λ et règle d'arrêt).

## 2. Décisions

| décision | état |
|---|---|
| D-S8 (réécrite) | **décidée par Lazar** (nœud 1 = b) : G1 contre les noires et les bases (ii), (iii) ; planchers rapportés |
| D-S25 bis (précisée, K8-1, K8-2) | identifiants d'unités, intersection refusée, déclaration tracée, journal du monde (0,85) |
| D-S18 (précisée, K8-4) | version de l'e-processus dans la clé (0,85) |
| nœud 2 (intervalle de N-054 point 4) | option (c) **lue** dans les fragments de Lazar du 27 octobre 23:10 — à confirmer d'un mot (N-056) |
| D-S29, D-S30 | nœuds de porte ; D-S29 (a) lue dans les mêmes fragments |

## 3. Code (v7, version 26)

`pole/pari_apparie.py` : `Course.ajouter_trajectoire(fiche, trajectoire_log, unites=None, sans_identite=False)` —
identifiants obligatoires, intersection refusée, `parties_sans_identite` tracées ; `abandonner(..., unites=…,
sans_identite=…)` ; second abandon d'une gelée tracé (`abandons[("redite", fiche)]`). `pole/engagement_apparie.py` :
`evaluer` rend `identifiants_unites` (banque, partie, unité). Essais : intersection partielle refusée, sans identité refusée
puis déclarée et tracée, redite d'abandon tracée, identifiants de l'engagement refusés à la seconde lecture. **262 essais.**
Le champ « version de l'e-processus » de la clé : version 27.

## 4. Ce que la v9 laisse ouvert (dit)

Sa contre-lecture ; la disjonction entre fiches par la mémoire ; le journal des parties par le monde ; K7-6, K7-7 ;
l'écart blanc-contre-blanc à mesurer pour dimensionner G1 (b) ; le lien au cycle.
