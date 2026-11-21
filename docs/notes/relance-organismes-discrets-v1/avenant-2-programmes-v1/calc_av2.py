#!/usr/bin/env python3
"""calc_av2.py — avenant 2 au devis des deux essais d'admission du bras A.

Refait par programme, en nombres décimaux exacts, les chiffres qui changent quand
la sortie maximale envoyée à Google passe de 32 768 à 65 536 jetons.
Aucun réseau. Un seul fichier lu : le relevé du taux, passé en argument.
Arrondis : un coût, une réserve, un excès, un besoin, un manque -> vers le haut ;
un crédit compté (solde converti) -> vers le bas, comme l'avenant 1 (4.4, point 1).
"""
import re
import sys
from decimal import Decimal as D, ROUND_CEILING, ROUND_FLOOR, getcontext

getcontext().prec = 60
CENT, MILLE, DIXIEME, UN, DEMI = D("0.01"), D("0.001"), D("0.1"), D(1), D("0.5")
MILLION = D(1000000)


def haut(x, pas=CENT):
    return (D(x) / pas).to_integral_value(rounding=ROUND_CEILING) * pas


def bas(x, pas=CENT):
    return (D(x) / pas).to_integral_value(rounding=ROUND_FLOOR) * pas


def fr(x, dec=2):
    """Écrit un nombre exact à la française ; refuse d'arrondir en silence."""
    x = D(x)
    q = D(1).scaleb(-dec)
    assert x == x.quantize(q), ("arrondi silencieux refusé", x, dec)
    s = f"{x.quantize(q):f}"
    ent, _, frac = s.partition(".")
    neg = ent.startswith("-")
    ent = ent.lstrip("-")
    groupes = []
    while len(ent) > 3:
        groupes.insert(0, ent[-3:])
        ent = ent[:-3]
    groupes.insert(0, ent)
    out = " ".join(groupes) + ("," + frac if frac else "")
    return ("−" if neg else "") + out


def ex(x):
    """Valeur exacte, sans zéros de queue."""
    x = D(x)
    s = f"{x.normalize():f}"
    dec = len(s.partition(".")[2])
    return fr(x, dec)


def tronque(x, dec=6):
    return fr(bas(x, D(1).scaleb(-dec)), dec)


def titre(t):
    print()
    print("=== " + t)


# ---------------------------------------------------------------- entrées
PE, PS = D(3), D(15)                 # Google, USD par million de jetons (devis 6.1)
DEBIT = D(200)                       # jetons par seconde, débit déclaré (devis 6.4, S)
RELAIS_FILE, RELAIS_VERIF = D(2690), D(890)   # délais des relais (devis 5.6)
CORPS_APP, CORPS_COUV = D(5000), D(24000)     # octets du corps, bornes du devis 6.3 (S)
CORPS_VERIF = D(160)                 # octets du corps d'un appel de vérification (S, voir 2.1)
N_APP, N_COUV, ENVOIS = 6, 2, 2      # file du juge : six lectures d'appariement, deux de couverture
MARGE_TEXTE = D(16000)               # règle des appels aux modèles de Google
ANCIEN, NEUF = D(32768), D(65536)


def sortie(jetons):
    return jetons * PS / MILLION


def entree(octets):
    return octets * PE / MILLION


def tableau(plafond_sortie):
    r = {}
    r["res_app"] = entree(CORPS_APP) + sortie(plafond_sortie)
    r["res_couv"] = entree(CORPS_COUV) + sortie(plafond_sortie)
    r["res_ver"] = entree(CORPS_VERIF) + sortie(plafond_sortie)
    r["pire_file"] = ENVOIS * (N_APP * r["res_app"] + N_COUV * r["res_couv"])
    r["pire_ver"] = 3 * r["res_ver"]
    r["plaf_file"] = haut(r["pire_file"], DEMI)
    r["plaf_ver"] = haut(r["pire_ver"], DEMI)
    r["coupe_file"] = sortie(DEBIT * RELAIS_FILE)      # sortie d'un envoi coupé au délai de la file
    r["coupe_ver"] = sortie(DEBIT * RELAIS_VERIF)
    r["exc_file_x"] = r["coupe_file"] - sortie(plafond_sortie)
    r["exc_ver_x"] = r["coupe_ver"] - sortie(plafond_sortie)
    r["exc_file"] = haut(r["exc_file_x"])
    r["exc_ver"] = haut(r["exc_ver_x"])
    r["borne_ver"] = r["plaf_ver"] + r["exc_ver"]       # plafond et excès, vérification
    r["borne_file"] = r["plaf_file"] + r["exc_file"]    # plafond et excès, file
    r["neuf_x"] = r["plaf_file"] + 9 * r["exc_file_x"]  # file, neuf excès, exact
    r["neuf"] = haut(r["neuf_x"])
    r["seuil_ver"] = r["borne_ver"] + r["borne_file"]
    r["seuil_file"] = r["borne_file"]
    r["prudent2"] = 2 * r["borne_ver"] + r["borne_file"]
    r["pire2"] = 2 * r["borne_ver"] + r["neuf"]
    return r


