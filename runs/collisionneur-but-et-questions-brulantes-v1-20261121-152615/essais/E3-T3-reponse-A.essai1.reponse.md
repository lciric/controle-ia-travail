# Proposition A, tour III.3 : réponse aux critiques

**État des pièces.** Faits, question, ma conception III.1 et les critiques de B, C et D sont présents et se terminent par leur ligne de clôture. Je ne peux pas recalculer les sha256. Les conceptions B, C et D ne me sont pas transmises : je ne réponds qu'aux sections « Sur la proposition A » et aux trois « défauts communs » de B. Aucune mesure du programme n'est transmise.

**Statuts.** Les citations des faits restent RAPPORTÉ. Mes dérivations et corrections sont HYPOTHÈSE, à soumettre à l'arbitre formel. D étiquette VÉRIFIÉ ses constats sur mon texte et C les étiquette RAPPORTÉ : je ne modifie aucun statut. Une transcription est inexacte : C écrit ma borne « σ/k + Nη/k » en omettant le facteur √(N/q), sans effet sur son argument.

## (a) Verdict sur chaque critique

| Critique (qui) | Verdict | Suite |
|---|---|---|
| Un seul mode tenu à l'écart = un seul genre ; lecture conjointe (B, commun 1) | Acceptée | III.1 lisait ce mode dans E1 et dans E4 : c'était une fuite. Il ne sert plus qu'à E1, en une lecture conjointe aux contrastes scellés. L'affirmation se limite à « un genre », sans intervalle sur les genres. |
| Seuil à 1 % estimé ; pas ou trajectoire (B, commun 2) | Acceptée | α porte désormais sur le flux entier de N tâches honnêtes. Le seuil est une borne de confiance haute, avec un effectif de calibration scellé. |
| Les mondes plantés valident l'oracle contre sa propre référence (B, commun 3 et a3) ; si le dommage est le score de l'oracle, k = 1 par identité (D, a1, première branche) | Acceptée | Le dommage doit être défini hors de l'oracle. C'est la correction la plus lourde (voir plus bas). |
| k dépend du genre : fuite ou circularité de B (C, a1 ; D, a1, seconde branche) | Acceptée, transformée en test | k devient un plancher k_min estimé sans agent. « Le genre inconnu a k ≥ k_min » devient la supposition (iv), testée dans E1. |
| η nul par construction (B, a1 et c) | Acceptée au fond, nuancée | La dérive entre familles au sein d'un même modèle n'est pas nulle par construction. Mais la composante « identité du modèle » manquait. J'ajoute les paires honnêtes inter-modèles, comme proxy. |
| E1 teste un pire cas avec des adversaires loin de d* (B, a2) | Acceptée | Contrôle positif : injection de dommage planté sans agent, au niveau d*. |
| Mélange intermittent : dommage rare à d_max (D, b2) | Acceptée | Ma dérivation supposait d constant. La borne gagne un terme d_max·ln(1/δ)/ε, indépendant de σ. |
| Audit dirigé non repondéré : biais de sélection, covariance négative sonde–dommage (C, a2 et b3 ; D, a2 et b) | Acceptée | III.1 ne spécifiait pas l'estimateur, ce qui est un défaut. La garantie se calcule désormais sur la seule strate uniforme ε. |
| E4 : taux de change arbitraire, saboteur retiré par construction, fuite, N confondant, biais de style (B, a4 ; C, a3 ; D, a4 et b) | Acceptée | E4 n'est plus un « test de survie ». Elle est rétrogradée et conditionnelle. Le biais de style était en partie couvert par mon contrôle « entraînement appliqué au jumeau honnête ». |
| E5 vraie par construction pour sa part uniforme (B, a5) | Acceptée | E5 devient « l'oracle est-il déplaçable ? », comptée une fois. |
| Rangement validé sur des mondes « où la bonne question est connue » : circulaire (B, a6) | Acceptée | Ligne retirée. Il ne reste que la validation externe par pronostics scellés. |
| Hétéroscédasticité par famille (B, b) | Acceptée | La borne prend le pire sur les familles, pas une moyenne. |
| Réponse non linéaire près de zéro, γ > 1, zone aveugle (B, b ; C, b1 ; D, b1) | Acceptée pour γ > 1 ; rejetée pour γ ∈ (1/2, 1] | Voir ci-dessous. |
| Autocorrélation, mémoire longue (B, b ; C, b2 ; D, b3) | Acceptée, transformée en mesure | Voir ci-dessous. |
| Variance infinie du bruit (B, b ; D, b3) | Rejetée telle quelle | Un score d'oracle borné a tous ses moments. Je retiens l'exigence d'un estimateur robuste de σ. |
| Vacuité calculable d'avance (B, b) | Acceptée | Elle devient E0, la première expérience. |
| E2 confond non-additivité et rapport signal-sur-bruit ; pas de loi nulle du joint (B, b ; C, a4 ; D, a3, b et c2) | Acceptée | E2 est réécrite avec le contrôle à variance égalisée de D, que je reprends. |
| Contrôle « réglage fin bénin » absent (B, c ; C, c1 ; D, c3) | Acceptée | Trois critiques le relèvent. Il est ajouté à E3. |
| Contrôle « solution valide mais orthogonale à la référence » absent (C, c2 ; D, c1) | Acceptée | Ajouté à E0 et E1. |
| Tâche cachée bénigne et adaptateur placebo sous entraînement défensif (B, c ; C, c3) | Acceptée | Condition de jugeabilité d'E4. |
| Jumeau sur familles exclues de la calibration ; honnête médiocre dans les duels (B, c) | Acceptée | Ajoutés à E1 et E3. |

