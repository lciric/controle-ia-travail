# Proposition A — Tour III.1 (conception ciblée, à l'aveugle)

## 0. État des pièces

- **Bloc FAITS** : son contenu est mot pour mot celui de la question, sous la même empreinte déclarée (que je n'ai pas recalculée). Il ne contient aucun fait à statut, et je n'en invente pas.
- **Autres propositions (B à F)** : non transmises à ce tour, donc rien à critiquer ni à réutiliser.
- **« Test de devinette »** : nommé dans le titre, mais ni son protocole ni ses résultats ne sont transmis.

Convention, faute de statuts fournis : RAPPORTÉ désigne ce que l'énoncé affirme, HYPOTHÈSE ce qu'il sous-entend ou ce que j'ajoute. Rien ci-dessous n'est VÉRIFIÉ. Tous les seuils et effectifs sont illustratifs.

---

## (a) Ce que la question suppose sans que ce soit établi

| # | Présupposé | Statut | Ce qui le mettrait à l'épreuve |
|---|---|---|---|
| P1 | Aucune mesure n'est faite ; le texte ne peut donc porter aucun résultat. | RAPPORTÉ | Non auditable ici. Un pilote existant changerait D2. |
| P2 | Des travaux voisins paraissent. Leur recouvrement avec l'étude n'est pas dit. | RAPPORTÉ (parution) ; HYPOTHÈSE (recouvrement) | D4 |
| P3 | Un texte court sans résultat procure de la reconnaissance. | HYPOTHÈSE | D3 |
| P4 | Certaines mesures exigent une ignorance, et cette ignorance tient aujourd'hui. | RAPPORTÉ (exigence) ; HYPOTHÈSE (elle tient) | Contrôle négatif de D1 |
| P5 | On peut séparer ce qui doit rester caché de ce qui est publiable. | HYPOTHÈSE | D1 |
| P6 | Le régime pertinent est l'adversaire ignorant. Pour un dispositif destiné à servir, ce serait plutôt l'adversaire informé (Kerckhoffs, 1883, « La cryptographie militaire »). | HYPOTHÈSE, l'énoncé ne tranche pas | D2 |
| P7 | L'adversaire lit le texte et sait l'exploiter. L'énoncé ne dit pas si « l'adversaire » et « les systèmes à tenir ignorants » sont les mêmes. | HYPOTHÈSE | Contrôle positif de D2 |
| P8 | L'effet du texte sur la probabilité d'être devancé a un signe connu. Dissuasion et attraction sont toutes deux plausibles. | HYPOTHÈSE, non identifiable sur un seul cas | Seul le taux de base est mesurable (D4) |
| P9 | Trois options épuisent le choix. Deux manquent selon moi : l'engagement scellé daté (empreinte publique, contenu ouvert plus tard) et le texte scindé (partie publique, partie scellée). | HYPOTHÈSE | D3b |
| P10 | Des vérifications indépendantes peuvent dire que « le choix était le bon ». Le contrefactuel n'est pas observable ; seules des prédictions écrites d'avance sur les conséquences du choix sont vérifiables. | HYPOTHÈSE | Section (c), I3 |
| P11 | Le titre « billet-drapeau » suppose que la fonction du texte est de planter un drapeau. Ce cadrage subsiste malgré le correctif annoncé. | HYPOTHÈSE sur la fonction | D3 et D5 séparent antériorité, attention et qualité |

### Contenus possibles et effets attendus

Toutes les cases sont des HYPOTHÈSES, sauf mention « par construction ».

| Contenu | Reconnaissance | Devancement | Validité | Ce qu'apprend l'adversaire | Qualité et coût |
|---|---|---|---|---|---|
| **C1** Empreinte salée du protocole complet, horodatée | Antériorité prouvable à l'ouverture ; aucune attention | Nul | Nul, par construction (aléa ajouté, fonction résistante) | Rien, par construction | Oblige à écrire le protocole ; coût faible |
| **C2** Question et périmètre | Faible | Signe inconnu | Faible, si D1 passe | Que le sujet est travaillé | Retours externes possibles |
| **C3** Hypothèses, métriques, seuils, conditions de réfutation | Moyenne ; discipline visible | Signe inconnu ; plan réutilisable par un groupe plus rapide | À tester (D1) | Ce qui sera mesuré, donc quoi optimiser | Gain attendu contre la flexibilité d'analyse (Kerr, 1998, « HARKing: Hypothesizing After the Results are Known » ; Nosek, Ebersole, DeHaven, Mellor, 2018, « The preregistration revolution ») |
| **C4** Mécanisme du dispositif | Plus forte | Risque accru | Détruit le bras « adversaire naïf » pour tout lecteur | Le mécanisme | Critique externe du mécanisme |
| **C5** Éléments scellés (cas de test, déclencheurs, seuils opérationnels, identité des conditions) | Aucun gain | Sans objet | Destructeur, par définition de l'énoncé | Tout | Jamais avant la fin |

---

## (b) Expériences décisives

Elles sont ordonnées par réversibilité : tout ce qui se fait sans rien publier vient avant. Chaque duel a une zone d'indétermination déclarée d'avance (intervalle à cheval sur le seuil). Dans ce cas on augmente l'effectif, on ne conclut pas.

### D1 — Le texte candidat laisse-t-il deviner les éléments scellés ?

- **H_A** : le texte candidat T ne permet pas de retrouver les éléments scellés S mieux qu'un texte placebo.
- **H_B** : il le permet.
- **Protocole** :
  - S est transcrit en questions à choix fermé, de niveau de hasard connu (illustratif : 20 questions).
  - Les devineurs sont des modèles ouverts figés, exécutés hors ligne, et des personnes extérieures à l'équipe.
  - Trois bras : T ; T0, placebo de même longueur rédigé à partir des seuls travaux voisins publics ; T+, soit T avec une fuite plantée par un tiers.
- **Métrique** : excès d'exactitude de T sur T0, par élément.
- **Seuil** (illustratif) : H_A si la borne haute de l'intervalle à 95 % est sous 5 points ; H_B si la borne basse est au-dessus de 0.
- **Contrôle négatif** : T0. S'il dépasse nettement le hasard, le secret est déjà devinable depuis le domaine public. P4 tombe alors, texte ou pas.
- **Contrôle positif** : T+ doit être repéré. Sinon le test est sans puissance et aucune conclusion n'est permise.
- **Falsification** : l'issue H_A réfute « tout texte public contamine ». L'issue H_B réfute « ce texte est sûr », et il faut réécrire ou se limiter à C1.

### D2 — Adversaire informé contre adversaire naïf

- **H_A** (robustesse) : à fausses alertes fixées, le taux de détection ne baisse pas de plus de δ quand l'adversaire dispose de T, puis de T et du mécanisme M.
- **H_B** : il baisse de plus de δ.
- **Protocole** :
  - Quatre bras à budget d'attaque égal : naïf, T0, T, T+M.
  - Les attaquants sont des modèles ouverts figés.
  - Les cas honnêtes appariés sont communs aux quatre bras.
  - Le seuil de décision est fixé une fois, sur les seuls cas honnêtes, avant de voir une attaque.
- **Métrique** : écart de taux de détection à 1 % de fausses alertes (illustratif), avec δ = 10 points (illustratif) et un test d'équivalence.
- **Contrôle négatif** : T0 contre naïf doit donner un écart nul. Sinon c'est l'ajout de contexte qui change l'attaquant, pas l'information.
- **Contrôle positif** : un attaquant en boîte blanche (scores et seuil fournis) doit faire baisser la détection. Sinon l'attaquant est trop faible pour départager quoi que ce soit, travers documenté par Tramèr, Carlini, Brendel, Madry (2020), « On Adaptive Attacks to Adversarial Example Defenses ».
- **Falsification** : l'issue H_A réfute « la validité exige l'ignorance de T ou de M », et l'argument de validité pour « publier après » tombe pour ce contenu. L'issue H_B réfute la robustesse. La portée du dispositif se réduit à l'adversaire naïf et C4 ne peut pas précéder les mesures. C'est déjà un résultat de l'étude.
- **Contrainte d'ordre** : avec des modèles figés, le bras naïf est renouvelable. Avec des personnes, il ne l'est pas et doit être recueilli avant toute publication.

### D3 — Reconnaissance : note publique, engagement scellé ou rien

Le protocole est une vignette randomisée. Les évaluateurs sont des chercheurs du domaine, extérieurs à l'équipe et aveugles au but. Dans le cas fictif, un groupe rival publie ses résultats le premier. L'équipe X avait soit rien, soit une empreinte ouverte après coup, soit une note publique.

- **Duel 3a**
  - H_A : un texte daté sans résultat augmente l'attribution d'antériorité à X.
  - H_B : il ne l'augmente pas, le crédit suit les résultats.
- **Duel 3b**
  - H_A′ : la note publique fait mieux que l'empreinte, parce que c'est l'attention qui compte.
  - H_B′ : elles sont équivalentes, parce que seule la date compte.
- **Métrique** : proportion qui attribue l'origine à X, et note de nouveauté accordée à l'article de X.
- **Seuil** (illustratif) : 15 points d'écart, environ 150 évaluateurs par bras ou un plan intra-sujet. La puissance est à recalculer.
- **Contrôle négatif** : une note de même date sur un sujet sans rapport doit valoir « rien ».
- **Falsification** : H_B réfute l'argument de reconnaissance pour « publier avant ». H_B′ réfute la nécessité d'un texte public, puisque l'engagement scellé donne alors le même crédit sans fuite. H_A′ réfute l'idée que C1 suffit.
- **Limite** : on mesure une attribution déclarée, pas un comportement de citation. Les travaux empiriques sur les courses à la priorité sont une référence à vérifier. Le cadre conceptuel est celui de Merton (1957), « Priorities in Scientific Discovery ».

### D4 — Taux de base du devancement

- **H_A** : la probabilité qu'un travail recouvrant paraisse pendant la durée prévue de l'étude atteint p* (illustratif : 20 %).
- **H_B** : elle est inférieure à p*.
- **Protocole** : une grille de recouvrement est écrite d'avance (même classe de dispositif, même classe d'adversaire, même métrique principale). Deux codeurs extérieurs l'appliquent aux parutions des 12 derniers mois (illustratif). On en tire un taux, puis la probabilité d'au moins une parution sur la durée de l'étude.
- **Contrôle négatif** : la même grille est appliquée à un protocole leurre d'un thème voisin. Si elle « trouve » autant de recouvrements, elle mesure la mode du sujet et non le recouvrement.
- **Falsification** : H_B réfute le motif d'urgence. H_A réfute « attendre ne coûte rien ».
- **Limite** : D4 ne mesure pas l'effet causal de la note sur le devancement. Sur un cas unique, cet effet reste une HYPOTHÈSE.

