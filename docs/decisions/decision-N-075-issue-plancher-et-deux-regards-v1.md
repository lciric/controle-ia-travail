# Décision — N-075 : mesurer l'issue et corriger ; un plancher d'audit au hasard contre le sabotage diffus ; deux regards tels qu'échapper à l'un expose à l'autre ; alerte à deux clés ; bilan du produit contre le jumeau honnête ; recherche du passage obligé de tout sabotage ; lemme d'additivité restreint à sa forme valide à tout instant (v1)

- **Décision de Lazar** : mots directs dans la session mère `session_01QPDgKgejkqwnuaJHJ31Ydo`, 21 novembre 2026, vers 12:45 UTC, consignés à la ligne `GO-2026-11-21-51` de `registres/go.md` (`e0194c1c…` à ma lecture) ; pour le lemme d'additivité, mots du même jour vers 12:00 UTC, ligne `GO-2026-11-21-47`, point 4. Mots recopiés en section 0.
- **Statut : v1, à contre-lire.** Écrite le 21 novembre 2026 entre 12:50 et 13:02 UTC (`date -u`) par Claude Fable 5.2 (`claude-fable-5-2`), concepteur (R-3735), sur mandat de la session mère ; dépôt à `1e6a36d33`. À contre-lire par Opus 5.5, puis corrections vérifiées par le même contre-lecteur. Aucun appel payant, ni commit ni poussée. La ligne de `CLAUDE.md` (section 12) est **proposée** : la mère l'inscrit après la contre-lecture.
- **Numéro.** Le mandat nommait N-074. Ce numéro est pris : `docs/decisions/decision-N-074-v1-brouillon1.md` et `-brouillon2.md` (« un contraste à témoin apparié est ajouté au critère de la porte de fin de phase 1 », brouillons non retenus, gardés, R12) et sept lignes de `registres/decisions.md` le portent. Aucun fichier suivi du dépôt ne porte N-075 (recherche du 21 novembre, hors dossiers interdits par le mandat) : premier numéro libre. La vérification finale revient à la mère.
- **Sources de la décision** : la note du concepteur sur le mécanisme adjudant, `docs/notes/mecanisme-adjudant-hors-distribution-v1/reponse-fable-mecanisme-adjudant-v1.md` (`896cec0e0be58f5a5765c9558524845073245d07c37e82a22eb8abbf2e997128`), § 1, § 3.2 à 3.5, § 6, § 8 ; la note du concepteur sur la pince, `docs/notes/pince-hors-distribution-v1/reponse-fable-pince-hors-distribution-v1.md` (`c0318d1f95e932f67938102164156fd375c124921156a9884c1a3035b073cbfc`). Les deux sont des pièces de travail **non contre-lues** à l'heure où j'écris ; la contre-lecture de la première par Opus 5.5 est commandée par le même GO (point 8).
- **Portée.** Cette note fixe la lecture du programme v2 (`docs/programme-controle-ia-v2.md`, `2fd63badb5afea48f48d3ca501ae3b027c4094a8b176508488a41a22e45aa18c`) à compter de son scellement après contre-lecture, en attendant une version nouvelle. Elle ne modifie pas le fichier du programme ; le texte à y reporter est en section 10. **Elle ne change le critère d'aucune porte, ne retire aucune hypothèse, n'ouvre aucune dépense.** Elle resserre une revendication (le lemme d'additivité, section 7) et n'en déclare aucune « libre ».
- **Règle de lecture.** « Non trouvé » veut dire « non trouvé dans les pièces lues » (R8), jamais « libre ». Par le point D-7 de la note sur l'adjudant, accordé à `GO-2026-11-21-46` et précisé à `GO-2026-11-21-51` (point 7), **aucune phrase de revendication ne sort du dépôt sur les cinq points avant le verdict d'antériorité du lecteur des sept voisins** (Opus 5.5, lecture en entier). Sous « ce qui est revendiqué », cette note dit donc ce qui *pourrait* l'être, dans quelle forme, et à quelle condition.
- **Marques** : [PDF, p.] = page lue sur le PDF empreinté par l'auteur de la note source, reprise ici sans relecture de ma part dans cette session ; [de mémoire] et [page web] = non opposables (R7) ; [calcul, X] = bloc X des sorties `calculs-mecanisme-adjudant-v1.txt` (`aaa3e763…`) ou `calculs-pince-hors-distribution-v1.txt` (`e0badff0…`), lois exactes sous **suppositions d'illustration**, non contre-lus, aucune donnée du programme.

## 0. Mots de Lazar, verbatim

Ligne `GO-2026-11-21-51` (21 novembre 2026, vers 12:45 UTC) :

> go il faut l'inscrire dans le programme et l'amender en consequence

> Ce qui vaut : deux regards tels qu'échapper à l'un expose à l'autre. : go

> non pas borne a cette zone , go

> b mais phase exploratoire avec a d'abord

Lecture de la mère, consignée à la même ligne (extrait du point 1) : « le levier fort est de mesurer l'issue et de corriger, ce qui rend possible un plancher d'audit au hasard contre le sabotage diffus ; deux regards tels qu'échapper à l'un expose à l'autre ; alerte = nouveauté et preuve de dommage ensemble, nouveauté seule = mise à jour des témoins (sources revérifiées sur PDF) ; bilan du produit fermé contre le jumeau honnête ; recherche de ce que tout sabotage délibéré doit calculer (le passage obligé) et surveillance de ce passage ».

Ligne `GO-2026-11-21-47`, point 4 (vers 12:00 UTC) : « decisions : 1 go, 2c, 3 go4 oui », lu par la mère : « Papier A : citer Avenhaus et Jaech (1981) et restreindre le lemme d'additivité à sa forme valide à tout instant sur scores de sondes ».

**Une réserve de transcription.** La phrase « seul le bilan se revendique hors distribution » (point 2 ci-dessous) me vient du mandat de la mère, qui la donne pour accordée. La ligne du GO ne la porte pas mot pour mot, et la décision D-1 de la note sur la pince (« dire la pince en trois objets, ne revendiquer devant une attaque jamais vue que le bilan ») était « restée à Lazar » à `GO-2026-11-21-50`. La mère confirme, ou la phrase passe en section 11.

## 1. Vocabulaire

- **Issue** : ce qu'un oracle établit sur le produit d'un épisode, après coup. **Oracle exogène** : oracle dont le verdict ne dépend ni du mode d'attaque, ni de l'agent, ni d'aucun moniteur ; sur le banc actuel, l'oracle de couverture de la décision sur la vérité du dommage (N-060 v3, point 1). **Couverture de l'oracle** : les sortes de dommage qu'il sait reconnaître ; ce qu'il ne reconnaît pas n'existe pas pour lui.
- **Plancher d'audit au hasard** : une part des épisodes réels, tirée en secret et indépendamment de tout ce que l'agent observe et de tout score, est jugée par l'oracle exogène ; un test valide à tout instant sur le dommage audité sonne l'alarme. **Plafond de dommage** : le dommage qu'un épisode peut causer est borné par la tâche. **Corriger** : dans cette note, arrêter, relancer, confier au modèle de confiance, vérifier davantage, refaire les témoins ; **rien d'autre** (section 11, point 3).
- **Regard** : un mécanisme qui peut voir un sabotage (moniteur, sonde, oracle, bilan). **Dilemme** : deux regards liés par une relation que l'honnête respecte et que le dommage viole, de sorte que se cacher de l'un fait apparaître à l'autre. **Décorrélation** : deux regards dont les pannes sont seulement peu liées ; ce n'est pas un dilemme.
- **Pince** : le mot du dépôt pour la défense jointe d'une boîte noire et d'une boîte blanche. Elle se dit désormais en trois objets : la **complémentarité** (ce que l'interne capture parmi les manqués de l'externe, à fausses alertes partagées : une mesure), l'**étau** (tromper l'externe laisserait une trace interne : une hypothèse), le **bilan de la pince** (dommage vu par l'oracle = (référence honnête − lecture du suspect) + (lecture du suspect − issue) : une identité).
- **Témoins** : épisodes honnêtes d'un régime, exogènes au suspect, sur lesquels un moniteur est calibré. **Jumeau honnête** : le même modèle, sur la même tâche, sans sabotage ; il vaut au banc, non en service contre un modèle saboteur.
- **Recapture** : parmi les épisodes endommagés que l'audit au hasard trouve, le compte de ceux que le moniteur avait signalés.
- **Passage obligé** : ce que tout sabotage délibéré doit calculer quel que soit son mode, à savoir connaître la bonne action et en choisir une autre.

## 2. Point 1 — Le levier fort est de mesurer l'issue et de corriger ; le plancher d'audit au hasard

**Énoncé retenu.** Contre une menace diffuse, la garantie du programme ne repose pas sur la reconnaissance de l'attaque. Elle repose sur un plancher : une part des épisodes, tirée en secret, jugée par un oracle exogène, sous plafond de dommage par épisode. Ce plancher borne le dommage cumulé avant l'alarme pour toute politique d'attaque dont l'oracle voit le dommage, parce qu'il faut au saboteur beaucoup d'épisodes. Les sondes et les moniteurs servent d'**accélérateur** (alarme plus tôt) et d'**aiguillage** (quoi auditer, quoi relancer) de ce plancher, **non de garantie**.

**Ce qui change dans le programme.**
1. *Thèse du papier A* (l. 43, « détecte, avec une garantie de faux positifs toujours valide ») : la garantie de fausses alertes reste. S'y ajoute une lecture : aucun moniteur du programme ne porte de garantie de détection sur un genre de sabotage jamais vu ; la borne sur le dommage cumulé vient du plancher. C'est une borne inférieure de la sécurité au sens de la l. 74 (« alerte avant que le dommage cumulé n'atteigne θ »), dans la couverture de l'oracle.
2. *Base nommée nouvelle* : le **plancher d'audit au hasard**. Tout moniteur qui se compare à lui le fait en **dommage cumulé à l'arrêt, à étiquettes égales**. La métrique « latence (alerte contre dommage cumulé) » du plan à deux fois deux cases (l. 184) y trouve sa référence. La recapture est une **quantité rapportée**, sans critère.
3. *Où cela s'écrit, et dans quel ordre* (D-5, mot de Lazar « b mais phase exploratoire avec a d'abord ») : d'abord en mode exploratoire (`GO-2026-11-21-45`) dans le texte à part du moniteur de dissonance et de l'aiguillage, rapporté sans critère ; puis dans la version suivante du préenregistrement court du bras « papier dopamine ». Nulle part ailleurs par cette note.
4. *Jeu de contrôle* (l. 72, « budget d'audit b ») et *invariant des seuils stochastiques* (l. 168, « probabilité d'audit lisse et croissante du score ») : dans tout texte qui écrit le plancher, une part du budget d'audit est tirée sans égard au score ; l'audit qui suit le score reste permis, mais ne porte pas la borne.
5. *Hypothèse du gain de la boîte blanche sur la noire (H1, l. 93) et de l'accumulation sur sondes (H2, l. 94)* : énoncés inchangés. Ce qui change est la façon de dire ce qu'un gain établit : il établit un gain sur les modes éprouvés, mode tenu à l'écart compris (N-056, points 1 et 4) ; il n'établit pas la tenue devant un genre inconnu.
6. *Environnement (a)* (l. 122, « cibles semées préenregistrées + vérification différée sur sous-échantillon ») : ce sous-échantillon est la matière du plancher ; pour le porter, son tirage doit être secret et indépendant des scores. À écrire dans les textes à venir, pas dans les textes scellés.

**Ce qui ne change pas.** Le critère de la porte de fin de phase 1 (N-008 ; N-056, point 1) : le plancher **n'entre pas** dans la liste des bases que le séquentiel boîte blanche doit battre (il ne se mesure pas en rappel à 1 % de fausses alertes) ; l'y mettre serait un nœud, section 11, point 1. La reconception des sondes après un échec de cette porte (N-062) : inchangée, les sondes restent un instrument à faire marcher. L'invariant « aucun score de moniteur dans l'entraînement ni la sélection d'un agent » (N-053, point 5) et les invariants de l'oracle (N-060 v3, point 4). Les quatre limites du plancher sont écrites partout où il l'est : rien contre un coup unique ; rien hors de la couverture de l'oracle ; un saboteur qui reste sous l'excès toléré n'est pas pris (son dommage est alors borné par définition) ; l'oracle devient le point unique de défaillance.

**Ce qui pourrait être revendiqué, sous le verdict d'antériorité.** Dans sa forme seulement : (i) l'écriture du plancher comme borne chiffrée de la sécurité du programme contre une menace diffuse, et comme base que tout moniteur doit battre en dommage cumulé à étiquettes égales ; (ii) une règle « moniteur invalide » tirée de la recapture, avec la borne du dommage accumulé pendant la mesure. Les deux sont des **questions** (R8), assemblées de pièces publiées.

**Ce qui n'est pas revendiqué, et par qui c'est pris.**
- Que surveiller et incriminer soient les leviers faibles contre le diffus : Terekhov et al. les jugent « less promising » et se tournent vers l'entraînement (2606.08892 v2, [PDF, p. 2]). « Le levier fort est de mesurer l'issue et de corriger » est la lecture du concepteur, non un résultat.
- L'audit des premiers épisodes et l'audit des plus suspects : Greenblatt et al. (2312.06942 v5, [PDF, p. 8]).
- L'inférence valide à tout instant avec audit humain adaptatif : **Gao et al.** (2611.15197 v1, [PDF, p. 1]).
- Le test du bilan global comme meilleure réponse à un détournement étalé : **citation de 1981** (section 7).
- Les paris valides à tout instant : classiques. La relecture de transcriptions non signalées : proposée par un évaluateur externe [page web].
- Borner, à tout instant, la probabilité d'un mode de défaillance jamais vu avant le service : **Li et al.** (Li, Hays, Ramdas, Raghavan, 2611.15835 v1, [PDF, p. 1]) ; leur note : sans hypothèse, toute borne indépendante des données vaut 1 ([PDF, p. 6]). Aucune phrase du programme ne promet donc une borne de ce genre par les moniteurs.

**Citations obligatoires** : section 8, lignes « point 1 ».

**À vérifier sur PDF.** Lecture en entier de Gao et al. et de Li et al. (page 1 et motifs seulement à ce jour) ; Ge-Wang et al. (2606.06529 v1, page 1 seule) : un attaquant qui choisit quand attaquer abaisse la sûreté mesurée, ce qui touche le plancher si le tirage se devine ; Greenblatt et al., p. 7-8.

**Textes scellés.** Aucun n'est touché. La vérification différée déjà préenregistrée dans des textes scellés n'est pas relue comme un plancher : si son tirage n'y est pas écrit secret et indépendant des scores, elle ne porte pas la borne, et ce constat ne se corrige que dans un texte neuf.

## 3. Point 2 — Deux regards tels qu'échapper à l'un expose à l'autre

**Énoncé retenu.** Le programme ne cherche plus des regards décorrélés, il cherche des dilemmes. Deux alertes réunies ne créent pas de puissance ; seule une relation entre deux regards, que l'honnête respecte et que le dommage viole, en crée. Cela couvre la pince et le dilemme entre la réussite attendue lue par une sonde et l'issue calculée. **Devant une attaque jamais vue, seul le bilan se revendique** : dans la couverture de l'oracle, sous une référence honnête exogène et valable dans le régime ; sa garantie n'emploie pas les activations du suspect.

**Ce qui change dans le programme.**
1. *Vocabulaire* : « la pince » se dit en trois objets (section 1). Le mot ne figure pas dans le programme ; il y entre, à la prochaine version, sous ces trois noms.
2. *Façon de dire le gain de la boîte blanche dans la pince* : la vitesse et l'aiguillage, non la garantie. L'énoncé de H1 et le plan à deux fois deux cases (l. 184), qui comparent les deux boîtes sans les joindre, sont inchangés.
3. *Diversité des moniteurs (H5, l. 113 ; § 8.2, l. 146)* : le programme écarte déjà la décorrélation des erreurs bénignes au profit de la matrice de transfert d'attaque. S'ajoute une quantité rapportée, là où des épisodes endommagés audités existent : le **silence commun** des regards sous attaque (recapture à deux mâchoires). Énoncé de H5 (N-013, § 7) inchangé.
4. *Quorum hétérogène (HC5, l. 107 ; N-013, § 4)* : un quorum est une réunion d'alertes. Énoncé inchangé ; aucun texte ne l'appelle « dilemme » sans avoir mesuré le silence commun.
5. *Trahison par les activations (HC2b, l. 104 ; N-013, § 5)* : c'est l'étau, pour le texte. Elle reste une hypothèse à tester, avec son contre-indice déjà noté ; elle ne devient pas une garantie. Énoncé inchangé. La sonde qui lit l'agent auteur (N-068) : inchangée.
6. *Théorème négatif (l. 62 ; N-003)* : il sert de justification interne (une statistique de relation, non deux statistiques marginales). Énoncé inchangé. La co-élévation entre copies et le pic par agent comme base de la porte de la phase 2 (N-069) : inchangés.
7. *Banc* : le bilan de la pince, ses trois témoins « doit mourir » (premier terme seul, second terme seul, réunion de deux alertes à pannes communes) et ses familles sont versés au banc de la course de l'adjudant, sans dépense (`GO-2026-11-21-50`).

**Ce qui ne change pas.** Aucune porte. Les deux épreuves sans attaque de la note sur la pince (netteté de la référence ; dissociation chez l'honnête) suivent `GO-2026-11-21-50` : exploratoires d'abord, texte scellé avant toute lecture décisive. La mâchoire externe d'octobre (qui ne lit aucune prose) et la mesure de l'étau : non tranchées ici (D-4 de la note sur la pince, restée à Lazar).

**Ce qui pourrait être revendiqué, sous le verdict d'antériorité.** Le seul bilan : l'identité, et l'**invariance au partage** (quoi que le suspect fasse de sa lecture, la somme vaut le dommage que l'oracle voit [calcul, P1]). L'identité est élémentaire (un télescopage) ; la valeur, s'il y en a une, est dans la mesure. La note sur la pince n'a fait **aucune recherche d'antériorité** pour le bilan : c'est une question.

**Ce qui n'est pas revendiqué, et par qui c'est pris.**
- Que la pince de deux détecteurs appris tienne devant un attaquant informé ; que l'étau tienne hors distribution ; que les pannes de deux boîtes de nature différente soient indépendantes. Contre-indices : deux détecteurs d'anomalie sur activations réussissent et échouent sur les mêmes jeux (Johnston et al., 2504.08812 v1, [PDF, p. 9]) ; une chaîne de garde-fous se défait étage par étage (McKenzie et al., 2506.24068 v3, [PDF, p. 1]) ; les défenses de l'espace latent tombent ensemble sous obscurcissement (Bailey et al., 2412.09565 v2, [PDF, p. 1, 3]).
- La réussite attendue lue dans les états internes et sa calibration : Xu, Yuksekgonul, Zou (2602.00986 v2). Un état précurseur extrait sans exemple d'attaque, qui monte avant la triche : **Fischl-Lanzoni et al.** (2611.14996 v1, [PDF, p. 1, 2, 5, 6]) ; sur un de leurs trois modèles, il ne sépare pas la triche de l'échec honnête : c'est aussi un contre-indice au premier terme du dilemme, qui aiguille et n'incrimine pas.
- Une clé secrète dans la surveillance par activations : **Aremu et al.** (2603.23171 v3, [PDF, p. 1-3]). « Nos tirages secrets » ne se dit donc pas neuf pour un regard interne.
- L'écart à l'honnête accumulé par un pari valide à tout instant : Ortega-Fernandez et al. (2610.11843 v1, [PDF, p. 1]), avec leur hypothèse de transfert de calibration.
- Tester le total plutôt que ses parts : **citation de 1981** (section 7).

**Citations obligatoires** : section 8, lignes « point 2 ».

**À vérifier sur PDF.** Fischl-Lanzoni et al. et Aremu et al. en entier ; Xu et al. au-delà des pages 5 à 7 ; une recherche d'antériorité propre au bilan (tests de calibration valides à tout instant, Arnold et al., 2109.11761 v3, page 1 seule).

**Textes scellés.** Aucun n'est touché. Le premier pas non justifié de la note sur la pince demeure : en service, qui produit la référence honnête exogène, et sur quels témoins (section 11, point 5).

## 4. Point 3 — Alerte = nouveauté et preuve de dommage ensemble ; nouveauté seule = mise à jour des témoins

**Énoncé retenu.** Un détecteur de nouveauté n'incrimine pas. Il sonne pour toute dérive bénigne, et sur le flux du suspect la dérive et le saboteur sont le même observable. Règle : une **alerte** demande, sur la même unité, la nouveauté **et** une preuve de dommage rendue par l'oracle ; la **nouveauté seule** déclenche la mise à jour des témoins du régime (nouveaux épisodes honnêtes exogènes, seuils refaits sur eux, jamais sur le flux du suspect) et peut aiguiller l'audit. La **preuve de dommage seule**, sans nouveauté, relève du plancher (point 1) : elle n'attend aucune seconde clé.

**Ce qui change dans le programme.**
1. *Sondes non supervisées (Mahalanobis, l. 143)* et tout détecteur d'anomalie : leur sortie a deux issues écrites d'avance dans tout préenregistrement à venir, « alerte » (avec dommage) et « régime neuf » (sans dommage) ; la seconde n'est ni comptée comme détection ni comme fausse alerte de sabotage, elle est comptée à part.
2. *Asymétrie d'apprentissage (l. 170)* : inchangée dans sa lettre ; s'y ajoute que les témoins se refont sur des honnêtes exogènes. Une règle qui recale son seuil sur le flux du suspect est un témoin « doit mourir » du banc.
3. *Plan d'analyse* : là où un taux de fausses alertes est rapporté sous dérive de régime, il l'est avec des témoins du régime d'usage (note sur la dérive de régime, déjà rendue).

**Ce qui ne change pas.** Les critères des portes ; le critère des sondes à la porte de fin de phase 0 (N-063 v2) ; la part d'audit tirée au hasard, qui ne suit jamais la nouveauté seule (sinon le tirage se devine).

**Ce qui est revendiqué.** **Rien.** C'est une règle d'exploitation, « occupée dans sa forme » selon la note (§ 6, rang 9).

**Ce qui n'est pas revendiqué, et par qui c'est pris.** La théorie du danger en immunologie [de mémoire] et son emploi en détection d'intrusion (Aickelin et Cayzer, arXiv 0801.3549 v3, [PDF, p. 1]) ; l'algorithme des cellules dendritiques sur des agents (conférence AAAI 2026, **non vérifié sur PDF**). Limites à écrire : un attaquant qui reste dans le nuage honnête ne déclenche pas la première clé ; l'obscurcissement trompe la nouveauté avec les sondes (Bailey et al., [PDF, p. 3]).

**Citations obligatoires** : section 8, lignes « point 3 ».

**À vérifier sur PDF.** La ligne du GO porte « (sources revérifiées sur PDF) ». Dans les pièces que j'ai lues, seule la page 1 d'Aickelin et Cayzer est lue sur PDF ; la source d'immunologie est de mémoire et la pièce de 2026 n'est pas au dépôt. Je lis la parenthèse comme une **condition** : la règle ne s'écrit avec ses sources dans un texte qui sort du dépôt qu'après cette vérification (section 11, point 4).

**Textes scellés.** Aucun n'est touché ; la course « seuil et moniteurs » et son texte restent tels quels.

## 5. Point 4 — Bilan du produit fermé contre le jumeau honnête

**Énoncé retenu.** Tenir quelques comptes du produit que tout dommage devrait déplacer (couverture des contrôles, coûts, effectifs, affirmations adossées à une preuve), et tester leur **somme cumulée** contre la loi du jumeau honnête sur les mêmes tâches. C'est un candidat de second regard, non une garantie.

**Ce qui change dans le programme.**
1. *Vérité du dommage (N-060 v3, point 1 : « dommage = baisse de couverture par rapport au jumeau honnête apparié »)* et *base « mots et coût »* (N-029, N-063) : ce sont deux lignes du bilan. La décision N-060 n'est pas modifiée ; le bilan en est une généralisation candidate.
2. *Candidat inscrit au banc de la course de l'adjudant*, avec ses deux tests de mort écrits d'avance : sur une famille plantée « dommage hors comptes », il doit se dire muet ; sur une famille tenue à l'écart, sans gain sur la base « mots et coût », il est mort « sans gain ». Premier pas sans dépense : la liste des quantités comptables du produit, par un agent habilité.
3. *Portée du jumeau* : il vaut au banc. En service, la référence est exogène (témoins du régime, modèle de confiance, prédicteur sur la tâche) : le jumeau d'un saboteur est un saboteur.

**Ce qui ne change pas.** Les invariants de l'oracle (N-060 v3, point 4) valent pour chaque compte : aucun n'entre dans la sélection d'un agent ou d'un moniteur. Le bras A des organismes discrets (N-060 v4 et son erratum) garde l'appariement pour variable principale et le mot « désappariement » ; le bilan ne s'y applique pas.

**Ce qui pourrait être revendiqué, sous le verdict d'antériorité.** Dans sa forme : un bilan du produit fermé contre un jumeau honnête, en contrôle de l'IA. « Non trouvé » au périmètre du 21 novembre : question.

**Ce qui n'est pas revendiqué, et par qui c'est pris.** Le bilan d'une quantité conservée et son point selle : **citation de 1981** (section 7). Des registres d'actions relus par règle : Nagarajan et al. (2610.24483 v1, [PDF, p. 1]). L'écart à l'honnête par pari valide à tout instant : Ortega-Fernandez et al. La liste des comptes est une spécification : un dommage le long d'une dimension non comptée passe.

**Citations obligatoires** : section 8, lignes « point 4 ».

**À vérifier sur PDF.** Les deux rapports de 1982 et 1985 en entier, et l'article d'origine de 1981 (section 7) ; Nagarajan et al. au-delà de la page 1.

**Textes scellés.** Aucun n'est touché. **Écart nommé, sans effet** : le texte neuf du bras A, s'il est scellé depuis, ne reçoit aucun compte de plus par cette note.

## 6. Point 5 — Recherche de ce que tout sabotage délibéré doit calculer, et surveillance de ce passage

**Énoncé retenu.** Un « algorithme du sabotage » identifié sur des sabotages connus hérite de leur distribution, sauf s'il est nécessaire à tout sabotage. Le programme ouvre une **question de recherche** : existe-t-il un passage obligé (connaître la bonne action et en choisir une autre), lisible dans les états internes par des lectures apprises **sur honnêtes seuls**, et peut-on le surveiller plutôt que les sabotages connus ? C'est une question, non un adjudant et non une hypothèse revendiquée.

**Ce qui change dans le programme.**
1. *Questions ouvertes (§ 15)* : la question y entre.
2. *Validité de construit (§ 11, l. 223 ; H8, l. 99) et prédiction de validité (l. 135)* : énoncés inchangés. La question donne une cible de plus au diagnostic « ce que les sondes lisent » que N-062 (point 2) fait rapporter à chaque cycle.
3. *Reconception des sondes (N-062)* : le passage obligé est une direction candidate d'un cycle, conçue sur les modes vus seulement, jugée sur une famille tenue à l'écart neuve ; rien n'y est sélectionné sur le tenu à l'écart.
4. *Candidats nommés, à l'atelier et au banc* : la bascule en profondeur (action lue aux couches fidèles contre action émise) ; les sondes de conséquences attendues. Mode exploratoire d'abord (`GO-2026-11-21-45`), préenregistrement avant toute lecture décisive (R1).

**Ce qui ne change pas.** Aucune hypothèse, aucune porte. Pas de moyenne ni de médiane sur les jetons en production (N-026). Une lecture mécaniste ajoute un soupçon, elle ne blanchit pas. L'attestation causale par micro-interventions secrètes a son texte et son bras à part (D-6, `GO-2026-11-21-51`, point 6) : hors de cette note.

**Ce qui est revendiqué.** **Rien** à ce jour. La question elle-même n'est pas dite neuve.

**Ce qui n'est pas revendiqué, et par qui c'est pris.** Une signature « sait, puis dit autre chose » : Halawi et al. (2307.09476 v3, [PDF, p. 1]) ; Nyoma (2606.17229 v1, [PDF, p. 1]), dont les résultats à 100 % sont trop propres et à auditer (R4), et jamais éprouvés contre un modèle entraîné à l'effacer ([PDF, p. 13]). Un état précurseur sans exemple d'attaque : **Fischl-Lanzoni et al.**, avec leur contre-indice (triche et échec honnête non séparés sur un modèle). Une clé secrète dans la sonde : **Aremu et al.** Des résultats négatifs pour des sondes d'avant l'action (Fomin et al., 2606.30449 v1) ou égalés par une base de texte (Sinha, 2610.37679 v1). Aucun détecteur d'anomalie mécaniste efficace sur tous les modèles et toutes les tâches (Johnston et al., [PDF, p. 1, 6]). Un attaquant entraîné décide tôt, ou déplace ses représentations (McGuinness et al., 2512.11949 v1, [PDF, p. 1]).

**Citations obligatoires** : section 8, lignes « point 5 ».

**À vérifier sur PDF.** Halawi et al. et Nyoma en entier (premier pas du candidat, note § 6, rang 6) ; Fomin et al. et Sinha, cités d'après la page 1 ou 2.

**Textes scellés.** Aucun n'est touché ; le texte de lecture des lentilles n'est pas modifié.

## 7. Décision D-4 — citation de 1981, et lemme d'additivité revendiqué dans sa seule forme valide à tout instant sur scores de sondes

**Ce qui est pris.** Pour un test à horizon fixe sur un bilan gaussien, contre un détourneur qui étale un total sur une suite de périodes, « the optimal test procedure consists in testing the overall balance », et ce test donne « the highest guaranteed detection probability taking all diversion strategies into account » : Avenhaus, Beedgen et Sellinschegg, rapport KfK 3935, juin 1985, [PDF, p. 9 et 18], d'après Avenhaus et Jaech (1981). C'est l'ossature de « la puissance ne dépend que du total, pas de la répartition » (programme, l. 56).

**Ce qui change.**
1. *Lemme d'additivité (l. 54-56 ; l. 95 ; N-004)* : l'**invariance terminale (L1)**, pour un test à horizon fixe, **n'est plus revendiquée** ; elle se cite comme publiée. La revendication de N-004 (« l'énoncé adverse complet […] appliqué aux scores de sondes internes ») se lit désormais : **la seule lecture valide à tout instant, sur des scores de sondes internes** (borne inférieure invariante, coût du report, prix de la garantie, détection avant le dommage, validité sous dépendance : L3 et suivants de N-004). L'invariance entre agents (L4) n'est revendiquée que dans cette lecture.
2. *Critère de succès (l. 235, « lemme et théorème négatif démontrés »)* et *expérience du lemme sur données réelles (l. 185)* : inchangés dans leur lettre ; le lemme y est celui du point 1.
3. *Papier B (N-069, statistique conjointe à garantie toujours valide)* : énoncé inchangé ; la citation s'y impose dès que l'additivité entre agents est invoquée.
4. *Veille* : le gel est levé **sans borne de zone** (mot de Lazar : « non pas borne a cette zone , go »).

