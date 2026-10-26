# Proposition B — Tour III.2 : équipe rouge croisée

**État des pièces.** Le bloc FAITS est vide, et il le signale lui-même ; je travaille sur le texte de la question. Les pièces A et C sont présentes et complètes : chacune se termine par sa ligne de fin, rien n'est coupé.

**Statuts.** Je reprends ceux de la question. Toutes mes affirmations sur des mécanismes sont des HYPOTHÈSES, sauf mention contraire. Tous les seuils et coûts que je cite sont **illustratifs**.

**Un point de statut pour Lazar, que je ne tranche pas.** A et C donnent des statuts différents aux mêmes éléments :
- les chiffres de l'essai : RAPPORTÉ chez A, OBSERVÉ-NON-AUDITÉ chez C ;
- la revue d'antériorité interne : OBSERVÉ-NON-AUDITÉ chez A, « VÉRIFIÉ dans le cadre » chez C.

L'écart est à arbitrer par Lazar ; je ne change aucun statut.

---

## Contre la proposition A

### (a) Failles

**A1. Le témoin « 50 directions aléatoires de même norme » est battu par construction (E2, E5, table (c)).**
- Dans un espace résiduel de grande dimension, une direction tirée de façon isotrope a une projection faible sur les activations réelles. En première approximation (HYPOTHÈSE sur ces modèles), cette projection est de l'ordre de ‖h‖/√d.
- La direction d'une sonde est au contraire apprise **sur** les données. Elle se loge dans un sous-espace de forte variance.
- Annuler la projection sur la sonde retire donc beaucoup plus de norme qu'annuler une direction aléatoire. Le critère « au-dessus du 95ᵉ centile des directions aléatoires » est presque acquis d'avance, quel que soit le concept.
- L'anisotropie connue des flux résiduels (dimensions aberrantes) peut atténuer l'écart ou l'aggraver. Rien dans A ne le mesure.
- Le témoin « direction sac-de-mots » corrige en partie le problème, mais une seule direction ne fait pas une distribution nulle.

**A2. La KL calculée sur les jetons où la sonde dépasse son 95ᵉ centile croît mécaniquement (E2).**
- Annuler une projection modifie davantage l'activation là où cette projection est grande.
- Conditionner la mesure sur ces jetons garantit donc un effet plus fort que sur les autres. C'est une identité, pas une découverte.
- Il faut comparer la sonde à une perturbation de **même amplitude** sur les mêmes jetons.

**A3. Les hypothèses H_A et H_B d'E2 ne sont pas exclusives au sens de B4.**
- « Projection nulle sans effet » ne veut pas dire « non lue ». Le réseau peut lire la direction et disposer d'un chemin de secours, ou se réparer en aval.
- Références à vérifier : McGrath et al., 2023, *The Hydra Effect: Emergent Self-repair in Language Model Computations*. Dans l'autre sens, une intervention sur un sous-espace peut activer une voie dormante et créer un effet qui n'existait pas : Makelov, Lange et Nanda, 2023, *Is This the Subspace You Are Looking For? An Interpretability Illusion for Subspace Activation Patching*.
- A ajoute bien trois couches en aval, mais ne propose aucun test qui sépare « non lue » de « lue mais redondante ».
- La conclusion de A pour l'issue H_B (« falsifie l'option (A) comme critère négatif ») repose donc sur une issue qui ne veut pas dire ce qu'elle dit.

