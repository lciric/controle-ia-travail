"""Brouillon 3 de la consigne du lecteur B, écrit par couples « ancien → nouveau » appliqués au brouillon 2 — v2.

Nom en v2 (règle R12) : un fichier `couples_consigne_b_brouillon3_v1.py`, non scellé, qui n'est pas de ce rédacteur,
occupait déjà le nom v1 dans ce dossier (créé à 13:04:06Z) ; il n'est ni lu, ni exécuté, ni modifié par ce programme.

Raison unique (décision de la session mère R-2980) : la commande de la phase C passe en version 4 et remet au lecteur B un
quinzième fichier, `diag/<run de T0.7>/sondes-t07.json`, avec son compagnon. Les couples ne changent que : la liste fermée
des pièces et le bordereau (29 lignes) ; ce que le lecteur lit dans ce fichier, et à quelle passe (motif de T7-P6, défaut
DF-05 ; effectifs des « paires des jeux » ; sondes principales et règle d'ex aequo ; état des phrases des concepts) ; les
mentions « non remis » ou « non vérifiable » devenues fausses pour ce fichier ; les puces « Qui t'envoie cette consigne »
et « État du fichier », le titre, et les comptes et renvois qui en dépendent. Les ambiguïtés A1 à A7 et les choix de
rédaction du rapport du premier rédacteur (§ 5 et § 6) ne sont pas touchés.

Usage : python3 -I -B couples_consigne_b_brouillon3_v2.py
Gardes : empreinte du brouillon 2 égale à l'attendue ; chaque « ancien » présent exactement une fois dans le brouillon 2 ;
aucun recouvrement entre deux « anciens » ; cible absente (création exclusive : jamais d'écrasement). Tout écart : code 1,
rien n'est écrit. Le sceau (compagnon `.sha256`) est posé ensuite par `controle_ia.scellement sceller`.
"""
import hashlib
import pathlib
import sys

ICI = pathlib.Path(__file__).resolve().parent
SOURCE = ICI / "consigne-lecteur-b-v1-brouillon2.md"
EMPREINTE_SOURCE = "6bcfa40005d8e194249568c98be6f855a39ac46792339bb6049895c892ecf421"
CIBLE = ICI / "consigne-lecteur-b-v1-brouillon3.md"

