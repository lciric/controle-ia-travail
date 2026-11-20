# Rapport du développeur — générateur des témoins et garde de recouvrement de l'étage 2 à 200 (ligne 3, organisme v9) — v1

Pièce de travail, écrite le 2026-11-20 sous le mandat `mandat-developpeur-generateur-etage-2-v1.md` (`9066be256c6a4cf00115b56427434a26bc436c1d90717ecf3e761ed0c550cab3`, recalculée égale). Développeur neuf, modèle O, qui n'a écrit ni le texte de la ligne 3, ni ses additifs, ni l'inventaire, ni les calculs du plafond, ni le code d'appel. **Aucune commande, d'aucune sorte, sur un chemin sous `archives-reponses-modeles/`** ; le fichier des cartes n'a été ouvert ni par moi, ni par le code, ni par un essai. Aucun appel à un fournisseur, aucune dépense, aucune clé lue, aucun relais, aucune écriture dans le dépôt de travail ni dans le dépôt de l'organisme.

## 0. Pièces lues (empreintes recalculées, égales à leur compagnon)

| pièce | sha256 | lu |
|---|---|---|
| texte v7, `L3/preenregistrement-ligne-3-votes-effectifs-juges-v7.md` | `4e3680d9915ef6e2fa33010fc9b7b2ef5575d74e58e982bfabdbdbcc3e99d5a0` | l. 1-128 (en-tête, Q1-Q8), 240-389 (étage 2, banque à garde, audit, liste d'arrêt, plafond), 554-564 (annexe A) |
| additif 3 v3, `origin/main:prereg/organisme-auto-conception-v9/additif-3-preenregistrement-ligne-3-portee-200-v3.md` (`git show` redirigé) | `71b7a876398cdcc133f006c01ff7eb644e8f2c69be79e90be50088bd26492807` | en entier |
| inventaire, `L3/etage-2-portee-200-v1/inventaire-etage-2-portee-200-ligne-3-v1.md` | `a2039f7d1e06ea3a045cfe1c1f9142c8ae4bf8e4a49e92a65c454dd00d49cfbe` | en entier (§ 1 gestes 1 à 12, § 5 remarque 1) |
| `origin/main:registres/decisions.md` (`git show` redirigé) | — | R-4183 et R-4246 seulement |
| code d'appel v4, `L3/etage-2-portee-200-v1/code-appel-v4/epreuve_juges_reels_ligne_3_v4.py` | `082d19d61922dbecd64d64435d8a8682f9e01abee6735ff01c6cc550c8f5484c` | en entier |
| onze témoins v2 | `84a1e0ea870ecb54c2de8ec5071e689e2ba409b3c97aecb57ab16ef3388439e0` | en entier |
| consigne figée du juge | `b03f33b87150eb67e5e55f3fc093812e5a359ab655362b3033dde561e58b5167` | en entier |
| hors mandat, déclaré (§ 8) : configuration des juges `course-v4/configuration-course-auto-conception-v5.json` | `3f662ee80e12db7af79428c0bd2b0efe7e560a6a36c440c322343003fe2cc4f8` | items et étiquettes interdites |
| hors mandat, déclaré : `scripts/epreuve_temoins_auto_conception_v9.py` (5be161fa…, empreinte non recalculée) ; banc v3 `code-etage-1-v3/banc_juges_scriptes_ligne_3_v3.py` | — | juges factices « longueur » et « champ lu » ; `verifier_autorisation` |

## 1. Livrables (dossier `generateur-v1/`)

| fichier | sha256 |
|---|---|
| `generer_temoins_ligne_3_v1.py` | `b264760c2234d00972f4c217f55e1233327824164f1e02beb7554910cd9c6dbb` |
| `essais_generer_temoins_ligne_3_v1.py` | `79bd8d87cf2c6d0b7fd9fd809e05255dd5203d271d2930074cfef122b3d89add` |
| `fragments-exemple-essais-v1.json` (factice) | `a66cf6d4ae04a66a3f90e9f0108e09cf68c911ba3ee25852bdcedcc093311cbd` |
| ce rapport et la table | dans `table-empreintes-generateur-v1.txt` |

Chaque fichier a son compagnon `.sha256` (`env -C DOSSIER sha256sum F`, redirigé vers `DOSSIER/F.sha256`).

## 2. Format du fichier de fragments (`schema` = `fragments-temoins-ligne-3-v1`)

Fichier de données à part (R-4246), jamais une constante du code (essai `test_aucun_fragment_dans_le_code`). Lu par empreinte passée en argument ; schéma vérifié au chargement (`valider_fragments`), **toutes** les fautes rendues, aucune corrigée.

```
{"schema": "fragments-temoins-ligne-3-v1", "version": "<libre>",
 "conformes": {"modules":    [F…], "mecanismes": [F…], "voisins": [F…], "epreuves": [F…], "limites": [F…]},
 "fautifs":   [G…]}
F = {"id": ID, "champs": {…champs de la catégorie…}, "citation": bool, "piege": null | "mot_juge" | "reprise_assumee" | "citation_non_verifiee"}
G = {"id": ID, "item": <item de la consigne>, "niveau": "declare" | "net" | "discret", "categorie": <catégorie>, "champs": {…}, "citation": bool}
ID = ^[A-Za-z0-9._-]{1,48}$, unique dans tout le fichier
```

Catégories et champs de la fiche qu'elles portent (choix du développeur, silence 9) : `modules` → `module_change` ; `mecanismes` → `titre`, `axe`, `mecanisme` ; `voisins` → `plus_proche_voisin`, `ce_qui_distingue` ; `epreuves` → `epreuve_monde_plante`, `cout`, `ce_qui_la_refuterait` ; `limites` → `limites`. Un témoin = un fragment par catégorie ; la fiche a les dix champs des témoins v2.

Règles vérifiées au chargement : clés exactes (aucune clé inconnue) ; champs exactement ceux de la catégorie, textes non vides ; aucun texte ne porte le mot « classe », le nom d'un item, ni une étiquette interdite de la configuration (garde « vérité non servie » tenue dès les fragments) ; un fragment conforme cite **si et seulement s'il** porte « non vérifié » ; un fautif qui ne cite pas ne porte pas « non vérifié » ; un fautif qui cite porte « non vérifié », sauf pour `reserves_tenues` (l. 253 : « sauf là où la marque manquante est le défaut planté ») ; catégorie d'un fautif : `module_nomme` → modules, `voisin_nomme` → voisins, `epreuve_plantee` → épreuves, `aucun_modele_ne_decide` et `reserves_tenues` → toute catégorie ; le piège « citation » cite ; le piège « reprise assumée » est un fragment de voisins ; un conforme de modules nomme au moins un module de la consigne. Couverture (pour qu'aucun tirage ne tombe à vide) : dans chaque catégorie, au moins un conforme simple qui ne cite pas ; des conformes simples qui citent dans deux catégories au moins ; chaque piège présent, « mot juge » et « reprise » avec un fragment qui ne cite pas ; pour chaque item et chaque niveau, au moins un fautif qui ne cite pas.

