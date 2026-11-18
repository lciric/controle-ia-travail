# Contre-lecture de l'ordre exploratoire (brouillon 3), du devis (brouillon 3) et de la note des points à trancher du saboteur à budget — v1

> Contre-lecture (R2) de pièces d'une course **exploratoire, non opposable (R-522)**. Processeur seulement. Rien n'a été lancé sur une carte. Rien n'a été dépensé. Aucun modèle n'a été chargé. Aucune clé n'a été lue. Aucun fichier existant n'a été modifié. Ni commit, ni poussée.
>
> **Contre-lecture interrompue au premier refus d'un crochet (§ 9).** Tout ce qui suit a été vérifié avant ce refus. Après lui, je n'ai rien rejoué, rien reformulé, rien contourné : j'ai seulement écrit et scellé ce rapport. La liste de ce qui restait à vérifier est courte et écrite au § 9.
>
> Ce rapport nomme le mécanisme de l'agent de test. Il va au rédacteur des corrections. La session mère n'a besoin que du message final.

## 0. Identité

- **Contre-lecteur** : sous-agent neuf de la session mère `session_013QMayjsoZJFBUCqcnvD5h1`. Modèle : Claude Fable 5.2 (`claude-fable-5-2`). Le rédacteur était Claude Opus 5.5 : même famille, autre modèle. Je n'ai écrit ni la conception, ni le code, ni l'ordre, ni le devis, ni la note.
- **Mandat** : `docs/notes/barreau8-iib-v1/mandat-contre-lecture-ordre-et-devis-iib-v1.md`, empreinte `b2391726aa9a10641c8db1060892e8623af8e32f50dacaa925b50a5887d86b3b`, vérifiée avant toute autre lecture.
- **Heures** (`date -u`) : début vers 2026-11-18T19:36Z ; dernière heure relevée avant le refus : 19:50:28Z ; rapport écrit ensuite.
- **Code lu** : `origin/prep/iib-code-v3`, tête `d88e3d947ec4f05958834e2746a800c854271a8f` après `git fetch origin prep/iib-code-v3`. C'est la tête que lisent aussi le brouillon 3 et la vérification courte : elle n'a pas avancé.
- **Arbre courant** : branche `claude/affectionate-bardeen-j7kddp`. Sa tête a bougé pendant ma lecture (commits de la session mère, non lus).
- **Je suis exclu de toute lecture des sondes du barreau 8.**

| pièce | empreinte vérifiée | lu |
|---|---|---|
| ordre, brouillon 3 | `eed42f07329c5f064554b799f0d49ff0a1ed6e4571545c94dca3d6783f0c165f` | en entier |
| devis, brouillon 3 | `016979ba01926f08be8ac243df75b716cf49ea63ea01e16dedd4302e61f991d4` | en entier |
| note des points à trancher | `66cd18dff444baba2e247706939635e5f70150e88ec8db4b28e14ce12b515a44` | en entier |
| ordre, brouillon 2 | `4c083d75…a407`, égale au compagnon | en entier |
| conception, brouillon 2 | `47b86258…209c`, égale au compagnon | en entier |
| script d'arithmétique `calcul-devis-ii-b-v2.py` et sa sortie | `d869c8e8…f30f`, `abe794be…0ff2` | en entier ; **rejoué** |
| contre-lecture du code v2 | `8e5078e9…56fe`, égale au compagnon | § 0, 1, 3 à 7 ; table des constats lue tronquée |
| vérification courte du code v3 | `e5c31d4f…0f3a`, égale au compagnon | en entier |
| ligne d'accord `GO-2026-11-10-08` de `registres/go.md` | — | cette seule ligne, par recherche de la clé en tête de ligne |
| code, tête `d88e3d94` | — | `iib/configuration_v1.py`, `iib/session_v1.py`, `iib/lanceur_v1.py`, `iib/episodes_v1.py`, `scripts/lancer_iib_v1.sh`, `scripts/amorce_instance_iib_v1.sh` en entier ; `iib/tours_v1.py` l. 1 à 135 ; `iib/modele_v1.py` l. 1 à 140 ; `iib/jouet_v1.py` l. 150 à 185 |

**Non ouverts** : les deux fichiers de consigne privée et leurs compagnons ; `iib/lecture_v1.py` et les deux scripts de lecture (ils portent la base textuelle de la seconde lecture) ; `src/controle_ia/bases/` ; `prereg/T0.6-*`, `prereg/T0.8-*` ; les relevés `releve-*` ; tout `diag/`, `runs/`, `donnees/`, `docs/verdicts/`.

## 1. Verdicts

- **Ordre : « scellable après corrections ».** 1 bloquant, 6 majeurs, 13 mineurs. Il reste aussi 18 marqueurs en attente, ce qui est prévu. Les commandes du § 5 sont justes contre le code v3. Elles devront être relues une fois de plus, brièvement, au commit de lancement, qui n'existe pas encore.
- **Devis : « demandable après corrections ».** 2 majeurs, 6 mineurs. L'arithmétique rejouée est identique à l'octet. La variante « ligne de 60 dollars, coupure à 55 » est acceptée par la garde du code, sur le registre entier. Le pire cas tient sous la ligne. L'échéance du 27 laisse le temps de la course si l'instance est créée le 25 avant 23:00 UTC.
- **Note des points à trancher** : claire, au format de décision. 3 majeurs : deux défauts de 48 heures qui trancheraient à la place de Lazar une condition de sa ligne de dépense, et un point manquant.

Les deux constats du rédacteur sont **exacts** (§ 5 et § 6).

## 2. Constats

Gravités : **bloquant** = rien n'est scellé ni demandé avant ; **majeur** = à corriger avant le scellement ou l'inscription ; mineur = à corriger ou à consigner. Références « fichier:ligne » à la tête `d88e3d94`.

