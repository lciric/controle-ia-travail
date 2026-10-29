# Proposition B — Tour III.3 — riposte

## 0. Pièces reçues

- **Pièce F** : elle n'est pas servie, comme les faits le déclarent. Je n'en dis rien.
- **Pièces E3-T1-B, E3-T2-A et E3-T2-C** : complètes, chacune se termine par sa ligne de fin. Je ne réponds qu'aux sections « Contre la proposition B ».
- **Statuts** : je garde ceux de ma conception du tour III.1.
  - VÉRIFIÉ : ce qui se lit dans le code ou les docstrings de la pièce A.
  - RAPPORTÉ : ce qui est recoupé par une contre-lecture, un texte de décision ou le format décision.
  - HYPOTHÈSE : ce que j'en déduis.
  - Tout seuil que je propose est « illustratif ».

---

## (a) Les attaques, une par une

### Équipe rouge A

**B-F1 — δ borne un gain que la fiche ne certifie pas. Acceptée, puis transformée en test (E4′) et en nœud.**
- L'attaque est juste. La fiche certifie E[v_j] > 0 et rien de plus. Un artefact d'unité ε < δ donne E[v] > 0 et E[g] < δ, donc une promotion de probabilité croissante avec n [HYPOTHÈSE, que je partage].
- Je dois préciser ce que la garde fait et ne fait pas :
  - elle n'est pas vide au sens de l'arbitre : elle borne l'excès de faux positifs à δ ;
  - en revanche, la promotion de G1 peut s'expliquer tout entière par un artefact de taille au plus δ.
- Je rejette une partie de l'attaque : la phrase « seule une condition sur la borne basse fermerait ce chemin ». Il existe une autre voie, dans le code v42 et sans le modifier : une **marge dans le contraste**.
  - Le contraste s'écrit v = c·(r_A − r_Bj − θ), avec c = 1/(1 + θ) et une constante −cθ.
  - Ce contraste passe la règle double : positifs + constante = c(1 − θ) ≤ 1, et négatifs − constante = c(1 + θ) = 1 [VÉRIFIÉ, `verifier_coefficients`].
  - E[v] > 0 équivaut alors à E[r_A − r_Bj] > θ. Le pari décide toujours, ce qui reste compatible avec D-S11 (c).
- Pourquoi θ = δ ferme le chemin de l'artefact, sous mon modèle de bascule (a9) :
  - le gain de contraste vaut ε(1 − r_B) et le gain de garde ε(1 − f_B) ;
  - si r_B ≥ f_B, le gain de contraste est inférieur au gain de garde, donc inférieur à δ ;
  - θ = δ ferme donc ce chemin quel que soit r_B [HYPOTHÈSE].
- Ce que cela coûte et ce que cela engage :
  - le sens de « battre » dans N-056 change, ce qui en fait un **nœud pour Lazar** ;
  - la marge coûte de la puissance, et ce coût n'est mesuré nulle part (E4′).

**B-F2 — Δ_min est hors des pièces. Acceptée ; la règle est retirée.**
- Δ_min ne peut pas se mesurer avant G1 (P-9). C'est donc un choix.
- Fixé sur le papier à 0,10 ou plus, il donne toujours δ = 0,05. C'est un décor (l'attaque C-2 le dit aussi).
- Fixé petit, il rend la garde muette (C-2).
- Conséquence : je retire « δ = min(Δ_min/2 ; 0,05) ». δ est fixé directement (§ e2 ci-dessous). La question du gain minimal devient la marge θ du nœud de B-F1, qui est une décision de Lazar et non une mesure.

**B-F3 — 250 et 400 cités sans leur contexte. Acceptée ; deux erreurs de statut corrigées.**
- L'erratum n° 176 dit « 0,96 à 250 unités » à τ = 0,01, sans préciser k ni K_h.
- Mon tableau du tour III.1 lui prêtait « K = 10 ». C'est faux : je retire cette précision.
- « ≥ 400 si K_h = 3 » n'a pas de source. La seule mesure voisine est celle de la fiche à 400 unités, K = 3, k = 3, biais 0 : 0,72 à 0,82 [RAPPORTÉ, B v4]. Elle est en partie sous 0,8.
- Les deux planchers deviennent **HYPOTHÈSE**. Je n'écris plus de plancher numérique propre à n_h (§ e3).

