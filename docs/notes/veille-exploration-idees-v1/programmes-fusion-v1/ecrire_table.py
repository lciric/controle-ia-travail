#!/usr/bin/env python3
"""Ecrit la table fusionnee (Markdown) a partir de fusion.json et couverture.json.

Usage : python -I ecrire_table.py fusion.json couverture.json DOSSIER_NOTES SORTIE.md
"""
import hashlib
import json
import re
import sys
from collections import Counter
from pathlib import Path

fusion = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
couv = json.loads(Path(sys.argv[2]).read_text(encoding="utf-8"))
dossier = Path(sys.argv[3])
sortie = Path(sys.argv[4])
T = fusion["travaux"]
ORDRE = ["mots-cles", "citations", "grise", "adverse"]
NOM = {"mots-cles": "mots-clés", "citations": "citations", "grise": "grise", "adverse": "adverse"}
ANN = [t for t in T if t["voies"]]
ANX = [t for t in T if not t["voies"]]


def fr(x, nd=0):
    """Nombre a la francaise (virgule decimale)."""
    return (f"{x:.{nd}f}").replace(".", ",")


def couvre(n, N):
    if N < n:
        return "estimation inférieure à ce qui a été vu : paire non crédible"
    return f"{100 * n / N:.0f} %"


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def par_cle(k):
    r = [t for t in T if k in t["cles"]]
    assert len(r) == 1, (k, len(r))
    return r[0]


def voies_txt(t):
    v = [NOM[x] for x in t["voies"]]
    if t["annexe_mots_cles"] and "mots-cles" not in t["voies"]:
        v.append("mots-clés (annexe de titres)")
    return ", ".join(v)


def lien(t):
    a = t["adresse"]
    if t["arxiv"] and "arxiv.org" in a:
        return f"[arXiv {t['arxiv'][0]}]({a})"
    return a


def cle_date(s):
    if not s:
        return (0, 0, 0)
    p = s.split("-")
    return (int(p[0]), int(p[1]) if len(p) > 1 else 0, int(p[2]) if len(p) > 2 else 0)


def remarques(t):
    r = []
    if t["dates_divergentes"]:
        r.append("dates relevées : " + t["dates_divergentes"])
    elif t["dates_brutes"]:
        r.append("date telle que rendue — " + t["dates_brutes"])
    if t["autres_adresses"]:
        r.append("autres adresses : " + " ; ".join(t["autres_adresses"]))
    if t["autres_titres"]:
        r.append("autres titres : " + " ; ".join("« " + x + " »" for x in t["autres_titres"]))
    if t["eclate"]:
        r.append("tiré d'une rangée groupée (" + ", ".join(t["eclate"]) + ")")
    return " — ".join(r) if r else ""


L = []
w = L.append
n4 = [t for t in ANN if len(t["voies"]) == 4]
n3 = [t for t in ANN if len(t["voies"]) == 3]
n2 = [t for t in ANN if len(t["voies"]) == 2]
n1 = [t for t in ANN if len(t["voies"]) == 1]
lu = Counter(re.sub(r" \(.*", "", t["lu"]) for t in ANN)
S = {s["nom"][0]: s for s in couv["strates"]}
A, B, C, D, Eh, F, G = (S[x] for x in "ABCDEFG")

w("# Veille « exploration d'idées nouvelles par les modèles de langue » — table fusionnée des quatre voies et mesure de leur couverture — v1")
w("")
w("- **Date** : 18 novembre 2026. **Auteur** : sous-agent de fusion, qui n'a mené aucune des quatre recherches. Aucun commit, aucune dépense, aucun résultat sous embargo ouvert, rien écrit dans `registres/`.")
w("- **Objet** : fusionner les listes rendues par quatre recherches menées à l'aveugle les unes des autres (voie « mots-clés et listes », voie « graphe de citations », voie « littérature grise et code », voie « adverse », celle qui cherche ce qui prend ou contredit les revendications du programme), mesurer ce qu'elles couvrent, et désigner au plus douze travaux à lire sur source.")
w("- **Pièces lues, avec leur empreinte SHA-256** (tableaux extraits par programme, lecture seule) :")
for f in ["recherche-mots-cles-v1.md", "recherche-citations-v2.md", "recherche-litterature-grise-v1.md", "recherche-adverse-v1.md", "revendications-v1.md"]:
    w(f"  - `docs/notes/veille-exploration-idees-v1/{f}` — `{sha(dossier / f)}`")
