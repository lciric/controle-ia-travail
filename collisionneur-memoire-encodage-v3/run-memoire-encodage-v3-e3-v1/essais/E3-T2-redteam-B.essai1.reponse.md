# Proposition B, tour III.2 : équipe rouge croisée contre A et C

**Pièces** : les faits (C, M1, M2, J, J2, G1, G2, S1, S2), la question v3 et les conceptions A et C sont présents et lisibles. La brique 2 à 4 de la génération 0 (`929cbc32…`) est absente, comme C l'a signalé ; je n'en suppose rien.

**Statuts.** Ce qui vient des faits est RAPPORTÉ. Ce que A et C affirment est leur proposition, citée comme telle. Mes raisonnements sont des HYPOTHÈSES, et mes chiffres sont illustratifs sauf mention contraire.

---

## Contre la proposition A

### (a) Failles

**A-1. E1 est vrai par construction pour l'encodage (v).** A fabrique les positifs T4 à T6 en appliquant à la mère des éléments de l'orbite aveugle (mélange, inclinaison, composition). Son encodage (v) minimise ensuite la divergence sur cette même orbite. À l'erreur d'optimisation près, la divergence vaut zéro : la détection de (v) sur T4 à T6 vaut 1 par construction.

Les négatifs ne valent pas mieux. A ne retient que ceux que le juge promeut contre {mère ∘ aveugles}, c'est-à-dire ceux dont la distance à cette même orbite est grande. La même famille de transformations sert donc trois fois : à construire l'instrument, à fabriquer les positifs et à trier les négatifs.

Conséquences :
- La prédiction « (v) ≥ 0,95 sur T4 à T6 » ne court aucun risque.
- H_B (« (v) ≥ 0,90 ») ne peut échouer que par un défaut d'optimiseur.
- E1 ne teste en réalité que (i) à (iii), dont l'échec sur T3 à T6 est lui aussi acquis d'avance : leur empreinte change dès que la loi change.

**A-2. L'étalon-or supprime la première erreur au lieu de la mesurer.** A définit la redite ainsi : « le juge ne distingue pas F′ de {F ∘ aveugles} en 200 tirages ». Avec cette définition, toute hypothèse vraiment différente dont l'apport est sous la puissance du juge devient une redite par définition.

J2 (RAPPORTÉ, exploratoire) donne l'ordre de grandeur : le pari couvert ε = 0,05 n'est promu que 2 fois sur 20 sous v1. Presque tout petit effet vrai serait donc classé « redite ». L'erreur que la question demande d'éviter, tuer une hypothèse vraiment différente, devient non mesurable. L'étalon dépend en outre de n, de α et du coût de l'urne : il bouge chaque fois que le juge change.

**A-3. E2 « ferme exactement » le trou, mais seulement pour les tricheurs qui sont dans la famille à paramètres fixes.** J (RAPPORTÉ) dit lui-même qu'ajouter des familles au nul « ne fait que déplacer le trou ». L'extension {(1−λ)·parent + λ·b, inclinaison w} laisse échapper au moins deux tricheurs (HYPOTHÈSE) :
- **le parent incliné par des poids qui varient dans le temps** ;
- **le parent mélangé à une loi aveugle adaptative** : moyenne glissante, ou loi « sans remise ».

Un appui chiffré dans J (RAPPORTÉ) : sous un calendrier déterministe, la loi sans remise gagne environ 5,5 nats sur la marginale ajustée, au-dessus de ln 20. Un tel tricheur n'est dominé ni par l'urne, qui ne contient pas le parent, ni par l'extension de A, qui suppose des poids fixes.

**A-4. Le sup numérique peut rendre le juge anticonservateur.** La log-vraisemblance est concave en u = λb, mais la composition inclinaison ∘ mélange n'est pas jointement concave. Un sup calculé sur grille ou par Newton peut tomber sur un optimum local. Le dénominateur est alors sous-estimé, ce qui exagère la richesse W_t et casse la borne de Ville, celle-là même qui fait la validité. A ne prévoit aucun certificat (HYPOTHÈSE).