A = tableau(ANCIEN)
N = tableau(NEUF)

# ---------------------------------------------------------------- 1. contrôle : le programme redonne le devis à 32 768
titre("1. Contrôle du programme : à 32 768, il redonne les chiffres du devis et de l'avenant 1")
print(f"réserve d'un envoi de la file : {ex(entree(CORPS_APP))} + {ex(sortie(ANCIEN))} = {ex(A['res_app'])} (devis : 0,507) ; "
      f"{ex(entree(CORPS_COUV))} + {ex(sortie(ANCIEN))} = {ex(A['res_couv'])} (devis : 0,564)")
assert haut(A["res_app"], MILLE) == D("0.507") and haut(A["res_couv"], MILLE) == D("0.564")
print(f"réserve d'un envoi de vérification, corps de 160 octets : {ex(entree(CORPS_VERIF))} + {ex(sortie(ANCIEN))} = {ex(A['res_ver'])} (devis : 0,492)")
assert A["res_ver"] == D("0.492")
print(f"pire cas des seize envois : 2 × (6 × {ex(A['res_app'])} + 2 × {ex(A['res_couv'])}) = {ex(A['pire_file'])} (devis : 8,33, au plus proche) ; "
      f"demi-dollar supérieur : {fr(A['plaf_file'])} (devis : 8,50)")
assert bas(A["pire_file"]) == D("8.33") and A["plaf_file"] == D("8.50")
print(f"pire cas des trois envois de vérification : 3 × {ex(A['res_ver'])} = {ex(A['pire_ver'])} (devis : 1,48) ; demi-dollar supérieur : {fr(A['plaf_ver'])} (devis : 1,50)")
assert haut(A["pire_ver"]) == D("1.48") and A["plaf_ver"] == D("1.50")
print(f"excès d'un envoi : file, {ex(A['coupe_file'])} − {ex(sortie(ANCIEN))} = {ex(A['exc_file_x'])} (devis : 7,58) ; "
      f"vérification, {ex(A['coupe_ver'])} − {ex(sortie(ANCIEN))} = {ex(A['exc_ver_x'])} (devis : 2,18)")
assert A["exc_file"] == D("7.58") and A["exc_ver"] == D("2.18")
print(f"plafond et excès : {fr(A['plaf_ver'])} + {fr(A['exc_ver'])} = {fr(A['borne_ver'])} (devis : 3,68) ; "
      f"{fr(A['plaf_file'])} + {fr(A['exc_file'])} = {fr(A['borne_file'])} (devis : 16,08) ; ensemble {fr(A['seuil_ver'])} (devis : 19,76)")
assert (A["borne_ver"], A["borne_file"], A["seuil_ver"]) == (D("3.68"), D("16.08"), D("19.76"))
print(f"file, neuf excès : {fr(A['plaf_file'])} + 9 × {ex(A['exc_file_x'])} = {ex(A['neuf_x'])} ; l'avenant 1 écrit 76,70, calculé sur 7,578 (76,702)")
assert bas(A["neuf_x"]) == D("76.70")
print(f"Google, deux vérifications : régime prudent, 2 × {fr(A['borne_ver'])} + {fr(A['borne_file'])} = {fr(A['prudent2'])} (avenant 1 : 23,44) ; "
      f"neuf excès, 2 × {fr(A['borne_ver'])} + 76,70 = {fr(2 * A['borne_ver'] + D('76.70'))} (avenant 1 et registre : 84,06)")
assert A["prudent2"] == D("23.44") and 2 * A["borne_ver"] + D("76.70") == D("84.06")
print(f"débit qui tient 32 768 jetons en 2 690 secondes : {tronque(ANCIEN / RELAIS_FILE, 4)} -> {fr(haut(ANCIEN / RELAIS_FILE, DIXIEME), 1)} (devis : 12,2)")
assert haut(ANCIEN / RELAIS_FILE, DIXIEME) == D("12.2")
print(f"durée sous laquelle un envoi est compté à sa réserve : 32 768 ÷ 200 = {ex(ANCIEN / DEBIT)} -> {fr(haut(ANCIEN / DEBIT, UN), 0)} secondes (devis : 164)")
assert haut(ANCIEN / DEBIT, UN) == 164
print(f"seuil de refus du compteur, envoi de couverture : {fr(A['plaf_file'])} − {ex(A['res_couv'])} = {ex(A['plaf_file'] - A['res_couv'])} (devis : 7,93)")
assert bas(A["plaf_file"] - A["res_couv"]) == D("7.93")
T_OD, B_A, B_B = D("1.0990"), D("11.93"), D("15.59")
od_v = haut(D("3.68") * D("1.05") / T_OD)
od_f = haut(D("23.44") * D("1.05") / T_OD)
print(f"journal, entrée OD-301 : 3,68 × 1,05 ÷ 1,0990 = {tronque(D('3.68') * D('1.05') / T_OD, 4)} -> {fr(od_v)} € ; "
      f"23,44 × 1,05 ÷ 1,0990 = {tronque(D('23.44') * D('1.05') / T_OD, 4)} -> {fr(od_f)} € ; manque {fr(od_f - B_A)} et {fr(od_f - B_B)} €")
