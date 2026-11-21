"""Véhicule NA-1, lot 6 — le moteur simulé et le faux fournisseur de la course (`simulation_na_v1`).

Lettre : conception du véhicule v5 (`1b7f6822…`), § 2.12 (moteur simulé au contrat de cette course ; faux fournisseur ;
textes inertes, sans rapport avec la question), § 6.3 ; V9 (`864f39a7…`), l. 77 (égalité entre ce qui est journalisé et ce
qui part) ; erratum 1 du mandat du lot 6, **versé v2** (`24d37f85…`, retenu par la mère à 17:44Z), E8 : le faux
fournisseur garde, pour chaque appel, la taille et l'empreinte du corps reçu, et la taille et l'empreinte de la chaîne de
contenu de chaque message de ce corps.

- `AdaptateurSimuleNA` : un adaptateur simulé, au contrat de cette course. Il reconnaît la sorte d'appel à la forme de la
  requête (lot 3) : un proposeur (la partie servie remplie, sa ligne de case) ; le portier, appel « fiche » (`## La fiche`,
  sans identifiant servi) ou « réponse sans fiche » (`## La réponse`) ; un juge (`## La fiche`, identifiant servi en
  dernière clé). Le proposeur rend, selon l'empreinte de l'identifiant de la case et du nom de l'adaptateur (ou selon un
  `decider` d'essai) : des fiches au contrat (en étiquettes ancrées ou en objet structuré), une fiche à un champ de plus,
  une fiche à champ fermé différent, une fiche « concret », une réponse sans fiche de chaque sorte. Le portier et les
  juges rendent leurs étiquettes fermées. **Tous les textes sont inertes** : ils ne disent rien de la question.
- `FauxFournisseurNA` : le faux fournisseur du lot 4 (boucle locale seule), et, pour chaque appel reçu, la taille et
  l'empreinte du corps et de la chaîne de contenu de chaque message (`requetes_na`).
- `AdaptateurBoucleLocaleNA` : un adaptateur d'essai qui envoie la chaîne qu'il reçoit au faux fournisseur, dans un seul
  message « user », sans rien y ajouter ; il sert à éprouver l'égalité « journal, chaîne reçue » (E8). Ce n'est pas un
  fournisseur : il ne parle qu'à `127.0.0.1`.

Aucune clé, aucun réseau hors de la boucle locale, aucune dépense : le coût rendu est un nombre fictif, déclaré.
"""

import hashlib
import json
import re
import urllib.request

from pole import faux_fournisseur_na_v1 as ff
from pole import requete_na_v3 as rq
from pole.adaptateurs import Resultat

VERSION = "simulation-na-v1"
COMPORTEMENTS = ("fiches_etiquettes", "fiches_json", "champ_en_plus", "champ_ferme_different", "concret", "vide_motivee",
                 "refus_modele", "illisible", "vide", "idee_marque_code")
COMPORTEMENTS_PAR_DEFAUT = ("fiches_etiquettes", "fiches_json", "fiches_etiquettes", "champ_en_plus", "champ_ferme_different",
                            "vide_motivee", "fiches_etiquettes", "refus_modele", "illisible", "fiches_json", "fiches_etiquettes")
IDEE_INERTE = "Idée factice, inerte, du moteur simulé : elle ne dit rien."
MARQUE_CONCRET = "concret factice"
MARQUE_VIDE_MOTIVEE = "réponse vide motivée factice"
MARQUE_DECLINE = "réponse factice qui décline"
TEXTE_ILLISIBLE = "Texte factice sans forme, inerte."
_LIGNE_CASE = re.compile(r"^case : (?P<id>[a-z]{6}) ; (?P<v1>.+?) ; (?P<v2>.+?) ; (?P<v3>.+)$", re.M)


def _sha(octets):
    return hashlib.sha256(octets).hexdigest()


