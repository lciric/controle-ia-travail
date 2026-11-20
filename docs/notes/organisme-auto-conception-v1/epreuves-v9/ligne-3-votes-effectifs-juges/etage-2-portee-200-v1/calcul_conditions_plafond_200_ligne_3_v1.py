"""Calcul versionné des conditions du plafond de l'étage 2 de la ligne 3, à 200 témoins — v1.

Ligne 3 de l'organisme v9 (votes effectifs des juges croisés, mesurés sur témoins plantés),
étage 2 à 200 témoins, plafond d'arrêt du compteur lu à 88,36 USD (GO-2026-11-20-26 ;
additif 3 v3, § 4.2, et son nœud 3, § 7 ; GO-2026-11-20-36, point 2 : « conditions du
plafond par calcul versionné sans devis neuf »). Pièce d'instrument (classe B).
Processeur seul, aucun appel de modèle, aucune dépense.

Nom neuf (règle R12), écrit à partir de calcul_devis_ligne_3_v3.py, qui n'est pas modifié :
mêmes entrées, vérifiées par empreinte ; mêmes tarifs par appel ; mêmes trois cas
(estimation, c'est-à-dire le cas attendu ; haut ; pire) ; même plan d'appels par témoin
(plomberie P : deux témoins de la version 2, deux juges ; bloc A : chaque juge une fois sur
chaque témoin ; bloc B : une lecture de plus par le juge Opus, deux de plus par le juge
Argon, entrelacées par témoin, la moitié « lecture » d'abord).

Ce qui est neuf :
- toute grandeur est une fraction exacte (fractions.Fraction) ; le plafond et la réserve
  sont des centimes entiers ; aucune comparaison de seuil ne passe par un flottant ; la
  sortie ne porte aucun flottant (décimaux écrits en texte, arrondis au demi pair sur la
  fraction exacte) ;
- deux lectures de la règle du compteur, toutes deux rendues :
  (a) « formule du devis » : la forme fermée du calcul v3 (un groupe d'appels est dit
      complet si le cumul compté APRÈS son dernier appel tient sous le plafond moins la
      réserve) ; elle ne dépend pas de l'ordre des appels dans le bloc A ; elle est
      prudente ;
  (b) « envoi par envoi » : la règle elle-même, jouée appel par appel (un envoi part si
      le cumul compté AVANT lui, plus la réserve de 0,60 USD, ne dépasse pas le plafond) ;
      c'est elle qui dit à quel témoin, à quel bloc et à quel rendu le compteur coupe ;
- l'issue écrite d'avance du pire cas à 200 (condition (ii)), le cas haut et le cas
  attendu ; les chiffres des conditions (i) et (iii) à 200 ;
- un contrôle à 100 témoins et 25 USD : les clés du compteur, du plafond, des scénarios à
  100 et 200 et des facteurs de la sortie v3 sont recalculées et comparées valeur par
  valeur (sortie v3 lue par empreinte) ; tout écart arrête le programme.

Hypothèses de modèle, dites (la lettre ne les fixe pas) :
- chaque appel d'un juge coûte le tarif moyen par appel de ce juge à la course v9, multiplié
  par le facteur du cas (comme au calcul v3) ;
- dans le bloc A, l'ordre est, par témoin, juge Opus puis juge Argon ; il ne joue que sur la
  lecture (b), à la frontière du bloc A ; l'ordre des témoins du bloc A est tiré à graine,
  la moitié d'un témoin coupé dans le bloc A n'est donc pas connue d'avance ;
- un envoi refusé (refusé, coupé par un délai, en erreur, sans coût lisible, engagement
  sans règlement) est compté 0,60 USD puis rejoué une fois, avec succès, à son coût ; les
  refus tombent au début du plan, avant toute coupure ;
- « tous refusés » : chaque envoi et son rejeu sont refusés (rendu « absent »).

Usage (depuis la racine du dépôt) : python3 -I -B CE_FICHIER > SORTIE.json
Aucun argument : le résultat sort sur la sortie standard, en UTF-8.
"""

import hashlib
import json
import sys
from decimal import Decimal
from fractions import Fraction

VERSION = "calcul-conditions-plafond-200-ligne-3-v1"

MANIFESTE = "runs/20261119-094145-course-auto-conception-v9/manifeste-lanceur-fin.json"
MANIFESTE_SHA = "28bc36df390d8481fb5bd9118cf764843ffea60856412d825ecbf08e7cee5be7"
EPREUVE = "docs/notes/organisme-auto-conception-v1/course-v4/epreuve-temoins-reelle-auto-conception-v9.json"
EPREUVE_SHA = "e7837f4c40bca9aaed7ae0d3e8bdb51f9f36284ffb21c677575368699a61ca84"
SORTIE_V3 = "docs/notes/organisme-auto-conception-v1/epreuves-v9/ligne-3-votes-effectifs-juges/calcul-devis-ligne-3-v3.json"
SORTIE_V3_SHA = "1a13fe2756a5587398e122c17700fab6472350d6c38975d58c1c3cf337ad6cf6"
APPELS_EPREUVE_TEMOINS = 33  # onze témoins, deux juges et l'aiguilleur (calcul v3)

SESSION_C = 60  # réserve et coût compté d'un envoi refusé : plafond de session d'un appel de juge
PLAFOND_200_C = 8836  # GO-2026-11-20-26 ; additif 3 v3, § 4.2
PLAFOND_100_C = 2500  # GO-2026-11-19-66 ; texte l. 193 (contrôle à 100)
N_200 = 200
N_100 = 100
SEUIL_LECTURE = 40  # texte l. 337 ; gardé à 40 à 200 (additif 3, nœud 2 ; GO-2026-11-20-36)
FACTEUR_ARRET_PLOMBERIE = 3  # texte l. 378 : « au-delà de trois fois le tarif des cartes »

