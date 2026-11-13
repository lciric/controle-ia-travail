# Ordre de lancement — témoin de Bailey, relance seule (addendum 5, condition 9′ de l'addendum 6), poste Hetzner v12 — 13 novembre 2026

Session `session_01XJ6MgnEhQMZteN9F8a1BST`, branche `claude/compassionate-meitner-d4ryyk`. Écrit **avant la création**
du poste et de l'instance (condition 8). Ne se réécrit pas (R12). Heure réelle du relevé : 2026-11-13T09:43:10Z.

| Champ | Valeur |
|---|---|
| Mot de lancement (condition 7) | Lazar, verbatim : « lance la relance » (≈ 09:42Z), en réponse à la demande qui citait l'addendum 6 (chemin, `982bfbcb…`), le relevé de 9′ (S, c₀, o), ses risques et le tirage attendu sur la carte (24 à 45 USD) ; vaut décision du nœud de l'écart de l'addendum 6 |
| Addenda | 5 : `prereg/temoin-attaque-publiee-bailey-v1-addendum-5-relance-seule-code-v20.md` (`eb97994a…`) ; 6 : `…-addendum-6-credit-recharge-auto.md` (`982bfbcb…`) ; tous deux sur la tête poussée `5f912c8a` (vérifié par `git ls-remote` à 09:43Z) ; pas encore déposés chez le tiers : datés par leurs commits |
| Condition 9′ (relevé 09:43:10Z) | `credit` 28,6386 ; `balance` 0 ; `has_billing` vrai ; `autobill_threshold` 5 ; `autobill_amount` 5 ; `billing_failed` faux ; c₀ = 1,1733 USD/h (5 offres du filtre) ; o = 0,1005 USD/h (58936096, 58936099, 58936100 arrêtées, stockage) ; S = max(20 ; 11 × (1,7 + 0,1005)) = 20,0 USD ; **remplie** (28,64 ≥ 20). Le poste prend une offre au plus tôt ; s'il attend plus d'une heure, la session refait le relevé ou arrête le poste (R10) |
| GO | `GO_ID=GO-2026-11-10-10` (amendé `GO-2026-11-11-01`, modèle `GO-2026-11-11-02`) ; présent sur `origin/main` (relu à 09:43Z) ; la conduite le relit |
| B, D | B = 75 USD ; D des sept instances antérieures ≈ 14,44 USD (compte prudent) |
| Code | commit `f60c2620a3891ebe579a807b2a90afb06e9e3ea5` (`lanceur_v20` ; instance `instance_v16`, exécution `execution_v4`) ; `src/` de la tête identique (garde du poste v12) |
| Manifeste | `runs/temoin-bailey-v1-20261111/manifeste-local-v6.json` (`5e62c0d8…`) |
| Conduite | `lancer-conduite-v13.py` (`db950a6d…`), relance seule : K′ = 8, règle de la série 3 (`2e8b7837…`), instance de la première 60417353, gardes tombées de la première : aucune ; sortie `/home/user/controle-ia-travail/runs/temoin-bailey-v1-20261111/sortie-conduite-v13`, disque 110 Go |
| Poste | `poste-hetzner-v12.sh` (`0990ff20…`), constructeur `construire-donnees-demarrage-v12.py` (`233793c7…`) ; l'empreinte imprimée par le constructeur doit être `0990ff20…` |
| Image | `runpod/pytorch:2.4.0-py3.11-cuda12.4.1-devel-ubuntu22.04` |
| `DEPOT_URL` | `https://github.com/lciric/controle-ia-travail.git` |
| Surveillance | réveils au plus toutes les 90 minutes : conduite (journal technique seulement), crédit, paiements, o ; alerte à Lazar sous 4 USD de crédit, `billing_failed` vrai, o + 0,5 USD/h, ou toute issue de la liste d'arrêt ; aucune note lue avant la fin de la relance et le scellement de ses journaux |