assert (od_v, od_f, od_f - B_A, od_f - B_B) == (D("3.52"), D("22.40"), D("10.47"), D("6.81"))

# ---------------------------------------------------------------- 2. chiffres neufs à 65 536
titre("2. Chiffres neufs, sortie maximale envoyée à Google : 65 536 jetons")
print(f"sortie pleine : 65 536 × 15 ÷ 1 000 000 = {ex(sortie(NEUF))} USD (à 32 768 : {ex(sortie(ANCIEN))})")
print(f"réserve d'un envoi de la file, appariement : {ex(entree(CORPS_APP))} + {ex(sortie(NEUF))} = {ex(N['res_app'])} -> {fr(haut(N['res_app'], MILLE), 3)}")
print(f"réserve d'un envoi de la file, couverture : {ex(entree(CORPS_COUV))} + {ex(sortie(NEUF))} = {ex(N['res_couv'])} -> {fr(haut(N['res_couv'], MILLE), 3)}")
print(f"réserve d'un envoi de vérification (appels A, A′ et sonde), corps de 160 octets : {ex(entree(CORPS_VERIF))} + {ex(sortie(NEUF))} = {ex(N['res_ver'])} -> {fr(haut(N['res_ver'], MILLE), 3)}")
print(f"pire cas des seize envois de la file, sortie pleine : 2 × (6 × {ex(N['res_app'])} + 2 × {ex(N['res_couv'])}) = {ex(N['pire_file'])} -> {fr(haut(N['pire_file']))}")
par_cle = ENVOIS * (3 * N["res_app"] + N["res_couv"])
print(f"   par clé (trois lectures d'appariement, une de couverture, deux envois) : 2 × (3 × {ex(N['res_app'])} + {ex(N['res_couv'])}) = {ex(par_cle)} -> {fr(haut(par_cle))} ; les deux : {ex(2 * par_cle)}")
assert 2 * par_cle == N["pire_file"]
print(f"pire cas des trois envois d'une vérification : 3 × {ex(N['res_ver'])} = {ex(N['pire_ver'])} -> {fr(haut(N['pire_ver']))}")
print(f"plafond de la file, demi-dollar supérieur du pire cas : {fr(N['plaf_file'])} USD (marge {ex(N['plaf_file'] - N['pire_file'])})")
print(f"plafond d'une vérification, demi-dollar supérieur du pire cas : {fr(N['plaf_ver'])} USD (marge {ex(N['plaf_ver'] - N['pire_ver'])})")
assert (N["plaf_file"], N["plaf_ver"]) == (D("16.50"), D("3.00"))
corps_max_ver = bas((N["plaf_ver"] / 3 - sortie(NEUF)) * MILLION / PE, UN)
print(f"   le plafond de 3,00 laisse passer trois envois tant que le corps d'un appel ne passe pas ({fr(N['plaf_ver'])} ÷ 3 − {ex(sortie(NEUF))}) × 1 000 000 ÷ 3 = {fr(corps_max_ver, 0)} octets")
assert 3 * (entree(corps_max_ver) + sortie(NEUF)) <= N["plaf_ver"] < 3 * (entree(corps_max_ver + 1) + sortie(NEUF))
deux_res = 2 * N["res_ver"]
print(f"   au plafond de 1,50 gardé, deux envois comptés à leur réserve : 2 × {ex(N['res_ver'])} = {ex(deux_res)} -> {fr(haut(deux_res))}, au-dessus de 1,50 : le second serait refusé")
assert deux_res > D("1.50")
print(f"   coût d'un appel de vérification à sortie pleine : {ex(N['res_ver'])} -> {fr(haut(N['res_ver']))} (devis, 13, point 12 : 0,49)")
quatre = 4 * N["res_ver"]
print(f"   un quatrième envoi : 4 × {ex(N['res_ver'])} = {ex(quatre)}, au-dessus de {fr(N['plaf_ver'])} : refusé")
assert quatre > N["plaf_ver"]
octets_max_file = bas((N["plaf_file"] - 16 * sortie(NEUF)) * MILLION / PE / 2, UN)
print(f"   le plafond de 16,50 tient les seize envois à sortie pleine tant que les huit corps ne passent pas ensemble ({fr(N['plaf_file'])} − 16 × {ex(sortie(NEUF))}) × 1 000 000 ÷ 3 ÷ 2 = {fr(octets_max_file, 0)} octets (bornes du devis : 6 × 5 000 + 2 × 24 000 = 78 000)")
trois = N["pire_file"] * 3 / 2
print(f"   pour information, trois envois par appel (colonne du devis) : 3 ÷ 2 × {ex(N['pire_file'])} = {ex(trois)} -> {fr(haut(trois))} (devis : 12,50)")
seuil_refus = N["plaf_file"] - N["res_couv"]
print(f"seuil de refus du compteur avant un envoi de couverture : {fr(N['plaf_file'])} − {ex(N['res_couv'])} = {ex(seuil_refus)} -> {fr(bas(seuil_refus))} (vers le bas)")
print(f"sortie d'un envoi coupé, à 200 jetons par seconde : file, 2 690 × 200 × 15 ÷ 1 000 000 = {ex(N['coupe_file'])} ; vérification, 890 × 200 × 15 ÷ 1 000 000 = {ex(N['coupe_ver'])} (inchangées)")
print(f"excès possible d'un seul envoi, file : {ex(N['coupe_file'])} − {ex(sortie(NEUF))} = {ex(N['exc_file_x'])} -> {fr(N['exc_file'])}")
print(f"excès possible d'un seul envoi, vérification : {ex(N['coupe_ver'])} − {ex(sortie(NEUF))} = {ex(N['exc_ver_x'])} -> {fr(N['exc_ver'])}")
for debit in (D(100), D(400)):
    ef = haut(sortie(debit * RELAIS_FILE) - sortie(NEUF))
    ev = haut(sortie(debit * RELAIS_VERIF) - sortie(NEUF))
    print(f"   à {fr(debit, 0)} jetons par seconde : file {fr(ef)} ; vérification {fr(ev)}")
