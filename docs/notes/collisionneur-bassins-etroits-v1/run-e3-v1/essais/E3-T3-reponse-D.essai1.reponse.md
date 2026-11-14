# Proposition D — Tour III.3

Aucun résultat expérimental nouveau n’est disponible. Les corrections algébriques ci-dessous sont démontrées dans le texte ; elles ne rehaussent aucun statut des faits transmis. Les seuils de décision restent à préenregistrer, et toute valeur chiffrée ultérieure sera **illustrative** tant qu’elle ne proviendra pas d’un pilote indépendant.

## (a) Réponse aux critiques visant D

### Critiques de A

1. **A(a1) — alignement entre dictionnaire et générateur : acceptée.**  
   Le succès sur la seule composante de signe rapportée dans [C4] ne distinguerait pas une aide générale d’une coïncidence de conception. J’ajoute des mondes réservés : seuil de condition décentré, dépendance à trois traits, condition portant sur une transformée et effet continu non monotone. Leur alignement avec le dictionnaire sera mesuré hors ligne par l’oracle, sans modifier les vues après coup.

2. **A(a2) et A(b, M2) — orthogonalité sous traits dépendants : acceptée.**  
   Centrage et orthogonalité doivent être calculés sous une loi explicitement spécifiée, puis leurs résidus mesurés sous les lois publiques de traits retenues. Une non-nullité de ces résidus invalide l’interprétation « invisible en moyenne », pas nécessairement la couverture mécanique des questions. Les mondes additifs à traits corrélés deviennent un contrôle obligatoire.

3. **A(a3), A(b, puissance) et C(b3) — 96 appels présentés comme décisifs : acceptée.**  
   Je retire cette prétention. Leur calcul précis dépend du dessin retenu, mais la conclusion méthodologique est correcte : un pilote de variance ne peut pas être annoncé comme un duel décisif. L’effectif de l’essai décisif sera calculé à partir d’un pilote indépendant ; si le devis ne permet pas la précision requise, l’essai ne sera pas lancé sous ce nom.

4. **A(a4) et A(c2) — estimation de la largeur : acceptée.**  
   La classification portera sur les **paramètres d’une famille de générateurs**, estimés avec le témoin générique sur des mondes d’étalonnage distincts. Elle ne sélectionnera jamais des graines individuelles parce que le témoin y a échoué. Les graines décisives seront tirées après gel de la classification. La largeur restera une propriété estimée pour une famille, un modèle et une vue, non une propriété connue de chaque graine.

5. **A(a5) — fermeture du nul et puissance de M4 : acceptée avec sa condition exacte.**  
   Si la candidate \(q\) appartient au nul \(\mathcal N\), alors \(\sup_{P\in\mathcal N}p(X)\ge q(X)\), donc la construction par épisode donne \(e(X)\le1\). Un nul suffisamment fermé peut donc absorber précisément les alternatives recherchées. M4 ne sera retenu que si un contrôle positif démontre une puissance non triviale sur des composantes additionnelles à l’archive ; la validité sous \(H_0\) seule ne suffit pas.

6. **A(b, M3), B(a3), C(a4,b2,c3) — maximum sur strates bruité : acceptée.**  
   Les ordres de grandeur proposés restent illustratifs et dépendent d’hypothèses de queue, mais le défaut est réel. M3 cesse d’être un critère discriminant autonome : famille de strates gelée, tailles d’échantillon déclarées, incertitude simultanée et calibration sous des paires \(P=Q\) évaluées sur échantillons indépendants. Les permutations ne seront utilisées que lorsque leur échangeabilité est justifiée. Une strate trop peu échantillonnée sera déclarée **non estimable**, jamais positive.

7. **A(b, invalidité grammaticale) : acceptée.**  
   Le coût comprendra jetons d’entrée, génération, cartes invalides et calcul. Le taux de cartes valides et le coût par carte valide seront des critères gelés. Une différence d’invalidité assez grande pour expliquer l’effet rendra l’interprétation « exploration d’idées » non recevable.

8. **A(c1) — mondes hors dictionnaire : transformée en test.**  
   \(H_A\) : le gain brut persiste hors dictionnaire ; \(H_B\) : il disparaît ou s’inverse. Si \(H_B\) est retenue, l’hypothèse d’une exploration générale est réfutée ; il pourrait rester un effet spécialisé, à nommer comme tel.

