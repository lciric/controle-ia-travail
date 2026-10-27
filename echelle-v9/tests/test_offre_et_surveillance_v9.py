"""Gardes du choix d'offre (`choisir_offre_v9.py` : CLX-07 ; CLY-03, 24 h de stockage ; CLZ-03, prix majoré de la
tolérance ; CLZ-05, remontée et débit ; CLW-10, 165 Go de descente), du contrôle du prix relu (`verifier_prix_relu` et
`controler_prix_v9.sh`, CLZ-04 : prix égal, +4 %, +6 %, illisible, arrêt relu ou non), du GO cité (`verifier_go_v9.py`,
CLW-03 : périmètre, empreinte du texte scellé, plafond, type, auteur), de la surveillance (`surveiller_echelle_v9.sh`,
R10 ; plafond exigé dans [4 500 ; 7 200] et égal à celui du lanceur, création et identifiant relus, code de fin de
l'amorce rendu, conteneur sorti sans ligne de fin, CLZ-11, CLW-09 ; empreinte attendue, CLV-06 ; appels lents ou
bloqués, CLV-02 ; outil sourd au signal d'arrêt, coupé par KILL, CLT-04 ; réglages d'essai bornés et consignés, CLU-02 ;
pause réelle bornée par le plafond, CLU-03), du plafond
de dépense avec toute la latence que couvre la marge (CLU-03) et des gardes du lanceur extraites telles quelles (commit cité, version de vastai, GO relu, empreinte
du texte scellé extraite, CLV-08 ; lanceur et surveillance du commit, CLV-06), sur des offres fabriquées, un registre
fabriqué, un faux dépôt et un faux outil vastai (R5). Aucun appel réseau, aucune instance réelle.
Lancement : python -m pytest -q echelle-v9/tests
"""
import hashlib
import importlib.util
import itertools
import json
import os
import pathlib
import stat
import subprocess
import sys
import time

import pytest

SCRIPTS = pathlib.Path(__file__).resolve().parent.parent / "scripts"
spec = importlib.util.spec_from_file_location("offre", SCRIPTS / "choisir_offre_v9.py")
OF = importlib.util.module_from_spec(spec)
spec.loader.exec_module(OF)


def offre(i, **kw):
    o = {"id": i, "machine_id": 1, "gpu_name": "A100 SXM4", "gpu_ram": 81920, "num_gpus": 2, "cuda_max_good": 13.2,
         "dph_base": 2.3, "dph_total": 2.4, "storage_total_cost": 0.1, "inet_down": 5000.0, "inet_down_cost": 0.004,
         "inet_up_cost": 0.004}
    o.update(kw)
    return o


def choisir(tmp_path, offres, plafond="8.00", prix_max="3.50", descente_max="0.005"):
    brut = tmp_path / "brut.json"
    brut.write_text(json.dumps(offres) if not isinstance(offres, str) else offres)
    r = subprocess.run([sys.executable, "-I", "-B", str(SCRIPTS / "choisir_offre_v9.py"), str(brut),
                        str(tmp_path / "offre.json"), prix_max, descente_max, plafond, str(tmp_path / "journal.txt"),
                        str(tmp_path / "relues.json")], capture_output=True, text=True)
    return r.returncode, r.stdout.split()


def test_offre_saine_moins_chere_et_plafonnee(tmp_path):
    code, sortie = choisir(tmp_path, [offre(1, dph_total=3.0), offre(2, dph_total=2.4), offre(3, num_gpus=1)])
    assert code == 0 and sortie[0] == "2"
    duree, pire = int(sortie[3]), float(sortie[4])
    assert duree <= 10800 and pire <= 8.0
    o = json.loads((tmp_path / "offre.json").read_text())
    assert o["tolerance_prix"] == 1.05 and o["attendu_destruction_rapide"] < o["estime"]


def test_offre_plafond_de_duree_calcule(tmp_path):
    # à 3,4 USD/h, 2 h dépasseraient 8 USD au prix majoré, avec la descente et 24 h de stockage : durée raccourcie
    code, sortie = choisir(tmp_path, [offre(1, dph_total=3.4, inet_down_cost=0.005, storage_total_cost=0.05)])
    assert code == 0 and int(sortie[3]) < 7200 and float(sortie[4]) <= 8.0


PRIX_MAX = 3.5
LATENCE_COUVERTE_S = OF.MARGE / (OF.TOLERANCE_PRIX * PRIX_MAX) * 3600     # ≈ 195,9 s : la borne de la marge (CLU-03)
LATENCE_SURVEILLANCE_S = 2 * 35 + 35          # deux appels bornés après le plafond, puis l'appel d'arrêt (CLV-02) ;
                                              # 30 s, plus 5 s avant KILL si l'outil ignore TERM (CLT-04)