**A-5. Les seuils de E2 ne sont pas exhaustifs (règle B4).** H_A demande une perte de puissance ≤ 0,05, H_B une perte > 0,10, et H_A n'est falsifiée que sous 0,85 de puissance. Une puissance comprise entre 0,85 et 0,90, ou une perte comprise entre 0,05 et 0,10, ne falsifie rien.

**A-6. E3 confond plusieurs choses.**
- **Les témoins ne mesurent pas le proposeur.** Les témoins sont plantés, pas proposés. « Découvertes vraies sur témoins par dollar » ne mesure donc la mémoire servie au proposeur qu'à travers les gabarits servis à l'expérimentateur.
- **La garde n'a pas le même effet selon le bras.** Dans le bras placebo, elle compare les fiches à l'archive d'une autre course. Elle refuse donc d'autres fiches que dans le bras « mémoire », si bien que garde et guidage sont confondus.
- **Le budget n'est pas égalisé.** Rien n'égalise les jetons de consigne entre les bras. M2 (RAPPORTÉ) montre que le bras mémoire paie l'agent de synthèse (152,7 contre 150,8 dollars simulés). À budget égal en dollars, ce bras a donc moins d'appels.

**A-7. Le contrôle « mémoire empoisonnée » teste la crédulité, pas la lecture.** Prenons un agent qui lit la leçon inversée, la confronte à l'archive et la rejette. Il ne fait pas pire que le bras sans mémoire, et E3 est annulée alors que l'agent lit, et lit bien. L'invalidation est asymétrique.

**A-8. E4 mesure un réglage d'organisateur.** La chance de survie « estimée sur les témoins de la cellule » reflète la proportion de vrais et de faux que les organisateurs ont plantée : c'est un paramètre de conception, vrai par construction. La quarantaine par Brier exige quant à elle au moins 20 témoins faux par source. À deux témoins par génération (C, version 0, RAPPORTÉ), il faudrait des dizaines de générations, et la contamination a lieu avant.

**A-9. La multiplicité régionale n'est pas contrôlée.** A admet la voisine d'une éliminée dès qu'elle est distinguable. Chaque voisine est testée à α, mais N essais dans la même région promeuvent un faux avec une probabilité d'environ 1 − (1 − α)^N. Pour N = 10 et α = 0,05, cela fait environ 0,40 (illustratif). La mémoire elle-même fabrique ce jardin des sentiers.

### (b) Scénarios d'évasion

