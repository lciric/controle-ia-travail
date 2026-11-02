"""Vérificateur neuf (VI), vraies pièces de P3 par liens symboliques dans un dossier temporaire, processeur, sans modèle.
Comptes seulement : aucun texte, aucun score, aucune étiquette, aucune activation n'est lu ni affiché (consignes par
`charger_consignes`, via `charger_pieces`).
(a) U+FFFD par épisode : les 7, les 147, les 240 ;
(b) épisode à U+FFFD : pas comptés (unité de `balayages_max`), complets, et pas de l'ancienne unité, le long du
    découpage canonique de chaque action qui en contient (ordre de grandeur du budget de 16 par U+FFFD) ;
(c) forme des 4 lots ciblés (B-L1), calculée sans modèle : longueurs de contexte de chaque ligne à chaque action,
    comme `rejouer_episode_lot` (lignes exactes : identifiants connus ; approchées et cible : `forcee`, nombre de jetons
    exact, fin par défaut) ; pas où une approchée fixe L (strict), à un jeton (règle du code), et à d_max jetons
    (d_max = nombre d'actions antérieures de la ligne à jeton de fin compté : borne de l'écart de clôture)."""
import json
import shutil
import sys
import tempfile
from pathlib import Path

COPIE, PRINCIPAL, TOK = (Path(x) for x in sys.argv[1:4])
sys.path.insert(0, str(COPIE / "src"))
from controle_ia.runs_nuit import resolution_graine_lot_v1 as rl  # noqa: E402
from controle_ia.runs_nuit import resolution_graine_v1 as rg  # noqa: E402
from controle_ia.scellement import sceller  # noqa: E402

