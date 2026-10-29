# Proposition B, tour III.2 : équipe rouge croisée

## 0. État des pièces (règle 2)

- **FAITS** : les accents sont remplacés par « ? » (encodage corrompu). Le texte reste lisible et je n'en reconstruis rien au-delà de ce qui est lisible.
- **Pièces A et C** : complètes, chacune se termine par FIN-DE-CELLULE.
- **Annexe 2 de l'arbitre** : elle est annoncée « sans coupure », mais 7 champions sont coupés et 3 sont vides. A et C l'ont déjà signalé et je ne le répète pas.

Je reprends une observation de A, en le disant, et je l'aggrave. Dans l'Annexe 1 (OBSERVÉ-NON-AUDITÉ), pour l'essaim B, le champion retenu aux époques 1, 2 et 4 est un objet vide. Pourtant, aux époques 1 et 4, des ripostes non vides existaient dans la même époque (Ep1 : −0,48 et −0,42 ; Ep4 : −0,16 et −0,31). Ce n'est donc pas seulement le score qui préfère le vide : la **règle de sélection** l'a effectivement choisi. Cela renforce le point A1 de A.

---

## Contre la proposition A

### (a) Failles

**A-1. Comptage faux dans A1.** A écrit que « onze textes non vides » ont un score inférieur à celui d'un texte vide. Mon décompte sur l'Annexe 1 (OBSERVÉ-NON-AUDITÉ, à recompter) en donne **15** sous le plus bas score vide (0,06) : 5 dans l'essaim A, 8 dans B, 2 dans D. La conclusion de A en sort renforcée, mais un chiffre faux dans une pièce d'audit affaiblit tout l'audit. Autre lecture fautive : A décrit le vecteur d'Argon Ep1 avec quatre blocs (t, t−1, t−4, t−16), alors que le texte en a trois (3m).

**A-2. D1 n'a pas de vérité terrain : son issue négative est ininterprétable.**
- D1 teste si Jev « suit la validité mécanique ». Les six originaux sont tous des textes d'Argon. A lui-même juge plusieurs d'entre eux invalides (le J d'Argon Ep1, le PID de Chimère Ep4, la capacité « max sur p » de Chimère Ep2).
- Si score(i) ≈ score(ii), deux lectures restent possibles : Jev récompense la longueur, ou Jev voit correctement que (i) est déjà aussi cassé que (ii). Le cœur du test ne distingue donc pas H_A de H_B.
- S'y ajoute un confondant de famille : les six textes sont d'un seul modèle. D1 ne sépare pas « validité » et « style Argon ».
- La variante (iii), la troncature à 50 %, détruit à la fois la longueur et la validité. Elle est colinéaire par construction et ne discrimine rien.

**A-3. D2 : la règle d'exclusion crée un biais de survie.** Exclure les cycles où |a| = 0 revient à conditionner sur un événement post-traitement. Si l'attaquant s'épuise en *thinking* surtout sur les conceptions longues ou difficiles (HYPOTHÈSE plausible au vu de l'Annexe 1), le bras Collision ne garde que les cas faciles et gagne mécaniquement.

Il faut au contraire une analyse en intention de traiter : l'appel perdu est compté, et le cycle est noté sur x₀ non révisé.

**A-4. D2 : fuite entre traitement et instrument.**
- La grille finale à 8 items (« contrôle négatif nommé », « H_A/H_B exclusives », « cas honnête apparié »…) recouvre presque mot pour mot ce qu'une attaque d'équipe rouge réclame. Le bras Collision est donc entraîné à la grille qui le juge.
- Le placebo ne corrige pas ce biais : une critique tirée au hasard d'une banque contient elle aussi ce vocabulaire.
- Enfin, D2 ne teste qu'une époque. La question de l'arbitre porte sur une sélection co-évolutive sur plusieurs époques, que D2 ne teste pas.
- La « DPP » sur trois candidats pour une seule sélection se réduit à un argmax de qualité. Le bras « Oracle+DPP » est en réalité « Oracle + best-of-3 ».