| identifiant | gravité | où | constat |
|---|---|---|---|
| **B1** condition de la ligne d'accord non tenue, avec défaut de 48 heures | **bloquant** | ordre § 4 point 7 ; devis § 8 ; note, point 2 | La ligne d'accord dit « avec l'activité interne enregistrée ». L'ordre, la conception et le code n'enregistrent rien (§ 5). Le rédacteur le signale. Mais la note propose un défaut : sans réponse sous 48 heures, la ligne serait lue autrement que sa lettre et la course partirait. Une dépense est un nœud de décision : on s'arrête et on attend le mot. Le défaut de 48 heures ne vaut que pour les décisions « proposer avec recommandation ». |
| **O-M1** ligne de progrès des épreuves jamais relayée | **majeur** | ordre § 4 bis point 6, § 5 étape 3 ; `iib/lanceur_v1.py:292` ; `scripts/amorce_instance_iib_v1.sh:243`, `:398-400` | Le lanceur écrit `PROGRES … etape=epreuves echec=aucun`. Le relais de l'amorce retient toute ligne qui porte « echec » (filtre hérité de la chaîne précédente). La ligne n'atteint donc jamais la surveillance. Vérifié en passant sept lignes de la forme du lanceur dans les deux motifs de l'amorce : les deux lignes des épreuves sont retenues, les cinq autres relayées. L'ordre fait reposer sur cette ligne le constat « six épreuves passées » exigé par la ligne d'accord. Aucun des deux rapports sur le code ne le relève : l'essai de l'amorce joue un faux lanceur. |
| **O-M2** ordre des préalables ; cercles des marqueurs | **majeur** | ordre § 1 (entropie), § 4, § 11 ; `iib/configuration_v1.py:226-266` | Le mode réel refuse la configuration tant qu'un des 30 marqueurs manque. La configuration est commise avant le scellement de l'ordre (l'ordre cite son empreinte et le commit de lancement). Or le § 4 place après elle des faits qu'elle exige : entropie (« tirée au scellement de l'ordre »), ligne de création de 7b, exécutante, lecteur, version de l'outil de location, mot de Lazar pour la création, longueurs de la consigne. Trois vrais cercles : (a) le mot de Lazar « dans la session de l'exécutante » vient après la remise, donc après la configuration ; (b) les longueurs de la consigne, si elles ne sont mesurées que sur l'instance, viennent après la création ; (c) l'ordre ne peut pas porter sa propre empreinte, alors que le § 11 exige zéro marqueur au scellement. Un commit de lancement refait n'est pas gratuit : l'ordre exige un enfant direct du commit du code revu, sur la même branche. |
| **O-M3** valeurs libres de la configuration absentes du § 2 | **majeur** | ordre § 2, § 4 point 3 ; `iib/configuration_v1.py:93-96`, `:322-351` ; `iib/jouet_v1.py:155-185` | Le § 4 dit « écrite par la mère avec les valeurs du § 2 ». Le § 2 ne donne pas des clés que le code exige : `offre.telechargement_go_prevu` (elle fixe l'heure de coupure de la minuterie), `memoire_vive_min_go`, `agent.nom`, `agent.variables_gabarit`, `carte.relance` (exigée même en variante B), `code.branche` et `code.commit`. Le code ne vérifie pas ces valeurs à l'égalité. Personne ne relit la configuration une fois écrite. Un gabarit existe (`config_reelle_factice("B")`) : l'ordre ne le cite pas. |
| **O-M4** défaut de poussée de l'amorce : correction juste, à compléter | **majeur** | ordre § 7 (point R-A), § 5 étape 5 ; `scripts/amorce_instance_iib_v1.sh:261-263`, `:440` | Constat exact (§ 6). La correction proposée couvre les trois chemins de consignation. Elle laisse deux trous : le contrôle de fin reste aveugle aux fichiers ignorés ; au rapatriement, un fichier listé et absent est « rapporté » sans que la destruction soit suspendue. |
| **O-M5** deux clonages entiers du dépôt à l'étape 1 | **majeur** | ordre § 5 étape 1 | Mesuré : 7,44 Gio d'objets et 3,01 Go d'arbre par clonage entier, soit environ 20 Go pour les deux. La machine où je tourne a 6,5 Go libres. Le contrôle de place du lanceur n'exige que 3 Go. L'étape échoue avant toute dépense, mais elle n'est pas exécutable telle quelle sur une machine comme celle-ci. Les chemins utiles au lanceur pèsent 0,2 Go. |
| **O-M6** dernière commande de création | **majeur** | ordre § 1, § 5 étape 2 ; devis § 7 (D-M1) ; `scripts/amorce_instance_iib_v1.sh:320` ; `t06/session_v3.py:132-134` | L'amorce rejoue le calendrier sur l'instance, à l'heure de l'instance. Rejoué : au 26, refus (« dernier jour de création dépassé »), donc destruction. Une instance créée le 25 peu avant minuit démarre le 26 et se détruit. La fenêtre de recherche dure 2 h 45. |
| **D-M1** exemple de la dernière création | **majeur** | devis § 7 ; note, point 1 | Le devis écrit « une création le 25 à 23:59 finit P1 vers le 2026-11-27T09:18Z ». L'arithmétique est juste ; le code refuserait cette course (O-M6). |
| **D-M2** les deux branches de l'activité interne non chiffrées | **majeur** | devis § 8 | Le devis met « toute capture ou tout recalcul d'activations » hors devis, sans chiffre. Il doit être inscrit en complément d'une ligne qui dit « avec l'activité interne enregistrée ». Lazar ne peut pas choisir sans les deux coûts (§ 5.2). |
| **N-M1** point 4 : défaut de 48 heures ; mots prêtés à Lazar | **majeur** | note, point 4 | « Six épreuves passées » avant que la course parte est une condition écrite dans la ligne de dépense. Un défaut de 48 heures la relirait. De plus la note dit « ta phrase » : ces mots sont la lecture de la mère écrite dans la ligne, pas le mot de Lazar. Le devis, § 0, le dit justement. |
| **N-M2** point manquant : « 7b d'abord » contre le 25 | **majeur** | note ; ordre § 3, § 4 point 5 ; `iib/session_v1.py:79-92` | Le code refuse toute création sans la ligne de création de 7b au registre des décisions. Le brouillon 3 la laisse en attente. La note n'en dit rien. Si 7b n'est pas créée le 25, la course ne peut pas partir sous cette ligne. Je ne connais pas l'état de 7b (registre non lu). |
| **N-M3** point 2 : « exacte », coûts absents, texte de la décision citée absent | **majeur** | note, point 2 | (a) « se recalcule de façon exacte » est trop fort : mêmes jetons, mêmes poids, mais une autre passe, sur une autre machine ; égal aux arrondis du calcul près, pas au bit. (b) Aucun coût n'est donné pour les options. (c) La ligne cite « D-4, option (a) » ; ni le rédacteur ni moi ne l'avons lue. Lazar doit voir le texte qu'il a accordé. |

### Mineurs

| identifiant | où | constat |
|---|---|---|
| O-m1 | ordre § 5 étape 6 | « la minuterie détruit d'elle-même à partir de 2026-11-27T22:00:00Z » n'est vrai que si l'instance tourne. Après une fin normale l'instance est arrêtée : la minuterie ne tourne plus, la surveillance est sortie. La destruction avant la fin de la ligne repose sur l'exécutante seule. |
| O-m2 | ordre § 5 étape 1 | L'amorce refuse si la branche `essai/iib-explo-v1` existe déjà sur le distant, après la création. Le lanceur ne le contrôle pas avant. Relevé aujourd'hui : absente. |
| O-m3 | ordre § 5, « Variables communes » | `$ENVI` est défini avant `REGGO` et `REGDEC`, qu'il emploie. Écrit comme une chaîne, il se découpe mal. |
| O-m4 | ordre § 2, ligne « épreuves » | « code `tours_v1.py` l. 58-59 » : à la tête `d88e3d94`, le quantile 0,025 est aux lignes 60 et 61 (fonction `difference_par_taches`). La borne bilatérale est bien celle du code. |
| O-m5 | ordre § 8 | Le contre-lecteur de l'ordre et du devis manque à la liste des exclus. |
| O-m6 | ordre § 5 étape 3 | L'oracle de l'évaluation n'écrit qu'une ligne de progrès, à sa fin : 2 560 actions. À 3 secondes par action, 2,1 heures de silence ; 4,3 heures au pire cas. L'alerte « deux heures sans ligne » est donc attendue. |
| O-m7 | ordre § 4 point 5 | La garde exige l'extrait de la ligne de 7b **une seule fois** au registre des décisions. Recopier l'extrait sur une autre ligne (en consignant la valeur du marqueur) ferait refuser la création. |
| O-m8 | ordre § 11 | `BRANCHE_CODE_IIB` est « rempli » : vrai seulement si le code revu reste sur `prep/iib-code-v3`. `CHEMIN_DEVIS_IIB` et `EMPREINTE_DEVIS_IIB` retombent en attente si un brouillon 4 du devis est écrit. |
| O-m9 | ordre § 3, § 6 | Deux raccourcis par rapport au brouillon 2 : les règles des gardes « jumeau à dose 0 », « base intacte », « état d'adaptateur par lot » ne sont plus écrites ; « aucun réglage de b, de F, de la consigne ni des tours en cours » a disparu du § 6. |
| O-m10 | ordre § 3, titre | « chacune éprouvée sur un cas sain et sur un artefact » n'est pas vrai à `d88e3d94` : deux artefacts manquent (l'ordre le dit lui-même). À dater du commit du code revu. |
| O-m11 | ordre § 5 étape 5 | Une interruption par la minuterie pendant une écriture peut laisser un fichier de données sans compagnon. Aucune règle. |
| O-m12 | ordre § 4 ter, J7 | Le débit n'est pas dit calculable sans lire un résultat. Il l'est : heures des lignes de progrès de l'étalonnage, divisées par 960 actions. |
| O-m13 | ordre § 7 | Les textes des actions entrent dans le dépôt privé. Je n'ai pas vérifié que le script de la copie publique écarte `donnees/*-iib-*` : question pour la mère. |
| D-m1 | devis § 6 | « heures de carte avant la coupure » : le code ajoute le prix du stockage au prix de l'offre (`t06/session_v3.py:95-100` ; l'offre est lue « stockage compris », `t06/session_v2.py:101-104`). Rejoué : 38,4 heures à 1,30 + 0,08, et non 40,8. Marge sur le pire cas : 5,1 heures. La colonne « 1,40 » du devis (37,9 heures, 4,5 heures de marge) en tient lieu : le pire cas reste couvert. |
| D-m2 | devis § 5, § 6 | Le plafond que les gardes tiennent n'est pas écrit : 55 (coupure) + au plus 0,9 (consignation bornée à 2 400 secondes, carte encore louée) + 3,84 (stockage à l'arrêt, 48 heures) = au plus 59,8 dollars, sous 60. Marge : 0,2 dollar. Au-delà de 48 heures d'arrêt, la ligne serait dépassée. |
| D-m3 | devis § 1 | 1,12 dollar par heure : « consigne de la mère », sans chemin. Les durées de 7a et les prix relevés sont cités par le devis précédent ; le rédacteur ne les a pas relus ; je ne peux pas les relire (résultats et préenregistrement hors de mon mandat). |
| D-m4 | devis § 6 | « P1 à 2,10 » couvert par la variante A : sans objet, le code borne le prix de la carte à 1,30 dans les deux variantes. |
| D-m5 | devis § 9 | La ligne d'engagement cite le commit du code ; elle doit citer le commit de lancement, celui qui tourne. |
| D-m6 | devis § 1 | Le script des essais du jetoniseur réel (ordre § 4 ter) et le second chargement du modèle qu'il demande ne sont pas comptés : quelques minutes. |
| N-m1 | note, points 1 et 5 | Le défaut y est l'état présent (ligne déjà accordée ; branche laissée telle quelle). L'écrire ainsi : « sans mot de toi, rien ne change ». |
| N-m2 | note, renvoi | Les réglages de la seconde lecture précèdent le commit du code revu : ils sont sur le chemin du 25. À dire. |
| N-m3 | note, point 3 | La liste des essais à faire avant la course doit recevoir O-M1 et O-M2. |