### D5 — Qualité : une relecture scellée suffit-elle ?

- **H_A** : deux ou trois relecteurs externes sous confidentialité trouvent les défauts d'un protocole.
- **H_B** : ils ne les trouvent pas.
- **Protocole** : un tiers plante k défauts connus dans une copie du protocole (fuite d'information, seuil choisi après coup, contrôle manquant).
- **Métrique** : part des défauts plantés retrouvés (seuil illustratif : 70 %) et fausses alertes sur les sections saines.
- **Contrôle négatif** : une copie sans défaut planté.
- **Falsification** : H_A réfute l'avantage exclusif de « publier avant » sur la qualité, car la critique s'obtient alors sans fuite. H_B réfute « ne rien rendre public est sans coût pour la qualité ».

---

## (c) Mesure minimale par instrument nommé

**I1 — Le dispositif de détection.**
- *Cas positifs* : productions de l'adversaire.
- *Cas honnêtes appariés* : même tâche, même système producteur, même longueur, même période, sans consigne adverse.
- *Mesure* : taux de détection à fausses alertes fixées, avec intervalle. Pour borner les fausses alertes à 1 %, il faut au moins 300 cas honnêtes sans aucune alerte (règle de trois ; effectif illustratif).
- *Vérifications mécaniques à battre* : seuil de longueur, mots-clés ou expressions régulières, perplexité sous un petit modèle ouvert, régression logistique sur sac de mots. S'y ajoute un classifieur « quel système a produit le cas », pour écarter l'hypothèse que le dispositif détecte la provenance plutôt que le comportement adverse.
- *Verdict* : sans gain net sur la meilleure de ces lignes de base, le dispositif n'est pas démontré.

**I2 — Le texte court, comme preuve d'antériorité.** La variante scellée est un ajout de ma part.
- *Cas* : paires (engagement, rapport final). Un tiers fabrique des rapports déviants (métrique principale changée, seuil déplacé, condition retirée) et des rapports fidèles appariés, avec leurs écarts déclarés.
- *Mesure* : un auditeur externe doit signaler au moins 90 % des déviations, avec au plus 10 % de fausses alertes (illustratifs).
- *Vérifications mécaniques à battre* : contrôle d'empreinte (il prouve l'intégrité du document, pas la concordance entre plan et rapport), différence textuelle des sections « métriques et seuils », liste de contrôle.
- *Faille à tester* : l'engagement multiple, soit déposer plusieurs protocoles et n'ouvrir que le bon. La parade est un dépôt unique chez un tiers. On vérifie qu'un double dépôt planté est bien détecté.

