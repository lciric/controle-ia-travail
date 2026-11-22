"""Essais du lot 7 — outils de quarantaine : branche orpheline par le graphe des commits seul (n° 17), journal des
lectures contre la liste (n° 18), recherche d'empreintes. Cas sain et artefact pour chaque garde (R5). Les dépôts sont
des dépôts d'essai, créés dans le dossier temporaire."""

import datetime
import os
import subprocess

import pytest

from pole import commun_na_lot7_v1 as cm
from pole import export_na_v1 as ex
from pole import quarantaine_na_v1 as qu


def _git(depot, *args):
    env = {k: v for k, v in os.environ.items() if not k.startswith("GIT_")}
    env.update(GIT_AUTHOR_NAME="essai", GIT_AUTHOR_EMAIL="essai@exemple.invalid", GIT_COMMITTER_NAME="essai",
               GIT_COMMITTER_EMAIL="essai@exemple.invalid", GIT_CONFIG_NOSYSTEM="1", HOME=depot)
    return subprocess.run(["git", "-C", depot, *args], check=True, capture_output=True, text=True, env=env).stdout.strip()


def _commit_fichier(depot, nom, texte, message):
    with open(os.path.join(depot, nom), "w", encoding="utf-8") as f:
        f.write(texte)
    _git(depot, "add", nom)
    _git(depot, "commit", "-q", "-m", message)
    return _git(depot, "rev-parse", "HEAD")


@pytest.fixture
def depot(tmp_path):
    d = str(tmp_path / "depot")
    os.makedirs(d)
    _git(d, "init", "-q", "-b", "main")
    _commit_fichier(d, "a.txt", "un\n", "m1")
    _commit_fichier(d, "b.txt", "deux\n", "m2")
    # branche orpheline : aucune histoire commune avec main
    _git(d, "checkout", "-q", "--orphan", "quarantaine")
    _git(d, "rm", "-q", "-rf", "--cached", ".")
    orph = _commit_fichier(d, "brut.txt", "réponse brute inerte\n", "q1")
    # branche tirée de main
    _git(d, "checkout", "-q", "-f", "main")
    _git(d, "checkout", "-q", "-b", "tiree")
    tiree = _commit_fichier(d, "c.txt", "trois\n", "t1")
    # une seconde orpheline, puis une branche liée à main qui la fusionne
    _git(d, "checkout", "-q", "--orphan", "quarantaine-2")
    _git(d, "rm", "-q", "-rf", "--cached", ".")
    orph2 = _commit_fichier(d, "brut2.txt", "autre réponse inerte\n", "q2")
    _git(d, "checkout", "-q", "-f", "main")
    _git(d, "checkout", "-q", "-b", "liee")
    _git(d, "merge", "-q", "--allow-unrelated-histories", "-m", "fusion", "quarantaine-2")
    _git(d, "branch", "-q", "-D", "quarantaine-2")
    _git(d, "checkout", "-q", "-f", "main")
    return d, orph, tiree, orph2


class TestBrancheOrpheline:
    def test_sain_branche_sans_ancetre_commun_admise(self, depot):
        d, orph, _, _ = depot
        c = qu.exiger_branche_orpheline(d, orph)
        assert c.orpheline and c.ancetres_avec_principale == () and c.ancetres_avec_liees == ()
        assert {x[0] for x in c.commandes} <= set(qu.SOUS_COMMANDES_GIT)

    def test_artefact_branche_tiree_de_main_refusee(self, depot):
        d, _, tiree, _ = depot
        assert qu.verifier_branche_orpheline(d, tiree).orpheline is False
        with pytest.raises(ex.ArretQuarantaineRompueNA17, match="état 2 est refusé"):
            qu.exiger_branche_orpheline(d, tiree)

    def test_artefact_orpheline_de_main_mais_fusionnee_dans_une_branche_liee(self, depot):
        d, _, _, orph2 = depot
        c = qu.verifier_branche_orpheline(d, orph2)
        assert c.ancetres_avec_principale == () and c.orpheline is False
        assert [r for r, _ in c.ancetres_avec_liees] == ["refs/heads/liee"]

    def test_aucun_objet_de_fichier_lu_objets_de_la_branche_supprimes(self, depot):
        d, orph, _, _ = depot
        arbre = _git(d, "rev-parse", orph + "^{tree}")
        blob = _git(d, "rev-parse", orph + ":brut.txt")
        for o in (arbre, blob):
            os.remove(os.path.join(d, ".git", "objects", o[:2], o[2:]))
        c = qu.exiger_branche_orpheline(d, orph)  # l'outil marche sans eux : il ne les lit pas
        assert c.orpheline

    def test_sous_commande_hors_liste_refusee_avant_d_etre_lancee(self, depot):
        d = depot[0]
        g = qu.Git(d)
        for sc in ("cat-file", "show", "ls-tree", "checkout", "archive", "log"):
            with pytest.raises(qu.CommandeGitRefusee):
                g(sc, "HEAD")
        assert g.commandes == []

    def test_sortie_de_merge_base_imprevue_refusee_jamais_lue_comme_orpheline(self, depot):
        d, orph, _, _ = depot
        vrai = qu.Git(d)

        class GitFaux:
            commandes = []

            def __call__(self, sc, *args):
                if sc == "merge-base":
                    return 128, ""
                return vrai(sc, *args)

        with pytest.raises(qu.BrancheRefusee, match="merge-base"):
            qu.verifier_branche_orpheline(d, orph, git=GitFaux())

    def test_commit_inconnu_refuse(self, depot):
        with pytest.raises(qu.BrancheRefusee):
            qu.verifier_branche_orpheline(depot[0], "0" * 40)