## 3. Ce que le programme écrit

- `composer` → `banque-temoins-ligne-3-v1.json` (`{"version", "fragments_sha256", "items", "temoins": [{identifiant_interne, classe, item, niveau, citation, moitie, contenu}]}`, le format de `valider_banque` du code d'appel v4 ; l'essai `test_banque_lisible_par_le_code_d_appel_v4` charge le v4 par son empreinte et y passe la banque : 200 témoins acceptés), `journal-construction-ligne-3-v1.json` (la vérité : classe, type de bon, piège, item, niveau, citation, catégorie qui porte la citation, bande, longueur, nombre de tirages, fragment employé par catégorie et par identifiant, moitié ; usages par fragment ; fragments jamais employés ; comptes), `partage-ligne-3-v1.json`, `manifeste-composition.json` ; tous scellés.
- `creer-journal-rejeux` → le journal vide et `manifeste-creation-journal-rejeux.json`.
- `garde` → `manifeste-garde.json` (écrit **avant** l'ouverture du fichier des cartes) et `rapport-garde.json` (liste fermée), scellés ; le rapport aussi à la sortie standard ; une ligne « ouverture » puis une ligne « cloture » au journal des rejeux.
- `auditer` → `rapport-audit-ligne-3-v1.json`, `manifeste-audit.json`, scellés.

## 4. À la lettre

- Proportions de l'additif 3 v3, § 4.2 : 100 bons (25 simples citants, 25 simples non citants, 25 à piège citants, 25 à piège non citants) ; 100 mauvais, 20 par item (4 déclarés, 8 nets, 8 discrets ; 10 citants par item, tirés à graine sur les niveaux). Garde `verifier_proportions` : un écart arrête, aucune banque écrite (essais sain et artefact).
- Longueurs de 1 200 à 2 800 caractères, entrelacées entre les classes : huit bandes de 200 caractères ; dans chaque classe, chaque bande reçoit 12 ou 13 témoins (suite de permutations tirées de huit bandes) ; une composition est retirée jusqu'à tomber dans sa bande, au plus 20 000 tirages ; sinon `FragmentsInsuffisants`, nommé (aucun repli).
- Citation équilibrée : 50 et 50 ; les citations des mauvais marquées « non vérifié » sauf le défaut planté de `reserves_tenues`.
- Partage moitié « lecture », moitié « étalonnage », stratifié par classe, item, niveau, citation (alternance à partir d'une parité tirée sur les témoins rangés par strate, ordre tiré dans chaque strate) : 100 et 100 ; 50 et 50 par classe ; 10 et 10 par item ; niveaux exacts ; 25 bons citants par moitié ; toute strate à un près.
- Garde de recouvrement : conditions (1) à (5) et repli, § 6.
- Audit (l. 266) : aire qui décide sur les seuls traits de présentation (longueur totale ; longueur et nombre de phrases de chacun des dix champs ; nombre de chiffres ; citation), refus au-dessus de 0,60 ; aire à tous les traits (plus les treize noms de modules, « non vérifié », « prédit ») rapportée sans seuil, mêmes plis ; contrôle des trois traits de la lettre, aire du trait seul par rangs, 100 bons contre 80 mauvais (`module_nomme` exclu pour le premier, `reserves_tenues` pour les deux autres), bande 0,35–0,65 ; régression logistique à pénalité quadratique 1,0 en numpy, Newton ≤ 200, traits centrés et réduits sur les plis d'apprentissage ; dix plis stratifiés par classe (racine 2026111937, clé 11) ; aire par statistique de rangs, en fraction exacte ; trois juges scriptés de surface (longueur, longueur du champ lu, citation) servis par la fonction de service injectée, lus par `lire_verdict`, bande [0,40 ; 0,60] ; le juge parfait en cas sain (erreur 0, sinon `BancInvalide`).
- Graines (R9) : `SeedSequence(racine, spawn_key=(clé,))`, tables gelées au code et au manifeste : composition 2026111934 (clés 1 citation des mauvais, 2 pièges des bons, 3 bandes, 4 tirage des fragments, `.spawn(200)` un enfant par place, 5 identifiants internes, 6 partage) ; plis de l'audit 2026111937 (clé 11). Ces deux racines ne se dérivent que sous autorisation vérifiée (additif de code par chemin et empreinte) ; toute autre racine du texte est refusée ; les essais ne dérivent que 2026111930.

## 5. Points de la condition (4)

Numéros de ligne de `generer_temoins_ligne_3_v1.py` (`b264760c…`).

| point | où il se tient |
|---|---|
| **Entrée unique** : chemin, empreinte, compte en constantes | l. 125-128 : `CHEMIN_CARTES` (dépôt + `archives-reponses-modeles/auto-conception-course-v9-2026-11-19-v1/course-v9-sortie/sortie/generation-1/fiches.json`), `EMPREINTE_CARTES = "ba65c411f4e3062fba29d93b5a00fe6fee23b34ebdc64f1708a0cc49177c3481"`, `COMPTE_CARTES = 94` ; l. 847 `EntreeCartes.production()` ne prend que ces constantes ; la ligne de commande n'expose aucune autre voie (l. 1608-1622 : `entree_cartes` n'est passable qu'en Python, par les essais) |
| voie d'essai, jamais le vrai fichier | l. 851-855 `EntreeCartes.essai` : `garde_chemins` refuse tout composant `archives-reponses-modeles` ou commençant par « coffre » sur la forme écrite, avant tout appel au système de fichiers (l. 335 et suivantes) |
| **une seule ouverture**, empreinte vérifiée avant tout usage | l. 857-860 `lire_octets` (seul lieu qui ouvre ce chemin, compteur `ouvertures`) ; l. 1173-1176 : empreinte calculée par le programme seul, autre que la constante → `EmpreinteCartesAutre`, ni garde ni repli |
| **compte de 94 avant toute comparaison** | l. 1185-1186 `CompteCartesAutre` ; la référence de bardeaux n'est construite qu'après (l. 1189) et `bardeaux_communs` n'est appelée qu'à l. 1195 (essais : aucune comparaison sur empreinte, compte ou forme fausse) |
| aucun autre chemin de l'archive | l. 1125 : `garde_chemins` sur la banque, le journal, la sortie, le contrôle (4) et la pièce du repli, avant tout |
| **retrait de `meta`** au chargement, avant tout usage | l. 895-917 `cartes_du_fichier`, l. 912 : chaque carte est recopiée sans sa clé `meta` avant tout autre traitement ; l. 1177 : appelée juste après l'empreinte ; le compte, l'identifiant du repli et les bardeaux ne voient que la carte sans `meta` |
| **aucune écriture d'un bardeau ou d'un texte de carte** | bardeaux en mémoire seulement : l. 890 `bardeaux`, l. 1189-1196 (référence locale, supprimée par `del`) ; le manifeste est écrit à l. 1166, **avant** l'ouverture (l. 1173) ; la ligne « ouverture » du journal aussi (l. 1168) ; ce qui sort après l'ouverture : la ligne « cloture » (champs fermés `CHAMPS_JOURNAL_CLOTURE`, l. 143, contrôlés à l'écriture par `JournalRejeux.ajouter`) et le rapport (liste fermée) ; aucun `print` dans la garde ; la sortie standard ne reçoit que le rapport validé (l. 1629) |
| messages d'erreur et traces d'exception | l. 1124 : avertissements changés en exceptions ; l. 1201-1211 : toute exception (`BaseException`) attrapée ; `lieu_de` (l. 931-938) ne rend que `{"classe", "fichier", "ligne"}` (nom de classe, nom du programme, dernière ligne du programme dans la trace), jamais un message ni une valeur ; la trace est détachée ; les refus de la garde sont des classes sans texte (l. 192 et suivantes), dont le nom dit la cause ; l. 1216 et 1227 : idem si la clôture ou l'écriture du rapport échoue ; l. 1623-1628 : idem au niveau de la ligne de commande |
| **liste fermée** des champs de sortie | l. 138 `CHAMPS_RAPPORT_GARDE` (13 champs : comptes, empreintes, décision, identifiants refusés, rejeux, exception, repli) ; l. 941-975 `valider_rapport_garde` : champ hors liste ou valeur hors forme → `RapportHorsListe` (identifiants ∈ banque, empreintes à 64 caractères hexadécimaux, entiers, décision parmi trois, exception à trois clés, repli exactement `{"mention": "repli sur sept cartes", "cause": <un des deux déclencheurs>}`) ; l. 976-978 : refus d'écrire avant toute écriture ; l. 1232 : contrôle avant de rendre |
| **compte des rejeux** | l. 981-1035 `JournalRejeux` : journal à ajout seul (`O_APPEND`, `fsync`), lu en entier au lancement ; absent → `JournalRejeuxAbsent`, illisible (JSON, ligne coupée, numéro, champs, rang) → `JournalRejeuxIllisible`, l. 1131, **avant** toute ouverture ; ligne « ouverture » écrite avant l'ouverture (l. 1168), donc toute exécution qui ouvre est comptée, panne comprise ; `nombre_de_rejeux` = ouvertures − 1, au rapport ; créé vide par `creer_journal_rejeux` (l. 1037), geste à son manifeste |
| **refus au sixième** | l. 132 `MAX_REJEUX_SANS_MOT = 5` ; l. 1139-1143 : si le journal porte déjà 6 ouvertures (premier passage + cinq rejeux), refus `SixiemeRejeuSansMotDeLaMere` avant toute ouverture sans `--mot-de-la-mere` ; un mot déjà cité (empreinte au journal) → `MotDeLaMereDejaCite` ; le texte du mot est cité au manifeste (l. 1161) |
| **chemin du repli** | l. 133 les deux déclencheurs ; l. 1134-1137 : cause hors des deux → `ReplisHorsDeclencheur`, pièce du déclencheur exigée par chemin et empreinte, avant ouverture ; même fichier, même ouverture, même empreinte (l. 1173-1176), même retrait de `meta`, l. 1183 et l. 919-928 `cartes_nommees` : les sept identifiants de l'en-tête (l. 129), chacun trouvé une fois et une seule, sinon `CartesNommeesIntrouvables` ; même liste fermée, `repli` au rapport, écart au manifeste ; même journal, le compte continue |
| contrôle (4) écrit exigé | l. 1133 : la garde ne tourne pas sans la pièce du contrôle, par chemin et empreinte (`ControleQuatreAbsentOuFaux`), avant toute ouverture |
| seconde entrée | l. 1085-1097 `_bardeaux_v2` : empreinte `84a1e0ea…` et compte de 11, avant l'ouverture du fichier des cartes |

Ce que le code ne peut pas contrôler : que la pièce du contrôle (4) dise « conforme » (il en exige seulement l'existence et l'empreinte) ; que la forme réelle du fichier des cartes soit l'une des trois formes admises (silence 1).

## 6. Silences de la lettre : nommés, non tranchés par le texte ; choix faits (à porter à la mère)

1. **Forme du fichier des cartes et champ de l'identifiant** : aucun texte lu ne les écrit et le fichier ne peut être ouvert. Formes admises : liste de cartes ; `{"fiches": [...]}` ; `{identifiant: carte}`. Identifiant : la clé `id` de la carte (ou la clé de l'objet). Si la forme réelle est autre, la garde refuse (`FormatCartesInconnu`) **après une ouverture, comptée comme passage ou rejeu**. À confirmer sans ouvrir le fichier, par exemple sur le code qui l'écrit (dépôt de l'organisme), avant le premier passage.
2. Repli : une carte nommée est trouvée si son identifiant égale le nom de treize caractères ou commence par lui, une seule fois ; sous le repli le compte de 94 n'est pas exigé (la lettre du repli ne le cite pas ; l'empreinte l'est).
3. `meta` : retiré au premier niveau de chaque carte (« le champ `meta` de chaque carte ») ; une clé `meta` imbriquée dans un autre champ reste lue.
4. Bardeaux : mots normalisés (sans accents, minuscules, ponctuation en espace), huit mots consécutifs, par chaîne de texte (aucun bardeau à cheval sur deux champs) ; côté cartes : toutes les chaînes sauf `meta` ; côté v2 : toutes les chaînes de chaque témoin (contenu, construction, identifiants) ; un seul bardeau commun refuse le témoin ; le compte rendu est celui des bardeaux distincts communs, sans distinguer cartes et témoins v2.
5. **Troisième valeur de décision**, « garde non jouée », pour tout refus de tourner (la lettre ne connaît que « passée » et « refusée ») ; la cause n'est dite que par le nom de la classe d'exception.
6. **Mot de la mère** : au-delà de cinq rejeux, un mot par rejeu ; un même texte ne vaut qu'une fois (son empreinte est au journal, son texte au manifeste seulement).
7. Le contrôle (4) et la pièce du déclencheur du repli sont exigés par chemin et empreinte (lecture du code de « sans ce contrôle passé et écrit, la garde ne tourne pas »).
8. **Longueur** d'un témoin : sa forme JSON indentée (`json.dumps(…, indent=1)`), mesure de l'épreuve des témoins v9 ; les onze v2 y vont de 1 251 à 2 761 (la somme des champs, elle, descend à 1 044). Entrelacement par huit bandes à effectif égal dans chaque classe.
9. Catégories → champs (§ 2) ; un témoin = un fragment par catégorie ; **réemploi des fragments** entre témoins permis, tirage uniforme, usages au journal (la lettre ne dit pas combien de fois un fragment sert).
10. **Pièges** : un seul par bon à piège ; seulement chez les bons ; répartition : citants 8/8/8 et un de plus tiré, non citants « mot juge » et « reprise » 12/12 et un de plus tiré (le piège « citation » seulement chez les citants).
11. Citation d'un témoin citant : portée par un seul fragment (le fautif s'il cite, sinon une catégorie tirée parmi celles qui ont des conformes citants).
12. Partage des bons : citation, puis type ; les simples se partagent alors à un près (26 et 24 possible).
13. Audit : pénalité ½·1,0·‖w‖², ordonnée non pénalisée ; écart type nul remplacé par 1 ; phrases = fins de phrase « . ! ? … » (au moins une pour un texte non vide) ; noms de modules au singulier ou au pluriel ; « prédit » et ses accords ; classe positive = mauvais ; bandes fermées ; une aire qui décide sous 0,40 n'est pas un refus (la lettre ne refuse qu'au-dessus de 0,60).
14. Juges de surface : définitions de l'épreuve des témoins v9 (médianes de la banque ; champ lu pour trois items, les deux autres vrais) ; le juge « à la citation » prend la citation de construction du témoin reconnu par son contenu ; identifiant opaque servi neuf par appel (forme « F » + cinq chiffres hexadécimaux).
15. Service réel : `charger_service_des_juges` du code d'appel v4, chargé par son empreinte ; jamais exercé (dépôt de l'organisme absent de cette machine).
16. Étiquettes interdites lues dans la configuration des juges (empreinte vérifiée) et refusées dans les fragments.

