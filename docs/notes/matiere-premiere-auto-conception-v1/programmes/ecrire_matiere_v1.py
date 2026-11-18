#!/usr/bin/env python3
"""Écrit matiere-premiere-v1.md à partir de releve-mecanismes-v1.json et de programmes/regroupements-v1/*.txt.
Arrêt si un mécanisme décrit des huit familles n'est pas rangé exactement une fois, ou si un identifiant est inconnu.
Usage (depuis docs/notes/matiere-premiere-auto-conception-v1) :
  python programmes/ecrire_matiere_v1.py > programmes/ecrire_matiere_v1.sortie.txt"""
import collections, hashlib, json, sys
from pathlib import Path

RACINE = Path(__file__).resolve().parents[4]
FAM8 = ["exploration", "originalité", "épreuve", "jugement", "mémoire", "sélection", "coût", "auto-conception"]
rel = json.loads(Path("releve-mecanismes-v1.json").read_text(encoding="utf-8"))
T = {e["indice"]: e for e in rel["travaux"]}
M = {m["id"]: (e, m) for e in rel["travaux"] for m in e["mecanismes"]}

def sha(chemin):
    return hashlib.sha256((RACINE / chemin).read_bytes()).hexdigest()

# --- regroupements ---------------------------------------------------------------------------
CL = {}  # famille -> liste de dicts(nom, ids)
for f in sorted(Path("programmes/regroupements-v1").glob("*.txt")):
    fam, cur = None, None
    for ligne in f.read_text(encoding="utf-8").splitlines():
        if ligne.startswith("# "):
            fam = ligne[2:].strip(); CL[fam] = []
        elif ligne.startswith("## "):
            cur = dict(nom=ligne[3:].strip(), ids=[]); CL[fam].append(cur)
        elif ligne.startswith("ids:"):
            cur["ids"] += ligne[4:].split()
for fam in FAM8:
    vus = collections.Counter(i for c in CL[fam] for i in c["ids"])
    attendus = {i for i, (e, m) in M.items() if m["famille"] == fam and not m["suggere_par_le_titre"]}
    dup = [i for i, n in vus.items() if n > 1]
    inconnus = [i for i in vus if i not in attendus]
    manquants = sorted(attendus - set(vus))
    if dup or inconnus or manquants:
        sys.exit(f"ARRÊT {fam} : doublons {dup} ; inconnus {inconnus} ; manquants {manquants}")
print("regroupements : chaque mécanisme décrit des huit familles est rangé une fois,", sum(len(c['ids']) for f in FAM8 for c in CL[f]), "mécanismes,", sum(len(CL[f]) for f in FAM8), "regroupements")

# --- machines (liste retenue ; titre et nature) ----------------------------------------------------
MACH_LUES = [593, 112, 121, 57]
MACH_NOTICE = [136, 240, 239, 236, 629, 241, 254, 245, 125, 595, 396, 482, 259, 384, 607, 625, 110, 70, 126, 611, 398, 513, 594, 358, 576, 577,
               2, 13, 133, 139, 142, 141, 135, 134, 150, 128, 279, 452, 102, 107, 118, 120, 395, 441, 488, 491, 332, 30, 541, 550, 529, 370, 198, 397, 104, 111, 407]
MACH = set(MACH_LUES) | set(MACH_NOTICE)
def court(nom):
    return nom.split(" : ")[0]
CLEF = {}  # id mécanisme -> (famille, numéro, nom)
for fam in FAM8:
    for n, c in enumerate(CL[fam], 1):
        for i in c["ids"]:
            CLEF[i] = (fam, n, c["nom"])

def lib(e):
    return f"{e['titre']} ({e['date']}) — {e['adresse']}"
