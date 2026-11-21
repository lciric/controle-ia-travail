#!/usr/bin/env python3
"""Fabrique `ordre-etalonnage-ii-b-v5-brouillon2.md` depuis le brouillon 1, en remplissant ce qui est connu.

Usage : python3 -I fabriquer-ordre-etalonnage-ii-b-v5-brouillon2-v1.py RACINE_DU_DEPOT DOSSIER DATE

Méthode : le brouillon 1 est lu dans DOSSIER, son empreinte vérifiée ; les empreintes des pièces citées sont vérifiées dans le
dépôt ; chaque changement est un remplacement dont l'ancre est trouvée le nombre de fois attendu, sinon rien n'est écrit ; les
champs remplis le sont partout ; la table des champs est reconstruite et comparée aux champs restés dans le texte. Le programme
écrit le brouillon 2, la note des différences (une par ligne) et leurs compagnons. Il n'écrase rien (R12). Aucun réseau.
"""
import hashlib
import re
import sys
from pathlib import Path

B1 = "ordre-etalonnage-ii-b-v5-brouillon1.md"
B1_SHA = "db7f4dc042b43776dba1cc2553ac60fd8cc3f8860138adf4b48192b965c04549"
B2 = "ordre-etalonnage-ii-b-v5-brouillon2.md"
NOTE = "differences-ordre-etalonnage-v5-brouillon1-vers-2-v1.md"
V5 = "brouillons/ii-b-saboteur-budget-v5/"
C = V5 + "code-v5/"
TETE = "45f9ba7aaca27fdab8a458072f883825991dd2fb"
ARBRE = "9917b13f3c57d0eeacf3b72fea9607a103da4f11"
ENTROPIE = "34177889608133376136283958643409181656"

# Correctifs, dans l'ordre d'application sur 836c7ccc : (rang, chemin, empreinte lue sur le compagnon et recalculée).
CORRECTIFS = [
    (7, C + "correctifs-v2/0007-Organisme-retenu-du-saboteur-budget-code-en-version-.patch", "3075a8df0becf391df583b0ffc300419a387ac49818a48c11d71dd5cd9dad20b"),
    (8, C + "correctifs-v3/0008-Organisme-retenu-du-saboteur-budget-code-en-version-.patch", "ad33fe2697fcdcb95242fe8464fcd154f14aea0140aac898796fb7ee5be88281"),
    (9, C + "distillateur-v5/correctifs/0001-Organisme-retenu-du-saboteur-budget-distillateur-en-.patch", "8cfb77005517c83229887fe78230c1b681f7c0793afc8d986ddaf8558c2debe3"),
    (10, C + "distillateur-v5/correctifs/0002-Organisme-retenu-du-saboteur-budget-distillateur-en-.patch", "a515c1d8372611595c3f7a9a77cc44ebb7083fc5e2698b58890fef4a8b562197"),
    (11, C + "distillateur-v5/correctifs/0003-Organisme-retenu-du-saboteur-budget-distillateur-en-.patch", "324b51fad40b3da3c129e254377a1c8a6fda6866f91ee000cd92a3e1a526a6bc"),
    (12, C + "correctifs-v4/0009-Organisme-retenu-du-saboteur-budget-code-en-version-.patch", "4287a6889061c921886582ff3a7ebffecd4bd67fcbb4556b102e9eb9e2737661"),
]
PIECES = {
    V5 + "conception-organisme-retenu-ii-b-v5-scellee-v1-erratum-2.md": "ab020d438cb6eaa46cd2df0a6ed76952b5dfb23497438e0f2b3fb4590b1d26e2",
    V5 + "devis-v5/devis-ii-b-v5-scelle-v1-erratum-1.md": "90342292f52daf2f7281acad68006598450033367d3a36aa1c6c72eac9150f9a",
    C + "rapport-developpeur-code-organisme-retenu-v5-v2.md": "5b71aa0ec23374ae4ce3e96a65fc9a49fb0de2d0767591942cc16f209c5f5d85",
    C + "rapport-developpeur-code-organisme-retenu-v5-v3-note.md": "1af79d4c935cb80cdd91c421be71836a80c4d52d1afd1e5f6eb6be5fdec62594",
    C + "rapport-developpeur-code-organisme-retenu-v5-v4-note.md": "bb6d6d4e283e6b91a8cddf97b342faa75673cf8f878152af1564c296be2493d1",
    C + "contre-lecture-cl1/verification-corrections-code-organisme-retenu-v5-cl1.md": "6a9e2e7927b03533552b676b694736e6eb3ace72d58ca52007cb1c6b9cadfa57",
    C + "sortie-repetition-locale-v2.txt": "2e6e88c97000e4b92c85764688517583261c3d1dcc60e0c39f54f3a8304fbc4f",
    C + "sortie-essais-cibles-v5-v3.txt": "358b8371332d8bc556f457849c0ad195877f89801da9681ee7508bd1a4183be3",
    C + "sortie-essais-cibles-v5-v4.txt": "044e1be395693c000bdb6152c925c0545b3e99ce4e5b84977d072e6b935f2d90",
}
PIECES.update({chemin: e for _, chemin, e in CORRECTIFS})

