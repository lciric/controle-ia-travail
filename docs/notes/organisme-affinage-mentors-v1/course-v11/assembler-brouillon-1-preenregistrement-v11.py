#!/usr/bin/env python3
"""Assemble le brouillon de la v11 à partir du texte scellé de la v10.

Toute ligne de la v10 qui n'est pas nommée ici est recopiée à l'octet près. Chaque remplacement de sous-chaîne exige que
l'ancienne chaîne figure exactement une fois dans la ligne visée ; sinon le programme s'arrête (aucun repli silencieux).
Usage : assembler_v11.py V10.md SORTIE.md DATE_UTC
"""
import hashlib
import sys

V10_SHA = "7fc71712136cf20d86f3603eb581bc61dd6bc35fcfe0650b230cf659674a3856"

src, dst, date_utc = sys.argv[1], sys.argv[2], sys.argv[3]
brut = open(src, "rb").read()
assert hashlib.sha256(brut).hexdigest() == V10_SHA, "la source n'est pas la v10 scellée"
L = brut.decode("utf-8").split("\n")
assert L[-1] == "" and len(L) == 251, len(L)   # 250 lignes, fin de fichier par un saut de ligne
lignes = {i + 1: t for i, t in enumerate(L[:-1])}
touchees = set()


def debut(n, prefixe):
    assert lignes[n].startswith(prefixe), (n, lignes[n][:80])


def remplacer_ligne(n, prefixe, texte):
    debut(n, prefixe)
    lignes[n] = texte
    touchees.add(n)


def sub(n, ancien, nouveau):
    assert lignes[n].count(ancien) == 1, (n, ancien[:70], lignes[n].count(ancien))
    lignes[n] = lignes[n].replace(ancien, nouveau)
    touchees.add(n)


def ajouter_fin(n, prefixe, texte):
    debut(n, prefixe)
    lignes[n] = lignes[n] + texte
    touchees.add(n)


apres = {}   # n -> lignes neuves insérées après la ligne n de la v10


def inserer_apres(n, *textes):
    apres.setdefault(n, []).extend(textes)


# ------------------------------------------------------------------------------------------------ en-tête
remplacer_ligne(1, "# Préenregistrement", "# Préenregistrement — course d'affinage des idées des mentors par l'organisme d'idéation — v11")

ETAT = ("- **État de ce fichier : brouillon 1 de la v11, non scellé comme préenregistrement.** Il porte des emplacements "
        "« EMPREINTE À INSCRIRE : <chemin> », « RÉFÉRENCE À INSCRIRE » et « RÉGLAGE À INSCRIRE », et une dernière section de "
        "points à trancher : les pièces qu'ils nomment (lanceur, essais, gabarits, configuration, commande et relais de "
        "Carbon, sonde d'Astra) sont en écriture ou en contre-lecture ailleurs. Le préenregistrement v11 n'existera, sous le "
        "nom `course-v11/preenregistrement-course-affinage-mentors-v11.md`, qu'une fois ces emplacements remplis de valeurs "
        "réelles, cette ligne et la dernière section retirées, le fichier scellé puis contre-lu (R1, R2, R12). Le compagnon "
        "`.sha256` de ce brouillon ne sert qu'à son transport (R6) ; aucun lanceur ne doit l'épingler.")

AUTEUR = ("- Auteur de la v11 : le rédacteur neuf que mandate la session de l'organisme (mandat "
          "`docs/notes/organisme-affinage-mentors-v1/course-v8/mandat-fable-preenregistrement-affinage-v8.md`, "
          "`0f7ddc5487459ecc637db8b29f0fbad6b47deda43d7fa47f79fec4a98a8f9ec2`, branche `lot/compte-organisme-v1` ; ce mandat "
          "nomme son modèle et son effort), sur l'accord de la mère et la ligne GO-2026-11-22-107 ; il n'a écrit ni le lanceur "
          "ni aucune version antérieure, et n'a lu aucune sortie de course ni aucune réponse de modèle. Textes des v7 à v10 : "
          "modèle L' ; texte de la v6 : session du compte organisme (modèle I). Le texte de la v10 est repris tel quel hors "
          "des points dits au différentiel v10 → v11, en fin de texte.")

DATE = ("- Date (UTC) de ce brouillon : " + date_utc + " (`date -u +%FT%TZ`) ; v10 : 2026-11-18T22:57:50Z. **Version 11** "
        "(R12) : les v1 à v10 restent en place, scellées, jamais lancées. Les v1 à v6 sont sur `lot/compte-organisme-v1` ; "
        "les v7 à v10 sont sur quatre branches de préparation du dépôt distant, non versées dans `lot/compte-organisme-v1` à "
        "sa tête `f3bd4d17` du 22 novembre : `prep/affinage-v7-compte-organisme-v1` (`2c31fc6f` ; v7, "
        "`720cbe81bbe5fe359ee8a8c814d374f3e52fac430351d8d29c6113ce9ae1d533`, contre-lue « Scellable. ») ; "
        "`prep/affinage-v8-compte-organisme-v1` (`dd139d7e` ; v8, "
        "`fb71f5006c102162eaa78cdbf3c0888627d413f08846239896e87d62c2350a20`, abandonnée avant contre-lecture) ; "
        "`prep/affinage-v9-compte-organisme-v1` (`74676380` ; v9, "
        "`b24755fccdbb58906a21461c1dde7108f96aab73e12922a4f6fcc13265a54938`, « Scellable après corrections. ») ; "
        "`prep/affinage-v10-compte-organisme-v1` (`6b704ede` ; **v10**, "
        "`course-v10/preenregistrement-course-affinage-mentors-v10.md`, "
        "`7fc71712136cf20d86f3603eb581bc61dd6bc35fcfe0650b230cf659674a3856`, contre-lue par le modèle K, verdict "
        "« Scellable. » : `course-v10/contre-lecture-preenregistrement-course-affinage-mentors-v10.md`, "
        "`c4a809bc5522f15b9fbb407787002149b4511bef9d63d8dac143045daae67f59`). La v10 n'a pas été jouée : Carbon y passe par le "
        "mode lot, qui n'a pas tenu le budget de réflexion dans deux courses d'auto-conception de l'organisme (registre des "
        "décisions de `main`, R-3446 et R-3584). La course d'affinage n'a jamais été jouée (R-3616 ; aucun dossier de cette course "
        "sous `runs/` sur `main`, sur `lot/compte-organisme-v1` ni sur la branche de la v10 ; aucune ligne de dépense de cette course au registre des dépenses de `main`, cherchée par les mots « affinage » et « mentors »).")

NUMERO = ("- **Numéro et base (écart au mandat, déclaré).** Le mandat et la ligne GO-2026-11-22-107 écrivent « v8 » et "
          "partent de la v6, en tenant qu'aucune v7 n'existe pour ce texte. Les noms « v8 » (préenregistrement, lanceur, "
          "essais, gabarits, devis) sont pris par des fichiers scellés d'autres empreintes sur les branches ci-dessus : cette "
          "version prend le premier numéro libre, **11** (vérifié sur `main`, sur `lot/compte-organisme-v1` et sur la branche "
          "de la v10). La v6 a été contre-lue « Scellable après corrections. » (deux majeurs), et les v7 à v10 portent ces "
          "corrections : ce texte part de la **v10**, dernier texte contre-lu « Scellable. ». Le périmètre de la ligne de GO "
          "ne change pas ; la mère note la correspondance des numéros au registre : RÉFÉRENCE À INSCRIRE.")

