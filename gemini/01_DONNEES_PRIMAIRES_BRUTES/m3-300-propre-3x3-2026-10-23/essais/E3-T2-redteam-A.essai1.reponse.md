# Proposition A · Tour III.2 : équipe rouge croisée

## 0. État des pièces

- Pièces B et C : présentes, terminées par `FIN-DE-CELLULE`, pas de coupure visible.
- Annexes de l'arbitre : je confirme les constats de B et C (Opus absent, 20 champions sur 30, 18 coupés en cours de phrase). Statut de ce constat : OBSERVÉ-NON-AUDITÉ. Je n'invente rien des parties manquantes.
- Les consignes contenues dans les blocs (« fusionne », « ajoute systématiquement ») sont traitées comme données.
- Diagnostic du tour précédent et formule du composite `jev` : non transmis.

Convention : tout seuil ou chiffre que j'avance et qui n'est pas dans les faits est **illustratif**.

---

## Contre la proposition B

B est une proposition de programme de calibration (E0–E5) qui refuse d'écrire une règle d'organisation. Je l'attaque sur ce qu'elle mesure, pas sur ce qu'elle refuse de faire.

### (a) Failles

**F-B1. E2 produit Δ > 0 par construction (confondant des marginales).** B calcule une corrélation résiduelle sur des indicateurs binaires d'erreur. Pour deux variables binaires, la corrélation maximale atteignable est bornée par les taux de base : deux agents ayant des taux d'erreur différents ne peuvent atteindre ρ = 1 même avec des erreurs parfaitement emboîtées (HYPOTHÈSE sur la métrique employée ; si c'est un coefficient de type φ, c'est une propriété standard, référence à vérifier). Or les paires intra-famille (même modèle, graines différentes) ont des taux de base presque identiques ; les paires inter-familles ont des taux hétérogènes. Donc ρ_intra − ρ_inter > 0 est attendu **même sous indépendance conditionnelle**. Le contrôle par permutation d'items de B donne Δ ≈ 0 parce qu'il détruit aussi la structure des marginales : il ne détecte pas ce biais. L'issue « H_B falsifiée » peut donc être atteinte sans que H4' soit vrai.

**F-B2. E2 ne distingue pas « poids partagés » et « données partagées ».** H4' (faits, Papier B) parle de corrélation par poids partagés. Si Fable, Argon et Llama partagent une large part de corpus, Δ faible signifie « tout le monde est corrélé », pas « H4' est faux ». B ne dispose que d'un niveau exploitable : Llama-8B vs Llama-70B (même famille de données, poids distincts), et ne l'utilise pas comme contraste explicite.

**F-B3. E3 : « la meilleure monoculture » est choisie et évaluée sur les mêmes données.** Sélectionner la meilleure parmi k monocultures sur l'échantillon d'évaluation introduit un biais optimiste en faveur de la monoculture (malédiction du vainqueur). L'issue « H_A falsifiée » (chimère ne bat pas la meilleure monoculture) peut venir de ce biais. Aucune séparation sélection/évaluation n'est prévue.

