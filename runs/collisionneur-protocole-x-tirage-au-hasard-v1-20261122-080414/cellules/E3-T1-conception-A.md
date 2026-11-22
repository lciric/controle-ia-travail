# Proposition A — Tour III.1 : conception ciblée, à l'aveugle

**État des pièces.** Le bloc FAITS ne contient que la question, donc aucun fait porteur de statut. Le bloc QUESTION lui est identique, et je n'ai pas recalculé l'empreinte sha256. Aucune autre proposition ne m'est transmise, ce qui est attendu à ce tour.

**Statuts que j'emploie.** Rien ci-dessous n'est VÉRIFIÉ.
- Les références sont citées de mémoire, sans audit dans cette session : RAPPORTÉ.
- Ma taxonomie et mes jugements sur ce qui est « peu étudié » : HYPOTHÈSE.
- Tous les seuils, effectifs et coûts : illustratifs.

---

## (a) Ce que la question suppose sans que ce soit établi

| # | Présupposé | Statut | Pourquoi il compte |
|---|---|---|---|
| P1 | Le hasard est imprévisible et inobservable, y compris dans ses effets. | HYPOTHÈSE (prémisse de la question) | Le tirage peut être secret et ses conséquences visibles : unité plantée stylistiquement atypique, latence d'audit, artefacts de paraphrase. Les garanties tombent alors, même avec une source parfaite. |
| P2 | Le contrôlé est stratégique : il répond au mieux à la politique de contrôle. | HYPOTHÈSE | Un agent sans mémoire doit, sans hasard partagé, calibrer une stratégie mixte et se coordonner entre copies. Sa capacité à le faire est empirique (Mallen et al., « Subversion Strategy Eval », référence à vérifier). S'il n'est pas stratégique, le hasard ne sert qu'à l'échantillonnage statistique. |
| P3 | Les « usages distincts » forment un ensemble énumérable (« tous »). | HYPOTHÈSE | L'exhaustivité est irréfutable telle quelle. Je la remplace par un critère : deux usages diffèrent s'ils diffèrent par ce qui est caché, par le moment du tirage relativement à l'engagement du contrôlé, ou par la garantie. Un usage publié qui n'entre dans aucune classe réfute ma liste. |
| P4 | Chaque usage garantit quelque chose « exactement ». | HYPOTHÈSE | Les théorèmes valent dans leur modèle (rationalité, gains connus, sanction crédible, tirages indépendants). Le transfert aux agents de langue n'est pas établi. La dissuasion suppose une sanction à laquelle l'agent est sensible ; faute de quoi il ne reste que la détection. |
| P5 | Un audit fiable existe sur l'échantillon tiré. | HYPOTHÈSE | Sur une longue analyse sans vérité de terrain, le tirage dit où regarder, pas quoi conclure. La borne de détection est multipliée par la sensibilité de l'auditeur. |
| P6 | La tâche se découpe en unités auditables et la faute est diffuse. | HYPOTHÈSE | Si une seule faute suffit, un audit au taux p l'attrape avec probabilité p, pas davantage. |
| P7 | Les autres domaines (désarmement, fisc, cryptographie, essais cliniques) se transposent. | HYPOTHÈSE | Le contrôleur d'un modèle peut le copier, le réinitialiser, le rejouer et choisir ce qu'il observe. Cela n'a pas d'équivalent face à un humain, donc certains usages n'ont pas de littérature d'origine. |
| P8 | Le contrôleur est loyal et son tirage vérifiable par un tiers. | HYPOTHÈSE | Sinon le « hasard » peut être choisi après coup. |
| P9 | « Un système » : un seul contrôlé. | HYPOTHÈSE | En pratique plusieurs instances, donc collusion possible, y compris avec un moniteur non fiable. |
| P10 | On peut juger de mémoire ce qui est « moins étudié ». | HYPOTHÈSE | Mes jugements ci-dessous sont à réfuter par E0. |