9. **A(c3) — « condition verrouillée » : rejetée telle quelle, puis remplacée.**  
   Un parent sans effet marginal n’implique pas que toute promotion soit fausse : une interaction conditionnelle réelle peut exister sans amorçage archivé. Je distingue donc :
   - un monde **nul**, sans composante additionnelle, où toute promotion est une fausse découverte au sens de l’oracle ;
   - un monde à interaction réelle non amorçable, où la couverture et les erreurs sont comptées selon la composante effectivement plantée.

10. **Remarque transversale sur \(n\) : acceptée.**  
    La taille des tirages frais du juge sera gelée après une étude hors ligne de détectabilité. Elle ne sera pas ajustée pendant le duel. Profondeur oracle et détectabilité à ce \(n\) seront rapportées séparément.

### Critiques de B

1. **B(a1) — absence de mesure d’exécution des questions : acceptée.**  
   J’ajoute une mesure mécanique sur les cartes analysables : présence de la paire, de la strate ou de la condition assignée. Cette mesure ne juge pas la qualité sémantique et n’est servie à aucun agent. Une faible exécution identifiera un échec d’interface ; une exécution élevée sans gain brut rendra l’inutilité des questions plus directement testable.

2. **B(a4) et E(a1) — énumération insuffisamment spécifiée : acceptée.**  
   Le témoin énumératif entre dans le premier essai : mêmes questions publiques naïves, ordre lexicographique, affectation équilibrée sans remise, même nombre de lignes et budget de contexte apparié par remplissage neutre. Les affectations indépendantes avec remise et le placebo générique restent des témoins distincts.

3. **B(b1) — gain nécessairement borné par \(j/k\) : rejetée comme borne universelle, transformée en test.**  
   Des questions peuvent déclencher une recherche non prévue et les modèles conservent une probabilité spontanée de trouver d’autres composantes. En revanche, l’alignement entre composantes vraies et dictionnaire sera mesuré et testé comme modérateur. Une projection faible ne prouve pas à elle seule l’absence de contribution causale.

4. **B(b2) — grille sous-estimant le supremum : acceptée.**  
   Une grille dont le maximum est seulement inférieur au supremum ne certifie pas une e-valeur. M4 exigera soit un calcul exact sur une classe finie, soit une borne \(U(X)\) démontrée supérieure au supremum, avec \(e=q/U\). À défaut, M4 ne sera pas déployée.

5. **B(c2) — recombinaisons hors nul : acceptée avec une distinction.**  
   Elles entrent dans l’audit des fausses nouveautés au sens de l’oracle. Mais un monde hors \(\mathcal N\) ne contredit pas, à lui seul, la preuve \(\mathbb E_P[e]\le1\), qui ne vaut que pour \(P\in\mathcal N\). Validité statistique et nouveauté oracle resteront deux colonnes distinctes.

6. **Observation transversale de B : test accepté, dichotomie rejetée.**  
   Un criblage préalable des réponses aux vues est utile. Mais une hausse de `si_sinon` sur monde nul ne démontre pas une défaillance du juge, et une absence de changement des fréquences de formes ne démontre pas une loi de cartes inchangée : le contenu des conditions peut changer à forme constante. Le criblage portera donc sur les cartes complètes, leur validité, leurs conditions et leur couverture brute, pas seulement sur les six étiquettes grammaticales.

### Critiques de C

1. **C(a1) — scores paramétriques non définis pour toute la grammaire : acceptée.**  
   L’orthogonalité aux scores ne sera revendiquée que pour une extension paramétrique lisse explicitement écrite. Pour un `si_sinon` ou un `melange` sans telle extension, M2 se réduira à des statistiques de déformation définies directement, sans langage d’espace tangent.

2. **C(a2) — dépendance de \(h\) envers \(y\) et traduction non formalisée : acceptée.**  
   Aucun \(y\) observé ni simulation ne sera servi. Un traducteur déterministe \(T\), gelé avant les graines, associera à chaque direction un gabarit public du type « examiner si la pente résiduelle autour de la loi archivée change selon le signe de ce trait ». La fidélité mécanique de \(T\) est vérifiable ; son utilité pour un modèle reste une **HYPOTHÈSE**.

