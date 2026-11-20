# Contre-lecture du générateur des témoins et de la garde de recouvrement — étage 2 à 200 (ligne 3) — v1

Pièce de travail (classe C), écrite le 2026-11-20 par un contre-lecteur neuf, modèle S, sous le mandat `mandat-contre-lecteur-generateur-etage-2-v1.md` (`83711f92e5308584c8f8a85d47f52c16ae9ce50250d0000af947aff437db7402`, recalculée égale à la valeur du mandat). Je n'ai écrit ni le texte de la ligne 3, ni ses additifs, ni le code d'appel, ni ce générateur. **Le fichier des cartes n'a été ouvert ni par moi, ni par un programme que j'ai lancé ; aucune commande sur un chemin sous `archives-reponses-modeles/`.** Aucun appel à un fournisseur, aucune dépense, aucune clé, aucune écriture dans le dépôt de travail ni dans le clone de l'organisme.

## 0. Verdict

**Conforme.** Aucune correction du code n'est exigée avant l'additif de code. Trois textes du rapport du développeur sont à mettre à jour (§ 5, points T1 à T3) et six points vont à la mère avec une recommandation (§ 6, M1 à M6) ; deux recommandations de code, non bloquantes, sont au § 5 (C1, C2). Aucune ne touche une des cinq conditions de la garde ni une proportion de l'additif.

## 1. Pièces et empreintes (recalculées)

| pièce | sha256 | état |
|---|---|---|
| `generer_temoins_ligne_3_v1.py` | `b264760c2234d00972f4c217f55e1233327824164f1e02beb7554910cd9c6dbb` | égale au compagnon et à la table |
| `essais_generer_temoins_ligne_3_v1.py` | `79bd8d87cf2c6d0b7fd9fd809e05255dd5203d271d2930074cfef122b3d89add` | idem |
| `fragments-exemple-essais-v1.json` | `a66cf6d4ae04a66a3f90e9f0108e09cf68c911ba3ee25852bdcedcc093311cbd` | idem |
| `rapport-developpeur-generateur-etage-2-v1.md` | `c447ed60d6d6b23ab4d67a1c9dda321f304999fb1a01fc1846ff5559b92d0589` | idem |
| `table-empreintes-generateur-v1.txt` | compagnon vérifié | OK |
| additif 3 v3, `origin/main:prereg/organisme-auto-conception-v9/additif-3-preenregistrement-ligne-3-portee-200-v3.md` (`git show` redirigé, copie `additif-3-v3-extrait-main.md`) | `71b7a876398cdcc133f006c01ff7eb644e8f2c69be79e90be50088bd26492807` | égale à celle du rapport |
| texte v7 (l. 20-34, 240-266, 296-307, 350-389, 552-564), consigne figée, témoins v2 (`84a1e0ea…`, recalculée égale dans mon programme), configuration des juges | lus | — |
| clone de l'organisme, commit | `a41b7b50f7c64ce488c120bb89ad3d25fb1dd1cb` (`git rev-parse HEAD`) | égal à celui du texte |
| cinq modules du service des juges dans le clone (`pole/__init__.py`, `outils.py`, `caviardage.py`, `fiches_v53.py`, `juges_croises_v53.py`) | `f7341b96…`, `966d9553…`, `78abfd47…`, `7cfcf832…`, `c4c6ab12…` | **égaux un à un** aux constantes `MODULES_ORCHESTRATEUR` du code d'appel v4 (l. 125-131) |

## 2. Essais : lecture d'abord, puis rejeu

**Lecture avant tout lancement : aucun essai n'ouvre le vrai fichier des cartes.** Ce que j'ai lu dans `essais_generer_temoins_ligne_3_v1.py` :
- La seule apparition du chemin réel est l. 732-733, une comparaison de chaînes `str(G.CHEMIN_CARTES) == "…"` ; l. 736, `G.EntreeCartes.production()` est seulement construite (`ouvertures == 0`, l. 737), jamais lue. `lire_octets` (code l. 857-860) n'est appelée par aucun essai sur une entrée de production.
- Tous les lancements de la garde passent par la fixture `Lancer` (l. 108-126), qui construit `EntreeCartes.essai(cartes_p, …)` sur un faux fichier écrit dans un dossier temporaire et le passe à `G.principal(argv, entree_cartes=entree, entree_v2=v2)` (l. 118, 123). Aucun essai n'appelle `principal(["garde", …])` ou `jouer_la_garde` sans entrée explicite (recherche de `jouer_la_garde`, `principal(`, `EntreeCartes` : seules lignes 118, 123, 726, 736, 901). L. 901, la ligne de commande n'est jouée que pour `composer`.
- `EntreeCartes.essai` appelle `garde_chemins` (code l. 852), qui refuse tout composant `archives-reponses-modeles` ou commençant par « coffre » sur la forme écrite, avant tout appel au système de fichiers ; l'essai l. 723-726 le montre sur des chemins factices d'un dossier temporaire.
- Le code d'appel v4, importé par empreinte, ne cite `archives-reponses-modeles` que dans sa propre garde (l. 146, 305).