COUPLES = [
    # 1. Titre
    ("titre",
     "# T0.7 — consigne du lecteur du verdict de l'étape B (sondes v0, critère 3 de G0, mode « coût ») — v1 — brouillon 2\n",
     "# T0.7 — consigne du lecteur du verdict de l'étape B (sondes v0, critère 3 de G0, mode « coût ») — v1 — brouillon 3\n"),

    # 2. Puce « État du fichier »
    ("etat-du-fichier",
     "- **État du fichier** : brouillon 2, écrit le 2026-11-16 par le même rédacteur ; **brouillon 2 = brouillon 1**\n"
     "  (`consigne-lecteur-b-v1-brouillon1.md`, `44f0fd1e6c95a0ef833b63cb6d99e6b91bbe76a1e1b9892858ae3069254586f5`, gardé tel\n"
     "  quel, règle R12) **plus neuf retouches** listées au rapport du rédacteur (`rapport-redacteur-consigne-b-v1.md`, § 4) ; **non\n"
     "  contre-lu, non scellé comme consigne** (son compagnon n'atteste que l'intégrité, règle R6). À contre-lire (règle R2)\n"
     "  par un sous-agent neuf d'un autre modèle que le rédacteur, puis à sceller par la session mère sous son nom définitif.\n"
     "  Cette puce est réécrite au scellement.\n",
     "- **État du fichier** : brouillon 3, écrit le 2026-11-16 par un second rédacteur, sous-agent neuf (modèle A) de la session\n"
     "  mère, qui n'a écrit ni le texte de T0.7 ni aucune autre pièce de ta liste, et n'a ouvert aucune donnée ni aucun résultat\n"
     "  de 7a, de 7b ou de T0.7 ; **brouillon 3 = brouillon 2**\n"
     "  (`consigne-lecteur-b-v1-brouillon2.md`, `6bcfa40005d8e194249568c98be6f855a39ac46792339bb6049895c892ecf421`, gardé tel\n"
     "  quel, règle R12 ; lui-même brouillon 1 plus neuf retouches, `rapport-redacteur-consigne-b-v1.md`, § 4) **plus les seuls\n"
     "  changements que demande la décision R-2980** : la commande de la phase C passe en version 4 et te remet un quinzième\n"
     "  fichier, `sondes-t07.json`, avec son compagnon (liste fermée et bordereau de 29 lignes ; ce que tu y lis, et à quelle\n"
     "  passe ; mentions « non remis » devenues fausses pour ce fichier) ; changements faits par le programme de couples\n"
     "  « ancien → nouveau » `couples_consigne_b_brouillon3_v2.py` (même dossier). **Non contre-lu, non scellé comme consigne**\n"
     "  (son compagnon n'atteste que l'intégrité, règle R6). À contre-lire (règle R2) par un sous-agent neuf qui n'en a écrit\n"
     "  aucun brouillon (son modèle est fixé par la session mère : brouillons 1 et 2 d'un rédacteur du modèle B, changements du\n"
     "  brouillon 3 d'un rédacteur du modèle A), puis à sceller par la session mère sous son nom définitif. Cette puce est\n"
     "  réécrite au scellement.\n"),

    # 3. Puce « Qui t'envoie cette consigne » : commande v4, jeton de mise au propre à la place de l'empreinte
    ("qui-t-envoie",
     "- **Qui t'envoie cette consigne** : la session hôte du compte 3, par le bloc C6 de\n"
     "  `docs/procedures/lecture-7b-etape-b-compte-3-v1/commande-compte-3-phase-c-v3.md`\n"
     "  (`9d7889198238c171447a06f56f1a37beb4190572c3a9ceceb18144541c258d2e`) ; tu ne lis pas cette commande (elle n'est pas dans\n"
     "  tes pièces).\n",
     "- **Qui t'envoie cette consigne** : la session hôte du compte 3, par le bloc C6 de\n"
     "  `docs/procedures/lecture-7b-etape-b-compte-3-v1/commande-compte-3-phase-c-v4.md`\n"
     "  (`EMPREINTE-COMMANDE-V4-A-REMPLIR`) ; tu ne lis pas cette commande (elle n'est pas dans tes pièces).\n"),

    # 4. Section 3.1, plages à lire : la section « Sorties » dit aussi ce que porte la pièce 15
    ("plages-sorties",
     "| l. 2466-2507 | « Module », « Sorties » | ce que `lecture-t07.json` porte |\n",
     "| l. 2466-2507 | « Module », « Sorties » | ce que `lecture-t07.json` porte, et `sondes-t07.json` (l. 2471-2473) |\n"),

    # 5. Section 3.1, plages à consulter : la ligne du contrôle des paires des jeux (point 15 de l'accord au code)
    ("plages-consulter",
     "points 1, 2, 3, 8, 9, 11 et 12) et l. 2668 (point 20, réserve\n"
     "CLC-07) ; l. 2679-2760 (« Concordance avec le texte scellé de T0.6 »).",
     "points 1, 2, 3, 8, 9, 11 et 12), l. 2663 (point 15 : paires\n"
     "des jeux, rejeu du contrôle 9) et l. 2668 (point 20, réserve CLC-07) ; l. 2679-2760 (« Concordance avec le texte\n"
     "scellé de T0.6 »)."),

    # 6. Section 2 : bordereau de 29 lignes
    ("bordereau-29",
     "une ligne par pièce, chemin `./…` relatif à `<ESPACE>/pieces/`, **27 lignes** attendues : treize fichiers, leurs treize\n"
     "compagnons, et l'extrait des registres (sans compagnon).",
     "une ligne par pièce, chemin `./…` relatif à `<ESPACE>/pieces/`, **29 lignes** attendues : quatorze fichiers, leurs\n"
     "quatorze compagnons, et l'extrait des registres (sans compagnon)."),

    # 7. Section 2 : quinzième pièce de la liste fermée
    ("piece-15",
     "| 14 | `diag/20261114-001352-t07-lecture-reel/lecture-t07.json` | **la sortie scellée de l'étape B**, écrite par le module seul, sur un code de sortie 0 (R123) | tout, en trois passes (sections 6.5 à 6.7) |\n",
     "| 14 | `diag/20261114-001352-t07-lecture-reel/lecture-t07.json` | **la sortie scellée de l'étape B**, écrite par le module seul, sur un code de sortie 0 (R123) | tout, en trois passes (sections 6.5 à 6.7) |\n"
     "| 15 | `diag/20261114-001352-t07-lecture-reel/sondes-t07.json` | fichier scellé de l'étape A, écrit par le module (ligne `SONDES-T07`) : sondes principales lues, sondes neuves et T7-P6, contrôles des paires des jeux | les clés nommées aux sections 6.4 (point 3), 6.6 (point 1) et 6.7 (points 3, 6, 7 et 8), par programme ; rien à la première passe |\n"),

    # 8. Section 2 : quatorze compagnons
    ("compagnons-14",
     "Chaque pièce des lignes 1 et 3 à 14 a son compagnon `<pièce>.sha256` (treize compagnons).",
     "Chaque pièce des lignes 1 et 3 à 15 a son compagnon `<pièce>.sha256` (quatorze compagnons)."),

    # 9. Section 2 : `sondes-t07.json` n'est plus « jamais remis »
    ("jamais-remis",
     "- **Jamais remis, et tu ne les demandes pas** : le fichier des scores, les sorties de l'étape A (`sondes-t07.json`,\n"
     "  `notation-t07.json`, `ouverture-t07.json`, le rapport de la réextraction), les mesures, les textes et les autres\n",
     "- **Jamais remis, et tu ne les demandes pas** : le fichier des scores, les autres sorties de l'étape A\n"
     "  (`notation-t07.json`, `ouverture-t07.json`, le rapport de la réextraction), les mesures, les textes et les autres\n"),

    # 10. Section 4, entrée G : la raison donnée devient fausse telle quelle (une sortie de l'étape A est remise)
    ("entree-G",
     "| G | l. 1813 ; lignes R11-arret et R12-invalide (R185, R186) | `lecture-t07.json` seulement (`resultat.entrees.G`) : les sorties de l'étape A ne te sont pas remises |\n",
     "| G | l. 1813 ; lignes R11-arret et R12-invalide (R185, R186) | `lecture-t07.json` seulement (`resultat.entrees.G`) : les sorties de l'étape A qui portent la garde d'identité (`ouverture-t07.json`, `notation-t07.json`) ne te sont pas remises, et la pièce 15 ne la porte pas |\n"),

    # 11. Section 5 : deux fichiers du code de plus, d'où sont tirées les clés de la pièce 15
    ("code-cite",
     "`e50236574fbcd7e48ea3005eadc8bdb68d2c753d10028db7f2c365648a843cec` ; `src/controle_ia/manifeste.py`\n",
     "`e50236574fbcd7e48ea3005eadc8bdb68d2c753d10028db7f2c365648a843cec`, `sondes_neuves_v1.py`\n"
     "`d4d354e769de279235a202b1ac803b6b508bb12a374f48d0352db13daaab9bc7`, `controle_jeux_v1.py`\n"
     "`27cf1fba9584f41632af4b352b048ecf46e8cc53695499385dd8c8eddc92a3ae` ; `src/controle_ia/manifeste.py`\n"),

    # 12. Section 5 : où sont les clés de la pièce 15
    ("cles-piece-15",
     "  - `graines_derivees`, `durees_s`, `couverture`.\n"
     "- **Pièce 11, manifeste** :",
     "  - `graines_derivees`, `durees_s`, `couverture`.\n"
     "- **Pièce 15, `sondes-t07.json`** (écrit à l'étape A ; T07 l. 2471-2473) : objet\n"
     "  `{\"run_id\", \"manifeste_sha256\", \"resultat\"}`, rattaché au même manifeste que la pièce 14. Sous `resultat` :\n"
     "  - sondes lues : `sondes_lues` (noms complets des sondes principales lues, dans l'ordre de `concepts`),\n"
     "    `sondes_lues_manifeste` (la liste telle que le manifeste l'écrit : `null` pour une sonde neuve), `concepts`,\n"
     "    `niveau_applique`, `jeux_scelles` (`J-D`, `J-C`, `J-A` : vrai ou faux), `jeux_hors_perimetre`, `non_lues`,\n"
     "    `principales` (par sonde : `nom`, `couche`, `agregation`, `famille`, `empreinte`, `concept`),\n"
     "    `principales_consignees` (nom de sonde → empreinte) ; puis `fichiers`, `couples_figes`, `cles_ignorees`,\n"
     "    `garde_adaptee` ;\n"
     "  - à l'étape complète (en mode réel, les sondes neuves sont apprises à l'étape A), en plus : `sondes_neuves`,\n"
     "    `disjonction`, `controles_jeux`, `phrases_concepts`, `fichiers_sondes_neuves`, `note` ;\n"
     "  - `sondes_neuves` : `decoupage` ; `concepts` (`dissimulation`, `domaine` ; chacun : `couples` par nom de sonde,\n"
     "    `principale`, `aire_validation`, `meilleure_aire`, `ex_aequo`, `saturation`, `regle` (la règle d'ex aequo appliquée,\n"
     "    écrite), `empreinte_principale`, `n_entrainement` et `n_validation` (exemples, non paires), `lue` ; ou `etat` seul,\n"
     "    « jeu non scellé : aucune sonde apprise ») ; `p6` (sonde de T7-P6 apprise : `sonde`, `temoin`, `famille`, `couche`,\n"
     "    `paires_entrainement`, `modes_temoin`, `aires_validation_ja` ; sinon `etat` seul : « échec : <motif> » si\n"
     "    l'apprentissage a échoué, « non lue : jeu J-A non scellé » ou « non lue : jeu J-C non scellé (famille et couche du\n"
     "    domaine) ») ; puis `directions`, `temoins_lexicaux`, `temoins_lexicaux_p3`, `reglages`, `frontieres_ajustees`,\n"
     "    `graines_derivees_apres_manifeste` ;\n"
     "  - `controles_jeux` : `remesure_jetons` (par jeu présent : `JD`, `JC`, `JA`) et `controle_9` (`regle`, `textes_course`,\n"
     "    `enonces`, `jeux` ; sous `jeux`, par jeu présent, `JD`, `JC` ou `JA` : `jeu`, `paires_scellees`, `paires_en_defaut`\n"
     "    (liste de `{\"tache\", \"paire\", \"motifs\"}`), `taches_sorties` (par tâche sortie du jeu :\n"
     "    `{\"tache\", \"paires_restantes\", \"paires_scellees\"}`, plus `mode` pour J-A), `paires_gardees`, `insertion_non_isolee`,\n"
     "    et `etat` si le rejeu vide le jeu) ;\n"
     "  - `phrases_concepts` : `etat` (« lues » ou « non lues »), puis `chemin` et `date`, ou `motif` et `ligne`.\n"
     "- **Pièce 11, manifeste** :"),

    # 13. Section 6.1 : 29 lignes
    ("controle-29",
     "Empreinte du bordereau égale à celle du message et à son compagnon ; 27 lignes ; l'ensemble des fichiers sous",
     "Empreinte du bordereau égale à celle du message et à son compagnon ; 29 lignes ; l'ensemble des fichiers sous"),

    # 14. Section 6.3, point 3 : la ligne SONDES-T07 et la pièce 15
    ("ligne-sondes",
     "pièce 12 ; `SCELLEMENT-T08-BASE-A` et la pièce 8. Écart : arrêt `piece-non-conforme`.",
     "pièce 12 ; `SCELLEMENT-T08-BASE-A` et la pièce 8 ; `SONDES-T07` et la pièce 15. Écart : arrêt `piece-non-conforme`."),

    # 15. Section 6.4, point 3 : rattachement de la pièce 15
    ("rattachement-15",
     "`SCORES-T07` ; `resultat.ouverture.manifeste.go_id` égal à `go_id_attendu` de la configuration (R174, R108). Écart :\n"
     "   arrêt `piece-non-conforme`.\n",
     "`SCORES-T07` ; `resultat.ouverture.manifeste.go_id` égal à `go_id_attendu` de la configuration (R174, R108). Écart :\n"
     "   arrêt `piece-non-conforme`. **Rattachement** de la pièce 15 (le script n'y lit que `run_id` et `manifeste_sha256`) :\n"
     "   `run_id` égal au run de T0.7 ; `manifeste_sha256` égal à l'empreinte de la pièce 11. Écart : arrêt `piece-non-conforme`.\n"),

    # 16. Section 6.5 : la pièce 15 n'est pas ouverte à la première passe
    ("passe-1",
     "`conditions_retirees`, `scores`, `garde_adaptee`, `cles_ignorees` et `ouverture`. Il écrit tes dérivations **avant** les\n"
     "valeurs du module, puis la comparaison.",
     "`conditions_retirees`, `scores`, `garde_adaptee`, `cles_ignorees` et `ouverture` ; il n'ouvre pas la pièce 15. Il écrit\n"
     "tes dérivations **avant** les valeurs du module, puis la comparaison."),

    # 17. Section 6.6, point 1 : sondes principales consignées à l'étape A (accord au code, point 3)
    ("passe-2-sondes",
     "   celui de la règle : arrêt `ecart-au-texte`. Désaccord entre la liste des sondes et les lignes de l'extrait : écrit,\n"
     "   question.\n",
     "   celui de la règle : arrêt `ecart-au-texte`. Désaccord entre la liste des sondes et les lignes de l'extrait : écrit,\n"
     "   question. **Pièce 15** (sondes principales consignées à l'étape A ; R170, l. 2611-2620) : `resultat.sondes_lues` et\n"
     "   `resultat.niveau_applique` égaux à ceux de la pièce 14 ; `resultat.concepts` égal à `config.concepts_lus` du manifeste ;\n"
     "   `resultat.sondes_lues` de même longueur que `config.sondes_lues` du manifeste, chaque nom égal au nom de même rang ou,\n"
     "   là où le manifeste écrit `null` (sonde neuve), commençant par le concept de même rang de `resultat.concepts` suivi d'un\n"
     "   tiret (l. 2618-2619) ; chaque nom de `resultat.sondes_lues` clé de `resultat.principales_consignees` (l. 2616-2617).\n"
     "   Écart : arrêt `piece-non-conforme` (choix de cette consigne : le texte fait refuser ces écarts par le module,\n"
     "   l. 2616-2619 ; des pièces qui les portent ne sont pas celles qu'il a lues).\n"),

    # 18. Section 6.6, point 6 : rien de la pièce 15 n'entre dans un état
    ("ne-compte-jamais",
     "   descriptifs (`jeux_hors_jugement`, `couples_figes_descriptif`, `planchers_p3_descriptif`) n'entrent dans aucun état.",
     "   descriptifs (`jeux_hors_jugement`, `couples_figes_descriptif`, `planchers_p3_descriptif`) n'entrent dans aucun état ;\n"
     "   rien de la pièce 15 non plus (aires de validation, couples, T7-P6)."),

    # 19. Section 6.7, point 3 : motif de T7-P6 (défaut DF-05, l. 2659)
    ("t7-p6",
     "   registre et tu l'écris ; si les deux sont présentes, le texte déclare que ce motif peut être faux et que le vrai\n"
     "   est dans `sondes-t07.json` (R122), qui ne t'est pas remis : tu l'écris en question, sans trancher — ; T7-P17 (chaque\n",
     "   registre et tu l'écris ; si les deux sont présentes, le texte déclare que ce motif peut être faux et que le vrai\n"
     "   est dans `sondes-t07.json` (R122) : tu lis `resultat.sondes_neuves.p6.etat` dans la pièce 15 et tu recopies ce motif\n"
     "   en regard de celui de la pièce 14, chacun avec sa clé ; si le motif de la pièce 15 commence par « échec » (T7-P6 en\n"
     "   échec dès l'apprentissage), tu écris que, dans ce cas, le texte tient le motif de l'étape B pour faux et celui de\n"
     "   `sondes-t07.json` pour le vrai (DF-05, l. 2659), sans rien trancher de plus ; `p6` sans `etat` (sonde apprise) ou\n"
     "   `sondes_neuves` absent : écrit, en question — ; T7-P17 (chaque\n"),

    # 20. Section 6.7, point 6 : sondes principales et règle d'ex aequo (plan, point 4 ; « Sorties »)
    ("point-10",
     "6. **Point 10** (R050) : pour les deux sondes figées, la lecture descriptive contre leurs 200 directions de P3\n"
     "   (`planchers_p3_descriptif` ; R129) ;",
     "6. **Point 10** (R050) : pour chaque sonde lue, son concept et sa couche (`resultat.principales` de la pièce 15) et,\n"
     "   pour la dissimulation et le domaine, la sonde principale choisie et la règle d'ex aequo appliquée, recopiées telles\n"
     "   qu'écrites (`resultat.sondes_neuves.concepts.<concept>` : `principale`, `aire_validation`, `meilleure_aire`,\n"
     "   `ex_aequo`, `saturation`, `regle` ; plan, point 4, l. 1373-1378 ; lecture de cette consigne : le texte écrit dans la\n"
     "   pièce 15 la sonde choisie et la règle appliquée, l. 2471-2473, et veut la saturation « rapportée comme un constat »,\n"
     "   l. 1378, sans dire par qui ; tu les recopies) ; pour les deux sondes figées, la lecture descriptive contre leurs 200\n"
     "   directions de P3 (`planchers_p3_descriptif` ; R129) ;"),

    # 21. Section 6.7, point 7 : effectifs des paires des jeux (l. 1539 ; l. 2663)
    ("paires-des-jeux",
     "   « paires des jeux » : relevées si une de tes pièces les porte ; sinon tu écris « paires des jeux : non relevées (les\n"
     "   sorties de l'étape A ne me sont pas remises) », en question.\n",
     "   « paires des jeux » (lecture de cette consigne : les paires des jeux génériques J-D, J-C et J-A ; l. 2663) : dans la\n"
     "   pièce 15, pour chaque jeu de `resultat.controles_jeux.controle_9.jeux` (`JD`, `JC`, `JA`), `paires_scellees`,\n"
     "   `paires_gardees` et le nombre d'éléments de `paires_en_defaut` et de `taches_sorties` ; et\n"
     "   `resultat.sondes_neuves.p6.paires_entrainement` (paires d'entraînement de la sonde de T7-P6), si la clé est écrite ; un\n"
     "   jeu absent de `controle_9.jeux` est écrit absent ; une clé absente : « non relevé (clé absente) », en question.\n"),

    # 22. Section 6.7, point 8 : réserve R15, état des phrases écrit à l'étape A (l. 1936)
    ("r15-phrases",
     "   présente : sa date est écrite, l'instant de fermeture ne se vérifie pas depuis tes pièces) — le texte déclare un cas\n",
     "   présente : sa date est écrite, l'instant de fermeture ne se vérifie pas depuis tes pièces), avec, recopié à côté, l'état\n"
     "   des phrases écrit à l'étape A (`resultat.phrases_concepts` de la pièce 15 ; le texte le place là et au manifeste quand\n"
     "   les scores ne sont pas ouverts : l. 1936) — le texte déclare un cas\n"),

    # 23. Section 8 : le contrôle des noms de la section 6.6, point 1
    ("calcul-prefixe",
     "d'éléments d'une liste ; la recherche d'une chaîne dans une pièce.\n",
     "d'éléments d'une liste ; la recherche d'une chaîne dans une pièce ; le début d'un nom comparé à une chaîne (section 6.6,\n"
     "point 1).\n"),

    # 24. Section 12, point 9 : descriptif
    ("verdict-descriptif",
     "9. **Descriptif** : T7-P6, T7-P17, T7-P16, T7-P10, T7-P9 ; sondes figées contre leurs 200 directions de P3 ; tableaux\n"
     "   descriptifs par renvoi.\n",
     "9. **Descriptif** : T7-P6, T7-P17, T7-P16, T7-P10, T7-P9 ; sondes principales et règle d'ex aequo (pièce 15) ; sondes\n"
     "   figées contre leurs 200 directions de P3 ; tableaux descriptifs par renvoi.\n"),

    # 25. Section 12, point 14 : le motif vrai de T7-P6 et les paires des jeux se lisent désormais dans la pièce 15
    ("non-verifiable",
     "    verdict en prose de P3-bis, G3 s'il y a lieu, le motif vrai de T7-P6, les paires des jeux) ; tes lectures marquées\n",
     "    verdict en prose de P3-bis, G3 s'il y a lieu) ; tes lectures marquées\n"),
]


