#!/usr/bin/env python3
"""Lanceur de la course d'affinage des idées des mentors par l'organisme d'idéation — version 7.

Version 7 (R12 ; v1 à v6 restent en place, jamais lancées). Porte la contre-lecture complète de la v6 et des commandes v6b
(modèle K, `course-v6/contre-lecture-complete-course-affinage-v6-v6b.md`, « Scellable après corrections. ») :
1. (majeur 1) bornes basses lues par PID **et** sur `/relais/etat` pour **tous** les relais annoncés au préenregistrement :
   Astra (et Kimi) : `--max-appels` ≥ 16 + 4 = 20, plafond du relais ≥ sa part au pire (Astra : égal, 24 USD = 16 × 1,50) ;
   Carbon : `--max-lots` ≥ 20 et `--max-appels` ≥ 40 ; Argon : inchangé (2 × (16 + 32 × espèces)) ; Claude : plafond 150 ;
   valeurs de l'état égales aux arguments ; un argument de borne absent est un refus (aucun défaut supposé) ;
2. (majeur 2) aucune course d'auto-conception en cours (manifeste de départ sans manifeste de fin) ; relevé des crédits
   postérieur à la fin de toute course d'auto-conception versée ; les commandes v7 disent le reste (ports, clés, sonde) ;
   sonde d'Astra : rapport de la sonde commune du jour exigé et lié au rapport v2 par son empreinte (le rapport du
   18 novembre, `course-v6/sonde-astra-course-affinage-v6.json`, est accepté ce jour-là) ;
3. (mineurs) état de relais vide ou sans « appels » refusé ; écart au devis recalculé sur les espèces actives (cinq : 37,576) ;
   code 6 pour une course partie dont l'orchestrateur rend un code non nul ou dont le lanceur échoue après le départ ; sonde
   commune épinglée ; Kimi refusé tant qu'aucune référence n'est admise par une version du lanceur (liste vide).
Codes : 0 course finie ; 2 refus avant le départ ; 3 alerte de crédit avant le départ ; 4 cumul au-dessus de 150 USD ;
5 arrêt par la garde de crédit ; 6 course partie, orchestrateur à code non nul (arrêt, nœud, signal) ou erreur du lanceur
après le départ (vrai code au manifeste de fin).
Le reste est la v6.

Texte de la v6 :

Lanceur de la course d'affinage des idées des mentors par l'organisme d'idéation — version 6.

Version 6 (R12 ; v1 à v5 restent en place, jamais lancées). Porte la contre-lecture de la v5 (modèle K,
`course-v5/contre-lecture-preenregistrement-course-affinage-mentors-v5.md`, `3da3379a…`) :
1. identifiant de run unique à la microseconde ; acte de gel, configuration et registre dérivé écrits dans un dossier de
   préparation hors dépôt ; `runs/<id>` n'est créé qu'après la porte à blanc (un refus ne laisse rien au dépôt) ;
2. sonde d'Astra : réglages dans les commandes (réserve du relais jeté, sortie bornée par le plafond) ;
3. Kimi non déclaré par défaut : déclaré seulement avec un mot écrit de la mère dans la déclaration
   (`"kimi_autorise_par_la_mere": {"reference": …}`) ;
4. clé faite d'espaces refusée ;
5. garde de crédit v6 : soupçon sur une ligne de limite de débit réglable par la déclaration
   (`"compter_limite_de_debit_comme_soupcon"`, vrai par défaut) ;
6. textes (titre de l'acte de gel) ; 7. part au pire par **nom de variable de clé** : somme des parts des relais qui la
   partagent (Argon et Carbon : 150 + 24), règle de clé par part appliquée à la somme.
Le reste est la v5.

Texte de la v5 :

Lanceur de la course d'affinage des idées des mentors par l'organisme d'idéation — version 5.

Version 5 (R12 ; v1 à v4 restent en place, jamais lancées). Porte :
A. les constats 1 à 5 de la contre-lecture de la v4 (rapportés par la mère) : (1) le dossier de sortie et le dossier des arrêts
   ne sont créés qu'après la vérification de l'orchestrateur et la porte à blanc, et une course ne compte comme lancée que par
   son manifeste de départ ou son journal ; (2) arguments de chaque commande de porte recoupés avec la déclaration et la
   configuration (`--url`, `--modeles-permis`, `--plafond-ligne` = 150) ; modèles permis du relais vivant égaux à ceux de la
   configuration ; (3) garde de crédit v5 (soupçon, arrêt au deuxième soupçon du même relais ; seuls les fichiers
   `arret-credit-*` arrêtent la course) ; (4) relais Gemini d'Argon (et de Carbon) contrôlés avant le départ : PID, programme
   épinglé, port, `--max-appels` suffisant, état neuf, variable de clé effacée ; (5) textes ;
B. Carbon déclaré (R-3274) : commande Gemini par lot épinglée, arguments exacts, relais Gemini v4 contrôlé ;
C. Astra déclaré seulement après une sonde triviale réussie (≤ 0,05 USD, relais jeté ; R-3273), relais de la course neuf ;
D. confidentialité (R-3273) : textes servis expurgés et vérifiés par programme (aucun nom de personne interne, aucun
   identifiant de session, aucun courriel) ; un texte servi où il en reste fait refuser le départ.
Le reste est la v4.

Texte de la v4 :

Lanceur de la course d'affinage des idées des mentors par l'organisme d'idéation — version 4.

Version 4 (R12 ; v1 à v3 restent en place, jamais lancées) : porte les douze constats de la contre-lecture de la v3 (modèle
K, `course-v3/contre-lecture-preenregistrement-course-affinage-mentors-v3.md`, `52e7cc02…`) :
1. porte de plafond des relais persistants = programme épinglé `scripts/porte_plafond_relais_v1.py` (relais de ligne
   entière), en tête de la commande de chaque porte ; **porte à blanc** avant le manifeste de départ ; relais vivant contrôlé
   par PID (programme épinglé par la procédure, variable de clé, port, plafond) ;
2. registre des GO **dérivé** (ligne du GO et révocations qui la visent), écrit et scellé dans le dossier du run, passé à
   l'orchestrateur ; empreinte du registre source au manifeste ;
3. contrôles de l'adaptateur de Kimi repris avant le départ ; 4. garde de crédit v4 ; 5. relevé du jour des prix Claude, scellé,
   comparé au barème du relais épinglé ; 6. relais lancés par le lanceur de relais de la procédure ; 7. variable Minuit vide
   refusée ; 8. pièce de la procédure épinglée ; 9. commandes d'Astra et de Carbon épinglées (table vide en v4 : ces espèces
   sont refusées tant qu'une version ne les épingle pas) ; 10. reste égal à la part refusé ; 11. sorties hors dépôt regardées ;
   12. alerte écrite pour la mère à l'arrêt pour crédit.
Codes : 0, 2, 3, 4, 5 comme la v3.

Texte de la v3 :

Lanceur de la course d'affinage des idées des mentors par l'organisme d'idéation — version 3.

Version 3 (R12 ; v1 `015f5c33…` et v2 `9a85e78d…` restent en place, jamais lancées). Décisions de la mère R-3237 :
(1) **règle de clé par part** : chaque clé est confrontée à sa part au pire (la course ne peut pas dépenser plus sur elle),
non au plafond global ; pour Kimi, part au pire + 11,3 USD (pire cas de la course Kimi de la relance, GO-2026-11-18-17)
≤ 90 % du reste lu, sinon refus (les deux courses se suivent, solde relu avant chacune) ; le plafond d'arrêt de 150 USD est
inchangé ; (2) **dispense écrite** (référence R-3237) pour les clés d'Argon, d'Astra et de Carbon, au solde illisible :
départ permis, chaque appel passe par `scripts/garde_credit_relais_v3.py`, et **la course est arrêtée au premier refus pour
crédit** (SIGTERM à l'orchestrateur par son PID, arrêt propre) ; coût compté au prix des fichiers ; (3) **procédure neutre
des relais persistants** : pièce `course-v3/procedure-relais-persistants-course-affinage-v3.json` (chemin et empreinte de la
procédure versée par la mère) ; moteur réel refusé tant qu'elle n'est pas remplie, scellée, à son empreinte, et citée par
les portes de plafond des relais persistants. Contre-lecture : modèle K, `course-v3/`.
Codes : 0 course finie ; 2 refus avant départ, ou arrêt ou nœud de l'orchestrateur ; 3 alerte de crédit avant le départ ;
4 cumul lu au-dessus de 150 USD ; 5 course arrêtée au premier refus pour crédit d'un relais dispensé.

Texte de la v2 (inchangé sur le reste) :

Lanceur de la course d'affinage des idées des mentors par l'organisme d'idéation — version 2.

Version 2 (R12 ; la v1, `scripts/lancer_course_affinage_mentors_v1.py`, `015f5c33…`, reste en place, jamais lancée).
Ajouts (consigne de la mère, R-3228) : tous les appels Claude passent par la clé `RR_ANTHROPIC_API_KEY_MINUIT` (nom seul) ;
arrêt au départ si cette variable est absente de l'environnement du lanceur (test par le nom, jamais par la valeur) ;
refus de tout relais configuré sur une autre clé de la famille Claude, `RR_ANTHROPIC_API_KEY_RIGAUD` nommément ; crédit
de la clé Minuit compté au prix relevé quand l'interface de facturation ne le rend pas (200 USD déclarés, R-3228, moins
la dépense antérieure déclarée) ; contre-lecture par le modèle K, garde stricte (première ligne du verdict exacte, refus
d'un rapport qui dit n'avoir pas relu) ; nom de la clé écrit pour chaque relais et chaque espèce au manifeste.

Texte de la v1 (inchangé sur le reste) :

Décision N-072 (texte `docs/decisions/decision-matiere-premiere-mentors-v1.md`), GO-2026-11-18-14 (plafond d'arrêt 150 USD,
R-3215), budget des appels d'interface séparé (GO-2026-11-18-13, R-3209 point 2). Préenregistrement :
`docs/notes/organisme-affinage-mentors-v1/course-v1/preenregistrement-course-affinage-mentors-v1.md` (empreinte épinglée
ci-dessous). Modèle : le lanceur de référence `scripts/lancer_course_ideation_organismes_discrets_v7.py` (`3b20b911…`) —
mêmes gardes de GO, d'orchestrateur, de pièces, d'environnement sans clé, de bac à sable, de manifestes scellés ; mais la
course passe par la **course 2** de l'orchestrateur (`demonstrations/ideation_v8.py --course-2`, v56), qui porte
l'aiguilleur, les juges croisés aveugles et la mémoire anti-redite que la voie v2 n'a pas.

Usage, seul et exact (cwd = racine du dépôt de travail) :

    GO_ID=GO-2026-11-18-14 /usr/local/bin/python3 -I -B scripts/lancer_course_affinage_mentors_v1.py

Essai à blanc (moteur simulé de l'orchestrateur, relais factices, aucune dépense, aucun GO) :

    /usr/local/bin/python3 -I -B scripts/lancer_course_affinage_mentors_v1.py --a-blanc DOSSIER_NEUF

Ce que fait le lanceur, dans cet ordre ; tout refus rend 2 (motif sur la sortie d'erreur), toute alerte de crédit avant le
départ rend 3 ; rien n'est appelé avant le manifeste de départ :
1. course jamais lancée sous ce lanceur (R12 : un dossier de run de cette course existe déjà = refus ; une relance est une
   nouvelle version et un mot de la mère) ; ligne de GO (type calcul, accordée par Lazar, période, non révoquée, plafond
   lu = 150 USD exactement) ;
2. garde (3) : préenregistrement à l'empreinte épinglée et scellé ; contre-lecture scellée, présente, qui cite l'empreinte du
   préenregistrement **et celle de ce lanceur**, au verdict « Scellable » sans réserve (sinon refus) ;
3. pièces épinglées (configuration fixe, liste des fils, consignes, enveloppe et commande d'Argon) ; liste des fils : aucune
   entrée servie dans les retraits, aucun jeton réservé dans un texte servi ;
4. déclaration des relais (écrite et scellée par la session d'exécution : adresses de boucle locale, portes de plafond, noms
   des clés, jamais une valeur) : espèces actives ; Carbon seulement si inscrite (R-3217) **et** relais et clé nommés ;
5. garde (2) : relevé du crédit de chaque clé employée (fichier scellé de la session d'exécution, du jour) : « non lisible »
   refusé sauf dispense écrite de la mère ; reste sous un cinquième du crédit ou sous le plafond d'arrêt : alerte écrite
   pour la mère (fichier et sortie), arrêt avant le départ (code 3) ;
6. orchestrateur : commit et empreintes épinglés, arbre propre (fichiers suivis, non suivis, ignorés) ;
7. garde (1) : configuration d'orchestrateur assemblée (plafond S17 = 150 = GO, portée « course », une génération, plafonds
   de relais des étapes protégées ≤ 150, passe « tableau » et fusions retirées par construction), écrite et scellée avec
   l'acte de gel ; `--verifier-seulement` de l'orchestrateur (aucun appel) exigé à 0, montant requis 150 ;
8. environnement sans clé (noms retirés, jamais une valeur), bac à sable (moteur réel), manifeste de départ scellé (R9) ;
9. course ; manifeste de fin scellé sur tout chemin ; garde (5) coût réel par relais (consommations de l'orchestrateur), écart
   au devis v3, relevé « après » estimé et alerte si un reste estimé passe sous les seuils.

Bibliothèque standard seulement (le lanceur tourne sous `-I`). Ce lanceur nomme des modèles dans la configuration qu'il
passe à l'orchestrateur (comme le lanceur de référence) ; les pièces versées n'en nomment aucun.
"""
from __future__ import annotations

import datetime as _dt
import hashlib
import json
import os
import re
import shutil
import signal
import subprocess
import sys
import unicodedata
from dataclasses import dataclass
from pathlib import Path

VERSION = "lancer_course_affinage_mentors_v7"
GO_ID = "GO-2026-11-18-14"
PLAFOND_ARRET_USD = 150.0
INSCRIPTION_CARBON = "R-3217"
DEPOT = Path(__file__).resolve().parents[1]
COURSE_V1 = "docs/notes/organisme-affinage-mentors-v1/course-v1"
COURSE_V2 = "docs/notes/organisme-affinage-mentors-v1/course-v2"
COURSE_V3 = "docs/notes/organisme-affinage-mentors-v1/course-v3"
COURSE_V6 = "docs/notes/organisme-affinage-mentors-v1/course-v6"
COURSE = "docs/notes/organisme-affinage-mentors-v1/course-v7"
# v7, majeur 1 : bornes basses des relais. L'orchestrateur épinglé fait un appel d'adaptateur par case et par proposeur, sans
# reprise (`pole/noyau_v56.py`, `appel` ; `pole/course2_v53.py`, `_proposer`) ; la commande d'Astra envoie une requête par
# appel, celle de Carbon un `countTokens` et un `batchGenerateContent` (un lot) par appel. Seize appels suffisent donc à la
# lecture ; la marge de quatre (25 %) couvre ce que la lecture ne peut exclure (un appel refusé par le relais avant l'amont
# compte quand même). Elle ne porte que sur les appels : le plafond en dollars du relais d'Astra reste sa part au pire.
APPELS_PAR_PROPOSEUR = 16
MARGE_APPELS_PROPOSEUR = 4
MIN_APPELS_RELAIS_PROPOSEUR = APPELS_PAR_PROPOSEUR + MARGE_APPELS_PROPOSEUR   # Astra, Kimi : 20
MIN_LOTS_CARBON = APPELS_PAR_PROPOSEUR + MARGE_APPELS_PROPOSEUR              # 20
MIN_APPELS_CARBON = 2 * MIN_LOTS_CARBON                                       # 40 : countTokens + lot, par appel
RELAIS_A_DOLLARS = ("claude", "kimi", "astra")
PORTS_DES_COURSES = (8787, 8788, 8789, 8790, 8791, 8792)
# v7, mineur 9 : références écrites de la mère qui autorisent Kimi ; vide : Kimi refusé (R-3279), quelle que soit la déclaration.
REFERENCES_KIMI_ADMISES: tuple = ()
# v7, majeur 2 : l'autre course de l'organisme qui partage ports, clés et sonde.
MOTIF_AUTRE_COURSE = re.compile(r"-course-auto-conception-v\d+$")
REFERENCE_DISPENSE = "R-3237"
FOURNISSEURS_DISPENSABLES = ("argon", "astra", "carbon")
KIMI_COURSE_SUIVANTE_PIRE_USD = 11.3   # R-3237 : pire cas de la course Kimi de la relance (GO-2026-11-18-17)
KIMI_PART_DU_RESTE = 0.9
PROCEDURE_RELAIS = f"{COURSE_V3}/procedure-relais-persistants-course-affinage-v3.json"
RELEVE_PRIX = f"{COURSE}/releve-prix-claude-course-affinage-v7.json"
# v7 : rapport v2 de la sonde (format lu depuis la v5) et rapport de la sonde commune du même appel, cherchés au jour du
# lancement. Le 18 novembre : `course-v6/sonde-astra-course-affinage-v6.json` (d2cacbcf…) et
# `organisme-auto-conception-v1/course-v2/sonde-astra-commune-2026-11-18-v1.json` (802b840e…). Un autre jour : une sonde
# neuve, rapports sous `course-v7/` aux noms datés.
SONDE_ASTRA = f"{COURSE_V6}/sonde-astra-course-affinage-v6.json"
SONDES_ASTRA_V2 = (f"{COURSE}/sonde-astra-course-affinage-v7-{{jour}}.json", SONDE_ASTRA)
SONDES_ASTRA_COMMUNES = (f"{COURSE}/sonde-astra-commune-{{jour}}-v1.json",
                         "docs/notes/organisme-auto-conception-v1/course-v2/sonde-astra-commune-{jour}-v1.json",
                         f"{COURSE_V6}/sonde-astra-commune-{{jour}}-v1.json")
