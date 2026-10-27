"""Gardes du choix d'offre (`choisir_offre_v5.py` : CLX-07 ; CLY-03, 24 h de stockage ; CLZ-03, prix majoré de la
tolérance ; CLZ-05, remontée et débit ; CLW-10, 165 Go de descente), du contrôle du prix relu (`verifier_prix_relu` et
`controler_prix_v5.sh`, CLZ-04 : prix égal, +4 %, +6 %, illisible, arrêt relu ou non), du GO cité (`verifier_go_v5.py`,
CLW-03 : périmètre, empreinte du texte scellé, plafond, type, auteur) et de la surveillance (`surveiller_echelle_v5.sh`,
R10 ; plafond exigé dans [4 500 ; 7 200] et égal à celui du lanceur, création et identifiant relus, code de fin de
l'amorce rendu, conteneur sorti sans ligne de fin, CLZ-11, CLW-09), sur des offres fabriquées, un registre fabriqué et
un faux outil vastai (R5). Aucun appel réseau, aucune instance réelle.
Lancement : python -m pytest -q echelle-v5/tests
"""
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
spec = importlib.util.spec_from_file_location("offre", SCRIPTS / "choisir_offre_v5.py")
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
    r = subprocess.run([sys.executable, "-I", "-B", str(SCRIPTS / "choisir_offre_v5.py"), str(brut),
                        str(tmp_path / "offre.json"), prix_max, descente_max, plafond, str(tmp_path / "journal.txt"),
                        str(tmp_path / "relues.json")], capture_output=True, text=True)
    return r.returncode, r.stdout.split()


def test_offre_saine_moins_chere_et_plafonnee(tmp_path):
    code, sortie = choisir(tmp_path, [offre(1, dph_total=3.0), offre(2, dph_total=2.4), offre(3, num_gpus=1)])
    assert code == 0 and sortie[0] == "2"
    duree, pire = int(sortie[3]), float(sortie[4])
    assert duree <= 7200 and pire <= 8.0
    o = json.loads((tmp_path / "offre.json").read_text())
    assert o["tolerance_prix"] == 1.05 and o["attendu_destruction_rapide"] < o["estime"]


def test_offre_plafond_de_duree_calcule(tmp_path):
    # à 3,4 USD/h, 2 h dépasseraient 8 USD au prix majoré, avec la descente et 24 h de stockage : durée raccourcie
    code, sortie = choisir(tmp_path, [offre(1, dph_total=3.4, inet_down_cost=0.005, storage_total_cost=0.05)])
    assert code == 0 and int(sortie[3]) < 7200 and float(sortie[4]) <= 8.0


def depense_reelle_au_pire(o, duree_s, latence_s=80):
    """Dépense si tout est facturé au prix relu le plus haut admis (tolérance), latence de la surveillance comprise."""
    t = OF.TOLERANCE_PRIX
    return ((duree_s + latence_s) / 3600 * t * o["dph_total"] + t * OF.DESCENTE_GO * o["inet_down_cost"]
            + t * OF.MONTEE_GO * o["inet_up_cost"] + t * OF.STOCKAGE_APRES_H * o["storage_total_cost"])


def test_plafond_tenu_au_prix_majore_sur_tout_le_domaine():
    """CLZ-03 : au prix relu le plus haut admis (offre × 1,05), la dépense réelle au pire tient sous 8 USD."""
    pires = []
    for dph, desc, mont, stock in itertools.product((0.8, 1.5, 2.2, 2.9, 3.2, 3.5), (0.0, 0.0026, 0.005),
                                                    (0.0, 0.004, 0.05), (0.0, 0.05, 0.08, 0.15)):
        o = offre(1, dph_total=dph, inet_down_cost=desc, inet_up_cost=mont, storage_total_cost=stock)
        e = OF.evaluer(o, 3.5, 0.005, 8.0)
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
    r = subprocess.run(["bash", str(SCRIPTS / "controler_prix_v5.sh"), "12345678", str(tmp_path / "offre.json"),
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
# faux vastai : l'état vit dans $ETAT_FAUX (running|stopped), les journaux dans $JOURNAL_FAUX, les arrêts dans $ARRETS_FAUX
case "$1 $2" in
  "show instance") echo "{\"actual_status\": \"$(cat "$ETAT_FAUX")\", \"cur_state\": \"$(cat "$ETAT_FAUX")\", \"dph_total\": 2.4, \"status_msg\": \"\"}" ;;
  "logs "*) cat "$JOURNAL_FAUX" ;;
  "stop instance") echo "$3" >> "$ARRETS_FAUX"; [ -n "$ARRET_EFFECTIF" ] && echo stopped > "$ETAT_FAUX"; echo "arrêt demandé" ;;
