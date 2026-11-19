"""Essais d'attaque : fichier de l'étape (m) (C-5), pièce scellée et fichier des rangs (C-9, C-10). Synthétique."""
import json, sys, tempfile
from pathlib import Path
sys.path.insert(0, "/home/user/controle-ia-travail/tests")
import test_analyse_bras_a_v5 as T
from controle_ia.organismes_discrets import analyse_bras_a_v5 as an, verdicts_bras_a_v5 as v
from controle_ia.scellement import sceller
from controle_ia.gardes import GardeArret
sys.path.insert(0, "/tmp/claude-0/-home-user-controle-ia-travail/b7727ccc-db8b-5b89-bce1-17602831b69d/scratchpad/contre-lecture-code-v5")
import contextlib, io
with contextlib.redirect_stdout(io.StringIO()):
    from attaques_regle_v1 import essai

d = Path(tempfile.mkdtemp())
scores = T.lignes_de_scores("classifieur-lexical", "dose-1.00")
rangs, piece = T.livrer(d, T.en_rangs(scores), "livraison")

# C-5 résiduel : sous A15, l'enchaînement écrit le fichier sans passer par verdicts (contenu public + sceller)
res_a = v.lire_table_a(["A15"])
print("table A sous A15 : etapes m et n jouees =", res_a.etapes_m_et_n_jouees)
(d / "a15").mkdir()
f = d / "a15" / an.NOM_DU_FICHIER_DE_L_ETAPE_M
f.write_text(json.dumps(an.contenu_du_fichier_de_l_etape_m(T.regle(T.sortie()), {})), encoding="utf-8")
sceller(f)
essai("C-5 residuel : fichier (m) ecrit a la main sous A15, puis rangs lus", lambda: type(an.lire_fichier_des_rangs(rangs, piece, f, an.USAGE_AIRE_CONDITIONNELLE)).__name__)
# ResultatA fabriqué à la main
(d / "faux").mkdir()
essai("C-5 : ResultatA fabrique a la main (aucune ligne)", lambda: v.ecrire_fichier_de_l_etape_m(d / "faux", resultat_a=v.ResultatA(lignes=(), verdicts=()),
      renvoi_de_la_base=v.RENVOI_DE_LA_BASE_VERIFIE, effectifs_de_la_base_conformes=True, resultat_de_discretion=T.regle(T.sortie()), lignes_c={}).name)

# C-9 : pièce « du côté habilité » fabriquée par l'appelant (n'importe quel fichier scellé aux onze noms)
autre = d / "autre"; autre.mkdir()
faux_rangs = autre / an.NOM_DU_FICHIER_DES_RANGS
faux_rangs.write_text((d / "livraison" / an.NOM_DU_FICHIER_DES_RANGS).read_text(encoding="utf-8"), encoding="utf-8")
sceller(faux_rangs)
import hashlib
p = autre / "n-importe-quel-nom.json"
p.write_text(json.dumps(T.sortie(scores_par_unite={"fichier": faux_rangs.name, "sha256": hashlib.sha256(faux_rangs.read_bytes()).hexdigest(),
                                                    "lignes": "?", "champs": "?", "forme": None})), encoding="utf-8")
sceller(p)
essai("C-9 : piece fabriquee et scellee par l'appelant, lignes et champs sous forme non reconnue", lambda: type(an.lire_fichier_des_rangs(faux_rangs, p, f, an.USAGE_AIRE_CONDITIONNELLE)).__name__)

# C-10 : sous-ensemble d'un pli (unités exclues après le classement)
sous = [x for x in T.en_rangs(scores) if not (x["tache"] == T.VER[0] and x["episode"] == 0)]
r2, p2 = T.livrer(d, sous, "sous-ensemble")
essai("C-10 : unites retirees apres le classement", lambda: type(an.lire_fichier_des_rangs(r2, p2, f, an.USAGE_AIRE_CONDITIONNELLE)).__name__)
# C-10 : rangs reclasses par (moniteur, dose) sans pli
r3, p3 = T.livrer(d, T.en_rangs(scores, groupe=lambda x: (x["moniteur"], x["dose"])), "sans-pli")
essai("C-10 : rangs sans egard au pli", lambda: type(an.lire_fichier_des_rangs(r3, p3, f, an.USAGE_AIRE_CONDITIONNELLE)).__name__)
# C-10 : rang 'entier' écrit 3 au lieu de 3.0 : accepté (attendu)
# dose ¼ absente des rangs alors que la sortie l'annonce : rien