PROF = {"lecture approfondie sur PDF": "lecture approfondie", "page ou résumé": "page ou résumé", "notice seule": "notice seule"}
out = []
w = out.append
c = rel["comptes"]
w("# Matière première de l'auto-conception de l'organisme d'idéation — mécanismes publiés d'exploration, d'originalité, d'épreuve, de jugement, de mémoire, de sélection, de coût et d'auto-conception — v1\n")
w("Pièce servie telle quelle à des proposeurs. Elle décrit ce que dit un moissonnage de 630 travaux ; elle ne juge aucun mécanisme et ne dit pas lequel est bon. Écrite le 18 novembre 2026 à partir de `docs/notes/matiere-premiere-auto-conception-v1/releve-mecanismes-v1.json` (relevé par mécanisme, vingt et un lots corrigés selon `contre-lecture-matiere-premiere-v1.md`).\n")
w("## 0. Comment lire cette pièce\n")
w("- **Qui affirme quoi.** Chaque mécanisme est ce qu'*affirment les auteurs* de chaque travail, d'après la notice, le résumé, la page ou la lecture approfondie du dépôt selon la « lecture » indiquée. Rien n'est vérifié par nous : aucun chiffre n'est opposable avant lecture sur PDF empreinté, page citée (R7).")
for k in ["oui, mesuré", "oui, affirmé", "non", "inconnu"]:
    w(f"- **Éprouvé contre le réel : « {k} »** — {rel['legende'][k]}.")
w(f"- **Lecture** — {rel['legende']['profondeur de lecture']}.")
w(f"- **Suggéré par le titre** — {rel['legende']['suggéré par le titre']}. Ils sont en section 6.")
w(f"- **Absence** — {rel['legende']['absence']}. Une absence dans cette pièce veut seulement dire : non trouvé dans ce moissonnage, à la profondeur de lecture indiquée.")
w("- **Identifiants.** « 593.3 » veut dire : quatrième mécanisme (position 3) du travail d'indice 593 de la table fusionnée. Le relevé donne, pour chaque identifiant, la phrase complète du mécanisme et sa source (chemin et empreinte sha256) : `releve-mecanismes-v1.json`. Les regroupements de cette pièce sont des rapprochements de lecture du relevé ; un travail peut y figurer sous plusieurs regroupements.")
w("- **Regroupement.** Les mécanismes décrits sont regroupés par ressemblance de ce qu'ils font. Le regroupement est un choix de lecture, rejouable par `programmes/ecrire_matiere_v1.py` ; il n'est pas une classification des auteurs.\n")
w("### Comptes\n")
w(f"- {c['travaux']} travaux ; {c['travaux_avec_au_moins_un_mecanisme']} portent au moins un mécanisme ; {sum(c['travaux_par_statut_sans_mecanisme'].values())} n'en portent aucun : {', '.join(f'{v} « {k} »' for k, v in c['travaux_par_statut_sans_mecanisme'].items())} (section 8).")
w(f"- {c['mecanismes_total']} mécanismes au total, dont **{c['mecanismes_decrits']} décrits** et **{c['mecanismes_suggeres_par_le_titre']} suggérés par le titre** (comptés à part, jamais additionnés).")
w("- Mécanismes décrits par famille : " + " ; ".join(f"{k} {v}" for k, v in c["decrits_par_famille"].items()) + ".")
w("- Mécanismes décrits par éprouvé contre le réel (selon les auteurs) : " + " ; ".join(f"{k} {v}" for k, v in c["decrits_par_eprouve"].items()) + ".")
w("- Travaux par lecture : " + " ; ".join(f"{k} {v}" for k, v in c["travaux_par_profondeur"].items()) + ".")
w("- Trois travaux de la dernière tranche (indices 605, 612, 625) ont une lecture approfondie au dépôt qui n'a pas été ouverte pour cette pièce : ils sont relevés d'après l'entrée de la table seulement.\n")

