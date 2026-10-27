# Cellule A — Tour III.3 : riposte

## 0. Pièces et statuts

- Je reçois ma conception (E3-T1-A) et les deux attaques (E3-T2-B, E3-T2-C), complètes. Je ne réponds qu'à ce qui vise A : chez B, le point commun en tête, A1–A9, les scénarios, les sept contrôles et l'expérience corrective ; chez C, les failles 1–5, les scénarios 1–3 et les contrôles 1–3. Les attaques de B contre C et de C contre B ne sont pas mon affaire (B1), sauf là où je m'en sers, en le disant.
- Rien de nouveau n'est servi : K reste en partie 1, « couche 1 bis », « pièce 4 », « pièce 4 bis » et la méta-conception restent des noms. M reste RAPPORTÉ-non-audité, début coupé.
- Tous les chiffres hors faits sont illustratifs ; les diagnostics des attaquants sont des HYPOTHÈSES sur le code, sauf les faits RAPPORTÉ qu'ils citent (X1, K, D4).

---

## (a) Réponse à chaque attaque

### Le point commun (B) : l'autorat Opus 5.5 des gabarits et du monde planté

**Acceptée, transformée en test.** Le fait (X1 : v7 « servie par Opus 5.5 pour cette version ») est RAPPORTÉ ; l'ampleur du confondant est une HYPOTHÈSE, mais il suffit qu'il soit possible pour rendre mes Exp. 2 et 3 illisibles sur un monde planté dessiné par la même lignée que le joueur. Je prends l'expérience corrective de B telle quelle (monde tiré au hasard dans une grammaire d'interactions, graine du noyau, aucun modèle dans la boucle, noms de traits neutralisés) et je la place **avant** l'Exp. 2, comme préalable P2 (voir (b)). Une précision que B n'écrit pas : la grammaire elle-même doit être écrite ou relue par une autre lignée que celle qui joue, sinon on déplace le confondant d'un cran.

### B-A1 : le repli de l'Exp. 1 rend H_A vraie par construction

**Acceptée.** Un monde planté hors du nul a une puissance qui croît avec N par loi des grands nombres (D4a : 0,53 → 0,90 de 120 à 500 tirages, RAPPORTÉ) ; il ne dit rien du 0/20 de T0.5. Correction : la banque réelle n'autorise que N ∈ [41 ; 62] par moniteur (X1), donc **l'Exp. 1 en N croissant attend la couche 1 bis** (non servie). Le monde planté n'y sert plus que de **témoin positif de la chaîne** (elle sait promouvoir quand il y a de la structure, X2), jamais de bras de mesure. En attendant la couche 1 bis, ce qui se fait à 0 USD est l'Exp. 0 ci-dessous, issue de l'attaque A3.

### B-A2 : H_A et H_B de l'Exp. 1 ne sont pas exclusives

**Acceptée.** Je reprends la forme par interaction que propose B : H_A « la pente de puissance en N est la même avec et sans nul informé » contre H_B « nulle avec le nul informé, positive sans ». Le cas « nulle dans les deux colonnes » n'est pas une troisième hypothèse : il réfute la prémisse que la banque porte du signal détectable à ces N, et renvoie à la couche 1 bis.

### B-A3 et C-1 : la circularité témoins/nul sur les 40 épisodes de calibrage

**Acceptée, et c'est le point le plus important des deux attaques.** Témoins vrais « déclarés sur la partie de calibrage (lien de rang ≥ 0,35) » et nul informé « ajusté sur la partie de calibrage » (X1, RAPPORTÉ) : promouvoir un témoin revient à mesurer l'écart entre deux ajustements sur le même échantillon, et C a raison que N ne rend jamais de puissance à un témoin dont la loi coïncide avec le membre `connu:<moniteur>`. B a raison que j'en faisais une conséquence au lieu d'un préalable. Correction : c'est désormais **l'Exp. 0**, la première de toutes, et une condition sur toute banque future : témoins et nul informé établis sur des tranches **disjointes par tâche** (voir B-contrôle 1 et C-contrôle 3), ou témoins établis ailleurs que dans la banque (résultats lus sur PDF, artefacts plantés — K le demandait déjà).