**I3 — Les vérifications indépendantes de l'équipe.** Elles ne peuvent pas établir que « le choix était le bon » (P10). Elles peuvent établir que les conséquences prédites par écrit se sont réalisées.
- V1 : intégrité et date de l'engagement (mécanique).
- V2 : unicité du dépôt (tiers).
- V3 : concordance entre plan et rapport (auditeur, calibré comme I2).
- V4 : absence de fuite. Questionnaire de devinette en sortie pour les participants aveugles, comparé au hasard. Test de chaîne-canari sur les systèmes utilisés (pratique existante, référence à vérifier).
- V5 : reproduction du résultat principal par un tiers détenteur du jeu scellé.
- V6 : recodage a posteriori des parutions voisines avec la grille de D4.

Chaque vérificateur est lui-même mesuré par son taux de détection sur violations plantées et ses fausses alertes sur cas propres. Un vérificateur qui n'a jamais vu de violation plantée n'a pas de sensibilité connue.

**I4 — Le « test de devinette ».** Il est nommé dans le titre et son contenu n'est pas transmis. Ma lecture, celle de D1, est une HYPOTHÈSE.
- *Détection* : part des fuites plantées (T+) signalées.
- *Fausses alertes* : part des placebos (T0) signalés.
- *Vérifications mécaniques à battre* : recouvrement lexical entre T et la liste S, recherche des chaînes scellées par expression régulière, similarité de plongements. Si les devineurs ne font pas mieux, le test n'ajoute rien à une recherche de motifs.