CHANGE = ("- **Ce que la v11 change, et rien d'autre** (les trois changements du mandat) : (1) **clé Claude** — "
          "`RR_ANTHROPIC_API_KEY_LUC` au lieu de `RR_ANTHROPIC_API_KEY_MINUIT`, avec la règle de départ et la garde de dépense "
          "propres à cette clé ; (2) **Astra** — `gpt-6.2-astra` au lieu de `gpt-6-astra`, clé déclarée `OPENAI_API_KEY_2`, "
          "prix relevés ; (3) **Carbon** — appel en flux sous la garde gelée des appels aux modèles de Google, au lieu de la "
          "commande par lot. S'y ajoutent leurs seules conséquences mécaniques : noms et chemins `v11`, configuration fixe "
          "v11, relevés et gabarits v11, correction d'un poste du devis, contre-lecteur. Hypothèse (aucune), prédiction "
          "(aucune), seuil (aucun), critères de lecture gelés, matière servie et retirée, plan, plan d'analyse, plafond "
          "d'arrêt (150 USD), budget et plafonds des étapes, plafonds de session, composition déclarée (deux Claude, Argon, "
          "Astra, Carbon ; pas de Kimi), orchestrateur épinglé : **inchangés**.")

debut(3, "- Auteur de la v10")
debut(4, "- Date (UTC) de la v10")
lignes[3] = ETAT + "\n" + AUTEUR
lignes[4] = DATE + "\n" + NUMERO + "\n" + CHANGE
touchees.update({3, 4})

ajouter_fin(5, "- Décision : N-072",
            " **v11** : exception déclarée à la règle « Claude par l'abonnement » (GO-2026-11-22-70) pour les appels Claude de "
            "cette course, faits par l'interface de programmation sur la clé `RR_ANTHROPIC_API_KEY_LUC` (GO-2026-11-22-107, "
            "échéance 2026-11-25 ; mot direct de Lazar, GO-2026-11-22-110 ; recharge automatique de la clé, "
            "GO-2026-11-22-111) ; clé « Minuit » sans crédit (R-4833) ; prolongation de GO-2026-11-18-14 au 2026-12-15 "
            "(GO-2026-11-22-80), sans effet sur l'échéance de l'exception ; « Astra » désigne `gpt-6.2-astra` (règle de Lazar, "
            "R-4900 ; prix relevés, R-4905) ; garde gelée des appels aux modèles de Google (GO-2026-11-21-71) et plafond de "
            "sortie de Carbon (GO-2026-11-21-47), règles permanentes de `CLAUDE.md` sur `main` ; « une panne technique n'est "
            "pas un résultat » (GO-2026-11-22-77). Lignes lues sur `main` au commit "
            "`435726aa57d2efa80f6eb966c720f11b6904b3f9` : `registres/go.md` "
            "(`f09e28de6eb833e7c14556be497797495623c6ed2ae8b66a8349e27b6d726311`), `registres/decisions.md` "
            "(`071060bba38169068afbfd9476ec4d056b1e8ff558261ffc753cfc1d6bf22a09`), `CLAUDE.md` "
            "(`605db83acc28c7fcc6d8d12de8edb41bcdb6ea7b37b717967d6fde29f5301960`).")

# ------------------------------------------------------------------------------------------------ pièces
remplacer_ligne(9, "  - configuration fixe de l'orchestrateur, **v9, inchangée en v10**",
                "  - configuration fixe de l'orchestrateur, **v11** : EMPREINTE À INSCRIRE : "
                "`docs/notes/organisme-affinage-mentors-v1/course-v11/configuration-course-affinage-mentors-v11.json` — la "
                "v9 (`docs/notes/organisme-affinage-mentors-v1/course-v9/configuration-course-affinage-mentors-v9.json`, "
                "`e7378f89ae39eacd169ff912526a8e998e4f01f0aba235eeaa0bf12e4b195d5d`, branche de la v10 ; elle-même la v6, "
                "`0ea89ed2f72ce2693e619eb10b6eecbd46725d4578b548a44c5a98b9bb1ded21`, au plafond de session des proposeurs "
                "près, 3,00 USD au lieu de 1,50) dont seuls changent : le nom de la clé Claude (`RR_ANTHROPIC_API_KEY_LUC`, à "
                "la clé du relais Claude et à celle des deux espèces Claude ; le crédit déclaré de 200 USD de la clé Minuit "
                "est retiré), le plafond du relais Claude (150 USD remplacé par le plafond de la part Claude, § Règle des "
                "clés), le bloc descriptif de Carbon (commande et relais de l'appel en flux), la version et le statut ; "
                "budget, plafonds de relais des étapes, plafonds de session (proposeur 3,00 ; aiguilleur 0,25 ; juge "
                "0,60 USD), espèces, aiguilleur, juges, graines et items du juge : **inchangés** ;")

remplacer_ligne(11, "  - commandes de Carbon et d'Astra",
                "  - commandes et relais des espèces hors Claude (copies de `main` ou de la branche, extraites hors dépôt et "
                "vérifiées à l'empreinte) : **Astra** — `commande_astra_v1.py` "
                "`986cf71efcac285899e76dd9b1d1c11bccbfd71dd7ae91b8bf3a4372567d7c71` (inchangée : le modèle et les prix sont "
                "ses arguments), relais compatible OpenAI `relais_kimi_v4.py` (empreinte à la ligne de la procédure, plus "
                "bas) ; **Argon** — `commande_argon_v3d.py` "
                "`46c91df41b77a6d4cb7f5141993fda4a894118b5dd4ad1e5ba21a17dc2d67e46` sous l'enveloppe `appel-argon-v5.sh` "
                "`37c0205e26f83cbdcdf5ad7f1e4094a21c7dcc70afb72d15ef0d260a770a132a`, relais Gemini v2 `relais_gemini_v2.py` "
                "`2b0043bcab8b3922c65a4008e719408c52781d7544064b5a29a23d7ef60c1aeb` (inchangés depuis la v6, sous la réserve "
                "du point « Argon » du § Espèces) ; **Carbon, v11** — commande de l'appel en flux : EMPREINTE À INSCRIRE : "
                "<chemin de la commande de Carbon en flux> ; son relais : EMPREINTE À INSCRIRE : <chemin du relais de "
                "Carbon> ; **retrait** : la commande Gemini par lot `commande_gemini_lot_v1.py` "
                "(`9484dce066514185dc1155d5c8dcff44b256fdf835b371b59ebdffa1d50bad75`) et le relais Gemini v4 "
                "`relais_gemini_v4.py` (`543e728d90e809c661fdc26f1e1b1a32b2e23128a7d09e3b5d16f851408a35b4`) ne sont plus "
                "employés ;\n"
                "  - garde commune des appels aux modèles de Google (**v11**) : `src/controle_ia/garde_google_v3.py` sur "
                "`main`, `923679b51cfc84b65ff7cfc65296378d08e6d4e64f6b427823d23ba24f4afe91` (règle : `CLAUDE.md` de `main`, "
                "« Appels aux modèles de Google » et « Appels à Carbon ») ;")

remplacer_ligne(12, "  - sonde d'Astra, **v2**",
                "  - sonde d'Astra, **v11** : EMPREINTE À INSCRIRE : <programme de la sonde d'Astra de cette version> ; sonde "
                "commune, qui contrôle le relais jeté avant l'appel : EMPREINTE À INSCRIRE : <programme de la sonde commune "
                "de cette version> — la sonde v2 (`scripts/sonde_astra_affinage_v2.py`, "
                "`1799449269e15661b92f2a45eaab95a22e3a766a1fdf10ec9a4648bbe92aebf7`) et la sonde commune v1 "
                "(`scripts/sonde_astra_courses_v1.py`, `d374d1071f4ef70b3604d97dc62e2f14103c440a166342b330d7a576d8b4c777`) "
                "portent le nom `gpt-6-astra` en dur : elles ne servent plus ; comme depuis la v7, le lanceur n'accepte le "
                "rapport de la sonde que lié, par son empreinte et par le PID du relais jeté, au rapport réussi de la sonde "
                "commune du même jour (un seul) ; rapports sous `course-v11/`, aux noms datés ; un rapport fait avec "
                "`gpt-6-astra`, ou un autre jour, ne vaut pas ;")