## 7. Sortie des essais

`env -C …/generateur-v1 /home/user/controle-ia-travail/.venv/bin/python -B -m pytest -q -p no:cacheprovider essais_generer_temoins_ligne_3_v1.py` (Python 3.13.18, numpy 2.4.6) : **68 passed in 3.65s**.

Couverture (cas sain et artefact) : graines (racine des essais ; racines décisives refusées sans autorisation ou à empreinte fausse ; racines 31 à 33, 35, 36 refusées ; table étrangère) ; schéma des fragments (14 artefacts) ; proportions exactes et artefact ; longueurs entrelacées ; journal = vérité ; reproductibilité à l'octet ; fragments insuffisants nommés ; vérité non servie ; partage stratifié ; banque lisible par le v4 ; **garde** : cas sain (rien des cartes ne sort : rapport, manifeste, journal, sorties standard et d'erreur relus ; aucun bardeau de carte factice) ; témoin recopié d'une carte et d'un témoin v2 → refusés ; empreinte, compte ou forme faux → refus avant comparaison ; trois formes admises ; `meta` portant seul un paragraphe → aucun refus ; rapport hors liste → refus d'écrire (8 formes) ; journal à cinq rejeux sans mot → refus sans ouverture, avec mot → passe, même mot → refus ; cinquième rejeu permis ; journal absent ou illisible (4 formes) → refus sans ouverture ; exception provoquée pendant la lecture d'une carte factice et JSON coupé → classe et lieu seulement ; repli (sept cartes, mention, écart au manifeste, compte des rejeux qui continue), hors déclencheur, sans pièce, empreinte autre, cartes nommées introuvables ; seconde entrée fausse ; sans contrôle (4) ; sortie existante ; chemin du coffre ; voie d'essai refusant l'archive ; constantes de l'entrée unique (comparaison de chaînes seulement) ; création du journal ; **audit** : banque factice équilibrée passée (aire qui décide 0,539 ; à tous les traits 0,594 ; traits de la lettre 0,5, 0,5, 0,5 ; juges longueur 0,50, champ lu 0,525, citation 0,50, parfait 0), mauvais plus courts de 30 % refusés, traits de la lettre hors bande refusés, service qui altère la fiche et juge parfait en erreur → banc invalide, aire contre le décompte par paires, Newton (gradient nul), plis stratifiés ; gestes écrits scellés et manifestes ; ligne de commande sans autorisation → refus.