3. **C(a3) et C(c2) — confusion M1, M2 et M4 : acceptée.**  
   M4 est retirée du préalable du duel de vues. Le même juge, déjà qualifié, sera utilisé dans tous les bras. L’allocation M1 et le contenu M2 seront croisés : allocation indépendante ou équilibrée, dictionnaire naïf ou construit par moments. Aucun effet ne sera attribué à la géométrie à partir du seul bloc combiné.

4. **C(b1) — effondrement asymptotique général de M4 : partiellement rejeté, test accepté.**  
   Les coefficients et régimes asymptotiques annoncés ne valent pas sans hypothèses de complexité et de régularité supplémentaires. La possibilité d’une pénalité absorbant \(n r(A)\delta\), elle, est réelle. Je mesurerai la dérive logarithmique et la puissance sur une grille de \(n\), masses de région et profondeurs, avec la carte oracle comme contrôle positif.

5. **C(c1) — contrôle positif de M4 : acceptée.**  
   Si la vraie completion oracle n’atteint pas le seuil dans le régime annoncé détectable, M4 est inutilisable pour ce duel, même si tous ses contrôles nuls passent.

### Critiques de E

1. **E(a2) — variance conditionnelle : acceptée.**  
   La formule correcte, à loi des traits \(\mu\) conservée, est
   \[
   D_{\mathrm{KL}}(P_0\|P_\theta)
   =\frac{\theta^2}{2}\,
   \mathbb E_\mu[\operatorname{Var}_{P_0}(h\mid X)]
   +o(\theta^2).
   \]
   Si \(h=a(X)\), la normalisation annule la déformation : \(P_\theta=P_0\). Ces directions deviennent un contrôle négatif mécanique ; une variance conditionnelle nulle exclut la direction.

2. **E(a3) — témoins nuls différents par strate : acceptée.**  
   En effet,
   \[
   \max_A\inf_QD_A(P,Q)\le \inf_Q\max_AD_A(P,Q).
   \]
   Le membre gauche devient un profil descriptif d’incompatibilités locales, non une distance à un nul unique. Toute affirmation portant sur un nul commun utilisera le membre droit ou un \(Q\) commun explicite ; l’écart entre les deux sera rapporté.

3. **E(a4) — deux supremums possibles : acceptée.**  
   Les constructions par épisode et sur vraisemblance d’échantillon seront distinguées avant tout calcul. Pour cette dernière,
   \[
   e_n=\frac{q_n}{\sup_{Q\in\mathcal N}Q_n}
   \]
   est valide pour \(q\) fixé et le nul exactement couvert, sous le traitement usuel des supports. Puissance et approximation seront auditées séparément.

4. **E(b, métrologie) — appariement impossible d’une copie exacte : acceptée.**  
   Une copie exacte, de divergence globale nulle, sert au contrôle des fausses alertes avec reparamétrisations. L’appariement à distance globale non nulle égale se fera entre une **copie approchée** et un départ localisé réel.

5. **E(c) — imprécision de la non-infériorité : acceptée.**  
   Zéro incident observé ne démontrera rien. La garde exigera une borne supérieure d’excès de fausses promotions et de promotions de copies sous la marge préenregistrée, avec assez de mondes nuls et d’injections pour atteindre cette précision.

---

## (b) Expériences corrigées

### 1. Qualification hors ligne de M3 et M4, avant tout nouvel appel de proposeur

**M3.** Strates et nuls gelés ; copies exactes, reparamétrisations, copies approchées, départs localisés et paires \(P=Q\) sur échantillons indépendants.  
Duel : \(H_A\) « fausses alertes sous la tolérance et détection des départs localisés au-dessus de la puissance minimale » contre \(H_B\) « échec d’au moins une condition ». M3 est abandonné comme instrument quantitatif si \(H_A\) est réfutée ; il ne pilote dans tous les cas ni sélection ni consigne.

**M4.** Classe finie exacte ou borne certifiée du supremum ; contrôle nul dans chaque partie de \(\mathcal N\), copies, recombinaisons hors nul pour l’audit oracle, et cartes oracle positives.  
Duel : \(H_A\) « validité statistique **et** puissance minimale dans le régime déclaré détectable » contre \(H_B\) « validité insuffisante, calcul non certifié ou puissance insuffisante ». M4 ne rejoint le juge de la course qu’après succès et préenregistrement séparé.