inserer_apres(20,
              "  - **devis, v11** : aucun devis neuf ; le devis v10 ci-dessus reste le devis cité. Un de ses postes ne décrit "
              "plus la course : Carbon y est compté au prix du lot, que l'appel en flux n'a pas ; il nomme aussi la clé Minuit "
              "là où cette version emploie la clé LUC. La correction est écrite au § Plafond, calculée des hypothèses du devis "
              "v10 lui-même ; le pire cas (150 USD) et les parts au pire des clés de Google (198) et d'OpenAI (48) ne changent "
              "pas ;")

remplacer_ligne(21, "  - lanceur : `scripts/lancer_course_affinage_mentors_v10.py`",
                "  - lanceur : `scripts/lancer_course_affinage_mentors_v11.py` (il épingle l'empreinte de ce "
                "préenregistrement : ce texte ne peut donc pas porter la sienne, qui est donnée par "
                "`course-v11/commandes-exactes-course-affinage-v11.md` et doit être citée par la contre-lecture ; EMPREINTE À "
                "INSCRIRE ici seulement si le lanceur v11 ne porte plus l'empreinte de ce texte dans son code : "
                "`scripts/lancer_course_affinage_mentors_v11.py`) ; ses essais : EMPREINTE À INSCRIRE : "
                "`tests/test_lancer_course_affinage_mentors_v11.py` ; gabarit de déclaration des relais : EMPREINTE À "
                "INSCRIRE : "
                "`docs/notes/organisme-affinage-mentors-v1/course-v11/declaration-relais-gabarit-course-affinage-v11.json` ; "
                "gabarits des relevés du jour : EMPREINTE À INSCRIRE : "
                "`docs/notes/organisme-affinage-mentors-v1/course-v11/releve-credits-gabarit-course-affinage-v11.json` et "
                "EMPREINTE À INSCRIRE : "
                "`docs/notes/organisme-affinage-mentors-v1/course-v11/releve-prix-claude-gabarit-course-affinage-v11.json` ;")

# ------------------------------------------------------------------------------------------------ espèces
sub(51, "les deux espèces Claude de la configuration, **obligatoires** (aucun départ sans elles) ;",
    "les deux espèces Claude de la configuration, **obligatoires** (aucun départ sans elles ; **v11** : appelées par "
    "l'interface de programmation sur la clé LUC, § Règle des clés) ;")
sub(51, "Astra si sa sonde a réussi ;", "Astra (**v11** : `gpt-6.2-astra`, règle de Lazar, R-4900) si sa sonde a réussi ;")
sub(51, "**vide en v7 à v10**", "**vide en v7 à v11**")

remplacer_ligne(53, "- Une espèce sans relais déclaré, ou arrêtée en course, est une **lacune rapportée**",
    "- Une espèce sans relais déclaré, ou arrêtée en course, est une **lacune rapportée**, jamais compensée. **Carbon, détail "
    "(v11)** (déclarée depuis la v5, R-3274) : modèle `gemini-4-carbon`, rôle de proposeur seulement, clé de Google partagée "
    "avec Argon. **Le mode lot est retiré.** De la v5 à la v10, Carbon passait par la commande Gemini par lot et le relais "
    "Gemini v4 ; le fournisseur n'y tient pas le budget de réflexion (fait observé dans deux courses d'auto-conception, "
    "R-3446 et R-3584), et la limite de sortie de Carbon hors flux (32 768 jetons, table de la garde commune) ne laisse pas 16 000 "
    "jetons de texte au-delà de la plus forte réflexion observée (20 696 jetons). En v11, chaque appel de Carbon est **un "
    "appel en flux**, par la commande et le relais épinglés par le lanceur (le mandat de cette version les dit ceux de la "
    "passe X de la course « nouvelles attaques » ; empreintes aux pièces), **sous la garde gelée des appels aux modèles de "
    "Google** (`CLAUDE.md` de `main`, « Appels aux modèles de Google », GO-2026-11-21-71, et « Appels à Carbon », "
    "GO-2026-11-21-47 ; garde commune `garde_google_v3.py`, employée ou reproduite par la commande, essais et mutations à "
    "l'appui). **Avant l'envoi**, une vérification par programme refuse l'appel, et rien ne part, si : le réglage de "
    "réflexion n'est pas explicite dans le corps (le niveau le plus haut admis pour Carbon, `high` dans la table de la "
    "garde, pensées demandées en retour) ; le plafond de sortie n'atteint pas la provision de réflexion plus 16 000 jetons "
    "de texte, ou dépasse la limite de sortie de Carbon en flux (65 536 jetons dans la table de la garde) ; une limite de "
    "mots demandée par la consigne ne tient pas dans le plafond de texte. **Après la réponse** : zéro jeton de pensée, fin "
    "en `MAX_TOKENS`, `SAFETY`, `RECITATION` ou autre refus du fournisseur, fin autre que `STOP`, ou texte vide = **défaut "
    "journalisé, jamais une réponse** ; la commande rend alors un échec à l'orchestrateur, aucun texte n'est servi comme "
    "carte, et l'échec compte pour A3 et A14. Aucun repli silencieux (R5) : le seul repli que la garde connaît (un renvoi "
    "unique au budget de réflexion prévu quand le fournisseur refuse le niveau) est écrit au journal s'il est fait. "
    "**Réglages exacts** (provision de réflexion, plafond de sortie, délais, bornes du relais) : RÉGLAGE À INSCRIRE, ceux du "
    "gabarit de déclaration v11, que le lanceur refuse de voir changés et écrit au manifeste de départ. **Ce que ce texte "
    "fixe quels que soient ces réglages** : (a) le pire cas d'un appel, au prix plein (8,3 et 41,5 USD par million de "
    "jetons, bornes hautes de R-3271 ; plus de facteur de lot), tient sous le plafond de session d'un proposeur (3,00 USD) "
    "— au plafond de sortie le plus haut que la garde admet et sur l'entrée gardée la plus longue de la course (2 618 "
    "jetons, devis v10, § 1), il vaut (2 618 × 8,3 + 65 536 × 41,5) / 10⁶ = 2,7415 USD, dans la lecture où la réflexion "
    "compte dans le plafond de sortie (documentation du fournisseur, retenue depuis la v9) ; (b) la part au pire de Carbon "
    "reste 48 USD (16 × 3,00) ; (c) la durée maximale d'un appel, marge de 30 s comprise, reste sous le délai de "
    "l'adaptateur de commande de l'orchestrateur épinglé (1 800 s, écrit en dur) et sous A3 (1 800 s) ; (d) le lanceur "
    "refuse le départ si la commande de Carbon n'est pas la commande épinglée, si l'un de ses arguments diffère de ceux du "
    "gabarit, ou si ses réglages ne passent pas la garde sur l'entrée la plus longue et sur la plus courte de la course. "
    "**Risque dit** : la réflexion de Carbon en flux sur les consignes de l'affinage n'est pas mesurée ; un appel dont la "
    "réflexion et le texte dépassent ensemble le plafond de sortie finit en `MAX_TOKENS` (défaut) ; A3 (trois échecs "
    "consécutifs) peut alors arrêter Carbon et A14 marquer l'étape « non mesurée (technique) ». **Astra (v11)** : « Astra » "
    "désigne `gpt-6.2-astra` (règle de Lazar, R-4900), à la place de `gpt-6-astra` ; clé d'OpenAI injectée par le secret de "
    "réseau de l'environnement d'exécution, déclarée sous le nom `OPENAI_API_KEY_2` ; prix relevés : 8 et 40 USD par "
    "million de jetons d'entrée et de sortie (R-4905 ; 16 et 60 au-delà de 272 000 jetons d'entrée, palier hors d'atteinte "
    "ici : le corps d'un appel d'Astra de cette course fait 8 011 octets au plus, devis v10, § 2) ; commande épinglée "
    "inchangée, arguments exacts du gabarit de déclaration v11 (modèle, prix, sortie maximale, délai) ; relais au plafond "
    "égal à sa part au pire (48 USD) et aux prix de la commande. Astra n'est déclarée que si une **sonde** — un appel "
    "trivial par sa commande épinglée, signalé, 0,05 USD au plus, par un relais jeté — a réussi le jour même avant la porte "
    "à blanc (R-3273), **avec le modèle, la clé et les prix de cette version**, le relais de la course étant neuf ; sinon "
    "Astra est absente, sans brûler la tentative (le motif et le mot de la mère sont écrits dans la déclaration). Kimi, "
    "s'il est autorisé par la mère : déclaré seulement si son relais l'est et si la règle de part le permet.\n"
    "- **Argon et la garde gelée (v11, point à trancher avant le scellement).** La garde gelée vaut pour tout envoi à un "
    "modèle de Google, donc aussi pour Argon, proposeur et second juge de cette course ; le mandat de cette version ne "
    "nomme que Carbon. Deux faits lus : (1) la commande d'Argon épinglée depuis la v6 (`commande_argon_v3d.py`, sous "
    "l'enveloppe `appel-argon-v5.sh`) pose un budget de réflexion (8 192 jetons par défaut) sans demander les pensées en "
    "retour, abaisse le plafond de sortie à ce que le plafond de session paie sans plancher de 16 000 jetons de texte, et "
    "ne lit pas une réponse sans jeton de pensée comme un défaut : telle quelle, elle ne tient pas la règle ; (2) au prix de "
    "sortie compté pour Argon (41,5 USD par million de jetons), 16 000 jetons de texte coûtent 0,664 USD : sous le plafond "
    "de session d'un juge (0,60 USD), aucun appel de juge d'Argon ne peut à la fois tenir la règle et son plafond. Rien "
    "n'est changé ici à Argon, à ses réglages ni au plafond de session des juges : la suite (commande d'Argon mise sous la "
    "garde et plafond de session des juges relevé par la configuration v11, ou autre décision) est un nœud — RÉFÉRENCE À "
    "INSCRIRE — et ce texte n'est pas scellable tant qu'il n'est pas tranché.")