SONDE_ASTRA_MAX_USD = 0.05
# Barème du relais de clé de la procédure (`pole/relais_reel.py`, 1b90b020…, l. 49-54), USD par million (entrée, sortie).
BAREME_CLAUDE = {"claude-opus-5-5": (4.0, 20.0), "claude-fable-5-1": (10.0, 50.0)}
# Programmes de relais épinglés par la procédure neutre (§ 1) : nom de fichier → empreinte.
PROGRAMMES_RELAIS = {"claude": ("relais_reel.py", "1b90b020287e575b5564508f9ba33b87bbc051c1015f4198e6b6e648d50ee153"),
                     "kimi": ("relais_kimi_v4.py", "67f369518102b3f7408f28dab053a4d6f9bc2b676eadfaa338f55d39af99027e"),
                     "astra": ("relais_kimi_v4.py", "67f369518102b3f7408f28dab053a4d6f9bc2b676eadfaa338f55d39af99027e"),
                     "argon": ("relais_gemini_v2.py", "2b0043bcab8b3922c65a4008e719408c52781d7544064b5a29a23d7ef60c1aeb"),
                     "carbon": ("relais_gemini_v4.py", "543e728d90e809c661fdc26f1e1b1a32b2e23128a7d09e3b5d16f851408a35b4")}
MODELES_RELAIS = {"kimi": ["kimi-k3.1-pro"], "astra": ["gpt-6-astra"], "argon": ["gemini-4-argon"], "carbon": ["gemini-4-carbon"]}
PORT_ARGON = 8788  # l'enveloppe d'Argon v5 (épinglée) parle à 127.0.0.1:8788
GEMINI = ("argon", "carbon")
# Commandes externes épinglées (constat 9 de la v3 ; B et C de la v5) : nom de fichier → empreinte (copies de main).
COMMANDES_EPINGLEES: dict = {
    "astra": {"commande_astra_v1.py": "986cf71efcac285899e76dd9b1d1c11bccbfd71dd7ae91b8bf3a4372567d7c71"},
    "carbon": {"commande_gemini_lot_v1.py": "9484dce066514185dc1155d5c8dcff44b256fdf835b371b59ebdffa1d50bad75"}}
# Arguments exacts après « python -I -B <commande> » (B, C) ; le délai total de la commande de Carbon (1 500 + 30 + 2 × 120 =
# 1 770 s) reste sous le délai de l'adaptateur de l'orchestrateur (1 800 s, non réglable par la configuration).
ARGUMENTS_COMMANDES = {
    "carbon": ["--modele", "gemini-4-carbon", "--url-base", "http://127.0.0.1:8792/v1beta", "--prix-entree", "8.3",
               "--prix-sortie", "41.5", "--facteur-lot", "0.5", "--max-sortie-jetons", "32768", "--sortie-min-jetons", "4096",
               "--provision-pensee-jetons", "8192", "--intervalle-s", "30", "--delai-s", "1500", "--roles", "proposeur_ideation"],
    "astra": ["--url-relais", "http://127.0.0.1:8790", "--modele", "gpt-6-astra", "--prix-entree", "10", "--prix-sortie", "50",
              "--max-sortie-jetons", "32768", "--sortie-min-jetons", "4096", "--delai-s", "1500"]}
ETAPE_A_BLANC = "porte-a-blanc"
SORTIES_COURSES = tuple(Path(f"/home/user/sorties-course-affinage-mentors-v{k}") for k in (1, 2, 3, 4, 5, 6, 7))
MARQUEUR_A_REMPLIR = "À REMPLIR"
CLE_CLAUDE = "RR_ANTHROPIC_API_KEY_MINUIT"
CLES_INTERDITES = ("RR_ANTHROPIC_API_KEY_RIGAUD",)
PREFIXE_CLES_CLAUDE = "RR_ANTHROPIC_API_KEY"
CREDIT_DECLARE_CLE_CLAUDE_USD = 200.0  # R-3228, mot de Lazar


PREREG = f"{COURSE}/preenregistrement-course-affinage-mentors-v7.md"
PREREG_SHA256 = "720cbe81bbe5fe359ee8a8c814d374f3e52fac430351d8d29c6113ce9ae1d533"
CONTRE_LECTURE = f"{COURSE}/contre-lecture-preenregistrement-course-affinage-mentors-v7.md"
DECLARATION_RELAIS = f"{COURSE}/declaration-relais-course-affinage-mentors-v7.json"
RELEVE_CREDITS = f"{COURSE}/releve-credits-avant-course-affinage-mentors-v7.json"

PIECES = {
    "configuration": (f"{COURSE_V6}/configuration-course-affinage-mentors-v6.json", "0ea89ed2f72ce2693e619eb10b6eecbd46725d4578b548a44c5a98b9bb1ded21"),
    "sonde_astra": ("scripts/sonde_astra_affinage_v2.py", "1799449269e15661b92f2a45eaab95a22e3a766a1fdf10ec9a4648bbe92aebf7"),
    "sonde_commune": ("scripts/sonde_astra_courses_v1.py", "d374d1071f4ef70b3604d97dc62e2f14103c440a166342b330d7a576d8b4c777"),
    "garde_credit": ("scripts/garde_credit_relais_v6.py", "1d9882f71b01491c3282d24b963d14e8ad4339c855ec969f85b420c463c60fff"),
    "porte_plafond": ("scripts/porte_plafond_relais_v1.py", "fab5fe2e924c47799d968663baddfecb85dd6f74e9f859d9047b185eb36382b1"),
    "procedure_relais": (PROCEDURE_RELAIS, "d97594dbc2263cd4200113d44dd4fd3fc8562bef617d3e182f6a382bf95ec792"),
    "procedure_ecrite": ("docs/procedures/relais-persistants-v1.md", "0ca9cf5daa190135f8f26175f2639e4c9c4b22b01c551ab30ff8f7bb0d085148"),
    "lanceur_relais": ("scripts/lancer_relais_local_v1.py", "d365affcb0303283a71ac7d5e67e24a5b6060e3b13c2a9e83ea592e48d4b3c82"),
    "liste_fils": (f"{COURSE_V1}/fils-servis-et-retraits-course-affinage-mentors-v1.json", "c30928c88feffc16d3aa1119efe2a54ba2d70cf135b8068855190a21470a56bb"),
    "consigne_proposeur": (f"{COURSE_V1}/consigne-proposeur-course-affinage-mentors-v1.md", "d36ba0a01c1c190d55d0ed63b053c951b5a767a9310013321d797e3e203d8c4f"),
    "consigne_aiguilleur": (f"{COURSE_V1}/consigne-aiguilleur-course-affinage-mentors-v1.md", "903318d7659db07819cbe9a7f89cbdbd292f59e14c32bb8811d8f8cb35dd955b"),
    "consigne_juge": (f"{COURSE_V1}/consigne-juge-course-affinage-mentors-v1.md", "a32583b14845343a613514cdcba3c24831a274b48ecc95fe0d884f017d27d346"),
    "consigne_passe_tableau": (f"{COURSE_V1}/consigne-passe-tableau-course-affinage-mentors-v1.md", "1ac9791b6aea1c97f534e32980f1f837cca425806ce8235b1064d98ce261dcbf"),
    "enveloppe_argon": ("rapports/fille-ideation-1-v1/appel-argon-v5.sh",
                        "37c0205e26f83cbdcdf5ad7f1e4094a21c7dcc70afb72d15ef0d260a770a132a"),
    "commande_argon": ("docs/notes/ideation-organisme-v1/argon-recherche-v1/commande_argon_v3d.py",
                       "46c91df41b77a6d4cb7f5141993fda4a894118b5dd4ad1e5ba21a17dc2d67e46"),
}
PIECES_SERVIES = ("consigne_proposeur", "consigne_aiguilleur", "consigne_juge", "consigne_passe_tableau")
DEPOT_ATTENDU_PAR_L_ENVELOPPE = Path("/home/user/controle-ia-travail")

ORCHESTRATEURS_CANDIDATS = (Path("/home/user/ideation-organism/orchestrator"),
                            Path("/home/user/lciric/ideation-organism/orchestrator"))
COMMIT_ORCHESTRATEUR = "a41b7b50f7c64ce488c120bb89ad3d25fb1dd1cb"
LANCEUR_ORCHESTRATEUR = "demonstrations/ideation_v8.py"
EMPREINTES_ORCHESTRATEUR = {
    "demonstrations/ideation_v8.py": "2e2be8d72c548e183b94c14de20c971f241f998f54f64c5281b2427fdd64e9d1",
    "demonstrations/ideation_v7.py": "7b90e65e1308b1c230b3f804743cfc42b9dc571d93b73ed6c5f3f8c9d2b481b2",
    "demonstrations/ideation_v6.py": "4c302e5b97b229d5b3edd9e9a427f1e50796c10f7081f63132165ffeef854ba4",
    "demonstrations/ideation_v5.py": "1894f250264eaaccbf891dfa255e71dc587fe415c8d21e283391203a2fe73444",
    "demonstrations/ideation_v4.py": "4212d4c9d014a265847d4c4ed87a8cd804fdafa73f85fd8947874d63fca1c36d",
    "demonstrations/ideation_v2.py": "bc5e9c98acff41b97487e2345d33768c8cdf41f0ededf8b2eed0bf842c889845",
    "pole/configuration_v53.py": "ef72ffbf6b5ba546fb5e509502b59f0d9ac4f78772dcb9570ef36086639f4a78",
    "pole/configuration_v54.py": "3424ca7fa8911e5c2656cb56632f7d74c958008b9366af0ac45e6a62e4d16d66",
    "pole/configuration_v55.py": "2e6237c0a8b1c823fa17ddd6c680357a59ec4030bfbe9ac6ba970a700a864071",
    "pole/configuration_v56.py": "122405228d6ec550b2120114e87a1e70bcc74c14eee17342605d8402bd015d6b",
    "pole/course2_v53.py": "8f2d035828df913d8fa92e1b7d0c8e41ac73e8416e60f3b674753c27f5c61237",
    "pole/course2_v54.py": "ac1980d04eb88d8fbb9a073902e47146ab9eadd3375a41cd72835fa5acf20342",
    "pole/course2_v55.py": "ee6a861e7f8db32a9545372a51f902389cdbea809b0ba354e621a3681e541a70",
    "pole/course2_v56.py": "14f655696876afc8453ec5237236b3f9daf8d87844c4acc9d5189b3e61b310f1",
    "pole/budget_v56.py": "3a672aceeeee3cf83cd4e46ca461fdbaf3acd0a9552be24d2566627ce6b7c13e",
    "pole/adaptateurs.py": "a1a8ede8d38884a28365ee797dcd3018dbf09ea1baefa3f57cfcb3281c529c99",
    "pole/adaptateurs_v56.py": "d36c79b272af450b8d67313f44068743d80f0204bcedbd30f5d879829c945a17",
    "pole/adaptateur_kimi_v53.py": "09a46515ff30a99f360fcbc7d4c613c35cb511439a5b6c249327e477fdee4ada",
    "pole/aiguilleur_v53.py": "a856cdaa37e8fb1f3b873ef2c0d9aa439ee0a8838f5ee9a2910cb3c0dcf8007f",
    "pole/juges_croises_v53.py": "c4c6ab12dc471eef078c116a4205a22d9b498da720ce71e37a0a6edae6c4239b",
    "pole/memoire_v53.py": "43b01b43b1ec347ff02b456975d74c17e7a0e974e9b95e9ba4935bdb895f31a0",
    "pole/noyau_v56.py": "eb5a003e8f23b0882e5588fe537e8b65b890f0d7d19560896be4e85a0731543b",
    "pole/gardes_e0_v56.py": "921e59f23753666d6367678447edf4ee2964dc6ec3d382aefa8582b996e123b9",
    "pole/simulation_v56.py": "bcafca44c5117dfd30262ee520a67944d051208f1b1deac6fac016e8cb95dc76",
    "pole/relais_reel_v2.py": "98c3e79e2c795a69345ffcf9aa742e31dde4a578a15f7c610f1ec7fd535ac8d7",
}

# Devis v6 et v6b (`devis-course-affinage-mentors-v6.md`, `…-v6b.md`, mêmes prix par appel que la v3 et la v5 ; noms des
# constantes gardés), estimation par appel, USD : sert à l'écart au devis (garde 5).
DEVIS_V5_PAR_APPEL = {"prop-opus": 0.141, "prop-fable": 0.3525, "prop-argon": 0.276, "prop-kimi": 0.276, "prop-astra": 0.276,
                      "prop-carbon": 0.276, "aiguilleur": 0.031, "juge-opus": 0.037, "juge-argon": 0.0347}
# v7, mineur 4 : base du devis recalculée sur les espèces actives (16 appels par espèce ; 2 cartes × 16 cases par espèce pour
# l'aiguilleur et chacun des deux juges) ; ces deux totaux ne servent plus qu'aux essais (cinq espèces : 37,576 ; six : 45,2784).
DEVIS_V5_TOTAL = {"cinq_especes": 37.576, "six_especes": 45.2784}

DOSSIER_SORTIES = Path("/home/user/sorties-course-affinage-mentors-v7")
SUFFIXE_RUN = "-course-affinage-mentors-v7"
SUFFIXES_DEJA_LANCEE = tuple(f"-course-affinage-mentors-v{k}" for k in (1, 2, 3, 4, 5, 6, 7))  # une seule course, quelle que soit la version
NOMS_PERMIS = ("PATH", "LANG", "LC_ALL", "TZ", "TMPDIR")
NOMS_DE_CLE = ("ANTHROPIC_API_KEY", "ANTHROPIC_AUTH_TOKEN", "CLAUDE_CODE_OAUTH_TOKEN", "OPENAI_API_KEY", "GOOGLE_API_KEY",
               "GEMINI_API_KEY", "KIMI_API_KEY", "AWS_SECRET_ACCESS_KEY", "AWS_SESSION_TOKEN", "GITHUB_TOKEN", "GH_TOKEN", "HF_TOKEN")
MOTIF_NOM_DE_CLE = re.compile(r"(API_?KEY|TOKEN|SECRET|PASSWORD|PASSWD|CREDENTIAL)", re.I)
MOTIF_VALEUR_DE_CLE = re.compile(r"(sk-ant-[A-Za-z0-9]|sk-[A-Za-z0-9]{20,}|ghp_[A-Za-z0-9]{20,}|hf_[A-Za-z0-9]{20,}|AKIA[A-Z0-9]{12}|"
                                 r"AIza[0-9A-Za-z_-]{20,}|Bearer\s+[A-Za-z0-9._-]{16,})")
NOM_DE_VARIABLE = re.compile(r"^[A-Z][A-Z0-9_]{1,63}$")
URL_LOCALE = re.compile(r"^http://(127\.0\.0\.1|localhost|\[::1\]):\d{2,5}(/.*)?$")
MODELES_CLAUDE = ("claude-opus-5-5", "claude-fable-5-1")
TYPES_PERMIS = {"claude": "claude_sdk", "argon": "commande_externe", "kimi": "kimi_protocole", "astra": "commande_externe",
                "carbon": "commande_externe"}
CLES_PERMISES = {"claude_sdk": {"type", "url_relais", "porte_plafond"},
                 "commande_externe": {"type", "commande", "modeles_servis_permis", "porte_plafond"},
                 "kimi_protocole": {"type", "url_relais", "modele", "prix_entree", "prix_sortie", "max_sortie_jetons",
                                    "sortie_min_jetons", "delai_s", "porte_plafond"}}
CLES_META = {"nom_cle", "modele_propose", "inscription", "pid_relais"}

SONDE_BAC_A_SABLE = (
    "import json, sys\n"
    "sys.path.insert(0, sys.argv[1])\n"
    "from pole.adaptateurs import etat_bac_a_sable_detaille\n"
    "print(json.dumps(etat_bac_a_sable_detaille()))\n"
)


class Refus(RuntimeError):
    """Garde du lanceur : rien n'est lancé (code 2)."""


class AlerteCredit(RuntimeError):
    """Garde (2) : un reste est sous un seuil ; alerte écrite, arrêt avant le départ (code 3)."""


def sha256_fichier(chemin: Path) -> str:
    h = hashlib.sha256()
    with open(chemin, "rb") as f:
        for bloc in iter(lambda: f.read(1 << 20), b""):
            h.update(bloc)
    return h.hexdigest()