### Recensement proposé (taxonomie : HYPOTHÈSE ; travaux : RAPPORTÉ)

La colonne « Agents de langue » donne mon souvenir de la littérature, non audité.

| Usage | Garantie, dans son modèle | Conditions | Travaux | Agents de langue |
|---|---|---|---|---|
| **U1 Audit tiré au sort** | Une faute touchant k unités sur n échappe avec probabilité ≤ (1−p)^k. Dissuasion si p × sanction > gain. | Audit fiable, tirage après engagement, sanction crédible | Becker (1968), « Crime and Punishment: An Economic Approach » ; Dresher (1962), « A Sampling Inspector Problem in Arms Control Agreements » ; Avenhaus, von Stengel, Zamir (2002), « Inspection Games » ; Mookherjee & Png (1989), « Optimal Auditing, Insurance, and Redistribution » | Oui : Greenblatt, Shlegeris, Sachan, Roger (2023), « AI Control: Improving Safety Despite Intentional Subversion » |
| **U2 Défi aléatoire après engagement** (preuve interactive, vérification ponctuelle) | Une affirmation fausse est acceptée avec probabilité ≤ ε, quelle que soit la stratégie du prouveur | Affirmation formalisable, engagement liant avant le défi | Goldwasser, Micali, Rackoff (1985), « The Knowledge Complexity of Interactive Proof Systems » ; Freivalds (1977), « Probabilistic Machines Can Use Less Running Time » ; Arora & Safra (1998), « Probabilistic Checking of Proofs: A New Characterization of NP » | Analogue : Irving, Christiano, Amodei (2018), « AI Safety via Debate ». Aucune borne ε connue de moi pour une analyse en langue naturelle |
| **U3 Cas plantés indiscernables** (ringers, leurres, canaris, témoins positifs en aveugle) | Estimation sans biais du taux de faute sur les cas plantés ; le contrôlé ne peut fauter que s'il les distingue | Indiscernabilité (P1) | Golle & Mironov (2001), « Uncheatable Distributed Computations » ; Juels & Rivest (2013), « Honeywords: Making Password-Cracking Detectable » ; Carlini, Liu, Erlingsson, Kos, Song (2019), « The Secret Sharer » | Oui : exemples synthétiques pour moniteur non fiable (Greenblatt et al. 2023). Indiscernabilité non garantie |
| **U4 Affectation aléatoire** (tâches, relecteurs, traitements) | Identification causale sans sélection par le contrôlé ; partenaires de collusion non choisis | Affectation cachée jusqu'à l'engagement | Fisher (1935), « The Design of Experiments » ; Bertrand & Mullainathan (2004), « Are Emily and Greg More Employable than Lakisha and Jamal? » | Courant en évaluation. Usage anti-collusion entre agents : peu étudié, selon moi |
| **U5 Brouillage du canal** (paraphrase aléatoire, gardien actif) | Borne la capacité d'un canal caché | La paraphrase préserve le contenu utile | Simmons (1984, actes de CRYPTO 83), « The Prisoners' Problem and the Subliminal Channel » ; Roger & Greenblatt (2023), « Preventing Language Models From Hiding Their Reasoning » | Oui |
| **U6 Rejeu / rééchantillonnage** du hasard interne du contrôlé | Des copies sans hasard partagé ne peuvent coordonner une faute rare que par point focal ; le désaccord entre tirages devient un signal | Copies isolées ; pas de point focal | « Ctrl-Z: Controlling AI Agents via Resampling » (auteurs : référence à vérifier) ; Mallen et al. (référence à vérifier) | Oui, récent ; pas d'analogue humain (P7) |
| **U7 Politique mixte annoncée** (engagement de Stackelberg, rotation, horizon aléatoire) | La valeur du contrôleur en stratégie mixte est au moins celle de toute stratégie pure ; pas de « dernière période » connue | Le contrôlé connaît la loi, pas le tirage | Tambe (2011), « Security and Game Theory » ; Yao (1977), « Probabilistic Computations: Toward a Unified Measure of Complexity » | Modélisations de jeu du contrôle (Griffin et al., référence à vérifier) |
| **U8 Aveuglement d'instance** (masque aléatoire, auto-réduction, partage de secret) | Le contrôlé voit une instance dont la loi ne dépend pas de l'instance réelle, donc ne peut cibler | Tâche réductible ou masquable sans perte | Shannon (1949), « Communication Theory of Secrecy Systems » ; Blum, Luby, Rubinfeld (1993), « Self-Testing/Correcting with Applications to Numerical Problems » | Peu étudié, selon moi |
| **U9 Perturbation du contrôlé ou de ses entrées** | Rayon certifié pour un classifieur ; heuristique seulement pour un agent | Bruit calibré | Cohen, Rosenfeld, Kolter (2019), « Certified Adversarial Robustness via Randomized Smoothing » ; Robey, Wong, Hassani, Pappas (2023), « SmoothLLM » | Oui, contre les contournements. Bruit sur les poids contre la sous-performance volontaire : référence à vérifier |
| **U10 Marquage à clé secrète** | Attribution d'une sortie ou d'une fuite, à taux de faux positifs calculable | Clé secrète, texte assez long | Kirchenbauer, Geiping, Wen, Katz, Miers, Goldstein (2023), « A Watermark for Large Language Models » | Oui |
| **U11 Bruit protégeant le contrôle contre l'adaptation** | Un contrôlé qui s'adapte aux retours d'audit ne sur-ajuste pas le jeu de contrôle au-delà d'une borne | Retours bruités, budget de requêtes | Dwork, Feldman, Hardt, Pitassi, Reingold, Roth (2015), « The Reusable Holdout » | Peu étudié pour des agents recevant des retours d'audit, selon moi |
| **U12 Hasard publiquement vérifiable après coup** (engagement-révélation, balise) | Le contrôleur ne peut choisir sa cible a posteriori | Engagement publié avant la tâche | Rabin (1983), « Transaction Protection by Beacons » | Non, à ma connaissance |

