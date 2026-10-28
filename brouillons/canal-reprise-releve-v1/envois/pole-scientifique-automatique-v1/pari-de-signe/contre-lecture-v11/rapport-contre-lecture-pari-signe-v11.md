# Contre-lecture (R2) — « Le pari apparié borné — conception v11 » et le code v7, version 29 — rapport v1

Contre-lecteur : sous-agent neuf **Opus 5.5**, autre modèle que l'auteur de la v11 et de la version 29 (Fable 5.1) ; je
n'ai écrit ni la conception, ni le code, ni une contre-lecture antérieure. Début : mercredi 28 octobre 2026,
**02:09:48 UTC** (`date -u`, appel séparé). Aucun fichier du dépôt modifié, aucun commit ; modules importés avec `-I -B`
(aucun bytecode écrit) ; rien lu dans `donnees/` ; aucune clé ni aucun jeton lu, affiché ou cherché ; processeur seul,
aucune dépense. Tout ce que j'ai écrit est dans ce dossier. **La suite entière des 278 essais n'est pas relancée** : elle
écrit dans `essais/_tmp/` du dépôt (`essais/aides.py`, `CasAvecDossier`), ce qui m'est interdit ; les 43 essais ciblés
du brief passent (2,9 s).

## Verdict

1. **Conception v11 : « à amender en v12 »** (corrections locales et une frontière à compléter, pas refaire). Les règles
   restent les bonnes, et la garantie de D-S25 bis tient en raisonnement sous (H) et (P) (Q3). La frontière de confiance
   est **juste** — aucun code ne peut empêcher de calculer en privé celui qui tient les scores — mais **incomplète** :
   - elle ne nomme que la banque, alors que la course, son journal, la graine du monde et la construction des engagements
     sont aussi du côté de confiance ;
   - le code ne la dessine pas : `construire(monde, …)` et `jouer_generation(course, monde, …)` exigent que l'appelant
     tienne le monde entier, épreuve comprise (K11-2) ;
   - surtout, **même frontière respectée, la règle `abandon_apres` que l'orchestrateur fournit voit l'issue d'une fiche
     avant que les suivantes soient calculées**, et peut interrompre la génération. L'espionne de K10-2 repasse ainsi par
     `jouer_generation` elle-même : **0,55 [0,45 ; 0,64] contre 0,04 [0,02 ; 0,10]** en course honnête, sur 30 générations (K11-1).

   Plusieurs phrases sont fausses ou trop larges (K11-5) :
   - « plus d'étiquette libre… vrai en v11 » : la graine du monde n'est ni scellée ni vérifiée, et `population` change
     l'ordre ;
   - « la fiche espionne est refusée par la mémoire » : seulement la copie exacte, et la course ne consulte pas la
     mémoire ;
   - « génération fournie par la course » : vrai dans `jouer_generation` seulement ;
   - « l'artefact 5 commenté juste » : le commentaire n'a pas changé.
2. **Code v7, version 29 : « à corriger ».** Ce qui est fermé l'est bien :
   - cent noms de contraste donnent un seul ordre ; le budget et une unité factice ne changent plus l'ordre ;
   - le journal public est un tuple, une génération en chaîne est refusée, les identifiants d'unités sont gardés ;
   - la partie vide vaut déclaration ;
   - une course sans journal et une entrée sans clés sont refusées ;
   - la copie à autre `population` est refusée par `Lignees`.

   Mais `jouer_generation` n'est **qu'un** chemin. L'interface publique (`evaluer` sans journal ou sous un nom fantôme,
   `Course.lire(sans_partie=…)`, `Course.abandonner(avant_partie=True)`, `Course.ajouter_trajectoire` avec une trajectoire
   fournie par l'appelant) laisse passer toutes les chaînes de la contre-lecture v10, et d'autres encore, toutes gardes de
   la version 29 en place, sur une banque à nul exact, au moins une fausse promotion sur 30 générations :
   - évaluation privée puis « non lancée » par `jouer_generation` : **0,79 [0,70 ; 0,86]** ;
   - évaluation fantôme journalisée sous un autre nom : **0,79** ;
   - espionne corrélée par la `Course` : **0,55** ;
   - en course honnête : **0,05** [0,022 ; 0,11] (fiche seule) et **0,04** [0,02 ; 0,10] (famille de deux) ; sur 10
     générations, 0,04 et 0,01 contre 0,005 et 0 (§ 2).

   S'y ajoutent :
   - une trajectoire fabriquée, acceptée et promue ;
   - une partie d'une autre clé, acceptée sous la clé déclarée ;
   - un abandon « avant partie » accepté alors que la partie est au journal (K11-3) ;
   - un refus dans `jouer_generation` qui laisse la génération sans aucune sortie honnête (K11-4).
3. **La démonstration v29 se relit** : `banque.json` (`a08426e0…`) et `course.json` (`58a7a755…`) sont reproduits à
   l'octet près, et la lecture est identique hors `nul_repete` et `reglages`. Tout ce que le LISEZMOI v29 affirme s'y
   relit (Q5) :
   - L1 et le contrôle 12 ;
   - les témoins, et leurs sorties e-Bonferroni ;
   - forme-G1 promue par e-BH en génération 3, non sortie, avec une garde comme processus minimal à chaque partie ;
   - sept artefacts refusés ;
   - nul × 200 : 0.

   Pas de sélection d'un résultat favorable : les essais 5 et 6 de l'auteur ont le même `course.json`. Il ne reste pas de
   lecture trompeuse sur la forme G1. Les artefacts n'exercent pas les chemins de K11-1 à K11-4.
4. **D-S8** : la réécriture de la v9 est conforme à N-056, et (α), (β), (γ) sont justes. Le § 6 renvoie à des chiffres
   qui existent (pari v2 § 6 et sa sortie `d07e43f9…`). L'ajout de la v11 (coût des gardes au devis, à confirmer par
   Lazar) est juste. Le pari v2 § 6 donnait déjà « 70 à 300 unités honnêtes d'épreuve pour la garde », ce qui est
   cohérent avec 80 à 210 (Q2).

---

## 1. K10-1 à K10-10, et ce qui restait de K9, K8, K7-6, K7-7