JUGES = ("juge-opus", "juge-argon")
NOM = {"juge-opus": "juge Opus", "juge-argon": "juge Argon"}
REPETITIONS_B = {"juge-opus": 1, "juge-argon": 2}
TEMOINS_PLOMBERIE = 2
REFUS_TABULES_100 = (0, 1, 2, 3, 5, 10)  # ceux du calcul v3
REFUS_TABULES_200 = (0, 1, 2, 3, 5, 10, 20, 40, 60, 80, 100)
EPSILON_FRONTIERE = Fraction(1, 10 ** 12)

MANQUE = ("non concluant par manque de témoins (rang 1 de la table de l'étage 2) ; "
          "jamais lu comme un « non »")
COUPE_SANS_MANQUE = ("coupure sans manque de témoins : la moitié « lecture » garde au moins 40 "
                     "témoins complets, le compteur ne donne pas le rang 1 ; la table de l'étage 2 "
                     "se lit selon ses rangs ; bras R sur les témoins complets de la moitié "
                     "« lecture » ; ρ, ρ′ et ρ′ − ρ, pour cette comparaison, sur les seuls témoins "
                     "complets pour les trois rendus de plus, le même ensemble pour les deux juges "
                     "(texte l. 293, l. 388)")
ENTIER = "aucune coupure : le plan entier est servi"


# ---------------------------------------------------------------- gardes d'exactitude

def centimes(x):
    """Un seuil en centimes entiers ; refuse un flottant (garde)."""
    if isinstance(x, bool) or not isinstance(x, int):
        raise TypeError("un seuil se donne en centimes entiers, jamais en flottant")
    if x < 0:
        raise ValueError("un seuil en centimes est positif ou nul")
    return x


def exacte(x):
    """Une grandeur exacte (entier ou fraction) ; refuse un flottant et un décimal (garde)."""
    if isinstance(x, bool) or not isinstance(x, (int, Fraction)):
        raise TypeError("grandeur exacte attendue (entier ou fraction), jamais un flottant")
    return Fraction(x)


def depuis_json(x):
    """Un nombre lu dans un JSON (décimal ou entier) en fraction exacte ; refuse un flottant."""
    if isinstance(x, bool) or not isinstance(x, (int, Decimal)):
        raise TypeError("nombre lu attendu en décimal exact ou en entier")
    return Fraction(x)


def arrondi(x, chiffres):
    """Arrondi au demi pair de la fraction exacte, rendu en décimal exact."""
    q = round(exacte(x) * 10 ** chiffres)
    return Decimal(q).scaleb(-chiffres)


def texte(x, chiffres=4):
    return format(arrondi(x, chiffres), f".{chiffres}f")


def fr(x, chiffres=2):
    return texte(x, chiffres).replace(".", ",")


def verifier_sans_flottant(objet, chemin="sortie"):
    """Garde : aucun flottant dans la sortie."""
    if isinstance(objet, float):
        raise SystemExit(f"flottant dans la sortie : {chemin}")
    if isinstance(objet, dict):
        for cle, valeur in objet.items():
            if not isinstance(cle, str):
                raise SystemExit(f"clé non textuelle dans la sortie : {chemin}")
            verifier_sans_flottant(valeur, f"{chemin}.{cle}")
    elif isinstance(objet, (list, tuple)):
        for i, valeur in enumerate(objet):
            verifier_sans_flottant(valeur, f"{chemin}[{i}]")
    elif not (objet is None or isinstance(objet, (str, int, bool))):
        raise SystemExit(f"type non permis dans la sortie : {chemin}")


# ---------------------------------------------------------------- entrées

def lire(racine, chemin, empreinte):
    """Lit un JSON par empreinte ; arrêt si l'empreinte diffère (garde)."""
    with open(f"{racine}/{chemin}", "rb") as f:
        octets = f.read()
    vu = hashlib.sha256(octets).hexdigest()
    if vu != empreinte:
        raise SystemExit(f"empreinte inattendue pour {chemin} : {vu}")
    return json.loads(octets.decode("utf-8"), parse_float=Decimal)


def tarifs(racine):
    m = lire(racine, MANIFESTE, MANIFESTE_SHA)
    e = lire(racine, EPREUVE, EPREUVE_SHA)
    usd = m["cout_reel"]["par_role_usd"]
    appels = m["cout_reel"]["appels_par_role"]
    roles = JUGES + ("aiguilleur",)
    par_appel = {r: depuis_json(usd[r]) / appels[r] for r in roles}
    devis_v1 = {r: depuis_json(m["ecart_au_devis_v1"]["par_role"][r]["devis_usd"]) for r in JUGES}
    reel_sur_devis = {r: depuis_json(usd[r]) / devis_v1[r] for r in JUGES}
    moyen_temoin = depuis_json(e["cout_usd"]) / APPELS_EPREUVE_TEMOINS
    moyen_carte = sum(par_appel[r] for r in roles) / 3
    return {
        "par_appel": {j: par_appel[j] for j in JUGES},
        "aiguilleur_par_appel": par_appel["aiguilleur"],
        "reel_sur_devis": reel_sur_devis,
        "facteurs": {"estimation": moyen_temoin / moyen_carte, "haut": Fraction(1),
                     "pire": max(reel_sur_devis[j] for j in JUGES)},
    }


# ---------------------------------------------------------------- plan et coûts

def plan_appels(n):
    if not isinstance(n, int) or n <= 0 or n % 2:
        raise ValueError("nombre de témoins pair et positif attendu")
    return {j: {"P": TEMOINS_PLOMBERIE, "A": n, "B": n * REPETITIONS_B[j]} for j in JUGES}


