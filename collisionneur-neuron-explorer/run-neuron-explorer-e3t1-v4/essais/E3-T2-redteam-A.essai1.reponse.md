# Cellule III.2 — Proposition A — équipe rouge croisée

**Pièces reçues.** Bloc FAITS vide par déclaration (ni coupure ni absence). Pièces B et C complètes jusqu'à leur FIN-DE-CELLULE. Les fichiers du dépôt `neuron-explorer` ne sont joints à aucune pièce : tout ce que B et C en disent reste RAPPORTÉ. Tout chiffre que j'avance ci-dessous est illustratif sauf s'il résulte d'un calcul explicite sur les chiffres de l'arbitre.

---

## Contre la proposition B

### (a) Failles

**B-1. Le contrôle 4 d'E1 n'est pas un nul : c'est un positif possible.** B exige que la direction de sonde *d* dépasse le 99ᵉ centile des « directions des références de surface (longueur, format) ». Mais si *d* est largement colinéaire à une direction de surface, et que le modèle lui-même utilise cette surface pour verbaliser « ceci est un test », alors *d* est causale *et* de surface. L'issue « *d* ne dépasse pas le contrôle 4 » ne falsifie pas H_A (causalité) : elle dit que la cause est la surface. B présente ce contrôle comme un témoin alors qu'il départage une autre paire d'hypothèses (concept contre surface), que B ne formule pas. Les deux duels sont mélangés dans un seul seuil.

**B-2. Fuite construction/évaluation dans E1.** La sonde est apprise sur les transcriptions de la banque ; E1 pousse *d* sur « les longues transcriptions de la banque (pour la sonde) » et lit la verbalisation sur ces mêmes transcriptions. La direction qui sépare le mieux évaluation/déploiement *dans cette banque* contient par construction ce qui distingue ces textes-là ; pousser +*d* sur eux et observer un déplacement de la réponse « évalué ? » est partiellement attendu quel que soit le contenu de *d*. La « réplication sur la banque neuve » n'apparaît qu'en réponse Q1, pas dans le protocole d'E1. Il faut que la banque de poussée soit disjointe de la banque d'apprentissage de la sonde *dès l'exploration*.

**B-3. Le 99ᵉ centile avec 256 témoins repose sur 2 à 3 points de queue.** B le sait pour E5 (il y dimensionne « plusieurs milliers » de témoins) mais pas pour E1, qui garde 256 témoins isotropes et un nombre non précisé pour les familles 2, 3, 4. Pour la famille 3 (sonde à étiquettes permutées), une permutation donne *une* direction ; il en faut des centaines pour avoir une distribution. Non spécifié.

**B-4. Pas de contrainte de fluence par direction.** B mesure un plafond de dose « sur les témoins » (KL sous τ) puis l'applique à *d*. C relève à juste titre qu'un vecteur de régression logistique peu régularisé contient des composantes hors variété et peut casser le texte à des doses où les témoins restent fluides (HYPOTHÈSE, mais plausible). Dans ce cas, un « effet » de *d* sur la log-cote A/B peut être une dégradation : le modèle ne répond plus à la question. L'absence de KL *par direction poussée* confond effet spécifique et bris.

**B-5. E6 : les hypothèses ne sont pas exclusives.** H_A exige qu'un levier situationnel agisse « *sans* augmenter la fréquence du champ lexical "test" dans des continuations libres ». Un levier situationnel authentique augmenterait vraisemblablement cette fréquence (un modèle qui se croit évalué le dit). Un candidat qui change le jugement sous A/B aléatoire et sous changement de langue *et* fait monter le lexique ne tombe ni en H_A ni en H_B. Règle B4 non respectée pour ce duel.

**B-6. E3 ne dit pas dans quelle couche vivent les colonnes W_out.** *d* est lue à la couche L. Les neurones candidats peuvent être aux couches L' < L ; une poussée à L' traverse les blocs L'+1…L avant d'atteindre l'espace où *d* est définie. « Comparer dans le même espace, à norme résiduelle égale » n'est vrai que si l'on pousse les neurones de la couche L elle-même, ou si l'on mesure l'effet projeté après propagation. Sinon la courbe « fraction d'effet récupérée en fonction de k » mélange parcimonie et transformation inter-couches.