# --- A : par famille --------------------------------------------------------------------------------
w("## 1. Mécanismes distincts, par famille\n")
w("Format d'une ligne : *titre (date) — adresse · identifiant(s) du mécanisme · éprouvé contre le réel selon les auteurs · lecture · « machine » si le travail est l'un des systèmes de la section 2.*\n")
STAT = {}
for fam in FAM8:
    w(f"### Famille « {fam} »\n")
    for n, cl in enumerate(CL[fam], 1):
        ids = cl["ids"]
        par_travail = collections.OrderedDict()
        for i in sorted(ids, key=lambda s: (int(s.split('.')[0]), int(s.split('.')[1]))):
            e, m = M[i]
            par_travail.setdefault(e["indice"], []).append((i, m))
        ep = collections.Counter(M[i][1]["eprouve_contre_le_reel"] for i in ids)
        pr = collections.Counter(T[k]["profondeur_de_lecture"] for k in par_travail)
        nm = sum(1 for k in par_travail if k in MACH)
        STAT[(fam, n)] = dict(nom=cl["nom"], n_trav=len(par_travail), n_mec=len(ids), n_mach=nm, ep=ep, hors=[k for k in par_travail if k not in MACH],
                              mesures=ep["oui, mesuré"])
        w(f"**{fam} n° {n} — {cl['nom']}**\n")
        w(f"{len(ids)} mécanismes, {len(par_travail)} travaux ({nm} sous forme de machine, section 2). Éprouvé contre le réel selon les auteurs : "
          + ", ".join(f"{k} {ep[k]}" for k in ["oui, mesuré", "oui, affirmé", "non", "inconnu"] if ep[k])
          + ". Lecture : " + ", ".join(f"{PROF[k]} {pr[k]}" for k in PROF if pr[k]) + ".\n")
        for k, lst in par_travail.items():
            e = T[k]
            etiq = sorted({m["eprouve_contre_le_reel"] for _, m in lst})
            w(f"- {lib(e)} · {', '.join(i for i, _ in lst)} · {' / '.join(etiq)} · {PROF[e['profondeur_de_lecture']]}" + (" · machine" if k in MACH else ""))
        w("")

# --- B : machines -----------------------------------------------------------------------------------
w("## 2. Machines : systèmes complets et les mécanismes qu'ils assemblent\n")
w("« Machine » veut dire ici : un système ou une boucle complète décrit comme tel par ses auteurs (ou par le dépôt de code), qui assemble au moins deux mécanismes du relevé. La liste est celle du relevé d'après le titre et la nature du travail ; elle n'est pas exhaustive (R8). Pour chaque machine : les mécanismes qu'elle assemble, avec le regroupement où chacun se range (section 1).\n")
def ecrire_machine(k):
    e = T[k]
    items = [m for m in e["mecanismes"] if m["id"] in CLEF]
    if len(items) < 1:
        return False
    parts = []
    for m in items:
        fam, n, nom = CLEF[m["id"]]
        parts.append(f"{fam} n° {n} ({court(nom)}) [{m['id']}, {m['eprouve_contre_le_reel']}]")
    w(f"- **{e['titre']}** ({e['date']}) — {e['adresse']} — lecture : {PROF[e['profondeur_de_lecture']]}\n  - assemble : " + " ; ".join(parts))
    return True
w("### 2.1 Machines relevées d'après une lecture approfondie du dépôt\n")
for k in MACH_LUES:
    ecrire_machine(k)
w("\nAutres études lues en profondeur, qui ne sont pas des machines mais des protocoles d'étude (leurs mécanismes sont en section 1) : indices 98, 450, 456 et 581. L'indice 136, dont les pages 1 à 4 du PDF ont été relues pour le relevé, figure en 2.2 faute de fiche de lecture approfondie au dépôt.\n")
w("### 2.2 Machines relevées d'après la notice, le résumé ou la page (non opposable, R7)\n")
nmach = 0
for k in MACH_NOTICE:
    if ecrire_machine(k):
        nmach += 1
w("")

