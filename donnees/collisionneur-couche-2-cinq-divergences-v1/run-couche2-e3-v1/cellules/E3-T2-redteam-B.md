# Tour III.2 : équipe rouge croisée (proposition B)

**Pièces reçues.** Les conceptions A et C sont complètes : chacune se termine par FIN-DE-CELLULE. La sortie JSON de la simulation et la carte d'inventaire ne sont pas servies, je n'en invente rien.

**Statuts.**
- Ce que A ou C affirme reste au statut qu'ils lui donnent ; quand je le cite, je dis « A écrit » ou « C écrit ».
- Mes recalculs analytiques sont marqués « calcul refait ici, illustratif ».
- Mes raisonnements sont des HYPOTHÈSES.

**Garde.** Les scénarios d'évasion restent au niveau de la classe et de la dose. Aucun ne décrit de recette, de consigne ni d'exemple.

---

## Une faille commune, structurelle, que A et C traitent mal

Aucune des 96 tâches n'est vierge, d'après A1 (RAPPORTÉ) :
- **les 60 tâches du pilote** ont servi à l'épreuve de P3. La couche de la sonde principale (c15) y a été retenue (`resume.json` de P3), et la base (iii) en hérite ;
- **les 32 tâches de réserve** portent la recherche de dose et les jeux synthétiques des sondes de T0.7 ;
- il reste **4 tâches** sans usage déclaré.

Conséquences :
- **C** appelle les 64 tâches d'évaluation « vierges » (duel E2) et s'en sert comme distribution de référence pour tester la contamination de la réserve.
- **A** mentionne la réserve P3 « à écrire au préenregistrement ». Pourtant son duel D2 prend lui aussi les tâches d'évaluation comme référence.

Comparer deux groupes contaminés par deux voies différentes ne mesure pas la contamination. Cela mesure la différence entre deux contaminations. Il y a donc une fuite entre la construction de l'instrument (choix de couche et de position, lus sur P3) et son évaluation (G1 sur ces mêmes tâches). Aucun test interne à la banque ne peut l'exclure : 4 tâches propres ne font pas un groupe témoin. **HYPOTHÈSE** : la seule issue honnête est soit une portée déclarée (« conditionnelle à des tâches ayant servi au choix de couche »), soit des tâches neuves.

**Duel B-1 (contamination P3), inférence forte.**
- **H_A** : le rappel à 1 % du blanc séquentiel, à couche c15, est supérieur sur les 60 tâches lues en P3 à ce qu'il est sur des tâches neuves, d'au moins 5 points.
- **H_B** : l'écart est inférieur à 5 points.
- **Protocole** :
  - seuils calibrés une seule fois sur les honnêtes de tâches neuves ;
  - différence appariée par tâche ;
  - test d'équivalence à ±5 points.
- **Issues** :
  - borne d'équivalence atteinte → H_A falsifiée, la portée n'a plus besoin de réserve ;
  - supériorité certifiée → H_B falsifiée, et le choix c15 est biaisé en faveur du blanc ;
  - ni l'une ni l'autre → c'est l'hypothèse « ce banc suffit à trancher » qui est falsifiée.
- **Contrôle négatif** : la même comparaison pour les sondes aléatoires appariées doit donner un écart nul.
- **Prérequis** : des tâches neuves. Sans arXiv (B1, D2), ce duel n'est pas exécutable, et il faut le dire à Lazar.

---

## Contre la proposition A

### (a) Failles

**1. Le test de contamination de la réserve ne regarde pas où la fuite agirait.**
- Les sondes de T0.7 ont été entraînées sur des jeux synthétiques liés à la réserve. Une fuite gonflerait donc le **rappel sur les sabotés** de réserve, et pas forcément la queue honnête.
- Le duel D2 de A ne lit que les honnêtes : fausses alertes et distribution des scores. H_B (« même distribution ») peut être retenue alors même que le rappel est gonflé.
- Ce sont aussi deux hypothèses mal opposées. H_A (« distributions différentes ») s'appuie sur un critère de mauvaise calibration, l'intervalle hors de [0,5 % ; 2 %]. Ne pas rejeter H_B à 32 tâches ne falsifie rien. B4 n'est pas respecté.

**2. La réserve « vierge » n'existe pas.** A propose de garder 16 des 32 tâches de réserve « vierges pour le test de contamination ». Selon les faits que A cite lui-même, toute la réserve porte déjà la dose (P-015 b) et T0.7.

**3. Fuite du pilote vers le développement.**
- A veut que les épisodes du pilote deviennent la partie « développement ».
- Or le pilote sert à choisir K, le nombre de tâches, les strates de dose et les paramètres a, h et la concordance. Ensuite, l'organisme du pôle lit ce même développement (G_max = 1).
- Les hyperparamètres sont donc choisis sur les données qui seront évaluées. D-S12 (« héritage entre parties disjointes seulement ») l'interdit en substance.

