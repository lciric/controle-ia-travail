# Ordre de lancement — témoin de Bailey, troisième série (addendum 4), poste Hetzner v11 — 12 novembre 2026, 23:12 UTC

Session `session_01XJ6MgnEhQMZteN9F8a1BST`, branche `claude/compassionate-meitner-d4ryyk`. Écrit **avant la création**
du poste et de l'instance (condition 8). Ne se réécrit pas (R12).

| Champ | Valeur |
|---|---|
| Addendum | `prereg/temoin-attaque-publiee-bailey-v1-addendum-4-code-v17-execution-v4-troisieme-serie.md` (`89d2f647…`), scellé au commit `6330000a` (2026-11-12T23:07:13Z), présent sur la tête poussée de la branche (vérifié par `git ls-remote`) ; **pas encore déposé chez le tiers** (ni l'addendum 3) : daté par son commit |
| Contre-lectures | addendum : `2db77cc7…` (brouillon 2) et différentielle `cb2eb8e5…` (version à sceller) ; code : `833429c6…` |
| Mot de lancement | « go (a), garde le poste » (22:10Z) et « avance en autonomie pendant 10h » (≈ 22:14Z), tenus ensemble pour le mot direct : **lecture de la session**, déclarée (addendum 4, § 6, condition 7 ; note `4f127118…`), rapportée à Lazar dès ce scellement ; **ne vaut que pour une création d'instance avant le 13 novembre 2026, 08:14Z** |
| Borne horaire | le poste attend une offre jusqu'à 24 h ; la session détruit le poste par son identifiant (R10) s'il n'a créé aucune instance à 08:05Z le 13 novembre (rappel programmé) ; une offre prise avant 08:14Z reste dans la borne |
| GO | `GO_ID=GO-2026-11-10-10` (amendé `GO-2026-11-11-01`, modèle `GO-2026-11-11-02`) ; présent sur `origin/main` (relu à 23:10Z), non révoqué ; la conduite le relit |
| B, D | B = 75 USD ; D antérieure = 2,778 USD (six instances détruites) |
| Code | commit `8d1c541ef7a3ac99f942e0b2f26567088f2cc503` (`lanceur_v17`, `instance_v16`, `execution_v4`) ; `src/` de la tête identique (vérifié à 23:07Z) ; garde du poste v11 |
| Manifeste | `runs/temoin-bailey-v1-20261111/manifeste-local-v5.json` (`111c6e98…`) |
| Conduite | `lancer-conduite-v11.py` (`d279ea19…`), sortie `/home/user/controle-ia-travail/runs/temoin-bailey-v1-20261111/sortie-conduite-v11`, disque 110 Go |
| Poste | `poste-hetzner-v11.sh` (`059d0837…`), constructeur `construire-donnees-demarrage-v11.py` (`2e9df5ba…`) ; l'empreinte imprimée par le constructeur doit être `059d0837…` ; offre choisie par le poste (filtre 128,9 Go, disque 115 Go) ; relevé à 22:50Z : aucune offre conforme |
| Image | `runpod/pytorch:2.4.0-py3.11-cuda12.4.1-devel-ubuntu22.04` |
| `DEPOT_URL` | `https://github.com/lciric/controle-ia-travail.git` |
| Poste v9 | 175884265 en marche, sans tâche, gardé (consigne de Lazar) |
| Surveillance | réveils au plus toutes les 60 minutes ; alertes de l'addendum 3, § 7.2 (30 min si visible, sinon 4 h après le lancement du pilote) et à toute issue de la liste d'arrêt ; aucune note lue avant la fin du run principal et le scellement |
