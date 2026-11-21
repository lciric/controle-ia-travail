"""Garde du budget de la **course**, version 68 (fichier neuf, R12 ; `budget_v56.py` et `noyau_v56.py` inchangés).

Défaut corrigé (rang 0, état du code § 3, manque 3 ; exigence bloquante de la mère, R-3861) : `noyau_v56` (l. 106) construit
un `BudgetV56` neuf à chaque génération ; `course2_v56` et `course2_v59` ne reportent aucun cumul d'une génération à l'autre,
et l'étage de tests de mort a son propre plafond, sans cumul non plus. Rien ne tenait donc la dépense de **la course**.

La v68 laisse la règle d'A1 de chaque génération telle quelle (plafond S17 par génération, second programme et formule
indépendante de la ligne 11a inchangés) et ajoute, au-dessus, une garde de course qui **cumule** :

1. **Réservation au pire, avant chaque poste** : une génération réserve son plafond S17 entier, un étage son plafond
   (`plafond_etage_usd`). Si cumul + réservation dépasse le plafond de la course, le poste n'est pas lancé :
   `PlafondDeCourseAtteint` (arrêt avant toute dépense de ce poste ; jamais un repli ; le bilan dit le poste refusé).
2. **Compte, après chaque poste** : le coût réel (cumul du budget de la génération ; coûts rendus par l'étage), compté en entier,
   jamais écrêté. Un coût **inconnu** (étage arrêté, résumé sans coûts) est compté à sa réservation entière. Un coût au-delà de
   la réservation (un plafond de génération ou d'étage qui n'a pas tenu) ou un cumul au-delà du plafond de la course :
   `CumulCourseAuDela` (arrêt).
3. Un poste lancé sans réservation, ou compté deux fois : `BudgetCourseRefuse` (défaut de code, arrêt).

Par construction (1 et 2), le cumul de la course ne dépasse jamais son plafond tant que chaque poste tient sa réservation ; la
garde le vérifie au lieu de le supposer. Les décisions ne lisent que des montants (A21)."""

from .budget_v53 import EPS

VERSION = "garde-budget-course-v68"
REGLE = ("v68 : réservation au pire avant chaque poste (génération : S17 entier ; étage : son plafond) ; poste refusé si cumul + "
         "réservation > plafond de la course (arrêt avant toute dépense du poste) ; coût réel compté en entier après le poste, "
         "coût inconnu compté à la réservation ; coût au-delà de la réservation ou cumul au-delà du plafond : arrêt")


class BudgetCourseRefuse(RuntimeError):
    """Usage fautif de la garde (plafond invalide, poste non réservé, compté deux fois) : défaut de code, arrêt."""


class PlafondDeCourseAtteint(RuntimeError):
    """La réservation du poste suivant ne tient pas sous le plafond de la course : le poste n'est pas lancé (arrêt propre)."""


class CumulCourseAuDela(RuntimeError):
    """Un poste a coûté plus que sa réservation, ou le cumul dépasse le plafond de la course : arrêt."""


def _reel(v, strict=False):
    return isinstance(v, (int, float)) and not isinstance(v, bool) and (float(v) > 0 if strict else float(v) >= 0)