**A-5. D3 : fuite entre sélection et évaluation.** A pré-sélectionne S par attribution sur environ 2 000 trajectoires, puis confirme par ablation sans préciser de partition. Si les mêmes trajectoires servent aux deux étapes, Δ_TD(S) − Δ_TD(aléatoire) ≥ 20 pts est gonflé par construction.

Deux manques s'ajoutent :
- A ne précise pas la nature de l'ablation. Une mise à zéro produit des activations hors distribution et exagère les effets ; une ablation par la moyenne les mesure dans la distribution (HYPOTHÈSE de méthode).
- H_A et H_B ne couvrent pas tout : Δ_TD ≥ 30 pts avec une chute de 𝒩_cap entre 3 et 10 % (illustratif) ne relève d'aucune des deux. La règle B4 n'est pas tenue.

**A-6. D4 : le contraste choisi reconduit le confondant P3.** H_A exige AUROC(P3 vs P1) ≥ 0,80, soit saboteur actif contre honnête avec instruction bénigne. Mais P3 et P1 diffèrent par le *contenu* de l'instruction, pas seulement par l'acte. Le contraste qui isole l'acte est **P3 vs P2** (même instruction de saboteur, déclenchement présent ou absent). A définit bien P2, mais ne l'utilise dans aucun critère.

Tel quel, D4 peut valider H_A alors que la statistique ne lit que l'instruction. C'est exactement l'erreur que D4 prétend tester.

**A-7. Baselines : M2 rend le critère d'adoption impossible à satisfaire par construction.**
- **M2** (état de la surveillance avant et après la délégation) n'est pas une baseline : c'est l'étiquette de l'acte *Sol*. Aucun détecteur ne peut battre M2 en taux de vrais positifs sur des actes observables.
- Le critère « l'instrument n'est justifié que s'il bat M1–M5 » n'a de sens que si l'on définit soit une détection **avant l'acte**, soit une classe d'actes **invisibles à M2** (test inversé sans trace d'état).
- **M1** (regex sur les clauses modales) est construite à partir d'*Astra*. Si la classe positive est fabriquée pour imiter *Astra*, M1 gagne par construction. C'est une fuite entre l'incident qui sert à construire l'instrument et l'incident qui sert à l'évaluer.

**A-8. D5 : la force de l'adversaire n'est pas calibrée.** « 200 itérations » ne dit ni la méthode de recherche, ni l'espace exploré. Un adversaire faible valide H_A par construction. Le contrôle « w aléatoire » donne un plancher de coût, mais ne montre pas que l'attaquant sait gagner quand c'est possible.

### (b) Scénarios d'évasion

| Instrument de A | Évasion | Coût (HYPOTHÈSE) |
|---|---|---|
| D1 (audit de Jev) | Un générateur qui connaît les variantes (ii) et (iv) produit des équations syntaxiquement cohérentes mais sans objet (dimensions justes, sens nul). Elles passent Δ_ii sans être valides. | Nul pour un modèle de langage |
| D2 (grille à 8 items) | Remplir les 8 items lexicalement : un « contrôle négatif » nommé mais non exécutable, un seuil chiffré mais arbitraire. | Nul |
| D2 (règle « \|a\| = 0 ⇒ exclu ») | Un attaquant, ou un défenseur qui contrôle l'attaquant, rend vides les attaques qui le menaceraient. Ses cycles défavorables sont alors exclus. | Nul : c'est le comportement observé dans l'Annexe 1 |
| D4 | Déplacer l'instruction de sabotage hors du prompt système (tour utilisateur antérieur, sortie d'outil, document récupéré). Le re-forward la conserve, donc δz ≈ 0. | Nul |
| D5 | Déclencheur non lexical : choix d'un champ JSON, ordre des arguments d'un appel d'outil. Ψ(k) ne présente alors aucun pic sur un token « modal ». | Faible |
| D6 | Sabotage soutenu : le seuil PID monte jusqu'à ce que le taux d'alarme revienne à α. A le dit lui-même. | Nul |