w("- **Statut des chiffres (R7 : aucun chiffre de la littérature n'est opposable sans source empreintée et page citée)** : je n'ai lu aucun des travaux listés. Tout chiffre de la colonne « ce qu'il fait » est recopié de la voie nommée entre crochets, avec la mention de source que cette voie lui a donnée (résumé, page web, « PDF, p. … ») ; aucun n'est opposable par cette table. Les seuls chiffres qui sont les miens sont les comptes de recoupement et les estimations de la section 3, calculés par programme sur les tableaux des quatre notes.")
w("- **Statut des zones (R8 : une zone vierge est une question, pas un trou du champ)** : « non trouvé » veut dire « non trouvé par ces quatre voies ». La section 3 chiffre à peu près combien de travaux du même genre elles n'ont pas vus.")
w("- **Colonne « touche »** : rapprochements proposés par chaque voie, recopiés tels quels et séparés par « ‖ » ; la voie adverse numérote les revendications comme `revendications-v1.md` (elle n'en a reçu que les points 1 à 12). Ce sont des pistes de lecture, jamais des constats de collision.")
w("- **Consignes dans les documents** : je n'ai ouvert aucun document téléchargé ; les quatre notes ne contiennent aucune consigne adressée au lecteur.")
w("")
w("## 1. Ce qui a été fusionné, et comment")
w("")
w(f"- **Entrées lues** : 268 de la voie mots-clés (258 articles arXiv annotés et 10 hors arXiv), 195 de la voie citations, 177 de la voie grise, 145 de la voie adverse — 785 entrées annotées — plus les 126 titres de l'annexe mécanique de la voie mots-clés (titres retenus par un filtre de mots, non lus, pertinence non confirmée).")
w(f"- **Après dédoublonnage : {len(ANN)} travaux distincts annotés par au moins une voie**, dont {len(n4)} trouvés par les quatre voies, {len(n3)} par trois, {len(n2)} par deux et {len(n1)} par une seule. S'y ajoutent {len(ANX)} titres qui ne figurent que dans l'annexe mécanique (section 6) ; {sum(1 for t in ANN if t['annexe_mots_cles'])} titres de cette annexe ont été retrouvés et annotés par une autre voie.")
w(f"- **Profondeur de lecture la meilleure, toutes voies confondues** : {lu.get('texte entier', 0)} travaux lus en texte entier (corps principal), {lu.get('résumé ou page', 0)} au résumé ou sur quelques pages, {lu.get('titre seul', 0)} au titre seul. La fusion n'ajoute aucune lecture.")
w("- **Règles de rapprochement** (programme `programmes-fusion-v1/fusionner.py`, déposé à côté de cette table avec les autres ; données de la table en `table-fusionnee-v1.json`) : deux entrées désignent le même travail si elles partagent un identifiant arXiv (pris dans l'adresse, ou dans le titre quand l'adresse n'est pas arXiv — c'est ainsi qu'un dépôt de code ou un billet qui nomme son article lui est rattaché), une adresse normalisée (billets LessWrong et GreaterWrong rapprochés par l'identifiant du billet ; document de travail du NBER rapproché de son DOI), ou un titre identique une fois retirés la casse, la ponctuation et les mentions de lieu entre crochets. Les paires de titres proches sans clé commune ont été listées par programme (rapport de similarité d'au moins 0,80 entre tous les groupes, d'au moins 0,55 quand l'un des deux n'a pas d'identifiant arXiv) et tranchées à la main ; celles que j'ai jugées être le même travail sont les fusions manuelles ci-dessous.")
w("- **Chaîne de programmes** (tous lancés avec l'option d'isolement `-I` de Python, lecture seule des notes) : `extraire.py` (tableaux des quatre notes vers une liste d'entrées) ; `candidats.py` et `candidats2.py` (paires de titres proches à trancher) ; `fusionner.py` (clés, règles manuelles, table) ; `couverture.py` (section 3) ; `ecrire_table.py` (ce fichier).")
w("- **Fusions manuelles** :")
for a, b, surete, raison in fusion["fusions_manuelles"]:
    w(f"  - `{a}` = `{b}` — {surete} : {raison}.")
w(f"- **Rangées groupées de la voie grise éclatées** : la rangée « autres articles arXiv croisés en chemin » (onze identifiants, comptés chacun comme trouvé au titre seul par la voie grise ; « RSI-top » et « LMCA », non identifiables, sont laissés de côté) ; la rangée des dépôts de Sakana pour « The AI Scientist » et sa version 2 (rattachés aux deux articles arXiv) ; la rangée « ShinkaEvolve ; alphaevolve » (le second rattaché à l'article AlphaEvolve). C'est pourquoi la voie grise compte {A['tailles']['grise']} travaux distincts pour 177 rangées. Deux autres rangées groupées de dépôts (cinq cadres d'agents ; deux bancs et une liste) restent une ligne chacune.")
w("- **Rapprochements possibles laissés séparés** (à vérifier, ils changeraient les comptes d'une unité) :")
for a, b, raison in fusion["possibles"]:
    w(f"  - {raison}.")
w("- **Date retenue** : la plus ancienne date relevée par une voie (champ `published` d'arXiv, date de soumission OpenReview, date du billet) ; quand les voies divergent, toutes les dates sont dans la colonne « remarques ». Aucune n'a été revérifiée sur la page d'origine. Cinq dates arXiv sont signalées douteuses par la voie citations (mois de l'identifiant postérieur au champ `published` : 2607.14118, 2609.15996, 2609.29636, 2610.32986, 2611.14539).")
w("- **« Mesuré ou affirmé »** : la mention la plus informative parmi les voies ; « avec données publiées » veut dire qu'une voie a repéré l'annonce d'un dépôt, non que le dépôt a été ouvert. Les désaccords entre voies sont écrits dans la cellule.")
w("")