Rejeu sur une copie de G (`…/contre-lecture-generateur-etage-2/copie-G`), Python 3.13.18 (`python3 --version`) : **68 passed in 4.08s**, sortie dans `sortie-essais-rejoues-v1.txt`. Les essais ont créé `tmp-essais/` à côté de la copie (voir C2).

## 3. Silence n° 1 : forme réelle du fichier des cartes, établie sans l'ouvrir

**Forme réelle : un objet JSON dont chaque clé est l'identifiant d'une carte et dont chaque valeur est `{"contenu": {…dix champs…}, "empreinte": "<64 hexadécimaux>", "meta": {…}}`. Il n'y a pas de clé `id` dans la carte : l'identifiant est la clé de l'objet.**

Établi sur le code de l'organisme (clone, commit `a41b7b50…`), par recherche bornée de `fiches.json` :
- `orchestrator/pole/course2_v56.py:366-367` : `ecrire_json_scelle(os.path.join(self.sortie, "fiches.json"), {f["ident"]: {"contenu": f["contenu"], "empreinte": f["empreinte"], "meta": f["meta"]} for f in lot})`. Même forme aux versions antérieures : `course2_v55.py:139-140`, `course2_v54.py:437-438`, `course2_v53.py:476-478`. Les versions 57 et 59 de la course n'ont pas leur propre écriture de `fiches.json` (elles reprennent la génération de la version 56 : `course2_v57.py:27`, `course2_v59.py:54`, aucune ligne `fiches.json`).
- `orchestrator/pole/outils.py:67-69` : écriture JSON, indentation 2, clés triées.
- La course v9 a bien tourné sur ce code : le lanceur épingle `pole/course2_v56.py` à `14f65569…` (`scripts/lancer_course_auto_conception_v9.py:504`), valeur que je retrouve par `sha256sum` sur le fichier du clone. Ce lanceur compte les cartes par `len(json.loads(fiches.json))` (l. 2484-2486), compatible avec un objet.
- `orchestrator/pole/fiches_v53.py:4-5, 30-46` : une fiche est `{"ident", "contenu", "empreinte", "meta"}` ; `contenu` est un dictionnaire (refus sinon, l. 31-32) et ne peut contenir ni `meta` ni `ident` ni `empreinte` (clés réservées, l. 19 et 33-35) : **aucune clé `meta` imbriquée dans `contenu` n'est possible**, ce qui referme la question du silence n° 3.
- Identifiant : `"f" + jeton_opaque(…, 6)` (`course2_v53.py:246, 428`, `course2_v56.py:217`) ; `graines_v53.py:65-67` : six octets, soit douze hexadécimaux, donc **treize caractères**, exactement la longueur des sept identifiants nommés à l'en-tête du texte (`fb3a2cc87251c`, …).