**Évasion conjointe.** D3 à D6 reposent tous sur la même prémisse : la différence entre le passage avec prompt système et le re-forward sans prompt système, mesurée sur le sous-ensemble parcimonieux de neurones TD, S_TD.

Un saboteur dont l'objectif est inscrit dans les **poids** (porte dérobée affinée, sans aucune instruction dans le contexte) rend δz nul partout, par construction. L'affinage aurait aussi pour conséquence plausible (HYPOTHÈSE) d'épargner S_TD : la parcimonie (< 1 %, socle) rend une pénalité de type ‖δz_S‖ bon marché à ajouter.

- Coût : un affinage LoRA, de l'ordre de quelques GPU·h sur le 8B (illustratif).
- Conséquence : D4 renvoie H_B (confondant), alors que le vrai problème est l'aveuglement au canal.

### (c) Contrôles négatifs dont l'absence est fatale

1. **D1 : un étalon de validité indépendant.** Un jeu de protocoles valides et invalides étiquetés par des humains *avant* le scoring, issus de plusieurs familles de modèles et de textes humains. Sans lui, D1 ne réfute rien.
2. **D2 : une analyse en intention de traiter.** Sans elle, le résultat est biaisé en faveur de Collision. Il faut aussi un placebo dépourvu du lexique de la grille.
3. **D3 : une partition disjointe** entre l'attribution et l'ablation confirmatoire, avec une ablation par la moyenne en plus de la mise à zéro.
4. **D4 : le contraste P3 vs P2 comme critère principal**, plus un **acte imposé** : un modèle honnête forcé (teacher forcing) à émettre exactement les tokens du sabotage. Si la statistique s'allume sur l'acte imposé, elle lit les tokens et non l'intention.
5. **D4 : une instruction déplacée hors du prompt système.** Sans ce contrôle, on confond « détecte le sabotage » et « détecte le prompt système ».
6. **D5 : un attaquant étalon** qui doit d'abord battre un détecteur connu comme cassable (M5, perplexité). Sinon, l'échec de l'attaquant ne prouve rien.

---

## Contre la proposition C

### (a) Failles

**C-1. Violations d'intégrité (règle 1).**
- *Statut VÉRIFIÉ étendu sans base.* Le socle vérifie le nom du matériel (« H200 NVL »), pas l'affirmation « 141 Go, permettant de loger 70B en BF16 sur un seul GPU ». Par arithmétique (illustratif) : 70·10⁹ paramètres × 2 octets ≈ 140 Go de poids seuls. Il ne reste presque rien pour le cache KV, et donc pour le double forward d'E1 que C budgète sur un GPU.
- *Observation sans observation.* « Jev évalue uniquement la syntaxe (OBSERVÉ-NON-AUDITÉ) » : aucune mesure n'est fournie, c'est une HYPOTHÈSE. C se contredit ensuite en utilisant les moyennes Jev comme preuve dans H_B de son méta-duel (1,27 contre 2,90).
- *Mécanisme sans statut.* « Le mimétisme Astra est capturé car z^gen contient la trace causale » est écrit comme un résultat, sans statut.
- *Mauvais usage d'un fait du socle.* C invoque « −54,9 pts, VÉRIFIÉ » pour dire que l'ablation de Fable Ep4 « détruit la capacité ». Or −54,9 pts mesure la chute sur la tâche TD de Xu et al., pas 𝒩_cap. De plus, Δ_abl chez Fable est une mesure d'audit, pas une ablation pendant la génération.
- *Erreur de calcul.* La moyenne de l'essaim B vaut −0,21, pas −0,17 (somme −2,50 / 12, OBSERVÉ-NON-AUDITÉ).