# ---------------------------------------------------------------- temoins
w("## 2. Rappel sur les huit travaux témoins")
w("")
w("Huit travaux connus de la session mère n'avaient été donnés à aucune voie. Identifiants pris dans le dépôt (`docs/notes/lecture-o4-englobement-v1.md` pour EvoSCM, ModelSMC et BEYOND ; `docs/notes/veille-spaceship-ram-v1/` pour le billet de Meta), recherchés dans les quatre notes par identifiant arXiv, par adresse et par titre, tableaux et texte compris.")
w("")
w("| témoin | identifiant | mots-clés | citations | grise | adverse | retrouvé ? |")
w("|---|---|---|---|---|---|---|")
temoins = [
    ("« Re-Search: Dissecting LLM Ideation Through a Two-Player Questioning Game »", "arXiv 2611.14487", "arxiv:2611.14487"),
    ("« Fork-and-Flush: Escaping Idea Basins in Autoresearch Agents »", "arXiv 2610.07447", "arxiv:2610.07447"),
    ("« Scaling Discovery Requires Forgetting » (Tan et al.)", "arXiv 2610.20563", "arxiv:2610.20563"),
    ("« How models explore ideas » (Bespoke Labs, banc AutoResearchExam)", "bespokelabs.ai/blog/how-models-explore-ideas", "url:bespokelabs.ai/blog/how-models-explore-ideas"),
    ("« Self-Improving Memory » (équipe RAM de Meta, billet)", "facebookresearch.github.io/RAM/blogs/self_improving_memory", None),
    ("EvoSCM", "arXiv 2609.01526", "arxiv:2609.01526"),
    ("ModelSMC (Wahl et al., « A Probabilistic Framework for LLM-Based Model Discovery »)", "arXiv 2602.18266", "arxiv:2602.18266"),
    ("BEYOND (Huang et Fan, « Beyond Prompting »)", "arXiv 2603.14288", "arxiv:2603.14288"),
]
trouves = 0
par_voie = Counter()
for nom, ident, k in temoins:
    r = [t for t in T if k and k in t["cles"]]
    v = set(r[0]["voies"]) if r else set()
    for x in v:
        par_voie[x] += 1
    trouves += bool(v)
    cells = ["oui" if x in v else "non" for x in ORDRE]
    w(f"| {nom} | {ident} | " + " | ".join(cells) + f" | {'oui, ' + str(len(v)) + (' voies' if len(v) > 1 else ' voie') if v else '**non**'} |")
w("")
w(f"- **Taux : {trouves} sur 8 ({fr(100 * trouves / 8, 1)} %)** pour l'union des quatre voies ; intervalle de Wilson à 95 % : 31 % à 86 %. Par voie : mots-clés {par_voie['mots-cles']} sur 8, citations {par_voie['citations']} sur 8, grise {par_voie['grise']} sur 8, adverse {par_voie['adverse']} sur 8.")
w("- **Nuances sur les « oui »** : la voie grise n'a « Re-Search » qu'au titre (fiche OpenReview) et « Scaling Discovery Requires Forgetting » qu'au titre (condensé d'un moteur de recherche) ; la voie citations a trouvé le travail de Wahl et al. sous son titre d'article, en suivant qui cite « Large Language Bayes » et « AutoDiscovery », sans le nom « ModelSMC » ; « How models explore ideas » n'a été trouvé que par la voie grise, qui l'a lu en entier. Aucun des trois témoins manqués n'apparaît non plus dans l'annexe mécanique de titres.")
w("- **Ce que vaut ce taux — peu.** Huit témoins donnent un intervalle qui va du tiers aux six septièmes : il ne distingue pas une couverture médiocre d'une bonne. Les témoins ne sont pas tirés au hasard : quatre sont les travaux de tête du sujet (bassins d'idées, exploration), tous retrouvés, trois par trois voies ou plus ; trois sont les voisins du juge au nul formé des lois connues, venus de la finance empirique et de la découverte de modèles (EvoSCM, ModelSMC, BEYOND), et **un seul sur trois est retrouvé** ; le huitième est un billet de laboratoire récent sans article (mémoire auto-améliorée de Meta), manqué. La lecture franche : le cœur du sujet est bien couvert, sa périphérie — là où vit la seule pièce encore revendiquée du juge — l'est mal, et les billets sans article passent à travers. Par strate, pour ce que valent des effectifs de deux à quatre : articles arXiv de la fenêtre, 3 sur 4 ; articles arXiv antérieurs à mai 2026, 1 sur 2 ; hors arXiv, 1 sur 2.")
w("")

# ---------------------------------------------------------------- estimation
w("## 3. Estimation de ce qui manque, par recoupement des voies (capture-recapture)")
w("")
w(f"Programme `programmes-fusion-v1/couverture.py` (sorties complètes en `couverture-v1.json`), graine `numpy.random.SeedSequence({couv['graine']})` pour le rééchantillonnage. Trois estimateurs : **Chapman** sur chaque paire de voies (variance de Seber, intervalle log-normal sur le non-vu) ; **borne inférieure de Chao** (1987, forme corrigée du biais), qui n'utilise que le nombre de travaux vus une fois et deux fois ; **modèles log-linéaires de Poisson à plusieurs listes**, sous indépendance puis avec des dépendances entre paires de voies (le meilleur des 64 jeux de dépendances selon le critère d'Akaike). Les histoires de capture sont écrites dans l'ordre mots-clés, citations, grise, adverse (« 1100 » = trouvé par les deux premières seulement).")
w("")


