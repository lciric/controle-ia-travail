# Ordre de lancement v4 — témoin de l'attaque publiée de Bailey — 12 novembre 2026, vers 08:30 UTC

Session `session_01XJ6MgnEhQMZteN9F8a1BST`, branche `claude/compassionate-meitner-d4ryyk`. Écrit **avant la création**
(condition 8). Ne se réécrit pas (R12). Mot de Lazar : « go (a) si le test réussit » ; test réussi
(`2026-11-12-0827-test-maintien-machine-session.md`).

| Champ | Valeur |
|---|---|
| GO | `GO_ID=GO-2026-11-10-10` (amendé `GO-2026-11-11-01`, modèle `GO-2026-11-11-02`), `origin/main` `bc01e23282dc2e337bcf088ec22a970b68a371be` (2026-11-12T08:26:17Z) |
| B | **75 USD** (fixé à la création de 60280913) ; arrêt à B − 2 |
| D avant création | ≈ 0,73 USD (60280913 ≈ 0,31 ; 60326443 ≈ 0,42 ; toutes deux dans `instances_anterieures`) |
| Offre | **57426813**, A100 SXM4 80 Go, Oregon (États-Unis), 258 Go de mémoire, fiabilité 0,992, vérifiée, CUDA 13.0 ; seule offre conforme à 08:27Z (même hôte et même taux que l'offre acceptée par Lazar dans la nuit) |
| Taux relevé (recherche, 08:27Z) | 1,336 USD/h hors stockage ; ≈ 1,61 USD/h avec 200 Go ; c réel relevé par la conduite |
| Image | `runpod/pytorch:2.4.0-py3.11-cuda12.4.1-devel-ubuntu22.04` |
| `DEPOT_URL` | `https://github.com/lciric/controle-ia-travail.git` |
| Commit du code | `4988f3f442c670887a0e8ad15ddfbac68a173d03` |
| Manifeste | `runs/temoin-bailey-v1-20261111/manifeste-local-v3.json` (`69143b99…`) |
| Script | `runs/temoin-bailey-v1-20261111/lancer-conduite-v4.py` (`180bc10d…`) ; PID dans `lancement-v4.pid` |
| Sortie | `/home/user/controle-ia-travail/runs/temoin-bailey-v1-20261111/sortie-conduite-v4` |
| Machine du poste | tenue allumée par des tâches d'arrière-plan suivies, enchaînées ; surveillance au plus toutes les 60 minutes |
| Addendum 2 du témoin | déposé chez le tiers le 2026-11-11T23:13:50Z |
