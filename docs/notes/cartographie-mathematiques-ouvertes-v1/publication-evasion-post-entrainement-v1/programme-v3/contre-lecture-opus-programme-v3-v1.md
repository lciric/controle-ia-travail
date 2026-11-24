# Contre-lecture du programme et de la feuille de route de publication du papier D, v3

- **Pièce contre-lue** : `strategie-cibles-et-feuille-de-route-publication-papier-d-v3.md` (bloc-notes, rédigée par Claude Fable 5.2), avec son script `calc/controle_v3.py`.
- **Contre-lecteur** : Claude Opus 5.5, effort élevé, neuf. Je n'ai pas écrit la pièce. Aucun fichier du dépôt ni de la pièce n'a été modifié.
- **Date** : 24 novembre 2026.
- **Calculs refaits** : script de l'auteur relancé (`python3 -I`), sorties identiques à celles qu'il annonce. Mes contrôles indépendants sont dans `scratchpad/verif-opus/verif_opus.py` et `verif_opus_2.py` (graines `SeedSequence(20261124)`).

## Verdict

**Accepté avec corrections.**
- Les chemins, les empreintes et presque tous les états « fait / non fait » tiennent.
- Les quatre calculs annoncés se reproduisent.
- Les contraintes sont respectées : aucune dépense, ni Lean ni arbre exact à quatre bras avant le 1er décembre, aucune diffusion, aucune date présentée comme vérifiée.

Six défauts sont à corriger avant que la pièce serve de programme :
- deux corrections de la v2 qui sont elles-mêmes inexactes ou incomplètes (normalisation par groupe ; point fixe sous normalisation par les survivants) ;
- une condition prêtée à Lazar qui n'est pas dans son mot ;
- une option déséquilibrée dans la décision sur la cible ;
- un accord antérieur de Lazar sur un dépôt public, renvoyé à la mère au lieu de lui être soumis ;
- plusieurs propositions de la note absentes de la table.

Aucun défaut bloquant : la pièce ne touche ni le manuscrit, ni une dépense, ni une porte.

## Défauts

### 1. La correction de la v2 sur la normalisation par groupe va trop loin (à corriger)

**Emplacement.** Section 8, ligne 7. Répercuté en section 1, point 6 ; section 2, ligne 13 ; section 4 (« prédiction à deux horizons ») ; section 7.3, tâche 4.

**Constat.** La v3 dit que l'affirmation de la v2 (« pénaliser le visible abaisse la moyenne du groupe et accélère directement le gradient relatif de la triche furtive », sous normalisation par groupe avec ou sans division par l'écart-type) est « contredite trois fois ». C'est vrai pour certaines quantités, faux pour d'autres, et le signe dépend de la géométrie du gradient. Mes calculs, en champ moyen, sur le modèle tabulaire à trois strates, niche parfaite ($\beta_{\mathrm f}=1$), 100 000 tirages :

- **Ligne de base par la moyenne seule, sans division par l'écart-type** (la « RLOO » nommée par la v2). L'avantage du furtif, $r_{\mathrm f}-\mu$, croît avec $C$ dans 100 000 tirages sur 100 000 : sa dérivée vaut $(1-\beta_{\mathrm v})\pi_{\mathrm v}>0$. Sous gradient naturel, c'est le taux de croissance de $\log\pi_{\mathrm f}$ : la pénalité l'**accélère** à l'instant. Le taux du furtif contre l'honnête, lui, ne change pas ($=\Delta R$). Pour ce cas, l'affirmation de la v2 est donc juste à la lettre.
- **Avec division par l'écart-type** (la normalisation par groupe proprement dite, « GRPO »).
  - L'avantage normalisé du furtif décroît en $C$ dans 100 000 tirages sur 100 000 : ici la v2 est contredite.
  - En revanche, le taux du furtif contre le visible, $(1-\beta_{\mathrm v})(\Delta R+C)/\sigma$, **croît** avec $C$ dans 75 289 tirages sur 100 000. Le brouillon en champ moyen dit seulement que ce taux reste borné (« does not accelerate … *without bound* », point 3). Il ne dit pas que la pénalité ne l'accélère pas. La passation `papiers/D/passations/2026-11-24-0918-…` le résume aussi comme « taux borné ».