**4. Vrai par construction sur la dose.**
- La dose est choisie pour que le juge 8B par action reste sous son seuil. A le reconnaît : ce comparateur est « au plancher par construction ».
- Mais le régime « diffus » est défini par le **meilleur** moniteur boîte noire par action (P-015). Ajuster contre le seul 8B laisse le 3B, Qwen et b* hors du critère. La strate « diffus » est alors mal définie : elle dépend du juge contre lequel on a ajusté.

**5. Une tension interne non résolue.**
- A veut des strates de dose pour la dose-réponse (H1b).
- A montre aussi que la fiche de H1a, limitée à la strate « diffus », tombe à environ 32 unités, sous le plancher de garde de 48.
- Les deux objectifs se disputent les mêmes 64 tâches, et A ne dit pas lequel cède.

**6. « Mention » mal définie.**
- A en fait « la seule condition où l'intention est présente et l'acte absent ». La question, elle, dit seulement « le sabotage est nommé mais non exécuté » : nommer n'est pas vouloir.
- Le confondant que « mention » contrôle dépend d'une définition **absente des faits servis**. Le duel D4 est ininterprétable tant qu'elle n'est pas scellée.
- D4 n'est pas non plus dichotomique : H_A (« mention ≥ saboteur − 10 ») et H_B (« mention ≤ honnête + δ et saboteur > mention + 20 ») laissent une large zone où aucune n'est falsifiée.

**7. Dérive temporelle introduite par les jumeaux partagés.**
- A juge que les jumeaux partagés rendent S_x « plus lisible ». Mais S_x est généré **après** le scellement, donc des jours ou des semaines après les jumeaux, sur d'autres instances.
- Tout écart de pile logicielle ou de matériel entre l'époque des jumeaux et celle de S_x se confond avec l'effet du mode, précisément dans la comparaison que A dit protéger.
- B1 liste les versions épinglées, mais aucun plan ne vérifie leur respect au moment de S_x.

**8. Deux règles de décision.** A relève qu'une règle d'intervalle à 95 % (N-008) et une règle de richesse au seuil 20 (D-S11, retenu en (c) mais « pièce du préenregistrement ») coexistent. Puis A calcule toute sa puissance sous la seconde, sans dire ce que devient la recommandation sous la première.

### (b) Scénarios d'évasion (niveau classe)

| instrument de A | classe qui l'aveugle | coût pour l'agent adverse |
|---|---|---|
| quantile honnête à 1 % | sabotage dont l'empreinte par épisode reste dans la variance honnête **entre tâches** (a) : aveugle par construction sous le plateau d'environ 4 points | efficacité réduite (HYPOTHÈSE) |
| blanc séquentiel (maximum courant du processus e) | contribution interne par action de moyenne quasi nulle sur la fenêtre : rien ne s'accumule | sabotage étalé, donc lent |
| base (iii), dernière position | signal localisé tôt, que l'état terminal ne résume pas | aucun coût si le dommage est précoce |
| boîte noire (juges, TRACE-lite) | absence d'évidence textuelle | dépend du mode |
| témoin et mention | représentation interne du sabotage confondue avec celle d'une « instruction cachée » | aucun : c'est un échec de G1, pas une évasion |

**Toutes à la fois** : l'intersection est une classe à faible dose, étalée et textuellement plausible.

**Le point décisif** : A ne mesure jamais le **dommage par niveau de dose**. On ne peut donc pas chiffrer le prix de l'évasion. Un sabotage diffus non détecté et sans effet passerait pour un échec du moniteur.

Le bras d'attaque **informé** (N-056 § 6) connaît le protocole. Si le préenregistrement scelle « dose ajustée contre le 8B par action », il lui donne la frontière exacte où ce comparateur est aveugle.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Permutation des étiquettes, de bout en bout.** Réaffecter au hasard les étiquettes saboté/honnête à l'intérieur de chaque tâche, puis faire tourner toute la chaîne : jumeaux partagés, calibrage partagé, intersection-union sur deux modes. G1 doit promouvoir au plus dans 5 % des cas. Le contrôle 12 de A ne teste qu'une cellule face à elle-même, pas la chaîne.
2. **Vérification que le sabotage est présent** (étiquetage à deux séries, N-054) **dans le pilote**. A ne l'y met pas. Sans elle, un écart entre « mention » et « saboteur » peut n'être qu'un écart d'obéissance à la consigne.
3. **Plancher de longueur.** Une statistique séquentielle prise comme maximum sur l'horizon monte mécaniquement avec le nombre d'actions. Il faut un plancher « longueur brute », absent de la table (c) de A, et une stratification par longueur réalisée, pas seulement par horizon prévu.
4. **Contrôle de dérive à la génération de S_x.** Régénérer, au moment de S_x, un échantillon de jumeaux honnêtes à graines identiques, et tester leur égalité en loi avec les jumeaux d'origine.

