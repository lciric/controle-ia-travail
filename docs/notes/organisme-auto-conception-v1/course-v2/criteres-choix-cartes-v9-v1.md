# Critères de choix des cartes à éprouver — course d'auto-conception v9 de l'organisme d'idéation — v1

- Écrit par un rédacteur neuf (Claude Fable 5.2), sur mandat de la mère (règle « Qui conçoit », R-3735), le 2026-11-19. Pièce de travail (classe C). Processeur seul, aucune dépense.
- **Écrit et scellé avant l'ouverture des cartes.** Lus à ce stade, et rien d'autre : la lecture descriptive `lecture-course-v9-v1.md` (`0306adf7…`), le préenregistrement v2 de la course (`0d51e0b3…`, lu au commit `8029ae7f`), les décisions N-058, N-064, N-065, N-067, N-071 (resserrement du juge au nul), N-072 (matière première des mentors), N-073 et ses compléments 1 à 3. La lecture descriptive résume les cartes par regroupements : j'en connais donc les thèmes et des identifiants, pas le contenu.
- Ce texte ne choisit rien. Il fixe la règle que j'appliquerai à la lettre. Si un critère s'avère inapplicable, je ne le change pas : j'écris l'écart dans la proposition.

## 0. Ce qui n'est pas un critère

- Le verdict des deux juges, « notable » ou non, et le classement de l'orchestrateur (N-058 ; préenregistrement, « Plan d'analyse »). Je n'ouvre pas le classement. Un item marqué faux par un juge ne sert qu'à relire la carte de plus près sur ce point et à écrire une réserve.
- L'espèce du proposeur. Je lis les cartes sans leur champ `meta` ; l'espèce ne départage rien.
- Le nombre de cartes d'un regroupement, ou la rencontre de plusieurs espèces sur une même idée : ce n'est pas un signal de valeur (lecture descriptive, § 4 et § 5).
- Le mot « inédit » d'un proposeur, et tout chiffre ou travail publié cité par une carte (règles R7 et R8).

## 1. Exclusions, appliquées d'abord, sur le texte de la carte

Une carte est écartée, sans note, si ma lecture y trouve l'un de ces cas.

- **X1 — un modèle décide.** Un modèle (note, score de logits, juge, aiguilleur, vote de modèles) trie, promeut, élimine, alloue le budget ou choisit ce qui va à l'épreuve, dans le mécanisme ou dans le critère de l'épreuve. Un modèle qui propose, traduit ou écrit, sous un critère calculé par programme, n'est pas un modèle qui décide.
- **X2 — porte « le séquentiel doit battre le meilleur de N tirages à budget égal »** prise comme mécanisme ou comme critère décisif de la carte (N-073, § 2 : protocole occupé, pratique publiée). Si ce critère est un témoin parmi d'autres et que l'épreuve se juge sans lui, la carte reste, avec la réserve « critère à réécrire, pratique à citer ».
- **X3 — pas d'oracle exécutable.** L'épreuve se juge par la note d'un juge, par une lecture humaine, ou sur un monde sans vérité plantée.
- **X4 — sélection d'agents sur le verdict d'un juge** : la carte choisit, pondère ou écarte un proposeur ou un juge d'après ce qu'un juge promeut (N-053 point 5, N-058).
- **X5 — principe occupé présenté comme le mécanisme même, sans forme distincte** : la carte n'est rien d'autre qu'une phrase des listes « Ne plus écrire » ou « Ne pas écrire » (N-073, § 1 ; compléments 2 et 3), ou qu'une composante du juge déjà cédée (N-067, § 4 : statistique calculée hors des agents, sceau par empreinte, multiplicité par e-valeurs, séparation de qui propose et de qui juge).
- **X6 — les deux cartes retenues par l'aiguilleur** (`f9a7c8311d714`, `f640bf1e40418`) : hors du choix. Je ne les ouvre pas ; aucune raison de les lire ne peut exister avant la lecture, et les lire est un choix de la mère (lecture descriptive, § 6, point 6).

## 2. Cinq critères notés, chacun de 0 à 2

**C1 — Ce que la carte permet d'éprouver sur monde planté.**
- 2 : la carte dit, ou permet d'écrire sans rien inventer, (i) un oracle qui est un programme comparant les sorties à la vérité plantée (structures retrouvées, témoins vrais promus, témoins faux rejetés, ou une quantité que le monde planté fixe par construction) ; (ii) un bras témoin sans le mécanisme, à coût apparié, et une base bon marché ; (iii) une règle de lecture chiffrable d'avance, où un « oui » et un « non » sont tous deux définis.
- 1 : l'oracle est exécutable, mais le témoin ou l'appariement du coût manque et peut être ajouté sans toucher au mécanisme.
- 0 : cas X3 (exclusion).

