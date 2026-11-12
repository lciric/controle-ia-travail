# Ordre de lancement — témoin de Bailey, nouvelle série (addendum 3), conduite v9 — 12 novembre 2026, 20:50 UTC

Session `session_01XJ6MgnEhQMZteN9F8a1BST`. Écrit **avant la création** (condition 8). Ne se réécrit pas (R12). Suit
`2026-11-12-2040-…` (`d48670b4…` : échec de l'envoi de l'archive, série non consommée).

Mot de Lazar (≈ 20:40Z) : « ne détruis rien relance avec correction non ? ».

Identique à l'ordre `2026-11-12-2006-…` (`6e7b55e1…`), sauf :
- **Correction (paramètre de lancement, code du run inchangé au commit `91238a73`)** : la conduite reçoit
  `FournisseurVastReprises` (`lancer-conduite-v9.py`), dont `envoyer_fichier` retente un `scp` en échec (3 essais, 20 s
  d'écart) ; épreuves : 2 échecs puis réussite → réussite ; échecs répétés → l'erreur sort après 3 essais ; refus sans
  `GO_ID`.
- Conduite : `runs/temoin-bailey-v1-20261111/lancer-conduite-v9.py` ; sortie `…/sortie-conduite-v9` ; instances
  antérieures : cinq (D = 2,033 USD).
- Poste : `poste-hetzner-v9.sh`, constructeur `construire-donnees-demarrage-v9.py` (v9 = v8 avec la conduite v9 ; garde
  du code `src/` identique au commit `91238a73` gardée).
- Addendum 3 : toujours pas déposé chez le tiers ; daté par son commit (`965d712b`).