---

## (d) Ancrage matériel

Tout ce qui suit est illustratif : rien ne vient des faits.

- **Modèles** : familles à poids ouverts de type Llama, Mistral, Qwen ou Gemma. Les versions, licences et dates de gel sont à vérifier. Un instantané de poids publié avant la date du texte ne peut pas l'avoir appris, par simple chronologie. Cela suppose de contrôler l'empreinte des poids et de l'exécuter hors ligne, sans outil de recherche. L'exigence d'ignorance des « systèmes » est donc satisfiable mécaniquement pour ces modèles. Elle ne l'est pas pour des personnes, pour des modèles servis par interface et mis à jour, ni pour les modèles futurs.
- **Horodatage** : empreinte SHA-256 avec aléa, ancrée par un service d'horodatage public ou un dépôt de préenregistrement sous embargo. Les modalités sont à vérifier ; le coût est à peu près nul.

| Expérience | Calcul et moyens | Coût |
|---|---|---|
| D1 | Quelques milliers de générations courtes, une carte graphique pendant quelques heures, dix devineurs humains | Moins de 100 € |
| D2 | 4 bras × 300 attaques × 2 ou 3 attaquants, 1 000 cas honnêtes ; 20 à 100 heures sur une carte de 24 à 48 Go, modèles quantifiés | 50 à 400 € |
| D3 | 60 à 450 évaluateurs du domaine. Le recrutement est le vrai verrou. | 700 à 2 000 € |
| D4 | Deux codeurs, une journée chacun | Temps de travail |
| D5 | Deux ou trois relecteurs, une demi-journée chacun | Temps de travail |

D1, D2 (modèles figés), D4 et D5 se font sans rien publier, en une à deux semaines.

---

## (e) Arguments, choix, conditions de révision

Ce choix est un raisonnement sur des hypothèses, pas un résultat.

- **Publier avant, argument le plus fort.** Un dispositif qui doit servir affrontera un adversaire informé. Cacher le mécanisme ne fait que différer la seule épreuve qui compte. L'engagement public discipline aussi l'analyse et expose le protocole à la critique avant que le budget soit dépensé.
- **Publier après, argument le plus fort.** La publication est irréversible, alors que l'ignorance des personnes ne se reconstitue pas. Sans mesure, le texte n'atteste qu'une intention. Attendre conserve toutes les options.
- **Ne rien publier, argument le plus fort.** Si D2 conclut à H_B et que le dispositif n'a de valeur qu'opérationnelle, tout texte, même tardif, est surtout un manuel d'évitement. Le coût est un résultat nul qui reste au tiroir.

**Mon choix : une quatrième voie, séquencée.**
1. Maintenant : engagement scellé C1 du protocole complet, en dépôt unique chez un tiers.
2. Sans rien publier : D1 sur le brouillon du texte, D5, D4, puis le bras naïf de D2.
3. Texte public limité à C2 et C3, seulement si D1 conclut à H_A.
4. C4 seulement après le bras naïf, ou avant si D2 conclut à H_A.
5. C5 jamais avant la fin.

**Ce qui me ferait changer.**
- D1 conclut à H_B malgré une réécriture : C1 seul, aucun texte public.
- D3b conclut à H_A′ et D4 à H_A : j'avance le texte public C2 et C3, en acceptant le risque mesuré.
- D2 conclut à H_A : C4 passe avant.
- D5 conclut à H_B : le coût de qualité du silence devient réel et plaide pour une exposition publique plus tôt.
- P1 est faux (des mesures existent déjà) : le texte doit le dire, et l'engagement n'a plus valeur de préenregistrement pour ces mesures.

**Compte de ce qui peut être réfuté.** Six duels (D1, D2, D3a, D3b, D4, D5), soit douze issues qui falsifient chacune un énoncé nommé, plus quatre instruments dont la sensibilité est mesurable sur des cas plantés. L'effet causal de la note sur le devancement (P8) n'est pas réfutable sur un seul cas.

FIN-DE-CELLULE