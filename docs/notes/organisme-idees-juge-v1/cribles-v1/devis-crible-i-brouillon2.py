"""Devis et comptes du crible (i), placebo par monde jumeau, brouillon 2 — processeur seul, aucun appel, aucune donnée de monde.

Programme neuf (R12) : copie de `devis-crible-i-brouillon1.py` (92932a6a8f51aa84dfceeac336750147771e3bf7862d95c8f4a3bee7023fe475),
dont seul le point 5 change (correction M3 de la contre-lecture du tour 1, `contre-lecture-crible-i-tour1-v1.md`, bb5829b0…) :
le budget de pire cas compte la mise en place ET le rapatriement à 1 800 s chacun, triplés (3 x (1 800 + 1 800)), comme le
texte le dit ; le brouillon 1 les comptait ensemble pour 1 800 s.

Entrées recopiées (aucune lecture de fichier) : section « Pour les cribles » et « Dépense rapprochée » du verdict v2 du pilote
MR-2 v14 (`e64458e8…`) ; plafonds et prix de la configuration v12 tels que les brouillons 8 de (iii) et 9 de (v) les recopient ;
pires cas des cribles (iii) et (v) tels que leurs sorties de devis des versions qui feront foi les donnent.
Usage : python -I devis-crible-i-brouillon2.py
"""
import math
from scipy.stats import binom

# --- pilote (verdict v2) ---
pr2_total, pr2_n = 1.057336, 4            # Pr-2, prix public = prix de la configuration (4 / 20)
pr1_total_public = 0.494324                   # Pr-1, prix public (sortie du devis (v) foi v1, point 2)
pr1_total_config = 2.471620
duree_pr2 = [109.396, 54.737, 72.991, 36.425]
prix_h = 0.052222
# --- configuration v12 (bloc gelé, recopié par (iii) et (v)) ---
plafond = {"Pr-2": 2.00, "Pr-1": 2.34}
prix_entree = {"Pr-2": 4.0, "Pr-1": 2.0}        # USD par million, public
N, bras = 20, 3

print("== 1. Attendu par appel (règle (b) de (v) : moyenne de tous les appels du pilote) ==")
a2 = pr2_total / pr2_n
print(f"Pr-2 : {a2:.6f} USD par appel ; Pr-1 : public {pr1_total_public/4:.6f}, configuration {pr1_total_config/4:.6f}")
print("fourchette par appel : coûts par appel non transmis par le verdict v2 ; bornes : plus petit <= moyenne <= plus grand <= total")

print("\n== 2. Surcoût d'entrée de la table (estimé, avant le constructeur) ==")
for octets in (2800, 4000, 6000):
    jetons = octets / 3.0                        # 3 octets par jeton supposés (texte de nombres), comme (v)
    print(f"table de {octets} octets ≈ {jetons:.0f} jetons : Pr-2 {jetons*prix_entree['Pr-2']/1e6:.4f} USD par appel ; "
          f"40 appels à table : {40*jetons*prix_entree['Pr-2']/1e6:.3f} USD")

print("\n== 3. Devis, variante « crédits de Claude au maximum » (Pr-2 seul) ==")
for n in (20, 24, 30):
    att_app = bras * n * a2 + 2 * n * 4000 / 3.0 * 4.0 / 1e6
    pire_app = bras * n * plafond["Pr-2"]
    sonde_att, sonde_pire = 2 * a2, 2 * plafond["Pr-2"]
    # machine attendue : barrières 6 000 s + mondes (12 min pour 4 au pilote, d'après [PROC-14] § 6 cité par (v)) + appels
    # (un monde à la fois, plus long des trois appels ≈ plus long appel de Pr-2 au pilote) + mesure (≈ 0,5 h, estimée)
    t = 6000 + n / 4 * 720 + n * max(duree_pr2) + 1800
    print(f"N={n} : appels {bras*n} ; attendu appels {att_app:.2f} ; pire appels {pire_app:.2f} ; sonde {sonde_att:.2f} / {sonde_pire:.2f} ; "
          f"machine attendue {t/3600:.2f} h = {t/3600*prix_h:.3f} USD (pire 3,00)")
    print(f"      crédits : attendu {att_app+sonde_att:.2f}, pire {pire_app+sonde_pire:.2f} ; hors crédits : attendu {t/3600*prix_h:.3f}, pire 3.00 ; "
          f"total pire {pire_app+sonde_pire+3:.2f}")

print("\n== 4. Forme fidèle à la note (Pr-1 seul, hors crédits), information ==")
print(f"N=20 : attendu public {60*pr1_total_public/4:.2f}, configuration {60*pr1_total_config/4:.2f} ; pire {60*plafond['Pr-1']:.2f} + machine 3,00")

print("\n== 5. Durée et borne par appel (règle de ce texte) ==")
lp = max(duree_pr2)
Ba = max(600, 300 * math.ceil(3 * lp / 300)); Ba = min(Ba, 3600)
print(f"plus long appel de Pr-2 au pilote {lp} s ; 3 x = {3*lp:.1f} s ; B_a = {Ba} s")
for M in (1, 2):
    pire = 6000 + 3 * (N / 4 * 720) + math.ceil(N / M) * Ba + 3 * 1800 + 3 * (1800 + 1800)
    print(f"M={M} : budget de pire cas (barrières 6 000 s + 3 x génération + ceil(N/M) x B_a + 3 x mesure + 3 x (mise en place + rapatriement), ces deux derniers estimés à 1 800 s chacun) = {pire:.0f} s = {pire/3600:.2f} h (<= 17 h : {pire <= 61200})")

print("\n== 6. Probabilité d'atteindre le minimum de 16 mondes complets sur 20 (trois appels répondus par monde) ==")
for p in (1.0, 0.97, 0.95, 0.90, 0.875):
    q = p ** 3
    print(f"taux par appel {p} : P(monde complet) = {q:.4f} ; P(n_c >= 16) = {binom.sf(15, 20, q):.4f}")

print("\n== 7. Test exact apparié des signes, seuils ==")
for a in (0.025, 0.05):
    print(f"niveau unilatéral {a} : pour d discordants, plus petit b rejeté : " +
          ", ".join(f"d={d}:{min([b for b in range(d+1) if binom.sf(b-1, d, .5) <= a] or [None]) if any(binom.sf(b-1,d,.5)<=a for b in range(d+1)) else '—'}" for d in range(1, 13)))

print("\n== 8. Enveloppe de GO-2026-11-15-06 (1 275 USD au pire) ==")
iii, v = 270.00, 204.67      # pires des versions qui feront foi : (iii) sonde comprise ; (v) sonde neuve comprise
i20 = bras * 20 * plafond["Pr-2"] + 2 * plafond["Pr-2"] + 3.00
for nom, i in (("(i) N=20", i20), ("(i) N=24", bras*24*2+4+3), ("(i) N=30", bras*30*2+4+3)):
    tot = iii + v + i
    print(f"{nom} : {i:.2f} ; avec (iii) et (v) : {tot:.2f} ; reste pour (ii) et (iv) : {1275 - tot:.2f} ; "
          f"(ii) 483 et (iv) 243 de la note : cumul {tot + 726:.2f}")
