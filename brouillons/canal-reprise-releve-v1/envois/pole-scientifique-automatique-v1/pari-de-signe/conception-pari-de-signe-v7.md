# Le pari apparié borné — conception v7, corrections locales après la contre-lecture de la v6

Lignée conv-audit (instance du 27 octobre 2026 ; servie par Opus 5.5), rédaction commencée après le relevé `date -u` de
21:35:27 UTC. **Remplace la v6** (`f21982cd…`, gardée, R12) par des **corrections locales**, comme la contre-lecture de
la v6 le demande (sous-agent neuf Fable 5.1 ; `contre-lecture-v6/rapport-contre-lecture-pari-signe-v6.md`, `490100af…`,
script `82edb8fb…` et sortie `7a6cd572…` dans le même dossier ; verdict : « D-S25 bis est opératoire et valide », le code
la met en œuvre, deux points touchent la garantie **hors** de D-S25 bis — K6-1 et K6-2 —, deux lectures trompeuses, une
option manquante à D-S29, un essai qui pouvait passer pour une mauvaise raison ; « amender en v7 par des corrections
locales, pas refaire »). Delta de la v6 : ce qu'elle ne nomme pas reste tel quel en v6 (et, par elle, en v5, v4, v3).
Exploratoire (R-546) ; décisif dès qu'il sert G1 (R1, R2, R13). Code : v7, version 24 (section 3).

## Verdict (ce que change la v7)

1. **D-S26 bis complétée (K6-1)** : les fiches relues après une panne confirmée, et le nouveau tirage du témoin, entrent
   dans la **famille de la génération où elles sont lues** (comptées dans m_{g′}, budget α_{g′}/m_{g′}) ; la quantité
   garantie est **l'union d'avant les retraits** ; les fiches retirées sont **exclues des lectures suivantes**. Codé
   (`Course.retirer`, `promues_rapportees`).
2. **Contrat d'abandon (K6-2 ; D-S25 bis (2))** : la valeur gelée est celle d'après la **dernière partie observée avant la
   décision**. Codé : une partie pour une fiche gelée est refusée (plus jamais ignorée en silence) ; l'abandon exige la
   partie de la génération courante, ou la déclaration « avant toute issue de cette génération » ; une partie par fiche et
   par génération ; une lecture par génération (la lecture ferme la génération).
3. **Condition de la preuve dite exactement (K6-3)** : « sous dépendance quelconque entre fiches ; entre générations, chaque
   partie est une e-valeur **conditionnelle au passé de toute la course** (unités fraîches tirées de la population, mise
   prévisible, parties disjointes) ».
4. **D-S29 : une option (d) ajoutée, comme nœud (K6-9)** ; D-S29 et D-S10 articulées ; contrainte de D-S30 (a) sur le brief
   du mode tenu à l'écart.
5. **Lectures et définitions corrigées (K6-5, K6-7, K6-8, K6-10, K6-11, K6-12)** ; essais renforcés (K6-6).

## 1. Corrections, section par section de la v6

### D-S25 bis (K6-1, K6-2, K6-3, K6-11)
- (1), ajouter : « Plusieurs familles entrant à une même génération (fiches nouvelles, relecture d'une strate, nouveau
  tirage d'un témoin) **se partagent α_g** : Σ des α_c de la génération ≤ α_g. »
- (2), remplacer « il est gelé quand la fiche est abandonnée ou promue » par : « il est gelé quand la fiche est abandonnée
  ou promue, **à sa valeur d'après la dernière partie observée avant la décision** : une décision d'abandon qui a vu la
  partie d'une génération gèle la fiche après cette partie, jamais avant (sinon la valeur gelée vaut en espérance
  E(g−1)·max(1, e_g), qui n'est plus une e-valeur : 1,77 par partie jetée dans le monde A′ à 20 pas, contre-lecture v6,
  § 4). Une partie par fiche et par génération. »