# --- C : hors de toute machine ------------------------------------------------------------------------
w("## 3. Mécanismes hors de toute machine\n")
w("Idées de méthode publiées (adresses et lecture : section 1, au même regroupement) dont le relevé ne trouve l'assemblage dans aucun des systèmes recensés en section 2. « Hors de toute machine » ne dit pas « inédit » : cela dit que, dans ce moissonnage, le travail qui porte le mécanisme n'est pas l'un des systèmes de la section 2 ; le mécanisme peut figurer dans un système non recensé (R8).\n")
w("### 3.1 Regroupements dont aucun travail n'est une machine recensée\n")
n_hors = 0
for fam in FAM8:
    for n, cl in enumerate(CL[fam], 1):
        s = STAT[(fam, n)]
        if s["n_mach"] == 0:
            n_hors += 1
            w(f"**{fam} n° {n} — {cl['nom']}** ({s['n_trav']} travaux ; éprouvé selon les auteurs : " + ", ".join(f"{k} {s['ep'][k]}" for k in ["oui, mesuré", "oui, affirmé", "non", "inconnu"] if s['ep'][k]) + ")\n")
            for k in s["hors"]:
                ids = [i for i in cl["ids"] if int(i.split('.')[0]) == k]
                w(f"- {T[k]['titre']} ({T[k]['date']}) · {', '.join(ids)}")
            w("")
w("### 3.2 Regroupements portés à la fois par des machines et par d'autres travaux\n")
w("Pour chacun : nombre de travaux hors machine (liste complète en section 1, sans la marque « machine »).\n")
for fam in FAM8:
    for n, cl in enumerate(CL[fam], 1):
        s = STAT[(fam, n)]
        if s["n_mach"] > 0:
            w(f"- {fam} n° {n} — {court(cl['nom'])} : {s['n_mach']} travaux sous forme de machine, {len(s['hors'])} hors machine ({', '.join(str(k) for k in s['hors']) or 'aucun'})")
w("")
print("regroupements sans machine :", n_hors)

# --- D : ce que l'organisme fait déjà --------------------------------------------------------------------
D = ["decision-N-044-v1.md", "decision-N-045-v2.md", "decision-N-049-v1.md", "decision-N-050-v1.md", "decision-N-053-v1.md", "decision-N-058-v1.md",
     "decision-N-064-v1.md", "decision-N-065-v1.md", "decision-N-067-v1.md", "decision-resserrement-juge-au-nul-v1.md",
     "decision-N-073-revendications-apres-veille-exploration-idees-v1.md"]
w("## 4. Ce que l'organisme actuel fait déjà\n")
w("**Cette section est remplie d'après les décisions de Lazar nommées ci-dessous, et d'elles seules** : elle dit ce que ces décisions retiennent ou interdisent, non ce que le code ou les courses ont réalisé. Plusieurs énoncés valent « à partir de l'étape 2 » ou « sur devis » ; une décision qui retient un énoncé n'est pas une mesure faite. Pièces lues, avec empreinte :\n")
for d in D:
    p = f"docs/decisions/{d}"
    w(f"- `{p}` — sha256 `{sha(p)}`")