def date_u() -> str:
    r = subprocess.run(["date", "-u"], capture_output=True, text=True, timeout=10)
    if r.returncode != 0 or not r.stdout.strip():
        raise Refus("`date -u` illisible")
    return r.stdout.strip()


def _normaliser(texte: str) -> str:
    return unicodedata.normalize("NFKD", texte.lower()).encode("ascii", "ignore").decode()


def scelle(chemin: Path) -> bool:
    """Compagnon `.sha256` présent, une ligne « empreinte  nom », égal à l'empreinte du fichier."""
    c = Path(str(chemin) + ".sha256")
    if not chemin.is_file() or not c.is_file():
        return False
    lignes = [x for x in c.read_text(encoding="utf-8").splitlines() if x.strip()]
    if len(lignes) != 1:
        return False
    m = re.match(r"^([0-9a-f]{64})  (\S.*)$", lignes[0])
    return bool(m) and m.group(2) == chemin.name and m.group(1) == sha256_fichier(chemin)


def ecrire_scelle(chemin: Path, contenu) -> str:
    if chemin.exists():
        raise Refus(f"{chemin} existe déjà (R12)")
    if isinstance(contenu, (bytes, str)):
        donnees = contenu.encode("utf-8") if isinstance(contenu, str) else contenu
    else:
        donnees = (json.dumps(contenu, ensure_ascii=False, indent=1, sort_keys=True) + "\n").encode("utf-8")
    with open(chemin, "xb") as f:
        f.write(donnees)
    h = hashlib.sha256(donnees).hexdigest()
    with open(str(chemin) + ".sha256", "x", encoding="utf-8") as f:
        f.write(f"{h}  {chemin.name}\n")
    return h


@dataclass
class Reglages:
    depot: Path
    orchestrateurs: tuple
    commit_orchestrateur: str
    empreintes_orchestrateur: dict
    pieces: dict
    prereg: tuple
    contre_lecture: Path
    declaration: Path
    releve: Path
    registre_go: Path
    procedure_relais: Path
    releve_prix: Path
    dossier_runs: Path
    dossier_sorties: Path
    depot_attendu_par_l_enveloppe: Path
    python: str
    lanceur: Path
    moteur: str = "reel"
    environnement: dict | None = None
    aujourd_hui: _dt.date | None = None
    horodatage: object = date_u
    exiger_bac_a_sable: bool = True
    sorties_courses: tuple = SORTIES_COURSES
    programmes_relais: dict | None = None
    lire_cmdline: object = None
    lire_etat_relais: object = None
    ref_registre: str | None = "origin/main"
    verifier_go: bool = True
    sondes_astra_v2: tuple = SONDES_ASTRA_V2               # v7 : chemins relatifs au dépôt, « {jour} » = jour du lancement
    sondes_astra_communes: tuple = SONDES_ASTRA_COMMUNES
    references_kimi_admises: tuple = REFERENCES_KIMI_ADMISES

    @classmethod
    def production(cls) -> "Reglages":
        return cls(depot=DEPOT, orchestrateurs=ORCHESTRATEURS_CANDIDATS, commit_orchestrateur=COMMIT_ORCHESTRATEUR,
                   empreintes_orchestrateur=dict(EMPREINTES_ORCHESTRATEUR), pieces=dict(PIECES),
                   prereg=(DEPOT / PREREG, PREREG_SHA256), contre_lecture=DEPOT / CONTRE_LECTURE,
                   declaration=DEPOT / DECLARATION_RELAIS, releve=DEPOT / RELEVE_CREDITS,
                   registre_go=DEPOT / "registres" / "go.md", procedure_relais=DEPOT / PROCEDURE_RELAIS, releve_prix=DEPOT / RELEVE_PRIX, dossier_runs=DEPOT / "runs", dossier_sorties=DOSSIER_SORTIES,
                   depot_attendu_par_l_enveloppe=DEPOT_ATTENDU_PAR_L_ENVELOPPE, python=sys.executable,
                   lanceur=Path(__file__).resolve())


# --- (1) GO, une seule course -------------------------------------------------------------------------------------------------


def _est_revocation(cellules: list, go_id: str) -> bool:
    return any(_normaliser(c).startswith("revoc") for c in cellules) and any(go_id in c for c in cellules)


def verifier_go(registre: Path, aujourd_hui: _dt.date, go_id: str = GO_ID) -> dict:
    """Même lecture que le lanceur de référence ; plafond lu exactement égal au plafond d'arrêt (150 USD)."""
    if not registre.is_file():
        raise Refus(f"registre des GO absent : {registre}")
    ligne_go = re.compile(r"^\|\s*(GO-\d{4}-\d{2}-\d{2}-\d{2})\s*\|")
    trouvees, revocations = [], []
    for ligne in registre.read_text(encoding="utf-8").splitlines():
        m = ligne_go.match(ligne)
        if not m:
            continue
        cellules = [c.strip() for c in ligne.strip().strip("|").split("|")]
        if m.group(1) == go_id:
            trouvees.append(cellules)
        elif _est_revocation(cellules, go_id):
            revocations.append(m.group(1))
    principales = [c for c in trouvees if not (len(c) == 8 and c[3].lower().startswith("extension"))]
    if len(principales) != 1:
        raise Refus(f"{go_id} : {len(principales)} ligne(s) principale(s) dans {registre.name} (une exigée)")
    c = principales[0]
    if len(c) != 8:
        raise Refus(f"{go_id} : ligne mal formée ({len(c)} colonnes, 8 attendues)")
    ident, accorde, typ, perimetre, plafond, echeance, par, _ref = c
    if typ != "calcul":
        raise Refus(f"{go_id} : type {typ!r}, « calcul » exigé")
    if par != "Lazar":
        raise Refus(f"{go_id} : accordé par {par!r}, Lazar exigé")
    try:
        d_acc, d_ech = _dt.date.fromisoformat(accorde), _dt.date.fromisoformat(echeance)
    except ValueError:
        raise Refus(f"{go_id} : dates illisibles ({accorde!r}, {echeance!r})") from None
    if not d_acc <= aujourd_hui <= d_ech:
        raise Refus(f"{go_id} hors de sa période de validité ({d_acc} → {d_ech}, aujourd'hui {aujourd_hui})")
    if revocations:
        raise Refus(f"{go_id} révoqué par {', '.join(sorted(revocations))}")
    p = _normaliser(perimetre)
    if "mentors" not in p and "affinage" not in p:
        raise Refus(f"{go_id} : périmètre sans « mentors » ni « affinage » — ce n'est pas le GO de cette course")
    m_plafond = re.match(r"^\s*(\d+(?:[.,]\d+)?)\s*(?:USD|usd)\s*$", plafond)
    if not m_plafond:
        raise Refus(f"{go_id} : plafond illisible {plafond!r} (un nombre + USD attendu)")
    plafond_lu = float(m_plafond.group(1).replace(",", "."))
    if plafond_lu != PLAFOND_ARRET_USD:
        raise Refus(f"{go_id} : plafond lu {plafond_lu} USD != plafond d'arrêt {PLAFOND_ARRET_USD} USD")
    return {"id": ident, "accorde": accorde, "echeance": echeance, "plafond": plafond, "plafond_lu": plafond_lu, "par": par,
            "ligne_sha256": hashlib.sha256(("|".join(c)).encode("utf-8")).hexdigest()}


def verifier_course_jamais_lancee(r: Reglages) -> None:
    """Une course est « lancée » dès que son manifeste de départ existe ; un essai refusé avant lui ne bloque rien."""
    if r.dossier_runs.is_dir():
        deja = sorted(p.name for p in r.dossier_runs.iterdir()
                      if p.name.endswith(SUFFIXES_DEJA_LANCEE) and (p / "manifeste-lanceur-depart.json").exists())
        if deja:
            raise Refus(f"course déjà lancée sous ce lanceur ({deja}) : une relance est une nouvelle version et un mot de la mère")
    for d in r.sorties_courses:  # v4, constat 11 ; v5, constat 1 : seul un journal de course compte, pas un dossier laissé par un refus
        lancees = sorted(x.name for x in d.iterdir() if (x / "course.stdout.txt").exists()) if d.is_dir() else []
        if lancees:
            raise Refus(f"course d'affinage déjà lancée (journal hors dépôt) : {d} {lancees} — une seule course")


# --- (3) préenregistrement, contre-lecture, liste des retraits ----------------------------------------------------------------


def verifier_preenregistrement(r: Reglages) -> dict:
    chemin, attendu = r.prereg
    if not re.fullmatch(r"[0-9a-f]{64}", attendu or ""):
        raise Refus("empreinte du préenregistrement non posée dans le lanceur : aucun lancement")
    if not chemin.is_file():
        raise Refus(f"préenregistrement absent : {chemin}")
    lu = sha256_fichier(chemin)
    if lu != attendu:
        raise Refus(f"préenregistrement d'empreinte {lu}, {attendu} épinglée")
    if not scelle(chemin):
        raise Refus("préenregistrement non scellé (compagnon .sha256 absent ou faux)")
    return {"chemin": str(chemin.relative_to(r.depot)) if chemin.is_relative_to(r.depot) else str(chemin), "sha256": lu}


def lire_verdict(texte: str) -> str | None:
    lignes = texte.splitlines()
    for i, l in enumerate(lignes):
        if re.match(r"^#{1,3}\s*Verdict\b", l.strip()):
            for suite in lignes[i + 1:]:
                if suite.strip():
                    return suite.strip()
    return None


VERDICTS_EXACTS = ("Scellable.", "**Scellable.**")
AVEUX_NON_RELU = re.compile(r"(n'ai pas (re)?lu|pas (ete )?relu|non relu|sans (la )?relire|sans relecture|n'a pas (ete )?(re)?lu|"
                            r"lecture partielle du (preenregistrement|lanceur)|pas pu (re)?lire)")


def verdict_favorable(verdict: str | None) -> bool:
    """v2 (garde stricte) : la première ligne du verdict est exactement « Scellable. » (en gras ou non), rien d'autre."""
    return isinstance(verdict, str) and verdict.strip() in VERDICTS_EXACTS


def verifier_contre_lecture(r: Reglages, prereg_sha: str, lanceur_sha: str) -> dict:
    c = r.contre_lecture
    if not c.is_file():
        raise Refus(f"contre-lecture absente : {c} (R2 : aucun lancement sans contre-lecture scellée)")
    if not scelle(c):
        raise Refus("contre-lecture non scellée (compagnon .sha256 absent ou faux)")
    texte = c.read_text(encoding="utf-8")
    if prereg_sha not in texte:
        raise Refus("la contre-lecture ne cite pas l'empreinte du préenregistrement épinglé")
    if lanceur_sha not in texte:
        raise Refus("la contre-lecture ne cite pas l'empreinte de ce lanceur (elle n'a pas lu cette version)")
    v = lire_verdict(texte)
    if not verdict_favorable(v):
        raise Refus(f"verdict de la contre-lecture défavorable, illisible ou inexact : {v!r} (première ligne exacte « Scellable. » exigée)")
    if "modele k" not in _normaliser(texte):
        raise Refus("la contre-lecture ne dit pas être du modèle K (contre-lecteur attendu)")
    aveu = AVEUX_NON_RELU.search(_normaliser(texte).replace("’", "'"))
    if aveu:
        raise Refus(f"la contre-lecture dit n'avoir pas relu ({aveu.group(0)!r}) : refusée")
    return {"chemin": str(c), "sha256": sha256_fichier(c), "verdict": v}


def verifier_pieces(r: Reglages) -> dict:
    if r.moteur == "reel" and r.depot.resolve() != r.depot_attendu_par_l_enveloppe.resolve():
        raise Refus(f"dépôt de travail en {r.depot}, l'enveloppe d'Argon v5 attend {r.depot_attendu_par_l_enveloppe}")
    lues, ecarts = {}, {}
    for nom, (rel, attendu) in sorted(r.pieces.items()):
        p = r.depot / rel
        lu = sha256_fichier(p) if p.is_file() else None
        if lu != attendu:
            ecarts[nom] = {"chemin": rel, "attendu": attendu, "lu": lu}
        lues[nom] = {"chemin": rel, "absolu": str(p), "sha256": lu}
    if ecarts:
        raise Refus("pièces absentes ou d'empreinte différente (R11) : " + json.dumps(ecarts, ensure_ascii=False))
    return lues


def verifier_liste(liste: dict) -> dict:
    """Garde (3), dernier point : aucune entrée servie dans la liste des retraits ; aucun jeton réservé servi."""
    retirees = {x["numero"] for x in liste["retraits"]["idees_de_la_table"]}
    jetons = sorted({f for x in liste["retraits"]["reserves_de_cloisonnement"] for f in x["fiches"]})
    servies = [s["numero"] for f in liste["fils"] for s in f["idees_servies"]]
    croisement = sorted(set(servies) & retirees)
    if croisement:
        raise Refus(f"entrée servie figurant dans la liste des retraits : {croisement}")
    textes = "\n".join(s["texte_servi"] for f in liste["fils"] for s in f["idees_servies"])
    for j in jetons:
        if j in textes:
            raise Refus(f"jeton d'une entrée réservée dans un texte servi : {j}")
    if len(liste["fils"]) != 16:
        raise Refus(f"liste des fils : {len(liste['fils'])} fils, 16 attendus")
    return {"fils": len(liste["fils"]), "idees_servies_distinctes": len(set(servies)), "idees_retirees": sorted(retirees),
            "jetons_reserves": jetons}


def texte_de_case(fil: dict) -> str:
    lignes = [f"Fil commun n° {fil['rang']} : {fil['titre']}",
              "Idées regroupées sous ce fil (avis de proposeurs d'une course passée, jamais des faits ni des preuves) :"]
    lignes += [f"- [{s['numero']}] {s['texte_servi']}" for s in fil["idees_servies"]]
    return "\n".join(lignes)


# --- (4) déclaration des relais -----------------------------------------------------------------------------------------------


def lire_json_scelle(chemin: Path, quoi: str) -> tuple:
    if not chemin.is_file():
        raise Refus(f"{quoi} absent : {chemin}")
    if not scelle(chemin):
        raise Refus(f"{quoi} non scellé (compagnon .sha256 absent ou faux) : {chemin}")
    brut = chemin.read_text(encoding="utf-8")
    if MOTIF_VALEUR_DE_CLE.search(brut):
        raise Refus(f"{quoi} : une chaîne de la forme d'une valeur de clé y figure — refus, rien n'est lu ni recopié")
    try:
        return json.loads(brut), sha256_fichier(chemin)
    except ValueError:
        raise Refus(f"{quoi} : JSON illisible") from None


