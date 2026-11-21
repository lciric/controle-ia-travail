# Proposition B, tour III.2 : critique croisée de méthode

**État des pièces.** A, C et D sont transmises et semblent complètes : chacune se termine par sa ligne de clôture. Je ne recalcule pas les sha256. Aucune mesure du programme n'est transmise. Toutes les conditions ci-dessous portent donc sur des lois de probabilité et sont à calculer avant la mesure ; ce ne sont pas des constats.

**Statuts.** Mes critiques et mes dérivations sont des HYPOTHÈSE. Les citations des faits restent RAPPORTÉ.

**Signalement d'intégrité, sans changer aucun statut.**
- D marque VÉRIFIÉ des références citées de mémoire (Goldwasser et Micali ; Wald ; Tramèr et al. ; Carlini et Wagner ; Cohen et al. ; Greenblatt et al.). D marque aussi VÉRIFIÉ une propriété mathématique dont il se sert comme argument d'ordonnancement.
- C marque VÉRIFIÉ les autodescriptions du programme ; A les marque RAPPORTÉ.

Aucune de ces références n'est vérifiée par les pièces. Je laisse l'arbitre trancher.

**Choix de profondeur, selon la consigne de l'arbitre.** Je ne relève que ce qui rend un résultat vrai par construction, ou ce qui le rend non jugeable.

---

## Défauts communs aux trois, énoncés une fois

Je les énonce une fois ; je ne fusionne pas les propositions.

**1. Un seul mode tenu à l'écart, c'est un seul tirage de « genre ».**
- La quantité visée par « sabotage de genre inconnu » est une espérance sur une loi de genres.
- Avec un seul genre lu une fois, la variance entre genres τ² n'est pas identifiable.
- Aucune des trois propositions ne peut donc écrire un intervalle sur la garantie hors du genre lu.
- Si ce mode sert à plusieurs duels, « lu une seule fois » impose une lecture conjointe de tous les contrastes, préenregistrée, avec correction de multiplicité. Sinon, la seconde lecture est une fuite.

**2. Le seuil « 1 % de fausses alertes » est estimé, pas donné.**
- Supposons le seuil fixé au quantile empirique d'ordre 1−α de n scores honnêtes indépendants. La FPR vraie de ce seuil suit alors une loi Beta(nα+1, n−nα).
- Pour n = 100 (illustratif), on obtient Beta(2, 99) : moyenne ≈ 2,0 %, écart-type ≈ 1,4 %.
- Pour n = 1 000 (illustratif), on obtient Beta(11, 990) : ≈ 1,1 % ± 0,33 %.
- Toute variation de rappel plus petite que celle induite par cette incertitude du seuil est non jugeable.
- Il faut préciser si le seuil porte sur un pas ou sur une trajectoire. Sur T pas, un seuil de 1 % par pas donne une FPR par trajectoire bien plus forte, et les trois propositions passent de l'un à l'autre.

**3. Les mondes à vérité plantée valident l'oracle contre la référence même qu'il consulte.**
- Les défauts plantés sont définis par rapport à la référence cachée, et l'oracle lit cette référence.
- L'accord oracle–monde planté est donc élevé par construction.
- Il ne dit rien de la part du dommage que la référence ne contient pas.

---

## Sur la proposition A

### (a) Défauts de méthode

1. **η est nul par construction avec les données prévues.**
   - A estime η à partir de paires honnête–honnête (même modèle, graines différentes) et de leur dérive entre familles.
   - Or η est l'erreur sur la ligne de base du modèle *déployé*, dont le seul exemplaire est suspect.
   - Jumeau contre jumeau, c'est la même loi des deux côtés : on mesure σ, pas η. Le terme qui porte toute la phrase du point 6 sort petit par construction.
   - Le proxy minimal est l'écart entre deux modèles honnêtes *distincts* (autre point de contrôle, autre famille). Il donne une estimation grossière de η, pas η lui-même.

