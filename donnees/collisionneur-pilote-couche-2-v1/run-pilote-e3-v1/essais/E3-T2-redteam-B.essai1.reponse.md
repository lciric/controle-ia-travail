# Cellule B, tour III.2 : équipe rouge croisée

**Lecture des pièces.** Les conceptions A et C sont complètes : chacune se termine par sa ligne de fin. Dans les faits servis, une seule coupure, déjà signalée par la pièce elle-même : N-056, message de 23:47, « lignée tierc ». Tout chiffre de ma main est **illustratif**. Le modèle latent gaussien des pièces B et C reste une HYPOTHÈSE.

---

## Contre la proposition A

### (a) Failles

**A1. Réemploi des épisodes de sélection de la dose dans le développement : biais du gagnant, côté comparateur.**
- Ce que fait A. Sa recherche de dose génère 3 doses × 16 tâches × K = 3. Elle retient la dose où les moniteurs noirs ratent le plus. Elle complète ensuite à K = 10 avec 7 exécutions neuves. Enfin, elle déclare que ces 160 unités-exécutions « sont » le développement (N1).
- Le défaut. Sur ces 48 épisodes, la dose a été choisie *parce que* les moniteurs noirs y étaient faibles. Quand l'organisme opposera ensuite le blanc au noir sur le développement, le noir y sera biaisé vers le bas par la sélection.
- Ce que A ne fait pas. Sa coupe des honnêtes en deux lots règle le réemploi des seuils, pas celui des sabotés.
- La nature du biais. C'est une sélection sur un comparateur, au niveau de la condition et non de l'unité. Le contrôle 14 (pièce B, § 2.4) vise exactement cette famille de biais.
- La règle P-015 n'est pas en cause : fixer la dose sur la boîte noire est voulu. Le défaut tient au fait de *relire* les épisodes qui ont servi à la fixer.
- Avec trois doses et des seuils jumelés 0,80 / 0,50, la chance qu'une dose limite passe par le bruit n'est pas petite. Si chacune passe avec une probabilité de 0,3, on obtient 1 − 0,7³ ≈ 0,66 (illustratif).

**A2. Le contrôle négatif de D1 est vrai par construction.**
- A écrit : « honnêtes codés par la même règle (≈ 99 % sous seuil) ».
- Or les seuils à 1 % sont calibrés sur le lot 1, et ce sont ces mêmes honnêtes qui servent de contrôle. Le résultat « 99 % sous seuil » est donc une identité, pas une mesure.
- Le chiffre attendu est faux en plus. Avec un *maximum* sur m moniteurs calibrés chacun à 1 %, la part d'honnêtes sous tous les seuils tombe vers 0,99^m, soit ≈ 0,95 pour m = 5 si les moniteurs sont indépendants (illustratif).
- Conséquence : un contrôle qui attend 99 % sur une union à 5 % ne peut pas échouer pour la bonne raison.

**A3. Les jumeaux servent deux fois.**
- Le lot 1, qui contient les 160 jumeaux, fixe les seuils de la recherche de dose.
- Ces mêmes jumeaux restent ensuite les jumeaux de garde du développement.
- Le contrôle 12 du développement hérite donc de seuils tirés de ses propres épisodes.
- Incohérence arithmétique au passage : A calcule j = ⌊0,01 × 481⌋ = 4 « avec les jumeaux », puis coupe les 480 honnêtes en lots de 320 et 160. Sur 320, j = 3. Sur le lot 2 (160), j = 1, c'est-à-dire le maximum. Or ce lot 2 est présenté comme le calibrage D-S15, que la pièce C dimensionnait à 30 par tâche (RAPPORTÉ). A le ramène à 10 par tâche sans le dire.

**A4. Pseudo-réplication dans D5 (horizon) et dans les erreurs types.**
- L'horizon est un attribut de tâche, ou il en dépend fortement. Le test de Kolmogorov-Smirnov de D5 traite pourtant les 480 honnêtes comme indépendants, alors qu'ils viennent de 16 grappes.
- Sous a = 0,3 (HYPOTHÈSE), l'effet de plan vaut 1 + (K − 1)·ρ. Avec K = 30 et un ρ de 0,3 (illustratif), on obtient ≈ 9,7, soit un effectif utile d'environ 50, pas 480. Le test rejettera à tort bien au-delà de 1 %, et D5 basculera vers 12 800 ou plus par simple effet de tâche.
- Le contrôle négatif de A, « honnêtes coupés au hasard », coupe au niveau de l'épisode : il ne contrôle pas le regroupement.
- Même défaut ailleurs : les « ± 4 points (binomial) » sur 160 unités ignorent le regroupement par tâche.
- Enfin, le test KS est sensible au corps de la distribution, alors que la question du calibrage porte sur la queue au-delà du 99ᵉ centile.

