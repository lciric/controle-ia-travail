# Notes à la mère — batterie de fuite de la banque révisée (mathématiques nouvelles) — v1

- Nature : notes de travail (classe C) qui accompagnent une pièce décisive. Auteur : le concepteur (mandat `mandat-fable-batterie-gelee-v1.md`, `575f8c29…`, adressé à Claude Fable 5.2, effort maximal ; le modèle servi est relevé dans le message de remise, non ici). Le 2026-11-22. Aucun appel de modèle, aucune dépense, processeur seul.
- Pièce rendue : `batterie-fuite-banque-revisee-v1.md`, même dossier. Calculs d'appui : `calculs-d-appui/` (trois scripts, deux modules, six sorties). Empreintes aux compagnons.
- Lu en entier : le mandat ; le rapprochement (`bd5c2af3…`) ; le jugement du juge Fable (`b1380fe3…`) et son erratum 1 ; le jugement du juge Opus (`f82e0c8f…`) ; la note du diagnostic (`da4d80f4…`), son script et sa sortie texte ; le brouillon 4 (`212c6eca…`). Lu aussi : le code figé de la version 6 (classifieur de style, grammaire, évaluateur, vérification d'une instance, sous-banque), les notes au directeur du brouillon 4, la sonde de la règle aveugle.

## Verdict

1. La batterie est écrite : C1 à C4, les trois sondes, les racines neuves, l'épreuve, les branches, la relecture. Elle suit le rapprochement, avec sept écarts que je nomme et motive (§ B).
2. Le plus lourd : **la sonde des nombres apprend par squelette et sur les autres racines**, non dans la racine. Sans cela elle ne voit pas la fuite la plus naturelle d'une banque appariée. Je l'ai éprouvé : sur un artefact où la vérité se lit entièrement dans la grandeur d'un littéral, la sonde prototype du diagnostic rend un excès nul ; la mienne rend 0,90.
3. Un fait te revient d'abord : **Lazar a déjà tranché la lecture du seuil** (§ A). Et trois nœuds (§ D), dont un sur C4, que je crois sérieux.

## A. Un fait postérieur au mandat

Le mandat dit la lecture « rappel ≤ 0,20 à fausses alarmes ≤ 0,10 » provisoire, en attente du mot de Lazar. En lisant `registres/go.md` sur `main` (commit `eca238f5`, du 22 novembre à 19:14Z), j'y trouve GO-2026-11-22-121 : mot de Lazar vers 19:11Z, option (i), « rappel d'au plus 0,20 à fausses alarmes d'au plus 0,10 », batterie « écrite par Fable, contre-lue par un Opus neuf ». Le texte garde la mention demandée et renvoie à cette ligne. À toi de confirmer et de porter l'identifiant au gel. La variante d'une ligne reste au § 5 du texte.

Pour mémoire, sur le cas sain simulé (`sortie-calcul-1-v1.txt`, parties 1 et 2 ; 400 générateurs par case) :
- lecture (i) : une banque saine tient dans 100 % des cas, à 40 comme à 120 racines ;
- lecture (ii), point de fonctionnement à 0,05 et excès d'au plus 0,05 : elle tient aussi dans 100 % des cas. La crainte du rapprochement (« peut-être intenable même sain ») n'est pas confirmée ;
- lecture (iii), excès d'au plus 0 : aucune réussite sur les neuf grandeurs réunies ; une sonde à scores continus n'y tient une grandeur que dans 3 % des cas au plus.

## B. Écarts aux décisions et au rapprochement

| n° | point | base | ce que le texte écrit | pourquoi | retour possible |
|---|---|---|---|---|---|
| 1 | apprentissage de la sonde des nombres | plis par mondes entiers, dans la racine (les deux juges) | un modèle par squelette, appris sur les viviers des autres racines neuves ; toujours par mondes entiers | dans une banque appariée, la vérité ne peut fuir que par les nombres, et le sens de la fuite change avec le gabarit (« E < c » : c grand, vrai ; « E > c » : l'inverse). Une sonde commune à tous les gabarits moyenne ces sens et ne voit rien ; une sonde par squelette n'a pas assez d'énoncés dans une seule racine (une douzaine). Éprouvé : `sortie-calcul-3-v1.txt`, partie A | la sonde prototype reste rapportée en description |
| 2 | règle des ex æquo | bloc jamais franchi (juge Opus, rapprochement) | bloc à cheval compté au prorata, sans tirage | le bloc entier tranche l'indéterminé du côté favorable. Cas d'école : 9 vérités sur 75 et 45 faux sur 75 à un même score haut ; le bloc entier rend un excès de −0,10 (aucune fuite), le prorata 0,40 (`sortie-calcul-1-v1.txt`, partie 0). Sur la banque saine du banc d'épreuve, la sonde de style rend −0,10 au bloc entier et 0 au prorata (`sortie-calcul-2-v1.txt`) | les neuf excès au bloc entier sont rapportés |
| 3 | réglage du seuil de score | « sur les mondes d'apprentissage » (juge Fable) ou « sur les vrais non vus » (juge Opus) ; le rapprochement les dit identiques | sur les 75 vérités notées de la sous-banque | les deux lettres diffèrent. Le seuil transporté des mondes d'apprentissage donne, sur la sous-banque, des fausses alarmes de 0,05 à 0,16 selon la racine (sortie texte du diagnostic, partie c) : le rappel n'est plus pris au même point. Le seuil sur les vérités notées ne lit aucun faux : il n'est pas optimiste | — |
| 4 | sur quoi les sondes apprennent | la sous-banque (juge Opus) | elles apprennent sur le vivier, elles sont notées sur la sous-banque | plus d'énoncés pour apprendre, donc une sonde plus forte ; la mesure reste celle de ce que les bras reçoivent ; mêmes modèles pour C2 et C3 | — |
| 5 | moment du tirage des racines | « au gel » | après le scellement de tout, sonde tenue à l'écart comprise | sinon le vérificateur pourrait régler sa sonde sur les racines neuves | — |
| 6 | relecture sur la banque réelle | « une valeur hors de la plage », pour chaque condition 2 à 4 | trois valeurs relues (l'aire ; le plus grand des neuf excès ; la part de la règle aveugle), plage des deux côtés | onze valeurs relues une à une pourraient fermer à tort la lecture en verdict dans 18 % des cas à 120 racines (11 × 2/121) ; trois valeurs : 5 % au plus | — |
| 7 | jugement des neuf excès | « borne haute du plus grand » (juge Opus) ou « pour chacune » (rapprochement) | chacune des neuf bornes hautes ≤ 0,10 | lettre du rapprochement ; plus simple à contrôler | — |

Aucune des décisions du mandat n'est rediscutée : quatre conditions, 0,75 gardé, deux sondes ajoutées, lecture (i), branches, troisième sonde gardée et retirable en premier, lecture en preuve partout, libellés.

## C. Nombres ajustés ou ajoutés

| nombre | base | texte | pourquoi |
|---|---|---|---|
| racines neuves | au moins 40 | 120, ni plus ni moins | (a) la relecture par la plage ferme à tort la lecture en verdict avec la probabilité 6/(R + 1) : 14,6 % à 40 racines, 5,0 % à 120 (`sortie-calcul-1-v1.txt`, partie 4) ; (b) la condition porte sur la borne haute : une banque d'excès vrai 0,08 échoue dans 84 % des cas à 40 racines, 57 % à 120 (partie 3 : une sonde, trois ensembles) ; (c) un nombre fixe ferme une fourche. Coût : du processeur seulement |
| plancher de racines plantées | — | 40 | reprend le plancher des deux juges, pour le cas où le générateur refuse des racines |
| graine des bornes hautes | « par exemple (10, 3) » | `SeedSequence(20261122, spawn_key=(2000 + j,))`, j de 0 à 10 | le rééchantillonnage porte sur les racines : il ne peut pas vivre dans l'arbre d'une racine ; la graine est écrite avant toute mesure |
| sonde des nombres | « au moins » cinq sortes de traits (juge Opus) | 17 traits par littéral, 2 par couple, 1 par énoncé ; pénalité 1 ; 50 pas ; 10⁻¹⁰ ; 10 décimales ; 20 énoncés au moins par squelette | spécification exacte demandée ; valeurs du prototype du diagnostic quand il en avait (pénalité 1, 50 pas, 10 décimales) |
| énoncés notés 0 faute d'apprentissage | — | plus d'un sur dix dans une sous-banque : sonde non calculable, donc condition non tenue | une banque aux squelettes trop variés rendrait la sonde des nombres aveugle sans qu'on le voie ; garde non exercée par le prototype (le compte y vaut zéro) |
| audit « trop beau » | — | excès moyen sous −0,03 ; aire moyenne sous 0,45 | règle R4 ; à 120 racines, −0,03 est à cinq écarts-types environ d'une sonde sans information (`sortie-calcul-1-v1.txt`, parties 1 et 2) |
| doses de l'artefact « grandeur » | — | 1 et 0,5 doivent tomber ; 0,25 est rapportée | à 0,25 l'excès vrai est d'environ 0,086 : c'est le bord de la tolérance (`sortie-calcul-2-v1.txt`) |

Non ajustés : 0,75 ; 0,10 d'excès ; 0,10 de fausses alarmes ; la moitié pour la règle aveugle ; 2 000 rééchantillonnages ; deux cycles ; le 4 décembre 23:59Z.

## D. Nœuds

### Nœud 1 — C4 peut être tenue à la lettre

- **Décision** : juger C4 sur la seule règle aveugle A, ou y joindre une règle qu'on ne peut pas contourner.
- **Enjeu** : le concepteur de la version 7 — moi — connaît les trois instances de la règle A (3N, 1, N + 1). Une banque dont les contre-exemples seraient à 3N − 1 tiendrait C4 sans fermer la fuite d'instance, et l'affirmation « le système avec outil dépasse la règle aveugle » serait acquise d'avance : un positif fabriqué par le dessin. Sur la version 6, trois instances tirées au hasard réfutent déjà 74 % des faux, et les instances saillantes 86 % (`sortie-calcul-3-v1.txt`, partie B).
- **Options**
  - (a) La lettre : règle A seule. Le texte ajoute une réserve écrite en tête du rapport si l'une des deux règles de description dépasse la moitié. Avantage : c'est la décision prise, rien ne change. Inconvénient : la réserve informe, elle ne décide rien.
  - (b) C4 tient si la règle A **et** la règle de trois instances au hasard tiennent, chacune sous 0,50 en borne haute. Avantage : la règle du hasard ne dépend d'aucun choix de valeurs ; elle mesure la densité des contre-exemples ; on ne la contourne pas. Inconvénient : une règle de plus dans une condition que Lazar a choisie.
  - (c) Les trois règles (A, hasard, instances saillantes). Avantage : la plus stricte. Inconvénient : dans la première famille (N = 4, treize instances pour un énoncé à une variable), les valeurs saillantes couvrent plus de la moitié des instances : la condition y devient presque intenable.
- **Recommandation** : (b), confiance 0,7. Une banque aux contre-exemples rares et bien répartis la tient sans peine : sur la banque saine du banc d'épreuve, la règle A vaut 0,07 et la règle du hasard 0,13.
- **Défaut sous 48 heures** : (a), le texte tel qu'il est.

### Nœud 2 — plancher de portée de la version 7

- **Décision** : exiger ou non un minimum de familles et de squelettes appariés pour que les bras courent sur la version 7.
- **Enjeu** : la lettre des branches accepte une version 7 réduite à une famille, voire à deux squelettes. La comparaison y serait juste, mais étroite.
- **Options**
  - (a) Aucun plancher ; la portée (familles, squelettes, gabarits écartés) est dite en tête du rapport. Avantage : une banque étroite et saine vaut mieux qu'une banque large qui fuit. Inconvénient : l'affirmation peut ne valoir que pour une forme d'énoncé.
  - (b) Plancher : au moins deux familles et six squelettes appariés ; sinon version 6. Avantage : portée garantie. Inconvénient : un nombre de plus, et un échec possible sans fuite.
- **Recommandation** : (a), confiance 0,6. Je viserai les trois familles.
- **Défaut sous 48 heures** : (a).

### Nœud 3 — qui contrôle la sonde tenue à l'écart

- **Décision** : désigner la session qui contrôle la sonde du vérificateur avant son scellement.
- **Enjeu** : le concepteur ne doit pas la voir ; la règle de classe B veut pourtant une contre-lecture par un autre modèle que l'auteur, qui sera un Opus.
- **Options** : (a) un Opus neuf, qui ne contrôle que les quatre interdits vérifiables à la lecture du code (points 5 à 8 du § 2.3) ; (b) un Sonnet 5.5 ; (c) aucune relecture, l'épreuve sur le banc suffit.
- **Recommandation** : (a), confiance 0,6. C'est un écart étroit à la règle de classe B, à inscrire.
- **Défaut sous 48 heures** : (a).

### Deux points sans décision, à connaître

- **La phrase « hors de portée ».** Le juge Fable écrit que, C4 non tenue, « gain d'au moins 0,20 en preuve » est hors de portée. Or ce test compare le système avec outil à la lecture nue, et il peut passer si la lecture nue cite peu d'instances. J'ai donc écrit la lecture que je crois voulue : un écart avec la lecture nue, même établi, n'y est jamais lu comme un gain dû au calcul. Si tu lis autrement, c'est une ligne du § 5 à changer.
- **Une version 7 qui tient C4 mais non C1** retombe sur la version 6, alors qu'elle servirait mieux la lecture en preuve. C'est cohérent : un invariant refusé par le code veut dire un générateur non certifié. Je ne le rediscute pas.

## E. Demande approfondie, en bref

1. **Ce qu'un expert ferait, et qui n'était pas demandé.** Traiter la batterie comme un détecteur à étalonner : mesurer son taux de fausses alertes sur un cas sain et sa sensibilité sur des fuites dosées, avant tout emploi. Se demander où une fuite peut encore passer dans une banque appariée (par les nombres, à squelette égal) et régler la sonde là-dessus. Protéger le critère contre son propre concepteur.
2. **Les données brutes.** Les textes servis, les définitions servies, les scores par énoncé et le profil complet des instances de chaque faux ; non les aires résumées.
3. **Les méthodes.** Paires minimales ; rappel à fausses alarmes fixées sur la courbe complète, ex æquo au prorata ; un modèle par squelette appris hors de la racine ; rééchantillonnage des racines ; banques d'épreuve à vérité connue ; puissance exacte par la loi binomiale.
4. **Ce qui vérifie hors de Lazar et de Claude.** L'évaluateur exact (les strates du banc d'épreuve lui sont confrontées) ; des scripts à graines consignées, rejoués à l'octet ; l'engagement des racines par leurs empreintes avant la mesure ; une sonde écrite par un autre modèle. Et, si Lazar le veut, le statisticien extérieur dont un brouillon de message existe au chantier (contact externe : nœud).

Demande reformulée : écrire un détecteur de fuite dont on connaît, avant de s'en servir, ce qu'il laisse passer et ce qu'il arrête, et que son auteur ne peut pas viser. Le texte y répond ; le § 8 dit où il n'y répond pas.

## F. Ce que j'ai éprouvé, et ce que cela vaut

| calcul | ce qu'il montre | sortie |
|---|---|---|
| 1 | une sonde sans information rend un excès moyen de 0,000 à 0,005 et une borne haute sous 0,06 ; les trois lectures du seuil ; la sensibilité ; la relecture par la plage ; la puissance exacte de la comparaison à la règle aveugle | `sortie-calcul-1-v1.txt` |
| 2 | banc d'épreuve, 120 racines : la banque saine tient tout (bornes hautes des excès sous 0,01 ; règle aveugle 0,07) ; « grandeur » fait tomber C3 par la seule sonde des nombres (0,90 à pleine dose, 0,23 à demi-dose) pendant que C2 reste à 0,5 ; « gabarit » fait tomber C1, C2 et C3 ; « plafond » fait tomber C4 seule | `sortie-calcul-2-v1.txt` |
| 3 | la sonde prototype du diagnostic ne voit pas « grandeur » (excès 0,000) ; sur la version 6, la batterie tombe partout et retrouve le diagnostic : aire 0,966, identique à celle du paquet sur les 41 racines ; règle aveugle 0,846, de 60 à 68 touches, médiane 63 | `sortie-calcul-3-v1.txt` |

- Les strates des 192 énoncés d'une banque d'épreuve ont été confrontées à l'évaluateur exact du paquet, pour quatre banques : aucun désaccord. Ce contrôle n'est pas versé ; il est à refaire par le code du banc.
- Deux passes de chaque calcul rendent les mêmes sorties à l'octet.
- **Ces calculs sont de moi, alors que le code revient à Opus.** Je les ai écrits parce que le mandat le permet et que trois choix du texte en dépendaient (écarts 1 et 2, nombre de racines). Ils importent le paquet figé sans le modifier. Ils ne sont vérifiés par personne : à refaire par le code de la batterie avant toute citation dans un texte scellé.
- Le calcul 2 ne porte que deux sondes : la sonde tenue à l'écart n'existe pas encore.

## G. Ce que je prévois, pour que tu saches où l'on va

| issue | probabilité que je lui donne |
|---|---|
| la version 7 tient C1 et C4 avant le 4 décembre 23:59Z | 0,55 |
| elle tient aussi C2 et C3 (lecture en verdict ouverte) | 0,20 |

La seconde est basse à dessein. Sous C1, la fuite se réfugie dans les nombres, et la sonde des nombres est forte. Dans les deux premières familles, un énoncé dont la vérité tient à un seuil porte des littéraux dont la grandeur suit la strate ; il faudra des énoncés d'un autre genre. La lecture en preuve, elle, ne dépend que de C1 et de C4.

## H. Ce qui reste avant le gel, dans l'ordre

1. Contre-lecture de la batterie par un Opus neuf ; je vérifie ses remarques, ou il vérifie mes corrections.
2. Tes réponses aux trois nœuds, ou les défauts.
3. Gel, avec l'identifiant du mot de Lazar.
4. Mandat à Opus pour le code de la batterie et du banc d'épreuve (classe B). Mes prototypes peuvent servir de point de comparaison ; ils ne sont pas l'instrument.
5. Mandat de la version 7 au concepteur. Je ne l'ai pas commencée.
6. Vérification du code de la version 7 ; sonde tenue à l'écart ; tirage des 120 racines ; mesure unique.

Le calendrier est serré : douze jours pour six étapes dont deux contre-lectures.

## I. Réserves sur mon travail

- Routine de reprise partielle, selon la consigne : empreintes des trois documents de lancement vérifiées, conformes. Ni vérification de l'arbre, ni défauts échus, ni inventaire des machines, ni essais, ni passation : ils reviennent à la mère.
- Je n'ai lu ni le brouillon 5 ni aucun fichier de clé. Les seules banques engendrées viennent des 41 racines d'essai déjà exposées de la version 6 et de 120 racines d'épreuve du banc (1000 à 1119), qui ne sont pas des racines du générateur du programme.
- J'ai lu `registres/go.md` sur `main` pour les mots de Lazar cités ; rien d'autre sur `main`.
- Le texte de la batterie fait environ 250 lignes. Le mandat le voulait court ; la spécification exacte de la sonde des nombres et les droits du vérificateur en prennent le tiers.