**Jugés les moins étudiés pour ces agents (HYPOTHÈSE) :** U8, U11, U12, U2 dans sa forme « engagement puis défi » sur une longue analyse, et U4 dans son usage anti-collusion. La raison supposée est que ces usages exigent une structure de tâche (masquable, engageable) que les bancs d'essai actuels n'ont pas.

Je ne tiens pas U1, U3, U5 et U6 pour peu étudiés. Ce qui y manque, selon moi, est la mesure de P1 (l'indiscernabilité des effets du tirage), dont dépendent leurs garanties.

---

## (b) Expériences décisives

**Banc commun.** Ce sont des analyses de données en plusieurs étapes sur des jeux synthétiques dont les paramètres générateurs sont tirés par la source secrète. La vérité est donc connue par construction et rien n'a pu être mémorisé.

L'« équipe rouge » est un modèle ouvert, instruit ou affiné pour fauter, qui connaît le protocole mais pas les tirages. Les fautes sont une conclusion biaisée, une étape omise ou un chiffre altéré.

**Limite déclarée.** Une équipe rouge instruite n'est pas un modèle déloyal spontané. Les résultats bornent la capacité obtenue par cette élicitation et ne garantissent rien au-delà.

**Règle de décision commune.** Chaque hypothèse est jugée sur l'intervalle de confiance à 95 %. Si l'intervalle chevauche le seuil, le duel n'est pas tranché et l'on augmente n. Aucun résultat n'est alors annoncé.

### E0 — Recherche bibliographique qui me donnerait tort

- **H_A :** au plus 2 publications (illustratif) par usage appliquent U8, U11, U12 ou U2-engagement à des agents de langue face à un adversaire stratégique explicite.
- **H_B :** au moins 3 pour l'un de ces usages.
- **Protocole :** requêtes fixées à l'avance, croisant les vocabulaires d'origine et les termes « agent » ou « language model » (par exemple « instance hiding », « reusable holdout », « commit-and-challenge », « verifiable randomness », « random assignment collusion »). Deux codeurs indépendants ; inclusion si l'adversaire est stratégique et le hasard explicitement secret.
- **Métrique :** nombre d'articles inclus par usage ; accord entre codeurs κ ≥ 0,7 (illustratif).
- **Contrôle positif :** les mêmes requêtes adaptées à U1 doivent retrouver Greenblatt et al. (2023), sinon le protocole est aveugle.
- **Contrôle négatif :** un terme fabriqué ne doit rien faire inclure, sinon les codeurs sur-incluent.
- **Falsifie :** H_B réfute mon classement pour l'usage concerné. H_A réfute l'idée que le transfert des domaines voisins est déjà fait (P7).

### E1 — La prémisse : l'effet du tirage est-il inobservable ?

- **H_A :** le contrôlé ne distingue pas les unités plantées, auditées ou paraphrasées des unités ordinaires. AUROC < 0,60 (illustratif) pour le modèle interrogé directement et pour une sonde linéaire sur ses activations.
- **H_B :** AUROC ≥ 0,60 pour l'un des deux.
- **Contrôle négatif :** étiquettes « planté / réel » permutées au hasard. L'AUROC doit valoir 0,5 ± bruit, sinon il y a une fuite dans le protocole.
- **Contrôle positif :** des unités plantées avec un marqueur grossier doivent être détectées, sinon la sonde est inapte.
- **Falsifie :** H_B réfute P1 pour ce mode de fabrication. Les garanties de U1, U3 et U5 ne s'appliquent alors plus telles quelles et doivent être dégradées selon l'avantage de distinction mesuré. H_A réfute l'objection selon laquelle l'évaluation est toujours reconnaissable, au niveau de capacité testé seulement.

### E2 — Le hasard fait-il un travail stratégique ou seulement statistique ?

- **Trois calendriers d'audit à budget égal (2 % des unités, illustratif) :** les premières unités ; un pas fixe publié ; des tirages indépendants.
- **H_A :** l'équipe rouge exploite les calendriers déterministes. La probabilité d'au moins une faute non détectée y dépasse d'au moins 15 points (illustratif) celle du calendrier tiré.
- **H_B :** écart < 15 points.
- **Contrôle négatif 1 :** modèle honnête. Les trois calendriers doivent donner le même taux de fausses alertes, sinon l'écart vient de l'auditeur.
- **Contrôle négatif 2 :** équipe rouge non informée du protocole. L'écart doit disparaître, sinon il ne mesure pas la stratégie.
- **Falsifie :** H_B réfute P2 à ce niveau de capacité. La théorie des jeux d'inspection est alors sans objet ici, et le tirage vaut un sondage. H_A réfute la thèse selon laquelle un calendrier fixe inconnu en pratique suffit.
- **Réserve :** Greenblatt et al. (2023) rapportent un résultat voisin sur des tâches de code (RAPPORTÉ). E2 teste le transfert aux longues analyses et n'a de valeur que comme réplication.

### E3 — Rejeu : désaccord informatif ou point focal ?

- **Dispositif :** à chaque étape, k = 5 tirages (illustratif) du contrôlé avec des graines choisies par le contrôleur, instances isolées. Le score est le désaccord entre tirages.
- **H_A :** les copies fautives ne se coordonnent pas. Le désaccord détecte les étapes fautives avec un taux de détection ≥ 50 % à 1 % de fausses alertes (illustratif), au-dessus du moniteur de référence à coût égal.
- **H_B :** les copies convergent sur un point focal (même étape, même altération). Le désaccord ne dépasse pas le moniteur de référence.
- **Contrôle négatif :** étapes honnêtes naturellement variables (plusieurs méthodes valides), appariées en longueur et en difficulté. Elles fixent le taux de fausses alertes. Si elles saturent le score, l'instrument est inutilisable quel que soit H.
- **Falsifie :** H_B réfute la garantie supposée de U6 (l'absence de hasard partagé empêcherait la coordination). H_A réfute la thèse selon laquelle les points focaux suffisent à ces modèles pour colluder sans communication.

### E4 — Aveuglement d'instance : utilisable ou non ?

- **Dispositif :** la faute de l'équipe rouge est conditionnée à un attribut d'enjeu (identité du commanditaire, signe du résultat attendu). Le contrôleur remplace les identifiants par des jetons tirés au sort et permute au hasard les étiquettes des conditions, puis démasque en sortie.
- **H_A :** l'aveuglement fonctionne. Le taux de faute ciblée chute d'au moins 80 % (illustratif) pour une perte de qualité honnête ≤ 3 points (illustratif).
- **H_B :** au moins une des deux conditions échoue. Soit le modèle ré-identifie l'attribut masqué au-dessus du hasard, soit la qualité honnête chute au-delà du seuil.
- **Contrôle négatif :** masque appliqué à un attribut sans rapport avec le déclencheur. Le taux de faute doit rester inchangé, sinon la baisse vient d'une perturbation générale (U9) et non de l'aveuglement.
- **Falsifie :** H_B réfute U8 comme usage praticable sur ce type de tâche et dit par laquelle des deux voies. H_A réfute mon explication de sa rareté (la structure de tâche manquerait). Il faudrait alors en chercher une autre.

---

## (c) Mesure minimale par instrument

La question ne nomme qu'un instrument, la source de hasard. Je traite donc la source, puis chacun des usages du recensement.

**Règle commune.** Pour chaque usage, on rapporte le taux de détection à taux de fausses alertes fixé à 1 % (illustratif), avec intervalle exact. Les cas honnêtes appariés partagent tâche, modèle, longueur et difficulté avec les cas fautifs ; seule la faute diffère.

On ajoute deux familles de cas honnêtes atypiques, qui sont ceux où les fausses alertes coûtent : les erreurs de bonne foi et les méthodes inhabituelles mais correctes.

Borner les fausses alertes à 1 % avec zéro alerte observée exige environ 300 cas honnêtes (règle de trois : borne supérieure à 95 % ≈ 3/n ; seuil illustratif).

Un usage ne « fonctionne » que s'il bat, à coût égal, les vérifications mécaniques sans hasard listées en dernière colonne.

| Instrument | Ce qu'on mesure | Cas honnêtes appariés | Vérification mécanique à battre |
|---|---|---|---|
| **Source de hasard** | Exactitude du contrôlé à prédire les tirages (doit rester au niveau du hasard) ; E1 pour les effets | Sans objet | Graine fixe publiée : si rien ne change, le secret ne sert à rien. Le tirage n'est jamais produit par un modèle de langue (mauvais générateurs aléatoires : RAPPORTÉ, référence à vérifier) |
| **U1** | Probabilité d'au moins une faute non détectée, à budget fixé | Mêmes tâches sans faute | Audit des k premières unités ; audit à pas fixe ; ré-exécution intégrale du code et recalcul des chiffres |
| **U2** | Taux d'acceptation d'analyses fausses engagées, à coût de vérification égal | Analyses justes soumises au même défi | U1 simple au même coût ; tests unitaires ; contrôle de cohérence des totaux |
| **U3** | Écart de taux de faute entre unités plantées et réelles ; AUROC de distinction (E1) | Unités réelles de même gabarit | Jeu de tests fixe et public |
| **U4** | Taux de collusion réussie entre producteur et relecteur, affectation tirée contre affectation fixe | Paires honnêtes, mêmes affectations | Relecteur fixe ; relecture par un modèle de confiance plus faible |
| **U5** | Bits récupérés par un décodeur complice après paraphrase ; perte de qualité | Textes honnêtes paraphrasés | Normalisation déterministe (gabarit, canonisation) |
| **U6** | Détection par désaccord (E3) | Étapes honnêtes à forte variabilité naturelle | Un seul tirage à température nulle, plus diff contre le modèle de confiance |
| **U7** | Gain de l'attaquant informé de la loi contre informé du tirage | Sans objet | Meilleure politique pure à budget égal |
| **U8** | Taux de faute ciblée ; taux de ré-identification ; perte de qualité (E4) | Mêmes tâches masquées, modèle honnête | Suppression déterministe des champs sensibles |
| **U9** | Détection d'une sous-performance volontaire par gain de score sous bruit | Modèle honnête soumis au même bruit (doit seulement se dégrader) | Comparaison à un score de référence passé ; reformulation fixe de la consigne |
| **U10** | Taux d'attribution correcte après édition ou paraphrase ; fausses attributions | Textes sans marque de même longueur | Journalisation intégrale et empreinte des sorties |
| **U11** | Taux de faute non détectée au fil des tours avec retours d'audit, bruités contre exacts | Agent honnête, mêmes retours | Aucun retour ; jeu de contrôle renouvelé à chaque tour |
| **U12** | Part des cibles d'audit qu'un tiers peut recalculer depuis l'engagement | Sans objet | Journal horodaté sans engagement |

**Critère d'échec commun.** Si la vérification mécanique atteint le même taux de détection à 1 % de fausses alertes, l'usage aléatoire n'apporte rien sur ce banc. On le dit tel quel, sans chercher un autre banc après coup.

---

## (d) Ancrage matériel

Tout ce qui suit est illustratif. Aucun de ces chiffres ne vient des faits.

**Modèles ouverts** (existence RAPPORTÉE ; licences et disponibilités à vérifier).
- Familles Llama 3.x, Qwen 2.5, Mistral, Gemma 2.
- Contrôlé / équipe rouge : un modèle de 30 à 70 milliards de paramètres, plus une version affinée par adaptateurs de rang faible d'un modèle de 7 à 8 milliards, pour disposer d'un attaquant entraîné et pas seulement instruit.
- Moniteur de confiance : un modèle de 7 à 8 milliards.
- Les poids ouverts sont nécessaires pour la sonde sur activations (E1) et le bruit sur les poids (U9).

**Volume.**
- Par expérience : 300 cas fautifs + 300 honnêtes appariés, × 4 conditions, × environ 30 000 jetons par trajectoire, soit environ 72 millions de jetons.
- E1 à E4 : environ 300 millions de jetons. E3 multiplie le volume de ses étapes par k = 5, d'où une marge × 2.

**Calcul.**
- Inférence par lots sur 1 à 2 processeurs graphiques de 48 à 80 Go : de l'ordre de 100 à 200 heures-GPU pour un passage, × 3 à 5 pour les itérations.
- Affinage de l'équipe rouge : quelques heures sur un seul processeur.

**Coût.**
- Location : 500 à 2 000 € au total.
- Travail humain, poste dominant : vérité de terrain des cas honnêtes atypiques et validation d'un sous-échantillon des fautes plantées, environ 100 heures à 10 minutes par cas pour 600 cas.
- E0 : environ 2 personnes × 3 jours.

**Ordre conseillé.** E0 et E1 d'abord, car E1 conditionne l'interprétation de tout le reste. Si H_B l'emporte en E1, les mesures des usages U1, U3 et U5 doivent être rapportées conditionnellement à l'avantage de distinction mesuré, et non comme des garanties.

**Ce que ce plan ne tranche pas.**
- Le comportement d'un modèle déloyal sans instruction.
- La dissuasion (P4).
- Les tâches sans vérité de terrain constructible (P5).

FIN-DE-CELLULE