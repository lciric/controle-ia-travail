"""Arithmétique du devis de (ii-b), v2 (développeur du code, 10 novembre 2026 ; nom neuf, R12 : la v1 reste telle quelle).

Reprend toutes les entrées de `calcul-devis-ii-b-v1.py` (débits de 7a, prix, stockage, téléchargement) et change, d'après le
code `src/controle_ia/iib/` (branche `prep/ii-b-code-v1`) et GO-2026-11-10-08 (R-2175) :
- juge de T0.8 : NON joué par le code v1 (forme non scellée ; la configuration le refuse) → 0 h ;
- activité interne (ajout R-2175) : une passe avant par épisode d'évaluation (256), estimée à 0,5 s chacune (prudent :
  ≈ 3 000 jetons, une passe sans génération), plus l'écriture des jetons des actions aux couches 7, 15, 23 en demi-précision
  (2 560 actions × L jetons × 4 096 × 2 octets × 3), à 200 Mo/s (prudent) ; L = 250 jetons attendu, 400 au pire
  (`max_nouveaux`) ; NON MESURÉ ;
- sortie des activations de l'instance : volume ci-dessus, compté au prix de téléchargement (≤ 0,05 USD/Go), faute d'un
  prix de sortie relevé (hypothèse, déclarée) ;
- jumeau : forme « cache dupliqué » (un préremplissage, huit suites de 16 jetons au plus sur un lot de 8) : 0,5 à 1,0 s
  attendu ; « prérempli par suite » si l'épreuve de forme échoue : 1,5 s ; pire 3,0 s (inchangé) ; NON MESURÉ.
Variante de plafond : B (ligne 60 USD, coupure 55, A100 seule), retenue par GO-2026-11-10-08 ; A rappelée pour comparaison.
"""
from __future__ import annotations

import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location("v1", Path(__file__).with_name("calcul-devis-ii-b-v1.py"))
v1 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(v1)

PASSE_S = 0.5
DEBIT_ECRITURE_GO_S = 0.2
LARGEUR, COUCHES = 4096, 3
N_ACTIONS_EVAL = v1.N_EVAL_EP * v1.T


def go_activites(jetons_par_action: float) -> float:
    return N_ACTIONS_EVAL * jetons_par_action * LARGEUR * 2 * COUCHES / 1e9


def heures(tours, t_j, n_acc, lent=1.0, jetons=250):
    h = v1.heures(tours, t_j, n_acc, lent=1.0, juge=False)
    h.pop("total")
    h.pop("juge T0.8 en une passe (option, lecture 2)")
    h["activité interne : passes et écriture"] = (v1.N_EVAL_EP * PASSE_S + go_activites(jetons) / DEBIT_ECRITURE_GO_S) / 3600
    h = {k: v * lent for k, v in h.items()}
    h["total"] = sum(h.values())
    return h


def usd(total_h, prix, stockage_h, telech_go, jetons):
    c, s = total_h * prix, stockage_h * v1.STOCKAGE_USD_H
    t, a = telech_go * v1.TELECH_USD_GO, go_activites(jetons) * v1.TELECH_USD_GO
    return c, s, t, a, c + s + t + a


def imprimer(nom, h, prix, stockage_h, telech_go, jetons):
    print(f"\n## {nom}")
    for k, v in h.items():
        print(f"  {k} : {v:.2f} h")
    print(f"  activité interne : {go_activites(jetons):.1f} Go ({jetons} jetons par action)")
    for p in prix:
        c, s, t, a, tot = usd(h["total"], p, stockage_h, telech_go, jetons)
        print(f"  à {p:.4g} USD/h : carte {c:.1f} + stockage arrêté ≤ {s:.1f} ({stockage_h} h) + téléchargement ≤ {t:.1f} "
              f"({telech_go} Go) + sortie des activations ≤ {a:.1f} = {tot:.1f} USD ; sous la coupure de 55 : "
              f"{'oui' if tot <= 55 else 'NON'} (marge {55 - tot:.1f})")


print("Devis (ii-b), v2 — heures de carte ; USD ; variante B (ligne 60, coupure 55, A100 seule)")
imprimer("Attendu bas : 6 tours, jumeau 0,5 s, 96 acceptés", heures(6, 0.5, 96), [1.0889, 1.12], 24, 20, 250)
imprimer("Attendu central : 10 tours, jumeau 1,0 s, 96 acceptés", heures(10, 1.0, 96), [1.12, 1.30], 24, 20, 250)
imprimer("Attendu haut : 12 tours, jumeau 1,5 s, 127 acceptés, 400 jetons", heures(12, 1.5, 127, jetons=400), [1.30], 24, 20, 400)
h = heures(4, 1.0, 0)
for k in ("distillation (élève et témoin-jumeau)", "évaluation : épisodes", "évaluation : jumeau (lecture 1)",
          "activité interne : passes et écriture"):
    h["total"] -= h.pop(k)
imprimer("Arrêt précoce M-1 au tour 4 (rien de distillé, aucune activité)", h, [1.12, 1.30], 24, 20, 0)
imprimer("Pire P1 : hôte deux fois plus lent, 12 tours, jumeau 3,0 s, 127 acceptés, 400 jetons", heures(12, 3.0, 127, lent=2.0,
         jetons=400), [1.30, 1.40], 48, 40, 400)
p = heures(12, 3.0, 127, lent=2.0, jetons=400)["total"]
print(f"\n## Prix horaire maximal de la carte pour que P1 tienne sous 55 USD : "
      f"{(55 - 48 * v1.STOCKAGE_USD_H - 40 * v1.TELECH_USD_GO - go_activites(400) * v1.TELECH_USD_GO) / p:.3f} USD/h")
hp = heures(12, 1.5, 127, jetons=400)["total"]
print(f"## Variante A rappelée : H200 NVL d'emblée à 4,70 USD/h, haut de l'attendu : {hp:.2f} h → "
      f"{hp * 4.70 + 48 * 0.08 + 40 * 0.05 + go_activites(400) * 0.05:.1f} USD ; heures permises sous 75 : "
      f"{(75 - 48 * 0.08 - 40 * 0.05 - go_activites(400) * 0.05) / 4.70:.2f} h (marge {(75 - 48 * 0.08 - 40 * 0.05 - go_activites(400) * 0.05) / 4.70 - hp:.2f} h)")