**C2 — Lien avec une question ouverte du programme.** Les cinq questions, fixées ici :
- (a) *l'héritage* : un registre des tentatives hérité d'une course puis tenu, comparé au même registre né vide et à aucun, cause-t-il les découvertes (N-073, § 1, complément 3) ;
- (b) *le juge au nul formé des lois connues* : le nul d'archive écarte-t-il ce qu'un nul classique laisse passer, et que vaut la réunion revendicable (N-067, § 4 et § 5 ; N-071) ;
- (c) *la sélection* : ce que la génération suivante lit de la sélection, note du juge montrée ou non, règle de survie des fiches ;
- (d) *la multiplicité* entre cartes et entre essais ;
- (e) *les juges croisés* : agrégation fixe, erreurs corrélées, tenue des juges — le second terrain du papier C (N-065, rôle 1).
- 2 : l'épreuve répond directement à l'une de ces questions. 1 : elle l'éclaire de biais (un instrument dont la réponse a besoin). 0 : aucun lien.

**C3 — Coût d'une épreuve**, estimé d'après les coûts réels de la v9 (proposeur : de 0,38 à 2,25 USD par appel selon l'espèce ; juge : de 0,03 à 0,07 USD par carte ; aiguilleur : 0,05 USD par carte ; course entière, une génération, cinq espèces : 72,50 USD), majorés de moitié, puisque le réel a dépassé le devis de 1,8 fois.
- 2 : processeur seul, ou rejeu sur des sorties déjà scellées, ou 10 USD d'appels au plus.
- 1 : 75 USD au plus (l'ordre de la course v9).
- 0 : au-delà, ou plusieurs générations complètes à plusieurs bras.

**C4 — Risque de collision avec un travail publié** (N-064, N-067, N-071, N-073 et compléments).
- 2 : le résultat se rapporte comme une mesure de l'organisme, sans avoir à présenter comme sien un principe dit occupé ; les voisins à citer sont déjà lus sur source au dépôt.
- 1 : le principe est occupé ou un voisin nommé n'est pas lu, mais une forme décrite reste (citations obligatoires à porter), ou la carte touche une revendication resserrée (juge au nul, héritage) et doit suivre sa lettre.
- 0 : cas X5 (exclusion).
Une collision n'interdit pas de mesurer : elle interdit de dire. Elle baisse la note, elle n'exclut qu'au cas X5.

**C5 — Valeur des deux issues** (règles R3 et R4).
- 2 : un « oui » et un « non » changeraient chacun une décision de conception nommée de l'organisme (garder, retirer ou régler un module).
- 1 : une seule des deux issues apprend quelque chose.
- 0 : aucune.

## 3. Seuil, fusion, nombre visé

- **Plancher** : C1 ≥ 1, C2 ≥ 1, et total ≥ 7 sur 10.
- **Fusion** : les cartes qu'une même épreuve juge (même oracle, mêmes bras, même monde planté) font une seule ligne. La ligne porte la carte la mieux notée ; les autres y sont des variantes ou des bras. La ligne prend la note de sa porteuse.
- **Nombre visé : cinq lignes**, six au plus, trois au moins. Si moins de trois lignes passent le plancher, j'en propose moins et je l'écris comme un écart.
- **Couverture** : deux lignes au plus par question de C2, tant qu'une ligne au plancher existe pour une question non couverte.

## 4. Règle de départage, dans cet ordre

1. total le plus haut ;
2. C1 le plus haut ;
3. C3 le plus haut (l'épreuve la moins chère) ;
4. la question de C2 qu'aucune ligne mieux classée ne couvre ;
5. C5 le plus haut ;
6. le moins de voisins non lus sur source ;
7. en dernier recours, l'ordre alphabétique de l'identifiant de la carte, règle sans contenu.

Jamais par le verdict d'un juge, le classement de l'orchestrateur ou l'espèce.

## 5. Ce que la proposition devra dire de chaque ligne

Les cinq notes et leur raison en une phrase ; les réserves repérées par les juges, dites comme telles ; les travaux voisins, tous marqués « non vérifié » sauf ceux lus sur source et nommés par les décisions ; la lettre de N-073 quand la ligne touche l'héritage, la banque sœur ou la porte du meilleur de N. Les cartes écartées de justesse sont celles qui manquent le plancher d'un point, ou qui le passent sans entrer dans le nombre visé.