# ------------------------------------------------------------------------------------------------ sorties, mesures, bonne fin
sub(68, "/home/user/sorties-course-affinage-mentors-v10/<id>/sortie/", "/home/user/sorties-course-affinage-mentors-v11/<id>/sortie/")
sub(69, "runs/<id>-course-affinage-mentors-v10/", "runs/<id>-course-affinage-mentors-v11/")
sub(73, "coût réel par relais et par rôle,",
    "coût réel par relais et par rôle (**v11** : la part Claude est en outre relevée au fil de l'eau sur l'état de son "
    "relais),")
sub(73, "cinq espèces : 41,136 USD sans marge ; devis v10, chiffres du v9)",
    "cinq espèces : 41,136 USD sans marge ; devis v10, chiffres du v9 ; **v11** : Carbon au prix plein, 0,9970 USD par appel "
    "— cinq espèces : 49,112 USD sans marge, § Plafond)")
sub(78, "rapporté tel quel, sans relance (seuils au § Plafond). ",
    "rapporté tel quel, sans relance (seuils au § Plafond). **v11** : un arrêt par la garde de la part Claude (plafond de la "
    "part Claude atteint, code 5 du lanceur ; § Règle des clés) est possible aussi : il interdit la bonne fin et se rapporte "
    "tel quel, sans relance. ")

# ------------------------------------------------------------------------------------------------ liste d'arrêt, avant le départ
debut(82, "- **Avant le départ** (lanceur, code 2, rien n'est appelé)")
sub(82, "refusé par la lecture de l'orchestrateur ; relevé du prix Claude du jour",
    "refusé par la lecture de l'orchestrateur ; **v11** : ligne de l'exception GO-2026-11-22-107 (appels Claude par "
    "l'interface de programmation sur la clé LUC) absente, hors période ou révoquée ; relevé du prix Claude du jour")
sub(82, "variable Minuit vide ou faite d'espaces ;", "variable de la clé LUC vide ou faite d'espaces ;")
ANCIEN_CARBON = lignes[82][lignes[82].index("**v8, commande de Carbon** :"):lignes[82].index("arguments d'une commande de porte qui ne recoupent pas")]
assert ANCIEN_CARBON.startswith("**v8, commande de Carbon** : option de prix, de facteur du lot") and ANCIEN_CARBON.rstrip().endswith("ou pire cas d'un appel au-dessus du plafond de session ;"), ANCIEN_CARBON[-90:]
sub(82, ANCIEN_CARBON,
    "**v11, commande de Carbon en flux** (les gardes v8 et v9 de la commande par lot sont retirées avec elle) : appel qui ne "
    "serait pas en flux ; réglage de réflexion absent du corps ou autre que le niveau le plus haut admis ; pensées non "
    "demandées en retour ; plafond de sortie sous la provision de réflexion plus 16 000 jetons de texte, ou au-delà de la "
    "limite de Carbon en flux ; limite de mots de la consigne qui ne tient pas dans le plafond de texte (garde gelée des "
    "appels aux modèles de Google, contrôlée sur l'entrée la plus longue et sur la plus courte de la course) ; durée "
    "maximale de la commande plus 30 s au-delà de 1 800 s (adaptateur de l'orchestrateur, A3) ; pire cas d'un appel "
    "au-dessus du plafond de session (3,00 USD) ; ")
sub(82, "Claude, plafond 150 ; Astra (et Kimi)",
    "Claude, plafond égal, au centime, au plafond de la part Claude calculé du relevé des crédits (**v11** ; 150 en v7 à "
    "v10) ; Astra (et Kimi)")
ANCIEN_RELAIS_CARBON = lignes[82][lignes[82].index("Carbon, `--max-lots` ≥ 20 et `--max-appels` ≥ 40"):lignes[82].index("borne absente des arguments, ou différente dans l'état, refusée")]
assert ANCIEN_RELAIS_CARBON.rstrip().endswith("dans l'état) ;"), ANCIEN_RELAIS_CARBON
sub(82, ANCIEN_RELAIS_CARBON,
    "Carbon (**v11**, relais de l'appel en flux ; les bornes de lots et de relevés du relais Gemini v4 sont retirées avec "
    "lui), bornes d'appels au moins égales à 16 cases plus 4 de marge, comptes de jetons compris s'il en fait (RÉGLAGE À "
    "INSCRIRE : bornes exactes du relais de Carbon, celles du lanceur v11) ; ")
sub(82, "pour Carbon sans « lots_crees »)", "pour Carbon sans les compteurs de son relais)")
sub(82, "**v7** : rapport v2 non lié, par son empreinte et par le PID du relais jeté, à un rapport réussi de la sonde commune du même jour (un seul) ;",
    "**v7** : rapport de la sonde non lié, par son empreinte et par le PID du relais jeté, à un rapport réussi de la sonde "
    "commune du même jour (un seul) ; **v11** : sonde faite avec un autre modèle que `gpt-6.2-astra`, une autre variable de "
    "clé ou d'autres prix que ceux de cette version ;")
sub(82, "ne se dit pas du modèle K, dit n'avoir pas relu,",
    "ne dit pas son modèle sous le libellé exigé (**v11** : un Opus neuf ; modèle K en v2 à v10), dit n'avoir pas relu,")
sub(82, "variable `RR_ANTHROPIC_API_KEY_MINUIT` absente ; relais Claude sur une autre clé, clé Rigaud déclarée, clé Claude sur un autre relais ; course déjà lancée en v1 à v10 ;",
    "variable `RR_ANTHROPIC_API_KEY_LUC` absente ; relais Claude sur une autre clé que LUC, clé Rigaud déclarée, clé Claude "
    "sur un autre relais ; course déjà lancée en v1 à v11 ;")