def depense_reelle_au_pire(o, duree_s, latence_s=LATENCE_COUVERTE_S):
    """Dépense si tout est facturé au prix relu le plus haut admis (tolérance), latence de la surveillance comprise :
    par défaut, toute la latence que couvre la marge (CLU-03 ; la v6 comptait 80 s)."""
    t = OF.TOLERANCE_PRIX
    return ((duree_s + latence_s) / 3600 * t * o["dph_total"] + t * OF.DESCENTE_GO * o["inet_down_cost"]
            + t * OF.MONTEE_GO * o["inet_up_cost"] + t * OF.STOCKAGE_APRES_H * o["storage_total_cost"])


def test_plafond_tenu_au_prix_majore_sur_tout_le_domaine():
    """CLZ-03, CLU-03 : au prix relu le plus haut admis (offre × 1,05), avec toute la latence que couvre la marge
    (195,9 s, plus que les 105 s que la surveillance admet au pire, CLT-04), la dépense réelle au pire tient sous
    8 USD."""
    assert LATENCE_COUVERTE_S >= LATENCE_SURVEILLANCE_S
    pires = []
    for dph, desc, mont, stock in itertools.product((0.8, 1.5, 2.2, 2.9, 3.2, 3.5), (0.0, 0.0026, 0.005),
                                                    (0.0, 0.004, 0.05), (0.0, 0.05, 0.08, 0.15)):
        o = offre(1, dph_total=dph, inet_down_cost=desc, inet_up_cost=mont, storage_total_cost=stock)
        e = OF.evaluer(o, PRIX_MAX, 0.005, 8.0)
        if e is not None:
            pires.append(depense_reelle_au_pire(o, e[1]))
    assert pires and max(pires) <= 8.0


@pytest.mark.parametrize("artefact", [
    {"dph_total": 3.9},                      # au-delà du prix maximal
    {"inet_down_cost": 0.04},                # descente trop chère
    {"num_gpus": 1},                         # une seule carte
    {"gpu_ram": 80},                         # unités en Go au lieu de Mo : refusée
    {"cuda_max_good": 12.4},                 # CUDA trop ancien
    {"storage_total_cost": None},            # stockage illisible
    {"inet_up_cost": None},                  # remontée illisible (CLZ-05)
    {"inet_down": 1999.0},                   # débit sous 2 000 Mb/s (CLZ-05)
    {"dph_total": 3.5, "inet_down_cost": 0.005, "storage_total_cost": 1.2},  # plafond de durée < 4 500 s
    {"dph_total": 2.6, "storage_total_cost": 0.2},   # 24 h de stockage après l'arrêt : le pire dépasse 8 USD (CLY-03)
    {"dph_total": 3.3, "storage_total_cost": 0.1, "inet_up_cost": 0.9},   # remontée chère : le pire dépasse 8 USD
])
def test_offre_artefacts(tmp_path, artefact):
    assert choisir(tmp_path, [offre(1, **artefact)])[0] == 3


def test_offre_illisible_ou_ambigue(tmp_path):
    assert choisir(tmp_path, "pas du json")[0] == 2
    assert choisir(tmp_path, [offre(1), offre(1)])[0] == 2


# ---------- prix relu (CLZ-04) ----------

@pytest.mark.parametrize("facteur, conforme", [(1.0, True), (1.04, True), (1.06, False)])
def test_prix_relu_tolerance(facteur, conforme):
    o = offre(1)
    inst = {k: o[k] * facteur for k in OF.CHAMPS_PRIX}
    assert OF.verifier_prix_relu(inst, o)[0] is conforme


def test_prix_relu_un_seul_champ_au_dela():
    o = offre(1)
    assert OF.verifier_prix_relu({**{k: o[k] for k in OF.CHAMPS_PRIX}, "storage_total_cost": 0.2}, o)[0] is False


@pytest.mark.parametrize("instance", [None, "texte", {}, {"dph_total": "2.4"}, {"dph_total": float("nan")},
                                      {"dph_total": 2.4, "storage_total_cost": "0.1"}])
def test_prix_relu_illisible(instance):
    assert OF.verifier_prix_relu(instance, offre(1))[0] is False


def test_prix_relu_champs_secondaires_absents_consignes():
    ok, lignes = OF.verifier_prix_relu({"dph_total": 2.4}, offre(1))
    assert ok and sum("non relu" in x for x in lignes) == 3


def test_prix_relu_offre_illisible():
    assert OF.verifier_prix_relu({"dph_total": 2.4}, {**offre(1), "inet_up_cost": None})[0] is False