Couverture par le code : `cartes_du_fichier` (code l. 895-916) prend la troisième forme (l. 904-905) : objet non vide dont toutes les valeurs sont des objets, paires `(clé, carte)`, identifiant = la clé (l. 913), `meta` retiré au premier niveau de chaque carte (l. 912). Les deux premières formes (liste ; `{"fiches": […]}`) ne se déclenchent pas sur la forme réelle (`objet.get("fiches")` n'est pas une liste). La chaîne `empreinte` de 64 hexadécimaux, lue comme texte, ne forme qu'un « mot » : aucun bardeau de huit mots. **Les trois formes admises et le choix de la clé de l'objet couvrent la forme réelle : le refus `FormatCartesInconnu` après une ouverture comptée ne devrait pas se produire.** Le compte de 94 est `len(objet)`.

Recommandation : le rapport (§ 6, silence 1) et l'additif de code gagnent à écrire cette forme réelle avec ces références (T1).

## 4. Le code contre la lettre

Recomptage indépendant (`verifs_independantes_generateur_v1.py`, sortie `sortie-verifs-independantes-v1.json`, fragments factices, racine des essais) :

| point de la lettre | constat |
|---|---|
| 100 bons : 50 simples, 50 à piège ; 50 citants (25 + 25 dans chaque type) | 100/100 ; types : 25 simples citants, 25 simples non citants, 25 à piège citants, 25 à piège non citants ; 50 citants. Lecture de l. 176 de l'additif (« 13 et 12 devient 25 et 25 ») : conforme |
| 100 mauvais : 20 par item ; 4 déclarés, 8 nets, 8 discrets ; 50 citants, 10 par item | exact pour les cinq items ; citants tirés sur les niveaux (de 1 à 7 par cellule selon le tirage, comme le texte le dit : « répartis sur les niveaux par tirage à graine ») |
| citation des bons « tous marqués non vérifié » ; des mauvais marquée sauf le défaut planté | code l. 549-552 (conformes), 578-581 (fautifs) ; sur la banque factice, deux mauvais de `reserves_tenues` citent sans marque (le défaut planté), aucun autre écart drapeau/texte |
| longueurs 1 200 à 2 800, entrelacées | min 1 200, max 2 798 ; la longueur du journal égale le recalcul ; huit bandes de 200 caractères, effectifs de 12 ou 13 dans chaque classe ; moyennes 1 992 (bons) et 2 008 (mauvais) |
| journal de construction = la vérité | recalculé ; classe, type, piège, item, niveau, citation, porteur, bande, longueur, tirages, fragments par catégorie (code l. 762-765) |
| partage stratifié | 100/100 ; 50/50 par classe ; 10/10 par item ; 2/4/4 et 2/4/4 par item et niveau ; 25/25 des bons citants ; écart maximal d'une strate (classe, item, niveau, citation) : 1. Les blocs (item, niveau) sont de taille paire et contigus dans l'ordre de tri : la méthode (alternance) les rend exacts |
| audit : aire qui décide ≤ 0,60 ; aire à tous les traits rapportée | 23 traits de présentation (longueur totale, dix longueurs, dix nombres de phrases, chiffres, citation), 15 de plus pour l'aire rapportée (13 modules, « non vérifié », « prédit ») ; aire qui décide 0,5394, **identique à mon décompte par paires** ; tous traits 0,594 |
| traits de la lettre, 100 bons contre 80 mauvais, bande 0,35–0,65 | 100 et 80 pour les trois traits ; exclusions correctes (`module_nomme` pour le premier, `reserves_tenues` pour les deux autres) ; aires 0,5 |
| régression logistique pénalisée 1,0, `numpy` seul, Newton ≤ 200 | convergence en 5 ou 6 itérations ; norme du gradient pénalisé au point rendu 1,9e-15, recalculée à part |
| dix plis stratifiés par classe, racine 2026111937, clé 11 | 10 et 10 dans chaque pli ; `plis_stratifies` code l. 1290-1298 |
| aire par rangs | égale au décompte par paires, avec ex æquo, sur cinq jeux de mon cru (plus les 20 jeux de l'essai l. 841-850) |
| trois juges scriptés par la fonction de service | parfait 0 ; longueur 0,50 ; champ lu 0,525 ; citation 0,50 ; bande [0,40 ; 0,60] fermée ; le juge parfait en erreur arrête (`BancInvalide`) ; le contenu servi est recomparé au témoin |
| racines et manifeste (R9) | 2026111934 (composition, partage ; clés 1 à 6 ; `.spawn(200)` clé 4) et 2026111937 (plis, clé 11) sous autorisation vérifiée (code l. 384-394, 419-436) ; manifeste : programme, commit, versions, graines et dérivations, configuration et son empreinte ; écriture exclusive et compagnon au format de `sha256sum` (l. 289-297) |
| fragments en données à part | aucun texte de fragment dans le code (relu en entier ; seuls des motifs de recherche et des noms) ; essai l. 264-272 |

Garde de recouvrement, lue ligne à ligne contre le texte (l. 257-263, 374) : toutes les références de lignes du tableau du rapport (§ 5) se vérifient (je les ai relues une à une). Points que j'ai pesés particulièrement : empreinte calculée par le programme avant tout usage (l. 1173-1176) puis forme (l. 1177) puis compte (l. 1185-1186) avant la première comparaison (l. 1195) ; retrait de `meta` avant tout autre traitement (l. 912) ; manifeste (l. 1166) et ligne « ouverture » (l. 1168) écrits avant l'ouverture (l. 1173) ; seul lieu d'ouverture du chemin : `lire_octets` (l. 857-860) ; exceptions : classe et ligne du programme seulement (l. 931-938), rapport à liste fermée validé avant toute écriture (l. 941-978) et avant d'être rendu (l. 1232) ; refus au sixième rejeu avant ouverture (l. 1139-1143, `ouvertures >= 6` : premier passage et cinq rejeux déjà au journal) ; repli par ses deux seuls déclencheurs (l. 1134-1137), sept identifiants trouvés une fois chacun (l. 919-928). Aucun défaut trouvé.

## 5. Corrections et recommandations de texte et de code (non bloquantes)

Textes à mettre à jour dans le rapport avant l'additif de code :
- **T1** — § 6, silence 1 : remplacer « aucun texte lu ne les écrit et le fichier ne peut être ouvert … À confirmer sans ouvrir le fichier » par la forme établie au § 3 de cette contre-lecture : « objet {identifiant : {contenu, empreinte, meta}} ; l'identifiant est la clé de l'objet ; troisième forme admise (code l. 904-905) ; sources : `course2_v56.py:366-367`, `fiches_v53.py:4-5`, `graines_v53.py:65-67` ».
- **T2** — § 6, silences 12 et 15, § 7 (mot « absent ») et en-tête de `generer_temoins_ligne_3_v1.py` l. 1505-1506 (« le dépôt de l'orchestrateur n'est pas sur sa machine ») : le clone existe à `/home/user/lciric/ideation-organism`, au commit `a41b7b50…`, et ses cinq modules ont les empreintes attendues (§ 1). L'énoncé « jamais exercé » reste vrai, la raison change. (Le commentaire du code ne change que par une version neuve, règle R12 : on peut le laisser et le dire dans l'additif.)
- **T3** — Numérotation : le mandat parle de douze silences, le rapport en numérote seize ; j'ai tout traité (§ 6 ci-dessous). Le « silence n° 12 » du mandat est le silence n° 15 du rapport.

Code, recommandations (version neuve si la mère les retient) :
- **C1** — `valider_fragments`, fautifs (code l. 559-583) : aucune garde mécanique n'oblige un fautif de la catégorie `modules`, d'un item autre que `module_nomme`, à nommer un module. Un tel fragment qui n'en nomme aucun violerait deux items à la fois (« un seul item violé par témoin », l. 253) et fausserait le contrôle de la lettre. Texte proposé après l. 581 : `if fr["categorie"] == "modules" and fr["item"] != "module_nomme" and not modules_nommes(fr["champs"]["module_change"]): F.append(f"{fid} : un fautif de modules d'un autre item nomme au moins un module")`. L'audit rattraperait un dérapage massif (bande 0,35–0,65), pas quelques fragments.
- **C2** — Essais : `TMP_RACINE = ICI.parent / "tmp-essais"` (essais l. 22) écrit à côté du dossier du code ; à l'emplacement du dépôt cela crée un dossier non suivi dans `etage-2-portee-200-v1/`. Proposer `tempfile.mkdtemp()` sans `dir=`, ou une consigne de rejeu sur copie (comme le mandat le fait).

## 6. Les seize silences du rapport (§ 6) et les écarts du développeur

| n° | décision | ma lecture |
|---|---|---|
| 1 | juste | forme établie, couverte (§ 3) ; T1 |
| 2 | juste | repli : identifiant égal ou commençant par le nom de treize caractères, trouvé une fois ; sur la forme réelle les identifiants ont exactement treize caractères, donc l'égalité suffit ; le compte de 94 n'est pas exigé sous le repli (le texte l. 263 ne le cite pas, l'empreinte l'est) |
| 3 | juste | retrait au premier niveau, seul niveau où `meta` existe ; pas de `meta` possible dans `contenu` (`fiches_v53.py:33-35`) |
| 4 | juste | bardeaux par chaîne ; côté témoins v2 toutes les chaînes (identifiants et construction compris) : plus strict que le texte, sans risque de fuite ; seule conséquence possible, un refus de plus sur un mot d'identifiant |
| 5 | juste, M3 | troisième valeur « garde non jouée » : nécessaire pour dire un refus de tourner (le texte ne connaît que passée/refusée) |
| 6 | juste, M2 | un mot par rejeu au-delà de cinq ; lecture la plus prudente de « permet seul la suite » (l. 260 : « aucun rejeu de plus sans le mot ») |
| 7 | juste | pièce du contrôle (4) et pièce du déclencheur exigées par chemin et empreinte ; le code n'en lit pas le contenu (dit au rapport § 5) |
| 8 | juste | **vérifié par programme** (`longueurs_v2_verif_v1.py`, sortie `sortie-longueurs-v2-v1.json`) : onze témoins v2, forme JSON indentée : de 1 251 à 2 761 ; somme des champs : de 1 044 à 2 554. Seule la première mesure tient dans l'intervalle « de 1 200 à 2 800 » du texte et est celle de l'épreuve des témoins v9 (`scripts/epreuve_temoins_auto_conception_v9.py:364, 403`) |
| 9 | juste, M4 | catégories → champs conformes aux champs lus par la consigne (module ; voisin + ce qui distingue ; épreuve + coût + réfutation) ; réemploi permis : voir M5 |
| 10 | juste | pièges seulement chez les bons : c'est ce que « bons à piège » dit ; 8/8/8 + 1 chez les citants, 12/13 chez les non citants : mesuré 9/8/8 et 12/13 |
| 11 | juste | une seule catégorie porte la citation (code l. 704-718 : un seul fragment citant par témoin ; le drapeau de citation concorde avec le texte sur les 200 témoins, sauf les deux défauts plantés de `reserves_tenues`) |
| 12 | juste | type du bon ajouté à la strate : plus fin que la lettre ; citants exactement 25/25 par moitié |
| 13 | juste | pénalité, phrases, noms de modules, « prédit », bandes fermées ; l'asymétrie (refus seulement au-dessus de 0,60) est celle de la lettre |
| 14 | juste | définitions identiques à celles de l'épreuve des témoins v9 (`:344-370`, `CHAMP_LU` l. 234, identique mot pour mot au code) ; l'erreur équilibrée de « citation » vaut 0,5 par construction (50/50 dans chaque classe) |
| 15 | juste, voir T2, M6 | `charger_service_des_juges` : les cinq empreintes du clone sont égales ; le format de la fonction de service transcrit dans les essais est celui du code réel : `fiches_v53.py:77-84` (signature `(consigne_figee, fiche, etiquettes_interdites, identifiant_servi=None)`, marque `"\n\n## La fiche\n```json\n"`, clé `identifiant` ajoutée), `juges_croises_v53.py:39-48` et `outils.py:106-128` (lecture du dernier bloc portant `items`, cinq clés booléennes) ; la normalisation du code (`a_le_mot`, `normaliser`) est identique à `outils.py:92-96` et `fiches_v53.py:62-64` |
| 16 | juste | étiquettes interdites lues dans la configuration (empreinte vérifiée) |

Écarts du développeur (§ 9) : tous recevables. Le 3 (format de banque pris dans `valider_banque`) est confirmé par moi : `epreuve_juges_reels_ligne_3_v4.py:381-425`, et l'essai de lecture par le v4.

Ce que change le clone (silence n° 12 du mandat) : (a) la voie réelle de l'audit (`construire_service_reel`) est exécutable **localement, sans fournisseur** : les empreintes sont bonnes ; (b) l'énoncé « la vraie fonction de service » n'est aujourd'hui exercé que par une transcription ; je l'ai relue contre le code réel et ne trouve aucune divergence, mais un exercice du service réel sur la banque factice serait la preuve (M6) ; (c) rien dans le générateur ne change : le clone n'est lu qu'à travers le code d'appel v4, par octets vérifiés. Je n'ai pas lancé le service réel.

## 7. Points pour la mère (avec recommandation)

- **M1 — champs du journal des rejeux hors de la liste fermée du (3).** Les lignes du journal portent `horodatage_utc`, `mot_de_la_mere_sha256`, `nature_entree` (code l. 141-144) en plus de champs de la liste. Aucun ne vient d'une carte. Recommandation : accepter et l'écrire à l'additif de code (« le journal est une sortie distincte du rapport ; ses champs sont fermés par `CHAMPS_JOURNAL_*` ») ; sinon retirer l'horodatage et la nature de l'entrée. Confiance : moyenne.
- **M2 — un mot par rejeu au-delà de cinq.** Recommandation : garder. Si la mère voulait qu'un seul mot lève la borne pour la suite, c'est un changement de code, à dire avant le premier passage.
- **M3 — troisième valeur de décision « garde non jouée ».** Recommandation : garder (codes de sortie 2, 4, 5 la distinguent).
- **M4 — refus des noms d'items en mots normalisés dans les fragments** (code l. 482 : `it in t or a_le_mot(n, normaliser(it))`). Les formes « module nommé », « voisin nommé », « épreuve plantée », « réserves tenues » et surtout « aucun modèle ne décide » sont du français courant ; le rédacteur des fragments (modèle F) verra son fichier refusé s'il les emploie, avec la liste de toutes les fautes. Le texte (l. 360) ne vise que « classe » et l'item planté. Recommandation : garder le refus (il est sans risque pour la vérité non servie) et **l'écrire au mandat du rédacteur des fragments**, pour qu'il ne l'apprenne pas par refus.
- **M5 — réemploi des fragments sans garde de doublons.** Sur la banque factice (pools de 5 à 12 fragments par catégorie) : aucun contenu identique, mais 29 paires de témoins partagent quatre fragments sur cinq et 383 en partagent trois (`doublons_et_usages_v1.py`, sortie `sortie-doublons-usages-v1.json`). Le texte est silencieux ; deux témoins presque identiques dans les deux moitiés (étalonnage et lecture) rendent ces moitiés moins indépendantes. Recommandation : au mandat du rédacteur, une taille minimale de chaque pool ; au code, rapporter (sans refuser) le nombre maximal de fragments communs entre deux témoins et refuser deux contenus identiques. Version neuve si retenu. Confiance : moyenne.
- **M6 — exercice du service réel sur la banque factice, avant le premier tirage décisif.** Un essai de plus, sans fournisseur : `construire_service_reel()` puis `jouer_juges_de_surface` sur la banque factice. Il fermerait la réserve « jamais exercé » du silence 15. À autoriser avant la contre-lecture finale ; je ne l'ai pas lancé (consigne du mandat).

Réserve de portée, sans demande : la borne de 1 200 caractères par champ de l'épreuve des témoins v9 (`BORNE_CHAMP`, `scripts/epreuve_temoins_auto_conception_v9.py:236`) n'est pas reprise par le générateur ; le texte ne la cite pas pour la banque ; le plus long champ des onze témoins v2 est de 573.

## 8. Écarts de ma contre-lecture

1. Pour l'additif 3 v3, `git show` redirigé depuis `origin/main` vers mon dossier (copie `additif-3-v3-extrait-main.md`).
2. Une commande `grep` a été lancée par `env -C <dossier> grep … <nom de fichier relatif>` sur le fichier des témoins v2 (non archivé), au lieu d'une ouverture par chemin complet ; le fichier est du dépôt, hors `archives-reponses-modeles/`.
3. Recherches et lectures du clone de l'organisme et du lanceur de la course par les outils de lecture et de recherche bornée à des fichiers ou dossiers nommés (`pole/` pour `fiches.json`) ; deux `sha256sum` et un `git rev-parse` sur le clone, lecture seule.
4. Mes programmes importent le générateur depuis la copie de G et lisent, par empreinte, la configuration des juges, la consigne figée et les témoins v2 ; aucun n'ouvre le fichier des cartes ni n'appelle la garde.
5. Les essais ont écrit `tmp-essais/` dans mon dossier (C2).

## 9. Pièces de ce dossier

`contre-lecture-generateur-etage-2-v1.md` (cette pièce) ; `verifs_independantes_generateur_v1.py` et `sortie-verifs-independantes-v1.json` ; `longueurs_v2_verif_v1.py` et `sortie-longueurs-v2-v1.json` ; `doublons_et_usages_v1.py` et `sortie-doublons-usages-v1.json` ; `sortie-essais-rejoues-v1.txt` ; `additif-3-v3-extrait-main.md` ; `copie-G/` et `tmp-essais/` (travail). Chaque pièce a son compagnon `.sha256` (`table-empreintes-contre-lecture-v1.txt` donne la liste).

Contre-lecteur, modèle S.
