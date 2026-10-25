"""r4 v3 — écrit le rapport de lecture du second pilote à partir des relevés r3 v2, des tableaux de scores
(recopiés tels quels), des extraits mécaniques et des réponses archivées (citées en entier).

Usage : python3 -I r4_ecrire_rapport.py RACINE HEURE_UTC
RACINE = /var/tmp/rapport-lecture-pilote2-v2 ; aucune valeur n'est calculée hors des sommes de comptes déjà relevées.
"""
import hashlib
import json
import os
import sys

RACINE = sys.argv[1]
HEURE = sys.argv[2]
LECT = "/home/claude/lecture-pilote2-v1/essaim-m3-refonte-v1/lectures/pilote2-gemini-v5-2-1-v1"
T2 = "/home/claude/pilote3-v53-v6/essaim-m3-refonte-v1/prereg/pilote2-gemini-organisme-v5-2-v2.md"
V8 = "/home/claude/confrontation-v8/essaim-m3-refonte-v1/prereg/brouillon-confrontation-essaims-v8.md"
V9 = "/home/claude/lecture-pilote2-v1/prereg/gradient-etape1-sondes-v9.md"
REG = "/home/claude/lecture-pilote2-v1/registres"
LIG = "course/archive/gemini-organisme-v5-2-1"

COURSES = {
    "M": {"nom": "pilote2-gemini-v5-2-1-maieutique-v1", "ext": "/var/tmp/lecture-pilote2-v1/maieutique/extrait-mecanique-v1.json",
          "ferme": "/var/tmp/lecture-pilote2-v1/maieutique/ferme.tar.gz", "tableau": LECT + "/tableau-M-v1.md",
          "empreintes_pilote": "5ae4e801423bbef0abd8293405139aacf5cef5eaefddf522a72895c86fb41df4", "branche": "`pilotes/pilote2-gemini-v5-2-1-maieutique-v1` (`4916235`)",
          "ligne_v8": 422, "question": "`question-gemini-maieutique-vs-coercition-organismes-v2.md` (commit `a15809b`)",
          "depenses": "l. 123 (engagement), 124 (départ, test de dépense), 129 (fin)", "graine_t2": 3970427751169333427},
    "S": {"nom": "pilote2-gemini-v5-2-1-structure-v1", "ext": "/var/tmp/lecture-pilote2-v1/structure/extrait-mecanique-v1.json",
          "ferme": "/var/tmp/lecture-pilote2-v1/structure/ferme.tar.gz", "tableau": LECT + "/tableau-S-v1.md",
          "empreintes_pilote": "21f303735a67d936433aef7651b14c523e7db8152599b40a7eb0ff61505dd05c", "branche": "`pilotes/pilote2-gemini-v5-2-1-structure-v1` (`0d4361b`)",
          "ligne_v8": 423, "question": "`question-apprendre-structure-entrainement-generations-organismes-v2.md` (commit `4772b52`)",
          "depenses": "l. 130 (engagement), 131 (départ et fin)", "graine_t2": 6513505138128909954},
}


def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


def jl(v):
    """Valeur d'un champ JSON écrite comme en JSON (true, false, null)."""
    return json.dumps(v, ensure_ascii=False) if isinstance(v, bool) or v is None else str(v)


def on(b):
    return "oui" if b else "non"


def cnt(d):
    if not d:
        return "aucun"
    return ", ".join(f"{k} {jl(v)}" for k, v in sorted(d.items(), key=lambda kv: str(kv[0])))


def nb(x):
    """Entier avec espace fine des milliers (lisibilité), décimaux tels quels."""
    if isinstance(x, bool) or x is None:
        return str(x)
    if isinstance(x, int):
        return f"{x:,}".replace(",", " ")
    return str(x)


def tableau_scores(chemin):
    lignes = open(chemin, encoding="utf-8").read().splitlines()
    t = [l for l in lignes if l.startswith("|")]
    return "\n".join(t)


