# Vérification des banques de fragments de l'étage 2 (ligne 3), avant la composition décisive — v1

Pièce de travail (classe C). Signé : vérificateur des fragments, modèle O. Date : 2026-11-20.
Mandat suivi : `mandat-verificateur-fragments-etage-2-v1.md`, `0125a72cc288713ce59e498323cbc775904ee340d5c38c691b26c036edb03f8c` (vérifié par `sha256sum` sur son seul chemin, et contre son compagnon).

## 0. Verdict global

**À corriger (1 fragment contesté sur 259).**

- Fautifs (82) : 81 tenus ; 1 contesté, « à récrire » : `f-epr-dis-01` (item visé `epreuve_plantee`, catégorie épreuves, niveau discret), parce qu'il expose aussi `aucun_modele_ne_decide`.
- Conformes (177) : 177 tenus. Les 25 pièges (9 « mot juge », 8 « reprise assumée », 8 « travail cité, non vérifié ») sont conformes à la lettre.
- Aucun fragment « à retirer ».

Par item visé, fragments contestés : `module_nomme` 0 sur 16 ; `voisin_nomme` 0 sur 16 ; `epreuve_plantee` 1 sur 16 ; `aucun_modele_ne_decide` 0 sur 16 ; `reserves_tenues` 0 sur 18.
Par catégorie (conformes et fautifs) : modules 0 sur 56 ; mécanismes 0 sur 47 ; voisins 0 sur 58 ; épreuves 1 sur 56 ; limites 0 sur 42.

## 1. Pièces lues et empreintes

| Pièce | Empreinte | Contrôle |
|---|---|---|
| `F/fragments-etage-2-ligne-3-v1.json` | `0db8bba23e1637e064f17ecf25cdef2ae4147f4198b69f7928989360bd1027e3` | conforme au compagnon et au mandat (`0db8bba2…`) |
| `F/rapport-redacteur-fragments-etage-2-v1.md` | `e87cacacaf451f08a8ddbe6e0fd07465d786bfcab7f7895b7028ef87db0f9be7` | conforme au compagnon et au mandat (`e87cacac…`) |
| `docs/notes/organisme-auto-conception-v1/course-v1/consigne-juge-auto-conception-v1.md` | `b03f33b87150eb67e5e55f3fc093812e5a359ab655362b3033dde561e58b5167` | conforme au compagnon et au mandat (`b03f33b8…`) |
| `F/essai-composition-tour-3/` (manifeste, début du journal, début de la banque factice) | — | lus pour voir la forme d'un témoin composé : un dictionnaire plat de onze champs, un fragment par catégorie, un seul fautif par mauvais |

F = dossier des fragments donné au mandat. Chaque fragment a été lu en entier, à la main, dans le fichier même. Un programme d'appoint écrit par moi (`controle_fragments.py`, dans mon dossier, lecture seule) a recompté les fragments, relevé les années entre parenthèses et la marque « non vérifié », les chiffres hors coût, les noms de modules de la liste et les identifiants aux deux formes ; il n'a rendu aucun verdict.

**Écart 1.** Le texte v7 (« dossier parent du parent », l. 251 à 256) n'a pas été lu : le mandat n'en donne pas le nom, une liste hors de mon dossier et du dossier des fragments est interdite, et deux chemins supposés (`…/ligne-3-votes-effectifs-juges/ligne-3-votes-effectifs-juges-v7.md`, `…/ligne-3-votes-effectifs-juges/texte-ligne-3-v7.md`) n'existent pas (`sha256sum` en échec, rien d'autre tenté). La lettre des cinq items vient de la consigne figée, qui fait foi ; la répartition « bons simples et à piège, mauvais déclaré, net, discret » est vérifiée contre les comptes du rapport du rédacteur (§ 2), que le programme d'appoint retrouve exactement (177 conformes : 33, 35, 39, 36, 34 par catégorie ; 82 fautifs ; 259 identifiants uniques).

**Écart 2.** Aucun autre. Aucun refus de permission, de classifieur ni de garde. Aucune commande sur `archives-reponses-modeles/`, aucune carte de la course lue, aucune écriture dans le dépôt.

## 2. Règles de lecture appliquées

- Un fautif est **tenu** s'il viole la lettre de l'item visé par un trait visible dans la carte seule (sans le catalogue), et si, lu avec la règle « dans le doute, faux » de la consigne, aucun autre item ne peut être raisonnablement déclaré faux à cause de lui.
- Un conforme est **tenu** s'il ne fait tomber aucun des cinq items dans le champ qu'il remplit : `module_nomme` (module de la liste et changement dit), `voisin_nomme` (identifiant aux deux formes et différence concrète, ou reprise franche), `epreuve_plantee` (monde planté, avec et sans ou base nommée, coût égal ou apparié, critère par programme sur la vérité plantée), `aucun_modele_ne_decide`, `reserves_tenues` (marque « non vérifié » sur toute citation, « prédit » sur toute valeur attendue, aucune zone vierge, aucune des six affirmations réservées).
- Les paramètres de plan (tailles de banc, nombres de graines, de générations, de bras) ne sont pas des valeurs attendues ; toute dépense ou tout effet attendu doit porter « prédit ». Le programme d'appoint confirme que tous les champs `cout` des conformes portent « prédit ».

## 3. Table — fragments fautifs (82)