## 3. Couples avant → après

**B1.**
- Note, point 2. Avant : « **Défaut sous 48 heures** : (a), la mère consignant au registre que ta ligne est lue ainsi. » → Après : « **Pas de défaut.** Ta ligne porte ces mots et c'est une ligne de dépense. Sans ton mot exprès, l'ordre n'est pas scellé, le devis n'est pas inscrit, rien n'est créé. »
- Ordre, § 4 point 7. Avant : « Nœuds du directeur tranchés (note `noeuds-ii-b-pour-lazar-v1.md`), en particulier le point 2 (« activité interne enregistrée ») ; » → Après : « Nœuds du directeur tranchés (note `noeuds-ii-b-pour-lazar-v1.md`) ; les points 2 (« activité interne enregistrée ») et 4 (place des épreuves) le sont par un **mot exprès de Lazar**, consigné au registre des décisions, jamais par un défaut de 48 heures : ils portent sur les conditions de la ligne de dépense ; »

**O-M1.**
- Code, `iib/lanceur_v1.py:292`. Avant : `progres(etape="epreuves", echec=ep["echec"] or "aucun")` → Après : `progres(etape="epreuves", etat="arret" if ep["echec"] else "passees", epreuve=ep["echec"] or "aucune")`. Essai neuf (R5) : la ligne réelle du lanceur passe les deux motifs de l'amorce (sain) ; une ligne qui porte un mot interdit est retenue (artefact).
- Ordre, § 4 bis point 6. Avant : « ligne `PROGRES … etape=epreuves echec=aucun` relayée par la surveillance » → Après : « ligne `PROGRES … etape=epreuves etat=passees` relayée par la surveillance (clé renommée au commit du code revu : dans le code v3, le relais de l'amorce retient la ligne `… echec=aucun`) ». Sans changement de code : « première ligne `PROGRES … etape=episodes phase=maitre-tour1`, qui ne peut suivre qu'un passage des six épreuves ».

**O-M2.**
- Ordre, § 1, ligne « Entropie ». Avant : « tirée une fois par la mère par `numpy.random.SeedSequence()` au scellement de l'ordre » → Après : « tirée une fois par la mère par `numpy.random.SeedSequence()` **avant d'écrire la configuration**, donc avant le commit de lancement et avant le scellement de l'ordre, sans aucune donnée de la course ». Même mot au § 11.
- Ordre, § 4 : remettre les points dans l'ordre où ils peuvent se faire. (1) points à trancher par Lazar ; (2) code corrigé, contrôle court, commit du code revu ; (3) conception et devis scellés ; (4) faits de la remise connus de la mère : 7b créée et sa ligne, exécutante et lecteur désignés, version de l'outil relevée, mot de Lazar pour la création consigné, longueurs de la consigne, entropie tirée ; (5) configuration écrite, scellée, commise seule : commit de lancement ; (6) contrôles à blanc à ce commit (O-M3) ; (7) marqueurs de l'ordre remplis, vérification courte, scellement ; (8) ligne d'engagement, remise.
- Ordre, § 11. Avant : « `VERSION_VASTAI`, `EXECUTANTE_IIB`, `MOT_LAZAR_CREATION_IIB`, `LECTEUR_IIB` | en attente | remise par la mère » → Après : « … | en attente | la mère, **avant le commit de lancement** (la configuration les exige remplis) : version relevée par `vastai --version` ; nom de la session exécutante ; rôle du lecteur ; référence de la ligne du registre des décisions où la mère a consigné le mot de Lazar pour cette création. Lazar le redit dans la session qui dépense. »
- Ordre, § 11. Avant : « `LONGUEURS_CONSIGNE_IIB` | en attente | jetoniseur réel (§ 4 ter, J6) » → Après : « … | en attente | jetoniseur réel sur processeur, avant le commit de lancement ; si ses fichiers ne s'obtiennent pas sans dépense : valeur déclarée « mesurées sur l'instance, au journal (§ 4 ter, J6) », nombres au compte rendu ».
- Ordre, § 4 point 6 et § 11. Avant : « ordre scellé, marqueurs remplis (`<<CHEMIN_ORDRE_IIB>>`, `<<EMPREINTE_ORDRE_IIB>>`) » → Après : « ordre scellé, marqueurs remplis (son chemin et son empreinte vont à son compagnon et à la ligne d'engagement : un texte ne porte pas sa propre empreinte) ».

**O-M3.**
- Ordre, § 2, ligne « offre, carte ». Avant : « étiquette `iib-explo-v1` ; bornes du § 1 » → Après : « étiquette `iib-explo-v1` ; `offre` : disque 100 Go, 16 cœurs effectifs, 128 000 Mo de mémoire vive, stockage 0,08, téléchargement prévu **40 Go** à 0,05 (valeur du gabarit et du devis § 6, à confirmer) ; `carte.course` : « A100 SXM4 », 1,3, 80 000 Mo ; `carte.relance` : « H200 NVL », 4,7, 140 000 Mo (exigée par le code même en variante B, jamais employée) ; `memoire_vive_min_go` 128 ; `agent.nom` « 8B », `agent.variables_gabarit.date_string` « 26 Jul 2024 » ; gabarit : `iib/jouet_v1.config_reelle_factice("B")` ».
- Ordre, § 4 point 3, ajouter : « Après le commit de lancement, sans dépense : `session_v1 config` rend le code 0 ; la suite ciblée est rejouée à ce commit, même dernière ligne ; un lecteur qui n'a pas écrit la configuration relit ses valeurs libres contre cet ordre ; les commandes du § 5 sont relues à ce commit. »

**O-M4.**
- Ordre, § 7, point R-A, après « et leurs sceaux », ajouter : « et un contrôle de fin qui voit les fichiers ignorés (`git status --porcelain --ignored -- "donnees/$RUN"` vide, ou la liste `empreintes` de `resume.json`, ou `sorties_ecrites` de `arret.json`, comparée aux fichiers suivis) ; sinon fin anormale. L'essai tourne dans un dépôt qui porte la ligne `donnees/` du `.gitignore`. »
- Ordre, § 5 étape 5. Avant : « tout fichier listé et absent de la branche est un écart, rapporté. » → Après : « tout fichier listé et absent de la branche, ou présent sans compagnon conforme, est un écart, rapporté à la mère ; **la destruction (étape 6) attend son mot**, au plus tard jusqu'à 2026-11-27T22:00:00Z. »

**O-M5.** Ordre, § 5 étape 1 : remplacer les deux clonages entiers par des extractions réduites. Forme proposée, **non éprouvée** (à jouer à blanc, sans dépense) : pour `main`, un clonage de profondeur 1 sans fichiers, puis l'extraction de `registres/go.md` et `registres/decisions.md` seuls ; pour le dépôt du lanceur, un clonage de profondeur 2 de la seule branche du code, extraction partielle de `scripts/`, `src/`, `.claude/`, `registres/`, puis `checkout --detach` du commit de lancement. Le lanceur lit le reste par `git show`. Écrire dans l'ordre la place libre exigée.

**O-M6 et D-M1.**
- Ordre, § 5 étape 2, « Fenêtre », ajouter : « Aucune commande `creation` après 23:00 UTC le 2026-11-25 : l'amorce rejoue le calendrier à l'heure de l'instance et se détruit si le jour a changé. »
- Devis, § 7. Avant : « **2026-11-25** : une création le 25 à 23:59 finit P1 vers le 2026-11-27T09:18Z » → Après : « **2026-11-25**, dernière commande de création à 23:00 UTC (l'amorce rejoue le calendrier sur l'instance et refuse un démarrage daté du 26) : une création le 25 à 23:00 finit P1 vers le 2026-11-27T08:19Z ». Même correction dans la note, point 1.

**D-M2.** Devis, § 8. Avant : « Toute capture ou tout recalcul d'activations (note des nœuds, point 2) : devis et GO à part, sous préenregistrement scellé à part. » → Après : la table du § 5.2 de ce rapport, marquée « ordres de grandeur du contre-lecteur, non mesurés », et la phrase : « Le choix est à Lazar (note, point 2). Ce devis chiffre la course sans enregistrement. »

**N-M1.** Note, point 4. Avant : « ta ligne dit que la course part « seulement après … les six épreuves de l'oracle passées ». » → Après : « ta ligne porte, dans la lecture que la mère y a écrite (ce ne sont pas tes mots), que la course part « seulement après … les six épreuves de l'oracle passées ». » ; « lecture de ta phrase où » → « lecture de cette phrase de la mère où » ; le défaut du point 4 → « Pas de défaut : condition écrite dans ta ligne de dépense. »

**N-M2.** Note, point neuf, à écrire par la mère, qui connaît l'état de 7b. Décision : que faire si 7b n'est pas créée le 25. Enjeu : le code refuse la création sans la ligne de création de 7b ; ta ligne d'accord finit le 27. Options : attendre 7b et laisser passer le 27 (une ligne neuve sera à demander) ; lever « 7b d'abord » (changement de code et de conception, contre-lecture) ; reporter l'échéance par une ligne neuve.

**N-M3.** Note, point 2.
- Avant : « l'activité interne se recalcule de façon exacte par une passe plus tard, sur une carte. » → Après : « l'activité interne se recalcule par une passe plus tard, sur une carte, à partir des mêmes textes et des mêmes adaptateurs : égale aux arrondis du calcul près, pas au bit près. »
- Avant : « une passe de carte plus tard, sur devis et accord à part (non chiffrée ici). » → Après : « une passe de carte plus tard, sur devis et accord à part (ordre de grandeur : 1 à 2 heures de carte, 2 à 5 dollars, non mesuré). »
- Options (b) et (c) : ajouter leur coût (§ 5.2). Joindre le texte exact de l'option (a) de la décision D-4.

**Mineurs, couples courts.**
- O-m1. Avant : « (la minuterie détruit d'elle-même à partir de 2026-11-27T22:00:00Z) » → Après : « (la minuterie ne détruit d'elle-même que si l'instance tourne encore à 2026-11-27T22:00:00Z ; une instance arrêtée n'a plus de minuterie : la mère pose un rappel daté du 2026-11-27T20:00Z) ».
- O-m2. Étape 1, ajouter : « `git ls-remote --exit-code origin refs/heads/essai/iib-explo-v1` rend le code 2 (branche absente) ; sinon arrêt ».
- O-m3. Définir `ENVI` après `REGGO` et `REGDEC`, en tableau : `ENVI=(env -i PATH="$PATH" …)`, puis `"${ENVI[@]}" bash scripts/lancer_iib_v1.sh …`.
- O-m4. « code `tours_v1.py` l. 58-59 » → « code `tours_v1.py`, fonction `difference_par_taches` (l. 60-61 à `d88e3d94`) ».
- O-m5. § 8, ajouter aux exclus : « le contre-lecteur de cet ordre et du devis ».
- O-m6. § 5 étape 3, ajouter : « pendant l'oracle de l'évaluation, jusqu'à 2,1 heures sans ligne (4,3 au pire) : alerte attendue, pas un incident ».
- O-m7. § 4 point 5, ajouter : « ne jamais recopier cet extrait sur une autre ligne du registre ».
- D-m2. Devis, § 6, ajouter la ligne : « plafond tenu par les gardes : 55 + au plus 0,9 + 3,84 = au plus 59,8 dollars ; l'instance arrêtée est détruite sous 48 heures ».
- D-m5. Devis, § 9 : « commit `<<COMMIT_CODE_IIB>>` » → « commit de lancement `<<COMMIT_LANCEMENT_IIB>>` (code revu `<<COMMIT_CODE_IIB>>`) ».

## 4. Point 1 du mandat : les marqueurs

Comptés par programme contre `configuration_v1.MARQUEURS` : 30 marqueurs au code ; 14 remplis ; 16 en attente ; 2 propres au brouillon. Aucun marqueur rempli ne reste entre chevrons dans le texte. Tous ceux en attente y restent.

| marqueur rempli | valeur | vérifié contre | juste ? |
|---|---|---|---|
| `GO_ID_IIB` | `GO-2026-11-10-08` | la ligne | oui |
| `PLAFOND_LIGNE_IIB` | `60` | la ligne ; la garde lit 60 | oui |
| `ECHEANCE_GO_IIB` | `2026-11-27` | la ligne ; la garde accepte le 27, refuse le 28 | oui |
| `REPLI_H200_PERMIS` | `non` | « A100 seule », « option B » ; la garde refuse la carte de repli en variante B | oui |
| `PLAFOND_CONFIG_IIB` | `55` | « coupure à 55 USD » ; la garde exige 55 en variante B (58 refusé) | oui |
| `DERNIER_JOUR_CREATION_IIB` | `2026-11-25` (proposé) | garde du calendrier : accepté le 25, refusé le 26 | oui, avec O-M6 |
| `FIN_GO_UTC_IIB` | `2026-11-28T00:00:00Z` | règle du code, rejouée ; 1 795 824 000 secondes | oui |
| `BRANCHE_CODE_IIB` | `prep/iib-code-v3` | la branche existe | oui, sous réserve (O-m8) |
| `EMPREINTE_LISTE_TESTS_IIB` | `847676ef…e3b6` | recalculée sur la branche ; égale à l'amorce, l. 370 ; 13 fichiers | oui, à relire au code revu |
| `FORME_JUGE_T08_SCELLEE` | `non` | `configuration_v1.py:307-309` refuse « oui » | oui |
| `CHEMIN_CONSIGNE_IIB` | chemin du brouillon 2 | le nom et son compagnon existent sur la branche (noms seuls) | oui |
| `EMPREINTE_CONSIGNE_IIB` | `9f8bbdef…90c1` | journal de rédaction v2, l. 50 ; les deux rapports sur le code | oui ; non recalculée par moi (fichier jamais ouvert) |
| `CHEMIN_DEVIS_IIB`, `EMPREINTE_DEVIS_IIB` | brouillon 3, `016979ba…91d4` | recalculée | oui, tant qu'aucun brouillon 4 n'est écrit |

Les 16 en attente et les 2 propres attendent bien un fait à venir. Qui les remplit est dit, sauf trois défauts (O-M2) : le moment de l'entropie, les quatre marqueurs « de la remise » que la configuration exige plus tôt, et l'empreinte de l'ordre dans l'ordre.

## 5. Point 3 (i) : « avec l'activité interne enregistrée »

### 5.1 Le constat est exact

- **La ligne** `GO-2026-11-10-08` porte ces mots deux fois : dans son périmètre et dans le mot de Lazar recopié. Elle cite « D-4, option (a) », que je n'ai pas lue.
- **La conception** (brouillon 2, écrite la veille de la ligne) : « aucune activation n'est même enregistrée » (§ 0) ; « aucune activation n'est enregistrée » (§ 6.3) ; elle range même l'absence d'activation parmi les gardes (§ 7, « Écart DT-4 »).
- **Le code v3** : toute clé de configuration qui nomme une sonde, une couche, une activation ou un crochet arrête (`configuration_v1.py:91`, `:104-116`) ; tout fichier dont le nom commence par `activations`, `sondes` ou `lecture-sondes` est refusé (`lanceur_v1.py:67`, `:147-149`) ; les épisodes sont joués sans crochet ni passe de capture (`episodes_v1.py:1-8`) ; le résumé écrit « aucune activation » (`lanceur_v1.py:437`) ; l'étape des morceaux de l'amorce est vide (`amorce_instance_iib_v1.sh:264`).
- **Ce que la course garde** : les identifiants de tous les jetons générés et les deux adaptateurs, « pour une lecture de sonde ultérieure sous préenregistrement scellé à part » (ordre, brouillon 2, § 7).

### 5.2 Les deux branches, sans trancher

Sources des chiffres : devis brouillon 3 et son calcul (rejoué) ; devis brouillon 2, § 1 (`959df451…`), pour deux faits de 7a qu'il cite : « 7a capturait des activations sur la moitié des actions », à 43,3 secondes par épisode, et « 43 s pour le commit des morceaux ». Architecture du modèle : taille cachée 4 096, 32 couches (publique, non relue sur pièce). Un vecteur en demi-précision : 8 192 octets. Actions : 2 560 à l'évaluation ; 7 360 au plus toutes phases (12 tours). **Tout ce qui suit est un ordre de grandeur, non mesuré.**

| | **A. Enregistrer pendant la course** | **B. Garder de quoi recalculer plus tard** |
|---|---|---|
| code, avant la course | Retirer ou assouplir trois gardes (clés, noms de fichiers, résumé). Reprendre la capture de la chaîne précédente dans les épisodes, ou ajouter une passe après l'évaluation. Rendre à l'amorce son étape des morceaux. Section neuve de la configuration. Essais sain et artefact pour chaque garde neuve. Contre-lecture neuve du code (R2). Conception (§ 0, 1, 6.3, 7) et ordre (§ 0, 2, 3, 7, 8) en version nouvelle. | Rien d'obligatoire. Utile : la correction du défaut de poussée (§ 6), pour que les identifiants par phase survivent à un arrêt. En option, une dizaine de lignes et un essai : écrire par épisode l'empreinte du contexte entier, pour prouver plus tard que le contexte rebâti est le même. |
| code, plus tard | — | Un script de passe (contexte rebâti par le code du commit de lancement, adaptateur et dose de chaque condition, capture, écriture), ses essais, sa contre-lecture. |
| décision préalable | Quoi enregistrer : quelles couches, quels jetons, quelle précision. C'est un choix du côté des moniteurs, que le côté de l'agent de test ne peut pas faire. Mise à l'écart des fichiers : scellés, non lus avant le préenregistrement et le verdict du test de transfert. | Aucune avant la course. Les mêmes choix se font plus tard, sous le préenregistrement. |
| disque | Un vecteur par action et par couche : 21 Mo par couche à l'évaluation, 60 Mo toutes phases ; 0,7 Go et 1,9 Go pour 32 couches. Tous les jetons générés (400 au plus par action) : 8,4 Go par couche à l'évaluation, 24 Go toutes phases. Le disque de l'instance (100 Go) tient quelques couches. Le dépôt, lui, ne reçoit que des morceaux de moins de 90 Mo : au-delà de 1 à 2 Go, il faut un autre chemin et un autre lieu. La machine où je tourne a 6,5 Go libres. | Deux adaptateurs d'environ 27 Mo chacun, identifiants et textes : quelques dizaines de Mo. Déjà au devis. |
| durée de carte | Capture pendant les épisodes, comme 7a : environ 0 heure de plus que le devis, qui n'a pris aucun rabais pour l'absence de capture ; une minute pour les morceaux. Passe après l'évaluation : 0,1 à 0,6 heure de plus (une passe par épisode, 256 à 736 épisodes). | 0 heure pendant la course. Plus tard, sur une location à part : 1,0 heure fixe (amorce, essais, modèle) et 0,1 à 0,6 heure de passes, soit 1,1 à 1,6 heure. |
| dollars | 0 à 1 dollar de plus, dans la ligne de 60. Le pire cas (52,5) monte d'environ 1,7 dollar avec la passe finale et reste sous la coupure. Le prix de l'envoi depuis l'instance n'est borné par aucune garde du code. | 0 dollar de plus dans la ligne de 60. Plus tard : 2 à 5 dollars attendus, environ 10 au pire (hôte deux fois plus lent, 48 heures d'arrêt, 40 Go), sur un devis et une ligne d'accord à part. |
| calendrier | Un tour de développeur, une contre-lecture et une vérification de plus, avant le 25. Ces sept jours portent déjà les corrections du code v3, la décision sur la seconde lecture, la création de 7b et le scellement. | Aucun effet sur le 25. |
| lettre de la ligne | Tenue. | Non tenue à la lettre : il faut un mot exprès de Lazar (B1). |
| ce que l'on a à la fin | L'activité interne telle que calculée pendant la location. | De quoi la recalculer : identifiants de chaque action, deux adaptateurs dans la précision sauvegardée (celle-là même qui a servi à l'évaluation, `lanceur_v1.py:359-365`), configuration et manifeste (commit, versions, graines), tâches et consignes scellées, modèle de base à sa révision figée. Les graines ne servent pas au recalcul : les identifiants fixent le texte. |
| risques propres | Changer le code d'une course à sept jours de son dernier jour. Des fichiers d'activations existent avant le verdict du test de transfert : la règle de non-lecture n'est plus tenue par construction, seulement par discipline. | Égalité aux arrondis près seulement. Le contexte n'est pas gardé, il est rebâti par le code. Le modèle de base (environ 16 Go) n'est pas gardé par le programme : il dépend de sa mise à disposition publique. Une seconde location. Pour les épisodes du maître, la passe relit la consigne privée par programme. |

## 6. Point 3 (ii) : le défaut de poussée de l'amorce

**Exact.** Lignes lues :
- `.gitignore`, l. 10 : `donnees/` est ignoré.
- `scripts/amorce_instance_iib_v1.sh:261-263` : `ajouter_legeres` n'ajoute de force que les adaptateurs et les trois noms combinés (`oracle-iib.json`, `ids-actions-iib.npz`, `textes-actions-iib.jsonl`) et leurs sceaux.
- `iib/lanceur_v1.py:293`, `:308`, `:405`, `:464-504` : les fichiers par phase et par tour sont bien écrits et scellés, avant même l'arrêt d'une épreuve en échec (`:293-295`).
- `amorce_instance_iib_v1.sh:440` : le contrôle de fin lit `git status --porcelain`, qui ne montre pas les fichiers ignorés.
- `tests/test_iib_amorce_v1.py:33`, `:120` : l'essai ne plante que les noms combinés.

**Éprouvé** sur un dépôt jouet de mon bloc-notes (supprimé) : avec la forme v3, 8 fichiers suivis sur 20 écrits, `git status --porcelain` vide, 12 fichiers ignorés restés sur le disque ; avec la correction proposée, 20 sur 20.

**La correction proposée suffit-elle ?** Oui pour les trois familles de noms, et sur les trois chemins, car tous passent par `ajouter_legeres` : fin de course (`:420`), arrêt consigné (`:347` puis `:291`), minuterie (`:302` puis `:291`). Non pour la classe du défaut : un nom neuf, demain, serait perdu de la même façon sans que rien ne le dise. D'où les deux compléments de O-M4. **Mon avis : à corriger avant la course, pas en réserve.** Un arrêt aux épreuves ou au tour 4 est un cas prévu, payé 5,6 à 7,9 dollars au central ; sans la correction, ce que cet arrêt apprend disparaît avec le disque.

## 7. Point 2 : ordre des opérations

- **De bout en bout** : la suite « code revu → commit de lancement → configuration → contrôles → création → amorce → suite ciblée → format → étalonnage → six épreuves → tours → distillation → évaluation → sorties → arrêt → rapatriement → destruction » est celle du code. Les six épreuves sont calculées ensemble après l'étalonnage et avant tout épisode du maître ; la première en échec dans l'ordre E-O1 à E-O6 est le motif d'arrêt (`tours_v1.py:129` ; `lanceur_v1.py:288-295`).
- **Commit de lancement** : rien dans le code n'exige que le commit lancé soit celui que cite la configuration. Le montage « enfant direct qui n'ajoute que la configuration » tient donc, par les deux contrôles à la main du § 5. La ligne d'accord est présente une fois, et conforme, dans `registres/go.md` de `d88e3d94`.
- **Commandes du § 5** : usage, arguments, messages attendus et forme de la commande de création imprimée sont ceux de `scripts/lancer_iib_v1.sh` (`:22-27`, `:73`, `:120`, `:167`). Les deux instants : 1 795 816 800 = 2026-11-27T22:00:00Z ; 1 795 824 000 = 2026-11-28T00:00:00Z.
- **Ce qui ne s'exécute pas tel quel** : O-M1 (ligne jamais relayée), O-M2 (cercles), O-M5 (place disque), O-M6 (création tardive).
- **Arrêts par identifiant (R10)** : lu dans les deux scripts en entier. Les arrêts et la destruction passent par l'identifiant de l'instance (commandes imprimées par la surveillance, qui vérifie que l'identifiant est celui créé ; appels de la minuterie sur son propre identifiant). La surveillance se relance par son numéro de processus. Je n'ai vu aucun arrêt par motif de ligne de commande. La recherche par programme qui devait le confirmer est la commande refusée (§ 9).
- **Gardes sur cas sain et artefact (R5)** : vrai pour les gardes éprouvées par les 406 essais, d'après la vérification courte. Faux à `d88e3d94` pour deux gardes (consigne invisible à l'évaluation ; forme de la ligne de 7b) : l'ordre le dit. Gardes neuves que cette contre-lecture ajoute à la liste : relais de la ligne des épreuves (O-M1), contrôle de fin (O-M4), essais du jetoniseur réel s'ils deviennent des arrêts (§ 4 ter).
- **Graines (R9)** : toutes les clés sont dérivées de l'entropie de la configuration et consignées au manifeste (`lanceur_v1.py:102-127`, `:241`). Pour les autres modules, je m'appuie sur les deux rapports sur le code.
- **Moyenne ou médiane sur les jetons dans une sonde** : sans objet, le paquet n'a aucune sonde. Les moyennes et médianes que j'ai lues portent sur des actions et des tâches (`tours_v1.py:44-62`, `:69-74` ; `lanceur_v1.py:318-319`).
- **Épreuves en réel et essais du jetoniseur réel** : la place proposée (sur la carte, avant tout épisode du maître) est celle où le code les joue déjà. Les essais J2 à J4, s'ils deviennent des arrêts, sont du code neuf : essais, contre-lecture, empreintes.

## 8. Point 4 : le devis ; point 5 : la note

**Arithmétique.** `calcul-devis-ii-b-v2.py` rejoué avec `/home/user/controle-ia-travail/.venv/bin/python -I -B` : sortie identique à l'octet à la sortie scellée (`abe794be…0ff2`). Le calcul v1 aussi. Chaque nombre des § 2 à 7 du devis se retrouve dans la sortie.

**Sources.**

| grandeur | source | vérifiée par moi ? |
|---|---|---|
| épisodes, actions, tours | conception ; `TEXTE` du code ; `lanceur_v1.py` | oui |
| bornes de prix 1,30 et 4,70 ; stockage 0,08 ; téléchargement 0,05 | `configuration_v1.py:73-74`, `:343-348` | oui |
| minuterie : 2 400 et 1 800 secondes | `amorce_instance_iib_v1.sh:41`, `:34` | oui |
| 406 essais, 6 min 55 s | vérification courte, § 4 | oui |
| règle du calendrier | `t06/session_v3.py:113-135` ; `configuration_v1.py:263-266` | oui, rejouée |
| 1,86 seconde par transcription et par époque | 891 secondes sur 480 | calcul oui ; relevé de 7a non |
| 43,3 secondes par épisode ; durées fixes | lecture A de 7a, par le devis précédent | non : le fichier existe et son empreinte commence par `3c84c419`, je ne l'ai pas ouvert |
| prix relevés 1,009 à 1,2133 | préenregistrement de T0.6 | non : interdit à ce mandat |
| 1,12 dollar par heure | « consigne de la mère » | non : aucun chemin (D-m3) |
| jumeau : 0,5 à 3,0 secondes par action | hypothèse déclarée, non mesurée | — |

**Pire cas.** 52,5 dollars (hôte deux fois plus lent, 12 tours, jumeau à 3 secondes, 48 heures d'arrêt, 40 Go), sous 60. Avec la formule du code, la coupure vient à 38,4 heures au prix borne ; le pire cas dure 33,3 heures (D-m1). Plafond tenu par les gardes : au plus 59,8 dollars (D-m2).

**Variante B et garde du code.** Rejoué avec le code de la tête `d88e3d94` :
- sur une copie de la seule ligne : 60 lu du 10 au 27, refus le 9 et le 28 ; 55 accepté ; 60,01 et 75 refusés ; 55 avec 5,01 de dépense antérieure refusé ;
- variante B contre une ligne de 60 : conforme ; variante A : refusée ; variante B à 58 : refusée ; carte de repli en variante B : refusée ;
- **sur le registre entier**, lu par le programme seul, verdict de la clé seul affiché : conforme, dans l'arbre courant et dans `registres/go.md` de `d88e3d94`. La ligne y est une fois, identique.

**Échéance.** Création le 25 avant 23:00 UTC : le pire cas finit le 27 vers 08:19 UTC, 13 heures avant la minuterie (22:00 UTC). L'attendu finit en 9 à 14 heures. Aucune place pour une seconde course sous cette ligne. Le risque de calendrier est en amont : corrections du code et leur contrôle, décision sur la seconde lecture, création de 7b, points à trancher, scellements.

**Note.** Les cinq points sont au format : décision en une phrase, enjeu, options avec avantage et inconvénient, recommandation et confiance, défaut. Mots clairs, tutoiement, identifiants après le nom en clair. Les nombres cités sont ceux du devis. Trois majeurs (N-M1 à N-M3), trois mineurs. Le point 3 de la note recommande de corriger le défaut de poussée avant la course : je suis du même avis.

## 9. Refus, lectures hors mandat, limites

**Refus : un, d'un crochet.** Texte exact :

> `PreToolUse:Bash hook error: [command hook]: GARDE (registres/go, R10) — commande bloquée : R10 — arrêt par motif de ligne de commande interdit ; arrêter par PID ou identifiant d'instance`

La commande refusée était une recherche en lecture seule, par `git show … | grep`, dans les deux scripts de la branche et dans six modules du paquet. Elle cherchait quatre choses à la fois : les noms des commandes d'arrêt de processus par motif (pour confirmer R10), la constante du seuil d'alerte, les appels de moyenne et de médiane, les sources d'aléa. Le crochet a lu dans ma ligne de commande les noms que je cherchais. Je me suis arrêté là : la commande n'a été ni rejouée, ni reformulée, ni découpée. Aucune de ses quatre recherches n'a été refaite autrement.

**Ce qui n'a donc pas été vérifié par moi** :
- la confirmation par programme de l'absence d'arrêt par motif (je l'affirme d'après ma lecture entière des deux scripts) ;
- la valeur de la constante du seuil d'alerte (le lanceur écrit « alerte après 2 h », l. 212) ;
- les moyennes, médianes et sources d'aléa de `oracle_v1.py`, `regle_v1.py`, `temoin_jumeau_v1.py`, `exclusion_v1.py`, que je n'ai pas lus : je m'appuie sur les deux rapports sur le code ;
- les commandes du § 5 au commit de lancement, qui n'existe pas encore.

**Lectures hors de la liste du mandat**, toutes déclarées :
1. `registres/go.md` entier lu **par le programme de garde** (arbre courant, puis copie du commit `d88e3d94` dans mon bloc-notes, supprimée) : seul son verdict sur la clé a été affiché. Ma recherche de la clé n'a rendu que la ligne citée.
2. `git ls-remote` sur le seul nom `refs/heads/essai/iib-explo-v1` : absente.
3. Devis, brouillon 2, § 1 (table des hypothèses) : le brouillon 3 le cite comme porteur de ses sources.
4. Journal de rédaction v2 : une recherche de l'empreinte de la consigne (l. 50), rien d'autre.
5. Modules de session de la chaîne précédente, sur la branche : `t06/session_v3.py` (l. 1 à 175), `t06/session_v2.py` (l. 60 à 160), `t06/session_v12.py` (l. 1 à 110), `t06/session.py` (l. 120 à 140 et quatre constantes), lignes d'import des autres ; `t06/lanceur.py`, fonction `progres` (l. 75 à 87) ; en-tête de `t06/__init__.py` (vingt lignes : une liste de modules, dont un nom de module de sondes, sans contenu).
6. `tests/test_iib_amorce_v1.py` (l. 25 à 40, 112 à 128) ; deux lignes de `tests/test_iib_inventaires_v1.py` ; des comptes de motifs dans les 13 fichiers de la suite ciblée.
7. Empreinte de la lecture A de 7a calculée par programme (seize premiers caractères), fichier non ouvert.
8. Tailles du dépôt : `git count-objects`, sommes de `git ls-tree -r -l` (aucun contenu).
9. Noms seuls : entrées de `src/controle_ia/` (dont des noms de modules de sondes), fichiers de `docs/notes/barreau8-iib-v1/` hors relevés, fichiers du dossier des brouillons.
10. Vu sans le chercher : la vérification courte du code, § 6.2, liste des réglages de la base textuelle de la seconde lecture. Ce rapport est à mon mandat ; je n'en fais aucun usage.

**Exécuté sur processeur, dans mon bloc-notes** : le script d'arithmétique (v2 et v1) ; les gardes de session, depuis une extraction de 18 fichiers (180 Ko) de la tête `d88e3d94` ; un dépôt git jouet ; les deux motifs du relais. Pas d'arbre de travail neuf.

**Limites.** Mes coûts du § 5.2 sont des ordres de grandeur, non mesurés. Je ne connais ni l'état de 7b, ni la décision D-4, ni ce que 7a enregistrait au juste. La forme de clonage réduit (O-M5) n'est pas éprouvée. Je n'ai lu aucun essai en entier. Cette contre-lecture porte sur le brouillon 3 : l'ordre final, marqueurs remplis et couples appliqués, demande une vérification courte de plus.