esac
"""


def surveiller(tmp_path, journal, duree="4500", effectif="1", sans_duree=False, duree_lancement=None, ident="12345678",
               age_s=0, creation_lancement=None, etat_initial="running"):
    faux = faux_vastai(tmp_path, FAUX_VASTAI)
    (tmp_path / "etat").write_text(etat_initial)
    (tmp_path / "journal").write_text(journal)
    creation = str(int(time.time()) - age_s)
    lanc = tmp_path / "lancement"
    lanc.mkdir()
    (lanc / "lancement.txt").write_text(f"go GO-0000-00-00-00\ncreation {creation_lancement or creation}\n"
                                        f"duree_max_s {duree_lancement or duree}\n"
                                        f"succès : True ; identifiant {ident} ; message : essai\n")
    env = dict(os.environ, VASTAI=str(faux), ETAT_FAUX=str(tmp_path / "etat"), JOURNAL_FAUX=str(tmp_path / "journal"),
               ARRETS_FAUX=str(tmp_path / "arrets"), ARRET_EFFECTIF=effectif, DUREE_MAX_S=duree, PAS_S="1",
               ATTENTE_ARRET_S="0")
    if sans_duree:
        env.pop("DUREE_MAX_S")
    r = subprocess.run(["bash", str(SCRIPTS / "surveiller_echelle_v5.sh"), "12345678", creation, str(lanc),
                        str(tmp_path / "s")], env=env, capture_output=True, text=True, timeout=60)
    arrets = (tmp_path / "arrets").read_text().split() if (tmp_path / "arrets").exists() else []
    arret_txt = (tmp_path / "s" / "arret.txt").read_text() if (tmp_path / "s" / "arret.txt").exists() else ""
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


@pytest.mark.parametrize("kw", [dict(sans_duree=True), dict(duree="9000"), dict(duree="7201"), dict(duree="4499"),
                                dict(duree="abc"), dict(duree="5000", duree_lancement="4500"),
                                dict(ident="87654321"), dict(creation_lancement="1700000000")])
def test_surveillance_refus_de_partir(tmp_path, kw):
    code, arrets, _ = surveiller(tmp_path, "AMORCE 2026 : fin, code 0\n", **kw)
    assert code == 2 and arrets == []


# ---------- GO cité (CLW-03) ----------

spec_go = importlib.util.spec_from_file_location("go", SCRIPTS / "verifier_go_v5.py")
GO = importlib.util.module_from_spec(spec_go)
spec_go.loader.exec_module(GO)
EMPREINTE = "0123456789abcdef" + "0" * 48
NOM = "test-echelle-conscience-eval-v6.md"
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
    code = lambda: subprocess.run([sys.executable, "-I", "-B", str(SCRIPTS / "verifier_go_v5.py"), str(f),
                                   "GO-2026-10-27-01", NOM, EMPREINTE, "8.00"], capture_output=True).returncode
    assert code() == 0
    f.write_text(ENTETE + ligne(plafond="2 USD"))
    assert code() == 1
    f.write_text(ENTETE + "| GO-2026-10-27-01 | 2026-10-27 | calcul | sept colonnes | 8 USD | Lazar | mot |\n")
    assert code() == 2


# ---------- gardes nouvelles du lanceur, extraites telles quelles (R5 ; CLW-03, CLW-04, CLW-10) ----------

def bloc_du_lanceur(debut, n_lignes):
    """Les n lignes du lanceur qui commencent par `debut` (la garde et sa suite), telles qu'elles sont dans le script."""
    lignes = (SCRIPTS / "lancer_echelle_v5.sh").read_text(encoding="utf-8").splitlines()
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
    (tmp_path / "verifier_go_v5.py").write_text((SCRIPTS / "verifier_go_v5.py").read_text(encoding="utf-8"))
    (tmp_path / "lancement.txt").write_text("")
    bloc = bloc_du_lanceur('python3 -I -B "$T/verifier_go_v5.py"', 2)
    prelude = (f"T={tmp_path}; DEPOT={tmp_path}; GO=GO-2026-10-27-01; PREREG=prereg/{NOM}; "
               f"EMPREINTE_PREREG={EMPREINTE}; PLAFOND_GO=8.00")
    assert jouer(tmp_path, prelude, bloc) == attendu
