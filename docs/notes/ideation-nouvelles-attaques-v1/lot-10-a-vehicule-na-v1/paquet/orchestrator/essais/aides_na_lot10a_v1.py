"""Aides des essais du lot 10 a du véhicule NA-1 (lisent `matiere_premiere_na_v1`) : données factices seules.

- **Le registre d'essai** : 35 entrées aux lignes inertes (24 « visée factice », 11 « défense factice »), chacune à quatre
  champs (`nom`, `enonce`, `sorte`, `renvoi`) : forme d'essai, déclarée comme telle ; le registre servi réel n'est pas
  ouvert, et sa forme n'est pas connue ici. Les noms et les énoncés sont bâtis de mots neutres (syllabes de l'alphabet des
  identifiants) ; aucun ne dit rien.
- **La pièce de relevés d'essai** : cinq lignes factices, inertes, puis la sixième ligne au libellé d'essai.
- **Deux fonctions d'identifiant de ligne** (E5), différentes : par le rang ; par une empreinte salée du rang.
- **Les conditions d'allumage d'essai** et un manifeste de lecture de fin d'essai, déclarés comme tels.
- **Un montage du lot 4** (`MontageColonne`) : celui des essais du lot 4, le vrai `appel` du noyau, avec le journal de la
  colonne à la place du journal du lot 3.

Lancé comme programme (`python -B aides_na_lot10a_v1.py SORTIE.json`), il mesure le taux de faux refus de la garde de la
colonne sur toutes les requêtes et tous les registres servis de l'essai, et l'écrit (le fichier ne doit pas exister, R12).
"""

import hashlib
import json
import os
import sys
import tempfile

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE_ORCHESTRATEUR = os.path.dirname(ICI)
for _p in (ICI, RACINE_ORCHESTRATEUR):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import aides_na_lot3_v3 as L3  # noqa: E402
import aides_na_lot4_v1 as L4  # noqa: E402
import aides_na_v4 as A  # noqa: E402
from pole import identifiants_na_v1 as ident  # noqa: E402
from pole import journal_na_v3 as jn  # noqa: E402
from pole import matiere_premiere_na_v1 as mp  # noqa: E402
from pole import registre_na_v1 as rg  # noqa: E402
from pole import requete_na_v3 as rq  # noqa: E402
from pole import routage_na_v1 as rt  # noqa: E402
from pole import appel_garde_na_v1 as ag  # noqa: E402

STATUT = "registre d'essai aux lignes inertes, forme d'essai déclarée comme telle ; le registre réel n'est pas ouvert"
CHAMPS = ("nom", "enonce", "sorte", "renvoi")
CHAMP_ENONCE = "enonce"
BORNE_ENONCE = 300
N_VISEES, N_DEFENSES = 24, 11
DATE_ESSAI = "2026-11-21"


def sha(octets):
    return hashlib.sha256(octets).hexdigest()


def mot(i):
    return ident.mot_de_case(1000 + 37 * i)


def nom_court(i):
    return f"entrée factice {mot(i)}"


def enonce(i):
    return f"Énoncé factice inerte de la colonne, entrée {mot(i)}, sans aucun contenu."


def entrees():
    rendu = []
    for i in range(N_VISEES + N_DEFENSES):
        rendu.append({"nom": nom_court(i), "enonce": enonce(i),
                      "sorte": "visée factice" if i < N_VISEES else "défense factice", "renvoi": "aucun"})
    return rendu


def registre_octets(liste=None):
    o = json.dumps(entrees() if liste is None else liste, ensure_ascii=False, indent=1).encode("utf-8")
    return o, sha(o)


def ident_par_rang(rang, entree):
    """Fonction d'essai 1 : les six octets du rang."""
    return rang.to_bytes(6, "big")


def ident_par_empreinte_salee(rang, entree):
    """Fonction d'essai 2 : six octets d'une empreinte salée du rang (aucun contenu lu)."""
    return hashlib.sha256(f"sel factice du lot 10 a, rang {rang}".encode("utf-8")).digest()[:6]


def reglages(fonction=ident_par_rang, **en_plus):
    r = {"normaliseur": A.normaliseur(), "octets_identifiant_ligne": fonction, "champ_enonce": CHAMP_ENONCE,
         "champs_entree": CHAMPS, "borne_enonce_octets": BORNE_ENONCE, "entrees_attendues": N_VISEES + N_DEFENSES}
    r.update(en_plus)
    return r


