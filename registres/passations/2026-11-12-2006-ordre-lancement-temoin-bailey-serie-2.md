# Ordre de lancement — témoin de Bailey, nouvelle série (addendum 3), poste Hetzner v8 — 12 novembre 2026, 20:06 UTC

Session `session_01XJ6MgnEhQMZteN9F8a1BST`, branche `claude/compassionate-meitner-d4ryyk`. Écrit **avant la création**
du poste et de l'instance (condition 8). Ne se réécrit pas (R12).

| Champ | Valeur |
|---|---|
| Addendum | `prereg/temoin-attaque-publiee-bailey-v1-addendum-3-code-v16-message-erreur-nouvelle-serie.md` (`4b1f33bf…`), scellé au commit `965d712b` (2026-11-12T20:05:10Z) ; **pas encore déposé chez le tiers** : daté par son commit (addendum 3, § 6, condition 6) |
| Mot de lancement | « go (a) » tenu pour mot de lancement (« go 1a 2a′ 3b », § 7.3) |
| GO | `GO_ID=GO-2026-11-10-10` (amendé `GO-2026-11-11-01`, modèle `GO-2026-11-11-02`) ; présent sur `origin/main`, non révoqué (relu à 20:05Z) ; la conduite le relit |
| B, D | B = 75 USD ; D antérieure = 1,976 USD (quatre instances détruites) |
| Code | commit `91238a735a2127a0879fb4533a6cde5baccb4efa` (`lanceur_v16`, `instance_v15`) ; garde du poste : `src/` de la tête identique (vérifié ici à 20:05Z) |
| Manifeste | `runs/temoin-bailey-v1-20261111/manifeste-local-v4.json` (`e15d456f…`) |
| Conduite | `runs/temoin-bailey-v1-20261111/lancer-conduite-v8.py` (`a02f7b5b…`), sortie `/home/user/controle-ia-travail/runs/temoin-bailey-v1-20261111/sortie-conduite-v8`, disque 110 Go |
| Poste | `poste-hetzner-v8.sh` (`6969fd53…`), constructeur `construire-donnees-demarrage-v8.py` (`2346cff3…`) ; offre choisie par le poste (filtre 128,9 Go, disque 115 Go) ; relevé à 20:05Z : 59431034 (Texas, ≈ 1,43 USD/h avec 110 Go) et 59306789 (Caroline du Nord) |
| Image | `runpod/pytorch:2.4.0-py3.11-cuda12.4.1-devel-ubuntu22.04` |
| `DEPOT_URL` | `https://github.com/lciric/controle-ia-travail.git` |
| Surveillance | réveils au plus toutes les 60 minutes ; alerte à Lazar si le pilote n'a pas fini 4 h après son lancement (§ 7.2) ; aucune note lue avant la fin du run principal et le scellement |
