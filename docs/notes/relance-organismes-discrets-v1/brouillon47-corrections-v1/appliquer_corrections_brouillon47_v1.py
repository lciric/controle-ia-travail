#!/usr/bin/env python3
"""Brouillon 47 du bras A des organismes discrets, depuis le brouillon 46.

Porte les majeurs M-1, M-2, M-4 et M-5 et les mineurs de la contre-lecture
10, par remplacements exacts ; remplit les cases « commit du code de
l'instrument et de l'analyse » et « familles » au texte du mandat de la
session (GO-2026-11-21-84 : mot pour mot, sans conception). Les textes
proposés par la contre-lecture sont lus dans son fichier (empreinte
contrôlée), non recopiés à la main. Chaque ancien doit se trouver une seule
fois, sinon arrêt. Les huit règles d'admission (lignes 542 à 550) doivent
rester égales, caractère pour caractère, aux mêmes numéros de ligne.
M-3, M-6 et M-7 ne sont pas portés.

Usage : python3 -I appliquer_corrections_brouillon47_v1.py RACINE_DU_DEPOT
"""
import hashlib
import pathlib
import sys

RACINE = pathlib.Path(sys.argv[1])
CL10 = "docs/notes/relance-organismes-discrets-v1/contre-lecture-10-brouillon46-bras-a-v1.md"
CL10_SHA = "f711c9be09b8912adcb82d469a09f03e89b80ac67950cc2235e4d2cfebda1881"
B46 = "prereg/T0.7-organismes-discrets-v-a-v2-brouillon46.md"
B46_SHA = "b5e1031c9b92d7643815e9d18abec86f900fee0931eb6030839729b2f32c3fb9"
B47 = "prereg/T0.7-organismes-discrets-v-a-v2-brouillon47.md"
REGLES46 = ("docs/notes/relance-organismes-discrets-v1/essais-admission-bras-a-v1/"
            "regles-admission-bras-a-v1-brouillon46.md")
REGLES46_SHA = "fdc9254fc2294343e1ff1d5d527ac8b24a466f084ff38d674013580321eb31d2"
CHEF12 = "scripts/chef_essais_admission_bras_a_v12.py"
CHEF12_SHA = "6aa04397997a52785ce4bd05e1b7a45c5886e1565f3e2927984b08373d9758b1"
REGLES_SHA = "3d1f0afe82f5aeb3bf5dd757cb6d814e19c66b93a89a65b6f08677823e1b8f96"


def arret(msg):
    sys.exit("ARRÊT : " + msg)


def lire(chemin, sha):
    octets = (RACINE / chemin).read_bytes()
    h = hashlib.sha256(octets).hexdigest()
    if h != sha:
        arret(f"{chemin} : empreinte {h} au lieu de {sha}")
    return octets.decode("utf-8")


v = lire(CL10, CL10_SHA).split("\n")
t46 = lire(B46, B46_SHA)
lire(REGLES46, REGLES46_SHA)
lire(CHEF12, CHEF12_SHA)


def ligne(n):
    return v[n - 1]


def entre(s, debut, fin, dernier=False):
    i = s.index(debut) + len(debut)
    j = s.rindex(fin) if dernier else s.index(fin, i)
    if j <= i:
        arret("extraction impossible : " + debut)
    return s[i:j]


