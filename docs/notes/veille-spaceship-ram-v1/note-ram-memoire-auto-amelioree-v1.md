# Veille — billet « Self-Improving Memory » de l'équipe RAM de Meta : ce qu'il prend à nos idées d'héritage entre générations, ce que vaut son gain, et l'essai qu'il suggère — v1

- **Rédacteur** : lecteur neuf, sous-agent de la session mère, le 18 novembre 2026 (03:15 à 03:55 UTC). Rien lancé sur
  un modèle, rien dépensé, rien committé.
- **Objet lu** : `docs/sources/web/ram-memoire-auto-amelioree-v1/page.html`
  (`87488923c7089fd61c6d203dcc75e3dd359a59048ba040ba09a90e93c45bc38a`, égale à son compagnon ; relue en ligne à 03:23 UTC :
  même empreinte). La page versée ne porte que le texte ; j'ai versé ses sept figures sous
  `sources/figures-billet-ram/` et j'en ai lu trois à l'œil (figures 4, 5 et 6).
- **Décisions lues** : N-044 (`2b70bdac…`), N-045 version 2 (`c7b05e39…`), N-049 (`8a5bf5e5…`), N-050 (`a54b128d…`),
  N-058 (`854f2724…`), sous `docs/decisions/`.
- **Chiffres** : ceux du billet sont **ses** chiffres, recopiés de la page, sans article ni code derrière ; aucun n'est
  opposable (R7). Tout chiffre de prédiction, de puissance ou de devis est mon estimation, et le dit.
- **Statut** : note de veille. L'essai de la section 4 est un **projet**, ni contre-lu ni scellé.

## 1. Verdict