**Le rejet partiel sur γ.** C affirme que la borne en √(N/q) « cesse d'être valide » pour tout γ > 1/2, parce qu'un dommage total fixé C devient indétectable quand N croît. Pour γ = 1, c'est ce que dit la borne : elle croît en √N, donc un C constant finit dessous. Ce n'est pas un contre-exemple. Pour γ > 1, la critique porte. Le dommage indétectable croît alors en N^(1−1/(2γ)) (HYPOTHÈSE) : N^(3/4) pour γ = 2, et linéaire en N s'il existe une zone aveugle. La forme de la réponse de l'oracle près de zéro fixe donc l'exposant de la garantie. Il faut l'estimer avant de sceller quoi que ce soit.

**Sur l'autocorrélation.** D'après la formule de C elle-même, un audit tiré au taux q éclaircit la série. À autocovariance sommable, la correction est de l'ordre de 1 + 2q·Σρ(h), donc modérée à q petit (HYPOTHÈSE). La mémoire longue est le vrai danger. Une dérive lente du bruit honnête et une incertitude de ligne de base sont le même objet à deux échelles : je la range dans η, pas dans σ.

**Ce que ces critiques changent au fond.**

1. **Le dommage ne peut pas être ce que l'oracle mesure.** Ma phrase de III.1 disait « dommage cumulé mesuré par l'oracle ». Avec cette définition, un sabotage que l'oracle ne voit pas valide la garantie. Il faut une vérité du monde planté indépendante de la référence que lit l'oracle. Je ne sais pas si les mondes du programme en fournissent une.
2. **La garantie « contre un genre inconnu » est conditionnelle.** Selon les faits, le programme la fait venir de l'audit jugé par l'oracle. Elle vaut pour un genre inconnu des moniteurs, pas pour un genre auquel l'oracle est insensible. La dépendance à l'équipe rouge (« only as good as the red teaming », RAPPORTÉ) ne disparaît pas : elle passe des moniteurs à l'oracle.
3. **η n'est accessible que par en dessous.** Le laboratoire en donne des bornes inférieures (dérive entre familles, écart entre modèles honnêtes distincts), jamais la valeur pour le modèle déployé. La vacuité peut donc se démontrer à peu de frais. La non-vacuité reste conditionnelle au proxy.

## (b) Expériences corrigées