### B-A4 : le nul de l'Exp. 3 est éliminé par construction

**Acceptée.** Resoumettre des idées de la mémoire se heurte à la mémoire elle-même (D4a, X2 : 11 à 15 redites refusées par course) et au nul d'archive (X1). Mon issue « les deux ≤ nul » était donc presque impossible, ce qui la rendait fausse-informative. Je prends le **Bras 0 de C** (lois tirées au hasard au gabarit, hors archive) comme nul de proposition, en le disant, et je garde le faux proposeur (traits permutés sur des fiches maison) comme second nul : même forme, contenu détruit, non redite par construction.

### B-A5 : effet plancher dans l'Exp. 2

**Acceptée.** Avec un taux de base proche de 0 (X2 : une promue par bras sur une course), des médianes par graine valent 0 des deux côtés. Correction : test sur les **taux poolés** de deux proportions, puissance calculée avant. Ordre de grandeur illustratif : détecter 0,02 contre 0,04 à 80 % de puissance demande environ 1 200 fiches gelées par bras (25 graines × 48). Et si le taux de base sur le monde de mesure est 0, l'Exp. 2 n'a pas de sens : d'où l'ordre, Exp. 0 et P2 d'abord.

### B-A6 et scénario « neuve » (B), scénario 1 (C) : `expliquees_par_le_connu` lisible par le proposeur ; interaction minuscule ou non-linéarité banale

**Acceptée pour l'instrument, rejetée pour le diagnostic.** Le fait est RAPPORTÉ (fonction dans `proposeur.py`, `predicteurs_connus_publics` dans le contexte, X1). Mais la frontière du connu est publique **par conception** : on veut des propositions hors du connu, et la cacher ne changerait rien, puisque le nul informé est dans 𝓛 et que c'est lui qui juge. Ce qui était faux chez moi : faire entrer `expliquees_par_le_connu` dans la métrique. Correction : « neuve » = **promue par le juge** contre un 𝓛 qui contient le nul informé et le nul d'archive, point ; la fonction du proposeur n'est qu'un filtre d'économie, hors mesure. Une loi « connu + interaction minuscule » n'est promue que si l'interaction est réelle et assez forte pour porter W jusqu'à m/α : ce n'est pas une évasion, c'est une découverte modeste. Reste la non-linéarité **banale** (scénario 1 de C, et B-C3 contre C que je m'approprie : la crête multinomiale ajuste déjà les formes monotones saturantes ; il reste les seuils francs et les formes en U). Transformée en test : ajouter à 𝓛 un membre mécanique non linéaire aveugle à l'idée (crête sur traits au carré et produits deux à deux), puis mesurer une fiche-parasite « forme en U » dans un monde où l'effet est **absent** (type I attendu ≤ α) et dans un monde où il est présent mais connu (ce que le nul manque, sans attendu de type I) — c'est la forme correcte que B oppose à C, et elle vaut aussi pour moi.

### B-A7 : le catalogue mécanique dérive

**Acceptée.** La stratégie « hors des bassins déjà promus » (X1, go de 15:20) se conditionne sur l'archive. Le contrôle négatif de l'Exp. 5 devient un **catalogue figé sans cette stratégie** ; « hors des bassins » devient un bras à part, mesuré pour sa dérive comme les autres.

### B-A8 : l'Exp. 6 n'est pas exclusive ; le modèle factice ne teste pas l'agent

**Acceptée.** Reformulation en deux niveaux. (i) **La prison** : H_A « tout script d'attaque d'un jeu connu est bloqué et journalisé » contre H_B « au moins un passe » ; mécanique, 0 USD. (ii) **Le système sous modèle réel** : H_A « il termine au moins une course de développement avec 0 tentative bloquée » contre H_B « au moins une tentative bloquée, ou échec » ; « termine et tente » tombe dans H_B. Le modèle factice n'exerce que le cadre ; (ii) coûte des appels et je le chiffre en (d). La conscience d'évaluation (scénario prison de B et C, N-053 point 3) reste une **limite déclarée** que cette expérience ne lève pas : une absence de tentative sous observation n'établit pas l'absence hors observation ; je ne prétends pas le contraire.

