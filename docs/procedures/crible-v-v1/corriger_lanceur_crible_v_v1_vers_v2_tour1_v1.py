#!/usr/bin/env python3
"""Applique à `lanceur_crible_v_v1.py` les corrections du tour 1 de sa contre-lecture qui portent sur lui (M2, M3, m1, m4) : v2 neuve.

Usage : python3 -I -B corriger_lanceur_crible_v_v1_vers_v2_tour1_v1.py SOURCE CIBLE HEURE_UTC
- SOURCE : le lanceur v1 (`lanceur_crible_v_v1.py`), d'empreinte EMPREINTE_SOURCE, égal à son compagnon ;
- CIBLE : le lanceur v2 (`lanceur_crible_v_v2.py`), fichier neuf, jamais écrasé (R12 : ouverture exclusive) ;
- HEURE_UTC : `date -u +%FT%TZ` au moment du scellement (écrite dans l'en-tête de la v2).
Le rapport du tour 1 (`contre-lecture-code-crible-v-tour1-v1.md`, même dossier que la source) doit avoir l'empreinte
EMPREINTE_RAPPORT et être égal à son compagnon ; le banc de mutations v1 (même dossier) doit être égal à son compagnon.
- Couples du rapport (cinq) : recopiés tels qu'il les écrit ; avant tout, le programme retrouve l'ancien et le nouveau de chacun,
  à l'identique, comme deux blocs de code entiers du rapport.
- Couples du rédacteur (quatre) : en tête (version et heure ; section « Contre-lecture ») et deux changements de nom, conséquences
  du nom neuf (R12) : la version écrite par le lanceur, et le lanceur compté dans les empreintes du code du crible.
Chaque « ancien » doit figurer exactement une fois au moment de son couple. Contrôles de sortie : le texte neuf se compile ; chaque
texte que vise une mutation du banc v1 sur le lanceur, et ceux des mutations M29 et M30 proposées au rapport, y figurent une fois.
Aucun accès réseau ; aucune pièce existante modifiée ; rien n'est écrit si un contrôle échoue.
"""
import hashlib
import os
import re
import runpy
import sys

NOM_SOURCE = "lanceur_crible_v_v1.py"
NOM_CIBLE = "lanceur_crible_v_v2.py"
EMPREINTE_SOURCE = "2636bcb1deefc0a7dc1427bb476b7c0e2efdc1b5ae6d9e76c3a7c2ac592d7725"
NOM_RAPPORT = "contre-lecture-code-crible-v-tour1-v1.md"
EMPREINTE_RAPPORT = "05809ac265f80e766690e43d5741f1fbd890e9057773658c0cfc4e4a6d959675"
NOM_BANC = "banc_mutations_crible_v_v1.py"
NOM_PROGRAMME = "corriger_lanceur_crible_v_v1_vers_v2_tour1_v1.py"
TQ = '"' * 3

# --- couples du rapport, tels qu'il les écrit (blocs de code de ses § 2 et 3) -----------------------------------------------------

M2 = ("M2 (lanceur : l'arrêt d'une file arrête aussitôt l'autre)",
      "            fs = [ex.submit(file, k, mk) for k, mk in enumerate(files)]",
      "            def file_gardee(k, mk):\n"
      "                try:\n"
      "                    file(k, mk)\n"
      "                except Exception as e:  # noqa: BLE001 — l'arrêt d'une file arrête aussitôt l'autre (aucune dépense de plus)\n"
      "                    with E.verrou:\n"
      "                        if not E.arret:\n"
      '                            E.arret, E.arret_classe = f"{type(e).__name__} : {e}", "arret"\n'
      "                    raise\n"
      "\n"
      "            fs = [ex.submit(file_gardee, k, mk) for k, mk in enumerate(files)]")

M3_1 = ("M3, couple 1 (lanceur : résultats d'un monde recueillis)",
        "                erreurs = []\n"
        "                for nom in lancer:",
        "                erreurs, rendus = [], {}\n"
        "                for nom in lancer:")