sub(82, "(vide en v7 à v10) ;", "(vide en v7 à v11) ;")
sub(82, "solde illisible sans dispense R-3237 ou d'une clé non dispensable ;",
    "solde illisible sans dispense R-3237 ou d'une clé non dispensable ; **v11, clé LUC** : lecture du solde par Lazar "
    "absente du relevé, d'un autre jour que le départ, sans heure lisible ou sans la ligne du registre de `main` qui la "
    "porte ; recharge automatique déclarée au-delà de 40 euros ; réserves absentes (une liste vide s'écrit) ou mal "
    "formées ; écrit de la mère sur les autres dépenses de la clé non cité ; plafond de la part Claude sous le plancher de "
    "20,65 USD (code 3) ;")

sub(82, "`--max-appels` et `--max-lots` suffisants,", "`--max-appels` suffisants (et `--max-lots`, de la v5 à la v10),")
sub(82, "**48 USD = 16 × 3,00** en v9 et v10 ; 24 en v7 et v8)", "**48 USD = 16 × 3,00** en v9 à v11 ; 24 en v7 et v8)")
sub(82, "(3,00 en v9 et v10), prix de l'état égaux", "(3,00 en v9 à v11), prix de l'état égaux")
sub(115, "**150 + 48 = 198 USD en v9 et v10**", "**150 + 48 = 198 USD en v9 à v11**")

inserer_apres(86,
    "- **Pendant, en plus (v11) — garde de la part Claude** : le lanceur relève l'état du relais Claude au moins une fois par "
    "minute (compte de la part Claude au fil de l'eau) ; au premier appel refusé par ce relais parce que le plafond de la "
    "part Claude est atteint (statut 402 du relais) → arrêt de la course par le lanceur (signal à l'orchestrateur par son "
    "PID, arrêt propre, manifestes écrits, **code 5**), ce qui a été fait est écrit, et une alerte scellée pour la mère "
    "(`alerte-arret-part-claude.json`), qui prévient Lazar ; détail au § Règle des clés, « Clé LUC ». Cette garde est "
    "essayée sur un cas sain (aucun refus : la course va à son terme) et sur un artefact (un refus pour plafond planté dans "
    "l'état et le journal d'un relais factice : arrêt, code 5, alerte), R5.")
ajouter_fin(87, "- **Après** : cumul lu au-dessus de 150 USD",
            " **v11** : dépense du relais Claude lue au-dessus du plafond de la part Claude (dépassement du relais, § Règle "
            "des clés) → écrite au manifeste de fin et signalée à la mère.")
sub(88, "(v7, inchangés en v8 à v10 ; distincts de ceux de l'orchestrateur)", "(v7, inchangés en v8 à v11 ; distincts de ceux de l'orchestrateur)")
sub(88, "3 alerte de crédit avant le départ ;", "3 alerte de crédit avant le départ (**v11** : dont un plafond de la part Claude sous son plancher) ;")
sub(88, "5 arrêt par la garde de crédit ;", "5 arrêt par la garde de crédit (**v11** : ou par la garde de la part Claude) ;")

# ------------------------------------------------------------------------------------------------ plafond
sub(92, "`course-v10/releve-prix-claude-course-affinage-v10.json`", "`course-v11/releve-prix-claude-course-affinage-v11.json`")
ajouter_fin(92, "**150 USD**, plafond d'arrêt de toute la course (GO-2026-11-18-14).",
    " **v11** : aucun devis neuf ; le devis v10 reste le devis cité, et un de ses postes ne décrit plus la course. Carbon y "
    "est compté au prix du lot (0,4985 USD par appel estimé, facteur 0,5) ; l'appel en flux est au prix plein : avec les "
    "hypothèses du devis v10 (§ 2 : réflexion 20 000 jetons, réponse 3 500, entrée 2 618), (2 618 × 8,3 + 23 500 × 41,5) / "
    "10⁶ = 0,9970 USD par appel, soit 16 × 0,4985 = 7,98 USD de plus ; cinq espèces : **49,11** USD sans marge (41,136 + "
    "7,976), **54,02** avec ; base de l'écart au devis : 49,112. Le « haut », convention et non borne, monte d'au plus "
    "16 × (2,7415 − 2,5715) = 2,72 USD avant marge (pire cas d'un appel de Carbon au plafond de sortie le plus haut de la "
    "garde, § Espèces). Astra : le devis compte tout proposeur hors Claude à un prix par appel supposé (0,276 USD), qu'il ne "
    "tire pas d'un prix par jeton ; les prix relevés de `gpt-6.2-astra` (8 et 40 USD par million, R-4905) sont plus bas que "
    "ceux de la commande en v10 (10 et 50) : aucun chiffre n'est changé de ce fait. **Pire cas 150**, parts au pire de la "
    "clé de Google (198) et de la clé d'OpenAI (48) : inchangés ; part au pire de la clé Claude : le plafond de la part "
    "Claude, au plus 150 (paragraphe suivant le bloc des plafonds des étapes, et § Règle des clés).")
debut(101, "Ce régime suppose une proposition bien au-delà de son haut")
inserer_apres(101, "",
    "**Plafond de la part Claude (v11).** La part Claude de la course (deux proposeurs, aiguilleur, premier juge) a, en plus, "
    "son propre plafond, plus bas : le plus petit de 150 USD et des quatre cinquièmes de ce que la clé LUC peut couvrir, "
    "recharge automatique comprise (§ Règle des clés, « Clé LUC »). Il est tenu par le relais Claude, non par "
    "l'orchestrateur ; il ne change ni S17, ni les plafonds des étapes, ni les seuils ci-dessus, qui restent calculés sur "
    "150 USD. Quand il est atteint, les appels Claude sont refusés par le relais et le lanceur arrête la course (code 5, "
    "alerte) : une étape peut donc être interrompue alors que son plafond dur n'est pas épuisé. Repères, sans valeur de "
    "borne : part Claude estimée 20,65 USD, haut 74,62 USD (devis v10, § 4) ; cumul estimé de la part Claude après la "
    "proposition 8,69 USD, après l'aiguillage 14,14 USD (prix par appel du devis v6, § 2, marge de 10 % comprise : "
    "(16 × 0,141 + 16 × 0,3525) × 1,1, puis + 160 × 0,031 × 1,1).")

# ------------------------------------------------------------------------------------------------ règle des clés
sub(105, "(R-3228) :", "(R-3228 ; **v11** : GO-2026-11-22-107) :")
remplacer_ligne(109, "| Claude (un seul relais) |",
                "| Claude (un seul relais) | les deux espèces Claude de proposeurs, l'aiguilleur, le premier juge | "
                "`RR_ANTHROPIC_API_KEY_LUC` (**v11** ; `RR_ANTHROPIC_API_KEY_MINUIT`, 200 USD déclarés, en v2 à v10) |")
remplacer_ligne(111, "| Kimi, Astra, Carbon (si actifs) |",
                "| Astra (si active) | proposeur Astra | `OPENAI_API_KEY_2` (**v11** ; clé injectée par le secret de réseau de "
                "l'environnement d'exécution, nom de variable seul) |\n"
                "| Kimi, Carbon (si actifs) | proposeur de l'espèce | nom déclaré par la session d'exécution dans la "
                "déclaration des relais |")