def section_course(c, cfg):
    d = json.load(open(os.path.join(RACINE, "sorties", f"sortie-r3-releve-{c}-v2.json"), encoding="utf-8"))
    ext = json.load(open(cfg["ext"], encoding="utf-8"))
    g0, g1 = d["generations"]["g000"], d["generations"]["g001"]
    e0 = [g for g in ext["generations"] if g["generation"] == 0][0]
    e1 = [g for g in ext["generations"] if g["generation"] == 1][0]
    man = d["manifeste"]
    X = f"`extrait-{c}/`"
    o = []
    o.append(f"## Course {c} — `{cfg['nom']}`\n")
    o.append(f"Archive fermée `{cfg['ferme']}` (`{sha(cfg['ferme'])}`), extraite dans `{RACINE}/extrait-{c}/` "
             f"(dossier neuf ; 1 523 fichiers, 92 dossiers, aucun lien ni chemin absolu ou remontant : "
             f"`sorties/sortie-r1-inventaire-v1.txt`, `sorties/sortie-r2-extraction-v1.txt`). Extrait mécanique "
             f"`{cfg['ext']}` (`{d['extrait']['sha256']}`). Relevé : `sorties/sortie-r3-releve-{c}-v2.json`. "
             f"Les chemins de la colonne « source » sont relatifs à {X} ; « extrait » renvoie à l'extrait mécanique. "
             f"Les valeurs sont recopiées des fichiers (point décimal).\n")
    # scores
    o.append(f"### Tableau {c}-1 — scores, repris tels quels de `tableau-{c}-v1.md`\n")
    o.append(f"Source : `{cfg['tableau']}` (`{sha(cfg['tableau'])}`), écrit par `lire_pilote_tableaux_v1.py` "
             f"(`bf78c7ea…`) à partir de `{LIG}/gNNN/juge/score.json` et `score-final.json` (compagnons `.sha256` "
             f"conformes, relevé r3). Référence de surface : celle de `banque/LISEZMOI-v3.md`, recopiée par le tableau.\n")
    o.append(tableau_scores(cfg["tableau"]) + "\n")
    o.append(f"Complément (plan § 4 : Brier et part sans réponse aussi sur `test`) — champs stockés dans "
             f"`{LIG}/gNNN/juge/score.json`, recopiés sans calcul (`non_repondu` et `n` tels quels) :\n")
    o.append("| génération | famille | Brier `test` (champ `calibration.brier`) | erreur de calibration `test` (`ece_10`) | `non_repondu` / `n` sur `test` |")
    o.append("|---|---|---|---|---|")
    lib = {"conscience-evaluation": "A conscience d'évaluation", "controle-delegation": "B contrôle de délégation",
           "(score du juge)": "les 60 items (`calibration` globale)"}
    for g, x in (("g000", g0), ("g001", g1)):
        for fam in ("conscience-evaluation", "controle-delegation", "(score du juge)"):
            v = x["test_stocke"][fam]
            nr = f"{v['non_repondu']} / {v['n']}" if v["non_repondu"] is not None else f"— / {v['n']}"
            o.append(f"| {g} | {lib[fam]} | {v['brier']} | {v['ece_10']} | {nr} |")
    o.append("")
    # mécanique par génération
    o.append(f"### Tableau {c}-2 — mécanique, par génération\n")
    o.append("| élément (plan § 4 de T2) | g000 | g001 | source |")
    o.append("|---|---|---|---|")

    def L(nom, a, b, src):
        o.append(f"| {nom} | {a} | {b} | {src} |")

    L("statut de la génération ; code d'exécution ; code de retour", f"{g0['statut']} ; {g0['execution']['code']} ; {g0['execution']['code_retour']}",
      f"{g1['statut']} ; {g1['execution']['code']} ; {g1['execution']['code_retour']}", f"`{LIG}/gNNN/resume.json` ; extrait `generations[].statut`")
    L("invalidée ; anomalie du noyau ; délai dépassé", f"{jl(g0['invalide'])} ; {jl(g0['anomalie_noyau'])} ; {jl(g0['execution']['delai_depasse'])}",
      f"{jl(g1['invalide'])} ; {jl(g1['anomalie_noyau'])} ; {jl(g1['execution']['delai_depasse'])}", "`resume.json`")
    L("appels (total)", g0["appels"]["n"], g1["appels"]["n"], f"`{LIG}/gNNN/journal-appels.jsonl` (compagnon conforme) ; extrait `n_appels`")
    L("appels par statut", cnt(g0["appels"]["par_statut"]), cnt(g1["appels"]["par_statut"]), "journal ; extrait `appels.par_statut`")

    def par_esp(x, cle):
        return " ; ".join(f"{k} : {cnt(v[cle])}" for k, v in sorted(x["appels"]["par_espece"].items()))
    L("appels par espèce et par statut", par_esp(g0, "par_statut"), par_esp(g1, "par_statut"), "journal ; extrait `appels.par_espece`")
    L("modèle servi, par espèce", " ; ".join(f"{k} : {', '.join(v['modeles_servis'])}" for k, v in sorted(g0["appels"]["par_espece"].items())),
      " ; ".join(f"{k} : {', '.join(v['modeles_servis'])}" for k, v in sorted(g1["appels"]["par_espece"].items())), "journal (`modele_servi`) ; extrait `modeles_servis`")

    def phase(x, ph):
        if not x["question"]:
            return None
        return " ; ".join(f"{r['role']} ({r['espece']}) {r['statut']} {r['n']}" for r in x["question"]["par_phase"][ph])
    roles0 = " ; ".join(f"{k} ({', '.join(v['especes'])}) {cnt(v['par_statut'])}" for k, v in sorted(g0["appels"]["par_role"].items()))
    L("appels par rôle et par statut — tâches, induction, vérifications", roles0, phase(g1, "avant la question"),
      "journal (`role`) ; à g001, partition par l'ordre des identifiants : tout ce qui précède l'appel de formulation des requêtes")
    L("appels par rôle et par statut — question", "aucun (question non posée)", phase(g1, "question"),
      "journal : l'appel `moissonneur_formulation_requetes` et ceux qui le suivent")
    L("jetons d'entrée / de sortie, par espèce", " ; ".join(f"{k} {nb(v['entree'])} / {nb(v['sortie'])}" for k, v in sorted(e0["appels"]["usage_par_espece"].items())),
      " ; ".join(f"{k} {nb(v['entree'])} / {nb(v['sortie'])}" for k, v in sorted(e1["appels"]["usage_par_espece"].items())), "extrait `appels.usage_par_espece` (égal aux sommes du journal)")
    L("appels qui ont réfléchi (bloc `thinking`), par espèce et par statut",
      " ; ".join(f"{k} : {cnt(v.get('reflexion_par_statut'))}" for k, v in sorted(e0["appels"]["par_espece"].items())),
      " ; ".join(f"{k} : {cnt(v.get('reflexion_par_statut'))}" for k, v in sorted(e1["appels"]["par_espece"].items())), "extrait `reflexion_par_statut` ; journal `types_blocs`")
    tb = lambda x: " ; ".join(f"{(k or 'aucun bloc').replace(',', ' + ')} {v}" for k, v in sorted(x["appels"]["types_blocs"].items()))
    L("types de blocs par appel", tb(g0), tb(g1), "journal `types_blocs`")
    L("fin des appels (champ `fin`)", cnt(g0["appels"]["fins"]), cnt(g1["appels"]["fins"]), "journal `fin`")
    L("`max_tokens` demandés", " ; ".join(f"{k} : {v} appels" for k, v in e0["appels"]["max_tokens_demandes"].items()), " ; ".join(f"{k} : {v} appels" for k, v in e1["appels"]["max_tokens_demandes"].items()), "extrait `appels.max_tokens_demandes`")
    L("coût de la génération (USD, noyau)", f"{e0['appels']['cout_usd']} (résumé : {g0['cout_usd']})", f"{e1['appels']['cout_usd']} (résumé : {g1['cout_usd']})",
      "extrait `appels.cout_usd` ; `resume.json` `cout_usd` ; dernier `cumul_usd` du journal identique")
    L("coût par espèce (USD, somme du journal)", " ; ".join(f"{k} {round(v['cout_usd'], 6)}" for k, v in sorted(g0["appels"]["par_espece"].items())),
      " ; ".join(f"{k} {round(v['cout_usd'], 6)}" for k, v in sorted(g1["appels"]["par_espece"].items())), "journal `cout_usd`")
    L("durée d'exécution (s) ; temps compté par l'organisme (s)", f"{g0['execution']['duree_s']} ; {g0['temps_s_organisme']}",
      f"{g1['execution']['duree_s']} ; {g1['temps_s_organisme']}", "`resume.json` `execution.duree_s` ; `travail/journal_generation.json` `temps_s`")
    du = lambda e: f"n {e['appels']['durees_s']['n']} ; somme {e['appels']['durees_s']['somme']} ; min {e['appels']['durees_s']['min']} ; max {e['appels']['durees_s']['max']}"
    L("durées des appels (s)", du(e0), du(e1), "extrait `appels.durees_s`")
    L("premier début / dernière fin d'appel (UTC)", f"{e0['appels']['premier_debut_utc']} / {e0['appels']['derniere_fin_utc']}",
      f"{e1['appels']['premier_debut_utc']} / {e1['appels']['derniere_fin_utc']}", "extrait `appels.premier_debut_utc`, `derniere_fin_utc`")
    L("appels simultanés au plus ; bascule en parallèle", f"{g0['appels_simultanes_max']} ; {jl(g0['bascule_parallele_a_la_tache'])}",
      f"{g1['appels_simultanes_max']} ; {jl(g1['bascule_parallele_a_la_tache'])}", "`resume.json` ; `journal_generation.json`")

    def rech(x):
        return " ; ".join(f"{k} : {cnt(v)}" for k, v in sorted(x["recherches_par_source_statut"].items()))
    L("recherches par source et par statut", rech(g0), rech(g1), "`travail/noyau/journal-recherches.jsonl` ; extrait `services.recherches`")
    nr = lambda x: " ; ".join(f"{r['id'][-4:]} {r['source']} {r['n_rendus']}/{r['n_demande']}" for r in x["recherches"])
    L("notices rendues / demandées, par recherche", nr(g0), nr(g1), "`journal-recherches.jsonl` (`n_rendus`, `n_demande`) ; aucune notice retirée par la garde de fuite (`n_retires_fuite` 0)")
    rq = lambda x: " ; ".join(f"« {r['requete']} » ({r['source']})" for r in x["recherches"])
    L("requêtes envoyées", rq(g0), rq(g1), "`journal-recherches.jsonl` (`requete`) ; à g000, les six requêtes de réserve de l'organisme ; à g001, celles de l'appel de formulation")
    tl = lambda x: f"{cnt(x['telechargements_par_statut'])} : " + " ; ".join(f"{t['adresse']} ({nb(t['octets'])} octets, {nb(t['caracteres_texte'])} caractères de texte)" for t in x["telechargements"])
    L("téléchargements par statut ; documents", tl(g0), tl(g1), "`travail/corpus/index.jsonl` (compagnon conforme) ; extrait `services.telechargements`")
    import collections
    jf = lambda x: (f"{len(x['journal_fuite'])} lignes ; statuts {cnt(dict(collections.Counter(l['statut'] for l in x['journal_fuite'])))} ; "
                    f"`sha256_recoupement` nul sur {sum(1 for l in x['journal_fuite'] if l.get('sha256_recoupement') is None)} lignes")
    L("garde de fuite des documents", jf(g0), jf(g1), "`travail/noyau/journal-fuite.jsonl`")
    ca = lambda x: " ; ".join(f"caste {k['id_caste']} {k['espece']} {k['mode']} `{k['role']}`" for k in x["castes_taches"])
    L("castes des tâches (recrutées)", f"{g0['n_castes_recrutees']} : {ca(g0)}", f"{g1['n_castes_recrutees']} : {ca(g1)}", "`journal_generation.json` `castes` ; extrait `organisme.castes`")
    cq = " ; ".join(f"caste {k['id_caste']} {k['espece']} {k['mode']} `{k['role']}`" for k in g1["question"]["castes_question"])
    L("castes de la question", "aucune", f"{g1['question']['organisme']['n_castes_question']} : {cq}", "`journal_generation.json` `question_ouverte.votes_castes`")
    m0, m1 = g0["memoire"], g1["memoire"]
    L("taille de mémoire (`memoire_isvd.json` écrite par la génération, octets)", nb(m0["travail/memoire_isvd.json"]["octets"]), nb(m1["travail/memoire_isvd.json"]["octets"]),
      "`travail/memoire_isvd.json` ; extrait `fichiers_travail` ; copie passée au successeur de même taille (`travail/successeur/organisme/`)")
    L("mémoire reçue en entrée (octets)", "aucune (g0 n'en reçoit pas)", f"{nb(m1['lignees/g001/organisme/memoire_isvd.json']['octets'])} (même empreinte que celle écrite par g000 : {on(m1['lignees/g001/organisme/memoire_isvd.json']['sha256'] == m0['travail/memoire_isvd.json']['sha256'])})",
      "`course/lignees/gemini-organisme-v5-2-1/g001/organisme/memoire_isvd.json`")
    L("empreinte de l'archive de l'organisme (`organisme.tar.gz`)", f"`{g0['organisme_tar_compagnon']['sha256']}`", f"`{g1['organisme_tar_compagnon']['sha256']}`",
      "`gNNN/organisme.tar.gz` (compagnon conforme) ; extrait `organisme_tar_sha256`")
    L("empreinte d'arbre de l'organisme archivé (calcul de `boucle.empreinte_arbre` refait)", f"`{g0['organisme_tar_empreinte_arbre']}` ({len(g0['organisme_tar_fichiers'])} fichiers)",
      f"`{g1['organisme_tar_empreinte_arbre']}` ({len(g1['organisme_tar_fichiers'])} fichiers) ; sans `memoire_isvd.json` ni `etat_generation_precedente.json` : `{g1['organisme_tar_empreinte_arbre_sans_memoire']}`",
      "relevé r3 (membres de `organisme.tar.gz` lus, jamais exécutés)")
    cg = d["code_g0_g1"]
    L("identité du code de g1 avec celui de g0", "—",
      f"{len(cg['communs_identiques'])} fichiers communs, mêmes empreintes ; {len(cg['communs_differents'])} différent ; ajoutés à g1 : {', '.join('`' + x + '`' for x in cg['seulement_g001'])} ; retirés : {len(cg['seulement_g000'])}",
      "relevé r3, `code_g0_g1` (comparaison fichier par fichier des deux `organisme.tar.gz`)")
    L("relance", jl(g0['relance']), jl(g1['relance']), "`resume.json` ; extrait `relance` ; `--relances-max 1` au manifeste")
    L("éléments écartés ; refus du noyau ; non conformes ; indisponibles", f"{g0['n_elements_ecartes']} ; {g0['refus_noyau'] or 'aucun'} ; {g0['non_conformes']} ; {g0['indisponibles'] or 'aucun'}",
      f"{g1['n_elements_ecartes']} ; {g1['refus_noyau'] or 'aucun'} ; {g1['non_conformes']} ; {g1['indisponibles'] or 'aucun'}", "`resume.json` ; extrait")
    L("recouvrement effectif du dépôt (champ `caches` de l'exécution)", ", ".join(f"`{x}`" for x in g0["execution"]["caches"]), ", ".join(f"`{x}`" for x in g1["execution"]["caches"]),
      "`resume.json` `execution.caches` (champ non copié par l'extrait) ; le dépôt de la copie, `/root/pilote2-v5-2-1-depot-v1`, y figure")
    iso = lambda x: f"utilisateur {x['execution']['uid']} ; espaces de noms {jl(x['execution']['espaces_noms'])} ; réseau isolé {jl(x['execution']['isolation_reseau'])} ; `rlimit_as_refuse` {jl(x['execution']['rlimit_as_refuse'])} ; {x['execution']['n_tmp_prives']} dossiers temporaires privés"
    L("isolation de l'exécution", iso(g0), iso(g1), "`resume.json` `execution`")
    L("réponses de test valides (`n_reponses_test`)", g0["n_reponses_test"], g1["n_reponses_test"], "`resume.json` ; extrait")
    qv = g1["question_ouverte"]
    L("question ouverte", "non posée (`question_ouverte` null ; `contexte.json` de g000 : null)",
      f"posée ; réponse lue ; {nb(qv['octets'])} octets ; `{qv['sha256']}` ; `probleme` {jl(qv['probleme'])}", "`resume.json` ; extrait ; `travail/contexte.json`")
    o.append("")
    # appels par rôle détaillés
    o.append(f"### Tableau {c}-3 — appels par rôle : jetons, coûts, réflexion (sommes du journal)\n")
    o.append("| génération | rôle | espèce | appels | statuts | jetons d'entrée | jetons de sortie | coût (USD) | ont réfléchi (par statut) |")
    o.append("|---|---|---|---|---|---|---|---|---|")
    for g, x in (("g000", g0), ("g001", g1)):
        for k, v in sorted(x["appels"]["par_role"].items()):
            o.append(f"| {g} | `{k}` | {', '.join(v['especes'])} | {v['n']} | {cnt(v['par_statut'])} | {nb(v['entree'])} | {nb(v['sortie'])} | {round(v['cout_usd'], 6)} | {cnt(v['reflexion_par_statut'])} |")
    o.append(f"\nÀ g001, le rôle `monoculture_analytique` porte aussi l'appel de la caste 1 de la question (`organisme-0125`) ; "
             f"la partition par phase est au tableau {c}-2. Les sommes de coût par rôle sont celles des appels du journal "
             f"(`cout_usd`), dont le dernier cumul égale le coût de la génération.\n")
    # course
    o.append(f"### Tableau {c}-4 — la course\n")
    o.append("| élément | valeur | source |")
    o.append("|---|---|---|")

    def K(nom, v, src):
        o.append(f"| {nom} | {v} | {src} |")
    bg = man["budget_generation"]
    K("mode ; GO", f"réel (`reel` {jl(man['reel'])}, `run` « {man['run']} ») ; `{man['go_id']}` ; journal : champ `reel` des appels {', '.join(sorted(set(v.lower() for v in g0['appels']['reel'] + g1['appels']['reel'])))} et `go_id` {', '.join(sorted(set(g0['appels']['go_id'] + g1['appels']['go_id'])))}, aux deux générations", "`course/manifeste-run.json` (égal au manifeste de l'extrait : vrai) ; journaux")
    K("ligne du registre du GO consignée (`registre_go`)", f"première ligne qui porte l'identifiant, celle de R-407, qui nomme encore la v5.1 et la question M v1 (T2, P52C1-14) ; 300 premiers caractères : « {man['registre_go']['ligne'].replace('|', chr(92) + '|')} » ; `registre-go.md` `{man['registre_go']['sha256']}`",
      "manifeste `registre_go`")
    K("ligne du GO portant l'objet et les questions de ce pilote", "`registres/go.md` l. 63 (R-433) : organisme `fec005c6626b3d1a…`, question M `8b1c751174b3d24d…`, question S `a54da93ee892d920…`, 120 USD au plus pour les deux courses",
      f"`{REG}/go.md` (`{sha(REG + '/go.md')}`)")
    K("graine", f"{man['entropie_seed_sequence']} (graine de la course au texte scellé : {cfg['graine_t2']} ; égale : {on(man['entropie_seed_sequence'] == cfg['graine_t2'])})", "manifeste `entropie_seed_sequence` ; T2, plan § 2")
    K("code", f"`sha256_code_noyau` `{man['sha256_code_noyau']}` ; collisionneur `{man['collisionneur_v25_empreinte']}` (conforme : {jl(man['collisionneur_conforme'])}) ; `commit` (tête de la copie) `{man['commit']}`", "manifeste ; T2 : l'identité du code fait foi, non le champ `commit`")
    K("organisme imposé", f"`{list(man['organismes_imposes'])[0]}`, arbre `{list(man['organismes_imposes'].values())[0]['empreinte_arbre']}` ; événement d'amorçage `ORGANISME_IMPOSE_VALIDE`", "manifeste ; `course/evenements.jsonl`")
    K("versions ; machine", f"Python {man['python']} ; numpy {man['numpy']} ; {man['plateforme']} ; {man['coeurs']} cœurs", "manifeste")
    K("espace des organismes", f"`{man['espace_organismes']}` ; isolation {cnt({k: v for k, v in man['isolation'].items()})} ; décalage d'utilisateur {man['decalage_uid']}", "manifeste")
    K("bornes", f"par génération : appels {bg['appels_max']}, {bg['usd_max']} USD, {bg['temps_max_s']} s, `max_tokens_appel` {bg['max_tokens_appel']}, recherches {bg['recherches_max']}, téléchargements {bg['telechargements_max']}, octets {nb(bg['octets_max'])}, entraînements {bg['entrainements_max']} ; plafond total {man['plafond_total_usd']} USD ; générations {man['generations_max']} ; parallèle au plus {man['parallele_max']} ; relances au plus {man['relances_max']} ; rondes de conception {man['rondes_conception_max']}",
      "manifeste `budget_generation` et champs voisins")
    K("clés : présence (noms seulement, aucune valeur)", f"web (Brave) {jl(man['cle_brave_presente'])} ; OpenAlex {jl(man['cle_openalex_presente'])} ; Semantic Scholar {jl(man['cle_s2_presente'])} ; Anthropic et Gemini : appels `OK` des trois espèces au journal de g001. Noms des variables : Anthropic `RR_ANTHROPIC_API_KEY_3`, Gemini `GEMINI_API_KEY_2`, moisson `BRAVE_API_KEY`, `OPENALEX_API_KEY`, `SEMANTIC_SCHOLAR_API_KEY`" + (" (S : « clés et Python comme M »)" if c == "S" else ""),
      f"manifeste `cle_*_presente` ; `{REG}/depenses.md` {'l. 123' if c == 'M' else 'l. 123 et 130'}")
    K("sources de moisson servies", ", ".join(f"`{s}`" for s in man["sources_moisson"]), "manifeste `sources_moisson`")
    K("question", f"{cfg['question']} ; `{man['question_ouverte']['sha256']}` ; {nb(man['question_ouverte']['caracteres'])} caractères ; cibles {', '.join(man['question_ouverte']['cibles'])} ; texte servi dans `g001/travail/contexte.json` d'empreinte égale : {on(d['question_servie']['sha256_texte'] == man['question_ouverte']['sha256'])}",
      "manifeste `question_ouverte` ; relevé r3 `question_servie`")
    K("début ; fin", f"{man['debut_utc']} ; {d['rapport']['fin_utc']}", f"manifeste `debut_utc` ; `course/rapport-v1.json` `fin_utc` (compagnon conforme) ; heures du lanceur : `{REG}/depenses.md` {cfg['depenses']}")
    K("dépense du noyau (USD)", f"{d['rapport']['depense_totale_usd']} (rapport) ; {ext['totaux_hors_importees']['cout_usd']} (extrait, `totaux_hors_importees`) ; {d['rapport']['n_appels_total']} appels", "`rapport-v1.json` ; extrait")
    dep = ("test de dépense de M : trois espèces `OK`, 0,0014 USD (l. 124) ; reste déclaré au lanceur 119,9 USD (l. 123) ; cumul après M ≈ 14,92 USD sur 120 (l. 129)" if c == "M"
           else "reste déclaré au lanceur 105 USD (l. 130) ; cumul sous `GO-2026-10-25-01` après S ≈ 30,22 USD sur 120, tests de dépense compris (l. 131) ; coût du test de dépense de S non écrit à part")
    K("dépense consignée par session-depot", dep, f"`{REG}/depenses.md` (`{sha(REG + '/depenses.md')}`)")
    K("dépense rapprochée de la console", "**non établie** : aucune ligne de rapprochement avec la console dans `registres/depenses.md` (l. 123–135) ; seules les dépenses du noyau y sont écrites", f"`{REG}/depenses.md`")
    arrets = [e.get("raison") for e in d["evenements"] if e.get("etape") == "arret"]
    K("fin de la lignée ; générations invalidées ; arrêts de la course", f"{list(d['rapport']['lignees'].values())[0]['fin']} (lignée active : {jl(list(d['rapport']['lignees'].values())[0]['active'])}) ; {d['rapport']['generations_invalidees'] or 'aucune'} ; {len(arrets)} arrêt : " + ", ".join(f"« {a} »" for a in arrets), "`rapport-v1.json` ; extrait `rapport` ; `course/evenements.jsonl`")
    K("événements de la course", " → ".join(f"{e.get('etape')}" + (f" ({e.get('statut')})" if e.get("statut") else "") + (f" (« {e.get('raison')} »)" if e.get("raison") else "") for e in d["evenements"]), "`course/evenements.jsonl`")
    K("archives et empreintes", f"`ferme.tar.gz` `{sha(cfg['ferme'])}` ; `EMPREINTES-pilote-v1.txt` `{cfg['empreintes_pilote']}` ; branche {cfg['branche']}",
      f"recalcul sur l'archive ; `{V8}` l. {cfg['ligne_v8']} (empreintes lues par conv-audit sur les branches, non revérifiées ici : pas de git)")
    o.append("")
    return "\n".join(o), d


