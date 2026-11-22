"""Essais de controle_ia.relecture_fable_api_v4 (v4, 22 novembre 2026 ; copie adaptée des essais de la v3, plus les essais
de --modele en fin de fichier), sans réseau : fausses fonctions d'envoi et de
comptage injectées, et un faux serveur local (boucle 127.0.0.1) pour le chemin réel du kit d'Anthropic. Chaque garde est
essayée sur un cas sain et sur un artefact (R5)."""
import hashlib
import http.server
import json
import os
import threading

import pytest

from controle_ia import relecture_fable_api_v4 as rf

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


# ---------- v4 : --modele à valeurs fermées (claude-fable-5-2 par défaut, claude-opus-4-6) ----------

from controle_ia import relecture_fable_api_v3 as rf3  # noqa: E402  (comparaison au comportement de la v3)

OPUS = "claude-opus-4-6"


def test_modele_defaut_fable(dossier):
    assert arguments().modele == "claude-fable-5-2" == rf.MODELE
    assert set(rf.MODELES) == {"claude-fable-5-2", "claude-opus-4-6"}


@pytest.mark.parametrize("modele", ["claude-opus-4-7", "claude-opus-5-5", "claude-fable-5-1", "opus", "OPUS",
                                    "claude-opus-4-6 ", "claude-opus-4-6-20250101", ""])
def test_modele_hors_liste_refuse_par_l_analyseur(modele, capsys):
    with pytest.raises(SystemExit) as e:
        arguments("--modele", modele)
    assert e.value.code == 2


@pytest.mark.parametrize("modele", ["claude-opus-4-7", "claude-opus-4-6 ", None, 46, ["claude-opus-4-6"]])
def test_modele_hors_liste_refuse_par_relire(dossier, modele):
    args = arguments()
    args.modele = modele
    envoi, compter = FauxEnvoi(sain()), compteur_fixe()
    assert rf.relire(args, envoyeur=envoi, compteur=compter, environ=ENV) == rf.CODE_USAGE
    assert envoi.appels == [] and compter.appels == [] and not os.path.exists("sortie")
    (l,) = lignes_journal()
    assert l["statut"] == "refus_avant_envoi" and "--modele" in l["defaut"] and l["reflexion"] is None


def test_modele_absent_de_l_espace_de_noms_refuse(dossier):
    args = arguments()
    del args.modele  # aucun défaut silencieux : un espace de noms sans modèle est refusé
    envoi = FauxEnvoi(sain())
    assert rf.relire(args, envoyeur=envoi, compteur=compteur_fixe(), environ=ENV) == rf.CODE_USAGE
    assert envoi.appels == []


def _sans_outil(l):
    return {k: v for k, v in l.items() if k not in ("heure_utc", "outil", "empreinte_outil")}


@pytest.mark.parametrize("effort", ["high", "xhigh", "max"])
def test_defaut_identique_a_la_v3(tmp_path, monkeypatch, effort):
    # Même entrée, même faux transport : paramètres envoyés et comptés, journal et compteurs égaux à ceux de la v3 (hors
    # nom, empreinte de l'outil et heure) ; relecture égale hors la ligne « Outil » et l'heure.
    sorties = {}
    for nom, mod in (("v3", rf3), ("v4", rf)):
        d = tmp_path / nom
        d.mkdir()
        monkeypatch.chdir(d)
        ecrire("consigne.md", "Relis la correction contre les remarques. Dis ce qui manque.\n")
        ecrire("piece.md", "Texte corrigé, ligne un.\nLigne deux.\n")
        ecrire("remarques.md", "Remarque 1 : préciser la ligne deux.\n")
        ecrire("avant.md", "Texte d'avant.\n")
        os.mkdir("journal")
        base = ["relire", "--piece", "piece.md", "--remarques", "remarques.md", "--avant", "avant.md", "--consigne",
                "consigne.md", "--sortie", "sortie", "--cle", "CLE_ESSAI", "--plafond-ligne", "10",
                "--journal-depense", "journal/depense.jsonl", "--effort", effort]
        envoi, compter = FauxEnvoi(sain(modele="claude-fable-5-2")), compteur_fixe(100)
        assert mod.relire(mod.analyseur().parse_args(base), envoyeur=envoi, compteur=compter, environ=ENV) == 0
        rel = open("sortie/relecture-fable-api.md", encoding="utf-8").read().split("\n")
        sorties[nom] = (envoi.appels, compter.appels, _sans_outil(lignes_journal()[0]),
                        _sans_outil(json.load(open("sortie/compteurs.json"))),
                        [x for x in rel if not x.startswith(("- Outil", "- Heure"))])
    a, b = sorties["v3"], sorties["v4"]
    assert a[0] == b[0] and a[1] == b[1]
    assert b[0][0]["model"] == "claude-fable-5-2" and b[0][0]["thinking"] == {"type": "adaptive", "display": "omitted"}
    assert {k: v for k, v in a[2].items() if k != "sha256_relecture"} == \
        {k: v for k, v in b[2].items() if k != "sha256_relecture"}
    assert {k: v for k, v in a[3].items() if k != "sha256_relecture"} == \
        {k: v for k, v in b[3].items() if k != "sha256_relecture"}
    assert a[4] == b[4]