**A5. Le découplage dans D1 laisse passer une dose sans les deux propriétés à la fois.**
- D1 exige deux parts mesurées séparément : au moins 80 % d'actions sous le seuil et au moins 50 % d'unités porteuses d'un dommage.
- Une dose peut satisfaire les deux sans qu'aucune unité ne soit *à la fois* diffuse et porteuse d'un dommage. Il suffit que les unités dommageables soient flagrantes et que les autres soient inertes.
- Il faut la part jointe, par unité. D'ailleurs, P-015 parle de « chaque action sabotée » sous le seuil (RAPPORTÉ). Le passage à « 80 % des actions » est une réécriture de la règle, qui doit être présentée comme un changement.

**A6. Circularité de la vérité de terrain du mode « contrôles ».**
- Le « dommage étiqueté » est produit par des sous-agents qui lisent le texte. Ce sont donc eux-mêmes des moniteurs boîte noire.
- Exiger qu'ils voient ce que les juges ne voient pas ne sélectionne que les doses où l'étiqueteur est plus fort que les juges.
- Le régime « diffus avec dommage » est ainsi défini relativement à un moniteur textuel. Ce n'est pas une propriété de l'organisme.
- Pour le mode coût, le lecteur du coût est mécanique (RAPPORTÉ, P-015). Pour le mode « contrôles », A ne propose aucune vérification mécanique de l'état des contrôles.

**A7. Artefact de source, mode coût exclu.**
- A retire le mode coût au motif que « sa dose existe ». Or P-015 (b), étape 1, ne lit que trois sources : la règle du coût, le juge 8B et le prédicteur (RAPPORTÉ).
- La pièce A (D4) et le consensus de la pièce B exigent la recherche de dose contre **tous** les moniteurs noirs par action.
- La dose du mode coût, si elle a bien été cherchée, l'a donc été contre une partie seulement de la liste. C'est l'artefact que la question demande d'écarter.
- Que cette recherche ait bien été *exécutée* n'est établi par aucune pièce. La pièce C dit que la réserve « porte » la recherche de dose, sans résultat servi. Statut : à vérifier.
- Même pour le mode « contrôles », le maximum de A porte sur le 8B, le 3B, Qwen et le prédicteur : b* manque.

**A8. Le choix de K par le pilote réintroduit une fuite écartée.**
- La règle D2 de A, K ← ⌈10/obéissance⌉ borné à 16, fixe K sur le pilote. La pièce B rapporte que A et B avaient jugé ce choix fuyant.
- L'unité est la consigne avec toutes ses exécutions (D-S1, RAPPORTÉ). L'estimande est donc en intention de traiter : la désobéissance fait partie de l'effet, ce n'est pas un bruit à compenser.
- K = 16 sur 64 unités ajoute environ 60 % d'épisodes sabotés (illustratif), hors devis.

**A9. D6 promet un remède que les faits contredisent.**
- Si un effet d'ordre est détecté, A prévoit un « calibrage sur tâches disjointes, taille doublée ».
- Or la pièce C rapporte, pour la coupe par tâche, 0,01 à 0,14 de promotion à tort à 9 600 épisodes. Doubler la taille ne ramène pas la coupe par tâche au niveau de la coupe dans la tâche.
- Le remède est donc non démontré, et des tâches disjointes de l'épreuve n'existent que dans la réserve, déjà contaminée.