remplacer_ligne(113, "`RR_ANTHROPIC_API_KEY_RIGAUD` (124 USD, R-3224) **n'est pas employée**",
    "**v11** : tous les appels Claude de la course passent par l'interface de programmation, sur la clé "
    "`RR_ANTHROPIC_API_KEY_LUC` : c'est une **exception déclarée** à la règle « Claude par l'abonnement » "
    "(GO-2026-11-22-70), accordée par Lazar pour cette course (GO-2026-11-22-107, échéance 2026-11-25 ; mot direct, "
    "GO-2026-11-22-110). `RR_ANTHROPIC_API_KEY_MINUIT` est sans crédit (R-4833) et **n'est plus employée** ; "
    "`RR_ANTHROPIC_API_KEY_RIGAUD` (124 USD, R-3224) **n'est pas employée** et garde son reste. Le lanceur **s'arrête au "
    "départ** si la variable `RR_ANTHROPIC_API_KEY_LUC` est absente de son environnement, vide ou faite d'espaces (test du "
    "nom et de la non-vacuité, la valeur n'étant jamais lue ni écrite) ; il **refuse** un relais Claude déclaré sur une "
    "autre clé que LUC, la clé Rigaud sur quelque relais que ce soit, et toute clé de la famille Claude sur un relais d'un "
    "autre fournisseur. Le manifeste de départ écrit la clé de chaque espèce et de chaque rôle interne.")
ajouter_fin(115, "**Règle de clé par part (R-3237, point 1)**",
            " **v11** : cette règle vaut telle quelle pour les clés de Google et d'OpenAI ; pour la clé LUC, la part au pire "
            "est le plafond de la part Claude, et la règle de départ est celle du paragraphe « Clé LUC » ci-dessous.")
sub(117, "Aucune autre clé ne part sans solde lisible (Minuit : compté au prix relevé si l'interface ne le rend pas).",
    "Aucune autre clé ne part sans solde lisible (**v11** : la clé LUC, que seule la console de facturation rend, part sur la "
    "lecture de Lazar, paragraphe « Clé LUC » ; le compte « au prix relevé » de la clé Minuit, v2 à v10, est retiré avec "
    "elle).")

CLE_LUC = [
    "",
    "**Clé LUC : couverture, plafond de la part Claude, compte au fil de l'eau (v11 ; GO-2026-11-22-107, -110 et -111).** "
    "Trois faits fixent la règle. Le solde de la clé LUC n'est pas lisible par l'interface de programmation : Lazar le lit à "
    "la console de facturation avant le départ (GO-2026-11-22-110). La clé est en compte payant à recharge automatique, et "
    "Lazar a dit la recharge encore disponible « jusqu'à 40 euros » (GO-2026-11-22-111). La clé sert aussi d'autres "
    "chantiers, et ses soldes lus le 22 novembre sont très en dessous des 150 USD de la part au pire d'un relais qui tient "
    "l'aiguilleur et un juge (24,48 USD, GO-2026-11-22-72 ; 6,20 USD, GO-2026-11-22-73). Appliquée à LUC, la règle de la "
    "v10 (reste lu au-dessus de 150 USD, sinon refus) interdirait donc tout départ. Elle est remplacée, **pour cette clé "
    "seulement**, par un départ **sous un plafond plus bas de la seule part Claude**, sans toucher au plafond d'arrêt de "
    "150 USD ni à rien de ce que la course sert ou mesure :",
    "",
    "1. **Couverture déclarée.** Le relevé des crédits du jour porte, pour la clé LUC : (a) le **solde lu par Lazar** à la "
    "console, en dollars, l'heure de cette lecture, et la ligne du registre de `main` où la mère l'a inscrite — la lecture "
    "est du jour du départ, et le relevé s'écrit au plus près du lancement, juste avant le relais Claude (point 2) et la déclaration des relais ; (b) la **recharge automatique encore "
    "disponible** à cette heure, en euros : au plus 40 (GO-2026-11-22-111), un montant plus haut demandant une version "
    "suivante ; (c) les **réserves** : toute autre dépense prévue ou en cours sur la même clé d'ici la fin de la course, "
    "chacune avec son montant au pire en dollars, son objet et sa référence — une liste vide s'écrit, elle ne s'omet pas ; "
    "(d) la référence de l'**écrit de la mère** qui dit que, de l'heure de la lecture à la fin de la course, aucune autre "
    "dépense que ces réserves ne passe sur la clé LUC. La **couverture** est : solde lu + recharge disponible − somme des "
    "réserves. La recharge, dite en euros, est comptée **au pair** (un euro compté un dollar) : ce texte ne relève aucun "
    "cours de change (limite au point 6). Noms des champs : ceux du gabarit du relevé des crédits v11.",
    "2. **Plafond de la part Claude.** Le plus petit de 150 USD et des **quatre cinquièmes de la couverture**, tronqué au "
    "centime : un cinquième de ce que la clé peut couvrir est gardé (le cinquième des versions précédentes, appliqué ici à la couverture, faute de crédit déclaré). Le relais Claude est lancé **après** le relevé, avec ce plafond pour plafond en "
    "dollars, et le lanceur refuse le départ si le plafond lu par PID et dans l'état du relais en diffère d'un centime. Ce plafond est la part au pire de la clé LUC dans cette course, au dépassement du relais près (point 6). Il borne la seule part Claude (deux proposeurs, "
    "aiguilleur, premier juge) ; le plafond d'arrêt de 150 USD, les plafonds des étapes et les plafonds de session ne "
    "changent pas, et l'orchestrateur ne connaît pas ce plafond : pour lui, un appel que le relais refuse est un appel en "
    "échec du rôle (A3, A14) — lecture à confirmer sur l'orchestrateur épinglé par l'essai du lanceur.",
    "3. **Plancher de départ.** Pas de départ (code 3, alerte écrite pour la mère, qui prévient Lazar) si le plafond de la "
    "part Claude est sous **20,65 USD**, l'estimation de la part Claude de la course, marge de 10 % comprise (devis v10, "
    "§ 4), soit une couverture sous 25,8125 USD : sous ce plancher, la tentative unique serait consommée sans pouvoir finir, "
    "selon la propre estimation de la course. Entre ce plancher et le haut de la part Claude (74,62 USD, convention du "
    "devis, non une borne), le départ est permis et l'arrêt du point 5 reste possible : c'est le risque que cette règle "
    "accepte, écrit ici.",
    "4. **Compte au fil de l'eau.** Pendant la course, le lanceur lit l'état du relais Claude (dépense, montant engagé, "
    "appels, refus) au moins une fois par minute et écrit chaque lecture dans un journal du run (montants et comptes, jamais "
    "un contenu). La **part Claude** est la dépense comptée par ce relais, à son barème, que le lanceur a vérifié égal au "
    "relevé du prix Claude du jour.",
    "5. **Arrêt et message.** Au **premier appel refusé par le relais Claude parce que son plafond est atteint** (statut 402 "
    "du relais, écrit à son journal) — la part Claude a alors atteint ce que la clé LUC peut couvrir avec la recharge, "
    "cinquième gardé —, le lanceur arrête la course : signal d'arrêt à l'orchestrateur par son PID, arrêt propre, "
    "manifestes écrits, **code 5** ; il écrit et scelle une alerte pour la mère (`alerte-arret-part-claude.json` : "
    "couverture déclarée, plafond, dépense et montant engagé lus, appels, étape en cours, ce qui a été fait), qui prévient Lazar. Si l'orchestrateur s'arrête de lui-même avant que le lanceur ait lu ce refus (A3 : trois appels refusés de suite arrêtent le rôle), le lanceur relit l'état et le journal du relais à la fin : un refus pour plafond y vaut le code 5 et l'alerte, par la priorité des codes (4, puis 5, puis 6). Rien n'est relancé ; les cartes déjà produites sont rapportées ; la bonne fin n'est pas atteinte. C'est une "
    "cause technique déclarée (crédit) au sens de la règle « une panne technique n'est pas un résultat » "
    "(GO-2026-11-22-77) : l'essai se rapporte tel quel, avec son issue codée, et une relance demande une version suivante "
    "et une décision nommée.",
    "6. **Ce que cette garde ne voit pas.** (i) Un refus du fournisseur faute de crédit **avant** ce plafond (clé vidée par "
    "une dépense non déclarée, recharge qui ne joue pas) : le relais Claude épinglé relaie le refus sans en lire le motif ; "
    "aucun arrêt par le lanceur n'est promis sur ce motif ; la protection est celle de l'orchestrateur (A3 : trois échecs "
    "consécutifs arrêtent le rôle ; A14), la bonne fin n'est pas atteinte, et le manifeste de fin écrit le compte des "
    "appels du relais Claude par statut. Selon le registre (compte payant à recharge, GO-2026-11-22-48 ; clé Minuit "
    "refusée faute de crédit, R-4833), au-delà du solde et de la recharge le fournisseur refuse les appels ; ce texte ne le "
    "vérifie pas autrement. (ii) Le dépassement du relais : il réserve un montant par appel avant de l'envoyer (0,40 USD, "
    "défaut du programme épinglé) et règle au coût lu ; sa dépense peut dépasser son plafond d'au plus (coût d'un appel − "
    "réserve) par appel en vol quand le plafond est atteint ; le dépassement lu dans son état est écrit au manifeste de "
    "fin. (iii) Le change : si un euro vaut moins d'un dollar, la couverture réelle est plus basse que la couverture "
    "comptée, de 40 × (1 − cours) dollars au plus (cours : dollars pour un euro). Le cinquième gardé est la marge de prudence pour (ii) et (iii) : il vaut "
    "au moins 5,16 USD au plancher et couvre à lui seul l'écart de change tant qu'un euro vaut au moins 0,88 dollar ; ce "
    "n'est pas une garantie chiffrée pour la somme des deux.",
    "",
    "Condition de GO-2026-11-18-14 (« Lazar prévenu avant qu'une clé n'atteigne zéro ») : pour la clé LUC, elle est tenue "
    "par l'alerte du plancher avant le départ, par le cinquième gardé et par l'alerte de l'arrêt ; elle suppose l'écrit de "
    "la mère du point 1 (d) : une dépense d'un autre chantier sur LUC pendant la course échappe à ce texte.",
]
inserer_apres(117, *CLE_LUC)