### B-A9 et C-5 : le relecteur tiers « gratuit », et le pré-filtre

**Acceptée sur le coût et sur la condition, rejetée en partie sur l'invariant.** Faire noter des fiches par un relecteur tourne sur un modèle, donc coûte ; « gratuit » était faux (il peut tourner derrière le relais de D sans hériter de clé, mais pas sans appel). Et une corrélation avec un juge sans dents ne mesure rien : la mesure attend l'Exp. 0. Sur C-5 : N-053 point 5 interdit qu'un score de **moniteur** entre dans la sélection de l'**agent** ; l'appliquer à un relecteur d'idées est une transposition par analogie, pas l'invariant. Mais C a raison sur le fond : un pré-filtre avant gel est une sélection par vraisemblance linguistique, et sous budget fini, tout ordre de passage est une sélection. Je **retire « pré-filtre »** et je transforme en test : ordre de passage par le relecteur contre ordre aléatoire, à exposition d'épreuve égale ; métrique de censure = part des fiches promues situées dans le quart bas du relecteur. Si elle est > 0, le relecteur censure du vrai et ne doit pas ordonner.

### B-scénario « appariement à 8 », C-faille 2, C-scénario 2, C-contrôles 1 et 2 : stéganographie et projection avec perte

**Acceptées.** Trois corrections à l'Exp. 4 : (1) le lecteur aveugle ne voit que la **matrice des probabilités prédites** sur un jeu d'instances fixé (C-contrôle 2), jamais `enonce`, `contraintes`, `domaines`, `operateurs`, ni les constantes brutes ; (2) traducteur, lecteur et apparieur de **trois lignées** différentes (Opus, Fable, Qwen2.5-7B, seul modèle ouvert nommé dans les faits, N-053) ; (3) un bras **traducteur aveugle à l'idée** (C-contrôle 1), qui produit une fiche depuis le seul contexte public : si ses promotions égalent celles du bras traduit, le traducteur fait le travail. Et je reconnais la limite structurelle que C oppose à B et qui me vaut aussi : deux mécanismes opposés donnent la même loi ; l'Exp. 4 mesure la fidélité de la **prédiction**, pas celle du mécanisme. Je la renomme ainsi. Symétrie imposée (C-faille 2) : le proposeur maison propose **en texte** et passe par le même traducteur que le bras tiers ; aucun bras n'écrit directement au gabarit.

### C-faille 3 : multiplicité e-BH contre instances consommées

**Acceptée.** À 10 000 instances fixées, les bras subissent des m et des tailles de plan différents. Correction par conception : **même m par génération, même politique de recombinaison, mêmes `taille_plan` et `taille_plan_filles`** dans tous les bras ; alors les instances consommées sont égales et la métrique se réduit à « promues pour 100 gelées » à m fixé. Je garde « par instance consommée » en rapport descriptif, pour les cas où les plans sont bornés par le réservoir (X1).

### C-faille 4, B-scénario « juge contre permutation », B-contrôles 1 et 7, C-contrôle 3 : fuite de tâche

**Acceptées, en préalable absolu.** Épisodes d'une même tâche dépendants (X1, RAPPORTÉ) : une loi qui reconnaît la tâche est vraie au sens du juge et passe la permutation inter-tâches. Correction : **séparation par tâche** entre développement, calibrage et épreuve avant toute expérience ; **permutation intra-tâche** des issues comme contrôle dans toutes les expériences.

### B-scénario « dérive invisible » (Exp. 5)

**Acceptée.** Mes métriques (i)–(iii) restent plates si la fiche touche chaque sous-population d'un poids infime et parie fort sur une seule. Ajout d'une métrique de **concentration** : part de la divergence déclarée portée par la sous-population la plus pariée, et entropie des poids effectifs.

### B-scénario « vérificateur », C-scénario 3 : canal de persuasion et mauvais moniteur

