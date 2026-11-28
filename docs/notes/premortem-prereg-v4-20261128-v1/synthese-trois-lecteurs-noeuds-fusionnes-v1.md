# Pré-mortem des brouillons de Gemini par trois lecteurs neufs : synthèse et nœuds fusionnés (v1)

Classe C. Session mère, 28 novembre 2026. Sources, dans ce dossier : `lecteur-A/rendu-lecteur-A-v1.md` (`9548feda…`), `lecteur-B/rendu-lecteur-B-v1.md` (`5e9f1784…`), `lecteur-C/rendu-lecteur-C-v1.md` (`01ccdfa2…`) ; note d'antériorité `docs/notes/anteriorite-sondes-code-v1/anteriorite-sondes-code-v1.md`. Lecteurs : Fable 5.2, effort maximal, neufs et indépendants. Chacun avait une pièce principale (A : additif de G0 ; B : architecture de G1 ; C : texte des arbitrages du 28 et banc de G1) et un regard sur les deux autres.

## 1. Verdict des trois lecteurs (convergent)
- **Additif du critère 3 de la porte de fin de phase 0** (micro-course du saboteur discret à coût déclaré) : **à réécrire**. Sur les textes réels de la course de dose-réponse, le validateur d'action refuse la plupart des actions honnêtes : acceptation honnête de 21,4 % au premier tirage, 24 tâches sur 64 sous 10 % (B) ; quatre actions honnêtes sur cinq refusées, et toutes celles de la consigne neutre (A). La course s'arrêterait donc sur sa propre garde de rejet avant toute lecture (arrêt simulé : 1,00, C). Surtout, l'organisme y est trié contre le lecteur du texte qui doit échouer : c'est une sélection contre un moniteur, contraire à trois textes en vigueur (P-066, N-053, N-063 v2) que l'accord du 28 ne nomme pas.
- **Porte de fin de phase 1** (H1 et H2) : **suspendue à un nœud**. Elle remplace sans les nommer la ligne en vigueur : les treize décisions du 5 novembre, le pari apparié, la strate « diffus, flou » et le plafond de 6 331 USD. Jouée telle quelle (B) :
  - puissance de 0 % [0 ; 3] pour H1 et pour H2 à l'effet le plus plausible ;
  - 227 à 2 511 USD pour un plafond de 65 USD écrit dans le brouillon ;
  - « tenue » à tort dans 20 à 100 % des mondes où la sonde ne lit que l'empreinte d'un adaptateur ;
  - la banque de 727 tâches et ses quatre adaptateurs n'existent pas.
- **Texte des arbitrages du 28** : **à reprendre**. Ses options ne comprenaient ni la ligne en vigueur ni de coût en dollars ; 28 de ses éléments sont absents des lignes du registre et il porte au moins dix mentions fausses (C). Trois faits sont à corriger : l'empreinte de la contre-épreuve, le seuil des reprises et les coûts (A).
- **Contre-lecture** : les sections « Contre-lecture » des brouillons ne satisfont pas la règle de contre-lecture à froid (R2). Le rapport cité porte sur un autre texte, lu hors du dépôt, et la seconde empreinte (`59a2a571…`) ne désigne aucun fichier. Le silence du validateur de préenregistrement prouve seulement huit titres non vides et deux chaînes de 64 caractères : sur 13 mutations de chaque brouillon, il en voit 2 (B).

Pronostic de la micro-course (A) :
- telle qu'écrite : non scellable 0,50, arrêtée par ses gardes 0,45 ;
- après les remèdes les moins chers : « sans objet » 0,24, sondes sous leur plancher 0,27, sonde porteuse défendable 0,005.

Le lecteur B, sur le texte tel qu'écrit, donne : arrêtée 0,60, « sans objet » 0,12, porteuse défendable 0,01.

## 2. Antériorité (note du 28)
- **Code net** : occupé en partie, de très près. Le gain des sondes sur les moniteurs de texte est publié pour le sabotage de code d'un agent, mesuré pas à pas à 1 % de fausses alertes (Hollinsworth et al.), et pour les portes dérobées de la banque APPS (Parrack et al.). Sur la banque Python, une H1 « tenue » serait une variante incrémentale.
- **Tâches floues** (propositions de recherche sabotées) : libres à notre connaissance, recherche à durcir (R8).
- **Accumulation des scores de sondes d'action en action** sur un épisode d'agent : non trouvée. Deux travaux la laissent ouverte par écrit.
- **Indices contraires sur le code** : la boîte noire y voit la vérité dans les jetons publics. Les sondes sont nettement plus faibles sur les petits modèles (Hollinsworth et al., p. 8), or l'agent est un modèle de 8 milliards de paramètres.