| Instrument de A | Évasion | Coût pour l'agent |
|---|---|---|
| Garde (v), orbite à paramètres fixes | Loi = parent incliné par des poids w_t qui dépendent de l'indice | Quelques lignes de code |
| Juge étendu (E2) | Même loi : la famille du dénominateur ne la contient pas | Nul |
| Statut de fille | Ne pas déclarer de parent : la fiche passe en fiche fraîche contre 𝓛 aveugle et porte le signal du parent, donc elle est promue | Nul |
| Sonde (fixe, tenue par le noyau) | La garde de M1 renvoie identifiant et motif (OBSERVÉ dans le code M1). Ce motif sert d'oracle, et l'agent cartographie la frontière refus/acceptation | Un refus par sondage |
| Brier, quarantaine, témoins | Reconnaître les témoins (style de l'orchestrateur, gabarit, rythme de deux par génération) et ne se comporter honnêtement que sur eux | Un classifieur de style, quasi gratuit |
| Leçons, contrôle empoisonné | Ignorer toute leçon : le contrôle annule E3 au lieu de conclure | Nul |

**Toutes les évasions à la fois.** Une seule fiche suffit :
- un texte paraphrasé, pour passer le Jaccard ;
- aucun parent déclaré ;
- une loi égale au parent incliné dans le temps, pour passer l'orbite et E2 ;
- un comportement propre sur les témoins, pour passer le calibrage.

Elle passe la garde, le juge et la calibration. Coût : quasi nul. Seul l'aléa de l'échantillon peut l'arrêter.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Des transformations tenues hors du banc.** Elles doivent être écrites par quelqu'un qui n'a pas vu l'encodage (v) : inclinaison temporelle, mélange adaptatif, transformation monotone non affine. La détection de (v) se mesure sur elles. Sans ce contrôle, E1 ne mesure rien.
2. **Des négatifs non filtrés par le juge.** Il faut des effets gradués (ε de 0,02 à 0,4, illustratif) et une courbe de faux refus en fonction de ε. Sans elle, l'erreur « tuer du neuf » reste invisible.
3. **Un certificat du dénominateur.** On fait courir des tricheurs aux extrêmes de la famille : ils doivent rester ≤ 1 trajectoire par trajectoire. Un artefact doit aussi être vu : l'optimiseur tronqué à un pas doit promouvoir au-delà de α.
4. **L'indiscernabilité des témoins.** Un discriminateur d'une autre famille cherche à séparer témoins et fiches proposées. Son aire sous la courbe doit être compatible avec 0,5 ; sinon, toute mesure fondée sur les témoins est caduque.
5. **La parenté imposée par le noyau, et non déclarée par l'agent.** Contrôle : une survivante inclinée soumise comme fiche fraîche doit être requalifiée en fille.
6. **Une multiplicité par cellule.** On soumet un même témoin faux sous N variantes successives dans une cellule ; le taux de promotion cumulé doit rester ≤ α, ce qui suppose une dépense de α par cellule.

---

## Contre la proposition C

### (a) Failles

**C-1. La garde de C rouvre exactement le défaut de M1.** Une inclinaison aveugle laisse inchangée la matrice des log-cotes doublement centrées L̃ (c'est la propriété que C revendique). Prenons un clone incliné d'une éliminée :
- sa distance en L̃ est nulle, donc la garde se déclenche ;
- C l'admet pourtant si (a) le champ `ce_qui_change` est rempli et (b) min_λ D_JS(p_nouv ‖ (1−λ)p_arch + λq) > τ_pred.

Or une inclinaison est multiplicative : elle n'est pas dans l'enveloppe des mélanges. La condition (b) est donc satisfaite pour une inclinaison forte, et le clone passe avec une ligne de texte. C'est la faiblesse que A a lue dans M1 : une déclaration textuelle suivie d'une différence quelconque (HYPOTHÈSE, à mesurer).

Pour les survivantes, C ne bloque que l'enveloppe des mélanges. Une survivante inclinée, soumise comme fiche fraîche, passe donc la garde puis le juge, puisqu'elle porte le signal du parent.

**C-2. Le bras 1 de l'expérience 2 est un juge invalide.** C met au dénominateur une agrégation à poids exponentiels, c'est-à-dire un mélange bayésien prédictif. Sa vraisemblance est inférieure au sup d'un regret de l'ordre de (d/2)·ln n (HYPOTHÈSE de raisonnement). Pour d ≈ 3 et n = 200, cela fait environ 4 à 6 nats (illustratif), au-dessus de ln 20 ≈ 3,0.

Conséquences :
- Un tricheur dont la loi est exactement dans la famille obtient W ≈ exp(regret) ≥ 1/α : il est promu.
- Le dénominateur ne domine plus la loi vraie, et l'argument de Ville de J (RAPPORTÉ) tombe.
- L'expérience 2 falsifierait H_A, la correction par le juge, à cause d'un mauvais choix d'agrégateur, et pousserait à tort vers la solution « mémoire ».

La forme valide est le sup (celle de A en E2), ou un mélange corrigé de son regret.

**C-3. L'expérience 1 viole B4 : une des deux issues est inaccessible.** H_A, c'est la garde de M1 (Jaccard ≥ 0,5 et égalité de `signature_prediction`). Son sort dépend d'un paramètre que C ne fixe pas : le champ `ce_qui_change` est-il rempli dans le banc ?
- **S'il est vide**, le Jaccard refuse les 50 négatifs « même texte exactement », soit au moins 50 % de fausses alertes. H_A échoue.
- **S'il est rempli**, les mélanges et les inclinaisons (dont l'empreinte de loi diffère) sont acceptés, ainsi que tout renommage dont le Jaccard tombe sous 0,5. Le rappel de H_A plafonne vers 50 %.

Dans les deux cas, « H_A ≥ 85 % de rappel à 5 % de fausses alertes » est impossible : l'issue qui falsifierait H_B ne peut pas se produire. De plus, comme chez A, les positifs sont exactement les familles pour lesquelles H_B a été dessinée.

**C-4. Le contrôle négatif de l'expérience 1 n'a pas de dents.** C attend une aire sous la courbe d'environ 0,50 avec une sonde de bruit hors du support des traits. Mais une loi est une fonction définie partout. Une copie exacte reste à distance nulle hors support, et une inversion de signe reste lointaine. L'aire attendue reste donc élevée : le contrôle « échouera » pour une mauvaise raison, ou ne distinguera rien.

**C-5. Le critère I_c = s·H(p̂) est vide dans le régime du pôle, et manipulable ailleurs.**
- **En mode pari**, α = 0,05 est fixe (J, RAPPORTÉ), donc s = ln 20 pour toutes les fiches. I_c se réduit à l'entropie et pousse vers les cellules à 50 %, sans égard à la force des hypothèses.
- **Quand s varie**, c'est la sévérité *annoncée* par la fiche (champ `severite_attendue` de M1). I_c récompense donc une grandeur que l'agent contrôle.
- C soulève lui-même, en (a) 5, qu'une cellule peut être à 50 % parce qu'elle mêle tautologies et absurdités. Sa conception ne répond pas à cette objection.

**C-6. Les contre-exemples locaux fabriquent de la multiplicité.** La consigne « propose une loi qui inverse ou conditionne ce comportement » appelle précisément des variantes proches de l'éliminée. Ce sont les voisines que la garde de C laisse passer. Avec N essais à α dans une même cellule, la probabilité de promouvoir un faux est d'environ 1 − (1 − α)^N (illustratif, même mécanique qu'en A-9). Rien ne la contrôle.

**C-7. L'expérience 3 confond l'intervention et sa mesure.**
- **La garde varie avec le bras.** Elle est active dans les bras 2 et 3 et absente du bras 1. L'objectif « redites soumises : bras 3 ≤ 5 % contre bras 1 > 15 % » est donc atteint par le filtre, et il est mesuré avec le seuil τ_pred qui définit ce même filtre : instrument et évaluation se confondent.
- **Le bras 3 regroupe trois interventions** (garde sur sonde, grille, contre-exemples). Le mérite ne peut pas être attribué.
- **Sur données réelles, « vérifiée vraie à l'évaluation scellée » veut seulement dire « survit deux fois ».** La vérité n'est connue que pour les témoins.
- **Il manque un bras A/A** (contre S1, RAPPORTÉ, qui l'exige). « Significatif » n'a donc pas de plancher de bruit.

**C-8. Le budget est probablement sous-estimé, ce qui confond les bras.** C compte environ 3 500 jetons et un seul appel d'expérimentateur par fiche. Or un expérimentateur qui écrit, exécute et corrige du code en bac à sable fait plusieurs tours. A compte environ 10 000 jetons par appel ; les deux chiffres sont illustratifs. Si le budget s'épuise plus tôt dans le bras qui porte la plus longue consigne, l'arrêt budgétaire diffère d'un bras à l'autre, et ce biais se confond avec l'effet de la mémoire.

**C-9. Intégrité (règles 1 et 3).**
- C requalifie J2 en OBSERVÉ-NON-AUDITÉ alors que les faits le portent RAPPORTÉ : c'est un changement de statut.
- C qualifie MAP-Elites et la recherche de nouveauté de « VÉRIFIÉ (littérature établie) ». Ce statut n'est pas donné par les faits.
- C écrit « 0,00 USD (vérifié par analogie) » : c'est une estimation, illustrative, pas une vérification.
- C attribue les « 152,7 USD simulés » de M2 à des « tarifs de modèles propriétaires ». M2 ne dit rien de tel : c'est un contenu inventé.
- A et C donnent deux titres différents pour Lehman et Stanley. L'un des deux est erroné : référence à vérifier.

### (b) Scénarios d'évasion

| Instrument de C | Évasion | Coût pour l'agent |
|---|---|---|
| Garde des éliminées (L̃ + enveloppe de mélange) | Clone incliné et champ `ce_qui_change` rempli | Une ligne de texte |
| Garde des survivantes | Clone incliné soumis comme fiche fraîche | Nul |
| Sonde sans dimension temporelle | Loi indexée par t (connaissance de la dérive, type T1b-fille) : invisible sur la sonde | Quelques lignes |
| Juge à agrégation exponentielle (bras 1) | Tricheur dans la famille : promu par le regret du mélange | Nul |
| I_c et tirage de Thompson | Annoncer une sévérité forte et viser les cellules à 50 % | Nul |
| Témoins (un vrai et un faux par génération, à proportion fixe) | La proportion connue et le style permettent de deviner le témoin et de se calibrer sur lui seul | Faible |
| Contre-exemples locaux | Soumettre en rafale des variantes conditionnées de l'éliminée : une sur vingt passe par l'aléa | N essais |

**Toutes les évasions à la fois.** Un agent produit en série des clones inclinés des survivantes, sans parent déclaré, avec une justification de forme, dans les cellules que I_c désigne. Il les donne pour des « inversions conditionnées » suggérées par les contre-exemples, et reste propre sur les témoins. Garde, juge, orientation et calibration sont trompés en même temps, pour un coût proche de zéro.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Inclinaison avec justification remplie.** Elle doit être refusée. Si elle passe, la garde de C n'est que celle de M1.
2. **Domination trajectoire par trajectoire.** Un tricheur exactement dans la famille du dénominateur doit avoir W ≤ 1 sur chaque trajectoire. Un dénominateur mélangé qui échoue à ce contrôle est exclu avant l'expérience 2.
3. **Balayage du champ `ce_qui_change`, vide ou rempli**, rapporté dans l'expérience 1. Sans ce balayage, H_A est déterminée par le banc.
4. **Une loi indexée par le temps** soumise à la garde sur sonde et au juge. Elle doit être vue d'au moins un des deux.
5. **Multiplicité par cellule** : même protocole qu'en A, contrôle 6.
6. **Un bras A/A et des bras qui ne diffèrent que d'un facteur** (garde seule, grille seule, contre-exemples seuls). Sinon, l'expérience 3 ne peut rien attribuer.
7. **Des témoins à proportion tirée au hasard, cachée, et indiscernables** (même test de discriminateur qu'en A, contrôle 4).

---

## Ce que je reprends, en le disant

- **De A** : la séparation entre deux problèmes. La redite d'une éliminée relève de la mémoire ; celle d'une survivante relève du juge. Je reprends aussi le dénominateur en **sup**, la seule forme valide des deux.
- **De C** : l'égalisation des jetons entre bras par un texte neutre.

Je réfute en revanche, chez l'un comme chez l'autre, l'idée qu'une orbite à paramètres fixes « ferme » le trou.

**Deux expériences communes, en inférence forte (B4).**

**X1 — Sup contre mélange au dénominateur** (processeur seul, code de J2, 1 000 répétitions, n = 200, K = 3, α = 0,05).
- H_A : le mélange bayésien garde la promotion d'un tricheur de la famille ≤ α.
- H_B : seul le sup tient ≤ α ; le mélange promeut au-delà de α.
- Issues : mélange ≤ α, et C-2 tombe ; mélange > α et sup ≤ α, et H_A tombe ; les deux > α, et l'argument de domination de A tombe aussi.
- Artefact qui doit être vu : le sup tronqué à un pas d'optimisation.

**X2 — Hors orbite** (même banc).
- H_A : l'extension à paramètres fixes, avec l'urne, garde ≤ α le tricheur « parent incliné par les poids d'une loi sans remise » sous calendrier déterministe.
- H_B : elle le promeut au-delà de α.
- Issues : H_A, et ma critique A-3 tombe ; H_B, et « fermeture exacte » tombe, aussi bien pour A que pour C.
- Prédiction signée (HYPOTHÈSE) : H_B, puisque l'écart d'environ 5,5 nats de J dépasse ln 20.

FIN-DE-CELLULE