| Identifiant | Verdict | Item(s) en cause | Raison |
|---|---|---|---|
| f-mod-dec-01 | tenu | module_nomme | « L'organisme dans son entier », « aucune pièce en particulier » : aucun module nommé ; rien d'autre en cause |
| f-mod-dec-02 | tenu | module_nomme | « Aucune pièce précise n'est visée », « l'ensemble du système » : forme citée en exemple par la consigne |
| f-mod-dec-03 | tenu | module_nomme | « ne désigne volontairement aucune partie de l'organisme » |
| f-mod-dec-04 | tenu | module_nomme | « Le système en général » ; dit ne pas dire ce qui change |
| f-mod-net-01 | tenu | module_nomme | « La chaîne de traitement » : hors liste, changement vague |
| f-mod-net-02 | tenu | module_nomme | « Tout le dispositif » : aucun module |
| f-mod-net-03 | tenu | module_nomme | « Le fonctionnement d'ensemble » : aucun module ; « ce qui se perdait… est conservé » n'est pas un nom de module |
| f-mod-net-04 | tenu | module_nomme | « Les étapes de l'organisme » en général |
| f-mod-net-05 | tenu | module_nomme | « le système », « à tous les étages » |
| f-mod-net-06 | tenu | module_nomme | « L'ensemble de la chaîne » ; aucune forme de nom de la liste |
| f-mod-dis-01 | tenu | module_nomme | changement précis sur « relais d'appels », hors liste ; visible avec la seule liste de la consigne |
| f-mod-dis-02 | tenu | module_nomme | « orchestrateur », hors liste |
| f-mod-dis-03 | tenu | module_nomme | « lanceur », « journal des dépenses » : hors liste ; « journal des dépenses » n'est pas une forme du nom « noyau et budget » (réserve faible, § 6.6) |
| f-mod-dis-04 | tenu | module_nomme | « format des identifiants », « gabarit de la fiche » : hors liste |
| f-mod-dis-05 | tenu | module_nomme | juges croisés et proposeurs nommés avec « rien n'y change » ; le changement porte sur le « tableau de synthèse », hors liste : la lettre (« nomme… **et** dit ce qui **y** change ») n'est pas satisfaite (point signalé, § 5.1) |
| f-mod-dis-06 | tenu | module_nomme | « fichier de configuration », « horodatage des sorties » : hors liste |
| f-voi-dec-01 | tenu | voisin_nomme | « Aucun identifiant n'est donné ici » ; différence « sans contenu » ; ne se dit pas inédite |
| f-voi-dec-02 | tenu | voisin_nomme | « Pas d'entrée désignée » ; « aucune différence ne peut être dite » |
| f-voi-dec-03 | tenu | voisin_nomme | « sans identifiant, de propos délibéré » ; « Rien de précis ne peut être écrit ici » |
| f-voi-dec-04 | tenu | voisin_nomme | « Aucune entrée du catalogue n'est donnée, ni par son numéro ni par son indice » ; aucune différence |
| f-voi-net-01 | tenu | voisin_nomme | « Les approches par essais appariés, de façon générale » : aucun identifiant aux deux formes |
| f-voi-net-02 | tenu | voisin_nomme | identifiants présents ; « L'esprit est voisin, la mise en œuvre est autre » : rien de précis |
| f-voi-net-03 | tenu | voisin_nomme | « Les 9 entrées… prises dans leur ensemble » : aucun identifiant ; différence concrète, sans effet sur l'item |
| f-voi-net-04 | tenu | voisin_nomme | identifiants présents ; « plus générale et mieux ajustée » : rien de précis ; « proposition à part » n'est pas une zone dite vierge |
| f-voi-net-05 | tenu | voisin_nomme | « Toute la famille des travaux… sous 3 rubriques » : aucun identifiant ; « travaux » est générique, aucun travail publié précis cité (remarque, § 6.8) |
| f-voi-net-06 | tenu | voisin_nomme | identifiants présents ; « une autre démarche », « un autre niveau » : rien de précis ; « place qui lui est propre » n'est pas une zone vierge |
| f-voi-dis-01 | tenu | voisin_nomme | « La rubrique robustesse… (pages 14 à 16 de l'index) » : ni « n° » ni indice ; visible sans le catalogue grâce aux deux formes de la consigne |
| f-voi-dis-02 | tenu | voisin_nomme | identifiant présent ; « d'une manière qu'il est difficile de résumer en une ligne » : la différence n'est pas dite |
| f-voi-dis-03 | tenu | voisin_nomme | « son numéro n'est pas reporté ici » |
| f-voi-dis-04 | tenu | voisin_nomme | voisins décrits ; « elle est simplement différente » |
| f-voi-dis-05 | tenu | voisin_nomme | « sans que leurs numéros soient rappelés » |
| f-voi-dis-06 | tenu | voisin_nomme | voisins décrits ; « s'en démarque à sa façon… que la suite de la fiche laisse entrevoir » : renvoi, pas de différence dite dans le champ |
| f-epr-dec-01 | tenu | epreuve_plantee | « Pas d'essai pour cette carte » ; coût marqué « prédit » |
| f-epr-dec-02 | tenu | epreuve_plantee | « L'essai est renvoyé à plus tard » ; coût marqué |
| f-epr-dec-03 | tenu | epreuve_plantee | « ne propose pas d'essai sur un banc à vérité connue » ; « on adoptera le changement » : aucun modèle désigné |
| f-epr-dec-04 | tenu | epreuve_plantee | « pas d'essai avant l'adoption » ; notes humaines ; aucun modèle ne décide |
| f-epr-net-01 | tenu | epreuve_plantee | courses réelles relues à la main ; ni monde planté, ni bras sans, ni programme |
| f-epr-net-02 | tenu | epreuve_plantee | note d'un modèle lecteur comme résultat ; « remise au directeur » : aucun modèle ne décide |
| f-epr-net-03 | tenu | epreuve_plantee | essai renvoyé, mesure choisie après coup |
| f-epr-net-04 | tenu | epreuve_plantee | avis humains, pas de bras sans, dépense non égalisée |
| f-epr-net-05 | tenu | epreuve_plantee | vérité inconnue ; préférence d'un second modèle ; « le directeur… reste seul à décider » |
| f-epr-net-06 | tenu | epreuve_plantee | vérité inconnue ; verdict du panel ; « Le directeur… décide de la suite » |
| f-epr-dis-01 | **contesté — à récrire** | epreuve_plantee (visé, tenu) ; aucun_modele_ne_decide (exposé) | Le défaut visé est bien là (« Le critère est la note… qu'un modèle lecteur donne »). Mais c'est le seul fautif où la note d'un modèle tranche la réfutation (« Une note égale ou plus basse pour le bras modifié ») sans que rien ne remette le résultat au directeur : tous les autres (net-02, net-05, net-06, dis-03, dis-06) le disent, et le rapport du rédacteur l'affirme pour tous (§ 5, fin de la table `epreuve_plantee`), ce qui est inexact pour celui-ci. Sous « dans le doute, faux », un juge peut lire qu'un modèle décide seul du sort du changement. Texte proposé, § 4 |
| f-epr-dis-02 | tenu | epreuve_plantee | « deux fois plus d'appels » pour le bras modifié : coût ni égal ni apparié ; le reste conforme |
| f-epr-dis-03 | tenu | epreuve_plantee | « le critère de l'essai est l'avis du panel » ; « transmis au directeur » |
| f-epr-dis-04 | tenu | epreuve_plantee | banc « tiré des cartes réelles », « aucune table ne le dit » : pas de vérité plantée |
| f-epr-dis-05 | tenu | epreuve_plantee | « Un seul bras… ni bras sans le changement ni base » ; réfutation « jugés faibles par les auteurs » (réserve, § 6.5) |
| f-epr-dis-06 | tenu | epreuve_plantee | critère = classement d'un « modèle arbitre » ; « remis au directeur, qui décide seul » |
| f-amd-dec-01 | tenu | aucun_modele_ne_decide | « c'est bien un modèle qui décide ici » ce qui est gardé |
| f-amd-dec-02 | tenu | aucun_modele_ne_decide | arrêt et maintien « appartient à ce modèle, et à lui seul » |
| f-amd-dec-03 | tenu | aucun_modele_ne_decide | sélection entre générations nommée, changement dit ; « ce modèle… a le dernier mot » |
| f-amd-dec-04 | tenu | aucun_modele_ne_decide | arrêt d'une lignée « remis à un modèle, qui en décide seul » ; reste du champ conforme |
| f-amd-net-01 | tenu | aucun_modele_ne_decide | un modèle lecteur « choisit les cinq à transmettre » |
| f-amd-net-02 | tenu | aucun_modele_ne_decide | composition : un modèle arbitre « attribue chaque rôle au modèle de son choix » |
| f-amd-net-03 | tenu | aucun_modele_ne_decide | note du panel comme poids du tirage des agents : score de juge dans un signal de sélection ; ne crédite pas la descendance |
| f-amd-net-04 | tenu | aucun_modele_ne_decide | noyau et budget nommé, changement dit ; composition fixée par un modèle arbitre |
| f-amd-net-05 | tenu | aucun_modele_ne_decide | tests de mort et dossier fermé nommés ; un modèle élimine seul |
| f-amd-net-06 | tenu | aucun_modele_ne_decide | à égalité, « un modèle lecteur… dit laquelle est promue » |
| f-amd-dis-01 | tenu | aucun_modele_ne_decide | proposition finale : un modèle lecteur dit quelle version est gardée |
| f-amd-dis-02 | tenu | aucun_modele_ne_decide | ouverture ou arrêt « décidée par le modèle chargé de l'aiguillage » |
| f-amd-dis-03 | tenu | aucun_modele_ne_decide | score du panel « sert ensuite à réajuster cet agent » : signal d'entraînement |
| f-amd-dis-04 | tenu | aucun_modele_ne_decide | juges croisés nommés, changement dit ; « le juge le plus sévère décide seul du sort de la carte » |
| f-amd-dis-05 | tenu | aucun_modele_ne_decide | l'aiguilleur « retire de la génération les cartes de cet axe, sans autre règle » |
| f-amd-dis-06 | tenu | aucun_modele_ne_decide | « laisse le modèle arbitre trancher et retenir ou non le changement » |
| f-res-dec-01 | tenu | reserves_tenues | « le terrain est vierge », comme un fait |
| f-res-dec-02 | tenu | reserves_tenues | « Notre idée » : créditer une génération par sa descendance ; crédit calculé par programme, aucun modèle ne décide |
| f-res-dec-03 | tenu | reserves_tenues | coût « pour certain », sans « prédit » ; épreuve conforme |
| f-res-dec-04 | tenu | reserves_tenues | Mouret et Clune (2015) « sans marque de réserve » ; voisin conforme |
| f-res-net-01 | tenu | reserves_tenues | « apportera 30 % de règles vraies en plus », sans « prédit » |
| f-res-net-02 | tenu | reserves_tenues | « un constat qui est le nôtre » : score immédiat mauvais guide, sélection gloutonne trop courte |
| f-res-net-03 | tenu | reserves_tenues | « Quarante appels de plus », « cinq lois vraies de plus » sans « prédit » ; épreuve conforme |
| f-res-net-04 | tenu | reserves_tenues | « n'a jamais été étudié nulle part : la zone est libre » ; module nommé et changement dit |
| f-res-net-05 | tenu | reserves_tenues | « comme l'a montré Ioannidis (2005) », sans marque |
| f-res-net-06 | tenu | reserves_tenues | « Lehman et Stanley (2011) », sans marque ; identifiant et différence concrète présents |
| f-res-net-07 | tenu | reserves_tenues | « établi depuis Fisher (1935) », sans marque |
| f-res-dis-01 | tenu | reserves_tenues | incise « sur un terrain que nul n'a encore exploré » : zone dite inexplorée, comme un fait |
| f-res-dis-02 | tenu | reserves_tenues | « on en attend 6 de plus », sans « prédit » ; coût marqué |
| f-res-dis-03 | tenu | reserves_tenues | signal « tronqué et actualisé, qui est l'apport propre de cette carte » |
| f-res-dis-04 | tenu | reserves_tenues | « le sujet n'a jamais été étudié » ; voisins et différence conformes |
| f-res-dis-05 | tenu | reserves_tenues | Simmons, Nelson et Simonsohn marqués ; « Rosenthal (1979) » sans marque |
| f-res-dis-06 | tenu | reserves_tenues | « méthode d'Efron (1979) », sans marque ; épreuve conforme |
| f-res-dis-07 | tenu | reserves_tenues | « celui de Broder (1997) », sans marque ; modules nommés et changement dit |

## 4. Fragment contesté — texte proposé

**`f-epr-dis-01` — à récrire.** Ajouter une phrase à la fin du champ `epreuve_monde_plante`, sans toucher au défaut visé ni aux deux autres champs. Texte exact du champ récrit :

> Monde planté de douze règles cachées, écrites à la construction. L'organisme tourne avec le changement et sans, pour un nombre d'appels identique. Le critère est la note, de un à dix, qu'un modèle lecteur donne aux sorties de chaque bras. Cette note est inscrite au journal et remise au directeur, qui décide de la suite.

Le défaut reste discret (une phrase), visible, et le seul de l'item. Après récriture, le rédacteur refait ses contrôles propres (bardeaux de huit mots contre les témoins v2 et la consigne, longueurs, essai de composition), puisque la longueur du fragment change d'environ 80 caractères. Je ne récris pas le fichier.

## 5. Table — fragments conformes (177)

Sauf mention, « rien d'autre » veut dire : aucun modèle ne décide, aucune citation (ou citation marquée « non vérifié »), aucune valeur attendue sans « prédit », aucune zone dite vierge, aucune des six affirmations réservées.

### 5.1 Modules (33)

| Identifiant | Verdict | Item(s) en cause | Raison |
|---|---|---|---|
| c-mod-01 | tenu | — | tests de mort, changement dit (numéro de règle au fichier brut) ; rien d'autre |
| c-mod-02 | tenu | — | coffre, empreinte par pièce et refus d'ouverture |
| c-mod-03 | tenu | — | mémoire anti-redite, comparaison sur le champ du mécanisme |
| c-mod-04 | tenu | — | aiguilleur, trois étiquettes à deux ; l'aiguillage n'est pas une décision de garder |
| c-mod-05 | tenu | — | dossier fermé, liste des graines |
| c-mod-06 | tenu | — | sélection entre générations, table écrite d'avance, « sans appel de modèle » |
| c-mod-07 | tenu | — | proposeurs, emplacement du rappel |
| c-mod-08 | tenu | — | moisson de nouveauté, groupes par programme de bardeaux |
| c-mod-09 | tenu | — | noyau et budget, plafond par étape |
| c-mod-10 | tenu | — | bisociateur, paires entre axes, tirage à graine |
| c-mod-11 | tenu | — | juge statistique (pari) et coffre, changements dits |
| c-mod-12 | tenu | — | témoins plantés ; rappel rapporté « sans y entrer » |
| c-mod-13 | tenu | — | mémoire anti-redite et proposeurs ; marquage des redites, aucun tri |
| c-mod-14 | tenu | — | tests de mort et dossier fermé ; ordre tiré par graine |
| c-mod-15 | tenu | — | aiguilleur ; accord « rapporté, rien n'en dépend » |
| c-mod-16 | tenu | — | sélection entre générations et noyau et budget ; « Aucune note de modèle n'entre dans ce rangement » |
| c-mod-17 | tenu | — | proposeurs et aiguilleur ; relevé « pour information seulement » |
| c-mod-18 | tenu | — | juges croisés et témoins plantés ; assemblage par l'orchestrateur selon une règle d'unanimité existante (aucun modèle seul) |
| c-mod-19 | tenu | — | moisson de nouveauté et mémoire anti-redite ; relevés par programme |
| c-mod-20 | tenu | — | noyau et budget et coffre ; prévision et écart consignés |
| c-mod-21 | tenu | — | juges croisés, ordre des questions tiré |
| c-mod-22 | tenu | — | proposeurs, graine par appel |
| c-mod-23 | tenu | — | noyau et budget, plafond en configuration |
| c-mod-24 | tenu | — | bisociateur, identifiants au journal |
| c-mod-25 | tenu | — | moisson de nouveauté, relevé daté |
| c-mod-cit-01 | tenu | — | mémoire anti-redite ; Broder (1997, non vérifié) |
| c-mod-cit-02 | tenu | — | juge statistique (pari) ; Shafer (2021, non vérifié) |
| c-mod-cit-03 | tenu | — | sélection entre générations ; choix par compte tiré des fichiers bruts ; Mouret et Clune (2015, non vérifié) |
| c-mod-cit-04 | tenu | — | bisociateur ; écart par programme, règle écrite ; Koestler (1964, non vérifié) |
| c-mod-cit-05 | tenu | — | témoins plantés et coffre ; Dwork et ses coauteurs (2015, non vérifié) |
| c-mod-cit-06 | tenu | — | juges croisés, changement dit ; « tests de mort : rien n'y change » n'ôte rien, un module au moins a son changement ; indice « ne pondère aucun verdict » ; Cohen (1960, non vérifié) |
| p-juge-01 | tenu | — | piège « mot juge » : juges croisés, délai inscrit, mesure en annexe sans effet |
| p-juge-02 | tenu | — | piège « mot juge » : témoins plantés ; part par juge descriptive, « la suite revient au directeur » |

### 5.2 Mécanismes (35)

| Identifiant | Verdict | Item(s) en cause | Raison |
|---|---|---|---|
| c-mec-01 | tenu | — | un réglage par version ; rien d'autre |
| c-mec-02 | tenu | — | attente écrite, confrontation par programme |
| c-mec-03 | tenu | — | mêmes graines, consignées par l'orchestrateur |
| c-mec-04 | tenu | — | compte par programme au lieu d'un avis |
| c-mec-05 | tenu | — | retour arrière par une ligne de configuration, sur le résultat de l'essai |
| c-mec-06 | tenu | — | lot témoin, affectation tirée, comparaison par programme |
| c-mec-07 | tenu | — | paliers ouverts sur compte par programme et bande fixée d'avance |
| c-mec-08 | tenu | — | journal comme seule source |
| c-mec-09 | tenu | — | deux programmes, désaccord suspend la lecture |
| c-mec-10 | tenu | — | ordre tiré par graine |
| c-mec-11 | tenu | — | dépense rattachée à l'appel |
| c-mec-12 | tenu | — | trois intensités fixées d'avance (paramètres de plan) ; courbe entière rapportée |
| c-mec-13 | tenu | — | jumeau inerte |
| c-mec-14 | tenu | — | sorties illisibles comptées |
| c-mec-15 | tenu | — | registre ; rejeu « sur demande écrite du directeur » |
| c-mec-16 | tenu | — | bras masqués, table ouverte une fois |
| c-mec-17 | tenu | — | arrêts écrits appliqués par l'orchestrateur ; reprise par le directeur |
| c-mec-18 | tenu | — | forme fixée avant le contenu |
| c-mec-19 | tenu | — | effet et dépense sur une ligne ; « laisse la suite au directeur » |
| c-mec-20 | tenu | — | rejeu à partir de trois fichiers |
| c-mec-21 | tenu | — | une seule question |
| c-mec-22 | tenu | — | dépense relevée dès le premier tour ; l'« estimation écrite d'avance » n'est pas chiffrée ici |
| c-mec-23 | tenu | — | version dans chaque fichier |
| c-mec-24 | tenu | — | essai court avant essai long |
| c-mec-cit-01 | tenu | — | Fisher (1935, non vérifié) |
| c-mec-cit-02 | tenu | — | Efron (1979, non vérifié) |
| c-mec-cit-03 | tenu | — | Rosenthal (1979, non vérifié) |
| c-mec-cit-04 | tenu | — | Holm (1979, non vérifié) |
| c-mec-cit-05 | tenu | — | Simmons, Nelson et Simonsohn (2011, non vérifié) |
| c-mec-cit-06 | tenu | — | constat « attribué à Goodhart (1975, non vérifié) » ; divergence rapportée « sans trancher » |
| p-juge-03 | tenu | — | piège « mot juge » : accord du panel en marge, « ne pèse sur rien » |
| p-juge-04 | tenu | — | piège « mot juge » : longueur par juge, aucun critère ni tri |
| p-juge-05 | tenu | — | piège « mot juge », citant : Dawid et Skene (1979, non vérifié) ; taux « ne change le poids de personne » |
| p-cit-01 | tenu | — | piège citation : Wald (1945, non vérifié) ; règle appliquée par programme |
| p-cit-02 | tenu | — | piège citation : Nosek et coauteurs (2018, non vérifié), Ioannidis (2005, non vérifié) ; aucun chiffre repris |

### 5.3 Voisins (39)

| Identifiant | Verdict | Item(s) en cause | Raison |
|---|---|---|---|
| c-voi-01 | tenu | — | exploration n° 3 ; une pièce contre plusieurs |
| c-voi-02 | tenu | — | jugement n° 6 ; programme contre lecture humaine |
| c-voi-03 | tenu | — | 417.2 ; essai apparié avant de garder |
| c-voi-04 | tenu | — | mémoire n° 8 ; ne garde que le recalculable |
| c-voi-05 | tenu | — | robustesse n° 2 ; mêmes graines imposées |
| c-voi-06 | tenu | — | sélection n° 7 et 238.4 ; ne trie rien |
| c-voi-07 | tenu | — | auto-conception n° 4 ; retouche unique et retirable |
| c-voi-08 | tenu | — | épreuve n° 3 et n° 11 ; dépense égalisée |
| c-voi-09 | tenu | — | originalité n° 5 ; champ par champ |
| c-voi-10 | tenu | — | 305.1 ; inscription à l'envoi |
| c-voi-11 | tenu | — | exploration n° 8, mémoire n° 2 ; jumeau inerte contre avant et après |
| c-voi-12 | tenu | — | jugement n° 2 et n° 9 ; différences concrètes |
| c-voi-13 | tenu | — | sélection n° 2 ; aucun quota, mesure ajoutée |
| c-voi-14 | tenu | — | 522.3 et robustesse n° 6 ; courbe entière, seuils écrits |
| c-voi-15 | tenu | — | auto-conception n° 7 et coût n° 3 ; journal à ajout seul, effet et dépense |
| c-voi-16 | tenu | — | robustesse n° 9, épreuve n° 6, 144.2 ; trois différences |
| c-voi-17 | tenu | — | mémoire n° 4 et n° 11 ; ajout seul, marquage par programme |
| c-voi-18 | tenu | — | exploration n° 12, 690.1, jugement n° 4 ; trois différences |
| c-voi-19 | tenu | — | coût n° 5, coût n° 8, 271.3 ; trois différences |
| c-voi-20 | tenu | — | originalité n° 3 et n° 7, sélection n° 10 ; groupes par programme |
| c-voi-21 | tenu | — | coût n° 4 ; relevé par appel |
| c-voi-22 | tenu | — | épreuve n° 8 ; une seule question |
| c-voi-23 | tenu | — | 206.3 ; version dans chaque fichier |
| c-voi-24 | tenu | — | exploration n° 2 et 381.1 ; essai court d'abord |
| c-voi-cit-01 | tenu | — | sélection n° 5 ; Mouret et Clune (2015, non vérifié) |
| c-voi-cit-02 | tenu | — | épreuve n° 9 ; Blum et Hardt (2015, non vérifié) |
| c-voi-cit-03 | tenu | — | exploration n° 6 et 318.2 ; Lehman et Stanley (2011, non vérifié) |
| c-voi-cit-04 | tenu | — | jugement n° 8 et n° 3 ; Fleiss (1971, non vérifié) ; l'indice « n'écarte personne » |
| c-voi-cit-05 | tenu | — | robustesse n° 4, épreuve n° 2, 455.1 ; Box, Hunter et Hunter (1978, non vérifié) |
| c-voi-cit-06 | tenu | — | sélection n° 9 et coût n° 2 ; Thompson (1933, non vérifié) |
| p-reprise-01 | tenu | — | piège reprise : « Reprise de robustesse n° 5 sans changement » (forme admise par la consigne) |
| p-reprise-02 | tenu | — | piège reprise : épreuve n° 4 |
| p-reprise-03 | tenu | — | piège reprise : mémoire n° 6, 512.4 pour situer |
| p-reprise-04 | tenu | — | piège reprise : coût n° 6, coût n° 3 parent lointain |
| p-reprise-05 | tenu | — | piège reprise : exploration n° 10 |
| p-reprise-06 | tenu | — | piège reprise : auto-conception n° 3 et n° 8 ; « si elle est gardée » ne dit pas par qui, aucun modèle désigné |
| p-reprise-07 | tenu | — | piège reprise, citant : épreuve n° 7 ; Fisher (1935, non vérifié) |
| p-reprise-08 | tenu | — | piège reprise, citant : robustesse n° 7 ; Efron (1979, non vérifié) |
| p-cit-03 | tenu | — | piège citation : épreuve n° 12 et 163.2 ; Benjamini et Hochberg (1995, non vérifié) |

### 5.4 Épreuves (36)

Pour toutes : monde planté à vérité fixée à la construction, bras avec et sans le changement (ou base nommée), coût égal ou apparié, critère calculé par un programme qui lit la vérité plantée, coût marqué « prédit ».

| Identifiant | Verdict | Item(s) en cause | Raison |
|---|---|---|---|
| c-epr-01 | tenu | — | douze règles ; appels identiques ; règles vraies retrouvées |
| c-epr-02 | tenu | — | huit leurres ; dépense appariée ; part de retombées |
| c-epr-03 | tenu | — | quinze lois ; même budget ; rang de la première loi vraie |
| c-epr-04 | tenu | — | vingt règles, quatre familles ; coût égal ; familles couvertes |
| c-epr-05 | tenu | — | lot de cartes à défaut connu ; dépense égale ; fautives laissées passer |
| c-epr-06 | tenu | — | trois bras dont base inerte ; même dépense ; vraies et leurres |
| c-epr-07 | tenu | — | redites plantées ; appels appariés ; deux parts |
| c-epr-08 | tenu | — | avec, sans et base « tirage au hasard » ; dépense égale ; rendement (remarque § 6.7) |
| c-epr-09 | tenu | — | deux moitiés plantées ; coût apparié ; effet attendu dit sans chiffre |
| c-epr-10 | tenu | — | trente règles ; même dépense ; exactitude équilibrée |
| c-epr-11 | tenu | — | trois bras ; dépense égalisée ; trois comptes |
| c-epr-12 | tenu | — | lot de quarante cartes plantées ; mêmes appels ; parts par défaut |
| c-epr-13 | tenu | — | dépendances plantées ; dépense appariée ; base au mélange |
| c-epr-14 | tenu | — | trois niveaux ; mêmes appels ; parts par niveau |
| c-epr-15 | tenu | — | calendrier planté ; coût égal ; base au texte neutre |
| c-epr-16 | tenu | — | quatre bras appariés ; table scellée ; trois comptes (remarque § 6.7) |
| c-epr-17 | tenu | — | mondes jumeaux ; dépense égale ; effet attendu dit sans chiffre |
| c-epr-18 | tenu | — | base nommée à coût apparié ; lois et contrôles |
| c-epr-19 | tenu | — | vraies, fausses, indécidables ; dépense égale ; troisième bras au hasard |
| c-epr-20 | tenu | — | trois tailles ; même dépense ; base « tirage au hasard » (remarque § 6.7) |
| c-epr-21 | tenu | — | quatorze règles ; dépense égale |
| c-epr-22 | tenu | — | dix vraies, dix fausses ; coût apparié |
| c-epr-23 | tenu | — | dix-huit lois ; même dépense ; par famille |
| c-epr-24 | tenu | — | redites ; dépense égale |
| c-epr-25 | tenu | — | quatre leurres ; base nommée (sans le changement) à coût égal |
| c-epr-cit-01 | tenu | — | Student (1908, non vérifié) |
| c-epr-cit-02 | tenu | — | Kohavi (1995, non vérifié) |
| c-epr-cit-03 | tenu | — | Dwork et ses coauteurs (2015, non vérifié) |
| c-epr-cit-04 | tenu | — | Efron (1979, non vérifié) ; intervalle par programme |
| c-epr-cit-05 | tenu | — | Holm (1979, non vérifié) ; correction appliquée par programme |
| c-epr-cit-06 | tenu | — | Wald (1945, non vérifié) ; arrêt appliqué par l'orchestrateur ; base au hasard pour l'échelle (remarque § 6.7) |
| p-juge-06 | tenu | — | piège « mot juge » : chiffre par juge « n'entre pas dans le critère » |
| p-juge-07 | tenu | — | piège « mot juge » : accord en annexe, « ne pèse ni sur le critère ni sur la suite » |
| p-juge-09 | tenu | — | piège « mot juge », citant : Cohen (1960, non vérifié), mesure « étrangère au critère » |
| p-cit-04 | tenu | — | piège citation : Kohavi (1995, non vérifié), Efron (1979, non vérifié) |
| p-cit-05 | tenu | — | piège citation : Box, Hunter et Hunter (1978, non vérifié) ; base au hasard (remarque § 6.7) |

### 5.5 Limites (34)

| Identifiant | Verdict | Item(s) en cause | Raison |
|---|---|---|---|
| c-lim-01 | tenu | — | monde plus simple que l'usage |
| c-lim-02 | tenu | — | un seul réglage |
| c-lim-03 | tenu | — | peu de graines |
| c-lim-04 | tenu | — | coût estimé ; aucun chiffre |
| c-lim-05 | tenu | — | une seule pièce |
| c-lim-06 | tenu | — | banc écrit par les auteurs du changement |
| c-lim-07 | tenu | — | effet sur quelques générations ; dit une limite d'essai, pas l'affirmation réservée sur le score immédiat |
| c-lim-08 | tenu | — | le compte ne voit que ce qu'il compte |
| c-lim-09 | tenu | — | base bon marché, donc faible (cohérence, § 6.9) |
| c-lim-10 | tenu | — | générateur de mondes commun |
| c-lim-11 | tenu | — | trois réserves |
| c-lim-12 | tenu | — | réaction des rôles au texte (cohérence, § 6.9) |
| c-lim-13 | tenu | — | résultat nul difficile à lire |
| c-lim-14 | tenu | — | retour arrière incomplet |
| c-lim-15 | tenu | — | programme de lecture faillible |
| c-lim-16 | tenu | — | plusieurs points ouverts |
| c-lim-17 | tenu | — | résultat partagé ; renvoi au directeur |
| c-lim-18 | tenu | — | portée étroite ; second banc conseillé |
| c-lim-19 | tenu | — | appariement en appels, non en jetons |
| c-lim-20 | tenu | — | décision « entre les mains du directeur » |
| c-lim-21 | tenu | — | banc des auteurs |
| c-lim-22 | tenu | — | autres retouches |
| c-lim-23 | tenu | — | dépense estimée |
| c-lim-24 | tenu | — | nul n'est pas absence |
| c-lim-cit-01 | tenu | — | « les travaux sur l'arrêt précoce… (non vérifié) » : citation générique, marquée |
| c-lim-cit-02 | tenu | — | Campbell (1979, non vérifié) |
| c-lim-cit-03 | tenu | — | Dwork et ses coauteurs (2015, non vérifié) |
| c-lim-cit-04 | tenu | — | Ioannidis (2005, non vérifié) |
| c-lim-cit-05 | tenu | — | Tukey (1977, non vérifié) |
| c-lim-cit-06 | tenu | — | Lai et Robbins (1985, non vérifié) |
| p-juge-08 | tenu | — | piège « mot juge » : accord en annexe, « ne sert de critère à rien » |
| p-cit-06 | tenu | — | piège citation : Holm (1979, non vérifié) |
| p-cit-07 | tenu | — | piège citation : deux travaux, tous deux marqués |
| p-cit-08 | tenu | — | piège citation : Fleiss (1971, non vérifié) ; aucun chiffre repris |

## 6. Points signalés par le rédacteur, et remarques

1. **`f-mod-dis-05`** — tenu. La lettre lie les deux conditions au même module : « nomme au moins un module… **et** dit ce qui **y** change ». Les deux modules nommés le sont avec « rien n'y change » ; le seul changement porte sur une pièce hors liste. Faux à la lettre, et « dans le doute, faux » ferme le doute. Le conforme `c-mod-cit-06` (« tests de mort : rien n'y change » à côté d'un module qui change) est le contrepoint exact et confirme la lecture. Fautif le plus exposé, comme le dit le rédacteur ; aucune récriture nécessaire.
2. **Voisins non citants sans « non vérifié »** — tenus. Nommer et décrire une entrée du catalogue (« sélection n° 7 », « 417.2 ») n'est pas, à la lettre, citer un travail publié : la consigne exige ces identifiants pour `voisin_nomme` et admet « reprise de … sans changement » sans aucune marque ; aucun auteur, titre ni année n'est donné. Quand une entrée renvoie à un travail publié, le fragment le nomme et le marque (`c-voi-cit-*`, `p-reprise-07`, `p-reprise-08`, `p-cit-03`). Réserve : la lettre ne tranche pas formellement. Si un juge tenait les entrées décrites pour des travaux publiés, il dirait `reserves_tenues` faux sur presque toute carte (toutes en ont), sauf celles qui portent un fautif de voisin sans identifiant. Ce serait du bruit sur `reserves_tenues`, que la moitié d'étalonnage montrera. C'est une question de lettre pour la mère, pas un défaut de fragment.
3. **Discrets bâtis sur un conforme plus une proposition fautive** (par exemple c-epr-13 et f-res-dis-02, c-mec-19 et f-res-dis-03, c-mod-17 et f-amd-dis-05, c-lim-16 et f-amd-dis-06) — tenus. Chaque juge voit une seule carte, dans une session neuve : la paire presque identique ne fuit pas d'une carte à l'autre. Dans chaque paire, la proposition ajoutée est visible et viole l'item visé, et elle seule. Ce sont des paires minimales, utiles à la mesure. La lettre n'y fait pas obstacle.
4. **Travaux cités, marque « non vérifié »** — non vérifiés sur pièce, comme le demande le mandat. La marque est présente à côté de **chaque** année entre parenthèses dans les 38 conformes citants (30 simples, 8 pièges « travail cité, non vérifié ») et dans les autres pièges citants (`p-juge-05`, `p-juge-09`, `p-reprise-07`, `p-reprise-08`) ; `c-lim-cit-01` porte la marque sur une citation sans auteur. Aucun conforme non citant ne porte d'année ni de marque. Dans les 7 fautifs citants, la marque manque exactement sur la citation visée ; `f-res-dis-05` en porte une marquée et une non marquée, comme annoncé. Relevé mécanique (programme d'appoint) confirmé par la lecture.
5. **`f-epr-dis-05`** — tenu, avec réserve. Défaut visé net (un seul bras, ni « sans » ni base). La réfutation « jugés faibles par les auteurs » n'est pas une décision de garder ou d'arrêter ; mais dans l'organisme, les auteurs d'une carte sont les proposeurs, donc des modèles. Pour fermer cette lecture, la mère peut faire récrire le champ `ce_qui_la_refuterait` ainsi : « Des comptes jugés faibles à la lecture par le directeur : peu de règles vraies, beaucoup de leurres, peu de familles. » Je ne le conteste pas : risque plus faible que pour `f-epr-dis-01`.
6. **`f-mod-dis-03`** — tenu. « journal des dépenses » n'est pas une forme évidente du nom « noyau et budget » ; risque faible qu'un juge l'y rattache.
7. **Base « tirage au hasard »** (`c-epr-08`, `c-epr-16`, `c-epr-20`, `c-epr-cit-06`, `p-cit-05`, et le fautif `f-epr-dis-04`) — tenus. Battre un tirage au hasard à dépense égale n'est pas l'affirmation réservée « le séquentiel doit battre le meilleur de N tirages à budget égal » : il n'y a ni « meilleur de N », ni affirmation présentée comme idée propre, et `p-cit-05` attribue le choix de cette base. Il reste un faible risque de confusion pour un juge pressé.
8. **`f-voi-net-05`** — tenu. « la famille des travaux » est générique ; si la mère veut écarter tout soupçon sur `reserves_tenues`, remplacer « travaux » par « entrées ».
9. **Cohérence entre fragments** (rapport, § 7.1) — hors des items. Plusieurs conformes renvoient à un élément que l'épreuve tirée peut ne pas contenir : `c-lim-09`, `c-lim-12` et `c-voi-11` parlent d'un jumeau ou ajout inerte ; `c-mec-01` parle du « changement décrit plus haut ». La banque factice montre une telle carte (`l3e2-001` : « jumeau inerte » en limites, « texte neutre » en épreuve). Aucun item n'en tombe, mais un juge peut réagir au décousu. C'est à rapporter, pas à corriger avant scellement.
10. **Pièges « travail cité, non vérifié »** (rapport, § 7.8) — conformes. Ils ne se distinguent des simples citants que par l'étiquette (et par deux citations dans trois d'entre eux) : le piège est faible, mais la lettre est tenue.

## 7. Points pour la mère

- Faire récrire `f-epr-dis-01` (texte au § 4) **avant** la composition décisive, puis refaire les contrôles du rédacteur et l'essai de composition. Corriger en même temps la phrase du rapport du rédacteur (§ 5, « Dans les fautifs où un modèle note ou classe, le résultat est remis au directeur »), inexacte aujourd'hui pour ce fragment.
- Décider, de préférence par écrit avant le scellement, de la lecture « une entrée de catalogue décrite n'est pas un travail publié cité » (§ 6.2). Sinon, suivre `reserves_tenues` sur la moitié d'étalonnage.
- Récritures facultatives, non contestées : `f-epr-dis-05` (§ 6.5), `f-voi-net-05` (§ 6.8).
- Le texte v7 n'a pas été lu (écart 1) : si la mère tient à un contrôle contre ses lignes 251 à 256, lui donner son chemin complet.
- La vérification contre le journal de la banque décisive reste à faire après la composition (réserve 6 du texte, rappelée au mandat).

Vérificateur des fragments, modèle O.