def colonne(fonction=ident_par_rang, liste=None, **en_plus):
    o, s = registre_octets(liste)
    return mp.lire_registre(o, s, **reglages(fonction, **en_plus))


def ligne_etat(etat=1, empreinte=None, nom=None, date=DATE_ESSAI, libelle=mp.LIBELLE_ESSAI):
    empreinte = empreinte if empreinte is not None else registre_octets()[1]
    nom = nom if nom is not None else mp.NOMS_ETATS[etat]
    return (f"{libelle} interrupteur {mp.INTERRUPTEUR} ; état {etat} ({nom}) ; registre servi {empreinte} ; "
            f"date {date}")


CINQ_LIGNES = ("relevé factice, clé une : inerte", "relevé factice, clé deux : inerte", "relevé factice, clé trois : inerte",
               "relevé factice, clé quatre : inerte", "relevé factice, clé cinq : inerte")


def piece_releves(*sixiemes, sans_sixieme=False, **kw):
    lignes = list(CINQ_LIGNES)
    if not sans_sixieme:
        lignes += list(sixiemes) if sixiemes else [ligne_etat(**kw)]
    o = ("\n".join(lignes) + "\n").encode("utf-8")
    return o, sha(o)


EMPREINTE_ADDITIF_ESSAI = sha(b"additif factice du vehicule, essai seulement")


def manifeste_lecture_fin(dossier, contenu):
    chemin = os.path.join(dossier, "manifeste-lecture-de-fin-essai.json")
    with open(chemin, "x", encoding="utf-8") as f:
        f.write(json.dumps(contenu, ensure_ascii=False))
    return chemin


def manifeste_sain():
    return {"format": mp.FORMAT_MANIFESTE_LECTURE_FIN, mp.CLE_EMPREINTE_ADDITIF: EMPREINTE_ADDITIF_ESSAI}


def conditions(dossier, manifeste="sain", **remplace):
    if manifeste == "sain":
        chemin = manifeste_lecture_fin(dossier, manifeste_sain())
    elif manifeste is None:
        chemin = os.path.join(dossier, "absent.json")
    else:
        chemin = manifeste_lecture_fin(dossier, manifeste)
    c = {"ligne_accord_lazar": f"accord factice d'essai : {mp.INTERRUPTEUR}, état 2, registre {registre_octets()[1]}",
         "chemin_manifeste_lecture_fin": chemin, "empreinte_additif_attendue": EMPREINTE_ADDITIF_ESSAI,
         "devis_ligne_a_part": {"ligne": mp.LIGNE_DEVIS, "plafond_usd": 5.0, "hors_parts_de_la_course": True},
         "lecteurs_inscrits": mp.JUGES_DE_FIN, "branche_orpheline": True}
    c.update(remplace)
    return mp.ConditionsAllumage(**c)


def pieces_fixes(**remplace):
    p = {"partie servie (gabarit)": A.GABARIT_FACTICE, "synthèse servie": A.SYNTHESE_FACTICE,
         "consigne du portier": L3.CONSIGNE_PORTIER_FACTICE, "consigne des juges": L3.CONSIGNE_JUGE_FACTICE,
         "témoins": "Témoin factice, inerte.\nSecond témoin factice, inerte.\n".encode("utf-8")}
    p.update(remplace)
    return p


def depart(etat=1, fonction=ident_par_rang, environ=None, configuration=None, conditions_allumage=None, pieces=None):
    o, s = piece_releves(etat=etat)
    return mp.preparer_depart(piece_releves=o, empreinte_piece_releves=s, empreinte_registre_attendue=registre_octets()[1],
                              configuration={} if configuration is None else configuration,
                              pieces_fixes=pieces_fixes() if pieces is None else pieces,
                              charger=lambda: colonne(fonction), environ={} if environ is None else environ,
                              conditions_allumage=conditions_allumage)


def synthese_avec(*lignes):
    """La synthèse factice, avec des lignes de plus à la fin."""
    return A.SYNTHESE_FACTICE + "".join(l + "\n" for l in lignes).encode("utf-8")


def tous_les_textes():
    """Tous les noms et tous les énoncés du registre d'essai, pour la recherche d'absence."""
    return [e["nom"] for e in entrees()] + [e["enonce"] for e in entrees()]


