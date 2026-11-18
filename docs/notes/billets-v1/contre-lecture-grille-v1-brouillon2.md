# Contre-lecture de la grille des gestes de rédaction des billets (brouillon 2), avant son gel — v1

Écrite le 2026-11-18 par un sous-agent neuf (Fable 5.2), contre-lecteur, sous le mandat `docs/notes/billets-v1/mandat-contre-lecture-grille-v1.md` (`4cd093e2d4188bbc65ba7a04770cabc05ed6681b42ff9a8c41d70eba0415bccf`, compagnon vérifié). Le contre-lecteur n'a écrit ni la grille ni le tri. Il ne codera pas la moitié tenue à l'écart et n'écrira aucun billet.

**Objet contre-lu** : `docs/notes/billets-v1/grille-gestes-v1-brouillon2.md` (`d6ead9a9a642ec98e9f66c5c0fe058309a502d81962981bc080296a8886e8a96`, compagnon vérifié) et ses huit pièces sous `docs/notes/billets-v1/pieces-grille-v2/` (compagnons vérifiés).

**Rien de la moitié tenue à l'écart n'a été ouvert**, ni dans son dossier, ni dans les dossiers communs. Aucune requête au site. Aucun fichier existant modifié. Ni commit, ni poussée.

## 0. Verdict

**Gelable après corrections.** La grille est bien construite : 25 questions fermées, modalités peu nombreuses, indicateur binaire écrit d'avance, citations vérifiées par programme, plan d'analyse mis en code avant tout codage. Mais deux défauts bloquent le gel, et dix autres sont à corriger avant le gel (texte de la grille) ou avant la préparation des copies (scripts).

- **Bloquants (2)** : l'exception de prévalence haute du seuil de fiabilité est une échappatoire (B1) ; le script de préparation écrit le dossier des commentaires, qui révèle le statut des billets, au même endroit et au même moment que les copies de la première passe (B2).
- **Majeurs (10)** : cas limites manquants sur dix gestes et aucun essai à deux codeurs avant le gel (M1) ; borne des 250 mots, texte et code en désaccord (M2) ; masquage des auteurs partiel (M3) ; aveugle non mesuré (M4) ; procédure de dépôt incomplète (M5) ; phrase sur la puissance inexacte (M6) ; deux gestes qui ne sont pas des gestes de rédaction peuvent devenir consignes (M7) ; règle du gabarit à préciser (M8) ; analyse des objections en désaccord avec le texte (M9) ; un décompte faux et une limite à ajouter (M10).
- **Ce que l'étude peut détecter** : avec 23 paires et 23 comparaisons corrigées, seul un écart vrai d'environ 0,6 entre les deux fréquences (par exemple 20 % contre 80 %) passe quatre fois sur cinq ; un écart de 0,4 passe une fois sur quatre ; un écart de 0,2 ou 0,3 ne passe presque jamais (section 7).

## 1. Ce qui a été vérifié et rejoué

| Vérification | Résultat |
|---|---|
| Empreintes du mandat, de la grille, des huit pièces, du mandat du réviseur, de la règle et du manifeste v2, du rapport du second lecteur, de la liste des billets marqués | toutes conformes (`controle_ia.scellement verifier`) |
| Rejeu de `verifier_citations_v2.py` | sortie **identique à l'octet** à la sortie scellée `verification-citations-v2.json` (`44150697ce40ea70…`) : 106 citations vérifiées, 0 échec, 0 problème de structure |
| Moitié des billets cités dans les sections A et B | 42 billets distincts, tous en développement v2, aucun des deux billets marqués (nommés en section 0 comme exclus) ; les 18 identifiants de la tenue à l'écart présents dans la grille ne figurent qu'en section 6, comme identifiants (`pieces-contre-lecture-grille-v1/decomptes-complementaires-v1.json`, `a0cb3494…`) |
| Citations hors du format vérifié | une seule vraie citation échappe au script : le cas d'école de la priorité des objections (commentaire `HhF5kESdtPHku7kim/zMh7XM5wm68hCSo9b`). Vérifiée à la main : présente, commentaire retenu, non écrit par un auteur |
| Rejeu de `preparer_copies_neutres_v1.py` sur la moitié développement, en dossier temporaire | 58 billets, 296 commentaires dont 80 d'auteur, 22 paires ; manifeste de préparation d'empreinte `b982583e787e15ef…`, **identique** à celle de l'essai scellé |
| Refus du script sur la tenue à l'écart | rejoué trois fois avec une racine inexistante (sans `--go`, avec `--go` malformé, avec `--go` sans valeur) : « REFUS : tenue à l'écart : préparation interdite sans --go GO-AAAA-MM-JJ-NN », code 2, aucun dossier créé. Le refus tient. Il ne contrôle que la **forme** de l'identifiant (lecture du code, ligne 47) : voir m5 |
| Rejeu de `analyser_codage_v1.py --essai-synthetique` | sortie identique à la sortie scellée, **sauf l'empreinte de la grille** : l'essai scellé a été joué sur un état antérieur de la grille (`b00d5dca…`), pas sur la grille scellée (`d6ead9a9…`) : voir m1 |
| Décomptes de la section 5.1 contre le manifeste et les deux listes de marquage | 62 billets, 39 bien notés, 16 sans apparié, 23 paires, 13 paires hors marquage 1, 11 hors des deux marquages : conformes. **Un décompte faux** : voir M10 |
| Structure des 25 gestes | question, 2 à 4 modalités distinctes, indicateur inclus strictement dans les modalités, statut d'analyse : présents partout (contrôle du script, rejoué) |

## 2. Bloquants

### B1. L'exception de prévalence haute est une échappatoire

**Avant** (section 5.2) : « si la prévalence de l'indicateur (deux codeurs réunis) dépasse 90 % ou est sous 10 %, le kappa est instable ; le geste est alors fiable si l'accord brut est ≥ 0,90 (prévalence haute) et non évaluable (prévalence basse, rare : rapporté, jamais consigne) ».

**Défaut.** À prévalence haute, l'accord brut de 0,90 s'obtient sans aucun accord réel. Deux codeurs qui codent « présent » 95 fois sur 100, chacun de son côté et au hasard, tombent d'accord sur 90,5 % des billets. Simulation de la règle écrite (62 billets, dont 44 hors marquage 1, 50 000 tirages) : deux codeurs **indépendants** sont déclarés « fiables » 13 fois sur 100 à prévalence 0,92, **52 fois sur 100 à 0,95, 87 fois sur 100 à 0,97** (`pieces-contre-lecture-grille-v1/verifs-complementaires-dev-v1.json`, `017ce1c5…`). Le cas n'est pas théorique : dans mon essai, trois gestes ont leur indicateur présent sur les six billets (place de la thèse, base de comparaison, lien vers le code). Un geste ainsi « fiable » passe ensuite presque sûrement le point 3 de la section 8 et devient consigne une fois sur deux par le seul hasard du signe de la différence.

