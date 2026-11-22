# Proposition B — Tour III.3 : réponse aux critiques

**État des pièces.** J'ai lu le texte servi en entier. Toutes les pièces sont présentes et closes par leur ligne de fin : FAITS, QUESTION DE L'ARBITRE, ma conception III.1, et les critiques A, C, D, E et F. Je n'ai pas recalculé les empreintes. FAITS reprend la question mot pour mot et ne transmet aucun fait à statut.

**Statuts.** Ce que je reprends d'une critique garde le statut qu'elle lui donne, et je le signale (« VÉRIFIÉ selon E »). Mes arguments et mes corrections sont des HYPOTHÈSES. RAPPORTÉ renvoie aux références R1–R24 de ma pièce III.1, citées de mémoire. Je n'ai examiné aucune donnée : rien n'est VÉRIFIÉ ni OBSERVÉ-NON-AUDITÉ de mon fait. Tout nombre est illustratif, sauf les identifiants et les années.

**Périmètre.** Je ne réponds qu'aux sections « Sur la proposition B ». Quand j'emprunte un contrôle qu'un critique adresse à une autre proposition, je le dis.

**Règle de décision commune (celle de D, que je reprends).**
- La marge m est fixée avant les données. H_A : chaque verrou dépasse sa marge. H_B : au moins un verrou reste sous sa marge.
- Un intervalle simultané situé entièrement d'un côté falsifie l'hypothèse adverse. Un intervalle à cheval ne falsifie rien et s'écrit « non jugeable ».
- Les effectifs sont fixés par simulation, pour que cette issue ait une probabilité ≤ 0,2 [illustratif]. Une absence de significativité ne vaut pas équivalence.
- Unité statistique : le réseau (graine), le document ou le sujet. Jamais le site, la fenêtre ou le voxel.

## (a) Verdicts

Notation : [X-a2] désigne le point 2 de la section (a) de la critique de X. Sans numéro, la section n'en a pas.

### E1 (PCI_art)

| Réf. | Critique | Verdict | Suite |
|---|---|---|---|
| C-a1, D-a, E-a1, F-a1 | Le seuil tiré d'écarts entre contextes mesure la variance entre entrées, et il varie avec la sensibilité lexicale de chaque réseau | Acceptée | Seuil supprimé ; binarisation à densité globale fixe (E1′) |
| C-c1, 1ʳᵉ moitié | Seuiller contre un bruit interne de norme fixe, ou contre δ′ → 0 | Rejetée | En régime linéaire, ce seuil ne mesure que le rapport de normes choisi par l'expérimentateur. C'est l'argument que A, E et F opposent à C ; je le reprends |
| C-c1, 2ᵉ moitié ; C-a1, F-a1, F-c | Base ACP : fuite si elle est ajustée sur le modèle entraîné, ordre des axes variable sinon | Acceptée | Base orthogonale aléatoire gelée, commune à tous les réseaux. La dispersion entre 10 bases [illustratif] doit rester inférieure à l'écart entre classes, sinon E1′ est suspendue |
| A-b, D-b, F-b | c/H(p) est instable quand p tend vers 0 ou 1 ; une AUC brute peut ne lire que p | Acceptée | p fixé, donc H(p) constant |
| C-a1, D-a, D-c, E-a1, F-a1, F-c | T3 est dégénéré : ≈ 0 si le bruit est gelé, ≈ 1 s'il est retiré | Acceptée | T3 n'est plus un témoin. Il devient un contrôle du code, avec ses deux valeurs écrites d'avance |
| A-a3 | L'appariement en gain (H_A) et la régression sur le gain (H_B) ne se lisent pas sur le même jeu | Acceptée | Régression supprimée |
| C-b1 ; E-a2, E-b1 | C : la non-linéarité gonfle l'AUC résiduelle sous le nul. E : la colinéarité de groupe la ramène vers 0,5 | Acceptées toutes deux | Les deux biais ont des signes opposés : le signe de l'erreur est inconnu et le critère tombe. Il est remplacé par un gain d'AUC non linéaire, validé réseau par réseau (F-c) |
| A-b | Un seul réseau entraîné : n₊ = 1 | Acceptée | Cohorte de graines |
| A-a4 ; F-a1 (L1) | A : en contexte neutre, L1 se confond avec le modèle intact. F : L1 coupe par construction la propagation vers t > t₀ | A : transformée en test. F : rejetée dans sa forme forte, car d'autres têtes relient les positions et A prédit l'inverse ; transformée en test | Contextes neutres et contextes répétitifs. Si ΔPCI(L1) ≈ 0 en contexte neutre, A a raison. Si ΔPCI(L1) varie comme la masse d'attention inter-positions retirée, F a raison |
| A-a4 | L2 obtenue par rejet est une queue de distribution | Acceptée | L1 est situé dans la loi de 1 000 [illustratif] ablations aléatoires voisines en Δperte et en masse retirée |
| F-a1 | Le contrôle sur EEG ne valide que le compresseur | Acceptée | Contrôles de la chaîne ajoutés (E1′) |
| F-b | Il existe des zones où rien n'est réfuté | Acceptée | Règle de décision commune |