def verifier_declaration(decl: dict, fixe: dict, r: Reglages) -> dict:
    """Rend {fournisseurs (blocs de l'orchestrateur), especes_actives, cles {fournisseur: nom}, absentes, carbon}."""
    f_decl = decl.get("fournisseurs")
    if not isinstance(f_decl, dict):
        raise Refus("déclaration des relais : « fournisseurs » (objet) exigé")
    inconnus = sorted(set(f_decl) - set(TYPES_PERMIS))
    if inconnus:
        raise Refus(f"déclaration des relais : fournisseurs inconnus {inconnus}")
    for requis in ("claude", "argon"):
        if requis not in f_decl:
            raise Refus(f"déclaration des relais : « {requis} » exigé (proposeurs Claude d'abord ; juge et lecteur Argon)")
    metas: dict = {}
    blocs, cles, modeles, carbon = {}, {}, {}, {"inscrite": INSCRIPTION_CARBON, "active": False, "motif": None}
    for nom, b in sorted(f_decl.items()):
        if not isinstance(b, dict):
            raise Refus(f"fournisseurs.{nom} : objet attendu")
        t = TYPES_PERMIS[nom]
        if b.get("type") != t:
            raise Refus(f"fournisseurs.{nom}.type : {t!r} exigé (reçu {b.get('type')!r})")
        en_trop = sorted(set(b) - CLES_PERMISES[t] - CLES_META)
        if en_trop:
            raise Refus(f"fournisseurs.{nom} : clés non permises {en_trop}")
        nom_cle = b.get("nom_cle")
        if not isinstance(nom_cle, str) or not NOM_DE_VARIABLE.match(nom_cle):
            raise Refus(f"fournisseurs.{nom}.nom_cle : nom de variable exigé (le nom seul, jamais la valeur)")
        if nom_cle in CLES_INTERDITES:
            raise Refus(f"fournisseurs.{nom}.nom_cle = {nom_cle} : clé exclue de cette course (R-3228, elle garde son reste)")
        if nom == "claude" and nom_cle != CLE_CLAUDE:
            raise Refus(f"fournisseurs.claude.nom_cle = {nom_cle} : tous les appels Claude passent par {CLE_CLAUDE} (R-3228)")
        if nom != "claude" and nom_cle.startswith(PREFIXE_CLES_CLAUDE):
            raise Refus(f"fournisseurs.{nom}.nom_cle = {nom_cle} : une clé de la famille Claude sur un autre relais est refusée")
        pp = b.get("porte_plafond")
        if not isinstance(pp, dict) or pp.get("type") not in ("commande", "environnement"):
            raise Refus(f"fournisseurs.{nom}.porte_plafond : {{type: commande|environnement}} exigé (A15, brouillon 10)")
        if t == "commande_externe" and pp["type"] != "environnement":
            raise Refus(f"fournisseurs.{nom}.porte_plafond : « environnement » exigé pour une commande externe")
        if t != "commande_externe":
            if pp["type"] != "commande" or not isinstance(pp.get("commande"), list) or not pp["commande"] \
                    or not all(isinstance(x, str) and x for x in pp["commande"]):
                raise Refus(f"fournisseurs.{nom}.porte_plafond : commande (liste non vide) exigée pour un relais persistant")
            if not isinstance(pp.get("delai_s"), (int, float)) or isinstance(pp.get("delai_s"), bool) or pp["delai_s"] <= 0:
                raise Refus(f"fournisseurs.{nom}.porte_plafond.delai_s : nombre > 0 exigé")
            if not isinstance(b.get("url_relais"), str) or not URL_LOCALE.match(b["url_relais"]):
                raise Refus(f"fournisseurs.{nom}.url_relais : adresse de boucle locale exigée (http://127.0.0.1:PORT)")
        if nom == "argon":
            attendue = ["bash", str(r.depot / PIECES["enveloppe_argon"][0])]
            if b.get("commande") != attendue:
                raise Refus(f"fournisseurs.argon.commande : {attendue} exigée (enveloppe épinglée)")
        if nom in ("astra", "carbon"):
            m = b.get("modele_propose")
            motif = next(e.get("motif_modele") for e in fixe["especes"] if e["fournisseur"] == nom)
            if not isinstance(m, str) or motif not in m.lower() or "claude" in m.lower() or not re.fullmatch(r"[a-z0-9.\-]+", m):
                raise Refus(f"fournisseurs.{nom}.modele_propose : identifiant de modèle qui contient « {motif} » exigé")
            if not isinstance(b.get("commande"), list) or not b["commande"]:
                raise Refus(f"fournisseurs.{nom}.commande : liste non vide exigée")
            c = b["commande"]
            epingles = COMMANDES_EPINGLEES.get(nom) or {}
            if len(c) < 4 or not os.path.isabs(c[0]) or c[1:3] != ["-I", "-B"] or os.path.basename(c[3]) not in epingles \
                    or not os.path.isfile(c[3]) or sha256_fichier(Path(c[3])) != epingles[os.path.basename(c[3])]:
                raise Refus(f"fournisseurs.{nom}.commande : « python -I -B <commande épinglée> » exigé, à l'empreinte épinglée "
                            f"({sorted(epingles)})")
            if c[4:] != ARGUMENTS_COMMANDES[nom]:
                raise Refus(f"fournisseurs.{nom}.commande : arguments différents des arguments épinglés {ARGUMENTS_COMMANDES[nom]}")
            if m != MODELES_RELAIS[nom][0]:
                raise Refus(f"fournisseurs.{nom}.modele_propose : {MODELES_RELAIS[nom][0]} exigé")
            modeles[nom] = m
        if nom == "kimi" and b.get("modele") != "kimi-k3.1-pro":
            raise Refus("fournisseurs.kimi.modele : « kimi-k3.1-pro » exigé (configuration fixe)")
        if nom == "kimi":
            controler_kimi(b)
            mot = decl.get("kimi_autorise_par_la_mere")
            if not (isinstance(mot, dict) and isinstance(mot.get("reference"), str) and re.fullmatch(r"R-\d{3,5}", mot["reference"])):
                raise Refus("fournisseurs.kimi : Kimi n'est pas déclaré par défaut (A14 : 6 appels inexploitables sur 16 rendent "
                            "l'étape « non mesurée (technique) ») ; il faut le mot écrit de la mère dans la déclaration : "
                            "\"kimi_autorise_par_la_mere\": {\"reference\": \"R-NNNN\"}")
            if mot["reference"] not in tuple(r.references_kimi_admises):  # v7, mineur 9 : la forme ne suffit plus
                raise Refus(f"fournisseurs.kimi : référence {mot['reference']} non admise par ce lanceur (admises : "
                            f"{list(r.references_kimi_admises) or 'aucune'} ; R-3279 : Kimi non déclaré) ; une autorisation de "
                            "la mère s'inscrit dans une version suivante du lanceur")
        if nom == "carbon":
            if b.get("inscription") != INSCRIPTION_CARBON:
                carbon["motif"] = f"inscription {b.get('inscription')!r} : {INSCRIPTION_CARBON} exigée ; Carbon non active"
                continue
            carbon.update(active=True, motif="inscrite (R-3217), relais et clé nommés dans la déclaration")
        elif "inscription" in b:
            raise Refus(f"fournisseurs.{nom}.inscription : clé réservée à Carbon")
        blocs[nom] = {k: v for k, v in b.items() if k not in CLES_META}
        metas[nom] = {k: v for k, v in b.items() if k in CLES_META}
        cles[nom] = nom_cle
    if "carbon" not in f_decl:
        carbon["motif"] = "relais et clé non nommés dans la déclaration : course sans Carbon"
    actives, absentes = [], []
    for e in sorted(fixe["especes"], key=lambda x: x["ordre"]):
        if e["fournisseur"] in blocs:
            actives.append(dict(e, modele=e["modele"] or modeles[e["fournisseur"]]))
        else:
            absentes.append({"etiquette": e["etiquette"], "motif": "relais non déclaré" if e["fournisseur"] != "carbon" else carbon["motif"]})
    return {"fournisseurs": blocs, "especes_actives": actives, "especes_absentes": absentes, "cles": cles, "carbon": carbon, "metas": metas,
            "absences": decl.get("absences") if isinstance(decl.get("absences"), dict) else None,
            "kimi_autorise_par_la_mere": decl.get("kimi_autorise_par_la_mere"),
            "compter_limite_de_debit_comme_soupcon": verifier_choix_limite(decl)}


# --- (2) relevé du crédit de chaque clé ---------------------------------------------------------------------------------------


def _reel_positif(v) -> bool:
    return isinstance(v, (int, float)) and not isinstance(v, bool) and v >= 0


def verifier_choix_limite(decl: dict) -> bool:
    """5 : choix de la mère sur la limite de débit dans la garde de crédit ; vrai par défaut (lettre de la v5)."""
    v = decl.get("compter_limite_de_debit_comme_soupcon", True)
    if not isinstance(v, bool):
        raise Refus("compter_limite_de_debit_comme_soupcon : booléen exigé (vrai par défaut)")
    return v


def controler_kimi(bloc: dict) -> None:
    """Constat 3 : les contrôles de l'adaptateur `adaptateur_kimi_v53` (l. 62-69), repris avant le départ."""
    for k in ("prix_entree", "prix_sortie", "delai_s"):
        v = bloc.get(k)
        if not (isinstance(v, (int, float)) and not isinstance(v, bool) and v > 0):
            raise Refus(f"fournisseurs.kimi.{k} : réel > 0 exigé, comme l'adaptateur de Kimi")
    for k in ("max_sortie_jetons", "sortie_min_jetons"):
        v = bloc.get(k)
        if not (isinstance(v, int) and not isinstance(v, bool) and v >= 1):
            raise Refus(f"fournisseurs.kimi.{k} : entier ≥ 1 exigé, comme l'adaptateur de Kimi")
    if bloc["sortie_min_jetons"] > bloc["max_sortie_jetons"]:
        raise Refus("fournisseurs.kimi : sortie_min_jetons > max_sortie_jetons")


def borne_appel_kimi(bloc: dict, octets_entree_max: int, plafond_session: float) -> float:
    """Pire coût d'un appel de Kimi (formule de l'adaptateur `adaptateur_kimi_v53`) : (octets du corps + 1024) × prix d'entrée
    + max_tokens × prix de sortie, borné par le plafond de session ; prix en USD par million de jetons."""
    for k in ("prix_entree", "prix_sortie", "max_sortie_jetons"):
        if not _reel_positif(bloc.get(k)):
            raise Refus(f"fournisseurs.kimi.{k} : nombre ≥ 0 exigé pour la part au pire")
    brut = ((octets_entree_max + 1024) * bloc["prix_entree"] + bloc["max_sortie_jetons"] * bloc["prix_sortie"]) / 1e6
    return round(min(brut, plafond_session), 6)


def parts_au_pire(fixe: dict, liste: dict, pieces: dict, decl: dict) -> dict:
    """Part au pire de chaque relais (donc de chaque clé) dans cette course, en USD (R-3237, point 1) :
    - relais qui tient l'aiguilleur ou un juge (Claude, Argon) : le nombre de cartes n'est borné par aucun programme, la seule
      borne dure est le plafond d'arrêt : 150 USD ;
    - relais de proposeur seulement : 16 appels × pire coût d'un appel (plafond de session ; pour Kimi, la formule de son
      adaptateur sur l'entrée la plus longue de la course, si elle est plus basse)."""
    actives = decl["especes_actives"]
    ps = fixe["plafonds_session"]
    internes = {fixe["aiguilleur"]["fournisseur"]} | {j["fournisseur"] for j in fixe["juges"]}
    consigne = Path(pieces["consigne_proposeur"]["absolu"]).read_bytes()
    entree_max = len(consigne) + max(len(texte_de_case(f).encode("utf-8")) for f in liste["fils"]) + 200
    parts = {}
    for f in sorted({e["fournisseur"] for e in actives} | internes):
        if f in internes:
            parts[f] = {"part_au_pire_usd": PLAFOND_ARRET_USD, "regle": "aiguilleur ou juge : cartes non bornées, plafond d'arrêt"}
            continue
        n = len(liste["fils"]) * sum(1 for e in actives if e["fournisseur"] == f)
        par_appel = float(ps["proposeur"])
        regle = f"{n} appels × plafond de session {par_appel}"
        if f == "kimi":
            par_appel = borne_appel_kimi(decl["fournisseurs"]["kimi"], entree_max, float(ps["proposeur"]))
            regle = f"{n} appels × pire coût d'un appel de Kimi (formule de son adaptateur, entrée ≤ {entree_max} octets)"
        parts[f] = {"part_au_pire_usd": round(min(n * par_appel, PLAFOND_ARRET_USD), 6), "par_appel_usd": par_appel, "regle": regle}
    return parts


def verifier_credits(releve: dict, cles: dict, aujourd_hui: _dt.date, dossier_alerte: Path, parts: dict | None = None) -> dict:
    """v3 (R-3237). Rend {nom_cle: {...}}.
    - Relevé du jour exigé ; chaque clé employée y figure (« non lisible » s'écrit).
    - Non lisible : Minuit compté au prix relevé (v2) ; Argon, Astra, Carbon seulement sous la dispense écrite de la mère
      citant R-3237 (départ permis, arrêt au premier refus pour crédit) ; toute autre clé : refus.
    - Lisible : alerte et arrêt avant le départ (code 3) si reste < sa part au pire, ou reste < un cinquième du crédit ;
      Kimi : part au pire + 11,3 USD > 90 % du reste → refus (les deux courses se suivent)."""
    parts = parts or {}
    quand = str(releve.get("releve_utc") or "")
    if not quand.startswith(aujourd_hui.isoformat()):
        raise Refus(f"relevé des crédits du {quand!r} : un relevé du jour ({aujourd_hui}) est exigé")
    instant_du_releve(releve)  # v7 : heure lisible exigée (comparée à la fin d'une autre course de l'organisme)
    lignes = releve.get("cles")
    if not isinstance(lignes, dict):
        raise Refus("relevé des crédits : « cles » (objet) exigé")
    dispense = releve.get("dispense") or {}
    dispensees = set(dispense.get("cles") or []) if dispense.get("par") == "mère" and dispense.get("reference") == REFERENCE_DISPENSE else set()
    sortie, alertes = {}, []
    groupes: dict = {}
    for f, n in sorted(cles.items()):
        groupes.setdefault(n, []).append(f)
    for nom, fours in sorted(groupes.items()):
        fournisseur = "+".join(fours)  # 7 : une clé partagée (Argon et Carbon) porte la somme des parts au pire
        x = lignes.get(nom)
        parts_k = [(parts.get(f) or {}).get("part_au_pire_usd") for f in fours]
        part = None if any(q is None for q in parts_k) else round(sum(parts_k), 6)
        if nom == CLE_CLAUDE and isinstance(x, dict) and x.get("non_lisible") is True:
            anterieure = x.get("depense_anterieure_usd")
            if not _reel_positif(anterieure):
                raise Refus(f"crédit de {nom} non lisible : depense_anterieure_usd (≥ 0) exigée pour le compter au prix relevé")
            x = {"credit_usd": CREDIT_DECLARE_CLE_CLAUDE_USD, "reste_usd": max(0.0, CREDIT_DECLARE_CLE_CLAUDE_USD - anterieure),
                 "source": "compté au prix relevé : crédit déclaré 200 USD (R-3228) moins la dépense antérieure déclarée"}
        if not isinstance(x, dict):
            raise Refus(f"relevé des crédits : clé {nom} ({fournisseur}) absente — « non lisible » s'écrit, il ne s'omet pas")
        if x.get("non_lisible") is True:
            if any(f not in FOURNISSEURS_DISPENSABLES for f in fours):
                raise Refus(f"crédit de la clé {nom} ({fournisseur}) non lisible : seules les clés d'Argon, d'Astra et de Carbon "
                            "peuvent partir sous dispense (R-3237)")
            if nom not in dispensees:
                raise Refus(f"crédit de la clé {nom} ({fournisseur}) non lisible et sans dispense écrite de la mère citant "
                            f"{REFERENCE_DISPENSE} : aucun départ")
            sortie[nom] = {"fournisseur": fournisseur, "relais": fours, "parts_par_relais": dict(zip(fours, parts_k)),
                           "lisible": False, "motif": x.get("motif"), "dispense": dispense, "part_au_pire_usd": part, "regle": "arrêt de la course au premier refus pour crédit (R-3237)"}
            continue
        credit, reste = x.get("credit_usd"), x.get("reste_usd")
        if not (_reel_positif(credit) and _reel_positif(reste)) or reste > credit:
            raise Refus(f"relevé des crédits : clé {nom} : credit_usd et reste_usd (nombres ≥ 0, reste ≤ crédit) exigés")
        if part is None:
            raise Refus(f"part au pire du relais {fournisseur} inconnue : aucun départ")
        d = {"fournisseur": fournisseur, "relais": fours, "parts_par_relais": dict(zip(fours, parts_k)), "lisible": True,
             "credit_usd": credit, "reste_usd": reste, "source": x.get("source"), "part_au_pire_usd": part, "cinquieme_usd": credit / 5.0}
        motifs = []
        if reste <= part:
            motifs.append(f"reste {reste} ≤ part au pire {part} (à l'égalité, le pire cas laisse zéro)")
        if reste < credit / 5.0:
            motifs.append(f"reste {reste} < un cinquième du crédit {credit / 5.0}")
        if "kimi" in fours and part + KIMI_COURSE_SUIVANTE_PIRE_USD > KIMI_PART_DU_RESTE * reste:
            motifs.append(f"part au pire {part} + {KIMI_COURSE_SUIVANTE_PIRE_USD} (course Kimi de la relance) > 90 % du reste "
                          f"({round(KIMI_PART_DU_RESTE * reste, 6)}) : les deux courses doivent se suivre, solde relu avant chacune")
        d["motifs_d_arret"] = motifs
        sortie[nom] = d
        if motifs:
            alertes.append({"cle": nom, "fournisseur": fournisseur, "reste_usd": reste, "credit_usd": credit, "part_au_pire_usd": part,
                            "motifs": motifs})
    if alertes:
        texte = {"alerte": "crédit insuffisant pour la part au pire d'une clé, avant la course d'affinage des idées des mentors : "
                           "départ refusé",
                 "regle": "R-3237 : chaque clé confrontée à sa part au pire ; un cinquième du crédit ; Kimi : part + 11,3 USD ≤ 90 % "
                          "du reste, sinon les deux courses se suivent et le solde est relu avant chacune ; Lazar à prévenir "
                          "avant qu'une clé n'atteigne zéro",
                 "cles": alertes, "pour": "la mère (à transmettre à Lazar)"}
        dossier_alerte.mkdir(parents=True, exist_ok=True)
        chemin = dossier_alerte / "alerte-credits-avant.json"
        if not chemin.exists():
            ecrire_scelle(chemin, texte)
        raise AlerteCredit(json.dumps(dict(texte, fichier=str(chemin)), ensure_ascii=False))
    return sortie


def instant_du_releve(releve: dict) -> _dt.datetime:
    """v7 : heure du relevé (« AAAA-MM-JJTHH:MM:SSZ », celle de `date -u +%FT%TZ`), en UTC ; illisible : refus."""
    m = re.match(r"^(\d{4}-\d{2}-\d{2})T(\d{2}):(\d{2}):(\d{2})Z", str(releve.get("releve_utc") or ""))
    if not m:
        raise Refus(f"relevé des crédits : releve_utc {releve.get('releve_utc')!r} illisible (« AAAA-MM-JJTHH:MM:SSZ » exigé, "
                    "date -u +%FT%TZ)")
    try:
        return _dt.datetime.fromisoformat(f"{m.group(1)}T{m.group(2)}:{m.group(3)}:{m.group(4)}+00:00")
    except ValueError:
        raise Refus(f"relevé des crédits : releve_utc {releve.get('releve_utc')!r} illisible") from None


