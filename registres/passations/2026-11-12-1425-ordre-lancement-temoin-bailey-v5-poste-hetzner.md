# Ordre de lancement v5 — témoin de l'attaque publiée de Bailey, piloté par un poste Hetzner — 12 novembre 2026, 14:25 UTC

Session `session_01XJ6MgnEhQMZteN9F8a1BST`, branche `claude/compassionate-meitner-d4ryyk`. Écrit **avant la création**
du poste et de l'instance (condition 8). Ne se réécrit pas (R12).

## Mots de Lazar
- « go c » (≈ 12:20 UTC) : poste de pilotage loué (Hetzner) ; plafond proposé 5 USD jusqu'au 30 novembre, silence valant
  accord (note `2026-11-12-1250-…`) ; **ligne de GO à inscrire sur `main` par la mère**.
- « clé de déploiement ajoutée, lance le témoin de Bailey » (≈ 14:22 UTC).

## Ordre
| Champ | Valeur |
|---|---|
| GO du run | `GO_ID=GO-2026-11-10-10` (amendé `GO-2026-11-11-01`, modèle `GO-2026-11-11-02`) ; la conduite relit `origin/main` |
| B | 75 USD (fixé à la création de 60280913) ; D antérieure ≈ 1,537 USD (trois instances détruites) |
| Poste | Hetzner `cx23`, Falkenstein, Debian 12, nom `poste-temoin-bailey-v1` ; ≈ 0,011 EUR/h ; « go c » de Lazar |
| Script du poste | `runs/temoin-bailey-v1-20261111/poste-hetzner-v1.sh` (`c6a96f30…`) ; données de démarrage assemblées par `construire-donnees-demarrage-v1.py` (`0e407d42…`), hors du dépôt |
| Conduite | `runs/temoin-bailey-v1-20261111/lancer-conduite-v5.py` (`aaf3889c…`), sortie `/home/user/controle-ia-travail/runs/temoin-bailey-v1-20261111/sortie-conduite-v5` sur le poste |
| Offre | choisie par le poste au démarrage, la moins chère du filtre de l'ordre v4, écrite dans `offre-choisie-v5.json` avant la création ; relevé de la session à 14:23Z : une seule offre conforme, 57426822 (Oregon), ≈ 1,50 USD/h avec 200 Go |
| Image | `runpod/pytorch:2.4.0-py3.11-cuda12.4.1-devel-ubuntu22.04` |
| `DEPOT_URL` | `https://github.com/lciric/controle-ia-travail.git` |
| Commit du code | `4988f3f442c670887a0e8ad15ddfbac68a173d03` |
| Accès | clé de déploiement ajoutée par Lazar (`SHA256:VW9jZJAwK2LruuNz9eGdJkp4uyhbjyfz3anq8gLitF4`) ; clé `ssh` Vast 1864483 ; clés Vast et Hugging Face déposées dans les données de démarrage (stockées chez Hetzner) |
| Surveillance | `git fetch` de la branche (journaux poussés par le poste toutes les 10 minutes), API Hetzner, `vastai show instances` ; aucune note de sonde ni de juge lue avant la fin du run principal et le scellement |
| Fin | la session détruit le poste par l'API Hetzner après `poste-fini-v1.json`, retire la clé de déploiement (par Lazar) et la clé Vast 1864483 |

Serveur Hetzner présent avant création : `organisme-v67-course` (175834755), hors de ce poste, non touché.