class GardeBudgetCourseV68:
    def __init__(self, plafond_course_usd):
        if not _reel(plafond_course_usd, strict=True):
            raise BudgetCourseRefuse(f"plafond de la course : réel > 0 exigé (reçu {plafond_course_usd!r}), aucun défaut")
        self.plafond = float(plafond_course_usd)
        self.cumul = 0.0
        self.en_cours = None  # (poste, réservation)
        self.journal = []
        self.postes = set()

    def reserver(self, poste, montant_usd):
        if self.en_cours is not None:
            raise BudgetCourseRefuse(f"poste {self.en_cours[0]} encore en cours : {poste} ne peut pas être réservé")
        if poste in self.postes:
            raise BudgetCourseRefuse(f"poste {poste} déjà joué : jamais rejoué")
        if not _reel(montant_usd):
            raise BudgetCourseRefuse(f"réservation de {poste} : réel ≥ 0 exigé (reçu {montant_usd!r})")
        montant = float(montant_usd)
        if self.cumul + montant > self.plafond + EPS:
            self.journal.append({"quoi": "refuse", "poste": poste, "reservation_usd": round(montant, 6),
                                 "cumul_usd": round(self.cumul, 6), "plafond_course_usd": self.plafond})
            raise PlafondDeCourseAtteint(
                f"plafond de la course atteint : {poste} réserve {montant:.2f} USD, cumul {self.cumul:.2f} USD, plafond de la "
                f"course {self.plafond:.2f} USD : poste non lancé, course arrêtée avant toute dépense de ce poste")
        self.en_cours = (poste, montant)
        self.postes.add(poste)
        self.journal.append({"quoi": "reserve", "poste": poste, "reservation_usd": round(montant, 6), "cumul_usd": round(self.cumul, 6)})
        return montant

    def compter(self, poste, cout_usd, inconnu=False):
        """Coût réel du poste en cours (None ou `inconnu` : la réservation entière). Lève `CumulCourseAuDela` après l'avoir
        noté si le coût dépasse la réservation ou si le cumul dépasse le plafond."""
        if self.en_cours is None or self.en_cours[0] != poste:
            raise BudgetCourseRefuse(f"poste {poste} compté sans réservation en cours ({self.en_cours!r})")
        reserve = self.en_cours[1]
        inconnu = bool(inconnu) or cout_usd is None
        if not inconnu and not _reel(cout_usd):
            raise BudgetCourseRefuse(f"coût de {poste} : réel ≥ 0 exigé (reçu {cout_usd!r})")
        cout = reserve if inconnu else float(cout_usd)
        self.cumul += cout  # jamais écrêté
        self.en_cours = None
        self.journal.append({"quoi": "compte", "poste": poste, "cout_usd": round(cout, 6), "cout_inconnu": inconnu,
                             "reservation_usd": round(reserve, 6), "cumul_usd": round(self.cumul, 6)})
        if cout > reserve + EPS:
            raise CumulCourseAuDela(f"{poste} a coûté {cout:.6f} USD, au-delà de sa réservation {reserve:.6f} USD (un plafond n'a "
                                    "pas tenu) : arrêt")
        if self.cumul > self.plafond + EPS:
            raise CumulCourseAuDela(f"cumul de la course {self.cumul:.6f} USD au-delà de son plafond {self.plafond:.6f} USD : arrêt")
        return cout

    def noter_arret(self, poste, cout_usd=None):
        """Chemin d'arrêt (exception pendant le poste) : le coût est compté s'il est connu, sinon la réservation ; ne lève
        jamais (l'exception d'origine reste celle qui est rapportée)."""
        if self.en_cours is None or self.en_cours[0] != poste:
            return None
        reserve = self.en_cours[1]
        inconnu = not _reel(cout_usd) if cout_usd is not None else True
        cout = reserve if inconnu else float(cout_usd)
        self.cumul += cout
        self.en_cours = None
        self.journal.append({"quoi": "compte-a-l-arret", "poste": poste, "cout_usd": round(cout, 6), "cout_inconnu": inconnu,
                             "reservation_usd": round(reserve, 6), "cumul_usd": round(self.cumul, 6)})
        return cout

    def etat(self):
        return {"version": VERSION, "regle": REGLE, "plafond_course_usd": self.plafond, "cumul_usd": round(self.cumul, 6),
                "reste_usd": round(self.plafond - self.cumul, 6), "depassement_usd": round(max(0.0, self.cumul - self.plafond), 6),
                "journal": list(self.journal)}


def rejouer_journal_course_v68(etat):
    """Second calcul, sur le seul journal écrit au bilan : le cumul est la somme des coûts comptés, jamais au-delà du plafond,
    chaque coût sous sa réservation ; rend le cumul recalculé. Lève `CumulCourseAuDela` sinon."""
    total = 0.0
    for j in etat["journal"]:
        if j["quoi"] in ("compte", "compte-a-l-arret"):
            if j["cout_usd"] > j["reservation_usd"] + 1e-6:
                raise CumulCourseAuDela(f"rejeu : {j['poste']} au-delà de sa réservation")
            total += j["cout_usd"]
    if abs(total - etat["cumul_usd"]) > 1e-5:
        raise CumulCourseAuDela(f"rejeu : cumul recalculé {total:.6f} ≠ cumul écrit {etat['cumul_usd']:.6f}")
    if total > etat["plafond_course_usd"] + 1e-6:
        raise CumulCourseAuDela(f"rejeu : cumul {total:.6f} au-delà du plafond de la course")
    return round(total, 6)


__all__ = ("GardeBudgetCourseV68", "PlafondDeCourseAtteint", "CumulCourseAuDela", "BudgetCourseRefuse",
           "rejouer_journal_course_v68", "REGLE", "VERSION")