- **Le freinage transitoire** ($\pi_{\mathrm h}>1/\sqrt3$), que je confirme, vaut sous gradient euclidien sur les logits. Sous gradient naturel (règle (a) du brouillon de dynamique, et le flot du brouillon en champ moyen), $\log\pi_{\mathrm f}$ est au contraire accéléré. Le brouillon de dynamique le dit lui-même : « The effect of the monitor must be read within one geometry » (`dynamics-section-v1-correctif-3.tex`, paragraphe « Geometry of rule (c) »).
- **Le retrait de Carbon** porte sur une affirmation voisine (représentations orthogonales), pas sur celle de la v2.

**Conséquence.** La « prédiction à deux horizons » (freinage transitoire, puis amplification à l'équilibre) n'est pas une prédiction du modèle. C'est une prédiction pour une géométrie donnée, et son signe s'inverse sous gradient naturel.

**Correction proposée.** Récrire la ligne 7 ainsi :
- l'affirmation de la v2 est ambiguë ;
- elle est vraie pour l'avantage du furtif sous ligne de base seule ;
- elle est fausse pour l'avantage normalisé et pour le rapport du furtif à l'honnête sous division par l'écart-type ;
- le taux du furtif contre le visible peut croître avec la pénalité, mais reste borné ;
- sur la croissance de $\pi_{\mathrm f}$, le signe dépend de la géométrie (freinage sous gradient euclidien si $\pi_{\mathrm h}>1/\sqrt3$ ; accélération sous gradient naturel).

En section 4 et en section 7.3, écrire « proposition sur l'effet instantané de la pénalité, par géométrie (euclidienne et naturelle) », au lieu de « freinage transitoire ».

Accessoirement, en section 2, ligne 15 : la division par l'écart-type laisse invariant le rapport $(R_0+C)/\Delta R$. Ce qui devient non réglable, c'est la pression effective $\eta/\sigma(\pi)$, donc les produits $\eta\Delta R$ et $\eta(R_0+C)$. Mieux vaut le dire ainsi que « la pénalité effective ».

### 2. Le point fixe sous normalisation par les survivants : il manque le cas qui correspond à la formule de la v2 (à corriger)

**Emplacement.** Section 8, ligne 5, colonne « Ce que dit la v3 ».

**Constat.** La colonne du milieu identifie bien la formule de la v2 : ce sont les équilibres du gradient sur les seuls acceptés, normalisé par leur nombre, avec leur moyenne pour ligne de base (brouillon de dynamique, proposition « Regularised discard policy gradient »). Je le confirme. La colonne de droite donne ensuite trois cas :
- lot entier, sans ligne de base : pénalité de score brut nul ;
- ligne de base constante : pénalité déplacée d'autant ;
- lot rempli de survivants : pénalité de score brut nul, à pression auto-cohérente.

Les deux premiers sont exacts, et le troisième l'est **sans ligne de base** (c'est ce que dit le manuscrit, remarque « Which training procedures realize each operator »). Mais la formule de la v2 réunit le remplissage et la ligne de base par la moyenne des acceptés. Son point fixe est la pénalité à $C=-b(\pi)$, l'épisode intercepté étant noté comme la moyenne acceptée, à pression $\eta/\bar Z(\pi)$ : une rétroaction positive, absente de la pénalité à score fixe, d'où la multiplicité des équilibres (brouillon de dynamique, l. 700-705). Vérifié sur un exemple ($p=(0{,}85;0{,}14;0{,}01)$, $\beta=(1;0{,}2;0{,}6)$, $\eta=1{,}5$) :
- écart de $3\cdot10^{-15}$ à la pénalité à $C=-b$ et pression $\eta/\bar Z$ ;
- écart de 0,016 à la pénalité de score brut nul.

Tel qu'il est écrit, le lecteur peut croire que la formule de la v2 se ramène au troisième cas, ce qui serait faux. « Selon la base » est en outre ambigu (ligne de base, ou base retenue ?).

**Correction proposée.** Ajouter un quatrième cas : « lot rempli de survivants, avec leur moyenne pour ligne de base (formule de la v2) : pénalité à $C=-b(\pi)$, pression $\eta/\bar Z(\pi)$, rétroaction positive, plusieurs équilibres possibles ». Écrire « selon la ligne de base » au lieu de « selon la base ».

### 3. Une condition est prêtée à Lazar sans qu'elle figure dans son mot (à corriger)

**Emplacement.** Section 6, « Décision de Lazar (mot du 24 novembre, R-5284) » et « Inscription au programme ».