M3_2 = ("M3, couple 2 (lanceur : appels répondus traités avant les autres)",
        '                    cs, info = ([], None) if r["etat"] == "echec" else P.cartes_d_un_appel(w, nom, r["texte"])\n'
        "                    with E.verrou:\n"
        "                        traiter_resultat(E, w, nom, lignes[nom], r, cs, info)",
        '                    cs, info = ([], None) if r["etat"] == "echec" else P.cartes_d_un_appel(w, nom, r["texte"])\n'
        "                    rendus[nom] = (r, cs, info)\n"
        "                for nom in sorted(rendus, key=lambda n: not repondu_au_lanceur(rendus[n][0], rendus[n][1])):  # répondus d'abord\n"
        "                    r, cs, info = rendus[nom]\n"
        "                    with E.verrou:\n"
        "                        traiter_resultat(E, w, nom, lignes[nom], r, cs, info)")

m1 = ("m1 (lanceur : aucun repli silencieux à zéro dans les dollars)",
      '                out.append({"monde": w, "proposeur": nom, "cout_config_usd": 0.0, "source": "journal_relais"})',
      '                out.append({"monde": w, "proposeur": nom, "cout_config_usd": float(a.get("cout_usd") or 0.0), "source": "journal_relais"})')

m4 = ("m4 (lanceur : configuration refusée en mode réel)",
      'CHAMPS_A_BLANC = ("scenarios", "lent", "borne_essai_s", "decalage_ports")',
      'CHAMPS_A_BLANC = ("scenarios", "lent", "borne_essai_s", "decalage_ports", "configuration")')

COUPLES_DU_RAPPORT = [M2, M3_1, M3_2, m1, m4]

# --- textes visés par les mutations M29 et M30 proposées au rapport (M4) : à garder une fois chacun ----------------------------------

CIBLES_M29_M30 = ['j = lignes.get((nom, a.get("texte_servi_sha256")), [])',
                  '"cout_usd": float(p["plafond_session_usd"]), "cout_origine": "plafond_de_session"})']

# --- couples du rédacteur : en tête et noms ----------------------------------------------------------------------------------------

SECTION = """Contre-lecture
- Rapport : `contre-lecture-code-crible-v-tour1-v1.md` (même dossier), empreinte
  `05809ac265f80e766690e43d5741f1fbd890e9057773658c0cfc4e4a6d959675` ; contre-lecteur neuf, d'un autre modèle que l'auteur de
  la v1 (R2) ; verdict « corrections » : quatre majeures (M1 à M4), quatre mineures (m1 à m4), cinq remarques facultatives
  (f1 à f5) et des points pour la mère (§ 5).
- Cette version : v2, écrite par un rédacteur neuf, qui n'a écrit ni la v1 ni le rapport, par le programme de couples
  `corriger_lanceur_crible_v_v1_vers_v2_tour1_v1.py` (même dossier, scellé avec son compagnon), depuis la v1
  `2636bcb1deefc0a7dc1427bb476b7c0e2efdc1b5ae6d9e76c3a7c2ac592d7725` ; chaque ancien présent une fois ; les couples du rapport
  sont recopiés tels qu'il les écrit (le programme retrouve leur ancien et leur nouveau, à l'identique, parmi les blocs du rapport).
- Réponse point par point :
  - M1 (l'outil de la session refuse le plafond de κv1 écrit « 104.39 USD (sur crédits) ») : correction de l'outil de la
    session, hors de ce lanceur ; le lecteur des lignes de GO de ce lanceur (`lire_go_du_crible`, lecteur v66 de l'arbre)
    accepte cette forme (rapport, M1 ; rejoué par le rédacteur sur les deux lignes du texte) ; rien ne change ici.
  - M2 (à M = 2, un arrêt levé dans une file n'arrêtait l'autre qu'une fois la file 0 finie) : appliquée, couple du rapport ;
    chaque file tourne dans une enveloppe qui, dès qu'une exception sort de la file, pose l'arrêt sous le verrou, puis la relève ;
    l'autre file s'arrête avant son monde suivant (seuls les appels déjà en vol finissent ; aucune dépense de plus).
  - M3 (la règle d'abandon dépendait de l'ordre de traitement des quatre appels d'un monde) : appliquée, deux couples du
    rapport ; les résultats des appels d'un monde sont d'abord tous recueillis, puis traités sous le verrou, les appels répondus
    vus du lanceur avant les autres (ordre des noms gardé entre égaux) ; « perdu en entier » ne dépend plus de l'ordre des noms.
  - M4 (dollars lus aux journaux des relais et dépense d'un appel coupé, sans essai) : correction des essais et du banc, hors de
    ce lanceur ; les deux textes que visent les mutations M29 et M30 proposées par le rapport restent ici inchangés, une fois
    chacun (contrôle de sortie du programme).
  - m1 (repli silencieux à zéro dans les dollars) : appliquée, couple du rapport ; un appel lancé, non coupé, sans ligne au
    journal de son relais prend le coût rendu par la commande (zéro seulement si la commande n'en a rendu aucun) ; la source
    écrite reste « journal_relais », comme le couple l'écrit.
  - m2 (portes du mode réel sans essai propre) : correction des essais ou de la répétition, hors de ce lanceur.
  - m3 (cadence de la minuterie : procédure et amorce) : hors de ce lanceur.
  - m4 (option de configuration acceptée en mode réel) : appliquée, couple du rapport ; la configuration rejoint les options de
    l'essai à blanc, refusées en mode réel (la machine ne la passe jamais).
  - f1 à f5 : remarques facultatives, aucune correction exigée ; rien d'appliqué.
  - Points pour la mère (§ 5) : non tranchés ici.
- Changements de nom, conséquences du nom neuf (R12), non corrections du rapport : la version que le lanceur écrit dans ses
  pièces passe à « lanceur-crible-v-v2 », et le lanceur que portent les empreintes du code du crible (addendum, manifeste,
  relevé de la sonde) est ce fichier, `lanceur_crible_v_v2.py`, pour que le code attesté soit celui qui tourne. Les pièces qui
  nomment le lanceur v1 (programme machine, outil de la session, essais, banc, répétition, gabarits, procédure) ne jouent pas
  cette v2 tant que leurs versions neuves ne la nomment pas.
- Rien d'autre ne change de la v1 à la v2 : en tête (version, heure, cette section), les cinq couples du rapport et les deux
  changements de nom ; noms des fichiers écrits, sous-commandes, options, gardes et nombres sont ceux de la v1.
- Rejeu exigé après les couples : essais (paliers unitaire, jouer, mesure) et banc de mutations, joués contre cette v2 ; sorties
  et empreintes rendues à la mère, hors de ce fichier.
"""


