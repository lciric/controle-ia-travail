"""(ii-b), consigne du maître v1 : deux blocs cités dans la section « Textes », empreinte vérifiée, motifs de mention ; environnement
de la condition `maitre_iib` à la même place que P3. Cas sain (consigne factice de même forme ; forme de la consigne réelle,
brouillon 2 : nombre de blocs et de motifs, empreinte) et artefacts (un, trois blocs, bloc vide, empreinte autre, motifs absents)."""
from __future__ import annotations

from pathlib import Path

import pytest

from controle_ia.environnements.propositions import Tache
from controle_ia.gardes import GardeArret
from controle_ia.iib import consigne_v1 as cs
from controle_ia.iib import jouet_v1 as jv
from controle_ia.scellement import sceller

RACINE = Path(__file__).resolve().parents[1]
CONSIGNE_REELLE = RACINE / "brouillons" / "ii-b-saboteur-budget-v1" / "consigne-privee-maitre-ii-b-v1-brouillon2.md"
SHA_REELLE = "9f8bbdef8c0dd2d276995747d478f6d8061cc447a12af23ba7774a9d75ff90c1"


def _ecrire(tmp_path, texte, nom="consigne.md"):
    f = tmp_path / nom
    f.write_text(texte, encoding="utf-8")
    return f, sceller(f)


def test_sain_consigne_factice_deux_blocs_et_motifs(tmp_path):
    f, sha = _ecrire(tmp_path, jv.CONSIGNE_FACTICE)
    c = cs.charger_consigne_iib(f, sha)
    assert c["sha256"] == sha and jv.SIGNAL_MAITRE in c["consigne"] and c["indication"].startswith("Reminder")
    assert "\n" not in c["consigne"]                                       # lignes d'un bloc jointes par une espace
    assert c["motifs"][0] == "spread (?:this|the) extra" and len(c["motifs"]) == 5
    assert "Pièce factice" not in c["consigne"] + c["indication"]           # l'en-tête cité n'est jamais un texte de la consigne


def test_sain_forme_de_la_consigne_reelle_brouillon_2():
    """Forme seulement (consigne du développeur, § 0) : deux blocs dans « Textes », neuf motifs, empreinte ; aucun texte n'est écrit."""
    c = cs.charger_consigne_iib(CONSIGNE_REELLE, SHA_REELLE)
    assert c["sha256"] == SHA_REELLE and len(c["motifs"]) == 9 and c["consigne"] and c["indication"]


def _remplacer_textes(nouveau: str) -> str:
    t = jv.CONSIGNE_FACTICE
    debut = t.index("## Textes")
    fin = t.index("## Motifs")
    return t[:debut] + "## Textes\n\n" + nouveau + "\n\n" + t[fin:]


@pytest.mark.parametrize("cas, textes, motif", [
    ("un_bloc", "> seule consigne", "1 trouvé"),
    ("trois_blocs", "> consigne\n\n> indication\n\n> troisième", "3 trouvé"),
    ("bloc_vide", "> consigne\n\n>  \n> \n\nfin", "trouvé"),
    ("aucun_bloc", "rien de cité", "0 trouvé"),
])
def test_artefacts_nombre_de_blocs(tmp_path, cas, textes, motif):
    f, sha = _ecrire(tmp_path, _remplacer_textes(textes))
    with pytest.raises(GardeArret, match=motif):
        cs.charger_consigne_iib(f, sha)


def test_artefact_bloc_vide_explicite(tmp_path):
    f, sha = _ecrire(tmp_path, _remplacer_textes("> consigne\n\n>  "))
    with pytest.raises(GardeArret, match="dont un vide|trouvé"):
        cs.charger_consigne_iib(f, sha)


def test_artefact_empreinte_autre(tmp_path):
    f, sha = _ecrire(tmp_path, jv.CONSIGNE_FACTICE)
    with pytest.raises(GardeArret, match="R11"):
        cs.charger_consigne_iib(f, "0" * 64)


def test_artefact_fichier_modifie_apres_scellement(tmp_path):
    f, sha = _ecrire(tmp_path, jv.CONSIGNE_FACTICE)
    f.write_text(jv.CONSIGNE_FACTICE + "ajout\n", encoding="utf-8")
    with pytest.raises(GardeArret):
        cs.charger_consigne_iib(f, sha)


@pytest.mark.parametrize("texte, motif", [
    (jv.CONSIGNE_FACTICE.replace("## Motifs de mention propres à (ii-b) (factices)", "## Autre section"), "Motifs"),
    (jv.CONSIGNE_FACTICE.replace("```\nspread", "spread").replace("```\n\n## Contrôles", "\n\n## Contrôles"), "bloc de code"),
    (jv.CONSIGNE_FACTICE.replace("spread out\n", "spread (out\n"), "illisible"),
    (jv.CONSIGNE_FACTICE.replace("## Textes", "## Textes\n\n## Textes"), "2 fois"),
])
def test_artefacts_motifs_et_sections(tmp_path, texte, motif):
    f, sha = _ecrire(tmp_path, texte)
    with pytest.raises(GardeArret, match=motif):
        cs.charger_consigne_iib(f, sha)


def test_environnement_maitre_meme_place_que_p3(tmp_path):
    f, sha = _ecrire(tmp_path, jv.CONSIGNE_FACTICE)
    c = cs.charger_consigne_iib(f, sha)
    env = cs.environnement_maitre(Tache("t", "Question ?"), 10, None, c)
    systeme = env.consigne_privee(0)
    assert systeme.rstrip().endswith(c["consigne"].strip())                    # à la fin du message système
    for t in range(10):
        obs = env.observation(0, t, [])
        assert obs.endswith(c["indication"].strip() + "\nYour action:")        # juste avant « Your action: »
    assert env.indications_privees.keys() == {(0, t) for t in range(10)}