w("")
w("### 4.1 Ce que les décisions disent que l'organisme est ou fait\n")
w("- **Un organisme qui se conçoit seul** sur un vivier de tâches à vérité connue, avec le droit de se réécrire ; sa méta-architecture est ensuite figée, et il répond à des questions nouvelles sans réentraînement ni réorganisation (N-044, énoncé 1). L'universalité se mesure sur des familles jamais vues à la conception, non sur des items inédits des familles de conception — **distinction que N-073 interdit de présenter comme nôtre** (section 4.3).")
w("- **Trois régimes de budget** (conception, usage, re-conception) : proposés à Lazar, en attente de son mot pour l'étape 1 (N-044, énoncé 2) ; **vivier de conception** à part de la banque scellée, identifiants disjoints du test et du test final (énoncé 3) ; le vivier existe en code dans le noyau de l'étape 1 (N-049, § 1) ; **questions ouvertes** posées aux organismes avant tout matériau, réponses archivées comme matière et jamais comme consigne (énoncé 4).")
w("- **Diversité des candidats** : trois bras à l'étape 2 (mission avec miroir fonctionnel ; contrainte câblée ; rien), le juge étant la seule pression ; un résultat négatif se publie (N-044, énoncé 5).")
w("- **Composition apprise** : nombre de parties, rôles, modèle par rôle (modèle de frontière ou instrument local entraîné), ordre des échanges, règle d'agrégation, mémoire transmise, part de budget (N-045 v2, énoncé 1) ; **coût dans le signal** rendu à l'organisme à côté de l'exactitude, score net gelé au préenregistrement (énoncé 2) ; **nécessité de la frontière mesurée** comme sortie, par rôle (énoncé 3) ; **voies bon marché avant la voie chère** : éliminations successives, matrices en cache, substituts à 8 milliards, affinage sur réponses filtrées ou préférences hors ligne, modèle de substitution du score, transitions depuis un tampon de rejeu, récompense dense par génération, distillation du concepteur figé (énoncé 4) ; **héritage d'une génération récompensé**, signal sur K générations avec K au moins 3 (énoncé 5 — lettre resserrée par N-073) ; **deux expériences bon marché** avant tout concepteur entraîné : pilote de bruit puis « poids contre archive » (énoncé 6) ; **espaces de conception égaux** entre concepteur contraint et libre (énoncé 7). Inchangé : les modèles de frontière ne sont jamais entraînés, la vérité du test caché ne nourrit ni l'organisme ni un concepteur (énoncé 8). Ces énoncés valent à partir de l'étape 2 ; pour les courses actuelles, l'historique servi contient déjà toutes les générations passées.")
w("- **Tâches fraîches** : à chaque génération, la part de test tirée dans un vivier plutôt que servie fixe ; banque sœur construite d'avance par quelqu'un qui n'a lu aucun score, lue une seule fois ; confirmation sur la banque scellée, famille tenue à l'écart (N-049 ; la construction de la banque sœur est une dépense sur devis, non décidée). **Part de test final lue une seule fois, à la fin de la boucle** (N-050).")
w("- **Composition des proposeurs jugée sur l'oracle du monde planté et sur le coût mesuré, seuls** ; le verdict du juge, aveugle à l'identité du proposeur, n'entre pas dans ce choix (N-058, point 1) ; l'invariant « aucun score de moniteur ni de juge dans l'entraînement ou la sélection de l'agent » vaut aussi pour l'organisme (N-053, point 5 ; N-065, point 4). La sélection des fiches par la sévérité du test survécu reste permise (N-058).")
w("- **Juge statistique** : statistique calculée par l'orchestrateur hors de tout agent, à partir d'un engagement scellé avant que les données existent, contre un nul formé des lois connues (l'archive), avec contrôle des comparaisons multiples (N-064) ; après N-067, **ne reste revendiqué en propre que le nul formé des lois déjà connues** (O2 resserrée, O4 seul porteur de la revendication du juge) ; après N-071, ce nul d'archive est occupé dans ses deux moitiés séparément, **seule leur réunion reste revendicable** (nul formé de l'archive entière et croissante, mis en commun et ajusté avant le gel, dans une règle de promotion à garantie valide à tout instant, sur prédictions scellées, hors des agents), et « lois prédictives et non rendements » n'est plus présenté comme une différence nette.")
w("- **Place dans le programme** : l'organisme est un second terrain du papier C (juges de la recherche automatisée), et un atelier d'idées du programme : ses fiches sont du matériau, jamais une preuve ; tout usage décisif passe par un préenregistrement scellé (N-065, rôles 1 et 2). Le banc de tricheurs et l'attaque de Goodhart du juge (revendications O11 et O12 de N-064 et N-067) relèvent d'une famille exclue de lecture de contenu pour cette pièce : **exclue** ; voir `docs/decisions/decision-N-064-v1.md` et `docs/decisions/decision-N-067-v1.md`.")
w("")
w("### 4.2 Ce que les décisions retirent de ce qui était revendiqué comme propre (N-064, N-067, N-071)\n")
w("Plus revendiqués comme propres : le recours aux e-valeurs et à un seuil posé hors des agents ; la statistique calculée hors des agents ; l'engagement scellé par empreinte ; le contrôle des comparaisons multiples ; le principe d'architecture « séparer qui propose de qui juge » (O1) ; le sceau par empreinte (O3) ; le gel avant lecture et l'interdit du repli silencieux comme idées (O17) ; le banc de tricheurs comme idée (O11) — publiés dans leur principe ou occupés en partie, citations obligatoires dans tout texte qui présente l'organisme : POPPER, Dwork et al., Blum et Hardt (« The Ladder »), Co-Scientist, et les pièces nommées par N-067 et N-071.\n")
w("### 4.3 Ce que N-073 interdit désormais de présenter comme nôtre\n")
w("Lettre de `docs/decisions/decision-N-073-revendications-apres-veille-exploration-idees-v1.md` (version de travail, contre-lecture à venir selon son texte) :\n")
w("1. **Héritage d'une génération récompensé** (N-045 v2, énoncé 5) : principe occupé par la machine de Huxley-Gödel (Wang et al., arXiv 2510.21614). Ne plus écrire comme idée ou constat du programme : « récompenser l'héritage d'une génération » ; « créditer un agent par les résultats de sa descendance » ; « le score immédiat est un mauvais guide du potentiel à long terme » ; « un signal sur plusieurs générations, tronqué à K et actualisé » présenté comme une idée ; « faire compter dans le mérite d'une génération ce qu'elle construit et qui ne sert qu'aux suivantes » ; « servir tout l'historique au concepteur ». La lettre retenue cite Wang et al. (2025), Schmidhuber et Zhao (1996, 1997 — à lire sur source avant de les citer), Sutton et Barto. Restent décrits sans être dits nouveaux ni propres : les objets (mémoire transmise, sondes et adaptateurs servis à la génération suivante), le concepteur entraîné avec le coût dans le signal, la question causale « l'archive héritée cause-t-elle les découvertes ? ». Indice contraire à dire avec la prémisse : chez Qin et al. (arXiv 2611.05108), ce qui est légué rapporte surtout au départ.")
w("2. **« Le séquentiel doit battre le meilleur de N tirages, à budget égal »** (N-045 v2, énoncés 4 et 6) : protocole occupé (Oved et al., arXiv 2610.23977 ; compagnon arXiv 2609.19799), issue occupée en partie ; les gardes de la porte (familles tenues à l'écart, témoin « un modèle, vote à k ») sont très probablement prises aussi, d'après des notices seulement. La porte reste une condition du programme, présentée comme **pratique publiée, citée**.")
w("3. **« Familles inédites contre items inédits des familles vues »** (N-044) : distinction faite en mots propres par Srikanth et al. (arXiv 2609.26457, p. 6) ; elle se cite. Ce qui se décrit comme mise en œuvre, sans priorité : la mesure par famille préenregistrée.")
w("4. **Banque sœur** (N-049) : elle sépare « adapté aux textes » de « adapté à la famille telle que ce générateur la rend », non de « adapté au générateur » (Zhu et al., « Bad Genius », arXiv 2609.18366, p. 5 : contredit faible) ; le générateur est audité avant toute banque sœur. La lecture unique du lot final est une pratique ancienne, citée.")
w("5. **Proposeurs de plusieurs fournisseurs** (N-045 v2, énoncés 1 à 3 ; N-067) : l'énoncé reste « voisin » ; tout texte qui présente la diversité des fournisseurs cite l'indice contraire de Ferreira, Liu, Zheng (arXiv 2609.35875) avec sa borne de terrain (réponses fermées, petits modèles ouverts), à côté de deux autres déjà au dépôt.")
w("")
w("Les restrictions antérieures (« lois prédictives et non rendements » ; e-valeurs ; calcul hors des agents ; sceau ; etc.) sont en 4.2. Rien dans cette section n'est une déclaration « libre » : « non trouvé dans les pièces lues » ne veut jamais dire « trou du champ » (R8).\n")