**Constat.**
- L'extrait de R-5284 dit deux choses : (b) une remarque au manuscrit, maintenant ; (a) un théorème resserré après le 1er décembre, sur préenregistrement neuf. Il ne dit pas « et seulement si la cible visée l'exige ». Cette restriction vient du mandat de la mère. La pièce la met pourtant en gras, sous le nom de Lazar.
- La « condition d'ouverture » (la cible doit faire entrer la section dans la version soumise, à un niveau où un facteur 2,5 serait une faiblesse) et la « priorité basse » restreignent encore son mot. Ce sont des recommandations, présentées comme inscrites.
- « Une remarque au manuscrit, maintenant : faite ». La remarque n'est que dans le brouillon de la section sur le budget d'audit, qui n'est pas dans le manuscrit de base. La pièce le dit, mais coche quand même « faite ». Si la version courte part sans cette section, le mot de Lazar n'aura pas d'effet visible.

**Correction proposée.**
- Séparer le mot de Lazar, cité tel quel avec sa source, de la restriction du mandat.
- Présenter « seulement si la cible l'exige », la condition d'ouverture et la priorité comme une proposition soumise à Lazar, puisqu'elles restreignent un accord donné. Si un autre mot de Lazar contient cette restriction, le citer.
- Écrire « faite dans le brouillon de section, hors du manuscrit de base ».

### 4. Décision sur la cible : une option est déséquilibrée (à corriger)

**Emplacement.** Section 5(a), option 3. Comparer avec la section 2, ligne 16c, et la section 7.4, ligne 3.

**Constat.** L'option 3 range la conférence de l'Institute of Electrical and Electronics Engineers sur l'apprentissage automatique sûr et digne de confiance sous « attendre une expérience ». Or la note dit qu'Opus la place, en piste courte, **pour le manuscrit actuel** (A, III.1). Carbon la préfère comme cible ; Neon la donne en alternative. La pièce le rapporte elle-même en section 7.4 (« Opus pour le manuscrit actuel, en piste courte »). La voie « cette conférence maintenant, en piste courte si elle existe » manque donc parmi les options présentées à Lazar.

**Correction proposée.** Scinder l'option 3 en deux :
- 3a : cette conférence, en piste courte, avec le manuscrit de base, si la piste existe ;
- 3b : attendre une expérience et viser une conférence principale.

Chacune avec son avantage et son inconvénient.

### 5. Propositions de la note absentes de la table (à corriger)

**Emplacement.** Section 2.

**Constat.** La table couvre l'essentiel, mais plusieurs propositions de la note n'y ont ni ligne ni statut. Par ordre d'importance :
1. **La sonde interne tenue hors de la boucle**, comparée au juge sur le texte :
   - duel d'Opus III.1, « l'audit hors boucle garde-t-il son taux de faux négatifs ? » ;
   - duel de Neon III.1, « sonde interne contre juge sur le texte », et ses rejets partiels au III.3 (juge en mesure secondaire) ;
   - Opus III.3, « sonde entraînée sans exemples furtifs », contre la covariance imposée par construction que relève Carbon au III.2.

   C'est le bras qui éprouverait le mécanisme d'audit du théorème 2. La ligne 8 (repasse dans les poids gelés) ne le couvre pas.
2. **Le plan croisé entre affinage complet et affinage de faible rang** (Carbon III.3). Neon avait relevé au III.2 que l'affinage de faible rang pourrait lui-même induire le couplage testé.
3. **La porte « égalité des bras sans détecteur »** (Carbon III.3), à côté de la qualification sur cas exact et de la translation.
4. **La loi jointe continue de $(\Delta R,\beta)$ avec contexte** (Carbon III.1), voisine de l'extension par la méthode de Laplace de la v2.
5. **Trois points que la note range parmi ce qui pourrait être neuf** (section 5 de la note) :
   - la linéarité du rejet pur en $\beta$, qui rend exacte l'agrégation par classe (Opus et Carbon III.3) ;
   - l'extinction d'une niche rare par l'estimation de la divergence en politique (Carbon III.3) ;
   - la borne exacte pour la classe composée de la politique et du banc de test (Neon III.3).
6. **La vacuité du régime des pièges quand leur support est disjoint** (distance en variation totale de 1 ; Neon III.1). Elle mérite une phrase au manuscrit ; la pièce ne l'évoque qu'à propos de la v2.
7. **Ligne 28** : les autres non retenues de la note manquent. Ce sont le contrôle négatif qui prédit le même signe que l'hypothèse rivale, l'ajustement à 0,90 sur quatre points, le conditionnement sur un taux de triche post-traitement et le rééchantillonnage sur graines.