print(f"plafond et excès, ce que le compteur borne : vérification, {fr(N['plaf_ver'])} + {fr(N['exc_ver'])} = {fr(N['borne_ver'])} ; file, {fr(N['plaf_file'])} + {fr(N['exc_file'])} = {fr(N['borne_file'])}")
cout_coupe_app = entree(CORPS_APP) + N["coupe_file"]
cout_coupe_couv = entree(CORPS_COUV) + N["coupe_file"]
print(f"coût d'un envoi de la file coupé à 2 690 secondes : {ex(cout_coupe_app)} (appariement) ; {ex(cout_coupe_couv)} (couverture) -> {fr(haut(cout_coupe_app))} ; {fr(haut(cout_coupe_couv))} (inchangé)")
print(f"neuf envois coupés seuls : 9 × {ex(cout_coupe_app)} = {ex(9 * cout_coupe_app)} ; 6 × {ex(cout_coupe_app)} + 3 × {ex(cout_coupe_couv)} = {ex(6 * cout_coupe_app + 3 * cout_coupe_couv)} (inchangé : 72,77 et 72,94)")
print(f"   ces neuf envois, comptés à leur réserve au régime courant : 9 × {ex(N['res_app'])} = {ex(9 * N['res_app'])} -> {fr(haut(9 * N['res_app']))} (devis : 4,56)")
print(f"file, neuf excès : {fr(N['plaf_file'])} + 9 × {ex(N['exc_file_x'])} = {ex(N['neuf_x'])} -> {fr(N['neuf'])}")
print(f"   écart avec l'ancien : {ex(N['neuf_x'])} − {ex(A['neuf_x'])} = {ex(N['neuf_x'] - A['neuf_x'])} -> {fr(haut(N['neuf_x'] - A['neuf_x']))} = 8,00 de plafond − 9 × {ex(sortie(NEUF) - sortie(ANCIEN))}")
assert N["neuf_x"] - A["neuf_x"] == D(8) - 9 * (sortie(NEUF) - sortie(ANCIEN))
print(f"Google, deux vérifications, régime prudent ou supposition tenue : 2 × {fr(N['borne_ver'])} + {fr(N['borne_file'])} = {fr(N['prudent2'])}")
print(f"Google, deux vérifications, neuf excès : 2 × {fr(N['borne_ver'])} + {fr(N['neuf'])} = {fr(N['pire2'])} (exact : {ex(2 * (N['plaf_ver'] + N['exc_ver_x']) + N['neuf_x'])})")
print(f"   au-dessus du pire cas accepté sous GO-2026-11-21-68 : {fr(N['pire2'])} − 84,06 = {fr(N['pire2'] - D('84.06'))}")
exact_n = 2 * (N['plaf_ver'] + N['exc_ver_x']) + N['neuf_x']
exact_a = 2 * (A['plaf_ver'] + A['exc_ver_x']) + A['neuf_x']
print(f"   en valeurs exactes : {ex(exact_n)} − {ex(exact_a)} = {ex(exact_n - exact_a)} -> {fr(haut(exact_n - exact_a))}")
print(f"   une ligne nouvelle de vérification ajoute {fr(N['borne_ver'])}")
print(f"   avec une seule vérification : {fr(N['borne_ver'])} + {fr(N['borne_file'])} = {fr(N['borne_ver'] + N['borne_file'])} ; {fr(N['borne_ver'])} + {fr(N['neuf'])} = {fr(N['borne_ver'] + N['neuf'])} (avenant 1 : 19,76 et 80,38)")

