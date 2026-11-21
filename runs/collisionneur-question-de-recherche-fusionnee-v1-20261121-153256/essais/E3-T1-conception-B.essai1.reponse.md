# Proposition B : ce qui ne s'achète pas

**Pièces.** Les FAITS sont complets, mais aucun item n'y porte d'étiquette de statut. Je les traite donc comme RAPPORTÉ. Font exception les passages que le texte qualifie lui-même de jugement ou d'hypothèse (étau à 0,35 et 0,15, « toute la question » du directeur) : ceux-là restent HYPOTHÈSE ou opinion RAPPORTÉE. Je ne vois pas A, C ni D à ce tour, et je n'ai donc rien à critiquer chez eux.

**Thèse.** La seule chose que l'adversaire ne peut pas changer à bas prix, c'est l'**indépendance entre un tirage frais, fait après l'épisode, et tout ce que l'agent peut calculer pendant l'épisode**. Tout le reste ne fait que déplacer une constante : sondes, pince, relations honnêtes. La profondeur consiste à écrire la borne exacte, à nommer ses trois suppositions et à mesurer chacune en service.

---

## 1. L'expert, et le généraliste

**Ce que ferait un expert du contrôle des IA sans qu'on le lui demande** (HYPOTHÈSE sur la pratique) :
- Il fixerait d'abord l'unité de dommage et le budget d'étiquettes.
- Il mesurerait ensuite, avant toute attaque, le **plancher de bruit σ** : la variance de la différence entre deux exécutions honnêtes de la même tâche, telle que l'oracle la voit.
- Il calculerait la valeur du jeu inspecteur-fraudeur pour ce σ. C'est la démarche de Greenblatt, Shlegeris, Sachan, Roger, *AI Control: Improving Safety Despite Intentional Subversion* (2023), mais posée en estimation d'un total plutôt qu'en détection.

**Ce qui est implicite et non établi.** Le « jumeau honnête » qui définit le dommage existe sur le banc, parce que le saboteur y est construit. En service, il n'existe pas, puisque l'agent est le suspect (HYPOTHÈSE non établie, centrale).

**D'où partirait un généraliste :**
- **Audits électoraux à risque limité** : Lindeman & Stark, *A Gentle Introduction to Risk-Limiting Audits* (2012). On échantillonne pour borner une erreur totale sans reconnaître le mode de fraude.
- **Comptabilité nucléaire des matières** : le « non-comptabilisé », déjà dans les faits. Avenhaus, von Stengel, Zamir, *Inspection Games* (2002, Handbook of Game Theory).
- **Sondages** : Horvitz & Thompson (1952), estimateur sans biais d'un total sous probabilités d'inclusion connues.
- **Logiciel N-versions** : Knight & Leveson (1986). Des versions écrites indépendamment échouent ensemble, ce qui décrit nos détecteurs voisins.
- **Écologie** : la capture-recapture estime ce que personne n'a vu.
- **Économie** : l'agglutinement sous un seuil (Saez, 2010) trahit l'optimisation contre un barème.
- **Vie privée différentielle** : Dwork & Roth (2014), pour borner ce qu'une correction révèle.

## 2. Données brutes de départ

Ce sont des données par épisode et jamais des taux agrégés (statut : proposition) :
1. La trajectoire complète, hachée.
2. Le tirage secret, son horodatage et sa probabilité d'inclusion π_i, **engagés par hachage avant l'audit**.
3. Les scores du moniteur à chaque pas d'action, engagés avant le tirage. Aucune moyenne sur les jetons : lecture à des positions fixées.
4. Le verdict **de chaque lecteur séparément**, avec ses extraits cités, et non le vote.
5. Des paires honnête-honnête sur la même tâche, pour mesurer σ.
6. Un indice de difficulté par tâche : le taux de réussite du modèle de confiance.
7. Les événements de correction et leur instant.
8. Pour les épisodes corrigés, la branche non corrigée rejouée en bac à sable par le harnais.

## 3. Méthodes et outils : ce que chacun suppose, comment il échoue