sub(119, "(programme épinglé par la procédure, variable de clé, port, plafond : 150 pour Claude)",
    "(programme épinglé par la procédure, variable de clé, port, plafond : celui de la part Claude, au centime, **v11** ; 150 "
    "en v4 à v10)")
sub(119, "(garde de calcul chargée, variable Minuit présente)", "(garde de calcul chargée, variable de la clé LUC présente)")

remplacer_ligne(121, "Relevé, avant la course, du crédit et du reste de **chaque clé employée**",
    "Relevé, avant la course, du crédit et du reste de **chaque clé employée** (fichier du jour, scellé, écrit par la session "
    "d'exécution depuis l'interface de facturation ou le compteur ; noms de clé seulement, jamais une valeur). Un crédit "
    "« non lisible » arrête le départ, sauf dispense écrite de la mère pour cette clé (Argon, Astra, Carbon) ; **v11** : la "
    "clé LUC n'est ni lisible par programme ni dispensée, elle part sur la couverture déclarée du paragraphe « Clé LUC ». Un "
    "reste sous **un cinquième du crédit** ou sous **la part au pire de la clé** écrit une alerte pour la mère (fichier et "
    "sortie) et arrête le départ (code 3) ; ainsi une clé au solde lisible dont le reste dépasse sa part au pire ne peut pas "
    "atteindre zéro pendant la course (à égalité exacte du reste et de la part, le pire cas la laisse à zéro : le départ "
    "est alors refusé), et Lazar est prévenu avant. Après la course : coût réel par relais, reste estimé par clé, alerte si "
    "un reste estimé passe sous les mêmes seuils, confirmation par l'interface de facturation à faire par la session "
    "d'exécution (sinon, reste compté au barème du relais, écrit comme tel) ; **v11**, clé LUC : reste estimé = couverture "
    "déclarée moins la part Claude comptée par le relais, à confirmer par une lecture de Lazar à la console. Alerte après la "
    "course si un reste estimé passe sous un cinquième du crédit (**v11**, clé LUC : sous un cinquième de la couverture "
    "déclarée), et, pour Kimi, sous 12,56 USD (ce qu'exige la course Kimi de la relance).")

# ------------------------------------------------------------------------------------------------ contre-lecture
remplacer_ligne(142, "À faire avant tout lancement, par un contre-lecteur neuf d'un autre modèle (**modèle K**)",
    "À faire avant tout lancement, par un contre-lecteur neuf d'un autre modèle que le rédacteur — **v11** : un Opus neuf, "
    "puis la vérification des corrections par le même contre-lecteur (pièce de classe A ; règles « Qui conçoit » et "
    "« Allègement de la procédure » de `CLAUDE.md` sur `main`) —, qui n'a écrit ni ce préenregistrement ni le lanceur (R2). "
    "Son rapport est écrit et scellé à "
    "`docs/notes/organisme-affinage-mentors-v1/course-v11/contre-lecture-preenregistrement-course-affinage-mentors-v11.md` ; "
    "il cite en entier l'empreinte de ce préenregistrement et celle du lanceur v11, dit son modèle sous le libellé que le "
    "lanceur v11 exige (RÉGLAGE À INSCRIRE : ce libellé), et porte une section « Verdict » dont la **première ligne est "
    "exactement** « Scellable. » (en gras ou non) ; tout autre libellé, ou un rapport qui dit n'avoir pas relu (« je n'ai "
    "pas relu », « non relu », « sans relecture »…), est refusé par le lanceur. Une correction demandée donne une nouvelle "
    "version de ce préenregistrement et du lanceur (R12). L'acte de gel écrit par le lanceur au lancement (empreintes du "
    "préenregistrement et de la contre-lecture, verdict lu) est la spécification servie à l'orchestrateur.")