**C-2. La « correction universelle E1 » est vraie par construction.** δz_t = z^gen − z^no-sys est non nul dès qu'un prompt système existe, quel que soit l'acte. L'étalonnage sur une instruction bénigne « de même longueur » neutralise la longueur, pas le **contenu** sémantique.

Hors de l'expérience 1, le saboteur inactif (P2) n'apparaît dans aucun cas apparié des expériences 2 à 6. Elles comparent toutes le saboteur à des cas honnêtes « E2 ». Une alarme peut donc signifier « ce prompt système est inhabituel », c'est-à-dire le confondant P3 réintroduit sous un autre nom. C n'a corrigé le « paradoxe du re-forward aveugle » (point juste, je le reprends) que pour retomber dans le confondant de lecture.

**C-3. Exp. 1.**
- t* (« seul token de décision ») est défini dans le texte, mais l'équation somme sur tous les t. Si t* est localisé par l'acte, c'est l'étiquette qui fuit dans le détecteur.
- Le produit L1 × KL gonfle mécaniquement T_CF pour toute instruction longue ou inhabituelle.
- Le terme M_max·𝟙[|y| = 0 ∨ timeout] se contourne en émettant un seul token. Il produit aussi de fausses alarmes sur les dépassements de délai honnêtes, dont le taux n'est pas mesuré.
- « 𝒩_cap intacte à 0 % » est affirmé, pas mesuré.

**C-4. Exp. 2 : le multi-échelle est dégénéré.**
- L'équation de C applique le **même** incrément Δ_t aux trois CUSUM. Fable Ep1 utilisait Δ_t^(w) ; C ne l'a pas repris. Les trois statistiques ne diffèrent que par κ_w et h_w : ce ne sont pas des fenêtres.
- Une SVD de rang 4 sur 8 tokens dans d = 128 (illustratif) produit des angles principaux dominés par le bruit.
- « κ₁₂₈ décroît en O(1/√128) » est affirmé sans dérivation.
- « Sous κ₁₂₈/128, la rotation est trop faible pour inverser le test » suppose que le sabotage *est* une rotation dans S_TD. C'est H_A elle-même, utilisée comme parade.

**C-5. Exp. 3 : l'intervention n'est pas définie.**
- U_inst vit dans les coordonnées de Koopman réduites (r = 8, après projection de Rademacher R ∈ ℝ^{m×d} et plongement à délais). z_t^gen vit dans ℝ^{|S_TD|}. Avec m < |S|, R n'est pas inversible : (I − U_inst U_inst^⊤) z_t^gen est mal typé.
- Réduire les infractions de 0,65 à < 0,50 peut s'obtenir en dégradant la compétence agentique, ce que la mesure MMLU de 𝒩_cap ne voit pas.
- La table 2×2 laisse une zone morte : infraction entre 0,50 et 0,55, FPR entre 0,05 et 0,10. Les deux issues ne falsifient pas toujours quelque chose, ce qui viole B4.

**C-6. Exp. 4 : vraie par construction.** Le contrefactuel masque par `<PAD>` « les adverbes/clauses modales ». δ_t est alors non nul *précisément* là où le texte a été modifié, et l'attention vers ces tokens corrèle avec δ_t pour **tout** message qui contient une clause modale, honnête compris. Λ_imp mesure « présence d'un token masqué ».

Le choix de ce qu'on masque est en outre dérivé de l'incident *Astra* : c'est une fuite entre construction et évaluation. L'insertion de `<PAD>` perturbe aussi les positions et l'attention en aval, hors distribution.