def verifier_autres_courses(r: "Reglages", releve: dict) -> dict:
    """v7, majeur 2 : la course d'auto-conception partage les ports 8787 à 8793, la clé Minuit (et celles de Google et
    d'OpenAI) et la sonde d'Astra. Refus si l'une de ses courses a un manifeste de départ sans manifeste de fin (en cours, ou
    interrompue sans fin écrite : à éclaircir avant tout départ), ou si le relevé des crédits n'est pas postérieur à la fin
    (date du manifeste de fin) de chacune de ses courses versées : il faut le refaire après elle, avec sa dépense réelle."""
    vues = []
    if not r.dossier_runs.is_dir():
        return {"autres_courses": vues}
    quand = instant_du_releve(releve)
    for p in sorted(r.dossier_runs.iterdir()):
        if not (p.is_dir() and MOTIF_AUTRE_COURSE.search(p.name) and (p / "manifeste-lanceur-depart.json").exists()):
            continue
        fin = p / "manifeste-lanceur-fin.json"
        if not fin.exists():
            raise Refus(f"course d'auto-conception {p.name} partie sans manifeste de fin : les deux courses ne tournent jamais en "
                        "même temps (ports 8787 à 8793, clés et sonde communs) ; attendre sa fin, arrêter ses relais par leur "
                        "PID, refaire le relevé des crédits")
        fini = _dt.datetime.fromtimestamp(fin.stat().st_mtime, _dt.timezone.utc)
        if quand <= fini:
            raise Refus(f"relevé des crédits du {quand.isoformat()} antérieur à la fin de la course d'auto-conception {p.name} "
                        f"({fini.isoformat()}) : relevé à refaire après elle, avec sa dépense réelle (clé Minuit comprise)")
        vues.append({"run": p.name, "fin_utc": fini.isoformat()})
    return {"autres_courses": vues, "releve_utc": quand.isoformat()}


# --- (R-3237, 3) procédure neutre des relais persistants ; (R-3237, 2) garde de crédit des relais dispensés ----------------


def modeles_du_fournisseur(fixe: dict, nom: str) -> list:
    if nom == "claude":
        return sorted(e["modele"] for e in fixe["especes"] if e["famille"] == "claude")
    return list(MODELES_RELAIS[nom])


def verifier_procedure_relais(r: "Reglages", decl: dict, pieces: dict, fixe: dict | None = None, parts: dict | None = None) -> dict:
    """Moteur réel : pièce de la procédure épinglée ; commande de chaque porte « commande » = « python -I -B porte » et ses
    arguments recoupés avec la déclaration et la configuration (v5, constat 2) ; **chaque** relais déclaré vivant contrôlé
    par son PID et par `/relais/etat` (v5, constat 4 ; B ; C)."""
    fixe = fixe or {"especes": []}
    o = json.loads(Path(pieces["procedure_relais"]["absolu"]).read_text(encoding="utf-8"))
    for cle_chemin, cle_sha, piece in (("chemin", "sha256", "lanceur_relais"), ("procedure_ecrite", "procedure_ecrite_sha256", "procedure_ecrite")):
        if o.get(cle_sha) != pieces[piece]["sha256"]:
            raise Refus(f"pièce de la procédure : {cle_chemin} d'une autre empreinte que la pièce épinglée {piece}")
    porte = pieces["porte_plafond"]["absolu"]
    relais = {}
    n_especes = len(decl["especes_actives"])
    for nom, b in sorted(decl["fournisseurs"].items()):
        pp = b.get("porte_plafond") or {}
        meta = decl.get("metas", {}).get(nom, {})
        if pp.get("type") == "commande":
            c = pp.get("commande") or []
            if len(c) < 4 or not os.path.isabs(c[0]) or c[1:3] != ["-I", "-B"] or c[3] != porte:
                raise Refus(f"fournisseurs.{nom}.porte_plafond : la commande doit commencer par « python -I -B {porte} » (constat 1)")
            reste = c[4:]
            try:
                plafond_ligne = float(_valeur_arg(reste, "--plafond-ligne"))
            except (TypeError, ValueError):
                plafond_ligne = None
            if _valeur_arg(reste, "--url") != b.get("url_relais"):
                raise Refus(f"fournisseurs.{nom}.porte_plafond : --url différent de l'adresse déclarée du relais (v5, constat 2)")
            mp = sorted(x for x in (_valeur_arg(reste, "--modeles-permis") or "").split(",") if x)
            if mp != modeles_du_fournisseur(fixe, nom):
                raise Refus(f"fournisseurs.{nom}.porte_plafond : --modeles-permis différents des modèles de la configuration (v5, constat 2)")
            if plafond_ligne != PLAFOND_ARRET_USD:
                raise Refus(f"fournisseurs.{nom}.porte_plafond : --plafond-ligne doit valoir {PLAFOND_ARRET_USD} (v5, constat 2)")
        relais[nom] = controler_relais_vivant(r, nom, dict(b, **meta), fixe, n_especes, parts)
    return {"procedure": o.get("procedure_ecrite"), "lanceur_relais": o.get("chemin"), "porte": porte, "relais_vivants": relais,
            "note": "la note de la pièce v3 (« chaque porte lance le lanceur de relais ») est périmée depuis la v4 : la porte "
                    "épinglée ouvre chaque commande de porte"}


def _cmdline(pid: int) -> list:
    with open(f"/proc/{int(pid)}/cmdline", "rb") as f:
        return [x.decode("utf-8", "replace") for x in f.read().split(b"\0") if x]


def _valeur_arg(args: list, nom: str):
    return args[args.index(nom) + 1] if nom in args and args.index(nom) + 1 < len(args) else None


def _valeurs_arg(args: list, nom: str) -> list:
    return [args[k + 1] for k, a in enumerate(args) if a == nom and k + 1 < len(args)]


def _etat_relais(url: str) -> dict:
    import urllib.request
    ouvreur = urllib.request.build_opener(urllib.request.ProxyHandler({}))
    with ouvreur.open(url.rstrip("/") + "/relais/etat", timeout=5) as rep:
        return json.loads(rep.read().decode("utf-8"))


def _port_du_fournisseur(nom: str, b: dict):
    if nom == "argon":
        return str(PORT_ARGON)
    if nom in ("astra", "carbon"):
        url = ARGUMENTS_COMMANDES[nom][ARGUMENTS_COMMANDES[nom].index("--url-relais" if nom == "astra" else "--url-base") + 1]
    else:
        url = b.get("url_relais") or ""
    m = re.search(r":(\d+)", url)
    return m.group(1) if m else None


def _entier_arg(args: list, option: str, nom: str) -> int:
    """v7 : borne lue sur la ligne de commande ; absente ou illisible : refus (aucun défaut du relais n'est supposé)."""
    v = _valeur_arg(args, option)
    if v is None:
        raise Refus(f"relais {nom} : {option} absent des arguments lus par PID (borne basse exigée, aucun défaut supposé)")
    try:
        return int(v)
    except ValueError:
        raise Refus(f"relais {nom} : {option} illisible ({v!r})") from None


def _nombre(v) -> bool:
    return isinstance(v, (int, float)) and not isinstance(v, bool) and v == v and v not in (float("inf"), float("-inf"))


def controler_relais_vivant(r: "Reglages", nom: str, b: dict, fixe: dict | None = None, n_especes: int = 6,
                            parts: dict | None = None) -> dict:
    """Arguments du relais lus par PID (jamais son environnement) et état lu sur `/relais/etat` : programme épinglé par la
    procédure, variable de la clé déclarée, port attendu, modèles permis égaux à ceux de la configuration ; v7 (majeur 1) :
    bornes basses de **tous** les relais — Claude : plafond 150 ; Astra, Kimi : `--max-appels` ≥ 20, plafond ≥ la part au pire
    (Astra : égal), réserve par appel ≤ plafond de session d'un proposeur, prix de l'état égaux à ceux de la commande ; Argon :
    `--max-appels` ≥ 2 × (16 + 32 × espèces) ; Carbon : `--max-lots` ≥ 20, `--max-appels` ≥ 40 ; bornes de l'état égales aux
    arguments ; variable de clé effacée (relais Gemini, Astra, Kimi) ; v7 (mineur 3) : état neuf **lu** — « appels » présent et
    nul ; « depense_usd » et « engage_usd » présents et nuls pour les relais à plafond en dollars ; « lots_crees » nul pour
    Carbon ; un état vide est refusé."""
    fixe = fixe or {"especes": []}
    pid = b.get("pid_relais")
    if not isinstance(pid, int) or isinstance(pid, bool) or pid <= 1:
        raise Refus(f"fournisseurs.{nom}.pid_relais : PID du relais vivant exigé (lancé par le lanceur de relais)")
    try:
        args = (r.lire_cmdline or _cmdline)(pid)
    except (OSError, KeyError):
        raise Refus(f"relais {nom} : PID {pid} absent") from None
    nom_prog, attendu = (r.programmes_relais or PROGRAMMES_RELAIS)[nom]
    progs = [a for a in args if os.path.basename(a) == nom_prog]
    if len(progs) != 1 or not os.path.isfile(progs[0]) or sha256_fichier(Path(progs[0])) != attendu:
        raise Refus(f"relais {nom} : programme {nom_prog} absent des arguments ou d'une autre empreinte que celle de la procédure")
    variable = _valeur_arg(args, "--variable-cle") or ("GEMINI_API_KEY" if nom in GEMINI else None)
    if variable != b["nom_cle"]:
        raise Refus(f"relais {nom} : lancé sur la variable {variable!r}, {b['nom_cle']} déclarée")
    port = _port_du_fournisseur(nom, b)
    if not port or _valeur_arg(args, "--port") != port:
        raise Refus(f"relais {nom} : port des arguments ({_valeur_arg(args, '--port')!r}) différent du port attendu ({port})")
    modeles_attendus = modeles_du_fournisseur(fixe, nom)
    if nom in GEMINI:
        modeles_args = sorted(_valeurs_arg(args, "--modele"))
    else:
        modeles_args = sorted(x for x in (_valeur_arg(args, "--modeles-permis") or "").split(",") if x)
    if modeles_args != modeles_attendus:
        raise Refus(f"relais {nom} : modèles permis des arguments {modeles_args} différents de la configuration (v5, constat 2)")
    out = {"pid": pid, "programme": progs[0], "programme_sha256": attendu, "variable_cle": variable, "port": port,
           "modeles": modeles_args}
    egal_a_l_etat: dict = {}  # bornes que /relais/etat doit rendre à l'identique des arguments (v7)
    if nom in GEMINI:
        max_appels = _entier_arg(args, "--max-appels", nom)
        minimum = 2 * (16 + 32 * n_especes) if nom == "argon" else MIN_APPELS_CARBON
        if max_appels < minimum:
            raise Refus(f"relais {nom} : --max-appels {max_appels} < {minimum} (comptes de jetons compris ; v7 : marge de "
                        f"{MARGE_APPELS_PROPOSEUR} lots pour Carbon)")
        out["max_appels"] = egal_a_l_etat["max_appels"] = max_appels
        if nom == "carbon":
            max_lots = _entier_arg(args, "--max-lots", nom)
            if max_lots < MIN_LOTS_CARBON:
                raise Refus(f"relais carbon : --max-lots {max_lots} < {MIN_LOTS_CARBON} (16 propositions + marge de "
                            f"{MARGE_APPELS_PROPOSEUR})")
            out["max_lots"] = egal_a_l_etat["max_lots"] = max_lots
    else:
        try:
            plafond = float(_valeur_arg(args, "--plafond-usd"))
        except (TypeError, ValueError):
            raise Refus(f"relais {nom} : --plafond-usd absent des arguments") from None
        if not _nombre(plafond) or plafond <= 0 or plafond > PLAFOND_ARRET_USD or (nom == "claude" and plafond != PLAFOND_ARRET_USD):
            raise Refus(f"relais {nom} : plafond {plafond} hors règle (≤ 150 ; Claude : 150, relais de ligne entière)")
        out["plafond_usd"] = egal_a_l_etat["plafond_usd"] = plafond
        if nom in ("kimi", "astra"):
            part = ((parts or {}).get(nom) or {}).get("part_au_pire_usd")
            if not _nombre(part) or part <= 0:
                raise Refus(f"relais {nom} : part au pire inconnue : borne basse du plafond non contrôlable")
            if plafond < part - 1e-9:
                raise Refus(f"relais {nom} : plafond {plafond} < part au pire {part} USD : les derniers appels seraient refusés "
                            "(402) et l'étape « proposition » perdue (v7, majeur 1)")
            if nom == "astra" and plafond > part + 1e-9:
                raise Refus(f"relais astra : plafond {plafond} > part au pire {part} USD : la barrière du relais doit égaler la "
                            "part de la clé (16 × plafond de session)")
            max_appels = _entier_arg(args, "--max-appels", nom)
            if max_appels < MIN_APPELS_RELAIS_PROPOSEUR:
                raise Refus(f"relais {nom} : --max-appels {max_appels} < {MIN_APPELS_RELAIS_PROPOSEUR} ({APPELS_PAR_PROPOSEUR} "
                            f"cases + marge de {MARGE_APPELS_PROPOSEUR}) (v7, majeur 1)")
            out["max_appels"] = egal_a_l_etat["max_appels"] = max_appels
            out["part_au_pire_usd"] = part
    try:
        etat = (r.lire_etat_relais or _etat_relais)(f"http://127.0.0.1:{port}")
    except Exception as e:  # noqa: BLE001
        raise Refus(f"relais {nom} : /relais/etat illisible ({type(e).__name__})") from None
    if not isinstance(etat, dict):
        raise Refus(f"relais {nom} : /relais/etat n'est pas un objet")
    champs = ("appels",) + (("depense_usd", "engage_usd") if nom in RELAIS_A_DOLLARS else ()) + (("lots_crees",) if nom == "carbon" else ())
    absents = [k for k in champs if k not in etat]
    if absents:
        raise Refus(f"relais {nom} : /relais/etat sans {absents} : état non reconnu (autre service, réponse tronquée ?) — "
                    "un relais neuf lisible est exigé (v7, mineur 3)")
    if any(not _nombre(etat[k]) or etat[k] != 0 for k in champs):
        raise Refus(f"relais {nom} : relais déjà employé ({ {k: etat[k] for k in champs} }) : un relais neuf est exigé")
    if "pid" in etat and etat["pid"] != pid:
        raise Refus(f"relais {nom} : /relais/etat rend le PID {etat['pid']!r}, {pid} déclaré")
    for k, v in sorted(egal_a_l_etat.items()):
        lu = etat.get(k)
        if not _nombre(lu) or abs(float(lu) - float(v)) > 1e-9:
            raise Refus(f"relais {nom} : /relais/etat rend {k} = {lu!r}, les arguments lus par PID {v!r} (v7)")
    if nom in GEMINI + ("kimi", "astra") and etat.get("variable_cle_encore_presente") is not False:
        raise Refus(f"relais {nom} : variable de clé non effacée de son environnement (variable_cle_encore_presente "
                    f"{etat.get('variable_cle_encore_presente')!r})")
    if nom in ("kimi", "astra"):
        session = ((fixe or {}).get("plafonds_session") or {}).get("proposeur")
        reserve = etat.get("reserve_par_appel_usd")
        if not (_nombre(session) and _nombre(reserve) and 0 <= reserve <= session):
            raise Refus(f"relais {nom} : réserve par appel {reserve!r} USD hors de [0, plafond de session {session!r}] : "
                        "les derniers appels seraient refusés (402)")
        if nom == "astra":  # Kimi : refusé à la déclaration en v7 (liste des références admises vide) ; prix non recoupés
            a = ARGUMENTS_COMMANDES["astra"]
            prix = (float(a[a.index("--prix-entree") + 1]), float(a[a.index("--prix-sortie") + 1]))
            lus = (etat.get("prix_entree_usd_par_million"), etat.get("prix_sortie_usd_par_million"))
            if not all(_nombre(x) for x in lus) or tuple(float(x) for x in lus) != prix:
                raise Refus(f"relais {nom} : prix de l'état {lus!r} différents de ceux de la commande {prix!r} (la barrière en "
                            "dollars du relais compterait faux)")
        out["reserve_par_appel_usd"] = reserve
    out["etat_neuf"] = True
    return out