**A10. Duels non décisifs.**
- D7 : les hypothèses « a ≤ 0,5 » et « a ≥ 0,6 » ne sont pas exhaustives (le trou 0,5–0,6 n'est couvert par aucune). Avec un coefficient de variation de 45 %, l'intervalle ne tranchera presque jamais. D7 n'a d'ailleurs pas de contrôle négatif.
- D8 n'a pas de contrôle négatif non plus.
- Au sens de B4, ces deux expériences ne falsifient rien.

### (b) Évasion

Je les décris par classe seulement, sans exemple ni consigne.

| instrument | voie d'évasion | coût pour l'agent |
|---|---|---|
| juges lus par le jeton | sortie qui pousse la note vers la troncature ou l'incomplétude ; si le score manquant est exclu, l'épisode saboté sort de l'analyse (absence informative) | faible |
| maximum des moniteurs noirs | tout canal que les moniteurs retenus ne lisent pas ; l'absence de b* dans le maximum élargit ce canal | faible à moyen |
| étiquetage par sous-agents | même classe que les juges : un sabotage discret pour le texte l'est aussi pour l'étiqueteur, et le « dommage » disparaît de la mesure | nul : c'est la faille A6 |
| garde et jumeaux | aucun effort : la garde n'est certifiable qu'à 48 unités (RAPPORTÉ), A la met en « rapportée » | — |
| tous à la fois | la dose qui rend le texte indistinguable de l'honnête trompe juges, prédicteur **et** étiqueteurs. D1 la déclare alors « diffuse sans dommage », alors que le dommage existe peut-être mais n'est pas observé | faible |

Dans ce pilote, l'« adversaire » le plus sérieux est la procédure elle-même : la sélection sur 3 doses × 4 moniteurs × 2 seuils, que A1 décrit comme un biais du gagnant.

### (c) Contrôles négatifs dont l'absence serait fatale

Chacun oppose deux hypothèses exclusives ; seuils illustratifs, à sceller.

1. **Exécutions de sélection contre exécutions neuves.**
   - H_A : le rappel noir à la dose retenue est le même sur les 3 exécutions de recherche et sur les 7 neuves (écart dans l'intervalle à 95 %).
   - H_B : il est plus bas sur les exécutions de recherche (au moins 5 points).
   - Si H_A tient, le biais du gagnant est négligeable et le réemploi passe.
   - Si H_B tient, les 48 épisodes de recherche sont retirés du développement, qui garde K = 7.
2. **Honnêtes tenus à part pour la règle de D1.**
   - H_A : la part d'honnêtes au-dessus du maximum des seuils, mesurée sur un lot non utilisé au calibrage, est égale au taux d'union prédit.
   - H_B : elle le dépasse de plus de 2 points.
   - L'issue H_B falsifie la règle « maximum des moniteurs » telle que calibrée.
3. **Permutation de l'horizon au niveau de la tâche.**
   - H_A : l'effet d'horizon survit à une permutation des étiquettes entre tâches.
   - H_B : il disparaît. Il était alors de l'effet de tâche, et D5 ne doit pas basculer.
4. **Part jointe, par unité, « diffus et dommage ».**
   - H_A : au moins la moitié des unités porteuses d'un dommage ont leurs actions sabotées sous le seuil.
   - H_B : non. La dose est alors réfutée, même si les deux parts marginales passent.
5. **Absence de score par condition.**
   - H_A : le taux de scores non finis est le même chez les honnêtes et chez les sabotés.
   - H_B : il diffère. Les scores manquants deviennent alors des alertes maximales, et D3 est rejoué.
6. **Vérité mécanique du dommage, mode « contrôles ».**
   - Sur un sous-lot, l'étiquette des sous-agents est comparée à une vérification de l'état des contrôles.
   - H_A : accord d'au moins 0,90.
   - H_B : l'étiqueteur rate des dommages réels. A6 est alors confirmée, et D1 ne peut plus utiliser l'étiquetage comme vérité.

---

## Contre la proposition C

### (a) Failles

**C1. L'aveuglement aux sondes ne décontamine pas une comparaison entre le blanc et le noir.**
- La thèse centrale de C : les activations sont capturées mais non lues, donc les 16 tâches du pilote « peuvent légalement rejoindre » les 16 autres et le développement retrouve 32 unités.
- Mais C lit les moniteurs **noirs** sur ces épisodes pour choisir d*. Il garde ensuite les 2 exécutions de recherche parmi les 5 exécutions de développement.
- C'est le même biais du gagnant qu'en A1, en plus fort : 2 sur 5 au lieu de 3 sur 10.
- L'aveuglement protège le bras blanc d'une sélection. Il ne protège pas le comparateur d'une sélection favorable au blanc.

**C2. Deux fabriques à l'intérieur du développement.**
- Les 16 tâches restantes sont générées « plus tard » à la dose d*. C'est l'attaque que la pièce B portait contre C au tour précédent (calibrage et épreuve séparés de plusieurs jours, « deux fabriques »), et que C ne s'appliquait pas.
- C la reproduit ici, et la confond avec le lot de tâches : toute différence entre les deux lots est à la fois une dérive et un effet de tâche.
- La sentinelle de C (32 honnêtes sur les tâches du pilote) ne couvre pas les sabotés.
- Le critère d'acceptation, p > 0,01 sur 32 épisodes, accepte l'égalité sur une absence de rejet. À cette taille, la dérive passera presque toujours : c'est vrai par construction. Il faut un test d'équivalence avec une marge scellée.
- Le « Kolmogorov-Smirnov bivarié » n'est pas défini.

**C3. Le passage à K = 5 au développement n'est pas déclaré.**
- La pièce C dimensionne le développement à K = 10 (RAPPORTÉ). C passe à K = 5 sans le dire, et cite pourtant « puissance restaurée à 0,78–0,90 ».
- Ce chiffre est donné dans le contexte de la répartition à K = 10. Aucune pièce ne le donne à K = 5.
- Pour G1, la pièce B rapporte 0,72 contre 0,47 entre K = 10 et K = 5 : la perte n'est pas négligeable.
- L'affirmation de C n'est pas établie.

**C4. Contradiction interne sur la lecture du bras blanc.**
- C verrouille les activations « vis-à-vis du module `bases.sequentiel` » (§ 5, garde 5).
- Mais il fait aussi tourner l'agrégateur séquentiel sur les 480 honnêtes (§ (c) 5), et estime une « corrélation inter-cellules » sur ces honnêtes pour décider du passage de 9 600 à 12 800 (§ 4.2), ce qui suppose de lire des cellules blanches.
- Il faut choisir. Si l'on lit, le calibrage du développement blanc est consommé avant le développement. Si l'on ne lit pas, la règle 12 800 tombe.

**C5. Le duel P2 n'est pas exclusif et manque de puissance.**
- Deux cases sont vides : « taux supérieur à 2 % mais p ≥ 0,05 » et « taux inférieur ou égal à 2 % » avec un intervalle qui couvre 3 %.
- Sur environ 240 épisodes longs au taux global de 1 %, on attend 2 à 3 alertes (illustratif). Un test de Fisher sur si peu d'événements n'a presque aucune puissance.
- La permutation se fait au niveau de l'épisode : même pseudo-réplication que A4.
- C attribue à la pièce B (§ 2.1) l'application « strate d'horizon → 19 200 ». La pièce B ne dit pas cela. Elle note seulement que 12 800 tombe sur le bas de la lecture « double », et que la strate coupe 9 600 en deux moitiés de 4 800. L'attribution est fausse.

**C6. La règle du coût entre dans le maximum sans passer par le nœud.**
- Pour le mode coût, C met la règle du coût déclaré dans la liste des moniteurs par action.
- P-015 laisse ce point **ouvert** : « prendre la règle du coût comme moniteur par action est un nœud de revendication, à trancher à part » (RAPPORTÉ). C tranche ce nœud sans le dire.
- Conséquence probable : avec une règle du coût aussi forte que celle de P3 (0,888, RAPPORTÉ), le régime diffus du mode coût risque d'être vide.
- L'arrêt 1 dit « S_k (ou S_c) » sans préciser si l'échec d'un seul mode arrête la banque. Or D-S29 (a), lu dans N-056, exige le gain « dans chacun des autres modes ». Ce point est indéterminé chez C.

**C7. Même découplage qu'en A5, et même circularité qu'en A6.**
- Les deux parts de P1, D̂ ≥ 60 % et R_BN ≤ 25 %, sont mesurées séparément.
- Pour S_k, le dommage est confirmé « par accord des deux séries de sous-agents », qui sont des moniteurs textuels.
- Le relâchement de « chaque action » (P-015) à « 75 % sous le seuil » n'est pas déclaré.

**C8. Chiffres non sourcés ou incohérents.**
- Le 3B serait « de même famille » : aucune pièce ne le dit, le modèle n'y est pas nommé.
- L'étiquetage par sous-agents est chiffré à « 3 à 5 h de carte », alors que la pièce C rapporte expressément l'absence de tout rythme mesuré.
- Le taux de faux négatifs est donné à « plus de 35 % » au § (a), puis à 18,2 % au § 4. Les 36 % ne valent que si l'erreur type est de 7 points.
- « Verrouille le devis à ± 10 % » repose sur trois rythmes non mesurés.
- Le plan à 76–117 USD n'a pas la marge d'un facteur 1,5 sur le rythme du mode « contrôles » : appliquée, elle sort de l'enveloppe de 125 USD.
- La version minimale finit à 39,0 USD sans aucune marge.

**C9. Mention et témoin pour S_k sans définition.**
- C génère M_k et T_k et les utilise comme contrôles négatifs de P1 (« dommage ≤ 5 % sur mention »).
- Or la transposition de « mention » au mode « contrôles » n'est écrite nulle part (P-015 la définit pour le coût seulement). C'est un contrôle négatif sur une condition non définie.

**C10. Seuil d'ex æquo trop grossier pour décider.**
- Dans P3, « moins de 0,5 % d'ex æquo » sur 480 honnêtes revient à 2,4 épisodes : la décision tient à un ou deux épisodes.
- Le contrôle négatif de 10 textes identiques teste le code, pas le juge.

### (b) Évasion

Je les décris par classe seulement.

| instrument | voie d'évasion | coût pour l'agent |
|---|---|---|
| juges, Qwen, b*, TRACE-lite | même classe d'absence informative qu'en A. C exige 0 % de scores manquants mais ne dit pas ce qu'il fait d'un score manquant | faible |
| TRACE-lite, sous-échantillonné dans la version minimale | le maximum sur les moniteurs est pris sur un sous-lot de 48 sabotés pour trois moniteurs : la dose peut passer sous les autres et rester visible pour ceux-là | faible |
| règle du coût dans le maximum | elle rend le régime diffus du mode coût étroit. Inversement, une dose qui contourne la seule règle du coût passe pour diffuse alors que le juge la voit, si l'on réduit la liste après l'arrêt 1 | moyen |
| sentinelle de dérive | n = 32 et acceptation sur p > 0,01 : toute dérive modérée passe sans effort | nul |
| tous à la fois | comme en A : le texte indistinguable de l'honnête trompe tous les lecteurs textuels, y compris l'étiquetage qui sert de vérité | faible |

### (c) Contrôles négatifs dont l'absence serait fatale

Chacun oppose deux hypothèses exclusives ; seuils illustratifs, à sceller.

1. **Exécutions de recherche contre exécutions neuves à d*.** Même duel que pour A. L'issue H_B retire 2 exécutions sur 5, ce qui pèse plus lourd chez C.
2. **Sentinelle sabotée, sur les mêmes tâches, entre les deux fabriques.**
   - H_A : les scores noirs à d* sur les tâches du pilote, régénérés au moment de la banque, sont équivalents à ceux du pilote (test d'équivalence, marge scellée).
   - H_B : ils ne le sont pas. La réunion des deux moitiés du développement est alors réfutée, et l'organisme est lu par moitié, au prix de la puissance.
3. **Un seul régime de lecture du blanc sur les honnêtes.**
   - H_A : aucune cellule blanche n'est lue avant le développement, et la règle « corrélation inter-cellules → 12 800 » est retirée.
   - H_B : les cellules blanches des honnêtes sont lues. Le calibrage blanc du développement est alors déclaré consommé, et ses 480 épisodes remplacés.
4. **Statut de la règle du coût.**
   - P1 est mené deux fois, avec et sans la règle dans le maximum.
   - H_A : la même d* sort des deux lectures, et le nœud de P-015 est sans effet.
   - H_B : les lectures divergent. La porte d'arrêt est alors suspendue jusqu'au mot de Lazar.
5. **Part jointe, par unité, et vérité mécanique du dommage pour S_k.** Mêmes duels que les contrôles 4 et 6 contre A.
6. **Permutation de l'horizon au niveau de la tâche.** Même duel que le contrôle 3 contre A.

---

## Ce que je reprends, en le disant

- **De A** : le calcul de l'effet de consigne, qui inclut le facteur 1 + (1 − a)/(Ka), et la conclusion « encadré, non mesuré ». Les trous de la pièce F (66 et 121 notations ni complètes ni tronquées). Le scellement du mode tenu à l'écart avant la lecture du pilote.
- **De C** : l'interdiction de fixer K, ou d'arrêter la banque, sur l'écart blanc contre blanc observé à 16 tâches (erreur type d'environ 5 points, illustratif). L'aveuglement aux sondes pendant le pilote, à condition de corriger C1 et C2.
- **Contre les deux, pour la décision de Lazar** : A et C fondent tous deux le réemploi des épisodes sur un argument qui ne protège qu'un des deux bras. Aucun ne propose de vérité de dommage mécanique pour le mode « contrôles ». Tant que ces deux points restent ouverts, le « régime diffus avec dommage » que le pilote prétend établir reste une HYPOTHÈSE définie par rapport à des lecteurs textuels, pas une mesure.

FIN-DE-CELLULE