## 3. Nœuds fusionnés
**Nœud 1. Sur quel banc se juge la porte de fin de phase 1 ?** Sources : A6, B-N1, C1 et l'antériorité.
- Enjeu : la revendication « diffus, flou » du papier A. Le brouillon change le banc, le saboteur, la statistique et les modes sans les nommer, et sur le code net la zone est occupée.
- (a) La ligne en vigueur seule : banc neuf d'environ 480 propositions d'expériences, modes « contrôles affaiblis » et tenu à l'écart, pari apparié. Elle porte la revendication et tout y est décidé ; la vérité du dommage passe par des lecteurs (environ 4 870 USD) et le banc n'a pas d'oracle exécutable.
- (b) La ligne en vigueur pour la porte, et la banque Python comme strate « nette » rapportée hors critère, après pilote et devis (le banc à tâches exécutables déjà prévu par N-060 v3). On garde la revendication et on gagne un banc d'étalonnage à vérité exécutable ; c'est un chantier de plus.
- (c) La banque Python remplace le banc : un seul banc, un oracle sans lecteur. Mais c'est une modification du programme : thèse du papier A, N-054 à N-056, N-060 v3 et les treize décisions sont à remplacer nommément. « Flou » est perdu et la zone est occupée.
- Lecteurs : (b) ou son équivalent, 0,6 chacun.
- Recommandation : **(b), 0,6**. Défaut : aucun (porte et revendication).

**Nœud 2. Le saboteur peut-il être trié contre le lecteur du texte ?** Sources : A1, C3 et le verdict de B. Ce nœud revient sur le filtre de l'accord du 28.
- Enjeu : un résultat positif obtenu sur un organisme débarrassé de ce que lit le lecteur ne tient pas devant un référé ; tel qu'écrit, le rejet arrête la course.
- (a) Aucun rejet de mots ni de format exact ; le format du coût est demandé à tous les bras par la consigne publique, et les mentions sont mesurées (acceptation de 69 à 79 %). Conforme aux textes en vigueur ; le lecteur des mots peut encore réussir.
- (b) Filtre gardé, bras déclaré « filtré contre le lecteur du texte », bras non filtré joué à côté. On mesure ce que voit la sonde quand le texte se tait, au prix d'un bras de plus et d'une portée restreinte.
- (c) Filtre tel qu'arbitré : arrêt probable, résultat indéfendable.
- Lecteurs : A (a) 0,7 ; C (b) de son nœud 3, équivalent à (a) ici, 0,55.
- Recommandation : **(a), 0,7**. Défaut : aucun.