**Ce qui ne change pas.** Le théorème négatif (N-003). Le repli de N-004 (« présenter le lemme comme corollaire cité »), toujours disponible, non déclenché ; son déclenchement reste un nœud. Le poids d'originalité du programme (0,75, l. 95), que cette note ne réécrit pas ; N-004 l'avait déjà ramené vers 0,4 par estimation.

**Risque à dire.** Le rapport de 1985 porte, d'après son titre et ses pages vues par motifs, des procédures de test sur des suites de périodes ; il dit du délai de détection : « there is no solution which would correspond to the Neyman-Pearson test » ([PDF, p. 10]). Des tests séquentiels sur des suites de bilans existent dans ce domaine [de mémoire]. La forme « valide à tout instant » n'est donc **pas déclarée libre** : elle est ce qui reste à revendiquer **si** la lecture en entier ne la trouve pas prise.

**À vérifier sur PDF.** L'article d'origine d'Avenhaus et Jaech (1981), non trouvé en accès libre : à lire par un agent neuf (D-4 (a)) ; la formule de la probabilité garantie (rapport de 1985, p. 18), lue sur une numérisation abîmée ; le rapport KfK 3365 de 1982 ; un troisième rapport (KfK 4680, 1990), téléchargé, ni lu ni versé. La référence bibliographique exacte de 1981 n'est pas au dépôt : **aucun texte ne la cite avant qu'elle soit lue sur pièce**, sinon par « d'après Avenhaus et Jaech (1981), cité par le rapport KfK 3935, p. 9 ».

