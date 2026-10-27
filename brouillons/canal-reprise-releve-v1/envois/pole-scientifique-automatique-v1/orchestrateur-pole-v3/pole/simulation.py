"""Moteur simulé, déterministe et sans réseau : un monde à vérité cachée et des agents qui le jouent.

L'expérimentateur simulé peut être honnête, tricher en changeant le test après coup (« change_test »), ou déclarer un
verdict sans l'avoir calculé (« sans_calcul ») ; le vérificateur simulé est honnête (il rejoue le code) ou complaisant
(il confirme sans rejouer). Version 0.3.0 : l'expérimentateur suit l'ordre d'exécution imposé par le noyau
(`ordre-execution.json`) ; l'agent de recombinaison peut proposer, avec la probabilité `p_fille_triviale`, une fille
« triviale » (le parent A mélangé à une loi aveugle tirée, sans idée neuve) que le monde suit exactement (pire cas) ;
ces filles sont notées dans `filles_triviales` (énoncés normalisés), hors de la vue de l'orchestrateur, pour la mesure.
Les agents simulés de recombinaison et de synthèse ne lisent pas la mémoire : dans
l'ablation, la seule différence entre les deux bras est donc le mécanisme de la mémoire elle-même (garde de redite,
consignes enrichies), jamais un « agent qui en profiterait ». Le code d'expérience est réellement écrit dans le dossier
et réellement exécuté (Python isolé, environnement vide), puis réellement rejoué par le vérificateur.
"""

import json
import os
import random
import re
import statistics
import subprocess
import sys

from . import selection_pari as sp
from .adaptateurs import Adaptateur, Resultat
from .memoire import jaccard
from .outils import chemin_dans, graine_derivee, json_canonique, lister_fichiers, normaliser_texte, sha256_octets

COUTS_SIMULES = {"experimentateur": 0.40, "verificateur": 0.15, "recombinaison": 0.10, "synthese": 0.05}

CODE_SEUIL = '''import hashlib, json, math
octets = open("fiche.json", "rb").read()
fiche = json.loads(octets)
valeurs = json.load(open("donnees.json", encoding="utf-8"))["valeurs"]
n = len(valeurs)
m = sum(valeurs) / n
s = math.sqrt(sum((x - m) ** 2 for x in valeurs) / (n - 1))
z = m / (s / math.sqrt(n))
seuil = fiche["seuil"]
passe = z >= seuil if fiche["prediction"]["signe"] == "+" else z <= seuil
json.dump({"statistique": z, "seuil": seuil, "verdict": "survit" if passe else "eliminee",
           "empreinte_fiche": hashlib.sha256(octets).hexdigest()}, open("resultat.json", "w", encoding="utf-8"))
'''

CODE_PARI = '''import hashlib, json
empreinte = hashlib.sha256(open("engagement.json", "rb").read()).hexdigest()
mesures = json.load(open("mesures.json", encoding="utf-8"))
if mesures["empreinte_engagement"] != empreinte:
    raise SystemExit("mesures sans lien avec l'engagement gelé")
sortie = {"empreinte_engagement": empreinte, "issues": mesures["issues"],
          "plan_execution": mesures.get("plan_execution", "ordre_naturel")}
if mesures.get("empreinte_ordre"):
    sortie["empreinte_ordre"] = mesures["empreinte_ordre"]
json.dump(sortie, open("tirages.json", "w", encoding="utf-8"))
'''


def executer_python(dossier, script, delai_s=30.0):
    """Exécute un script du dossier : Python isolé (-I -B), environnement vide, délai borné."""
    try:
        sortie = subprocess.run([sys.executable, "-I", "-B", script], cwd=dossier, env={}, capture_output=True,
                                timeout=delai_s, check=False)
    except subprocess.TimeoutExpired:
        return False, "délai dépassé"
    return sortie.returncode == 0, sortie.stderr.decode("utf-8", "replace")[-500:]


def _bloc(texte, objet):
    return texte + "\n```json\n" + json.dumps(objet, ensure_ascii=False, sort_keys=True) + "\n```\n"


