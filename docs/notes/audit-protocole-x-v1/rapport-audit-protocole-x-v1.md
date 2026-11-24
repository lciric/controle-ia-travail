# Audit du protocole X comme instrument — rapport v1

Session fille d'audit (Claude Opus 5.5), mandat de la mère `session_01Qi7Gr3Ggccg85kjmP654WC`, règle 9 du protocole X, version 2 (`docs/notes/protocole-x-v2/protocole-x-v2.md`), GO-2026-11-24-44. Écrit le 24 novembre 2026 vers 19:45Z. Branche `audit/protocole-x-v1`. Aucune dépense, aucun appel à un modèle externe, tout sur processeur. Pièce de travail (classe C) ; ses chiffres renvoient aux sorties scellées de `sorties/`.

## Verdict en trois lignes

1. **Rendement nul à ce jour (mesure).** Sur 115 propositions retenues par 20 notes de sortie et synthèses couvrant 23 des 42 courses du collisionneur (464 dollars comptés au total), une seule a été tentée (issue non évaluable) et aucune n'a survécu à une épreuve : le coût par proposition survivante n'est pas défini ; 33 retenues sont « adoptées sans épreuve » et 9 « en préparation ».
2. **Les modèles d'un même fournisseur ne sont pas indépendants (mesure).** Au tour 1, écrit sans voir les autres, les paires Fable–Opus et Argon–Carbon–Neon sont nettement plus proches entre elles (similarité moyenne 0,34) que les paires de fournisseurs différents (0,21) ; test par permutation, p ≈ 0,0001 sur 33 courses. La règle 6 (« une voix par fournisseur ») est confirmée.
3. **Les tours de critique informent peu (mesure).** Au tour 3, environ 97 % des critiques reçues sont acceptées au moins en partie (5 652 lignes de décision), sans différence selon que la critique porte un calcul ou non, ni selon le fournisseur du critique : le changement d'avis suit la critique, pas la vérification.

