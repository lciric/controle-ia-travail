"""(ii-b), consigne invisible v1 (conception, section 10 ; modèle : `tests/test_t06_cibles_invisibles_v1.py`). Un marqueur planté dans la
consigne factice du maître n'apparaît dans **aucune** transcription de distillation (élève, témoin-jumeau), **aucune** invite
d'évaluation, **aucun** contexte du jumeau, **aucun** fichier écrit (le maître jouet ne l'écrit jamais dans ses actions, les textes
du maître compris), ni sur les sorties standard et d'erreur ; les cibles marquées des tâches factices non plus. Gardes éprouvées
(R5) : la collecte voit le marqueur dans les invites du maître (elle voit bien les invites) ; si le maître recopie le marqueur dans
ses actions, la collecte le trouve dans les transcriptions de distillation et dans les textes écrits (elle voit bien les
transcriptions et les fichiers)."""
from __future__ import annotations

import re
import subprocess

import pytest

from controle_ia.harnais import formats
from controle_ia.iib import jouet_v1 as jv
from controle_ia.iib import lanceur_v1 as la
from controle_ia.iib import modele_v1 as mv

RUN = "20261114-070000-iib-jouet"
MARQUEURS = (jv.MARQUEUR_CONSIGNE.casefold(), jv.MARQUEUR_CIBLES.casefold(), "987654.321", "7654321")


def _fuit(texte: str) -> bool:
    compact = re.sub(r"\s+", "", str(texte)).casefold()
    return any(m in compact for m in MARQUEURS)


def _consigne_fuit(texte: str) -> bool:
    return jv.MARQUEUR_CONSIGNE.casefold() in re.sub(r"\s+", "", str(texte)).casefold()


def _collecter(tmp_path, monkeypatch, capfd, recopier: bool) -> dict:
    d = tmp_path / "d"
    d.mkdir()
    for a in (["init", "-q", "-b", "main"], ["config", "user.email", "t@example.invalid"], ["config", "user.name", "t"]):
        subprocess.run(["git", "-C", str(d), *a], check=True)
    c = jv.preparer_monde(d)
    subprocess.run(["git", "-C", str(d), "add", "-A"], check=True)
    subprocess.run(["git", "-C", str(d), "commit", "-qm", "x"], check=True)
    vus = {"invites": [], "jumeau": [], "distillation": []}
    phase = {"courante": "chargement"}

    def espion_ouverture(original):
        def f(self, consigne, observation):
            vus["invites"].append((phase["courante"], str(consigne) + "\n" + str(observation)))
            return original(self, consigne, observation)
        return f
    for classe in (formats.FormatBrut, formats.FormatChat):
        monkeypatch.setattr(classe, "ouverture", espion_ouverture(classe.ouverture))
    plan_original = la.jouer_plan

    def espion_plan(modele, plan, config, entrees, g, quoi, chrono):
        phase["courante"] = quoi
        return plan_original(modele, plan, config, entrees, g, quoi, chrono)
    monkeypatch.setattr(la, "jouer_plan", espion_plan)
    oracle_original = la.appliquer_oracle

    def espion_oracle(*a, **k):
        avant, phase["courante"] = phase["courante"], "oracle"
        try:
            return oracle_original(*a, **k)
        finally:
            phase["courante"] = avant
    monkeypatch.setattr(la, "appliquer_oracle", espion_oracle)
    tours_originaux = la.tv.boucle_des_tours

    def espion_tours(*a, **k):
        try:
            return tours_originaux(*a, **k)
        finally:
            phase["courante"] = "distillation"
    monkeypatch.setattr(la.tv, "boucle_des_tours", espion_tours)
    suites_originales = mv.ModeleJouetScripte.suites

    def espion_suites(self, prefixe, graines, max_jetons, temperature):
        vus["jumeau"].append(self.fmt.tok.decode(list(prefixe), skip_special_tokens=False))
        return suites_originales(self, prefixe, graines, max_jetons, temperature)
    monkeypatch.setattr(mv.ModeleJouetScripte, "suites", espion_suites)
    distiller_original = la.dt.distiller_transcriptions

    def espion_distiller(modele, exemples, *a, **k):
        for ids, _ in exemples:
            vus["distillation"].append(phase_tok["tok"].decode(ids, skip_special_tokens=False))
        return distiller_original(modele, exemples, *a, **k)
    phase_tok = {"tok": mv.format_jouet().tok}
    monkeypatch.setattr(la.dt, "distiller_transcriptions", espion_distiller)
    if recopier:
        action_originale = mv.ModeleJouetScripte._action

        def recopie(self, contexte, graine):
            texte = action_originale(self, contexte, graine)
            systeme = contexte.split("<|im_end|>", 1)[0]
            premier = contexte.count("<|im_start|>assistant") == 1          # le premier pas seulement : l'action sort de la perte,
            return texte + (f" {jv.MARQUEUR_CONSIGNE}" if self.cfg["signal_maitre"] in systeme and premier else "")   # les autres restent
        monkeypatch.setattr(mv.ModeleJouetScripte, "_action", recopie)
    la.executer(c, d, RUN)
    sortie, erreur = capfd.readouterr()
    fichiers = [(str(p.relative_to(d)), p.read_text(encoding="utf-8", errors="replace")) for dossier in ("diag", "donnees", "runs")
                for p in sorted((d / dossier).rglob("*")) if p.is_file() and p.suffix in (".json", ".jsonl", ".txt", ".sha256")]
    return {**vus, "fichiers": fichiers, "sortie": sortie + "\n" + erreur}