def porte_a_blanc(decl: dict) -> dict:
    """Constat 1 : chaque porte « commande » est jouée une fois avant le manifeste de départ, avec l'environnement minimal du
    contrat (`PortePlafondCommande`) et l'étape « porte-a-blanc » ; aucun appel au fournisseur ; accusé exigé au centime."""
    sortie = {}
    for nom, b in sorted(decl["fournisseurs"].items()):
        pp = b.get("porte_plafond") or {}
        if pp.get("type") != "commande":
            continue
        env = {"PATH": os.environ.get("PATH", os.defpath), "LANG": "C.UTF-8", "ETAPE_POLE": ETAPE_A_BLANC,
               "PLAFOND_ETAPE_USD": "1.00"}
        try:
            p = subprocess.run(pp["commande"], env=env, capture_output=True, text=True, timeout=float(pp["delai_s"]),
                               stdin=subprocess.DEVNULL)
        except (OSError, subprocess.SubprocessError) as e:
            raise Refus(f"porte à blanc de {nom} non jouée ({type(e).__name__})") from None
        lignes = [x for x in p.stdout.splitlines() if x.strip()]
        try:
            accuse = json.loads(lignes[-1]) if lignes else None
        except ValueError:
            accuse = None
        if p.returncode != 0 or not isinstance(accuse, dict) or accuse.get("etape") != ETAPE_A_BLANC \
                or round(float(accuse.get("plafond_usd") or -1), 2) != 1.00:
            raise Refus(f"porte à blanc de {nom} refusée (code {p.returncode}) : {(p.stderr or p.stdout).strip()[-300:]!r}")
        sortie[nom] = {"accuse": accuse, "code": 0}
    return sortie


# --- constat 2 : registre des GO dérivé ; constat 5 : prix Claude du jour -------------------------------------------------------


def verifier_registre_main(r: "Reglages") -> str | None:
    """v5, constat 5 (R-3249) : le registre lu est celui de `main` (le dépôt de travail mis à jour sur `origin/main`, récupérée
    avant) ; rend le commit source, cité par le registre dérivé. Sans référence (essais) : None."""
    if not r.ref_registre:
        return None
    commit = _git(r.depot, "rev-parse", r.ref_registre).strip()
    p = subprocess.run(["git", "-C", str(r.depot), "show", f"{r.ref_registre}:registres/go.md"], capture_output=True, timeout=60)
    if p.returncode != 0 or not r.registre_go.is_file() or p.stdout != r.registre_go.read_bytes():
        raise Refus(f"registre des GO du dépôt différent de celui de {r.ref_registre} ({commit[:8]}) : se mettre à jour sur main")
    return commit


def ecrire_registre_derive(registre: Path, chemin: Path, go_id: str = GO_ID, commit: str | None = None) -> dict:
    """Lit le registre source par lignes nommées seulement (la ligne du GO et les révocations qui la visent) et écrit, scellé,
    un registre dérivé que la lecture de l'orchestrateur accepte (aucun identifiant en double)."""
    gardees = []
    for ligne in registre.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^\|\s*(GO-\d{4}-\d{2}-\d{2}-\d{2})\s*\|", ligne)
        if not m:
            continue
        cellules = [c.strip() for c in ligne.strip().strip("|").split("|")]
        if m.group(1) == go_id and not (len(cellules) == 8 and cellules[3].lower().startswith("extension")):
            gardees.append(ligne)
        elif len(cellules) == 8 and cellules[2] == "révocation" and go_id in (cellules[3] + cellules[7]):
            gardees.append(ligne)
    texte = ("# Registre des GO dérivé (course d'affinage, lanceur v5) — lignes nommées seulement\n\n"
             f"Source : `registres/go.md` de main au commit {commit or 'non cité (essai)'} (R-3249).\n\n"
             "| id | accordé le | type | périmètre | plafond | échéance | accordé par | référence |\n"
             "|---|---|---|---|---|---|---|---|\n" + "\n".join(gardees) + "\n")
    h = ecrire_scelle(chemin, texte)
    return {"source": str(registre), "source_sha256": sha256_fichier(registre), "commit_source": commit, "derive": str(chemin),
            "derive_sha256": h,
            "lignes": [hashlib.sha256(l.encode("utf-8")).hexdigest() for l in gardees], "nombre_de_lignes": len(gardees)}


def verifier_releve_prix(chemin: Path, fixe: dict, aujourd_hui: _dt.date) -> dict:
    """Constat 5 (condition de GO-2026-11-18-14 : « prix Claude relevé avant le départ ») : fichier du jour, scellé, prix des
    deux espèces Claude (par leur rang dans la configuration) égaux au barème du relais épinglé ; source et heure exigées."""
    o, h = lire_json_scelle(chemin, "relevé des prix Claude")
    if not str(o.get("releve_utc") or "").startswith(aujourd_hui.isoformat()):
        raise Refus(f"relevé des prix Claude : du jour ({aujourd_hui}) exigé")
    if not isinstance(o.get("source"), str) or not o["source"].strip():
        raise Refus("relevé des prix Claude : source exigée")
    claude = [e for e in fixe["especes"] if e["famille"] == "claude"]
    prix = o.get("prix") or {}
    for k, e in enumerate(claude, 1):
        lu = prix.get(f"espece_claude_{k}")
        if not (isinstance(lu, dict) and [lu.get("entree"), lu.get("sortie")] == list(BAREME_CLAUDE[e["modele"]])):
            raise Refus(f"relevé des prix Claude : espèce Claude {k} lue {lu!r}, différente du barème du relais : arrêt, nouveau devis")
    return {"chemin": str(chemin), "sha256": h, "source": o["source"], "releve_utc": o["releve_utc"], "egal_au_bareme": True}


def verifier_sonde_astra(r: "Reglages", decl: dict, aujourd_hui: _dt.date) -> dict:
    """C (R-3273) : Astra n'est déclarée qu'après un appel trivial réussi par sa commande épinglée, par un relais jeté, pour
    0,05 USD au plus ; le relais de la course est neuf (contrôlé par `controler_relais_vivant`)."""
    if "astra" not in decl["fournisseurs"]:
        return {"astra": "non déclarée", "motif": (decl.get("absences") or {}).get("astra")}
    # v7 (mineur 8, majeur 2) : le rapport v2 n'est accepté que lié, par son empreinte, au rapport de la sonde commune du jour
    # (`scripts/sonde_astra_courses_v1.py`, épinglée), qui a contrôlé le relais jeté avant l'appel.
    jour = aujourd_hui.isoformat()
    communes = [(m.format(jour=jour), r.depot / m.format(jour=jour)) for m in r.sondes_astra_communes]
    trouvees = [(rel, p) for rel, p in communes if p.exists()]
    if len(trouvees) != 1:
        raise Refus(f"sonde d'Astra : {len(trouvees)} rapport(s) de la sonde commune du jour parmi {[x for x, _ in communes]} "
                    "(un seul exigé, R-3273) ; un autre jour : sonde neuve, rapports sous course-v7/")
    rel_c, chemin_c = trouvees[0]
    c, h_c = lire_json_scelle(chemin_c, "rapport de la sonde commune d'Astra")
    rj = c.get("relais_jete") if isinstance(c.get("relais_jete"), dict) else {}
    v2c = c.get("rapport_v2") if isinstance(c.get("rapport_v2"), dict) else {}
    ecarts = []
    if c.get("version") != "sonde_astra_courses_v1":
        ecarts.append(f"version {c.get('version')!r}")
    if c.get("ok") is not True or c.get("echec_de_configuration") is not False or c.get("appel_envoye") is not True:
        ecarts.append("sonde commune non réussie")
    if c.get("jour") != jour or not str(c.get("horodatage_utc") or "").startswith(jour):
        ecarts.append(f"jour {c.get('jour')!r}")
    if (c.get("sonde_v2") or {}).get("sha256") != PIECES["sonde_astra"][1]:
        ecarts.append("sonde v2 d'une autre empreinte")
    sha_commande = sha256_fichier(Path(decl["fournisseurs"]["astra"]["commande"][3]))  # épinglée par verifier_declaration
    if (c.get("commande") or {}).get("sha256") != sha_commande:
        ecarts.append("commande d'une autre empreinte que la commande déclarée")
    if rj.get("programme_sha256") != PROGRAMMES_RELAIS["astra"][1] or rj.get("max_appels") != 1 \
            or rj.get("plafond_usd") != SONDE_ASTRA_MAX_USD or rj.get("port") in PORTS_DES_COURSES:
        ecarts.append("relais jeté hors règle (programme, un appel, 0,05 USD, port hors des courses)")
    dep = c.get("depense_relais_usd")
    if not _nombre(dep) or dep > SONDE_ASTRA_MAX_USD:
        ecarts.append(f"dépense lue au relais jeté {dep!r}")
    if ecarts:
        raise Refus(f"sonde d'Astra : rapport de la sonde commune {rel_c} refusé ({'; '.join(ecarts)})")
    permis = {m.format(jour=jour) for m in r.sondes_astra_v2}
    permis |= {str(r.depot / x) for x in permis}
    if v2c.get("chemin") not in permis:
        raise Refus(f"sonde d'Astra : la sonde commune cite le rapport v2 {v2c.get('chemin')!r}, hors des chemins lus par ce "
                    f"lanceur {sorted(m.format(jour=jour) for m in r.sondes_astra_v2)}")
    chemin_v2 = Path(v2c["chemin"]) if os.path.isabs(v2c["chemin"]) else r.depot / v2c["chemin"]
    o, h = lire_json_scelle(chemin_v2, "sonde d'Astra")
    if h != v2c.get("sha256"):
        raise Refus("sonde d'Astra : rapport v2 d'une autre empreinte que celle citée par la sonde commune")
    if o.get("relais_pid") != rj.get("pid"):
        raise Refus("sonde d'Astra : rapport v2 et sonde commune d'un autre relais jeté")
    if not str(o.get("horodatage_utc") or "").startswith(aujourd_hui.isoformat()):
        raise Refus("sonde d'Astra : du jour exigée")
    cout = o.get("cout_usd")
    if o.get("code") != 0 or o.get("ok") is not True or not isinstance(cout, (int, float)) or cout > SONDE_ASTRA_MAX_USD:
        raise Refus(f"sonde d'Astra échouée ou trop chère ({o.get('code')!r}, {cout!r} USD) : Astra ne se déclare pas")
    if o.get("version") != "sonde_astra_affinage_v2":
        raise Refus("sonde d'Astra : fichier non écrit par la sonde épinglée (scripts/sonde_astra_affinage_v2.py)")
    if o.get("commande_sha256") != sha256_fichier(Path(decl["fournisseurs"]["astra"]["commande"][3])):
        raise Refus("sonde d'Astra faite par une autre commande que la commande épinglée")
    if o.get("relais_pid") == (decl.get("metas", {}).get("astra") or {}).get("pid_relais"):
        raise Refus("sonde d'Astra faite par le relais de la course : un relais jeté est exigé")
    return {"chemin": str(chemin_v2), "sha256": h, "cout_usd": cout, "modele_servi": o.get("modele_servi"),
            "sonde_commune": {"chemin": rel_c, "sha256": h_c, "relais_jete_pid": rj.get("pid"),
                              "depense_relais_usd": dep},
            "relais_jete_a_arreter": f"PID {rj.get('pid')} : arrêt par son PID (R10), consigné dans registres/arrets.md"}


# D (R-3273) : aucun nom de personne interne, aucun identifiant de session, aucun courriel dans un texte servi. Les noms
# d'auteurs de travaux publiés cités par les idées (Berkson, Petri, Gu, Krenn…) restent.
MOTIFS_CONFIDENTIELS = (
    ("courriel", re.compile(r"[\w.+-]+@[\w-]+(?:\.[\w-]+)+")),
    ("identifiant de session", re.compile(r"session_[A-Za-z0-9]{6,}|claude\.ai/\S+|\b[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\b")),
    ("nom de variable de clé", re.compile(r"\bRR_[A-Z0-9_]+\b")),
    ("nom de personne interne", re.compile(r"\b(Lazar|Ciric|lciric|Rigaud|Minuit|Heimersheim|Kirchner|Ibrahim|Scheurer|Colognese|"
                                          r"Ward|Jang|Feng)\b")),
)


def expurger(texte: str) -> tuple:
    """Rend (texte expurgé, liste des expurgations {motif, empreinte de l'extrait}) ; jamais l'extrait lui-même."""
    faites = []
    for motif, rx in MOTIFS_CONFIDENTIELS:
        for m in rx.finditer(texte):
            faites.append({"motif": motif, "extrait_sha256": hashlib.sha256(m.group(0).encode("utf-8")).hexdigest()})
        texte = rx.sub("[retiré]", texte)
    return texte, faites


def verifier_confidentialite(textes: dict) -> None:
    """Refus si un texte servi porte encore un motif confidentiel (D, R-3273)."""
    for nom, t in textes.items():
        for motif, rx in MOTIFS_CONFIDENTIELS:
            if rx.search(t):
                raise Refus(f"texte servi « {nom} » : {motif} présent (R-3273) : départ refusé")


def envelopper_commandes(decl: dict, python: str, garde: Path, dossier_arrets: Path) -> dict:
    """Met la garde de crédit devant la commande de chaque relais dispensable actif (Argon, Astra, Carbon)."""
    option = [] if decl.get("compter_limite_de_debit_comme_soupcon", True) else ["--limite-de-debit-pas-soupcon"]
    for nom in FOURNISSEURS_DISPENSABLES:
        b = decl["fournisseurs"].get(nom)
        if b is not None:
            b["commande"] = [python, "-I", "-B", str(garde), str(dossier_arrets), nom] + option + ["--"] + list(b["commande"])
    return decl


# --- (6) orchestrateur --------------------------------------------------------------------------------------------------------


def _git(dossier: Path, *args: str) -> str:
    p = subprocess.run(["git", "-C", str(dossier), *args], capture_output=True, text=True, timeout=60)
    if p.returncode != 0:
        raise Refus(f"git {' '.join(args)} dans {dossier} : code {p.returncode} ({p.stderr.strip()[:200]})")
    return p.stdout


def verifier_orchestrateur(r: Reglages) -> dict:
    presents = [o for o in r.orchestrateurs if (o / LANCEUR_ORCHESTRATEUR).is_file()]
    if len(presents) != 1:
        raise Refus(f"orchestrateur : {len(presents)} copie(s) trouvée(s) parmi {[str(o) for o in r.orchestrateurs]} (une exigée)")
    o = presents[0]
    tete = _git(o, "rev-parse", "HEAD").strip()
    if tete != r.commit_orchestrateur:
        raise Refus(f"orchestrateur au commit {tete}, {r.commit_orchestrateur} exigé")
    porcelaine = _git(o, "status", "--porcelain", "--untracked-files=all", "--ignored=matching").strip()
    if porcelaine:
        raise Refus(f"orchestrateur modifié, fichiers non suivis ou ignorés : {porcelaine[:200]!r}")
    ecarts = {rel: (sha256_fichier(o / rel) if (o / rel).is_file() else None) for rel in r.empreintes_orchestrateur}
    ecarts = {k: v for k, v in ecarts.items() if v != r.empreintes_orchestrateur[k]}
    if ecarts:
        raise Refus(f"orchestrateur : empreintes différentes ou fichiers absents : {ecarts}")
    return {"chemin": str(o), "commit": tete, "empreintes": dict(r.empreintes_orchestrateur)}


# --- (1) configuration de l'orchestrateur, acte de gel ------------------------------------------------------------------------


def assembler_configuration(fixe: dict, liste: dict, pieces: dict, decl: dict, specification: dict | None) -> dict:
    garde_configuration_fixe(fixe)
    garde_cles_configuration(fixe)
    actives = decl["especes_actives"]
    if not any(e["famille"] == "claude" for e in actives):
        raise Refus("aucune espèce Claude active : Claude d'abord (R-3209, point 2)")
    interdites = list(fixe["etiquettes_interdites_fixes"]) + [x["numero"] for x in liste["retraits"]["idees_de_la_table"]] \
        + sorted({f for x in liste["retraits"]["reserves_de_cloisonnement"] for f in x["fiches"]})
    conf = {k: v for k, v in fixe.items() if k not in ("version", "statut", "orchestrateur", "generations", "cartes_par_appel",
                                                       "especes", "etiquettes_interdites_fixes", "cles",
                                                       "cles_interdites", "credit_declare_usd", "regle_cles_v3",
                                                       "relais_persistants_v4", "carbon_v5", "confidentialite_v5",
                                                       "risques_v6")}
    conf["proposeurs"] = [{"etiquette": e["etiquette"], "modele": e["modele"], "fournisseur": e["fournisseur"],
                           "consigne": "consigne_proposeur"} for e in actives]
    cases, expurgations = [], []
    for f in liste["fils"]:
        t, faites = expurger(texte_de_case(f))
        expurgations += [dict(x, fil=f["rang"]) for x in faites]
        cases.append([t, "affinage"])
    verifier_confidentialite({f"fil {k + 1}": c[0] for k, c in enumerate(cases)})
    conf["cases"] = cases
    conf["_expurgations"] = expurgations
    conf["pieces"] = {n: {"chemin": pieces[n]["absolu"], "sha256": pieces[n]["sha256"]} for n in PIECES_SERVIES}
    conf["etiquettes_interdites"] = interdites
    conf["fournisseurs"] = decl["fournisseurs"]
    if specification is not None:
        conf["specification"] = specification
    for e in actives:
        if e["fournisseur"] not in conf["fournisseurs"]:
            raise Refus(f"espèce {e['etiquette']} active sans relais")
    utilises = {conf["aiguilleur"]["fournisseur"]} | {j["fournisseur"] for j in conf["juges"]} | \
        {x["fournisseur"] for x in conf["lecteurs_etiquettes"]}
    manquants = sorted(utilises - set(conf["fournisseurs"]))
    if manquants:
        raise Refus(f"relais absents pour l'aiguilleur, un juge ou un lecteur : {manquants}")
    return conf