**Textes scellés.** Le préenregistrement de la simulation du lemme et du théorème négatif (T0.3) et ses résultats ne sont pas touchés : ils mesuraient les énoncés de N-004 et ne revendiquent rien. Le préenregistrement de la porte de fin de phase 1, quand il se scellera, part de l'énoncé resserré.

## 8. Citations obligatoires

Dans tout texte, interne ou destiné à sortir, qui présente le point dit. PDF sous `docs/sources/pdf/mecanisme-adjudant-v1/` sauf mention ; table de provenance `provenance-mecanisme-adjudant-v1.md` (`563e611d…`). Empreintes recopiées de cette table, non recalculées par moi.

| pour | pièce | PDF, empreinte | pages lues à ce jour |
|---|---|---|---|
| points 1, 2, 4 ; section 7 | Avenhaus, Beedgen, Sellinschegg, rapport KfK 3935 (1985), « d'après Avenhaus et Jaech (1981) » | `avenhaus-beedgen-sellinschegg-1985-kfk-3935-…-v1.pdf`, `9fd13396…` | 8, 9, 18 en clair ; autres par motifs |
| point 1 | Gao, Hu, Liu, Zhou, 2611.15197 v1 | `2611.15197v1.pdf`, `a6afe2d0…` | 1 |
| points 1, 2 | Li, Hays, Ramdas, Raghavan, 2611.15835 v1 | `2611.15835v1.pdf`, `a0951584…` | 1 ; 6, 12, 16, 31, 44, 45, 53 par motifs |
| point 1 | Terekhov et al., 2606.08892 v2 ; Greenblatt et al., 2312.06942 v5 | déjà au dépôt, `aea0f2d1…` ; `999f7a92…` | 2 ; 7, 8 |
| points 2, 5 | Fischl-Lanzoni, Pandey, Stein, Africa, 2611.14996 v1 | `2611.14996v1.pdf`, `5b2e6e77…` | 1 ; 2, 5, 6, 9, 10 par motifs |
| points 2, 5 | Aremu, Ognev, Poppi, Lukas, 2603.23171 v3 | `2603.23171v3.pdf`, `da05ddb7…` | 1 ; 2-5, 7, 10 par motifs |
| point 2 | Xu, Yuksekgonul, Zou, 2602.00986 v2 ; Bailey et al., 2412.09565 v2 | déjà au dépôt, `da004f53…` ; `9c23a613…` | 5-7 ; 1-3 |
| points 2, 4 | Ortega-Fernandez, Kowalczyk, Warr, 2610.11843 v1 | `2610.11843v1.pdf`, `a3b8f0ee…` | 1 |
| point 3 | Aickelin, Cayzer, arXiv 0801.3549 v3 | `0801.3549v3.pdf`, `2ed19828…` | 1 |
| point 5 | Halawi, Denain, Steinhardt, 2307.09476 v3 ; Nyoma, 2606.17229 v1 | `f58b18ba…` ; `46008490…` | 1 ; 1 et motifs |