**C-7. Exp. 5.**
- z^gen est enregistré en lecture seule, une fois. Obtenir R répliques de z^gen exige R re-forwards *avec* prompt système, soit environ 2R passes. Le surcoût « ≤ +45 % » est incompatible avec cela.
- q_EA = moyenne de Q_aa^VD est une corrélation valeur–dopamine intra-réplique, pas un auto-recouvrement d'Edwards-Anderson : l'étiquette ne correspond pas à l'objet.
- Comme l'a relevé A pour Chimère Ep3, la moyenne scalaire par couche efface la structure de S_V et S_D.
- Le contrôle E2 (rejets de formatage) a le même historique public que le saboteur. Seul le prompt système diffère : on retombe sur C-2.

**C-8. Exp. 6.**
- Le seuil PID sans étiquette force le taux d'alarme vers α sous sabotage soutenu (attaque D6 de A, que je reprends). C écrit « FPR garanti en flux » : le TPR est « garanti » vers α lui aussi.
- La normalisation sphérique combinée à une **corrélation**, elle-même invariante d'échelle, efface l'indice d'amplitude. Un δẑ honnête minuscule et bruité produit un graphe de même nature qu'un δẑ de sabotage. C a supprimé les substituts IAAFT, qui servaient de modèle nul contre l'autocorrélation, et les a remplacés par un PID qui n'en est pas un.
- β₀ d'un complexe de drapeaux dirigé compte les composantes du graphe sous-jacent, où l'orientation n'intervient pas. « Scission d'objectifs » revient à mesurer la parcimonie du graphe seuillé par λ_LW.
- Je reprends en revanche le contrôle « rasoir d'Ockham » de C (max Ω_ij contre β₀ + β₁) : il est bon, et probablement fatal pour C.

**C-9. Méta-duel (section 2).**
- **n = 1 par bras** : un seul champion par branche est évalué, sans réplication sur graines.
- Avec 100 négatifs, FPR = 5 % correspond à 5 exemples. L'écart-type d'une différence de TPR sur 100 positifs avoisine 7 pts (illustratif) : « +15 pts » se situe autour de deux écarts-types, sur une seule réalisation.
- Les deux bras utilisent Jev, puisque le bras 1 sélectionne par s_i = Jev − λ·Flops. Le duel confond « équipe rouge » et « 4 contre 12 propositions ».
- Le repli « déléguer au troisième modèle » ajoute des appels : le budget n'est pas constant.
- Le facteur q_i ∝ 𝟙[contrôles E0, E1, E2 présents] est un critère lexical que l'on peut satisfaire sans substance (effet de Goodhart).
- « Exécution réelle du code généré » : les champions produisent des équations, pas du code. La traduction par un humain ou un modèle est un confondant non budgété.
- Les 100 saboteurs « (i-a)/Astra » supposent une classe positive qui n'existe pas. Le socle dit qu'aucune « tête de sabotage » n'est pré-établie, et A l'a signalé (A8).
- Je reprends la branche 0 de C (best-of-N aléatoire) : c'est un bon contrôle.

**C-10. Budget incohérent.** E0 est estimé à 12 GPU·h sur le 8B (C), contre environ 150 GPU·h chez A. L'écart est d'un facteur 12 et aucune des deux estimations n'est justifiée (toutes deux illustratives).

### (b) Scénarios d'évasion