def tab_strate(s):
    w(f"**{s['nom']}** — {s['n_union']} travaux vus ; tailles : " + ", ".join(f"{NOM.get(k, k)} {v}" for k, v in s["tailles"].items()) + ".")
    w("")
    w("Histoires de capture : " + ", ".join(f"`{h}` {c}" for h, c in s["histoires"].items()) + ".")
    w("")
    w("| estimateur | effectifs | total estimé | intervalle à 95 % | couverture de l'union |")
    w("|---|---|---|---|---|")
    for k, v in s["chapman"].items():
        a, b = k.split(" x ")
        w(f"| Chapman, {NOM.get(a, a)} × {NOM.get(b, b)} | {v['n1']} et {v['n2']} ; en commun : {v['m']} | {fr(v['N'])} | {fr(v['bas'])} à {fr(v['haut'])} | {couvre(s['n_union'], v['N'])} |")
    c = s["chao"]
    w(f"| Chao, borne inférieure | {c['f1']} vus une fois, {c['f2']} vus deux fois | {fr(c['N'])} | {fr(c['bas'])} à {fr(c['haut'])} (rééchantillonnage : {fr(s['chao_reechantillonnage_2000'][0])} à {fr(s['chao_reechantillonnage_2000'][1])}) | au plus {100 * s['n_union'] / c['N']:.0f} % |")
    if "loglineaire" in s:
        l = s["loglineaire"]
        i = l["independance"]
        w(f"| log-linéaire, voies indépendantes | critère d'Akaike {fr(i['aic'], 1)} | {fr(i['N'])} | {fr(i['bas'])} à {fr(i['haut'])} | {100 * s['n_union'] / i['N']:.0f} % |")
        m = l["meilleur_aic"]
        if m["N"] < 1e6:
            w(f"| log-linéaire, dépendances entre paires (meilleur critère d'Akaike : {fr(m['aic'], 1)} ; {len(m['interactions'])} dépendances) | — | {fr(m['N'])} | {fr(m['bas'])} à {fr(m['haut'])} | {100 * s['n_union'] / m['N']:.0f} % |")
        else:
            w("| log-linéaire, dépendances entre paires | — | instable (recoupements trop petits) | — | — |")
    w("")


tab_strate(B)
tab_strate(C)
tab_strate(Eh)
tab_strate(A)
w(f"**Sensibilité à l'annexe mécanique** : si l'on compte les 126 titres non lus de l'annexe comme trouvés par la voie mots-clés, l'union des articles arXiv de la fenêtre passe de {B['n_union']} à {G['n_union']} ; Chapman mots-clés × citations donne {fr(G['chapman']['mots-cles x citations']['N'])} ({fr(G['chapman']['mots-cles x citations']['bas'])} à {fr(G['chapman']['mots-cles x citations']['haut'])}), la borne de Chao {fr(G['chao']['N'])} ({fr(G['chao']['bas'])} à {fr(G['chao']['haut'])}). L'annexe gonfle surtout les travaux vus une seule fois, dont la pertinence n'est pas confirmée : ces chiffres bornent par le haut, ils ne corrigent pas les précédents.")
w("")
bn = B["n_union"]
ch = B["chao"]
ll = B["loglineaire"]["meilleur_aic"]
cmin = B["chapman"]["mots-cles x citations"]
w("### Ce que j'en retiens")
w("")
w(f"- **Articles arXiv de la fenêtre (mai 2026 ou après) : {bn} vus.** Les trois paires qui incluent la voie grise donnent moins que ce qui a été vu ({fr(B['chapman']['citations x grise']['N'])} à {fr(B['chapman']['grise x adverse']['N'])}) : la voie grise n'a d'articles arXiv que ceux qu'elle a croisés en chemin, presque tous déjà dans les autres voies ; ces paires sont sans valeur. Parmi les trois voies tournées vers arXiv, la paire la plus optimiste (mots-clés × citations) donne {fr(cmin['N'])} ({fr(cmin['bas'])} à {fr(cmin['haut'])}) ; les paires avec la voie adverse donnent {fr(B['chapman']['mots-cles x adverse']['N'])} et {fr(B['chapman']['citations x adverse']['N'])} ; la borne inférieure de Chao {fr(ch['N'])} ({fr(ch['bas'])} à {fr(ch['haut'])}) ; le modèle qui admet des dépendances entre voies {fr(ll['N'])} ({fr(ll['bas'])} à {fr(ll['haut'])}). **Fourchette retenue : de 380 à 700 travaux, soit de {380 - bn} à {700 - bn} non vus ; valeur de travail : environ {round(ch['N'] / 5) * 5}, soit environ {round((ch['N'] - bn) / 10) * 10} non vus et une couverture d'environ les deux tiers.** Plus de 700 n'est pas exclu : l'intervalle du modèle à dépendances monte à {fr(ll['haut'])}. L'estimation de {fr(cmin['N'])} n'est pas crédible : les deux voies qui la produisent se ressemblent trop (voir limites). Cette couverture des deux tiers s'accorde avec le rappel sur témoins (5 sur 8 ; 3 sur 4 pour les articles arXiv de la fenêtre), sans que huit témoins puissent la confirmer.")
w(f"- **Hors arXiv (billets, dépôts, soumissions sans identifiant arXiv) : {Eh['n_union']} vus, dont {Eh['histoires'].get('0010', 0)} par la seule voie grise.** Les recoupements vont de zéro à cinq travaux : aucun estimateur n'est fiable (la borne de Chao donne {fr(Eh['chao']['N'])}, avec un intervalle de {fr(Eh['chao']['bas'])} à {fr(Eh['chao']['haut'])}). **Ce qui manque ici n'est pas estimable** ; tout indique que c'est plusieurs fois ce qui a été trouvé. La littérature grise repose sur une seule voie, et cette voie n'a atteint OpenReview que par mots de recherche, sans texte entier.")
w(f"- **Toutes pièces confondues ({A['n_union']} vus)** : les estimations vont de {fr(A['chapman']['mots-cles x citations']['N'])} — moins que ce qui a été vu, donc absurde — à {fr(A['loglineaire']['meilleur_aic']['N'])}. Le mélange de deux populations (articles arXiv, littérature grise) que les voies ne visent pas également rend ce total sans valeur ; je ne le retiens pas.")
w("")
w("### Limites de l'estimation")
w("")
w(f"1. **Les voies ne sont pas indépendantes.** Mots-clés et citations puisent toutes deux dans arXiv, trient toutes deux par un score de mots sur titres et résumés, et trouvent toutes deux d'abord les travaux très cités ou au vocabulaire attendu : leur recoupement est gonflé ({A['chapman']['mots-cles x citations']['m']} communs sur {A['chapman']['mots-cles x citations']['n2']}) et Chapman sous-estime le total. Un travail au titre opaque échappe aux deux à la fois.")
w("2. **Les travaux ne sont pas également trouvables.** Les travaux de tête sont vus par toutes les voies, les obscurs par aucune ; dans ce cas tous les estimateurs sous-estiment, et celui de Chao n'est par construction qu'une borne inférieure.")
w("3. **La voie adverse est orientée.** Elle cherche ce qui prend ou contredit douze revendications ; elle vise donc en partie une autre population (agents qui se réécrivent, tests séquentiels, comparaison à budget égal) que les trois autres. Son faible recoupement vient pour partie de cette différence de cible et non d'un manque : les paires qui l'incluent surestiment le total de la cible commune, mais mesurent correctement que l'union des cibles est plus large que ce qu'une voie seule couvre.")
w("4. **La population n'est pas définie.** « Pertinent » est le jugement de chaque lecteur : la voie mots-clés a annoté 268 notices sur 2 247 moissonnées, la voie citations 195 sur 3 251. L'estimation porte sur « ce qu'un lecteur de ces voies aurait retenu », non sur « tout ce qui touche le programme ».")
w("5. **La fenêtre n'est pas fermée.** L'indexation de Semantic Scholar a du retard : les deux dernières semaines sont sous-représentées dans la voie citations, ce qui ajoute des manquants récents que le recoupement voit mal.")
w("6. **Le dédoublonnage a ses erreurs** : deux fusions « probables » non vérifiées, un rapprochement possible laissé séparé ; l'effet est d'une ou deux unités sur les recoupements.")
w(f"7. **Ce que l'estimation ne dit pas** : rien sur la profondeur. {lu.get('texte entier', 0)} travaux seulement ont été lus en entier ; pour la question « une revendication est-elle prise ? », la lecture manquante pèse plus que les travaux manquants.")
w("")