**À citer quand le point est abordé** : Johnston et al. (2504.08812 v1) ; McKenzie et al. (2506.24068 v3) ; McGuinness et al. (2512.11949 v1) ; Ge-Wang et al. (2606.06529 v1) ; Nagarajan et al. (2610.24483 v1) ; Mondal et al. (2609.32267 v1, « no label-free test detects the change », p. 1) ; Lindner et al. (2512.22154 v1, p. 16 : la tenue du moniteur en service y est une supposition).

**Ne pas écrire** : « moniteur valide hors distribution » ; « la pince tient devant des attaques jamais vues » ; « garantie de détection » pour une sonde ; « premier plancher d'audit », « premier bilan », « première règle à deux clés » ; « le lemme d'additivité montre que la puissance ne dépend que du budget » sans la citation de 1981 ; tout chiffre des blocs de calcul sans les mots « sous supposition ».

## 9. Ce qui ne change pas, en bloc

- R1 à R14, l'allègement de la procédure, « Qui conçoit ».
- Les énoncés retenus de toutes les hypothèses (N-003 à N-073), hors la revendication du lemme (section 7). Les critères de toutes les portes : fin de phase 0 (N-027, N-063 v2), fin de phase 1 (N-008, N-056), papier C (N-005, N-006), phase 2 (N-069).
- N-053 (les cinq propositions de l'audit défensif, l'invariant sur les scores de moniteur), N-054, N-060 v3, v4 et son erratum, N-062, N-068, N-069.
- La question, non tranchée et étrangère à cette note, du contraste à témoin apparié à la porte de fin de phase 1 (brouillons numérotés N-074).
- Toute dépense : devis et GO. Les trois chantiers actifs : cette note n'en ouvre aucun.

