# Rapport du rédacteur — banques de fragments des témoins de l'étage 2 à 200 (ligne 3, organisme v9) — v1

Pièce de travail (classe C). Signé : rédacteur neuf, modèle F. Date : 2026-11-20.
Mandat suivi : `mandat-redacteur-fragments-etage-2-v1.md`, `293b3d28954f7b7c324b16613215272025a7ccef22562e8f168f8b65b0c642a1` (vérifié).

## 1. Pièces rendues (dossier du rédacteur)

Dossier : `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/redacteur-fragments-etage-2/`

| Pièce | Empreinte |
|---|---|
| `fragments-etage-2-ligne-3-v1.json` | `0db8bba23e1637e064f17ecf25cdef2ae4147f4198b69f7928989360bd1027e3` |
| `rapport-redacteur-fragments-etage-2-v1.md` | au compagnon `.sha256` |
| `essai_composition.py` (pilote de l'essai, écrit par moi) | au compagnon `.sha256` |
| `essais/tour-3/` (banque factice, journal, partage, manifeste, rapport d'audit de l'essai) | compagnons posés par le générateur |

Pièces qui font foi, empreintes vérifiées avant lecture : texte v7 (`4e3680d9…`), consigne figée (`b03f33b8…`), témoins v2 (`84a1e0ea…`), générateur v2 (`a3a4e82f…`, copie de travail de même empreinte), additif 3 v3 (`71b7a876…`, extrait de `origin/main` par `git show` redirigé). Le fichier d'exemple a été lu pour la forme. Le rapport du développeur (`64254de5…`) n'a pas été ouvert : son chemin n'est pas au mandat et je n'ai lancé aucune liste hors de mon dossier ; le schéma a été pris dans `valider_fragments`, que mon fichier passe (écart 1).

## 2. Comptes

**Fragments conformes : 177.**

| Catégorie | Simples non citants | Simples citants | Piège « mot juge » | Piège « reprise assumée » | Piège « travail cité, non vérifié » |
|---|---|---|---|---|---|
| modules | 25 | 6 | 2 | 0 | 0 |
| mecanismes | 24 | 6 | 3 (dont 1 citant) | 0 | 2 |
| voisins | 24 | 6 | 0 | 8 (dont 2 citants) | 1 |
| epreuves | 25 | 6 | 3 (dont 1 citant) | 0 | 2 |
| limites | 24 | 6 | 1 | 0 | 3 |
| Total | 122 | 30 | 9 | 8 | 8 |

**Fragments fautifs : 82.**

| Item | déclaré | net | discret | Total | Catégories |
|---|---|---|---|---|---|
| `module_nomme` | 4 | 6 | 6 | 16 | modules 16 |
| `voisin_nomme` | 4 | 6 | 6 | 16 | voisins 16 |
| `epreuve_plantee` | 4 | 6 | 6 | 16 | epreuves 16 |
| `aucun_modele_ne_decide` | 4 | 6 | 6 | 16 | mecanismes 8, modules 5, limites 3 |
| `reserves_tenues` | 4 (3 non citants, 1 citant sans marque) | 7 (4 et 3) | 7 (4 et 3) | 18 | limites 5, mecanismes 4, epreuves 4, voisins 3, modules 2 |

Les fautifs des quatre premiers items ne citent pas : la citation d'un mauvais de ces items est portée par un fragment conforme citant d'une autre catégorie, marqué « non vérifié ». Les sept fautifs citants sont tous de `reserves_tenues` : la marque manquante y est le défaut planté.

## 3. Cible de taille du pool (M5)

Cible écrite avant l'essai : au moins 20 fragments simples non citants par catégorie, répartis sur quatre paliers de longueur ; au moins 6 simples citants par catégorie, sur trois paliers ; au moins 8 fragments par piège ; par item, au moins 4 fautifs déclarés, 6 nets et 6 discrets, dont au moins 3 non citants par niveau.

Justification. Avec n fragments par catégorie, la part attendue de paires de témoins à quatre fragments communs sur cinq est de l'ordre de 5/n⁴ ; sur 19 900 paires, cela donne moins d'une paire à n = 20, à tirage uniforme. Le tirage n'est pas uniforme : les bandes de longueur basses (1 200 à 1 600) ne se composent qu'avec les fragments courts. Au tour 1 (20 par catégorie), le maximum était de 3 fragments communs, sur 10 paires, et un fragment court servait 18 fois. J'ai donc ajouté 22 fragments courts (4 ou 5 par catégorie) : le pool final est de 24 ou 25 simples non citants par catégorie, et il n'y a plus que 3 paires à 3 fragments communs.

## 4. Essai de composition (mode essai, racine 2026111930, sortie sous mon dossier)

Commande : `python3 -I -B essai_composition.py composer N`. Le pilote charge ma copie du générateur (empreinte contrôlée), appelle `valider_fragments`, `geste_composer` avec `Contexte("essais")`, puis `auditer` avec un service de nature « essai » (fonctions factices de service et de lecture de verdict, aucun juge réel, aucun réseau). La garde de recouvrement n'a pas été lancée ; le fichier des cartes n'a pas été ouvert.

| | Tour 1 | Tour 2 | Tour 3 (final) |
|---|---|---|---|
| Empreinte des fragments | `9b658ec8…` | `d3778230…` | `0db8bba2…` |
| Schéma (`valider_fragments`) | passe | passe | passe |
| Proportions (additif 3 v3, § 4.2) | passent | passent | passent |
| Longueurs | 1 214 à 2 790 | 1 208 à 2 798 | 1 208 à 2 798 |
| Contenus identiques | 0 | 0 | 0 |
| Maximum de fragments communs | 3 (10 paires) | 3 (3 paires) | 3 (3 paires) |
| Paires à 0, 1, 2 fragments communs | 16 638, 3 020, 232 | 17 355, 2 422, 120 | 17 359, 2 418, 120 |
| Usage maximal d'un fragment | 18 | 15 | 14 |
| Aire qui décide (≤ 0,60) | 0,538 | 0,499 | 0,514 |
| Aire à tous les traits (rapportée) | 0,599 | 0,656 | 0,673 |
| Lettre, modules distincts (0,35–0,65) | 0,610 | 0,490 | 0,490 |
| Lettre, « non vérifié » | 0,488 | 0,488 | 0,488 |
| Lettre, « prédit » | 0,498 | 0,479 | 0,479 |
| Juges scriptés : longueur, champ lu, citation | 0,50 ; 0,525 ; 0,50 | 0,50 ; 0,515 ; 0,50 | 0,50 ; 0,52 ; 0,50 |
| Décision de l'audit | banque passée | banque passée | banque passée |

Proportions au tour 3 : 200 témoins ; 100 bons (50 citants) ; 100 mauvais (50 citants) ; par item 20 mauvais (4 déclarés, 8 nets, 8 discrets ; 10 citants) ; 100 en lecture, 100 en étalonnage. Juge parfait à 0 d'erreur (cas sain). Convergence de la régression à chaque pli.

**Trois tours, aucun sur refus de l'audit.** Avant le tour 1, sur la mesure des fragments seuls : chiffres ajoutés aux fautifs de voisins et d'épreuves, deux fautifs de mécanismes raccourcis, un axe changé. Entre les tours 1 et 2 : l'aire du trait « modules distincts » était à 0,610, dans la bande mais proche du bord ; j'ai retiré des noms de modules de cinq fautifs de `aucun_modele_ne_decide`, écrit « juges croisés » dans quatre pièges « mot juge », raccourci trois fautifs de modules, et ajouté les 22 fragments courts. Entre les tours 2 et 3 : deux fragments récrits pour un bardeau de huit mots commun avec un témoin v2 (voir § 6), un troisième par précaution.

Limite de l'essai : la graine décisive (2026111934) n'est pas celle de l'essai. Les valeurs ci-dessus ne prédisent donc pas celles de la banque décisive ; elles disent que le pool passe sur un tirage.

## 5. Table des fragments fautifs : item violé et trait visible

Chaque fautif viole la lettre d'un seul item, dans le champ dit ; les autres champs du fragment sont conformes.

### `module_nomme` (champ `module_change`)

| Identifiant | Niveau | Trait visible |
|---|---|---|
| f-mod-dec-01 | déclaré | « l'organisme dans son entier », « ne vise aucune pièce en particulier » |
| f-mod-dec-02 | déclaré | « aucune pièce précise n'est visée », « l'ensemble du système » |
| f-mod-dec-03 | déclaré | « ne désigne volontairement aucune partie de l'organisme » |
| f-mod-dec-04 | déclaré | « le système en général, et non l'une de ses pièces » ; dit ne pas dire ce qui change |
| f-mod-net-01 | net | « la chaîne de traitement » : aucun module de la liste, changement vague |
| f-mod-net-02 | net | « tout le dispositif » : aucun module |
| f-mod-net-03 | net | « le fonctionnement d'ensemble » : aucun module |
| f-mod-net-04 | net | « les étapes de l'organisme » en général : aucun module |
| f-mod-net-05 | net | « le système », « à tous les étages » : aucun module |
| f-mod-net-06 | net | « l'ensemble de la chaîne » : aucun module |
| f-mod-dis-01 | discret | changement précis, sur le « relais d'appels », qui n'est pas dans la liste |
| f-mod-dis-02 | discret | changement précis, sur l'« orchestrateur », hors liste |
| f-mod-dis-03 | discret | « lanceur » et « journal des dépenses », hors liste |
| f-mod-dis-04 | discret | « format des identifiants » et « gabarit de la fiche », hors liste |
| f-mod-dis-05 | discret | « tableau de synthèse », hors liste ; juges croisés et proposeurs sont nommés avec « rien n'y change » : un module nommé sans ce qui y change |
| f-mod-dis-06 | discret | « fichier de configuration » et « horodatage des sorties », hors liste |

### `voisin_nomme` (champs `plus_proche_voisin`, `ce_qui_distingue`)

| Identifiant | Niveau | Trait visible |
|---|---|---|
| f-voi-dec-01 | déclaré | « aucun identifiant n'est donné ici » ; champ de différence dit sans contenu |
| f-voi-dec-02 | déclaré | « pas d'entrée désignée » ; « aucune différence ne peut être dite » |
| f-voi-dec-03 | déclaré | « champ laissé sans identifiant, de propos délibéré » ; « rien de précis ne peut être écrit » |
| f-voi-dec-04 | déclaré | « aucune entrée du catalogue n'est donnée, ni par son numéro ni par son indice » |
| f-voi-net-01 | net | voisin dit en général (« les approches par essais appariés »), aucun identifiant aux deux formes |
| f-voi-net-02 | net | identifiants présents ; différence vide : « l'esprit est voisin, la mise en œuvre est autre » |
| f-voi-net-03 | net | « les 9 entrées […] prises dans leur ensemble » : aucun identifiant |
| f-voi-net-04 | net | identifiants présents ; différence sans rien de précis (« plus générale et mieux ajustée ») |
| f-voi-net-05 | net | « toute la famille des travaux […] sous 3 rubriques » : aucun identifiant |
| f-voi-net-06 | net | identifiants présents ; différence sans rien de précis (« une autre démarche », « un autre niveau ») |
| f-voi-dis-01 | discret | différence concrète, mais voisin dit « la rubrique robustesse », sans numéro ni indice |
| f-voi-dis-02 | discret | identifiant présent, voisin décrit ; la différence se réduit à « d'une manière qu'il est difficile de résumer » |
| f-voi-dis-03 | discret | différence concrète ; « son numéro n'est pas reporté ici » |
| f-voi-dis-04 | discret | identifiants présents, voisins décrits ; « elle est simplement différente » |
| f-voi-dis-05 | discret | différence concrète ; « sans que leurs numéros soient rappelés » |
| f-voi-dis-06 | discret | identifiants présents, voisins décrits ; « s'en démarque à sa façon » |

### `epreuve_plantee` (champ `epreuve_monde_plante`)

| Identifiant | Niveau | Trait visible |
|---|---|---|
| f-epr-dec-01 | déclaré | « pas d'essai pour cette carte » |
| f-epr-dec-02 | déclaré | « l'essai est renvoyé à plus tard, et la carte l'écrit en toutes lettres » |
| f-epr-dec-03 | déclaré | « ne propose pas d'essai sur un banc à vérité connue, et elle le reconnaît » |
| f-epr-dec-04 | déclaré | « il n'y aura pas d'essai avant l'adoption : c'est un choix » |
| f-epr-net-01 | net | courses réelles relues à la main ; ni monde planté, ni bras sans, ni programme |
| f-epr-net-02 | net | cartes réelles notées de un à dix par un modèle lecteur ; la moyenne des notes est le résultat |
| f-epr-net-03 | net | essai « arrêté une fois le changement en place » : renvoyé à plus tard sans le dire |
| f-epr-net-04 | net | avis de lecteurs humains ; pas de bras sans, dépense non égalisée |
| f-epr-net-05 | net | cartes réelles « dont nul ne sait lesquelles sont justes » ; critère : préférence d'un second modèle |
| f-epr-net-06 | net | sujets de l'usage, vérité inconnue ; le verdict du panel de juges tient lieu de mesure |
| f-epr-dis-01 | discret | monde planté, bras, coût égal ; « le critère est la note […] qu'un modèle lecteur donne » |
| f-epr-dis-02 | discret | tout conforme, sauf « deux fois plus d'appels » pour le bras modifié : coût ni égal ni apparié |
| f-epr-dis-03 | discret | tout conforme, sauf « le critère de l'essai est l'avis du panel » |
| f-epr-dis-04 | discret | bras, base, coût égal, programme ; mais banc « tiré des cartes réelles », « aucune table ne le dit » |
| f-epr-dis-05 | discret | monde planté et programme ; « un seul bras », « ni bras sans le changement ni base » |
| f-epr-dis-06 | discret | tout conforme, sauf « le critère n'est pas un compte, c'est le classement […] que rend un modèle arbitre » |

Dans les fautifs où un modèle note ou classe, le résultat est remis au directeur, qui décide : `aucun_modele_ne_decide` reste vrai.

### `aucun_modele_ne_decide`

| Identifiant | Niveau | Catégorie | Trait visible |
|---|---|---|---|
| f-amd-dec-01 | déclaré | mecanismes | « c'est bien un modèle qui décide ici, sans règle écrite ni contrôle par programme » |
| f-amd-dec-02 | déclaré | mecanismes | « la décision de garder ou d'arrêter appartient à ce modèle, et à lui seul » |
| f-amd-dec-03 | déclaré | modules | sélection entre générations : « c'est ce modèle […] qui a le dernier mot » |
| f-amd-dec-04 | déclaré | limites | « l'arrêt d'une lignée […] est remis à un modèle, qui en décide seul » |
| f-amd-net-01 | net | mecanismes | un modèle lecteur « choisit les cinq à transmettre » |
| f-amd-net-02 | net | mecanismes | un modèle arbitre « attribue chaque rôle au modèle de son choix » (composition) |
| f-amd-net-03 | net | mecanismes | la note des juges du panel sert de poids au tirage des agents (score de juge dans un signal de sélection) |
| f-amd-net-04 | net | modules | noyau et budget : un modèle arbitre « fixe lui-même quel modèle tiendra chaque rôle » |
| f-amd-net-05 | net | modules | tests de mort : une carte que le modèle élimine sort, sans autre contrôle |
| f-amd-net-06 | net | limites | à égalité, « c'est un modèle lecteur qui dit laquelle est promue » |
| f-amd-dis-01 | discret | mecanismes | proposition finale : « un modèle lecteur dit laquelle des deux versions est gardée » |
| f-amd-dis-02 | discret | mecanismes | dernière phrase : ouverture du palier ou arrêt « décidée par le modèle chargé de l'aiguillage » |
| f-amd-dis-03 | discret | mecanismes | une phrase : le score du panel de juges « sert ensuite à réajuster cet agent » (signal d'entraînement) |
| f-amd-dis-04 | discret | modules | juges croisés : « le juge le plus sévère décide seul du sort de la carte » |
| f-amd-dis-05 | discret | modules | l'aiguilleur « retire de la génération les cartes de cet axe, sans autre règle » |
| f-amd-dis-06 | discret | limites | dernière phrase : « laisse le modèle arbitre trancher et retenir ou non le changement » |

Les cinq fautifs de modules nomment un module de la liste et disent ce qui y change (C1).

### `reserves_tenues`

| Identifiant | Niveau | Catégorie | Citation | Trait visible |
|---|---|---|---|---|
| f-res-dec-01 | déclaré | limites | non | « personne n'a jamais étudié cette question : le terrain est vierge », dit comme un fait |
| f-res-dec-02 | déclaré | mecanismes | non | « notre idée, et nous la revendiquons » : créditer une génération par sa descendance |
| f-res-dec-03 | déclaré | epreuves | non | coût chiffré, « pour certain », refus de le dire estimation ; pas de « prédit » |
| f-res-dec-04 | déclaré | voisins | oui | travail publié cité « sans marque de réserve », dit comme tel |
| f-res-net-01 | net | limites | non | « apportera 30 % de règles vraies en plus », sans « prédit » |
| f-res-net-02 | net | mecanismes | non | « un constat qui est le nôtre » : score immédiat mauvais guide, sélection gloutonne trop courte |
| f-res-net-03 | net | epreuves | non | coût et gain chiffrés (« quarante appels », « cinq lois vraies de plus »), sans « prédit » |
| f-res-net-04 | net | modules | non | « n'a jamais été étudié nulle part : la zone est libre » |
| f-res-net-05 | net | limites | oui | « comme l'a montré Ioannidis (2005) », sans « non vérifié » |
| f-res-net-06 | net | voisins | oui | « Lehman et Stanley (2011) », sans « non vérifié » |
| f-res-net-07 | net | mecanismes | oui | « établi depuis Fisher (1935) », sans « non vérifié » |
| f-res-dis-01 | discret | limites | non | une incise : « sur un terrain que nul n'a encore exploré » |
| f-res-dis-02 | discret | epreuves | non | une incise : « on en attend 6 de plus dans le bras modifié », sans « prédit » (le coût, lui, est marqué) |
| f-res-dis-03 | discret | mecanismes | non | une phrase : signal « tronqué et actualisé, qui est l'apport propre de cette carte » |
| f-res-dis-04 | discret | voisins | non | dernière phrase : « le sujet n'a jamais été étudié » |
| f-res-dis-05 | discret | limites | oui | deux travaux cités, l'un marqué, l'autre non : « Rosenthal (1979) » |
| f-res-dis-06 | discret | epreuves | oui | « méthode d'Efron (1979) », sans « non vérifié » |
| f-res-dis-07 | discret | modules | oui | « celui de Broder (1997) », sans « non vérifié » |

## 6. Contrôles propres au rédacteur

- **Noms d'items (M4), mot « classe », étiquettes interdites** : aucun, par `valider_fragments` et par la garde « vérité non servie » de la composition.
- **Reprise d'un témoin v2 ou de la consigne.** Mon pilote compare les bardeaux de huit mots de mes fragments à ceux des onze témoins v2 et de la consigne (geste `v2` ; ce n'est pas la garde de recouvrement, aucune carte n'est ouverte). Après le tour 2 : deux fragments avec un bardeau commun avec un témoin v2 (c-mod-cit-03, f-epr-net-02), récrits. État final : 0 champ avec un bardeau commun.
- **Paires voulues.** 93 paires de fragments partagent au moins un bardeau entre eux. C'est voulu pour les fautifs discrets : beaucoup sont un fragment conforme auquel une proposition fautive est ajoutée (par exemple c-epr-13 et f-res-dis-02, c-lim-11 et f-res-dis-01, c-mod-17 et f-amd-dis-05). Deux témoins de la banque peuvent donc avoir un champ presque identique, l'un bon, l'autre mauvais.

## 7. Ce que la lettre ne fixe pas (remarques)

1. **Cohérence entre fragments.** Le générateur tire chaque catégorie à part. J'ai donc écrit des fragments qui se composent : les mécanismes décrivent une manière de conduire le changement, valable pour n'importe quelle pièce ; les épreuves parlent du « changement » sans le décrire ; les voisins se distinguent par la méthode. Un témoin composé reste moins lié qu'une carte écrite d'un trait, et un juge peut y réagir. La lettre ne dit pas si cette cohérence fait partie d'un item.
2. **Identifiant de catalogue et « travail publié cité ».** Les voisins non citants nomment des entrées du catalogue (« sélection n° 7 », « 417.2 ») et les décrivent sans « non vérifié », comme les témoins v2. La lettre ne dit pas si décrire une entrée du catalogue est citer un travail publié. Les 24 voisins simples non citants et 6 reprises sont concernés.
3. **f-mod-dis-05** nomme deux modules de la liste et dit que rien n'y change. Je le lis comme faux à la lettre (« et dit ce qui y change ») ; c'est le fautif le plus exposé à une contestation. Les cinq autres discrets de cet item n'ont pas cette ambiguïté.
4. **Pièces hors liste.** « Orchestrateur », « relais d'appels », « lanceur », « journal » ne sont pas des noms de la liste ; j'ai évité « les juges », « la mémoire », « le budget », qu'un juge pourrait prendre pour une forme évidente d'un nom.
5. **Paramètres de plan et valeurs attendues.** Les épreuves conformes donnent des tailles de banc et des nombres de graines sans « prédit » : ce sont des choix de construction, non des valeurs attendues. Toute valeur attendue (coût, dépense) y est marquée « prédit ». La consigne ne trace pas cette frontière.
6. **Fautifs de voisins sans identifiant** : aucun ne se dit inédit ni sans équivalent, pour ne pas violer aussi `reserves_tenues`.
7. **Travaux cités.** Les citations nomment des travaux réels connus (auteur et année), tous marqués « non vérifié » dans les fragments conformes ; aucun chiffre n'en est tiré. Je n'ai vérifié aucune de ces références sur pièce.
8. **Piège « travail cité, non vérifié » et simple citant** : le schéma ne les distingue que par l'étiquette. Trois des huit pièges portent deux citations marquées, contre une dans tous les simples citants.

## 8. Écarts

1. Rapport du développeur (`64254de5…`) non ouvert, chemin inconnu sans liste ; schéma pris dans le code.
2. Une liste hors de mon dossier a été écrite dans un fichier de mon dossier : `git show origin/main:prereg/organisme-auto-conception-v9/`, redirigé, pour trouver le nom de l'additif 3 v3 que le mandat ne donne pas. Rien d'autre n'a été listé.
3. Le fichier de fragments a été écrit par l'outil d'écriture, puis complété et retouché par l'outil d'édition (remplacements de texte écrits à la main). Aucun programme n'a produit ni assemblé de texte.
4. Le pilote lit, dans le dépôt, la configuration v5 (étiquettes interdites) et la consigne, par les fonctions du générateur, sur empreinte. Le générateur appelle `git rev-parse HEAD` pour son manifeste. Aucune écriture dans le dépôt.
5. Aucun refus de permission, de classifieur ni de garde.