# ---------------------------------------------------------------- douze
w("## 4. Douze travaux à lire sur source, du plus menaçant au moins menaçant")
w("")
w("Critère : ce qui prend, avoisine de près ou contredit une revendication ou un choix de conception du programme, **et que le dépôt n'a pas encore lu sur source pour cet angle**. Ce qui arrange le programme n'est pas retenu. Les verdicts « prend », « contredit » viennent de résumés ou de quelques pages : ce sont des raisons de lire, pas des faits (R7). Vérification faite dans le dépôt par recherche des identifiants dans `docs/notes/`, `docs/decisions/`, `registres/decisions.md` et `registres/veille.md` (hors de ce dossier de veille) : dix de ces douze travaux n'y figurent nulle part ; « Selecting LLM-Generated Hypotheses… » y est lu sur quatre pages pour un autre angle ; la machine de Huxley-Gödel y est signalée le 18 novembre comme « collision à instruire », au résumé seul.")
w("")
w("| rang | travail | première version relevée | voies | revendications touchées | pourquoi le lire, et quoi y chercher | lu jusqu'ici |")
w("|---|---|---|---|---|---|---|")
DOUZE = [
    ("arxiv:2611.14539", "14 (forme encore revendiquée de l'attaque contre un juge statistique) ; 1 et 2 (règle de promotion)",
     "Un seuil statistique placé dans la boucle de recherche devient un objet contre lequel la recherche optimise ; l'article compare ce que change le fait de montrer la comptabilité du seuil au critique, avec protocole gelé avant lancement. C'est le voisin le plus proche trouvé de la forme encore revendiquée (juge statistique, proposeur qui en lit la description, bras informé et bras non informé). À chercher : y a-t-il un proposeur chargé de tromper, une description du juge donnée en texte, deux bras qui ne diffèrent que par les verdicts rendus. Cité sans développer le contenu de l'attaque. Date à vérifier (identifiant de novembre, champ `published` d'octobre).",
     "p. 1 à 3 du PDF (voie citations)"),
    ("arxiv:2611.04070", "6 (mondes plantés comme arbitre) ; 14 (juge mesuré sur des mondes où toute promotion est fausse) ; 4 (statistique hors des agents, réserve scellée)",
     "Note un agent de recherche comme un test statistique, taille et puissance, dans des mondes simulés à signal planté, mondes sans signal compris ; conclut à une règle de décision fixée hors de l'agent et à une réserve scellée. Prend la justification de l'architecture et une partie de la mesure « mondes négatifs ». À chercher : la mesure porte-t-elle sur un juge statistique ou seulement sur l'agent ; y a-t-il un proposeur adverse ; comment les mondes sont engendrés. Deux titres : celui-ci est celui de l'interface d'arXiv ; le PDF de la version 2 s'intitule, d'après la voie citations, « Are LLM Research Agents Reliable Judges of Predictability? Evidence from Planted-Signal Worlds ».",
     "p. 1 à 4 du PDF (voie citations)"),
    ("arxiv:2611.00643", "1 (juge au nul des lois connues, voisin le plus proche avec prédiction préenregistrée) ; 5 ; 6 ; 14",
     "Ne crédite une hypothèse écrite par un modèle que pour le vrai au-delà de ce qu'un panel étalonné de modèles attend, sur vérité exacte, en étude préenregistrée : trois des cinq éléments de la grille du juge, avec un nul fait d'attentes de modèles au lieu de l'archive des lois. Le dépôt l'a lu p. 1, 2, 10 et 12 pour la prémisse du juge génératif, pas pour cet angle. À chercher : le « connu » du panel inclut-il des lois ou résultats publiés ; la règle de crédit est-elle séquentielle ; ce qui sépare encore ce nul d'un nul d'archive.",
     "p. 2 du PDF (voie adverse) ; p. 1, 2, 10, 12 dans le dépôt, autre angle"),
    ("arxiv:2606.29182", "1 (nul qui grossit avec ce qui est déjà établi) ; 10 (mémoire)",
     "Suite de « AutoDiscovery » (piste de priorité haute encore à lire selon la décision R-3143) : la surprise d'une hypothèse se mesure contre des croyances mises à jour par les preuves déjà accumulées, sur un horizon long. Si ces croyances jouent le rôle d'une archive du connu contre laquelle une découverte doit gagner, l'élément (ii) de la grille est pris pour des propositions de modèle de langue. À chercher : ce qui est stocké (résultats, lois ajustées, croyances d'un modèle) ; y a-t-il une règle de promotion et une garantie d'erreur.",
     "résumé (voies mots-clés et adverse)"),
    ("arxiv:2510.21614", "8 (l'héritage d'une génération est récompensé)",
     "La machine de Huxley-Gödel guide l'arbre d'auto-modifications par une mesure qui agrège les scores des descendants de chaque agent : c'est le principe même « le signal porte sur les générations suivantes », publié en octobre 2025. À chercher : l'horizon de l'agrégat, l'actualisation, ce qui est transmis (code, mémoire), et s'il existe une comparaison à un signal à un pas.",
     "résumé (voie adverse) ; résumé dans le dépôt"),
    ("url:neurips.cc/virtual/2026/169839", "7 (organisme qui se conçoit puis se fige, mesuré sur des viviers tenus à l'écart) ; 8 (expérience « poids contre archive »)",
     "« MetaEvoForge » : un améliorateur partagé, poids figés, journalise parent, modification et enfant, fusionne les preuves entre environnements, et se compare entraîné contre non entraîné sur des viviers tenus à l'écart à budget fixe. C'est, d'après une page de conférence résumée, le plan de l'expérience « concepteur figé avec archive contre concepteur entraîné ». Aucun texte n'a été trouvé (ni arXiv ni OpenReview) : il faut d'abord le localiser.",
     "page de conférence lue par un outil qui résume (voie adverse)"),
    ("arxiv:2610.23977", "9 (le séquentiel doit battre le meilleur de N tirages indépendants à budget égal)",
     "Prend le protocole de la porte et en contredit l'attente : à jetons égaux, l'avantage de l'évolution de programmes sur des tirages indépendants disparaît presque, une proposition conditionnée coûtant environ six tirages. Les auteurs disent que leur fenêtre favorise l'échantillonnage. À lire avec ses compagnons du même angle, non retenus parmi les douze : arXiv 2609.19799 (mêmes auteurs), 2607.12227 (issue selon le terrain), 2607.04108, 2610.22466, 2606.13003. À chercher : l'unité de budget, les tâches, ce qui est hérité.",
     "p. 1 et 5 du PDF (voie adverse)"),
    ("arxiv:2609.26457", "7 (universalité mesurée sur des familles inédites)",
     "Un agent de recherche réécrit son propre code, sélectionné sur des évaluations cachées, et ses gains se transfèrent à quatre bancs tenus à l'écart dont un hors distribution : la mesure de transfert d'une conception apprise est prise pour des agents de recherche. À chercher : familles ou simples items tenus à l'écart ; conception figée ou non au moment du transfert ; ce qui distingue ce transfert d'une universalité sur familles de questions.",
     "résumé (voies mots-clés, citations, adverse)"),
    ("arxiv:2610.41157", "8 (mémoire transmise et effets différés) ; 10",
     "Étude préenregistrée, 1 750 lancements : hériter du meilleur candidat courant apporte l'essentiel du progrès, plus que le résumé des échecs ou un proposeur plus gros. Si ce qui s'hérite utilement est l'artefact et non la mémoire, la prémisse qui exclut le signal à un pas est affaiblie. À chercher : budgets courts seulement ou non ; y a-t-il un bras à plusieurs générations.",
     "p. 1 et 2 du PDF (voie citations)"),
    ("arxiv:2609.18366", "11 (tâches fraîches du même générateur contre le surajustement adaptatif)",
     "Montre qu'un gain peut tenir à un raccourci commun à tout le banc, que des tâches tenues à l'écart du même protocole ne révèlent pas : la garde « tâches fraîches, même générateur » ne protégerait pas d'un défaut du générateur. À chercher : la preuve du raccourci, et si une banque sœur construite à l'aveugle l'aurait vu.",
     "résumé (voie adverse)"),
    ("arxiv:2609.35875", "12 (proposeurs de plusieurs fournisseurs, valeur de la diversité)",
     "Rejette, contre un vote majoritaire à budget apparié, l'hypothèse que la diversité (personas, température, identité du modèle) explique les gains d'un débat entre agents : troisième contre-indice à la diversité des fournisseurs, après les deux que le dépôt cite déjà. Terrain différent (débat, petits modèles) : à chercher, ce qui se transporte à des proposeurs indépendants jugés sur un oracle.",
     "résumé (voie adverse)"),
    ("arxiv:2611.05108", "10 (mémoire) ; 8",
     "Instances persistantes contre instances remises à zéro du même agent, sur neuf familles de tâches, avec ablation de ce qui est retenu : l'état persistant accélère sans améliorer régulièrement la solution finale. Second contre-indice à la mémoire, indépendant de celui de Qu, Chen et Wang. Dernier du classement parce que le dépôt tient déjà la mémoire pour « occupée dans son principe » et cite un contre-indice.",
     "p. 1 et 2 du PDF (voie adverse)"),
]
douze_json = []
for rang, (k, rev, pourquoi, lu_) in enumerate(DOUZE, 1):
    t = par_cle(k)
    d = t["date"] + (f" (voies divergentes : {t['dates_divergentes']})" if t["dates_divergentes"] else "")
    w(f"| {rang} | « {t['titre']} » — {t['auteurs'] or 'auteurs non relevés'} — {lien(t)} | {d} | {voies_txt(t)} | {rev} | {pourquoi} | {lu_} |")
    douze_json.append(dict(rang=rang, titre=t["titre"], adresse=t["adresse"], date=d, revendications=rev, pourquoi=pourquoi, lu=lu_, voies=voies_txt(t)))
