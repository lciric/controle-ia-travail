import json, os, sys
import pytest
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import astra62_lots_v1 as A
SECRET = "REPONSESECRETE"


class Faux:
    def __init__(self, sortie=None, statut="completed", total=3):
        self.appels, self.sortie, self.statut, self.total = [], sortie, statut, total
    def __call__(self, m, chemin, cle, corps=None, ent=None):
        self.appels.append((m, chemin, corps))
        if chemin == "/v1/files":
            return 200, b'{"id":"file-in"}'
        if chemin == "/v1/batches":
            return 200, b'{"id":"batch_1","status":"validating"}'
        if chemin.startswith("/v1/batches/"):
            return 200, json.dumps({"id": "batch_1", "status": self.statut, "output_file_id": "file-out",
                                    "request_counts": {"total": self.total}}).encode()
        if chemin == "/v1/files/file-out/content":
            return 200, self.sortie
        return 404, b"{}"


def sortie(ids=("astra62-groupe-1", "astra62-groupe-2", "astra62-groupe-3"), modele="gpt-6.2-astra"):
    return "\n".join(json.dumps({"custom_id": i, "response": {"status_code": 200, "body": {
        "model": modele, "choices": [{"finish_reason": "stop", "message": {"content": SECRET}}],
        "usage": {"prompt_tokens": 3000, "completion_tokens": 20000}}}}) for i in ids).encode()


def test_lot_textes_et_reglages():
    l = A.lignes_du_lot()
    assert [x["custom_id"] for x in l] == ["astra62-groupe-1", "astra62-groupe-2", "astra62-groupe-3"]
    for x in l:
        b = x["body"]
        assert b["reasoning_effort"] == "xhigh" and b["max_completion_tokens"] == 96000 and b["model"] == "gpt-6.2-astra"
        assert [m["role"] for m in b["messages"]] == ["user"]
    assert A.pire(l) <= A.PLAFOND_LOT


def test_soumettre(tmp_path):
    t = Faux(); j = tmp_path / "j.jsonl"
    assert A.soumettre("k", str(j), t) == "batch_1"
    assert [a[1] for a in t.appels] == ["/v1/files", "/v1/batches"]
    assert b'name="purpose"\r\n\r\nbatch' in t.appels[0][2]
    assert json.loads(t.appels[1][2])["completion_window"] == "24h"


def test_releve_saine_sans_texte(tmp_path):
    t = Faux(sortie()); j = tmp_path / "j.jsonl"; q = tmp_path / "q"
    assert A.relever("k", "batch_1", str(j), str(q), t) == "completed"
    txt = j.read_text()
    assert SECRET not in txt and (q / "astra62-lot-output_file_id.jsonl.sha256").exists()
    r = [json.loads(x) for x in txt.split("\n") if x]
    assert sum(1 for x in r if x["type_ligne"] == "réponse") == 3 and r[-1]["cout_total_usd"] == "1.245000"


@pytest.mark.parametrize("s,total", [(sortie(ids=("astra62-groupe-1", "astra62-groupe-1", "astra62-groupe-3")), 3),
                                     (sortie(), 4), (sortie(ids=("astra62-groupe-1", "astra62-groupe-2", "autre")), 3)])
def test_releve_incoherente_refusee(tmp_path, s, total):
    with pytest.raises(A.Refus):
        A.relever("k", "batch_1", str(tmp_path / "j.jsonl"), str(tmp_path / "q"), Faux(s, total=total))
    assert not (tmp_path / "j.jsonl").exists() or "réponse" not in (tmp_path / "j.jsonl").read_text()


def test_releve_en_cours(tmp_path):
    assert A.relever("k", "b", str(tmp_path / "j.jsonl"), str(tmp_path / "q"), Faux(statut="in_progress")) == "in_progress"
    assert not (tmp_path / "q").exists()


def test_modele_autre_en_liste_fermee(tmp_path):
    A.relever("k", "b", str(tmp_path / "j.jsonl"), str(tmp_path / "q"), Faux(sortie(modele=SECRET)))
    assert SECRET not in (tmp_path / "j.jsonl").read_text()


def test_go_absent(tmp_path):
    r = tmp_path / "go.md"; r.write_text("| GO-2026-11-22-45 | x |\n")
    with pytest.raises(A.Refus):
        A.verifier_go(str(r))


def test_texte_altere(tmp_path):
    import shutil
    d = tmp_path / "t"; shutil.copytree(A.TEXTES, d)
    (d / "groupe-2.md").write_bytes((d / "groupe-2.md").read_bytes() + b"x")
    with pytest.raises(A.Refus):
        A.lignes_du_lot(str(d))