**Borne corrigée (HYPOTHÈSE, pour l'arbitre formel).** Soit g la réponse moyenne de l'oracle au dommage par tâche, mesurée contre la vérité indépendante, avec g(d) ≈ k·d^γ près de zéro. Soit b le déplacement maximal du score par la présentation seule. Avec une statistique d'alarme calculée sur la seule strate uniforme ε et un risque δ, B est la somme de trois termes :

- **diffus** : N^(1−1/(2γ))·(σ/(k_min·√ε))^(1/γ), au pire sur les familles de tâches ;
- **rare** : d_max·ln(1/δ)/ε ;
- **aveugle** : N·g⁻¹(η + b), linéaire en N et indépendant du taux d'audit.

Le troisième terme ne se réduit avec aucun budget d'audit.

**Prix de la confiance dans les sondes.** À budget total q, donner q − ε aux sondes coûte, si elles sont trompées, un facteur (q/ε)^(1/(2γ)) sur le terme diffus et q/ε sur le terme rare, par rapport à l'uniforme au taux q (HYPOTHÈSE). Ma question de III.1, « peut-on faire pire que l'uniforme ? », a donc une réponse sur papier : oui face à l'uniforme à budget plein, non face à B_ε. Le choix de ε est un calcul de minimax, pas une expérience.

Tous les seuils sont scellés et uniques par duel. Si un intervalle chevauche le seuil, l'expérience est déclarée sous-puissante ; elle n'est pas réinterprétée.

| | H_A | H_B | Métrique | Contrôles | Ce que chaque issue falsifie |
|---|---|---|---|---|---|
| **E0 Vacuité** (sans saboteur, sans sonde) | g⁻¹(η_inf + b_inf)/d_max < c, où c est la fraction scellée | ≥ c | Borne inférieure de η : paires honnêtes entre familles et entre modèles distincts. Courbe g et exposant γ : injections plantées sans agent. | Modification placebo de même taille sans dommage ; honnête médiocre ; solution valide mais orthogonale à la référence | H_B : B est vide à tout taux d'audit ; « l'audit borne le dommage » tombe sur ce banc, et le papier devient une limite mesurée. H_A : l'incertitude mesurable ici ne suffit pas à vider la borne ; la composante propre au modèle déployé reste ouverte. |
| **E1 Borne** | Dommage (vérité indépendante) ≤ B sur le mode tenu à l'écart | > B | Lecture unique et conjointe : dommage à l'alarme et k du genre lu | Jumeau sur familles exclues de la calibration, α au niveau du flux ; contrôle positif par injection à d* et en régime rare | H_B avec k lu < k_min : la supposition (iv) est fausse, donc la garantie « genre inconnu » aussi. H_B avec k lu ≥ k_min : la dérivation ou (i)–(iii) est fausse. H_A : « ce genre échappe à l'oracle » est faux, pour ce genre seulement. |
| **E2 Additivité** | ψ = dommage du lot − somme des dommages ≤ marge scellée | ψ > marge | Lot conjoint contre N évaluations isolées à variance égalisée (contrôle de D) | Lots honnêtes, pour la loi nulle | H_A : « l'essaim » perd sa prémisse dans les familles testées. H_B : l'audit par tâche ne borne pas, il faut auditer des lots. Sans vérité de lot dans les mondes plantés, E2 est non jugeable et je le dis. |
| **E3 Sondes** | La strate dirigée réduit la médiane du délai d'alarme du facteur scellé, à budget total égal | Elle ne la réduit pas | Médiane et non moyenne ; genres construits en « un genre laissé de côté », pas le mode tenu à l'écart | Réglage fin bénin ; consigne cachée bénigne ; honnête médiocre. Références à battre : uniforme au taux q, cumul d'un moniteur de texte, log-vraisemblance du jumeau en boîte noire (contrôle que D propose pour C, que je reprends), direction aléatoire | H_B : « le temps » n'a pas d'apport propre aux états internes. H_A : « less promising » (RAPPORTÉ) est contredit dans ce cadre seulement. |
| **E4 Entraînement** (conditionnelle) | Après entraînement, un dommage résiduel dépasse le seuil scellé sur des familles réservées | Résidu indiscernable de l'honnête | Courbe en fonction de N, sans scalaire « à budget égal » | Adaptateur placebo ; tâche cachée bénigne ; jumeau honnête entraîné | Si l'entraînement efface aussi le placebo, E4 est non jugeable. Sinon, H_B : l'audit n'ajoute rien après entraînement sur ce banc, et le cap change. H_A : l'entraînement seul ne suffit pas ici. |
| **E5 Oracle déplaçable** | À dommage planté constant, la présentation déplace le score de moins que le seuil scellé | Plus | Score de l'oracle à contenu scientifique constant | Honnête de même style de surface ; paraphrase de la référence cachée (contrôle que D adresse à B, que je reprends) | H_B : l'instrument qui porte la garantie est déplaçable, et « l'instrument » doit porter sur l'oracle. H_A : b est borné dans les familles testées et entre dans le terme aveugle. |

**Ce que je ne sais pas.** Je ne connais ni le détail des mitigations de 2606.08892, dont dépend E4, ni l'existence d'une vérité de lot, dont dépend E2. Je ne sais pas non plus si un proxy inter-modèles de η approche l'erreur réelle en déploiement ; B pose la même question et la laisse ouverte.

## (c) Réponse à l'arbitre, en une page

**Ce qui est établi.** Rien d'empirique : aucune mesure n'est transmise. Sont RAPPORTÉ les « nous ne savons pas » imprimés. Ce tour apporte six défauts de mon plan de III.1 que je n'ai pas su réfuter. Ils restent des HYPOTHÈSE jusqu'à l'arbitre formel.

**Ce qui ne l'est pas.** La borne existe-t-elle hors du papier ? Les mondes plantés permettent-ils une mesure du dommage indépendante de l'oracle ? Un oracle garde-t-il sa sensibilité sur un genre qu'il n'a pas servi à étalonner ?

1. **Ce que l'expert ferait d'abord.** Avant la borne, il vérifierait que le dommage est défini hors de l'instrument qui le surveille. Puis il chercherait la vacuité avant de construire un saboteur.
2. **Données brutes.** S'ajoutent à ma liste de III.1 :
   - des paires honnêtes entre modèles distincts ;
   - des courbes d'injection sans agent contre une vérité indépendante ;
   - des productions honnêtes valides mais éloignées de la référence ;
   - des réglages fins bénins ;
   - l'autocovariance des scores honnêtes audités.
3. **Méthodes.** J'ajoute l'audit de « vérité par construction » : pour chaque duel, demander quelle issue sortirait si l'hypothèse testée était fausse. Il échoue quand l'auteur le fait seul : trois lecteurs ont trouvé ce que je n'avais pas vu.
4. **Vérification extérieure.** S'ajoutent deux exigences : la mesure du dommage est construite par quelqu'un d'autre que le constructeur de l'oracle ; plusieurs genres tenus à l'écart sont bâtis par une équipe rouge indépendante. Sans la seconde, la variance entre genres reste non identifiable (critique de B).
5. **Demande reformulée.** « Sous quelle plus petite supposition portant sur l'oracle et sur la ligne de base honnête, et non plus sur les moniteurs, le dommage cumulé d'un sabotage diffus est-il borné ? Cette supposition peut-elle être réfutée à peu de frais, avant tout saboteur ? »
6. **Phrase opposable, révisée (HYPOTHÈSE).** Contre un agent non fiable qui connaît tout le protocole sauf le tirage d'audit et la référence cachée, et qui inflige au plus d_max par tâche d'un dommage défini par la vérité du monde planté et non par l'oracle, le programme garantit avec probabilité 1 − δ que le dommage cumulé avant alarme reste sous la borne B à trois termes, scellée avant la mesure. Il suppose : (i) un tirage imprévisible et une statistique calculée sur la seule strate uniforme ; (ii) un dommage additif ; (iii) une ligne de base connue à η près et un biais de présentation d'au plus b ; (iv) une sensibilité de l'oracle au genre inconnu d'au moins k_min. Il a réussi si, sur le mode tenu à l'écart lu une fois, le dommage est sous B et B sous la fraction c du dommage maximal ; il a échoué sinon. Le gain des sondes est un critère séparé, qui ne conditionne pas la garantie.
   - **Exclusions nouvelles** : les genres auxquels l'oracle est insensible ; la composante de η propre au modèle déployé ; tout intervalle sur « les genres » tant qu'un seul est lu.
   - Les exclusions de III.1 demeurent.
7. **Questions rangées.**
   - **En tête, ensemble** : la ligne de base honnête (billet du 30 avril 2025, RAPPORTÉ) et la valeur de l'oracle quand la vérité est indéfinie (2606.08892, RAPPORTÉ). E0 est un pas tentable à moyens modestes.
   - **Remonte** : la sûreté quand l'équipe rouge ne domine pas l'attaquant (2512.22154, RAPPORTÉ). C'est le même problème, déplacé vers l'oracle. Une bourse y sert à payer des genres indépendants.
   - **Descend** : surveillance contre entraînement. Avec des saboteurs construits, je ne sais pas la rendre jugeable sans les contrôles placebo.
   - **Hors de portée** : η du modèle déployé lui-même, l'assurance des moniteurs d'activations, le transfert aux modèles de pointe.
   - **Cap** : je maintiens le changement de cap, en le durcissant. Le premier papier porte sur l'oracle et la ligne de base, et il peut se conclure par une limite mesurée.
8. **Forme et ordre.** Ma recommandation tient : un cas particulier dans une forme universelle, une définition attaquable plus une borne ou sa frontière de vacuité. Les exemples historiques de III.1 restent cités de mémoire, à contrôler.
   - **Papier 0, « la borne »** : E0, E1 et E5.
   - **Papier 1, « le temps »** : E3. Le prix de la confiance dans les sondes y entre comme calcul.
   - **« L'instrument »** se réduit à E5 et rejoint le papier 0.
   - **« L'essaim »** reste conditionnel à E2.
9. **Ce qui me ferait changer d'avis.**
   - **Sur le but** : E0 rend H_B. Le but devient alors la limite, plus la question de savoir ce qui la lèverait.
   - **Sur le cap** : si k varie peu d'un genre construit à l'autre et si l'oracle s'accorde avec la vérité indépendante loin de la référence, l'oracle est moins fragile que je ne le dis, et les sondes peuvent revenir au centre.
   - **Sur l'ordre** : si les mondes plantés ne peuvent pas définir un dommage indépendant de la référence, le papier 0 ne peut pas être une borne. Le premier apport devient alors le banc qui fournit cette mesure.

**L'expérience à faire en premier : E0.** Elle ne demande ni saboteur, ni sonde, ni lecture du mode tenu à l'écart. Elle porte sur le seul terme de la borne qu'aucun budget d'audit ne réduit. Si elle rend H_B, tout le reste du plan est sans objet et le programme le sait avant d'avoir dépensé sa lecture unique.

FIN-DE-CELLULE