w("")
seuls = sum(1 for k, *_ in DOUZE if len(par_cle(k)["voies"]) == 1)
w(f"**Ce que dit la provenance de ces douze** : {seuls} sur douze n'ont été trouvés que par une seule voie ({sum(1 for k, *_ in DOUZE if par_cle(k)['voies'] == ['adverse'])} par la voie adverse seule, {sum(1 for k, *_ in DOUZE if par_cle(k)['voies'] == ['citations'])} par la voie citations seule), et les deux premiers du classement ne viennent que du graphe de citations. Les travaux les plus menaçants sont donc surtout des travaux vus une fois : la part non vue estimée à la section 3 en contient très probablement d'autres du même rang.")
w("")
w("**Écartés de la liste, et pourquoi** :")
w("- Déjà lus sur source dans le dépôt pour l'angle qui compte, donc à ne pas relire ici : Liu, Liu, Liu et Mei (SSRN 6569258, lu en entier sur la copie de conférence ; la voie adverse le retrouve seule et le classe comme le voisin le plus proche du juge au nul des lois connues, ce qui confirme la lecture du dépôt sans rien y ajouter) ; Pan, Ding et Giesecke (arXiv 2609.00731) ; Qu, Chen et Wang (arXiv 2609.27051) ; la promotion certifiée sous réutilisation du même jeu (arXiv 2609.33180) ; Xia et Wang (arXiv 2606.14386, p. 1 à 4) ; « Fork-and-Flush », « Scaling Discovery Requires Forgetting » et le billet de Bespoke Labs (registre de veille, semaine 2026-W46).")
w("- Menaçants mais sans texte accessible (OpenReview refuse les PDF) — à lire dès qu'une version paraît : « How Many Scientists? Epistemic Diversity in Expanding-Frontier Discovery » (nombre et isolement des états de recherche comme variables de conception ; revendication 12) ; « Approval Is Not Discovery » et « Do LLMs Have Research Taste? An Analysis Using BóLèBench » (juge contre oracle ; revendication 6) ; « Replay the Scientist » et « When Statistical Discoveries Become State » (validité après recherche adaptative ; revendications 2 et 4) ; « What Does LLM-Judged Novelty Reward? » (revendication 14, cité sans développer) ; « When Failure Banks Kill Good Ideas » (revendication 10).")
w("- Proches mais d'un cran en dessous : le billet d'Anthropic sur le chercheur automatisé du faible vers le fort et l'article sur les chercheurs d'alignement automatisés (arXiv 2608.28945) — effondrement de l'entropie des directions, avantage d'amorces diverses qui s'éteint en une vingtaine de méthodes ; ils prédisent l'issue du bras « rien » de la comparaison de diversité, que le programme publie de toute façon si elle est négative ; « Hyperagents » (arXiv 2603.19461, déjà au dépôt) ; « Not Every Agent Needs the Strongest Model » (arXiv 2610.31743, modèle par rôle avec le coût) ; « On the Use of LLM Priors in Multiple Hypothesis Testing with e-Values » (terrain déjà cédé).")
w("- **Trou signalé par les témoins** : EvoSCM (arXiv 2609.01526) et BEYOND (arXiv 2603.14288), voisins connus du juge au nul des lois connues, n'ont été retrouvés par aucune voie. La liste ci-dessus ne peut donc pas passer pour un inventaire des voisins de ce juge ; la veille concurrentielle du dépôt (protocole v2, section 2.10) reste la référence pour cette pièce.")
w("")