# régime prudent
titre("2 bis. Régime prudent du compteur, à 65 536")
print(f"durée sous laquelle un envoi est compté à sa réserve : 65 536 ÷ 200 = {ex(NEUF / DEBIT)} -> {fr(haut(NEUF / DEBIT, UN), 0)} secondes")
compte_ver = entree(CORPS_VERIF) + N["coupe_ver"]
print(f"appel de vérification coupé à 890 secondes : compté {ex(compte_ver)} -> {fr(haut(compte_ver))}, sous le plafond de {fr(N['plaf_ver'])} ; "
      f"avec la réserve de l'envoi suivant, {ex(compte_ver + N['res_ver'])} -> {fr(haut(compte_ver + N['res_ver']))}, au-dessus : l'envoi suivant est refusé")
assert compte_ver < N["plaf_ver"] < compte_ver + N["res_ver"]
duree_lim = (N["plaf_ver"] - N["res_ver"] - entree(CORPS_VERIF)) / sortie(DEBIT)
print(f"   un appel coupé avant ({fr(N['plaf_ver'])} − {ex(N['res_ver'])} − {ex(entree(CORPS_VERIF))}) ÷ 0,003 = {ex(duree_lim)} secondes laisse partir l'envoi suivant (à 1,50 : {ex((A['plaf_ver'] - A['res_ver'] - entree(CORPS_VERIF)) / sortie(DEBIT))})")
print(f"file partie sur un mot de Lazar, envoi coupé à 2 690 secondes : compté {ex(cout_coupe_app)} ou {ex(cout_coupe_couv)}")
lim_app = N["plaf_file"] - cout_coupe_app - N["res_app"]
lim_couv = N["plaf_file"] - cout_coupe_couv - N["res_couv"]
print(f"   la reprise part si le cumul compté avant l'envoi coupé est d'au plus {fr(N['plaf_file'])} − {ex(cout_coupe_app)} − {ex(N['res_app'])} = {ex(lim_app)} (appariement) ; "
      f"{fr(N['plaf_file'])} − {ex(cout_coupe_couv)} − {ex(N['res_couv'])} = {ex(lim_couv)} (couverture) ; au plus bas des deux, vers le bas : {fr(bas(lim_couv))}")
print(f"   à 8,50 : 8,50 − {ex(cout_coupe_app)} − {ex(A['res_app'])} = {ex(A['plaf_file'] - cout_coupe_app - A['res_app'])} : négatif, la reprise était toujours refusée")
assert A["plaf_file"] - cout_coupe_app - A["res_app"] < 0 < lim_couv < lim_app
deux = 2 * cout_coupe_app
print(f"   deux envois coupés à 2 690 secondes : 2 × {ex(cout_coupe_app)} = {ex(deux)} ; avec la réserve du suivant, {ex(deux + N['res_app'])}, au-dessus de {fr(N['plaf_file'])} : la file s'arrête à son plafond")
assert deux + N["res_app"] > N["plaf_file"]
borne_prudent = N["plaf_file"] - N["res_couv"] + cout_coupe_couv
print(f"   borne de la dépense au régime prudent : ({fr(N['plaf_file'])} − {ex(N['res_couv'])}) + {ex(cout_coupe_couv)} = {ex(borne_prudent)} -> {fr(haut(borne_prudent))} = plafond et un excès")
assert haut(borne_prudent) == N["borne_file"]