### 2. Premier essai de vues : mécanisme sur cartes brutes

Une seule génération, sans M4 ni modification du juge. Dictionnaire, traducteur, vues, énumérateur et règles d’affectation sont scellés avant les graines. Les mondes comprennent : nul avec traits indépendants ou dépendants ; familles alignées large/étroit et peu profond/profond ; familles hors dictionnaire réservées.

Les bras croisent allocation M1 et contenu M2, avec placebo générique et énumération lexicographique. Coût total, contexte, modèle, décodage, archive et plafonds sont appariés. Les lectures sont : exécution mécanique des questions, validité, loi des conditions proposées, couverture oracle brute aux composantes et coût par carte valide.

Le contraste principal oppose \(H_A\) « le bloc sophistiqué bat à la fois l’énumération et le placebo d’au moins \(\delta\) sur la couverture brute étroite-profonde, sans pénalité excessive de validité » à \(H_B\), son complément. Un intervalle entièrement favorable réfute \(H_B\) ; un intervalle excluant le gain minimal réfute \(H_A\) ; un intervalle chevauchant le seuil réfute seulement le caractère décisif du dessin.

### 3. Essai de course, seulement après franchissement du mécanisme

Mêmes mondes appariés, coût mesuré égal, juge et \(n\) gelés, mondes et modèles réservés. Les trois étages D2 — brutes, représentants, retenues — sont obligatoires.  
\(H_A\) : gain minimal sur les **retenues**, avec borne de non-infériorité de la garde satisfaite ; \(H_B\) : gain inférieur ou garde dégradée. Monde nul, copies renommées, recombinaisons hors classe, placebo et strates permutées sont communs aux bras. Un gain limité aux cartes brutes ne justifie aucun déploiement ; un gain sans avantage sur l’énumération réfute l’utilité de la sophistication.

## (c) Réponse à l’arbitre, en une page

### Ce qui est établi

Par calcul seulement : un plan couvrant garantit la couverture de ses affectations, pas celle des idées ; la déformation conditionnelle fait intervenir la variance conditionnelle ; une candidate absorbée par le nul ne peut fournir une e-valeur robuste puissante ; un supremum approximé par défaut ne certifie pas la validité ; et le maximum de divergences locales avec un \(Q\) différent par strate ne mesure pas l’écart à un nul commun.

Il est également impossible d’obtenir un gain universel entre mondes indistinguables par la même vue publique, ou une certification absolue contre toutes les lois hors du nul spécifié. Un gain exige une structure exploitable : questions informatives, conditions publiques, archive séquentielle, expressibilité et détectabilité.

Empiriquement, rien de tout cela ne démontre qu’un modèle transforme ces indications en découvertes. La convergence de v67 est **RAPPORTÉE** pour une course ; la découverte de la composante conditionnelle par de vrais proposeurs est une **HYPOTHÈSE** ; le transfert causal des observations Bespoke n’est pas établi.

### Ce qui ne l’est pas

Ne sont ni établis ni plausibles au point de justifier un déploiement : la supériorité de M1–M2 sur une énumération simple, leur transfert hors dictionnaire, un gain après dédoublonnage et jugement, ou la non-infériorité de la garde à coût égal. M3 reste un diagnostic à calibrer. M4 reste suspendue à une preuve de calcul **et** à un contrôle positif de puissance. La largeur est une classification estimée par famille, non un bouton de l’oracle.

### Expérience à faire en premier

Le **criblage de mécanisme sur cartes brutes** décrit ci-dessus, et non la course coûteuse : bloc sophistiqué contre énumération lexicographique et placebo, à coût et contexte appariés, avec mondes nuls, traits dépendants et structures hors dictionnaire. Il teste directement le maillon sans lequel toute la méthode est vide : les vues changent-elles les cartes de façon assez ciblée pour couvrir davantage de composantes certifiées, sans simplement accroître l’invalidité ou les conditions fabriquées ?

Je changerais d’avis contre M1–M2 si l’énumération les égale, si le gain disparaît hors dictionnaire ou aux étages de représentants et retenues, ou si la garde ne peut être bornée avec la précision requise. Je ne soutiendrais un essai de course plus coûteux qu’après un mécanisme reproduit et une qualification indépendante du juge.

FIN-DE-CELLULE