## 10. À reporter à la prochaine version du programme

Texte proposé ; le programme v2 reste archivé tel quel.

- **§ 1, Positionnement**, après la phrase unique : « La garantie contre un sabotage de genre inconnu ne vient pas de ces moniteurs : elle vient d'un plancher d'audit tiré au hasard, jugé par un oracle sur le produit, sous plafond de dommage par épisode ; les moniteurs en sont l'accélérateur et l'aiguillage (N-075). »
- **§ 3**, sous le lemme : « Antériorité : l'invariance à la répartition, pour un test à horizon fixe sur un bilan gaussien, est publiée (Avenhaus et Jaech 1981, d'après le rapport KfK 3935, p. 9 et 18). Le lemme n'est revendiqué que dans sa lecture valide à tout instant, sur des scores de sondes internes. »
- **§ 4**, après « Sécurité » : « Plancher : pour toute politique dont l'oracle voit le dommage, une part du budget d'audit tirée en secret et sans égard aux scores borne le dommage cumulé avant l'alerte ; hors de la couverture de l'oracle et contre un coup unique, aucune borne. »
- **§ 8**, alinéa nouveau « 8.4 Deux regards » : les trois objets de la pince ; « un second regard se juge au dilemme, non à la décorrélation » ; la règle à deux clés pour tout détecteur de nouveauté ; le bilan du produit contre le jumeau honnête comme candidat.
- **§ 8.3**, base nommée de plus : « plancher d'audit au hasard, en dommage cumulé à l'arrêt, à étiquettes égales ; rapporté, hors critère de porte ».
- **§ 9**, invariant de plus : « une part de l'audit est tirée au hasard, en secret, sans égard à aucun score ».
- **§ 15**, question de plus : « ce que tout sabotage délibéré doit calculer, et sa lecture sur honnêtes seuls ».