def sorte_de_requete(consigne):
    """La sorte d'appel, lue à la forme de la requête (lot 3) : « proposeur », « portier_fiche »,
    « portier_reponse_sans_fiche », « juge »."""
    ouverture = "\n" + rq.OUVERTURE_BLOC + "\n"
    if "\n\n" + rq.TITRE_REPONSE + ouverture in consigne:
        return "portier_reponse_sans_fiche"
    if "\n\n" + rq.TITRE_FICHE + ouverture in consigne:
        corps = consigne.split("\n\n" + rq.TITRE_FICHE + ouverture, 1)[1].rsplit("\n" + rq.FERMETURE_BLOC, 1)[0]
        try:
            objet = json.loads(corps)
        except ValueError:
            return "portier_fiche"
        return "juge" if isinstance(objet, dict) and rq.CLE_IDENTIFIANT_JUGE in objet else "portier_fiche"
    return "proposeur"


def fiche_inerte(identifiant, valeurs, *, idee=IDEE_INERTE, n=0):
    return {"case": identifiant, "ce_que_le_moniteur_suppose": valeurs[0], "menace_du_programme": valeurs[1],
            "etage_de_lecture": valeurs[2], "idee": idee + (f" Variante factice {'abc'[n % 3]}." if n else ""),
            "mesurable_sur_monde_plante": "grandeur factice", "ce_qui_la_refuterait": "issue factice une",
            "issue_contraire": "issue factice deux", "voisin_le_plus_proche_connu": "aucun connu",
            "ecart_au_voisin": "écart factice", "filiation": "aucune", "piece_produite": "publique"}


def en_etiquettes(fiche):
    return "\n".join(f"{k} : {v}" for k, v in fiche.items())


def en_json(fiche):
    return "```json\n" + json.dumps(fiche, ensure_ascii=False, indent=2) + "\n```"


