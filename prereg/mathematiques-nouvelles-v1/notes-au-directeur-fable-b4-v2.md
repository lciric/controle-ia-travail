# Notes au directeur — brouillon 4 du préenregistrement du pilote « oracles plantés » et devis v4 — v2

- Nature : notes de travail (classe C) qui accompagnent deux pièces décisives. Auteur : le concepteur (mandat adressé à Claude Fable 5.2 ; session fille de l'abonnement, effort maximal ; le modèle servi est relevé dans le message de remise à la mère, non ici). Le 2026-11-22. Aucun appel à un fournisseur, aucune dépense, processeur seul.
- Mandat servi : `mandat-fable-brouillon-4-v2.md` (`4a3412ab3fafcf79a6651f486ed972ee370beb62646c026c408d6cf5f1ae9116`). La consigne d'ouverture nommait la v1 (`d57c9906…`) ; la mère a demandé la v2 par message. Empreinte vérifiée ; la v2 n'ajoute que la question du directeur.
- Pièces rendues, même dossier : `preenregistrement-pilote-generation-v1-brouillon-4-v2.md`, `devis-pilote-generation-v4-brouillon.md`, `empreintes-code-lot-b1-v6.md`, et `calculs-v4/` (script du devis et sa sortie, `8194b015…` ; sonde et sa sortie, `e6ae3d49…`). Empreintes aux compagnons.

## Verdict

Le brouillon 4 traite les 27 remarques : 27 acceptées, dont 6 avec un changement que je motive ; aucune refusée en entier. Le code de la version 6 est retenu tel quel, le blanc du commit est rempli. Un fait d'instrument trouvé en écrivant change la portée de H3 et te revient (nœud 1) : sur les racines d'essai, une règle sans calcul rend déjà un contre-exemple vérifié sur 80 % à 91 % des faux.

## A. Ce que j'ai trouvé en écrivant (faits d'instrument, racines d'essai seulement)

1. **Une règle aveugle fait presque tout le travail de la lecture « sur contre-exemples vérifiés ».** Avancer trois instances sans évaluer l'énoncé (toutes les variables au plafond 3N, à 1, à N + 1) donne un contre-exemple vérifié sur 60 à 68 des 75 faux de la sous-banque, selon la racine (41 racines ; médiane 63). 20 des 24 gabarits de faux tombent à chaque fois : un seuil monotone dépassé est faux à toute instance assez grande. Seuls quatre gabarits résistent ; il reste 7 à 15 énoncés où un calcul est nécessaire. Source : sonde `prereg/mathematiques-nouvelles-v1/calculs-v4/sortie-sonde-instances-aveugles-v1.txt` (`e6ae3d49…`). La règle a été écrite avant sa première mesure et n'a pas été retouchée.
2. **Conséquence.** Le seuil que le contre-lecteur proposait pour la branche haute (« S produit des contre-exemples vérifiés » si sa part dépasse 0,30) aurait été acquis d'avance, comme le « N aucun par construction » qu'il dénonçait. Je l'ai remplacé par deux comparaisons appariées : S contre la lecture nue, S contre la règle aveugle.
3. **Ce que S et N jugent n'était écrit nulle part.** La définition servie ne parle que de la vérité bornée à N. Sous cette borne, un piège est vrai : le compter « faux » aurait puni une réponse juste. Et sans plafond annoncé, aucun bras ne sait où un contre-exemple est admis. Le brouillon 4 fixe : l'énoncé se juge jusqu'au plafond B = 3N, donné en nombre dans la consigne des deux bras.
4. **Le balayage compte 41 racines distinctes, non 42** : la racine 11 y passe deux fois (`v6-aires.json`, `32cd1781…`). Les bornes 0,939 et 0,982 ne changent pas.
5. **L'écart « 16 contre 17 textes répétés » n'en est pas un** : le compte dépend de la racine (16 sur 24 racines, 17 sur 13, 18 sur 4). Et un texte de piège se répète sur 10 racines sur 41 ; la note du code n'en voyait aucun sur ses deux racines.
6. **La base « grammaire aléatoire » va de 0,052 à 0,125 de précision** (médiane 0,076). À 0,125, la condition « la battre de 0,15 » exige 0,275 : elle peut mordre au-dessus du seuil de 0,25.

## B. Décisions qui changent une prédiction, un seuil ou le code

1. **H3 reformulée.** Lecture en preuve dans les deux branches d'aire : cinq affirmations E1 à E5 sur les contre-exemples vérifiés (§ Seuil). Lecture en verdict seulement si l'aire est sous 0,75. Aucun seuil sur la part de S seule.
2. **Le bras N** reçoit le schéma de sortie de S et passe par la même vérification exacte. Trois instances au plus par sortie, pour les deux bras : sans cette borne, énumérer toutes les instances ferait vérifier tous les faux par le code.
3. **Prédictions de H3 récrites.** Les anciens intervalles des contre-exemples vérifiés de S sur les pièges ([0,15 ; 0,50]) supposaient un bras qui ne cherche pas au-delà de N ; avec le plafond servi, je prédis [0,65 ; 1,00]. Les intervalles des verdicts déclarés sont élargis et passent en description. Deux prédictions d'instrument ajoutées : la règle aveugle (58 à 70 sur 75) et l'aire (au-dessus de 0,75).
4. **H1** : aucun seuil ne change ; les deux verdicts ne se recouvrent plus ; la condition sur la base entre dans le critère ; la règle est dite descriptive, sans niveau nominal.
5. **H2** : rendement par dollar par monde ; seuil du test des signes selon le nombre de mondes sans ex æquo ; **un seul prix d'Argon** pour toute la course (aucun appel d'Argon entre le 30 novembre et le 2 décembre), sinon H2 passe en description.
6. **H4** : les 20 énoncés de mondes sont des énoncés faux (la note devient mécanique). Une pièce de plus à écrire avant le scellement : la liste source des connus (au moins 24 par strate, les obscurs relevés sur source versée). Une étape de plus après : la relecture de fidélité des reformulations, avec remplacement du connu si la reformulation reste infidèle.
7. **Réserve de la garde de dépense : 5,93 → 6,50.** Un item N en vol (0,496 au pire) et le relecteur de repli manquaient. Le plafond reste 300.
8. **Garde de projection ajoutée (A14).** À la fin de chaque bloc d'un monde, la dépense totale est projetée sur les coûts mesurés ; arrêt si elle dépasse 293,50.
9. **Racine.** Trois racines de 128 bits tirées dans la commande de scellement. Le manifeste poussé ne porte que leurs empreintes : une racine en clair sur la branche livrerait les clés. Elles sont écrites en clair à l'ouverture des clés.
10. **Proposeurs** : une proposition par appel ; chacun voit ses propres propositions antérieures dans le monde, jamais leur issue. Les brouillons précédents ne le disaient pas ; sans cela H1 et H2 ne sont pas définies.
11. **Code** : version 6 retenue (`35ac9e10738ccaac486ec9b9684fe70441f6371a`), aucune version 7.
    - Test de redite non appliqué aux pièges à la plantation : approuvé.
    - Journal des refus quand les trois racines échouent : exigence au lot B3 (la commande de scellement écrit le manifeste d'arrêt).
    - Tout le reste de mes demandes vit dans le lot B3 : harnais d'appels, commande de scellement, script d'analyse.

## C. Nœuds qui te reviennent

### Nœud 1 — Périmètre de H3 après la mesure de la règle aveugle

- **Décision** : courir ou non les bras S et N dans ce pilote, sachant qu'une règle sans calcul atteint déjà 80 % à 91 % des faux.
- **Enjeu** : 92,35 USD attendus sur 165,17 (0,559 du total), la seule machine louée du pilote et la part la plus lourde du lot B3 ; en face, une affirmation « S dépasse la règle aveugle » qui ne peut reposer que sur 7 à 15 énoncés de quatre gabarits. Elle exige au moins 6 de ces énoncés vérifiés par S sans aucune perte ailleurs, 8 avec une perte, 10 avec deux (sortie du script v4, bloc 12).
- **Options**
  - (a) Courir S et N comme écrit. Avantage : l'expérimentateur est mesuré maintenant ; sa chaîne (bac, machine jetable, vérification exacte) est éprouvée avant le pilote 2 ; ses réfutations fausses sont lues ; c'est la priorité que tu as dite (GO-2026-11-21-16). Inconvénient : issue la plus probable de la comparaison à la règle aveugle, rien d'établi.
  - (b) Courir S sans N. Avantage : 28,29 d'économie attendue ; plafond 250. Inconvénient : plus de comparaison à la lecture nue, et plus de lecture en verdict même si l'aire tombait sous le seuil.
  - (c) Reporter S et N au pilote 2, sur la banque de la version 7. Avantage : 92,35 d'économie attendue, plafond 150, aucune machine, lot B3 allégé ; H1, H2 et H4 inchangées ; l'expérimentateur serait mesuré sur une banque faite pour le distinguer. Inconvénient : rien n'est appris sur lui avant le pilote 2, et sa chaîne y serait éprouvée pour la première fois.
- **Recommandation** : (a), confiance 0,55. Ce qui me ferait changer : si la part « bras S » du lot B3 menace l'échéance, ou si tu préfères ne payer cette mesure qu'une fois : alors (c), sans perte pour H1, H2 ni H4. Le brouillon 4 et le devis v4 sont écrits pour (a) ; (b) ou (c) demandent un brouillon 5 en différences.
- **Défaut** : aucun (dépense et périmètre).

### Nœud 2 — Le plafond d'appels (ta question, point i)

- **Décision** : garder 300 USD d'appels et 65 USD de machine, avec la garde de projection.
- **Enjeu** : les profils de jetons sont supposés. Le plafond vaut 1,82 fois l'attendu ; le pire cas vaut 3,58 fois l'attendu. Une course coupée par le plafond laisse des hypothèses « non courues » après 300 USD.
- **Options**
  - (a) 300 et 65, avec la garde de projection et la réserve à 6,50. Avantage : marge de 107,21 sur l'attendu avec lignes conditionnelles ; un dérapage des coûts se voit à la fin du premier bloc, après 15,69 attendus (54,00 au pire), et non à 300. Inconvénient : si les coûts réels dépassent 1,78 fois l'attendu, la course s'arrête au premier bloc et il faut un devis v5.
  - (b) 400. Avantage : tolère des coûts jusqu'à (400 − 6,50 − 0,10) / 165,07 = 2,38 fois l'attendu sans retour vers toi. Inconvénient : 100 USD d'exposition de plus, que rien ne justifie avant la mesure du premier bloc.
  - (c) 250. Avantage : exposition moindre. Inconvénient : marge de 250 − 192,79 = 57,21 seulement ; des profils une fois et demie plus lourds tronquent la course.
- **Recommandation** : (a), confiance 0,7. Si le périmètre change (nœud 1) : 250 et 65 sans le bras N, 150 et 0 sans S ni N (devis v4, § 8). La ligne du protocole d'antériorité est à part (nœud 4).
- **Défaut** : aucun (dépense).

### Nœud 3 — L'échéance de la course (point ii)

- **Décision** : fixer l'échéance au 13 décembre 2026, 23:59 UTC, et à sept jours après l'appel de fumée, le premier des deux ; ne pas viser le 30 novembre.
- **Enjeu** : le doublement d'Argon ne pèse que 7,20 USD à l'attendu, 23,04 au pire. Avant le premier appel il reste : la vérification de ce brouillon, les consignes, la liste des connus, le lot B3 et ses essais, le protocole d'antériorité, le script d'analyse. Huit jours n'y suffisent pas sans presser une chaîne de classe A.
- **Options**
  - (a) 30 novembre. Avantage : Argon au prix de novembre. Inconvénient : presser le lot B3 et deux contre-lectures pour 7 USD ; un pilote lancé sur un harnais mal éprouvé coûte plus que le doublement.
  - (b) 13 décembre, et sept jours après la fumée. Avantage : trois semaines depuis le relevé des prix ; un seul prix d'Argon ; un GO de dépense qui ne reste pas ouvert. Inconvénient : Argon au prix de décembre.
  - (c) Aucune date, seulement une durée après le GO. Avantage : souplesse. Inconvénient : un GO de dépense sans terme, alors que les prix et les modèles servis bougent.
- **Recommandation** : (b), confiance 0,65. Avec elle, les prix sont relus la veille de la fumée ; un écart au devis demande un devis v5.
- **Défaut** : aucun (dépense).

### Nœud 4 — Qui exécute le protocole d'antériorité (point iii)

- **Décision** : confier la lecture à `gpt-6.2-astra`, par l'interface, dans un montage où le code moissonne et contrôle les extraits ; `kimi-k3.1-pro` relit les pièces douteuses ; devis à part.
- **Enjeu** : R8 avant le scellement. Le lecteur ne doit partager les angles morts ni des proposeurs (Opus, Argon) ni du concepteur, qui est un Claude : j'ai donc écrit « ni Claude, ni Gemini ». Le pilote ne revendique rien : la lecture doit rester proportionnée.
- **Options**
  - (a) **Lecteur : `gpt-6.2-astra` (lignée OpenAI). Voie : l'interface.** Un script de classe B, écrit par Opus, lance les requêtes sur deux index publics, télécharge et empreinte les PDF, les découpe par page, puis cherche chaque extrait cité sur la page citée. Second lecteur `kimi-k3.1-pro` sur les pièces dites « collision » ou « doute ». **Devis : 10,72 / 25,10 / 94,80 ; plafond proposé 40** (devis v4, § 7). Avantage : lignée étrangère aux proposeurs et au concepteur ; aucun constat ne repose sur la parole du lecteur ; un à deux jours. Inconvénient : une dépense de plus ; un montage à coder ; Astra est aussi le juge de H4 (aucune mémoire d'un appel à l'autre, mais aucune famille n'est sans rôle dans ce pilote).
  - (b) **Un humain** : toi, ou un spécialiste extérieur. 0 USD. Avantage : le lecteur le plus sûr sur le fond. Inconvénient : jusqu'à 50 pièces, plusieurs heures de ton temps ; un extérieur est un contact, donc un nœud.
  - (c) **Une session de l'abonnement** (Fable ou Sonnet). 0 USD, immédiat. Inconvénient : même maison qu'un proposeur et que le concepteur : c'est un écart à la règle de lignée. Je l'admets pour la moisson mécanique, pas pour le jugement.
