"""Extraction des termes et des groupes — rétrodiction Swanson v1 (préenregistrement, sections 2 et 3).

Un document = ensemble de ses unigrammes et bigrammes (présence). Les deux listes de mots vides sont recopiées telles
quelles du préenregistrement ; l'essai `essai_listes_conformes` vérifie l'égalité avec les blocs du document scellé.
"""
import hashlib
import re
import unicodedata

MOTS_VIDES = frozenset("""
a about above across after afterwards again against all almost alone along already also although always am among
amongst an and another any anybody anyhow anyone anything anyway anywhere are aren around as at be became because become
becomes becoming been before beforehand behind being below beside besides between beyond both but by can cannot could
couldn did didn do does doesn doing don done down during each either else elsewhere enough etc ever every everybody
everyone everything everywhere except few for from further furthermore had hadn has hasn have haven having he hence her
here hereafter hereby herein hereupon hers herself him himself his how however i if in indeed into is isn it its itself
just less many may me meanwhile might mightn mine more moreover most mostly much must mustn my myself namely neither never
nevertheless no nobody none noone nor not nothing now nowhere of off often on once only onto or other others otherwise
ought our ours ourselves out over own per perhaps quite rather same shall shan she should shouldn since so some somebody
somehow someone something sometime sometimes somewhat somewhere still such than that the their theirs them themselves then
thence there thereafter thereby therefore therein thereof thereupon these they this those though through throughout thru
thus to together too toward towards under unless until up upon us very via was wasn we were weren what whatever when
whence whenever where whereafter whereas whereby wherein whereupon wherever whether which while whither who whoever whom
whose why will with within without won would wouldn yet you your yours yourself yourselves
""".split())

MOTS_GENERIQUES = frozenset("""
additionally address addressed addresses aim aims analyse analysed analyze analyzed analyzes approach approaches article
articles based consider considered considering considers demonstrate demonstrated demonstrates demonstrating describe
described describes describing discuss discussed discusses discussing discussion examine examined examines examining
explore explored explores exploring finally find finding findings finds found give given gives giving important
importantly indicate indicated indicates introduce introduced introduces introducing investigate investigated investigates
investigating investigation letter manuscript method methodology methods novel obtain obtained obtaining obtains paper
papers particular particularly perform performed performing performs present presented presenting presents previous
previously propose proposed proposes proposing provide provided provides providing recent recently report reported reports
respectively result resulting results show showed showing shown shows significantly studied studies study studying suggest
suggested suggests use used uses using various
""".split())

VIDES = MOTS_VIDES | MOTS_GENERIQUES

# Formules (remplacées par une coupure), puis commandes LaTeX (retirées sans espace), puis accolades (retirées).
_FORMULES = re.compile(
    r"\$\$.*?\$\$|\$.*?\$|\\\(.*?\\\)|\\\[.*?\\\]"
    r"|\\begin\{(equation|eqnarray|align|gather|multline|displaymath|math)(\*?)\}.*?\\end\{\1\2\}",
    re.S,
)
_COMMANDES = re.compile(r"\\[a-z]+\*?|\\[^a-z\s]")
_ELEMENTS = re.compile(r"[a-z]+|[^a-z\s\-]+")

GROUPES = ("math", "cs", "physique", "q-bio", "q-fin", "stat", "autre")
CHAMPS = GROUPES[:6]
AUTRE = 6
_PHYSIQUE = {"astro-ph", "cond-mat", "gr-qc", "math-ph", "nlin", "physics", "quant-ph"}


def nettoyer(titre, resume):
    texte = titre + " . " + resume
    texte = unicodedata.normalize("NFKD", texte).encode("ascii", "ignore").decode("ascii").lower()
    texte = _FORMULES.sub(" . ", texte)
    texte = _COMMANDES.sub("", texte)
    return texte.replace("{", "").replace("}", "")


def termes_document(titre, resume):
    """Ensemble des unigrammes et bigrammes du document (section 3 du préenregistrement)."""
    termes = set()
    precedent = None
    for element in _ELEMENTS.findall(nettoyer(titre, resume)):
        if "a" <= element[0] <= "z" and len(element) >= 3 and element not in VIDES:
            termes.add(element)
            if precedent is not None:
                termes.add(precedent + " " + element)
            precedent = element
        else:
            precedent = None
    return termes


def empreinte64(terme):
    return int.from_bytes(hashlib.blake2b(terme.encode("ascii"), digest_size=8).digest(), "little")


def groupe_de(categories):
    """Code du groupe (index dans GROUPES) de la catégorie principale (premier élément de `categories`)."""
    elements = categories.split()
    prefixe = elements[0].split(".")[0] if elements else ""
    if prefixe == "math":
        return 0
    if prefixe == "cs":
        return 1
    if prefixe in _PHYSIQUE or prefixe.startswith("hep-") or prefixe.startswith("nucl-"):
        return 2
    if prefixe == "q-bio":
        return 3
    if prefixe == "q-fin":
        return 4
    if prefixe == "stat":
        return 5
    return AUTRE