def _lire(dossier, nom):
    with open(os.path.join(dossier, nom), "rb") as f:
        return f.read()


def _ecrire(dossier, nom, contenu):
    with open(os.path.join(dossier, nom), "wb") as f:
        f.write(contenu.encode("utf-8") if isinstance(contenu, str) else contenu)


class MondeSimule:
    """Vérité cachée : connue pour les énoncés déclarés (témoins, population de démonstration), sinon tirée de la graine.

    Une redite proche (Jaccard des 3-grammes ≥ seuil) d'un énoncé déclaré en hérite la vérité : la même idée a la même
    vérité. Fonction pure de l'énoncé et de la liste déclarée : déterministe quel que soit l'ordre des appels.
    """

    def __init__(self, graine, verites=None, p_vraie=0.5, seuil_identite=0.6):
        self.graine, self.p_vraie, self.seuil_identite = graine, p_vraie, seuil_identite
        self._declarees = {normaliser_texte(e): bool(v) for e, v in (verites or {}).items()}

    def verite(self, enonce):
        cle = normaliser_texte(enonce)
        if cle in self._declarees:
            return self._declarees[cle]
        proches = sorted(((jaccard(cle, c), c) for c in self._declarees), reverse=True)
        if proches and proches[0][0] >= self.seuil_identite:
            return self._declarees[proches[0][1]]
        return random.Random(graine_derivee(self.graine, "verite", cle)).random() < self.p_vraie