def faux_vastai(tmp_path, script):
    faux = tmp_path / "vastai"
    faux.write_text(script)
    faux.chmod(faux.stat().st_mode | stat.S_IEXEC)
    return faux


FAUX_PRIX = r"""#!/usr/bin/env bash
# faux vastai du contrôle de prix : la réponse de « show instance » vit dans $INSTANCE_FAUSSE ; l'état après l'arrêt
# dans $ETAT_FAUX ; les arrêts demandés dans $ARRETS_FAUX
case "$1 $2" in
  "show instance") if [ -s "$ARRETS_FAUX" ]; then echo "{\"actual_status\": \"$(cat "$ETAT_FAUX")\", \"cur_state\": \"$(cat "$ETAT_FAUX")\"}"; else cat "$INSTANCE_FAUSSE"; fi ;;
  "stop instance") echo "$3" >> "$ARRETS_FAUX"; echo "arrêt demandé" ;;
esac
"""


def controler(tmp_path, instance, etat_apres="stopped"):
    faux = faux_vastai(tmp_path, FAUX_PRIX)
    (tmp_path / "offre.json").write_text(json.dumps(offre(1)))
    (tmp_path / "instance.json").write_text(instance if isinstance(instance, str) else json.dumps(instance))
    (tmp_path / "etat").write_text(etat_apres)
    env = dict(os.environ, VASTAI=str(faux), INSTANCE_FAUSSE=str(tmp_path / "instance.json"),
               ETAT_FAUX=str(tmp_path / "etat"), ARRETS_FAUX=str(tmp_path / "arrets"), ATTENTE_ARRET_S="0")
    r = subprocess.run(["bash", str(SCRIPTS / "controler_prix_v9.sh"), "12345678", str(tmp_path / "offre.json"),
                        str(tmp_path / "journal.txt")], env=env, capture_output=True, text=True, timeout=60)
    arrets = (tmp_path / "arrets").read_text().split() if (tmp_path / "arrets").exists() else []
    return r.returncode, arrets


def prix(facteur):
    return {k: offre(1)[k] * facteur for k in OF.CHAMPS_PRIX}


def test_controle_prix_egal(tmp_path):
    assert controler(tmp_path, prix(1.0)) == (0, [])


def test_controle_prix_plus_4(tmp_path):
    assert controler(tmp_path, prix(1.04)) == (0, [])


def test_controle_prix_plus_6_arret_relu(tmp_path):
    assert controler(tmp_path, prix(1.06)) == (4, ["12345678"])          # arrêt par identifiant (R10)


def test_controle_prix_illisible_arret_relu(tmp_path):
    assert controler(tmp_path, "pas du json") == (4, ["12345678"])


def test_controle_prix_arret_non_relu(tmp_path):
    assert controler(tmp_path, prix(1.06), etat_apres="running") == (6, ["12345678"])


# ---------- surveillance ----------

FAUX_VASTAI = r"""#!/usr/bin/env bash
# faux vastai : l'état vit dans $ETAT_FAUX (running|stopped), les journaux dans $JOURNAL_FAUX, les arrêts dans
# $ARRETS_FAUX (et leur heure dans $ARRETS_FAUX.heure) ; avant tout arrêt, « show » et « logs » répondent en
# $LENTEUR_FAUSSE secondes (CLV-02) ; avec $SOURD_FAUX, l'outil ignore TERM (CLT-04)
[ -n "${SOURD_FAUX:-}" ] && trap '' TERM
case "$1 $2" in
  "show instance") [ -s "$ARRETS_FAUX" ] || sleep "$LENTEUR_FAUSSE"; echo "{\"actual_status\": \"$(cat "$ETAT_FAUX")\", \"cur_state\": \"$(cat "$ETAT_FAUX")\", \"dph_total\": 2.4, \"status_msg\": \"\"}" ;;
  "logs "*) [ -s "$ARRETS_FAUX" ] || sleep "$LENTEUR_FAUSSE"; cat "$JOURNAL_FAUX" ;;
  "stop instance") date +%s.%N >> "$ARRETS_FAUX.heure"; echo "$3" >> "$ARRETS_FAUX"; [ -n "$ARRET_EFFECTIF" ] && echo stopped > "$ETAT_FAUX"; echo "arrêt demandé" ;;
esac
"""
SURVEILLANCE = SCRIPTS / "surveiller_echelle_v9.sh"


def sha_fichier(f):
    return hashlib.sha256(pathlib.Path(f).read_bytes()).hexdigest()


