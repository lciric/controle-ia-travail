# Complément au registre des affirmations — Kirchner Q2, réponse v2 — conv-audit, 14:21 UTC (`date -u`)

Révision v1 → v2 par le directeur, sur les seuls points de `verification-chiffres-v1.md` (`bf2804ee…`) et `lecture-mentor-v1.md` (`1acc61ce…`). Le registre du rédacteur (`f45553dc…`) vaut pour tout le reste.

| Changement | Source | Force |
|---|---|---|
| « Ville's always-valid alarm rule » (le papier ne nomme jamais Ville) | page T0.3 au commit `faff48b` (`resultats/controle-simulation-defenses`) | publique et vérifiée |
| « from the same law » (le calibrage ne vaut que si calibrage et emploi suivent la même loi) | même page, lignes 30 et 82 (robustesse à un décalage non testée) | publique et vérifiée |
| « at the largest shifts » (au lieu de « strongest settings ») | même page : les trois plus forts effets d'épisode de la grille | publique et vérifiée |
| « (same held-out tie-break) » (le gagnant est choisi parmi les trois premiers par le banc tenu à l'écart) | 2608.28945 v3, §2.3 p. 4 ; C.2 p. 31 (lecteur-mentor) | publique et vérifiée |
| « 800 times each » (au lieu de 400) | calcul : intervalles à 95 % de la figure 19 (100 audits par méthode, p. 38) : 0,61 et 0,64 → écart-type par audit ≈ 3.11 et 3.27 ; demi-largeur à 95 % d'un écart entre deux méthodes : 0.44 à 400 audits chacune (trop près du seuil de 0,5), 0.31 à 800 | calcul |
| « (95% interval about ±0.3; …) » | même calcul | calcul |
| « give each method 100 Petri audits » (au lieu de « give it ») : 4 000 = 2 échecs × 20 méthodes × 100 | vérificateur, n° des calculs du plan | calcul |
| Citation de §5.1 raccourcie à « biased upwards by taking a maximum over noisy evaluations », le reste paraphrasé | 2608.28945 v3, §5.1 p. 7 | publique et vérifiée |
| Retiré : « crowned within each climb's first half » (pari temporel sans résultat contraire annoncé ; lecteur-mentor) | — | — |

Compte : 446 mots (découpage sur les blancs). Règle R-1395 : cette version ne vaut que si le groupe gagnant de l'ensemble tour plus course contient KM-13.