| Outil | Suppose | Échoue quand |
|---|---|---|
| Estimateur de Horvitz-Thompson + séquence de confiance (Ville, 1939 ; Freedman, *On tail probabilities for martingales*, 1975 ; Howard, Ramdas, McAuliffe, Sekhon, *Time-uniform, nonparametric, nonasymptotic confidence sequences*, 2021) | Tirage indépendant du passé et de d_i ; d_i borné ; oracle non influençable | L'oracle est biaisé par l'attaque (persuasion) ; le tirage fuit ; le dommage n'est pas additif (assemblage) |
| Test par paris / e-processus (Shafer, *Testing by betting*, 2021 ; Ramdas et al., *Game-theoretic statistics and safe anytime-valid inference*, 2023) | Alternative composite, arrêt optionnel | Même chose ; perte de puissance si le pari est mal choisi |
| Audit à risque limité (Lindeman & Stark, 2012) | Un résultat déclaré à comparer | Pas de résultat déclaré : il faut le jumeau honnête, absent en service |
| CUSUM (Page, 1954), SPRT (Wald) | Lois avant et après connues | Alternative inconnue : remplacer par des e-processus |
| Mélange défensif (Hesterberg, *Weighted average importance sampling and defensive mixture distributions*, 1995) | Plancher π_min > 0 | Ne protège pas l'oracle, seulement l'échantillonnage |
| Mutants plantés (DeMillo, Lipton, Sayward, 1978, « Hints on test data selection ») | Les défauts plantés ressemblent aux vrais | Genre jamais vu : la couverture mesurée ne dit rien de lui |
| Capture-recapture à deux lecteurs | Indépendance des lecteurs | Lecteurs corrélés : sous-estimation, d'où la nécessité de mesurer la dépendance sur des défauts plantés |
| Lentille réglée (Belrose et al., *Eliciting Latent Predictions from Transformers with the Tuned Lens*, 2023) ; Halawi, Denain, Steinhardt, *Overthinking the Truth* (2023) | Les prédictions intermédiaires sont lisibles et liées à la sortie | Représentations déplacées (2412.09565, RAPPORTÉ) |
| Surveillance par une copie non fiable avec pots de miel (Greenblatt et al., 2023) | La copie ne distingue pas un pot de miel d'un vrai produit | Point focal partagé |
| Vie privée différentielle (Dwork & Roth, 2014) | Le mécanisme est aléatoire avec un rapport borné | Aucune fuite bornée si l'audit déclenche une action visible pendant l'épisode |

Le « billet du 30 avril 2025 » sur les menaces diffuses est probablement de Redwood Research : pas sûr. Le rapport de 1985 sur les garanties : référence à vérifier.

## 4. Vérifier hors du programme

- **Couverture par un tiers.** Une équipe extérieure exécute la borne sur des mondes plantés, y compris la famille tenue à l'écart, et rapporte la couverture empirique.
- **Ordre des engagements.** Les hachages des tirages et des scores sont publiés chez un tiers horodateur avant l'audit.
- **Revue statistique.** Des spécialistes des audits électoraux ou des garanties nucléaires relisent le plan d'échantillonnage.
- **Réplication** sur des modèles ouverts.
- **Bornes préenregistrées** avant d'ouvrir les données.

Le directeur juge la couverture de l'oracle « toute la question » (opinion, RAPPORTÉ). J'y ajoute deux paramètres aussi décisifs : σ, et l'indépendance effective du tirage.

## 5. Ce que la question suppose, et reformulation

**Ce que la question suppose sans que ce soit établi :**
- Le dommage est additif entre épisodes : HYPOTHÈSE, que l'assemblage viole.
- Un jumeau honnête est disponible en service : HYPOTHÈSE, et c'est la plus fragile.
- L'oracle ne peut pas être influencé par l'agent : HYPOTHÈSE. La vérification mot à mot des citations est RAPPORTÉ, mais elle ne couvre pas la persuasion.
- « Tout sabotage délibéré doit nécessairement faire » quelque chose de lisible : HYPOTHÈSE.
- Le plafond par épisode est effectif : RAPPORTÉ comme élément du dispositif, son efficacité est HYPOTHÈ