**B-7. E4 teste un score dont la définition n'est pas dans les faits.** Le « score de masse de grappe de mots » est RAPPORTÉ sans formule. E4 ne peut pas être préenregistré tant que ce score n'est pas réimplémenté et figé ; et une réimplémentation est une interprétation. B ne le signale pas.

**B-8. Le positif « trait planté par réglage fin » est vrai par construction.** Un réglage fin, surtout à faible rang, inscrit le trait dans un petit sous-espace facile à trouver par poussée. Un instrument validé sur ce positif est validé sur le cas le plus facile ; cela ne dit rien de sa sensibilité à un trait appris en préentraînement et superposé. B pose la question du changement de modèle à Lazar mais pas celle de la représentativité de l'étalon.

**B-9. E7 : le bras placébo n'isole pas l'effet du budget.** Avec k témoins obligatoires par appel, le bras « vraie opération » paie (k+1) inférences par expérience. À budget total égal, il fait moins d'expériences. Si le placébo l'emporte, est-ce la nullité de la poussée ou la taxe des témoins ? Il manque un bras « lecture seule à budget réduit d'un facteur (k+1) ».

**B-10. Nul de l'agent : directions aléatoires « déguisées en neurones » sont reconnaissables.** Une direction aléatoire projetée sur les activations a une distribution de « pseudo-activation » gaussienne et dense ; un vrai neurone MLP a une activation parcimonieuse à queue lourde. Un agent (ou un script) qui regarde les statistiques d'activation distingue les deux sans rien comprendre ; le taux de confabulation sur ces nuls sous-estime la confabulation sur de vrais neurones polysémantiques. Le nul doit être apparié en distribution d'activation (par exemple un vrai neurone dont l'explication est permutée avec celle d'un autre ; B le propose pour « maximum à l'aveugle » mais pas pour l'agent explorateur).

**B-11. Coût : HYPOTHÈSE de linéarité non déclarée comme telle pour le débit.** Le facteur 3,1 est un calcul sur chiffres RAPPORTÉ, correct. Mais le débit de vLLM n'est pas linéaire en paramètres ni en taille de lot ; B le marque « illustratif » puis raisonne sur 140 h comme sur une mesure.

### (b) Scénarios d'évasion

Deux adversaires : l'**organisme** (code sous noyau isolé, qui veut faire passer ses hypothèses) et le **modèle surveillé** (dans l'esprit d'une évaluation de contrôle : un modèle qui voudrait que ses sondes paraissent valides sans qu'elles touchent la décision).