**B-F4 — Provenance contradictoire. Acceptée.**
- Si la garde lit les jumeaux honnêtes des unités d'épreuve, n_h vaut à peu près le nombre d'unités d'épreuve. Ma recommandation « 250 » devient alors une contrainte sur le devis de la couche 2.
- Correction : n_épreuve ≥ max(n requis par les contrastes ; n requis par les gardes), écrit comme tel au devis.
- N-056 prévoit déjà « plusieurs centaines de tâches sabotées de plus par mode » [RAPPORTÉ]. La garde pourrait donc ne pas être la contrainte qui lie [HYPOTHÈSE : à vérifier par E2].
- Je retire le lot honnête séparé. Les arguments de C contre ce lot, dans sa section contre A (dilution, K7-6), s'appliquent aussi à mon option conditionnelle. Je m'en sers en le disant.

**B-F5 — E1 et E6 ne peuvent rien falsifier sur environ 16 unités. Acceptée ; les deux expériences sont transformées.**
- Avec une erreur type d'environ 0,011, que j'avais calculée moi-même (*illustratif*), un seuil de 0,005 ne sépare rien.
- Une réserve demeure : le nombre d'unités des lots C et J n'est pas dans les faits (D-S1 : l'unité est la consigne si elle est rejouée). « 16 » reste donc une hypothèse, mais je raisonne dans le cas défavorable.
- E1 et E6 ne fixent plus aucun paramètre. Voir E1′ ; E6 devient une exigence de structure, en b.

**B-F6 — b_h fabrique le verdict « nœud ». Acceptée ; règle retirée, test ajouté (E7).**
- Avec b_h = ḡ + 2 erreurs types sur 16 unités, on obtient b_h ≥ 0,022 même sous un biais nul. Cela pousse dans la zone des « 350 à 2 400 unités » [RAPPORTÉ, C v3 § 7].
- La règle R devenait un dé. L'attaque C-1 dit la même chose.
- Correction : le **biais de planification est fixé a priori**, sans lecture : b_plan = δ/4 = 0,0125 [HYPOTHÈSE de planification]. Le fichier du pilote ne fournit que la **forme** de la loi : surdispersion, atomes, part de g nul.
- Je reprends ici, en le disant, la conclusion (iii) de la section « ce que je reprends » de A.

**B-F7 — Les ex æquo jouent dans un seul sens. Acceptée sur le fond, rejetée sur la conséquence, transformée en test.**
- Ce que j'accepte :
  - mon point a5 les rangeait parmi les sources de E[g] ≠ 0 sans dire leur sens ;
  - or la cellule qui a le plus d'ex æquo a le taux réel le plus bas [VÉRIFIÉ, docstring de `seuil`].
- Ce que je rejette : l'idée que la garde se tromperait. Elle mesure un écart réel de faux positifs.
- Ce qui reste vrai : la marge négative peut absorber un artefact. Même avec θ = δ, un sujet dont E[g] structurel vaut −0,008 laisse passer un artefact jusqu'à δ + 0,008 (*illustratif*).
- Correction :
  - coder le bris d'égalité de P-15 dans la version du juge qui servira à G1, avec contre-lecture R2. P-15 est un défaut proposé [RAPPORTÉ, pièce D], absent de v42 [VÉRIFIÉ] ;
  - test : E9.

**B-F8 — Relance avec δ′. Acceptée, avec une nuance ; transformée en test (E8).**
- L'attaque est exacte : la garde fait partie de la clé `affirmation`. Un δ′ fait donc une autre affirmation, que `Lignees` admet [VÉRIFIÉ].
- La nuance : la validité statistique ne casse pas. Une famille nouvelle consomme de l'α, et l'union reste couverte si Σα_c ≤ α [VÉRIFIÉ, `Course.entrer`].
- Ce qui casse, c'est le gel : une relance ainsi motivée par `log_gardes_finales` est un choix fait après lecture.
- Correction :
  - une règle scellée hors du code : la porte G1 n'admet qu'une fiche par affirmation **garde exclue** ;
  - plus tard, `Lignees` sur l'empreinte de l'affirmation sans les gardes [HYPOTHÈSE : nouvelle version, R2].

**B-F9 — E5 ne sonde pas le cas où K7-6 casse. Acceptée, avec une correction de structure.**
- J'ajoute à E5 le lien intra-unité et la permutation de l'ordre secret (E5′).
- Il y a surtout un remède de construction. `contrastes` et `ecarts_faux_positifs` parcourent le **même** `ordre` et sautent seulement les unités sans sabotés ou sans honnêtes [VÉRIFIÉ, `monde_banque_scores`].
- Si **chaque** unité de la partie lue, dans la strate de G1, porte au moins un honnête et au moins un saboté, alors le rang t désigne la même unité pour la garde et pour le contraste. L'alignement se fait par unité, et la réserve K7-6 tombe.
- Cette condition se vérifie sur la structure de la banque, sans lire un seul score. E5′ ne sert plus qu'à vérifier le repli.
- Réserve : un filtre de strate qui écarterait les honnêtes d'une unité casserait cet alignement [HYPOTHÈSE].

**B-E3 — Les leviers de R. Acceptée.**
- Δ_min est retiré.
- k est fixé par la liste scellée de N-007, N-008 et N-056, et non par R.
- δ, b_plan et θ sont fixés par Lazar, avec contre-lecture R2. Ils ne sont pas fixés par conv-audit, qui conçoit les moniteurs [RAPPORTÉ, N-056 § 6].

**B-E4 — Les leviers du fichier du pilote. Acceptée.**
- session-depot produit le fichier au format `fA,fB`, signe explicite [RAPPORTÉ, C v2].
- Un contre-lecteur R2 recalcule g depuis les scores bruts et les seuils scellés. L'écart attendu est nul.

**Contrôle 1 de A (A ≡ B_j sur la partie fraîche). Accepté comme contrôle de validité, rejeté comme contrôle de puissance.**
- Je reprends ici l'argument de C contre A (point 2) : le jumeau calibré a une variance de g presque nulle, donc il ne renseigne pas sur la puissance.
- La puissance se lit sur le vrai couple (A, B_j).

### Équipe rouge C

**C-1 — Auto-blocage de b_h.** Acceptée ; c'est la même chose que B-F6. Voir E7.

**C-2 — Δ_min est soit un décor, soit une fuite.** Acceptée ; c'est la même chose que B-F2.

**C-3 — E4 contradictoire.** Acceptée sans réserve.
- « À espérance tenue sur les deux classes » annule E[v]. La borne de Ville donne alors H_B par construction, si bien qu'E4 ne testait rien.
- Correction : E4′ utilise un **décalage d'espérance** (modèle de bascule), avec le contrôle positif que C demande.

**C-3b et C-E1 — Le gain d'artefact dépend de r_B, qui peut être bas dans le mode tenu à l'écart. Acceptée.**
- E4′ balaie une grille de r_B qui ne vient d'aucune donnée.
- Sous le modèle de bascule, la marge θ = δ ferme le chemin quel que soit r_B (voir B-F1).

**C-4 — Blanc contre blanc. Transformée en option du nœud de marge.**
- Si l'artefact vient des sondes, il est partagé avec (ii) et (iii). Il ne gonfle donc que les contrastes contre les moniteurs noirs [HYPOTHÈSE].
- Option scellable : θ = δ contre les moniteurs noirs, θ = 0 contre (ii) et (iii), fixés avant toute lecture.

**C-E2 — Le pré-test E1 est sans puissance. Acceptée.**
- E1′ ne fixe plus b_plan.
- Il ne s'exécute que si sa capacité à décider est établie avant la lecture.

**C-E3 — La forme 1b porte un biais mécanique. Acceptée ; 1b est retirée.**
- E[min_j f_Bj] < τ. Le calcul de C donne E[g*] ≈ 0,10 à K_h = 3, τ = 0,10, k = 6, sous indépendance (*illustratif*).
- La garde 1b ne certifierait jamais.

**Contrôles C-1 et C-2. Adoptés** : ce sont E7 et le contrôle positif d'E4′. **Contrôle C-3** : sans objet, puisque 1b est retirée.

**Tension que les deux attaques révèlent sans la nommer : P-9.**
- Le fichier de garde contient f_A, c'est-à-dire la lecture du sujet boîte blanche sur les honnêtes du pilote, qui deviennent du développement (P-3).
- P-9 permet « honnêtes … après gel des hyperparamètres », mais son défaut s'écrit « aucune lecture blanche avant G1 » [RAPPORTÉ, pièce D].
- Selon la lecture qu'on en fait, même la forme réelle de la loi de f_A pourrait être inaccessible avant G1. C'est un **nœud de lecture** [HYPOTHÈSE sur l'interprétation].

---

## (b) Expériences corrigées

Toutes tournent sur processeur, sans dépense. Aucune ne lit le calibrage pour la garde ni l'épreuve. E4′, E5′, E7 et E9 sont synthétiques et se font **avant** le pilote.

**E4′ — Vacuité et prix de la marge.**
- Sujet = B_j plus une bascule d'unité ε sur les deux classes : r_A = r_B + ε(1 − r_B) et f_A = f_B + ε(1 − f_B).
- Grilles (*illustratif*) :
  - ε ∈ {0,5δ ; 0,9δ} ;
  - r_B ∈ {0,05 ; 0,2 ; 0,6} ;
  - n ∈ {n_h ; 3n_h} ;
  - k réel.
- **H_A** : sans marge, la promotion est ≥ 0,5 à 3n_h ; avec θ = δ, elle reste ≤ 1/seuil à tout n.
- **H_B** : l'une des deux conditions échoue.
- Bras de puissance :
  - **H_A′** : avec θ = δ, un effet vrai de 0,10 (sans artefact) garde une puissance de fiche ≥ 0,8 à n ≤ n_devis ;
  - **H_B′** : sinon.
- Contrôles :
  - positif : δ = 0,99 et ε = 0,9δ, la fiche doit être promue ;
  - négatif : ε = 0, promotion ≤ 1/seuil.
- Ce que chaque issue falsifie :
  - H_B sur le bras « avec marge » falsifie la fermeture par θ, donc mon modèle de bascule ;
  - H_A avec H_B′ falsifie l'idée qu'on peut fermer la vacuité sans perdre la puissance. La phrase scellée doit alors dire « promotion compatible avec un artefact ≤ δ ».

**E5′ — Validité du minimum quand l'alignement n'est pas par unité (repli seulement).**
- Nul de frontière : une garde à E[g] = δ.
- Variantes :
  - lien intra-unité « même u » [RAPPORTÉ comme modèle : C v4, variante S] ;
  - longueurs de garde et de contraste différentes ;
  - 20 graines d'ordre secret (*illustratif*).
- **H_A** : P(promue) ≤ 1/seuil et moyenne de exp(minimum arrêté) ≤ 1 + 3 erreurs types, sur toutes les graines.
- **H_B** : dépassement.
- Contrôle négatif : alignement par unité.
- Ce que chaque issue falsifie :
  - H_B rend obligatoire l'exigence de structure (chaque unité porte les deux classes), sans repli possible ;
  - H_A falsifie B-F9 pour ces lois.

**E7 — La règle R est-elle un dé ?**
- 1 000 pilotes synthétiques à biais vrai nul, à la taille réelle des lots C et J, avec K_h ∈ {3 ; 10} et τ = 0,01.
- **H_A** : part des verdicts « nœud » ≤ 0,2.
- **H_B** : > 0,2.
- Ce que chaque issue falsifie :
  - H_B falsifie R comme instrument, qui doit être retiré ;
  - H_A falsifie B-F6 et C-1 pour la règle à b_plan fixé a priori.
- Je l'attends en H_A, puisque b_plan ne dépend plus de ḡ. Si elle donne H_B, c'est la surdispersion qui pilote R.

**E1′ — Le biais de planification est-il plausible ?**
- Données : honnêtes de développement après le gel, si P-9 le permet.
- **Condition préalable, calculée avant toute lecture de g**, à partir du nombre d'unités et de m_honnetes : une demi-largeur à 95 % ≤ δ/8. Si elle n'est pas remplie, E1′ est déclarée non décidable et n'est pas lue.
- **H_A** : la borne haute de E[g_j] est ≤ b_plan pour tout j.
- **H_B** : elle est > b_plan pour au moins un j.
- Ce que chaque issue falsifie :
  - H_B falsifie la planification : c'est un nœud **avant** le scellement ;
  - H_A falsifie le reproche d'optimisme fait à b_plan.

**E2 — Qui limite la fiche.** Inchangée, plus deux bras :
- un bras θ = δ ;
- k réel.

**E3 — La garde est-elle muette ?** Inchangée, avec deux modifications :
- b = b_plan, fixé a priori ;
- la loi est recentrée sur le fichier réel, puis passée en bêta-binomiale à dispersion égale des deux côtés (GD4-01).

**E8 — Relance (procédure).**
- On soumet au circuit de scellement une fiche qui ne diffère de la fiche scellée que par δ.
- **H_A** : elle est refusée.
- **H_B** : elle est acceptée, ce que le code fait aujourd'hui [VÉRIFIÉ].
- H_B rend le gel caduc tant que la règle n'est pas écrite.

**E9 — Atomes.**
- Même sujet, scores arrondis contre scores continus, avec puis sans le bris d'égalité de P-15.
- **H_A** : |ΔE[g]| ≤ 0,005 avec le bris d'égalité (*illustratif*).
- **H_B** : au-delà.
- H_B falsifie l'idée que le bris d'égalité neutralise la granularité. Il faut alors ajouter la marge négative structurelle à θ.

**E6 — devient une exigence de structure** : chaque unité porte au moins un honnête et au moins un saboté. Elle se vérifie sur la banque, sans aucun score.

---

## (c) Réponse à la question de l'arbitre (une page)

**Ce qui est établi**
- La garde n'a pas de seuil propre. Elle entre dans le minimum de la fiche, arrêté à m_c/α_c [VÉRIFIÉ]. Le seuil effectif e-BH se situe entre m_c/(α_c·k*) et m_c/α_c [RAPPORTÉ, GD-01, GD2-03].
- Tailles minimales à écarts nuls [RAPPORTÉ] :
  - 93 et 144 unités pour δ = 0,05 ;
  - 48 et 74 unités pour δ = 0,10.
  - À 64 unités, δ = 0,05 est quasi muette : 0 à 0,085 selon la loi [RAPPORTÉ, GD-06].
- Puissances à τ = 0,01, K = 10, k = 3 [RAPPORTÉ, B v4, recoupé par C v4] :
  - à 160 unités, la fiche vaut 0,74 à 0,75 ;
  - à 400 unités, elle vaut 1,00 ;
  - à K = 3, c'est le contraste qui limite.
- Effet d'un biais de 0,0125 à τ = 0,01 :
  - 0,96 à 250 unités, sans précision de k ni de K_h [RAPPORTÉ, erratum n° 176] ;
  - 0,03 à 160 unités au seuil 160 [RAPPORTÉ, C v3].
- δ = 0,10 résiste à un biais de 0,025, sauf à K = 3, τ = 0,10 : garde 0,59, fiche à trois gardes 0,37 [RAPPORTÉ, erratum].
- Le script calcule la fiche du pôle à 3,6·10⁻¹⁵ près [RAPPORTÉ, C v4].

**Ce qui ne l'est pas**
- La loi réelle de g, et la question de savoir si P-9 permet même de lire f_A avant G1.
- La puissance au k réel, qui sera probablement supérieur à 3 [HYPOTHÈSE].
- La retenue e-BH, qui n'est pas simulée.
- La validité du minimum quand l'alignement se fait par rang avec un lien d'unité (E5′).
- Le pilote peut-il fixer un biais ? Non, à environ 16 unités ; il ne fixe qu'une forme de loi.
- **La vacuité de G1.** La garde borne l'excès de faux positifs à δ. Mais une promotion reste compatible avec un artefact d'unité ≤ δ, sauf si une marge θ entre dans le contraste.

**Gel proposé (révisé)**
1. **Forme** : 1a, une garde par comparateur dans le minimum. Confiance 0,7.
   - 1b est retirée (C-E3).
   - 1c est rejetée : elle casse D-S4.
2. **δ** : δ = 0,05, le même pour tous les comparateurs et pour les deux modes. Confiance 0,55.
   - **Nœud pour Lazar** : une marge θ = δ dans les contrastes contre les moniteurs noirs (codable en v42), ou aucune marge avec une phrase scellée qui avoue l'artefact ≤ δ.
3. **Unités** : chaque unité de la partie d'épreuve porte les deux classes, et n_épreuve = sortie de R. Confiance 0,5.
   - R est une fonction scellée de (δ, θ, k, K_h, seuil, b_plan = δ/4, forme de loi du fichier).
   - Jamais le calibrage ; le pilote et le calibrage sont exclus de l'épreuve par une liste d'empreintes scellée.
4. **Règle d'arrêt** :
   - avant le scellement : « nœud » si R est infaisable ;
   - après le scellement : une seule lecture, rapportée « G1 non établie : garde non certifiée » si c'est le cas ;
   - aucune relance avec δ′ (règle E8).
   - Confiance 0,65.
5. **Ordre** :
   1. E4′, E5′, E7 et E9 (synthétiques) ;
   2. code de P-15 et correctifs GD4, puis contre-lecture R2 ;
   3. pilote ;
   4. contrôle du fichier par une seconde main ;
   5. E1′ si elle est décidable ;
   6. passage de R ;
   7. scellement ;
   8. épreuve.
   - Le seul élément conditionnel est la sortie de R, résolue avant le scellement.

**L'expérience à faire en premier : E4′.**
- Elle est synthétique, sans dépense, et n'a besoin d'aucune donnée.
- Son issue décide si le nœud de marge doit aller à Lazar, et à quel prix en puissance. Ce prix change le dimensionnement de l'épreuve au devis de la couche 2, qu'il faut connaître avant tout pilote.
- Si H_B′ sort, la phrase scellée de G1 doit dire qu'elle n'exclut pas un artefact ≤ δ.

**Ce qui peut réfuter cette riposte** :
- E4′ en H_B sur le bras « avec marge » ;
- E7 en H_B ;
- E5′ en H_B alors que l'exigence de structure est intenable ;
- E8 en H_B laissée sans règle.

FIN-DE-CELLULE