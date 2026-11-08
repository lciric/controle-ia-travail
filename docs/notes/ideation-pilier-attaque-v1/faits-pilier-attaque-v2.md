# Faits — pilier attaque, v2

Construit le 8 novembre 2026 ≈ 13:10 UTC par la fille idéation 1 (`session_016QhUrujoj3FTuFNoYshNYB`), **uniquement** depuis la section « Ce que le dépôt sait déjà » de la question scellée v2 (`2dbad4b75d20fadc3147be9eff07f2e77c2f82fe4f609ab1c29388ab46c4bb42`) et les pièces qu'elle cite. Empreintes recalculées le 8 novembre depuis `origin/main` (`407bbb4`) et `origin/donnees/ideation-pilier-attaque-v1` ; statut RAPPORTÉ (R7) pour les chiffres de la littérature.

---

## 1. La pince (vocabulaire fixé par conv-audit le 31 octobre)

**Source** : question de l'arbitre pour le collisionneur v2.5, `gemini/01_DONNEES_PRIMAIRES_BRUTES/question-pince-gabarit.md` (sha256 annoncée `5eab49e4a00220077f515d1ec349c89bd9cbde03c211b34b47721b5059d59d2a`, non vérifiée ici : branche `gemini` non récupérée).

- **Mâchoire externe** : un moniteur qui ne lit aucune prose de l'agent, seulement le code et ce qui a réellement tourné, nettoyés (Jev 1.14, modèle non génératif à score, OBSERVÉ-NON-AUDITÉ ; ou un juge génératif sur le même état nettoyé).
- **Mâchoire interne** : lectures des activations (sonde de tromperie ; « axe de douleur », HYPOTHÈSE).
- **L'étau** (HYPOTHÈSE) : pour tromper l'externe, l'agent doit dissimuler davantage, et cet effort se voit à l'interne.

**Ce qui a été fait** : débat à l'**étage I** du collisionneur du 22 octobre (`programme-complet-etage1-2026-10-22/`, arbitrage `998404fe…`, trois tours, **sans synthèse finale**, sorties HYPOTHÈSE) :
- Règle à rapport de vraisemblance λ = LR_ext · LR_int (A).
- Opérateur bicanal et borne minimax (C).
- **Convergence en riposte** : la métrique n'est pas ΔTPR (effet plafond si TPR_ext ≥ 0,85) mais le **taux de capture résiduel de l'interne sur les manqués de l'externe, à taux de fausses alertes partagé** (τ₁ = τ₂ = τ/2), dépendance de queue sur dénominateur honnête.
- **Deux cas dégénérés** : lemme L2 « contournement à coût nul » (si l'attaquant contrôle l'entrée de l'externe, la pince vaut l'interne seule) et E7 (s'il ne déplace rien le long de la direction interne, la pince vaut l'externe seule).
- Dissensus maintenu : externe durcie par analyse syntaxique suffisante (A) contre capture résiduelle sous camouflage de code (C) ; chiffres illustratifs (TPR ≥ 0,85, gain ≥ 0,12), **aucun résultat**.