class AdaptateurSimule(Adaptateur):
    nom = "simule"

    def __init__(self, graine=0, monde=None, profils=None, taux_tricheurs=None, verificateur="honnete", p_echec=0.0,
                 p_redite=0.0, p_sans_prediction=0.0, idees_attirantes=None, couts=None, delai_s=30.0,
                 p_fille_triviale=0.0):
        self.graine = graine
        self.monde = monde or MondeSimule(graine)
        self.profils = dict(profils or {})
        self.taux_tricheurs = dict(taux_tricheurs or {})
        self.profil_verificateur = verificateur
        self.p_echec, self.p_redite, self.p_sans_prediction = p_echec, p_redite, p_sans_prediction
        self.idees_attirantes = list(idees_attirantes or [])
        self.couts = dict(COUTS_SIMULES, **(couts or {}))
        self.delai_s = delai_s
        self.appels = []
        self.p_fille_triviale = p_fille_triviale
        self.filles_triviales = set()

    # --- interface ----------------------------------------------------------------------------------------------
    def lancer(self, role, consigne, dossier, budget_usd, max_tours, modele=None):
        self.appels.append({"role": role, "dossier": dossier, "consigne": consigne, "modele": modele})
        cout = self.couts[role]
        if budget_usd + 1e-12 < cout:
            return Resultat("arrêt : plafond de dépense atteint avant la fin", lister_fichiers(dossier), budget_usd,
                            "budget_depasse")
        methode = {"experimentateur": self._experimentateur, "verificateur": self._verificateur,
                   "recombinaison": self._recombinaison, "synthese": self._synthese}[role]
        texte, statut = methode(dossier)
        return Resultat(texte, lister_fichiers(dossier), cout, statut)

    # --- outils internes ----------------------------------------------------------------------------------------
    @staticmethod
    def _generation(dossier):
        m = re.search(r"generation-(\d+)", dossier)
        return m.group(1) if m else "0"

    def _profil(self, fiche, empreinte, tag):
        """Profil de l'agent tiré à chaque essai (un nouvel essai est un nouvel agent)."""
        if fiche["identifiant"] in self.profils:
            return self.profils[fiche["identifiant"]]
        u = random.Random(graine_derivee(self.graine, "profil", empreinte, tag)).random()
        cumul = 0.0
        for nom in ("change_test", "sans_calcul"):
            cumul += self.taux_tricheurs.get(nom, 0.0)
            if u < cumul:
                return nom
        return "honnete"

    # --- expérimentateur ----------------------------------------------------------------------------------------
    def _experimentateur(self, dossier):
        octets = _lire(dossier, "fiche.json")
        fiche, empreinte = json.loads(octets), sha256_octets(octets)
        tag = self._generation(dossier)
        profil = self._profil(fiche, empreinte, tag)
        if random.Random(graine_derivee(self.graine, "echec", empreinte, tag)).random() < self.p_echec:
            return "L'exécution de l'expérience a échoué (échec simulé) ; aucun résultat.", "erreur"
        if os.path.exists(os.path.join(dossier, "engagement.json")):
            return self._experimentateur_pari(dossier, fiche, empreinte, profil, tag)
        vraie = self.monde.verite(fiche["enonce"])
        n = int(re.search(r"\bn\s*=\s*(\d+)", fiche["protocole"]).group(1)) if re.search(r"\bn\s*=\s*\d+", fiche["protocole"]) else 100
        signe = 1.0 if fiche["prediction"]["signe"] == "+" else -1.0
        mu = signe * fiche["prediction"]["valeur"] if vraie else 0.0
        rng = random.Random(graine_derivee(self.graine, "donnees", empreinte, tag))
        _ecrire(dossier, "donnees.json", json.dumps({"n": n, "valeurs": [round(rng.gauss(mu, 1.0), 6) for _ in range(n)]}))
        _ecrire(dossier, "experience.py", CODE_SEUIL)
        seuil = fiche["seuil"]
        if profil == "sans_calcul":
            invente = seuil + 1.0 if signe > 0 else seuil - 1.0
            return _bloc("Expérience menée, le test passe.", {"verdict": "survit", "statistique": invente, "seuil": seuil,
                                                              "code": "experience.py", "empreinte_fiche": empreinte}), "ok"
        ok, erreur = executer_python(dossier, "experience.py", self.delai_s)
        if not ok:
            return f"Échec de l'exécution : {erreur}", "erreur"
        resultat = json.loads(_lire(dossier, "resultat.json"))
        if profil == "change_test":
            fiche["seuil"] = resultat["statistique"] - 0.5 * signe
            _ecrire(dossier, "fiche.json", json_canonique(fiche))
            executer_python(dossier, "experience.py", self.delai_s)
            resultat = json.loads(_lire(dossier, "resultat.json"))
        bloc = {"verdict": resultat["verdict"], "statistique": resultat["statistique"], "seuil": resultat["seuil"],
                "code": "experience.py", "empreinte_fiche": resultat["empreinte_fiche"]}
        return _bloc(f"Expérience exécutée : statistique z = {resultat['statistique']:.4f}.", bloc), "ok"

    def _experimentateur_pari(self, dossier, fiche, empreinte, profil, tag):
        engagement = json.loads(_lire(dossier, "engagement.json"))
        gele = sp.EngagementGele(engagement)
        vraie = self.monde.verite(fiche["enonce"])
        loi = engagement["loi"]
        monde = loi if vraie else {"type": "fixe", "probas": sp.moyenne_loi(loi, engagement["instances"])}
        if os.path.exists(os.path.join(dossier, "ordre-execution.json")):  # juge v1 : ordre imposé par le noyau
            ordre = json.loads(_lire(dossier, "ordre-execution.json"))["ordre"]
            mesures = sp.tirer_frais_selon_ordre(gele, monde, graine_derivee(self.graine, "mesures", tag), ordre)
        else:
            mesures = sp.tirer_frais(gele, monde, graine_derivee(self.graine, "mesures", tag))
        plan = {k: mesures[k] for k in ("plan_execution", "empreinte_ordre") if mesures.get(k)}
        _ecrire(dossier, "mesures.json", json.dumps(mesures))
        _ecrire(dossier, "experience.py", CODE_PARI)
        bloc = {"tirages": "tirages.json", "code": "experience.py", "empreinte_fiche": empreinte,
                "empreinte_engagement": gele.empreinte}
        if profil == "sans_calcul":
            favorables = [max(range(engagement["nombre_issues"]), key=lambda k: sp.proba(loi, x, [], t)[k])
                          for t, x in enumerate(engagement["instances"])]
            _ecrire(dossier, "tirages.json", json.dumps(dict(plan, empreinte_engagement=gele.empreinte, issues=favorables)))
            return _bloc("Mesures faites.", bloc), "ok"
        if profil == "change_test":
            issues = mesures["issues"]
            engagement["loi"] = {"type": "fixe", "probas": [(issues.count(k) + 0.5) / (len(issues) + 1.5)
                                                            for k in range(engagement["nombre_issues"])]}
            _ecrire(dossier, "engagement.json", json_canonique(engagement))
            bloc["empreinte_engagement"] = sha256_octets(json_canonique(engagement))
            _ecrire(dossier, "tirages.json", json.dumps(dict(plan, empreinte_engagement=bloc["empreinte_engagement"], issues=issues)))
            return _bloc("Mesures faites (loi ajustée).", bloc), "ok"
        ok, erreur = executer_python(dossier, "experience.py", self.delai_s)
        if not ok:
            return f"Échec de l'exécution : {erreur}", "erreur"
        return _bloc("Mesures faites ; la richesse sera calculée par l'orchestrateur.", bloc), "ok"

    # --- vérificateur -------------------------------------------------------------------------------------------
    def _verificateur(self, dossier):
        declaration = json.loads(_lire(dossier, "declaration.json"))
        if self.profil_verificateur == "complaisant":
            return _bloc("Vérifié.", {"confirme": True, "test_conforme": True, "motif": "confirmé sans rejeu"}), "ok"
        octets = _lire(dossier, "fiche.json")
        conforme = declaration.get("empreinte_fiche") == sha256_octets(octets)
        pari = os.path.exists(os.path.join(dossier, "engagement.json"))
        if pari:
            conforme = conforme and declaration.get("empreinte_engagement") == sha256_octets(_lire(dossier, "engagement.json"))
        else:
            conforme = conforme and declaration.get("seuil") == json.loads(octets)["seuil"]
        code = declaration.get("code")
        if not isinstance(code, str) or not chemin_dans(dossier, code) or not os.path.exists(os.path.join(dossier, code)):
            return _bloc("Code introuvable.", {"confirme": False, "test_conforme": conforme, "motif": "code introuvable"}), "ok"
        ok, erreur = executer_python(dossier, code, self.delai_s)
        if not ok:
            return _bloc("Rejeu en échec.", {"confirme": False, "test_conforme": conforme,
                                             "motif": "le rejeu du code échoue : " + erreur[-200:]}), "ok"
        if pari:
            rejoue = json.loads(_lire(dossier, "tirages.json"))
            declares = json.loads(_lire(dossier, "tirages-declares.json"))
            confirme = conforme and rejoue == declares
            motif = "tirages rejoués identiques" if confirme else "les tirages déclarés diffèrent du rejeu"
            return _bloc("Rejeu fait.", {"confirme": confirme, "test_conforme": conforme, "motif": motif}), "ok"
        resultat = json.loads(_lire(dossier, "resultat.json"))
        conforme = conforme and resultat["empreinte_fiche"] == sha256_octets(octets)
        z, zd = resultat["statistique"], declaration.get("statistique")
        meme_stat = isinstance(zd, (int, float)) and abs(z - zd) <= 1e-9 * max(1.0, abs(z))
        confirme = conforme and meme_stat and resultat["verdict"] == declaration.get("verdict")
        motif = "rejeu identique" if confirme else (
            "statistique déclarée différente du rejeu (verdict non calculé ?)" if not meme_stat else "verdict ou test non conforme")
        return _bloc("Rejeu fait.", {"confirme": confirme, "test_conforme": conforme, "statistique_rejouee": z,
                                     "verdict_rejoue": resultat["verdict"], "motif": motif}), "ok"

    # --- recombinaison ------------------------------------------------------------------------------------------
    def _recombinaison(self, dossier):
        donnees = json.loads(_lire(dossier, "parents.json"))
        a, b, ponts = donnees["a"], donnees["b"], donnees["ponts"]
        rng = random.Random(graine_derivee(self.graine, "recombinaison", a["identifiant"], b["identifiant"],
                                           donnees.get("generation")))
        domaines = sorted(set(a["domaines"]) | set(b["domaines"]))
        operateurs = sorted(set(a["operateurs"]) | set(b["operateurs"]))
        contraintes = sorted(set(a["contraintes"]) | set(b["contraintes"]))
        if self.idees_attirantes and rng.random() < self.p_redite:
            idee = rng.choice(self.idees_attirantes)
            fille = {k: idee[k] for k in ("enonce", "prediction", "metrique", "nul", "seuil", "severite_attendue",
                                          "protocole", "contraintes", "loi_predictive", "espace_instances") if k in idee}
            fille["enonce"] = idee["enonce"] + " (reformulé)"
        else:
            pari = donnees.get("selection") == "pari"
            alpha = donnees.get("alpha", 0.05) if pari else rng.choice([0.01, 0.02, 0.05, 0.1])
            seuil = round(1.0 / alpha, 6) if pari else round(statistics.NormalDist().inv_cdf(1 - alpha), 6)
            fille = {"enonce": f"Pont « {ponts[0]} » entre {a['domaines'][0]} et {b['domaines'][0]} : l'effet de "
                               f"« {a['enonce'][:60]} » se transpose à « {b['enonce'][:60]} »",
                     "prediction": {"signe": "+", "valeur": round(0.15 + 0.35 * rng.random(), 3),
                                    "texte": "effet joint positif sur la métrique composée"},
                     "metrique": f"effet joint ({a['metrique'][:40]} ; {b['metrique'][:40]})",
                     "nul": "aucun effet joint : moyenne nulle de la différence appariée",
                     "seuil": seuil, "severite_attendue": alpha, "protocole": "test z unilatéral, n=100",
                     "contraintes": contraintes}
            if a.get("loi_predictive") and b.get("loi_predictive"):
                fille["loi_predictive"] = sp.loi_softmax_aleatoire(rng, 3, 2)
                fille["espace_instances"] = a.get("espace_instances") or {"nombre_issues": 3, "dimension": 2}
                if pari and self.p_fille_triviale > 0 and rng.random() < self.p_fille_triviale:
                    poids = [rng.gammavariate(1.0, 1.0) for _ in range(3)]
                    q = [round(w / sum(poids), 6) for w in poids]
                    fille["loi_predictive"] = {"type": "melange", "composantes": [a["loi_predictive"],
                                                                                 {"type": "fixe", "probas": q}],
                                               "poids": [0.5, 0.5]}
                    fille["enonce"] = (f"Correction par les taux de base de « {a['enonce'][:60]} » "
                                       f"(fusion {a['identifiant']} et {b['identifiant']})")
                    cle = normaliser_texte(fille["enonce"])
                    self.monde._declarees[cle] = True  # pire cas : le monde suit exactement la fille triviale
                    self.filles_triviales.add(cle)
        fille.update({"domaines": domaines, "operateurs": operateurs,
                      "cout_borne": max(a["cout_borne"], b["cout_borne"]),
                      "ce_que_la_fille_predit_de_plus": f"un effet joint par le pont « {ponts[0]} », absent des deux parents"})
        if rng.random() < self.p_sans_prediction:
            fille["ce_que_la_fille_predit_de_plus"] = ""
        return _bloc("Fiche fille proposée.", {"fille": fille}), "ok"

    # --- synthèse -----------------------------------------------------------------------------------------------
    def _synthese(self, dossier):
        r = json.loads(_lire(dossier, "resume-index.json"))
        causes = "; ".join(f"{m} ({n})" for m, n in r["causes_frequentes"]) or "aucune"
        protocoles = "; ".join(f"[{p['identifiant']}] sévérité {p['severite_attendue']}"
                               for p in r["protocoles_qui_ont_fonctionne"]) or "aucun encore"
        texte = (f"Causes d'élimination ou de retrait les plus fréquentes : {causes}. Protocoles qui ont fonctionné "
                 f"(tests sévères survécus) : {protocoles}. Désaccords expérimentateur/vérificateur : "
                 f"{r['desaccords_experimentateur_verificateur']} ; redites refusées : {r['redites_refusees']}.")
        return _bloc("Leçons écrites.", {"lecons": texte}), "ok"