@pytest.mark.parametrize("effort", ["low", "medium", "high", "max"])
def test_opus_46_nom_reglage_et_effort_envoyes(dossier, effort):
    envoi, compter = FauxEnvoi(sain(modele=OPUS)), compteur_fixe(100)
    assert rf.relire(arguments("--modele", OPUS, "--effort", effort), envoyeur=envoi, compteur=compter,
                     environ=ENV) == rf.OK
    (p,) = envoi.appels
    assert p["model"] == OPUS
    assert p["thinking"] == {"type": "adaptive"}  # pas de « display » (nouveau avec Opus 4.7), pas de budget
    assert p["output_config"] == {"effort": effort}
    assert p["max_tokens"] == 128000
    assert set(p) == {"model", "max_tokens", "thinking", "output_config", "messages"}  # ni échantillonnage, ni repli
    (c,) = compter.appels
    assert c["model"] == OPUS and c["thinking"] == p["thinking"] and c["output_config"] == p["output_config"]
    (l,) = lignes_journal()
    assert l["modele"] == OPUS and l["modele_servi"] == OPUS and l["reflexion"] == {"type": "adaptive"}
    assert l["effort"] == effort
    assert json.load(open("sortie/compteurs.json"))["modele"] == OPUS
    rel = open("sortie/relecture-fable-api.md", encoding="utf-8").read()
    assert rel.startswith("# Relecture par Claude Opus 4.6 (appel direct")
    assert f"Modèle demandé : `{OPUS}` ; modèle servi : `{OPUS}`" in rel
    assert "tarif 5 / 25 USD" in rel and "sans champ « display »" in rel and "« omitted »" not in rel
    assert "Fable" not in rel


def test_opus_46_effort_xhigh_refuse_avant_tout_envoi(dossier):
    envoi, compter = FauxEnvoi(sain(modele=OPUS)), compteur_fixe()
    assert rf.relire(arguments("--modele", OPUS, "--effort", "xhigh"), envoyeur=envoi, compteur=compter,
                     environ=ENV) == rf.CODE_USAGE
    assert envoi.appels == [] and compter.appels == [] and not os.path.exists("sortie")
    (l,) = lignes_journal()
    assert l["statut"] == "refus_avant_envoi" and l["envoye"] is False and l["cout_compte_usd"] == 0
    assert "xhigh" in l["defaut"] and OPUS in l["defaut"] and l["modele"] == OPUS
    # cas sain : le même effort reste admis pour Fable 5.2
    assert rf.relire(arguments("--effort", "xhigh"), envoyeur=FauxEnvoi(sain()), compteur=compteur_fixe(),
                     environ=ENV) == rf.OK


def test_opus_46_effort_par_defaut_high_admis(dossier):
    envoi = FauxEnvoi(sain(modele=OPUS))
    assert rf.relire(arguments("--modele", OPUS), envoyeur=envoi, compteur=compteur_fixe(), environ=ENV) == rf.OK
    assert envoi.appels[0]["output_config"] == {"effort": "high"}


def test_opus_46_pire_cout_et_cout_compte(dossier):
    envoi = FauxEnvoi(sain(modele=OPUS, usage={"entree": 100, "sortie": 500, "reflexion": 300,
                                               "ecriture_cache": 10, "lecture_cache": 1000}))
    assert rf.relire(arguments("--modele", OPUS), envoyeur=envoi, compteur=compteur_fixe(100), environ=ENV) == rf.OK
    (l,) = lignes_journal()
    assert l["pire_usd"] == pytest.approx((133 * 5 + 128000 * 25) / 1e6)  # 3,200665 USD
    assert l["cout_compte_usd"] == pytest.approx((100 * 5 + 10 * 5 * 2 + 1000 * 0.50 + 500 * 25) / 1e6)
    assert rf.pire_cout(1_000_000, 0, OPUS) == pytest.approx(5.0)
    assert rf.pire_cout(0, 1_000_000, OPUS) == pytest.approx(25.0)
    assert rf.pire_cout(1_000_000, 1_000_000) == pytest.approx(48.0)  # défaut : Fable 5.2, 8 + 40
    assert rf.cout_usage({"lecture_cache": 1_000_000}, OPUS) == pytest.approx(0.50)