R = Path(tempfile.mkdtemp(prefix="vi-reel-"))
try:
    for d in ("donnees/20261019-230011-p3-reel", "donnees/t05-pilote-v1", "diag/20261019-230011-p3-reel",
              "runs/20261019-230011-p3-reel"):
        (R / d).parent.mkdir(parents=True, exist_ok=True)
        (R / d).symlink_to(PRINCIPAL / d)
    (R / "prereg").mkdir(exist_ok=True)
    for n in ("P3-consignes-v1.md", "P3-consignes-v1.md.sha256"):
        (R / "prereg" / n).symlink_to(PRINCIPAL / "prereg" / n)
    shutil.copy(COPIE / "prereg/R1-table-tokenisation-v2.json", R / "prereg/R1-table-tokenisation-v2.json")
    sceller(R / "prereg/R1-table-tokenisation-v2.json")          # sceau de la copie temporaire seulement
    config = json.loads((COPIE / "prereg/R1-graine-config-v1.json").read_text(encoding="utf-8"))
    p = rg.charger_pieces(config, R)
    T = int(config["T"])
    from transformers import AutoTokenizer

    from controle_ia.harnais.formats import FormatChat

    tok = AutoTokenizer.from_pretrained(str(TOK))
    fmt = FormatChat(tok, variables=config["agent"]["variables_gabarit"])
    fmt.fins = {int(x) for x in p.table["fins_du_format"]} | {fmt._pieces(("x", "y"))["cloture"][0]}
    cl = rg.classer(p, fmt, T)
    val = rg.episodes_de_l_etape("validation", config, cl)
    res = rg.episodes_de_l_etape("resolution", config, cl)
    nr = [e for e, x in cl.items() if x["entree"] and x["entree"]["methode"] == "non_resolu"]

    def nf(e):
        return sum(x["texte"].count(rg.FFFD) for x in rg.EpisodeP3(p, e, T).lignes)

    print("(a) U+FFFD : 7 →", {e: nf(e) for e in res if nf(e)}, "; total des 7", sum(nf(e) for e in res),
          "; 147 →", sum(nf(e) for e in val), "; 240 →", sum(nf(e) for e in p.par_episode),
          "; épisodes à U+FFFD parmi les 240 :", sum(1 for e in p.par_episode if nf(e)))
    voc = rg.Vocabulaire(tok, fmt.fins, len(tok))
    for e in res:
        if not nf(e):
            continue
        ep = rg.EpisodeP3(p, e, T)
        for t, x in enumerate(ep.lignes):
            texte = x["texte"]
            if rg.FFFD not in texte:
                continue
            cible, etat = rg.Cible(texte, voc), rg.Cible.initial()
            comptes = complets = anciens = 0
            ids = tok(texte, add_special_tokens=False)["input_ids"]
            ok = True
            for i in ids:
                cands, compte, complet = cible.recherche(etat)
                if i not in cands:
                    ok = False
                    break
                comptes += compte
                complets += complet
                anciens += bool((cible._attendu(etat) or (b"", False))[1])
                etat = cible.avancer(etat, i)
            print(f"(b) {e}, action {t} : U+FFFD {texte.count(rg.FFFD)} ; chemin canonique valide {ok and cible.fini(etat)}"
                  f" ; pas comptés {comptes} (dont complets {complets}) ; ancienne unité {anciens} ; plafond de "
                  f"l'épisode {config['balayages_max'] * nf(e)} ; jetons de P3 de l'action {ep.jetons[t]}, canoniques "
                  f"{len(ids)}")
    # (c) forme des lots
    from controle_ia.environnements.pilote_a import charger_taches

    taille = rl.exiger_meme_lot_que_p3(config, p.manifeste_p3)
    lots = rl.plan_des_lots(charger_taches(R / config["chemin_taches"]), taille, p.lignes)
    pad = rl.pad_du_format(fmt)
    fins = {int(x) for x in fmt.fins}
    for e in sorted(nr, key=lambda x: rl.lot_de(lots, x)[0]):
        k, lot, rang = rl.lot_de(lots, e)
        lignes = rl.lignes_du_lot(p, fmt, T, cl, lot, e)
        # la cible est traitée comme une ligne approchée pour sa longueur (nombre de jetons exact, fin par défaut)
        tc = lignes[rang]
        lignes[rang] = rl.LigneLot(tc.episode, tc.fabrique_env, tc.textes, tc.jetons, tc.jetons_notes,
                                   [list(x) for x in cl[e]["base_nv"]], "cible-longueur", False, tc.graines)
        envs = [x.fabrique_env() for x in lignes]
        B = len(lignes)
        trs, debuts, journaux = [[] for _ in range(B)], [None] * B, [[] for _ in range(B)]
        afin_avant = [0] * B
        approchee = [b != rang and not lignes[b].exacte for b in range(B)]
        f_strict = f_un = f_dmax = egal = 0
        for t in range(T):
            ctx = []
            for b in range(B):
                obs = envs[b].observation(0, t, journaux[b])
                if t == 0:
                    debuts[b] = (envs[b].consigne_privee(0), obs)
                    ctx.append(fmt.ouverture(*debuts[b]))
                else:
                    ctx.append(trs[b] + fmt.tour(debuts[b], obs))
            lon = [len(c) for c in ctx]
            m_e = max(x for b, x in enumerate(lon) if not approchee[b])
            appr = [(lon[b], afin_avant[b]) for b in range(B) if approchee[b]]
            if appr:
                m_a = max(x for x, _ in appr)
                f_strict += m_a > m_e
                f_un += m_a + 1 > m_e
                f_dmax += any(x + d > m_e for x, d in appr)
                egal += m_a == m_e
            for b in range(B):
                fd = rl.fin_par_defaut(fmt, debuts[b])
                nv = lignes[b].forcee(t, pad, fd, fins)
                trs[b] = ctx[b] + nv + fmt.cloture(debuts[b], nv)
                journaux[b].append((0, t, lignes[b].textes[t]))
                afin_avant[b] += int(lignes[b].jetons[t]) - int(lignes[b].jetons_notes[t])
        print(f"(c) lot {k} (cible {e}, rang {rang}) : approchées {sum(approchee)} ; actions {T} ; L fixée strictement "
              f"par une approchée {f_strict} ; à un jeton (règle du code) {f_un} dont égalités {egal} ; à d_max jetons "
              f"{f_dmax}")
finally:
    shutil.rmtree(R)