# --- textes de la contre-lecture 10, lus dans son fichier ---
L24, L26 = ligne(24), ligne(26)
M1_CL_ANCIEN = entre(L24, "remplacer « ", " » par « ")
M1_CL_NEUF = entre(L24, " » par « ", " ».", dernier=True)
M1_ETAPE6 = entre(ligne(25), "même changement (« ", " »).")
M1_E_A = entre(L26, "remplacer « ", " » par « ")
_r = L26[L26.index(" » par « ") + len(" » par « "):]
M1_E_B = _r[:_r.index(" » ; et remplacer « ")]
_r = _r[_r.index(" » ; et remplacer « ") + len(" » ; et remplacer « "):]
M1_E_C = _r[:_r.index(" » par « ")]
M1_E_D = _r[_r.index(" » par « ") + len(" » par « "):_r.rindex(" ».")]
L36 = ligne(36)
M4_ANCIEN = entre(L36, "ligne 551, à la place de « ", " » : « ")
M4_NEUF = entre(L36, " » : « ", " » ; et « Le rang")
M4_GARDE = entre(L36, "Ajouter une ligne à 8.4 : « ", " ».", dernier=True)
M5 = entre(ligne(38), "et dans la case « version des modèles » de 13.2 : « ", " »", dernier=True)
m1 = entre(ligne(48), "Ajouter à la ligne A8 : « ", " ».", dernier=True)
m2_5 = entre(ligne(50), "Écrire « ", " » et « ")
m2_10 = entre(ligne(50), " » et « au", " », ou renvoyer")
m2_10 = "au" + m2_10
m3_922 = entre(ligne(53), "Écrire « ", " ».", dernier=True)
m3_972 = entre(ligne(54), "Écrire « ", " ».", dernier=True)
m5 = entre(ligne(63), "(« ", " »)")
m6 = entre(ligne(65), "dire : « ", " ».", dernier=True)
m7 = entre(ligne(67), "une phrase : « ", " ».", dernier=True)
m8 = entre(ligne(69), "(« ", " »)")
m9 = entre(ligne(71), "Écrire « ", " ».", dernier=True)

for nom, val, attendu in [
    ("M1_CL_ANCIEN", M1_CL_ANCIEN,
     "(du texte aux cases remplies, et de la reprise des corrections de la contre-lecture 9)"),
    ("m2_5", m2_5, "au plus 5 %"), ("m2_10", m2_10, "au plus 10 %"),
    ("m3_922", m3_922, "est écrit côté habilité (case de 13.1)"),
    ("m3_972", m3_972, "écrit (case « code de la base », 13.1)"),
    ("m8", m8, "température retirée d'avance"),
]:
    if val != attendu:
        arret(f"extraction {nom} : {val!r}")
for nom, val, debut, fin in [
    ("M1_CL_NEUF", M1_CL_NEUF, "(du texte entier, cases de 13.1 ouvertes", "celle de son rapport"),
    ("M1_ETAPE6", M1_ETAPE6, "contre-lecture 10 sur le texte", "; scellement"),
    ("M1_E_A", M1_E_A, "quand toutes les autres cases", "vérification habilitée sont rendues"),
    ("M1_E_B", M1_E_B, "quand toutes les autres cases", "vérification habilitée sont rendues"),
    ("M1_E_C", M1_E_C, "la différence entre le texte contre-lu", "et de la vérification habilitée"),
    ("M1_E_D", M1_E_D, "la différence entre le texte relu", "que la contre-lecture 10 fait corriger"),
    ("M4_ANCIEN", M4_ANCIEN, "(étape (d) de 6.3", "en un second lot)"),
    ("M4_NEUF", M4_NEUF, "(à l'étape (d) de 6.3, deux lots", "`ordr/{lot}` (6.2)"),
    ("M4_GARDE", M4_GARDE, "voie de service du juge | chaque appel", "dépend d'une réponse : refusés"),
    ("M5", M5, "La sortie maximale que donne la règle 7", "sur un artefact (8.4)."),
    ("m1", m1, "sur l'épreuve en vigueur ;", "est rapporté et ne décide pas"),
    ("m5", m5, "une confrontation négative", "par les règles 5 et 6"),
    ("m6", m6, "si le rapport demande une correction", "avant le scellement"),
    ("m7", m7, "un repli inséré à ce point", "les deux sont rapportés"),
    ("m9", m9, "; les appels de rang impair", "`GEMINI_API_KEY_2`"),
]:
    if not (val.startswith(debut) and val.endswith(fin)):
        arret(f"extraction {nom} : {val[:60]!r} … {val[-60:]!r}")

M1_ETAPE6_TETE = M1_ETAPE6[0].upper() + M1_ETAPE6[1:]   # début d'un point numéroté
m3_972_TETE = "**É" + m3_972[1:].replace(" (case", "** (case", 1)
M4_1483 = ("(rang compté dans chaque lot du juge : "
           + M4_NEUF[1:].replace("`revision/…/ancre-jumeaux`), chacun",
                                 "`revision/…/ancre-jumeaux` ; chacun") + ")")