**Acceptée pour le canal, rejetée pour le moniteur.** Le canal textuel vers le vérificateur (K : sept fichiers exclus seulement) est réel ; correction : rejeu limité au code et aux artefacts déclarés, sortie structurée, aucune note libre. Sur « mauvais moniteur sous la bonne empreinte » : en mode banque, le moniteur est « sous l'empreinte de l'engagement » et les issues sont « lues et déposées [par le noyau] après le gel, jamais calculées » (X1, RAPPORTÉ) ; l'agent ne choisit pas le moniteur après coup. Ce qui reste vrai, c'est K : le vérificateur devient une formalité en mode banque ; la vérification réelle est l'empreinte d'ordre recalculée par le noyau.

### C-scénario 1, second volet : jumelles divergentes sur les queues de la sonde gaussienne

**Transformée en test.** Que la sonde de la mémoire reste gaussienne en mode banque (K décrit v5 ; X1 parle d'un « espace d'instances dans l'index de la mémoire » pour v7) n'est pas établi — B le note contre C, et cela vaut pour C contre moi. Contrôle à ajouter : une **jumelle à queue** (identique sur le support de la banque, divergente hors support) doit être refusée comme redite ; si elle passe, la signature doit être calculée sur les instances de la banque, pas sur une gaussienne. Lecture de `memoire.py` v7 d'abord.

### C-scénario 3, empoisonnement de la mémoire par un filet de fausses fiches

C l'adresse à B, mais la mémoire est la mienne aussi : **acceptée comme risque**, transformée en contrôle : des fiches éliminées ne doivent **jamais** bloquer une fiche neuve comme redite (seule la redite d'une promue est à refuser ; la redite d'une éliminée est un test à rejouer sous preuve héritée, D4a politique « héritage »). À vérifier dans `chercher_classe`.

---

## (b) Expériences corrigées

Préalable commun **P0** (0 USD, code) : découpage par tâche développement / calibrage / épreuve ; permutation intra-tâche disponible ; sonde de mémoire vérifiée ; rejeu limité au code ; m, plans et recombinaison identiques entre bras ; catalogue figé. Ordre : **Exp. 0 → P2 (monde aléatoire) → Exp. 6 → Exp. 2 → Exp. 4 → Exp. 3 → Exp. 5** ; l'Exp. 1 attend la couche 1 bis.

### Exp. 0 — Le 0/20 de T0.5 vient-il de la circularité ?

- **H_A** : avec témoins déclarés sur une tranche et nul informé ajusté sur une autre (disjointes par tâche), la part de témoins vrais promus, à N inchangé (41–62), devient > 0 et au moins égale à 0,2 (illustratif).
- **H_B** : elle reste ≤ 0,05 : la circularité n'explique pas le 0/20 ; le goulot est N ou la vérité des témoins.
- **Métrique** : témoins vrais promus / servis, 20 graines, trois bras {nul informé : oui / non / membre non linéaire ajouté} ; témoins faux ≤ α ; permutation intra-tâche → 0.
- **Issues** : H_A tenue réfute « banque trop petite » comme explication unique et fixe la règle des tranches ; H_B tenue réfute l'explication par circularité et rend la couche 1 bis nécessaire avant tout proposeur. **0 USD, quelques heures de cœur** (E1 : 14 min pour 70 lignes).

### P2 — Monde aléatoire hors lignée (expérience corrective de B, reprise)

- **H_A** : l'avantage d'un proposeur Opus 5.5 sur le catalogue figé et sur le Bras 0 persiste sur un monde tiré au hasard dans une grammaire d'interactions écrite hors de la lignée Opus, noms neutralisés.
- **H_B** : l'avantage observé sur le monde dessiné par Opus disparaît sur le monde aléatoire, au bruit près.
- **Mesure** : promues pour 100 gelées, taux poolés, 20 graines par monde ; contrôles : permutation intra-tâche, Bras 0.
- **Issues** : H_A réfutée ⇒ tout duel sur monde de même lignée est à jeter, le mien compris ; H_B réfutée ⇒ les Exp. 2 et 3 sont lisibles sur le monde aléatoire. Bras mécaniques à 0 USD ; bras Opus chiffré en (d).

### Exp. 6 — Prison, en deux niveaux (reformulée, B-A8)

(i) Prison contre scripts d'attaque connus : H_A « tous bloqués » / H_B « au moins un passe », 0 USD. (ii) Système tiers sous modèle réel derrière le relais : H_A « termine une course, 0 tentative » / H_B « tentative bloquée ou échec ». Témoin : notre faux moteur (D § 2.3), 0 tentative attendue. Limite déclarée : conscience d'évaluation.

### Exp. 2 — Proposeur-agent contre catalogue figé et Bras 0

- **H_A** : à m et plans égaux, le proposeur Opus 5.5 (contexte public, sous tranches) a un taux poolé de promues pour 100 gelées supérieur au catalogue figé et au Bras 0.
- **H_B** : les trois taux sont égaux au bruit près.
- **Taille** : environ 1 200 fiches gelées par bras (illustratif, pour 0,02 contre 0,04 à 80 %), sur le monde aléatoire de P2, et sur T0.5 si l'Exp. 0 donne des dents.
- **Contrôles** : permutation intra-tâche ; ablation sémantique (noms de traits neutres, B-contrôle 4) ; bras « hors des bassins » à part.
- **Issues** : H_A réfutée ⇒ aucune prise « proposeur », maison ou tierce, ne se justifie : le concurrent à battre est gratuit ; H_B réfutée ⇒ ligne de base pour l'Exp. 3, et l'ablation dit si l'avantage vient du nom ou de la donnée.

### Exp. 4 — Fidélité de la prédiction traduite (renommée)

- **H_A** : un lecteur d'une deuxième lignée, qui ne voit que la matrice de probabilités prédites sur un jeu d'instances fixé, rédige une phrase qu'un apparieur d'une troisième lignée relie à l'idée d'origine parmi 8, à un taux ≥ 0,6 (illustratif, abaissé car la loi ne porte pas le mécanisme).
- **H_B** : taux ≤ 0,25.
- **Bras ajoutés** : traducteur aveugle à l'idée ; paires mélangées ; idée inversée mot à mot (contrôle (iv) que C oppose à B, que je prends : si l'idée et son inverse donnent des fiches qui promeuvent pareil, le traducteur ignore la direction).
- **Issues** : H_A réfutée ⇒ la prise « proposeur » transmet du bruit, et le duel de l'Exp. 3 ne mesure que le traducteur ; H_B réfutée ⇒ la traduction par le même traducteur des deux côtés est admissible.