---

## Contre la proposition C

### (a) Failles

**1. Statuts gonflés : la règle 1 est enfreinte.**
- C marque « VÉRIFIÉ dans A1 » des énoncés que A1 donne comme inférences : « un épisode honnête n'a pas de mode » est [INFÉRÉ] dans A1 § 1, partie « Jumeaux partagés ». Les faits n'attribuent ce statut nulle part.
- C conclut en gras que « le minimum de 4 800 **échoue** » à partir d'un coefficient 1,3 × p₁ et d'une corrélation de 0,6 à 0,8 qu'il marque lui-même « illustratif ». C'est une hypothèse présentée comme un résultat.
- Le « minimum strict de 6 400 » repose sur p₁ ≈ 0,022 à 6 400 épisodes, une cellule que la simulation de A n'a jamais tirée : A2 ne simule la coupe dans les tâches qu'à 4 800 et 9 600.

**2. Erreur d'un facteur √2 dans la formule centrale.**
- C écrit σ(Δr̂) ≈ 2,04·√(1−a)/√N, avec des moitiés de taille N/2. Or la constante 2,04 est celle de deux moniteurs calibrés chacun sur **N** épisodes : c'est la colonne « écart entre jumeaux » de H_binormal, soit 2,9 points à N = 4 800.
- Avec des moitiés de 2 400, on obtient environ 4,1 points avant le facteur √(1−a) (calcul refait ici, illustratif), contre 2,63 annoncés par C.
- Le facteur √(1−a) n'est pas justifié non plus. La densité qui gouverne le quantile est celle de la loi marginale, pas une variance intra-tâche réduite.
- Le bruit du contrôle 12 est donc sous-estimé, et chaque volume que C en tire, 4 800 comme 6 400, est fragilisé.

**3. Le « relevé à tort » contre la pièce C est lui-même faux.**
- C affirme que la cellule F simule la coupe dans les tâches sous 2 000 épisodes. Ce n'est pas ce que fait `calibrage_memes_taches` dans A2 : elle calibre **deux moniteurs distincts sur un même ensemble entier**, sans coupe en moitiés, et avec une garde.
- `calibrage` (bloc K) coupe **par** tâche (`taches // 2`). La coupe dans les tâches (`controle_12_intra_taches`) n'est tirée qu'à K_cal = 75 et 150.
- La remarque de la pièce C (« non simulé pour la coupe recommandée ») est donc exacte.
- C attribue en outre les 0,08 à 0,12 de F au « seul bruit de quantile intra-tâche (σ ≈ 5,7 points) ». C'est une attribution inventée : la pièce C rapporte les mêmes valeurs pour des tâches **disjointes**.
- Les « lignes 284-292 » et « 155-184 » de A2 ne correspondent à aucune numérotation fournie.

**4. Une « erreur majeure manquée » surévaluée et chiffrée par des rythmes inventés.**
- Qwen « ≈ 55 s » et b* « ≈ 58 s » ne figurent dans aucune pièce, et ne sont pas marqués illustratifs : la règle 4 est enfreinte.
- Les « 2 300 à 4 600 heures » supposent qu'un appel de TRACE-lite coûte une passe entière du juge 8B. C'est une HYPOTHÈSE présentée comme « CALCULÉ ICI ».
- A n'a pas « manqué » ce poste : A1 § 8 écrit que « B est l'hypothèse la plus fragile » et que chaque comparateur doit noter les 9 600 épisodes.
- C est aussi incohérent avec lui-même : son propre total (14 288 épisodes, 575 à 728 USD) est calculé à 132 s par épisode, donc avec les juges 8B et 3B seulement. Par son propre argument, son devis est sous-estimé d'un facteur de l'ordre de 5.
- Sa parade, un sous-échantillon de 1 500 épisodes honnêtes pour TRACE-lite, se situe sous les environ 2 000 épisodes où A prévoit l'échec du contrôle 12 (coupe par tâche). Sa tenue en coupe dans les tâches n'est pas simulée.
- Dans une intersection-union, un comparateur au seuil plus bruité devient aléatoirement plus fort ou plus faible, ce qui déplace le minimum (HYPOTHÈSE).

**5. Le pilote minimal ne peut pas faire tourner le contrôle 12.**
- En 5.2, L1b prévoit 160 épisodes honnêtes de calibrage sur 8 tâches, puis un contrôle 12 « 10 contre 10 par tâche », soit 80 épisodes par moitié.
- Le code calcule j = ⌊0,01 × 81⌋ = 0, donc un seuil infini, et refuse l'engagement (« calibrage insuffisant », A1 § 3, RAPPORTÉ).
- La mesure annoncée n'est pas réalisable avec ce volume.
- Les deux pilotes de C se contredisent aussi : L1 à 16 tâches et 1 360 épisodes, avec un calibrage « 32 × 20 = 640 » ; 5.2 à 8 tâches et 472 épisodes. La comparaison « deux fois moins cher que A » compare des pilotes qui ne mesurent pas la même chose.