def surveiller(tmp_path, journal, duree="4500", effectif="1", sans_duree=False, duree_lancement=None, ident="12345678",
               age_s=0, creation_lancement=None, etat_initial="running", attendue=None, lenteur="0", appel_s=None,
               avec_heure=False, reglages=None, sourd=""):
    """`attendue` : empreinte écrite par le lanceur (par défaut, celle du script ; "" : ligne absente, CLV-06)."""
    faux = faux_vastai(tmp_path, FAUX_VASTAI)
    (tmp_path / "etat").write_text(etat_initial)
    (tmp_path / "journal").write_text(journal)
    creation = str(int(time.time()) - age_s)
    lanc = tmp_path / "lancement"
    lanc.mkdir()
    attendue = sha_fichier(SURVEILLANCE) if attendue is None else attendue
    (lanc / "lancement.txt").write_text((f"surveillance attendue {attendue}\n" if attendue else "")
                                        + f"go GO-0000-00-00-00\ncreation {creation_lancement or creation}\n"
                                        f"duree_max_s {duree_lancement or duree}\n"
                                        f"succès : True ; identifiant {ident} ; message : essai\n")
    env = dict(os.environ, VASTAI=str(faux), ETAT_FAUX=str(tmp_path / "etat"), JOURNAL_FAUX=str(tmp_path / "journal"),
               ARRETS_FAUX=str(tmp_path / "arrets"), ARRET_EFFECTIF=effectif, DUREE_MAX_S=duree, PAS_S="1",
               ATTENTE_ARRET_S="0", LENTEUR_FAUSSE=lenteur, SOURD_FAUX=sourd)
    if appel_s is not None:
        env["APPEL_S"] = appel_s
    env.update(reglages or {})
    if sans_duree:
        env.pop("DUREE_MAX_S")
    attente = int(env["ATTENTE_ARRET_S"]) if env["ATTENTE_ARRET_S"].isdigit() else 0
    r = subprocess.run(["bash", str(SURVEILLANCE), "12345678", creation, str(lanc), str(tmp_path / "s")], env=env,
                       capture_output=True, text=True, timeout=60 + attente)
    arrets = (tmp_path / "arrets").read_text().split() if (tmp_path / "arrets").exists() else []
    arret_txt = (tmp_path / "s" / "arret.txt").read_text() if (tmp_path / "s" / "arret.txt").exists() else ""
    if avec_heure:
        heures = [float(x) for x in (tmp_path / "arrets.heure").read_text().split()]
        return r.returncode, arrets, arret_txt, heures, int(creation) + int(duree)
    return r.returncode, arrets, arret_txt


def test_surveillance_fin_saine(tmp_path):
    code, arrets, txt = surveiller(tmp_path, "ECHELLE 2026 : fini\nAMORCE 2026 : fin, code 0\n")
    assert code == 0 and arrets == ["12345678"] and "code 0" in txt          # arrêt par identifiant (R10)


@pytest.mark.parametrize("code_amorce", ["1", "124"])
def test_surveillance_amorce_en_echec(tmp_path, code_amorce):
    code, arrets, txt = surveiller(tmp_path, f"AMORCE 2026 : fin, code {code_amorce}\n")
    assert code == 7 and arrets == ["12345678"] and f"code {code_amorce}" in txt


def test_surveillance_plafond(tmp_path):
    # création 4 499 s dans le passé : le plafond de 4 500 s tombe à la première ou à la deuxième relève
    code, arrets, txt = surveiller(tmp_path, "ECHELLE 2026 : mesure\n", age_s=4499)
    assert code == 5 and arrets == ["12345678"] and "plafond" in txt


def test_surveillance_arret_non_relu(tmp_path):
    code, arrets, _ = surveiller(tmp_path, "AMORCE 2026 : fin, code 0\n", effectif="")
    assert code == 6 and arrets == ["12345678"]


def test_surveillance_conteneur_sorti_sans_ligne_de_fin(tmp_path):
    """CLW-09 : le conteneur est sorti sans ligne « fin, code » : arrêt par identifiant, code 5."""
    code, arrets, txt = surveiller(tmp_path, "ECHELLE 2026 : mesure\n", etat_initial="exited")
    assert code == 5 and arrets == ["12345678"] and "conteneur sorti" in txt


@pytest.mark.parametrize("kw", [dict(sans_duree=True), dict(duree="12000"), dict(duree="10801"), dict(duree="4499"),
                                dict(duree="abc"), dict(duree="5000", duree_lancement="4500"),
                                dict(ident="87654321"), dict(creation_lancement="1700000000"),
                                dict(attendue="0" * 64), dict(attendue="")])          # CLV-06
def test_surveillance_refus_de_partir(tmp_path, kw):
    code, arrets, _ = surveiller(tmp_path, "AMORCE 2026 : fin, code 0\n", **kw)
    assert code == 2 and arrets == []