| constat | état (texte v11 / code v29) | où, pourquoi | vérifié par |
|---|---|---|---|
| **K10-1** évaluation privée puis « sans partie » | **à moitié** | Texte : frontière dite (verdict 1, D-S25 bis (2)) ; juste mais incomplète (K11-2). Code : `jouer_generation` existe, mais `evaluer` sans journal reste permis (l. 154 : les deux à `None`), puis « non lancée » passe par `jouer_generation` (A5a ; H1b) ou par `Course.lire` (H1a) ; une évaluation journalisée sous un **nom fantôme** passe aussi (N1 ; H1c). La correction « `evaluer` refuse une partie d'épreuve sans journal » n'est pas faite ; elle ne suffirait d'ailleurs pas (nom fantôme). | A5a, N1, H1 |
| **K10-2** décision de non-lecture après les issues | **à moitié** | `jouer_generation` prend les décisions « avant » en entrée, mais : `Course.lire(sans_partie=…)` et `abandonner(avant_partie=True)` ne regardent toujours pas l'ordre du journal ; la règle `abandon_apres` voit l'issue de l'espionne avant le calcul de O et peut interrompre (N4 : journal vu par la règle = `["A-espion"]` ; H2c) ; l'espionne corrélée (τ = 0,051, autre affirmation, mêmes seuils, même valeur finale) passe la mémoire (H2b, H2c). Seule la copie exacte à autre `population` est refusée, par `Lignees`, que la `Course` ne consulte pas (A3). | N4, N5, A3, H2 |
| **K10-3** ordre dépendant d'entrées hors clé | **à moitié** | Fermé : nom, budget, empreinte de l'engagement, unité factice (rejeu L : cent noms → un ordre ; budget, factice → même trajectoire). Ouvert : **graine du monde** (même engagement, monde d'autre graine : accepté, autre trajectoire, y compris par `jouer_generation` — A7 ; la graine n'est ni dans l'engagement ni vérifiée) ; `population` libre et découpage du plan changent l'ordre d'une même affirmation (A3), figés à l'entrée par la course. | L rejoué, A7, A3, H3 |
| **K10-4** journal réécrit, génération libre, unités | **à moitié** | Fermé : tuple public (A5d public refusé), chaîne refusée (N10), identifiants gardés. Ouvert : la génération d'`evaluer` reste celle de l'appelant hors de `jouer_generation` (A5c : tranche 2 journalisée en génération 1, puis ajoutée en génération 2 ; N10 : génération 5 acceptée) ; `premiere_lecture` n'est toujours remplie qu'à l'ajout (N9 : 0 unité après une lecture fantôme) ; `_journal` reste une liste (A5d privé : effacé). | A5c, A5d, N9, N10 |
| **K10-5** partie vide ou refusée | **à moitié** | Vide : fermé (journalisée vide d'office, déclaration acceptée, A10 ; essai réécrit). Refusée : **ouvert** — un refus de fraîcheur dans `jouer_generation` lève une exception au milieu de la génération ; relance refusée, « sans partie » refusée, seul l'« avant partie » mensonger passe (N6). | A10, N6 |
| **K10-6** clé en deux parties | **à moitié** | Deux empreintes, `Lignees` sur l'affirmation : fait. Mais la v29 met l'étiquette libre `population` dans la **lecture** et aucune identité de population dans l'affirmation (contraire à la correction de K10-6 et à D-S18 v6 point 3) ; banque sans `identite` : repli silencieux sur l'empreinte (A4) ; identité ré-étiquetée : dite à la charge de la mémoire du noyau. | A1, A3, A4 |
| **K10-7** gardes facultatives | **fermé pour le repli silencieux ; résidu** | `Course` sans journal, entrée sans clés : refusées (A9, A2). Résidu : un journal de n'importe quel type et des clés quelconques passent (N8) ; la `Course` ne consulte pas `Lignees`. | A2, A9, N8 |
| **K10-8** forme G1 : ce qui fixe l'e-valeur | **fermé** | Compte rendu avec `log_gardes_finales` ; L3 rapporte par partie contrastes, gardes et processus minimal ; recalculé : incréments 2,1177 / 1,7779 / 1,3264 = minima rapportés (`garde:blanc-juge`, `garde:blanc-cascade` ×2). | F |
| **K10-9** coût des gardes | **fermé au texte** | v11 point 7 et § 1 D-S8 : 80 à 210 unités honnêtes par mode, au devis, joint à la question à Lazar. | lecture |
| **K10-10** mineurs | **(b), (d), (e) fermés ; (a), (c), (f), (g), (h) ouverts ou à moitié** | (a) dit dans la v11, pas dans la docstring de la démonstration (l. 16-17) ; (c) pas de plan exigé dans `jouer_generation` (N7) ; (f) **non corrigé** (l. 292 : « ajoutée à la fiche x », code l. 295 : « y »), alors que la v11 le dit corrigé ; (g) non écrit ; (h) version de l'e-processus toujours à la main (28 ; la règle n'a pas changé, la valeur est juste). | lecture, N7 |
| **K9-1** fraîcheur et décision prévisible | **à moitié** | Comme K10-2 : la tranche d'avance par une autre fiche reste refusée ; la décision prévisible n'est tenue que sur le chemin `jouer_generation` sans règle qui interrompt. | H2, N4 |
| **K9-2** lien fiche ↔ clé | **à moitié** | Clés obligatoires ; mais la `Course` compare la clé **déclarée par l'appelant**, pas celle du journal (N3 : partie de τ = 0,10 journalisée sous f, ajoutée avec la clé de f). | N3 |
| **K9-3** noms libres | **à moitié** | Noms hors de l'ordre et de la clé ; `population` libre reste (K11-6). | A3 |
| **K9-5** étiquette libre | **à moitié** | Restent la graine du monde et l'absence de plan exigé. | A7, N7 |
| **K9-6** journal tenu par qui calcule | **à moitié** | Vrai dans `jouer_generation` ; hors d'elle, journal facultatif, nom et génération libres, trajectoire non liée au journal (N2). | A5, N1, N2 |
| **K9-8** « G1 promue » n'est pas G1 | **fermé** | Avec K10-8. | F |
| **K9-10 (b)** « avant partie » contredit | **ouvert** | A8 : accepté par la `Course` et par `jouer_generation(abandons_avant=…)` alors que la partie de la fiche est au journal. | A8 |
| **K8-1** fraîcheur | **presque fermé** | Restes : identité absente ou ré-étiquetée ; unités d'une lecture non ajoutée restent fraîches (N9). | A4, N9 |
| **K8-2** « sans partie » mensonger | **à moitié** | Refusé contre le journal ; accepté après un calcul hors journal ou fantôme (A5a, N1). | A5a, N1 |
| **K8-5** essais | **fermé** | « Λ changée ⇒ clé changée » ajouté (`test_cle_de_l_heritage`). | lecture |
| **K7-6** alignement par rang | **ouvert, déclaré** | Inchangé. | lecture |
| **K7-7** ordre sans les scores d'épreuve | **fermé pour l'ordre** (la v11 le dit encore ouvert) | `ordre_secret` dérive de la graine, de l'empreinte de la clé (seuils de calibrage, plan, population) et de l'**identité** : plus de score d'épreuve dans l'ordre. Le plan reste choisi par l'orchestrateur (dit). | lecture |

## 2. Les chaînes de la contre-lecture v10 rejouées contre la version 29

**Scripts tels quels.**
- `contre-verification-pari-signe-v10.py` s'arrête dès la section A, l. 93, `pa.Course(alpha=0.05)` : « course sans
  journal des parties… (K10-7) ». Rien après n'est exécuté.
- `contre-verification-pari-signe-v10-etiquettes.py` s'exécute en entier (`rejeu-etiquettes-v10-contre-v29-sortie.json`).
  - L : cent noms donnent **un** ordre (contre cent) ; budget et unité factice : même trajectoire ; **graine du monde :
    autre trajectoire, acceptée** par `Lignees` et la `Course` ; génération `"1"` refusée ; identifiants gardés au
    journal.
  - F : il lit `course.json` v28, d'où une clé différente de la publiée. Les incréments restent 2,118 / 1,778 / 1,326 :
    la garde, non arrêtée, a une valeur finale indépendante de l'ordre.

**Chaîne par chaîne, adaptées** (`contre-verification-pari-signe-v11.py`, sections R et H ; courses de production :
`Lignees` entrées, `Course(journal=…)`, clés, plan scellé). Banque à nul exact de la v10, à l'identique, 20 unités par
tranche, α = 0,05. Intervalles de Wilson à 95 %.

| chaîne | v28 (rapport v10) | v29 | 10 générations (200) | 30 générations (100) |
|---|---|---|---|---|
| H1 honnête (fiche seule, seuil 20), par `jouer_generation` | 0,005 / 0,01 | — | 0,005 [0,001 ; 0,028] | 0,05 |
| H1a évaluation privée puis `Course.lire(sans_partie)` (chaîne v10 telle quelle) | 0,055 / 0,79 | **passe** | 0,04 [0,02 ; 0,077] | **0,79** [0,70 ; 0,86] |
| H1b évaluation privée puis `jouer_generation(non_lancees=…)` | — | **passe** | 0,04 [0,02 ; 0,077] | 0,79 [0,70 ; 0,86] |
| H1c évaluation journalisée sous un nom fantôme, puis `non_lancees` | — | **passe** | 0,04 [0,02 ; 0,077] | 0,79 |
| H2 honnête (famille {espionne, O}, seuil 40), par `jouer_generation` | 0 / 0,01 | — | 0 [0 ; 0,019] | 0,04 [0,02 ; 0,10] |
| H2a espionne à autre `population` (chaîne v10) | 0,01 / 0,62 | **refusée par `Lignees`** à l'entrée | — | — |
| H2b espionne corrélée (τ = 0,051), interface de la `Course` | — | **passe** | 0,01 [0,003 ; 0,036] | 0,55 |
| H2c la même par `jouer_generation`, règle `abandon_apres` qui interrompt | — | **passe** | 0,01 [0,003 ; 0,036] | 0,55 [0,45 ; 0,64] |

Lecture : les trois chemins de H1 (a, b, c) donnent des courses **identiques**, décision pour décision (mêmes issues privées ; 13,82 déclarations « sans partie » par course à 30 générations) : la chaîne de K10-1 passe telle quelle par `jouer_generation`, et un nom fantôme au journal la rend même « journalisée ». De même H2b et H2c (15,91 déclarations par course) : la règle `abandon_apres` reproduit exactement l'espionne de K10-2. Aucun refus de la course sur les 300 répétitions (1 500 courses de chaîne). L'espionne τ = 0,051 a, dans 100 % des banques, les mêmes seuils et la même valeur finale que O. L'honnête à 30 générations, 0,05 [0,022 ; 0,11], reste sous la borne de Ville d'une fiche seule (1/20) ; la v10 avait 0,01 sur d'autres graines.

Autres chaînes de la v10 (section R) :

| contrôle v10 | v28 | v29 |
|---|---|---|
| A2 course sans clés reçoit une partie d'une autre clé | acceptée | **entrée sans clés refusée** ; mais clé déclarée par l'appelant, non confrontée au journal (N3 : acceptée) |
| A3 même contraste, autre `population`, seconde fiche | acceptée | refusée par `Lignees` ; **acceptée par la `Course` et `jouer_generation`** sans `Lignees` (2 parties calculées) |
| A4 banque sans `identite` | repli silencieux | repli silencieux (inchangé) |
| A5a évaluation sans journal, puis « sans partie » | acceptée | acceptée (par `Course.lire` et par `jouer_generation`) |
| A5c tranche 2 journalisée en génération 1 | acceptée | acceptée ; puis `jouer_generation` en génération 2 **refusée** (seconde évaluation), ajout direct **accepté** |
| A5d effacer le journal | accepté (liste) | refusé par `journal` ; **accepté par `_journal`** (attribut privé) |
| A7 monde d'autre graine | accepté | accepté (aussi par `jouer_generation`) |
| A8 « avant partie » alors que la partie est au journal | accepté | **accepté** (par la `Course` et par `jouer_generation(abandons_avant=…)`) |
| A9 course sans journal | silencieuse | **refusée** |
| A10 partie vide | sans issue honnête | **déclaration acceptée** (`vides` du compte rendu) |
| G (chaîne K9-1) | 451 refus sur 457 | non rejouée : elle demandait d'effacer le journal, désormais impossible par l'interface publique ; la garde de fraîcheur est inchangée (N6 la déclenche) |
| H3 graine du monde essayée K fois | 0,005 → 0,015 | 0,015 / 0,02 / 0,035 pour K = 1 / 10 / 100 (200 courses) : non significatif sur cette banque, comme en v10 ; le canal existe, son ampleur suit la variance par unité |

## 3. Réponses aux questions du brief

### Q1 — Fermeture, et frontière de confiance

Fermeture : § 1. **La frontière dite est juste** : tant qu'une partie tient les scores d'épreuve, aucun code de son
processus ne l'empêche de calculer. **Elle n'est pas complète**, pour quatre raisons.
- **(a) Elle ne nomme que la banque.** Qui tient la `Course` peut :
  - ajouter une trajectoire fabriquée (N2 : `[10.0]` acceptée, fiche promue) ;
  - ajouter une partie d'une autre clé en déclarant la bonne (N3) ;
  - déclarer « sans partie » ou geler « avant partie » après les issues (H2b, A8).

  Qui choisit la graine du monde choisit l'ordre (A7, H3). Qui tient le journal peut écrire sous des noms fantômes (N1).
  Le côté de confiance comprend donc le monde **et sa graine**, la course, le journal, la construction des engagements
  et le déroulement de la génération.
- **(b) Le code ne la dessine pas.** `construire(monde, …)` prend le monde entier pour calculer les seuils de calibrage,
  et `jouer_generation(course, monde, …)` le reçoit de son appelant. L'orchestrateur qui construit ses engagements tient
  donc la banque d'épreuve. La démonstration, qui joue l'orchestrateur, tient monde, course et journal.
- **(c) La règle `abandon_apres` traverse la frontière au milieu de la génération.** C'est du code de l'orchestrateur,
  appelé après la partie de chaque fiche, avant le calcul des suivantes (ordre des noms). Il reçoit la valeur, et une
  exception de sa part interrompt la génération (N4, H2c). Même un orchestrateur qui ne tient ni la banque ni la course
  y lit une issue de la génération en cours. La façon de clore une génération interrompue n'est pas dite. Le seul
  moyen offert par le code, `Course.lire(sans_partie=…)`, accepte la déclaration.
- **(d) Le code ne fait pas tout ce qui est possible de son côté.** Mesures simples non faites :
  - `evaluer` refuse une partie d'épreuve sans journal ;
  - le journal appartient à la course : `journaliser` refuse une fiche non entrée et une génération ≠ `course.generation`,
    et remplit `premiere_lecture` dès la journalisation ;
  - `jouer_generation` vérifie à l'entrée que le journal n'a aucune entrée de génération ≥ g ;
  - la règle d'abandon est appelée après l'ajout de **toutes** les parties ;
  - `Course.ajouter_trajectoire` prend la trajectoire dans le journal (ou en vérifie l'empreinte) et confronte la clé du
    journal à `cle_de` ;
  - `lire` et `abandonner(avant_partie=True)` refusent toute déclaration qui n'a pas été enregistrée avant la première
    entrée du journal de la génération ;
  - la `Course` consulte `Lignees` sur l'affirmation ;
  - l'empreinte de la graine du monde est scellée dans l'engagement et vérifiée.

### Q2 — D-S8 réécrite (nœud 1 = b), (α), (β), (γ), § 6

- **Conforme à N-056** (`6aac9746…`, « Ce que cela fixe », point 1) : chaque moniteur boîte noire de la liste scellée,
  plus (ii) cascade et (iii) dernier état ; planchers rapportés ; H2c garde ses tests. La v11 n'y change rien. Elle
  ajoute le coût des gardes « à confirmer par Lazar ». « Une garde par comparateur » n'est pas dans N-056, et la v11
  le soumet à juste titre.
- **(α) juste**, et désormais servi par la lecture. La v29 rapporte, par partie, chaque composante (contrastes et
  gardes) et celle qui fixe le minimum. C'est la bonne décomposition, puisque la course multiplie les minima par partie
  (Π_g min_k), et non les minima des cumuls.
- **(β) juste** : 0,63 à 60 et 0,96 à 100 pour 10 points ; 0,88 à 250 pour 5 ; 0,97 à 40 pour 20. Ces valeurs sont dans
  la table du pari v2 § 6 et dans `simulation-dimensionnement-v2-sortie.json` (`d07e43f9…`, revérifiée : 0,628, 0,964,
  0,876, 0,966).
- **(γ) juste** : les comparateurs diffèrent, donc les affirmations aussi.
- **§ 6** : renvoie à des chiffres qui existent. Les 80 à 210 unités honnêtes par mode viennent de la contre-lecture
  v10 (K10-9), en cohérence avec « 70 à 300 unités honnêtes d'épreuve pour la garde » du pari v2 § 6. Le v2 parlait
  d'une garde ; ici, c'est le minimum de cinq.

### Q3 — Garantie sous la règle de l'héritage avec des tranches

Mêmes notations que la contre-lecture v10 :
- budgets b_i fixés à l'entrée, Σ b_i ≤ Σ α_c ≤ α (tenu par `Course.entrer`) ;
- E_i(g) le produit des parties, gelé à la promotion, à l'arrêt ou à l'abandon ;
- R_g l'ensemble e-BH de la lecture g, U = ∪_g R_g, F_g l'information de toute la course à la fin de g.

Il faut **(H)** : chaque partie e_{i,g} est une e-valeur sachant F_{g−1}. Et **(P)** : toute décision de ne pas lire,
ou de geler avant partie, à g est F_{g−1}-mesurable. Alors E_i est une surmartingale positive, et le temps de gel est un
temps d'arrêt.
- **(i) Promotions accumulées.** Pour i ∈ U promue en γ_i, b_i E_i(γ_i) ≥ 1/k*_{γ_i} et |U| ≥ k*_{γ_i}. Donc
  1(i ∈ U)/|U| ≤ b_i E_i(τ_i), et le taux de fausses découvertes est au plus Σ_{nulles} b_i E[E_i(τ_i)] ≤ α (arrêt
  optionnel, horizon borné). L'accumulation ne fait que grossir |U|. Dans le code, les promues sont gelées
  (`ajouter_trajectoire` rend la valeur sans la changer ; `jouer_generation` ne les joue plus) et restent dans le pool,
  et un retrait ne fait que retirer des candidates. **Tient.**
- **(ii) Arrêt à m_c/α_c.** C'est un temps d'arrêt unité par unité. Une fiche arrêtée a b_i E_i ≥ 1 et entre dans R
  quel que soit k*. Code conforme (`ajouter_trajectoire`, l. 367-374 ; la trajectoire passée est la trajectoire entière du
  minimum, la course arrête sur le cumul). **Tient.**
- **(iii) Abandon sous contrat.**
  - « Après partie » : le gel de i après l'ajout de sa partie de g est un temps d'arrêt pour F_g. Il le reste quand la
    règle le décide au milieu de la génération, après les issues d'autres fiches. **Tient.**
  - « Avant partie » : valide seulement sous (P). Le code ne le vérifie pas, et l'accepte avec la partie au journal
    (A8) ou décidé par la règle après l'issue d'une autre fiche (N5). Le gain est **borné une fois** par fiche
    (E[max(1, e_g)] ≤ 2), puisque le gel est définitif.
- **(iv) « Sans partie ».** Les entrées `non_lancees` de `jouer_generation` sont prévisibles, et la partie vide l'est
  aussi (elle dépend du plan et des strates, pas des scores). **Le trou reste** : une déclaration vraie mais décidée
  après une issue de la génération se répète à chaque génération et compose. C'est E[max(1, e_g)] par génération. La
  version 29 l'accepte :
  - par `Course.lire` (H1a, H2b) ;
  - par `jouer_generation(non_lancees=…)` après une évaluation privée ou fantôme (H1b, H1c) ;
  - **par `jouer_generation` lui-même**, la règle `abandon_apres` voyant l'issue de l'espionne puis interrompant
    (H2c).

**Conclusion.** Le raisonnement tient pour une course jouée **uniquement** par `jouer_generation` :
- avec une règle d'abandon qui ne fait que rendre un motif ;
- sans autre appel à `evaluer` ni aux méthodes de la `Course` ;
- avec un monde dont la graine est fixée.

Hors de ces conditions, le trou de K10-1 et K10-2 est intact. Le compte rendu, lui, ne casse rien (Q4).

### Q4 — Code contre texte (version 29)

**Conforme :**
- `jouer_generation` prend les décisions « avant » en entrée et les applique avant tout calcul ;
- les parties sont calculées, journalisées sous `course.generation` et ajoutées dedans ;
- le compte rendu ne contient aucune trajectoire (essai `assertNotIn("trajectoire_log_min", …)`) ;
- la clé est en deux parties ; `Lignees.entrer` porte sur `empreinte_affirmation` ;
- l'ordre vient de `empreinte_cle|g`, de la graine du monde et de son identité (`ordre_secret`, l. 144) ;
- le journal public est un tuple de copies ; la génération est entière ; les identifiants sont gardés ; `marquer_vide`
  existe (redondant : `journaliser` marque déjà vide une partie de 0 unité) ;
- `Course(essai=False)` refuse journal et clés absents ; la partie vide est acceptée comme déclaration.

**Degrés de liberté qui restent du côté du code de la frontière, choisis après des issues :**

| entrée | effet | vérif. |
|---|---|---|
| règle `abandon_apres` (code de l'orchestrateur, appelé au milieu de la génération) | voit l'issue d'une fiche avant le calcul des suivantes ; peut interrompre la génération, puis « sans partie » par `lire` ; peut geler une autre fiche « avant partie » | N4, N5, H2c |
| graine du monde passé à `jouer_generation` | ordre de la tranche, donc instant du franchissement ; engagement accepté | A7, H3 |
| `evaluer` hors de `jouer_generation` (sans journal, nom fantôme, génération libre) | partie vue, puis « non lancée » acceptée | A5a, A5c, N1, H1b, H1c |
| méthodes publiques de la `Course` | trajectoire fournie par l'appelant ; clé déclarée par l'appelant ; « sans partie » et « avant partie » sans confrontation à l'ordre du journal | N2, N3, A8, H2b |
| ordre de traitement des fiches (ordre des noms, choisi à l'entrée) | désigne qui lit la première (l'espionne s'appelle « A-… ») | H2c |

**Le compte rendu ne permet pas, par lui-même, une décision après coup qui casse la garantie.** Il rend, par fiche, la
valeur cumulée après la partie, les richesses finales des contrastes et des gardes, et l'arrêt. Tout cela est dans F_g.
Une décision de la génération g + 1 qui ne s'appuie que sur lui est F_g-mesurable, donc prévisible : abandon « avant »,
non-lancement, nouvelles fiches, budgets. Les unités qu'il décrit sont toutes enregistrées dans `premiere_lecture` (une
partie calculée est ajoutée ou fait échouer la génération), donc refusées à toute fiche plus tard. Une partie vide n'en
dit rien. **Le canal est la règle `abandon_apres`**, qui reçoit la même information **avant** la fin de la génération.

### Q5 — La démonstration v29

- **Reproduite** (`--nul 50`, 21,7 s) : `banque.json` `a08426e0…` et `course.json` `58a7a755…` sont identiques aux
  publiés. `lecture-pari-apparie.json` est identique hors `nul_repete` (0 sur 50 ; Wilson [0 ; 0,071]) et `reglages`.
- **R4** : les essais de l'auteur en version 29 sont `demo-pari-essai5` (nul 20, 0 promotion) et `-essai6` (publié, nul 200).
  Leurs `course.json` sont identiques (`58a7a755…`) : pas de choix d'un résultat.
- **Le LISEZMOI v29 se relit dans les sorties publiées** (`lecture-pari-apparie.json` `6c905f54…`, `course.json`
  `58a7a755…`) :
  - L1 tenue (aucune promue d'espérance conditionnelle ≤ 0) ;
  - contrôle 12 : « jumeau non promu » (+0,035) ;
  - témoins aux décalages 1,2 et 1,0 promus en génération 2 et sortis par e-Bonferroni (6,885 et 7,001 ≥ 6,867 : arrêt
    au franchissement, donc juste au-dessus) ; 0,5 promu en génération 2, non sorti (5,66) ; 0,8 « concentré » promu en
    génération 4, non sorti (5,01) ; 0,1 non promu ;
  - forme-G1 promue par e-BH en génération 3, non sortie (5,222 < 6,867), processus minimal `garde:blanc-juge`,
    `garde:blanc-cascade`, `garde:blanc-cascade`. Recalculé sur `course.json` : incréments égaux aux valeurs rapportées,
    à 10⁻¹⁵ près (F). En cumul, la garde blanc−cascade vaut 5,34, contre au moins 9,45 pour les contrastes ;
  - 25 fiches, 25 affirmations ; nul × 200 : 0 (Wilson [0 ; 0,019]) ;
  - sept artefacts refusés par la bonne garde (messages relus).
- **« Les log e des témoins bougent de quelques dixièmes, les promotions sont les mêmes »** : promotions et sorties
  Bonferroni identiques à la v28. Seuls les deux témoins arrêtés bougent, de ±0,11 (6,993 → 6,885 ; 6,892 → 7,001). Les
  autres valeurs finales, non arrêtées, ne dépendent pas de l'ordre, et sont inchangées.
- **Lecture trompeuse restante : aucune sur L1, L2, L3.** Les artefacts ne montrent que les refus attendus.
  - L'artefact 6 n'est refusé que parce que la démonstration appelle `lg.entrer`.
  - L'artefact 3 passe par `Course.lire` directement ; il montre la garde du journal, pas celle de l'ordre des décisions.
  - Aucun artefact n'exerce la règle d'abandon, l'évaluation hors journal, la trajectoire fournie, ni le refus au milieu
    de `jouer_generation`.

  Le lecteur ne doit pas en conclure que K10-1 et K10-2 sont fermés.

## 4. Constats, du plus grave au moins grave

### Touche la garantie

**K11-1 — La règle `abandon_apres` voit l'issue d'une fiche au milieu de la génération, et peut l'interrompre : l'espionne passe par `jouer_generation`.**
- **Où.** `engagement_apparie.jouer_generation`, l. 210-230 : boucle par ordre des noms ; après l'ajout de la partie de
  f, `abandon_apres(f, valeur)` est appelé, avant le calcul des fiches suivantes. Une exception de la règle traverse la
  fonction sans rien clore. v11 verdict 1 : « les décisions "avant toute issue"… prises avant qu'elle ne calcule quoi que
  ce soit ».
- **Problème.**
  - Quand la règle est appelée pour l'espionne, le journal ne contient qu'elle (N4). Si son issue déplaît, la règle lève
    une exception, puis `Course.lire(sans_partie={"O": …})` accepte : O n'a rien au journal.
  - Mesuré (H2c) : **0,01 [0,003 ; 0,036] / 0,55 [0,45 ; 0,64]** sur 10 et 30 générations, contre 0 [0 ; 0,019] / 0,04 [0,02 ; 0,10] en honnête.
  - Variante : la règle gèle O « avant partie » après l'issue de l'espionne (N5, accepté, gain borné une fois).
  - L'espionne est une fiche légitime d'une autre affirmation (τ = 0,051 : mêmes seuils, même valeur finale). La mémoire
    ne peut pas la refuser ; c'est le moment de la décision qu'il faut tenir.
- **Correction (code).**
  - Appeler la règle d'abandon **après** l'ajout de toutes les parties de la génération. Le gel « après partie » reste
    valide, et il ne reste plus rien à déclarer.
  - Mieux : une règle déclarée comme donnée (seuil scellé), évaluée par le noyau.
  - Rendre `jouer_generation` transactionnelle : toute exception marque la génération « interrompue », et la `Course`
    refuse alors toute déclaration qui n'était pas en entrée.

  **(texte)** : D-S25 bis (2), « la règle d'abandon après partie est une donnée, appliquée après toutes les parties de la
  génération ».

**K11-2 — La frontière de confiance est incomplète et n'est pas dessinée dans le code.**
- **Où.** v11 verdict 1 et § 1 D-S25 bis (2) ; LISEZMOI v29 ; `construire(monde, …)` ; `jouer_generation(course, monde,
  …)` ; démonstration `course()`.
- **Problème.** Le texte ne place que la banque du côté de confiance. Or :
  - qui tient la course ajoute ce qu'il veut (N2, N3) et déclare après les issues (H2b, A8) ;
  - qui choisit la graine choisit l'ordre (A7) ;
  - qui tient le journal évalue sous des noms fantômes (N1, H1c) ;
  - l'API oblige qui construit un engagement à tenir le monde entier, épreuve comprise.
- **Correction.**
  - **Texte** : « côté de confiance : le monde et sa graine, la course, le journal, la construction des engagements
    (seuils), le déroulement de la génération et la règle d'abandon ; l'orchestrateur ne tient aucun de ces objets ; il
    soumet des engagements (sans scores) et des décisions, et reçoit des comptes rendus ; tant que le pôle ne sépare pas
    ces objets, toute garantie de D-S25 bis est sous l'obligation de l'orchestrateur ».
  - **Code** : une vue « calibrage » du monde pour `construire` (cellules, strates, identifiants, seuils), et un objet
    noyau qui tient course, monde et journal.

**K11-3 — De son côté de la frontière, le code ne fait pas ce qu'il peut : les chaînes v10 passent toutes hors de `jouer_generation`.**
- **Où.** `evaluer` l. 154 (journal facultatif) ; `Lignees.journaliser` (nom et génération libres, aucun lien à la
  course) ; `Course.ajouter_trajectoire` l. 334-342 :
  - trajectoire et clé fournies par l'appelant ;
  - le journal n'est confronté que sur l'empreinte des unités, jamais sur sa clé ni sur la valeur.

  Aussi `Course.lire` et `Course.abandonner(avant_partie=True)` (pas d'ordre du journal), et `premiere_lecture`, remplie
  à l'ajout seulement.
- **Problème.** Mesuré, toutes gardes de la version 29 en place :
  - H1a **0,79** [0,70 ; 0,86], H1b 0,79 [0,70 ; 0,86], H1c 0,79, H2b 0,55 sur 30 générations ;
  - trajectoire fabriquée promue (N2) ;
  - partie de τ = 0,10 ajoutée sous la clé de τ = 0,05 (N3) ;
  - « avant partie » contredit par le journal (A8) ;
  - lecture d'avance journalisée puis ajoutée (A5c) ;
  - lecture fantôme invisible à la fraîcheur (N9) ;
  - deux fiches de même affirmation acceptées par la `Course` sans `Lignees` (A3).
- **Correction.** Les mesures de Q1 (d). La plus simple et la plus forte : **le journal appartient à la course**, et
  `ajouter_trajectoire` ne reçoit qu'une référence d'entrée du journal (la trajectoire, la clé et les unités sont lues
  dedans). `lire` n'accepte que les déclarations enregistrées avant la première entrée de la génération, plus les
  parties vides.

### Garde qui bloque à tort

**K11-4 — Un refus au milieu de `jouer_generation` laisse la génération sans sortie honnête.**
- **Où.** `jouer_generation` l. 215-222 : `evaluer` journalise, puis `ajouter_trajectoire` peut refuser (fraîcheur, clé,
  partie d'un engagement sans plan à la génération 2). L'exception traverse, et rien n'est clos.
- **Problème.** Deux fiches entrées ensemble, aux plans croisés (x lit t1 puis t2, z lit t2 puis t1), sont acceptées à
  l'entrée et en génération 1. En génération 2, x est refusée (« lue par la course à une génération antérieure »), z n'est
  pas calculée (N6). Ensuite :
  - relancer `jouer_generation` est refusé (seconde évaluation de x) ;
  - « sans partie » est refusée (journal) ;
  - **seul l'abandon « avant partie », mensonger pour x, passe**.

  C'est la moitié non fermée de K10-5. Une garde qui bloque pousse à contourner les autres. Même chose pour un
  engagement sans plan : il est accepté en génération 1 (N7 ; K10-10 c) et lit toute la partie. Par le code, il sera
  refusé en génération 2, puisqu'il relit les mêmes unités. Ce refus n'est pas mesuré ici : la fiche s'est arrêtée en
  génération 1.
- **Correction.**
  - Vérifier **avant de calculer** : à l'entrée, refuser des plans qui relisent plus tard des unités qu'une autre fiche
    entrée lit plus tôt ; exiger un plan ; vérifier la clé.
  - Dans `jouer_generation`, consulter `premiere_lecture` avant `evaluer`.
  - Tout refus restant devient une partie « refusée », facteur 1, tracée (décision de la course, donc prévisible).

### Texte

**K11-5 — Phrases de la v11 fausses ou trop larges.**
- (a) Verdict 3, « "plus d'étiquette libre" était faux en v10, vrai en v11 ». Faux :
  - la graine du monde n'est ni dans l'engagement ni vérifiée (A7 : acceptée, autre trajectoire, par `jouer_generation`
    aussi) ;
  - `population` (chaîne libre) et le découpage du plan changent l'ordre d'une même affirmation (A3), figés seulement à
    l'entrée.

  Écrire : « plus d'étiquette libre **après l'entrée**, hors la graine du monde, qui doit être scellée ».
- (b) Verdict 1, « La fiche espionne est refusée par la mémoire ». Vrai pour la copie exacte (même affirmation) et
  seulement si l'orchestrateur appelle `Lignees.entrer` : la `Course` ne consulte pas la mémoire (A3). L'espionne
  corrélée, une autre affirmation, passe (H2b, H2c). Écrire que c'est le **moment** de la décision qui ferme K10-2, pas
  la mémoire.
- (c) Verdict 4, « génération fournie par la course ». Vrai dans `jouer_generation` seulement (A5c, N10). Docstring de
  `pari_apparie` l. 26 : « jamais par l'appelant » est faux pour `evaluer`.
- (d) Verdict 5, « les gardes sont obligatoires » : un objet quelconque passe pour journal, et une chaîne quelconque
  pour clé (N8).
- (e) Verdict 8, « l'artefact 5 commenté juste » : faux (démonstration l. 292 inchangée). « 0,5 ≈ 14 points… (dit) » :
  dit dans la v11, pas dans la docstring de la démonstration (l. 16-17).
- (f) § 4 : K7-7 est fermé pour l'ordre par la version 29 (identité au lieu de l'empreinte) ; la v11 le laisse ouvert,
  ce qui la sous-estime.

**K11-6 — La population n'est plus dans l'affirmation ; l'étiquette libre reste.**
- **Où.** `construire` l. 110-112 : `affirmation` sans population ; `lecture["population"] = population or
  monde.identite`. D-S18 de la v6 (point 3) : population (vivier) dans la clé. La correction de K10-6 demandait
  « population = `monde.identite` seule » dans l'affirmation.
- **Problème.**
  - Deux viviers réels de mêmes seuils (calibrage commun, épreuves distinctes) font une même affirmation : la seconde
    fiche est refusée alors que le nul diffère.
  - L'étiquette libre reste un canal d'ordre avant l'entrée.
  - Une banque sans `identite` est acceptée, avec repli silencieux sur l'empreinte (A4).
  - Question liée, au lien au cycle : un engagement est scellé sur `monde.empreinte`. La façon dont une fiche continue
    sur le vivier frais de la génération suivante (N-049) n'est pas dite, et un recalibrage change les seuils, donc
    l'affirmation (nouvelle fiche, nouveau budget).
- **Correction.**
  - `affirmation["population"] = monde.identite`, obligatoire et sans repli ; retirer l'argument `population`.
  - Dire comment une fiche lit le vivier d'une autre génération.

### Mineurs

**K11-7.**
- (a) Docstrings restées en v28 :
  - `engagement_apparie` l. 8, « L'empreinte de l'engagement fixe l'ordre secret » ;
  - `evaluer` l. 129, « dérivé de l'empreinte de l'engagement » ;
  - démonstration l. 1 et l. 247 (« version 28 », « cinq refus attendus »).
- (b) `E_PROCESSUS["version"]` toujours écrit à la main (28 ; la règle n'a pas changé, la valeur est juste) — K10-10 h.
- (c) Aucun essai pour `abandon_apres`, pour une exception au milieu de `jouer_generation`, ni pour `_journal`.
  `test_v7_pari_apparie.py` n'a changé que pour `essai=True`.
- (d) « 278 essais passent » : 278 `def test_` comptés. La suite entière n'est pas relancée ici, parce qu'elle écrit
  dans le dépôt (`essais/_tmp`). Le dire dans le LISEZMOI, ou faire écrire les essais hors du dépôt.
- (e) `marquer_vide` est redondant avec `journaliser`, qui marque déjà vide une partie de 0 unité. Sans effet.
- (f) « Nul en population » (K10-10 g) n'est pas écrit.

## 5. Décisions de la v11 : avis

| décision | avis |
|---|---|
| D-S25 bis (2), (5) (0,85) | règle juste ; **0,85 tenable pour le texte une fois la frontière complétée et la règle d'abandon placée après toutes les parties** (K11-1, K11-2) ; le code n'en tient que le chemin `jouer_generation` sans règle qui interrompt |
| D-S18 (0,85, « codée ») | séparation faite ; population à remettre dans l'affirmation comme identité, sans étiquette libre (K11-6) |
| D-S8 (garde par comparateur, coût) | à confirmer par Lazar, avec le coût, comme la v11 le dit |
| nœud 2, D-S29, D-S30 | inchangés, conformes à N-056 (« lue, non confirmée ») |

## 6. Chiffres de la v11 et du LISEZMOI v29 contre leurs fichiers

| où | cité | fichier, valeur | verdict |
|---|---|---|---|
| v11 en-tête | v10 `1237d52d…`, rapport v10 `7bb83a48…` | `sha256sum` | justes |
| v11 verdict 1 | 0,055 / 0,79 contre 0,005 / 0,01 ; 0,62 contre 0,01 | rapport v10, Q3 | justes |
| v11 verdict 3 | « cent noms donnaient cent ordres » | rapport v10, L ; rejoué : 1 ordre en v29 | juste (fermé pour les noms) |
| v11 verdict 6 | 2,118 / 1,778 / 1,326 ; trois gardes | F (v28 et v29) | justes |
| v11 verdict 7 | 80 à 210 unités honnêtes par mode | rapport v10, K10-9 | juste (estimation) |
| v11 § 3 | signatures `Course(alpha, journal, essai=False)`, `jouer_generation(...)`, `empreinte_affirmation`, `_Journal`, `marquer_vide` | code v29 | justes |
| LISEZMOI v29 | 278 essais | 278 `def test_` ; 43 ciblés passent | juste (suite entière non relancée) |
| LISEZMOI v29 | promotions, Bonferroni, processus minimal, 25 / 25, nul × 200 : 0, sept refus | sorties v29 | justes |
| LISEZMOI v29 | « ≈ 90 s » pour nul 200 | 21,7 s pour nul 50 | plausible |
| EMPREINTES v29 | 133 fichiers | `sha256sum -c` : 133 OK | juste |

## 7. Vérifications sur processeur

Interpréteur `/opt/venv-essaim-sim-v1/bin/python -I -B` (Python 3.13.17, numpy 2.5.4). Graines :
`numpy.random.SeedSequence(2026102811, spawn_key=(section, …))` (R9). Le manifeste est dans la sortie (empreintes du
script et du code lu, durées).

Le script n'a pas changé entre l'exécution de mise au point (REP = 4, rendue) et l'exécution rendue (REP = 200) : même
empreinte, section R identique. Aucune retouche ne les a précédées.

| fichier | SHA-256 |
|---|---|
| `contre-verification-pari-signe-v11.py` (R, F, H, H3) | `17cb1c1b66048a9a12f613bf27b457011f7a36d41849503511ab77d18919c789` |
| `contre-verification-pari-signe-v11-sortie.json` (REP = 200 ; 244 s) | `2786ca5b548e1842e89e4c814da9bc24180f9995e4282faf412587725684e15f` |
| `contre-verification-pari-signe-v11-mise-au-point-rep4-sortie.json` | `1c942ddb24b6b27fb7f181801ab9a7994f402cba4f4039981b5b901dc2866ce0` |
| `rejeu-scripts-v10-tels-quels-console.txt` (scripts v10 tels quels contre la v29) | `9b0ce5c55be475412480eb44dd9702b8323249ccd72bff2af34843c0ff94e076` |
| `rejeu-etiquettes-v10-contre-v29-sortie.json` (script d'étiquettes v10, en entier) | `e6968277522e5f22ce5b86ffa219acc4cb121178780df5b6b12716d66cf6d25b` |
| `essais-cibles-console.txt` (43 essais, OK) | `3f72cd3e9c62fdaa086bc7999761f3c7ea5667f547cb91f7a3a30602673b134a` |
| `demo-reproduite-nul50-console.txt` | `08ebcf3c0b04f41390f1450b25e640386e9325b322be3650bd4fcc1c7779bf41` |
| `demo-reproduite-nul50/banque.json` (identique : `a08426e0…`) | `a08426e0e9925da51c1d80ed8dc64bd11d660a39252d079eee851178bcbedcad` |
| `demo-reproduite-nul50/course.json` (identique au publié) | `58a7a7557cfaad4099799d876a7413c8e492c2ba5b2dd24cc65eb1600ed0a1e2` |
| `demo-reproduite-nul50/lecture-pari-apparie.json` | `1587f2f8d0406622240f89a34d7ad55c011775bd49fcc7dfb89971f2237a8b54` |

**Pour reproduire**, depuis ce dossier, avec `R=…/orchestrateur-pole-v7` :
```
REP=200 /opt/venv-essaim-sim-v1/bin/python -I -B contre-verification-pari-signe-v11.py $R > contre-verification-pari-signe-v11-sortie.json
/opt/venv-essaim-sim-v1/bin/python -I -B ../…/contre-lecture-v10/contre-verification-pari-signe-v10-etiquettes.py $R
(cd $R && /opt/venv-essaim-sim-v1/bin/python -I -B -m unittest -k test_v7_pari_apparie -k test_v7_engagement -k test_v7_demo_pari)
(cd $R && /opt/venv-essaim-sim-v1/bin/python -I -B demonstrations/demo_pari_apparie_v7.py DOSSIER_NEUF --nul 50)
```

**Limites.**
- Mondes synthétiques, courses à une ou deux fiches : l'ampleur dépend de la variance par unité.
- L'espionne de H2 est un quasi-doublon (τ = 0,051). Toute fiche corrélée sert, avec un effet moindre.
- La suite entière n'est pas relancée (elle écrit dans le dépôt).
- Le lien au cycle n'existe pas en code.

## 8. Fichiers lus et empreintes SHA-256

Dossier `…/` = `/home/claude/canal-conv-audit-n04/brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/`.

Tous les fichiers sont conformes à leurs compagnons `.sha256`. Le code est conforme à
`EMPREINTES-orchestrateur-pole-v7-v29.txt` (`sha256sum -c` : 133 OK), elle-même conforme à son compagnon (`91ec728e…`).

De la v28 à la v29 ont changé : `pari_apparie.py`, `engagement_apparie.py`, `monde_banque_scores.py`, la démonstration,
les trois fichiers d'essais et le LISEZMOI. `cycle.py` est inchangé.

| fichier | SHA-256 |
|---|---|
| `…/pari-de-signe/conception-pari-de-signe-v11.md` | `8307a6ac802531d06740465852165e9c342ffae22dedeb446ba37057cbec12e5` |
| `…/pari-de-signe/conception-pari-de-signe-v10.md` | `1237d52d15f6b55cf3fd44c8ad6a6e155882b130c90c7f3022b501f9fad97bd2` |
| `…/pari-de-signe/conception-pari-de-signe-v9.md` | `aab37f630a1a310d1a4cebf35dac4c0cd6e53ebac327af5771ddaae101c0ceeb` |
| `…/pari-de-signe/conception-pari-de-signe-v8.md`, `-v7.md`, `-v6.md`, `-v5.md` (empreintes ; v6 lue pour D-S25 bis et D-S18) | `3e9609fc…`, `fb422cbc…`, `f21982cd…`, `95af46e4…` |
| `…/pari-de-signe/conception-pari-de-signe-v2.md` (§ 6) | `9c39a73ddbf681270610e6a3552fd85045fae46ade21d8d38c77564b7b461e1a` |
| `…/pari-de-signe/simulation-dimensionnement-v2-sortie.json` | `d07e43f9702eabe93470ffee9f2124fdd18dfec1473ade225a8a6f9afafa33ea` |
| `…/pari-de-signe/contre-lecture-v10/rapport-contre-lecture-pari-signe-v10.md` | `7bb83a48c88dbc3cedfa9eade34c6f2104aa82ac033d7acf6d11ba558559c8d8` |
| `…/pari-de-signe/contre-lecture-v10/contre-verification-pari-signe-v10.py` | `4606a33c8289e8dfbc448df3b5b29f65247f7f856f3391579103ab3b588c73f2` |
| `…/pari-de-signe/contre-lecture-v10/contre-verification-pari-signe-v10-etiquettes.py` | `cfa8e8ab80982d667d2b13c9c5bff94c8731f16922cb8a8c7c48b6b09593534a` |
| `…/pari-de-signe/contre-lecture-v10/contre-verification-pari-signe-v10-sortie.json` | `0a2a2d109071ca79dd7dd445f5b0774ddf91b3948a27d12a6af51428a2ff7374` |
| `…/../decision-N-056-noeuds-G1-bras-attaque-mesures-fortes-v1.md` | `6aac9746543cd05d0fc4fb89b32938d272e9b9723dab820d191cbb8297669eff` |
| `…/orchestrateur-pole-v7/EMPREINTES-orchestrateur-pole-v7-v29.txt` | `91ec728e107bc6915dfae4f8ff86c0ee6b13664ab6db45b12405377ae2e3f14e` |
| `…/orchestrateur-pole-v7/LISEZMOI-orchestrateur-pole-v7-v29.md` | `e86098af79fe9376b2f9004f0d050bc5b8a8af7bb745fe74cb44517b1ccafe6f` |
| `…/orchestrateur-pole-v7/LISEZMOI-orchestrateur-pole-v7-v28.md` | `6e105930aec90de6f76c28cafeb53ecc014018105518a0d87c03290d4d1271f3` |
| `…/orchestrateur-pole-v7/pole/pari_apparie.py` | `403fb30acc54c8225169bceb4081e24f21f4a0fc71fe54f5b1d415aaad262a0d` |
| `…/orchestrateur-pole-v7/pole/engagement_apparie.py` | `2f280dbc86e67cf7af7665954907439b9ad5ec4503b46e10348c534f79c9eba0` |
| `…/orchestrateur-pole-v7/pole/monde_banque_scores.py` | `477988810a3edbc605f84a61aa5d7532a7df4f2300eb3f6f1d8504f3c3d6f743` |
| `…/orchestrateur-pole-v7/demonstrations/demo_pari_apparie_v7.py` | `eec91fb9461fe8eeb9adef94a0cf9b834c531c2d65e19ce0d58e337a94139908` |
| `…/orchestrateur-pole-v7/essais/test_v7_pari_apparie.py` | `f3fc7b38d72a0e60f89ea9e15d30f7b06d0a591167ed65f1ccbc9ec3876b440b` |
| `…/orchestrateur-pole-v7/essais/test_v7_engagement_apparie.py` | `08743e40a38730a3eb2f9129e50c7f7b6bb1780d5b468196f0ce5547361c2ac0` |
| `…/orchestrateur-pole-v7/essais/test_v7_demo_pari_apparie.py` | `21a714e11d38db0a63ea1db1b7ff0723e716ff259ebb51acf359ca652d311aa7` |
| `…/pari-de-signe/demonstration-v29/lecture-pari-apparie.json` | `6c905f542fcd2fde6b57ff7b3d085e93684d21f3c12b6e800c53645be7ce1e1c` |
| `…/pari-de-signe/demonstration-v29/course.json` | `58a7a7557cfaad4099799d876a7413c8e492c2ba5b2dd24cc65eb1600ed0a1e2` |
| `…/pari-de-signe/demonstration-v29/LISEZMOI-demonstration-v29.md` | `2e455b35d2f1bed297f36bdd987f18658f2de6c0f77284623adbc842b8d6bf52` |
| `…/pari-de-signe/demonstration-v29/banque.json.sha256-seule.txt` (banque `a08426e0…`) | `845b17174f3d3e0e61562582c725e4e576c903ebfa00833b9684517a1102770a` |
| `…/pari-de-signe/demonstration-v28/lecture-pari-apparie.json` | `c91eee0226daa1a71973ef30796dca06ef929ae7f51d97d477b7ebff8b3a7131` |

L'empreinte de ce rapport est dans son compagnon `rapport-contre-lecture-pari-signe-v11.md.sha256` (un fichier ne peut
pas contenir sa propre empreinte). Heure de fin, lue sur `date -u` dans un appel séparé, juste avant cette ligne :
mercredi 28 octobre 2026, **02:30:03 UTC**.