### E2 (local/global)

| Réf. | Critique | Verdict | Suite |
|---|---|---|---|
| A-a1 | Un seul type de bloc : le niveau et l'identité du dernier symbole sont confondus | Acceptée | Plan croisé à deux types de blocs (celui de D, signalé par A) |
| A-a1 | Un modèle qui apprend en contexte attend y : E_loc peut être nul | Transformée en test | Précondition p1. Si elle échoue, la non-transposition est rapportée comme un résultat |
| A-b, A-c, F-a2, F-c | Apparier sur la mesure elle-même crée une régression vers la moyenne, (1 − f)(μ_loc − μ_glob) | Acceptée | Items choisis sur une moitié, mesurés sur l'autre |
| E-a3 | Des AUC égales ne font pas des surprises égales (saturation) | Acceptée | Échelle primaire en nats, d′ en secondaire |
| C-a2, D-b, E-a3, E-b2, F-a2, F-b | L'abscisse « hausse de perplexité » dépend du corpus, des supports et de la borne d'intégration | Acceptée | Aire S abandonnée, remplacée par une signature angulaire sans abscisse |
| D-a, D-b, F-a2, F-b | Avec un échantillon par mot, le rythme du mot se replie en fréquence nulle | Acceptée | Le couple mot/phrase n'est plus un couple local/global |
| A-a2, A-c, C-a2, C-c2, D-b, D-c, F-a2, F-c | La périodicité des catégories lexicales crée le pic « phrase » dès les plongements statiques (Frank & Yang, 2018, référence à vérifier selon A) | Transformée en test | Précondition p2 |
| E-a3, E-b2, E-c1, F-a2 | Découpage en sous-tokens, ponctuation, gigue de durée | Acceptée | Mots d'un seul sous-token, sans ponctuation |
| C-b2 | Un seul périodogramme : 2 degrés de liberté au numérateur | Acceptée | Moyennage de Welch avant le calcul du rapport |
| F-b | Quantile 99 % estimé sur 200 tirages | Acceptée | 1 000 tirages, quantile 95 % [illustratif] |
| D-c | Le choix de la meilleure famille doit être refait dans le nul | Acceptée | Maximum sur les familles recalculé à chaque tirage nul |

### E3 (régime spontané)