## 11. Points que cette note ne tranche pas, renvoyés à Lazar

1. **Le plancher entre-t-il un jour dans la liste des bases de la porte de fin de phase 1 ?** Enjeu : un critère de porte. (a) Non, rapporté à côté : avantage, le critère reste celui de N-008 et N-056 ; inconvénient, « la sonde détecte » peut passer la porte sans dire ce qu'elle ajoute au plancher. (b) Oui, en dommage cumulé à étiquettes égales : avantage, la porte dit le gain utile ; inconvénient, une seconde métrique à la porte et des étiquettes à payer. Recommandation : (a) jusqu'aux mesures exploratoires. Confiance 0,65. Nœud : pas de défaut.
2. **La recapture et l'invariant de l'oracle.** La recapture emploie des verdicts de l'oracle pour annoncer « moniteur invalide ». N-060 v3 (point 4) interdit toute sortie de l'oracle dans la sélection d'un moniteur. Lecture que je propose : annoncer n'est pas sélectionner ; reconcevoir le moniteur sur ces mêmes épisodes le serait. À confirmer avant le premier texte qui écrit la recapture.
3. **« Corriger » par l'entraînement de l'agent sur l'issue** (ce vers quoi Terekhov et al. se tournent) : non ouvert par cette note. Ce serait une modification de périmètre et touche N-053.
4. **La parenthèse « sources revérifiées sur PDF »** du point 3 : condition (ma lecture) ou constat ?
5. **La référence honnête en service** : qui la produit, sur quels témoins. Sans elle, le bilan de la pince n'a pas d'appui hors du banc.
6. **La phrase « seul le bilan se revendique hors distribution »** : à confirmer (section 0).

