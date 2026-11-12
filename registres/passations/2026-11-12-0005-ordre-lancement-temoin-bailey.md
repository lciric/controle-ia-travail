# Ordre de lancement — témoin de l'attaque publiée de Bailey — 12 novembre 2026, vers 00:05 UTC

Session « attaquant informé » `session_01XJ6MgnEhQMZteN9F8a1BST` (autre compte), branche `claude/compassionate-meitner-d4ryyk`.
Écrit **avant la création de l'instance** (procédure `2026-11-11-1624-…`, étape 5 ; condition de lancement 8). Ne se
réécrit pas (R12).

## Mots de Lazar reçus dans cette session
- Clé `ssh` : « Ou tu me dis en clair de l'ajouter moi-même. […] go » (≈ 23:54 UTC le 11 novembre). Clé de session
  ajoutée au compte Vast : identifiant **1864483**, empreinte `SHA256:ewBln+4RHDnCKVZSPnkke4U1FVBDauXtbfifZi6z8TA`, à
  retirer après la destruction de l'instance. Suite du refus consigné dans `2026-11-11-2350-…` (`77e3f20c…`) : levé par
  le mot direct de Lazar, sans reformulation.
- Offre : l'offre `49739788` (≈ 1,15 USD/h) ayant été louée entre-temps, question posée (≈ 1,64 USD/h en Oregon : régime
  publié atteignable seulement si un tour dure 25 minutes ou moins). Réponse de Lazar : **« Lancer maintenant Oregon »**.

## Ordre
| Champ | Valeur |
|---|---|
| GO | `GO_ID=GO-2026-11-10-10` (amendé par `GO-2026-11-11-01`, modèle `GO-2026-11-11-02`), lus sur `origin/main` `ee4eed985f75b211f031594ea725dcc37e2c3b90` (2026-11-11T23:55:04Z) ; la conduite les relit elle-même |
| B | **75 USD**, fixé à la création de la première instance du poste ; arrêt à B − 2 |
| Échéance du GO | 2026-11-30 (fin du jour à Paris) ; vérifiée par la conduite contre création + (B − 0,5)/c h + 1 h |
| Offre | **57426822**, A100 SXM4 80 Go, Oregon (États-Unis), 258 Go de mémoire allouée, fiabilité 0,992, vérifiée, CUDA 13.0 |
| Taux relevé (recherche, 23:57 UTC) | 1,370 USD/h hors stockage ; stockage 1,0 USD par Go et par mois, soit ≈ 1,644 USD/h pour 200 Go ; **c réel relevé par la conduite après la création** (`dph_total`) |
| Image | `runpod/pytorch:2.4.0-py3.11-cuda12.4.1-devel-ubuntu22.04` (configuration `sha256:ff5fe688…`), choix motivé dans `2026-11-11-2350-…` |
| Disque | 200 Go |
| `DEPOT_URL` | `https://github.com/lciric/controle-ia-travail.git` |
| Commit du code | `4988f3f442c670887a0e8ad15ddfbac68a173d03` |
| Manifeste | `runs/temoin-bailey-v1-20261111/manifeste-local-v3.json` (`69143b99…`) |
| Script | `runs/temoin-bailey-v1-20261111/lancer-conduite-v1.py` (`a970abc0…`) |
| Sortie | `/home/user/controle-ia-travail/runs/temoin-bailey-v1-20261111/sortie-conduite-v1` (même chemin absolu pour `reprendre`) |
| Étiquette | tirée par la conduite (`temoin-bailey-c6-` + 16 hexadécimaux), écrite dans `conduite-v5.jsonl` |
| Instances antérieures du poste | aucune |
| Addendum 2 du témoin | déposé chez le tiers le **2026-11-11T23:13:50Z**, avant ce lancement |

## Après le lancement
PID du script consigné à la prochaine note. Aucune note de sonde ni de juge lue avant la fin du run principal et le
scellement de ses journaux ; verdict par un lecteur neuf (R13).