def cout_du_plan(n, par_appel, facteur):
    facteur = exacte(facteur)
    par_bras, par_juge = {}, {}
    for j, bras in plan_appels(n).items():
        par_juge[j] = Fraction(0)
        for nom, k in bras.items():
            c = k * exacte(par_appel[j]) * facteur
            par_bras[nom] = par_bras.get(nom, Fraction(0)) + c
            par_juge[j] += c
    return par_bras, par_juge, sum(par_juge.values())


def sequence(n):
    """Ordre des envois prévus : (bloc, rang du témoin dans l'ordre du bloc, juge, rendu)."""
    for t in range(1, TEMOINS_PLOMBERIE + 1):
        for j in JUGES:
            yield ("P", t, j, 1)
    for t in range(1, n + 1):
        for j in JUGES:
            yield ("A", t, j, 1)
    for t in range(1, n + 1):
        for j in JUGES:
            for k in range(REPETITIONS_B[j]):
                yield ("B", t, j, 2 + k)


# ---------------------------------------------------------------- compteur, envoi par envoi

def simuler(n, plafond_c, couts, refus=0, tous_refuses=False, session_c=SESSION_C):
    """Joue la règle du compteur envoi par envoi.

    Un envoi part si cumul compté + réserve <= plafond (texte l. 382 : « aucun envoi ne part
    si le cumul compté plus cet engagement dépasse » le plafond). Un envoi refusé est compté
    la réserve, jamais zéro, puis rejoué une fois. Un coût relevé au-dessus de la réserve
    arrête le programme après cet envoi.
    """
    plafond = Fraction(centimes(plafond_c), 100)
    session = Fraction(centimes(session_c), 100)
    couts = {j: exacte(couts[j]) for j in JUGES}
    if not isinstance(refus, int) or refus < 0:
        raise ValueError("nombre d'envois refusés entier et positif attendu")
    cumul, envois, refus_comptes, restants = Fraction(0), 0, 0, refus
    obtenus, coupure, arret, dernier = set(), None, None, None
    for appel in sequence(n):
        bloc, t, j, rendu = appel
        if tous_refuses:
            essais = [None, None]
        elif restants > 0:
            essais = [None, couts[j]]
            restants -= 1
        else:
            essais = [couts[j]]
        for rang, c in enumerate(essais, 1):
            if cumul + session > plafond:
                coupure = {"bloc": bloc, "temoin": t, "juge": j, "rendu": rendu, "essai": rang,
                           "cumul_compte_avant": cumul}
                break
            envois += 1
            cumul += session if c is None else c
            dernier = {"bloc": bloc, "temoin": t, "juge": j, "rendu": rendu, "essai": rang,
                       "refuse": c is None}
            if c is None:
                refus_comptes += 1
                continue
            obtenus.add(appel)
            if c > session:
                arret = {"bloc": bloc, "temoin": t, "juge": j, "rendu": rendu,
                         "motif": "coût relevé au-dessus du plafond de session : arrêt"}
            break
        if coupure is not None or arret is not None:
            break
    moitie = n // 2
    b_complets = [t for t in range(1, n + 1)
                  if all(("B", t, j, 2 + k) in obtenus for j in JUGES for k in range(REPETITIONS_B[j]))]
    b_partiels = [t for t in range(1, n + 1) if t not in b_complets
                  and any(("B", t, j, 2 + k) in obtenus for j in JUGES for k in range(REPETITIONS_B[j]))]
    return {
        "n": n, "plafond_c": plafond_c, "envois_partis": envois, "rendus_obtenus": len(obtenus),
        "envois_refuses_comptes": refus_comptes, "cumul": cumul, "coupure": coupure,
        "arret": arret, "dernier": dernier, "obtenus": obtenus,
        "plomberie_complete": all(("P", t, j, 1) in obtenus
                                  for t in range(1, TEMOINS_PLOMBERIE + 1) for j in JUGES),
        "A_complets": sum(1 for t in range(1, n + 1) if all(("A", t, j, 1) in obtenus for j in JUGES)),
        "B_complets": len(b_complets),
        "lecture_complets": sum(1 for t in b_complets if t <= moitie),
        "etalonnage_complets": sum(1 for t in b_complets if t > moitie),
        "B_partiels": b_partiels,
        "envois_prevus": sum(p["P"] + p["A"] + p["B"] for p in plan_appels(n).values()),
    }


def verdict(sim):
    if not sim["plomberie_complete"] or sim["A_complets"] < sim["n"]:
        return "manque", MANQUE + " ; coupure avant la fin du bloc A (texte l. 384, dernière phrase)"
    if sim["lecture_complets"] < SEUIL_LECTURE:
        return "manque", MANQUE
    if sim["coupure"] is None and sim["arret"] is None:
        return "entier", ENTIER
    return "coupe_sans_manque", COUPE_SANS_MANQUE


def moitie_de(bloc, t, n):
    if bloc == "B":
        return ("lecture", t) if t <= n // 2 else ("étalonnage", t - n // 2)
    return (None, None)


def decrire_envoi(e, n):
    if e is None:
        return None
    moitie, rang = moitie_de(e["bloc"], e["temoin"], n)
    d = {"bloc": e["bloc"], "temoin_dans_l_ordre_du_bloc": e["temoin"], "juge": NOM[e["juge"]],
         "rendu": e["rendu"], "essai": e["essai"]}
    if e["bloc"] == "B":
        d["moitie"] = moitie
        d["rang_dans_la_moitie"] = rang
    elif e["bloc"] == "A":
        d["moitie"] = "non connue d'avance (ordre du bloc A tiré à graine)"
    if "refuse" in e:
        d["refuse"] = e["refuse"]
    if "cumul_compte_avant" in e:
        d["cumul_compte_avant_usd"] = texte(e["cumul_compte_avant"])
    return d