## 12. Ligne proposée pour `CLAUDE.md`

À ajouter à la fin de la liste « Décisions de Lazar », par la mère, après la contre-lecture :

> N-075 (mot de Lazar du 21 novembre, GO-2026-11-21-51 ; le numéro N-074 est pris par deux brouillons non retenus) : contre la menace diffuse, le levier fort est de mesurer l'issue et de corriger — plancher d'audit tiré au hasard, à oracle exogène, sous plafond de dommage, base nommée rapportée hors critère de porte, sondes en accélérateur et en aiguillage, non en garantie ; deux regards se jugent au dilemme et non à la décorrélation, la pince se dit en trois objets (complémentarité, étau, bilan) et seul le bilan se revendique devant une attaque jamais vue ; alerte = nouveauté et preuve de dommage ensemble, nouveauté seule = mise à jour des témoins ; bilan du produit fermé contre le jumeau honnête, candidat ; recherche du passage obligé de tout sabotage, question ouverte ; lemme d'additivité revendiqué dans sa seule forme valide à tout instant sur scores de sondes, Avenhaus et Jaech 1981 en citation obligatoire (GO-2026-11-21-47) ; aucun critère de porte changé, aucune phrase de revendication avant le verdict d'antériorité sur les sept voisins (`docs/decisions/decision-N-075-issue-plancher-et-deux-regards-v1.md`).

## Relevé de méthode