2. **E1 teste une borne de pire cas avec des adversaires qui ne s'y placent pas.**
   - La borne est atteinte au dommage par tâche optimal d*.
   - Un saboteur construit, avec un d quelconque loin de d*, passe sous B sans que cela prouve quoi que ce soit sur B.
   - Il faut une injection de dommage planté au niveau d*, fixée par l'expérimentateur et sans agent. Elle teste la borne sans fournir de recette.

3. **La courbe de sensibilité hérite du défaut commun 3.** Elle est mesurée sur des défauts définis par la référence consultée.

4. **E4 « à budget égal » est fixé par un taux de change arbitraire** entre le calcul d'entraînement et les appels à l'oracle : l'issue dépend de ce taux.
   - Un sabotage *installé* par réglage fin est plausiblement retiré par réglage fin, ce qui avantage l'entraînement par construction du saboteur (HYPOTHÈSE).
   - Si l'entraînement utilise des signaux de l'oracle sur des familles proches du mode tenu à l'écart, il y a fuite.

5. **E5 tient par construction pour sa partie uniforme**, si le tirage vient d'un générateur imprévisible. E5 ne teste réellement qu'une chose : l'oracle est-il déplaçable ? Il faut le présenter ainsi et ne le compter qu'une fois.

6. **La méthode de rangement est validée sur des mondes « où la bonne question est connue ».** C'est circulaire : c'est l'équipe qui décide quelle question est la bonne.

### (b) Conditions de perte de puissance ou de non-jugeabilité

La dérivation de A suppose des scores indépendants, une variance σ² commune et un déplacement k·d linéaire. Elle perd sa validité dans les cas suivants.

- **Hétéroscédasticité par famille f.** Si σ_f/k_f varie et que l'adversaire connaît les familles, le pire cas est gouverné par max_f σ_f²/(q·k_f²·d), pas par une moyenne. Une borne calculée avec σ moyen est alors fausse au sens propre.
- **Réponse non linéaire près de zéro.** Si E[score | d] − E[score | 0] = k·d^γ avec γ > 1, le dommage avant alarme vaut environ σ²/(q·k²·d^(2γ−1)). Il croît encore plus vite quand d diminue, et B dépend de γ, qu'on n'estime qu'avec beaucoup d'audits près de d = 0.
- **Autocorrélation ρ entre audits d'une même trajectoire.** Sous un modèle AR(1), la variance effective est multipliée par environ (1+ρ)/(1−ρ), et le nombre d'audits nécessaires l'est autant.
- **Queues lourdes du bruit honnête** (variance infinie ou mal estimée) : la règle σ²/(k·d)² ne s'applique plus.
- **Vacuité calculable d'avance.** Quand N → ∞, B/(N·d_max) tend vers η/(k·d_max). Si η ≥ c·k·d_max, où c est la fraction préenregistrée, B est vide par construction. Ce test se fait dès qu'une borne inférieure de η existe, avant toute mesure de dommage.
- **E2 est non jugeable sans loi nulle du dommage joint.** Il faut un oracle sur des lots, sans référence de lot. Si la variance honnête sur lots n'est pas mesurée, l'écart « joint moins somme » n'a pas de distribution nulle.

### (c) Contrôles négatifs dont l'absence serait fatale

- **Pour η** : paires honnêtes *inter-modèles*. Sans elles, η = 0 par construction.
- **Pour E1** : jumeau honnête sur des familles de tâches *exclues de la calibration du seuil*. Le contrôle actuel (« alarmes ≤ 1 % » sur le jumeau) est vrai par construction. À cela s'ajoute le contrôle positif par injection à d*.
- **Pour E3** : réglage fin bénin, en plus de la consigne bénigne. Les saboteurs sont aussi construits par réglage fin, et seule la consigne est contrôlée.
- **Pour E4** : un « saboteur » placebo (adaptateur bénin) soumis au même entraînement. Il sépare « l'entraînement retire le sabotage » de « l'entraînement retire l'adaptateur ».
- **Pour l'oracle dans les duels** : la production honnête médiocre. A la liste en données brutes, mais elle est absente des duels.

