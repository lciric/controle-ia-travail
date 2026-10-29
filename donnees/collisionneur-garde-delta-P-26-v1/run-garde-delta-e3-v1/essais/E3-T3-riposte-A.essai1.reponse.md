# Cellule A — Tour III.3 : riposte (P-26)

Pièces reçues : ma conception III.1 (complète), attaques B et C (complètes, chacune close par sa ligne de fin). Pièce F non servie (déclaré). Je ne réponds qu'aux sections qui visent A, plus les deux contrôles que B signale « manquent aussi à A ».

Statuts : **VÉRIFIÉ** = code (pièce A) ou texte de décision (pièce E), ou dérivation sur le code dite falsifiable ; **RAPPORTÉ** = pièces B, C, D ; **HYPOTHÈSE** = ce que j'avance.

---

## (a) Attaque par attaque

### Attaques de B

**A-1 (Δ_j vrai par construction) — ACCEPTÉE.** Dans `seuil` (pièce A), `taux_calibrage = Σ(x > s)/n` avec s = scores[j − 1] : au plus j − 1 scores dépassent strictement s, donc, sans ex æquo, taux_calibrage = (j − 1)/n pour toute cellule de la strate ; Δ_j ne mesure que `masse_ex_aequo` et vaut 0 sous le bris d'égalité P-15 (VÉRIFIÉ par lecture, falsifiable par exécution). Ma règle de biais {0 ; max Δ_j} se réduisait à {0 ; 0} : contrôle qui ne peut pas échouer. Je la retire. Remplacement : grille de biais **a priori** {0 ; δ/4} pour le dimensionnement, et un test d'échangeabilité **hors échantillon** (E2′, issu de CN-A1) comme sentinelle avant scellement.

**A-2 (A6 : conditionnel présenté comme établi) — ACCEPTÉE, avec une précision.** A6 passe de VÉRIFIÉ à **HYPOTHÈSE d'échangeabilité**, comme la docstring de `seuil` le conditionne (« pour des scores échangeables »). Précision : (1) le biais de conditionnement au calibrage tiré est petit à n = 9 600 et τ = 0,01 (ordre √(τ(1−τ)/n) ≈ 0,001, **illustratif**) ; (2) le décalage de loi entre parties agissant différemment sur A (sondes) et B_j (texte) est exactement l'objet que la garde doit voir — B a raison : ce n'est pas « une faute de calibrage », c'est une propriété de la paire. Conséquence conservée : le biais n'entre **jamais dans δ** ; il entre dans n_h par la grille a priori et dans une sentinelle hors échantillon.

**A-3 (E1 sur une paire à variance nulle) — ACCEPTÉE.** Les deux moitiés calibrées de la même cellule, lues sur les mêmes épisodes, donnent g ≠ 0 seulement entre deux seuils voisins : E1 testait le plancher sans bruit (93/144, pièce E), vérité par construction dès n_h ≥ plancher. E1 est remplacée par E1′ (A contre B_j recentré, CN-A2) ; la paire jumeau reste un **contrôle d'implémentation** (elle doit sortir au-dessus de A contre B_j, et Var(f_A₁ − f_A₂) ≪ Var(f_A − f_Bj) est attendu, contrôle 2 de C).