@pytest.mark.parametrize("reglages", [{"APPEL_S": "0"}, {"APPEL_S": "31"}, {"APPEL_S": "030"}, {"APPEL_S": ""},
                                      {"PAS_S": "abc"}, {"PAS_S": "0"}, {"PAS_S": "61"}, {"PAS_S": "1.5"},
                                      {"ATTENTE_ARRET_S": "61"}, {"ATTENTE_ARRET_S": "-1"}])
def test_surveillance_reglages_hors_bornes(tmp_path, reglages):
    """CLU-02 : un réglage d'essai illisible ou hors de ses bornes (APPEL_S=0 ôterait la borne des appels ; PAS_S=abc
    ferait sortir la surveillance sans arrêter l'instance) : refus de partir, code 2, avant tout appel."""
    code, arrets, txt = surveiller(tmp_path, "AMORCE 2026 : fin, code 0\n", reglages=reglages)
    assert code == 2 and arrets == [] and txt == "" and not (tmp_path / "s").exists()


@pytest.mark.parametrize("reglages", [{}, {"APPEL_S": "1", "PAS_S": "60", "ATTENTE_ARRET_S": "60"},
                                      {"APPEL_S": "30", "PAS_S": "1", "ATTENTE_ARRET_S": "0"}])
def test_surveillance_reglages_consignes(tmp_path, reglages):
    """CLU-02, cas sains (bornes comprises) : les valeurs employées sont écrites en tête d'etats.txt et dans arret.txt."""
    code, arrets, txt = surveiller(tmp_path, "AMORCE 2026 : fin, code 0\n", reglages=reglages)
    v = {"APPEL_S": "30", "PAS_S": "1", "ATTENTE_ARRET_S": "0", **reglages}
    attendu = f"réglages : APPEL_S={v['APPEL_S']} PAS_S={v['PAS_S']} ATTENTE_ARRET_S={v['ATTENTE_ARRET_S']} DUREE_MAX_S=4500"
    assert code == 0 and arrets == ["12345678"] and attendu in txt
    assert (tmp_path / "s" / "etats.txt").read_text().splitlines()[0] == attendu


def test_surveillance_pause_bornee_par_le_plafond(tmp_path):
    """CLU-03 : pause réelle (PAS_S = 60 s), appels instantanés, plafond 5 s après le départ : la pause s'arrête au
    plafond, l'arrêt est demandé au plus 2 s après lui (une pause de 60 s non bornée le demanderait 55 s après)."""
    code, arrets, txt, heures, fin = surveiller(tmp_path, "ECHELLE 2026 : mesure\n", age_s=4495, avec_heure=True,
                                                reglages={"PAS_S": "60"})
    assert code == 5 and arrets == ["12345678"] and "plafond" in txt and "PAS_S=60" in txt
    assert fin <= heures[0] <= fin + 2


@pytest.mark.parametrize("lenteur, appel_s", [("2", "3"),        # appels lents, sous leur borne
                                               ("30", "2")])     # appels bloqués, coupés à leur borne
def test_surveillance_appels_lents(tmp_path, lenteur, appel_s):
    """CLV-02 : le plafond tombe une seconde après le départ, pendant les appels ; l'heure relue après les appels et la
    pause bornée par le temps qui reste font demander l'arrêt au plus deux appels après le plafond (la v5, qui testait
    l'heure lue avant les appels, attendait encore une pause et deux appels)."""
    code, arrets, txt, heures, fin = surveiller(tmp_path, "ECHELLE 2026 : mesure\n", age_s=4499, lenteur=lenteur,
                                                appel_s=appel_s, avec_heure=True)
    assert code == 5 and arrets == ["12345678"] and "plafond" in txt
    assert fin <= heures[0] <= fin + 2 * int(appel_s) + 1


def test_surveillance_outil_sourd_au_signal(tmp_path):
    """CLT-04 : un outil qui ignore TERM et ne rend pas la main (30 s) ; appels bornés à 2 s : KILL 5 s après TERM,
    chaque appel coupé à 7 s ; l'arrêt est demandé au plus deux appels après le plafond (la v7 attendait la fin de
    chaque appel : 598 s dans l'essai de cl7)."""
    code, arrets, txt, heures, fin = surveiller(tmp_path, "ECHELLE 2026 : mesure\n", age_s=4499, lenteur="30",
                                                appel_s="2", avec_heure=True, sourd="1")
    assert code == 5 and arrets == ["12345678"] and "plafond" in txt
    assert fin <= heures[0] <= fin + 2 * (2 + 5) + 1


# ---------- GO cité (CLW-03) ----------

