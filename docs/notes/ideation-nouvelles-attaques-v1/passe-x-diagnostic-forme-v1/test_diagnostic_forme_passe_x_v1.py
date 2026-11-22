import json, os, sys, hashlib
import pytest
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import diagnostic_forme_passe_x_v1 as G

SECRET = "PHRASESECRETEDEREPONSE"


def flux_google(texte):
    evs = [{"modelVersion": "gemini-4-argon", "candidates": [{"content": {"parts": [{"text": texte}]}, "finishReason": "STOP"}],
            "usageMetadata": {"promptTokenCount": 1, "candidatesTokenCount": 1, "thoughtsTokenCount": 1}}]
    return b"".join(b"data: " + json.dumps(e).encode() + b"\n\n" for e in evs)


def monter(tmp_path, textes):
    q = tmp_path / "q"; q.mkdir(); j = tmp_path / "j.jsonl"; lignes = []
    for i, (texte_servi, texte, cause) in enumerate(textes):
        b = flux_google(texte); (q / f"f{i}.flux").write_bytes(b)
        lignes.append({"type_ligne": "tentative", "classe": "réponse rendue", "proposeur": "espece_1",
                       "texte_servi": texte_servi, "fournisseur": "google", "flux_sha256": hashlib.sha256(b).hexdigest()})
        lignes.append({"type_ligne": "garde de coupure", "proposeur": "espece_1", "texte_servi": texte_servi, "cause": cause})
    j.write_text("".join(json.dumps(l) + "\n" for l in lignes))
    return str(j), str(q)


def test_aucun_texte_ne_sort(tmp_path, capsys):
    t = f"**Answer 1** {SECRET}\n\nsome text {SECRET}\n\n**Answer 2**\n{SECRET}\n\nEND OF ANSWERS"
    j, q = monter(tmp_path, [("groupe-1", t, "texte coupé")])
    G.main(["--journal", j, "--quarantaine", q, "--sortie", str(tmp_path / "s.json")])
    s = (tmp_path / "s.json").read_text()
    assert SECRET not in s and SECRET not in capsys.readouterr().out
    c = json.loads(s)["flux"][0]["comptes"]
    assert c["titre_answer_k"] == 2 and c["titre_gras_seul"] == 1 and c["derniere_ligne"]["ligne_finale_anglaise"]
    assert c["langue_des_titres"]["en"] == 2


def test_compte_les_formes(tmp_path):
    t = "## Réponse 1\nx\n## 2. Pièce 2\ny\n### Réponse 3\nz\nFIN DES RÉPONSES."
    j, q = monter(tmp_path, [("groupe-1", t, "texte coupé")])
    G.main(["--journal", j, "--quarantaine", q, "--sortie", str(tmp_path / "s.json")])
    c = json.load(open(tmp_path / "s.json"))["flux"][0]["comptes"]
    assert c["titre_reponse_k"] == 1 and c["titre_reponse_k_autre_espace"] == 2 and c["titre_markdown"] == 3
    assert c["derniere_ligne"]["ligne_finale_ponctuee"] and not c["derniere_ligne"]["ligne_finale_exacte"]
    assert c["numeros_de_pieces_cites_en_titre"] == [1, 2, 3]


def test_ne_lit_que_les_defauts(tmp_path):
    j, q = monter(tmp_path, [("groupe-1", "a", "texte coupé"), ("groupe-2", "b", None)])
    G.main(["--journal", j, "--quarantaine", q, "--sortie", str(tmp_path / "s.json")])
    assert [f["texte_servi"] for f in json.load(open(tmp_path / "s.json"))["flux"]] == ["groupe-1"]


def test_sortie_jamais_ecrasee(tmp_path):
    j, q = monter(tmp_path, [("groupe-1", "a", "texte coupé")])
    (tmp_path / "s.json").write_text("x")
    with pytest.raises(SystemExit):
        G.main(["--journal", j, "--quarantaine", q, "--sortie", str(tmp_path / "s.json")])
    assert (tmp_path / "s.json").read_text() == "x"


def test_flux_introuvable_refuse(tmp_path):
    j, q = monter(tmp_path, [("groupe-1", "a", "texte coupé")])
    os.remove(os.path.join(q, "f0.flux"))
    with pytest.raises(SystemExit):
        G.main(["--journal", j, "--quarantaine", q, "--sortie", str(tmp_path / "s.json")])