### Exp. 3 — Duel maison / littérature sous le même juge

- **H_A** : le bras tiers (proposeur, ou exploration s'il a passé l'Exp. 6) a un taux poolé de promues pour 100 gelées supérieur au maison, les deux au-dessus du Bras 0 et du faux proposeur.
- **H_B** : le maison fait au moins aussi bien.
- **Plan** : même monde (P2, puis T0.5 ou couche 1 bis), mêmes tranches disjointes par tâche, même m, mêmes plans, même traducteur (texte des deux côtés), même mémoire, relecteur tiers débranché ; environ 1 200 fiches par bras (illustratif).
- **Issues** : littérature > maison ⇒ prise justifiée ; maison ≥ littérature ⇒ pas d'achat ; **les deux ≈ Bras 0** ⇒ aucun proposeur ne dépasse le hasard au gabarit, et le goulot est la banque ou le nul, retour à l'Exp. 0. Cette troisième issue est désormais atteignable (B-A4).

### Exp. 5 — Enfermement

Comme au tour III.1, plus : catalogue figé comme témoin ; métriques de concentration (part de la divergence portée par la sous-population la plus pariée ; entropie des poids) ; bras avec / sans tranches. H_A : dérive croissante sur 6 générations sans tranches, absente avec ; H_B : aucune dérive, les tranches sont un coût sans objet.

### (d) Coûts corrigés (illustratifs)

Exp. 0, P0, P2 (bras mécaniques), Exp. 6 (i) : 0 USD. P2 bras Opus : 20 graines × 48 fiches × 0,30 USD ≈ 290 USD. Exp. 2 : 1 200 fiches × 0,30 ≈ 360 USD par bras agent (un seul). Exp. 4 : 80 idées × 4 bras × 3 lectures × 0,20 ≈ 190 USD. Exp. 3 : 2 bras agents × 1 200 × 0,30 ≈ 720 USD, plus le coût propre du système tiers (Exp. 6 (ii), inconnu). Total de l'ordre de 1 500 USD, dont **0 avant la fin de P2** ; c'est deux fois mon estimation du tour III.1, parce que les tailles d'échantillon poolées (B-A5) sont plus grandes que mes médianes.