# --- E : questions ouvertes -----------------------------------------------------------------------------
w("## 5. Questions ouvertes\n")
w("Ce sont des questions posées par la matière, jamais des affirmations d'absence : chacune dit ce que ce moissonnage montre et ce qu'il ne montre pas. Les comptes viennent du relevé, recalculés par programme.\n")
nul = [(f, n) for (f, n), s in STAT.items() if s["mesures"] == 0]
w(f"1. **Regroupements sans aucun mécanisme marqué « oui, mesuré »** ({len(nul)} sur {len(STAT)}) : " + " ; ".join(f"{f} n° {n} ({court(STAT[(f, n)]['nom'])})" for f, n in nul) + ". Question : ces mécanismes sont-ils éprouvés quelque part hors de ce moissonnage, et sur quelle vérité ?")
tot = {f: sum(STAT[(f, n)]["mesures"] for n in range(1, len(CL[f]) + 1)) for f in FAM8}
w("2. **Éprouvé contre le réel et machines.** Parmi les travaux sous forme de machine (section 2), la part de mécanismes éprouvés « oui, mesuré » est " + 
  f"{sum(1 for k in MACH for m in T[k]['mecanismes'] if m['id'] in CLEF and m['eprouve_contre_le_reel']=='oui, mesuré')} sur {sum(1 for k in MACH for m in T[k]['mecanismes'] if m['id'] in CLEF)} (selon les auteurs). Question : quels mécanismes d'une machine sont isolés par une ablation, et lesquels ne sont éprouvés qu'ensemble ? (Le relevé note plusieurs cas d'absence d'ablation : indices 112 et 593.)")