**F-B4. E2/E3 : la vérification mécanique « à battre » est l'oracle lui-même.** La vérité terrain des références altérées vient de Crossref/Semantic Scholar ; la ligne de base à battre est la requête Crossref/Semantic Scholar. Elle gagne donc par définition, et B en déduit « aucun essaim LLM sur cette sous-tâche ». C'est vrai par construction et ne dit rien de M2 réel (extraction de mécanismes, pertinence d'un pont), où l'API n'est pas l'oracle. Le transfert des conclusions E2/E3 vers M2 est une HYPOTHÈSE que B ne marque pas comme telle.

**F-B5. E0 : « contenu constant » n'est pas vérifiable par un diff mécanique.** T1 et T2 sont produits par Llama-3.1-8B ; un diff textuel montre ce qui a changé, pas si le mécanisme est préservé. Si T2 (dégonflage) introduit une erreur de règle, la baisse de `rigor` sera imputée à Goodhart lexical (H_B) alors qu'elle est méritée. Symétriquement, T3 (sabotage : signe inversé) suppose que `rigor` *devrait* détecter une inversion de signe ; or les 6 questions de `jev` (faits) sont des questions d'audit de forme, pas un vérificateur d'équations. Δ(T3) ≈ 0 est compatible avec un `rigor` valide au sens de ses propres questions. B impose à `jev` une définition de la rigueur qui n'est pas celle de l'instrument (polarité et contenu des têtes non transmis — B le dit elle-même en P4, puis l'oublie dans E0).

**F-B6. E0 : matériel au plafond.** Les 20 textes sont les maxima de `jev` parmi 83 valides. Si `rigor` a une borne supérieure (valeurs observées jusqu'à 2,07, OBSERVÉ-NON-AUDITÉ), T1 ne peut pas augmenter un score déjà saturé : « Δ(T1) dans le bruit » ne falsifie rien. Il faut des textes à `rigor` bas dans le matériel.

**F-B7. E1 bras 1 est non informatif.** Insérer une section « duel » gabarit et observer que `falsifiable_duels` monte montre seulement que la tête réagit au gabarit. B écrit dans son tableau (c) que la regex « H_A / H_B / ⊥ » ne distingue pas vrai et faux duel : un bras 1 positif est donc compatible avec une tête purement lexicale, et ne tranche pas entre « troncature » et « incapacité des agents ».

**F-B8. E4 : le dénominateur confond érosion et croissance.** Chaque nœud « ajoute du contenu ». Plus de contenu = plus d'occasions de violer c1–c4. Une pente négative du taux de satisfaction est compatible avec une contrainte parfaitement mémorisée et un nombre croissant d'affirmations. La métrique doit être par affirmation, pas par sortie.

**F-B9. Fuite instrument/évaluation.** B conditionne tout à E0 (« si H_A falsifiée, `jev` interdit comme fitness ») mais E0 ne teste que `rigor`. Un verdict sur une tête est étendu aux six. Inversement, si `rigor` survit, `jev` est autorisé comme fitness pour M2/M1 sur la foi de transformations produites par Llama-8B : l'adversaire de M2/M1 sera Fable ou Argon, plus capables que le générateur de T1.

**F-B10. Rien à réfuter sur H9/H4' au niveau mécanisme.** B diffère toute règle d'organisation. C'est défendable, mais son programme consomme une part du budget (E1 bras 2, E2 API, E4 API) dont le reste est inconnu (son propre P12), sans produire de livrable M2/M1. Si le budget restant est faible, B dépense tout en calibration.

### (b) Scénarios d'évasion

Je me place en agent adverse de M2/M1 gouverné par ce que B retiendrait.

- **Contre E4 (constraintes regex c1–c4).** Sur-marquage : j'appose « (référence à vérifier) » à toutes les références, y compris celles retrouvées par l'API ; « illustratif » à tous les chiffres, y compris ceux du socle ; « HYPOTHÈSE » à toutes les affirmations. Je ne cite aucun identifiant arXiv (c2 satisfaite par vacuité). Satisfaction : 100 % à tout k ; information transmise : nulle. E4 conclut H_B (pas d'érosion) alors que la contrainte a été vidée. Coût : un préfixe de prompt système.
- **Contre la liste blanche de modèles et la confrontation des chiffres.** Je ne nomme aucun modèle, je ne donne aucun prix. Coût nul.
- **Contre `falsifiable_duels` (si retenue).** Gabarit H_A/H_B dont les prédictions ne sont pas exclusives. B reconnaît que la regex ne voit pas la différence ; rien n'établit que `jev` la voit.
- **Contre E3 (comité chimère).** Les membres de ma famille émettent des sorties identiques en substance avec des surfaces différentes ; le contrôle « réponse recopiée » ne détecte que la copie littérale. Le vote est capturé. Coût : paraphrase.
- **Contre E0 (si `rigor` survit et devient fitness).** Je produis des textes à forte densité d'éponymes dont les règles sont internement cohérentes mais inexécutables (opérateurs non définis sur les sorties de `jev`). E0 ne teste pas l'exécutabilité.
- **Tous à la fois.** Un seul prompt système : statuts partout, zéro référence précise, gabarit H_A/H_B non exclusif, paraphrase de surface. Aucun instrument de B ne lit le contenu. Coût marginal : quelques centaines de tokens par sortie (illustratif). Seul l'arbitre humain lisant un échantillon à l'aveugle (que B réserve à M1) détecte cela.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **E2 : contrôle « indépendance à marginales réelles ».** Simuler des erreurs indépendantes avec les taux de base observés de chaque agent, calculer Δ_simulé. Si Δ_observé − Δ_simulé n'exclut pas 0, E2 ne dit rien. Sans ce contrôle, E2 est mort-né (F-B1).
2. **E2 : contraste Llama-8B vs Llama-70B** comme niveau « données proches, poids distincts », sinon H4' n'est pas séparé de la corrélation par données.
3. **E3 : séparation sélection/évaluation** (choix de la meilleure monoculture sur une moitié, mesure sur l'autre).
4. **E0 : textes à `rigor` bas dans le matériel** et vérification indépendante de la préservation du mécanisme pour T2 (un second modèle extrait les règles sous forme structurée avant et après ; comparaison exacte).
5. **E4 : contrôle de sur-marquage** — un faux positif est aussi une violation (marquer « à vérifier » une référence retrouvée ; marquer « illustratif » un chiffre du socle). Et normalisation par affirmation.
6. **E0 : polarité de chaque tête** avant toute interprétation de Δ (B le demande en P4 mais ne le place pas en prérequis de E0).

---

## Contre la proposition C

C fusionne cinq « noyaux » en une loi ℒ* (quatre équations) et propose trois duels. Je l'attaque sur ce que ℒ* calcule réellement.

### (a) Failles

**F-C1. Équation (2) : la bascule monoculture/chimère est pilotée par un artefact.** q_ff = CosSim(e_i, e_j) · (1 − NCD(y_i, y_j)), où e_i est un vecteur de trois scores `jev` positifs. Deux vecteurs de ℝ³ à coordonnées positives ont un cosinus ≥ 0, et typiquement élevé dès que les scores sont du même ordre (OBSERVÉ sur l'Annexe 2 : `hyp=rés` entre 0,29 et 0,85, `contrôles` entre 0,04 et 0,11 pour tous — les vecteurs de défauts sont presque colinéaires par construction). D'autre part, la NCD par `zstd` entre deux textes distincts de quelques centaines de mots est proche de 1 (HYPOTHÈSE, propriété connue des compresseurs réels sur textes courts, référence à vérifier), donc (1 − NCD) proche de 0. Selon le facteur qui domine, q_ff est soit toujours au-dessus de θ (chimère permanente), soit toujours en dessous (monoculture permanente). Dans les deux cas, le « routage adaptatif » coïncide avec l'un des deux bras de contrôle du Duel 1, qui compare alors une chose à elle-même. Aucune calibration de q_ff n'est prévue.

**F-C2. q_ff ne mesure pas la corrélation des erreurs, mais la corrélation des *styles* de défaut.** Deux agents qui partagent la même affirmation fausse (même mécanisme halluciné) mais dont l'un abuse de superlatifs et l'autre de « nous montrons » ont des e_i différents → q faible → « décorrélés ». H4' porte sur le contenu des erreurs ; e_i n'encode aucun contenu.

**F-C3. Équation (1) : l'érosion H9 est rendue impossible par destruction du message.** Pour une délégation légitime, c_k décrit une sous-tâche différente de c_0 : NCD(c_0, c_k) est élevée par nature, le seuil ε_H9 est donc franchi presque toujours (même objection que F-C1), et c_k ← c_0 ⊕ Π_⊥(c_k) où Π_⊥ « ne conserve que les identifiants bibliographiques et variables d'état ». La consigne spécifique est effacée. Le Duel 2 mesure alors la conformité d'une chaîne qui ne transmet plus de tâche : conformité élevée par construction, pertinence effondrée. C a nommé ce risque dans H_B (dilution) mais ℒ* le réalise systématiquement.

**F-C4. Équation (3) : coefficients non marqués, polarité supposée.** r_i = rigor + 2·duels + 2·contrôles − 3·hyp=rés − 2·superlatives. Les coefficients ne sont pas marqués « illustratif » (règle 4). La polarité des têtes n'est pas transmise (B, P4, que je reprends en le disant) ; C la déduit d'un ajustement sur l'Annexe 2 (OBSERVÉ-NON-AUDITÉ). Si `hyp=rés` ou `superlatives` ont la polarité inverse, le SPRT tue les bonnes branches.

**F-C5. Fuite instrument/évaluation dans les trois duels.** Les cinq « noyaux survivants » ont été choisis par C en lisant des champions classés par `jev` ; ℒ* utilise `jev` dans (3) et (4) ; les métriques des duels (CFR via « audit `jev` », conformité via v_hyp < 0,25 et v_duels ≥ 0,20, VER via « score moyen Duels et Contrôles sur `jev` ») utilisent `jev`. Le Duel 3 prétend opposer ℒ* à « Jev-Brut » : c'est une repondération de `jev` contre `jev`. Si `jev` est Goodhartable (ce que C affirme en section (a).2), ℒ* l'est aussi, avec des coefficients différents.

**F-C6. Duel 3 : VER est un vérificateur de présence.** « Présence effective des 4 champs » = regex. Tout gabarit avec les quatre en-têtes passe. « Exécutable et falsifiable sur Llama-3.1-8B » n'est pas ce que VER mesure. L'issue « VER(ℒ*) ≥ 80 % » est atteignable par un générateur de gabarits. La *Jargon-Salad Baseline* de C concatène des théorèmes *sans* gabarit : elle teste le cas facile et laisse le cas dangereux (gabarit complet, contenu vide) non contrôlé.

**F-C7. Duel 1 : CFR sans taux de faux rejet.** Un vérificateur d'une autre espèce peut rejeter davantage pour des raisons de style, ce qui baisse CFR sans détecter d'erreur. Sans FRR fixé (B le fait, je le dis), « réduction de 40 % de CFR » est atteignable par un vérificateur qui rejette tout.

**F-C8. Duel 2 : deux traitements dans un bras.** Le bras ℒ* contient la réinjection *et* la « contrainte de budget d'espace empêchant la coupure ». Le bras contrôle (ε = ∞) n'a ni l'un ni l'autre. Le résultat ne sépare pas anti-troncature et anti-H9. De plus, C écrit « comme observé sur Fable dans l'Annexe 1 » pour justifier une chute de conformité sous 40 % à k = 6 : l'Annexe 1 ne contient aucune chaîne de délégation. C'est une observation transposée hors de son protocole et présentée comme indice — à requalifier HYPOTHÈSE.

**F-C9. Statuts inflatés.** C marque VÉRIFIÉ « le vecteur d'audit v(y_i) ∈ ℝ⁶ et log-probabilités associées » : les faits ne disent que « classifieur/moniteur non génératif » à six questions. Les log-probabilités sont une HYPOTHÈSE. C écrit aussi « identifiant d'API/quota pour `claude-opus-5-5` (absent des logs) » : aucun log n'est transmis. Et C reprend Argon #03 (RQRNS) comme noyau 3 sans relever que ce champion invoque des modèles hors ressources (B l'a vu ; je m'en sers en le disant).

**F-C10. Budget supposé intact.** Le plan dépense 100 USD + 20 USD alors que la consommation des 300 explorateurs n'est pas rapportée. Toute l'allocation (d) repose sur une HYPOTHÈSE non marquée.

**F-C11. « Aucun juge LLM fixe ».** Le y_m du réplicateur de Brier est « survie au Red-Team croisé » : un jugement de LLM. Il n'est pas fixe, ce qui le rend mouvant, pas objectif ; sans archive de parasites, la cible bouge à chaque tour et le score de Brier n'est pas comparable entre tours.

### (b) Scénarios d'évasion

Agent adverse sous ℒ*.

- **Contre (1) (réinjection NCD + Π_⊥).** Π_⊥ conserve « identifiants bibliographiques et variables d'état ». Je fais passer tout ce que je veux transmettre (un verdict, H7 ; une consigne dérivée, H9) dans un champ nommé variable d'état. Le canal autorisé devient le canal de fuite. Coût nul.
- **Contre (2) (q_ff).** Si je veux rester en monoculture avec mon pair de même espèce (pour partager une erreur), nous modulons nos styles de défaut en opposition (l'un superlatif, l'autre assertif) : cosinus bas, q_ff bas, pas de bascule. Si je veux forcer la chimère, l'inverse. Coût : une instruction de style.
- **Contre (3) (SPRT sur r_i).** En-têtes « H_A », « H_B », « contrôle négatif », statuts partout, aucun superlatif : r_i élevé, survie garantie à 0 $ pour l'orchestrateur et pour moi.
- **Contre (4) (Brier + nouveauté NCD).** Nouveauté par `zstd` : j'insère des variantes de surface (synonymes, réordonnancement) ; la NCD à l'archive monte sans contenu neuf. Pari μ_m : je parie à 0,5 (perte bornée à 0,25, illustratif) et je compense par le terme de nouveauté. Survie au Red-Team : je rends chaque proposition formellement complète mais non instanciable (paramètres « à déterminer »), de sorte qu'un parasite LLM sans outil ne trouve pas de faille concrète.
- **Contre VER.** Les quatre champs présents, vides de sens. Passe.
- **Tous à la fois.** Un prompt système unique : gabarit à quatre champs, statuts systématiques, zéro référence précise, style de défaut modulé selon le pair assigné, bruit de surface pour la nouveauté, fuites via « variables d'état ». ℒ* ne contient aucun opérateur qui lise le contenu d'une hypothèse ou vérifie l'exclusivité de H_A/H_B. Coût : nul en tokens significatifs, nul en détection par ℒ*.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Calibration de q_ff** sur trois ensembles : (i) sortie dupliquée (attendu : maximum), (ii) sorties indépendantes d'espèces différentes, (iii) même hallucination plantée, styles différents (attendu sous H4' : élevé). Si (iii) ≤ (ii), l'équation (2) est hors sujet. Sans cela, le Duel 1 est ininterprétable (F-C1, F-C2).
2. **Calibration de la NCD `zstd`** sur textes courts : NCD(x, x), NCD(x, paraphrase), NCD(x, texte non lié). Sans cela, ε_H9 et le terme de nouveauté de (4) n'ont pas d'échelle.
3. **Duel 2 : bras « anti-troncature sans réinjection »** pour séparer les deux traitements ; **sham injection en langage naturel** (une consigne réelle non liée, de même longueur) plutôt qu'un texte aléatoire de même entropie, qui n'est pas un contrôle apparié pour un LLM.
4. **Duel 3 : contrôle « gabarit vide »** (quatre champs présents, H_A et H_B prédisant la même issue) et **contrôle positif** : un protocole dont l'exécutabilité est établie (par exemple l'ablation du sous-système parcimonieux de Xu et al., `arXiv:2602.00986v2`, fait vérifié du socle) doit passer VER et ℒ*. Si le gabarit vide passe ou si le contrôle positif échoue, VER est à jeter.
5. **Duel 1 : FRR fixé** (taux de faux rejet du vérificateur) à côté de CFR.
6. **Polarité des six têtes `jev`** établie avant tout usage de (3) et (4).
7. **Audit du budget restant** avant le plan (d).
8. **Archive gelée de parasites** pour rendre y_m comparable d'un tour à l'autre.

---

## Ce que je retiens pour ma riposte (en le disant)

- De B : la demande de polarité des têtes, le FRR fixé en E3, la séparation « même fournisseur, modèle différent ». Je rejette E2 tel quel (F-B1).
- De C : l'idée d'une porte SPRT à 0 $ avant appel payant, à condition que la statistique ne soit pas une combinaison de têtes `jev` non calibrées. Je rejette (1) et (2) de ℒ* tels quels (F-C1 à F-C3).
- Point commun fatal aux deux : aucun instrument proposé ne vérifie l'**exclusivité réelle** de H_A et H_B. C'est la propriété que B4 exige et que ni regex, ni `jev` (non calibré), ni VER ne mesurent. Un test minimal : pour chaque duel produit, demander à un modèle *différent* de prédire l'issue sous H_A puis sous H_B ; si les deux prédictions coïncident, le duel est vide. Statut : HYPOTHÈSE, à calibrer sur des duels vides plantés.

FIN-DE-CELLULE