def main() -> int:
    if CIBLE.exists():
        print(f"ARRÊT : {CIBLE.name} existe déjà : rien n'est écrit (règle R12)")
        return 1
    octets = SOURCE.read_bytes()
    h = hashlib.sha256(octets).hexdigest()
    if h != EMPREINTE_SOURCE:
        print(f"ARRÊT : empreinte de {SOURCE.name} = {h}, attendue {EMPREINTE_SOURCE} : rien n'est écrit")
        return 1
    texte = octets.decode("utf-8")
    places = []
    fautes = 0
    for nom, ancien, nouveau in COUPLES:
        n = texte.count(ancien)
        if n != 1:
            print(f"FAUTE : couple {nom} : « ancien » présent {n} fois (une attendue)")
            fautes += 1
            continue
        if ancien == nouveau:
            print(f"FAUTE : couple {nom} : « nouveau » égal à « ancien »")
            fautes += 1
            continue
        debut = texte.index(ancien)
        places.append((debut, debut + len(ancien), nom, nouveau))
    places.sort()
    for (a1, b1, n1, _), (a2, b2, n2, _) in zip(places, places[1:]):
        if a2 < b1:
            print(f"FAUTE : couples {n1} et {n2} : « anciens » qui se recouvrent")
            fautes += 1
    if fautes:
        print(f"ARRÊT : {fautes} faute(s) : rien n'est écrit")
        return 1
    morceaux, curseur = [], 0
    for debut, fin, _, nouveau in places:
        morceaux.append(texte[curseur:debut])
        morceaux.append(nouveau)
        curseur = fin
    morceaux.append(texte[curseur:])
    sortie = "".join(morceaux)
    with open(CIBLE, "x", encoding="utf-8", newline="\n") as f:          # création exclusive : jamais d'écrasement
        f.write(sortie)
    hc = hashlib.sha256(CIBLE.read_bytes()).hexdigest()
    print(f"source : {SOURCE.name} ({h}) ; {len(COUPLES)} couples appliqués, chacun à un seul endroit, sans recouvrement")
    for debut, fin, nom, nouveau in places:
        ligne = texte.count("\n", 0, debut) + 1
        print(f"  {nom} : ligne {ligne} du brouillon 2 ; {texte.count(chr(10), debut, fin)} → {nouveau.count(chr(10))} sauts de ligne")
    print(f"cible écrite : {CIBLE.name} ; {sortie.count(chr(10))} lignes ; {len(sortie.encode('utf-8'))} octets ; sha256 {hc}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
