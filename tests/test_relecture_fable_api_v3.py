"""Essais de controle_ia.relecture_fable_api_v3 (v3, 21 novembre 2026), sans réseau : fausses fonctions d'envoi et de
comptage injectées, et un faux serveur local (boucle 127.0.0.1) pour le chemin réel du kit d'Anthropic. Chaque garde est
essayée sur un cas sain et sur un artefact (R5)."""
import hashlib
import http.server
import json
import os
import threading

import pytest

from controle_ia import relecture_fable_api_v3 as rf

SECRET = "sk-ant-essai-SECRET-0123456789"
ENV = {"CLE_ESSAI": SECRET}


def ecrire(chemin, texte, compagnon=True, empreinte=None):
    with open(chemin, "w", encoding="utf-8") as f:
        f.write(texte)
    if compagnon:
        h = empreinte or hashlib.sha256(texte.encode("utf-8")).hexdigest()
        with open(chemin + ".sha256", "w", encoding="utf-8") as f:
            f.write(f"{h}  {os.path.basename(chemin)}\n")


@pytest.fixture
def dossier(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    ecrire("consigne.md", "Relis la correction contre les remarques. Dis ce qui manque.\n")
    ecrire("piece.md", "Texte corrigé, ligne un.\nLigne deux.\n")
    ecrire("remarques.md", "Remarque 1 : préciser la ligne deux.\n")
    ecrire("avant.md", "Texte d'avant.\n")
    os.mkdir("journal")
    return tmp_path


def arguments(*extra, piece="piece.md", consigne="consigne.md", plafond="10", journal="journal/depense.jsonl"):
    base = ["relire", "--piece", piece, "--remarques", "remarques.md", "--avant", "avant.md",
            "--consigne", consigne, "--sortie", "sortie", "--cle", "CLE_ESSAI",
            "--plafond-ligne", plafond, "--journal-depense", journal]
    return rf.analyseur().parse_args(base + list(extra))


class FauxEnvoi:
    def __init__(self, resultat=None, exception=None):
        self.appels = []
        self.resultat = resultat
        self.exception = exception

    def __call__(self, params):
        self.appels.append(params)
        if self.exception:
            raise self.exception
        return self.resultat


def sain(texte="Rien à redire.", fin="end_turn", modele=rf.MODELE, usage=None, **kw):
    return rf.Resultat(envoye=True, texte=texte, raison_arret=fin, modele_servi=modele, identifiant="msg_essai",
                       usage=usage if usage is not None else {"entree": 100, "sortie": 500, "reflexion": 300,
                                                              "ecriture_cache": 0, "lecture_cache": 0}, **kw)


def compteur_fixe(n=100):
    appels = []

    def compter(params):
        appels.append(params)
        return n
    compter.appels = appels
    return compter


def lignes_journal(chemin="journal/depense.jsonl"):
    if not os.path.exists(chemin):
        return []
    with open(chemin, encoding="utf-8") as f:
        return [json.loads(l) for l in f if l.strip()]


def tout_le_texte_ecrit(racine):
    morceaux = []
    for d, _, fichiers in os.walk(racine):
        for nom in fichiers:
            with open(os.path.join(d, nom), "rb") as f:
                morceaux.append(f.read().decode("utf-8", "replace"))
    return "\n".join(morceaux)


# ---------- cas sain ----------

def test_cas_sain(dossier, capsys):
    envoi, compter = FauxEnvoi(sain()), compteur_fixe(100)
    code = rf.relire(arguments(), envoyeur=envoi, compteur=compter, environ=ENV)
    assert code == rf.OK
    assert len(envoi.appels) == 1
    p = envoi.appels[0]
    assert p["model"] == "claude-fable-5-2"
    assert p["output_config"] == {"effort": "high"}  # v3 : défaut « high »
    assert p["thinking"] == {"type": "adaptive", "display": "omitted"}
    assert p["max_tokens"] == 128000
    assert "fallbacks" not in p and "workspace_id" not in p
    invite = p["messages"][0]["content"]
    assert invite.startswith("Relis la correction")
    h_piece = hashlib.sha256(open("piece.md", "rb").read()).hexdigest()
    assert f'<piece role="correction" chemin="piece.md" sha256="{h_piece}">' in invite
    assert invite.index('role="correction"') < invite.index('role="remarques"') < invite.index('role="avant"')
    # sortie et compagnon
    rel = open("sortie/relecture-fable-api.md", encoding="utf-8").read()
    assert rel.endswith("Rien à redire.\n") and "claude-fable-5-2" in rel and h_piece in rel
    h = hashlib.sha256(rel.encode("utf-8")).hexdigest()
    assert open("sortie/relecture-fable-api.md.sha256").read() == f"{h}  relecture-fable-api.md\n"
    compteurs = json.load(open("sortie/compteurs.json"))
    assert compteurs["statut"] == "reponse" and compteurs["jetons"]["reflexion"] == 300
    assert os.path.exists("sortie/compteurs.json.sha256")
    # journal
    (l,) = lignes_journal()
    assert l["statut"] == "reponse" and l["envoye"] is True and l["raison_arret"] == "end_turn"
    assert l["cout_compte_usd"] == pytest.approx((100 * 8 + 500 * 40) / 1e6)
    assert l["jetons"] == {"entree": 100, "sortie": 500, "reflexion": 300, "ecriture_cache": 0, "lecture_cache": 0}
    assert l["entree_comptee"] == 100 and l["entree_garde"] == 133  # ⌈100 × 1,01⌉ + 32
    assert l["sha256_relecture"] == h
    assert {e["role"] for e in l["entrees"]} == {"consigne", "correction", "remarques", "avant"}
    assert all(len(e["sha256"]) == 64 and e["compagnon"] == "vérifié" for e in l["entrees"])
    assert l["heure_utc"].endswith("Z")
    assert SECRET not in tout_le_texte_ecrit(dossier)
    sortie = capsys.readouterr()
    assert SECRET not in sortie.out + sortie.err


# ---------- garde de motifs ----------

ARTEFACTS = [
    "Lu par Lazar hier.", "lu par LAZAR", "M. Ciric a dit", "M. Ćirić a dit",
    "voir session_01Qi7Gr3eYmAhDEJzqLgWcv1", "écrire à quelqu.un@exemple.fr",
    "lire consigne-privee-v1.md", "la consigne privée", "consigne_privee", "la conception-ii-b",
    "voir docs/verite_dommage/x.md", "la vérité-cachée.md", "fichier rendu-v1.md", "le `rendu`",
    "le fichier scores.json", "dossier `scores`", "lire donnees/brut.csv", "lire données/brut.csv",
    "voir SESSION_01Qi7Gr3eYmAhDEJzqLgWcv1", "voir session-01Qi7Gr3eYmAhDEJzqLgWcv1",
    "dossier 2eb82089-3810-5ff8-881f-da5f24b622eb", "lu par La\u200bzar", "lire conception-ii-b1-v1.md",
]
SAINS = [
    "le rendu est bon", "les scores montent", "la vérité du dommage", "session_court", "écrire à a@b",
    "Lazarus n'est pas là", "rendu.", "compte des scores, puis rendu final",
]


@pytest.mark.parametrize("ligne", ARTEFACTS)
def test_garde_refuse_chaque_motif(dossier, ligne):
    ecrire("piece.md", f"Texte corrigé.\n{ligne}\n")
    envoi = FauxEnvoi(sain())
    code = rf.relire(arguments(), envoyeur=envoi, compteur=compteur_fixe(), environ=ENV)
    assert code == rf.CODE_GARDE
    assert envoi.appels == []
    assert not os.path.exists("sortie")
    (l,) = lignes_journal()
    assert l["statut"] == "refus_avant_envoi" and l["envoye"] is False and l["cout_compte_usd"] == 0
    assert l["details"]["motifs"] and l["details"]["motifs"][0]["ligne"] == 2
    assert ligne not in json.dumps(l, ensure_ascii=False)  # le texte trouvé n'est jamais recopié


@pytest.mark.parametrize("ligne", [l for l in SAINS if "Lazarus" not in l])
def test_garde_laisse_passer_le_sain(dossier, ligne):
    ecrire("piece.md", f"Texte corrigé.\n{ligne}\n")
    envoi = FauxEnvoi(sain())
    assert rf.relire(arguments(), envoyeur=envoi, compteur=compteur_fixe(), environ=ENV) == rf.OK
    assert len(envoi.appels) == 1


def test_garde_nom_compris_dans_un_mot_est_refuse(dossier):
    # Prudence déclarée : « lazar » est cherché comme sous-chaîne ; « Lazarus » est refusé (faux positif accepté).
    ecrire("piece.md", "Lazarus n'est pas là\n")
    assert rf.relire(arguments(), envoyeur=FauxEnvoi(sain()), compteur=compteur_fixe(), environ=ENV) == rf.CODE_GARDE


def test_garde_porte_sur_le_chemin_de_la_piece(dossier):
    ecrire("rendu-v1.md", "Texte sans motif.\n")
    envoi = FauxEnvoi(sain())
    assert rf.relire(arguments(piece="rendu-v1.md"), envoyeur=envoi, compteur=compteur_fixe(),
                     environ=ENV) == rf.CODE_GARDE
    assert envoi.appels == []
    ecrire("piece-v1.md", "Texte sans motif.\n")
    assert rf.relire(arguments(piece="piece-v1.md"), envoyeur=envoi, compteur=compteur_fixe(), environ=ENV) == rf.OK


def test_garde_porte_sur_la_consigne(dossier):
    ecrire("consigne2.md", "Ne cite pas Lazar.\n")
    envoi = FauxEnvoi(sain())
    assert rf.relire(arguments(consigne="consigne2.md"), envoyeur=envoi, compteur=compteur_fixe(),
                     environ=ENV) == rf.CODE_GARDE
    assert envoi.appels == []


def test_garde_unitaire_rend_noms_de_motifs():
    assert rf.garde_motifs_ligne("rien ici") == []
    assert rf.garde_motifs_ligne("voir session_" + "a" * 20) == ["identifiant de session"]
    assert rf.garde_motifs_ligne("voir session_" + "a" * 19) == []


# ---------- empreintes et pièces ----------

def test_empreinte_inegale_refusee(dossier):
    ecrire("piece.md", "Texte corrigé.\n", empreinte="0" * 64)
    envoi = FauxEnvoi(sain())
    assert rf.relire(arguments(), envoyeur=envoi, compteur=compteur_fixe(), environ=ENV) == rf.CODE_PIECE
    assert envoi.appels == []
    (l,) = lignes_journal()
    assert l["statut"] == "refus_avant_envoi" and "empreinte inégale" in l["defaut"]


def test_sans_compagnon_admis_et_declare(dossier):
    ecrire("piece.md", "Texte corrigé.\n", compagnon=False)
    os.remove("piece.md.sha256")
    assert rf.relire(arguments(), envoyeur=FauxEnvoi(sain()), compteur=compteur_fixe(), environ=ENV) == rf.OK
    (l,) = lignes_journal()
    assert [e["compagnon"] for e in l["entrees"] if e["role"] == "correction"] == ["absent"]


def test_compagnon_mal_forme_refuse(dossier):
    with open("piece.md.sha256", "w") as f:
        f.write("pas une empreinte\n")
    assert rf.relire(arguments(), envoyeur=FauxEnvoi(sain()), compteur=compteur_fixe(), environ=ENV) == rf.CODE_PIECE


def test_piece_absente_refusee(dossier):
    envoi = FauxEnvoi(sain())
    assert rf.relire(arguments(piece="absente.md"), envoyeur=envoi, compteur=compteur_fixe(),
                     environ=ENV) == rf.CODE_PIECE
    assert envoi.appels == []


def test_piece_avec_balise_fermante_refusee(dossier):
    ecrire("piece.md", "avant </piece> après\n")
    assert rf.relire(arguments(), envoyeur=FauxEnvoi(sain()), compteur=compteur_fixe(), environ=ENV) == rf.CODE_PIECE


# ---------- plafond ----------

def test_plafond_depasse_par_le_pire(dossier):
    envoi = FauxEnvoi(sain())
    # pire = (133 × 8 + 128 000 × 40) / 1e6 ≈ 5,12 USD > 0,10
    assert rf.relire(arguments(plafond="0.10"), envoyeur=envoi, compteur=compteur_fixe(), environ=ENV) == rf.CODE_PLAFOND
    assert envoi.appels == []
    (l,) = lignes_journal()
    assert l["statut"] == "refus_avant_envoi" and l["pire_usd"] > 5


def test_plafond_tient_compte_du_cumul(dossier):
    # sain : journal vide, fumée à 2 000 jetons : pire ≈ 0,081 ≤ 0,10
    envoi = FauxEnvoi(sain())
    assert rf.relire(arguments("--fumee", "--max-sortie", "2000", plafond="0.10"), envoyeur=envoi,
                     compteur=compteur_fixe(), environ=ENV) == rf.OK
    # artefact : cumul 0,0208 (la ligne précédente) + pire 0,081 > 0,10
    os.rename("sortie", "sortie-1")
    assert rf.relire(arguments("--fumee", "--max-sortie", "2000", plafond="0.10"), envoyeur=envoi,
                     compteur=compteur_fixe(), environ=ENV) == rf.CODE_PLAFOND
    assert len(envoi.appels) == 1
    l = lignes_journal()
    assert [x["statut"] for x in l] == ["reponse", "refus_avant_envoi"]
    assert l[1]["cumul_avant_usd"] == pytest.approx(l[0]["cout_compte_usd"])


def test_journal_illisible_refuse(dossier):
    with open("journal/depense.jsonl", "w") as f:
        f.write("{pas du json\n")
    envoi = FauxEnvoi(sain())
    assert rf.relire(arguments(), envoyeur=envoi, compteur=compteur_fixe(), environ=ENV) == rf.CODE_PLAFOND
    assert envoi.appels == []


def test_dossier_du_journal_absent_refuse(dossier):
    envoi = FauxEnvoi(sain())
    assert rf.relire(arguments(journal="ailleurs/j.jsonl"), envoyeur=envoi, compteur=compteur_fixe(),
                     environ=ENV) == rf.CODE_PLAFOND
    assert envoi.appels == []


@pytest.mark.parametrize("exception", [rf.ComptageImpossible("essai"), RuntimeError(f"boum {SECRET}")])
def test_comptage_impossible_refuse_sans_envoi(dossier, exception):
    def compter(params):
        raise exception
    envoi = FauxEnvoi(sain())
    assert rf.relire(arguments(), envoyeur=envoi, compteur=compter, environ=ENV) == rf.CODE_COMPTAGE
    assert envoi.appels == [] and not os.path.exists("sortie")
    (l,) = lignes_journal()
    assert l["statut"] == "refus_avant_envoi" and l["cout_compte_usd"] == 0 and "comptage" in l["defaut"]
    assert SECRET not in json.dumps(l)


def test_cle_refusee_au_comptage_arrete_avant_envoi(dossier):
    def compter(params):
        raise rf.CleRefusee("HTTP 401")
    envoi = FauxEnvoi(sain())
    assert rf.relire(arguments(), envoyeur=envoi, compteur=compter, environ=ENV) == rf.CODE_ENVOI
    assert envoi.appels == []


# ---------- défauts de réponse ----------

def test_reponse_vide_est_un_defaut(dossier):
    envoi = FauxEnvoi(sain(texte="  \n"))
    assert rf.relire(arguments(), envoyeur=envoi, compteur=compteur_fixe(), environ=ENV) == rf.CODE_DEFAUT
    assert not os.path.exists("sortie/relecture-fable-api.md")
    (l,) = lignes_journal()
    assert l["statut"] == "defaut" and l["defaut"] == "texte vide" and l["cout_compte_usd"] > 0
    assert json.load(open("sortie/compteurs.json"))["statut"] == "defaut"


def test_arret_en_max_tokens_est_un_defaut(dossier):
    envoi = FauxEnvoi(sain(texte="Début coupé", fin="max_tokens"))
    assert rf.relire(arguments(), envoyeur=envoi, compteur=compteur_fixe(), environ=ENV) == rf.CODE_DEFAUT
    assert not os.path.exists("sortie/relecture-fable-api.md")
    partiel = open(f"sortie/{rf.NOM_PARTIEL}", encoding="utf-8").read()
    assert "PAS une relecture" in partiel and "Début coupé" in partiel
    (l,) = lignes_journal()
    assert l["defaut"] == "arrêt en max_tokens" and l["raison_arret"] == "max_tokens"


def test_refus_du_modele_est_un_defaut(dossier):
    envoi = FauxEnvoi(sain(texte="", fin="refusal", categorie_refus="reasoning_extraction"))
    assert rf.relire(arguments(), envoyeur=envoi, compteur=compteur_fixe(), environ=ENV) == rf.CODE_DEFAUT
    (l,) = lignes_journal()
    assert "refus du modèle" in l["defaut"] and l["categorie_refus"] == "reasoning_extraction"


@pytest.mark.parametrize("fin", ["stop_sequence", "pause_turn", "tool_use", None])
def test_autre_raison_arret_est_un_defaut(dossier, fin):
    envoi = FauxEnvoi(sain(fin=fin))
    assert rf.relire(arguments(), envoyeur=envoi, compteur=compteur_fixe(), environ=ENV) == rf.CODE_DEFAUT
    assert not os.path.exists("sortie/relecture-fable-api.md")
    (l,) = lignes_journal()
    assert l["statut"] == "defaut" and "raison d'arrêt inattendue" in l["defaut"]


def test_journal_ecrit_avant_toute_sortie(dossier, monkeypatch):
    vus, vrai = [], rf.ecrire_neuf

    def espion(chemin, texte):
        vus.append((os.path.basename(chemin), len(lignes_journal())))
        return vrai(chemin, texte)
    monkeypatch.setattr(rf, "ecrire_neuf", espion)
    assert rf.relire(arguments(), envoyeur=FauxEnvoi(sain()), compteur=compteur_fixe(), environ=ENV) == rf.OK
    assert len(vus) == 2 and all(n == 1 for _, n in vus)
    vus.clear()
    os.rename("sortie", "sortie-1")
    assert rf.relire(arguments(), envoyeur=FauxEnvoi(sain(texte="coupé", fin="max_tokens")),
                     compteur=compteur_fixe(), environ=ENV) == rf.CODE_DEFAUT
    assert len(vus) == 2 and all(n == 2 for _, n in vus)


def test_interruption_pendant_envoi_comptee_au_pire(dossier):
    with pytest.raises(KeyboardInterrupt):
        rf.relire(arguments(), envoyeur=FauxEnvoi(exception=KeyboardInterrupt()), compteur=compteur_fixe(),
                  environ=ENV)
    (l,) = lignes_journal()
    assert l["statut"] == "defaut" and l["base_cout"] == "pire" and l["cout_compte_usd"] == l["pire_usd"]
    assert not os.path.exists("sortie/relecture-fable-api.md")


def test_sigterm_pendant_envoi_compte_au_pire(dossier):
    import signal
    import time
    avant = signal.getsignal(signal.SIGTERM)

    def envoyer(params):
        os.kill(os.getpid(), signal.SIGTERM)
        time.sleep(5)
        return sain()
    with pytest.raises(KeyboardInterrupt):
        rf.relire(arguments(), envoyeur=envoyer, compteur=compteur_fixe(), environ=ENV)
    (l,) = lignes_journal()
    assert l["base_cout"] == "pire" and l["cout_compte_usd"] == l["pire_usd"]
    assert signal.getsignal(signal.SIGTERM) is avant


def test_modele_servi_autre_est_un_defaut(dossier):
    envoi = FauxEnvoi(sain(modele="claude-opus-4-8"))
    assert rf.relire(arguments(), envoyeur=envoi, compteur=compteur_fixe(), environ=ENV) == rf.CODE_DEFAUT
    assert not os.path.exists("sortie/relecture-fable-api.md")


def test_erreur_apres_envoi_comptee_au_pire(dossier):
    res = rf.Resultat(envoye=True, erreur=f"coupure, clé {SECRET}", base_cout="pire")
    assert rf.relire(arguments(), envoyeur=FauxEnvoi(res), compteur=compteur_fixe(), environ=ENV) == rf.CODE_ENVOI
    (l,) = lignes_journal()
    assert l["statut"] == "defaut" and l["base_cout"] == "pire" and l["cout_compte_usd"] == l["pire_usd"]
    assert SECRET not in json.dumps(l)


def test_exception_imprevue_comptee_au_pire(dossier):
    envoi = FauxEnvoi(exception=RuntimeError("boum"))
    assert rf.relire(arguments(), envoyeur=envoi, compteur=compteur_fixe(), environ=ENV) == rf.CODE_ENVOI
    (l,) = lignes_journal()
    assert l["base_cout"] == "pire" and l["cout_compte_usd"] == l["pire_usd"]


def test_usage_absent_compte_au_pire(dossier):
    res = sain()
    res.usage = None
    assert rf.relire(arguments(), envoyeur=FauxEnvoi(res), compteur=compteur_fixe(), environ=ENV) == rf.CODE_DEFAUT
    (l,) = lignes_journal()
    assert l["base_cout"] == "pire" and l["cout_compte_usd"] == l["pire_usd"]


# ---------- clé, espace, sortie, fumée ----------

def test_cle_absente_refusee(dossier):
    envoi = FauxEnvoi(sain())
    assert rf.relire(arguments(), envoyeur=envoi, compteur=compteur_fixe(), environ={}) == rf.CODE_CLE
    assert envoi.appels == []
    (l,) = lignes_journal()
    assert l["statut"] == "refus_avant_envoi" and "CLE_ESSAI" in l["defaut"]


def test_nom_de_variable_mal_forme_refuse(dossier):
    args = arguments()
    args.cle = "sk-ant-pas-un-nom"
    assert rf.relire(args, envoyeur=FauxEnvoi(sain()), compteur=compteur_fixe(), environ=ENV) == rf.CODE_USAGE


def test_espace_envoye_seulement_si_demande(dossier):
    envoi = FauxEnvoi(sain())
    env = dict(ENV, ESPACE_ESSAI="wrkspc_essai")
    assert rf.relire(arguments("--espace", "ESPACE_ESSAI"), envoyeur=envoi, compteur=compteur_fixe(),
                     environ=env) == rf.OK
    assert envoi.appels[0]["workspace_id"] == "wrkspc_essai"
    os.rename("sortie", "sortie-1")
    assert rf.relire(arguments("--espace", "ESPACE_ABSENT"), envoyeur=envoi, compteur=compteur_fixe(),
                     environ=env) == rf.CODE_CLE


def test_sortie_existante_jamais_ecrasee(dossier):
    os.mkdir("sortie")
    ecrire("sortie/relecture-fable-api.md", "ancienne\n", compagnon=False)
    envoi = FauxEnvoi(sain())
    assert rf.relire(arguments(), envoyeur=envoi, compteur=compteur_fixe(), environ=ENV) == rf.CODE_EXISTE
    assert envoi.appels == [] and open("sortie/relecture-fable-api.md").read() == "ancienne\n"


@pytest.mark.parametrize("nom", ["relecture-fable-api.md.sha256", "compteurs.json.sha256"])
def test_compagnon_orphelin_jamais_ecrase(dossier, nom):
    os.mkdir("sortie")
    with open(f"sortie/{nom}", "w") as f:
        f.write("ancien\n")
    envoi = FauxEnvoi(sain())
    assert rf.relire(arguments(), envoyeur=envoi, compteur=compteur_fixe(), environ=ENV) == rf.CODE_EXISTE
    assert envoi.appels == [] and open(f"sortie/{nom}").read() == "ancien\n"


def test_max_sortie_basse_refusee_hors_fumee(dossier):
    envoi = FauxEnvoi(sain())
    assert rf.relire(arguments("--max-sortie", "2000"), envoyeur=envoi, compteur=compteur_fixe(),
                     environ=ENV) == rf.CODE_USAGE
    assert rf.relire(arguments("--max-sortie", "64000"), envoyeur=envoi, compteur=compteur_fixe(),
                     environ=ENV) == rf.OK
    assert envoi.appels[0]["max_tokens"] == 64000


def test_fumee_marquee(dossier):
    envoi = FauxEnvoi(sain(texte="OK"))
    assert rf.relire(arguments("--fumee", "--max-sortie", "2000"), envoyeur=envoi, compteur=compteur_fixe(),
                     environ=ENV) == rf.OK
    assert "pas une relecture" in open("sortie/relecture-fable-api.md", encoding="utf-8").read()
    assert lignes_journal()[0]["fumee"] is True


# ---------- chemin réel du kit d'Anthropic, contre un faux serveur local ----------

def sse(evenements):
    return "".join(f"event: {e['type']}\ndata: {json.dumps(e)}\n\n" for e in evenements).encode("utf-8")


FLUX_SAIN = [
    {"type": "message_start", "message": {"id": "msg_local", "type": "message", "role": "assistant",
                                          "model": "claude-fable-5-2", "content": [], "stop_reason": None,
                                          "stop_sequence": None, "usage": {"input_tokens": 57, "output_tokens": 1}}},
    {"type": "content_block_start", "index": 0, "content_block": {"type": "thinking", "thinking": "", "signature": ""}},
    {"type": "content_block_delta", "index": 0, "delta": {"type": "signature_delta", "signature": "sig"}},
    {"type": "content_block_stop", "index": 0},
    {"type": "content_block_start", "index": 1, "content_block": {"type": "text", "text": ""}},
    {"type": "content_block_delta", "index": 1, "delta": {"type": "text_delta", "text": "O"}},
    {"type": "content_block_delta", "index": 1, "delta": {"type": "text_delta", "text": "K"}},
    {"type": "content_block_stop", "index": 1},
    {"type": "message_delta", "delta": {"stop_reason": "end_turn", "stop_sequence": None},
     "usage": {"input_tokens": 57, "output_tokens": 40, "output_tokens_details": {"thinking_tokens": 37}}},
    {"type": "message_stop"},
]


@pytest.fixture
def serveur():
    etat = {"requetes": [], "compte": (200, {"input_tokens": 57}), "messages": (200, FLUX_SAIN)}

    class Gestionnaire(http.server.BaseHTTPRequestHandler):
        def log_message(self, *a):
            pass

        def do_POST(self):
            corps = self.rfile.read(int(self.headers.get("Content-Length", 0)))
            etat["requetes"].append({"chemin": self.path, "entetes": dict(self.headers), "corps": json.loads(corps)})
            if self.path.startswith("/v1/messages/count_tokens"):
                code, charge = etat["compte"]
                donnees, type_ = json.dumps(charge).encode(), "application/json"
            else:
                code, charge = etat["messages"]
                if code == 200:
                    donnees, type_ = sse(charge), "text/event-stream"
                else:
                    donnees, type_ = json.dumps(charge).encode(), "application/json"
            self.send_response(code)
            self.send_header("Content-Type", type_)
            self.send_header("Content-Length", str(len(donnees)))
            self.end_headers()
            self.wfile.write(donnees)

    srv = http.server.ThreadingHTTPServer(("127.0.0.1", 0), Gestionnaire)
    fil = threading.Thread(target=srv.serve_forever, daemon=True)
    fil.start()
    etat["url"] = f"http://127.0.0.1:{srv.server_address[1]}"
    yield etat
    srv.shutdown()
    srv.server_close()


def test_chemin_reel_sain_contre_serveur_local(dossier, serveur):
    code = rf.relire(arguments("--fumee", "--max-sortie", "2000"), environ=ENV, base_url=serveur["url"])
    assert code == rf.OK
    chemins = [r["chemin"] for r in serveur["requetes"]]
    assert chemins[0].startswith("/v1/messages/count_tokens") and chemins[1].startswith("/v1/messages")
    assert len(chemins) == 2
    corps = serveur["requetes"][1]["corps"]
    assert corps["model"] == "claude-fable-5-2" and corps["stream"] is True and corps["max_tokens"] == 2000
    assert corps["output_config"] == {"effort": "high"} and corps["thinking"]["type"] == "adaptive"
    assert "fallbacks" not in corps
    entetes = {k.lower(): v for k, v in serveur["requetes"][1]["entetes"].items()}
    # kit d'Anthropic 2.x (version d'interface 2026-10-21) : la clé part en « Authorization: Bearer »
    assert entetes["authorization"] == f"Bearer {SECRET}" and "anthropic-workspace-id" not in entetes
    assert entetes["x-stainless-retry-count"] == "0"
    (l,) = lignes_journal()
    assert l["jetons"]["entree"] == 57 and l["jetons"]["sortie"] == 40 and l["jetons"]["reflexion"] == 37
    assert l["raison_arret"] == "end_turn" and l["modele_servi"] == "claude-fable-5-2"
    assert l["cout_compte_usd"] == pytest.approx((57 * 8 + 40 * 40) / 1e6)
    assert open("sortie/relecture-fable-api.md", encoding="utf-8").read().endswith("\nOK\n")


def test_chemin_reel_cle_refusee_sans_relance(dossier, serveur):
    serveur["compte"] = (401, {"type": "error", "error": {"type": "authentication_error", "message": "invalid x-api-key"}})
    code = rf.relire(arguments("--fumee", "--max-sortie", "2000"), environ=ENV, base_url=serveur["url"])
    assert code == rf.CODE_ENVOI
    assert len(serveur["requetes"]) == 1  # aucune relance, aucun envoi
    (l,) = lignes_journal()
    assert l["statut"] == "refus_avant_envoi" and "clé refusée" in l["defaut"]


def test_chemin_reel_erreur_serveur_sans_relance_comptee_au_pire(dossier, serveur):
    serveur["messages"] = (500, {"type": "error", "error": {"type": "api_error", "message": "boum"}})
    code = rf.relire(arguments("--fumee", "--max-sortie", "2000"), environ=ENV, base_url=serveur["url"])
    assert code == rf.CODE_ENVOI
    assert [r["chemin"].split("?")[0] for r in serveur["requetes"]] == ["/v1/messages/count_tokens", "/v1/messages"]
    (l,) = lignes_journal()
    assert l["base_cout"] == "pire" and l["cout_compte_usd"] == l["pire_usd"]


def test_chemin_reel_comptage_500_refuse_sans_envoi(dossier, serveur):
    serveur["compte"] = (500, {"type": "error", "error": {"type": "api_error", "message": "boum"}})
    code = rf.relire(arguments("--fumee", "--max-sortie", "2000"), environ=ENV, base_url=serveur["url"])
    assert code == rf.CODE_COMPTAGE
    assert len(serveur["requetes"]) == 1  # le comptage seul, aucune relance, aucun envoi
    (l,) = lignes_journal()
    assert l["statut"] == "refus_avant_envoi" and l["cout_compte_usd"] == 0


def test_chemin_reel_refus_400_compte_zero(dossier, serveur):
    serveur["messages"] = (400, {"type": "error", "error": {"type": "invalid_request_error", "message": "mauvais"}})
    code = rf.relire(arguments("--fumee", "--max-sortie", "2000"), environ=ENV, base_url=serveur["url"])
    assert code == rf.CODE_ENVOI
    (l,) = lignes_journal()
    assert l["base_cout"] == "zero" and l["cout_compte_usd"] == 0


def test_chemin_reel_erreur_dans_le_flux_comptee_au_pire(dossier, serveur):
    serveur["messages"] = (200, FLUX_SAIN[:6] + [{"type": "error",
                                                  "error": {"type": "overloaded_error", "message": "coupé"}}])
    code = rf.relire(arguments("--fumee", "--max-sortie", "2000"), environ=ENV, base_url=serveur["url"])
    assert code == rf.CODE_ENVOI
    assert len(serveur["requetes"]) == 2
    (l,) = lignes_journal()
    assert l["statut"] == "defaut" and l["base_cout"] == "pire" and l["cout_compte_usd"] == l["pire_usd"]
    assert not os.path.exists("sortie/relecture-fable-api.md")


def test_chemin_reel_espace_envoye_en_entete(dossier, serveur):
    env = dict(ENV, ESPACE_ESSAI="wrkspc_essai")
    code = rf.relire(arguments("--fumee", "--max-sortie", "2000", "--espace", "ESPACE_ESSAI"), environ=env,
                     base_url=serveur["url"])
    assert code == rf.OK
    for r in serveur["requetes"]:
        entetes = {k.lower(): v for k, v in r["entetes"].items()}
        assert entetes.get("anthropic-workspace-id") == "wrkspc_essai"


# ---------- v3 : effort à valeurs fermées, défaut « high » ; aucun budget de réflexion ----------

@pytest.mark.parametrize("effort", ["low", "medium", "high", "xhigh", "max"])
def test_effort_admis_envoye_et_consigne(dossier, effort):
    envoi = FauxEnvoi(sain())
    assert rf.relire(arguments("--effort", effort), envoyeur=envoi, compteur=compteur_fixe(), environ=ENV) == rf.OK
    assert envoi.appels[0]["output_config"] == {"effort": effort}
    (l,) = lignes_journal()
    assert l["effort"] == effort and l["statut"] == "reponse"
    assert l["pire_usd"] == pytest.approx((133 * 8 + 128000 * 40) / 1e6)  # pire inchangé, quel que soit l'effort
    assert json.load(open("sortie/compteurs.json"))["effort"] == effort
    assert f"effort `{effort}`" in open("sortie/relecture-fable-api.md", encoding="utf-8").read()


@pytest.mark.parametrize("effort", ["MAX", "maximum", "", "ultra", "high ", "none", "disabled"])
def test_effort_hors_liste_refuse_par_l_analyseur(effort, capsys):
    with pytest.raises(SystemExit) as e:
        arguments("--effort", effort)
    assert e.value.code == 2


@pytest.mark.parametrize("effort", ["MAX", "ultra", None])
def test_effort_hors_liste_refuse_par_relire(dossier, effort):
    args = arguments()
    args.effort = effort
    envoi = FauxEnvoi(sain())
    assert rf.relire(args, envoyeur=envoi, compteur=compteur_fixe(), environ=ENV) == rf.CODE_USAGE
    assert envoi.appels == [] and not os.path.exists("sortie")
    (l,) = lignes_journal()
    assert l["statut"] == "refus_avant_envoi" and "--effort" in l["defaut"]


def test_effort_defaut_high(dossier):
    assert arguments().effort == "high"


@pytest.mark.parametrize("valeur", ["16000", "0"])
def test_budget_de_reflexion_refuse(valeur, capsys):
    # La compétence ne permet pas de borner la réflexion de claude-fable-5-2 : l'option n'existe pas, l'analyseur la refuse.
    with pytest.raises(SystemExit) as e:
        arguments("--budget-reflexion", valeur)
    assert e.value.code == 2


def test_chemin_reel_effort_envoye(dossier, serveur):
    code = rf.relire(arguments("--fumee", "--max-sortie", "2000", "--effort", "medium"), environ=ENV,
                     base_url=serveur["url"])
    assert code == rf.OK
    for r in serveur["requetes"]:  # comptage et génération portent le même effort
        assert r["corps"]["output_config"] == {"effort": "medium"}