class AdaptateurSimuleNA:
    """Adaptateur simulé au contrat de cette course ; garde les consignes reçues en mémoire (jamais sur disque)."""

    nom = "simule-na"

    def __init__(self, nom_adaptateur, *, declaration, items, cout_par_appel_usd=0.01, decider=None, marqueur=None,
                 reglages=None, modele_servi=None, garder_consignes=False, portier_illisible=False, juge_illisible=False):
        self.nom_adaptateur = nom_adaptateur
        self.declaration = declaration
        self.items = list(items)
        self.cout = float(cout_par_appel_usd)
        self.decider = decider
        self.marqueur = marqueur
        self.reglages = list(reglages or [])  # file de résultats imposés (dict de `Resultat`), consommée d'abord
        # None : le modèle demandé ; une fonction (sorte, k) -> str, k le rang de l'appel de cette sorte (essais d'A2)
        self.modele_servi = modele_servi
        self.garder_consignes = garder_consignes  # essais seulement : les consignes en mémoire, jamais sur disque
        self.portier_illisible, self.juge_illisible = portier_illisible, juge_illisible
        self.recus = []
        self.consignes = []
        self._par_sorte = {}

    def description(self):
        return {"type": "simule-na", "adaptateur": self.nom_adaptateur, "cout_par_appel_usd": self.cout}

    def _servi(self, modele):
        if self.modele_servi is None:
            return modele
        sorte = self.recus[-1]["sorte"] if self.recus else None
        return self.modele_servi(sorte, self._par_sorte.get(sorte, 0)) if callable(self.modele_servi) else self.modele_servi

    def _resultat(self, texte, modele, **en_plus):
        if self.marqueur is not None:
            texte = texte + "\n" + self.marqueur
        d = {"texte_final": texte, "texte_brut": texte, "statut": "ok", "cout_declare_usd": self.cout,
             "modele_servi": self._servi(modele)}
        d.update(en_plus)
        return Resultat(**d)

    def comportement(self, identifiant_case):
        if self.decider is not None:
            return self.decider(identifiant_case, self.nom_adaptateur, len(self.recus) - 1)  # rang de cet appel, de 0
        h = int(_sha(f"{identifiant_case}|{self.nom_adaptateur}".encode("utf-8"))[:8], 16)
        return COMPORTEMENTS_PAR_DEFAUT[h % len(COMPORTEMENTS_PAR_DEFAUT)]

    def lancer(self, role, consigne, dossier, budget_usd, max_tours, modele=None):
        sorte = sorte_de_requete(consigne)
        self.recus.append({"role_kit": role, "sorte": sorte, "consigne_sha256": _sha(consigne.encode("utf-8")),
                           "taille": len(consigne.encode("utf-8")), "budget": budget_usd, "modele": modele})
        self._par_sorte[sorte] = self._par_sorte.get(sorte, 0) + 1
        if self.garder_consignes:
            self.consignes.append((sorte, consigne))
        if self.reglages:
            r = dict(self.reglages.pop(0))
            r.setdefault("texte_final", "")
            r.setdefault("texte_brut", r["texte_final"])
            r.setdefault("cout_declare_usd", self.cout)
            r.setdefault("statut", "ok")
            r.setdefault("modele_servi", self._servi(modele) if r["statut"] == "ok" else None)
            return Resultat(**r)
        if sorte == "proposeur":
            return self._proposer(consigne, modele)
        if sorte == "portier_fiche":
            return self._portier_fiche(consigne, modele)
        if sorte == "portier_reponse_sans_fiche":
            return self._portier_reponse(consigne, modele)
        return self._juger(modele)

    def _proposer(self, consigne, modele):
        m = _LIGNE_CASE.search(consigne)
        if m is None:
            return self._resultat(TEXTE_ILLISIBLE, modele)
        identifiant, valeurs = m.group("id"), (m.group("v1"), m.group("v2"), m.group("v3"))
        c = self.comportement(identifiant)
        if isinstance(c, dict):
            return self._resultat(c.get("texte", ""), modele)
        if c == "fiches_etiquettes":
            texte = en_etiquettes(fiche_inerte(identifiant, valeurs)) + "\n\n---\n\n" + \
                en_etiquettes(fiche_inerte(identifiant, valeurs, n=1))
        elif c == "fiches_json":
            texte = en_json(fiche_inerte(identifiant, valeurs, n=2))
        elif c == "champ_en_plus":
            f = fiche_inerte(identifiant, valeurs)
            f["remarque"] = "champ factice en plus"
            texte = en_json(f)
        elif c == "champ_ferme_different":
            texte = en_json(fiche_inerte(identifiant, (valeurs[0] + " différent", valeurs[1], valeurs[2])))
        elif c == "idee_marque_code":
            texte = en_json(fiche_inerte(identifiant, valeurs, idee=IDEE_INERTE + " `marque factice`"))
        elif c == "concret":
            texte = en_json(fiche_inerte(identifiant, valeurs, idee=IDEE_INERTE + " " + MARQUE_CONCRET + "."))
        elif c == "vide_motivee":
            texte = "Aucune fiche : " + MARQUE_VIDE_MOTIVEE + "."
        elif c == "refus_modele":
            texte = "Aucune fiche : " + MARQUE_DECLINE + "."
        elif c == "illisible":
            texte = TEXTE_ILLISIBLE
        elif c == "vide":
            texte = ""
        else:
            raise ValueError("comportement simulé inconnu")
        return self._resultat(texte, modele)

    def _etiquette(self, sorte, sens):
        return f"{self.declaration.cle} : {self.declaration.textes(sorte)[sens]}"

    def _portier_fiche(self, consigne, modele):
        if self.portier_illisible:
            return self._resultat(TEXTE_ILLISIBLE, modele)
        sens = "concret" if MARQUE_CONCRET in consigne else "niveau de l'idée"
        return self._resultat("Réponse factice du portier, inerte.\n" + self._etiquette("fiche", sens) + "\n", modele)

    def _portier_reponse(self, consigne, modele):
        if self.portier_illisible:
            return self._resultat(TEXTE_ILLISIBLE, modele)
        if MARQUE_VIDE_MOTIVEE in consigne:
            sens = "réponse vide motivée"
        elif MARQUE_DECLINE in consigne:
            sens = "refus du modèle"
        else:
            sens = "réponse illisible"
        return self._resultat("Réponse factice du portier, inerte.\n" + self._etiquette("réponse sans fiche", sens) + "\n",
                              modele)

    def _juger(self, modele):
        if self.juge_illisible:
            return self._resultat(TEXTE_ILLISIBLE, modele)
        bloc = {"items": {k: True for k in self.items}, "note": 1}
        return self._resultat("Verdict factice, inerte.\n```json\n" + json.dumps(bloc, ensure_ascii=False) + "\n```\n", modele)