# ---------------------------------------------------------------- 3. sommes
titre("3. Sommes des six lignes de calcul")
plaf_mistral = [D("0.25"), D("4.75"), D("0.25")]
exc_mistral = [D("1.17"), D("0.64"), D("1.17")]
plaf_google = [N["plaf_ver"], N["plaf_ver"], N["plaf_file"]]
exc_google = [N["exc_ver"], N["exc_ver"], N["exc_file"]]
sp, se = sum(plaf_mistral) + sum(plaf_google), sum(exc_mistral) + sum(exc_google)
print(f"plafonds : Mistral 0,25 + 4,75 + 0,25 = {fr(sum(plaf_mistral))} ; Google {fr(N['plaf_ver'])} + {fr(N['plaf_ver'])} + {fr(N['plaf_file'])} = {fr(sum(plaf_google))} ; ensemble {fr(sp)} (sans la ligne 5 : {fr(sp - D('0.25'))}) ; avenant 1 : 16,75")
print(f"excès, un par ligne : Mistral 1,17 + 0,64 + 1,17 = {fr(sum(exc_mistral))} ; Google {fr(N['exc_ver'])} + {fr(N['exc_ver'])} + {fr(N['exc_file'])} = {fr(sum(exc_google))} ; ensemble {fr(se)} (sans la ligne 5 : {fr(se - D('1.17'))}) ; avenant 1 : 14,92")
print(f"plafonds et excès : {fr(sp)} + {fr(se)} = {fr(sp + se)} (sans la ligne 5 : {fr(sp + se - D('1.42'))}) ; avenant 1 : 31,67 ; recoupe 8,23 + {fr(N['prudent2'])} = {fr(D('8.23') + N['prudent2'])}")
assert sp + se == D("8.23") + N["prudent2"]
print(f"   avec les lignes de Mistral et une seule vérification de Google : 8,23 + {fr(N['seuil_ver'])} = {fr(D('8.23') + N['seuil_ver'])} (devis, ligne 563 : 27,99)")
pires = [D("3.99"), haut(N["pire_file"]), D("0.23"), D("0.23"), haut(N["pire_ver"]), haut(N["pire_ver"])]
print(f"pire cas à la sortie maximale, tous envois (colonne du devis, 6.3) : 3,99 + {fr(pires[1])} + 0,23 + 0,23 + {fr(pires[4])} + {fr(pires[5])} = {fr(sum(pires))} (devis : 14,26 ; avec la seconde vérification à 1,48 : 15,74)")
print("attendu : inchangé, ≈ 0,57 USD (devis 0,55, plus 0,02 pour la seconde vérification) : il ne dépend pas de la sortie maximale")
print(f"   attendu chez Google seul : 0,34 + 0,02 + 0,02 = {fr(D('0.34') + D('0.02') + D('0.02'))} USD (devis, 6.3)")

# ---------------------------------------------------------------- 4. crédit
titre("4. Seuils de crédit par projet, et manque en euros")
src = open(sys.argv[1], encoding="utf-8").read()
jour = re.search(r"<Cube time='([0-9-]+)'>", src).group(1)
T = D(re.search(r"<Cube currency='USD' rate='([0-9.]+)'/>", src).group(1))
assert T == T_OD and jour == "2026-11-20"
MARGE = D("0.05")
TC = T * (1 - MARGE)
print(f"taux relevé : {fr(T, 4)} USD pour 1 €, fixage du {jour} ; diminué de 5 % : {fr(T, 4)} × 0,95 = {ex(TC)}")
print(f"seuil avant chaque vérification de clé : {fr(N['borne_ver'])} + {fr(N['borne_file'])} = {fr(N['seuil_ver'])} USD (avenant 1 : 19,76)")
print(f"seuil avant la file du juge : {fr(N['seuil_file'])} USD (avenant 1 : 16,08)")


def compte(euros):
    return bas(euros * TC)


def euros_requis(usd):
    e = haut(usd / TC)
    assert compte(e) >= usd > compte(e - CENT), (usd, e)
    return e


cA, cB = compte(B_A), compte(B_B)
print(f"crédit compté aujourd'hui, solde seul : projet à 11,93 € : 11,93 × {ex(TC)} = {ex(B_A * TC)} -> {fr(cA)} USD ; projet à 15,59 € : 15,59 × {ex(TC)} = {ex(B_B * TC)} -> {fr(cB)} USD (un crédit se compte vers le bas)")
print(f"   ni l'un ni l'autre n'atteint {fr(N['seuil_file'])}, ni même le plafond seul de la file, {fr(N['plaf_file'])} ; à l'ancien plafond de 8,50, les deux le couvraient")
assert max(cA, cB) < N["plaf_file"] < N["seuil_file"]
att = D("0.02")
cas = [
    ("vérification de la clé 1 (ligne 2), première ligne de Google", N["seuil_ver"], D(0), D(0)),
    ("vérification de la clé 2 (ligne 6)", N["seuil_ver"], N["borne_ver"], att),
    ("file du juge (ligne 4)", N["seuil_file"], 2 * N["borne_ver"], 2 * att),
]
print("ligne | seuil | dépense retirée (pire ; attendue) | crédit compté à avoir | euros à voir | manque à 11,93 € | manque à 15,59 €")
besoins = {}
for nom, seuil, pire, attendu in cas:
    for etiquette, ret in (("pire", pire), ("attendu", attendu)):
        usd = seuil + ret
        eur = euros_requis(usd)
        besoins[(nom, etiquette)] = eur
        print(f"{nom} | {fr(seuil)} | {etiquette} : {fr(ret)} | {fr(seuil)} + {fr(ret)} = {fr(usd)} USD | {fr(usd)} ÷ {ex(TC)} = {tronque(usd / TC, 4)} -> {fr(eur)} € | {fr(max(D(0), eur - B_A))} € | {fr(max(D(0), eur - B_B))} €")