**A4. E1 compare la sonde à un témoin trop faible.**
- Le **thème** n'est pas seulement lexical : il peut être sémantique. Un texte qui paraphrase « on te met à l'épreuve » sans aucun mot de la liste reste dans le thème.
- Battre un sac-de-mots de 0,10 d'AUROC ne falsifie donc pas « thème » ; cela falsifie seulement « lexique de surface ».
- Il manque un témoin sémantique : un classifieur sur un encodeur de phrases externe et gelé, ou une sonde sur la couche 0 (C l'a, voir plus bas).

**A5. E1 contient aussi une fuite possible de construction.**
- Les cellules « test sans lexique » sont écrites par des gens qui savent ce que la sonde est censée détecter.
- Si la sonde a été entraînée sur des structures proches, les cellules croisées évaluent la distribution d'entraînement.
- A n'impose ni des générateurs disjoints de ceux de l'entraînement, ni un étiquetage des cellules à l'aveugle du score.

**A6. Le contraste nul d'E3 est dégénéré par construction.**
- Deux paraphrases du même contenu ont une différence de logits proche de zéro.
- Un pipeline d'attribution qui vise cette différence ne peut rien y trouver. Le témoin passe donc toujours, et ne teste rien.
- Le témoin utile est un contraste de **même amplitude** de différence de logits, avec une cause sans rapport : registre, thème, ou le « témoin impératif » de C.

**A7. La validation d'E3 n'est pas indépendante si les 400 contrastes sortent des mêmes gabarits.**
- Recherche et validation partagent alors leurs traits de surface.
- Il faut une validation tirée d'une **autre famille de gabarits**, écrite par un autre rédacteur.

**A8. E3 laisse deux choix ouverts qui décident du résultat.**
- Le type d'ablation n'est pas fixé (zéro, moyenne, rééchantillonnage). Mettre à zéro des neurones SwiGLU sort des distributions d'activation et gonfle les effets. Référence à vérifier : Zhang et Nanda, 2023, *Towards Best Practices of Activation Patching in Language Models: Metrics and Methods*.
- Les graphes « à neurones bruts » ne couvrent que les MLP. Une porte qui passe par les têtes d'attention est invisible par construction, et E3 conclurait H_B à tort.

**A9. E4 contient trois biais de construction.**
- **Effet plancher.** La rigueur est mesurée sur des tâches à vérité connue (faits datés, calculs). Ces tâches ressemblent elles-mêmes à des tests, ce qui peut saturer la conscience d'évaluation dans les quatre cellules.
- **La mesure favorise le bras qui la demande.** « Taux d'incertitude exprimée » avantage le bras maïeutique, qui demande explicitement les incertitudes. « Nombre d'affirmations vérifiables » avantage les réponses longues, et la longueur de **sortie** n'est pas appariée.
- **Le facteur « demande d'audit » est du lexique.** « Demande explicite × lexique doux » contient quand même des mots d'audit. Les deux facteurs ne sont pas séparables à 100 %.

**A10. Le modèle de base n'est pas un témoin interprétable dans E4.** Il ne suit pas les consignes multi-tours. Ses écarts entre bras ne mesurent pas « l'effet d'entraînement » mais l'incapacité à suivre le cadre.

**A11. E5 est en partie circulaire avec E1.**
- Les textes doivent être « honnêtes, non-test », mais qui en juge ? Si c'est un agent qui voit le texte, l'issue H_B (« n'atteignent pas ce centile sans structure de test ») dépend d'un jugement de « structure de test » non opérationnalisé.
- Un agent neuf qui produit 100 textes en un coup représente un adversaire faible. Conclure, pour l'issue H_B, que « la fiche peut être rendue publique sans coût de contrôle » dépasse ce que le test mesure. Un adversaire itératif est absent.

**A12. Le test H_B d'E6 réussit par construction.**
- Il décode des concepts hors fiche depuis les activations faibles de 100 neurones pris **ensemble**, avec une sonde linéaire.
- Une population de 100 variables continues permet presque toujours de décoder beaucoup de concepts corrélés aux concepts des fiches.
- E6 ne sépare pas « superposition » de « corrélation entre traits ». Il faut un témoin : les mêmes sondes sur des concepts **décorrélés** de ceux des fiches (corrélation résiduelle contrôlée). Et l'AUROC doit être comparée à celle de 100 neurones choisis au hasard, faibles activations comprises.

**A13. Deux points de statut.**
- Le label « VÉRIFIÉ : propriété statistique élémentaire » sur « le max croît avec la longueur » est un raisonnement, pas un fait du programme. Ce n'est garanti que si les jetons ajoutés viennent **après** un préfixe inchangé, avec une attention causale. Si les injonctions sont ajoutées en tête, rien n'est garanti. Je le note sans changer le statut.
- A et C supposent tous deux des comportements post-entraînement (refus, hésitation), alors que le cadre ne dit pas si Llama-3.1-8B et Qwen2.5-7B sont des versions de base ou instruites. C'est à fixer avant toute mesure de comportement.

### (b) Scénarios d'évasion

Ces scénarios visent deux types d'agents adverses : le **modèle** sondé, s'il porte un état de test qu'il « cache », et l'**organisme**, s'il obtient un jour un accès aux lectures. Tout ce qui suit est HYPOTHÈSE.

**La sonde lue au max (E1, moniteur).**
- *Évasion.* L'état est porté hors de la direction sondée, ou seulement à des positions que la lecture couvre mal. Pour un modèle, le coût est nul : aucune pression d'entraînement ne l'aligne sur notre sonde.
- *Attaque inverse, moins chère.* Le max sur les jetons est sensible à **un seul jeton**. Un organisme qui insère du lexique d'évaluation partout fait monter la sonde sur tous ses textes : les fausses alertes explosent et le moniteur ne discrimine plus. Le coût est d'un jeton par texte.

**La projection nulle (E2).** La redondance naturelle suffit à obtenir un verdict « non lue » alors que l'état est utilisé, sans aucun coût pour l'adversaire. A3 rend ce verdict non falsifiant.

**La porte (E3).** Un calcul réparti sur des milliers de neurones, ou qui passe par l'attention, rend tout ensemble ≤ k neurones inopérant. Le coût est nul. Le verdict H_B serait alors lu comme « pas de porte » au lieu de « pas de porte dans la base MLP ».

**La spoofabilité (E5).** Un adversaire qui reçoit un retour (score par texte) fait une escalade. Le test de A, en un coup sur 100 textes, ne borne pas ce cas. Coût : le nombre de requêtes, inconnu (illustratif : quelques centaines).

**Toutes les défenses à la fois.** Un organisme qui réécrit ses formulations pour que le comportement du modèle reste « de test » tout en déplaçant l'état hors de la sonde obtiendrait :
- une sonde basse (E1 dit « pas d'état ») ;
- une projection nulle sans effet (E2 dit « non lue ») ;
- pas de porte (E3 dit H_B).

Tous les instruments s'accordent alors sur « rien ». Seule une mesure **comportementale indépendante de la sonde** contredirait ce verdict. A n'en a une que dans E4, sans la relier au moniteur.

La « mesure de fuite » de A (primitive réelle contre primitive bruitée) détecte une dérive **sur la sonde surveillée**. Elle ne voit pas un déplacement vers une couche ou une direction non surveillée.

### (c) Contrôles négatifs dont l'absence est fatale

1. **Des directions témoins appariées en variance**, tirées de la covariance des activations, plus un panel de sondes de concepts sans lien entraînées comme la sonde. Sans eux, E2 et E5 sont vrais par construction (A1).
2. **Une perturbation d'amplitude égale sur les mêmes jetons** pour la KL conditionnelle (A2).
3. **Un témoin sémantique** (encodeur externe gelé, sonde sur la couche 0) en plus du sac-de-mots (A4).
4. **Une sonde à étiquettes permutées**, lue au max sur les mêmes textes. Elle contrôle l'inflation due au max et la capacité de la sonde.
5. **Un contraste nul de même amplitude de logits** et une validation sur des gabarits disjoints (A6, A7).
6. **Un type d'ablation fixé d'avance** (moyenne ou rééchantillonnage) et une couverture de l'attention, ou une déclaration explicite que H_B ne vaut que pour la base MLP (A8).
7. **Une élicitation finale identique dans les quatre cellules d'E4**, puis une rigueur normalisée par la longueur de sortie, notée par un juge aveugle au bras (A9).
8. **Un jugement « honnête / non-test » des textes d'E5 à l'aveugle du score**, et un adversaire itératif (A11).

---

## Contre la proposition C

### (a) Failles

**C1. Des statuts relevés sans source.**
- Les dimensions des modèles (couches, dimension résiduelle, dimension intermédiaire) sont marquées « VÉRIFIÉ dans le cadre ». Or le cadre ne nomme que les modèles. Ces valeurs viennent de mémoire : elles sont à vérifier sur les fichiers de configuration avant d'entrer dans un budget. Je ne change pas leur statut ; je signale l'écart.
- Même remarque pour « Elhage et al. … **démontrent** que … la compression optimale projette les traits hors de la base canonique ». C'est un résultat sur des modèles jouets. Le transposer à un 8B est une HYPOTHÈSE, et « mécaniquement plus forte » à 7B/8B l'est aussi.

**C2. L'expérience 1 a les mêmes témoins isotropes que A (même faille que A1), plus deux défauts propres.**
- *La contrainte de perplexité ne contraint rien.* « ΔPPL < 5 % sur WikiText » n'élimine presque aucune intervention de rang 1, puisqu'enlever une direction change rarement la perplexité globale.
- *Pas de condition préalable.* « ΔP > 0,15 » suppose qu'il existe au départ un écart de comportement entre contexte d'évaluation et contexte neutre. C n'impose cette mesure qu'à la toute fin (ΔP > 0,20), pas comme condition d'E1.
- Si le 8B ne se comporte pas différemment sous évaluation, E1 « falsifie H_A » par effet plancher, et C en conclut « moniteur passif valide ». Rien dans E1 n'autorise cette conclusion.

**C3. H_B de l'expérience 1 regroupe des hypothèses incompatibles.** « Épiphénoménal **ou** lexical **ou** chemins redondants » : la redondance est un **usage**. L'issue nulle ne falsifie donc pas H_A (voir A3, et la référence McGrath et al. à vérifier).

**C4. Dans l'expérience 2, le témoin favorise le dictionnaire par construction.**
- On compare 50 neurones sélectionnés par attribution à une direction dense de rang 1 **apprise** sur le pli de découverte, qui pondère librement toute la couche. Les degrés de liberté ne sont pas comparables.
- Le critère « neurones < 0,20 alors que dense ≥ 0,50 » penche donc d'avance vers la falsification de la thèse de l'essai.
- Le témoin SAE exige un auto-encodeur épars sur le 8B. Le budget affirme pourtant « aucun entraînement de SAE n'est requis », ce qui est une incohérence interne. Il existe peut-être des SAE publics pour Llama-3.1-8B (référence à vérifier), mais C ne le dit pas.
- L'attribution linéaire (gradient × écart d'activation) est fragile précisément sur les « doubles négations » SwiGLU que l'essai met en avant. Avec 10 pas, les gradients intégrés réduisent le problème sans le traiter.

**C5. L'expérience 3 contient deux biais de construction opposés.**
- *Le score de Brier favorise la maïeutique.* Il suppose des probabilités ou des incertitudes déclarées. Or le bras maïeutique est **celui qui les demande** : sans élicitation finale identique dans les quatre bras, la calibration est mesurée là où on l'a sollicitée.
- *La densité d'assertions vérifiables favorise la coercition.* Une réponse brève et affirmative a plus d'assertions par jeton qu'une réponse qui expose ses doutes.
- Les deux biais tirent en sens inverse ; l'issue dépend de leur poids relatif, pas du cadre.

**C6. La maïeutique de C est à un seul tour.**
- La question M définit la maïeutique comme un **échange**. Un bras maïeutique en un tour est une version affaiblie, et C reconnaît lui-même le « un tour » dans l'issue nulle.
- Un nul sur ce dessin ne dit rien sur la question M.
- L'appariement de perplexité à 10 % entre registres opposés sélectionne aussi des prompts atypiques, ce qui coûte en validité écologique.

**C7. Des hypothèses composites qui laissent des issues sans verdict (contraire à B4).**
- Dans l'expérience 3, H_A et H_B sont chacune une conjonction de plusieurs clauses. Beaucoup d'issues mixtes, par exemple « A_max différent mais I_vérif égal », ne falsifient rien.
- Dans l'expérience 4, une AUC entre 0,50 et 0,75 ne falsifie rien non plus. Il y a une zone morte.

**C8. Deux fuites dans l'expérience 4.**
- *L'explication décrit le jeu d'entraînement, pas la sonde.* L'agent 1 l'établit à partir des textes du **pli d'entraînement**, qui portent par construction les étiquettes ayant servi à apprendre la sonde. Il faut un corpus d'activation tenu hors de l'entraînement.
- *L'agent 2 connaît le but du test.* Il écrit les deux batteries en sachant laquelle doit gagner, ce qui permet de confirmer ou d'infirmer sans le vouloir. Il faut des rédacteurs distincts, aveugles au but.

**C9. Le « vrai état sans lexique » d'E4 peut rester lexical.** Les « pièges logiques classiques » sont probablement des éléments de bancs d'essai connus du modèle. Leur caractère « test » peut passer par la reconnaissance du contenu mémorisé, donc par un indice de surface que la liste noire ne couvre pas. E4 réussirait alors sans établir un état abstrait.

**C10. La primitive bornée fuit encore (table (c) et section (d)).** Ne renvoyer que des statistiques agrégées par lots d'au moins 20 textes ne ferme pas la fuite :
- un organisme qui fait varier une partie du lot et garde le reste fixe lit, par différence entre deux lots, l'effet de la partie variée sur la médiane et l'écart interquartile ;
- le filtre de quasi-copies (cosinus ≥ 0,85) devient une frontière apprenable dès que les refus sont visibles. C'est un oracle de similarité avec la banque de tâches.

Je n'en tire aucune stratégie de classement. Je constate que la borne proposée n'est pas une borne.

**C11. Le critère global de falsification dépend d'un réglage.** « Combinaisons denses de plus de 500 neurones » : la parcimonie d'une sonde dépend de sa régularisation. Ce seuil se fixe par le choix de la pénalité ; c'est vrai par construction.

### (b) Scénarios d'évasion

**La dissociation lexicale (E4).** Un modèle qui reconnaît l'évaluation par la familiarité du contenu (C9) passe E4 et échoue sur une évaluation nouvelle. Le coût est nul. Le verdict « la sonde capte l'état » serait faux en déploiement.

**La primitive agrégée.**
- *Comment.* Un organisme lit, par différence entre lots, quelles variantes de formulation font baisser la sonde (C10).
- *Coût.* Deux lots par comparaison (illustratif), donc une partie du plafond.
- *Effet.* Des formulations « maïeutiques » qui gardent la sonde basse quel que soit l'état du modèle.

**La porte (E2).** Comme chez A : un calcul réparti ou passant par l'attention, sans coût. S'y ajoute le biais de C4 : le dictionnaire « gagne » même si l'information est présente dans les neurones.

**L'usage causal (E1).** Avec de la redondance, le verdict « épiphénomène fidèle » est obtenu sans coût, et le programme abandonne à tort l'intervention (N-015).

**Toutes les défenses à la fois.** C combine sa matrice 2×2 (dissociation × usage) avec le plan à 4 bras. Un adversaire qui :
- déplace l'état hors de la sonde ;
- laisse un comportement de test ;
- profite du bras maïeutique en un tour ;

obtient la case « dissociation échouée + usage nul ». C prescrit alors l'« abandon immédiat de l'architecture de sonde ». L'attaque fait donc **retirer** le moniteur, ce qui est le résultat le plus favorable pour l'adversaire, pour un coût faible.

### (c) Contrôles négatifs dont l'absence est fatale

1. **Des directions témoins appariées en variance** et un panel de sondes de concepts sans lien (C2), et non seulement des directions isotropes.
2. **Un écart comportemental de départ mesuré et préenregistré** comme condition d'entrée d'E1 et d'E3. Sans écart, l'issue nulle est non informative (C2).
3. **Un témoin dense à budget comparable** (sonde éparse à 50 coordonnées dans la base neuronale, contre 50 coordonnées dans une base aléatoire orthonormée). Il remplace la comparaison avec une direction dense libre (C4).
4. **Une élicitation finale identique dans les quatre bras**, puis une rigueur normalisée par la longueur, notée à l'aveugle du bras (C5).
5. **Un bras maïeutique en plusieurs tours**, apparié en nombre total de jetons à un bras coercitif en plusieurs tours (C6).
6. **Un corpus tenu hors de l'entraînement pour l'agent 1**, et des rédacteurs aveugles au but pour chaque batterie (C8).
7. **Des items d'évaluation implicite inédits** (non issus de bancs connus) dans la batterie positive (C9).
8. **Une attaque différentielle contre la primitive agrégée**, menée par l'expérimentateur avant tout octroi (C10).
9. Je reprends le témoin de C sur **un modèle à poids aléatoires**. Il manque chez A ; il est présent chez C et doit rester.

---

## Ce que je reprends, en le disant (B1)

- **De C**, le bras 4 « témoin impératif hors audit ». C'est le meilleur contraste nul non dégénéré des deux pièces. Il corrige A6.
- **De C aussi**, la sonde sur la couche 0 et le modèle à poids aléatoires. Ils corrigent A4.
- **De A**, la mesure de fuite « primitive réelle contre primitive bruitée ». Elle corrige en partie C10, sous réserve du point sur les directions non surveillées.
- **De A aussi**, la lecture d'E5 comme mesure de **spoofabilité** plutôt que de validité.

## Deux tests de mes propres attaques (inférence forte)

Les seuils sont illustratifs ; tout est préenregistré.

**T1 — Le témoin aléatoire est-il vrai par construction ?**
- *Hypothèses.* H_A : l'effet de la projection nulle de la sonde reste au-dessus du 95ᵉ centile **même** contre des directions appariées en variance et un panel de sondes sans lien. H_B : l'effet dépasse les directions isotropes mais tombe dans la distribution des directions appariées.
- *Issues.* H_B vraie : les critères d'E2 (A) et d'E1 (C) sont invalides tels qu'écrits, et A1/C2 sont confirmées. H_A vraie : mon attaque A1/C2 est réfutée pour ces modèles, et les deux propositions gardent leur témoin.

**T2 — La primitive agrégée fuit-elle ?**
- *Hypothèses.* H_A : un agent de l'expérimentateur, sans accès aux tâches, reconstruit par différences de lots le classement de sonde de textes individuels avec une corrélation de rang > 0,5 (illustratif), dans un budget égal au plafond prévu. H_B : il n'y parvient pas mieux qu'avec une primitive bruitée de même distribution.
- *Issues.* H_A vraie : la correction architecturale de C est falsifiée, et l'option (D) reste exclue. H_B vraie : mon attaque C10 est réfutée à ce budget. Cela ne dit rien d'un budget plus grand.

Le résultat de T2 n'est servi à aucun organisme.

FIN-DE-CELLULE