class Horloge:
    def __init__(self):
        self.t = datetime.datetime(2026, 11, 22, 12, 0, 0, tzinfo=datetime.timezone.utc)

    def __call__(self):
        self.t += datetime.timedelta(seconds=1)
        return self.t


E1 = "1" * 64
COMMIT = "88b55a9e"


@pytest.fixture
def liste(tmp_path):
    chemin = str(tmp_path / "liste.json")
    e = cm.ecrire_json_scelle(chemin, {"format": qu.FORMAT_LISTE, "lecteurs": ["lecteur-anteriorite-1", "juge-fin-1"]})
    return chemin, e


class TestJournalDesLectures:
    def test_sain_lecteur_inscrit_ligne_ecrite_avant_l_ouverture(self, tmp_path, liste):
        lecteurs = qu.lire_liste_nominative(*liste)
        j = qu.JournalLectures(str(tmp_path), "journal-lectures.jsonl")
        vu = []

        def ouvrir():
            lignes = cm.relire_ajout_seul(j.chemin)
            vu.append(lignes[-1]["evenement"])
            return "ouvert"

        h = Horloge()
        assert qu.ouvrir_en_quarantaine(j, lecteurs, "lecteur-anteriorite-1", COMMIT, [E1], ouvrir, h) == "ouvert"
        assert vu == ["ouverture"]
        j.sceller()
        lecture = {"role": "lecteur-anteriorite-1", "heure": h().strftime("%Y-%m-%dT%H:%M:%S.%fZ"), "commit": COMMIT,
                   "empreinte": E1}
        c = qu.exiger_lectures_conformes(j.chemin, lecteurs, [lecture])
        assert c.conformes == 1 and not c.a_porter_a_lazar

    def test_artefact_lecteur_absent_de_la_liste_refuse_et_consigne(self, tmp_path, liste):
        lecteurs = qu.lire_liste_nominative(*liste)
        j = qu.JournalLectures(str(tmp_path), "journal-lectures.jsonl")
        appels = []
        with pytest.raises(qu.ArretLectureHorsListeNA18):
            qu.ouvrir_en_quarantaine(j, lecteurs, "concepteur-sondes", COMMIT, [E1], lambda: appels.append(1), Horloge())
        assert appels == []
        assert cm.relire_ajout_seul(j.chemin)[-1]["evenement"] == "refus"

    def test_artefact_lecture_sans_ligne_constatee_et_portee(self, tmp_path, liste):
        lecteurs = qu.lire_liste_nominative(*liste)
        j = qu.JournalLectures(str(tmp_path), "journal-lectures.jsonl")
        j.sceller()
        lecture = {"role": "juge-fin-1", "heure": "2026-11-22T12:00:00.000000Z", "commit": COMMIT, "empreinte": E1}
        c = qu.controler_lectures(j.chemin, lecteurs, [lecture])
        assert c.sans_ligne == (0,) and c.a_porter_a_lazar
        with pytest.raises(qu.ArretLectureHorsListeNA18, match="sans ligne"):
            qu.exiger_lectures_conformes(j.chemin, lecteurs, [lecture])

    def test_artefact_ligne_ecrite_apres_la_lecture(self, tmp_path, liste):
        lecteurs = qu.lire_liste_nominative(*liste)
        j = qu.JournalLectures(str(tmp_path), "journal-lectures.jsonl")
        h = Horloge()
        avant = h().strftime("%Y-%m-%dT%H:%M:%S.%fZ")
        qu.ouvrir_en_quarantaine(j, lecteurs, "juge-fin-1", COMMIT, [E1], lambda: None, h)
        j.sceller()
        c = qu.controler_lectures(j.chemin, lecteurs, [{"role": "juge-fin-1", "heure": avant, "commit": COMMIT,
                                                         "empreinte": E1}])
        assert c.sans_ligne == (0,)

    def test_artefact_lecture_constatee_par_un_role_hors_liste(self, tmp_path, liste):
        lecteurs = qu.lire_liste_nominative(*liste)
        j = qu.JournalLectures(str(tmp_path), "journal-lectures.jsonl")
        j.sceller()
        c = qu.controler_lectures(j.chemin, lecteurs, [{"role": "mere", "heure": "2026-11-22T12:00:00.000000Z",
                                                         "commit": COMMIT, "empreinte": E1}])
        assert c.hors_liste == (0,) and c.a_porter_a_lazar

    def test_artefact_liste_d_une_autre_empreinte_ou_non_scellee(self, tmp_path, liste):
        with pytest.raises(qu.ArretLectureHorsListeNA18):
            qu.lire_liste_nominative(liste[0], "0" * 64)
        os.remove(liste[0] + ".sha256")
        with pytest.raises(qu.ArretLectureHorsListeNA18):
            qu.lire_liste_nominative(liste[0], liste[1])

    def test_artefact_journal_non_scelle_refuse_au_controle(self, tmp_path, liste):
        lecteurs = qu.lire_liste_nominative(*liste)
        j = qu.JournalLectures(str(tmp_path), "journal-lectures.jsonl")
        with pytest.raises(cm.AjoutSeulRefuse):
            qu.controler_lectures(j.chemin, lecteurs, [])