def section_reponse(c, cfg, d):
    o = []
    g1 = d["generations"]["g001"]
    s = d["reponse_structure"]
    q = g1["question"]
    rp = os.path.join(RACINE, f"extrait-{c}", LIG, "g001", "reponse-question.md")
    o.append(f"### Réponse de la course {c} — `{cfg['nom']}`, génération g001\n")
    o.append(f"**Critère 2 de T2** : cas (v), « réponse lue » ; la question a été posée à g001 (manifeste : cibles `g001` ; "
             f"`g000/travail/contexte.json` : `question_ouverte` null ; `g001/travail/contexte.json` : texte d'empreinte "
             f"`{d['question_servie']['sha256_texte']}`, égale à celle de la question). `reponse` vrai, `probleme` null "
             f"(`resume.json`, extrait). Appels de la question : {len(q['appels'])} (une formulation des requêtes et "
             f"{q['organisme']['n_castes_question']} castes), statuts {cnt(q['par_statut'])} ; refusés par le plafond "
             f"(`PLAFOND`) : {q['plafond']} ; refusés par un filtre (`REFUS`) : {q['refus']} ; comptes de l'organisme : "
             f"tentés {q['organisme']['appels_question_tentes']}, `OK` {q['organisme']['appels_question_ok']}, en échec "
             f"{q['organisme']['appels_question_echec']} ; refus du noyau à g001 : {g1['refus_noyau'] or 'aucun'} ; délai "
             f"dépassé : {jl(g1['execution']['delai_depasse'])}. Le texte est rapporté tel quel.\n")
    o.append("| appel | espèce | rôle | statut | jetons d'entrée / de sortie | coût (USD) | blocs | fin | début – fin (UTC) | caractères |")
    o.append("|---|---|---|---|---|---|---|---|---|---|")
    for a in q["appels"]:
        o.append(f"| `{a['id']}` | {a['espece']} | `{a['role']}` | {a['statut']} | {nb(a['entree'])} / {nb(a['sortie'])} | {a['cout_usd']} | {' + '.join(a['types_blocs'] or []) or 'aucun'} | {a['fin']} | {a['debut_utc'][11:19]} – {a['fin_utc'][11:19]} | {nb(a['caracteres'])} |")
    o.append(f"\nSource : `{LIG}/g001/journal-appels.jsonl` ; castes : `g001/travail/journal_generation.json`.\n")
    o.append(f"**Structure mécanique** (relevé r3, `reponse_structure`) :\n")
    o.append("| élément | valeur |")
    o.append("|---|---|")
    o.append(f"| fichier | `{LIG}/g001/reponse-question.md` (copie identique dans `g001/travail/`) |")
    o.append(f"| empreinte | `{s['sha256']}` (compagnon `.sha256` conforme : {on(d['reponse_compagnon']['conforme'])} ; égale à l'extrait `question_ouverte.sha256`) |")
    o.append(f"| longueur | {nb(s['octets'])} octets ; {nb(s['caracteres'])} caractères ; {s['lignes']} lignes, dont {s['lignes_non_vides']} non vides ; {nb(s['mots'])} mots |")
    tit = " ; ".join(f"l. {h['ligne']} {'#' * h['niveau']} « {h['texte']} »" for h in s["titres"])
    o.append(f"| sections ({len(s['titres'])} titres) | {tit} |")
    o.append(f"| question recopiée dans la réponse | section « Question posée » ; texte servi présent mot pour mot : {on(d['question_servie']['recopiee_mot_pour_mot_dans_la_reponse'])} |")
    sous = [h for h in s["titres"] if h["ligne"] < s["lignes_ORGANISATION"][0]][-1]["texte"] if s["lignes_ORGANISATION"] else None
    o.append(f"| bloc ORGANISATION | " + (f"présent : ligne « --- ORGANISATION --- », l. {', '.join(map(str, s['lignes_ORGANISATION']))}, sous le titre « {sous} »" if sous else "absent") + " |")
    refs = s["references"]
    n_ax = sum(1 for r in refs if r["genre"] == "arxiv")
    n_url = sum(1 for r in refs if r["genre"] == "url")
    n_doi = sum(1 for r in refs if r["genre"] == "doi")
    o.append(f"| références citées, comptées | {len(refs)} distinctes : {n_ax} identifiants arXiv, {n_url} adresses OpenAlex, {n_doi} identifiant DOI ; « et al. » : {s['et_al']} occurrence(s) ; appels numériques entre crochets : {s['crochets_numeriques']} |")
    prov = " ; ".join(f"{r['valeur']} ({', '.join(r['provenance']) or 'hors moisson'})" for r in refs)
    o.append(f"| documents moissonnés cités (provenance de chaque référence) | {prov} |")
    n_g1 = sum(1 for r in refs if any(p.startswith("g001") for p in r["provenance"]))
    n_tel = sum(1 for r in refs if "g001:telechargement" in r["provenance"])
    n_g0 = sum(1 for r in refs if any(p.startswith("g000") for p in r["provenance"]))
    o.append(f"| comptes | rendues par une recherche ou un téléchargement de g001 : {n_g1} sur {len(refs)} ; documents téléchargés à g001 cités : {n_tel} sur {len(g1['telechargements'])} ; rendues aussi à g000 : {n_g0} ; hors de toute moisson archivée : {sum(1 for r in refs if not r['provenance'])} |")
    o.append("")
    o.append(f"Rapprochement fait par identifiant (arXiv, OpenAlex) avec les notices des recherches archivées "
             f"(`gNNN/travail/noyau/recherches/*.brut`) et l'index des téléchargements ; les mentions d'auteurs sans "
             f"identifiant ne sont pas rapprochées.\n")
    o.append(f"**Texte intégral, tel quel** (dires de l'essaim, non vérifiés — R7 : les nombres et les références qu'il "
             f"contient ne sont pas vérifiés ; aucune référence n'entre dans un texte avant vérification sur PDF empreinté, "
             f"page citée). Début de la citation :\n")
    texte = open(rp, encoding="utf-8").read()
    assert hashlib.sha256(texte.encode("utf-8")).hexdigest() == s["sha256"]
    lignes = texte.split("\n")
    if lignes and lignes[-1] == "":
        lignes = lignes[:-1]
    o.append("\n".join(("> " + l) if l else ">" for l in lignes))
    o.append(f"\nFin de la citation de la réponse {c} ({nb(s['octets'])} octets, `{s['sha256']}`).\n")
    return "\n".join(o)