# ---------------------------------------------------------------- table
w(f"## 5. Table fusionnée — {len(ANN)} travaux annotés par au moins une voie")
w("")
w("Une ligne par travail. Tri : nombre de voies décroissant, puis date décroissante. « Ce qu'il fait » reprend la description de la voie qui a lu le plus loin ; « lu jusqu'où » donne la meilleure profondeur atteinte et la voie qui l'a atteinte.")
w("")
ENT = "| n° | voies | première version relevée | nature | titre — auteurs | adresse | ce qu'il fait | mesuré ou affirmé | lu jusqu'où | touche (par voie) | remarques |"
SEP = "|---|---|---|---|---|---|---|---|---|---|---|"
num = 0
for titre_s, groupe in ((f"5.1 Trouvés par les quatre voies ({len(n4)})", n4), (f"5.2 Trouvés par trois voies ({len(n3)})", n3),
                        (f"5.3 Trouvés par deux voies ({len(n2)})", n2), (f"5.4 Trouvés par une seule voie ({len(n1)})", n1)):
    w(f"### {titre_s}")
    w("")
    w(ENT)
    w(SEP)
    cle_tri = (lambda t: (ORDRE.index(t["voies"][0]), tuple(-x for x in cle_date(t["date"])))) if groupe is n1 else (lambda t: tuple(-x for x in cle_date(t["date"])))
    for t in sorted(groupe, key=cle_tri):
        num += 1
        t["numero"] = num
        ta = f"{t['titre']}" + (f" — {t['auteurs']}" if t["auteurs"] else "")
        w(f"| {num} | {voies_txt(t)} | {t['date'] or 'non relevée'} | {t['nature']} | {ta} | {lien(t)} | {t['fait']} | {t['mesure']} | {t['lu']} | {t['touche']} | {remarques(t)} |")
    w("")