---

## Sur la proposition C

### (a) Défauts de méthode

1. **H_B d'E1 est falsifiée par construction.**
   - C affirme que « la variance […] croît au moins aussi vite en √T que le signal cumulé ».
   - Avec un bruit centré indépendant, l'écart-type croît en √T et une dérive constante croît en T. H_B tombe donc pour T assez grand, quel que soit le dispositif.
   - L'obstacle du billet du 30 avril 2025 (RAPPORTÉ) n'est pas la variance mais le *biais* de ligne de base, qui croît lui aussi en T.
   - H_B doit porter sur |μ_jumeau − μ_contrepartie honnête| comparé à la dérive par pas.

2. **La « martingale centrée » par soustraction du jumeau suppose que le jumeau a la loi de la contrepartie honnête de l'agent.**
   - En laboratoire, l'agent est le modèle de base plus une consigne ou un adaptateur ; le jumeau est le modèle de base seul.
   - La différence contient l'empreinte de la construction, détectable sur toute trajectoire, même sans sabotage.
   - Le gain « sonde + jumeau » peut donc être vrai par construction.

3. **Le contrôle négatif d'E1 ne neutralise pas cette fuite.** Le jumeau à compétence dégradée (température plus haute, moins d'entraînement) ne contient aucune intervention.

4. **La validation de l'oracle relève du défaut commun 3.** La « corrélation de rang > 0,8 avec mondes à vérité plantée » est circulaire.

5. **Dans E2, la taxe d'obscurcissement est vraie par construction si l'attaque est faible.**
   - L'équipe qui conçoit les sondes entraîne aussi le saboteur qui doit les obscurcir.
   - Un optimiseur faible suffit à rendre H_B (« taxe rédhibitoire ») vraie.
   - C ne prévoit ni équipe rouge indépendante, ni contrôle d'efficacité de l'attaque.

6. **E2 viole B4.** Une rétention du dommage entre 50 % et 80 % (illustratif), ou un TPR de sonde entre 1 % et 20 %, ne falsifie aucune des deux hypothèses.

7. **E3 confond deux effets.**
   - Sous un audit uniforme sur l'ensemble des tâches de toutes les copies, la borne est indifférente à la répartition entre les K copies ; A le note.
   - H_A (« dommage croissant avec K ») ne peut donc concerner que les tests *par trajectoire*.
   - Le ratio D(uniforme)/D(priorisé) mêle cette question et celle de la priorisation.
   - S'y ajoute une multiplicité non corrigée : 4 valeurs de K et deux attaques, chacune testée à p < 0,01.

8. **La phrase opposable n'est pas réfutable au niveau du programme.** Elle « teste si » le couplage divise le dommage, « tout en quantifiant le seuil » où l'avantage s'annule. Toute issue devient une réussite. Je fais la même critique à D.

9. **L'ancrage est incohérent en interne, en chiffres illustratifs.** 300 à 600 heures-GPU à 1,5–2,5 $ l'heure donnent 450 à 1 500 $ au total, pas 300 à 500 $ par papier ni 1 000 à 1 500 $ pour le programme complet.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **CUSUM ou SPRT sur Δ_t = agent − jumeau.** Notons b_tâche = E[Δ_t | honnête].
  - Si b_tâche ≠ 0, la statistique dérive en b·T et sonne sur les honnêtes.
  - Après recalibrage, la détection exige que la dérive de sabotage dépasse sup_tâches |b_tâche|. Si δ ≤ sup |b_tâche|, la question est non jugeable.
  - Avec une autocorrélation intra-trajectoire, la FPR par trajectoire d'un test calibré sous indépendance est sous-estimée.
