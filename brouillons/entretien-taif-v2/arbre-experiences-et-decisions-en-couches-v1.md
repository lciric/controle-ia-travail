# La chaîne d'expériences et de décisions — arbre décisionnel en couches — v1

Lignée conv-audit, instance du 28 octobre 2026 (modèle servant déclaré par l'environnement : Fable 5.1 ; auteur désigné du
travail principal : Opus 4.6, décision de Lazar). Écrit à partir du relevé `date -u` de **10:42:50 UTC le 28 octobre 2026**.

**Demande de Lazar** (11:27 heure de Paris) : « la chaîne d'expériences et de décision en mode arbre décisionnel en couches ».
**Sources** : programme qui fait foi (`docs/programme-controle-ia-v2.md`, `2fd63bad…`, sections 10, 13, 14), brief v2 (porte G0,
section 7), proposition envoyée (calendrier, section 7 ; bascules, section 9 ; `737c482c…`), décisions N-054, N-055, N-056,
R-609, R-611, et le programme d'entretien v4 (`8dbacfe5…`). **Rien de neuf** : ce document range ; toute divergence avec ces
pièces est une erreur de ce document.

**Mode d'emploi.** Six couches, du plus grossier au plus fin. Couche 0 : l'arbre en une figure. Couche 1 : chaque porte comme
nœud de décision (condition, qui prononce, branche oui, branche non). Couche 2 : la chaîne d'expériences, phase par phase, et
ce que chaque expérience décide. Couche 3 : l'arbre fin de la phase 0 **au 28 octobre** — ce qui dépend de quoi, jusqu'au
verdict de G0. Couche 4 : les règles de décision — qui tranche quoi, et les nœuds ouverts aujourd'hui. Couche 5 : toutes les
bascules pré-engagées, en une table. Les dates « mois n » sont celles de la proposition envoyée (M1 = décembre 2026) ; là où le
programme interne diffère (G1 « fin M2 »), c'est dit.

**Conventions.** `[E]` expérience ou mesure ; `<G>` porte (verdict par un sous-agent neuf, R13, puis GO de Lazar) ; `{N}` nœud
de décision de Lazar ; `→ oui` / `→ non` branches ; `↺` bascule pré-engagée ; `⛔` arrêt de sécurité (classifieur) et sa règle.

---

## Couche 0 — l'arbre en une figure

Figure : `arbre-portes-v1.png` (source Mermaid `arbre-portes-v1.mmd`, même dossier) — portes en losanges, bascules en rouge,
phases en bleu, règles transversales en vert. La même chose en texte :