**Correction proposée.** Une ligne et un statut pour chacun ; au minimum pour les points 1 et 2, à transmettre aussi à la session du préenregistrement sur modèle ouvert, qui a une sonde figée et une sonde réapprise.

### 6. Un accord antérieur de Lazar sur un dépôt public, renvoyé à la mère (à corriger)

**Emplacement.** Section 8, ligne 11 ; section 7.1, ligne « Toute diffusion ».

**Constat.**
- L'accord GO-2026-11-24-05 (registre des accords, l. 883) autorise un petit dépôt public compagnon. C'est déjà un geste de Lazar.
- La v3 ajoute des préalables à toute diffusion (antériorité, références, règles des appels) et laisse « l'exécution de l'accord antérieur à confirmer par la mère ».
- Suspendre ou conditionner un accord de Lazar n'appartient ni à la pièce ni à la mère.

**Correction proposée.** Soumettre ce point à Lazar, sans défaut, sous forme de troisième point ou de sous-point de (a). Question : l'accord sur le dépôt public compagnon tient-il tel quel, ou attend-il les préalables de la section 7.1 ? Garder la recommandation d'attendre, avec sa raison.

### 7. Un état « déjà fait en partie » surévalué (mineur)

**Emplacement.** Section 2, ligne 4.

**Constat.** La proposition porte sur la qualification du **code d'entraînement** sur un cas exact.
- Les trois bancs témoins de l'expérience de seuil qualifient un simulateur du calendrier d'audit, pas un code d'entraînement.
- Le script du correctif 3 calcule des points fixes par gradients en espérance exacte, sans entraîner.

Les deux appliquent le principe, mais ailleurs. La pièce dit bien qu'aucun code d'entraînement n'existe. Le statut reste flatteur.

**Correction.** Statut : « principe déjà appliqué à d'autres codes (chemins) ; pour l'objet visé, non fait, reporté ».

### 8. Qui choisit la réalisation de référence du rejet pur (mineur)

**Emplacement.** Section 2, ligne 3, contre section 5(b), « Dans tous les cas ».

**Constat.** La ligne 3 soumet ce choix à Lazar avec le point (b). La section 5(b) le range dans la conception par Fable, « pas de la présente pièce ».

**Correction.** Choisir une seule formulation, par exemple : « proposé par la conception de Fable, arrêté avec la décision (b) ».

### 9. « Ce que la note ignorait » : citation déformée (mineur)

**Emplacement.** Section 2, paragraphe final.

**Constat.** La note écrit : « Le manuscrit ne contient ni expérience sur réseaux ni preuve mécanisée » (l. 23). C'est toujours vrai du manuscrit. La v3 cite « il n'y avait … », comme si la note s'était trompée sur l'existence de Lean.

**Correction.** Citer exactement, et dire que les brouillons et Lean existaient hors du manuscrit.

### 10. Traces internes : un « lien laissé en attente » introuvable (mineur)

**Emplacement.** Section 7.1, « Traces internes à retirer ».

**Constat.** Le manuscrit de base porte « [Author Name] » et une note d'auteur interne, mais aucun lien en attente : j'ai cherché `github`, `url`, `href` et les marques entre crochets.

**Correction.** Retirer « et le lien », ou citer la ligne.

### 11. Identifiants internes en guise de nom (mineur, forme)

**Emplacement.** Section 7.2, tâche 6 (« les lignes 5 à 11, 15, 19, 20 et 25 de la table ») ; cellules « soumise à Lazar (b) » de la section 2.

**Constat.** La règle du programme veut un groupe nominal explicite, avec le numéro entre parenthèses seulement.

**Correction.** Nommer les propositions dans la tâche 6 : bras de masquage, classes aveugles au détecteur, tests disjoints, repasse dans les poids gelés, taux de faux négatifs à taux de fausses alertes fixé, nombre de graines, abandon de la normalisation par groupe et test de translation, critères mesurés avant l'entraînement, vérifications mécaniques, classe « échec ». Dans la table, écrire « soumise à Lazar (banc de code à niches construites) ».

### 12. Préalables de diffusion incomplets dans le calendrier (mineur)

**Emplacement.** Section 4 (« trois gestes ») ; section 7.2.