**Après** (proposé) : « si la prévalence de l'indicateur (deux codeurs réunis) dépasse 90 % ou est sous 10 % sur l'un des deux ensembles, ni le kappa ni l'accord brut ne mesurent la fiabilité : le geste est **non évaluable**, rapporté avec sa prévalence et son accord brut. Prévalence haute : le geste est dit « quasi universel » ; il n'entre au gabarit que sous le qualificatif « convention du genre (fiabilité non mesurée) », hors des points 1 à 4 de la section 8, et n'est jamais « distinctif » ni « à éviter ». Prévalence basse : rapporté, jamais consigne. » Le code (`statut_fiab` et le bloc des consignes) suit. La prévalence elle-même reste un fait solide : si les deux codeurs voient le geste presque partout, « presque tous les billets le font » est établi sans accord billet par billet.

### B2. Le dossier des commentaires révèle le statut pendant la première passe

**Avant.** Le script écrit en un seul appel `SORTIE/codeurs/billets/`, `SORTIE/codeurs/commentaires/` et les deux listes d'ordre. Le dossier des commentaires ne contient un fichier que pour les billets bien notés : 36 fichiers pour 36 bien notés dans le rejeu sur le développement. La section 4.3 dit bien que la seconde passe « révèle quels billets sont bien notés » et vient après le scellement de la première ; mais rien n'empêche un codeur, qui est un agent avec accès aux fichiers, de lister le dossier voisin. La section 4.4 lui donne « leur dossier de copies neutres » sans le nommer. La barrière n'est que de convention.

**Après** (proposé). Deux appels distincts du script. `--passe 1` écrit `SORTIE/passe-1/codeur-1/` et `SORTIE/passe-1/codeur-2/` (copies des billets et liste d'ordre du seul codeur) et `SORTIE/cles/`. `--passe 2` **refuse** tant qu'on ne lui donne pas les deux fichiers de la première passe et leurs compagnons d'empreinte, qu'il vérifie ; alors seulement il écrit `SORTIE/passe-2/commentaires/`. Le mandat de chaque codeur nomme le seul dossier qu'il ouvre, nomme comme interdits `cles/`, le manifeste, `/home/user/billets-corpus-v2/` et le dossier de l'autre codeur, et demande la liste de tous les fichiers ouverts. Le refus de la seconde passe se teste comme celui de la tenue à l'écart (cas sain et cas fautif).

## 3. Majeurs

### M1. Dix gestes laissent une hésitation qui peut changer l'indicateur ; aucun essai à deux codeurs avant le gel

Constat (section 5) : sur 150 décisions de mon essai, 32 portent un doute qui peut changer l'indicateur binaire. Sept gestes n'en portent aucun. Neuf en portent sur deux billets ou plus : le choix justifié contre une option écartée (4 sur 6), le caractère préliminaire, l'enjeu de sûreté, l'analogie (3 chacun), le dispositif nommé, les limites, les impasses, l'explication concurrente, l'appel à poursuivre (2 chacun) ; un dixième, les non-revendications, s'y ajoute par sa frontière avec les limites.

**Avant** : cas limites actuels. **Après** : ajouter les cas limites listés en section 5.3, puis faire coder par **deux agents neufs** une douzaine de billets de la moitié développement tirés par graine, sur copies neutres, et calculer le kappa de l'indicateur par geste avec les fonctions du script d'analyse. Réécrire les gestes sous 0,60, puis geler. Cet essai ne touche pas la tenue à l'écart et c'est le seul moment où un geste peut encore être réécrit : après le gel, un geste non fiable est perdu (« jamais redéfini puis recodé sur la même moitié »). Sans cet essai, je m'attends à perdre plusieurs des dix gestes ci-dessus.

### M2. La borne des 250 mots : le texte et le code ne disent pas la même chose

**Avant** (section 4.2) : « mots = suites séparées par des blancs, marqueurs exclus ». Le code (`inserer_borne`) compte **tous** les jetons, marqueurs compris : un lien compte pour trois jetons (`[lien`, `:`, `hôte]`), une image pour deux ou plus, un soulignement d'intertitre pour un. Effets mesurés sur les 58 copies de développement (`fuites-copies-neutres-dev-v1.json`, `0f88d03a…`) : les mots réels avant la borne vont de 220 à 251 (médiane 243) ; et **la borne tombe à l'intérieur d'un marqueur dans 2 billets sur 58** (`decomptes-complementaires-v1.json`) : elle coupe un marqueur d'image en deux dans `7TxeC9WPc5LxpjgP8` (« [IMAGE », borne, « 1] ») et un marqueur de lien dans `Qe3jdphWCg9kny3e5`. Dans le premier cas, la figure de résultat en tête (G11) n'est plus décidable.

**Après** : le code compte les seuls mots hors marqueurs (`[IMAGE …]`, `[lien : …]`, `[AUTEUR]`, `[ÉLÉMENT INTERACTIF]`) et hors jetons de pure mise en forme, et insère la borne au premier blanc hors marqueur après le 250e ; l'essai rapporte le minimum et la médiane des mots réels et le nombre de bornes dans un marqueur (attendu : 0). La section 1 reçoit une convention commune : « un énoncé, une liste, un bloc ou une figure compte comme en tête si son **début** est avant la borne » (aujourd'hui dit pour la thèse et le résumé seulement ; manque pour le chiffre, l'enjeu de sûreté et la figure). Dire aussi en section 1 que l'avant-propos compte dans les 250 mots : c'est le choix fait, il se défend (ce que le lecteur voit d'abord), mais il n'est écrit nulle part.

### M3. Le masquage des auteurs est partiel

**Avant** (section 4.2 et cas limites du contexte de production) : les noms de l'auteur et des coauteurs sont « remplacés par [AUTEUR] » ; « les noms d'auteurs sont masqués dans la copie neutre ».

**Constat** sur le développement. Le script remplace le nom affiché entier, par sous-chaîne, sans frontière de mot. (a) Des fragments de noms affichés restent dans 14 billets sur 58, dont 13 bien notés (prénom seul, nom seul dans une référence ; `fuites-copies-neutres-dev-v1.json`). (b) Les noms réels des auteurs à pseudonyme ne sont pas masqués : dans `v7f8ayBxLhmMFRzpa`, un seul pseudonyme est remplacé ; les six noms réels restent dans la liste des contributions, et une phrase donne le nom réel suivi de `[AUTEUR]`. D'après le manifeste seul, 32 billets de développement sur 58 et 36 billets de la tenue à l'écart sur 62 ont au moins un nom affiché en un seul mot, pseudonyme ou prénom (`decomptes-complementaires-v1.json`). (c) Le marqueur lui-même parle : il est présent dans 15 bien notés sur 36 et 4 appariés sur 22 (même pièce). (d) Une adresse électronique est masquée à moitié et garde le domaine de l'organisation. (e) Sans frontière de mot, un nom court peut remplacer un morceau de mot courant ; aucun cas en développement, mais le manifeste de la tenue à l'écart contient onze noms affichés de cinq lettres au plus.