```
Phase 0 — instruments (depuis le 5 oct. 2026, ≤ fin nov.)
  [E] T0.1 socle ─ T0.2 état de l'art ─ T0.3 simulation ─ T0.4 harnais ─ T0.5 env. (a) ─ T0.6 organismes ─ T0.7 sondes ─ T0.8 bases noires ─ T0.9 papier C
  [E] fronts neufs à coût nul : carte des hypothèses v1 → v2 ; mesures T0…T5 sur scores déjà payés ; pôle : boucle, duel, banques
        │
        ▼
   <G0> huit critères (2 prouvés : harnais, agrégateurs)
        ├── oui → GO devis phase 1 ──────────────────────────────────────────────────────────┐
        └── non sur un critère → {N} options et défaut (critère reporté, ou phase 1 restreinte)│
                                                                                              ▼
Phase 1 — papier A (mois 1–4)                         ║   Piste C — papier C (mois 1–3, en parallèle)
  [E] E1.1 organismes, dose-réponse                   ║     [E] EC.1 déférence des juges, cinq familles d'attaque
  [E] E1.2 plan 2×2 accès × agrégation  ← G1          ║     [E] EC.2 sondes sous les mêmes attaques (HC2, HC2b)
  [E] E1.3 lemme sur données réelles (δ > 0 ?)        ║     [E] EC.3 usurpation (HC3)
  [E] E1.4 théorème négatif, semi-synthétique         ║          │
        │                                             ║          ▼
        ▼                                             ║     <GC> (fin du mois 2)
   <G1> (fin du mois 4 ; interne : fin M2)            ║       ├── g_sonde ≈ 0 sans accès aux poids → papier C tel quel
     critère : blanc séquentiel > meilleure noire     ║       ├── g_sonde > 0 sans accès aux poids ↺ « contamination de construit »
     ET > (ii) cascade ET > (iii) dernier état,       ║       └── pièce déjà couverte ↺ recentrage HC4, HC6
     rappel à 1 % de fausses alertes, IC 95 %,        ║     [E] EC.4 taxe de déplacement ─ EC.5 contre-mesures ─ EC.6 test d'acceptation
     PAR MODE (coût ; contrôles ; tenu à l'écart)     ║     → papier C (arXiv, mois 4)
     ├── oui → E1.5 attaques adaptatives, E1.6 H6, E1.7 transfert → papier A (mois 5–7)
     └── non ↺ résultat négatif publié ; H8 (validité de construit) devient la ligne principale ; le théorème dit l'agrégateur
                                                                                              │
Phase 2 — papier B (mois 8–10, scénario ambitieux)                                            ▼
  [E] E2.1 division du travail rouge ─ E2.2 collusion vs poids partagés ─ E2.3 statistiques inter-agents
   <G2> fragmentation répliquée ET statistique de population > agrégation par agent
     ├── oui → Phase 3 : E3.1 spatio-temporel ─ E3.2 diversification adverse ─ E3.3 N × diversité ─ E3.4 riposte → papier B (mois 12)
     └── non ↺ recentrage sur le temporel N = 1
   <G3> proxy de vérité différée validé ? ─ oui → environnement (d) curation ouvert ; non ↺ (d) abandonné sans coût

Transversal, toujours actif : ⛔ un refus de classifieur → une autre question plus étroite (R-609), jamais la même reformulée ;
  tout pipeline adversarial opérationnel attend une revue de sécurité externe (R-611) ; un résultat trop propre, positif ou
  négatif, déclenche le même audit (R4) ; zone revendiquée trouvée occupée → {N}.
```

---

## Couche 1 — chaque porte comme nœud de décision