spec_go = importlib.util.spec_from_file_location("go", SCRIPTS / "verifier_go_v9.py")
GO = importlib.util.module_from_spec(spec_go)
spec_go.loader.exec_module(GO)
EMPREINTE = "0123456789abcdef" + "0" * 48
NOM = "test-echelle-conscience-eval-v10.md"
ENTETE = """# Registre des GO

| id | accordé le | type | périmètre | plafond | échéance | accordé par | référence |
|---|---|---|---|---|---|---|---|
"""


def ligne(ident="GO-2026-10-27-01", type_="calcul", perimetre=None, plafond="8 USD", par="Lazar"):
    perimetre = perimetre if perimetre is not None else f"comparaison d'échelle, `prereg/{NOM}` (`{EMPREINTE}`)"
    return f"| {ident} | 2026-10-27 | {type_} | {perimetre} | {plafond} | 2026-10-31 | {par} | mot direct |\n"


@pytest.mark.parametrize("lignes, conforme", [
    ([ligne()], True),
    ([ligne(plafond="12,5 USD")], True),
    ([ligne(), ligne(perimetre="extension : durée prolongée")], True),       # ligne d'extension non lue
    ([ligne(perimetre=f"pré-autorisation d'une autre expérience")], False),  # autre périmètre (CLW-03)
    ([ligne(perimetre=f"`prereg/{NOM}`, sans empreinte")], False),          # GO antérieur au scellement
    ([ligne(plafond="2 USD")], False),                                       # plafond plus petit
    ([ligne(plafond="—")], False),                                           # plafond illisible
    ([ligne(type_="porte")], False),
    ([ligne(par="la session")], False),
    ([ligne(), ligne()], False),                                             # doublon hors extension
    ([ligne(ident="GO-2026-10-27-02")], False),                              # GO absent
])
def test_go(lignes, conforme):
    ok, motifs = GO.verifier(ENTETE + "".join(lignes), "GO-2026-10-27-01", NOM, EMPREINTE, 8.0)
    assert ok is conforme and (ok or motifs)


def test_go_ligne_mal_formee_et_codes(tmp_path):
    f = tmp_path / "go.md"
    f.write_text(ENTETE + ligne())
    code = lambda: subprocess.run([sys.executable, "-I", "-B", str(SCRIPTS / "verifier_go_v9.py"), str(f),
                                   "GO-2026-10-27-01", NOM, EMPREINTE, "8.00"], capture_output=True).returncode
    assert code() == 0
    f.write_text(ENTETE + ligne(plafond="2 USD"))
    assert code() == 1
    f.write_text(ENTETE + "| GO-2026-10-27-01 | 2026-10-27 | calcul | sept colonnes | 8 USD | Lazar | mot |\n")
    assert code() == 2


# ---------- gardes nouvelles du lanceur, extraites telles quelles (R5 ; CLW-03, CLW-04, CLW-10) ----------

def bloc_du_lanceur(debut, n_lignes):
    """Les n lignes du lanceur qui commencent par `debut` (la garde et sa suite), telles qu'elles sont dans le script."""
    lignes = (SCRIPTS / "lancer_echelle_v9.sh").read_text(encoding="utf-8").splitlines()
    i = [k for k, l in enumerate(lignes) if l.startswith(debut)]
    assert len(i) == 1, debut
    return "\n".join(lignes[i[0]:i[0] + n_lignes])


def jouer(tmp_path, prelude, bloc):
    script = tmp_path / "essai.sh"
    script.write_text("set -uo pipefail\n" + prelude + "\n" + bloc + "\necho passe\n")
    r = subprocess.run(["bash", str(script)], capture_output=True, text=True, timeout=60)
    return r.returncode, "passe" in r.stdout


@pytest.mark.parametrize("cite, attendu", [(True, (0, True)), (False, (2, False))])
def test_lanceur_texte_scelle_cite_le_commit(tmp_path, cite, attendu):
    """CLW-04 : un texte scellé qui ne cite pas le commit lancé arrête avant toute création."""
    commit = "f" * 40
    (tmp_path / "prereg").mkdir()
    (tmp_path / "prereg" / "texte.md").write_text(f"commit `{commit if cite else '0' * 40}`\n")
    bloc = bloc_du_lanceur('grep -qF "$COMMIT" "$DEPOT/$PREREG"', 2)
    prelude = f'COMMIT={commit}; DEPOT={tmp_path}; PREREG=prereg/texte.md; T={tmp_path}'
    assert jouer(tmp_path, prelude, bloc) == attendu