w(f"## 6. Titres de l'annexe mécanique de la voie mots-clés, non retrouvés par une autre voie ({len(ANX)})")
w("")
w(f"Retenus par un filtre de mots, jamais lus au-delà du titre ; pertinence non confirmée (beaucoup sont des systèmes d'un domaine ou des agents de recherche documentaire). Ils ne comptent pas dans les {len(ANN)} travaux ni dans les estimations de la section 3, sauf dans la ligne de sensibilité.")
w("")
w("| arXiv | première version | titre |")
w("|---|---|---|")
for t in sorted(ANX, key=lambda t: tuple(-x for x in cle_date(t["date"]))):
    w(f"| {lien(t)} | {t['date']} | {t['titre']} |")
w("")
w("## 7. Limites de cette fusion")
w("")
w(f"1. Je n'ai lu aucun travail : la table vaut ce que valent les quatre notes. {lu.get('texte entier', 0)} textes lus en entier sur {len(ANN)} ; le reste au résumé, sur quelques pages ou au titre.")
w("2. Les descriptions et les rapprochements « touche » sont recopiés, non réconciliés : deux voies peuvent décrire le même travail différemment, et la table garde la description de la voie qui a lu le plus loin.")
w("3. La voie adverse n'a reçu les revendications que jusqu'au point 12 (b) : les points 12 (c) à 15 (proposeurs de plusieurs fournisseurs, collisionneur de modèles, juges sous attaque, banc de tricheurs) n'ont été cherchés de façon adverse par personne ; ce que la table en dit vient des trois autres voies.")
w("4. Aucune des quatre voies n'a couvert SSRN, le NBER, bioRxiv ni les catégories d'arXiv hors apprentissage automatique (économie, interaction, scientométrie) autrement que par quelques recherches web ; les deux témoins de finance manqués le confirment.")
w("5. Les dates sont les plus anciennes relevées par une voie, non vérifiées ; avant tout usage d'antériorité, les relire sur la page d'origine.")
w("6. Les notices arXiv des douze travaux de la section 4 n'ont pas pu être revérifiées par l'interface d'arXiv au moment de la fusion (quatre essais entre 05:19 et 05:26 UTC : trois réponses « débit dépassé », un délai dépassé ; non contourné) : titres, auteurs et dates y sont ceux des voies.")
w("")

sortie.write_text("\n".join(L), encoding="utf-8")
if len(sys.argv) > 5:
    Path(sys.argv[5]).write_text(json.dumps(douze_json, ensure_ascii=False, indent=1), encoding="utf-8")
print("ecrit", sortie, len(L), "lignes", sortie.stat().st_size, "octets ; annotés", len(ANN), "annexe seule", len(ANX), "lu", dict(lu))
print("temoins trouves", trouves, dict(par_voie))