# Changements : (nom, ancre trouvée `compte` fois dans le texte courant, texte neuf, compte). Appliqués dans l'ordre.
CHANGEMENTS = [
    ("titre", "machine à part — brouillon 1\n", "machine à part — brouillon 2\n", 1),
    ("statut", "- **Statut** : brouillon 1, pièce décisive (ordre d'une course payante), non contre-lu. Fabriqué par programme",
     "- **Statut** : **brouillon 2**, pièce décisive (ordre d'une course payante), non contre-lu. Fabriqué par programme (`fabriquer-ordre-etalonnage-ii-b-v5-brouillon2-v1.py`) depuis le brouillon 1 (`" + B1 + "`, `" + B1_SHA + "`, intact, R12), le @@DATE@@, par le même rédacteur, sous le même mandat, sur le message de la session de reconception : il remplit ce qui est connu depuis le brouillon 1 (code à sa tête, errata, entropie, ligne d'accord du 21 novembre au soir) et écrit le risque de la coupe ; rien d'autre ne change ; différences, une par ligne : `" + NOTE + "`. Le brouillon 1 avait été fabriqué par programme", 1),
    ("ligne d'accord, mot de Lazar pour la création",
     "Le mandat cite aussi `GO-2026-11-21-74` (« l'étalonnage dès ce soir si les épreuves le permettent ») : ligne non trouvée par le rédacteur au registre de `main` à cette tête (champ `<<LIGNE_MOT_LAZAR_CREATION>>`).",
     "Ligne `GO-2026-11-21-74`, lue au brouillon 2 au registre de `main` (tête `f390cf712aba0896c48132735244a07b064360af`) : mots de Lazar vers 18:30Z, « 22 au soir : création, puis étalonnage. pourquoi pas dès ce soir ? ».", 1),
    ("pièces citées, ajouts", "« autorisable », deux restes portés ici (§ 3).",
     "« autorisable », deux restes portés ici (§ 3). **Au brouillon 2** (empreintes recalculées par le programme) : erratum 2 du texte scellé (`ab020d438cb6eaa46cd2df0a6ed76952b5dfb23497438e0f2b3fb4590b1d26e2` : épisodes distillés jusqu'à 127, 3 830 actions d'oracle hors tours ; aucune règle, aucun seuil ne change) ; erratum 1 du devis scellé (`90342292f52daf2f7281acad68006598450033367d3a36aa1c6c72eac9150f9a` : plafond, coupures, fichier d'entrées, plafond de tours et dates inchangés ; le fichier d'entrées porte 3 830) ; rapport du développeur v2 (`5b71aa0ec23374ae4ce3e96a65fc9a49fb0de2d0767591942cc16f209c5f5d85`), notes v3 (`1af79d4c935cb80cdd91c421be71836a80c4d52d1afd1e5f6eb6be5fdec62594`) et v4 (`bb6d6d4e283e6b91a8cddf97b342faa75673cf8f878152af1564c296be2493d1`) ; vérification des corrections par le même contre-lecteur (`6a9e2e7927b03533552b676b694736e6eb3ace72d58ca52007cb1c6b9cadfa57`) : « autorisable après deux restes », R1 (coupe après une clé en gras) et R2 (amorce jamais jouée), traités par le correctif 0008 ; répétition locale à blanc (`" + C + "sortie-repetition-locale-v2.txt`, `2e6e88c97000e4b92c85764688517583261c3d1dcc60e0c39f54f3a8304fbc4f`) ; sorties d'essais v3 (`358b8371332d8bc556f457849c0ad195877f89801da9681ee7508bd1a4183be3`) et v4 (`044e1be395693c000bdb6152c925c0545b3e99ce4e5b84977d072e6b935f2d90`). La contre-lecture du distillateur n'a pas été ouverte : le distillateur ne sert pas à l'étalonnage.", 1),
    ("code lu, ajout",
     "**Des correctifs neufs arrivent** (point d'entrée en version 5, amorce en version neuve, et les corrections de la contre-lecture) : tout ce qui en dépend est un champ à remplir, marqué par des chevrons doubles (§ 11).",
     "**Au brouillon 2** : les douze correctifs du § 11 appliqués dans l'ordre dans le dossier du rédacteur, pour la lecture des scripts et des modules en version 5 seulement ; lus : les différences de `scripts/lancer_iib_v3.sh` avec la version 2, l'en-tête et les lignes des essais et du run de `scripts/amorce_instance_iib_v5.sh`, le gabarit de configuration en version 4, le point d'entrée et les noms des sorties de `lanceur_v5.py` ; les empreintes de l'amorce, du lanceur de session, de la liste figée, du gabarit et du module de lecture sont égales à celles de la tête locale du développeur, `" + TETE + "`, dont l'objet est dans le dépôt local (arbre `" + ARBRE + "`) ; aucun essai rejoué, aucun modèle chargé.", 1),
    ("§ 1, ligne du code",
     "| Code | commit du code revu `<<COMMIT_CODE_REVU_V5>>` sur `<<BRANCHE_CODE_V5>>` : base `836c7cccda5071fe54ecb148d214d74b5cb90474`, correctifs 0001 à 0006 (§ 11), correctifs neufs `<<EMPREINTES_CORRECTIFS_NEUFS>>` ; vérification des corrections par le même contre-lecteur : `<<VERIFICATION_CORRECTIONS_CODE_V5>>` ; **commit de lancement** `<<COMMIT_LANCEMENT_ETALONNAGE>>` |",
     "| Code | base `836c7cccda5071fe54ecb148d214d74b5cb90474` (`origin/prep/iib-code-v4`), plus les douze correctifs du § 11, appliqués dans l'ordre ; tête locale du développeur `" + TETE + "`, arbre `" + ARBRE + "`. La session de reconception ne peut pousser que sa branche : la mère ou l'exécutante appliquent les correctifs sur une branche `prep/` neuve et la poussent : `<<BRANCHE_CODE_V5>>`, commit du code revu `<<COMMIT_CODE_REVU_POUSSE>>`. **Ce qui fait foi est l'arbre** : `git rev-parse <commit>^{tree}` doit rendre `" + ARBRE + "` ; l'empreinte du commit peut différer de la tête locale, parce qu'elle porte le nom et l'heure de qui applique. Vérification des corrections : `6a9e2e7927b03533552b676b694736e6eb3ace72d58ca52007cb1c6b9cadfa57` (correctif 0007) ; vérification courte des correctifs 0008 et 0009, en cours : `<<VERIFICATION_COURTE_CORRECTIFS_0008_0009>>`. **Commit de lancement** `<<COMMIT_LANCEMENT_ETALONNAGE>>` |", 1),
    ("§ 1, ligne de l'amorce", "| Amorce | `<<AMORCE_V5_CHEMIN_ET_EMPREINTE>>` ; l'amorce",
     "| Amorce | `scripts/amorce_instance_iib_v5.sh` (`42196f90da0f104fb36a5f618a14e44ef03863d0541bb3b77f1f29f130a9e43c` à la tête du code) : elle joue la liste figée, puis `python -m controle_ia.iib.lanceur_v5 --phase etalonnage` ; jouée en essai local par la répétition, jamais sur une machine louée ; l'amorce", 1),
    ("§ 1, ligne des essais",
     "| Essais | suite ciblée en version 5, `scripts/tests-cibles-iib-v5.txt` (`<<LISTE_ESSAIS_V5_EMPREINTE>>` ; vingt fichiers dans le correctif 0005, `79dd4fbba8be1261ee8baa332ec17da6c06ac09a3cbcaf67d4dc078c76a297ea`) ; dernière ligne attendue : « `<<TESTS_ATTENDUS_V5>>` passed », durée exclue ;",
     "| Essais | liste figée `scripts/tests-cibles-iib-v5-v4.txt` (`342ee21d495b54cb5fd4a8ae6d7427043edb3c228cc16afd57ab4f9e3d099b68`, écrite en dur dans l'amorce ; 23 fichiers, sans l'essai du tokeniseur réel ni celui du moteur à torch du distillateur, qui se sautent sans leurs dépendances) ; **267 essais attendus** : « 267 passed in 415.80s (0:06:55) » à la tête du code, sur processeur (`sortie-essais-cibles-v5-v4.txt`) ; dernière ligne attendue : « `<<TESTS_ATTENDUS_V5>>` passed », durée exclue ; une ligne « N passed, 1 skipped » est refusée par l'amorce ;", 1),
    ("§ 1, calendrier", "**aucune création après 2026-11-27T00:00Z** (ligne d'accord, choix (d) ;",
     "**aucune création à partir de 2026-11-27T00:00:00Z, instant exclu : dernier jour de création le 2026-11-26** (`calendrier.dernier_jour_creation` du gabarit, vérifié à l'égalité en mode réel ; lecture du développeur, notes v3 et v4) (ligne d'accord, choix (d) ;", 1),
    ("§ 1, configuration", "| Configuration | `<<CONFIG_ETALONNAGE_CHEMIN_ET_EMPREINTE>>` au commit de lancement |",
     "| Configuration | `<<CONFIG_ETALONNAGE_CHEMIN_ET_EMPREINTE>>` au commit de lancement ; tirée du gabarit `docs/notes/barreau8-iib-v1/config-iib-organisme-retenu-v5-gabarit-v4.json` (`eb329185948ef80d37e724f73d8c210a02d72312befbf6c0fd5e489b255fc9e1`, dans le correctif 0009) ; la même configuration servira à la course, qui n'y écrit que l'oracle de la règle (note v3 du développeur) |", 1),
    ("§ 1, entropie", "tirée une fois par la mère avant la configuration, sans aucune donnée ; consignée au registre des décisions et dans la configuration",
     "tirée une fois par la mère le 2026-11-21 à 18:26:49Z, avant la configuration, sans aucune donnée ; consignée au registre des décisions (ligne `R-4659`, lue sur `main`) et dans le gabarit", 1),
    ("§ 2, sections de location", "**exigées et vérifiées en mode réel** par le code corrigé (contre-lecture du code, M7) |",
     "**exigées et vérifiées en mode réel**, bornes du devis à l'égalité (M7, levé par la vérification des corrections) ; le gabarit porte l'étiquette `iib-explo-v5` |", 1),
    ("§ 2, intouchables", "l'attestation `IIB_AUCUNE_INTOUCHABLE=oui` est **interdite** sous cet ordre |",
     "l'attestation `IIB_AUCUNE_INTOUCHABLE=oui` est **interdite** sous cet ordre, et le lanceur de session en version 3 refuse cette variable |", 1),
    ("§ 2, marqueurs de consigne", "| marqueurs de consigne | `<<MARQUEURS_DE_CONSIGNE>>` |",
     "| marqueurs de consigne | section `marqueurs_de_consigne` de la configuration scellée : empreinte et longueur de chaque marqueur, non vides, jamais leur texte ; fournis par un agent du côté du saboteur, jamais par la mère |", 1),
    ("§ 2, lignes ajoutées à la table de la configuration", "| entropie | `<<ENTROPIE_ETALONNAGE>>` |",
     "| entropie | `<<ENTROPIE_ETALONNAGE>>` |\n| `code` | branche `<<BRANCHE_CODE_V5>>` et commit du code revu `<<COMMIT_CODE_REVU_POUSSE>>` |\n| `prealables.ligne_registre_creation_7b` | l'extrait `7b créée, instance 60218139 à 2026-11-11T14:19:58Z`, trouvé une seule fois au registre des décisions ; ne jamais le recopier sur une autre ligne du registre |\n| première action dans la perte de distillation | `gardee` dans le gabarit ; elle ne joue qu'à la course, mais la configuration est scellée une fois pour l'étalonnage et la course : **à confirmer par le mot de Lazar avant le scellement de la configuration**, `<<MOT_LAZAR_PREMIERE_ACTION_DANS_LA_PERTE>>` |", 1),
    ("§ 2, dépense passée", "| dépense passée | 0, plus `<<DEPENSE_LIGNE_AVANT_LOCATION_USD>>` |",
     "| dépense passée | 0 ; une création manquée qui aurait coûté quelque chose avant la location arrête tout : le fichier d'entrées est à sceller de nouveau, mot de la mère |", 1),
    ("§ 2, actions d'oracle hors tours", "| nombre d'oracles par tour ; actions d'oracle hors tours | 1 ; 3 520 |",
     "| nombre d'oracles par tour ; actions d'oracle hors tours | 1 ; **3 830** (1 270 + 2 560 : erratum 2 du texte scellé, erratum 1 du devis ; le code refuse toute autre valeur) |", 1),
    ("§ 2, vérification du fichier d'entrées", "Le code ne vérifie pas ces valeurs contre le devis (contre-lecture du code, m8) : un lecteur qui n'a pas écrit le fichier les relit",
     "En mode réel, le code vérifie à l'égalité le plafond, le coût fixe, le prix et le nœud 7 (m8, corrigé) ; un lecteur qui n'a pas écrit le fichier les relit tout de même", 1),
    ("§ 2, plafond de tours sous 12",
     "Lecture retenue : `<<LECTURE_PLAFOND_DE_TOURS_SOUS_DOUZE>>`. Le rédacteur ne tranche pas ; la lecture conforme au devis est « ne part pas, motif tours ». **Sans valeur à ce champ, cet ordre n'est pas scellé et rien n'est créé.**",
     "**Lecture retenue, portée par le code à sa tête** (`branches_v5.conditions` ; rapport v2 du développeur, M6 ; levée par la vérification des corrections, « conforme au § 6 du devis ») : si le nombre de tours de la course (R, ou 12 si R ≤ 12) dépasse le plafond de tours, **« ne part pas », motif « tours »** ; jamais 12 tours au-delà du plafond.", 1),
    ("§ 3, règle à 12 USD, état du code", "sans cet essai, aucune création.",
     "sans cet essai, aucune création. À la tête du code, cette règle n'est écrite nulle part (rapport v2 du développeur, § 4 point 3 ; note v4, reste 4) : la surveillance du lanceur de session ne coupe qu'au plafond de la configuration, 55 USD.", 1),
    ("§ 3, restes de la relecture du lanceur", "empreinte du module de lecture portée par la configuration (§ 2).",
     "empreinte du module de lecture portée par la configuration (§ 2). Faits à la tête du code : le lanceur de session en version 3 refuse la variable d'attestation, et le gabarit porte l'empreinte du module de lecture dans `code.module_de_lecture` et dans la liste des empreintes du code.", 1),
    ("§ 3, risque de la coupe",
     "- **Étiquette** ; **branche d'essai absente du distant** ; **réponse brute du loueur conservée**, masquée, jamais supprimée.",
     "- **Étiquette** ; **branche d'essai absente du distant** ; **réponse brute du loueur conservée**, masquée, jamais supprimée.\n\n**Risque écrit d'avance : la valeur du coût à la ligne qui suit la clé.** Le tokeniseur réel a un jeton « :\\n » : une valeur écrite à la ligne suivante, ou une clé vide, n'a alors aucune coupe conforme « juste après COST: » ; l'action est comptée et n'est pas bornable (vérification des corrections, constat 8, point 2 ; la coupe de la première course rejetait aussi cette forme). La clé en gras fermée après les deux-points, elle, est corrigée par le correctif 0008. Si moins de 95 % des actions honnêtes à champ de coût ont une coupe conforme, l'épreuve de la coupe, commune aux deux oracles, les met tous deux en défaut : **l'issue est « ne part pas »** (texte scellé, section 9 ; 10.3, étape 2 ; section 15), écrite d'avance, sans liberté. **La perte est bornée à l'étalonnage** (devis § 3 : environ 4,8 USD attendus si la course ne part pas). Personne n'a mesuré la fréquence de cette forme ; admettre une coupe après « :\\n » changerait la définition du texte scellé : ce serait un nœud de conception, que cet ordre ne pose pas.", 1),
    ("§ 4, préalable du code",
     "2. **Code** : B1, M1, M2, M3 et M7 corrigés, M6 tranché (§ 2), puis vérifiés par le même contre-lecteur (`<<VERIFICATION_CORRECTIONS_CODE_V5>>`) ; un essai à blanc de bout en bout par le point d'entrée, sur le monde jouet. Le distillateur n'est pas nécessaire à l'étalonnage seul.",
     "2. **Code** : B1, M1, M2, M3, M6 et M7 corrigés par le correctif 0007 et levés par la vérification des corrections (`6a9e2e7927b03533552b676b694736e6eb3ace72d58ca52007cb1c6b9cadfa57`), qui laisse deux restes : R1, la coupe après une clé en gras fermée après les deux-points, et R2, l'amorce jamais jouée ; tous deux traités par le correctif 0008 ; le correctif 0009 raccorde le distillateur, porte 3 830 et fige la liste des essais. **Reste : la vérification courte des correctifs 0008 et 0009 par le même contre-lecteur**, `<<VERIFICATION_COURTE_CORRECTIFS_0008_0009>>` ; sans elle, pas de scellement. Répétition locale à blanc, mode jouet, faux outil de location : lanceur de session en version 3, amorce en version 5 (267 essais), étalonnage versé par lot et poussé, destruction par l'identifiant, conditions et désignation, second passage refusé : réussie, code 0 (`sortie-repetition-locale-v2.txt`). **Jamais éprouvés** : le mode réel (carte, chargement du modèle réel, consignes et tâches réelles), la minuterie et les appels au loueur de l'amorce, la commande de création elle-même. Le distillateur n'est pas nécessaire à l'étalonnage seul.", 1),
    ("§ 4, essai sur le tokeniseur réel",
     "coupe, fenêtre de 16 jetons, réécriture et gardes de décodage (`<<ESSAI_TOKENISEUR_REEL_PIECE>>`) ; un échec : arrêt, code en version nouvelle.",
     "coupe, fenêtre de 16 jetons, réécriture et gardes de décodage : **fait** par le développeur (135 cas au correctif 0007, rejoués par le contre-lecteur ; 16 cas de clé en gras de plus au correctif 0008 ; `sortie-essais-cibles-v5-v3.txt` : 359 réussis, tokeniseur réel compris) ; les cas du correctif 0008 attendent la vérification courte. Limite dite par le développeur : son essai imite le nettoyage du décodage de la bibliothèque, qui n'est pas éprouvée elle-même. Cet essai n'est pas dans la liste figée de la machine.", 1),
    ("§ 5, commandes",
     "Commandes : `<<COMMANDES_POINT_D_ENTREE_V5>>` ; les sous-commandes citées ci-dessous sont celles de `scripts/lancer_iib_v2.sh` dans les correctifs 0001 à 0003 ; elles sont relues au commit de lancement avant le scellement.",
     "Le lanceur de session est `scripts/lancer_iib_v3.sh` (`5fd1105c2ae3575b10087fbb90ad7baec30480f909055b40d343e82dd4aa7d54` à la tête du code) : la version 2 avec sept lignes changées (amorce en version 5, configuration vérifiée par `session_v5`, pièces lues sous `pieces.`, branche par défaut `essai/iib-explo-v5`, attestation « aucune intouchable » retirée) ; mêmes sous-commandes que la version 2 : `outil`, `--verifier-go-seulement`, `controles-explo`, `creation`, `apres-creation`, `surveillance`, `destruction`. Toutes les commandes sont de la forme `\"${ENVI[@]}\" bash scripts/lancer_iib_v3.sh …`, depuis le dépôt extrait au commit de lancement ; elles sont rejouées à blanc à ce commit par l'exécutante (§ 4 étape 6).", 1),
    ("§ 5, chemin de l'outil", "`VAST=<<CHEMIN_OUTIL_LOCATION>>`, chemin explicite",
     "variable `VAST`, chemin explicite de l'outil, relevé par l'exécutante et porté au compte rendu", 1),
    ("§ 5, parent du commit de lancement", "son parent est `<<COMMIT_CODE_REVU_V5>>`", "son parent est `<<COMMIT_CODE_REVU_POUSSE>>`, dont l'arbre est `" + ARBRE + "`", 1),
    ("§ 5, dernière création", "**aucune commande `creation` après 2026-11-27T00:00Z**",
     "**aucune commande `creation` à partir de 2026-11-27T00:00:00Z (instant exclu ; dernier jour : le 26)**", 1),
    ("§ 5, lieu du passage des conditions", "lieu : `<<LIEU_DU_PASSAGE_DES_CONDITIONS>>` ;",
     "lieu : sur processeur, par l'exécutante, après le rapatriement vérifié, sur les sorties rapatriées du même run, par `PYTHONPATH=src python -m controle_ia.iib.lanceur_v5 --phase conditions --config <configuration> --run-id <run>` ;", 1),
    ("§ 5, sort de la machine", "7. **Sort de la machine** : après le rapatriement vérifié",
     "7. **Sort de la machine** : `<<SORT_DE_LA_MACHINE_APRES_ETALONNAGE>>` (mot de la mère, écrit ici avant le scellement) ; dans tous les cas, après le rapatriement vérifié", 1),
    ("levée bornée, lanceur de session", "les appels faits par `scripts/lancer_iib_v2.sh` lui-même", "les appels faits par `scripts/lancer_iib_v3.sh` lui-même", 1),
    ("§ 6, heure de la dernière création", "heure passée 2026-11-27T00:00Z", "heure à partir de 2026-11-27T00:00:00Z", 1),
    ("§ 6, issues, la coupe", "coupe en échec, « ne part pas », « non calculable »",
     "coupe en échec (risque écrit au § 3), « ne part pas », « non calculable »", 1),
    ("§ 7, noms des sorties",
     "Noms au correctif 0005 (`lanceur_v5.py`) ; liste au commit de lancement, fichiers par lot compris : `<<LISTE_SORTIES_ETALONNAGE>>`.",
     "Noms à la tête du code (`lanceur_v5.py`, amorce en version 5) : après chaque lot de huit épisodes, les sorties d'oracle sous `diag/<run>/lots/` et les identifiants des actions sous `donnees/<run>/lots/`, scellés et poussés ; le manifeste du run sous `runs/<run>/` ; à la fin `diag/<run>/resume.json` ; sur toute garde, toute erreur ou tout signal d'arrêt, `diag/<run>/arret.json`, avec l'étape, le motif et la liste de ce qui est écrit : les lots restent, aucune issue n'est inventée.", 1),
    ("§ 7, manifeste", "| fin de l'étalonnage | `manifeste-etalonnage-iib-v5.json` | configuration et empreinte, versions, entropie et graines, commit, sorties |",
     "| début, puis fin | manifeste du run sous `runs/<run>/` ; `diag/<run>/resume.json` | configuration et empreinte, versions, entropie et graines, commit ; liste des sorties, lots, durées, validité du contrôle du premier coût |", 1),
    ("§ 9, erratum du devis", "les deux oracles neufs n'ont jamais été chronométrés.",
     "les deux oracles neufs n'ont jamais été chronométrés. L'erratum 1 du devis ne change aucun chiffre de l'étape 1.", 1),
    ("§ 11, correctifs lus, ajout",
     "| `0006-Organisme-retenu-du-saboteur-budget-code-en-version-.patch` | `ee867c9c6d429d4b5e2aef6b48ccc67ef3e1073e043aec34f2d19ef521ca73ca` |",
     "| `0006-Organisme-retenu-du-saboteur-budget-code-en-version-.patch` | `ee867c9c6d429d4b5e2aef6b48ccc67ef3e1073e043aec34f2d19ef521ca73ca` |\n@@CORRECTIFS@@\n\nOrdre d'application sur `836c7cccda5071fe54ecb148d214d74b5cb90474` : les douze lignes de cette table, de haut en bas ; les lignes 7 à 12 sont sous `" + C + "` ; arbre attendu `" + ARBRE + "`.", 1),
    ("§ 12, point 2", "2. **Cas du plafond de tours sous 12** : à écrire avant le scellement (§ 2).",
     "2. **Cas du plafond de tours sous 12** : réglé par le code, « ne part pas », motif « tours » (§ 2).", 1),
    ("§ 12, point 3", "3. **Ligne `GO-2026-11-21-74`** : citée par le mandat, non trouvée au registre de `main`.",
     "3. **Ligne `GO-2026-11-21-74`** : trouvée au registre de `main` au brouillon 2 ; la mère confirme qu'elle vaut mot de Lazar pour la création.", 1),
    ("§ 12, point 4", "l'ordre suit la ligne d'accord.",
     "l'ordre suit la ligne d'accord, lue « instant exclu, dernier jour le 26 », comme le code ; si la ligne veut dire « le 27 compris », la constante du code est à changer avant le scellement.", 1),
    ("§ 12, point 5", "le lanceur de session exige une branche `prep/…`.",
     "le lanceur de session exige une branche `prep/…` : la mère ou l'exécutante appliquent les douze correctifs sur une branche `prep/` neuve et la poussent (§ 1) ; le code et la configuration du saboteur ne vont jamais sur `main`.", 1),
    ("§ 12, point 6", "si le code corrigé l'exige encore, la configuration reprend l'extrait de l'ordre d'origine, sans le recopier au registre.",
     "le code l'exige encore en mode réel : la configuration reprend l'extrait de l'ordre d'origine (§ 2), sans le recopier au registre.", 1),
    ("§ 12, points ajoutés", "et laisse le choix à la mère, dans les bornes du devis.\n",
     "et laisse le choix à la mère, dans les bornes du devis.\n8. **Règle de la surveillance à 12 USD** : accordée par la ligne d'accord et exigée par le devis, avec son essai sur un cas sain et sur un artefact avant la création ; elle n'est écrite dans aucun code à la tête. Elle reste un champ : sa forme et son essai sont à fournir avant le scellement.\n9. **Empreinte du commit du code revu** : la tête locale du développeur est `" + TETE + "` ; un commit refait par qui applique les correctifs peut porter une autre empreinte ; l'ordre exige l'égalité de l'arbre.\n10. **Première action dans la perte de distillation** : `gardee` dans le gabarit, à confirmer par le mot de Lazar avant le scellement de la configuration.\n11. **Jamais éprouvés avant la machine** : le chargement du modèle réel et le mode réel, la minuterie et les appels au loueur de l'amorce en version 5.\n", 1),
]