def resume(sim):
    cle, texte_verdict = verdict(sim)
    return {
        "envois_partis": sim["envois_partis"], "envois_prevus": sim["envois_prevus"],
        "rendus_obtenus": sim["rendus_obtenus"],
        "envois_refuses_comptes": sim["envois_refuses_comptes"],
        "cumul_compte_a_l_arret_usd": texte(sim["cumul"]),
        "dernier_envoi_parti": decrire_envoi(sim["dernier"], sim["n"]),
        "premier_envoi_interdit_par_la_regle": decrire_envoi(sim["coupure"], sim["n"]),
        "arret_par_cout_releve": sim["arret"] and {k: (NOM[v] if k == "juge" else v)
                                                   for k, v in sim["arret"].items()},
        "complets": {"plomberie": sim["plomberie_complete"], "bloc_A": sim["A_complets"],
                     "bloc_B": sim["B_complets"], "bloc_B_moitie_lecture": sim["lecture_complets"],
                     "bloc_B_moitie_etalonnage": sim["etalonnage_complets"]},
        "temoins_partiels_au_bloc_B": sim["B_partiels"],
        "verdict": cle, "verdict_en_clair": texte_verdict,
    }


def balayer_refus(n, plafond_c, couts):
    """Envoi par envoi, pour r = 0, 1, 2… envois refusés, jusqu'à la coupure dans le bloc A."""
    lignes, r = [], 0
    while True:
        s = simuler(n, plafond_c, couts, refus=r)
        lignes.append((r, s))
        if not s["plomberie_complete"] or s["A_complets"] < n:
            return lignes
        r += 1