w("3. **Largeur et profondeur à budget apparié.** Le regroupement « coût n° 3 » et le regroupement « coût n° 5 » portent les comparaisons à dépense totale égale et les témoins à calcul apparié. Question : quelle part de ces comparaisons distingue le gain d'une architecture du gain d'un calcul d'inférence ajouté, sur des familles de tâches tenues à l'écart ?")
w("4. **Vérité de l'épreuve.** Le relevé range sous « épreuve » des vérités très différentes (monde planté, futur, redécouverte, exécutable, expert). Question : un même mécanisme d'exploration garde-t-il son classement quand on change la vérité de l'épreuve, à coût égal ?")
w("5. **Originalité.** La nouveauté se mesure par distance dans un espace, par antériorité, par juge ou par écart de croyance. Question : ces quatre mesures s'accordent-elles sur les mêmes idées, et laquelle suit un résultat réel obtenu plus tard ?")
w("6. **Diversité.** Le relevé porte des diagnostics d'effondrement et des remèdes dont plusieurs sont notés sans effet par leurs auteurs (exploration n° 12 et n° 15). Question : quels remèdes survivent quand on juge sur l'oracle d'un monde planté et sur le coût plutôt que sur un juge de nouveauté ?")
w("7. **Mémoire.** La mémoire se mesure surtout par comparaison « avec / sans » ; plusieurs mesures du regroupement « mémoire n° 11 » ne trouvent pas de gain constant au résultat final. Question : que lègue réellement une génération à la suivante, au départ, à mi-budget et à l'échéance, une fois l'effet de départ séparé ?")
w("8. **Jugement.** Les juges sont mesurés contre des experts, des issues ou des preuves traçables, et leurs erreurs se corrèlent. Question : quelle composition d'un collège de juges maintient son nombre de votes effectifs au-dessus de deux sur des idées de recherche ?")
w("9. **Auto-conception.** Les systèmes qui se réécrivent sont presque tous éprouvés sur des bancs de code ou d'ingénierie. Question : que devient une auto-modification sélectionnée quand la famille de tâches de la mesure est inédite à la conception ?")
w("10. **Entrées lues sur notice seule.** {} travaux ne sont lus que par le titre ou une courte description ; leurs mécanismes (section 6) sont des hypothèses de lecture. Question : lesquels, lus sur PDF, tiennent ?".format(c["travaux_par_profondeur"]["notice seule"]))
w("11. **Limites du moissonnage.** Une seconde passe de recherche, limitée à la périphérie du juge (finance empirique, découverte de modèles, billets de laboratoire), est accordée par N-073 (§ 7) après le 22 novembre 2026 ; les voisins nommés par N-073 à lire sur PDF ne le sont pas encore. Les lectures approfondies des travaux d'indices 605, 612 et 625 n'ont pas été ouvertes pour cette pièce.")
w("")