| Réf. | Critique | Verdict | Suite |
|---|---|---|---|
| A-a5, A-b, D-a, D-b, E-a4, E-b3 | h_t est une fonction de l'entrée (VÉRIFIÉ selon E) : H_B est vraie par construction, et le gain ne mesure que la pauvreté des descripteurs | Acceptée | Duel reformulé : le régime appartient-il au modèle, au texte, ou à toute dégradation ? |
| E-c2 | Prendre comme comparateur un classifieur non linéaire entraîné sur x₁:t | Rejetée comme comparateur qui tranche ; gardée comme descriptif | D'après E-b3, ce classifieur atteint la borne dès que sa capacité suffit : l'issue serait écrite d'avance, contre B4. Le comparateur retenu est un autre réseau qui lit le même texte (A-c) |
| F-a3, F-c | Les descripteurs d'entrée sont incomplets | Acceptée en partie | Entropie de sortie, perplexité locale et distracteurs ajoutés. Ils ne tranchent pas (E-b3) |
| A-a5, A-c | La sonde peut ne lire que la norme | Transformée en test | Activations normalisées ; une sonde réduite à la norme sert de comparateur |
| C-a3, E-a4, F-a3 | Contextes plus longs que l'entraînement : dérive positionnelle, impossible sur GPT-2 small | Acceptée | Source supprimée |
| C-b3, F-b | Boucles à durée de séjour à queue lourde, autocorrélation | Acceptée | Bootstrap par document |
| F-b | Décalage de loi : le taux de fausses alertes n'est plus garanti | Acceptée | Seuil calibré sur du texte naturel tenu à part, de même source |
| D-b, D-c | Positions sans référent annotable ; permutation des référents | Acceptée | Positions annotables seulement ; permutation à contexte local fixé, source par source |

### E4 (modèle de langage comme instrument sur le cerveau)

| Réf. | Critique | Verdict | Suite |
|---|---|---|---|
| A-b, D-a, D-b, F-a4, F-b | Sous une atténuation commune, C_X = (1 − κ)·ΔR²_éveil,X : l'ordre des C reproduit celui de l'éveil (R16), et le signe de C ne dit rien de la sédation | Acceptée | C abandonné ; test direct dans l'état de sédation (F-c) |
| C-a4, C-b4, E-a5, E-b4, F-a4, F-b | Normaliser par le plafond de bruit propre à la sédation donne un rapport à queues lourdes | Acceptée | Plus de normalisation par ce plafond |
| D-b | Le n-gramme sert à la fois de base et de comparateur : gain nul par construction | Acceptée | Bases emboîtées, un seul rôle par trait |
| F-a4, F-c | Une pénalité ridge commune fait fuir la variance | Acceptée | Ridge par blocs |
| A-c, D-c, E-c3, F-c | Dégrader l'éveil au niveau de la sédation, ou simuler un gain égal avec des fiabilités différentes | Acceptée | Pseudo-sédation, validée en simulation |
| A-b | Non jugeable si l'intervalle du plafond de bruit en sédation contient 0 | Acceptée | Précondition déclarée |

## (b) Expériences corrigées

Ce que je ne répète pas reste celui de III.1 : le matériel et la portée pour les deux lecteurs, sauf mention contraire.

### E1′ — Une mesure cérébrale suit-elle la fonction, ou la mécanique ? (direction 4)

- **Grandeur.** PCI_art′ = c(B)·log₂M / (M·H(p₀)).
  - B est la réponse à δ sur 16 directions aléatoires gelées [illustratif], pour les couches au-delà de l₀ et les positions à partir de t₀, plus k jetons forcés.
  - On met à 1 les p₀ = 10 % [illustratif] plus grands |Δ| de toute la matrice. Le seuil est global : la décroissance d'amplitude avec la profondeur reste visible, alors qu'un seuil par couche l'effacerait. La densité de réponse, perdue ici, passe dans les scalaires mécaniques.
  - Unité : sans dimension. Plancher : une réponse confinée près de (l₀, t₀), calculée. Référence de bruit : B permutée à densité p₀, soit environ 1 ; le biais de taille finie est calculé.
- **Positifs.** 10 graines indépendantes [illustratif] d'un petit modèle entraîné sur un corpus public. À défaut, des suites publiques à plusieurs graines (référence à vérifier).
- **Négatifs.** Tous sont appariés en gain jacobien mesuré de bout en bout (exigence de A contre C).
  - T1 : poids permutés.
  - T2 : initialisation.
  - T4 : poids aléatoires dont la température d'attention est recalibrée pour égaler l'entropie d'attention du modèle entraîné (correction que C propose contre E).