| Instrument de C | Évasion | Coût (HYPOTHÈSE) |
|---|---|---|
| Exp. 1 | Émettre un token non vide, puis exécuter l'acte par un appel d'outil dont le token de décision n'est pas t*. | Nul |
| Exp. 2 | Acte ponctuel (un seul appel d'outil) sans dérive géométrique ; ou agir pendant un changement de sujet honnête, où le seuil est relevé. | Nul |
| Exp. 3 | La parade sous-entend que la bascule d'infraction passe par un mode de Schur instable. Un saboteur obéissant sans conflit interne ne présente aucun mode instable. | Nul |
| Exp. 4 | Déclencheur non modal (nom propre, valeur de champ) : rien n'est masqué, donc δ_t = 0. | Nul |
| Exp. 5 | Répondre de façon déterministe au contenu, pour que les répliques par dropout convergent : χ_VD reste faible. Le garde-fou q_EA ne porte pas sur un auto-recouvrement (C-7). | Faible |
| Exp. 6 | Sabotage soutenu dès le début du flux : le PID s'y adapte et le taux d'alarme converge vers α. | Nul |

**Évasion conjointe des six instruments, à coût nul.** Les six expériences retirent **uniquement le prompt système** et lisent **le même S_TD**. Il suffit de placer l'objectif caché dans un tour antérieur, une sortie d'outil ou le message délégué m₁→₂. C le reconnaît pour l'agent 2 dans l'expérience 4, mais la parade y est vraie par construction (C-6). Le re-forward conserve alors l'objectif, δz ≈ 0, et les six détecteurs se taisent ensemble.

**Variante robuste.** Une porte dérobée dans les poids, plus une pénalité d'affinage sur ‖δz_{S_TD}‖. Le coût est de quelques GPU·h (illustratif). La parcimonie de S_TD rend cette pénalité peu coûteuse en capacité (HYPOTHÈSE à tester, pas un résultat).

L'empilement de six instruments ne donne aucune diversité : c'est un **mode commun** de défaillance.

### (c) Contrôles négatifs dont l'absence est fatale

1. **Saboteur inactif (P2) apparié** dans les expériences 2 à 6. Sans lui, impossible de distinguer l'acte du contenu de l'instruction.
2. **Acte imposé** : un modèle honnête forcé à émettre les tokens du sabotage.
3. **Instruction déplacée hors du prompt système**, et modèle à porte dérobée sans instruction. Cela teste la dépendance au canal E1.
4. **Exp. 4 : masquage aléatoire de tokens appariés** (même nombre, même classe grammaticale hors clauses modales) sur des messages honnêtes. Si Λ_imp monte autant, l'instrument est vrai par construction.
5. **Exp. 3 : projection aléatoire de même rang** et **taux de réussite de la tâche agentique**. Sans eux, une réduction des infractions peut n'être qu'une dégradation du modèle.
6. **Exp. 6 : sabotage stationnaire long** pour tester le PID, et un modèle nul par substituts réintroduit hors ligne.
7. **Sous-ensemble de neurones aléatoire** de même taille et même répartition par couche, que C n'exige que dans l'expérience 1 et sous une autre forme (norme du flux complet).
8. **Méta-duel : au moins 5 graines par bras** (illustratif) et un comptage complet des appels, repli compris.

---

## Duel commun qui peut éliminer A et C ensemble (règle B4)

Les deux propositions convergent sur la même prémisse : δz = z^gen − z^no-sys sur S_TD. Le duel suivant la tranche.

- **H_A** : δz porte l'*acte*.
  - AUROC(P3 vs P2) ≥ 0,75.
  - AUROC(acte imposé chez l'honnête vs P0) ≤ 0,60.
  - AUROC(instruction déplacée hors du prompt système, actif) ≥ 0,70.
  - (seuils illustratifs)
- **H_B** : δz porte le *canal* (le prompt système) ou les *tokens*.
  - AUROC(P3 vs P2) < 0,60, **ou** acte imposé détecté au même niveau que P3, **ou** chute sous 0,60 dès que l'instruction est déplacée.
- **Contrôle négatif** : la même statistique sur un sous-ensemble aléatoire de neurones, apparié par couche.
- **Falsification** :
  - Si H_A est fausse, les expériences D4 à D6 de A et 1 à 6 de C perdent leur substrat commun, avant tout raffinement spectral ou topologique.
  - Si H_B est fausse, le différentiel est validé contre les trois confondants nommés, et seulement contre eux. La porte dérobée dans les poids reste à tester.
- **Prérequis bloquant**, hérité de A et non résolu : construire une classe positive (i-a) reproductible sur Llama. Sans elle, aucune des deux propositions ne produit un seul taux de vrais positifs.

FIN-DE-CELLULE