class TestAjoutSeul:
    def test_sain_relu(self, tmp_path):
        j = qu.JournalLectures(str(tmp_path), "j.jsonl")
        j.ajouter({"evenement": "refus", "role": "x", "heure": "h", "commit": "c", "empreintes": [], "cause": "c"})
        j.sceller()
        assert len(cm.relire_ajout_seul(j.chemin, exiger_sceau=True)) == 1

    def test_artefact_ligne_recrite_hors_forme_canonique(self, tmp_path):
        j = qu.JournalLectures(str(tmp_path), "j.jsonl")
        j.ajouter({"evenement": "refus", "role": "x", "heure": "h", "commit": "c", "empreintes": [], "cause": "c"})
        with open(j.chemin, "rb") as f:
            o = f.read()
        with open(j.chemin, "wb") as f:
            f.write(o.replace(b'": ', b'":  ', 1))
        with pytest.raises(cm.AjoutSeulRefuse, match="forme"):
            cm.relire_ajout_seul(j.chemin)


class TestRechercheEmpreintes:
    def test_sain_aucune_empreinte_de_la_branche_hors_d_elle(self, tmp_path):
        d = tmp_path / "run"
        d.mkdir()
        (d / "x.txt").write_text("rien\n", encoding="utf-8")
        qu.exiger_absence([str(d)], empreintes=[cm.sha256_octets(b"brut\n")])

    def test_artefact_copie_d_un_fichier_de_la_branche_trouvee(self, tmp_path):
        d = tmp_path / "run"
        d.mkdir()
        (d / "copie.txt").write_bytes(b"brut\n")
        with pytest.raises(ex.ArretQuarantaineRompueNA17):
            qu.exiger_absence([str(d)], empreintes=[cm.sha256_octets(b"brut\n")])

    def test_artefact_empreinte_recopiee_en_clair_trouvee(self, tmp_path):
        d = tmp_path / "run"
        d.mkdir()
        e = cm.sha256_octets(b"brut\n")
        (d / "registre.md").write_text(f"empreinte {e}\n", encoding="utf-8")
        assert qu.rechercher_empreintes([str(d)], [e])