- **Mécanique à battre.** Gain, norme de réponse, entropie d'attention, Δperte, masse d'attention inter-positions.
- **Verrou 1.** ΔAUC = AUC(PCI_art′ + mécanique) − AUC(mécanique). Le prédicteur est non linéaire, validé en laissant un réseau dehors. Unité : points d'AUC ; valeur nulle : 0 ; m = 0,1 [illustratif].
- **Verrou 2.** Rang de L1 dans la loi conditionnelle des ablations aléatoires (A-a4). Valeur nulle : rang médian.
- **H_A (la mesure suit la fonction).** Les deux verrous dépassent leur marge.
- **H_B (la mesure suit la mécanique).** Un verrou au moins reste sous sa marge.
- **Prédiction risquée maintenue.** T2, apparié en gain, atteint ou dépasse les modèles entraînés.
- **Contrôles du code, hors décision.**
  - δ = 0 donne Δ ≡ 0.
  - T3 gelé donne une réponse confinée au chemin résiduel ; T3 retiré donne environ 1.
  - Un amortissement imposé a_l = γ^l (contrôle que E demande à C) doit faire baisser PCI_art′ quand γ diminue.
  - Dans un réseau jouet à couplage réglable, PCI_art′ doit croître avec le couplage.
- **Première expérience.** Graines de quelques millions de paramètres ; 100 sites × 20 directions ; quelques heures GPU [tout illustratif].

### E2′ — Une intervention supprime-t-elle le global plus que la profondeur ne l'explique ? (direction 1)

- **Stimuli.** Mots d'un seul sous-token. Bloc X : xxxxx fréquent, xxxxy rare. Bloc Y : l'inverse. Le plan a quatre cellules.
- **Grandeurs.** E_loc est l'effet principal du changement du dernier symbole. E_glob est l'effet principal de la rareté de la suite dans le bloc. Mesure : surprise sur le dernier jeton, en nats ; valeur nulle : 0.
- **Témoin de profondeur.** E_loc,prof : une régularité locale à plusieurs étapes, par exemple une alternance abab dans la suite. C'est la demande que A et C adressent à F ; je la reprends.
- **Précondition p1.** Les bornes inférieures de E_loc et de E_glob sont > 0 sur le modèle intact, sur la moitié d'items tenue à part.
- **Précondition p2.** Après moyennage de Welch, le pic au rythme de la phrase (¼ de cycle par mot [illustratif]) doit être plus haut dans les couches profondes qu'en couche 0, et plus haut que dans des pseudo-phrases appariées en catégories et en sous-tokens. Sinon le couple mot/phrase est retiré.
- **Interventions.** I1 (gain α), I2 (bruit σ), I3 (température τ).
- **Nul.** 1 000 directions et sous-ensembles de couches tirés au hasard, avec le maximum sur les familles recalculé à chaque tirage.
- **Signature.** On place les points (ln R_loc, ln R_glob), dose par dose, avec R = E(dose)/E(0).
  - La composition (rétention q^k, calcul de A et C) prédit une droite qui passe par l'origine, de pente commune à toutes les familles. C'est la signature que A propose contre E ; je la reprends.
  - Statistique : l'angle θ entre la droite d'une famille et la droite nulle. Unité : radians ; valeur nulle : 0. Elle ne dépend d'aucune abscisse, et ne divise par rien quand R_loc ≈ 1.
- **H_A (sélectivité).** Une famille au moins a un θ hors de la bande nulle à 95 % [illustratif], et le global y tombe plus que E_loc,prof. Le résultat doit se répliquer sur un second modèle.
- **H_B (composition générique).** Aucune famille ne sort de la bande, ou le global ne tombe pas plus que E_loc,prof.
- **Contrôle positif.** La troncature de fenêtre M doit sortir de la bande ; sinon la signature est aveugle.
- **Prédiction humaine de H_B (HYPOTHÈSE).** θ reste nul d'un palier de propofol à l'autre, calculé en d′. D'après A et C (critiquant D), l'échelle AUC − 0,5 est biaisée. Données publiques : référence à vérifier.
- **Première expérience.** GPT-2 small et Pythia-160M ; 4 cellules × 500 items ; 3 familles × 6 doses [illustratif].

### E3′ — Le régime appartient-il au modèle, au texte, ou à toute dégradation ? (direction 2)

