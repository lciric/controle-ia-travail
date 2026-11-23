"""Préalables du service v8 : réglages de chaque espèce et garde de Google rejouée, sans réseau."""
import sys, json, hashlib
from pathlib import Path
W = Path(sys.argv[1]); Q = Path(sys.argv[2])
sys.path.insert(0, str(W / "src")); sys.path.insert(0, str(W / "docs/notes/collisionneur-v9/abonnement-v1"))
import voie_abonnement_v6 as va
v = va.charger(*va.MOTEURS["v8m"], "moteur_v8m_prealable")
texte = Q.read_text(encoding="utf-8")
assert hashlib.sha256(Q.read_bytes()).hexdigest() == "f3f47c08bfb1885a1a277fc5af33b6ac115fa88fc9aaa16d61b9e93cd54da4f7"
print("question servie : empreinte f3f47c08… conforme")
print("garde de motifs du moteur sur la question :", v.motifs_trouves(texte) or "zéro")
mods = v.fixer_composition(["opus", "argon", "astra", "carbon", "neon"], nom_cle_anthropic="CLE_ANTHROPIC_FACTICE",
                           nom_cle_openai="OPENAI_API_KEY_2", sortie_max=True)
cles = ("id", "fournisseur", "max", "max_relance", "provision", "niveau_reflexion", "effort", "delai_s", "prix")
ok = True
for l, m in mods.items():
    print(l, m["espece"], {k: m.get(k) for k in cles})
    if m["fournisseur"] == "gemini":
        for tour, t in v.TOURS.items():
            for plafond in (m["max"], m["max_relance"]):
                corps = v.demande_gemini(m, texte, plafond)
                pb = v.verifier_reglages_google(m["espece"], corps, m["provision"], mots=t["mots"], mode="flux",
                                                niveau_attendu=m.get("niveau_reflexion"))
                if pb: ok = False; print("  REFUS", tour, plafond, pb)
        print("  garde de Google : rien de refusé sur tous les tours" if ok else "  garde de Google : REFUS")
attendu = {"argon": (65536, 16384, "high"), "carbon": (65536, 49152, "high"), "neon": (65536, 32768, "xhigh"),
           "astra": (128000, 0, None)}
for l, m in mods.items():
    if m["espece"] in attendu:
        a = attendu[m["espece"]]
        r = (m["max"], m["provision"], m.get("niveau_reflexion"))
        conf = r == a and m["max_relance"] == a[0]
        ok &= conf
        print(f"{m['espece']} : devis {a}, code {r}, relance {m['max_relance']} : {'conforme' if conf else 'ÉCART'}")
print("PRÉALABLES :", "TENUS" if ok else "ÉCART")
sys.exit(0 if ok else 2)