def seuils_de_refus(n, lignes):
    def plus_grand(cond):
        vus = [r for r, s in lignes if cond(s)]
        return max(vus) if vus else None
    return {
        "sans_aucune_coupure": plus_grand(lambda s: s["coupure"] is None and s["arret"] is None),
        "moitie_lecture_entiere_au_bloc_B": plus_grand(lambda s: s["lecture_complets"] == n // 2),
        "moitie_lecture_au_seuil_de_40": plus_grand(lambda s: s["lecture_complets"] >= SEUIL_LECTURE),
        "plomberie_et_bloc_A_complets": plus_grand(lambda s: s["plomberie_complete"] and s["A_complets"] == n),
    }


# ---------------------------------------------------------------- formule du devis (calcul v3, exacte)

class Formule:
    """La forme fermée du calcul v3, en fractions exactes."""

    def __init__(self, n, plafond_c, par_appel, comme_v3=False):
        """comme_v3 : le calcul v3 lit le coût de la plomberie et celui du bloc A au cas haut
        dans sa sortie arrondie à quatre décimales (base["haut"]["par_bras_usd"]) avant ses
        formules du plafond ; ce mode le reproduit, pour le seul contrôle à 100."""
        self.n = n
        self.plafond = Fraction(centimes(plafond_c), 100)
        self.session = Fraction(SESSION_C, 100)
        self.disponible = self.plafond - self.session
        self.par_appel = {j: exacte(par_appel[j]) for j in JUGES}
        paire = sum(self.par_appel.values())
        self.p = TEMOINS_PLOMBERIE * paire
        self.a = n * paire
        if comme_v3:
            self.p = Fraction(arrondi(self.p, 4))
            self.a = Fraction(arrondi(self.a, 4))
        self.b = sum(self.par_appel[j] * REPETITIONS_B[j] for j in JUGES)

    def facteur_pour_b_complets(self, k):
        return self.disponible / (self.p + self.a + k * self.b)

    def facteur_bloc_a(self):
        return self.disponible / (self.p + self.a)

    def temoins_b_complets(self, facteur, refus=0):
        facteur = exacte(facteur)
        reste = self.disponible - refus * self.session - facteur * (self.p + self.a)
        if reste < 0:
            return 0
        return min(self.n, reste // (facteur * self.b))

    def refus_supportes(self, total):
        marge = self.disponible - exacte(total)
        return 0 if marge < 0 else marge // self.session

    def envois_si_tous_refuses(self):
        plafond_c = int(self.plafond * 100)
        k = 0
        while k * SESSION_C + SESSION_C <= plafond_c:
            k += 1
        return k

    def temoins_au_plus(self, reserve, borne_haute=2000):
        borne = self.plafond - (self.session if reserve else 0)
        ok = [m for m in range(2, borne_haute + 1, 2)
              if cout_du_plan(m, self.par_appel, 1)[2] <= borne]
        return max(ok) if ok else None


def facteur_exact(formule, k_b):
    """Envoi par envoi : plus grand facteur qui laisse partir le dernier envoi du groupe.

    Groupe : plomberie et bloc A (k_b = None), ou en plus le bloc B sur ses k_b premiers
    témoins. Le dernier envoi du groupe est celui du juge Argon (ordre supposé, en tête).
    """
    total = formule.p + formule.a + (0 if k_b is None else k_b * formule.b)
    return formule.disponible / (total - formule.par_appel[JUGES[-1]])


def groupe_complet(sim, k_b):
    if not sim["plomberie_complete"] or sim["A_complets"] < sim["n"]:
        return False
    return True if k_b is None else sim["B_complets"] >= k_b


def verifier_frontiere(n, plafond_c, par_appel, f, k_b):
    """Garde : le facteur de frontière laisse le groupe complet, un epsilon de plus le coupe."""
    dedans = simuler(n, plafond_c, {j: par_appel[j] * f for j in JUGES})
    dehors = simuler(n, plafond_c, {j: par_appel[j] * (f + EPSILON_FRONTIERE) for j in JUGES})
    if not groupe_complet(dedans, k_b) or groupe_complet(dehors, k_b):
        raise SystemExit(f"frontière non vérifiée par la simulation (n={n}, groupe={k_b})")
    return True


# ---------------------------------------------------------------- contrôle à 100 contre la sortie v3

def valeurs_v3_recalculees(t, comme_v3=True):
    """Les clés de la sortie v3 recalculées en exact, avec le nombre de décimales du v3.

    comme_v3 : coûts de la plomberie et du bloc A arrondis à quatre décimales avant les
    formules du plafond, comme le fait le calcul v3 ; sinon, tout exact."""
    pa, fa = t["par_appel"], t["facteurs"]
    f100 = Formule(N_100, PLAFOND_100_C, pa, comme_v3=comme_v3)
    tot = {}
    for cas in fa:
        par_bras, par_juge, total = cout_du_plan(N_100, pa, fa[cas])
        # Le calcul v3 lit aussi les totaux dans sa sortie arrondie à quatre décimales.
        tot[cas] = (par_bras, par_juge, Fraction(arrondi(total, 4)) if comme_v3 else total)
    v = {}
    c = "compteur_d_arret."
    v[c + "cout_compte_d_un_envoi_refuse_ou_sans_cout_lisible_usd"] = (Fraction(SESSION_C, 100), 2)
    v[c + "cumul_au_pire_cas_plomberie_bloc_A_et_18_temoins_du_bloc_B_usd"] = (
        fa["pire"] * (f100.p + f100.a + 18 * f100.b), 4)
    k = f100.envois_si_tous_refuses()
    v[c + "envois_qui_partent_si_tous_sont_refuses"] = (k, None)
    v[c + "cumul_compte_a_l_arret_si_tous_sont_refuses_usd"] = (Fraction(k * SESSION_C, 100), 2)
    for cas in ("estimation", "haut", "pire"):
        v[c + "envois_refuses_que_la_base_supporte_sans_coupure." + cas] = (
            f100.refus_supportes(tot[cas][2]), None)
    for r in REFUS_TABULES_100:
        v[c + f"temoins_B_complets_au_pire_cas_selon_les_envois_refuses.{r}"] = (
            f100.temoins_b_complets(fa["pire"], r), None)
        v[c + f"temoins_B_complets_au_cas_haut_selon_les_envois_refuses.{r}"] = (
            f100.temoins_b_complets(1, r), None)
    p = "plafond."
    v[p + "usd"] = (Fraction(PLAFOND_100_C, 100), 2)
    v[p + "reserve_plafond_de_session_usd"] = (Fraction(SESSION_C, 100), 2)
    v[p + "disponible_avant_le_dernier_appel_usd"] = (f100.disponible, 4)
    v[p + "haut_depasse_le_plafond"] = (tot["haut"][2] > f100.plafond, None)
    v[p + "haut_plus_reserve_depasse_le_plafond"] = (tot["haut"][2] + f100.session > f100.plafond, None)
    v[p + "pire_depasse_le_plafond"] = (tot["pire"][2] > f100.plafond, None)
    v[p + "marge_nominale_sur_le_haut"] = (f100.plafond / tot["haut"][2], 4)
    v[p + "marge_effective_sur_le_haut"] = (f100.disponible / tot["haut"][2], 4)
    v[p + "facteur_que_le_bloc_A_supporte_apres_plomberie"] = (f100.facteur_bloc_a(), 4)
    for kb in (40, 50, 100):
        v[p + f"facteur_jusqu_ou_B_est_complet_sur_k_temoins.{kb}"] = (f100.facteur_pour_b_complets(kb), 4)
    for cas in ("estimation", "haut", "pire"):
        v[p + f"temoins_B_complets_selon_le_facteur.{cas}"] = (f100.temoins_b_complets(fa[cas]), None)
    v[p + "temoins_au_plus_au_cas_haut.avec_reserve"] = (f100.temoins_au_plus(True, 400), None)
    v[p + "temoins_au_plus_au_cas_haut.sans_reserve"] = (f100.temoins_au_plus(False, 400), None)
    v[p + "plomberie_bloc_A_et_B_sur_40_temoins_au_pire_usd"] = (
        fa["pire"] * (f100.p + f100.a + 40 * f100.b), 4)
    br = p + "base_reduite_plomberie_et_bloc_A."
    v[br + "appels"] = (sum(TEMOINS_PLOMBERIE + N_100 for _ in JUGES), None)
    v[br + "estimation_usd"] = (fa["estimation"] * (f100.p + f100.a), 4)
    v[br + "haut_usd"] = (f100.p + f100.a, 4)
    v[br + "pire_usd"] = (fa["pire"] * (f100.p + f100.a), 4)
    for n in (N_100, N_200):
        s = f"scenarios_par_nombre_de_temoins.{n}."
        v[s + "appels_total"] = (sum(sum(b.values()) for b in plan_appels(n).values()), None)
        for cas in ("estimation", "haut", "pire"):
            par_bras, par_juge, total = cout_du_plan(n, pa, fa[cas])
            v[s + f"{cas}.total_usd"] = (total, 4)
            for nom, x in par_bras.items():
                v[s + f"{cas}.par_bras_usd.{nom}"] = (x, 4)
            for j, x in par_juge.items():
                v[s + f"{cas}.par_juge_usd.{j}"] = (x, 4)
    v["facteurs.estimation"] = (fa["estimation"], 4)
    v["facteurs.pire"] = (fa["pire"], 4)
    v["cout_du_bloc_B_par_temoin_au_cas_haut_usd"] = (f100.b, 6)
    v["cout_reel_v9.paire_de_juges_par_carte_usd"] = (sum(pa.values()), 6)
    return v


def _valeur_v3(sortie_v3, chemin):
    attendu = sortie_v3
    for morceau in chemin.split("."):
        attendu = attendu[morceau]
    return attendu


def comparer_a_v3(sortie_v3, recalculees):
    """Compare chaque valeur recalculée à celle de la sortie v3, en décimal exact."""
    differentes = []
    for chemin, (valeur, chiffres) in sorted(recalculees.items()):
        attendu = _valeur_v3(sortie_v3, chemin)
        if isinstance(valeur, bool) or isinstance(attendu, bool):
            egal = valeur is attendu
        elif chiffres is None:
            egal = isinstance(attendu, int) and valeur == attendu
        else:
            egal = arrondi(valeur, chiffres) == Decimal(attendu)
        if not egal:
            differentes.append(chemin)
    return {"cles_comparees": len(recalculees), "cles_differentes": differentes,
            "toutes_egales": not differentes}


# ---------------------------------------------------------------- à 200 : les trois conditions

def bloc_cas(nom, t, formule, n, plafond_c):
    pa, f = t["par_appel"], t["facteurs"][nom]
    par_bras, par_juge, total = cout_du_plan(n, pa, f)
    couts = {j: pa[j] * f for j in JUGES}
    sim0 = simuler(n, plafond_c, couts)
    lignes = balayer_refus(n, plafond_c, couts)
    par_r = dict(lignes)
    tab = {}
    for r in REFUS_TABULES_200:
        s = par_r[r] if r in par_r else simuler(n, plafond_c, couts, refus=r)
        tab[str(r)] = {"envois_partis": s["envois_partis"], "bloc_A_complets": s["A_complets"],
                       "bloc_B_complets": s["B_complets"], "moitie_lecture_complets": s["lecture_complets"],
                       "verdict": verdict(s)[0],
                       "formule_du_devis_bloc_B_complets": formule.temoins_b_complets(f, r)}
    return {
        "facteur": texte(f), "facteur_exact": str(f),
        "total_du_plan_usd": texte(total), "total_du_plan_exact_usd": str(total),
        "par_bras_usd": {k: texte(x) for k, x in sorted(par_bras.items())},
        "par_juge_usd": {NOM[j]: texte(x) for j, x in par_juge.items()},
        "par_appel_usd": {NOM[j]: texte(couts[j], 6) for j in JUGES},
        "total_depasse_le_plafond": total > formule.plafond,
        "total_depasse_le_plafond_moins_la_reserve": total > formule.disponible,
        "envoi_par_envoi_sans_refus": resume(sim0),
        "formule_du_devis": {
            "bloc_B_complets": formule.temoins_b_complets(f),
            "envois_refuses_supportes_sans_coupure": formule.refus_supportes(total)},
        "selon_les_envois_refuses": tab,
        "seuils_de_refus_envoi_par_envoi": seuils_de_refus(n, lignes),
    }


def issue_du_pire(cas_pire, sim, formule, n):
    """Condition (ii) : l'issue du pire cas, écrite d'avance, à partir de la simulation."""
    d, c = sim["dernier"], sim["coupure"]
    cle, _ = verdict(sim)
    moitie_d, rang_d = moitie_de(d["bloc"], d["temoin"], n)
    lu = [
        "plomberie : quatre appels, complets" if sim["plomberie_complete"] else "plomberie incomplète",
        f"bloc A : {sim['A_complets']} témoins complets pour les deux juges sur {n} ; ρ entre juges, "
        "nombre de votes effectifs, table par juge ; bras U, C, F, P, S-Opus et S-Argon sur la moitié "
        f"« lecture » ({n // 2} témoins)",
        f"bloc B : {sim['B_complets']} témoins complets pour les trois rendus de plus "
        f"({sim['lecture_complets']} de la moitié « lecture », {sim['etalonnage_complets']} de la moitié "
        "« étalonnage ») ; bras R-Argon et R-Opus-2 sur les témoins complets de la moitié « lecture » ; "
        f"ρ, ρ′ et ρ′ − ρ, pour cette comparaison, sur les {sim['B_complets']} témoins complets, "
        "le même ensemble pour les deux juges (texte l. 293)",
        f"seuil de {SEUIL_LECTURE} témoins complets dans la moitié « lecture » : "
        + ("tenu" if sim["lecture_complets"] >= SEUIL_LECTURE else "non tenu")
        + f" ({sim['lecture_complets']})",
    ]
    manque = []
    for tt in range(sim["B_complets"] + 1, n + 1):
        absents = [f"rendu {2 + k} du {NOM[j]}" for j in JUGES for k in range(REPETITIONS_B[j])
                   if ("B", tt, j, 2 + k) not in sim["obtenus"]]
        partis = [f"rendu {2 + k} du {NOM[j]}" for j in JUGES for k in range(REPETITIONS_B[j])
                  if ("B", tt, j, 2 + k) in sim["obtenus"]]
        moitie_t, rang_t = moitie_de("B", tt, n)
        ligne = (f"témoin {tt} de l'ordre du bloc B (moitié « {moitie_t} », rang {rang_t}) : "
                 f"non partis : {', '.join(absents)}")
        if partis:
            ligne += (f" ; partis : {', '.join(partis)}, déposés, hors de l'ensemble des témoins "
                      "complets")
        manque.append(ligne)
    reste_sous_plafond = formule.plafond - sim["cumul"]
    phrase = (
        f"Au pire cas du devis (tarif des cartes × {fr(Fraction(cas_pire['facteur_exact']), 4)}), "
        f"le plan de {sim['envois_prevus']} envois coûterait {fr(Fraction(cas_pire['total_du_plan_exact_usd']), 4)} USD, "
        f"au-dessus du plafond de {fr(formule.plafond)} USD. Le compteur coupe au bloc {c['bloc']} : "
        f"le dernier envoi parti est le rendu {d['rendu']} du {NOM[d['juge']]} sur le témoin "
        f"{d['temoin']} de l'ordre du bloc {d['bloc']} (moitié « {moitie_d} », rang {rang_d}), "
        f"parti à un cumul compté de {fr(c['cumul_compte_avant'] - (Fraction(cas_pire['par_appel_exact'][d['juge']])), 4)} USD ; "
        f"le rendu {c['rendu']} du {NOM[c['juge']]} sur le témoin {c['temoin']} ne part pas : cumul compté "
        f"{fr(c['cumul_compte_avant'], 4)} USD plus la réserve de {fr(formule.session)} USD dépasse "
        f"{fr(formule.plafond)} USD. {sim['envois_partis']} envois partent sur {sim['envois_prevus']} ; "
        f"plomberie et bloc A complets ; bloc B complet sur {sim['B_complets']} témoins, dont les "
        f"{sim['lecture_complets']} de la moitié « lecture ». Dépense comptée à l'arrêt : "
        f"{fr(sim['cumul'], 4)} USD ; reste sous le plafond : {fr(reste_sous_plafond, 4)} USD, "
        "moins que la réserve."
    )
    return {
        "phrase": phrase,
        "verdict": cle,
        "verdict_en_clair": verdict(sim)[1],
        "jamais_lu_comme_un_non": True,
        "ce_qui_est_encore_lu": lu,
        "ce_qui_manque": manque,
        "reprendre": ("aucune reprise sous cette ligne : le programme s'arrête, ce qui est fait est "
                      "déposé, scellé et rapporté (texte l. 382)"),
    }


def calculer(racine="."):
    t = tarifs(racine)
    pa, fa = t["par_appel"], t["facteurs"]
    n, plafond_c = N_200, PLAFOND_200_C
    formule = Formule(n, plafond_c, pa)

    # Contrôle à 100 contre la sortie v3 (garde : tout écart arrête).
    sortie_v3 = lire(racine, SORTIE_V3, SORTIE_V3_SHA)
    controle = comparer_a_v3(sortie_v3, valeurs_v3_recalculees(t))
    if not controle["toutes_egales"]:
        raise SystemExit(f"contrôle à 100 non égal à la sortie v3 : {controle['cles_differentes']}")
    # Information : les clés où le calcul tout exact (sans l'arrondi intermédiaire du v3)
    # diffère de la sortie v3 au dernier chiffre écrit.
    tout_exact = valeurs_v3_recalculees(t, comme_v3=False)
    ecarts = comparer_a_v3(sortie_v3, tout_exact)["cles_differentes"]
    controle["arrondi_intermediaire_du_v3"] = {
        "nature": ("le calcul v3 lit les coûts de la plomberie, du bloc A et les totaux au cas haut dans sa "
                   "sortie arrondie à quatre décimales avant ses formules du plafond ; reproduit ici pour le "
                   "contrôle ; les chiffres à 200 de ce calcul sont tout exacts"),
        "cles_ou_le_tout_exact_differe_au_dernier_chiffre": {
            k: {"sortie_v3": str(_valeur_v3(sortie_v3, k)),
                "tout_exact": (str(tout_exact[k][0]) if tout_exact[k][1] is None
                               else texte(tout_exact[k][0], tout_exact[k][1]))}
            for k in ecarts}}
    f100 = Formule(N_100, PLAFOND_100_C, pa)
    sim100 = simuler(N_100, PLAFOND_100_C, {j: pa[j] * fa["pire"] for j in JUGES})
    cent = {
        "comparaison_a_la_sortie_v3": controle,
        "pire_cas_envoi_par_envoi": resume(sim100),
        "pire_cas_formule_du_devis_bloc_B_complets": f100.temoins_b_complets(fa["pire"]),
        "pire_cas_selon_les_envois_refuses_envoi_par_envoi": {
            str(r): simuler(N_100, PLAFOND_100_C, {j: pa[j] * fa["pire"] for j in JUGES}, refus=r)["B_complets"]
            for r in REFUS_TABULES_100},
        "multiples_envoi_par_envoi": {
            "plomberie_et_bloc_A": texte(facteur_exact(f100, None)),
            "plus_bloc_B_sur_40": texte(facteur_exact(f100, 40)),
            "plus_bloc_B_sur_50_moitie_lecture": texte(facteur_exact(f100, 50)),
            "tout_100": texte(facteur_exact(f100, 100))},
    }

    cas = {nom: bloc_cas(nom, t, formule, n, plafond_c) for nom in ("estimation", "haut", "pire")}
    for nom in cas:
        cas[nom]["par_appel_exact"] = {j: str(pa[j] * fa[nom]) for j in JUGES}

    # Garde interne : cas sain du compteur (cas haut, aucun refus) : tout part, cumul = total.
    sim_haut = simuler(n, plafond_c, {j: pa[j] for j in JUGES})
    if sim_haut["envois_partis"] != sim_haut["envois_prevus"] or sim_haut["cumul"] != cout_du_plan(n, pa, 1)[2]:
        raise SystemExit("cas sain du compteur non tenu au cas haut")

    # Multiples du tarif des cartes qui laissent un groupe complet.
    groupes = (("plomberie_et_bloc_A", None), ("plus_bloc_B_sur_40_temoins_seuil_de_lecture", SEUIL_LECTURE),
               ("plus_bloc_B_sur_les_100_temoins_de_la_moitie_lecture", n // 2),
               ("tout_les_200_temoins", n))
    multiples = {}
    for nom_g, k_b in groupes:
        fx = facteur_exact(formule, k_b)
        verifier_frontiere(n, plafond_c, pa, fx, k_b)
        fd = formule.facteur_bloc_a() if k_b is None else formule.facteur_pour_b_complets(k_b)
        multiples[nom_g] = {"formule_du_devis": texte(fd), "envoi_par_envoi": texte(fx),
                            "envoi_par_envoi_exact": str(fx)}

    sim_pire = simuler(n, plafond_c, {j: pa[j] * fa["pire"] for j in JUGES})
    sim_tous = simuler(n, plafond_c, {j: pa[j] for j in JUGES}, tous_refuses=True)
    sim_plomberie = simuler(n, plafond_c, {j: pa[j] * FACTEUR_ARRET_PLOMBERIE for j in JUGES})

    resultat = {
        "version": VERSION,
        "nature": ("calcul versionné des conditions du plafond de l'étage 2 à 200 témoins (nœud 3 de "
                   "l'additif 3 v3) ; pas un devis ; aucun montant neuf"),
        "entrees": {"manifeste": [MANIFESTE, MANIFESTE_SHA], "epreuve_temoins_v9": [EPREUVE, EPREUVE_SHA],
                    "sortie_du_calcul_v3": [SORTIE_V3, SORTIE_V3_SHA]},
        "regle_du_compteur": {
            "texte": ("aucun envoi ne part si le cumul compté plus l'engagement de 0,60 USD dépasse le "
                      "plafond ; un envoi refusé, coupé, en erreur ou sans coût lisible est compté 0,60 USD ; "
                      "rejeu unique ; un coût relevé au-dessus de 0,60 USD arrête le programme"),
            "plafond_centimes": plafond_c, "plafond_usd": texte(formule.plafond, 2),
            "ligne_de_go": "GO-2026-11-20-26",
            "reserve_centimes": SESSION_C, "cumul_utile_centimes": plafond_c - SESSION_C,
            "cumul_utile_usd": texte(formule.disponible, 2)},
        "hypotheses_de_modele": [
            "chaque appel d'un juge coûte le tarif moyen par appel de ce juge à la course v9, multiplié par le facteur du cas",
            "dans le bloc A, par témoin, juge Opus puis juge Argon (la lettre ne le fixe pas)",
            "un envoi refusé est compté 0,60 USD puis rejoué une fois avec succès ; les refus tombent au début du plan",
            "« tous refusés » : chaque envoi et son rejeu sont refusés"],
        "plan_appels_200": {"plomberie": 2 * TEMOINS_PLOMBERIE, "bloc_A": n * len(JUGES),
                            "bloc_B": n * sum(REPETITIONS_B.values()),
                            "total": sim_haut["envois_prevus"]},
        "cas": cas,
        "condition_i_arret_dur_par_compteur": {
            "cumul_utile_usd": texte(formule.disponible, 2),
            "borne_de_la_depense": ("88,36 USD si aucun appel ne coûte plus que 0,60 USD ; sinon 87,76 USD "
                                    "plus le coût du dernier envoi, et ce coût relevé arrête le programme"),
            "garde_cas_sain_cas_haut": {"envois_partis": sim_haut["envois_partis"],
                                        "cumul_compte_usd": texte(sim_haut["cumul"]),
                                        "cumul_egal_au_total_du_plan": True},
            "garde_artefact_cout_gonfle_au_pire_cas": {"envois_partis": sim_pire["envois_partis"]},
            "au_seuil_d_arret_de_la_plomberie_trois_fois_le_tarif": resume(sim_plomberie),
            "multiples_du_tarif_des_cartes_qui_laissent_complet": multiples,
            "lecture_des_multiples": ("« formule du devis » : cumul après le dernier envoi du groupe sous "
                                      "87,76 USD (prudente, comme le devis v7) ; « envoi par envoi » : le "
                                      "dernier envoi du groupe part encore (règle elle-même, ordre supposé)"),
            "temoins_au_plus_au_cas_haut": {"avec_reserve": formule.temoins_au_plus(True),
                                            "sans_reserve": formule.temoins_au_plus(False)},
            "marge_nominale_sur_le_haut": texte(formule.plafond / cout_du_plan(n, pa, 1)[2]),
            "marge_effective_sur_le_haut": texte(formule.disponible / cout_du_plan(n, pa, 1)[2]),
        },
        "condition_ii_issue_du_pire_cas_ecrite_d_avance": issue_du_pire(cas["pire"], sim_pire, formule, n),
        "condition_iii_envoi_refuse_compte_au_pire": {
            "cout_compte_d_un_envoi_refuse_usd": texte(formule.session, 2),
            "si_tous_les_envois_sont_refuses": {
                "envois_partis": sim_tous["envois_partis"],
                "formule_du_devis_envois_partis": formule.envois_si_tous_refuses(),
                "cumul_compte_a_l_arret_usd": texte(sim_tous["cumul"], 2),
                "rendus_obtenus": sim_tous["rendus_obtenus"],
                "dernier_envoi_parti": decrire_envoi(sim_tous["dernier"], n),
                "premier_envoi_interdit_par_la_regle": decrire_envoi(sim_tous["coupure"], n),
                "verdict": verdict(sim_tous)[0]},
            "envois_refuses_que_le_plan_supporte_sans_coupure": {
                nom: {"formule_du_devis": cas[nom]["formule_du_devis"]["envois_refuses_supportes_sans_coupure"],
                      "envoi_par_envoi": cas[nom]["seuils_de_refus_envoi_par_envoi"]["sans_aucune_coupure"]}
                for nom in cas},
        },
        "controle_a_100_temoins_et_25_usd": cent,
    }
    for nom in cas:
        del cas[nom]["par_appel_exact"]
    return resultat


def main(argv):
    if len(argv) != 1:
        raise SystemExit("usage : python3 -I -B calcul_conditions_plafond_200_ligne_3_v1.py > SORTIE.json "
                         "(aucun argument)")
    resultat = calculer(".")
    verifier_sans_flottant(resultat)
    texte_json = json.dumps(resultat, ensure_ascii=False, indent=1, sort_keys=True) + "\n"
    sys.stdout.buffer.write(texte_json.encode("utf-8"))


if __name__ == "__main__":
    main(sys.argv)