def adaptateurs_simules_na(table, *, declaration, items, cout_par_appel_usd=0.01, **kw):
    """Un adaptateur simulé par nom d'adaptateur de la table qui porte un rôle (jamais `hors_course`)."""
    noms = sorted({e.adaptateur for e in table.roles.values() if e.cle != "hors_course"})
    return {n: AdaptateurSimuleNA(n, declaration=declaration, items=items, cout_par_appel_usd=cout_par_appel_usd, **kw)
            for n in noms}


# --- le faux fournisseur (E8, et l'ajout de la version 2 de l'erratum) -------------------------------------------------

def empreintes_messages(corps):
    """Pour chaque message du corps : son rang, son rôle, la taille et l'empreinte de sa chaîne de contenu (UTF-8). Un
    contenu en blocs donne une entrée par bloc de texte (`bloc`). Un corps sans messages rend une liste vide."""
    rendu = []
    messages = corps.get("messages") if isinstance(corps, dict) else None
    for i, m in enumerate(messages or [], start=1):
        if not isinstance(m, dict):
            continue
        contenu = m.get("content")
        if isinstance(contenu, str):
            o = contenu.encode("utf-8")
            rendu.append({"rang": i, "role": m.get("role"), "bloc": None, "contenu_taille": len(o), "contenu_sha256": _sha(o)})
        elif isinstance(contenu, list):
            for k, b in enumerate(contenu, start=1):
                if isinstance(b, dict) and isinstance(b.get("text"), str):
                    o = b["text"].encode("utf-8")
                    rendu.append({"rang": i, "role": m.get("role"), "bloc": k, "contenu_taille": len(o),
                                  "contenu_sha256": _sha(o)})
    return rendu


class FauxFournisseurNA(ff.FauxFournisseur):
    """Le faux fournisseur du lot 4 (boucle locale seule) ; `requetes_na()` rend, pour chaque appel reçu, la taille et
    l'empreinte du corps (gardées par le lot 4 à la réception) et celles de la chaîne de contenu de chaque message."""

    def requetes_na(self):
        with self._verrou:
            requetes = list(self.requetes)
        return [{"rang": e["rang"], "chemin": e["chemin"], "corps_taille": e["corps_taille"], "corps_sha256": e["corps_sha256"],
                 "messages": empreintes_messages(e["corps"])} for e in requetes]


class AdaptateurBoucleLocaleNA:
    """Adaptateur d'essai : la chaîne reçue part seule dans un message « user » vers le faux fournisseur, sur la boucle
    locale, sans mandataire ; la réponse est rendue telle quelle."""

    nom = "boucle-locale-na"

    def __init__(self, url, *, cout_par_appel_usd=0.0, delai_s=10):
        if not url.startswith("http://127.0.0.1:"):
            raise ValueError("boucle locale seule")
        self.url, self.cout, self.delai = url.rstrip("/"), float(cout_par_appel_usd), delai_s
        self._ouvreur = urllib.request.build_opener(urllib.request.ProxyHandler({}))

    def description(self):
        return {"type": "boucle-locale-na", "url": "boucle locale"}

    def lancer(self, role, consigne, dossier, budget_usd, max_tours, modele=None):
        corps = json.dumps({"model": modele or "modele-essai-inerte", "max_tokens": 64,
                            "messages": [{"role": "user", "content": consigne}]}, ensure_ascii=False).encode("utf-8")
        req = urllib.request.Request(self.url + "/v1/messages", data=corps, method="POST",
                                     headers={"content-type": "application/json"})
        with self._ouvreur.open(req, timeout=self.delai) as r:
            rep = json.loads(r.read().decode("utf-8"))
        texte = "".join(b.get("text", "") for b in rep.get("content") or [] if isinstance(b, dict))
        return Resultat(texte_final=texte, texte_brut=texte, statut="ok", cout_declare_usd=self.cout,
                        modele_servi=rep.get("model"))


__all__ = ("AdaptateurSimuleNA", "adaptateurs_simules_na", "FauxFournisseurNA", "AdaptateurBoucleLocaleNA",
           "empreintes_messages", "sorte_de_requete", "fiche_inerte", "COMPORTEMENTS", "VERSION")