def test_marqueur_de_la_consigne_absent_de_tout_ce_qui_n_est_pas_le_maitre(tmp_path, monkeypatch, capfd):
    r = _collecter(tmp_path, monkeypatch, capfd, recopier=False)
    maitre = [x for p, x in r["invites"] if p.startswith("maitre-tour")]
    autres = [x for p, x in r["invites"] if not p.startswith("maitre-tour")]
    assert maitre and all(_consigne_fuit(x) for x in maitre)                    # R5 : la collecte voit les invites du maître
    assert autres and not [x for x in autres if _fuit(x)]                        # étalonnage, oracle et évaluation : aucune
    assert any(p == "oracle" for p, _ in r["invites"])
    assert any(p.startswith("evaluation-") for p, _ in r["invites"])
    assert len(r["jumeau"]) > 100 and not [x for x in r["jumeau"] if _fuit(x)]  # aucun contexte du jumeau
    assert len(r["distillation"]) >= 2 and not [x for x in r["distillation"] if _fuit(x)]
    assert r["fichiers"] and not [n for n, t in r["fichiers"] if _fuit(t)]      # aucun fichier écrit, textes du maître compris
    assert not _fuit(r["sortie"])
    assert not [x for p, x in r["invites"] if p.startswith("maitre-tour") and (jv.MARQUEUR_CIBLES.casefold() in x.casefold())]


def test_garde_la_collecte_voit_une_fuite_plantee(tmp_path, monkeypatch, capfd):
    """Artefact (R5) : le maître recopie le marqueur dans ses actions ; il atteint les transcriptions de distillation (élève et
    témoin-jumeau : l'action sort de la perte par le motif, mais reste au contexte) et le fichier des textes : la collecte le voit."""
    r = _collecter(tmp_path, monkeypatch, capfd, recopier=True)
    assert any(_consigne_fuit(x) for x in r["distillation"])
    assert any(_consigne_fuit(t) for n, t in r["fichiers"] if n.endswith("textes-actions-iib.jsonl"))
    assert any(_consigne_fuit(x) for x in r["jumeau"])                           # contexte réécrit : seules les valeurs COST changent
    assert [n for n, t in r["fichiers"] if _consigne_fuit(t)] == [n for n, _ in r["fichiers"] if n.endswith("textes-actions-iib.jsonl")]


def test_garde_le_balayage_voit_un_marqueur_plante(tmp_path):
    (tmp_path / "diag").mkdir()
    (tmp_path / "diag" / "x.json").write_text(f'{{"y": "{jv.MARQUEUR_CONSIGNE}"}}', encoding="utf-8")
    assert _fuit((tmp_path / "diag" / "x.json").read_text(encoding="utf-8"))
    assert not _fuit('{"y": "propre"}')


@pytest.mark.parametrize("texte", [jv.CONSIGNE_FACTICE])
def test_le_marqueur_est_bien_dans_la_consigne_factice(texte):
    assert jv.MARQUEUR_CONSIGNE in texte and jv.SIGNAL_MAITRE in texte