- **Recommandation** : (a), confiance 0,6 ; la moisson peut y être faite par une session de l'abonnement, sans coût. Carbon est exclu (même maison qu'Argon). Je ne sais pas de quelle maison est Neon : s'il n'est ni de celle d'Opus ni de celle d'Argon, il ferait un lecteur sans rôle dans le pilote. Si tu refuses toute dépense pour l'antériorité d'un pilote qui ne revendique rien : (c), dit comme un écart, et la lecture par une autre lignée reportée à la première revendication.
- **Défaut** : aucun (dépense).

### Nœud 5 — Le seuil de 0,75 (défaut en cours)

Le texte suit le défaut : seuil gardé, dit gardé après lecture de la mesure, branche haute dite attendue, version 7 au dossier du pilote 2. Le blanc « décision sur le seuil » attend l'identifiant de ton mot ou du défaut échu. Un ajout pour la version 7 : elle doit fermer deux fuites, non une. La fuite de style (pièges à borne naturelle), et la fuite d'instance (faux dont le contre-exemple n'est pas à une instance extrême : non monotones, à deux variables). Sinon la règle aveugle restera vers 80 %.

### Nœud 6 — La règle de retirage (rappel)

Elle sélectionne les racines plantables. Je la crois sans effet sur les hypothèses (aucun appel avant) ; c'est une sélection, et le rapport le dira. Aucune racine d'essai n'a été refusée en version 6 (0 sur 41).

## D. Réserves sur mon propre travail

- **La sonde et le script du devis v4 sont de moi**, alors que le code revient à Opus. Je les ai écrits parce que le critère de H3 en dépendait. Ils sont courts, importent le paquet figé sans le modifier, et sont à vérifier par le contre-lecteur du code (classe B) avant d'être cités dans un texte scellé.
- Le script v4 a relevé deux valeurs fausses que j'avais écrites à la main (dépense basse à la fin du premier bloc ; nombre d'énoncés exigés avec trois pertes). Elles sont corrigées ; la sortie versée ne porte aucun écart.
- J'ai contrôlé qu'une racine d'essai de 128 bits plante sous le code de la version 6. Ce contrôle n'est pas versé : il est à refaire au lot B3.
- Je n'ai pas relu le brouillon 3 de l'essai « preuve formelle contre suite bon marché » ; il n'est cité que pour le nom du bras S.
- **Noms en « -v2 ».** Une première rédaction du brouillon 4 (`28ef25bd…`) et de ces notes (`7be57e7c…`), scellée sur place et jamais versée, portait dans sa ligne « Auteur » une mention que mes consignes de session m'interdisent d'écrire dans un dépôt. La garde du scellement interdit d'écraser (R12) : je ne l'ai pas contournée, j'ai écrit une version neuve sous un nom neuf et écarté la première. Seule la ligne « Auteur » diffère ; le devis n'est pas touché.
- Rien n'a été lu des fichiers interdits par le mandat, ni d'une autre branche. Ni routine de reprise ni passation, selon la consigne.

## E. Ce qui reste avant le scellement, dans l'ordre

1. Vérification des corrections par le même contre-lecteur (Opus 5.5) ; vérification de la sonde et du script v4.
2. Tes mots : seuil (défaut), périmètre, plafond, échéance, exécutant du protocole d'antériorité.
3. Consignes et liste des connus, par le concepteur, contre-lues.
4. Lot B3 par Opus : harnais d'appels, commande de scellement, script d'analyse, essais R5.
5. Protocole d'antériorité.
6. GO sur le devis ; blancs portés ; scellement et tirage des racines.