# Champs remplis partout : nom -> valeur.
REMPLIS = {
    "TESTS_ATTENDUS_V5": "267",
    "ENTROPIE_ETALONNAGE": ENTROPIE,
    "BRANCHE_ETALONNAGE": "essai/iib-explo-v5",
    "LIGNE_MOT_LAZAR_CREATION": "GO-2026-11-21-74",
    "DEPENSE_LIGNE_AVANT_LOCATION_USD": "0",
}
# Champs restants : nom -> (ce qu'il attend, qui le remplit).
CHAMPS = [
    ("BRANCHE_CODE_V5", "branche `prep/` neuve, poussée, qui porte la base et les douze correctifs", "mère ou exécutante"),
    ("COMMIT_CODE_REVU_POUSSE", "commit du code revu sur cette branche ; son arbre est `" + ARBRE + "`", "mère ou exécutante"),
    ("VERIFICATION_COURTE_CORRECTIFS_0008_0009", "chemin, empreinte et verdict de la vérification courte des correctifs 0008 et 0009 par le même contre-lecteur", "session de reconception"),
    ("COMMIT_LANCEMENT_ETALONNAGE", "commit de lancement : enfant direct du commit du code revu, qui n'ajoute que la configuration, le fichier d'entrées et leurs sceaux", "exécutante, vérifié par la mère"),
    ("CONFIG_ETALONNAGE_CHEMIN_ET_EMPREINTE", "chemin et empreinte de la configuration scellée, au commit de lancement", "exécutante"),
    ("FICHIER_ENTREES_CHEMIN_ET_EMPREINTE", "chemin et empreinte du fichier d'entrées scellé (§ 2)", "exécutante, vérifié par la mère"),
    ("INSTANCES_INTOUCHABLES", "identifiants des machines des autres chantiers, relevés à l'inventaire en champs filtrés ; liste non vide", "exécutante"),
    ("ETIQUETTE_ETALONNAGE", "étiquette de la machine, qui commence par `iib` ; le gabarit porte `iib-explo-v5`", "mère"),
    ("MOT_LAZAR_PREMIERE_ACTION_DANS_LA_PERTE", "ligne du registre qui porte le mot de Lazar sur la première action dans la perte de distillation (`gardee` ou `exclue`)", "mère"),
    ("REGLE_COUPURE_ETALONNAGE_FORME_ET_ESSAIS", "forme exacte de la règle de la surveillance à 12 USD, et pièce de son essai sur un cas sain et sur un artefact ; elle n'est pas écrite dans le code à sa tête", "session de reconception"),
    ("SORT_DE_LA_MACHINE_APRES_ETALONNAGE", "destruction après le rapatriement vérifié, ou garde à l'arrêt pour la course sous son ordre à part", "mère"),
]