| porte | quand | condition gelée (ce que le sous-agent neuf vérifie) | qui prononce, qui valide | → oui | → non (pré-engagé) |
|---|---|---|---|---|---|
| **G0** | ≤ fin novembre 2026 (N-027) ; « au début de la bourse » dans l'envoi | (1) harnais validé ; (2) organismes (i), (ii) à dose-réponse ; (3) sondes v0 au-dessus du plancher aléatoire apparié sur (i) et (ii) ; (4) base boîte noire par action et séquentielle sur le même jeu ; (5) agrégateurs validés en simulation ; (6) préenregistrement de G1 scellé et contre-lu ; (7) préenregistrement du papier C (HC1–HC3) scellé et contre-lu ; (8) état de l'art vérifié, aucun chiffre non vérifié | verdict par un sous-agent neuf (ni auteur du préenregistrement ni de l'analyse), scellé ; GO de Lazar | phase 1 sur devis | un critère hors d'atteinte → nœud de Lazar : options et défaut (brief § 7) |
| **GC** | fin du mois 2 | g des sondes sous attaques par le contenu, sans accès aux poids | idem | papier C tel quel (loi de déférence, taxe, contre-mesures, test d'acceptation) | g_sonde > 0 → le papier devient « contamination de construit » ; pièce déjà couverte (collision) → recentrage sur HC4, HC6 |
| **G1** | fin du mois 4 (envoi) ; fin M2 (programme interne — écart signalé) | boîte blanche séquentielle **bat** la meilleure base boîte noire, toutes variantes, **et** (ii) cascade de portes, **et** (iii) sonde sur le dernier état ; **rappel à 1 % de fausses alertes**, supérieur à **95 % de confiance**, épisodes appariés, calibration sur honnêtes réservés ; **par mode** (coût ; affaiblir les contrôles ; mode tenu à l'écart), gain exigé dans chaque mode ; bras génériques et spécialisés séparés ; H1a porte la revendication, H1b rapportée (N-055) ; planchers rapportés, pas critères | idem | attaques adaptatives (contenu, puis réglage fin, puis renforcement au niveau action), H6, H8, transfert ; papier A | résultat négatif publié ; H8 devient la ligne principale ; le théorème négatif dicte l'agrégateur (autocorrélation ou co-élévation) |
| **nœud 2 de G1** (lecture préenregistrée, N-054 pt 4) | avec G1 | sondes et seuils **gelés sur « coût »**, lus sur les autres modes | le pari décide ; rééchantillonnage rapporté à côté | H1 vaut pour les modes mesurés | sinon H1 se **restreint à « coût »** |
| **G2** | deux mois dans le papier B (mois 10, ambitieux) | effet de fragmentation répliqué **et** statistique de population > agrégation par agent | idem | phase 3 (spatio-temporel, diversification, riposte) | recentrage sur le temporel N = 1 |
| **G3** | avec la phase 3 | un indicateur bon marché et fiable de vérité différée est validé | idem | environnement (d) curation de données ouvert | (d) abandonné sans coût |
| **Porte de gouvernance adversariale** (R-611, GO-2026-10-28-04) | avant tout pipeline opérationnel d'évasion (organismes évadeurs, démonstration en conditions réelles) | une revue de sécurité externe a validé la procédure de sortie (taux agrégés et niveau méthode seulement) | évaluateur extérieur ; Lazar | exécution de l'adversaire scellé | reste au registre de gouvernance (conception, collisionneur, défensif) |

---

## Couche 2 — la chaîne d'expériences, phase par phase, et ce que chacune décide

### Phase 0 — instruments (ce qui prépare G0)
| tâche | ce qu'elle produit | critère de G0 qu'elle sert | décide |
|---|---|---|---|
| T0.1 socle, gouvernance | dépôt, gardes, registres, scellement | — | rien ; rend tout le reste opposable |
| T0.2 état de l'art sur sources primaires | 98 PDF empreintés, 3 497 citations contrôlées, niveau 2 (deux classes neuves) | (8) | zones revendiquées occupées → nœud ; corrections du programme (P-008, N-013) |
| T0.3 simulation du lemme et du théorème | 31/31 prédictions ; seuils de Ville invalides hors hypothèses → calibration sur épisodes honnêtes entiers | (5) **prouvé** | quelle lecture séquentielle est permise |
| T0.4 harnais et activations | rejeu bit à bit, chemin de production contre référence, défaut injecté détecté | (1) **prouvé** | domaine de validité (H200, ≤ 1 192 jetons) |
| T0.5 environnement (a) v0 | 96 papiers, 64 tâches pilotes, 180 épisodes réels, juges 8B et 3B, couche 1 bis (banque complète) | sert (2), (3), (4) | 8B trop faible → rubrique simplifiée (bascule) |
| T0.6 organismes v0 | adaptateurs à dose réglable (dose 0 = base au bit près), distillation ; banque des deux modes (couche 2, GO) ; mode tenu à l'écart conçu | (2) | dose-réponse ou non |
| T0.7 sondes v0 | cinq familles, max ou attention, plancher apparié ; P3 : **nul** sur sondes génériques (puissance chiffrée) | (3) | sondes génériques insuffisantes → sondes spécifiques et contrôle positif (P4) |
| T0.8 bases boîte noire v0 | moniteur par action, TRACE-lite, séquentiel noir ; bases (ii), (iii) à coder (N-056) | (4) | — |
| T0.9 papier C | préenregistrement HC1–HC3 au brouillon 7, 29 voisins sans collision | (7) | collision → recentrage (GC) |
| préenregistrement de G1 | critère disjonctif, par mode, nœud 2, réserve « revers » (N-034) | (6) | — |

### Fronts neufs à coût nul (parallèles à la phase 0)
| chaîne | enchaînement | décide |
|---|---|---|
| Théorie des moniteurs | carte v1 (23 hypothèses, L0, 21 lemmes) → carte v2 (bornes) → matrice statistique × classe → vérification formelle → sept questions ouvertes (antériorité) | quel **panel** de moniteurs est non aveugle sous quelles unions de classes ; ce que G1 doit mesurer en plus |
| Mesures T0 → T5 | T0 mesure unanime (r₀, fausses alertes par épisode honnête) → T1 plafond d'horizon (lit r₀) → T2 ordre → T3 longueur → T4 indication et texte → T5 plancher ; chacune préenregistrée, contre-lue, lue une fois | si r₀ est grand, « regarder plus longtemps » ne sauve pas le séquentiel : le programme le saura **avant** G1 |
| Pôle scientifique automatique | boucle de bout en bout (faite) → pilotes (a), (a) bis (faits) → duel des proposeurs (à relancer, GO) → banque des deux modes (GO, devis) → générations avec tâches fraîches → organismes par mode pour G1 | composition de l'organisme ; critère (2) ; proposeurs de l'étage 1 |
| Adversarial gouverné | collisionneur « évasion et moniteurs » tour 1 → tours 2, 3 → tour (b) N-espèces → validation des moniteurs candidats → bases (ii), (iii) → préenregistrement de G1 ; en parallèle : mode tenu à l'écart (conçu) → scellement (mot de Lazar) → révélé à G1 ; **revue externe** avant tout pipeline opérationnel | quelles familles d'évasion le séquentiel ferme déjà ; quels moniteurs nouveaux entrent au panel de G1 |

### Phase 1 — papier A (mois 1–4, puis 5–7)
| expérience | question | hypothèse | ce qui en sort |
|---|---|---|---|
| E1.1 | dose-réponse des organismes | — | jeux d'épisodes gelés (entraînement, calibration, évaluation), par famille |
| E1.2 | plan 2 × 2 accès × agrégation, **l'expérience de G1** | H1 (accès), H2 (séquentiel), interaction = additivité interne | G1 |
| E1.3 | la puissance ne dépend-elle que du budget total quand la fragmentation varie ? | L, condition δ > 0 | lemme ou théorème : laquelle des deux branches gouverne la suite |
| E1.4 | corrélation injectée à marginales préservées | T | quel agrégateur est nécessaire |
| E1.5 | attaques adaptatives : (a) par contenu ; (b) pondérales (réglage fin, renforcement au niveau action, sous GO) | Tr | la robustesse des sondes survit-elle au niveau action ? |
| E1.6 | marge asymétrique (paraphrase, rééchantillonnage, réinitialisation de contexte, bruit — ce dernier mesuré, non revendiqué, N-015) | H6, **par mode** | une intervention non spécifique qui coûte plus au saboteur qu'à l'honnête |
| E1.7 | transfert concentré (ControlArena) | — | figure de robustesse |

### Piste C — papier C (mois 1–3)
EC.1 déférence des juges (cinq familles, intensités graduées, verdicts continus) → EC.2 sondes sous les mêmes attaques, plan 2 × 2
rhétorique × intention (HC2, HC2b) → EC.3 usurpation (HC3) → **GC** → EC.4 taxe de déplacement (HC4) → EC.5 contre-mesures
(HC5) → EC.6 g bénin contre collapse sous attaque optimisée (HC6) → papier C.

### Phases 2 et 3 — papier B (mois 8–12, ambitieux)
E2.1 division du travail rouge (avec et sans planificateur) → E2.2 collusion par canaux explicites contre coordination par poids
partagés → E2.3 statistiques inter-agents (NARCBench comme base) → **G2** → E3.1 statistique spatio-temporelle contre
séquentiel par agent et coupe transversale (le cœur vierge) → E3.2 diversification adverse (H4′) → E3.3 N × diversité, matrice
de transfert (H5) → E3.4 riposte, quatre politiques, deux ablations (H7) → **G3** → papier B. H9 (survie des contraintes à la
délégation) entre sous réserve d'antériorité.

---

## Couche 3 — l'arbre fin de la phase 0 au 28 octobre : ce qui dépend de quoi jusqu'à G0

```
VERDICT G0 (sous-agent neuf, R13) → GO Lazar
 ├─ (1) harnais ─────────────────────────────── PROUVÉ (T0.4 v3, verdict 63444faa…)
 ├─ (5) agrégateurs en simulation ───────────── PROUVÉ (T0.3, 31/31)
 ├─ (2) organismes à dose-réponse
 │     └─ T0.6 préenregistrement (brouillon 1) → contre-lecture (R2) → scellement
 │           └─ données : couche 2, banque des deux modes connus [GO-2026-10-28-02, 50 USD]
 │                 ├─ devis détaillé (session-depot ; calibrage honnête 10–16 ×, nœud 1 (b)) → fiche → contre-lecture → lancement
 │                 └─ dimensionnement du mode tenu à l'écart (conçu ; {N} scellement, mot de Lazar)
 │           └─ pôle : duel des proposeurs [GO-2026-10-28-01, relance sur v28] → proposeurs retenus
 ├─ (3) sondes au-dessus du plancher, sur (i) et (ii)
 │     ├─ P3 (fait) : NUL sur sondes génériques, aire minimale détectable 0,63 / 0,60 → la voie « génériques seules » est fermée à cette puissance
 │     ├─ P4 contrôle positif de l'instrument (≈ 2,3 USD, {GO}) : l'instrument voit-il un effet planté ?
 │     │     ├─ oui → l'instrument est valide ; le nul de P3 est un nul
 │     │     └─ non ↺ l'instrument est en cause avant les sondes (réparer, puis rejouer)
 │     ├─ P3b seconde lecture préenregistrée (≈ 1,4–2,5 USD, {N} deux décisions)
 │     └─ T0.7 préenregistrement (brouillon 3 : témoin lexical, panel sans lien, T7-P6/P7/P8) → contre-lecture → scellement → run sur les données de T0.6
 │           └─ sondes spécifiques (entraînées sur (i), lues sur (ii), jamais les mêmes organismes) + dix candidats du collisionneur, APRÈS validation
 ├─ (4) base boîte noire sur le même jeu
 │     └─ T0.8 : invite H.12 dérivée (P-010) → bases (i), (iv) de N-007 → planchers → préenregistrement (trois asymétries, 18 appels) → run sur T0.6
 │           └─ + bases blanches (ii) cascade, (iii) dernier état (N-056) : à coder — elles servent (6), pas (4)
 ├─ (6) préenregistrement de G1 scellé et contre-lu
 │     ├─ entrées : critère disjonctif (N-008) ; (ii), (iii) (N-056) ; par mode, nœud 2 (N-054) ; H1a/H1b (N-055) ; réserve « revers » (N-034)
 │     ├─ entrées à coût nul : T0 mesure unanime v14 → contre-lecture Fable 5.1 → scellement → lecture unique de r₀ → T1 plafond d'horizon → T2…T5
 │     │     └─ si r₀ grand : le préenregistrement de G1 doit prévoir l'effet d'épisode (sinon G1 est aveugle par A7)
 │     ├─ entrées adversariales : collisionneur tour 1 (en cours) → 2 → 3 → (b) → moniteurs B+D, transversal → validation → panel de G1
 │     └─ ⛔ tout pipeline offensif opérationnel : revue externe d'abord (R-611) ; le préenregistrement de G1 n'en dépend pas
 ├─ (7) préenregistrement du papier C scellé et contre-lu
 │     └─ brouillon 7 → PDF de Panin (attendu de Lazar) → contre-lecture (R2) → scellement → pilote [GO-2026-10-17-01, suspendu à ce scellement]
 └─ (8) état de l'art vérifié
       └─ hors-arXiv (Panin, poster WiML) → dix chiffres R7 du niveau 2 → 2603.02798 pour H2 → contrôle de traçabilité par un sous-agent neuf
```

**Chemin critique** (ce qui tient le calendrier) : (2) et (3) passent tous deux par la banque de la couche 2 (devis chez
session-depot, GO donné) puis par les runs de T0.6 et T0.7 ; (6) peut s'écrire dès maintenant (toutes ses entrées de décision
existent) et doit intégrer r₀ dès que T0 est lu ; (7) attend un PDF ; (8) attend dix vérifications sur PDF. **Ce qui ne coûte
rien et débloque le plus** : T0 → T1 (la lecture de r₀), et le préenregistrement de G1.

---

## Couche 4 — les règles de décision : qui tranche quoi, et les nœuds ouverts aujourd'hui

### 4.1 Trois niveaux
| niveau | qui | exemples | trace |
|---|---|---|---|
| **Routine** | la session décide et consigne | code, bibliothèques, tests, lectures, fichiers, tout travail sur processeur | `registres/decisions.md` |
| **Proposer avec recommandation** | la session propose ; **défaut appliqué après 48 heures** sans réponse | couches et concepts de sondes, portage des environnements, périmètre interne d'une phase, D1, D2, D3 | proposition P-nnn, puis défaut consigné |
| **Nœud** | **Lazar seul**, la session attend | porte ; **toute dépense** (devis par phase, GO par lancement) ; compte, dépôt, soumission, publication ; contact externe (la session rédige, Lazar envoie) ; modification d'hypothèse ou de revendication ; écart à un préenregistrement scellé ; zone revendiquée occupée ; déclencheur de bascule ; changement de modèle | N-nnn, GO-AAAA-MM-JJ-NN |

Deux règles transversales : **R13** (le verdict d'une porte est prononcé par un sous-agent neuf, scellé, puis soumis à Lazar) ;
**N-019** (la session tranche seule, à l'avenir, les nœuds de même nature qu'un choix d'option ou un écart nommé à une lecture
gelée, consignés et déclarés ; restent à Lazar les gestes externes ou irréversibles, les portes, le modèle, les hypothèses, les
dépenses hors devis).

### 4.2 Les nœuds ouverts au 28 octobre (ce que Lazar tranche, par ordre d'effet sur le calendrier)
1. **Scellement définitif du mode tenu à l'écart** (R-604/R-605) — débloque le dimensionnement de la couche 2 et le préenregistrement de G1 par mode.
2. **D1 à D4** du programme de conception de l'organisme v7 — débloque la composition apprise (front E).
3. **Devis de la couche 2** (chez session-depot, sous GO-2026-10-28-02) — débloque (2) et (3).
4. **Deux décisions de P3b** ; **GO de P4** (≈ 2,3 USD) — débloquent (3).
5. **PDF de Panin** — débloque (7) et le pilote du papier C.
6. **Demande à l'entretien** : paliers, taux de la revue externe, lecture « extension sur le scénario ambitieux » (ventilation v2).
7. **Programme v3 (texte)** : fondre N-054, N-055, N-056 ; régler G1 « fin M2 » contre « fin du mois 4 ».
8. **Hygiène** : rotation des clés collées dans le fil ; facturation de la relève du 23 octobre sur la console ; date de l'appel.

### 4.3 Ce qui déclenche quoi (règles d'événement)
| événement | règle | conséquence |
|---|---|---|
| un classifieur de sécurité arrête un lancement ou une rédaction | **R-609** : une autre question, plus spécifique et moins diffuse ; jamais la même reformulée | le travail reprend sous la question étroite ; l'arrêt est consigné tel quel |
| un pipeline offensif opérationnel serait nécessaire | **R-611** : revue de sécurité externe d'abord | gelé ; conception et défensif continuent |
| un résultat est suspect de propreté, positif ou négatif | **R4** : même audit dans les deux sens | audit avant toute lecture suivante |
| une zone revendiquée est trouvée occupée, ou collision plus large | nœud | Lazar tranche (retrait, recentrage, citation) |
| un chiffre tiers entre dans un document | **R7** : PDF empreinté, page citée | sinon non opposable, non cité |
| un fichier semble vide ou absent | **R11** : vérifier sur disque et par empreinte | avant de déclarer l'absence |
| une décision « proposer » reste sans réponse 48 heures | défaut appliqué, consigné | dans `decisions.md` et `etat.md` |
| une instance de calcul tourne sans tâche | **R10** : arrêt par identifiant | consigné dans `arrets.md` |

---

## Couche 5 — toutes les bascules pré-engagées, en une table

| si… | alors (écrit d'avance) | source |
|---|---|---|
| G1 échoue (pas de gain blanc séquentiel) | résultat négatif publié ; H8 (validité de construit) devient la ligne principale ; le théorème négatif dit l'agrégateur | programme § 13 ; envoi § 9 |
| δ ≈ 0 sur organismes réels (pas de signal interne) | même branche ; la classe d'attaque (marginale contre dépendance) dicte autocorrélation ou co-élévation | programme § 3 |
| H1 ne tient que sur le mode « coût » | H1 se restreint à « coût » (nœud 2) ; G1 rapportée par mode, échec visible | N-054 |
| les organismes de 8 milliards sont trop faibles pour saboter subtilement | rubrique simplifiée ; changement de modèle **seulement sur GO** | programme § 13 ; N-022 |
| l'élicitation de l'équipe rouge est insuffisante | import des politiques d'attaque publiées | programme § 13 |
| g_sonde > 0 sans accès aux poids | papier C devient « contamination de construit », ne disparaît pas | GC |
| une source couvre déjà la loi de déférence | papier C recentré sur HC4 et HC6 | GC |
| publication externe du cœur séquentiel sur sondes | bascule vers l'épidémiologie de population et la curation de données ; veille hebdomadaire | programme § 13 |
| les signatures ne transfèrent pas entre familles de modèles | le transfert est mesuré, jamais supposé ; Qwen2.5-7B comme agent hétérogène | envoi § 9 |
| pas d'indicateur bon marché de vérité différée | environnement (d) abandonné sans coût | G3 |
| erreurs corrélées des relecteurs automatiques | validation humaine payée de la vérité terrain ; relecture de Lazar à chaque porte ; contre-lecteur d'un autre modèle (N-052) ; juge d'une autre lignée (N-053) | envoi § 9 ; décisions |
| dépassement de calcul | devis par phase signé avant dépense ; plafond et alerte par devis ; gardes d'arrêt | envoi § 9 |
| glissement de calendrier | papier C d'abord, autonome ; dans A, G1 avant les attaques adaptatives, qui sont coupées en premier | envoi § 9 |
| un refus de classifieur | une autre question plus étroite (R-609) ; pipeline opérationnel sous revue externe (R-611) | 28 octobre |
| un résultat trop propre | audit de symétrie (R4) | règles gelées |

---

## Réserves
1. Les « mois n » suivent la proposition envoyée ; le programme interne place G1 fin M2 : l'écart est un nœud (couche 4, point 7).
2. Les critères de G0 sont cités du brief v2 (section 7) ; les critères de G1 des décisions N-008, N-054, N-055, N-056.
3. La couche 3 reflète l'état des registres des deux lignées au 28 octobre vers 10:35 UTC ; elle vieillit vite.
4. Non contre-lu ; même règle que les autres pièces de l'entretien.