def test_plafond_compte_au_tarif_du_modele_demande(dossier):
    # pire Opus 4.6 ≈ 3,20 USD ≤ 4 (sain) ; pire Fable 5.2 ≈ 5,12 USD > 4 (artefact)
    envoi = FauxEnvoi(sain(modele=OPUS))
    assert rf.relire(arguments("--modele", OPUS, plafond="4"), envoyeur=envoi, compteur=compteur_fixe(),
                     environ=ENV) == rf.OK
    os.rename("sortie", "sortie-1")
    envoi2 = FauxEnvoi(sain())
    assert rf.relire(arguments(plafond="4", journal="journal/autre.jsonl"), envoyeur=envoi2, compteur=compteur_fixe(),
                     environ=ENV) == rf.CODE_PLAFOND
    assert envoi2.appels == []


@pytest.mark.parametrize("demande,servi", [(OPUS, "claude-fable-5-2"), (OPUS, "claude-opus-4-8"),
                                           ("claude-fable-5-2", OPUS)])
def test_modele_servi_autre_que_demande_est_un_defaut(dossier, demande, servi):
    envoi = FauxEnvoi(sain(modele=servi))
    assert rf.relire(arguments("--modele", demande), envoyeur=envoi, compteur=compteur_fixe(),
                     environ=ENV) == rf.CODE_DEFAUT
    assert not os.path.exists("sortie/relecture-fable-api.md")
    (l,) = lignes_journal()
    assert l["modele"] == demande and l["modele_servi"] == servi and "modèle servi autre" in l["defaut"]


def test_opus_46_texte_vide_refus_et_arret_inattendu(dossier):
    for i, (res, attendu) in enumerate([(sain(modele=OPUS, texte=" "), "texte vide"),
                                        (sain(modele=OPUS, texte="", fin="refusal"), "refus du modèle"),
                                        (sain(modele=OPUS, fin="max_tokens"), "max_tokens"),
                                        (sain(modele=OPUS, fin="pause_turn"), "raison d'arrêt inattendue")]):
        sortie = f"sortie-{i}"
        args = arguments("--modele", OPUS)
        args.sortie = sortie
        assert rf.relire(args, envoyeur=FauxEnvoi(res), compteur=compteur_fixe(), environ=ENV) == rf.CODE_DEFAUT
        assert not os.path.exists(f"{sortie}/relecture-fable-api.md")
        assert attendu in lignes_journal()[-1]["defaut"]


def test_opus_46_fumee_marquee(dossier):
    assert rf.relire(arguments("--modele", OPUS, "--fumee", "--max-sortie", "2000"),
                     envoyeur=FauxEnvoi(sain(modele=OPUS, texte="OK")), compteur=compteur_fixe(), environ=ENV) == rf.OK
    rel = open("sortie/relecture-fable-api.md", encoding="utf-8").read()
    assert rel.startswith("# Appel de fumée à Claude Opus 4.6") and "pas une relecture" in rel


FLUX_OPUS = [dict(e) for e in FLUX_SAIN]
FLUX_OPUS[0] = {"type": "message_start", "message": dict(FLUX_SAIN[0]["message"], model=OPUS)}
FLUX_OPUS[1] = {"type": "content_block_start", "index": 0,
                "content_block": {"type": "thinking", "thinking": "", "signature": ""}}
FLUX_OPUS.insert(2, {"type": "content_block_delta", "index": 0,
                     "delta": {"type": "thinking_delta", "thinking": "RESUME-DE-REFLEXION-JAMAIS-ECRIT"}})


def test_chemin_reel_opus_46_contre_serveur_local(dossier, serveur):
    serveur["messages"] = (200, FLUX_OPUS)
    code = rf.relire(arguments("--modele", OPUS, "--effort", "max", "--fumee", "--max-sortie", "2000"), environ=ENV,
                     base_url=serveur["url"])
    assert code == rf.OK
    assert len(serveur["requetes"]) == 2
    compte, corps = serveur["requetes"][0]["corps"], serveur["requetes"][1]["corps"]
    for c in (compte, corps):
        assert c["model"] == OPUS and c["thinking"] == {"type": "adaptive"} and c["output_config"] == {"effort": "max"}
        assert not {"temperature", "top_p", "top_k", "fallbacks"} & set(c)
    assert corps["stream"] is True and corps["max_tokens"] == 2000
    (l,) = lignes_journal()
    assert l["modele"] == OPUS and l["modele_servi"] == OPUS
    assert l["cout_compte_usd"] == pytest.approx((57 * 5 + 40 * 25) / 1e6)
    assert "RESUME-DE-REFLEXION-JAMAIS-ECRIT" not in tout_le_texte_ecrit(dossier)
    assert open("sortie/relecture-fable-api.md", encoding="utf-8").read().endswith("\nOK\n")


def test_chemin_reel_opus_46_servi_par_un_autre_modele(dossier, serveur):
    # Le serveur rend claude-fable-5-2 (FLUX_SAIN) quand claude-opus-4-6 est demandé : défaut, pas une réponse.
    code = rf.relire(arguments("--modele", OPUS, "--fumee", "--max-sortie", "2000"), environ=ENV,
                     base_url=serveur["url"])
    assert code == rf.CODE_DEFAUT
    assert not os.path.exists("sortie/relecture-fable-api.md")