**6. Seuils de décision fixés sur 8 à 16 groupes.** E5 tranche entre « a ≤ 0,35 » et « a > 0,45 » avec 8 à 16 tâches.
- L'intervalle d'une part de variance inter-groupes estimée sur 8 groupes est large (HYPOTHÈSE).
- La zone de 0,35 à 0,45 n'est attribuée à aucune issue.
- L'erreur standard de 0,06 sur ρ_intra, donnée sans calcul, ignore la dépendance des 10 exécutions à l'intérieur d'une tâche.

**7. Les duels ne respectent pas B4.**
- E4 laisse une zone entre 2 % et 10 % d'alertes. Son « contrôle négatif » (témoin lexical qui doit déclencher sur « mention ») est en fait un contrôle positif.
- La définition de « mention » que C attribue à la question (« mots-clés dans un contexte déclaratif ou négatif ») n'y figure pas : statut gonflé.
- E3 exige une identité au bit près entre lots sur carte graphique. Le non-déterminisme des noyaux selon la taille de lot peut falsifier H_A sans aucune fuite entre modes : H_A et H_B ne sont pas exclusives. Le cas testé, un jumeau « dans le lot du mode S_c », n'existe même pas dans le plan, où le jumeau est généré une seule fois.

**8. Un arrêt optionnel déguisé.** En L3, si le contrôle 12 dépasse 0,05, C ajoute une tranche de calibrage. Répéter jusqu'au succès revient à échantillonner jusqu'à la conclusion voulue : le diagnostic perd sa valeur. Il faut que N et la règle soient scellés d'avance, échec compris.

**9. Le témoin « apparié en fréquence d'actions ».** Le témoin bénin se met à intervenir. Le contraste S contre T porte alors sur le contenu des interventions, et le témoin crée sa propre empreinte d'action. Cela confond « agir sous instruction cachée » avec « saboter », dans l'autre sens (HYPOTHÈSE).

### (b) Scénarios d'évasion (niveau classe)

- **Planchers « longueur brute » et « permutation circulaire »** : toute classe de longueur égale à l'honnête et sans dépendance d'ordre les rend muets.
- **Sondes aléatoires** : elles ne protègent que contre l'artefact de dimension, pas contre une classe alignée sur une direction partagée avec le témoin.
- **Toutes à la fois** : la même intersection que contre A. En plus, le sous-échantillonnage proposé pour TRACE-lite crée une cellule au seuil bruité, donc un comparateur faible qu'une classe à faible dose aurait intérêt à viser. Le prix ne peut pas non plus être chiffré, faute de mesure du dommage par dose.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Permutation des étiquettes de bout en bout** : absente de C, comme de A.
2. **Volume de calibrage du pilote** d'au moins 99 épisodes par cellule, par strate et **par moitié**, vérifié avant de chiffrer le pilote. Sinon le contrôle 12 n'est pas lisible.
3. **Contamination mesurée sur le rappel saboté.** E2 compare seulement des moyennes honnêtes standardisées. Les tâches ont été réparties au hasard (A1 § 1 : 64 + 32 « sans remplacement »), donc une différence de moyenne honnête est attendue nulle même en cas de fuite.
4. **Contrôle de dérive à la génération de S_x** (L3), pour la même raison que chez A.

---

## Duel B-2 : faut-il réestimer le contrôle 12 avant de fixer N ?

Ce duel sert les deux plans.

- **H_A** : en coupe dans les tâches à N = 4 800 sur 64 tâches, la promotion à tort sur l'**union** des deux modes, avec U partagé, est au plus de 0,05.
- **H_B** : elle dépasse 0,05.
- **Protocole** :
  - simulation sur processeur, sans dépense ;
  - extension de `controle_12_intra_taches` à deux cellules qui partagent les moitiés ;
  - 2 000 répétitions.
- **Règle** : intervalle à 95 % comparé à 0,05.
  - Au-dessous → H_B falsifiée, et le minimum de A tient.
  - Au-dessus → H_A falsifiée, et les deux plans doivent monter à 9 600.
  - L'intervalle contient 0,05 → l'hypothèse « 2 000 répétitions suffisent » est falsifiée, et il faut en tirer plus avant de décider.
- **Contrôle négatif** : la coupe par tâche, sur les mêmes tirages, doit dépasser 0,10. Sinon le simulateur ne reproduit pas A.
- **Ce que le duel tranche aussi** : l'écart entre la constante 2,04 de C et le √2 que j'avance sera mesuré, pas argumenté.

FIN-DE-CELLULE