@pytest.mark.parametrize("version, attendu", [("1.8.3", (0, True)), ("1.8.2", (2, False)), ("", (2, False))])
def test_lanceur_version_de_vastai(tmp_path, version, attendu):
    """CLW-10 : une autre version de vastai que 1.8.3 arrête avant tout appel."""
    faux = faux_vastai(tmp_path, f'#!/usr/bin/env bash\n[ "$1" = --version ] && echo "{version}"\n')
    bloc = bloc_du_lanceur('[ "$("$V" --version', 1)
    assert jouer(tmp_path, f"V={faux}", bloc) == attendu


@pytest.mark.parametrize("plafond, attendu", [("8 USD", (0, True)), ("2 USD", (2, False))])
def test_lanceur_go_relu(tmp_path, plafond, attendu):
    """CLW-03 : la ligne du lanceur qui relit le GO arrête si le GO n'est pas propre à l'expérience."""
    (tmp_path / "registres").mkdir()
    (tmp_path / "registres" / "go.md").write_text(ENTETE + ligne(plafond=plafond))
    (tmp_path / "verifier_go_v9.py").write_text((SCRIPTS / "verifier_go_v9.py").read_text(encoding="utf-8"))
    (tmp_path / "lancement.txt").write_text("")
    bloc = bloc_du_lanceur('python3 -I -B "$T/verifier_go_v9.py"', 2)
    prelude = (f"T={tmp_path}; DEPOT={tmp_path}; GO=GO-2026-10-27-01; PREREG=prereg/{NOM}; "
               f"EMPREINTE_PREREG={EMPREINTE}; PLAFOND_GO=8.00")
    assert jouer(tmp_path, prelude, bloc) == attendu


def jouer_sortie(tmp_path, prelude, bloc, apres=""):
    script = tmp_path / "essai.sh"
    script.write_text("set -uo pipefail\n" + prelude + "\n" + bloc + "\n" + apres + "\necho passe\n")
    r = subprocess.run(["bash", str(script)], capture_output=True, text=True, timeout=60, env=dict(os.environ))
    return r.returncode, r.stdout


STUB_PREREG = '''import os


def exiger_prereg_scelle(chemin):
    mode = os.environ["ESSAI_PREREG"]
    if mode == "scelle":
        return "ab" * 32
    if mode == "court":
        return "abc"
    raise RuntimeError(f"{chemin} : non scellé")
'''


@pytest.mark.parametrize("mode, attendu", [("scelle", (0, "ab" * 32)), ("court", (2, None)), ("refus", (2, None))])
def test_lanceur_empreinte_du_texte_scelle_extraite(tmp_path, monkeypatch, mode, attendu):
    """CLV-08 : les lignes du lanceur qui appellent la garde de scellement et extraient l'empreinte passée au contrôle du
    GO, jouées telles quelles sur un faux dépôt dont la garde rend une empreinte (cas sain), une réponse trop courte ou
    un refus (artefacts) ; la garde réelle a ses propres tests dans le dépôt."""
    depot = tmp_path / "depot"
    (depot / "src" / "controle_ia").mkdir(parents=True)
    (depot / "src" / "controle_ia" / "__init__.py").write_text("")
    (depot / "src" / "controle_ia" / "prereg.py").write_text(STUB_PREREG)
    (tmp_path / "t").mkdir()
    monkeypatch.setenv("ESSAI_PREREG", mode)
    bloc = bloc_du_lanceur('(cd "$DEPOT" && PYTHONPATH=src python3', 4)
    assert "EMPREINTE_PREREG=" in bloc.splitlines()[-1]
    code, sortie = jouer_sortie(tmp_path, f"DEPOT={depot}; PREREG=prereg/texte.md; T={tmp_path / 't'}", bloc,
                                'echo "empreinte=$EMPREINTE_PREREG"')
    extraite = next((l.split("=", 1)[1] for l in sortie.splitlines() if l.startswith("empreinte=")), None)
    assert (code, extraite) == attendu


def depot_du_commit(tmp_path, lanceur, surveillance):
    """Faux dépôt git dont un commit porte le lanceur et la surveillance donnés ; rend (dépôt, commit)."""
    d = tmp_path / "depot-git"
    (d / "echelle-v9" / "scripts").mkdir(parents=True)
    (d / "echelle-v9" / "scripts" / "lancer_echelle_v9.sh").write_bytes(lanceur)
    (d / "echelle-v9" / "scripts" / "surveiller_echelle_v9.sh").write_bytes(surveillance)
    g = ["git", "-C", str(d), "-c", "user.name=essai", "-c", "user.email=essai@invalid"]
    subprocess.run(["git", "init", "-q", str(d)], check=True)
    subprocess.run(g + ["add", "."], check=True)
    subprocess.run(g + ["commit", "-q", "-m", "essai"], check=True)
    commit = subprocess.run(["git", "-C", str(d), "rev-parse", "HEAD"], check=True, capture_output=True,
                            text=True).stdout.strip()
    return d, commit