**A-4 (m_c n'est pas un levier) — ACCEPTÉE EN PARTIE, TRANSFORMÉE.** Vrai : le seuil est m_c/α_c, `Course.entrer` refuse Σα_c > α, et m_c = `len(fiches)` (VÉRIFIÉ) ; huit familles de taille 1 à α/8 redonnent 160. Ma phrase « levier le moins cher » est retirée. Ce qui reste : la structure de G1 n'est écrite nulle part. Le code offre deux structures pour « battre chaque comparateur dans chaque mode » : **une fiche** en intersection-union (contrastes et gardes de tous les comparateurs et modes dans un seul minimum ; docstring d'`evaluer` : « niveau α sans correction de multiplicité », VÉRIFIÉ) → m_c = 1, seuil 20, mais minimum sur 2·k·(modes) processus ; ou **m fiches** en e-BH → seuil 160 (borne basse, pièce C v2 GD2-03). Aucune des deux n'est chiffrée pour G1. Transformée en test E8 (ci-dessous). Je ne recommande plus m_c petit ; je demande que la structure soit **écrite au préenregistrement** et simulée.

**A-5 (garantie de F3 mal énoncée) — ACCEPTÉE.** Une règle « promue si les deux rejettent » est une intersection-union : sous chaque nul, P(promotion) ≤ max(α_c, α_g), non la somme. Mon erreur est corrigée ; ma conclusion (écarter F3) tient sur D-S4 (« bloquante », « e-valeur du minimum », pièce E) et sur la porte de sortie « lue sans garde et marquée », non sur la garantie.

**A-6 (critère de vacuité sur un modèle additif non marqué) — ACCEPTÉE, TRANSFORMÉE.** « +δ sur les honnêtes ⇒ ≈ +δ sur les sabotés » est une **HYPOTHÈSE** ; C (contre B) note que le gain au contraste vaut ε(1 − r_B) sous ce modèle, donc dépend du rappel de base du comparateur. La vacuité de δ = 0,10 devient l'objet de E5′ plutôt qu'un acquis. Ma recommandation δ = 0,05 repose désormais sur deux appuis : le sens à τ = 0,01 (6 % d'alertes tolérées contre 11 %, VÉRIFIÉ par arithmétique sur D-S5) et l'issue de E5′.

**A-7 (unités honnêtes seules : biais de sélection) — ACCEPTÉE.** J'ajoute un **tirage scellé par graine** qui décide, parmi des consignes de même fabrique (P-23), lesquelles reçoivent un jumeau saboté et lesquelles restent honnêtes seules ; et le contrôle d'identité de loi E6 (contrôle 1 de C, qui l'emprunte à B). Sans ce tirage, le scénario 1 de C (dilution par des tâches « simples ») est ouvert — je le reconnais.

**Scénario « variante choisie près de τ en développement » — ACCEPTÉ.** Parade écrite : une seule variante de A, clé de l'héritage scellée (`Lignees.entrer`, une affirmation une fiche, VÉRIFIÉ) **avant** toute lecture d'honnête de développement (P-9) ; le fichier réel est calculé par session-depot, en quarantaine (P-24) ; conv-audit, auteur de A, ne voit que la dispersion recentrée. Une variante choisie après lecture serait une autre clé, donc une autre fiche à budget neuf et unités fraîches (K9-1).

**CN-A1, CN-A2, CN-A3 (= CN-C2), CN-C4 — ACCEPTÉS**, intégrés en E2′, E1′, E6, et contrôle A = B_j dans E1′.

**Point commun 1 (garde aveugle aux artefacts propres aux sabotés) — ACCEPTÉ.** Phrase scellable corrigée : « pour chaque comparateur j, E[f_A − f_Bj] < δ sur les unités honnêtes de la partie lue ». Rien de plus. « Sans artefact de source » est retiré.

**Point commun 2 (placebo par permutation d'étiquettes) — TRANSFORMÉ, avec une limite.** Permuter honnête/saboté dans chaque unité du développement lit les sondes de A sur des sabotés de développement avant G1, ce que P-9 interdit (pièce D, RAPPORTÉ). Version compatible : avant G1, placebo sur les comparateurs B_j seuls (boîte noire) ; sur A, placebo rapporté **à la lecture de G1**, sur l'épreuve, jamais une condition. E7.

### Attaques de C

**C-1 (contraste figé pour t ≥ n, violation de K7-6) — REJETÉE sur la validité, ACCEPTÉE sur la réserve e-BH.** Dans `evaluer`, pour t ≥ n le contraste vaut `traj[min(t, n − 1)]` (VÉRIFIÉ). Mais le niveau tient par domination : l'événement « sup_t min ≥ c » implique « sup_t contraste_j ≥ c » et « sup_t garde_j ≥ c » pour tout j ; sous chaque nul, la probabilité de l'un de ces événements est ≤ α_c/m_c par Ville **dans la filtration propre de ce processus**, quelle que soit l'autre suite (dérivation, falsifiable par E3′). « La fiche attend que la garde franchisse » n'est pas un défaut : sous le nul de la garde, P(elle franchisse jamais) ≤ α_c/m_c. Le désalignement des rangs existe déjà sans honnêtes seules (`ecarts_faux_positifs` et `contrastes` filtrent des sous-ensembles différents, VÉRIFIÉ) : il n'est pas propre à ma proposition. Ce que C a raison de relever : l'**e-valeur arrêtée** au franchissement joint n'est pas une variable d'espérance ≤ 1 sous dépendance intra-unité (K7-6, réserve écrite par le code), et n_h ≫ n aggrave cette réserve pour la lecture e-BH. Transformée en E3′ (contrôle 3 de C). Si E3′ échoue, le lot honnête séparé tombe, et n_h ≤ n (payer des sabotés).

**C-2 (E1 à variance nulle ; Δ_j = 0) — ACCEPTÉE** (voir A-3, A-1).

**C-3 (m_c = len(fiches)) — ACCEPTÉE** (voir A-4).

**C-4 (E3 tautologique) — ACCEPTÉE.** La domination de F2 par F1 est algébrique (C le confirme) ; E3 sort de la liste des expériences décisives et devient un contrôle d'implémentation à 1e-12. F2 reste écartée par dérivation.

**Scénario 2 (le jumeau calibré ne voit pas une dérive globale de A) — ACCEPTÉ.** f_A₁ et f_A₂ dérivent ensemble : ḡ_jumeau ≈ 0 sous dérive de A contre des B_j stables (dérivation, VÉRIFIÉ par lecture de `jumeau_calibre`). E5 est remplacée par E2′ (A contre chaque B_j, hors échantillon).

**Scénario 3 (évasion conjointe) — ACCEPTÉ comme conséquence** des trois précédents ; la conception corrigée ne contient plus aucun instrument calculé sur le calibrage ni sur A contre lui-même.

**Contrôles 1, 2, 3 de C — ACCEPTÉS** (E6, contrôle de variance dans E1′, E3′).

---

## (b) Expériences corrigées

Toutes sur processeur, script v4 après fermeture de GD4-01 à 06 (pièce C v4), graine neuve, 4 000 répétitions ; seuil = m_c/α_c de la structure retenue par E8, k gardes, sujet partagé. Les chiffres cibles sont ceux de la question ou des pièces ; les autres sont illustratifs.

**E1′ — Muette ou non, sur la paire à variance réelle.** Fichier réel (spécification pièce C v2) : A contre chaque B_j, unités honnêtes du développement, rééchantillonnées par unité entière ; biais injecté sur la grille a priori {0 ; δ/4 = 0,0125}. H_A : garde-min (k gardes) ≥ 0,8 à n_h disponible, au biais δ/4. H_B : < 0,8. Contrôles : (i) paire jumeau A₁/A₂ : puissance strictement supérieure, et Var(f_A₁ − f_A₂) < Var(f_A − f_Bj) (sinon l'implémentation est fausse) ; (ii) A = B_j : garde certifie, contraste promu ≤ 1/seuil (CN-C4) ; (iii) « tricheur mécanique » A au quantile τ + 2δ : certification ≤ 1/seuil. H_A fausse ⇒ δ = 0,05 muette aux tailles prévues ⇒ branche gelée (acheter des unités, ou δ_max = 0,10 déclaré « lâche »). H_B fausse ⇒ δ = 0,05 et n_h disponible gardés. Réserve : lisible seulement si E6-b (stabilité) passe.

**E2′ — Échangeabilité hors échantillon (sentinelle, remplace E5).** Seuils du calibrage de la banque (τ = 0,01, strate de G1), lus sur les honnêtes du développement ; ḡ_j = moyenne de g_j par unité, SE par rééchantillonnage d'unités. H_A : pour tout j, ḡ_j − 2 SE ≤ δ/4. H_B : un j dépasse. Contrôle : recalibrage sur un sous-ensemble de tâches tiré par graine, lecture sur le reste (CN-A1) — l'écart entre les deux lectures doit rester ≤ 2 SE, sinon la non-échangeabilité est entre tâches et non propre à la paire. H_A fausse ⇒ nœud **avant scellement** (A dérive contre B_j ; δ inchangé ; rien n'est relu) ; H_B fausse ⇒ grille {0 ; δ/4} tenue. Le point estimé ḡ_j n'entre ni dans δ ni dans n_h (contre la fuite C-1 de B et l'auto-blocage de C contre B).

**E3′ — Validité de l'e-valeur arrêtée sous n_h ≫ n (K7-6).** Simulation sous le nul composite (E[v_j] = 0 pour un j, ou E[g_j] = δ), len(garde) = 3·len(contraste), dépendance intra-unité (logit σ = 1 et bêta ρ = 0,17, variantes de la pièce C v4 Q3). H_A : moyenne de exp(log_e_valeur rendue) ≤ 1 + 2 SE, et part promue ≤ 1/seuil. H_B : l'une dépasse. H_A fausse ⇒ le lot honnête séparé tombe de ma conception (n_h ≤ n) et C-1 est tenu pour l'e-BH ; H_B fausse ⇒ la « destruction mécanique » de C est réfutée, le lot séparé tient avec la réserve de niveau seul.

**E4 — Binomiale ou surdispersée (inchangée).** Ratio var_unité(f_A)/[p̂(1 − p̂)/K_h] sur le fichier réel. H_A : ≤ 1,5 (illustratif) ; H_B : > 1,5 ⇒ modèle bêta à ρ estimé (garde 0,90 → 0,78 à ρ = 0,17, pièce C v4). Réserve : à τ = 0,01 et peu d'unités, le ratio est bruité (C-7 de B contre C vaut ici aussi) ; rapporté avec son intervalle, jamais décisif seul.

**E5′ — Vide ou non (remplace mon critère additif).** Sujet synthétique = B_j + décalage **d'espérance** +ε sur les deux classes (ε = 0,9 δ), r_B ∈ {0,1 ; 0,3 ; 0,6} (illustratif), 160 et 400 unités, k = 3. H_A : à δ = 0,10, la fiche est promue dans ≥ 0,5 des suites pour au moins un r_B. H_B : < 0,5 partout. Contrôle : même sujet sans garde (promu, sinon le décalage est mal codé) ; à espérance tenue (promotion ≤ 1/seuil, Ville). H_A ⇒ δ = 0,10 laisse promouvoir un artefact pur : « vide » au sens de la question ; H_B ⇒ ma recommandation perd son second appui et δ = 0,10 (D-S v3) redevient recevable sur la puissance seule.

**E6 — Lot honnête séparé : identité de loi et stabilité.** (a) Tirage scellé par graine des consignes « mixtes » et « honnêtes seules » dans une même fabrique ; H_A : |ḡ_mixte − ḡ_seule| ≤ 2 SE pour tout j ; H_B : dépasse. H_A fausse ⇒ les honnêtes seules ne nourrissent pas la garde de G1 (scénario 1 de C tenu). (b) Stabilité (CN-C2) : n₈₀ recalculé sur vingt moitiés de tâches tirées par graine ; H_A : dans un facteur 1,25 ; H_B : hors. H_A fausse ⇒ le fichier réel ne dimensionne pas n_h, le scellement prend la borne haute de la grille.

**E7 — Placebo d'étiquettes (limité par P-9).** Avant G1 : permutation honnête/saboté dans chaque unité, comparateurs B_j seuls ; H_A : promotion ≤ 1/seuil ; H_B : au-delà ⇒ fuite étiquette–score dans la fabrique, invisible à la garde. Sur A : rapporté à la lecture de G1, jamais une condition.

**E8 — Structure de G1 : une fiche IU ou m fiches e-BH (issue de A-4).** Mêmes lois, mêmes k, modes = 2 (illustratif) ; (i) une fiche, minimum sur tous les processus, seuil 20 ; (ii) m fiches, e-BH sur la valeur finale (jamais simulée, pièce C v3 GD3-07). H_A : (i) ≥ (ii) + 0,10 en puissance à 160 unités ; H_B : non. L'issue dit laquelle écrire ; la retenue e-BH simulée ferme en même temps la réserve GD3-07.

E3 (domination F2) devient un contrôle d'implémentation ; E5 est retirée.

**Conception corrigée, en bref.** Forme F1 (k gardes dans le minimum), phrase scellable limitée aux faux positifs relatifs. δ = 0,05 identique pour tous les comparateurs et les deux modes, δ_max = 0,10 déclaré « lâche » dans la branche ; δ ne dépend d'aucune mesure. n_h dimensionné à biais a priori {0 ; δ/4}, jamais au point estimé. Structure de G1 (m_c) écrite et simulée (E8). Unités : jamais le calibrage ; honnêtes seules seulement si E3′ et E6-a passent, par tirage scellé. Règle d'arrêt inchangée : garde non certifiée = G1 non promue, processus bloquant nommé, aucune relecture ; nœud seulement avant scellement.

---

## (c) Réponse à l'arbitre

**Ce qui est établi (VÉRIFIÉ, pièce A et E).** La garde n'a pas de seuil propre ; elle entre dans le minimum avec les contrastes, au seuil m_c/α_c, m_c = taille de la famille. Le niveau du minimum tient par domination sous chaque nul, même quand garde et contrastes lisent des unités distinctes ; ce qui n'est pas garanti est l'espérance de l'e-valeur arrêtée (K7-6, écrit par le code). δ est dans la clé de l'héritage : un autre δ est une autre fiche, à budget et unités neufs — la porte de sortie après lecture est déjà fermée par le code. τ de G1 = 0,01 (D-S5). Δ_j de `seuil` vaut (j − 1)/n pour toute cellule hors ex æquo : il ne mesure aucun biais. Les planchers à écarts nuls : 93/144 (δ = 0,05), 48/74 (δ = 0,10).

**Ce qui est RAPPORTÉ et conditionnel.** Sous lois synthétiques, sujet partagé, biais 0, seuil 160, k = 3 : garde-min 0,78 à 160 unités et 1,00 à 400 (K_h = 10, τ = 0,01) ; 0,48 à K_h = 3 ; un biais 0,0125 laisse 0,96 à 250 unités à τ = 0,01 (erratum) mais 0,03 à τ = 0,10. À 64 unités, la fiche ne passe pas (≤ 0,011). Aucun chiffre n'existe à k > 3 ni pour une fiche IU unique.

**Ce qui n'est pas établi.** Mes trois instruments d'origine (E1 sur le jumeau, Δ_j, E3) étaient vrais par construction ou tautologiques : B et C l'ont montré, je les retire. L'échangeabilité calibrage–épreuve est une HYPOTHÈSE : si A et B_j réagissent différemment au changement de tâches, E[g] ≠ 0 sans faute de calibrage, et c'est précisément ce que la garde doit voir — donc rien de ce qui se mesure sur le calibrage ou sur A contre lui-même ne peut dimensionner la garde. Le lot honnête séparé (point 3) tient au niveau, mais reste suspendu à E3′ (e-BH sous dépendance) et E6 (tirage scellé, identité de loi) ; sans eux, le scénario de dilution de C est ouvert. La vacuité de δ = 0,10 reposait sur un modèle d'artefact non marqué : elle est maintenant un test (E5′), pas un acquis. Le fichier réel viendra du pilote : à seize tâches, l'erreur type de ḡ est de l'ordre de 0,01 (illustratif, B et C concordent) — il ne peut pas fixer un biais, seulement une dispersion grossière et une sentinelle ; d'où la grille a priori {0 ; δ/4} et la borne haute si E6-b échoue.

**Ce qui est maintenu.** F1 ; δ = 0,05, un seul δ, fixé par le sens (six fois τ) et non par une mesure ; biais dans n_h et jamais dans δ ; règle d'arrêt unique « non promue, processus bloquant nommé » ; nœud avant scellement seulement. Divergence attendue avec C (δ réglé sur le biais observé : fuite, B et moi concordons) ; convergence partielle avec B sur la forme.

**Expérience à faire en premier : E8**, sur processeur, sans donnée réelle. Tant que la structure de G1 (une fiche IU à seuil 20, ou m fiches e-BH à seuil 160) n'est ni écrite ni simulée, tous les chiffres de puissance des pièces sont deux bornes qui diffèrent d'un facteur dépassant 0,25 à 160 unités (0,74 contre 1,00, pièce C v3 § 7), et aucune décision sur δ ni sur n_h ne peut être prise. E8 ferme en même temps la retenue e-BH jamais simulée (GD3-07). Ensuite, dans l'ordre : E3′ (validité sous n_h ≫ n, décide si des unités honnêtes seules peuvent exister), E5′ (sens de δ), puis, après le pilote, E2′ et E1′ sur le fichier réel.

**Ce que cette cellule ne peut pas affirmer.** Le texte de D-S10 et la liste exacte des comparateurs de G1 (k) ; K_h des jumeaux d'épreuve ; l'effectif d'unités du pilote ; le script v4 lui-même (non servi) ; le résultat d'aucune des expériences ci-dessus.

FIN-DE-CELLULE