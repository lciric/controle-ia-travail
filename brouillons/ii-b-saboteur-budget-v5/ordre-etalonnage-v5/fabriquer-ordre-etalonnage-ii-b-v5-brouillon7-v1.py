"""Fabrique le brouillon 7 de l'ordre de l'étalonnage depuis le brouillon 6, par remplacements à ancre comptée.
Demande de la mère (2026-11-21 vers 20:37Z), d'après le compte rendu 3 de l'exécutante neuve : (A) les pièces citées par la
configuration sont absentes de l'arbre du code revu, alors que les contrôles les exigent au commit de lancement ; (B)
registres/go.md au commit du code n'a pas la ligne GO-2026-11-21-70. Donc : commit de lancement élargi aux pièces citées et à
leurs compagnons, copiés à l'octet depuis la branche de la reconception, et à registres/go.md de main ; chemins et empreintes des
pièces ; valeur de prefixe_graines pour l'étalonnage ; mot de Lazar GO-2026-11-21-84 (étalonnage accordé, première action
« gardée »). Rien d'autre. Usage : python3 fabriquer-ordre-etalonnage-ii-b-v5-brouillon7-v1.py (depuis ce dossier)."""
import hashlib, pathlib

ICI = pathlib.Path(__file__).resolve().parent
SOURCE, CIBLE = ICI / "ordre-etalonnage-ii-b-v5-brouillon6.md", ICI / "ordre-etalonnage-ii-b-v5-brouillon7.md"
t = SOURCE.read_text(encoding="utf-8")
assert hashlib.sha256(t.encode("utf-8")).hexdigest().startswith("4e5c156e"), "brouillon 6 inattendu"

B = "brouillons/ii-b-saboteur-budget-v5/"
TABLE_PIECES = (
    "| pièces | au commit de lancement, aux chemins ci-dessous, copiées à l'octet depuis la branche "
    "`claude/iib-reconception-oracle-v1` avec leurs compagnons `.sha256` (la configuration cite chemin et empreinte, le code "
    "vérifie l'empreinte à l'égalité) : "
    f"`conception` = `{B}conception-organisme-retenu-ii-b-v5-scellee-v1.md` (`c1dc54597a1ab4b467331673607d986e46a706c06253bb40070e5d15caaa61f2`) ; "
    f"`consigne_maitre_N` = `{B}consignes-v5/consigne-privee-maitre-ii-b-v5-issue-N-v3.md` (`6b6cfe2218734873e3f9c07dcbd872350cf0bb4b994b0ea4f17e3e2aad8cb226`) ; "
    f"`consigne_maitre_P` = `{B}consignes-v5/consigne-privee-maitre-ii-b-v5-issue-P-v3.md` (`0d854766f794a6d384474124fcc207fc11cdba2722d421bb865f5b847869f1ad`) ; "
    f"`consigne_flagrant` = `{B}consignes-v5/consignes-flagrant-etalonnage-ii-b-v5-rien-au-premier-cout-v2.md` (`24af4e2e79961891f4fa89ba60910f222f23cf1603c134a72bc84aba192f1869`) ; "
    "`taches_reserve` = `donnees/20261007-082440-t05-extraction/taches-entrainement.json` (`8d20a698d76baa8a42cd1494227fc411ef043d24a67a413e5cf812541166a4fd`, "
    "déjà dans l'arbre du code revu, celles de la première course) ; "
    "`taches_evaluation` = `donnees/20261007-082440-t05-extraction/taches-evaluation.json` (`76cdeace861d2fff45ca732c55c2d97611dcd47edc7c27d62bdad4c37755e67e`, idem) ; "
    "`entrees` = `<<FICHIER_ENTREES_CHEMIN_ET_EMPREINTE>>`. "
    f"Copiés aussi, pour lecture seule, sans être cités par la configuration : `{B}conception-organisme-retenu-ii-b-v5-scellee-v1-erratum-1.md` "
    f"(`2031baba173cad5cd410ea22d069b118d4ba04783013495388a6db0b53f15433`), `…-erratum-2.md` (`ab020d438cb6eaa46cd2df0a6ed76952b5dfb23497438e0f2b3fb4590b1d26e2`), "
    f"`{B}devis-v5/devis-ii-b-v5-scelle-v1.md` (`cb881522378ace662787a7097c2baa6d461c766d70782d28636c132ce09f3ee8`) et son erratum 1 "
    "(`90342292f52daf2f7281acad68006598450033367d3a36aa1c6c72eac9150f9a`) ; et `registres/go.md` de `main` (au plus tôt la tête "
    "`bef65df0d19e5f678acb7aa94aa692df1644d4ef`, qui porte `GO-2026-11-21-70` et `GO-2026-11-21-84`), copié à l'octet ; "
    "son empreinte au commit de lancement est relevée au compte rendu. Les consignes privées ne sont lues que par les chargeurs du code ; "
    "aucun texte n'en est affiché ni recopié |\n"
    "| `prefixe_graines` | `\"\"` (chaîne vide) pour l'étalonnage : les clés sont celles du texte scellé (section 14), qui portent déjà la phase ; "
    "la course aura son préfixe propre, fixé par son ordre |"
)

REMPLACEMENTS = [
    ("| pièces | texte scellé, deux variantes de la consigne du maître, consigne du flagrant, tâches de réserve, tâches d'évaluation, fichier d'entrées : chemins et empreintes |",
     TABLE_PIECES, 1),
    ("la différence entre les deux ne porte que la configuration, le fichier d'entrées et leurs sceaux",
     "la différence entre les deux ne porte que la configuration, le fichier d'entrées, les pièces du § 2 copiées à l'octet, "
     "`registres/go.md` de `main` et leurs sceaux", 1),
    ("qui n'ajoute que la configuration, le fichier d'entrées et leurs sceaux",
     "qui n'ajoute que la configuration, le fichier d'entrées, les pièces du § 2 copiées à l'octet, `registres/go.md` de `main` et leurs sceaux", 1),
    ("mot de Lazar pour la création : `GO-2026-11-21-74`",
     "mot de Lazar pour la création : `GO-2026-11-21-74`, et l'étalonnage accordé par `GO-2026-11-21-84`", 1),
    ("**à confirmer par le mot de Lazar avant le scellement de la configuration**, `<<MOT_LAZAR_PREMIERE_ACTION_DANS_LA_PERTE>>`",
     "**`gardee`, confirmé par le mot de Lazar** (`GO-2026-11-21-84`, `registres/go.md` de `main`)", 1),
]
for ancien, nouveau, n in REMPLACEMENTS:
    assert t.count(ancien) == n, (ancien[:60], t.count(ancien))
    t = t.replace(ancien, nouveau)
LIGNE_CHAMP = "| `<<MOT_LAZAR_PREMIERE_ACTION_DANS_LA_PERTE>>` |"
lignes = t.split("\n")
idx = [i for i, l in enumerate(lignes) if l.startswith(LIGNE_CHAMP)]
assert len(idx) == 1
lignes[idx[0]] = ("| ~~`<<MOT_LAZAR_PREMIERE_ACTION_DANS_LA_PERTE>>`~~ | rempli au brouillon 7 : `GO-2026-11-21-84` (« gardée ») | mère |")
t = "\n".join(lignes)
assert "<<MOT_LAZAR_PREMIERE_ACTION_DANS_LA_PERTE>>`," not in t
CIBLE.open("x", encoding="utf-8").write(t)
print(CIBLE.name, hashlib.sha256(t.encode("utf-8")).hexdigest())