# --- registre servi d'essai (forme du lot 5) ------------------------------------------------------------------------------

def registre_servi(enonces):
    """Des lignes de tentative à la forme de `registre_na_v1`, aux noms réencodés, champs fermés factices."""
    lignes = [rg.ligne_tentative(ident.encoder_octets(bytes([9, 9, 9, 9, 9, i])), ["fermé un", "fermé deux", "fermé trois"],
                                 e) for i, e in enumerate(enonces)]
    lignes.append(rg.ligne_compte(ident.mot_de_case(5), "au coffre", 0))
    return ("\n".join(lignes) + "\n").encode("utf-8")


# --- montage du lot 4, avec le journal de la colonne ------------------------------------------------------------------

class MontageColonne(L4.Montage):
    """Le montage des essais du lot 4, journal de la colonne à la place de celui du lot 3 ; le reste à l'identique."""

    def __init__(self, depart_colonne, generation=1, journal_nom="journal-requetes-g1.jsonl"):
        self.dossier = tempfile.mkdtemp(prefix="essais-na-lot10a-")
        self.sortie = os.path.join(self.dossier, "sortie")
        os.makedirs(self.sortie)
        self.table = L4.table(None, "course")
        self.journal = mp.JournalRequetesColonneNA(self.sortie, journal_nom, depart=depart_colonne)
        self.garde = A.garde_essai()
        self.cumul = rt.CumulParCle(self.table)
        self.lectures_relais = []
        etat = L4.etat_relais_sain()
        self.contexte = ag.ContexteAppelGardeNA(
            numero_generation=generation, table=self.table, parts=L4.parts(self.table), pires_par_role=L4.pires(self.table),
            journal=self.journal, garde=self.garde, identifiant_case_de_session=L4.case_de_session, cumul=self.cumul,
            lire_etat_relais=lambda cle: dict(etat), portee_arret_1="appel")
        self.ad = L4.adaptateurs()
        self.gen = L4.GenerationEssai(self.ad, self.dossier, contexte_na=self.contexte)


# --- toutes les requêtes de l'essai ---------------------------------------------------------------------------------------

ROLES_PROPOSEURS = ("proposeur-espece-1", "proposeur-espece-2", "proposeur-espece-3", "proposeur-espece-4",
                    "proposeur-espece-5")


def requetes_de_l_essai():
    """Les requêtes de proposeur de l'essai (33 cases × 3 générations, registre factice aux générations 2 et 3), celles du
    portier et des juges sur chaque case, et la sonde sur la première case."""
    cs, g = L3.cases(), L3.gabarit()
    rendu = []
    for gen in (1, 2, 3):
        for c in cs[str(gen)]:
            if gen == 1:
                rendu.append(rq.assembler_proposeur(g, c, L3.synthese(), 1))
            else:
                reg = rq.charger_piece("registre servi", registre_servi([f"Idée factice passée, {mot(k)}." for k in range(3)]),
                                       sha(registre_servi([f"Idée factice passée, {mot(k)}." for k in range(3)])))
                rendu.append(rq.assembler_proposeur(g, c, L3.synthese(), gen, reg, L3.TITRE_REGISTRE_FACTICE))
            rendu.append(rq.assembler_portier_fiche(L3.consigne_portier(), L3.contenu_fiche(c), c.identifiant, gen))
            rendu.append(rq.assembler_juge(L3.consigne_juge(), L3.contenu_fiche(c), L3.identifiant_juge(), c.identifiant, gen))
    rendu.append(rq.assembler_sonde_refus(g, cs["1"][0]))
    return rendu


def principal(sortie):
    col = colonne()
    reqs = requetes_de_l_essai()
    registres = [registre_servi([f"Idée factice passée, {mot(k)}." for k in range(3)])]
    m = mp.mesurer_faux_refus(col, reqs, registres)
    m["pieces_fixes_controlees"] = mp.controler_pieces_fixes(col, pieces_fixes())
    m["statut"] = STATUT
    m["version"] = "mesure-faux-refus-essai-na-lot-10-a-v1"
    with open(sortie, "x", encoding="utf-8") as f:
        f.write(json.dumps(m, ensure_ascii=False, sort_keys=True, indent=1) + "\n")
    print(json.dumps(m, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(principal(sys.argv[1]))