# --- F : suggérés par le titre ---------------------------------------------------------------------------
w("## 6. Mécanismes suggérés par le titre (comptés à part)\n")
w(f"{c['mecanismes_suggeres_par_le_titre']} mécanismes dont la phrase du relevé dit qu'ils sont inférés du seul titre ou d'après le titre. Ce sont des hypothèses de lecture : ni description des auteurs, ni mesure. Par famille : " + " ; ".join(f"{k} {v}" for k, v in c["suggeres_par_famille"].items()) + ".\n")
for fam in FAM8 + ["autre"]:
    lst = [(e, m) for e in rel["travaux"] for m in e["mecanismes"] if m["suggere_par_le_titre"] and m["famille"] == fam]
    if not lst:
        continue
    w(f"### {fam} ({len(lst)})\n")
    for e, m in lst:
        w(f"- {lib(e)} — {m['id']} — {m['eprouve_contre_le_reel']} — lecture : {PROF[e['profondeur_de_lecture']]} — {m['mecanisme_en_une_phrase']}")
    w("")

# --- G : autre ------------------------------------------------------------------------------------------------
w("## 7. Mécanismes classés « autre » : reclassés ou justifiés\n")
w("Quarante mécanismes étaient classés « autre » dans les lots. Neuf ont été reclassés dans une des huit familles, un a été retiré (cloisonnement), trente sont conservés avec la justification ci-dessous (table `programmes/corrections-v1.json`, correction 4 de la contre-lecture). Les mécanismes « autre » suggérés par le titre sont en section 6.\n")
for e in rel["travaux"]:
    for m in e["mecanismes"]:
        if m["famille"] == "autre" and not m["suggere_par_le_titre"]:
            w(f"- {lib(e)} — {m['id']} — {m['eprouve_contre_le_reel']} — lecture : {PROF[e['profondeur_de_lecture']]} — {m['mecanisme_en_une_phrase']} — *{m['justification_autre']}*")
w("")

# --- H : sans mécanisme ----------------------------------------------------------------------------------------
w("## 8. Travaux sans mécanisme relevé\n")
w("Pour chacun, le statut dit pourquoi. Les travaux « exclue » relèvent de familles exclues de toute lecture de contenu pour cette pièce : seuls l'indice, le statut et le chemin sont donnés.\n")
for e in rel["travaux"]:
    if not e["mecanismes"]:
        st = e.get("statut", "?")
        if st == "exclue":
            w(f"- indice {e['indice']} — exclue — chemin : `docs/notes/veille-exploration-idees-v1/table-fusionnee-v1.json`, travaux[{e['indice']}]")
        else:
            w(f"- indice {e['indice']} — {st} — {lib(e)}")
w("")
w("## 9. Retraits et pièces\n")
w("- Retraits : " + " ; ".join(f"indice {r['indice']} (correction {r['correction']})" for r in rel["retraits"]) + " — lignes retirées du relevé parce qu'elles reprenaient une facette d'une famille exclue ; leur contenu n'est pas reproduit.")
for p in ["releve-mecanismes-v1.json", "programmes/corrections-v1.json", "programmes/fusionner_v1.py"]:
    w(f"- `docs/notes/matiere-premiere-auto-conception-v1/{p}` — sha256 `{sha('docs/notes/matiere-premiere-auto-conception-v1/' + p)}`")
Path("matiere-premiere-v1.md").write_text("\n".join(out) + "\n", encoding="utf-8")
print("écrit matiere-premiere-v1.md :", len(out), "lignes,", sum(len(x) for x in out), "caractères")