def couples_du_redacteur(heure):
    return [
        ("en tête : version, heure, prédécesseur",
         TQ + "Lanceur du crible (v) de l'organisme d'idéation — code v1 (fichier neuf, R12), dérivé du lanceur v74 du pilote MR-2\n",
         TQ + "Lanceur du crible (v) de l'organisme d'idéation — code v2 (fichier neuf, R12 ; `lanceur_crible_v_v1.py` reste en place,\n"
         "inchangé), scellé à " + heure + " (`date -u`) ; suit la v1 (`2636bcb1…`) par les corrections du tour 1 de sa contre-lecture\n"
         "et les seuls changements de nom de la version (section « Contre-lecture », en fin d'en-tête). La v1 était dérivée du lanceur\n"
         "v74 du pilote MR-2\n"),
        ("en tête : section « Contre-lecture »",
         "Codes : 0 conforme ; 2 refus nommé (rien appelé) ; 3 arrêt (pièces versées).\n" + TQ + "\n",
         "Codes : 0 conforme ; 2 refus nommé (rien appelé) ; 3 arrêt (pièces versées).\n\n" + SECTION + TQ + "\n"),
        ("nom : version écrite par le lanceur",
         'VERSION = "lanceur-crible-v-v1"',
         'VERSION = "lanceur-crible-v-v2"'),
        ("nom : lanceur compté dans les empreintes du code du crible",
         'FICHIERS_DU_CRIBLE = ("crible_v_commun_v1.py", "lanceur_crible_v_v1.py", "mesure_crible_v_v1.py", "lire_crible_v_v1.py")',
         'FICHIERS_DU_CRIBLE = ("crible_v_commun_v1.py", "lanceur_crible_v_v2.py", "mesure_crible_v_v1.py", "lire_crible_v_v1.py")'),
    ]