# --- textes du mandat de la session (points 3 et 4), recopiés du mandat ---
COMMIT_NEUF = ("**remplie** : commit `2b9f82328f2fd729cd21bf8b0150cf76ae12690d`, branche "
               "`claude/pensive-bardeen-1fv7hw`, inscrit par la session mère (registre des "
               "décisions, R-4885 ; dix empreintes recalculées au commit et à la tête, concordantes)")
FAMILLES_NEUF = ("**la confrontation est faite le 22 novembre 2026 par le lecteur habilité : "
                 "`mistral-large-4-0` et `gemini-4-neon` sont hors de toute famille de la liste, "
                 "conforme** (pièce sans interne `docs/notes/bras-a-contre-lecture-habilitee-v1/"
                 "familles-confrontation-lecteurs-bras-a-sans-interne-v1.md`, "
                 "`5e83cf07fef0aa5efd55b03b2edd9b88891457b915f79d9c01ec3a006bcf46c8`, sur la "
                 "branche principale ; contenu non lu par la session)")

# --- textes du correcteur (le plus court qui porte ce que dit la contre-lecture), déclarés ---
CL10_REF = f"`{CL10}`, `{CL10_SHA}`"
HISTOIRE = (
    "**Statut : brouillon 47, non exécutable.** Le brouillon 47, écrit par Claude Opus 5.5, "
    "agent neuf, par un programme de remplacements exacts, porte les corrections M-1, M-2, M-4 "
    "et M-5 et les mineurs de la contre-lecture 10 (" + CL10_REF + ", « scellable après "
    "corrections » : aucun bloquant, sept majeurs, neuf mineurs), mot pour mot, sans rien "
    "concevoir (décision de Lazar, GO-2026-11-21-84) ; les cases « commit du code de "
    "l'instrument et de l'analyse » et « familles » de 13.1 sont remplies ; M-3, M-6 et M-7 ne "
    "sont pas portés et restent en attente (M-6 et M-7 au directeur) ; aucune règle, aucun "
    "seuil, aucune issue ni aucune prédiction ne change, et les huit règles d'admission restent "
    "aux lignes 542 à 550, caractère pour caractère. **Cases de 13.1 ouvertes, déclarées** "
    "(contre-lecture 10, M-2) : « nœuds », « lecteurs et juge des ancres », « entropie », "
    "« renvoi de la base », « module des cinq moniteurs, côté habilité ». "
    "**État au brouillon 46, dépassé pour ce que le brouillon 47 change** : "
    "Le brouillon 46, écrit par Claude Opus 5.5, agent neuf, par un programme de remplacements "
    "exacts, porte les corrections C-1 à C-5"
)
CL10_INSCRITE = (
    ". **Contre-lecture 10 faite** : texte relu `" + B46 + "`, `" + B46_SHA + "` ; rapport " + CL10_REF +
    " ; contre-lecteur : agent neuf, Claude Opus 5.5 ; verdict « scellable après "
    "corrections », aucun bloquant, sept majeurs, neuf mineurs ; traitement : au brouillon 47, "
    "M-1, M-2, M-4, M-5 et les mineurs, mot pour mot ; M-3, M-6 et M-7 en attente (statut). "
    "À inscrire ici avant scellement, à part :"
)
M4_LIGNE_84 = "| " + M4_GARDE + " |"
REGLES_FOI = (
    " **Fichier des règles qui fait foi au scellement** (contre-lecture 10, m-4) : `" + REGLES46 +
    "`, `" + REGLES46_SHA + "`, qui porte les lignes 542 à 550 caractère pour caractère et "
    "l'empreinte du brouillon 46 ; il nomme comme programme qui applique les règles "
    "`scripts/chef_essais_admission_bras_a_v6.py` ; la file du juge a été conduite par `" +
    CHEF12 + "`, `" + CHEF12_SHA + "` : déclaré."
)
RESTENT_ETAT = (" — **fait** (contre-lecture 10, m-3) : pièces de constat inscrites au "
                "brouillon 45, sous la levée partielle de GO-2026-11-21-68, et point d'accès "
                "européen inscrit plus haut")