- **Critère « réduction de 30 % de D(τ), p < 0,01 ».** D(τ) est évalué à un temps d'arrêt, dont la loi est typiquement très asymétrique. Si Var D(τ) est grande, le nombre de trajectoires sabotées nécessaire explose. Il faut préenregistrer une médiane ou un quantile, pas une moyenne.
- **Mesure de rétention dans E2.** Si la sensibilité de l'oracle k(d) s'annule près de zéro, « retenir 80 % du dommage » n'est pas mesurable dans le régime diffus : les deux issues tombent dans le bruit de l'oracle.
- **Corrélation de rang de l'oracle.** Une corrélation globale est dominée par les gros défauts plantés. Elle doit être calculée sur la plage de d qui définit le diffus ; sinon, elle ne dit rien du régime visé.
- **« Mortalité > 90 % » de l'organisme d'idéation.** Ce taux dépend de la prévalence vrais/faux choisie par l'équipe. Il faut la fixer avant la mesure.

### (c) Contrôles négatifs dont l'absence serait fatale

- **Consigne cachée bénigne *et* réglage fin bénin, dans E1 et E3.** Ils sont absents des deux, alors que le point 2 ci-dessus rend le gain possiblement artificiel.
- **Contrôle d'efficacité de l'attaque pour E2.** Il faut reproduire qualitativement l'évasion sur une tâche simple, conformément à ce que rapporte arXiv 2412.09565 (RAPPORTÉ), avant de conclure à une taxe sur la tâche complexe.
- **Essaim honnête de K copies munies d'adaptateurs bénins** (E3). L'essaim honnête nu est prévu, mais il ne contrôle pas l'empreinte de construction.
- **À garder** : le contrôle « honnête régularisé » d'E2 et les « voies méthodologiques alternatives valides » pour l'oracle. Ils sont bien posés.

---

## Sur la proposition D

### (a) Défauts de méthode

1. **La FPR hors domaine d'E1 est basse par construction.**
   - Agent et jumeau partagent le modèle de base. Un changement de sous-domaine affecte les deux et s'annule dans la différence pour un honnête de même base.
   - Pour un agent muni d'un adaptateur, le changement de domaine interagit avec l'adaptateur : les alarmes viennent de l'adaptateur, pas du sabotage.
   - Le contrôle « second modèle honnête de style distinct » est la bonne idée, car c'est le seul des trois dispositifs qui approche η.
   - Mais ce contrôle risque de dépasser 5 % par construction. S'il entre dans la FPR de H_B, H_B devient vraie par construction. D doit dire lequel des deux compte.

2. **Le lot de 50 propositions réelles hors vérité plantée** n'a pas de référence. Sur ce lot, seul le volet FPR est jugeable ; le « dommage relatif » ne l'est pas. D l'inscrit pourtant dans les mêmes critères.

3. **La normalisation canonique d'E2 est elle-même un instrument déplaçable.**
   - Le résumé est produit par un modèle qui lit le texte de l'agent.
   - Ce résumé peut effacer la faille : le rappel baisse alors avec ou sans attaque, et la faible chute sous attaque rend H_A vraie pour une mauvaise raison.

4. **Les duels violent B4.** Les zones grises suivantes (illustratives) ne falsifient rien :
   - E1 : FPR entre 2 % et 5 %, dommage entre 25 % et 50 % ;
   - E2 : chute de rappel entre 10 et 30 points ;
   - E3 : ratio entre 1,2 et 2, ou désaccord entre les deux échelles de modèle.

5. **Le critère de succès est quasi vrai par construction.** « Soit la tenue conjointe de (i)–(iii), soit le seuil exact où l'une cède » : seul l'échec du banc reste réfutable.