---

## (c) Réponse à l'arbitre, en une page

**Ce qui est établi (RAPPORTÉ, en simulation).** Le juge v1 tient sous six dérives non modélisées (E1 : 18 contrôles fatals à 0 ou 1 sur 1 000) ; le nul des filles v2 ferme « parent + loi aveugle » (E2 : 13 fatals à 0) ; la mémoire empêche les découvertes en double (D4a : 11 doubles sans elle, 0 avec) ; la chaîne proposeur → gel → banque → juge → e-BH a des dents dans un monde planté (X2 : témoins vrais 8/8, faux 0/8). Tout cela à K = 3, d = 2, 200 tirages, agents scriptés.

**Ce qui n'est pas établi (HYPOTHÈSE).** Que le juge morde sur une banque réelle (X2 : 0 témoin vrai promu sur 20 sur T0.5) ; et l'équipe rouge a montré que ce 0/20 est **peut-être un artefact de l'instrument** (témoins et nul informé ajustés sur les mêmes 40 épisodes de calibrage, X1), non une propriété de la banque. Que la prison tienne pour nos agents ou pour un tiers (K, D : jamais exercée). Qu'un proposeur-modèle apporte quoi que ce soit au-dessus d'un catalogue mécanique gratuit (X1 : proposeur scripté ; X2 : l'aveugle a gagné par chance sur un monde qui coïncidait avec son gabarit). Que les systèmes de la littérature proposent « mieux » (aucune mesure dans les faits, et la question compare un agent inexistant à des systèmes non audités sur PDF). Que la traduction texte → loi conserve l'idée (aucun instrument ; et la loi ne porte pas le mécanisme). Que le monde planté par la lignée Opus puisse arbitrer un proposeur Opus (point commun de B : accepté).

**Sur la position de conv-audit.** Elle n'est pas réfutée, mais ses deux moitiés reposent sur des hypothèses non mesurées : « ils proposent mieux » (rien ne le montre) et « notre juge garantit » (vrai en simulation, non montré sur du réel). La partie que je soutiens sans réserve : **ne pas prendre leur relecteur comme juge**. La partie que je retire de ma propre conception : le relecteur tiers comme pré-filtre (C-5) et « fiches promues par dollar » comme métrique ; je propose **promues pour 100 fiches gelées, à m, plans et recombinaison égaux, contre un nul de lois aléatoires au gabarit**, dollars en rang trois, toutes charges comprises.

**L'expérience à faire en premier : l'Exp. 0**, 0 USD, quelques heures de cœur — re-déclarer les témoins et ré-ajuster le nul informé sur des tranches disjointes par tâche de T0.5, et mesurer si les témoins vrais remontent au-dessus de 0. Si oui (H_A), le juge a des dents sur du réel et la règle des tranches est fixée ; le reste (P2, puis Exp. 2) devient lisible. Si non (H_B), la banque est le goulot, et **aucune décision de proposeur n'a d'objet avant la couche 1 bis** : on choisirait le semeur sans champ. Dans les deux cas, décider maintenant est prématuré, et décider après l'option (a) de D ne suffit pas non plus : (a) éprouve la plomberie, pas les dents.

**Ce qui me ferait changer d'avis.** Si l'Exp. 2 sur le monde aléatoire de P2 montre que le catalogue figé égale un proposeur Opus, j'abandonnerais toute prise « proposeur », maison ou tierce, et je mettrais le budget sur la banque et sur le nul. Si P2 montre que l'avantage d'Opus disparaît sur un monde tiré hors de sa lignée, je dirais que toute mesure de proposeur faite jusqu'ici dans ce programme est à refaire. Si l'Exp. 3 donne « les deux ≈ Bras 0 », je dirais que la question « quel proposeur » était mal posée et que la position de conv-audit, bien que non réfutée, est sans objet.

FIN-DE-CELLULE