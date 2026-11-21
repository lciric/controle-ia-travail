# Faits : un seuil de moniteur à 1 % de fausses alertes qui ne tient plus quand le régime change

## Le programme

Un programme de recherche défensif sur le contrôle des systèmes d'IA cherche à détecter un agent qui sabote discrètement des tâches de recherche. Il lit des sondes linéaires sur les états internes de l'agent, compare l'agent à un jumeau honnête qui reçoit la même tâche, et agrège plusieurs moniteurs. Chaque moniteur rend un score par épisode (ou par pas) ; un seuil est réglé pour viser 1 % de fausses alertes sur des épisodes honnêtes d'étalonnage, souvent peu nombreux (quelques centaines).

## Le défaut

Des travaux récents rapportent qu'un seuil réglé ainsi ne tient plus quand la distribution des scores honnêtes change : nouvelles tâches, nouvelle version de l'agent, autre longueur d'épisode, autre source de comportements bénins. Un de ces travaux (CURA, arXiv 2608.27808) rapporte un taux réel de fausses alertes qui triple sous un tel changement de régime. Le programme ne tient ce chiffre pour acquis qu'avec la page du PDF lue.

## Ce que le programme a déjà

- Un seuil unique sur un score normalisé, qui garantit 1 % en moyenne sur les longueurs, mais pas par tranche de longueur.
- Des formes séquentielles (surveillance au fil des pas) qu'il faut durcir contre les franchissements répétés.
- Un jumeau honnête, qui peut servir de référence courante, mais dont l'écart à l'agent honnête est lui-même fragile.
- Un étage de tests de mort : toute règle candidate est implémentée sous une interface fixe et éprouvée contre des mondes plantés dont la vérité est connue, dont une famille de dérive où un décalage des scores honnêtes triple le taux réel au seuil de 1 %. La vérité et le verdict restent hors de la machine qui exécute.

## Contraintes

- Peu d'épisodes honnêtes par régime ; épisodes de sabotage rares et jamais employés pour régler un seuil honnête.
- Aucune moyenne ou médiane sur les jetons dans une sonde de production.
- Budget de calcul modeste ; relecture humaine rare.