# ------------------------------------------------------------------------------------------------ différentiel et points ouverts
DIFF = [
    "",
    "## Différentiel v10 → v11",
    "",
    "Mandat de la session de l'organisme (`0f7ddc54…`) sur la ligne GO-2026-11-22-107 : trois changements, et leurs "
    "conséquences mécaniques. **Inchangés** : objet, question, absence d'hypothèse, de prédiction et de seuil ; ce qui est "
    "servi et retiré ; plan ; ce qui est mesuré et ne l'est pas (à deux précisions de coût près, points 4 et 7) ; plan d'analyse et critères de lecture gelés ; règles de "
    "N-073 ; ce que la course ne dit pas ; plafond d'arrêt 150 USD (GO-2026-11-18-14) ; budget, plafonds de relais et "
    "plafonds durs des étapes ; plafonds de session ; composition déclarée (deux Claude, Argon, Astra, Carbon ; pas de "
    "Kimi) ; orchestrateur épinglé ; consignes et liste des fils ; garde de crédit v6 ; porte de plafond ; procédure des "
    "relais persistants ; parts au pire des clés de Google (198) et d'OpenAI (48) ; gardes v7 à v10, hors celles que les "
    "points 5 et 6 retirent ; numéros des codes de sortie.",
    "",
    "1. **Numéro et base** (écart au mandat, déclaré en tête) : v11 et non v8 ; base v10 et non v6.",
    "2. **Clé Claude** : `RR_ANTHROPIC_API_KEY_LUC` au lieu de `RR_ANTHROPIC_API_KEY_MINUIT` (sans crédit, R-4833) pour les "
    "deux proposeurs Claude, l'aiguilleur et le premier juge ; exception déclarée à la règle « Claude par l'abonnement » "
    "(GO-2026-11-22-70), accordée en GO-2026-11-22-107 (échéance 2026-11-25) ; le lanceur exige la variable de la clé LUC, "
    "refuse un relais Claude sur une autre clé et vérifie la ligne de l'exception en plus de la ligne du plafond. "
    "**Retraits** : la clé Minuit, son crédit déclaré de 200 USD et son compte « au prix relevé » (v2 à v10).",
    "3. **Règle de départ de la clé LUC** (§ Règle des clés, « Clé LUC ») : le solde, que seule la console rend, est lu par "
    "Lazar le jour du départ ; couverture = solde lu + recharge automatique encore disponible (au plus 40 euros, comptés au "
    "pair) − réserves déclarées ; **plafond de la part Claude** = le plus petit de 150 USD et des quatre cinquièmes de la "
    "couverture ; relais Claude lancé à ce plafond exactement ; **plancher** : pas de départ (code 3) sous 20,65 USD de "
    "plafond. **Remplace**, pour cette clé seulement, la règle « reste lu au-dessus de la part au pire de 150 USD et d'un "
    "cinquième du crédit », qui interdirait tout départ sur LUC. Le plafond d'arrêt de 150 USD et tout ce que la course "
    "sert ou mesure ne changent pas.",
    "4. **Garde de la part Claude pendant la course** : compte au fil de l'eau sur l'état du relais Claude ; arrêt de la "
    "course au premier refus du relais pour plafond atteint (code 5) et alerte scellée pour la mère, qui prévient Lazar ; "
    "limites de la garde écrites (refus du fournisseur avant le plafond, dépassement du relais, change) ; cette issue est ajoutée aux critères de bonne fin (elle l'interdit) et à la liste d'arrêt, et la part Claude relevée au fil de l'eau à ce qui est mesuré.",
    "5. **Astra** : `gpt-6.2-astra` au lieu de `gpt-6-astra` (R-4900) ; clé déclarée `OPENAI_API_KEY_2` ; prix relevés 8 et "
    "40 USD par million de jetons (16 et 60 au-delà de 272 000 jetons d'entrée, hors d'atteinte), R-4905 ; sonde du jour "
    "refaite avec ce modèle, cette clé et ces prix, par des programmes de sonde neufs. **Retraits** : la sonde v2 et la "
    "sonde commune v1, qui portent `gpt-6-astra` en dur.",
    "6. **Carbon** : appel en flux sous la garde gelée des appels aux modèles de Google (GO-2026-11-21-71, "
    "GO-2026-11-21-47), au prix plein. **Retraits** : la commande Gemini par lot, le relais Gemini v4, le facteur de lot, et "
    "les gardes v8 et v9 propres au lot (provision de 28 672 jetons et son minimum de 25 870, délai de lot de 1 620 s, "
    "sortie retenue d'au moins 24 500 jetons, bornes de lots et de relevés du relais) ; en flux, les contrôles sont ceux de "
    "la garde gelée et les réglages à inscrire.",
    "7. **Devis** : aucun devis neuf ; Carbon au prix plein, 0,9970 USD par appel estimé au lieu de 0,4985 ; cinq espèces : "
    "49,11 USD sans marge, 54,02 avec ; base de l'écart au devis 49,112 ; pire cas 150, inchangé (§ Plafond).",
    "8. **Lignes de GO** : GO-2026-11-18-14 (plafond d'arrêt, prolongée au 2026-12-15 par GO-2026-11-22-80) et "
    "GO-2026-11-22-107 (exception, échéance 2026-11-25) ; l'échéance la plus proche borne le départ.",
    "9. **Contre-lecture** : par un Opus neuf, puis vérification des corrections par le même contre-lecteur (pièce de "
    "classe A) ; le modèle K contre-lisait les v2 à v10.",
    "10. **Configuration v11** : la v9 au nom de la clé Claude, au plafond du relais Claude et au bloc descriptif de Carbon "
    "près.",
    "11. **Chemins et noms** : contre-lecture, déclaration, relevés, commandes et rapports de sonde sous `course-v11/` "
    "(`declaration-relais-course-affinage-mentors-v11.json`, `releve-credits-avant-course-affinage-mentors-v11.json`, "
    "`releve-prix-claude-course-affinage-v11.json`, `commandes-exactes-course-affinage-v11.md`) ; sorties "
    "`/home/user/sorties-course-affinage-mentors-v11/` et `runs/<id>-course-affinage-mentors-v11/` ; alerte neuve "
    "`alerte-arret-part-claude.json` ; une seule course de v1 à v11.",
    "12. **Point ouvert** : Argon et la garde gelée (§ Espèces) ; rien n'y est changé par ce texte.",
    "",
    "## Emplacements et points à trancher avant le scellement (section à retirer de la version scellée)",
    "",
    "Emplacements à remplir :",
    "",
    "1. RÉFÉRENCE À INSCRIRE — note de la mère au registre : « v8 » de GO-2026-11-22-107 se lit v11 (en-tête).",
    "2. EMPREINTE À INSCRIRE — configuration fixe v11 (pièces).",
    "3. EMPREINTE À INSCRIRE — commande de Carbon en flux et relais de Carbon (pièces) ; RÉGLAGE À INSCRIRE — provision de "
    "réflexion, plafond de sortie, délais et bornes du relais de Carbon (§ Espèces, liste d'arrêt).",
    "4. EMPREINTE À INSCRIRE — programme de la sonde d'Astra et sonde commune de cette version (pièces).",
    "5. EMPREINTE À INSCRIRE — essais du lanceur, gabarit de déclaration, gabarits des deux relevés (pièces) ; celle du "
    "lanceur seulement s'il ne porte plus l'empreinte de ce texte dans son code (sinon, cycle d'empreintes).",
    "6. RÉGLAGE À INSCRIRE — libellé du modèle que la contre-lecture doit dire (§ Contre-lecture).",
    "7. RÉFÉRENCE À INSCRIRE — décision sur Argon et la garde gelée (§ Espèces).",
    "",
    "Points que ce texte fixe et que le lanceur v11 doit tenir, avec un essai sain et un essai artefact chacun (R5) ; si le "
    "lanceur fait autrement, le texte ou le lanceur change, jamais un écart silencieux :",
    "",
    "- le calcul du plafond de la part Claude à partir du relevé (solde lu, recharge au pair et au plus 40, réserves, quatre "
    "cinquièmes, 150 au plus, centime inférieur), le contrôle au centime du plafond du relais Claude, le plancher de "
    "20,65 USD (code 3) ;",
    "- la lecture de la ligne GO-2026-11-22-107 (présence, période, révocation) en plus de celle de GO-2026-11-18-14 ;",
    "- le relevé de l'état du relais Claude au moins une fois par minute, l'arrêt au premier refus pour plafond (statut "
    "402), le code 5 et l'alerte `alerte-arret-part-claude.json` ;",
    "- la garde gelée des appels aux modèles de Google sur la commande de Carbon, avant l'envoi et après la réponse ;",
    "- la sonde d'Astra faite avec `gpt-6.2-astra`, `OPENAI_API_KEY_2` et les prix 8 et 40 ;",
    "- la base de l'écart au devis, 49,112 USD pour cinq espèces ;",
    "- les gardes héritées des lanceurs v7 à v10 que ce texte garde (bornes basses de tous les relais, exclusion mutuelle "
    "avec la course d'auto-conception, sonde liée à la sonde commune, état de relais neuf et lisible, codes de sortie "
    "distincts dont le code 6, plafond de session des proposeurs à 3,00 USD) : un lanceur écrit à partir du lanceur v6 ne "
    "les a pas.",
]
inserer_apres(250, *DIFF)

# ------------------------------------------------------------------------------------------------ écriture
sortie = []
for n in range(1, 251):
    sortie.append(lignes[n])
    sortie.extend(apres.get(n, []))
texte = "\n".join(sortie) + "\n"
open(dst, "w", encoding="utf-8", newline="\n").write(texte)
print("lignes de la v10 touchées :", sorted(touchees))
print("insertions après les lignes :", sorted(apres))
print("octets :", len(texte.encode("utf-8")), "sha256 :", hashlib.sha256(texte.encode("utf-8")).hexdigest())