**Confiance** : ligne 1, 0,85 (une épreuve faite hors des registres lus, ou sur une branche non ouverte, m'aurait échappé) ; ligne 2, 0,75 (la similarité de mots mêle style et contenu ; la mesure par « premier choix » et par co-soutien va dans le même sens, plus faiblement) ; ligne 3, 0,8 (classement automatique des lignes, erreur résiduelle estimée à 1 sur 25).

**Statut des énoncés.** Chaque résultat est marqué **mesure** (compté par programme sur les données brutes, ou codé à la main sur un échantillon tiré), **calcul** (dérivé par code d'hypothèses déclarées, sans donnée nouvelle) ou **argument** (raisonnement de l'auditeur).

### Dossiers exclus pour cloisonnement, nommés sans être lus

Exclus par leur chemin, avant toute lecture (objet ou en-tête cloisonné, ou doute) :

- `runs/collisionneur-protocole-x-modes-attaque-v1-20261122-112512` (attaques contre les moniteurs ; branche `coffre/` homonyme) ;
- `runs/collisionneur-protocole-x-lot-quarantaine-v1-20261122-112512` et sa note de sortie (cas tenus à l'écart) ;
- `runs/collisionneur-protocole-x-taches-sabotage-isole-v1-20261122-115058` et ses notes de sortie v1 et v2 (doute : modes de sabotage) ;
- `runs/collisionneur-protocole-x-conscience-anesthesie-v3-reserve-abonnement-v1-20261122-153110` et sa note (doute sur « réserve ») ;
- `runs/collisionneur-organismes-discrets-v1/etage3-20261117-050702` (textes du bras A, cloisonnés pour les concepteurs) ;
- `docs/notes/protocole-x-attaquant-v1` (côté attaquant qui connaît le dispositif ; doute) ;
- `docs/notes/collisionneur-modes-et-attaques-v1` (session déclarée « cloisonnée »), `docs/notes/collisionneur-evasion-moniteurs-v1`, `docs/notes/service-collisionneur-modes-v8-v1` (modes de sabotage, évasion des moniteurs) ;
- toutes les branches `coffre/*` et `donnees/*` (interdites par le mandat ; une soixantaine de branches `donnees/collisionneur-*` portent sans doute les cellules des dossiers d'octobre ; question posée à la mère, sans réponse à l'heure du rapport).

**Écart déclaré** : deux fichiers du dossier exclu « attaquant » ont été lus par programme sans affichage de leur contenu : ses faits (appariement de mots pour rattacher les dossiers de première étape à leurs courses) et sa contre-lecture (comptes de mots). Aucun texte n'a été vu.

Hors périmètre (ni collisionneur ni protocole X) : sept courses de l'organisme d'idéation Gemini d'octobre (`gemini/01_DONNEES_PRIMAIRES_BRUTES/…`). Doublons : deux copies partielles d'un relais de 06:20Z.

## 1. Données et méthode

Sources : les cellules brutes de chaque tour (`cellules/E3-T1…T3-*.md`), les journaux d'appel (`journal.jsonl`, coût, statut, modèle servi), les questions et faits servis, sur `main` et sur les branches `runs/collisionneurs-*`, `protocole-x/entrainement-et-juges-v1`, `idees/protocole-x-structure-du-langage-fable-v1` ; le journal des idées de la veille de cap ; `registres/decisions.md`, `registres/go.md`, `registres/rappels.md` ; les contre-lectures des réponses de Fable. Les notes de sortie ne servent qu'à savoir quelles propositions ont été retenues.

Scripts (dans `scripts/`, graines par `numpy.random.SeedSequence`, racine 20261124, clé par tâche) :

| script | rôle | sortie |
|---|---|---|
| `inventaire_v1.py` | inventaire des dossiers, exclusions par chemin avant lecture | `inventaire-v1.json`, `.csv` |
| `unites_v1.py` | unités de proposition du dernier tour, « expérience à faire en premier » | `unites-v1.json` |
| `retenues_v1.py` | sélection lue dans 22 notes et synthèses (20 en donnent une) | `retenues-v1.json` |
| `devenir_v1.py` | devenir codé, avec sources | `jeu-des-propositions-v1.json`, `.csv` |
| `cellules_v1.py` | chargement de toutes les cellules | — |
| `erreurs_v1.py` | « vérifié » sans source, calculs rejoués, références | `erreurs-v1.json` |
| `accords_v1.py` | accords par paire, indépendance | `accords-v1.json` |
| `suivisme_v1.py` | concessions entre tours | `suivisme-v1.json` |
| `fidelite_v1.py` | rejeux et bras jumeaux | `fidelite-v1.json` |
| `rendement_v1.py` | rendement, coût, soutien par espèce | `rendement-v1.json` |
| `ablation_v1.py` | puissance du plan d'ablation | `ablation-puissance-v1.json` |
| `temoins_v1.py` | réserve de questions témoins, réponses vérifiées | `../questions-temoins-v1.md`, `../reponses-ne-pas-servir/` |
| `juges_humains_v1.py` | échantillon mêlé pour juges humains | `../juges-humains/fiche-juges-v1.md`, clé séparée |
| `echantillons_v1.py` | rejoue les tirages codés à la main | — |

Codages à la main (auditeur seul, non aveugle) : précision des unités (`precision-unites-v1.json`), étiquettes « VÉRIFIÉ » (`codage-verifie-v1.json`), lignes de décision (`codage-suivisme-v1.json`).

## 2. Inventaire (mesure)

- **42 courses du collisionneur incluses** (9 au 24 novembre), 508 cellules, dont 33 à trois tours, 3 à deux tours, 6 à un tour ; parmi elles, 5 rejeux d'Argon, un bras témoin (boucle organisme-contrôle), un bras jumeau (question générale), trois relances partielles.
- **9 dossiers de première étape du protocole X** (réponse de Fable, réponse d'Opus en effort maximal, contre-lecture par Opus, version 2) ; seuls deux sont rattachés à une course du collisionneur trouvée (boucle organisme-contrôle ; conscience et anesthésie) ; pour les sept autres, la question au collisionneur est écrite mais aucune cellule n'a été trouvée sur les branches permises.
- **Modèles** : Carbon et Opus 5.5 (37 courses), Argon (36), Astra et Fable 5.2 (33), Neon (13), Fable 5.1, Opus 4.6 (6), Kimi (5).
- **Coût compté** (somme des coûts journalisés, cellules échouées comprises) : 464,11 dollars ; **payé au pire** (somme des plafonds par appel) : 917,08 dollars ; les cellules par abonnement ne sont pas comptées. Le livre de coût (règle 7) ne porte que trois lignes : le coût par dossier vient ici des journaux.
- **Pannes** : 61 appels non conformes (32 interrompus, 15 tronqués, 4 échecs, 4 réflexions hors provision, 3 vides, 1 refus, 2 autres).
- **Reformulateur** : déclaré mais non identifiable dans l'en-tête pour 20 courses, non déclaré pour 15, « question neutre » d'auteur non déclaré pour 7. **L'ablation de la reformulation (règle 8) n'est donc pas mesurable sur le passé** : le livre doit l'inscrire à partir de maintenant.
- **19 des 42 courses n'ont pas de note de sélection trouvée** (dont les neuf courses du 21 novembre, versées dans des réponses de Fable, et deux synthèses sans section de sélection repérable : seuil et moniteurs ; dopamine).

## 3. Jeu des propositions (mesure)

`sorties/jeu-des-propositions-v1.json` et `.csv` : 232 éléments lus dans 20 notes (couvrant 23 courses), chacun avec sa note, sa branche, son commit, ses lettres et espèces porteuses, son devenir et ses sources. **115 retenues**, 20 « à reprendre », 97 non retenues. Attribution des porteurs : déclarée par la note pour 200, par similarité avec les unités de dernier tour pour 29, aucune pour 3. Les 33 « retenues » de la synthèse de conception sur la lecture tôt du témoin positif (octobre-novembre) sont des clauses de texte, marquées « règle de texte ».

Unités de dernier tour (`unites-v1.json`) : 809 unités dans 174 cellules ; **précision mesurée** sur 60 unités tirées : 0,83, et 0,96 hors cellules de rejeu (le premier filtre, abandonné, donnait 0,58). Le rappel n'est pas mesuré.

Devenir des 115 retenues (codage de l'auditeur sur traces écrites) :

| état | nombre |
|---|---|
| jamais éprouvée — aucune trace | 72 |
| jamais éprouvée — adoptée sans épreuve (inscrite dans une conception ou une règle) | 33 |
| jamais éprouvée — en préparation (file gelée des textes de Fable, rappels du 2 décembre) | 9 |
| non évaluable (pilotes de « Raisons ou regard ? » refusés par les modèles) | 1 |
| éprouvée et survivante | 0 |
| éprouvée et tombée | 0 |
| trouvée occupée par la littérature | 0 trouvée par l'audit (la recherche d'antériorité n'a pas été refaite) |

## 4. Mesures

### 4.1 Rendement (mesure, puis calcul)

- Part des retenues éprouvées : 1/115 (0,9 %) ; part survivante : 0.
- Coût par survivante : non défini (aucune). Coût par retenue : 2,54 dollars comptés (291,81 dollars sur les 23 courses à note).
- Presque toutes les retenues sont des **consensus** : 81 des 90 retenues à porteurs déclarés sont portées par au moins deux fournisseurs, 9 par un seul ; une seule espèce seule n'en porte que 6. La sélection retient l'accord, donc le point 4.3 pèse directement sur elle.
- Part des retenues portées par chaque espèce, là où elle était présente : Opus 0,93 ; Fable 0,90 ; Carbon 0,88 ; Neon 0,84 ; Argon 0,78 ; Astra 0,74 ; Kimi 0,37 (souvent absent ou en panne).

**Argument.** Le protocole produit des propositions bien plus vite que le programme ne les éprouve ; tant que la règle 1 (épreuve la moins chère, date, critère de mort) n'est pas tenue, aucune mesure de qualité du protocole n'est possible. Le premier levier n'est pas de mieux sélectionner, c'est d'éprouver.

### 4.2 Taux d'erreur relevés par programme (mesure)

- **Étiquette « VÉRIFIÉ » posée par un modèle sur sa propre affirmation** (`erreurs-v1.json`, « verifie_strict ») : fréquence par 10 000 signes : Carbon 6,3 ; Neon 5,3 ; Argon 3,9 ; Astra 1,4 ; Opus 0,7 ; Fable 0,3. Sur un échantillon codé de 8 lignes signalées par espèce, part des étiquettes non fondées (littérature de mémoire, fait empirique, propriété mathématique sans dérivation visible) : Argon 7/8, Neon 6/8, Carbon 2/8, Opus 2/8, Astra 0/8, Fable 0/8. Estimation des étiquettes non fondées parmi toutes : **Argon 18 %, Neon 16 %, Opus 14 %, Carbon 4 %, Astra et Fable ≈ 0** (petits échantillons : intervalles larges). Les modèles de Google étiquettent « VÉRIFIÉ » des références citées de mémoire et des propriétés non dérivées.
- **Calculs simples rejoués par code** (« a op b = c ») : 33 rejoués, **aucun faux** après correction de l'analyseur (les 10 premiers signalements étaient des morceaux d'expressions plus longues ou des pourcentages, tous justes à la relecture). Couverture faible : la plupart des calculs des cellules ne sont pas de cette forme simple.
- **Références arXiv** : 261 citations repérées, aucun identifiant de forme impossible ; 169 renvoient à un PDF présent dans le dépôt (les modèles citent surtout ce qui leur est servi). Le contrôle de concordance auteur–première page n'est jugeable que pour 13 citations ; les 6 signalées sont toutes des voisinages d'une autre citation (faux signalements). **Aucune référence fausse confirmée**, sur une couverture très partielle.
- **Contre-lectures des réponses de Fable, première étape** : 16 à 19 constats par réponse (5 contre-lectures lisibles ; celle du contrôle diffus a un autre format), soit 1,9 à 3,3 constats pour 10 000 signes, dont un « bloquant » dans trois cas ; par type estimé : calcul 35, fond 32, source 18. Ce sont les seules erreurs relevées après coup par un tiers : **le collisionneur n'a pas de contre-lecture de ses cellules**, ses erreurs ne sont relevées que par les autres modèles au tour 2.

### 4.3 Accords et indépendance (mesure)

Similarité de mots pondérée par leur rareté (fréquence du terme multipliée par le logarithme de l'inverse de sa fréquence dans le corpus), formules, balises et étiquettes de statut retirées ; test par permutation des étiquettes d'espèce à l'intérieur de chaque course, 10 000 permutations.

| mesure | écart « même fournisseur » moins « autres » | courses | valeur p unilatérale |
|---|---|---|---|
| conceptions du tour 1 (écrites sans voir les autres) | +0,118 | 33 | 0,0001 |
| « expérience à faire en premier » du dernier tour | +0,037 | 30 | 0,0001 |
| co-soutien des retenues (accord « porte ou ne porte pas ») | +0,043 | 13 | 0,06 |

Matrice du tour 1 (paires d'au moins 8 dossiers communs) : Carbon–Neon 0,345 ; Argon–Carbon 0,345 ; Fable–Opus 0,334 ; Argon–Neon 0,325 ; paires entre fournisseurs : de 0,161 (Astra–Opus) à 0,274 (Neon–Opus), moyenne 0,210. Astra est le plus éloigné de tous. Au co-soutien, Fable–Opus est la paire la plus accordée (0,88).

**Argument.** Compter deux modèles d'un même fournisseur comme deux voix gonfle les « accords indépendants » des notes de sortie ; la règle 6 doit rester tant qu'une indépendance n'est pas démontrée, ce que ces données ne font pas. Réserve : la mesure confond en partie le style (les trois modèles de Google partagent une forme) et le contenu ; le « premier choix », plus proche du contenu, garde un écart net mais petit.

### 4.4 Suivisme entre tours (mesure)

Section (a) des 157 réponses du tour 3 : 5 652 lignes de décision rattachées à une critique : 4 694 acceptées, 778 partielles, **180 rejetées (3,2 %)**. Par répondant, la part non rejetée va de 95 % (Neon, Fable 5.1) à 98 % (Astra) ; par critique, de 92 % (Opus 4.6) à 98 % (Fable).

- **Pas de déférence au même fournisseur** : écart −0,008 (p = 0,88, permutation des critiques à l'intérieur de chaque répondant et course).
- **Pas de lien avec la vérification** : part non rejetée 96,6 % quand la ligne porte un calcul ou une étiquette de vérification, 96,9 % sinon. Approximation déclarée : faute d'épreuves faites ensuite, « ce qui a été vérifié ensuite » n'est pas observable ; on ne voit que la trace de vérification au moment de la critique.
- Classement contrôlé sur 25 lignes tirées : 3 erreurs avant correction, 1 cas limite après.

**Argument.** Un tour où presque tout est concédé ajoute de la longueur, pas de la sélection ; les tours 2 et 3 sont le premier candidat à l'ablation.

### 4.5 Fidélité (mesure)

- **Rejeux d'Argon** (5 courses, 10 cellules rejouées) : similarité rejeu–origine de 0,37 à 0,55, toujours au-dessus de la similarité maximale de l'origine avec une autre espèce de la même course (10 sur 10). Un modèle se ressemble plus qu'il ne ressemble aux autres, mais la moitié du texte change d'un tirage à l'autre.
- **Bras jumeau, question générale** (isolé contre jumeau en abonnement) : même espèce d'un bras à l'autre 0,26 en moyenne, contre 0,16 entre espèces d'un même bras. **Retenues** : sur les 4 retenues du jumeau, une seule a un équivalent parmi les 2 retenues du bras isolé (la porte de faisabilité du sabotage diffus sur un modèle de huit milliards de paramètres) ; l'autre retenue de l'isolé (régler un détecteur, le geler, le porter ailleurs) n'apparaît pas dans le jumeau (lecture de l'auditeur). Selon la règle 5, trois des quatre retenues du jumeau porteraient la marque « fragile ».
- **Bras témoin, boucle organisme-contrôle** : même espèce entre bras 0,24, entre espèces 0,18 ; une seule note couvre les deux bras, sans marque de fragilité.
- Aucun dossier n'a été **rejoué à l'identique en entier** : la fidélité de la sélection elle-même n'est pas mesurable.

### 4.6 Calibration (règle 2)

Aucune question témoin n'a encore été servie : exactitude et score de Brier ne sont pas mesurables. **Poids de la règle 2, fixés ici** : jusqu'à 30 témoins répondus par modèle, aucun poids (accords bruts seuls, une voix par fournisseur). Ensuite, à titre descriptif seulement, poids d'un modèle = max(0 ; 1 − Brier/0,25), normalisés à l'intérieur de chaque fournisseur, chaque fournisseur pesant une voix ; la sélection reste sur les accords bruts jusqu'à un audit qui montre que les poids prédisent la survie aux épreuves.

## 5. Plan d'ablation fixé d'avance

**Critères de jugement, fixés avant toute donnée** (puissance 0,80, α = 0,05, simulation `ablation_v1.py`, **calcul**) :

- **J1, préférence appariée à l'aveugle** : sur une même question, deux jeux de propositions (bras A, bras B), noms masqués ; un juge humain ou deux juges de lignées différentes choisissent le meilleur. Dossiers appariés nécessaires : 190 pour une préférence vraie de 60 %, 88 pour 65 %, **52 pour 70 %**, 36 pour 75 %, 20 pour 80 %.
- **J2, survie à l'épreuve de la règle 1** : trois retenues par dossier, corrélation intra-dossier 0,2 : **56 dossiers par bras** pour 15 % contre 30 % de survie, 37 pour 20 % contre 40 %, 46 pour 10 % contre 25 %.

**Phase 0, gratuite, rétrospective (à faire d'abord).** Sur les 33 courses à trois tours déjà faites, construire trois bras à partir des cellules existantes : (a) le tour 1 d'un seul modèle (Opus 5.5, tiré d'avance) ; (b) les tours 1 de tous les modèles, sans critique ; (c) le dernier tour complet. Juges : un humain (protocole du point 6) sur un sous-échantillon, et deux juges de lignées différentes, à l'aveugle, sur les 33. Elle mesure la valeur des tours de critique et du nombre de modèles, sans égalité de budget (le bras (a) coûte environ quinze fois moins) ; elle ne demande que le coût des juges.

**Phase 1, prospective : protocole complet contre base à un seul modèle au même budget.** Base : Opus 5.5 seul, plusieurs tirages indépendants puis une autocritique, plafonnés au coût compté du protocole complet sur la même question. 52 dossiers appariés (préférence de 70 % détectable), ou 36 si l'on vise 75 %. Au rythme observé (42 courses en 15 jours), environ cinq semaines ; devis à écrire, de l'ordre de deux fois le coût compté moyen d'un dossier (11 dollars) par paire. **Règle de décision écrite d'avance** : si le protocole complet n'est pas préféré au seuil de 5 % sur 52 paires, il est réduit à la base plus un tour de critique ; s'il l'est, la phase 2 suit.

**Phase 2, plan factoriel fractionnaire 2⁴⁻¹** (huit conditions, résolution IV, relation D = ABC) sur quatre facteurs : reformulation (avec ou sans), question neutre (avec ou sans), tours (un ou trois), modèles (trois, un par fournisseur, ou six). Critère J1 contre la base, et exactitude aux questions témoins. Chaque effet principal oppose quatre conditions à quatre ; pour un effet de 15 points de survie, environ 2 × 40 dossiers au total. À ne lancer que si la phase 1 conclut.

**Ce qui tranche hors de nous** : les épreuves de la règle 1, scellées et tranchées à date ; les juges humains ; les questions témoins à réponse publique.

## 6. Questions témoins (règle 2) et juges humains

**Réserve** : `questions-temoins-v1.md` (16 questions, servable) ; réponses dans une pièce séparée, `reponses-ne-pas-servir/reponses-questions-temoins-v1.md` et `.json`, **à ne jamais servir**. Dix calculs refaits par code (borne exacte sans échec, détection cumulée, procédure de Benjamini et Hochberg, kappa de Cohen, score de Brier, borne de Clopper et Pearson, loi binomiale, seuils de Wald, inégalité de Ville, Bonferroni) et six faits publiés lus à la page sur un PDF du dépôt (Wen et al. 2411.17693 p. 1 ; Bailey et al. 2412.09565 p. 1 ; Greenblatt et al. 2312.06942 p. 3 ; Korbak et al. 2504.05259 p. 1 ; Foygel Barber et al. 1903.04684 p. 1 ; Efron 0808.0572 p. 1) ; le script échoue si le passage attendu manque à la page. Aucune n'est cloisonnée ni ne porte un chiffre du programme. **À vérifier à chaque service** : que les faits servis ne contiennent pas le passage attendu (Bailey et al. figure dans plusieurs faits passés).

**Protocole des juges humains à l'aveugle** (Lazar ou un mentor) :

1. Échantillon mêlé tiré (`juges_humains_v1.py`, graine dérivée) : 15 retenues et 15 non retenues ou « à reprendre », de 18 dossiers, réduites à leur énoncé (noms de modèles, lettres, comptes de soutien et motifs de rejet retirés) : `juges-humains/fiche-juges-v1.md`. La clé est à part (`reponses-ne-pas-servir/cle-juges-v1.json`). Dès la phase 0 ou 1, y ajouter 10 propositions de la base à un seul modèle.
2. Notes de 1 à 5 en testabilité et nouveauté, survie attendue en pourcentage, priorité oui ou non ; environ 45 minutes, sans consulter le dépôt ni un modèle.
3. Lecture : aire sous la courbe de la note de priorité pour séparer retenues et non retenues (la sélection des notes s'accorde-t-elle à l'humain ?) ; kappa entre deux juges ; corrélation entre survie attendue et survie réelle quand les épreuves seront faites.
4. Réserve : les énoncés retenus sont mieux rédigés que les non retenus (écrits par l'auteur de la note) ; deux énoncés de la fiche restent mal découpés (J-03, J-05) ; à remplacer avant envoi si Lazar le veut.

## 7. Réserves

- Codages à la main par un seul codeur, non aveugle (espèces visibles), sur de petits échantillons (8 lignes par espèce pour « VÉRIFIÉ »).
- Extraction mécanique des unités et des retenues : précision mesurée, rappel non mesuré ; des lignes d'exclusion des notes ont pu passer pour des propositions (filtrées dans l'échantillon des juges, pas dans le jeu complet).
- Branches `donnees/collisionneur-*` non ouvertes : les dossiers d'octobre (une soixantaine de branches) ne sont pas audités ; si la mère les permet, l'inventaire et les mesures se rejouent par les mêmes scripts.
- Le devenir est cherché dans les registres et le journal des idées ; une épreuve faite sans trace écrite y échappe.
- Similarité de mots : mesure de forme autant que de fond.
- Le module commun existe en deux versions : `audit_commun_v1.py` (scellé au jalon 2, utilisé par les scripts d'extraction) et `audit_commun_v2.py` (graines par empreinte du nom de tâche, utilisé par les mesures) ; les deux tirages codés à la main ont été faits avec l'ancienne dérivation, que `echantillons_v1.py` rejoue à l'identique.

## 8. Recommandations (argument)

1. Geler l'ouverture de nouveaux dossiers sur un thème tant que ses retenues n'ont pas d'épreuve fixée (règle 1) : 72 retenues n'ont aucune trace de suite.
2. Garder la règle 6 ; publier dans chaque note le compte par fournisseur à côté du compte brut.
3. Lancer d'abord la phase 0 de l'ablation (gratuite) : elle dit si les tours 2 et 3, qui concèdent 97 % des critiques, valent leur coût.
4. Servir les questions témoins dès le prochain dossier ; inscrire le reformulateur au livre de coût, dossier par dossier.
5. Faire contre-lire les étiquettes « VÉRIFIÉ » d'Argon et de Neon par le contrôle de la règle 4 avant toute note.
6. Écrire la note de sélection manquante des 19 courses qui n'en ont pas, ou les déclarer closes sans proposition.