def sha(p):
    with open(p, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def compagnon_egal(p):
    try:
        with open(p + ".sha256", encoding="utf-8") as f:
            lignes = [x for x in f.read().splitlines() if x.strip()]
    except OSError:
        return False
    return lignes == [f"{sha(p)}  {os.path.basename(p)}"]


def refus(motif):
    print(f"REFUS : {motif} ; rien n'est écrit", file=sys.stderr)
    return 2


def main():
    if len(sys.argv) != 4:
        print(__doc__)
        return 2
    src, cible, heure = sys.argv[1:]
    if not re.fullmatch(r"\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ", heure):
        return refus("heure illisible (attendu : date -u +%FT%TZ)")
    if os.path.basename(src) != NOM_SOURCE or os.path.basename(cible) != NOM_CIBLE:
        return refus(f"noms attendus : source {NOM_SOURCE}, cible {NOM_CIBLE}")
    if os.path.lexists(cible):
        return refus("la cible existe déjà (R12 : on n'écrase jamais)")
    if sha(src) != EMPREINTE_SOURCE or not compagnon_egal(src):
        return refus("source d'empreinte ≠ v1 (2636bcb1…) ou différente de son compagnon")
    ici = os.path.dirname(os.path.abspath(src))
    rapport, banc = os.path.join(ici, NOM_RAPPORT), os.path.join(ici, NOM_BANC)
    if not os.path.isfile(rapport) or sha(rapport) != EMPREINTE_RAPPORT or not compagnon_egal(rapport):
        return refus("rapport du tour 1 absent, d'empreinte inattendue ou différent de son compagnon")
    if not os.path.isfile(banc) or not compagnon_egal(banc):
        return refus("banc de mutations v1 absent ou différent de son compagnon")
    with open(rapport, encoding="utf-8") as f:
        texte_rapport = f.read()
    blocs = re.findall(r"^```\n(.*?)\n```$", texte_rapport, flags=re.S | re.M)
    for nom, ancien, nouveau in COUPLES_DU_RAPPORT:
        if blocs.count(ancien) != 1 or blocs.count(nouveau) != 1:
            return refus(f"{nom} : ancien ou nouveau absent des blocs du rapport, ou présent plus d'une fois (recopie inexacte)")
    with open(src, encoding="utf-8") as f:
        t0 = f.read()
    t = t0
    ordre = couples_du_redacteur(heure) + [m4, m1, M3_1, M3_2, M2]  # dans l'ordre des lignes de la v1
    journal = []
    for i, (nom, ancien, nouveau) in enumerate(ordre, 1):
        k = t.count(ancien)
        if k != 1 or t0.count(ancien) != 1:
            return refus(f"couple {i} ({nom}) : « ancien » trouvé {k} fois (attendu 1)")
        ligne = t0[:t0.index(ancien)].count("\n") + 1
        t = t.replace(ancien, nouveau)
        journal.append(f"couple {i} appliqué (ancien à la ligne {ligne} de la v1) : {nom}")
    try:
        compile(t, NOM_CIBLE, "exec")
    except SyntaxError as e:
        return refus(f"le texte neuf ne se compile pas : {e}")
    B = runpy.run_path(banc, run_name="banc_lu_par_le_correcteur")
    vises = [m[3] for m in B["MUTATIONS"] if m[2] == B["L"] and m[3] is not None] + CIBLES_M29_M30
    manques = [v[:60] for v in vises if t.count(v) != 1]
    if manques:
        return refus(f"textes visés par le banc présents ≠ une fois dans la v2 : {manques}")
    if t.count('VERSION = "lanceur-crible-v-v2"') != 1 or t.count('"lanceur_crible_v_v2.py"') != 1 \
            or t.count('"lanceur_crible_v_v1.py"') != 0:
        return refus("changement de nom incomplet")
    with open(cible, "x", encoding="utf-8") as f:
        f.write(t)
    for x in journal:
        print(x)
    print(f"contrôles de sortie : compilé ; {len(vises)} textes visés par le banc (v1 et M29, M30) présents une fois chacun")
    print(f"v2 écrite : {cible} ; {len(ordre)} couples ({len(COUPLES_DU_RAPPORT)} du rapport, {len(ordre) - len(COUPLES_DU_RAPPORT)} du"
          f" rédacteur) ; source {EMPREINTE_SOURCE[:12]}… ; cible {sha(cible)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