def garde_cles_configuration(fixe: dict) -> None:
    """v2 : la configuration fixe nomme Minuit pour Claude, exclut Rigaud, et chaque espèce Claude porte Minuit."""
    if (fixe.get("cles") or {}).get("claude") != CLE_CLAUDE:
        raise Refus(f"configuration : cles.claude doit être {CLE_CLAUDE}")
    if any(c not in (fixe.get("cles_interdites") or []) for c in CLES_INTERDITES):
        raise Refus("configuration : la clé Rigaud doit figurer dans cles_interdites")
    for e in fixe.get("especes") or []:
        if e.get("famille") == "claude" and e.get("cle") != CLE_CLAUDE:
            raise Refus(f"configuration : espèce {e.get('etiquette')} sur une autre clé que {CLE_CLAUDE}")


def garde_configuration_fixe(fixe: dict) -> None:
    """Garde (1) sur la partie fixe : S17 = plafond d'arrêt, portée « course », une génération, étapes retirées par
    construction, plafonds de relais des étapes protégées ≤ S17, aucune étape de tests de mort."""
    b = fixe.get("budget") or {}
    if b.get("plafond_usd") != PLAFOND_ARRET_USD:
        raise Refus(f"configuration : budget.plafond_usd {b.get('plafond_usd')!r} != plafond d'arrêt {PLAFOND_ARRET_USD}")
    if b.get("portee_plafond") != "course" or fixe.get("generations") != 1:
        raise Refus("configuration : portée « course » et une seule génération exigées")
    etapes = {e["nom"]: e for e in b.get("etapes") or []}
    for nom in ("passe_tableau", "fusions"):
        e = etapes.get(nom) or {}
        if e.get("role") != "sacrifiable" or not e.get("plafond_relais_usd", 0) > PLAFOND_ARRET_USD or e.get("attendu_usd") != 0:
            raise Refus(f"configuration : l'étape {nom} doit être retirée par construction (sacrifiable, plafond de relais > S17, attendu 0)")
    protegees = sum(e["plafond_relais_usd"] for e in etapes.values() if e.get("role") == "protegee")
    if protegees > PLAFOND_ARRET_USD:
        raise Refus(f"configuration : somme des plafonds de relais des étapes protégées {protegees} > {PLAFOND_ARRET_USD}")
    if "etage_tests_de_mort" in fixe:
        raise Refus("configuration : pas de tests de mort dans cette course")
    if fixe.get("bisociateur", {}).get("bras") != [] or fixe.get("bisociateur", {}).get("k_paires") != 0:
        raise Refus("configuration : aucun bras du bisociateur, aucune fusion")


def acte_de_gel(prereg: dict, cl: dict, lanceur_sha: str, horodatage: str) -> str:
    return (f"# Acte de gel — course d'affinage des idées des mentors, lanceur {VERSION}\n\n"
            f"Écrit par le lanceur `{VERSION}` (sha256 {lanceur_sha}) le {horodatage}, après vérification.\n\n"
            f"- Préenregistrement : `{prereg['chemin']}`, sha256 {prereg['sha256']}, scellé.\n"
            f"- Contre-lecture : `{cl['chemin']}`, sha256 {cl['sha256']}, scellée ; verdict lu : {cl['verdict']}\n"
            "- Cet acte est la spécification servie à l'orchestrateur (`specification.preenregistrement`) ; il ne change rien au "
            "préenregistrement.\n")


# --- (8) environnement, bac à sable -------------------------------------------------------------------------------------------


def environnement_filtre(env: dict, dossier_maison: Path) -> tuple:
    retires = sorted(n for n in env if n in NOMS_DE_CLE or MOTIF_NOM_DE_CLE.search(n))
    hors_liste = sorted(n for n in env if n not in NOMS_PERMIS and n not in retires)
    garde = {n: env[n] for n in env if n in NOMS_PERMIS}
    garde["GO_ID"] = GO_ID
    garde["HOME"] = str(dossier_maison)
    garde["PYTHONPYCACHEPREFIX"] = str(dossier_maison / "pycache")
    return garde, retires, hors_liste


def sonder_bac_a_sable(r: Reglages, orchestrateur: Path, env: dict) -> dict:
    try:
        p = subprocess.run([r.python, "-I", "-B", "-c", SONDE_BAC_A_SABLE, str(orchestrateur)], cwd=str(orchestrateur), env=env,
                           capture_output=True, text=True, timeout=120)
    except (OSError, subprocess.SubprocessError) as e:
        raise Refus(f"sonde du bac à sable non exécutée ({type(e).__name__})") from None
    lignes = [x for x in p.stdout.splitlines() if x.strip()]
    try:
        etat = json.loads(lignes[-1]) if p.returncode == 0 and lignes else None
    except json.JSONDecodeError:
        etat = None
    if not (isinstance(etat, dict) and isinstance(etat.get("actif"), bool)):
        raise Refus(f"sonde du bac à sable illisible (code {p.returncode})")
    if r.exiger_bac_a_sable and not (etat["actif"] and etat.get("proc_neuf")):
        raise Refus("bac à sable inactif ou sans /proc neuf : " + str(etat.get("motif")))
    return etat


# --- (5) coût réel, écart, relevé après ---------------------------------------------------------------------------------------


def couts_reels(sortie: Path) -> dict:
    chemin = sortie / "generation-1" / "consommations.json"
    if not chemin.is_file():
        return {"lisible": False, "motif": f"{chemin} absent"}
    donnees = json.loads(chemin.read_text(encoding="utf-8")).get("consommations") or []
    par_relais, par_role, appels, coupures, inconnus = {}, {}, {}, [], {}
    for x in donnees:
        role = x.get("role")
        if role == "plafond-relais":
            continue
        if role == "coupure" or x.get("coupure"):
            coupures.append(str(x.get("etape")))
            continue
        f, role, c = str(x.get("fournisseur") or "(sans relais)"), str(role or "(sans rôle)"), float(x.get("cout_usd") or 0.0)
        par_relais[f] = round(par_relais.get(f, 0.0) + c, 6)
        par_role[role] = round(par_role.get(role, 0.0) + c, 6)
        appels[role] = appels.get(role, 0) + 1
        if x.get("cout_inconnu"):
            inconnus[f] = inconnus.get(f, 0) + 1
    return {"lisible": True, "fichier_sha256": sha256_fichier(chemin), "par_relais_usd": par_relais, "par_role_usd": par_role,
            "appels_par_role": appels, "total_usd": round(sum(par_relais.values()), 6), "coupures": coupures,
            "appels_a_cout_inconnu_par_relais": inconnus}


def devis_estimation(etiquettes_actives: list) -> float:
    """v7, mineur 4 : estimation sans marge du devis pour les espèces **actives** : 16 appels par espèce de proposeurs, et
    2 cartes × 16 cases par espèce pour l'aiguilleur et pour chacun des deux juges (prix par appel du devis v6)."""
    inconnues = [e for e in etiquettes_actives if e not in DEVIS_V5_PAR_APPEL]
    if inconnues:
        raise Refus(f"devis : espèces sans prix par appel {inconnues}")
    n = len(etiquettes_actives)
    proposeurs = sum(APPELS_PAR_PROPOSEUR * DEVIS_V5_PAR_APPEL[e] for e in etiquettes_actives)
    internes = 2 * APPELS_PAR_PROPOSEUR * n * sum(DEVIS_V5_PAR_APPEL[k] for k in ("aiguilleur", "juge-opus", "juge-argon"))
    return round(proposeurs + internes, 6)


def ecart_au_devis(couts: dict, etiquettes_actives: list) -> dict:
    if not couts.get("lisible"):
        return {"lisible": False}
    lignes = {}
    for role, n in sorted(couts["appels_par_role"].items()):
        attendu = DEVIS_V5_PAR_APPEL.get(role)
        reel = couts["par_role_usd"][role]
        lignes[role] = {"appels": n, "reel_usd": reel, "devis_usd": round(n * attendu, 6) if attendu is not None else None,
                        "ecart_usd": round(reel - n * attendu, 6) if attendu is not None else None}
    total_devis = devis_estimation(etiquettes_actives)
    return {"lisible": True, "par_role": lignes, "total_reel_usd": couts["total_usd"], "devis_estimation_sans_marge_usd": total_devis,
            "base_du_devis": {"especes_actives": list(etiquettes_actives), "nombre": len(etiquettes_actives),
                              "regle": "recalculée sur les espèces actives (v7, mineur 4)"},
            "ecart_total_usd": round(couts["total_usd"] - total_devis, 6)}


def releve_apres(credits: dict, couts: dict, cles: dict) -> tuple:
    """Reste estimé = reste avant − coût compté des relais de la clé (consommations de l'orchestrateur, au prix des fichiers ;
    à confirmer par l'interface de facturation). Alerte sous un cinquième du crédit, et pour Kimi sous ce qu'exige la course
    Kimi de la relance (11,3 / 0,9 USD). Rend (relevé, alertes)."""
    apres, alertes = {}, []
    for nom, avant in sorted(credits.items()):
        fournisseurs = [f for f, n in cles.items() if n == nom]
        depense = round(sum((couts.get("par_relais_usd") or {}).get(f, 0.0) for f in fournisseurs), 6) if couts.get("lisible") else None
        if not avant.get("lisible") or depense is None:
            apres[nom] = {"lisible": False, "depense_comptee_usd": depense, "a_relever": "par l'interface de facturation si elle le permet"}
            continue
        reste = round(avant["reste_usd"] - depense, 6)
        seuil = avant["credit_usd"] / 5.0
        if "kimi" in fournisseurs:
            seuil = max(seuil, KIMI_COURSE_SUIVANTE_PIRE_USD / KIMI_PART_DU_RESTE)
        apres[nom] = {"lisible": "estimé", "reste_estime_usd": reste, "depense_comptee_usd": depense, "seuil_usd": seuil,
                      "a_relever": "par l'interface de facturation (confirmation)"}
        if reste < seuil:
            alertes.append({"cle": nom, "reste_estime_usd": reste, "seuil_usd": seuil})
    return apres, alertes


def lire_resume_course(sortie: Path) -> dict:
    """Ce qui a été fait, sans lire aucun verdict : étapes, nœud, arrêt, cumul, nombre de cartes."""
    out = {}
    m = sortie / "generation-1" / "manifeste-fin.json"
    if m.is_file():
        d = json.loads(m.read_text(encoding="utf-8"))
        out.update(etapes=d.get("etapes"), noeud=d.get("noeud"), arret=d.get("arret"), roles_arretes=d.get("roles_arretes"),
                   exclues_a4=d.get("exclues_a4"), cumul_usd=(d.get("budget") or {}).get("cumul_usd"),
                   depassement_s17_usd=(d.get("budget") or {}).get("depassement_s17_usd"))
    f = sortie / "generation-1" / "fiches.json"
    if f.is_file():
        out["cartes_a_passeport"] = len(json.loads(f.read_text(encoding="utf-8")))
    b = sortie / "bilan-course.json"
    if b.is_file():
        out["bilan_sha256"] = sha256_fichier(b)
    return out


# --- exécution ----------------------------------------------------------------------------------------------------------------


def _depot_git(r: Reglages) -> dict:
    try:
        return {"commit": _git(r.depot, "rev-parse", "HEAD").strip(),
                "arbre_modifie": bool(_git(r.depot, "status", "--porcelain", "--untracked-files=no").strip())}
    except Refus as e:
        return {"commit": None, "erreur": str(e)}


def _versions(r: Reglages, orch: Path, env: dict) -> dict:
    p = subprocess.run([r.python, "-I", "-B", "-c", "import numpy, platform; print(numpy.__version__, platform.python_version())"],
                       cwd=str(orch), env=env, capture_output=True, text=True, timeout=60)
    morceaux = p.stdout.split()
    return {"python": morceaux[1] if len(morceaux) == 2 else None, "numpy": morceaux[0] if len(morceaux) == 2 else None,
            "executable": r.python}