pire_eur = max(v for (n_, e_), v in besoins.items() if e_ == "pire")
att_eur = max(v for (n_, e_), v in besoins.items() if e_ == "attendu")
print(f"pour passer les trois lignes même au pire : {fr(pire_eur)} € vus sur chaque projet ; manque {fr(pire_eur - B_A)} € et {fr(pire_eur - B_B)} €, soit {fr(2 * pire_eur - B_A - B_B)} € en tout")
print(f"   contrôle : {fr(pire_eur)} € comptent pour {fr(compte(pire_eur))} USD ; {fr(pire_eur - CENT)} € pour {fr(compte(pire_eur - CENT))} USD ; les deux projets ensemble : 2 × {fr(pire_eur)} = {fr(2 * pire_eur)} €")
print(f"au plus juste, vérifications à leur attendu de 0,02 USD chacune : {fr(att_eur)} € vus sur chaque projet ; manque {fr(att_eur - B_A)} € et {fr(att_eur - B_B)} €, soit {fr(2 * att_eur - B_A - B_B)} € en tout")
print(f"   alors la seconde vérification ne part que si la première est comptée au plus {fr(compte(att_eur) - N['seuil_ver'])} USD, et la file que si les deux le sont au plus {fr(compte(att_eur) - N['seuil_file'])} USD ensemble")
for d1 in (D("0.25"), D("1.00")):
    print(f"   première vérification comptée {fr(d1)} USD : {fr(N['seuil_ver'] + d1)} USD, soit {fr(euros_requis(N['seuil_ver'] + d1))} € vus par projet")
anc = {"avant une vérification, la première": D("19.76"), "avant la seconde vérification ou la file, au pire": D("23.44")}
for nom, usd in anc.items():
    eur = euros_requis(usd)
    print(f"pour mémoire, aux seuils de l'avenant 1, {nom} : {fr(usd)} USD -> {fr(eur)} € ; manque {fr(eur - B_A)} € et {fr(eur - B_B)} €")
print(f"   le journal (OD-301) écrit 22,40 € pour 23,44 USD : 22,40 € comptent pour {fr(compte(D('22.40')))} USD, sous 23,44 ; la règle de l'avenant 1 demande {fr(euros_requis(D('23.44')))} €")
anc_pire = euros_requis(D("23.44"))
print(f"   versement de plus que le plafond neuf demande, au pire : {fr(2 * pire_eur - B_A - B_B)} − ({fr(anc_pire - B_A)} + {fr(anc_pire - B_B)} = {fr(2 * anc_pire - B_A - B_B)}) = {fr((2 * pire_eur - B_A - B_B) - (2 * anc_pire - B_A - B_B))} €")
print(f"   besoin propre d'une vérification, sans la file : {fr(N['borne_ver'])} USD -> {fr(euros_requis(N['borne_ver']))} € : les deux soldes le couvrent")
print(f"essai chiffré de la règle (avenant 1, section 7, point 7), valeurs neuves : cas sain, dépenses de {fr(N['borne_ver'])} et 0,02, deux projets distincts, crédit compté de {fr(N['seuil_ver'])} : "
      f"{fr(N['seuil_ver'])} − {fr(N['borne_ver'])} = {fr(N['seuil_ver'] - N['borne_ver'])}, la file part ; artefact, somme retirée : {fr(N['seuil_ver'])} − {fr(N['borne_ver'] + att)} = {fr(N['seuil_ver'] - N['borne_ver'] - att)}, sous {fr(N['seuil_file'])}")