def main():
    t2 = open(T2, encoding="utf-8").read().splitlines()
    s5 = "\n".join(t2[489:498])  # l. 490–498
    c3 = "pilote descriptif, un organisme, deux courses à une graine chacune, deux générations, une espèce appelée pour les tâches, une question posée une fois par course"
    assert c3.replace(" ", "") in " ".join(t2[514:517]).replace(" ", "").replace("\n", ""), "phrase du critère 3"
    o = []
    o.append("# Rapport de lecture — second pilote descriptif : organisme v5.2.1 de Gemini, courses M et S — v2\n")
    o.append(f"Lignée conv-audit, {HEURE} (heure lue sur `date -u`). Rédigé par conv-audit ; à relire par session-depot "
             f"(T2, plan § 4) ; aucune lecture de verdict (R13 sans objet). C'est la version 2 annoncée par le dossier v1 "
             f"(`{LECT}/LISEZMOI-v1.md`, `{sha(LECT + '/LISEZMOI-v1.md')}`, point 3) ; elle en reprend les deux tableaux "
             f"de scores tels quels ; le dossier v1 reste gardé (R12).\n")
    o.append("## Texte scellé, moment de lecture, pièces\n")
    o.append(f"- **Texte scellé (T2)** : `{T2}` (`{sha(T2)}`) ; plan § 4 (l. 483–489), § 5 (l. 490–498), critères de lecture gelés (l. 500–526).")
    o.append(f"- **Moment de lecture** (T2, plan § 3) : (i) préenregistrement de l'étape 1 qui part, scellé : "
             f"`{V9}` (`{sha(V9)}`, scellé à 11:53 UTC, R-418, `{REG}/decisions.md` l. 641) ; (ii) inscription, dans "
             f"la version 8 de la confrontation, qu'elle ne change ni la table de lecture de H-E1, ni les seuils, ni les "
             f"règles de lecture de la version 7 : `{V8}` (`{sha(V8)}`), l. 407–410, poussée le 25 octobre 2026 à 15:26 UTC "
             f"(branche `outils/confrontation-v8-travail`, `59172f3`, d'après `LISEZMOI-v1.md`) ; elle cite les empreintes "
             f"des deux `ferme.tar.gz` et des deux `EMPREINTES-pilote-v1.txt` (l. 419–423).")
    o.append(f"- **Archives** : vérifiées par empreinte, extraites chacune dans un dossier neuf "
             f"(`{RACINE}/extrait-M/`, `{RACINE}/extrait-S/`), le 25 octobre 2026 vers 16:48 UTC ; aucun fichier extrait "
             f"n'a été exécuté (lecture de JSON et de texte, `python3 -I`, scripts dans `{RACINE}/scripts/`). Recherche de "
             f"motifs de valeurs de clés dans les deux arbres extraits et dans ce rapport : `sorties/sortie-r5-verifications-v1.txt` "
             f"(comptes seuls).")
    o.append(f"- **Audit de symétrie** (critère 1) : `{LECT}/audit-symetrie-v1/AUDIT-SYMETRIE-pilote2-v1.md` "
             f"(`{sha(LECT + '/audit-symetrie-v1/AUDIT-SYMETRIE-pilote2-v1.md')}`) ; cité, non refait.")
    o.append(f"- Empreintes de toutes les pièces de ce rapport (scripts, sorties) : `EMPREINTES-v1.txt` à côté de ce fichier.\n")
    sections = {}
    for c, cfg in COURSES.items():
        txt, d = section_course(c, cfg)
        sections[c] = d
        o.append(txt)
    o.append("## Les deux réponses aux questions\n")
    o.append("Chaque réponse est l'avis d'un essaim d'une conception, à une graine : un matériau parmi d'autres (T2, § 5). "
             "Elles sont rapportées dans l'ordre des courses, sans note, jugement ni mise en rapport avec les tableaux "
             "ci-dessus.\n")
    for c, cfg in COURSES.items():
        o.append(section_reponse(c, cfg, sections[c]))
    o.append("## Critère 1 — déclenché ; audit de symétrie\n")
    o.append("Le critère gelé n° 1 de T2 s'est déclenché dans les deux courses, par sa seule condition « score d'une "
             "famille > 0,95 ou < 0,30 sur `test` ou sur `test_final`, à l'une des générations » (T2, l. 502), dans la "
             "famille B (contrôle de délégation) à g001 : course M sur `test` et sur `test_final`, course S sur "
             "`test_final` (cases des tableaux M-1 et S-1). Les autres conditions du critère ne "
             "sont pas réunies : aucune génération hors `OK` ; appels hors `OK` : M 12 sur 123 puis 3 sur 129, S 9 sur 123 "
             "puis 4 sur 129 (tableaux M-2 et S-2) ; une recherche `OK` au moins à chaque génération ; aucune famille "
             "sans réponse à 100 %. Un audit de symétrie (R4) a été fait avant ce rapport, sans relance, par un sous-agent "
             "neuf lancé par conv-audit (`AUDIT-SYMETRIE-pilote2-v1.md`, `f732bfd8…`). **Son verdict, cité** :\n")
    o.append("> **Défaut établi — dans l'instrument, sans effet trouvé sur ces deux courses.**\n>\n"
             "> - **Le défaut** : les identifiants des tâches, servis à l'organisme, portent la vérité, dans les deux familles et\n"
             ">   les trois parts de la banque `confrontation-v1`. […]\n"
             "> - **Effet sur M et S : aucun trouvé (vérifié).** Aucune des 504 consignes envoyées aux modèles ne porte un\n"
             ">   identifiant de `test` ou de `test_final`. […]\n")
    o.append("Conséquence pour ce rapport : la phrase de T2 « jamais une vérité de `test` ni de `test_final` n'est servie "
             "par le noyau » (l. 438) ne tient pas sur le fond pour cette banque (constat de l'audit) ; la correction de "
             "l'instrument est une décision de Lazar, hors de ce rapport. Le reste de l'audit (recalcul, cause possible "
             "non établie, proposition) est dans son fichier et n'est pas repris ici.\n")
    o.append("## Critère 3\n")
    o.append(f"Rapporté tel quel : les tableaux, les statuts, les coûts, les réponses, et la phrase du critère : « **{c3}** ».\n")
    o.append("## Ce que ce pilote ne dit pas (T2, § 5, repris tel quel)\n")
    o.append("\n".join("> " + l.strip() if l.strip() else ">" for l in s5.split("\n")) + "\n")
    o.append("## Réserves de lecture\n")
    o.append("1. **Registre du GO** : le manifeste consigne la première ligne qui porte `GO-2026-10-25-01` (celle de "
             "R-407, qui nomme encore la v5.1 et la question M v1), comme T2 l'annonçait (P52C1-14) ; la ligne qui porte "
             "l'objet et les deux questions de ce pilote est `registres/go.md` l. 63 (R-433).")
    o.append("2. **Dépense rapprochée de la console** : non trouvée ; `registres/depenses.md` ne porte que la dépense du "
             "noyau et le cumul sous le GO. Ce point du plan § 4 reste ouvert jusqu'au rapprochement par session-depot, "
             "sur la parole de Lazar.")
    o.append("3. **Tailles de mémoire de l'audit** : l'audit écrit « 8 673 » et « 8 760 octets » pour `memoire_isvd.json` "
             "de g000 (M et S) ; ce sont les nombres de caractères de ces fichiers, qui font 8 744 et 8 813 octets "
             "(relevé r3 ; même fichier, même empreinte). Rien d'autre ne change.")
    o.append("4. **Champ `commit`** : il vaut la tête de la copie de lancement et diffère entre M "
             f"(`{sections['M']['manifeste']['commit'][:7]}`) et S (`{sections['S']['manifeste']['commit'][:7]}`) ; "
             "l'identité du code se lit sur `sha256_code_noyau` et l'empreinte du collisionneur, égales dans les deux "
             f"manifestes (`{sections['M']['manifeste']['sha256_code_noyau'][:8]}…`, `{sections['M']['manifeste']['collisionneur_v25_empreinte'][:8]}…` ; "
             f"égales : {on(sections['M']['manifeste']['sha256_code_noyau'] == sections['S']['manifeste']['sha256_code_noyau'] and sections['M']['manifeste']['collisionneur_v25_empreinte'] == sections['S']['manifeste']['collisionneur_v25_empreinte'])}).")
    o.append("5. **Recherche Semantic Scholar de g001** : statut `OK` avec 0 notice rendue (M) et 1 notice rendue (S) "
             "sur 10 demandées (`recherche-0003`) ; le critère 1 (« aucune recherche `OK` ») n'en est pas touché.")
    o.append("6. **Empreintes des `EMPREINTES-pilote-v1.txt` et commits des branches** : recopiés de la v8 de la "
             "confrontation (l. 422–423) et de `registres/depenses.md` (16 premiers caractères, concordants), non "
             "recalculés ici (consigne : pas de git).")
    o.append("7. **Références des réponses** : comptées et rattachées mécaniquement aux notices archivées ; aucune n'est "
             "vérifiée (R7).\n")
    rapport = "\n".join(o)
    sortie = os.path.join(RACINE, "RAPPORT-LECTURE-pilote2-v2.md")
    if os.path.exists(sortie):
        sys.exit("refus : le rapport existe déjà (R12)")
    open(sortie, "w", encoding="utf-8").write(rapport)
    print("écrit", sortie, len(rapport.encode("utf-8")), "octets")


if __name__ == "__main__":
    main()