def executer(r: Reglages) -> int:
    env_lu = dict(os.environ) if r.environnement is None else dict(r.environnement)
    aujourd_hui = r.aujourd_hui or _dt.datetime.now(_dt.timezone.utc).date()
    reel = r.moteur == "reel"

    verifier_course_jamais_lancee(r)
    cle_presente = bool((env_lu.get(CLE_CLAUDE) or "").strip())  # nom présent, valeur non vide ni faite d'espaces ; jamais écrite
    if reel and not cle_presente:
        raise Refus(f"variable {CLE_CLAUDE} absente ou vide dans l'environnement du lanceur : arrêt au départ (R-3228)")
    commit_registre = verifier_registre_main(r) if (reel and r.verifier_go) else None
    go = verifier_go(r.registre_go, aujourd_hui) if (reel and r.verifier_go) else {"go": "sans objet (moteur simulé, aucune dépense)"}
    lanceur_sha = sha256_fichier(r.lanceur)
    prereg = verifier_preenregistrement(r)
    cl = verifier_contre_lecture(r, prereg["sha256"], lanceur_sha)
    pieces = verifier_pieces(r)
    fixe = json.loads(Path(pieces["configuration"]["absolu"]).read_text(encoding="utf-8"))
    liste = json.loads(Path(pieces["liste_fils"]["absolu"]).read_text(encoding="utf-8"))
    controle_liste = verifier_liste(liste)
    decl_brute, decl_sha = lire_json_scelle(r.declaration, "déclaration des relais")
    decl = verifier_declaration(decl_brute, fixe, r)
    releve_brut, releve_sha = lire_json_scelle(r.releve, "relevé des crédits")
    horodatage = r.horodatage()
    ident = _dt.datetime.now(_dt.timezone.utc).strftime("%Y%m%d-%H%M%S-%f") + SUFFIXE_RUN  # 1 : unique à la microseconde
    dossier_run = r.dossier_runs / ident
    parts = parts_au_pire(fixe, liste, pieces, decl)
    autres_courses = verifier_autres_courses(r, releve_brut)  # v7, majeur 2
    credits = verifier_credits(releve_brut, decl["cles"], aujourd_hui,
                               r.dossier_runs / (ident.replace(SUFFIXE_RUN, "") + "-alerte-credits-affinage-mentors-v7"), parts)
    verifier_confidentialite({n: Path(pieces[n]["absolu"]).read_text(encoding="utf-8") for n in PIECES_SERVIES})
    procedure = verifier_procedure_relais(r, decl, pieces, fixe, parts) if reel else {"exigee": False, "motif": "moteur simulé : aucun relais réel"}
    sonde = verifier_sonde_astra(r, decl, aujourd_hui) if reel else {"exige": False, "motif": "moteur simulé"}
    prix = verifier_releve_prix(r.releve_prix, fixe, aujourd_hui) if reel else {"exige": False, "motif": "moteur simulé"}
    orch = verifier_orchestrateur(r)
    orch_dir = Path(orch["chemin"])

    dossier_sortie = r.dossier_sorties / ident
    sortie = dossier_sortie / "sortie"
    prepa = r.dossier_sorties / (ident + "-preparation")  # 1 : hors dépôt ; runs/<id> n'est créé qu'après la porte à blanc
    if dossier_run.exists() or dossier_sortie.exists() or prepa.exists():
        raise Refus(f"{dossier_run}, {dossier_sortie} ou {prepa} existe déjà (R12)")
    env, retires, hors_liste = environnement_filtre(env_lu, dossier_sortie)
    bac = sonder_bac_a_sable(r, orch_dir, env) if reel else {"exige": False, "motif": "moteur simulé : aucun agent réel"}

    prepa.mkdir(parents=True)
    dossier_arrets = dossier_sortie / "arrets-credit"  # v5, constat 1 : créé seulement après la porte à blanc
    decl = envelopper_commandes(decl, r.python, Path(pieces["garde_credit"]["absolu"]), dossier_arrets)
    h_acte = ecrire_scelle(prepa / "acte-de-gel.md", acte_de_gel(prereg, cl, lanceur_sha, horodatage))
    spec = {"preenregistrement": {"chemin": str(prepa / "acte-de-gel.md"), "sha256": h_acte},
            "contre_lecture": {"chemin": cl["chemin"], "sha256": cl["sha256"]}}
    conf = assembler_configuration(fixe, liste, pieces, decl, spec)
    chemin_conf = prepa / "configuration-orchestrateur.json"
    expurgations = conf.pop("_expurgations")
    h_conf = ecrire_scelle(chemin_conf, conf)
    base = [r.python, "-I", "-B", LANCEUR_ORCHESTRATEUR, "--course-2", str(chemin_conf), str(sortie), "--generations", "1"]
    registre = ecrire_registre_derive(r.registre_go, prepa / "registre-go-derive.md", commit=commit_registre) if reel else {"motif": "moteur simulé"}
    moteur = ["--moteur", "reel", "--confirmer-moteur-reel", "--registre-go", registre["derive"]] if reel else ["--moteur", "simule"]
    verif = subprocess.run(base + ["--verifier-seulement"] + (moteur if reel else []),
                           cwd=str(orch_dir), env=env, capture_output=True, text=True, timeout=600)
    try:
        verif_json = json.loads(verif.stdout) if verif.returncode == 0 else None
    except ValueError:
        verif_json = None
    if verif_json is None or verif_json.get("montant_requis_go_usd") != PLAFOND_ARRET_USD:
        raise Refus(f"vérification de l'orchestrateur refusée (code {verif.returncode}) : "
                    f"{(verif.stderr or verif.stdout).strip()[-800:]!r}")
    if verif_json.get("specification", {}).get("conforme") is not True:
        raise Refus(f"spécification refusée par l'orchestrateur : {verif_json.get('specification')}")
    portes = porte_a_blanc(decl) if reel else {"exige": False, "motif": "moteur simulé : portes tenues par le noyau"}
    dossier_run.mkdir(parents=True)  # 1 : seulement après la porte à blanc
    for f in sorted(prepa.iterdir()):  # copie au dépôt, pour mémoire ; l'orchestrateur lit les pièces de la préparation
        shutil.copy2(f, dossier_run / f.name)
    dossier_sortie.mkdir(parents=True)
    dossier_arrets.mkdir()
    argv = base + moteur
    etiquettes_actives = [e["etiquette"] for e in decl["especes_actives"]]
    depart = {
        "lanceur": {"version": VERSION, "chemin": str(r.lanceur), "sha256": lanceur_sha}, "moteur": r.moteur,
        "horodatage_canonique": horodatage, "id": ident, "go": go, "plafond_arret_usd": PLAFOND_ARRET_USD,
        "preenregistrement": prereg, "contre_lecture": cl, "acte_de_gel_sha256": h_acte, "pieces": pieces,
        "liste_fils": controle_liste, "declaration_relais": {"chemin": str(r.declaration), "sha256": decl_sha},
        "especes_actives": [e["etiquette"] for e in decl["especes_actives"]], "especes_absentes": decl["especes_absentes"],
        "carbon": decl["carbon"], "cles_employees": decl["cles"],
        "cle_par_espece": {e["etiquette"]: decl["cles"][e["fournisseur"]] for e in decl["especes_actives"]},
        "cle_par_role_interne": {"aiguilleur": decl["cles"][fixe["aiguilleur"]["fournisseur"]],
                                 **{j["etiquette"]: decl["cles"][j["fournisseur"]] for j in fixe["juges"]}},
        "parts_au_pire": parts, "procedure_relais_persistants": procedure, "porte_a_blanc": portes,
        "registre_go_derive": registre, "releve_prix_claude": prix, "sonde_astra": sonde, "preparation": str(prepa),
        "kimi_autorise_par_la_mere": decl.get("kimi_autorise_par_la_mere"),
        "compter_limite_de_debit_comme_soupcon": decl.get("compter_limite_de_debit_comme_soupcon", True),
        "confidentialite": {"regle": "R-3273", "expurgations": expurgations, "textes_verifies": list(PIECES_SERVIES) + ["16 fils"]}, "dossier_arrets_credit": str(dossier_arrets),
        "cle_claude": {"nom": CLE_CLAUDE, "presente_dans_l_environnement_du_lanceur": cle_presente, "valeur": "jamais lue",
                       "cles_exclues": list(CLES_INTERDITES)},
        "releve_credits_avant": {"chemin": str(r.releve), "sha256": releve_sha, "cles": credits},
        "orchestrateur": orch, "configuration": {"chemin": str(chemin_conf), "sha256": h_conf},
        "verification_orchestrateur": {k: verif_json.get(k) for k in ("configuration_sha256", "montant_requis_go_usd",
                                                                      "specification", "go", "generations")},
        "commande": argv, "cwd": str(orch_dir), "sortie": str(sortie), "bac_a_sable": bac,
        "environnement": {"noms_retires": retires, "noms_exclus": hors_liste, "valeurs": "jamais lues"},
        "graines": {"racine": conf["racine_graines"], "prefixe": conf["graines"]["prefixe"],
                    "regle": "numpy.random.SeedSequence(racine, spawn_key=(cle_de_tache(tache),)) dans l'orchestrateur (R9)"},
        "versions": _versions(r, orch_dir, env), "depot_travail": _depot_git(r),
        "devis_estimation_sans_marge_usd": devis_estimation(etiquettes_actives),
        "base_du_devis": {"especes_actives": etiquettes_actives, "regle": "recalculée sur les espèces actives (v7, mineur 4)"},
        "autres_courses_de_l_organisme": autres_courses,
        "codes_de_sortie": {"0": "course finie", "2": "refus avant le départ", "3": "alerte de crédit avant le départ",
                            "4": "cumul au-dessus de 150 USD", "5": "arrêt par la garde de crédit",
                            "6": "course partie : orchestrateur à code non nul ou erreur du lanceur après le départ"},
        "journaux": {"stdout": str(dossier_sortie / "course.stdout.txt"), "stderr": str(dossier_sortie / "course.stderr.txt")},
    }
    h_depart = ecrire_scelle(dossier_run / "manifeste-lanceur-depart.json", depart)
    print(json.dumps({"manifeste_depart": str(dossier_run / "manifeste-lanceur-depart.json"), "sha256": h_depart}, ensure_ascii=False),
          flush=True)

    code, pid, echec, arret_credit = None, None, None, []
    debut = _dt.datetime.now(_dt.timezone.utc)
    try:
        with open(dossier_sortie / "course.stdout.txt", "xb") as fo, open(dossier_sortie / "course.stderr.txt", "xb") as fe:
            enfant = subprocess.Popen(argv, cwd=str(orch_dir), env=env, stdout=fo, stderr=fe)
            pid = enfant.pid

            def relayer(num, _cadre):
                try:
                    enfant.send_signal(num)
                except ProcessLookupError:
                    pass
            anciens = {s: signal.signal(s, relayer) for s in (signal.SIGTERM, signal.SIGINT, signal.SIGHUP)}
            try:
                while True:
                    try:
                        code = enfant.wait(timeout=1.0)
                        break
                    except subprocess.TimeoutExpired:
                        if not arret_credit and any(dossier_arrets.glob("arret-credit-*.json")):
                            arret_credit = sorted(x.name for x in dossier_arrets.glob("arret-credit-*.json"))
                            enfant.send_signal(signal.SIGTERM)  # R-3237 : arrêt au premier refus pour crédit (par PID, R10)
            finally:
                for s, a in anciens.items():
                    signal.signal(s, a)
    except BaseException as exc:  # noqa: BLE001 — le manifeste de fin est écrit sur tout chemin
        echec = f"{type(exc).__name__}: {exc}"
    fin = _dt.datetime.now(_dt.timezone.utc)
    bilan = {"id": ident, "manifeste_depart_sha256": h_depart, "pid_orchestrateur": pid, "code": code, "echec_lanceur": echec,
             "debut_utc": debut.isoformat(), "fin_utc": fin.isoformat(),
             "arret_au_premier_refus_pour_credit": [json.loads(x.read_text(encoding="utf-8"))
                                                    for x in sorted(dossier_arrets.glob("arret-credit-*.json"))],
             "soupcons_de_refus_pour_credit": [json.loads(x.read_text(encoding="utf-8"))
                                               for x in sorted(dossier_arrets.glob("soupcon-credit-*.json"))]}
    alertes_apres, depasse = [], False
    try:
        couts = couts_reels(sortie)
        cumul = (lire_resume_course(sortie).get("cumul_usd") or 0.0)
        apres, alertes_apres = releve_apres(credits, couts, decl["cles"])
        depasse = bool(couts.get("lisible") and couts["total_usd"] > PLAFOND_ARRET_USD + 1e-9) or cumul > PLAFOND_ARRET_USD + 1e-9
        bilan.update({"ce_qui_a_ete_fait": lire_resume_course(sortie), "cout_reel": couts,
                      "ecart_au_devis": ecart_au_devis(couts, etiquettes_actives),
                      "plafond_arret": {"usd": PLAFOND_ARRET_USD, "depasse": depasse},
                      "releve_credits_apres": apres, "alertes_apres": alertes_apres})
    except Exception as exc:  # noqa: BLE001 — le manifeste de fin est écrit quand même, l'erreur y est dite
        bilan["erreur_bilan"] = f"{type(exc).__name__}: {exc}"
        echec = echec or bilan["erreur_bilan"]
    bilan["journaux_sha256"] = {n: sha256_fichier(dossier_sortie / n) for n in ("course.stdout.txt", "course.stderr.txt")
                                if (dossier_sortie / n).is_file()}
    if bilan.get("arret_au_premier_refus_pour_credit"):
        ecrire_scelle(dossier_run / "alerte-arret-credit.json",
                      {"alerte": "course arrêtée par la garde de crédit (refus pour crédit, ou deuxième soupçon du même relais ; R-3237)",
                       "relais": bilan["arret_au_premier_refus_pour_credit"], "pour": "la mère, qui prévient Lazar"})
    if alertes_apres or depasse:
        ecrire_scelle(dossier_run / "alerte-credits-apres.json",
                      {"alerte": "après la course : reste estimé sous le seuil ou plafond d'arrêt dépassé", "cles": alertes_apres,
                       "plafond_depasse": bool(depasse), "pour": "la mère (à transmettre à Lazar avant qu'une clé n'atteigne zéro)"})
    sortie_lanceur = code_de_sortie(depasse, bool(bilan.get("arret_au_premier_refus_pour_credit")), echec, code)
    bilan["code_orchestrateur"] = code
    bilan["code_du_lanceur"] = sortie_lanceur
    h_fin = ecrire_scelle(dossier_run / "manifeste-lanceur-fin.json", bilan)
    print(json.dumps({"manifeste_fin": str(dossier_run / "manifeste-lanceur-fin.json"), "sha256": h_fin, "code": code,
                      "code_du_lanceur": sortie_lanceur, "cout_reel_usd": (bilan.get("cout_reel") or {}).get("total_usd"),
                      "alertes_apres": alertes_apres}, ensure_ascii=False), flush=True)
    if echec:
        print(json.dumps({"erreur_apres_depart": echec}, ensure_ascii=False), file=sys.stderr)
    return sortie_lanceur


def code_de_sortie(depasse: bool, arret_credit: bool, echec, code_orchestrateur) -> int:
    """v7, mineur 5 : codes du lanceur distincts de ceux de l'orchestrateur. 4 (plafond) prime, puis 5 (garde de crédit) ;
    toute autre issue non nette d'une course partie — code non nul ou absent de l'orchestrateur, signal, erreur du lanceur
    après le manifeste de départ — rend 6 (le vrai code est au manifeste de fin) ; 0 seulement pour un code 0 sans erreur."""
    if depasse:
        return 4
    if arret_credit:
        return 5
    if echec or code_orchestrateur != 0:
        return 6
    return 0


# --- essai à blanc ------------------------------------------------------------------------------------------------------------


CHEMINS_MAIN_COMMANDES = {
    "carbon": "docs/notes/ideation-organisme-v1/argon-recherche-v1/commande_gemini_lot_v1.py",
    "astra": "docs/notes/ideation-organisme-v1/relais-kimi-v1/commande_astra_v1.py"}


def extraire_de_main(depot: Path, chemin: str, attendu: str, destination: Path) -> Path:
    """Extraction hors dépôt, depuis `origin/main` (récupérée avant par un `git fetch` ciblé), vérifiée à son empreinte."""
    p = subprocess.run(["git", "-C", str(depot), "show", "origin/main:" + chemin], capture_output=True, timeout=60)
    if p.returncode != 0 or hashlib.sha256(p.stdout).hexdigest() != attendu:
        raise Refus(f"extraction de {chemin} depuis origin/main : absente ou d'une autre empreinte que {attendu[:12]}…")
    if destination.exists():
        raise Refus(f"{destination} existe déjà (R12)")
    destination.write_bytes(p.stdout)
    return destination


def reglages_a_blanc(dossier: Path) -> Reglages:
    """Moteur simulé, relais factices (adresses locales sans serveur, portes « commande » factices jamais appelées par le moteur
    simulé), contre-lecture et relevé d'essai écrits dans le dossier, aucun GO. Rien n'est lu dans `registres/`."""
    if dossier.exists():
        raise Refus(f"{dossier} existe déjà (R12)")
    dossier.mkdir(parents=True)
    essai = dossier / "pieces-d-essai"
    essai.mkdir()
    r = Reglages.production()
    lanceur_sha = sha256_fichier(r.lanceur)
    prereg_sha = r.prereg[1] if re.fullmatch(r"[0-9a-f]{64}", r.prereg[1]) else sha256_fichier(r.prereg[0])
    cl = essai / "contre-lecture-d-essai.md"
    ecrire_scelle(cl, f"# Contre-lecture d'ESSAI par le modèle K (aucune valeur réelle)\n\nPréenregistrement lu : {prereg_sha}\n"
                      f"Lanceur lu : {lanceur_sha}\n\n## Verdict\n\nScellable.\n\nEssai à blanc seulement.\n")
    porte = ["/bin/false"]
    cmd = {n: extraire_de_main(r.depot, CHEMINS_MAIN_COMMANDES[n], next(iter(COMMANDES_EPINGLEES[n].values())),
                               essai / os.path.basename(CHEMINS_MAIN_COMMANDES[n])) for n in ("carbon", "astra")}
    decl = {"version": "declaration-relais-essai-a-blanc", "fournisseurs": {
        "carbon": {"type": "commande_externe", "commande": [sys.executable, "-I", "-B", str(cmd["carbon"])] + ARGUMENTS_COMMANDES["carbon"],
                   "modele_propose": "gemini-4-carbon", "nom_cle": "CLE_FACTICE_ARGON", "inscription": INSCRIPTION_CARBON,  # 7 : clé partagée
                   "porte_plafond": {"type": "environnement"}},
        "astra": {"type": "commande_externe", "commande": [sys.executable, "-I", "-B", str(cmd["astra"])] + ARGUMENTS_COMMANDES["astra"],
                  "modele_propose": "gpt-6-astra", "nom_cle": "CLE_FACTICE_ASTRA", "porte_plafond": {"type": "environnement"}},
        "claude": {"type": "claude_sdk", "url_relais": "http://127.0.0.1:18999", "nom_cle": CLE_CLAUDE,
                   "porte_plafond": {"type": "commande", "commande": porte, "delai_s": 5}},
        "argon": {"type": "commande_externe", "commande": ["bash", str(r.depot / PIECES["enveloppe_argon"][0])],
                  "nom_cle": "CLE_FACTICE_ARGON", "porte_plafond": {"type": "environnement"}}}}
    chemin_decl = essai / "declaration-relais-d-essai.json"
    ecrire_scelle(chemin_decl, decl)
    maintenant = _dt.datetime.now(_dt.timezone.utc)
    releve = {"version": "releve-credits-essai-a-blanc", "releve_utc": maintenant.strftime("%Y-%m-%dT%H:%M:%SZ"),
              "note": "essai à blanc : aucune valeur réelle",
              "cles": dict({n: {"non_lisible": True, "motif": "essai à blanc : solde illisible, sous dispense"}
                            for n in ("CLE_FACTICE_ARGON", "CLE_FACTICE_ASTRA")},
                           **{CLE_CLAUDE: {"non_lisible": True, "motif": "essai à blanc : compté au prix relevé",
                                           "depense_anterieure_usd": 0.0}}),
              "dispense": {"par": "mère", "reference": REFERENCE_DISPENSE,
                           "cles": ["CLE_FACTICE_ARGON", "CLE_FACTICE_ASTRA"]}}
    chemin_releve = essai / "releve-credits-d-essai.json"
    ecrire_scelle(chemin_releve, releve)
    r.prereg = (r.prereg[0], prereg_sha)
    r.contre_lecture, r.declaration, r.releve = cl, chemin_decl, chemin_releve
    r.dossier_runs, r.dossier_sorties = dossier / "runs", dossier / "sorties"
    r.moteur, r.exiger_bac_a_sable, r.verifier_go = "simule", False, False
    return r


def principal(argv: list | None = None, reglages: Reglages | None = None) -> int:
    argv = sys.argv[1:] if argv is None else list(argv)
    try:
        if argv and argv[0] == "--a-blanc" and len(argv) == 2:
            reglages = reglages or reglages_a_blanc(Path(argv[1]).resolve())
        elif argv:
            print(json.dumps({"refus": f"arguments non admis (reçu {argv!r}) ; seul « --a-blanc DOSSIER »"}, ensure_ascii=False),
                  file=sys.stderr)
            return 2
        return executer(reglages or Reglages.production())
    except AlerteCredit as e:
        print(json.dumps({"alerte_credit": str(e)}, ensure_ascii=False), file=sys.stderr)
        return 3
    except Refus as e:
        print(json.dumps({"refus": str(e)}, ensure_ascii=False), file=sys.stderr)
        return 2
    except Exception as e:  # noqa: BLE001
        print(json.dumps({"erreur": f"{type(e).__name__}: {e}"}, ensure_ascii=False), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(principal())
