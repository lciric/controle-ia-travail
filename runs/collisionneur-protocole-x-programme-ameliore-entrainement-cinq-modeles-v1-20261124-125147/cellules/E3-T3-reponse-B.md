# Proposition B, tour III.3 : réponse aux critiques

**Pièces.** Ma conception du tour III.1 et les quatre critiques croisées (A, C, D, E) sont reçues entières. Chacune est close par `FIN-DE-CELLULE`. Je ne réponds qu'aux sections « Sur la proposition B ». Dans la pièce C, je ne traite que cette section, pas les §1 à §7 qui exposent son propre plan. Les seuils et effectifs repris des critiques gardent leur statut « illustratif ».

---

## (a) Verdict sur chaque critique

Les critiques qui disent la même chose sont regroupées. Pour chaque groupe, la source est indiquée.

| # | Source | Critique | Verdict | Conséquence |
|---|---|---|---|---|
| 1 | A(a1), D(a, c1), E(c4) | Le témoin bénin n'est pas apparié en amplitude du déplacement. Un seul adaptateur bénin donne une variance inter-fabrication à zéro degré de liberté. | **Acceptée, transformée en test** | C1′ : série graduée de plusieurs adaptateurs bénins. L'unité de réplication est la fabrication, pas l'épisode. Je n'impose pas d'appariement forcé en divergence KL, car C note, à propos de E, qu'il peut retirer une partie du phénomène. J'analyse plutôt sur la zone de recouvrement des amplitudes. |
| 2 | A(a2), C(a), D(a, b1), E(a, b) | Le témoin du dernier jeton du message système est asymétrique : l'égalité condamne, l'inégalité n'absout pas. Il est inapplicable à l'adaptateur, qui ne porte pas de consigne (VÉRIFIÉ). Projeter `w` sur une position d'un autre rôle n'a pas de sens. Les variances du score sur un jeton et sur dix pas ne sont pas commensurables. | **Acceptée, transformée** | Le témoin ne tranche plus rien. Il devient descriptif : une sonde réapprise aux positions du message système, qui contraste saboteur et bénin de même procédé au même jeton, dans les deux familles. Le verdict « la sonde lit le texte » passe au lecteur sans état (ligne 3). |
| 3 | A(intro, c) ; réserve de D sur A | Il faut un contrôle « lecteur sans état ». | **Acceptée, reprise de A** | Je l'adopte avec la réserve de D : la sonde est réapprise sur les activations du modèle de base qui relit la transcription, jamais projetée depuis l'agent. Il entre en C3′. |
| 4 | E(a1) | C3 exige une famille inédite, alors que C9 est différé et que C1, C2 et C7 lisent les deux familles existantes. | **Acceptée sur le fond, nuancée sur la règle** | La règle de lecture unique (VÉRIFIÉ) vise la reconception d'une sonde. Sans reconception, C3 sur des articles tenus à l'écart ne la viole pas, mais ne peut rien dire du transfert. Or C1 rend une reconception probable. Correction : une famille scellée F_s, décrite en (b). |
| 5 | A(a3, b), D(b3), E(a, b) | C2 n'a pas d'échelle d'entraînement. Le jumeau de référence est ambigu : le jumeau gelé donne une « survie » artificielle, le jumeau entraîné un « effondrement » artificiel. L'estimateur en rapport est instable. La puissance est bornée par le nombre de graines G, quel que soit le nombre d'articles. | **Acceptée** | Échelle fixée par un étalon (un adaptateur à trait bénin mesurable). Estimateur en différence de différences sur articles disjoints. Garde de plancher sur la qualité honnête absolue. Unité de réplication : la graine d'entraînement, avec issue rapportée graine par graine. |
| 6 | A(a4), E(a) | Le témoin à consigne en C2 n'est pas défini : on ne sait pas si la consigne est présente pendant l'entraînement. Il mesure l'obéissance, pas la tenue d'une politique inscrite dans les poids. | **Acceptée** | Retiré du duel C2′. Il pourra être mesuré, mais à titre non décisif. |
| 7 | A(a5), E(b, sur max-AUC) | Les « meilleurs » comparateurs sont choisis sans règle, d'où un risque de fuite ou de biais du maximum. | **Acceptée** | Comparateurs gelés au préenregistrement et choisis sur une partition de développement. Tous les comparateurs sont rapportés sur la partition de test. |
| 8 | A(b), C(b), D(b4), E(b) | Le délai médian est indéfini si P(détection dans l'horizon) < 1/2. La « dose minimale détectable » n'est pas identifiée entre les doses observées. | **Acceptée** | Analyse de survie censurée. Métrique primaire : P(τ ≤ h). Résultats donnés par dose observée, sans interpolation. |
| 9 | A(b), E(b) | Comparer à α nominal égal mesure la tension de la borne, pas l'information du score. Le quantile empirique a une variance non nulle. | **Acceptée** | Comparaison à α réalisé égal, sur des flux honnêtes tenus à l'écart. La marge préenregistrée doit dépasser l'erreur du quantile. |
| 10 | A(b), C(b) | Un écart d'AUROC ne montre pas un apport interne. La grandeur utile est I(S ; Z \| T). | **Acceptée** | En C3′, métrique secondaire : le gain de vraisemblance du classifieur sur (T, S) par rapport à T seul. |
| 11 | A(a6), C(b), D(a, b5), E(a, b) | C4 confond la guérison du saboteur et la destruction de la sonde. Les traces du modèle de confiance changent la capacité. Les saboteurs publics retrouvent leur capacité après un réglage fin sur traces bénignes (VÉRIFIÉ). | **Acceptée, avec une réserve de statut** | D attribue un VÉRIFIÉ à la faiblesse du modèle de confiance du programme en citant le papier de 2026. Les faits ne décrivent pas le modèle de confiance du programme. Le confondant tient quand même, puisqu'il s'agit d'un modèle distinct. Correction : auto-distillation, et un duel principal sans classe positive (ligne 22 et C4′). |
| 12 | E(c1) | Conditionner C4 aux organismes dont le sabotage survit. | **Rejetée au niveau de la graine ou de l'épisode, acceptée au niveau du bras** | Retenir les graines survivantes d'après le dommage mesuré ferait entrer une sortie de l'oracle dans la sélection d'un agent, ce qu'interdit une règle VÉRIFIÉE. C fait la même objection à A. Le volet « séparation » de C4′ ne se lit que si le bras entier garde un dommage, selon une règle préenregistrée, sans tri des graines. |
| 13 | A(a7, b), C(a, b), D(a, b6), E(a, b) | C5 cumule plusieurs défauts : journaux réutilisés, π choisi par l'expérimentateur, « première confirmation » géométrique et sensible aux faux positifs de l'oracle (Cov(π(S), p₀(S)) > 0), confusion entre trouver un cas et resserrer une borne, élargissement de la borne quand le budget est scindé. | **Acceptée** | C5′ est redéfini sur une décision : établir un excès de dommage au-dessus du taux honnête de référence. Il compare l'aiguillage à un placebo de mêmes probabilités inégales, sur R flux, avec un flux à π = 0. |
| 14 | C(a, b) | Une erreur réelle d'un honnête n'est pas une fausse alerte de dommage. | **Acceptée, c'était une erreur de ma part** | Les paires honnête contre honnête mesurent le taux honnête de référence, et non des « fausses alertes ». |
| 15 | A(a8) | Le critère de réfutation de P2 est mal posé : la co-évolution du dommage et de la séparation y est déclarée « sans contenu », alors que c'est l'issue où la sonde validerait un entraînement. | **Acceptée** | P2 est réécrit en (b). |
| 16 | C(a) | Réapprendre la sonde sur la famille inédite ne la teste pas sur cette famille (P3). | **Acceptée** | La sonde est réapprise sur une partition d'apprentissage et évaluée sur une partition tenue à l'écart. |
| 17 | A(a9), D(a, b2) | En C8, les erreurs sont corrélées si un même juge produit les deux lectures. L'échantillon n'est pas stratifié par dose. | **Acceptée** | La référence vient d'une autre classe de lecteurs que l'oracle. Stratification par dose, avec puissance calculée à la plus faible dose. |
| 18 | A(b), C (convention « indécis ») | Grappes par article (n_eff). Sans calcul de taille préalable, l'issue « indécis » domine. | **Acceptée** | Le calcul de taille est préenregistré avant toute lecture. Si un test est non jugeable aux effectifs disponibles, on le déclare avant de le lancer. |
| 19 | E(a) | En C1, les deux hypothèses n'épuisent pas les issues (sonde nulle partout). Les seuils de C2 à C4 n'ont pas de forme. | **Acceptée** | Hypothèses réécrites pour être exhaustives à une marge près. « Indécis » est une issue déclarée, qui bloque l'étape suivante. |
| 20 | D(a) | Pas de partition entre l'étalonnage du seuil et le test. | **Acceptée** | Partition des articles en trois blocs (apprentissage, étalonnage, test), scellée. Je reprends l'idée de C, que A crédite. |
| 21 | A(c), E(c5), D(c4) | Contrôles manquants : honnêtes sur questions plus difficiles, sonde à étiquettes permutées, flux honnête de difficulté hétérogène, flux à π = 0. | **Acceptés** | Intégrés aux contrôles de C1′, C3′ et C5′. |
| 22 | C(b), E(b) | En C4, l'AUROC peut rester constante pendant que le taux d'alerte au seuil gelé change. Les deux métriques peuvent entrer en conflit. | **Acceptée** | Métrique primaire : le taux de fausses alertes au seuil gelé, qui porte la garantie. L'AUROC devient secondaire. |

---

## (b) Expériences corrigées

Tous les seuils, marges, effectifs et coûts sont **illustratifs**, à fixer au préenregistrement. Les coûts sont comptés en courses ; le fait VÉRIFIÉ est seulement qu'une course coûte quelques dizaines de dollars. Toute expérience décisive est préenregistrée (règle VÉRIFIÉE).

### Préalables, avant toute lecture

- **P-a. Partition et puissance.**
  - Les articles sont répartis en trois blocs scellés : apprentissage, étalonnage, test.
  - Le calcul de taille repose sur σ₀ (honnête contre honnête), ρ_c (corrélation intra-article) et le nombre d'articles. Je ne connais pas ce nombre.
  - Ce qui est non jugeable est déclaré tel avant de lancer.
- **P-b. Famille scellée F_s** (correction de la ligne 4).
  - Un contenu de sabotage différent de celui des deux familles existantes, fabriqué dans les deux formes (consigne et adaptateur) selon une procédure automatisée préenregistrée.
  - Scellé avant la lecture de C1′, idéalement par un tiers, sans inspection humaine des transcriptions. Je reprends ce point de la critique de D sur E.
  - **Limite** : F_s est une fabrication du programme. Elle teste le transfert à un nouveau contenu de sabotage, pas le transfert hors fabrication connue. Seule la troisième famille sans texte, ou une famille extérieure, le testerait.
- **Point à trancher par le directeur.** C2′ et C4′ modifient les poids du modèle soupçonné à des fins de mesure. Aucun score de moniteur ni sortie de l'oracle n'entre dans leur signal : je les lis comme conformes. Les critiques montrent cependant que les propositions divergent sur ce point. Je demande une décision écrite. Si le directeur y voit un changement de règle, je le déclare comme tel.

### C1′. Signal de sabotage ou artefact de modification

- **Montage.**
  - Plusieurs adaptateurs bénins (nombre illustratif) fabriqués par le même procédé, à partir de consignes bénignes graduées en contrainte. Leur amplitude couvre celle des quatre doses.
  - L'amplitude est mesurée par la norme du déplacement d'activation et par la divergence des sorties, sur des entrées fixes.
  - Même construction pour la famille à consigne : une série graduée de consignes bénignes.
- **H_A** : à amplitude égale, dans la zone de recouvrement, le taux d'alerte du saboteur dépasse celui de la courbe bénigne de plus de m₁.
- **H_B** : l'excès est inférieur ou égal à m₁ ; l'alerte s'explique par l'amplitude de la modification. Une sonde nulle partout tombe dans H_B.
- **Métrique.**
  - Taux d'alerte au seuil fixé sur le bloc d'étalonnage honnête.
  - Écart vertical entre le saboteur et la régression bénigne alerte ~ amplitude, avec un intervalle qui traite la fabrication comme unité.
- **Issue non jugeable.** Si les amplitudes des saboteurs sortent du support bénin, l'issue est « non jugeable ». Elle n'est jamais lue comme H_A.
- **Contrôles négatifs.**
  - Paires honnête contre honnête de graines différentes.
  - Honnêtes sur des questions plus difficiles.
  - Sonde apprise sur des étiquettes permutées.
- **Volet descriptif, non décisif** : une sonde réapprise aux positions du message système, qui contraste saboteur et bénin de même procédé.
- **Ce qui réfuterait H_A** : une courbe bénigne qui rejoint les saboteurs à amplitude égale.
- **Coût** : une à deux dizaines de courses (illustratif).

### C2′. L'organisme est-il un témoin valide ?

- **Montage.**
  - L'échelle d'entraînement est fixée par un étalon : un adaptateur de même procédé qui porte un trait bénin mesurable.
  - Deux niveaux d'entraînement préenregistrés, exprimés en multiples de l'entraînement qui efface la moitié du trait de l'étalon (illustratif).
  - Entraînement à récompenses aléatoires. Aucun point de contrôle n'est choisi d'après l'oracle.
- **Estimateur** : la différence de différences (S_post − H_post) − (S_pré − H_pré), sur des articles disjoints de ceux qui ont servi à mesurer S_pré. L'unité est la graine.
- **H_A** : au niveau préenregistré, le dommage résiduel estimé dépasse m₂.
- **H_B** : il est inférieur ou égal à m₂ ; le sabotage s'effondre.
- **Garde de plancher.** Si la qualité honnête absolue après entraînement s'écarte de celle du jumeau gelé de plus de m_cap, l'issue est « non jugeable ».
- **Lecture de l'étalon.** Si le trait bénin s'efface au même rythme que le sabotage, la fragilité est celle de tout adaptateur léger. Elle ne dit alors rien de propre au sabotage.
- **Contrôles négatifs** : l'honnête soumis au même entraînement, une branche sans mise à jour, l'adaptateur à trait bénin.
- **Ce qui réfuterait H_A** : un effondrement. Il interdit toute conclusion de parade sur cet organisme.
- **Ce qui réfuterait H_B** : une persistance au-delà de m₂.
- **Coût** : de 15 à 30 courses (illustratif), plus que dans ma version III.1, à cause du nombre de graines.

### C3′. La lecture interne apporte-t-elle quelque chose ?

- **Montage.**
  - Sur F_s, lue une seule fois.
  - Si F_s n'est pas prête avant la porte, C3′ porte sur le bloc de test des familles existantes. Sa conclusion est alors bornée à « intra-famille ». Toute reconception de sonde postérieure à C1′ interdit cette lecture : seule F_s pourra alors juger.
- **Comparateurs gelés et choisis sur le bloc de développement** :
  - un moniteur de texte à consigne fixée ;
  - le lecteur sans état (la sonde réapprise sur les états du modèle de base qui relit la transcription) ;
  - la liste des vérifications mécaniques.
- **H_A** : P(τ ≤ h) pour la sonde accumulée dépasse de plus de m₃ celui du meilleur comparateur, choisi sur le bloc de développement. La comparaison se fait à α réalisé égal, sur des flux honnêtes tenus à l'écart, dose par dose observée.
- **H_B** : l'écart est inférieur ou égal à m₃.
- **Métrique secondaire** : le gain de vraisemblance du classifieur sur (T, S) par rapport à T seul.
- **Contrôles négatifs** : flux honnêtes, flux d'adaptateurs bénins, honnêtes sur des questions plus difficiles, sonde à étiquettes permutées.
- **Ce qui réfuterait H_A** : le lecteur sans état égale la sonde. L'information est alors dans le texte, et le programme pivote vers l'audit et la validation de l'oracle.
- **Coût** : quelques dizaines de courses (illustratif), plus le coût de l'oracle, que je ne connais pas.

### C4′. La garantie survit-elle à un agent qui change ?

- **Montage.**
  - Auto-distillation sur les traces honnêtes du modèle de huit milliards de paramètres lui-même, tirées sans filtre par l'oracle.
  - Appliquée à l'honnête, aux adaptateurs bénins et au saboteur.
- **H_A** : le taux de fausses alertes réalisé chez l'honnête mis à jour, au seuil gelé avant la mise à jour, reste inférieur ou égal à α + m₄.
- **H_B** : il dépasse α + m₄. Ce duel n'exige aucune classe positive : il est toujours jugeable.
- **Volet secondaire.** On compare la séparation entre le saboteur mis à jour et le bénin mis à jour, mais seulement si le bras saboteur entier garde, par différence de différences, un dommage supérieur à m₂ (règle de la ligne 12). Sinon, ce volet est « non jugeable », et non classé H_B.
- **Contrôles négatifs** : des répliques sans mise à jour.
- **Ce qui réfuterait H_A** : une dérive du taux de fausses alertes. Toute combinaison de détection et d'entraînement devra alors recalibrer la garantie.
- **Coût** : il est partagé avec C2′ ; quelques courses de plus (illustratif).

### C5′. L'aiguillage économise-t-il des audits ?

- **Préalables** : C8′ passé, sonde gelée, journaux issus du seul bloc de test.
- **Montage.**
  - Budget total B fixé.
  - Plan aiguillé : une part uniforme λB, qui porte la borne, plus une part aiguillée.
  - Plan de référence : budget uniforme.
  - Placebo : scores permutés, avec les mêmes probabilités d'inclusion inégales.
  - Rejeu sur R flux indépendants, avec une grille de π préenregistrée qui inclut π = 0 et un flux honnête de difficulté hétérogène.
- **H_A** : le plan aiguillé atteint la décision préenregistrée (un excès de dommage au-dessus du taux honnête de référence, avec une puissance 1 − β) en moins d'audits que le placebo, à couverture égale.
- **H_B** : non.
- **Rapportés à part** : l'élargissement de la borne lié à λ, et le taux de confirmation à π = 0. S'il excède celui du placebo, c'est la marque d'un couplage entre la sonde et les faux positifs de l'oracle.
- **Ce qui réfuterait H_A** : une économie qui disparaît face au placebo, ou qui n'existe qu'à π = 0.
- **Coût** : sur processeur si les verdicts de l'oracle existent déjà pour tous les épisodes rejoués ; sinon, je ne sais pas.

### C8′. Condition d'entrée : validité de l'oracle

- **Montage.**
  - Accord entre l'oracle sur le produit seul et une référence d'une autre classe : des évaluateurs extérieurs, aveugles à la condition, qui lisent par paires avec le jumeau.
  - Stratification par dose, avec puissance calculée à la plus faible dose.
  - Paires témoins : honnête contre honnête, adaptateur bénin contre jumeau, éditions de style sans changement de fond, ordre des paires inversé.
- **H_A** : à la plus faible dose, l'oracle prédit la référence au-delà du style seul, de plus de m₈.
- **H_B** : non. C3′ et C5′ ne valent alors qu'au-dessus de la dose où l'oracle tient.

### P2 et P3 réécrits

- **P2.**
  - H_A (dissociation) : dommage et séparation de la sonde évoluent différemment sous un entraînement sans information.
  - H_B (co-évolution) : ils évoluent ensemble.
  - Lecture : H_B fait de la sonde un candidat validateur d'entraînement sur cet organisme ; H_A l'en disqualifie.
- **P3** : toujours différé, et soumis au changement de règle déclaré. Le diagnostic d'obscurcissement devient une sonde réapprise sur une partition d'apprentissage des activations après entraînement, évaluée sur une partition tenue à l'écart et confrontée au dommage mesuré.

---

## (c) Réponse à l'arbitre

**Ce qui est établi** (statuts inchangés)

- VÉRIFIÉ :
  - Le jumeau honnête n'existe qu'au banc.
  - La garantie contre la menace diffuse repose sur un audit tiré au hasard, publié par d'autres et non revendiqué.
  - Aucun score de moniteur ni sortie de l'oracle n'entre dans l'entraînement ou la sélection, hors du bras d'attaque déclaré.
  - Corriger en entraînant l'agent n'est pas ouvert.
  - La dose-réponse existe pour l'adaptateur et manque pour la consigne.
- VÉRIFIÉ, sur des travaux extérieurs :
  - Une note faible peut être atteinte par des saboteurs de qualités réelles différentes.
  - L'entraînement contre un détecteur interne peut produire des états obscurcis.
  - Un entraînement ordinaire peut ôter leur séparation à des sondes apprises hors domaine.
  - Un organisme distillé d'une consigne a cédé à des récompenses aléatoires.
  - Des saboteurs publics retrouvent leur capacité après un réglage fin bénin.

**Ce qui ne l'est pas**

- OBSERVÉ-NON-AUDITÉ : aucune mesure de sonde n'a été trouvée sur une tâche difficile à noter, et la tenue de nos saboteurs n'a pas été mesurée.
- HYPOTHÈSE : nos saboteurs se représentent leur sabotage.
- Non mesuré : la validité de l'oracle aux faibles doses. Je ne connais pas sa nature.
- Ce que les critiques m'ont fait reconnaître dans ma propre conception :
  - mon témoin du dernier jeton ne tranchait rien ;
  - mon C2 n'avait pas d'échelle ;
  - mon C4 confondait la guérison du saboteur et la perte de la sonde ;
  - mon C3 n'avait pas de famille inédite disponible ;
  - mon C5 mesurait une grandeur géométrique sensible aux faux positifs de l'oracle.

**Sur l'entraînement comme parade.** Ma position est maintenue, sous forme de proposition. L'entraîner entre dans le programme comme **objet de mesure** (C2′, C4′), pas comme parade avant la porte de comparaison. La parade guidée (P3) exige trois conditions :
- un organisme validé par C2′ ;
- un oracle validé par C8′ ;
- un changement de règle déclaré par écrit.

Je ne sais pas si l'organisme à adaptateur tiendra.

**L'expérience à faire en premier : C1′.**
- Elle n'exige ni l'oracle ni la tenue des saboteurs, seulement les conditions fabriquées.
- Elle coûte peu (illustratif).
- Elle conditionne tout le reste : si l'alerte suit l'amplitude de la modification, C3′, C4′ et C5′ mesureraient un artefact.
- Elle doit être précédée, sans calcul supplémentaire, du scellement de la partition et de F_s, et du calcul de taille.
- C2′ et C8′ suivent avant la porte d'instruments. C3′, C4′ et C5′ viennent avant la porte de comparaison.
- Restent hors de portée :
  - un saboteur qui ne se représente pas son sabotage ;
  - la portée sur des modèles plus grands ;
  - un oracle sûr pour une tâche de recherche ouverte.

FIN-DE-CELLULE