## 8. Ce que l'additif de code de l'étage 2 devra porter

- Fichiers et empreintes : `generer_temoins_ligne_3_v1.py` (`b264760c…`), ses essais (`79bd8d87…`), les fragments factices (`a66cf6d4…`), ce rapport et la contre-lecture ; le commit qui les verse.
- **Autorisation des racines 2026111934 (composition et partage) et 2026111937 (plis de l'audit)** : la pièce scellée elle-même, passée par `--autorisation-additif CHEMIN --empreinte-additif HEX`.
- Le fichier de fragments réel (modèle F) n'est pas nommé par l'additif de code : il est scellé avec la banque (R-4246) ; son empreinte est passée à `composer` et portée au manifeste et à la banque.
- Commandes (lancées depuis le dossier du code, `python3 -B`, dossiers de sortie neufs hors du dossier du code) :
  - `generer_temoins_ligne_3_v1.py composer --fragments F --empreinte-fragments HEX --sortie DOSSIER_NEUF --autorisation-additif CHEMIN --empreinte-additif HEX`
  - `generer_temoins_ligne_3_v1.py creer-journal-rejeux --journal CHEMIN_DU_JOURNAL --manifeste DOSSIER_NEUF` (une fois, avant le premier passage)
  - `generer_temoins_ligne_3_v1.py garde --banque B --journal-rejeux CHEMIN_DU_JOURNAL --sortie DOSSIER_NEUF --controle-4 PIECE --empreinte-controle-4 HEX [--mot-de-la-mere "TEXTE"] [--repli CAUSE --piece-repli P --empreinte-piece-repli HEX]` — seulement après le contrôle (4) écrit et « conforme »
  - `generer_temoins_ligne_3_v1.py auditer --banque B --empreinte-banque HEX --sortie DOSSIER_NEUF --autorisation-additif CHEMIN --empreinte-additif HEX [--orchestrateur RACINE]`
- Codes de sortie : 0 fait ou banque passée ; 2 refus avant tout ; 4 banque refusée ; 5 garde non jouée.

## 9. Écarts

1. Pour trouver le chemin de l'additif 3, que le mandat ne donnait pas : recherche bornée (R-4183, puis motifs de nom de fichier) dans `registres/decisions.md` tiré de main par `git show` redirigé vers mon dossier ; puis `git show` redirigé du verdict « portée à 200 » v2, qui nomme ce chemin. Aucune commande de liste.
2. Pièces lues hors de la liste du mandat (§ 0) : configuration des juges, épreuve des témoins v9 (juges factices), banc v3 (`verifier_autorisation`).
3. Le « rapport v1, § format » du code d'appel n'a pas été lu (chemin non donné) : le format vient de `valider_banque` du v4 lui-même, et l'essai le vérifie.
4. Aides de travail hors des cinq livrables, dans mon dossier : `construire_fragments_exemple_v1.py` (écrit le fichier factice), `longueurs_v2.py`, `apercu_audit_factice_v1.py` ; extraits de main ; dossier `tmp-essais/` des essais. Un premier brouillon du fichier factice (longueurs mal étagées : composition impossible dans la bande 0) a été supprimé et réécrit avant toute livraison.
5. Le fichier d'essais contient la chaîne du vrai chemin des cartes, comparée à la constante du code, sans aucun appel au système de fichiers.
6. Version de Python : relevée sur l'interpréteur du venv (`.venv/bin/python --version`), non sur `python3`.

Développeur, modèle O.