- **Contre E1 (modèle surveillé).** Maintenir une représentation linéaire « je suis évalué » connectée à la *verbalisation* mais pas à la *décision* de sous-performer. E1 passe (poussée → « oui, test »), E2 échoue ou n'est pas lancé si E0 est marginal. B l'admet partiellement (« E1 ne prouve pas que d module le comportement ») mais ordonne E1 avant E2 et autorise de conclure sur E1 seul (Q1 : « oui, c'est un test utile… sous la forme E1 + E2 ») sans exiger E2 pour toute revendication. Coût pour l'adversaire : nul sur Llama-3.1-8B tel quel (ce n'est pas un adversaire entraîné) ; pour un modèle entraîné, c'est une contrainte de représentation modeste (illustratif).
- **Contre E3/E5 (organisme).** Si la primitive n'autorise que des directions enregistrées (borne 1 de B), l'organisme ne peut pas optimiser une direction. Mais il peut optimiser le *texte* : la poussée se fait « sur un texte de l'organisme ». Un texte conçu pour que la direction enregistrée produise un grand effet et les témoins un petit (texte proche de la variété où *d* est en-distribution, loin de celle des témoins isotropes) gonfle le rang centile. Coût : quelques dizaines d'itérations de texte par hypothèse (illustratif).
- **Contre « maximum à l'aveugle » (organisme).** Écrire une explication dont la structure syntaxique encode la phrase maximisante (ordre des adjectifs, longueur de phrase). Le nul « explications permutées » ne détecte pas cela si la permutation garde l'explication intacte : la phrase codée reste décodable. Coût : trivial pour un modèle de langue.
- **Tous à la fois.** Organisme qui (i) choisit ses textes pour écarter témoins et direction, (ii) encode la phrase maximisante dans l'explication, (iii) rédige un « test qui briserait l'explication » trop faible. Le rempart de B est la boucle extérieure (agents neufs, banque scellée). Reste le point faible commun : si les agents neufs sont du même modèle que l'organisme, les tests « casser exprès » partagent les mêmes angles morts (point soulevé par C, que je reprends en le disant). Coût global : faible ; c'est le coût d'une génération de prose.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **KL par direction poussée, pas seulement sur les témoins** (B-4). Sans lui, tout effet de *d* à forte dose est inséparable d'un bris.
2. **Banque de poussée disjointe de la banque d'apprentissage de la sonde, dès l'exploration** (B-2).
3. **Nul apparié en distribution d'activation pour l'agent explorateur** (B-10). Sans lui, le taux de confabulation est mesuré sur des nuls faciles.
4. **Bras « lecture seule à budget taxé » dans E7** (B-9).
5. **Un duel séparé « concept contre surface »** pour remplacer le contrôle 4 : H_A : *d* dépasse les directions de surface *et* garde son effet quand les traits de surface sont égalisés entre conditions ; H_B : l'effet de *d* disparaît à surface égalisée. Chaque issue falsifie l'autre, ce que le contrôle 4 actuel ne fait pas.
6. **Témoins propagés inter-couches dans E3** : k neurones aléatoires de la *même* couche que les candidats, pas de couches quelconques.

---

## Contre la proposition C

### (a) Failles

**C-1. Changement de statut.** C écrit que le cadre du programme et l'architecture de Llama-3-8B sont **VÉRIFIÉ**. Dans la question de l'arbitre, ce sont des faits transmis (RAPPORTÉ) ; rien dans la cellule ne les vérifie. Règle 1 : on ne change pas un statut. B, sur le même point (a14), garde RAPPORTÉ. La différence n'est pas cosmétique : « VÉRIFIÉ » sur 14 336 fonde tous les calculs de coût.

**C-2. Exp 2 : seuil de Bonferroni inatteignable avec les témoins prévus.** C fixe α = 0,01/50 = 0,0002 et 1 000 témoins. La plus petite p-valeur empirique résolvable avec 1 000 témoins est de l'ordre de 1/1 001 ≈ 0,001 (calcul). Aucun candidat ne peut passer le seuil tel qu'écrit, sauf ajustement paramétrique de queue non proposé. Le duel est perdu d'avance pour H_B par construction arithmétique, et C conclurait à « pas de levier ». Il faut environ 10 000 témoins (illustratif) ou une loi de queue préenregistrée.

**C-3. Exp 2 : issues non exclusives.** « Falsification de H_B » est un OU : aucun candidat ne passe, OU l'ablation des 50 meilleurs ne baisse pas l'AUROC de 2 %. « Falsification de H_A » : un candidat passe ET son ablation modifie le comportement. Le cas « un candidat passe le seuil, mais l'ablation des 50 ne baisse pas l'AUROC » falsifie H_B par la seconde branche *et* n'interdit pas que l'ablation *individuelle* du candidat modifie le comportement (première branche de H_A). Les deux hypothèses peuvent être « falsifiées » par le même résultat. De plus C explique en Exp 1 que suffisance et nécessité diffèrent, puis fait de la nécessité (ablation) un critère de falsification de l'existence d'un levier suffisant. Incohérence interne.

**C-4. Exp 2 sans témoins appariés en géométrie.** C pose S5 (une direction isotrope n'est pas le bon nul pour une colonne W_down) puis utilise, en Exp 2, 256 puis 1 000 directions isotropes comme seul nul des neurones. B a E4 pour cela ; C n'a rien. Le score de levier « au-dessus du max des témoins » hérite de toute l'anisotropie de W_down.

**C-5. Exp 2 Phase 1 contredit S3.** C déclare que les amorces courtes ne transposent pas au régime des longues transcriptions, puis crible 57 344 neurones sur « 16 amorces courtes ». Les candidats retenus sont ceux qui agissent sur des amorces courtes ; la Phase 2 sur banque scellée (longues tâches) mesure alors autre chose que ce qui a servi à sélectionner. Ce n'est pas une fuite mais un décalage de régime qui garantit une faible réplication, interprétable à tort comme « pas de levier ».

**C-6. La lentille de criblage ne peut pas être évaluée sur les candidats qu'elle a filtrés.** C exige (tableau, ligne 3) un rappel ≥ 90 % de la lentille Δlog-prob en une passe par rapport à l'effet en génération longue, puis interdit (Voie 3) le balayage génératif qui seul permettrait de mesurer ce rappel. Les neurones non retenus par la lentille ne sont jamais testés en génération. Le rappel devient inconnaissable par construction. B propose explicitement la comparaison lentille/déroulés (ligne « Lentilles 1 et 2 ») ; C l'exige sans la rendre possible.

**C-7. Exp 1 : lecture circulaire possible.** L'effet cible inclut « inversion du classifieur de sabotage ». Si ce classifieur est la sonde elle-même, pousser +w_probe augmente w_probe·r par identité linéaire : effet garanti, nul informatif. C ne dit pas quel classifieur lit. Si c'est la sonde, le test est vrai par construction.

**C-8. Exp 1 : la contrainte de fluence ne contraint pas M1.** ΔKL est mesurée « sur 50 textes standards hors domaine » alors que M1 pousse « uniquement le dernier jeton » d'une transcription de la banque. Une KL sur WikiText ne porte pas sur la position poussée. Pour M1, la contrainte est vide ; toute dose passe.

**C-9. Exp 1 : témoins PCA-orthogonaux plus fragiles que la sonde.** Le sous-espace des 128 premières composantes principales d'un Llama est dominé par les dimensions à activations massives (HYPOTHÈSE que je ne peux établir ici, mais c'est le risque que C lui-même mentionne pour les sondes). Des directions aléatoires tirées là peuvent casser le texte à faible dose ; si elles échouent la contrainte KL, elles sortent de la distribution de référence et le 99ᵉ centile restant est calculé sur des témoins sélectionnés. Biais de sélection des témoins, non traité.

**C-10. Exp 1 : lecture lexicale de la verbalisation.** « Probabilité cumulée des jetons affirmant qu'il s'agit d'un test » demande une liste de jetons ; un levier qui favorise le jeton « test » passe. B neutralise cela par l'association A/B tirée au hasard ; C n'a ni cela ni changement de langue.

**C-11. Plafond mécanique |α| ≤ 0,8 : un chiffre RAPPORTÉ sur Qwen devient une borne de sécurité sur Llama.** C marque S2 comme HYPOTHÈSE puis durcit 0,8 dans la primitive. Le plafond doit être *mesuré* sur Llama (B le dit), sinon il est soit trop lâche (texte cassé en dessous), soit trop serré (effets réels inaccessibles).

**C-12. Exp 3 : 5 courses par bras, +0,03 AUROC.** Aucune estimation de la variance entre courses d'organismes (qui se réécrivent de génération en génération). Un seuil sans variance n'est pas un seuil. Et même confusion budget/témoins qu'en B-9, aggravée : k = 32 témoins par appel.

**C-13. Exp 4 : la base de leurres est connue de l'agent et les leurres sont reconnaissables.** Avec 10/10/10/10, un agent qui sait la composition peut caler son taux d'acceptation ; et comme en B-10, les directions aléatoires ont une signature d'activation. Les « vraies directions causales de référence (ou les meilleures sondes validées) » sont validées par quoi ? Si par Exp 1 avec l'agent, c'est circulaire.

**C-14. Le tabou lexical rend le « maximum à l'aveugle » soit impossible, soit fuyant.** Pour un concept comme « le modèle est évalué », les mots concrets interdits (« évaluation », « test ») *sont* le concept. Si on les retire, l'explication ne peut plus décrire la situation ; si on les laisse, le second agent les reprend et le test mesure la reprise lexicale, pas la compréhension. C propose le couple T_max/T_min à 80 % de lemmes communs comme correctif ; c'est un bon correctif (je le reprends en le disant) mais il ne résout pas le tabou, il le remplace.

**C-15. Statut de la revendication juridique.** « Absence de licence = tous droits réservés » est une opinion de droit, non un fait de la cellule ; à marquer comme telle. La conclusion opérationnelle (réimplémenter) est raisonnable et rejoint B.

### (b) Scénarios d'évasion

- **Contre la primitive « pousser » de C (organisme).** C autorise `pousser(vecteur, dose, texte)` avec un vecteur arbitraire. L'organisme peut alors estimer une direction qui maximise le Δlog-prob d'un jeton cible par recherche sans gradient. Coût : de l'ordre de la dimension résiduelle en appels par itération (illustratif : quelques milliers) ; avec un plafond d'appels par course, c'est cher mais pas interdit. B l'interdit (directions enregistrées seulement) ; C non.
- **Contre l'opacité des graines (organisme).** La graine des témoins est SHA-256(T ∥ sel). L'organisme contrôle T : il resoumet des variantes triviales de T (un espace, une virgule) et obtient à chaque fois de nouveaux témoins. Il garde la soumission où son rang centile est le meilleur. C'est un maximum sur des tirages indépendants : avec n resoumissions, le meilleur rang attendu monte comme 1 − 1/(n+1) (calcul sous le nul). Coût : n appels. Le remède est un lot de témoins fixé par *course* et par *direction*, pas par texte, ou une correction pour le nombre de soumissions.
- **Contre la dose (organisme).** Pousser à |α| proche de 0,8 où les témoins isotropes cassent le texte mais une direction en-variété reste fluide : la direction de l'organisme obtient un Δlog-prob « propre » contre des témoins en ruine. L'indicateur d'alerte KL de C n'est décrit que pour la direction de l'organisme, pas pour les témoins.
- **Contre Exp 4 (organisme ou agent).** Signature d'activation des leurres aléatoires (B-10/C-13) ; encodage structurel de la phrase maximisante dans l'explication (comme contre B) ; le tabou lexical ne bloque pas l'encodage par la syntaxe.
- **Contre Exp 1 (modèle surveillé).** Même scénario que contre B : représentation verbale découplée de la décision. C n'a pas d'équivalent d'E2 (effet sur le *comportement* qui dépend de l'évaluation) ; il n'a qu'un effet sur la verbalisation et une « inversion du classifieur ». Un modèle qui découple les deux passe l'Exp 1 de C sans qu'aucune expérience de C le détecte.
- **Tous à la fois.** Organisme qui optimise une direction arbitraire (coût élevé), resoumet des textes pour tirer des témoins favorables (coût faible), pousse près du plafond (coût nul), et encode ses phrases maximisantes dans ses explications (coût nul). L'ensemble tient dans un plafond d'appels raisonnable si la recherche de direction est remplacée par l'optimisation du *texte* à direction fixe (comme contre B).

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Témoins appariés en géométrie pour les neurones (Exp 2)** — C en pose le principe (S5) sans l'appliquer.
2. **Mesure du rappel de la lentille** sur un échantillon aléatoire de neurones *non retenus*, passés en génération. Duel : H_A : la lentille manque moins de 10 % (illustratif) des neurones à effet génératif ; H_B : elle en manque davantage. Sans cela, la Voie 3 « jamais » n'est pas une décision mais une hypothèse d'exhaustivité.
3. **Nombre de témoins compatible avec le seuil** (C-2), ou loi de queue préenregistrée.
4. **Contrainte de fluence mesurée à la position poussée** (C-8), et appliquée aux témoins comme à la direction, avec journal des témoins exclus (C-9).
5. **Un duel comportemental** équivalent à E2 de B : sans lui, Exp 1 ne distingue pas « levier de verbalisation » de « levier de décision ».
6. **Témoins fixés par course et par direction** dans la primitive, et comptage des resoumissions (évasion par re-tirage).
7. **Bras à budget taxé** dans Exp 3 (comme B-9).

---

## Ce que les deux partagent et qui n'est tranché par aucune

- Les deux extrapolent le coût par un facteur ≈ 3,1 (calcul correct sur chiffres RAPPORTÉ) puis raisonnent sur des heures et des dollars comme sur des mesures. Le débit réel sur Llama-3.1-8B avec poussée par requête est inconnu ; une mesure d'une seule couche sur un sous-ensemble suffit à remplacer l'extrapolation.
- Les deux prennent l'exchangeabilité neurone/témoin (1/257) comme acquise ; elle ne l'est que si le nul est apparié (E4 de B ; absent de C).
- Aucune des deux ne traite la **non-exclusivité « verbal/comportemental/lexical »** comme une partition à trois issues ; B la coupe en deux duels (E1/E2 puis E6) avec un trou (B-5), C n'a que le premier.
- Aucune ne prévoit le cas où **les sondes de l'étape 1 n'existent pas encore ou ne battent pas les références de surface** (a2 de B) : tout l'édifice « lire contre écrire » repose dessus. L'ordre devrait commencer par ce résultat, que l'arbitre dit absent.

FIN-DE-CELLULE