**Constat.**
- La section 4 annonce trois gestes. La section 7.1 en exige davantage : vérification du billet et de la page de dépôt, règles lues, phrase sur le filtre de sortie.
- Le registre des références (correction 8) demande de lire sur PDF, avant soumission, les affirmations attribuées à Price, Robertson et Fisher, cités **dans le manuscrit de base** ; ces PDF sont à fournir par Lazar. Aucune tâche de la section 7.2 ne les lui demande.
- La dépendance « décision (a) : appels de l'année lus » peut bloquer si les appels de 2027 ne sont pas encore parus fin novembre.

**Correction.**
- Aligner la section 4 sur la section 7.1.
- Ajouter en section 7.2 la demande des PDF de Price, Robertson et Fisher à Lazar.
- Prévoir un repli : consigner l'appel de l'année précédente, marqué « indicatif ».

### 13. Précisions de chiffres et d'empreintes (mineur)

- Section 1.1, ligne du billet et de la page de dépôt : une seule empreinte pour deux fichiers. Celle de la page de dépôt est `ca195464f3870b8c…`. L'empreinte de l'erratum de la note manque (`d82ebef9a0b3af5b…`).
- Section 6, « 2 à 57 % de trop » : le dénominateur est le budget de référence $B^\star_{\mathrm{unif}}$ (remarque du brouillon : « of the reference budget »), pas le budget réservé. Le dire.
- Section 8, ligne 2 : la v2 écrivait « > 80 % à TMLR **avec expériences contrôlées** ». Citer la condition.
- Section 2, ligne 13 : « le mot réplicateur n'y figure pas » est exact. Mais le flot de gradient naturel tabulaire sans ancre (règle (a) du brouillon) est la dynamique du réplicateur sur la partition. Dire « déjà traitée sous le nom de gradient naturel ».
- Section 5(a), option 2 : « une théorie déjà archivée oblige ensuite à un article expérimental autonome » dépend des règles de double soumission, non vérifiées. Marquer « à vérifier ».
- En-tête, ligne 15 : phrase boiteuse (« dont le lecteur de la note était déjà »). Écrire : « le lecteur de la note était déjà un Opus 5.5 ».

## Ce qui a été vérifié et tient

**Empreintes et chemins.** Toutes les empreintes de la section 1.1 et de la section 1.2 concordent avec les fichiers sur disque ou sur les branches distantes :
- manuscrit de base `25d094dd…` ; script et sortie du correctif 3 ; note du correctif 2 ; deux audits ;
- préenregistrement de seuil et son erratum ; témoin des bancs ; brouillons de budget d'audit, de dynamique, du champ moyen et du découplage ;
- table de Lean ; registre des références ; préenregistrement et devis sur modèle ouvert ; v1 et v2 de la stratégie ;
- note de sortie sur `origin/runs/collisionneurs-reprise-2026-11-24-v1` (`d26699cc…` ; version PDF `62f26113…`) ;
- verdict de seuil sur `origin/lecture/seuil-papier-d-v1` (`6967654e…`).

**Fidélité à la note.** Pour les lignes 1 à 28, les sources (modèle et tour) sont exactes. L'erratum sur la réflexion d'Opus est intégré. Les désaccords non tranchés (revue à évaluation continue, pièges tirés parmi des épisodes réels, Lean) sont rapportés fidèlement.

**Déjà fait.**
- La condition de l'inversion est au théorème 1, point 4(c), et sa forme générale avec $R_0$ dans la section « Task Reward and In-Loop Monitor ».
- Le coût de maintien ($\delta_{\mathrm{maint}}$) et $\tau_{\mathrm{ord}}$ sont définis dans la base.
- La remarque « Which training procedures realize each operator » dit ce que la pièce en rapporte : grand lot depuis l'erratum 1, « not claimed in general ».
- Les chiffres du script du correctif 3 sont exacts : neuf cas de translation, écart d'au plus $2{,}2\cdot10^{-16}$, translation naïve de 0,015 à 0,35 ; grille de 384 cas, 20 000 tirages, 64 points en arithmétique à 50 chiffres, aucun défaut.
- Les audits disent bien « accepté avec corrections », puis « corrections acceptées », avec une réserve sur le grand lot, levée par l'erratum 1 (vérifié par différence de fichiers).
- Les dix corrections de l'audit et le défaut majeur sur la suffisance des trois hypothèses sont attestés.