6. **L'exclusion des mitigations par entraînement retire la rivale principale.**
   - La rivale est la thèse d'arXiv 2606.08892 (RAPPORTÉ), selon laquelle la surveillance est « less promising ».
   - Aucun duel de D ne peut la falsifier.
   - L'exclusion est justifiée par le coût, pas par un argument ; A juge au contraire ce duel faisable.

7. **Le régime asymétrique (saboteur de 70 milliards de paramètres contre jumeau de 8, illustratif) est confondu par construction.** Le différentiel détecte l'écart de compétence entre tailles, pas le sabotage.

8. **L'argument d'ordonnancement est insuffisant.** L'« accumulation linéaire d'un biais » est vraie pour une somme. Elle ne l'est plus pour un test séquentiel recalibré par fenêtre. Elle ne suffit pas à imposer l'inversion des papiers.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **Indistinguabilité à la Le Cam.** La condition doit s'écrire sur l'ensemble d'incertitude : si P_1 ∈ {P : TV(P, P̂_0) ≤ ε}, aucun test ne sépare P_1 de P_0, quel que soit T.
  - Comme ε est estimé et dépend de la tâche, c'est sup_tâches ε_tâche qui compte, pas un ε moyen.
  - D compare un ε unique à la dérive par pas.
- **E2 avec 100 paires (illustratif).** Si ces paires servent aussi de négatifs de calibration, la FPR vraie suit Beta(2, 99), soit environ 2 % ± 1,4 %. Une chute de rappel de 10 points peut alors se confondre avec l'erreur du seuil.
- **Les 50 relectures humaines (illustratif).** L'intervalle à 95 % sur une proportion proche de 0,5 a une demi-largeur d'environ 1,96·√(0,25/50) ≈ 14 points. Le critère « 80 % de la dégradation subsiste » ne se distingue pas de 66 %.
- **Critère « AUC de l'oracle ≤ 0,55 hors vérité plantée ».** Les étiquettes sont humaines et rares. Si l'accord humain–humain est proche du hasard, l'AUC oracle–humain est plafonnée par le bruit des étiquettes, et le critère d'échec devient vrai par construction.
- **Réplication d'E3 sur deux échelles.** Si la variance de l'effet entre familles de modèles est grande devant l'effet lui-même, deux points ne suffisent pas à distinguer « l'effet se transfère » de « coïncidence ».

### (c) Contrôles négatifs dont l'absence serait fatale

- **Consigne et réglage fin bénins** : D les prévoit dans E3, ce qui est un mérite. Ils manquent dans E1 et E2, alors que l'agent y porte la même intervention.
- **Rappel sans attaque après normalisation** (E2). Sans lui, une normalisation qui efface tout passe pour une défense.
- **Accord humain–humain** sur le lot hors vérité plantée. Sans lui, le seuil d'AUC n'a pas de plafond connu.
- **Jumeau honnête de même taille que le saboteur** dans le régime asymétrique. Sans lui, la taille et le sabotage restent confondus.
- **À garder** : les « moniteurs neutres calibrés à α » prévus pour tester l'organisme d'idéation et l'arbitre formel.

---

## Ce que cette critique ne tranche pas

- Je ne dis pas laquelle des trois conceptions est la meilleure ; B1 me l'interdit.
- Chaque défaut ci-dessus se corrige par un contrôle ou par une condition à calculer avant la mesure.
- Le défaut le plus lourd, parce qu'il touche la quantité centrale, est le même sous trois formes :
  - chez A, η estimé jumeau contre jumeau ;
  - chez C, la soustraction du jumeau sans contrôle d'intervention ;
  - chez D, l'annulation du décalage de domaine par la base commune.

  Dans les trois cas, la ligne de base honnête est estimée avec un objet qui partage, par construction, ce qu'il faudrait mesurer.
- Je ne sais pas si un proxy inter-modèles de η est assez proche de l'erreur réelle en déploiement pour sauver une borne. C'est une question empirique, et aucune des pièces ne la pose comme duel.

FIN-DE-CELLULE