def sha(chemin: Path) -> str:
    return hashlib.sha256(chemin.read_bytes()).hexdigest()


def ecrire(chemin: Path, texte: str) -> str:
    if chemin.exists() or Path(str(chemin) + ".sha256").exists():
        sys.exit(f"{chemin} existe déjà : refus d'écraser (R12)")
    chemin.write_bytes(texte.encode("utf-8"))
    e = sha(chemin)
    Path(str(chemin) + ".sha256").write_text(f"{e}  {chemin.name}\n", encoding="utf-8")
    return e


def main(argv) -> int:
    if len(argv) != 4:
        sys.exit("usage : RACINE_DU_DEPOT DOSSIER DATE")
    racine, dossier, date = Path(argv[1]), Path(argv[2]), argv[3]
    if sha(dossier / B1) != B1_SHA:
        sys.exit("brouillon 1 : empreinte différente de celle attendue")
    for chemin, attendue in PIECES.items():
        if sha(racine / chemin) != attendue:
            sys.exit(f"pièce citée {chemin} : empreinte différente de celle attendue")
        compagnon = (racine / (chemin + ".sha256")).read_text(encoding="utf-8").split()[0]
        if compagnon != attendue:
            sys.exit(f"pièce citée {chemin} : compagnon différent")
    texte = (dossier / B1).read_text(encoding="utf-8")
    avant = set(re.findall(r"<<([A-Z0-9_]+)>>", texte))
    lignes_note = []
    for nom, ancre, neuf, compte in CHANGEMENTS:
        n = texte.count(ancre)
        if n != compte:
            sys.exit(f"changement « {nom} » : ancre trouvée {n} fois, {compte} attendu : {ancre[:80]!r}")
        texte = texte.replace(ancre, neuf.replace("@@DATE@@", date))
        resume = " ".join(neuf.replace("@@DATE@@", date).split())
        lignes_note.append(f"- {nom} : « {' '.join(ancre.split())[:110]}… » remplacé par « {resume[:260]}{'…' if len(resume) > 260 else ''} ».")
    for nom, valeur in REMPLIS.items():
        jeton = f"<<{nom}>>"
        n = texte.count(jeton) - 1          # l'occurrence de la table des champs est retirée avec la table
        if n < 1:
            sys.exit(f"champ {nom} : aucune occurrence hors de la table")
        texte = texte.replace(jeton, valeur)
        lignes_note.append(f"- champ `<<{nom}>>` rempli partout ({n} fois hors de la table) : {valeur}.")
    debut = "| champ | ce qu'il attend | qui le remplit |\n|---|---|---|\n"
    fin = "\n\n**Correctifs lus**"
    if texte.count(debut) != 1 or texte.count(fin) != 1:
        sys.exit("table des champs : bornes introuvables ou en double")
    i, j = texte.index(debut) + len(debut), texte.index(fin)
    texte = texte[:i] + "\n".join(f"| `<<{n}>>` | {quoi} | {qui} |" for n, quoi, qui in CHAMPS) + texte[j:]
    table = "\n".join(f"| {rang} | `{Path(chemin).parent.name}/{Path(chemin).name}` | `{e}` |" for rang, chemin, e in CORRECTIFS)
    if texte.count("@@CORRECTIFS@@") != 1:
        sys.exit("jeton de la table des correctifs")
    texte = texte.replace("@@CORRECTIFS@@", "\n".join(f"| `{Path(chemin).parent.name}/{Path(chemin).name}` (rang {rang}) | `{e}` |" for rang, chemin, e in CORRECTIFS))
    del table
    if "@@" in texte:
        sys.exit("un jeton n'a pas été rempli")
    restants = set(re.findall(r"<<([A-Z0-9_]+)>>", texte))
    noms = {c[0] for c in CHAMPS}
    if restants != noms:
        sys.exit(f"champs du texte et table des champs différents : {sorted(restants ^ noms)}")
    for interdit in ("lancer_iib_v2.sh` lui-même", "3 520 |", "IIB_AUCUNE_INTOUCHABLE=oui` est permise"):
        if interdit in texte:
            sys.exit(f"reste inattendu : {interdit}")
    e2 = ecrire(dossier / B2, texte)
    note = [f"# Différences — ordre de l'étalonnage de l'organisme retenu, du brouillon 1 au brouillon 2 — v1", "",
            f"Source : `{B1}` (`{B1_SHA}`). Produit : `{B2}` (`{e2}`). Écrite par le programme `fabriquer-ordre-etalonnage-ii-b-v5-brouillon2-v1.py`, le {date}. Une différence par ligne ; tout le reste est recopié à l'octet.", "",
            "## Remplacements, un par ligne (ancre trouvée le nombre de fois attendu)", ""] + lignes_note
    note += ["", "## Table des champs du § 11, une différence par ligne", ""]
    note += [f"- champ `<<{n}>>` retiré de la table : {'rempli' if n in REMPLIS else 'rempli ou remplacé par un remplacement ci-dessus'}." for n in sorted(avant - noms)]
    note += [f"- champ `<<{n}>>` ajouté : {quoi}." for n, quoi, _ in CHAMPS if n not in avant]
    note += [f"- champ `<<{n}>>` gardé." for n, _, _ in CHAMPS if n in avant]
    note += ["", "## Pièces dont l'empreinte et le compagnon ont été vérifiés avant l'écriture, une par ligne", ""] + [f"- `{c}` : `{e}`." for c, e in PIECES.items()]
    e_note = ecrire(dossier / NOTE, "\n".join(note) + "\n")
    print(f"brouillon 2 : {e2} ; {len(texte)} caractères ; {len(CHANGEMENTS)} remplacements ; champs restants : {len(CHAMPS)}")
    print(f"note des différences : {e_note}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