**Utile comme contre-exemple et comme voisin à citer, pas comme résultat.** Le billet fait apprendre à un modèle ses
consignes de mémoire par une recherche à sélection, puis les verse dans ses poids par affinage. Il **occupe en partie**
deux de nos idées (la mémoire transmise comme chose apprise ; l'affinage sur des réponses filtrées) et laisse intact le
reste. Son gain de tête n'est pas séparé du biais de sélection — il l'écrit lui-même — et son propre compte (37 révisions
sur 44 sans progrès) plaide pour notre ordre « le bon marché d'abord » et pour nos gardes « tâches fraîches » et
« lecture unique ». Il pointe enfin un trou de notre course à plusieurs générations : rien n'y établit que l'archive
héritée **cause** les découvertes ; l'essai de la section 4 le comble pour quelques dizaines de dollars.

## 2. Ce qu'il prend à nos idées d'héritage, élément par élément

Ce que fait le billet, en clair : dans chaque tâche, un agent traite une suite de sous-tâches ; entre deux sous-tâches
son contexte est vidé et seul un dossier de fichiers de mémoire passe ; deux consignes règlent ce qu'il y écrit et ce
qu'il y relit. Un second agent (le même modèle, Kimi-K2.6) lit les trajectoires et les scores des sous-tâches
d'entraînement et réécrit ces deux consignes ; chaque réécriture est évaluée par cinq passages de la suite entière ; les
quatre meilleures servent de parents. Ensuite, le modèle rejoue avec les consignes retenues, on remet les consignes
génériques dans les trajectoires enregistrées, et on affine le modèle dessus (adaptateurs de rang faible, rang 64).

« Libre » veut dire ici **libre au regard de ce billet**, jamais « libre dans le champ » (R8).

| n° | notre idée (source) | ce que fait le billet | verdict |
|---|---|---|---|
| 1 | La **mémoire transmise** est une chose que l'organisme apprend, le noyau ne la fixe pas (N-045 v2, énoncé 1) | La politique de mémoire (quoi écrire, comment ranger, quand relire) est apprise, par recherche sur deux consignes puis par affinage. Mais la mémoire passe entre les sous-tâches d'**un** agent, pas entre les générations d'un organisme qui se réécrit ; et c'est une boucle extérieure qui apprend, pas l'organisme en course. Le billet cite deux travaux qui cherchent déjà des conceptions de mémoire (ALMA, arXiv 2602.07755 ; MemEvolve, arXiv 2512.18746 — notices lues, PDF non lus) | **occupé en partie** |
| 2 | L'**héritage d'une génération est récompensé** : le signal couvre plusieurs générations, le bandit à un pas est exclu (N-045 v2, énoncé 5) | À l'échelle des sous-tâches, oui par construction : le score d'une suite entière paie ce qu'une sous-tâche écrit pour les suivantes. À l'échelle des **générations de conception**, non : les parents sont choisis sur leur seul score moyen, une réécriture qui ne bat pas le meilleur est perdue même si elle ouvrait la suite. C'est le bandit à un pas que nous excluons | **libre** au regard du billet ; **voisin hors billet à lire avant toute revendication** : « Huxley-Gödel Machine » (arXiv 2510.21614), dont le résumé décrit une mesure qui agrège les performances des **descendants** d'un agent pour guider la recherche — absent du dépôt (recherche du nom dans les fichiers de texte de `docs` et `registres` : rien) |
| 3 | **Instruments à effet différé** : sondes et adaptateurs entraînés à la génération t, servis à t+1 (N-045 v2, énoncés 1 et 5) | Un adaptateur est entraîné sur les trajectoires de la recherche et servi ensuite, **une fois, en fin de course** ; il ne revient pas dans la recherche. Le billet cite deux travaux qui **alternent** recherche du harnais et affinage (Co-Harness, arXiv 2607.22688 ; WHALE, arXiv 2609.00196 — notices lues, PDF non lus) : ceux-là sont plus près de nous que le billet | **voisin** (le billet) ; **occupé en partie, à vérifier sur PDF** (les deux travaux qu'il cite) |
| 4 | **Affinage sur réponses filtrées** à la place du renforcement en ligne (N-045 v2, énoncé 4) | C'est son second étage : affiner sur les trajectoires produites sous les consignes que la sélection a gardées | **occupé en partie** |
| 5 | **Distillation du concepteur figé** : affiner un concepteur ouvert sur les réécritures acceptées (N-045 v2, énoncé 4) | Il distille le **produit** (la conduite de l'agent sous les bonnes consignes), pas le **producteur** (l'agent qui réécrit reste figé) | **voisin** ; libre au regard du billet |
| 6 | **Poids contre archive**, à information égale (N-045 v2, énoncé 6) | Il donne une comparaison voisine et non contrôlée : consignes apprises en contexte (56,0 selon lui) contre poids affinés sous consignes génériques (43,1 selon lui) ; évaluations séparées, information non égalisée, et l'objet est l'agent, pas le concepteur. Il dit lui-même que les poids ne gardent qu'« une part » du gain | **voisin** ; indice, sous réserve, en faveur de la voie bon marché (contexte ou archive) |
| 7 | **Tâches fraîches**, vivier par génération, banque sœur, **test final lu une seule fois** (N-044 énoncé 3, N-049, N-050) | L'inverse : sélection et rapport sur la même part de test, mêmes passages (section 3) | **libre** au regard du billet ; ce n'est pas une idée à revendiquer (hygiène connue), c'est un cas d'école du risque |
| 8 | **Séquentiel contre meilleur de N tirages indépendants à budget égal** ; pilote de bruit (N-045 v2, énoncés 4 et 6) | Absents : ni bras « réécritures sans retour », ni mesure du bruit d'une évaluation répétée | **libre** au regard du billet ; son 37 sur 44 est un indice, sur le banc d'un autre, que la révision séquentielle progresse rarement |
| 9 | **Concevoir, puis figer** ; universalité mesurée sur des **familles inédites** (N-044, énoncé 1) | Concevoir puis figer : c'est sa chaîne, et selon lui celle de toute une littérature. Familles inédites : non ; il évalue sur les **mêmes** trois tâches après un changement prévu par le banc, et le dit | concevoir-puis-figer : **occupé** ; mesure sur familles inédites : **libre** au regard du billet |
| 10 | **Coût dans le signal** ; nécessité de la frontière mesurée (N-045 v2, énoncés 2 et 3) | Aucun coût rapporté, un seul modèle | **libre** au regard du billet |

Un point de dessin à retenir : son canal d'héritage porte des **scores** (l'agent qui réécrit lit les scores des
sous-tâches d'entraînement). Le nôtre ne sert que des lois, jamais un verdict (garde de la vue de la boucle fermée) :
notre choix est le plus sûr contre le sur-ajustement adaptatif, et le billet ne donne aucune raison d'en changer.

## 3. Ce que vaut son gain

**Établi sur la page (ses mots ou ses figures).**
- Les scores de tête (56,0 contre 44,6 ; par tâche 53,8, 64,3, 49,9) sont « les meilleurs scores observés parmi les
  candidats évalués », des deux côtés : il l'écrit.
- La sélection se fait sur le score moyen de la **part de test** (la consigne de recherche dit « un jeu tenu à part,
  différent de la part d'entraînement que l'agent qui réécrit peut voir » ; la figure 7 nomme ces scores « test score » ;
  le 43,7 de l'étude de cas est le 43,7 de la figure 4). Les chiffres rapportés sont ces mêmes scores. **Aucune
  réévaluation sur des passages neufs n'est mentionnée.**
- Le vivier de chaque tâche **contient** les quatre consignes écrites à la main ; on garde « le mieux classé ».
  Conséquence que le billet ne tire pas : sur le score de sélection, « optimisé ≥ meilleur écrit à la main » est vrai
  **par construction**. Le signe du gain de tête ne porte aucune information ; seule sa taille, comparée au bruit, en
  porte.
- 37 révisions sur 44 ne battent pas le meilleur score des itérations précédentes ; deux tâches sur trois ne
  progressent plus après la première génération de recherche ; une seule (la tâche sur une base de code) progresse
  jusqu'à la quatrième.
- Le gain de l'affinage (43,1 contre 37,6) est mesuré sur « dix graines d'évaluation appariées » entre deux modèles
  affinés ; l'écart au modèle non affiné est « descriptif », l'évaluation de base étant séparée (ses mots).
- Un modèle, trois tâches d'un banc, test pris dans la suite de la même tâche ; intervalles à 95 % sur cinq passages.

**Non établi.**
- Le gain **net de la sélection**. Le candidat retenu est le maximum d'un vivier de 16 à 20 candidats par tâche
  (4 écrits à la main + 4 révisions par itération ; itérations lues sur la figure 6 : 16 + 16 + 12 = 44 révisions, ce
  qui recoupe son compte) ; le meilleur écrit à la main est le maximum de 4. Ordre de grandeur, **raisonnement et non
  mesure** : si σ est l'écart-type d'une moyenne de cinq passages et si tous les candidats se valaient, le maximum de
  20 dépasserait leur moyenne de 1,87 σ, celui de 16 de 1,77 σ, celui de 4 de 1,03 σ (calcul par tirages, loi normale) ;
  l'asymétrie seule vaut donc environ 0,8 σ. Lus à l'œil sur la figure 4 (non opposable), les intervalles suggèrent un
  σ de l'ordre d'un à deux points : la sélection seule pèserait alors un à deux points. Le gain annoncé sur la base de
  code (20,6) dépasse largement cet ordre ; ceux des deux autres tâches (5,9 et 7,8) n'en sont qu'à quelques σ. **Je ne
  conclus pas** : il manque les scores par passage.
- Une fuite indirecte dans l'étage d'affinage : les consignes qui produisent les démonstrations ont été **choisies sur
  la part de test**, puis le modèle affiné est évalué sur cette même part. Les démonstrations viennent bien de la part
  d'entraînement, mais le choix de ce qu'on distille a vu le test.
- La variance d'une recherche à l'autre (une seule recherche par tâche, semble-t-il), le coût en jetons ou en
  dollars, l'effort mis dans les consignes écrites à la main, le nombre d'affinages essayés.

**Ce qu'il faudrait pour séparer le gain du biais de sélection.**
1. **Graines neuves** : réévaluer la consigne retenue et la meilleure consigne écrite à la main sur des passages qui
   n'ont pas servi à choisir ; mieux, sur une **troisième part** de sous-tâches que la recherche n'a jamais vue (notre
   « test final lu une seule fois », N-050).
2. **Trajectoires** : les scores par passage des 48 candidats de chaque tâche, pour estimer le bruit d'une moyenne de
   cinq passages et le maximum attendu sous l'hypothèse « toutes les révisions valent leur parent ».
3. **Témoin sans effet** : évaluer vingt fois la **même** consigne comme si c'étaient vingt candidats, et mesurer
   l'écart entre le maximum et la moyenne (notre pilote de bruit, N-045 v2, énoncé 6).
4. **Témoin à budget égal** : des réécritures indépendantes, sans retour des scores, en même nombre (notre « meilleur
   de N tirages indépendants », N-045 v2, énoncé 4).
5. **Recherche répétée** à graines différentes, pour la loi du gain final.

**Article ou code ailleurs ?** Cherché le 18 novembre 2026 : arXiv par le titre, par le nom de la méthode et par les
auteurs (`sources/arxiv-recherche-titre-v1.xml`, `…-methode-v1.xml`, `…-auteurs-v1.xml`,
`…-auteur-et-banc-v1.xml`) : **aucun article des auteurs**. Deux recherches sur la toile : rien. Le dépôt public de
l'équipe (`github.com/facebookresearch/RAM`) porte un dossier `projects/self_improving_memory` : selon l'outil qui me
l'a résumé, il ne contient que **le même texte et les mêmes sept figures** — ni code, ni consignes, ni données, ni
scores par graine, ni article. **Limite** : cette liste a été lue par un outil qui résume, pas sur le contenu brut ; et
un article peut exister sous un autre titre ou paraître demain.

## 4. Projet d'essai préenregistrable — la mémoire héritée améliore-t-elle la récupération des lois plantées ?

Nom en clair : **essai de l'héritage sur le monde planté**. Rien n'est lancé. Avant tout lancement : texte au gabarit,
contre-lecture par un sous-agent neuf (R2), scellement (R1), devis, feu vert.

**Pourquoi maintenant.** Le texte de la course à plusieurs générations
(`docs/notes/organisme-multi-generations-v1/preenregistrement-v1/preenregistrement-multi-generations-v1-brouillon6.md`,
`4deec525…`, non scellé) n'a qu'un bras et l'écrit : une découverte sur une composante conditionnelle « n'établit pas
que l'archive a causé la découverte » (point 7 de son résumé). Sa conception
(`docs/notes/organisme-multi-generations-v1/conception-monde-riche-doublons-v7.md`, `1f1b64df…`) **suppose** que les
proposeurs trouvent une composante conditionnelle bien plus souvent une fois sa condition connue (0,02 puis 0,25,
« estimé », point 6 de son résumé). L'essai mesure cette supposition.

**Règles qui gouvernent.** Le juge est **l'oracle du monde planté et le coût mesuré, seuls** ; aucun verdict de
juge-modèle n'entre nulle part (N-058). Aucun score n'est rendu aux proposeurs. Les tables de l'oracle se calculent
après le dernier appel et **se lisent une seule fois, en fin de boucle** (N-050). Mondes neufs, jamais servis ailleurs
(N-049).

### Étage 1 — les propositions seules (le bon marché d'abord)

- **Mondes** : 12 mondes neufs de la famille à composantes conditionnelles (générateur de la conception citée),
  disjoints des mondes de calibration et de développement, secrets engagés par empreinte avant le premier appel ; chaque
  monde porte au moins une composante conditionnelle certifiée.
- **Conditions de vue**, appariées dans chaque monde :
  - *sans héritage* : la vue ne porte que la loi connue de départ ;
  - *héritage des lois* : la vue porte en plus les lois qu'une génération 1 lègue (celles que retient la génération 1
    simulée du banc — code existant, aucun coût de modèle) ;
  - *héritage des lois et carnet* : la même, plus un **carnet** de 2 000 caractères au plus, écrit par un appel de la
    condition « sans héritage » du même monde (ce qu'il a essayé, ce qu'il essaierait) ; c'est l'élément repris du
    billet ; un filtre mécanique refuse tout carnet qui porte un verdict ou un score ;
  - *héritage permuté* (contrôle) : les lois léguées d'un **autre** monde de la famille — sépare « information sur ce
    monde » de « vue plus longue ».
- **Appels** : deux fournisseurs × deux appels par monde et par condition : 192 appels de proposeurs. Ni juge
  statistique, ni tests de mort, ni bac à sable.
- **Métrique** : par condition, part des appels dont au moins une loi proposée **couvre, selon l'oracle, une
  composante conditionnelle certifiée que la vue ne couvrait pas** (critère de vraie découverte de l'oracle, gain
  au-delà de l'enveloppe d'au moins 0,02). Écarts : Δ1 = héritage des lois − sans héritage (principal) ;
  Δ2 = avec carnet − sans carnet ; Δ3 = héritage permuté − sans héritage. Intervalles à 95 % par rééchantillonnage des
  mondes. Second axe : découvertes par dollar mesuré.
- **Prédictions chiffrées et signes** (ancrées sur la supposition de la conception ; a priori du rédacteur pour le
  reste) : **Δ1 = +0,20**, signe +, attendu dans [+0,05 ; +0,40] ; **Δ2 = 0**, attendu dans [−0,10 ; +0,10], sans signe
  affirmé (le 37 sur 44 du billet ne donne pas de raison d'attendre mieux) ; **Δ3 = 0**, attendu dans [−0,05 ; +0,05].
- **Seuils gelés** : « l'héritage cause des découvertes » si la borne basse de (Δ1 − Δ3) est au-dessus de 0 ; « sans
  effet mesurable » si la borne haute de Δ1 est sous 0,10 ; sinon « indéterminé ». Pour le carnet : « utile » si la
  borne basse de Δ2 est au-dessus de 0 ; « nuisible » si sa borne haute est sous 0 ; sinon « sans effet établi ».
- **Plan d'analyse** : gardes d'abord (empreintes des vues servies égales aux vues prévues ; aucun verdict dans une
  vue ; filtre du carnet essayé sur un cas sain et un artefact, R5) ; un test principal (Δ1 − Δ3) ; le reste
  descriptif, par fournisseur. Puissance à calculer par simulation **avant** scellement (R1). Audit de symétrie (R4) :
  un Δ1 au-dessus de 0,6 ou un Δ3 hors de son intervalle déclenche le même audit (fuite du secret du monde dans la vue).
- **Liste d'arrêt** : secret d'un monde lisible par un proposeur ; vue servie différente de la vue prévue ; carnet
  porteur d'un verdict ; plus d'un tiers d'appels sans loi conforme ; plafond de dépense atteint ; tout juge-modèle
  dans la chaîne ; toute lecture d'une table de l'oracle avant le dernier appel.
- **Ce que l'étage ne dit pas** : il mesure l'effet de l'information héritée sur les propositions, avec un héritage
  simulé ; il ne dit rien de la chaîne entière (juge, tests de mort, sélection).
- **Devis (ordre de grandeur, estimé)** : 192 appels. Coût par appel non relu dans les mesures du pilote ; repères du
  dépôt : la course réelle de la plus petite boucle comptait environ 31 appels pour 1,5 à 2 USD attendus, avec une borne
  de 1,50 USD par session de proposeur. **Central : quelques dizaines de dollars (20 à 60 USD) ; pire cas sous la borne
  par session : 288 USD.** Oracle sur processeur. Aucune machine louée si les relais des fournisseurs tournent déjà.

### Étage 2 — la boucle entière, à deux bras (seulement si l'étage 1 dit « l'héritage cause », et sur feu vert à part)

- **Bras** : *chaîné* (deux générations, la seconde lit la sélection scellée de la première) contre *sans héritage, à
  budget égal* (deux générations 1 indépendantes sur le même monde, même nombre d'appels et de tests ; on prend l'union
  de ce qu'elles retiennent) — le témoin « meilleur de N tirages indépendants » de N-045 v2. Mondes appariés.
- **Métrique** : par monde et par bras, « progrès certifié » selon l'oracle (une composante certifiée captée en fin de
  budget, absente à mi-budget) ; test du signe exact, unilatéral, sur les mondes ; coût mesuré par bras.
- **Prédiction** : le bras chaîné progresse dans plus de mondes. Sous le modèle de proposeurs de la conception (0,02
  par appel tant que la condition n'est pas connue, 0,25 ensuite ; quatre appels de proposeurs par génération ; l'unité
  « par appel » est ma lecture du compte « 0 sur 14 appels » du pilote), une génération trouve une composante
  conditionnelle avec une chance d'environ 0,68 quand elle hérite de la condition et d'environ 0,08 sinon : le bras
  chaîné progresserait dans environ deux mondes sur trois (la conception simule 8 sur 12), le bras sans héritage dans
  environ un sur dix. Mon calcul exact du test du signe (seuil 0,05) donne une puissance de **0,70 à 0,91 à 12 mondes**
  et de **0,40 à 0,62 à 8** (0,67 contre 0,15, puis contre 0,05) : à refaire dans les formes.
- **Devis (estimé, par règle de trois sur le devis de la conception, lui-même estimé)** : environ 7 USD par monde et
  par génération en central (41 USD pour 6), environ 68 au pire. À 12 mondes × 2 générations × 2 bras : **≈ 330 USD en
  central, ≈ 3 300 USD au pire sous les bornes.** Dix fois l'étage 1 : à ne payer que sur preuve.
- **Variante presque gratuite** : ajouter le seul bras « sans héritage, à budget égal » à la course à plusieurs
  générations **avant le scellement de son texte** ; avec ses 2 mondes, elle ne peut pas atteindre le seuil (deux paires ne suffisent pas au test du signe), mais
  elle éprouve la plomberie du bras.

## 5. Voisin de méthode pour la fabrication des organismes par adaptateurs — une phrase

Oui : la « distillation de harnais » du billet (jouer sous une consigne, la retirer des trajectoires, affiner dessus)
est la distillation de contexte que le programme nomme déjà pour sa famille d'organismes par adaptateurs, et se cite
comme voisin de méthode avec Snell, Klein et Zhong, « Learning by Distilling Context » (arXiv 2209.15189), et ses
suites de 2026 que le billet cite (arXiv 2602.12275 ; arXiv 2609.24974) — citation seulement.

## 6. Voisins établis

Sur notice arXiv seulement (titre, auteurs, date, résumé : `sources/arxiv-voisins-memoire-v1.xml`, `5ff80294…`) ;
**aucun PDF lu, aucun chiffre repris** : Continual Learning Bench (arXiv 2606.05661, le banc du billet) ; ALMA (arXiv
2602.07755) et MemEvolve (arXiv 2512.18746), recherche de conceptions de mémoire ; Meta-Harness (arXiv 2603.28052) ;
Automated Design of Agentic Systems (arXiv 2408.08435) ; Darwin Gödel Machine (arXiv 2505.22954) ; **Huxley-Gödel
Machine (arXiv 2510.21614)**, crédit par les descendants ; Co-Harness (arXiv 2607.22688) et WHALE (arXiv 2609.00196),
alternance entre recherche du harnais et affinage ; Harness-Zero (arXiv 2609.24974) ; « Learning by Distilling
Context » (arXiv 2209.15189) ; « Prompt Baking » (arXiv 2409.13697) ; « On-Policy Context Distillation » (arXiv
2602.12275). Pour le sur-ajustement adaptatif, les deux références que N-049 porte déjà (« à vérifier » dans son texte).

## 7. Nœuds pour Lazar

1. **Collision à instruire sur « l'héritage d'une génération est récompensé »** (N-045 v2, énoncé 5). Le billet ne
   l'occupe pas, mais « Huxley-Gödel Machine » pourrait l'occuper en partie (crédit d'un agent par ses descendants),
   et Co-Harness et WHALE touchent les instruments à effet différé. Options : (a) lecture sur PDF de ces trois
   articles par un lecteur neuf avant tout texte qui présente l'énoncé 5 comme nôtre (gratuit) ; (b) ne rien faire
   tant que l'énoncé reste une règle de dessin et non une revendication. Recommandation : **(a)**, confiance ≈ 80 % —
   N-045 demande déjà une recherche bibliographique « avant de revendiquer ».
2. **« La mémoire transmise est apprise » est occupée en partie** (le billet, ALMA, MemEvolve). Ce n'est pas
   aujourd'hui une revendication d'un de nos papiers ; à ne pas le devenir sans lecture sur PDF.
3. **Essai de l'héritage, étage 1** : feu vert sur devis (central 20 à 60 USD, pire 288 USD), après texte contre-lu
   et scellé. Recommandation : **oui**, après la course à plusieurs générations ou à sa place si tu veux d'abord
   savoir si l'archive cause quelque chose ; confiance ≈ 65 %. L'étage 2 (≈ 330 USD en central) seulement sur preuve.
4. **Ajouter un bras « sans héritage, à budget égal » au texte de la course à plusieurs générations** avant son
   scellement : c'est un changement de son dessin et de son devis, donc ta décision. Recommandation : **non** à deux
   mondes (il ne trancherait rien et consommerait les marges du devis, annoncées minces) ; la question se traite mieux
   par l'étage 1.
5. **Citation de méthode** (section 5) : à ajouter aux voisins de la fabrication des organismes par adaptateurs ;
   aucun énoncé ne change.

## 8. Limites

- Une page web sans date, sans article, sans code : rien de ce qu'elle chiffre n'est vérifiable ni opposable.
- Figures 4 à 6 lues à l'œil ; l'ordre de grandeur du biais de sélection est un raisonnement, pas une mesure.
- Voisins lus sur notice arXiv, jamais sur PDF. Les verdicts « occupé en partie » sont des verdicts de lecteur rapide ;
  « libre » veut dire « libre au regard de ce billet ».
- Le contenu du dossier du dépôt public de l'équipe est connu par un outil qui résume, pas par lecture brute.
- Je n'ai pas relu les coûts mesurés par appel du pilote du monde riche : les devis de la section 4 sont des règles de
  trois sur des devis eux-mêmes estimés.
- Je n'ai pas lu le code du générateur ni celui de la génération 1 simulée : l'étage 1 suppose qu'ils servent tels
  quels ; à vérifier par le rédacteur du texte.
- Je n'ai ouvert aucun résultat des travaux sous embargo.