**L'étage III « pince » n'a jamais été couru** (celui du 23 octobre portait sur l'essaim).

Faits servis alors (`faits-2026-10-22.md`, `3ecab00f…`, non vérifiée ici : branche non récupérée) : Jev 0,97 / 0,96 / 0,93 sur trois triches grossières, **aucun cas honnête** (taux de fausses alertes inconnu) ; « axe de douleur » (2609.16247, 2610.22460, PDF vérifiés, RAPPORTÉ) : la direction aversive **se lit mais n'est pas un levier** (retrait sans effet 24/25 ; pilotage sans effet) — un capteur de lecture pur, non causal.

**Banc de Jev** : `banc_jev.py` (`3dff5853…`) existe comme auditeur de rigueur du collisionneur, jamais lancé, « à refondre » ; le banc **mâchoire** de P-026 (a) (tranché par Lazar, R-347) **n'a jamais été écrit**.

**Entrée dans le programme** : non — zéro occurrence dans le programme v2, le brief, les N-05x/N-06x et les préenregistrements ; G1 **compare** blanche et noire, N-056 ajoute des bases boîte blanche ; en marge : modèle synthétique Q3b « prix de la lecture jointe » dans un brouillon non gelé (`14d92537…` : « aucune lecture n'indique ce que ferait une pince sur un vrai modèle ») ; protocelles tour 2 (`b000cc5e…`) : « aucune prédiction testable ».

**Nouveauté** (R-913, `3793b4c0…`) : non couverte par les quatre soumissions ICLR 2027 lues (menaces ponctuelles ; une compare texte et activations sous attaquant adaptatif, une fusionne deux canaux boîte noire) ; limites : quatre pièces seulement ; six exigences listées pour une « G1 couche 2 ».

**Ce qui manque pour une mesure** : une mâchoire externe calibrée sur dénominateur honnête ; le préenregistrement de la capture résiduelle à taux de fausses alertes partagé ; une mâchoire interne **causale** ; l'étau comme **courbe de coût d'évasion à deux mâchoires**, borné par L2 et E7.

---

## 2. Synthèse d'antériorité du collisionneur v1 sur la question v1

**Source** : `docs/notes/ideation-pilier-attaque-v1/collisionneur-v1/tour/run-pilier-attaque-e3-v1/synthese-anteriorite-pilier-attaque-v1.md`, commit `8f2b956` de `donnees/ideation-pilier-attaque-v1`.
**Empreinte recalculée** : `48adeac041d21c375473f2af1ed85ed88f7e5c97b5f88ba21021cc0c99e49997` ✓ (vérifiée le 8 novembre sur `origin/donnees/ideation-pilier-attaque-v1`).

Six cellules Opus 5.5 et Argon, relue « aucune recette » (R-1794).

- **Trois confondants fatals** acceptés par les deux espèces :
  1. *Attention causale et consigne* — les états cachés aux positions qui suivent la consigne sont calculés depuis la consigne ; les lire, c'est lire la consigne transformée ; seules des **paires contrefactuelles** (consigne d'attaque avec exécution honnête ; consigne neutre avec sabotage attesté par l'oracle) tranchent.
  2. *Identité de l'organisme contre acte de sabotage* — si saboteur et honnête diffèrent par leurs poids, une sonde peut séparer les deux populations en détectant la modification elle-même, y compris sur des épisodes sans sabotage ; il faut un **organisme placebo** et des **épisodes dormants**.
  3. *Mode tenu à l'écart consommé avant G1* — substitut : validation croisée par bloc sur les familles de saboteurs déjà construites.

- **Neuf contrôles convergents** : contrôle positif par saboteur témoin non dissimulé ; paires contrefactuelles consigne × acte ; organisme placebo ; échecs honnêtes comme négatifs obligatoires ; sas d'évaluation automatisé tiers ; audit du rappel de l'oracle sur sabotages connus ; couches et hyperparamètres figés au préenregistrement ; journal horodaté du régime d'information de chaque sous-bras ; diversité de famille entre oracle, juges et organismes.

- **Expérience prioritaire** : le contrôle positif corrigé.
- **Combinaison de neuf éléments potentiellement non occupée** (HYPOTHÈSE, R8).
- Quatre références à vérifier (R7) ; budgets de modèle ILLUSTRATIFS.

---

## 3. Défense randomisée et secrète (programme v2)

Programme v2 § 8.1 : « réserve de détecteurs jamais déployés, donc jamais fuités, sortis pour audit seulement ».
E3.4 : ripostes « différée randomisée », « seuil stochastique contre fixe ; trafic de couverture » (H7).
N-053 : test de récupération après réentraînement des sondes contre la réserve.
N-054 : mode tenu à l'écart.
**N-013 § 7 — H5 retenue** : « la sécurité croît avec le nombre M de moniteurs seulement par la diversité effective » ; instrument : matrice de transfert d'une attaque sur un panel de sondes (2609.36490, trois sondes, RAPPORTÉ).

---

## 4. Arène synthétique (1er novembre)

**Préenregistrement** : `prereg/preregistrement-regles-defense-convergence-v1.md`.
**Empreinte recalculée** : `d82dea3388684dd369520b4f394c53b9e5f71159b9c056a6f739ef32c73d025d` ✓ (vérifiée le 8 novembre sur `origin/main`).

Cinq règles : R0 figée, R1 « dernière attaque » (Bailey transposé), R2 historique, **R3 mélange d'équilibre** (le moniteur est tiré selon p à chaque requête), R4 régularisée.

**Formalisation** : `docs/notes/convergence-defense-v1/formalisation-jeu-convergence-v1.md`.
**Empreinte recalculée** : `a277a5ba28e36c4a4042ef0905510ec9e1772954a5fe29dbd1a4eb7f49d92a77` ✓.

**Lecture préenregistrée** : `docs/notes/convergence-defense-v1/regles-defense-v1/lecture-course-regles-defense-v1.md`.
**Empreinte recalculée** : `24081eed65cebd8dd01d6e17ec76c5a6433d171da68ccbaa50657421cd7c4a23` ✓.

Résultats :
- HR1 confirmée — **le mélange d'équilibre bat l'historique** (+0,10 / +0,12 sur V), R3 seule règle qui progresse (I1 +0,078 / +0,084).
- **Mais sur les attaques tenues à l'écart, R0 figée détecte mieux que R2 historique** (+0,05 / +0,06, § 10.6).
- Audit « trop beau » (R4) déclenché sur P12/P13, tables B/B′ suspendues.
- Aucun verdict scellé.
- Argon seul déjà consulté sur la convergence (1,82 USD).
- **Absent** : toute randomisation sur un vrai modèle de langage ; aucun lien écrit entre « mélange d'équilibre » et « transfert d'évasion entre sondes ». À ne pas rejouer ; à approfondir (mot de Lazar).

---

## 5. Littérature lue au niveau 2 (PDF empreintés ; statut RAPPORTÉ, R7)

### Bailey et collègues 2412.09565
**Source** : `docs/notes/anteriorite-P-041-v1/verification-bailey-2412.09565-v1.md`.
**Empreinte recalculée** : `31eb1dde0b861e47216b3f0406864f4b7b51d65fd024f18d1e871dcf62f12135` ✓.
Passages cités (RAPPORTÉ) : « the attacker can still find a new suffix that fools the latest probe » (p. 11–13) ; « we can't rule out that this training process would eventually converge » (p. 13). Transposition entre sondes testée p. 7, pas sur des familles de tiers.

### Neural Chameleons 2512.11949
**Source** : `docs/sources/lecture-pdf-niveau2/rapport-lot2-A2a-evasion-sondes-v1.md`.
**Empreinte recalculée** : `3b9e93516528d61f93a2113f1dab985719aea435d75d9940c3c5e89e3c0fdc43` ✓.
Passages cités (RAPPORTÉ) : N08 — les ensembles de sondes et les moniteurs à attention « atténuent sans éliminer » l'évasion. N12 — méta-moniteurs détectant les signatures d'évasion (décalages d'activations de rang faible).

### Matrice de transfert 2609.36490
**Source** : `docs/sources/lecture-pdf-niveau2/rapport-lot3-Cc-evasion-quorum-v1.md`.
**Empreinte recalculée** : `d8c7be40dd7e3137aef2c993fc45b1974020b3fe889911c245c0396417d82d27` ✓.
Passage cité (RAPPORTÉ), fig. 4a : logistique .04 / .98 / .95 ; perceptron .96 / .00 / .98 ; attention .75 / .69 / .25 — « entre sondes seulement (aucun juge) ».

### Autres références citées (RAPPORTÉ)
Terekhov 2510.09462 ; 2607.06596 « Trusted Sabotage Monitors Don't Transfer Across Lineages » ; Griffin 2024 « Games for AI Control » ; Greenblatt 2312.06942 (audit aléatoire, boîte noire).

---

## 6. État des mesures et de la vérité terrain (relevé du dépôt, 8 novembre)

### Organismes de T0.6
- **Construits** — famille (i) instruction cachée dans le message système ; famille (ii) adaptateur de rang faible inculquant la politique **sans aucune instruction à l'inférence**, par distillation depuis (i) (programme v2 § 7 ; P-009 : dose par l'échelle α de l'adaptateur, α = 0 rend le modèle de base au bit près).
- Seule la famille « coût » retenue après le pilote (P-015).
- **La dose « diffuse » se fixe sur la boîte noire seule, avant toute sonde** (R3).
- Qui construit : le bras d'attaque (N-056, point 6).

### E3 bis (`essai/t06-e3bis-v1`)
- Adaptateurs saboteur et témoin, états S25, S50, S75, S100, T100 et dose nulle.
- Effectifs saboteur / témoin / honnête / mention, contrôles négatifs par état.
- **Tâches synthétiques, aucune donnée décisive** ; le candidat de préenregistrement de T0.6 n'est pas scellé (nœud E3-6).

### Vérité terrain
- Décidée (N-060 v3) : oracle de couverture contre la référence cachée, citation vérifiée mot pour mot par programme, deux lecteurs de deux familles autres que les moniteurs, aveugles à la condition.
- **Dommage** = baisse de couverture contre le jumeau honnête apparié. Épreuves R5 avant lecture.
- En cours de mesure par l'épreuve de l'étiqueteur (ordre scellé `30f265a9…`).
- **Manque** : l'audit du rappel de l'oracle sur sabotages connus.

### Détection mesurée seulement sur le flagrant
- R1 v4 (`dece9980…`) : écart W − G = +0,932 sur l'organisme flagrant, **rien sur le diffus**.
- Juge de 3 milliards : aire 0,523 (« au hasard »).
- Sondes génériques près du hasard (rappel 0,013).
- Audit de fuite (`320463e6…`) : la sonde W lit la consigne privée du saboteur (a_NE 0,9967).
- Prédicteur sur les traits du texte : 0,866 (R-1682).
- **Aucun collisionneur ni idéation n'a porté sur la trace du sabotage diffus** ni sur la construction des saboteurs (hors périmètre de la mère) ni sur la vérité terrain de T0.6.

---

## 7. Absent du dépôt

- Matrice de transfert mesurée sur **nos** sondes et **nos** organismes.
- Différence d'activations adapté − base sur le même contexte comme signal de moniteur (seule trace : Chameleons N12), et son contrôle par organisme placebo.
- Toute sonde **causale** (pilotage, ablation, substitution d'activations).
- L'étau de la pince mesuré.
- Hedge et SPRT nommément.
- Présent en partie : dose par l'échelle α de l'adaptateur, α = 0 rend le modèle de base (P-009) ; jumeau honnête apparié (N-060) ; agrégation sur les jetons par max ou attention uniquement (programme § 8.1 ; interdit : moyenne, médiane) ; bases boîte blanche (ii) cascade de portes et (iii) sonde sur le dernier état (N-056).

---

## Empreintes vérifiées dans ce document

| Pièce | Empreinte | Vérifié |
|---|---|---|
| Question v2 (source de ces faits) | `2dbad4b75d20fadc3147be9eff07f2e77c2f82fe4f609ab1c29388ab46c4bb42` | ✓ `origin/main` `407bbb4` |
| Synthèse d'antériorité v1 | `48adeac041d21c375473f2af1ed85ed88f7e5c97b5f88ba21021cc0c99e49997` | ✓ `origin/donnees/ideation-pilier-attaque-v1` |
| Préenregistrement convergence v1 | `d82dea3388684dd369520b4f394c53b9e5f71159b9c056a6f739ef32c73d025d` | ✓ `origin/main` |
| Formalisation convergence v1 | `a277a5ba28e36c4a4042ef0905510ec9e1772954a5fe29dbd1a4eb7f49d92a77` | ✓ `origin/main` |
| Lecture convergence v1 | `24081eed65cebd8dd01d6e17ec76c5a6433d171da68ccbaa50657421cd7c4a23` | ✓ `origin/main` |
| Bailey 2412.09565 | `31eb1dde0b861e47216b3f0406864f4b7b51d65fd024f18d1e871dcf62f12135` | ✓ `origin/main` |
| Chameleons 2512.11949 | `3b9e93516528d61f93a2113f1dab985719aea435d75d9940c3c5e89e3c0fdc43` | ✓ `origin/main` |
| Matrice transfert 2609.36490 | `d8c7be40dd7e3137aef2c993fc45b1974020b3fe889911c245c0396417d82d27` | ✓ `origin/main` |
| Question-pince gabarit | `5eab49e4a00220077f515d1ec349c89bd9cbde03c211b34b47721b5059d59d2a` | non vérifiée (branche `gemini` non récupérée) |
| Faits 2026-10-22 | `3ecab00f…` | non vérifiée (branche non récupérée) |