# ---------------------------------------------------------------- 5. délais
titre("5. Débit requis et délais")
print(f"débit qui tient 65 536 jetons en 2 690 secondes : 65 536 ÷ 2 690 = {tronque(NEUF / RELAIS_FILE, 4)} -> {fr(haut(NEUF / RELAIS_FILE, DIXIEME), 1)} jetons par seconde (à 32 768 : 12,2)")
print(f"à 12,2 jetons par seconde, 2 690 secondes rendent {ex(D('12.2') * RELAIS_FILE)} jetons ; à 24,4 : {ex(D('24.4') * RELAIS_FILE)}")
print(f"appel de vérification à sortie pleine en 890 secondes : 65 536 ÷ 890 = {tronque(NEUF / RELAIS_VERIF, 4)} -> {fr(haut(NEUF / RELAIS_VERIF, DIXIEME), 1)} jetons par seconde (à 32 768 : {fr(haut(ANCIEN / RELAIS_VERIF, DIXIEME), 1)}) ; le devis ne l'exige pas")
print(f"délai global de la file du juge : 8 × (2 × 2 700 + 600 + 10) + 600 = {fr(D(8 * (2 * 2700 + 600 + 10) + 600), 0)} secondes ; d'un lancement de vérification : 3 × 900 + 600 = {fr(D(3 * 900 + 600), 0)} : inchangés")
print(f"durée d'une lecture de 65 536 jetons : à 24,4 jetons par seconde, {tronque(NEUF / D('24.4'), 1)} secondes ; à 12,2, {tronque(NEUF / D('12.2'), 1)} ; à 50, {tronque(NEUF / D(50), 1)}")
duree = NEUF / D("12.2")
print(f"pour information, délai qui garderait 12,2 jetons par seconde : 65 536 ÷ 12,2 = {tronque(duree, 1)} secondes -> relais 5 390, délai 5 400 (65 536 ÷ 5 390 = {tronque(NEUF / D(5390), 4)})")
coupe_long = sortie(DEBIT * D(5390))
exc_long = coupe_long - sortie(NEUF)
print(f"   alors : sortie d'un envoi coupé {ex(coupe_long)} ; excès {ex(exc_long)} -> {fr(haut(exc_long))} ; plafond et excès de la file {fr(N['plaf_file'] + haut(exc_long))} ; neuf excès {fr(haut(N['plaf_file'] + 9 * exc_long))} ; "
      f"Google, deux vérifications : {fr(2 * N['borne_ver'] + N['plaf_file'] + haut(exc_long))} et {fr(2 * N['borne_ver'] + haut(N['plaf_file'] + 9 * exc_long))} ; délai global 8 × (2 × 5 400 + 600 + 10) + 600 = {fr(D(8 * (2 * 5400 + 600 + 10) + 600), 0)} secondes")

# ---------------------------------------------------------------- 6. réflexion
titre("6. Borne de réflexion et plafond de texte")
borne = NEUF - MARGE_TEXTE
print(f"plus grande borne de réflexion qui passe la garde : 65 536 − 16 000 = {fr(borne, 0)} jetons ; plafond de texte : 65 536 − {fr(borne, 0)} = {fr(NEUF - borne, 0)}")
print(f"à l'ancien plafond : 32 768 − 16 000 = {fr(ANCIEN - MARGE_TEXTE, 0)} (la valeur d'essai de la livraison 4)")
for ratio in (D("1.5"), D(2), D(3), D(4)):
    print(f"   limite de mots qui tient dans 16 000 jetons à {ex(ratio)} jeton(s) par mot : {fr(bas(MARGE_TEXTE / ratio, UN), 0)} mots")

# ---------------------------------------------------------------- 7. sensibilité
titre("7. Sensibilité au débit déclaré : 400 jetons par seconde au lieu de 200")
ef4x = sortie(D(400) * RELAIS_FILE) - sortie(NEUF)
ev4x = sortie(D(400) * RELAIS_VERIF) - sortie(NEUF)
ef4, ev4 = haut(ef4x), haut(ev4x)
print(f"excès : vérification {ex(ev4x)} -> {fr(ev4)} ; file {ex(ef4x)} -> {fr(ef4)}")
print(f"Google, deux vérifications, régime prudent : 2 × ({fr(N['plaf_ver'])} + {fr(ev4)}) + {fr(N['plaf_file'])} + {fr(ef4)} = {fr(2 * (N['plaf_ver'] + ev4) + N['plaf_file'] + ef4)} (avenant 1 : 36,85)")
print(f"Google, deux vérifications, neuf excès : 2 × {fr(N['plaf_ver'] + ev4)} + {fr(N['plaf_file'])} + 9 × {ex(ef4x)} = {ex(2 * (N['plaf_ver'] + ev4) + N['plaf_file'] + 9 * ef4x)} -> {fr(haut(2 * (N['plaf_ver'] + ev4) + N['plaf_file'] + 9 * ef4x))} (avenant 1 : 162,05)")
print(f"avec une seule vérification : {fr(N['plaf_ver'])} + {fr(ev4)} + {fr(N['plaf_file'])} + {fr(ef4)} = {fr(N['plaf_ver'] + ev4 + N['plaf_file'] + ef4)} ; {fr(N['plaf_file'])} + 9 × {ex(ef4x)} = {ex(N['plaf_file'] + 9 * ef4x)} -> {fr(haut(N['plaf_file'] + 9 * ef4x))} (avenant 1 : 30,50 et 149,35)")
print()
print("fin : toutes les assertions passent")