@pytest.mark.parametrize("lanceur_modifie, attendu", [(False, 0), (True, 2)])
def test_lanceur_et_surveillance_du_commit(tmp_path, lanceur_modifie, attendu):
    """CLV-06 : les lignes du lanceur qui comparent son empreinte à celle du fichier du commit et écrivent l'empreinte
    attendue de la surveillance, jouées telles quelles ; la surveillance relit cette ligne (test de refus de partir)."""
    vrai = (SCRIPTS / "lancer_echelle_v9.sh").read_bytes()
    depot, commit = depot_du_commit(tmp_path, vrai, SURVEILLANCE.read_bytes())
    local = tmp_path / "lancer_echelle_v9.sh"
    local.write_bytes(vrai + (b"# copie modifiee\n" if lanceur_modifie else b""))
    (tmp_path / "t").mkdir()
    bloc = bloc_du_lanceur('L_COMMIT=$(git -C "$DEPOT" show', 4)
    code, _ = jouer_sortie(tmp_path, f"DEPOT={depot}; COMMIT={commit}; LANCEUR={local}; T={tmp_path / 't'}", bloc)
    assert code == attendu
    ecrit = (tmp_path / "t" / "lancement.txt").read_text() if (tmp_path / "t" / "lancement.txt").exists() else ""
    assert (f"surveillance attendue {sha_fichier(SURVEILLANCE)}" in ecrit) is (attendu == 0)


# ---------- v9 (R-555) : plafond de durée de 3 h ; crédit et recharge automatique déclarée ----------

def test_offre_trois_heures_sous_quatorze_usd(tmp_path):
    """v9 : à 3,37 USD/h, un plafond de 14 USD laisse les 3 h entières ; 8 USD les raccourcit."""
    o = [offre(1, dph_total=3.3694, inet_down_cost=0.004, storage_total_cost=0.0694)]
    code, sortie = choisir(tmp_path, o, plafond="14")
    assert code == 0 and int(sortie[3]) == 10800 and float(sortie[4]) <= 14.0
    (tmp_path / "huit").mkdir()
    code, sortie = choisir(tmp_path / "huit", o, plafond="8")
    assert code == 0 and int(sortie[3]) < 7200 and float(sortie[4]) <= 8.0


def bloc_credit():
    lignes = (SCRIPTS / "lancer_echelle_v9.sh").read_text(encoding="utf-8").splitlines()
    i = [k for k, l in enumerate(lignes) if l.startswith('CREDIT_LIGNE=$(timeout 60 "$V" show user --raw')]
    assert len(i) == 1
    j = next(k for k in range(i[0], len(lignes)) if lignes[k] == "esac")
    return "\n".join(lignes[i[0]:j + 1])


@pytest.mark.parametrize("credit, recharge, attendu, mot", [
    ("6.81", "0", (3, False), "minimum 9.20 USD"),          # cas du 27 octobre, 13:15 UTC (R-554)
    ("9.20", "0", (0, True), "minimum 9.20 USD"),
    ("6.81", "1", (0, True), "non exigé : recharge automatique déclarée"),
    ("\"x\"", "1", (2, False), "crédit illisible"),          # illisible : arrêt, même sous recharge automatique
    ("\"x\"", "0", (2, False), "crédit illisible")])
def test_lanceur_credit_et_recharge_automatique(tmp_path, credit, recharge, attendu, mot):
    """R5 : le contrôle du crédit, extrait tel quel ; RECHARGE_AUTO=1 consigne le crédit sans exiger le minimum."""
    faux = faux_vastai(tmp_path, f'#!/usr/bin/env bash\necho \'{{"credit": {credit}}}\'\n')
    prelude = (f"V={faux}; T={tmp_path}; HEURES_CREDIT=2; PIRE=8.00; SOMME_AUTRES=0; RECHARGE_AUTO={recharge}; "
               f": > {tmp_path}/lancement.txt; c=0")
    code, sortie = jouer_sortie(tmp_path, prelude, bloc_credit())
    assert (code, "passe" in sortie) == attendu and mot in sortie


@pytest.mark.parametrize("valeur, attendu", [("0", (0, True)), ("1", (0, True)), ("2", (2, False)), ("oui", (2, False))])
def test_lanceur_recharge_auto_lisible(tmp_path, valeur, attendu):
    bloc = bloc_du_lanceur('[[ "$RECHARGE_AUTO" =~ ^[01]$ ]]', 1)
    assert jouer(tmp_path, f"RECHARGE_AUTO={valeur}", bloc) == attendu