**Après** : masquer aussi chaque partie d'au moins quatre lettres de chaque nom affiché, avec frontières de mot ; masquer les adresses électroniques entières ; faire écrire au manifeste de préparation, par billet, le nombre de remplacements et le nombre de marqueurs collés à un mot (sans texte) ; et **écrire dans la grille que le masquage est partiel** : noms réels des auteurs à pseudonyme, signatures de section, affiliations restent. La phrase du geste G09 devient « les noms affichés des auteurs sont masqués quand ils sont écrits tels quels ; les autres formes restent ».

### M4. L'aveugle n'est pas mesuré, et des codeurs modèles reconnaîtront des billets

Les copies cachent bien le score, les votes, le nombre de commentaires, les étiquettes, l'adresse et l'identifiant : aucune adresse, aucun identifiant du site ne reste (contrôle rejoué, 0 sur 58). La longueur ne dit presque rien (aire sous la courbe 0,59 en développement, 0,53 dans la tenue à l'écart, d'après le manifeste ; 0,56 pour le nombre d'images en développement). Mais il reste, outre M3 : le titre, que les codeurs lisent ; la mémoire des codeurs, qui connaissent sans doute les billets les plus cités de 2022 à 2024 ; les présentations de soi (`S9xyqRAziRMCcJQmz` — « This is my first interpretability research project, coming from a different field. ») ; les notes d'édition et les mentions de publication (`khFC2a4pLPvGtXAGG` — « EDIT: Many people said they found the results very surprising », `N6WM6hs7RQMKDhYjB` — « was published as a spotlight paper at ICLR 2023 ») ; les hôtes des liens (hôte d'un programme de formation : 4 bien notés, 0 apparié ; `verifs-complementaires-dev-v1.json`). La section 4.2 nomme une partie de ces fuites. Elle ne nomme ni la mémoire des codeurs ni les présentations de soi.

**Après** : (a) deux champs par billet, remplis **après** les 25 lignes : `reconnu` (oui / non) et `pari_statut` (bien noté / peu noté / ne sait pas) ; l'analyse rapporte la part de paris justes et rejoue les différences sans les billets reconnus par un codeur au moins (sensibilité, hors règle du gabarit). (b) Les codeurs reçoivent un **extrait** de la grille produit par programme : sections 1, A sans les lignes « Indicateur » et « Analyse », B, 4.5. Ils n'ont besoin ni du plan d'analyse, ni de la règle du gabarit, ni de la liste des billets marqués. (c) Ajouter aux fuites dites d'avance : mémoire des codeurs, titre, présentations de soi, hôtes des liens.

### M5. La procédure de dépôt laisse quatre points ouverts

- **Contrôle avant scellement.** Le contrôle de complétude vit dans `analyser_codage_v1.py`, qui demande les deux codages, l'arbitrage et la table des clés. Un fichier incomplet ne serait donc vu qu'après la seconde passe, quand le codeur n'est plus aveugle. **Après** : un mode de contrôle seul (un fichier, la liste des identifiants neutres), lancé au dépôt, avant scellement et avant la seconde passe ; le même codeur complète.
- **Appui vérifié par programme.** Les codeurs sont des modèles ; la grille vérifie ses propres citations par programme mais pas les leurs. **Après** : au dépôt, chaque appui de 25 mots au plus doit se retrouver dans la copie neutre après la normalisation de la grille ; pour les modalités d'en-tête (thèse, résumé, chiffre, enjeu, figure), avant la borne ; appui vide permis pour les seules modalités d'absence. Permettre deux fragments pour le choix justifié, dont les trois éléments tiennent rarement en 25 mots.
- **Une seule fois.** Rien n'interdit de recommencer le codage avec d'autres codeurs si le résultat déçoit. **Après** : « le codage de la tenue à l'écart a lieu une seule fois, par les deux codeurs nommés avant la préparation des copies ; aucun troisième codage ».
- **Fichier de l'arbitre.** Le script attend un fichier arbitré complet ; la section 4.6 ne dit pas qui l'écrit. **Après** : il est construit par programme (valeur commune en cas d'accord, choix de l'arbitre sinon).

### M6. La phrase sur la puissance est inexacte

**Avant** (section 5.3) : « avec 23 paires, seule une différence d'au moins 0,4 environ a une chance raisonnable de passer ».

**Après** : « avec 23 paires et m = 23, le test ne passe que s'il y a au moins 10 paires dans un sens et aucune dans l'autre (ou 13 contre 1, 16 contre 2, 18 contre 3), soit une différence observée d'au moins 0,43. Un écart vrai de 0,2 passe 2 fois sur 100 ; de 0,3, 7 à 10 fois ; de 0,4, 21 à 29 fois ; de 0,5, 46 à 55 fois ; de 0,6, 75 à 79 fois ; de 0,7, 94 fois. Sur les 11 paires hors des deux marquages, il faudrait 10 ou 11 paires du même côté. » (calcul exact, section 7).

### M7. Deux « gestes » ne sont pas des gestes de rédaction et peuvent devenir consignes

La polarité du résultat principal (G03) et le rapport à un article des auteurs (G08) décrivent le travail, pas la rédaction. Avec le statut « comparée », la règle de la section 8 peut en faire des consignes : « avoir un résultat négatif ou mixte », « avoir un article ». **Avant** : « Analyse : comparée ». **Après** : « Analyse : descriptive (caractère du travail : rapporté avec sa différence, jamais consigne) ». Le code calcule déjà la différence et son intervalle pour les gestes descriptifs. Même question, à trancher, pour le contexte de production nommé (G09), qui mesure surtout qui écrit. Effet : m passe de 23 à 21 ou 20 au plus.

### M8. La règle du gabarit : quatre précisions et un avertissement

- **Ordre des qualificatifs.** Dans le texte, « à éviter » et « consigne sous réserve » se recouvrent (différence négative après correction sur les 23 paires, mais positive ou nulle sur les 11 paires hors marquages). Le code tranche par son ordre. **Après** : écrire l'ordre du code : non fiable ; descriptif ; à éviter ; consigne distinctive ; consigne ; consigne sous réserve ; piste ; **aucune consigne** (catégorie restante, aujourd'hui sans nom dans le texte).
- **Ensemble de la correction.** Écrire que « après correction de Holm » se lit sur les 23 paires (c'est ce que fait le code).
- **Sous réserve.** La règle donne « consigne sous réserve » à un geste **moins** fréquent chez les bien notés sur les 23 paires dès qu'il ne l'est pas sur les 11 paires hors marquages : 12 à 14 fois sur 100 pour un geste sans aucune différence vraie. **Après** (proposé) : « sous réserve » seulement si la différence est positive ou nulle sur les 23 paires et négative sur les 11.
- **Libellé de la consigne.** La règle dit quels gestes passent, pas ce que la consigne dira. Pour un indicateur à deux modalités, le libellé est un choix après coup. **Après** : une ligne « Consigne si retenue » par geste, écrite avant le codage.
- **Avertissement à écrire dans le gabarit.** Simulation de la règle (200 000 tirages, fiabilité supposée acquise, `puissance-contre-lecture-v1.json`, `0b4d2dd8…`) : un geste aussi fréquent des deux côtés (60 à 90 %) reçoit « consigne » 43 à 51 fois sur 100 et « consigne sous réserve » 22 à 25 fois sur 100. Un geste vraiment moins fréquent de 0,2 chez les bien notés reçoit encore l'un des deux 18 à 23 fois sur 100, et « à éviter » 2 fois sur 100. La consigne simple dit donc « pratique majoritaire chez les bien notés, non contredite ». Elle ne dit pas que le geste distingue les bien notés. L'essai sur codages tirés au hasard le montre déjà : 6 consignes et 2 sous réserve sur 21.

### M9. Objections : le code et le texte divergent ; trois règles manquent

- La section 5.1 dit « chaque résultat est rapporté sur quatre ensembles ». Le code n'analyse les objections que sur l'ensemble entier. **Après** : quatre ensembles, ou le dire.
- Le contrôle « l'arbitre choisit une des deux classes » existe pour les gestes, pas pour les objections. L'ensemble des commentaires codables est défini par le fichier de l'arbitre lui-même. **Après** : même contrôle ; ensemble codable lu dans le manifeste de préparation.
- « Objection à prévenir » n'exclut que la classe hors typologie. La réplication par le lecteur (O12) et l'éloge argumenté, rangé avec la critique dans la forme et présentation (O10), ne sont pas des objections. **Après** : exclure O12 ; séparer l'éloge de la critique dans O10 (deux classes, ou l'éloge argumenté rangé à part comme signal favorable).
- **Réponses dans un fil.** En développement, 63 commentaires codables sur 216 répondent à un autre commentaire, dont 18 à un parent non retenu (`decomptes-complementaires-v1.json`). La grille ne dit pas quoi faire d'un lecteur qui défend le billet (`v7f8ayBxLhmMFRzpa/5H64rdESFnCDZ3yez` — « The finetuning worked fine for just getting the model to answer which of A/B is more/less sycophantic. ») ou qui poursuit sa propre remarque. **Après** : « une réponse se code par l'objection qu'elle énonce elle-même ; si elle défend, précise ou poursuit sans objection nouvelle : hors typologie ; incompréhensible sans un parent non retenu : hors typologie, doute coché ».
- **Base de comparaison jugée faible ou injuste.** Objection courante dans ce genre, vue une fois dans mon essai, sans place écrite (`v7f8ayBxLhmMFRzpa/AP72BpS9CQuYCbjs3` — « Hmm, yeah, that seems like a quite unfair comparison. »). J'ai hésité entre l'explication concurrente, le cadrage et l'expérience suivante. **Après** : cas limite de l'explication concurrente (O1) : « base de comparaison jugée faible, injuste ou mal réglée → O1 ».
- **Technique connue proposée** (`v7f8ayBxLhmMFRzpa/mfixbQMzhJSNfe9XZ` — « I think DPO on contrast pairs seems like a pretty natural approach. ») : travaux voisins (O4) ou expérience suivante (O9) ? L'ordre de priorité donne O4 ; le dire en cas limite.
- **Limite à écrire.** Avec une seule classe par commentaire et un ordre de priorité, un long commentaire à plusieurs points tombe dans la première classe de l'ordre. Les parts des classes basses de l'ordre (travaux voisins, demande de précision, expérience suivante, forme) sont sous-estimées.

### M10. Un décompte faux ; une limite mesurable à ajouter

- **Avant** (section 5.1) : « 18 billets (…), dont 12 bien notés, 6 appariés ». Le manifeste et la section 6 de la grille donnent **13 bien notés et 5 appariés** (dont 3 bien notés sans apparié ; `decomptes-complementaires-v1.json`). Le code est juste (26 bien notés hors marquage 1 = 39 − 13). **Après** : « dont 13 bien notés (3 sans apparié) et 5 appariés ».
- **Section 5.5.** Deux écarts de population, lisibles dans le manifeste, méritent d'être écrits : publication aussi sur le forum voisin du site (champ `alignment_forum`) : 28 bien notés sur 36 contre 3 appariés sur 22 en développement, 27 sur 39 contre 1 sur 23 dans la tenue à l'écart ; nombre moyen d'auteurs : 3,6 contre 1,4 en développement, 3,1 contre 1,4 dans la tenue à l'écart (`decomptes-complementaires-v1.json`). La comparaison oppose surtout des équipes installées à des auteurs seuls. Toute différence de geste se lit d'abord ainsi.

## 4. Mineurs

- **m1.** L'essai scellé du plan d'analyse cite une grille d'empreinte `b00d5dca…`, qui n'est pas la grille scellée. Rejoué sur la grille scellée : même sortie. À rejouer et resceller sur la grille gelée.
- **m2.** Le cas d'école de la priorité des objections n'est pas au format que le script vérifie. Le mettre au format (`identifiant/commentaire` — « … »).
- **m3.** Déclaration d'usage d'une intelligence artificielle (G24) : la grille dit « un seul cas trouvé » en développement. J'en trouve deux : celui de la grille et `S9xyqRAziRMCcJQmz` — « alongside with some paraphrasing support. ». Ajouter le cas limite : code écrit par un modèle → `aucune` (`LQBFqyXA5to4iHEBC` — « A lot of the code is written by ChatGPT or Claude ») ; schémas produits par un modèle → à trancher.
- **m4.** Le manifeste de la tenue à l'écart contient un nom d'auteur nul. Le test « nom du commentateur dans les noms des auteurs » marquerait alors « réponse d'auteur » tout commentaire d'un compte supprimé sur ce billet. Retirer les valeurs nulles de l'ensemble.
- **m5.** La garde du script vérifie la forme de l'identifiant d'accord, pas son existence dans le registre. Le dire dans la grille : c'est une barrière contre l'erreur, pas contre l'intention.
- **m6.** Modalités décisives sans exemple : `dispersées` pour les limites (G17), qui entre dans l'indicateur ; `plus-loin` pour la place de la thèse (G02). Exemple possible de `dispersées` : `v7f8ayBxLhmMFRzpa` — « Before concluding superadditivity in general, remember that this is just one datapoint ».
- **m7.** Priorités non écrites : figure de résultat et autre figure toutes deux en tête (G11 ; proposer « figure de résultat prime ») ; bloc étiqueté et liste (G04) ; chiffre avec et sans comparaison (G05).
- **m8.** Section 1 : dire une fois pour toutes que les notes de bas de page et les annexes comptent, sauf pour les questions d'en-tête, et qu'un renvoi à l'article ne remplace jamais le texte (dit pour le dispositif seulement).
- **m9.** Résumé en tête (G04) : dans `sTe78dNJDGywu9Dz6`, l'intertitre « Summary of our solution (TL,DR) » arrive juste après la borne ; le billet est codé `aucun`. La règle est claire et le cas est rare (en développement, 2 billets sur 58 ont leur première étiquette de résumé entre le 250e et le 500e jeton, dont celui-ci seul change de modalité ; `verifs-complementaires-dev-v1.json`) ; le gabarit devra dire « résumé dans les 250 premiers mots », pas « résumé en tête ».
- **m10.** Images : 53 images sur 712 ont un texte de remplacement ; 47 billets à images sur 57 n'en ont aucun. La figure de résultat en tête mesure donc « figure légendée » ; le dire dans son nom.
- **m11.** Hors périmètre, pour mémoire : le manifeste consigne numpy 2.5.3 pour le partage ; l'environnement du dépôt a numpy 2.4.6.

## 5. Mon essai de la grille sur six billets de développement

### 5.1 Tirage

Graine écrite avant le tirage (2026-11-18, 18:51 UTC) : `numpy.random.SeedSequence(119271480372058747686740415618928751187)`, `default_rng`, identifiants de développement hors des deux billets marqués, triés (56), `choice(56, size=6, replace=False)`, numpy 2.4.6. Tirés, dans l'ordre : A `sTe78dNJDGywu9Dz6` (bien noté, 2023), B `69fachkoAs2ZHeSst` (apparié, 2026), C `S9xyqRAziRMCcJQmz` (apparié, 2026), D `v7f8ayBxLhmMFRzpa` (bien noté, 2024), E `rbqJoxFZtae9x93mx` (bien noté, 2026), F `bWxNPMy5MhPnQTzKz` (bien noté, 2023). Lecture intégrale des copies neutres produites par le script. Codage complet : `pieces-contre-lecture-grille-v1/essai-six-billets-v1.json` (`61837126…`), accepté par le contrôle de forme du script d'analyse.

Limites de l'essai : un seul lecteur, donc des hésitations et non un accord mesuré ; je connaissais le statut des billets ; les six billets sont tous cités en exemple dans la grille (40 billets de développement sur 58 le sont), ce qui rend l'essai plus facile que le codage réel.

### 5.2 Codage (« ? » : doute qui peut changer l'indicateur)

| Geste | A | B | C | D | E | F | Doutes |
|---|---|---|---|---|---|---|---|
| Forme du titre (G01) | sans-résultat ? | affirmation-atténuée | affirmation | sans-résultat | sans-résultat | sans-résultat | 1 |
| Place de la thèse (G02) | premier-paragraphe ? | premier-paragraphe | premier-paragraphe | en-tête | premier-paragraphe | en-tête | 1 |
| Polarité du résultat principal (G03) | positif | négatif-ou-nul | négatif-ou-nul | positif | positif | mixte | 0 |
| Résumé en tête (G04) | aucun | aucun ? | bloc-étiqueté | bloc-étiqueté | aucun | liste-non-étiquetée | 1 |
| Chiffre de résultat en tête (G05) | aucun | aucun | seul | aucun | avec-comparaison | seul | 0 |
| Statut épistémique déclaré (G06) | absent | absent | absent | absent | absent | absent ? | 1 |
| Caractère préliminaire annoncé (G07) | annoncé ? | annoncé | non-dit ? | non-dit | non-dit ? | non-dit | 3 |
| Rapport à un article des auteurs (G08) | aucun-article | aucun-article | aucun-article | présente-l-article | complète-l-article ? | aucun-article | 1 |
| Contexte de production nommé (G09) | programme-de-formation | programme-de-formation ? | aucun | programme-de-formation | programme-de-formation | aucun | 1 |
| Enjeu de sûreté explicite (G10) | absent | en-tête | en-tête ? | plus-loin ? | absent | en-tête ? | 3 |
| Figure de résultat en tête (G11) | autre-figure | aucune | aucune | figure-de-résultat | figure-de-résultat | aucune | 0 |
| Base de comparaison du résultat principal (G12) | base-nommée ? | base-nommée | base-nommée | base-nommée | base-nommée | base-nommée | 1 |
| Choix justifié contre une option écartée (G13) | présent | absent ? | présent | absent ? | présent ? | présent ? | 4 |
| Dispositif nommé (G14) | trois-éléments ? | trois-éléments | trois-éléments | moins-de-trois ? | moins-de-trois | trois-éléments | 2 |
| Incertitude statistique (G15) | aucune | intervalles-ou-barres | test-statistique | intervalles-ou-barres | aucune | aucune | 0 |
| Non-revendications (G16) | absentes | phrase | section | phrase | absentes ? | phrase | 1 |
| Limites (G17) | absentes ? | section | section | dispersées | dispersées | dispersées ? | 2 |
| Impasses rapportées (G18) | mentionnées | mentionnées ? | absentes ? | mentionnées | mentionnées | absentes | 2 |
| Explication concurrente anticipée (G19) | aucune | posée-et-contrôlée ? | posée-et-contrôlée | posée-et-contrôlée ? | posée-sans-contrôle | posée-et-contrôlée | 2 |
| Appel à poursuivre (G20) | absente | suite-des-auteurs-seule ? | absente ? | appel-aux-autres | appel-aux-autres | appel-aux-autres | 2 |
| Code, modèles et données des auteurs (G21) | lien | lien | lien | lien | lien | lien | 0 |
| Note d'édition visible (G22) | mise-à-jour | aucune | aucune | aucune | aucune | aucune | 0 |
| Analogie pour le non-spécialiste (G23) | absente ? | absente | absente ? | absente | présente ? | absente | 3 |
| Déclaration d'usage d'une intelligence artificielle dans l'écriture (G24) | aucune | aucune | déclarée | aucune | aucune | aucune | 0 |
| Appel aux retours (G25) | non | non | oui | non | oui ? | non | 1 |

Bilan : 32 doutes sur 150 décisions. Sans doute : polarité, chiffre en tête, figure en tête, incertitude statistique, code et données, note d'édition, déclaration d'usage d'un modèle. Pour la polarité, la place de la thèse et le chiffre en tête, j'ai aussi hésité entre deux modalités qui ont le même indicateur : sans effet sur l'analyse, ce qui montre que le choix des indicateurs est bon.

### 5.3 Où j'ai hésité, geste par geste, et le cas limite à écrire

- **Forme du titre (G01).** A : titre au gérondif qui suggère une réussite (« Solving … »). Le contre-exemple de la grille range un autre gérondif en `sans-résultat`. F : interrogative indirecte sans point d'interrogation (`question` ou `sans-résultat`, même indicateur). À écrire : « gérondif ou groupe nominal d'action → `sans-résultat`, même si le verbe suggère une réussite ; interrogative indirecte → `sans-résultat` ».
- **Place de la thèse (G02).** A : le premier paragraphe annonce une réussite sans dire son contenu ; le contenu vient après la borne. À écrire : l'annonce d'une réussite compte-t-elle comme énoncé du résultat ? Je propose oui. C et D : qu'est-ce que le premier paragraphe quand le corps s'ouvre sur une liste ou sur une image légendée ? Sans effet sur l'indicateur. À écrire : « une liste entière est un bloc ; une légende n'est pas un paragraphe ».
- **Résumé en tête (G04).** B : le billet s'ouvre sur un paragraphe de résumé en italique, sans étiquette ni liste. La lettre donne `aucun`. Un codeur sera tenté. À écrire : « paragraphe de résumé sans étiquette ni liste → `aucun` (la thèse relève de G02) ».
- **Chiffre de résultat en tête (G05).** C : un multiple (`S9xyqRAziRMCcJQmz` — « Within-family activations are much stronger (4~9x) ») est-il `seul` ou `avec-comparaison` ? Même indicateur. À écrire.
- **Statut épistémique (G06).** F : `bWxNPMy5MhPnQTzKz` — « Interpretation (speculative): ». « Étiquette équivalente » n'est pas défini, et la grille dit qu'une étiquette au milieu d'une section compte. À écrire : liste fermée des étiquettes ; une mention locale qui qualifie un seul passage ne compte pas.
- **Caractère préliminaire (G07).** A : le travail vient d'un hackathon (`sTe78dNJDGywu9Dz6` — « We spent the last Alignment Jam hackathon attempting to solve the two challenges presented there »), mais le billet se dit version finale d'une solution confirmée. La règle (liste : « en hackathon ») et la question se contredisent ; le hackathon compte déjà dans le contexte de production (G09). C : aveu d'inexpérience de l'auteur, qui ne qualifie pas le travail. E : `rbqJoxFZtae9x93mx` — « We haven't yet verified how well these improvements transfer to LLM SAEs ». À écrire : retirer « en hackathon » de la liste, sauf lien explicite à la hâte ; aveu d'inexpérience → `non-dit` ; étape de validation non faite → limite, `non-dit`.
- **Rapport à un article (G08).** E : l'article des auteurs sert d'outil (`rbqJoxFZtae9x93mx` — « In the paper, we found that the best SAE architecture we tested »). Suite de l'article ou billet sans article ? À écrire : « article antérieur des auteurs employé comme outil ou point de départ → `aucun-article`, sauf si le billet se présente comme sa suite ».
- **Contexte de production (G09).** B : travail fait comme candidature à un programme (`69fachkoAs2ZHeSst` — « This was originally produced as part of application to Neel Nanda's MATS research stream »). À écrire.
- **Enjeu de sûreté (G10).** Le plus incertain après le choix justifié. C : `S9xyqRAziRMCcJQmz` — « Not enough for fine grained auditing tools. » suffit-il ? La phrase qui dit l'enjeu commence avant la borne et finit après. D : l'en-tête liste des comportements (complaisance, recherche de pouvoir) sans phrase de lien ; l'enjeu vient plus loin. F : `bWxNPMy5MhPnQTzKz` — « It might be a stepping stone towards recovering superhuman beliefs of AI systems » : usage de sûreté pour qui connaît le domaine, sans mot de risque. À écrire : une liste fermée de mots d'usage ou de risque ; « une liste de comportements étudiés ne suffit pas » ; la convention de l'énoncé coupé par la borne (M2).
- **Base de comparaison (G12).** A : le résultat est un mécanisme, pas un score ; les comparaisons sont un plafond et des ablations. La règle range l'ablation et la condition de contrôle dans `base-nommée` : mes six billets y tombent. Le geste risque d'être quasi universel et de ne rien séparer. À trancher par le réviseur : séparer la base externe (méthode concurrente, base naïve nommée, résultat antérieur rejoué) du contrôle interne (ablation, condition de contrôle, plafond).
- **Choix justifié contre une option écartée (G13).** Quatre doutes sur six. Les trois éléments sont presque toujours dispersés (B : `69fachkoAs2ZHeSst` — « I selected a Qwen-family judge partly because Qwen’s J-space readouts contained Chinese and tokenizer-specific fragments », l'option écartée n'est nommée que plus loin). E : le choix justifié est le résultat lui-même. F : c'est une recommandation aux autres. À écrire : « les trois éléments dans la même phrase ou deux phrases voisines ; option écartée nommée en toutes lettres ; un choix qui est le résultat, ou une recommandation à autrui, ne compte pas ». Sans cela, je ne crois pas ce geste fiable.
- **Dispositif nommé (G14).** A : une taille de jeu de données vaut-elle effectif ? D : quantité vague (`v7f8ayBxLhmMFRzpa` — « with the average taken over dozens of these dataset contrast pairs »). À écrire : « taille du jeu de données : oui si la mesure porte dessus ; quantité vague : non ».
- **Non-revendications (G16) et limites (G17).** La frontière tient à la tournure : « nous n'avons pas vérifié » est une limite, « nous ne prétendons pas » une non-revendication, pour la même information (E). A : part non expliquée présentée comme une force (`sTe78dNJDGywu9Dz6` — « showing ~6% of model behavior is not compatible with our hypothesis ») : limite ou rien ? F : une restriction de portée entre parenthèses. À écrire : « part non expliquée chiffrée → limite `dispersées` » ; un exemple de `dispersées` (m6).
- **Impasses (G18).** B et C : dans un billet à résultat négatif, tout « n'a pas marché ». À écrire : « ne compter que les tentatives distinctes de celles qui font le résultat principal ; une expérience non menée faute de moyens est une limite ».
- **Explication concurrente (G19).** B, D, et A à un moindre degré : la frontière entre « contrôle prévu dès le dispositif » (`aucune`) et « objection posée puis contrôlée » est mince, et l'indicateur en dépend. À écrire : « il faut une phrase qui nomme une autre cause possible du résultat, et une expérience des auteurs qui lui répond, dans n'importe quel ordre ».
- **Appel à poursuivre (G20).** B : liste de travaux futurs à l'impératif, annoncée comme le plan de l'auteur. C : `S9xyqRAziRMCcJQmz` — « Whether this holds at larger scales remains an open question. » : question ouverte, mais adressée à personne. À écrire : « question ouverte impersonnelle isolée → `absente` ; liste de travaux sans sujet « nous » ni annonce de plan → `appel-aux-autres` ».
- **Analogie (G23).** A, C : métaphores mortes et expressions figées. E : `rbqJoxFZtae9x93mx` — « Overall this feels like having a really fast and extremely smart masters student » : comparaison explicite, mais elle décrit une expérience de travail, pas un mécanisme. À écrire : « expressions figées : non ; l'analogie doit éclairer un mécanisme ou un résultat ».
- **Appel aux retours (G25).** E : `rbqJoxFZtae9x93mx` — « I'd be curious to hear any ideas on this from others in the community too! » : appel à poursuivre ou appel aux retours ? À écrire : « demande d'idées pour la suite → G20 ; G25 exige critique, correction ou retour sur le billet ».
- **Recherche dans le texte.** L'incertitude statistique, les non-revendications et le lien vers le code tiennent parfois à une seule phrase courte dans 3 000 mots (D : `v7f8ayBxLhmMFRzpa` — « The bars show variance. »). Le risque est l'oubli, pas le désaccord de lecture ; l'appui vérifié (M5) ne le couvre pas pour les modalités d'absence.

### 5.4 Objections (commentaires des quatre billets bien notés de l'essai)

J'ai parcouru les 31 commentaires neutres de A, D, E et F (19 codables, 12 réponses d'auteur marquées par le script) ; les plus longs n'ont été lus que sur leurs 150 à 250 premiers mots. Classes nettes : hors typologie, demande de précision (exemple de la grille), expérience suivante, réplication par le lecteur (exemple de la grille), travaux voisins. J'ai hésité sur environ la moitié des commentaires codables, pour quatre raisons : réponses dans un fil ; base de comparaison jugée injuste ; technique connue proposée ; désaccord sur l'interprétation, à cheval sur la validité de la mesure (O2), l'exactitude (O3) et le cadrage (O5). Les trois premières ont une correction proposée en M9. Pour la quatrième, à écrire : « conteste ce que la mesure saisit → O2 ; conteste un calcul ou une définition → O3 ; ne conteste ni l'un ni l'autre mais la conclusion tirée → O5 ».

## 6. Aveugle des codeurs : réponse aux questions du mandat

- **Score, votes, nombre de commentaires, étiquettes, adresse, identifiant** : cachés. Vérifié sur 58 copies.
- **Date** : absente des métadonnées ; visible dans le texte (dates de notes, noms de modèles). Sans effet sur la comparaison, les paires étant de la même année.
- **Auteurs** : cachés en partie seulement (M3).
- **Statut** : non écrit, mais devinable par le dossier des commentaires (B2), par les noms et la mémoire des codeurs (M3, M4), par les présentations de soi et les notes d'édition.
- **Longueur, nombre d'images** : signal faible (aires sous la courbe 0,53 à 0,59 pour la longueur, 0,56 pour les images).
- **Ordre « gestes d'abord, objections ensuite »** : suffisant à trois conditions, aujourd'hui non garanties : les fichiers de la seconde passe n'existent pas avant le scellement de la première (B2) ; la complétude de la première passe est contrôlée avant son scellement (M5) ; l'arbitre des gestes ne voit jamais la seconde passe.
- **Refus sur la tenue à l'écart** : tient (section 1).

## 7. Plan d'analyse : ce que 23 paires permettent

Le plan est complet et le code le suit : accord brut et kappa de Cohen sur les modalités puis sur l'indicateur, intervalle par rééchantillonnage des billets ; seuil 0,60 sur 62 billets et sur les 44 hors marquage 1 ; différence appariée, intervalle par rééchantillonnage des paires, test du signe exact, correction de Holm sur les gestes fiables d'analyse comparée ; graines par `SeedSequence`, enfants par ensemble puis par geste ; quatre ensembles. Les écarts trouvés sont B1, M6, M8, M9.

**Puissance** (calcul exact pour le test du signe au premier pas de la correction de Holm, paires supposées indépendantes ; `puissance_contre_lecture_v1.py`, `3ae2bd61…`, sortie `0b4d2dd8…`, graine consignée dans la sortie).

| Fréquence chez les appariés → chez les bien notés | Écart vrai | Probabilité de passer, m = 23 | m = 10 | Sans correction (m = 1) |
|---|---|---|---|---|
| 0,40 → 0,60 | 0,2 | 0,02 | 0,03 | 0,17 |
| 0,35 → 0,65 | 0,3 | 0,07 | 0,12 | 0,40 |
| 0,10 → 0,40 | 0,3 | 0,10 | 0,17 | 0,52 |
| 0,30 → 0,70 | 0,4 | 0,21 | 0,30 | 0,68 |
| 0,10 → 0,50 | 0,4 | 0,29 | 0,39 | 0,78 |
| 0,25 → 0,75 | 0,5 | 0,46 | 0,59 | 0,89 |
| 0,10 → 0,60 | 0,5 | 0,55 | 0,66 | 0,93 |
| 0,20 → 0,80 | 0,6 | 0,75 | 0,85 | 0,98 |
| 0,10 → 0,70 | 0,6 | 0,79 | 0,88 | 0,99 |
| 0,15 → 0,85 | 0,7 | 0,94 | 0,97 | 1,00 |

**En clair.** Détectable : un geste présent chez quatre bien notés sur cinq et un apparié sur cinq, ou plus tranché. Il faut un écart vrai d'environ 0,5 pour une chance sur deux et d'environ 0,6 pour quatre chances sur cinq. Non détectable : un écart vrai de 0,3 ou moins (moins d'une chance sur dix), qui serait pourtant un écart important pour un geste de rédaction. Un écart de 0,4 passe une fois sur quatre ou cinq. Sur les 11 paires hors des deux marquages, rien ne peut passer sauf 10 ou 11 paires du même côté ; cet ensemble ne sert qu'à vérifier le signe.

**Fiabilité, même prudence.** Avec 62 billets, le kappa estimé est incertain de 0,2 environ. Simulation de la règle (50 000 tirages) : un geste de kappa vrai 0,7 est déclaré fiable 60 à 76 fois sur 100 ; de kappa vrai 0,6, 37 à 40 fois ; de kappa vrai 0,5, 13 à 17 fois ; de kappa vrai 0,4, 2 à 6 fois, mais **66 fois sur 100 à prévalence 0,93** (B1). La liste des gestes fiables aura donc une part de hasard ; l'intervalle du kappa doit accompagner chaque consigne.

## 8. Règle de passage au gabarit : réponse au mandat

Le passage du geste à la consigne est décidé par une règle écrite et mise en code avant le codage. Il reste quatre choix après coup : le libellé de la consigne, l'ordre des qualificatifs dans le texte, l'ensemble sur lequel se lit la correction, la catégorie restante (M8), plus l'échappatoire de la prévalence (B1). Les qualificatifs sont sans recouvrement **dans le code** ; dans le texte, « à éviter » et « sous réserve » se recouvrent sur un cas. « Piste » est bien défini et ne recouvre rien. Un cas de bord à connaître : un geste distinctif après correction mais présent chez moins de la moitié des bien notés n'est que « piste » ; c'est un choix de la règle, à assumer en clair.

## 9. Avis sur les points à trancher du réviseur

1. **Deux codeurs de deux modèles différents et un arbitre** : d'accord. Deux agents du même modèle partagent leurs lectures ; leur accord surestimerait la fiabilité. Si le programme le permet, un des deux d'une autre lignée que celle du réviseur ; cela relève d'une décision du directeur. Arbitre : agent neuf, autre que les deux codeurs, qui ne voit jamais le statut. En complément utile et peu coûteux : le directeur code lui-même, en aveugle, une dizaine de copies tirées par graine ; son accord avec le codage arbitré est rapporté. Confiance : bonne.
2. **Images invisibles** : accepter pour ce tour. Télécharger les images sortirait du mandat, ouvrirait le réseau et remettrait des adresses du site dans les copies. Mais le dire dans les noms et les limites : 7 % des images de développement ont un texte de remplacement ; la figure en tête, la base de comparaison et l'incertitude sont mesurées sur le texte seul et donc sous-estimées. Garder les décomptes d'images et de tableaux par programme. Confiance : bonne.
3. **Seuil de 0,60** : garder 0,60. Avec 62 billets, l'incertitude du kappa (0,2 environ) pèse plus que l'écart entre 0,60 et 0,70. Un geste dont le kappa vrai vaut juste le seuil passe moins d'une fois sur deux (37 à 40 fois sur 100 au seuil de 0,60, section 7) ; à 0,70, ce sort toucherait les gestes de kappa vrai 0,7, qui sont de bons gestes. Deux conditions : corriger l'exception de prévalence (B1) ; publier l'intervalle avec chaque consigne. Confiance : moyenne à bonne.
4. **Classes nouvelles et fusions** : confirmer la demande de précision ou de matériel (O11) : nette, fréquente, utile au gabarit. Confirmer la réplication par le lecteur (O12) comme classe, mais hors des « objections à prévenir » : c'est un signal favorable. Confirmer la fusion des explications concurrentes (O1), avec le cas limite de la base de comparaison jugée faible. Confirmer la fusion de l'exactitude (O3), avec la règle de partage entre O2, O3 et O5 (section 5.4). Ajouter : la règle des réponses dans un fil ; la séparation de l'éloge et de la critique dans la forme (O10). Confiance : moyenne (essai sur 19 commentaires).
5. **Gel** : après correction de B1 et B2 dans le texte et le code, des majeurs, et, de préférence, après l'essai à deux codeurs sur le développement (M1).

## 10. Limites de cette contre-lecture, lectures, pièces

**Limites.** Un seul contre-lecteur, d'un modèle de la même lignée que le réviseur. Essai sur six billets, non aveugle, sans second codeur ; essai des objections sur 19 commentaires, dont les plus longs lus en partie. Le calcul de puissance suppose des paires indépendantes et un seul geste vraiment différent. Je n'ai lu ni la grille v1, ni le rapport du corpus v2, ni aucun texte de la tenue à l'écart ; je ne peux donc rien dire de formes de texte propres à cette moitié (balises, noms courts) que le script traiterait mal.

**Lu, dans le mandat.** Le mandat ; la grille brouillon 2 ; ses huit pièces ; le mandat du réviseur ; la règle de tri v2 ; le manifeste v2 (par programme : structure, moitiés, classes, et pour la tenue à l'écart des **métadonnées seulement** : décomptes, noms affichés courts, champ du forum voisin, longueurs ; un titre de la tenue à l'écart s'est affiché lors d'une recherche de mot dans les titres) ; le rapport du second lecteur ; la liste des billets marqués ; la moitié développement (58 textes et 36 fichiers de commentaires par programme ; six billets lus en entier ; les commentaires de quatre billets parcourus, les plus longs sur leur début seulement).

**Lu ou touché hors de la liste du mandat.** Les consignes permanentes du dépôt (`CLAUDE.md`, fournies d'office). La liste des noms de fichiers de `docs/notes/billets-v1/`. Par le rejeu du script de vérification des citations : l'empreinte du manifeste v1 et les identifiants cités par la grille v1 (ni l'un ni l'autre ouvert par moi). La liste des noms et des dates du bac temporaire partagé de la session, et de deux de ses sous-dossiers sans rapport avec ce travail (aucun fichier ouvert). Une sortie de `git status --short`, qui a montré le nom d'un fichier non suivi sous `prereg/` (non ouvert). Rien sous `diag/`, `runs/`, `donnees/`, `docs/verdicts/`, `registres/`.

**Disque.** Copies neutres de développement écrites dans le bac temporaire de la session puis supprimées avec tout mon dossier de travail. Aucun texte de billet dans le dépôt ; les citations de ce rapport font 25 mots au plus et sont vérifiées par programme contre les textes de développement.

**Pièces déposées** sous `docs/notes/billets-v1/pieces-contre-lecture-grille-v1/`, chacune avec son compagnon `.sha256` ; aucune ne contient de texte de billet.

| Pièce | Empreinte |
|---|---|
| `puissance_contre_lecture_v1.py` | `3ae2bd61ae17e482ed7a7563336444489a4a792ba450d181d2de97d6fcb6d3b1` |
| `puissance-contre-lecture-v1.json` | `0b4d2dd8582cd612f9d1ea4816aa9e671d7cc3a9af5072159f36211f9c8d8eee` |
| `fuites_copies_neutres_dev_v1.py` | `24b9a1ee4352a79c4300c9acf1b9ba78b00e44b7323384398f9339be591d26bf` |
| `fuites-copies-neutres-dev-v1.json` | `0f88d03a9732bdf95579e2889b6b0bf2a4a64837348e2d7379711370efe00f58` |
| `verifs_complementaires_dev_v1.py` | `d3ad174b1c132f81fadfae7f31236047dbd0e1cc1d23880999a700d41f5bb35e` |
| `verifs-complementaires-dev-v1.json` | `017ce1c5f9863ee757c5276ff99d5eb4af7117599258c06a1c14081c68690222` |
| `essai-six-billets-v1.json` | `6183712678faef1e3a5d4e943cf26d893e281362a398ff9e56b6d61c810a3f4e` |
| `decomptes_complementaires_v1.py` | `6905a1f2a3f6571b64036b4776802768c63dfbfbb9d1ed6f3b58fe8760bef754` |
| `decomptes-complementaires-v1.json` | `a0cb34941eb70eaba3d1d89f4e926e2dd943c4a4444c2c630d427ee31063c137` |

Les trois scripts qui lisent les copies prennent en argument un dossier qui contient `copies-dev/`, sortie de `preparer_copies_neutres_v1.py` sur la moitié développement. Graines : tirage des six billets, `119271480372058747686740415618928751187` ; simulations, `271828182845904523536028747135266249775` (`SeedSequence`, enfants par `spawn`).