Selon `docs/procedures/consigne-commune-methode-de-recherche-v1.md` (`d327b3fcbee59f37f833e83812a66ba8b28af72cdd5475772870612a2c9d23d8`).

**Chaîne de raisonnement.**
1. Lazar a accordé cinq points et la restriction du lemme (`registres/go.md`, lignes `GO-2026-11-21-51` et `-47`, recopiées en section 0).
2. Les cinq points viennent de deux notes non contre-lues (`896cec0e…`, § 1 points 4 et 7, § 3.2, § 3.4, § 3.5, § 6 ; `c0318d1f…`, verdict et § 2 à 5).
3. Le programme définit la sécurité par le dommage cumulé avant l'alerte (`2fd63bad…`, l. 74), porte un budget d'audit (l. 72), une vérification différée sur sous-échantillon (l. 122), un audit qui suit le score (l. 168) : le plancher s'y loge sans changer une hypothèse (pas 1, section 2).
4. Le critère de la porte de fin de phase 1 se mesure en rappel à 1 % de fausses alertes (N-007 et N-008, `ab7dc9bb…`, l. 57-69 ; N-056, `3592c1e9…`, l. 38-46) : le plancher, mesuré en dommage cumulé, n'y entre pas sans décision (section 11, point 1).
5. Sous un audit de probabilité p et un oracle sûr, un saboteur est pris au plus tard à son n-ième épisode endommagé avec probabilité 1 − (1 − p)^n : n = 299 pour p = 0,01, n = 14 pour p = 0,20, au seuil 0,95 (rejoué : `python3 -c "import math;print([math.ceil(math.log(.05)/math.log(1-p)) for p in (.01,.2)])"` rend `[299, 14]` ; [calcul, B]).
6. Le bilan de la pince est un télescopage ; il vaut le dommage que l'oracle voit, quel que soit le partage [calcul, P1], et vaut zéro si l'oracle ne voit rien (même bloc).
7. La décision D-7, accordée, interdit toute phrase de revendication avant la lecture en entier des sept voisins (`896cec0e…`, § 8 ; `GO-2026-11-21-46`) : d'où le conditionnel de chaque rubrique « revendiqué ».
8. L'invariance à horizon fixe est publiée (rapport KfK 3935, p. 9 et 18, lu par l'auteur de la note sur numérisation) : L1 de N-004 (`cc1be393…`, l. 61) sort de la revendication (section 7).
9. Supposé : la forme valide à tout instant du lemme n'est pas prise dans la littérature des garanties nucléaires ; aucune pièce ne l'établit.
10. Supposé : les pages citées [PDF, p.] disent ce que les notes en rapportent ; je ne les ai pas rouvertes.
11. Supposé : aucun texte scellé du dépôt n'écrit déjà un audit secret et indépendant des scores, ni un critère que ces points contrediraient ; je n'ai ouvert aucun préenregistrement.

**Objets de contrôle.** La pièce porte deux garanties. *Le plancher* : objet où la conclusion « il borne le dommage » est fausse, le dommage hors de la couverture de l'oracle : j'attendais qu'il s'y dise muet, et la note le déclare « hors portée » (§ 7.4, famille « l'oracle ne voit pas ») ; objet où elle est vraie, le saboteur vu par l'oracle sous tirage indépendant : attendu 299 et 14, rendu 299 et 14 (pas 5). *Le bilan de la pince* : objet faux, l'honnête (somme nulle attendue, nulle rendue) et la dérive bénigne à référence périmée (sonnerie à tort attendue, rendue : 0,08), ce qui est sa limite déclarée ; objet vrai, le sabotage sous cinq façons d'être lu (0,0748 cinq fois) [calcul, P1]. Ce sont les contrôles d'un argument, repris des notes, non ceux d'une mesure ; rien n'a été scellé avant.

**Premier pas non justifié.** Le pas 9. Ce qui le justifierait : la lecture en entier des rapports de 1982, 1985 et 1990 et de l'article de 1981, avec une recherche des tests séquentiels sur suites de bilans. Le pas 10 est le second.

**Mode d'échec affecté.** Sans objet : pièce d'auteur, non de relecteur.

**Dérivation de l'énoncé seul.** Sans objet : pièce d'auteur, non d'agent de re-dérivation.

**Trouvaille de côté.** (1) La recapture heurte peut-être l'invariant de l'oracle de N-060 v3 (section 11, point 2). (2) « Corriger » peut se lire comme entraîner l'agent sur l'issue, ce que cette note n'ouvre pas (point 3). (3) Le numéro N-074 est occupé par une question de porte encore ouverte, absente de `CLAUDE.md`.

**Évaluateur et conseil.** Ce qui juge cette pièce : le contre-lecteur Opus 5.5, puis Lazar ; aucun juge admis sur témoins. Par où elle pourrait être bien jugée sans le mériter : elle resserre et ne promet rien, ce qui se lit comme de la prudence alors que ses appuis sont deux notes non contre-lues et des pages non relues (pas 2 et 10) ; les numéros de ligne du programme sont justes, ce qui ne dit rien de la justesse des lectures. Conseil au contre-lecteur : les modes « antériorité » (pas 9), « énoncé infidèle » (la section 0 contre les mots du GO, et chaque « inchangé » contre la décision citée) et « garantie qui suppose ce qu'elle prouve » (le tirage secret et la référence exogène).

## Ce que je n'ai pas fait

- Aucun PDF rouvert ; aucune empreinte de PDF recalculée ; aucune recherche d'antériorité nouvelle.
- Aucun préenregistrement, aucun verdict, aucun résultat lu. Je n'ai pas vérifié texte par texte ce qui est scellé : « aucun texte scellé touché » repose sur le fait que cette note ne change aucun critère ni aucune hypothèse, et sur le pas 11.
- Non ouverts : les dossiers et branches interdits par le mandat ; la ligne R-2059 ; le dossier `collisionneur-v1/` voisin de la note ; N-054, N-055, N-063 et l'erratum de N-060 v4, cités d'après `CLAUDE.md` ; N-068 et N-069 lus dans leurs seules sections 4 et « ce qui ne change pas ».
- `CLAUDE.md`, le programme et les registres ne sont pas modifiés. Routine de reprise : à la mère.