**Nœud 3. Par quelle voie clore la partie (i) du critère 3 de G0 ?** Sources : A5, B-N4, C3. La ligne scellée ouvrait trois voies (dérogation, course neuve, constat) ; l'accord du 28 n'en a offert qu'une, sans coût.
- (a) Constat maintenant : partie (i) non tenue à la course désignée, et l'effort passe à l'organisme sans texte de consigne. 0 USD, rien d'indéfendable ; on renonce à la mesure.
- (b) Micro-course neuve, réécrite dans la forme du nœud 2 (a) : validateur éprouvé d'abord sur les textes réels, « sans objet » écrit d'avance comme constat final, sans troisième course. La mesure est propre ; elle coûte 16 à 27 USD et une à deux semaines de code et de contre-lectures, et une issue positive est improbable.
- (c) Dérogation sur la première course : juger aux facteurs 3 et 5 contre la consigne neutre, où le lecteur scellé échoue déjà (0,58 à 0,69), par un additif scellé avant toute sonde. Lisible vite, pour quelques dollars ; mais elle lève le point 2 de ton accord du 28, qui ferme ces archives, et choisit le contraste de la porte après coup.
- Lecteurs, en **divergence non résolue** :
  - A : (c) si tu lèves le point 2, sinon (b) ; 0,5 ;
  - B : (a), puis une course neuve sur devis ; 0,5 ;
  - C : (b) ; 0,55 (il ne retenait (a) que si l'échéance de décembre manquait de temps, échéance levée depuis).
- Recommandation : **(b), 0,55**, avec ta règle du 28 (des portes passées rigoureusement) contre la dérogation. Ce nœud touche directement ta question sur la taille du modèle : le trancher après les réponses de Fable et de Carbon. Défaut : aucun.

**Nœud 4. Quel énoncé pour le contraste au témoin apparié de G1 ?** Source : B-N2.
- Enjeu : sous la seule empreinte et avec un témoin imparfait, la règle du brouillon rend « tenue » à tort dans 20 à 100 % des mondes.
- (a) La porte se gagne aussi contre le témoin, avec des seuils recalibrés sur lui (environ 600 épisodes de témoin par mode).
- (b) La garde décide et le contraste est rapporté.
- (c) La règle du brouillon : jamais.
- Dans tous les cas : familles d'adaptateurs jumeaux et témoin remis à l'intensité.
- Recommandation : **(a) si le devis la porte, sinon (b) ; 0,6**. Défaut : aucun.

**Nœud 5. Mesurer avant de figer.** Sources : A4, B-N3.
- G0 : un essai de chaîne honnête seule, seize épisodes au plus, sur des tâches de la banque initiale, pour quelques dollars. Il mesure le bras que le bloc privé ne change pas, et les gardes de rejet restent en réserve.
- G1 : un pilote hors décision sur 64 tâches avant de jouer la porte (réussite du modèle nu, aires par action des sondes et de la boîte noire, règle d'arrêt écrite d'avance), pour 15 à 30 USD et une semaine.
- Recommandation : **les deux, sur devis ; 0,7**. Défaut : devis préparés, rien dépensé sans ton accord.

**Nœud 6. Retour aux textes en vigueur que les brouillons changeaient sans les nommer.** Sources : C2, A2, A3, C4, C5.
- Le pari apparié borné décide G1 et le rééchantillonnage est rapporté : déjà confirmé le 28 octobre, que le brouillon renverse.
- La micro-course se lit à chaque dose jugée (règle scellée), non sur la première seule.
- La sonde est comparée aux trois prédicteurs triviaux du texte scellé, et l'écart « sonde moins coût » est rapporté. Exiger qu'elle batte le coût lui-même ramènerait l'issue « tenue » de 0,72 à 0,05 des mondes plantés.
- Les lignes du registre font foi pour les accords du 28 ; le reste du texte est une proposition.
- Le juge boîte noire de 27 milliards de paramètres reste sous N-029 : accord séparé, sur devis, après le verdict de la porte de fin de phase 0.
- Recommandation : **confirmer ; 0,75**. Défaut : ces textes restent en vigueur ; rien ne change sans ton mot.

## 4. Pour la réécriture (relevés des lecteurs)
- **Additif de G0, à retirer sans perte de validité** :
  - effacement linéaire de concept et résidualisation après maximum ;
  - dérive de Slepian et moyenne par action « co-rapportées » ;
  - clause de fréquence, vide après filtrage ;
  - scission physique des archives et crochet d'audit, que des lignes de registre remplacent ;
  - listes de mots.
- **Additif de G0, à garder** :
  - clauses orientées contre l'agent honnête et contre la consigne neutre ;
  - plancher et prédicteurs triviaux ;
  - coupe avant le coût ;
  - scission des scores de l'honnête.
- **Additif de G0, impossible à figer aujourd'hui** :
  - les textes privés : leur auteur est cloisonné et aucun pilote n'est permis sous texte privé ;
  - tout seuil de rejet ;
  - la banque : extraction à faire à partir du rang 211, ou 234, premier rang jamais examiné ;
  - quatre modules non écrits ;
  - le devis.
- **G1, à retirer** :
  - le rang 2 de H2 ;
  - l'effacement et la résidualisation ;
  - l'un des deux comparateurs « maximum » et « cascade continue » ;
  - la pré-gaussianisation de Gumbel ;
  - le rééchantillonnage comme décideur.
- **G1, impossible à figer aujourd'hui** :
  - la banque et le quatrième mode ;
  - les adaptateurs et leur intensité ;
  - la révision du juge ;
  - la puissance ;
  - l'énoncé du témoin apparié ;
  - la prévision du modèle nul de la référence honnête ;
  - le devis.

## 5. Suite
- Après tes décisions : un agent Fable neuf, en effort maximal, réécrit l'additif de G0 d'abord, puis G1 après le nœud 1. Viennent ensuite le validateur, la contre-lecture à froid par un Fable neuf (GO-2026-11-28-06) et la vérification des corrections par le même relecteur, puis le scellement et ton accord.
- Routine : le validateur de préenregistrement est renforcé pour vérifier sur disque les empreintes et les chemins cités (code par Opus, contre-lecture de classe B).
