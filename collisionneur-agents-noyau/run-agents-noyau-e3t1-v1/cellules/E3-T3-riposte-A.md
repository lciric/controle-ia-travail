# Tour III.3 — Proposition A : riposte

## 0. Pièces et statuts

- FAITS : présent, vide par décision de l'arbitre (conv-audit, n° 28 § 1). Rien d'ajouté.
- Pièces reçues : ma conception (E3-T1-conception-A), l'attaque de B et l'attaque de C ; toutes trois complètes en apparence. Je ne réponds qu'aux sections qui visent A. Je n'attaque pas C ici : ce n'est pas le livrable du tour.
- Statuts : mes recalculs portent **VÉRIFIÉ (recalcul)** et ne vérifient que l'arithmétique ; tout dispositif que je propose est **HYPOTHÈSE** ; tout chiffre hors recalcul est **illustratif**. Quand je reprends un contrôle de B ou de C, je le dis.

---

## (a) Réponse à chaque attaque

Les deux équipes rouges se recouvrent sur quatre points (k = 3, scission 48/12, défauts plantés, permutation non aveugle). Je les traite une fois, en citant les deux identifiants.

### Acceptées sans réserve

**B A-1 (seuil d'un écart).** Accepté. Pour une différence entre deux courses indépendantes, l'ET est multipliée par √2 : 36 tâches → 0,102, seuil 2 ET ≈ 0,20 ; 24 tâches → 0,125, seuil ≈ 0,25 — **VÉRIFIÉ (recalcul)**. Ma phrase « le cadre inclut une marge pour les graines » était fausse : le 0,2 du cadre est le facteur √2 seul, et ne contient aucune marge pour les graines. Conséquence : en contrôle de délégation, à une course par objet, un écart de 0,25 (6 tâches sur 24) est le minimum lisible contre le seul bruit de tâches — c'est pire que ce que j'écrivais.

**B A-4, C 2 (scission 48/12).** Accepté, et la scission est abandonnée. Trois raisons cumulées, toutes justes : (i) le score agrégé rendu à l'organisme est dans les journaux, donc 12 = agrégat − 48 ; (ii) l'organisme s'adapte aux 12 puisqu'elles entrent dans son signal ; (iii) 12 tâches ont une ET ≈ 0,125, soit un seuil de différence ≈ 0,35 — **VÉRIFIÉ (recalcul)**. Une garde sans puissance qui coûte 20 % de la banque n'est pas une garde. Remplacement en (b), E2′ (v3-bis).

**B A-7 ; B (c) 6 ; C 3 pour la partie dépense (E3 sans témoin à coût égal).** Accepté. Je reprends le témoin de C transmis par B : un vote d'appels simples au même plafond de jetons. Sans lui, E3 mesure le calcul dépensé.

**B A-8 ; B (c) 1 (`test` > `test_final` confondu par la sélection interne).** Accepté et transformé en test : l'écart `test` − `test_final` d'un organisme sans itération humaine (courses d'E1) devient la ligne de base ; seul l'excès au-dessus de cette ligne peut désigner la boucle (4). Voir E8′.

**B (c) 7 ; C (c) 1 (le contrôle « constant » ne sépare rien ; graine de génération vs graine d'appel).** Accepté. Mon contrôle constant ne testait que le déterminisme de la notation, et je n'avais pas dit ce que « même code » voulait dire. E1′ le précise : « même code » = code de départ, ronde 0, puisque l'objet mesuré est la course entière ; et un bras supplémentaire gèle l'organisme à la génération 0 pour séparer le bruit des appels du bruit des trajectoires de réécriture.

**B A-6 ; C évasion « permutation » ; C (c) 4 (le concepteur reconnaît la course permutée).** Accepté. Le contrôle par permutation tel que je l'avais écrit mesurait l'arrêt du concepteur, pas le sur-ajustement. Je reprends la correction de C : le bras permuté est itéré par l'organisme seul (ou par un correcteur automatique), à budget et consigne identiques, sans qu'un humain lise un texte ; et j'accepte qu'il ne donne qu'un plancher pour la partie automatisée de (4), jamais une soustraction du gain réel (point B).

**C (c) 3 ; C évasion « outils inertes ».** Accepté. Un retour vide casse le format et fabrique l'écart. Le témoin devient un retour syntaxiquement plausible mais non informatif, généré hors ligne, de même longueur et de même format.

**C (c) 2 (ablation sémantique) ; B « tous à la fois » ; C « offuscation sémantique ».** Accepté, et c'est l'attaque la plus sérieuse des deux pièces : la trajectoire par défaut de (4) est un indice de surface stable entre graines, invisible aux canaris, propre à la relecture, transférable si la v6 sort du même générateur. Mes références de surface ne défendent que si l'indice exploité en fait partie — B le dit justement. J'adopte le contrôle de C : l'organisme final tourne sur une v3 dévitalisée (contenu lexical remplacé, structure des tours, longueurs et métadonnées conservées). Voir E9′.

**B, « points où A et C échouent ensemble » — lecture humaine de `test_final`, générateur commun v3/v6, journal des lectures.** Acceptés tous trois. (i) Règle : personne ne lit `test_final` avant la fin du compteur d'itérations de la phase (4) ; une lecture unique, agrégée, consignée ; le noyau écrit `test_final` dans un fichier séparé, chiffré par une clé détenue par un tiers, pas dans le journal de course. (ii) Le générateur commun : réponse par E2′ (v3-bis, même générateur) et E9′ (ablation). (iii) Le journal consigne les lectures : chaque ouverture d'une trace par tâche passe par un lecteur du noyau qui l'enregistre (tâche, date, qui) ; un script de lancement qui trouve des lectures non consignées refuse de lancer.

### Acceptées avec transformation

**B A-2 ; C 1 (k = 3 ne tranche pas).** Accepté sur l'arithmétique — je retrouve les deux calculs : intervalle à 95 % pour σ de 0,52 s à 6,3 s (χ²₂ : 0,051 et 7,38) ; et P(s < 0,05 | σ = 0,10) = 1 − e^(−0,25) ≈ 0,22 — **VÉRIFIÉ (recalcul)**. Mes seuils 0,05 / 0,10 lus sur un s à 2 ddl ne falsifiaient rien ; B a raison de dire que ma zone grise contrevenait à B4. Transformation en deux temps : (1) à k = 3 par objet, E1′ est unilatéral : il ne peut que réfuter « le bruit entre graines est petit » ; au seuil unilatéral 95 % (χ²₂ à 0,95 = 5,99), la borne inférieure de σ est 0,58 s, donc s ≥ 0,087 réfute σ ≤ 0,05 — **VÉRIFIÉ (recalcul)**. Si s est petit, H_A n'est pas établie, elle est seulement non réfutée, et je le dis ainsi. (2) Pour rendre le duel bilatéral, on met en commun les 4 strates (2 organismes × 2 familles, k = 3 chacune) sous l'**HYPOTHÈSE** d'un σ commun : 8 ddl, χ²₈ à 0,05 et 0,95 = 2,73 et 15,5 ; bornes 0,72 s et 1,71 s ; s > 0,070 réfute σ ≤ 0,05, s < 0,058 réfute σ ≥ 0,10 ; entre les deux, zone grise déclarée d'avance et qui déclenche k = 5 — **VÉRIFIÉ (recalcul)** pour les quantiles, **HYPOTHÈSE** pour le σ commun. L'hypothèse de σ commun est forte : l'organisme qui réécrit sa récompense peut être plus dispersé. Elle est elle-même testée par le rapport des s entre organismes (test F à 2/2 ddl, qui ne verra qu'un rapport > 19 — **VÉRIFIÉ (recalcul)** ; donc elle restera le plus souvent non réfutée, et je le consigne comme limite).

**B A-3 (faible variance ≠ valeur).** Accepté sur le fond, transformé : E1′ ne porte que sur la lisibilité des comparaisons, et son résultat ne vaut que pour un organisme qui bat les références de surface sur la même part ; un organisme sous les références n'est pas un objet à comparer, quelle que soit sa variance. Les deux contrôles de B (re-notation double ; organisme gelé à température réelle) remplacent mon contrôle constant.

**B A-5 (E2/E6 consomment la v6).** Accepté pour la famille tenue à l'écart ; rejeté quant à l'idée que je voulais apprendre n sur la v6 — mais mon texte le permettait, donc la faute est mienne. Transformation : le nombre d'itérations n est fixé par le budget avant la première itération, pas par E2 ; E2′ mesure le transfert v3 → v3-bis (tirage neuf du même générateur, même famille, construit par quelqu'un qui n'a pas lu les scores) ; la famille v6 tenue à l'écart n'est lue qu'une fois, en confirmation, après déclaration de ce que les auteurs ont lu. B a aussi raison que E2 confondait sur-ajustement et différence de famille : v3-bis sépare les deux (même famille, tâches neuves).

**B A-9 ; C 4 (défauts plantés par les mêmes esprits ; E4 asymétrique).** Accepté. Pour E4 : zéro divergence sur 6 laisse un taux jusqu'à ≈ 0,39 à 95 % — **VÉRIFIÉ (recalcul)** ; E4′ devient unilatéral et chiffré en coût (voir (b)). Pour E5/E7 : la moitié des défauts plantés viendra d'une source extérieure à l'équipe de défense — les corrections réellement faites par conv-audit sur du code Gemini, si cet historique existe (**à vérifier**) ; sinon, un troisième modèle qui n'a lu ni le noyau ni les consignes d'audit plante les siens. Un vrai défaut inconnu compté comme fausse alerte (B) : toute « fausse alerte » est contre-expertisée avant d'être comptée, et si elle est fondée, elle est reclassée en découverte, ce qui est la meilleure issue possible de l'instrument.

**B (c) 4 ; C 5 ; B et C évasions « canaris ».** Accepté sur trois points : « quelques » n'était pas un nombre ; avec 6 canaris, exploiter 5 sur 6 donne p ≈ 0,11 (7/64) — **VÉRIFIÉ (recalcul)** ; des canaris au contenu non informatif sont repérables. Transformation : (i) les canaris ne comptent pas dans le score rendu à l'organisme (répond à C 5 sur la dégradation du signal) ; (ii) leur nombre est fixé à ≥ 10 par part (illustratif) et ils sont construits en dupliquant des tâches ordinaires avec une étiquette inversée portée seulement par le canal illégitime, ce qui les rend indiscernables au contenu — contrôle de B (c) 4 : un classifieur trivial ne doit pas les distinguer mieux que le hasard. (iii) J'accepte la limite résiduelle : les canaris ne voient qu'une exploitation uniforme du canal ; la vraie garde est structurelle (métadonnées supprimées, ordre tiré au sort à chaque génération, gigue ajoutée aux latences), et les canaris n'en sont que le moniteur.

**C 3 (E6 confondu : l'humain lit les textes, le bras graines ne le peut pas).** Accepté à moitié. La lecture des textes par l'humain est constitutive de (4) : E6 mesure la boucle humaine avec ses fuites, c'est voulu. Mais C a raison que, si H_A gagne, on ne saura pas si le gain est une correction ou une heuristique injectée. Transformation : E6′ évalue les deux bras sur trois jeux — v3 (lu), v3-bis (même générateur, neuf), famille v6 tenue (autre famille, une seule fois). Une heuristique propre aux 60 textes ne passe pas v3-bis ; une heuristique propre au générateur passe v3-bis mais pas v6 ; une correction réelle passe les deux. E9′ (ablation) complète.

### Rejetées, avec raison

**C, évasion « journal » (l'attente vague ; 10 pas d'adaptation interne pour une entrée).** Rejeté sur le second point : le journal n'a jamais prétendu borner les degrés de liberté *de l'organisme* ; ceux-là sont l'objet mesuré. Il borne ceux de l'expérimentateur. Accepté sur le premier : l'entrée doit contenir une attente chiffrée (famille, sens, taille en ET) ; une attente sans nombre est refusée par le script.

**C, évasion « split-brain » sur la taille en octets et l'ordre.** Rejeté en partie : la taille en octets est une propriété du contenu, pas une fuite de vérité, et toute référence de surface la mesure déjà ; l'ordre d'arrivée est tiré au sort par génération dans le dessin § 4. Accepté pour la latence : le noyau ajoute une gigue, et c'est un essai du noyau avant toute course sous la lecture (1).

**C, « Grand Chelem » — le point 6 (E3 en dernier produit l'illusion du gain).** Rejeté comme enchaînement : mon § 6 plaçait E3 en dernier et le conditionnait aux essais du noyau ; mais accepté comme contenu, puisque chacun des maillons 1 à 5 est une faille reconnue ci-dessus. La réponse n'est pas de contester le scénario, c'est E9′ et v3-bis comme portes avant toute v6.

---

## (b) Expériences corrigées (toutes HYPOTHÈSE ; seuils illustratifs, consignés dans le journal avant lancement)

Convention commune : exactitude par famille et par part ; différence entre deux courses lue contre 2 ET_diff (0,20 / 0,25) ; références de surface (classe majoritaire, longueur, mots-clés) calculées sur chaque part et chaque jeu, y compris v3-bis et v6 (contrôle B (c) 5) ; aucune comparaison n'est rapportée sans elles.

**E1′ — Variance entre graines (lisibilité).**
- Objet : course entière depuis le code de ronde 0, même noyau, même banque, même ordre de tâches, graines différentes ; k = 3 par organisme du pilote 4 ; mise en commun des 4 strates.
- H_A : σ_graine ≤ 0,05 (les comparaisons à une course sont lisibles au seuil 2 ET_diff). H_B : σ ≥ 0,10.
- Décision : s_commun > 0,070 réfute H_A ; s_commun < 0,058 réfute H_B ; entre les deux, k passe à 5 (coût 2 × 2 courses de plus, ≈ 120–220 USD dérivés du cadre) avant toute itération.
- Contrôles : re-notation double des mêmes sorties (déterminisme de la notation, s attendu 0) ; organisme gelé à la génération 0, k = 3, température réelle (bruit des appels seul) ; l'écart entre ce s et le s de la course entière est le bruit de trajectoire (C (c) 1).
- Ce que falsifie chaque issue : H_A réfutée → toute lecture à une course par objet, y compris la lecture du pilote 4 cette nuit, est réfutée comme méthode, et le budget va aux graines ; H_B réfutée → l'objection « la variance entre graines domine » est réfutée pour ces organismes et cette banque, et la lecture à une course redevient admissible au seuil √2.
- Limite déclarée : l'hypothèse de σ commun ; si le rapport des s entre organismes dépasse 19 (F à 2/2 ddl), elle tombe et chaque organisme est traité seul, en mode unilatéral.

**E2′ — Transfert v3 → v3-bis (sur-ajustement adaptatif, famille constante).**
- v3-bis : 60 tâches neuves du même générateur, mêmes familles, construites par quelqu'un qui n'a lu ni scores ni erreurs ; jamais rendues à l'organisme ; lues une fois en fin de phase.
- H_A : Δv3-bis ≥ 0,5 × Δv3 et Δv3-bis > 2 ET_diff. H_B : Δv3 > 2 ET_diff et Δv3-bis < 1 ET_diff.
- Plancher : Δ_perm obtenu par l'organisme seul itérant sur étiquettes permutées, même budget, sans lecture humaine (C (c) 4). Δv3 ≤ Δ_perm → non interprétable.
- Falsification : H_B → la phase (4) telle que pratiquée est réfutée comme source de connaissance (adaptation aux 60 textes) ; H_A → l'objection de sur-ajustement aux textes est réfutée pour ce n, sans rien dire du transfert entre familles, qui reste à la confirmation v6.

**E3′ — Outils (lecture 1), reportée après les essais du noyau.**
- Quatre bras, 3 graines chacun : outillé ; outils à retour plausible non informatif (C (c) 3) ; vote d'appels simples au même plafond de jetons (témoin de C) ; appels simples nominaux.
- H_A : outillé > témoin à dépense égale de ≥ 2 ET_diff sur ≥ 2 graines sur 3, canaris au hasard, et outillé > retour plausible. H_B : l'un des trois écarts manque.
- Ajout (B (c) 6) : tâches à injection plantée ; l'agent outillé doit garder son exactitude à ± 1 ET ; sinon l'isolation par le contenu est réfutée, indépendamment du gain.
- Falsification : H_B → la lecture (1) est réfutée comme objet de pilote prioritaire ; H_A → « les outils n'ajoutent que du calcul » est réfutée.

**E4′ — Essai réel court (lecture 2), unilatéral.**
- Sur N lancements (N non borné d'avance ; chaque lancement consigne simulation et réel), on compte les divergences. Une divergence réfute « (2) est inutile ». Zéro sur N n'établit rien tant que la borne supérieure 1 − 0,05^(1/N) dépasse le rapport coût de l'essai court / coût d'une course perdue — c'est ce rapport, et non N, qui ferme l'expérience.
- Contrôle : défaillance connue injectée (clé invalide, budget nul) ; si l'essai court ne la voit pas, il ne mesure rien.

**E5′/E7′ — Attaquants et relecture.**
- Défauts : p = 8 (illustratif), dont ≥ 4 d'origine extérieure à l'équipe de défense (historique conv-audit si existant, **à vérifier** ; sinon tiers modèle aveugle). Mesure : détection et fausses alertes, chaque fausse alerte contre-expertisée.
- H_A / H_B inchangées ; mais une détection > 70 % sur les seuls défauts « maison » et < 40 % sur les extérieurs est consignée comme réfutation de l'instrument, pas comme succès partiel.
- Les deux instruments ne prétendent pas voir une règle de récompense dégénérée en détecteur de surface (C) ; c'est E9′.

**E6′ — Itérer ou répliquer, à budget égal.**
- Bras 1 : m itérations humaines de (4) sur v3 ; bras 2 : m graines de l'organisme non corrigé, meilleure graine choisie sur `test`. Évaluation sur v3, v3-bis, puis famille v6 tenue (lecture unique).
- H_A : bras 1 > bras 2 sur v3-bis de ≥ 2 ET_diff, et l'avantage se retrouve sur v6. H_B : égalité sur v3-bis, ou avantage sur v3-bis disparaissant sur v6 (gain propre au générateur).
- Falsification : H_B → (4) est réfutée comme méthode distincte de la sélection sur le bruit, ou n'apporte qu'une adaptation au générateur ; H_A → l'objection « (4) n'est que de la sélection » est réfutée.

**E8′ (nouveau, de B (c) 1) — Ligne de base A/A de `test` − `test_final`.**
- Sur les courses d'E1′ (aucune itération humaine), lecture unique agrégée de `test_final`, consignée.
- H_A : l'écart n'est pas lisible (< 2 ET_diff). H_B : il l'est.
- H_B → le signal « `test` > `test_final` » de mon tableau (c) est réfuté comme mesure de la boucle (4) : la sélection interne suffit à le produire ; H_A → l'objection A-8 est réfutée pour cet organisme, et tout excès ultérieur au-dessus de cette ligne devient imputable à (4).

**E9′ (nouveau, de C (c) 2) — Ablation sémantique.**
- L'organisme final issu de (4) tourne sur une v3 dévitalisée (contenu remplacé par des pseudonymes ou traduction en boucle ; structure, longueurs, métadonnées conservées).
- H_A : exactitude au hasard ± 2 ET (l'organisme lit le fond). H_B : exactitude maintenue au-dessus du hasard (artefact de surface).
- H_B → toute valeur mesurée en (4) pour cet organisme est réfutée, quel que soit son score v3 ; H_A → l'objection « indice de surface » est réfutée pour les traits conservés par l'ablation, et seulement ceux-là (une ablation plus agressive reste possible).

**Gardes transversales corrigées.** Journal : lancements *et* lectures, attente chiffrée obligatoire, hachages de code/noyau/banque/graine. `test_final` : fichier séparé, clé tierce, lecture unique en fin de compteur. n fixé par le budget avant la première itération. v3-bis construite avant la première itération. Canaris : ≥ 10 par part, indiscernables au contenu, hors score rendu. Ordre de tâches tiré au sort, latences avec gigue, métadonnées supprimées : trois essais du noyau avant toute course sous (1).

---

## (c) Réponse à l'arbitre

**Ce qui est établi (au sens : vérifié par recalcul, ou admis par les trois cellules).**
- Les ordres de grandeur du cadre sont justes : ET ≈ 0,072 (36 tâches) et ≈ 0,088 (24), et pour une *différence* entre deux courses uniques, les seuils à 2 ET sont ≈ 0,20 et ≈ 0,25. À une course par objet, aucune différence inférieure n'est lisible, avant même de compter le bruit entre graines.
- Trois courses identiques ne permettent pas d'estimer l'écart type entre graines avec une précision utile ; elles peuvent seulement réfuter « ce bruit est petit » s'il est grand. Toute règle de décision qui lit un s à 2 ddl comme une mesure est fausse.
- Un sous-ensemble tenu de 12 tâches n'a aucune puissance et fuit par soustraction : la scission 48/12 est morte.
- La trajectoire par défaut d'une boucle « tourner, regarder, corriger, relancer » sans scellement n'est pas la fraude : c'est la dérive vers un indice de surface stable entre graines, invisible aux canaris et à la relecture, et transférable à toute banque issue du même générateur. Ni le journal, ni la relecture, ni les canaris ne le voient. Seules l'ablation sémantique (E9′) et une banque neuve du même générateur (v3-bis) le voient.

**Ce qui n'est pas établi.**
- La variance entre graines, la variance entre trajectoires de réécriture, le taux de base de chaque famille, la corrélation entre tâches de la v3 : rien de cela n'a été mesuré, et aucune lecture du pilote 4 ne devrait être rapportée sans ces inconnues en face.
- Que la relecture remplace ce que le scellement protégeait : non établi, et E7′ ne le testera que sur des défauts d'un certain type.
- Que les quatre lectures aient un ordre : ce que je maintiens, c'est seulement que (1) n'a pas de sens avant E1′ et les essais du noyau, et que (2) et (3) sont des instruments à qualifier (E4′, E5′) avant d'être recommandés ou écartés ; la position de conv-audit sur (2) et (3) n'est ni établie ni réfutée.
- La valeur de (4) elle-même : non établie. E6′ est l'expérience qui la départage de la sélection sur le bruit, et elle coûte deux fois m courses.

**Ce qui entre dans le pilote 4 cette nuit sans changer l'objet.** Une entrée de journal avec attente chiffrée avant lecture ; une troisième course de chaque organisme (graine différente) si le budget le permet, sinon de l'organisme simple ; `test_final` écrit à part et non lu ; aucune correction de l'organisme avant que v3-bis existe.

**L'expérience à faire en premier : E1′, avec ses deux contrôles, et E8′ qui ne coûte rien de plus.** Raison : tout le reste — le pilote 4, chaque itération de (4), E2′, E6′, E3′ — se lit contre un bruit dont on ignore la taille, et E1′ est la seule expérience dont l'issue défavorable (H_A réfutée) rend inutile la dépense de toutes les autres à une course par objet. Son coût (≈ 120–220 USD dérivés du cadre pour 4 courses supplémentaires, davantage si la zone grise impose k = 5) est du même ordre qu'une seule itération de (4) ; une itération faite avant E1′ ne pourra pas être lue. Ce qu'il faudrait savoir avant de la lancer : le budget total de la phase (4), sans lequel n n'est pas opposable, et qui construira v3-bis sans avoir lu les scores.

FIN-DE-CELLULE