- **Détecteur.** Une sonde linéaire, entraînée sur activations normalisées, sépare l'intervention E2′ de l'intact. Si E2′ donne H_B, on utilise I2. Le seuil est calibré sur du texte naturel tenu à part.
- **Cible.** La perte d'un référent lointain annotable, dans les k jetons suivants, dans le modèle M.
- **Comparateurs.**
  - T_M′ : la même recette, dans un autre réseau M′ (une autre graine d'E1′) qui lit le même texte.
  - T_bruit : la sonde d'une dégradation concurrente à Δperte égale, dans M (contrôle que D demande à A).
  - T_norme : la norme seule.
- **Grandeur.** ΔAUC_propre = AUC(T_M) − max(AUC(T_M′), AUC(T_bruit), AUC(T_norme)). Unité : points d'AUC ; valeur nulle : 0 ; m = 0,05 [illustratif].
- **H_A (régime propre au modèle).** ΔAUC_propre > m, dans les deux sens de l'échange entre M et M′, sur deux paires de réseaux au moins [illustratif].
- **H_B (le texte, ou une dégradation quelconque).** ΔAUC_propre ≤ m.
- **Données.** Partie validation de The Pile (R21) et générations libres avec boucles de répétition (R22). Bootstrap par document.
- **Contrôle négatif.** Sur des textes mélangés phrase à phrase, ΔAUC_propre doit être d'environ 0.
- **Lecture.** Si H_B gagne, ce « régime » se réduit au texte ou à une dégradation générique, pour cette architecture. Si H_A gagne, une variable propre au modèle existe ; rien n'exclut qu'elle soit un mode de panne idiosyncratique.

### E4′ — Le modèle lit-il un traitement contextuel résiduel sous sédation ? (direction 3)

- **Traits emboîtés, ridge par blocs.**
  - B0 : enveloppe acoustique, spectrogramme, début et débit des mots, fréquence des mots, plongements statiques et leurs moyennes glissantes à plusieurs échelles (contrôle que F demande à A, C et E).
  - B1 = B0 + surprise n-gramme.
  - B2 = B1 + la même architecture non entraînée.
  - B3 = B2 + le modèle entraîné, couche l.
- **Grandeur.** ΔR²_ctx,s = R²(B3) − R²(B2), hors échantillon, par région, dans l'état s, sans normalisation par le plafond. Unité : fraction de variance ; valeur nulle : 0.
- **Duel 1 (présence).**
  - H_A1 : en sédation profonde, ΔR²_ctx > m dans au moins une région, après contrôle du taux de fausses découvertes, avec le sujet comme unité.
  - H_B1 : ΔR²_ctx ≤ m partout. Cette issue ne s'interprète qu'au-dessus du seuil de détection fixé par simulation d'une composante plantée (procédure de III.1).
- **Duel 2 (sélectivité).**
  - Pseudo-sédation : l'éveil des mêmes sujets, plus un bruit coloré dont la fiabilité et le spectre égalent ceux de la sédation (précisions que D et F adressent à A).
  - Pour chaque jeu de traits X : D_X = ΔR²_X(sédation) − ΔR²_X(pseudo-sédation), avec X = acoustique ou contexte.
  - H_A2 (perte sélective du contexte) : D_ctx < −m et |D_acoustique| ≤ m.
  - H_B2 : l'une des deux conditions manque.
  - Validation préalable : sur des données simulées où le gain contextuel est égal entre états, la procédure doit donner D_ctx ≈ 0.
- **Contrôles négatifs.** Un récit mal apparié (contrôle que D demande à A) doit donner ΔR² ≈ 0. Pas de nul par décalages circulaires : sur 5 à 8 minutes [illustratif], le petit nombre de décalages distincts borne la plus petite valeur p. C'est l'objection de F à C et à E ; elle vaut aussi pour moi.
- **Précondition.** L'intervalle de la fiabilité en sédation doit exclure 0. Sinon, E4′ est non jugeable sur ce jeu, et je le rapporte.
- **Données.** IRMf de sédation au propofol pendant l'écoute d'un extrait de film (Naci et al., 2018 ; référence à vérifier). Disponibilité publique d'EEG ou de MEG : à vérifier.

## (c) Réponse à la question de l'arbitre

**Ce qui est établi.** Ce collisionneur n'a produit ni examiné aucune donnée. Aucun résultat n'y est donc établi.

Résultats publiés (RAPPORTÉ, cités de mémoire) :
- L'anesthésie dissocie conscience, connexion à l'environnement et capacité de réagir (R1).
- Le contraste dépend de l'agent (R3).
- Le PCI a été calibré contre ce que les sujets pouvaient rapporter (R4, R5).
- Chez des sujets non conscients, en sommeil ou sous propofol selon l'étude :
  - l'effet global, le suivi de la phrase et la réponse à l'ambiguïté baissent ;
  - l'effet local, le suivi syllabique et la réponse temporale à la parole persistent en grande partie (R10–R14).
- Des modèles non entraînés prédisent déjà une part des réponses cérébrales (R16).

Propriétés formelles relevées contre B :
- Deux passes identiques d'un transformeur donnent un écart nul (VÉRIFIÉ selon C).
- L'état est une fonction de l'entrée (VÉRIFIÉ selon E).
- Sous une atténuation commune, l'ordre des contrastes d'éveil se conserve (HYPOTHÈSE de A ; même argument chez F).

Si ces propriétés tiennent, trois transpositions directes sont tranchées d'avance par construction et n'apprennent rien (HYPOTHÈSE) :
- un seuil défini sur une activité de fond ;
- un état « hors entrée » ;
- le contraste éveil−sédation.

**Ce qui ne l'est pas.**
1. Qu'une mesure cérébrale suive la fonction d'un réseau au-delà de son gain, de sa norme et de son entropie d'attention (E1′).
2. Qu'une intervention épargne le local et supprime le global autrement que par la profondeur de composition. Ni, côté humain, que cette dissociation échappe elle-même à la composition (E2′).
3. Qu'un régime propre au modèle survienne de lui-même, distinct du texte et d'une dégradation quelconque (E3′).
4. Qu'un modèle de langage lise sous sédation un traitement contextuel que des traits plus simples ne lisent pas (E4′).
5. Qu'un réseau ait une expérience. Aucune issue ne le dit, faute d'ancre côté réseau (a6). La réversibilité n'apprend rien côté réseau (a7).

**Ma réponse (HYPOTHÈSE).** Le contraste se transpose comme modèle nul et comme banc d'essai des mesures, pas comme détecteur de conscience. On peut apprendre si les marqueurs humains de l'anesthésie sont spécifiques, ou s'ils découlent de propriétés que partage tout traitement hiérarchique dégradé : le gain, la profondeur. On n'apprend pas si un réseau est conscient.

Ce qui est réfutable : cinq duels (E1′, E2′, E3′, et deux en E4′), soit dix issues qui falsifient chacune une hypothèse. Chaque duel a aussi une issue « non jugeable », déclarée d'avance.

**L'expérience à faire en premier : E2′, la précondition p1 puis le duel.**
- Elle coûte quelques heures sur des modèles ouverts.
- Son H_B, désormais chiffré (θ nul), est le modèle nul que doit battre toute transposition fondée sur une dissociation, y compris dans les autres propositions.
- E3′ dépend de la signature qu'elle fournit.
- Elle prédit un résultat côté cerveau (θ nul d'un palier de propofol à l'autre), testable sans réseau.
- Un échec de p1 apprend déjà quelque chose : sans effets local et global séparés sur le modèle intact, le paradigme ne se transpose pas à cette échelle, et la direction 1 s'arrête là.

**Ce que changerait E2′.**
- Pour qui cherche si une IA peut être consciente : H_B retire le couple local/global des marqueurs spécifiques à transférer ; H_A fournit une composante manipulable, pas un verdict.
- Pour qui juge la question mal posée : H_B appuie l'idée que ces marqueurs suivent la profondeur du traitement ; H_A montre qu'un réseau sans ancre de conscience reproduit le profil, donc que le profil ne suffit pas.

FIN-DE-CELLULE