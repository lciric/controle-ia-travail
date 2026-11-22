# Vérification finale : commande v6 — v1

Même contre-lecteur Opus. Rapport recopié tel quel.

Verdict : Conforme.

Mes deux réserves sont corrigées, et le diff v5→v6 ne montre aucun autre changement.

- **Reprise (ligne 22) :** les serveurs Hetzner sont listés avant toute reprise. Si un serveur de l'essai 3 existe, aucune reprise : il est relevé, et on attend le mot de la mère pour le détruire ou le garder.
- **Repli (section « Repli ») :** il est jouable tel quel seulement si le poste de Lazar a la même arborescence et le même `.venv` (chemins écrits en dur dans le fabricant, lignes 37 et 109). Sinon, il faut une version propre au poste, contre-lue avant usage.
- **Reste du diff :** l'en-tête et la section « Différence avec la v5 », tous deux déclarés. Les trois commandes, leurs arguments et leurs options sont inchangés.
- **Empreintes :** v6 `45770257…` et le recopiage de mon rapport sur la v5 `ad6ef4e2…` concordent avec leurs compagnons.

À noter, sans bloquer l'envoi : sur un poste macOS, le repli échouerait aussi, parce que le fabricant appelle les formes GNU de `stat -c` et de `date -d`.