LISTE_ETAT = (
    " ; **état au brouillon 47** (contre-lecture 10, m-3) : (1) fait, pièces de constat "
    "`4907d092…` et `2234e0cb…`, sous la levée partielle de GO-2026-11-21-68 ; (2) fait pour "
    "le devis (`421ee2e6…`) et ses avenants, et pour les lignes GO-2026-11-21-83 et "
    "GO-2026-11-22-60 à -62 ; reste : la contre-lecture du devis, par chemin et empreinte ; "
    "(3) reste : le relevé de chaque vérification de clé par chemin et empreinte (celui de "
    "Mistral n'est nommé que par son dossier) ; (4) fait, fichier des règles ci-dessus et "
    "rapports techniques `74106c3e…` et `7bb8cc95…` ; (5) fait, plus haut ; (6) sans objet, "
    "les deux modèles tiennent"
)

L551_RANG = ("existe ; ceux de rang impair partent sous la clé lue sous `GEMINI_API_KEY`, ceux "
             "de rang pair sous la clé lue sous `GEMINI_API_KEY_2`")

REMPLACEMENTS = [
    ("titre", "— v2, BROUILLON 46\n", "— v2, BROUILLON 47\n"),
    ("statut et histoire ; M-2 (cases ouvertes déclarées)",
     "**Statut : brouillon 46, non exécutable.** Le brouillon 46, écrit par Claude Opus 5.5, "
     "agent neuf, par un programme de remplacements exacts, porte les corrections C-1 à C-5",
     HISTOIRE),
    ("m-8, 3.4 (demi-ligne)",
     "provenance par transcription, non opposable, R7) ; offre payante ; sortie maximale large "
     "devant la réflexion ; appels synchrones.",
     "provenance par transcription, non opposable, R7) ; " + m8 + " pour `mistral-large-4-0` "
     "(GO-2026-11-21-86) ; offre payante ; sortie maximale large devant la réflexion ; appels "
     "synchrones."),
    ("M-4 (i), ligne 551", M4_ANCIEN, M4_NEUF),
    ("m-9, ligne 551", L551_RANG, "existe " + m9),
    ("M-5, 3.4, ligne neuve après la règle 8 (règles inchangées)",
     "la correction C-2 du brouillon 40 ne visait que la formule « sans choix de la session », "
     "à la ligne des réglages.\n  - **La file du juge sur deux clés de Google",
     "la correction C-2 du brouillon 40 ne visait que la formule « sans choix de la session », "
     "à la ligne des réglages.\n  - " + M5 + "\n  - **La file du juge sur deux clés de Google"),
    ("m-2, prédiction",
     "contrôles d'une autre tâche presque jamais jugés « appariés spécifiques » ; texte sans "
     "rapport jamais jugé apparié |",
     "contrôles d'une autre tâche jugés « appariés spécifiques » " + m2_10 + " ; texte sans "
     "rapport jugé apparié " + m2_5 + " |"),
    ("m-7, 6.3, point 2", "(section 9.2, lignes 277 et 278) ;",
     "(section 9.2, lignes 277 et 278) ; " + m7 + " ;"),
    ("m-3, 6.10, Message", "est à écrire, avec ses essais (13.1)", m3_922),
    ("m-3, 6.12, point 6", "**Manque, à écrire avant scellement** (13.1)", m3_972_TETE),
    ("m-1, ligne A8",
     "| A8 | effet minimal détectable > 0,20 (étape (h1), sur les seuls honnêtes, avant (e′) et "
     "les jumeaux) |",
     "| A8 | effet minimal détectable > 0,20 (étape (h1), sur les seuls honnêtes, avant (e′) et "
     "les jumeaux) " + m1 + " |"),
    ("M-4 (iii), ligne neuve de 8.4",
     "\n\n**Deux gardes tenues côté habilité",
     "\n" + M4_LIGNE_84 + "\n\n**Deux gardes tenues côté habilité"),
    ("m-3, 8.4 sous la table",
     "case « entropie », 13.1 ; ligne de GO à inscrire, case « nœuds »)",
     "case « entropie », 13.1 ; ligne de GO inscrite, case « nœuds »)"),
    ("m-3, 8.7", "la ligne du mot « go recos », encore à inscrire",
     "la ligne du mot « go recos », GO-2026-11-20-19 (case « nœuds »)"),
    ("M-1, section 13, étape 6",
     "6. Cases de 13.1 remplies ; vérification du texte aux cases remplies et de la reprise des "
     "corrections de la contre-lecture 9 par un contre-lecteur d'un autre modèle que le "
     "rédacteur, inscrite comme contre-lecture 10 (R2) ; vérification habilitée ; scellement (R1).",
     "6. " + M1_ETAPE6_TETE + " (R1)."),
    ("m-3, case « nœuds »", "date d'envoi à Lazar à inscrire)", "date d'envoi à Lazar **À REMPLIR**)"),
    ("case « familles », marque", "| familles | **remplie, sauf un reste À REMPLIR** (",
     "| familles | **remplie** ("),
    ("case « familles », confrontation ; m-5",
     "**au 22 novembre 2026, cette confrontation n'existe pas, et la case reste ouverte** (",
     FAMILLES_NEUF + " ; " + m5 + " ("),
    ("m-3, case « lecteurs », restent à inscrire",
     "pour Mistral, le point d'accès retenu ; **inscrit au brouillon 44",
     "pour Mistral, le point d'accès retenu" + RESTENT_ETAT + " ; **inscrit au brouillon 44"),
    ("m-4, case « lecteurs », fichier des règles",
     "qui cite les lignes 529 à 537 et l'empreinte du brouillon 44.",
     "qui cite les lignes 529 à 537 et l'empreinte du brouillon 44." + REGLES_FOI),
    ("m-3, case « lecteurs », liste (1) à (6)",
     "(6) si un modèle ne tient pas, le mot de Lazar qui pourvoit son rôle ;",
     "(6) si un modèle ne tient pas, le mot de Lazar qui pourvoit son rôle" + LISTE_ETAT + " ;"),
    ("m-3, case « lecteurs », ligne de GO",
     "Lazar (mot du 19 novembre 2026 ; ligne de GO à inscrire, case « nœuds »)",
     "Lazar (mot du 19 novembre 2026 ; ligne de GO inscrite, case « nœuds »)"),
    ("M-1, case « entropie » (a)", M1_E_A, M1_E_B),
    ("M-1, case « entropie » (b)", M1_E_C, M1_E_D),
    ("m-6, case « renvoi de la base »",
     "ou « non vérifié : discrétion non lue » | la discrétion |",
     "ou « non vérifié : discrétion non lue » ; " + m6 + " | la discrétion |"),
    ("case « commit »",
     "**À REMPLIR** : le commit, à inscrire par la session qui orchestre (GO-2026-11-19-24, point 1)",
     COMMIT_NEUF),
    ("M-4, ligne 1483",
     "(rang compté dans chaque lot du juge, étapes (d) et (e′), dans l'ordre tiré du lot)",
     M4_1483),
    ("M-5, case « version des modèles » de 13.2",
     "rien n'y dépend d'une réponse, d'un solde ni d'une dépense | session de relance |",
     "rien n'y dépend d'une réponse, d'un solde ni d'une dépense. " + M5 + " | session de relance |"),
    ("M-1, section « Contre-lecture », contre-lecture 10", M1_CL_ANCIEN, M1_CL_NEUF),
    ("contre-lecture 10 inscrite",
     " : non faite. À inscrire ici avant scellement : identifiant du contre-lecteur neuf, d'un "
     "autre modèle que le rédacteur, empreinte du texte relu, chemin et empreinte de son "
     "rapport, traitement de chaque remarque ; et, à part,",
     CL10_INSCRITE),
]

t47 = t46
for nom, ancien, neuf in REMPLACEMENTS:
    n = t47.count(ancien)
    if n != 1:
        arret(f"{nom} : ancien trouvé {n} fois")
    t47 = t47.replace(ancien, neuf)
    print(f"porté : {nom}")

l46, l47 = t46.split("\n"), t47.split("\n")
if l46[541:550] != l47[541:550]:
    arret("les huit règles ont bougé")
if hashlib.sha256("\n".join(l47[541:550]).encode()).hexdigest() != REGLES_SHA:
    arret("empreinte des huit règles")
avant = [i + 1 for i in range(541) if l46[i] != l47[i]]
if avant != [1, 3, 522]:
    arret(f"avant les règles, seules les lignes 1, 3 et 522 peuvent changer : {avant}")
for marque in ("⟦", "⟧"):
    if marque in t47:
        arret("marque " + marque)

sortie = RACINE / B47
if sortie.exists():
    arret(f"{B47} existe déjà (R12)")
sortie.write_text(t47, encoding="utf-8")
print("écrit", B47, hashlib.sha256(t47.encode()).hexdigest())