- (3), ajouter : « La lecture **ferme** la génération. Lire plus souvent resterait valide (temps d'arrêt plus fins) ; la
  règle est une lecture par génération, tenue par le code. Une abandonnée gelée **sous** son seuil peut être promue plus
  tard quand k* grandit : c'est voulu et valide (processus arrêté). Nature de la règle e-BH : une fiche sans preuve
  (E = 1) est promue si k* ≥ 1/b_i ; la garantie porte sur l'union, et la lecture e-Bonferroni protège ce qui sort. »
- (5), remplacer « sous dépendance quelconque entre fiches et entre générations » par : « sous dépendance quelconque
  entre fiches ; entre générations, à condition que chaque partie soit une e-valeur conditionnelle au passé de toute la
  course (unités fraîches tirées de la population, mise prévisible, parties disjointes) — c'est ce que la preuve
  utilise ». Et ajouter : « **la quantité garantie est l'union d'avant les retraits** (D-S26 bis). »

### D-S26 bis (K6-1, K6-7)
- (3), remplacer « comme des fiches **nouvelles** (nouveaux budgets, nouvelle entrée) » par : « comme des fiches
  nouvelles **de la génération g′ où elles sont relues** : elles entrent dans sa famille (comptées dans m_{g′}, budget
  α_{g′}/m_{g′}, ce qui réduit d'autant le budget des autres fiches nouvelles de g′) ; aucune réserve hors de la suite de
  dépense. » (Une réserve scellée au gel, α = Σ_g α_g + α_réserve, serait aussi valide : écartée pour la simplicité.)
- Le **nouveau tirage du témoin** entre dans la famille de la génération où il est lu, comme **témoin faux** (compté dans
  m_{g′}) : c'est ce qui le rend « lu à la même règle ».
- Ajouter (5) : « **Retrait** : une fiche retirée est marquée (motif, jamais effacée), gelée et **exclue des lectures
  suivantes** (valide : cela ne fait que réduire les promotions de chaque lecture) ; si elle était promue, elle reste dans
  l'union garantie et sort de l'ensemble rapporté, qui porte la réserve de la suspension : la probabilité d'au moins une
  fausse promotion ne peut que baisser ; le taux de fausses découvertes de l'ensemble rapporté n'est pas couvert par la
  preuve. »
- **K6-7** : « α/m s'il est seul promu ; jusqu'à α·k/m dans une strate qui porte k promotions vraies » devient : « **au
  plus** α/m s'il est seul promu ; jusqu'à **α·k/m avec k le nombre total de promotions de la lecture, témoin compris**
  (k = 4 pour 3 vraies : seuil 5/(0,05·4) = 25, borne 0,04) ».

### D-S27 (K6-8)
« Elle coïncide avec celle de N-054 si aucune unité ne dépasse m_max, ou si v ne dépend pas de la longueur » devient :
« elle a **le même signe** que celle de N-054 dans ces deux cas ; son **échelle** est E[m_t]/m_max (aucune unité au-delà
de m_max) ou E[min(m_t, m_max)]/m_max (v indépendant de la longueur) : la borne basse rapportée porte sur E[v′] et se
déclare avec cette échelle, jamais comme un gain de rappel par épisode. »

### D-S24 (K6-10)
Ajouter : « Le plafond G_max ne se relève jamais après une lecture. Une course **reprise** après un arrêt réutilise les
créneaux α/G_max restants (même course, même G_max) ; sinon c'est une course nouvelle, avec son propre α et ses propres
fiches. Perdre le reliquat des générations non faites est **un choix** (une réaffectation prévisible, déclarée avant la
lecture de la dernière génération, serait aussi valide). »

### 4, ligne H1 — D-S29 et D-S30 (K6-9)
- D-S29, option ajoutée : **(d) le mode tenu à l'écart rapporté, hors de la décision de H1**, par symétrie avec D-S10
  (« mode tenu à l'écart hors décision » pour G1). Elle répond au problème soulevé en v6 (un mode conçu tard et petit
  décide seul de H1), mais **s'écarte de la lettre du point 4 de N-054** (« dans les autres modes », qui comprend le mode
  tenu à l'écart) : ce n'est pas une lecture, c'est une **modification de décision** — nœud pour Lazar.
- D-S29 (a) et D-S10 ne se contredisent pas : **D-S10 vaut pour la porte G1**, **D-S29 pour la revendication de H1** ;
  objets différents.
- D-S30 (a) : le **brief du mode tenu à l'écart** doit produire des unités de la strate « diffus, flou » en nombre suffisant
  et la **coder sans connaissance des moniteurs** ; sinon (a) est inapplicable à ce mode. Une ligne au poste de devis.

### 3 (le code, K6-5)
« `ebh_pondere` … refuse une somme de budgets au-dessus de α » était faux (elle refusait au-dessus de 1 ; le contrôle
≤ α était dans `Course.entrer`) : en version 24, `ebh_pondere(..., alpha=…)` refuse au-dessus de α quand α est donné
(au-dessus de 1 sinon), et `Course.lire` le donne.

### En-tête (K6-12)
- La sortie reproduite du script de la contre-lecture v5 est **versée** :
  `contre-lecture-v5/reproduction-conv-audit-v1/sortie-reproduite.json` (`34cf6eb0…`), identique à `285e222f…` hors
  `duree_secondes`.
- Les heures de modification « en avance d'une heure » vues par les contre-lecteurs sont un **affichage** : le conteneur a
  `TZ=Europe/Paris`, et `ls` affiche l'heure de Paris (UTC+1 depuis le 25 octobre) ; les heures des en-têtes sont celles
  de `date -u`.

## 2. Décisions (v6, avec D-S25 bis, D-S26 bis, D-S24, D-S27 précisées, et D-S29 (d))

| décision | recommandation (confiance) |
|---|---|
| D-S24 (précisée, K6-10) | uniforme α/G_max sur un plafond scellé, jamais relevé ; reprise = créneaux restants ; reliquat perdu par choix (0,75) |
| D-S25 bis (précisée, K6-1 à K6-3) | budget d'entrée gardé à vie ; familles d'une génération se partageant α_g ; gel après la dernière partie observée ; une partie et une lecture par génération ; condition conditionnelle au passé ; union d'avant les retraits (0,85) |
| D-S26 bis (complétée, K6-1, K6-7) | relecture et nouveau tirage du témoin dans la famille de g′ ; retraits marqués, exclus des lectures, union garantie d'avant les retraits (0,7) |
| D-S27 (précisée, K6-8) | plafond ; estimande « plafonnée » de même signe, échelle déclarée avec la borne basse (0,8) |
| D-S29 (nœud de porte) | (a) dans chacun des autres modes, mode tenu à l'écart compris (lecture) ; (b) ; (c) ; **(d) mode tenu à l'écart hors décision (modification de N-054 point 4 : nœud)** ; recommandation inchangée **(a)**, avec le dimensionnement du mode tenu à l'écart ; (d) si ce dimensionnement est refusé (0,55) |
| D-S30 (nœud de porte) | (a) strate « diffus, flou » de chaque mode, avec la contrainte sur le brief du mode tenu à l'écart (0,6) |

Défauts sous 48 heures : les recommandations, sauf les nœuds de porte (D-S10, D-S11, D-S20, D-S29, D-S30) et le poste
de devis.

## 3. Code (v7, version 24)

`pole/pari_apparie.py` : `ebh_pondere(..., alpha=None)` ; `Course` : une partie par fiche et par génération, partie
refusée pour une gelée, `abandonner(fiche, trajectoire_log=None, avant_partie=False)` (contrat de D-S25 bis (2)),
lecture qui ferme la génération, `retirer(fiche, motif)` (marque, gèle, exclut), `promues_rapportees()`, `bonferroni()`
sans les exclues. Essais (`essais/test_v7_pari_apparie.py`, quatre de plus, et l'essai du monde A′ affirme désormais
qu'il y a des promotions — attendu environ 11 sur 400, K6-6) : contrat d'abandon (cas sain, artefact refusé, partie
passée avec la décision, déclaration « avant partie », partie refusée pour une gelée, une partie par génération) ;
retrait (union garantie inchangée, ensemble rapporté réduit, exclusion qui empêche une promotion que la retirée aurait
permise) ; budgets entre α et 1 refusés quand α est donné ; ex æquo au bord (trois fiches à 1/3, toutes promues) et
abandonnée promue plus tard par k*. **259 essais passent.**

## 4. Ce que la v7 laisse ouvert (dit)

Comme la v6 : le lien avec le cycle (l'engagement « apparié » et le monde sur banque de scores existent, v7 versions 22 et
23, mais le proposeur, le gabarit et la mémoire n'y sont pas branchés) ; la règle n'est simulée que dans des mondes
illustratifs ; D-S26 bis n'est pas simulée (le retrait est codé, la panne confirmée n'est pas encore déclenchée par le
noyau) ; contrôle 18 non simulé ; R7 (e-LOND, Maurer et Pontil) ; nœuds de porte au préenregistrement de G1.