**État des autres travaux.**
- Lean : 30 théorèmes en cinq fichiers, sans `sorry`, alignés sur le correctif 1 de la v4, installés sur le mot de Lazar.
- Références : 80, dont 76 concordantes, 1 corrigée, 1 année à trancher, 2 non confirmées, et 8 corrections à porter. Skaf et al., Gupta et Jenner, Baker et al. et Korbak et al. y figurent bien.
- Préenregistrement sur modèle ouvert :
  - non scellé ; vérification des corrections interrompue ; six décisions ouvertes ;
  - bras sans filtre, rejet répété, pénalité et filtre au hasard, sans masquage ;
  - soupçon gradué, donc survie par épisode ;
  - variable principale « triché et non intercepté », avec la vérité par programme ;
  - huit à douze paires ;
  - étage d'étalonnage de 16 à 86 heures, second étage de 66 à 601 heures, sans prix ;
  - textes du tour 0 réencodés au tour K ; aire sous la courbe pour les sondes.
- Le brouillon en champ moyen se limite au cas sans ancre ; aucune contre-lecture trouvée.

**Calculs, refaits.**
1. Condition de l'inversion avec $R_0\neq0$ : 0 désaccord sur 100 000 tirages, par le script de l'auteur relancé.
2. Freinage sous gradient euclidien : la formule $-(1-\beta_{\mathrm v})\pi_{\mathrm v}(\sum\pi^2-\pi_{\mathrm v}-\pi_{\mathrm f})$ est juste. Le seuil $1/\sqrt3$ est exact : en minimisant $\sum\pi^2$ à $\pi_{\mathrm h}$ fixé, on obtient $3\pi_{\mathrm h}^2>1$. Le signe est négatif dans les 17 750 tirages annoncés. La portée est à restreindre (défaut 1).
3. Pièges par mélange : $\sup dP_{\mathrm{ord}}/dP_{\mathrm{trap}}\le 1/(1-q)$, avec égalité atteinte (20 000 lois discrètes tirées au hasard). Avec $M=1/(1-q)$, le seuil de la v2 se retrouve exactement.
4. Point fixe sous division par l'écart-type, avec ancre : $\pi\propto p\,e^{\eta\bar r/\sigma(\pi)}$, écart de $2{,}8\cdot10^{-15}$. C'est en fait une dérivation générale d'une ligne, et pas seulement un exemple. Avec ancre, la normalisation déplace bien l'équilibre.
5. Seuil de la v2 sous borne de rapport de densité, et poids de Laplace $\Gamma(\gamma)[\eta(\Delta R+C)]^{-\gamma}e^{\eta\Delta R}$ au premier ordre : justes. Leur statut d'options non dérivées dans le dépôt est correct.
6. Les trois premiers cas de la ligne 5 de la section 8 sont justes (défaut 2 pour le quatrième).
7. Section 8, ligne 8 : la borne de rapport de densité est bien infinie pour des supports disjoints.

**Marge du plancher d'audit.** Tous les chiffres de la section 6 sont conformes au verdict de lecture et à la remarque du brouillon (`f546547e…`) :
- 137 points sur 138, le point n° 31 non concluant ;
- fréquence d'au moins 0,86 sans marge ;
- facteur de 1,75 à 3,56, médiane 2,49 ;
- de 2 à 57 % du budget de référence, médiane 10,5 % ;
- 32 points calculés exactement.

« Deux fois moins d'audits » est bien écarté.

**Contraintes et calendrier.**
- Aucune dépense.
- Lean, arbre à quatre bras, théorème resserré et toute conception de banc sont hors de la période d'avant le 1er décembre.
- Aucune diffusion.
- Toutes les dates sont dites « proposées » ; toutes les échéances de conférence sont « à vérifier dans l'appel de l'année ».
- Aucune probabilité d'acceptation.
- Les coûts des modèles sont donnés comme illustratifs et attribués à leurs auteurs.

**Points soumis à Lazar.** Les points (a) et (b) restent ouverts, sans défaut (ce sont des nœuds de décision), avec trois options chacun. Les recommandations sont marquées comme telles, avec leur confiance, et ne sont pas présentées comme des décisions, sauf en section 6 (défaut 3) et pour l'accord sur le dépôt public (défaut 6).

**Corrections de la v2, lignes 1 à 4, 6, 8 à 13.** Elles sont justes et sourcées. « Zéro erreur » est démenti par les corrections de l'audit, la licence du plus petit modèle Qwen est « other » selon l'inventaire, et le devis est en heures sans prix.

**Forme.** Aucun acronyme nu, hors « PDF », d'usage courant dans le dépôt. Les identifiants internes sont entre parenthèses, sauf au défaut 11. Aucun texte interne n'est destiné au manuscrit.
