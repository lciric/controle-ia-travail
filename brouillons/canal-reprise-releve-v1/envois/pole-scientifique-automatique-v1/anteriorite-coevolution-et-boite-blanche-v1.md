# Antériorité — co-évolution attaque/défense, et moniteurs boîte blanche — v1

Lignée conv-audit, 28 octobre 2026. Deuxième et troisième des trois recherches d'antériorité lancées sur le « go » de
Lazar (12:49 heure de Paris) pour la question élevée. Rendues par deux sous-agents neufs.

**Statut R7 : tout RAPPORTÉ d'après résumés / pages HTML lues par un sous-agent, rien vérifié sur PDF empreinté. Aucun
chiffre ni aucune citation n'est opposable avant vérification.** Contrainte respectée par les deux sous-agents : aucune
technique d'attaque ni charge utile ; les contributions côté attaque ne sont nommées que par classe et protocole
d'évaluation.

## A. Co-évolution attaque/défense avec généralisation à des familles tenues à l'écart

**Verdict : partiellement occupé, moins ouvert qu'il n'y paraît.**

Occupé, à ne pas revendiquer comme neuf :
- **SafeCoEvo** (arXiv 2609.36580, 2026, préimpression) — collision la plus nette : co-évolue une garde d'exécution qui
  surveille un agent, modèle de tâche figé, partie de test tenue à l'écart. **À citer comme l'occupant le plus proche, pas
  comme fond.** Réserve : sa sélection se fait sur une validation **en-distribution** (partage scénarios et groupes de
  tâches avec le flux d'évolution) ; l'axe tenu à l'écart est « scénarios/outils », **pas** « familles d'attaque ».
- Durcissement itéré red-team/blue-team d'un moniteur comme **pratique** : Anthropic « Auto Mode » (billet du 22 oct 2026) ;
  UK AISI Control Red Team (billet, juillet 2026). Pas de critère de généralisation, durcissement manuel.
- La généralisation comme quantité **mesurée** dans une boucle co-évolutive : Chong, Tiňo, Yao, IEEE TEC 2008 (stratégies
  de jeu, pas des moniteurs) — 18 ans.
- Autres, plus loin : AgentSafeEvo (2610.19422, fait évoluer la politique du défenseur, pas un moniteur) ; RvB
  (2601.19726, patchs de code + règles de garde-fou, généralisation hors-domaine revendiquée) ; MAGIC (2602.01539,
  politique de refus) ; MonitoringBench (2605.09684, moniteurs **figés**, axe tenu à l'écart = moniteurs) ; EvoDefense
  (2605.31140, chevauchement entraînement/test). Terekhov et al. **ICLR 2026** (attaques adaptatives subvertissent des
  moniteurs de confiance ; moniteurs figés, mitigations en travaux futurs) — seul avec Chong/Tiňo/Yao à être relu par les
  pairs ; le reste sont des préimpressions ou billets.

**Résidu défendable (apparemment ouvert ; INFÉRÉ, à vérifier sur PDF)** : la **famille d'attaque comme axe tenu à
l'écart pour un moniteur de comportement d'agent**, et surtout la **généralisation comme critère de sélection lui-même**
(aptitude = performance sur des familles tenues hors de la conception, pas performance de validation en-distribution).
L'union des quatre — moniteur d'agent + co-évolution + famille tenue à l'écart + généralisation-comme-aptitude — n'est
tenue par aucun travail trouvé. **Recommandation du sous-agent** : rétrécir la revendication au critère de sélection et à
l'axe famille, citer SafeCoEvo comme occupant le plus proche. **Nœud (modification de revendication) : GO de Lazar.**

## B. Moniteurs boîte blanche (activations internes) pour sabotage / tromperie d'agents

**Verdict : la croyance « la boîte blanche seule fait toute l'originalité » est RÉFUTÉE.**

Le champ est **peuplé** :
- « Telling FIBS » (anc. « Caught in the Act »), arXiv 2610.12445, oct 2026 — sondes multi-couches qui détectent le
  **sabotage** agentique et la tromperie, et **battent** un moniteur boîte noire sur SHADE-Arena et BashArena (aire sous
  la courbe rapportée 98,3 contre 97,7 ; 98,0 contre 97,6). Comparé au boîte noire, **pas combiné** ; **pas** de test sur
  familles tenues à l'écart.
- Goldowsky-Dill et al., **ICML 2025** — sondes linéaires, tromperie stratégique, aire 0,96–0,999.
- McKenzie et al., **NeurIPS 2025** — cascade sonde→modèle, hors-distribution central.
- Kramár et al. (Google DeepMind), jan 2026 — sondes **en production dans Gemini**, cascade sonde+Flash, ≈ 10 000× moins
  cher.
- Parrack et al. (juillet 2025) — **fait déjà le joint** boîte noire + sonde (ensembles). Kumar (mai 2026) — meilleur
  protocole de généralisation trouvé (matrices de transfert entre domaines, styles tenus à l'écart), mais styles/domaines,
  **pas** familles d'attaque délibérément retirées.

Ce qui est **déjà fait** : le **joint boîte blanche + boîte noire** (trois fois : ensembles, cascades) — mais **jamais
sur des menaces diffuses / entre épisodes**. Ce qui **n'est pas** fait : la généralisation à des **familles tenues à
l'écart**. Deux papiers « notre cadre exact » sont **100 % boîte noire** : Terekhov et al. (tâches floues, diffus,
arXiv 2606.08892) et UK AISI (attaques distribuées multi-agents, 2607.07368).

**Territoire survivant (INFÉRÉ ; R8 — vérifier plus durement avant toute revendication)** : l'**intersection** — menaces
diffuses / entre épisodes **×** joint boîte blanche + boîte noire **×** familles tenues à l'écart, sous juge figé avec
garantie de fausses promotions. Étroit, mais non trouvé occupé.

## Conséquence pour le programme

1. Ne pas revendiquer « la boîte blanche » comme l'originalité (réfuté), ni « la course aux armements co-évolutive »
   (occupée : SafeCoEvo et al.).
2. L'originalité défendable est l'**intersection** ci-dessus, plus la **généralisation comme critère de sélection** sur
   familles tenues à l'écart. Zone séduisante → R8 → **vérifier sur PDF** et **recadrer avec l'organisme et le
   collisionneur** (Lazar, 12:52) avant toute revendication.
3. Falsifiabilité : « notre défense bat notre attaquant » est de l'auto-jeu quasi infalsifiable (critique standard,
   Tramèr et al. 2020) ; « notre défense généralise à une famille jamais conçue, au degré k » peut échouer — c'est ce qui
   rend la version asymétrique **préférable**, pas « plus forte » dans l'absolu.

## À vérifier sur PDF avant tout préenregistrement (R7)

SafeCoEvo : construction exacte de la partie tenue à l'écart, y a-t-il une stratification par type d'attaque ; « Telling
FIBS » : confirmer l'absence de test tenu à l'écart (lecture partielle) et le titre (retitré) ; AgentSafeEvo et MAGIC :
existe-t-il une partie tenue à l'écart dans les tableaux complets ; McKenzie : lieu de publication. Statut de revue par
les pairs : seuls Terekhov et al. (ICLR 2026), Chong/Tiňo/Yao (IEEE TEC), Goldowsky-Dill (ICML 2025), McKenzie
(NeurIPS 2025) confirmés ; le reste préimpressions/billets.
