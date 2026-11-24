# Erratum 1 de la réponse à la question 1 : les quatre étapes de procédure lues comme oracles de l'organisme (v1)

- **Nature** : pièce de travail (classe C), erratum ; la pièce visée n'est pas modifiée. Les errata mineurs déjà versés (`errata-mineurs-q1-q2-q7-v1.md`, `fcac74f5…`, section « Question 1 ») restent en vigueur.
- **Heure** : `2026-11-24T18:00:18Z` (`date -u`).
- **Auteur** : Claude Opus 5.5, effort élevé, sous-agent de la session fille `session_016QhUrtAyz3dFV4u1BbUBoS`.
- **Pièce visée** : `reponse-q1-quatre-etapes-oracles-organisme-v1.md` (`2cc296327b889056b629ad3bc737ff489e409d39a3c6b0278f4d5686537aad5e`).
- **Source des constats** : `contre-lecture-questions-directeur-opus-max-v1.md` (`31eb1c07fe83084df51e840ebeaf867905503d6304c1853440341550019f5eed`), section 3.1, constats Q1-M1, Q1-M2 et Q1-m1. Chaque constat a été revérifié sur la pièce et sur les décisions citées avant d'être accepté.

## Majeur 1 (Q1-M1, accepté) : la borne de la répétition générale ne couvre pas la chaîne réelle

**Texte fautif** (section 2, « Borne de la répétition générale ») : « Le « 0 sur 1 000 » rapporté pour le nul (N-067, section 2) borne donc le taux à 0,30 %, non à zéro ; la répétition générale étend cette borne du juge seul à la chaîne entière. »

**Vérification.** Le calcul `1 − 0,05^(1/n)` est juste (0,99 %, 0,30 %, 0,10 % pour n = 300, 1 000, 3 000). Mais la borne est celle d'un taux sous la loi des objets joués : `decision-N-067-v1.md` (l. 44) dit « 0 sur 1 000 sur chaque ligne fatale », pour un banc de 27 tricheurs scriptés. La répétition générale joue des proposeurs scriptés sur des mondes à issue connue. Un proposeur adaptatif, ou une composition choisie sur ce banc, suit une loi que la répétition n'a pas jouée : c'est l'analyse adaptative que la pièce cite elle-même (Dwork et collègues ; Blum et Hardt). La phrase laisse lire une garantie sur la chaîne en usage ; elle ne vaut que pour la chaîne entière sous les objets joués.

**Correction.** Lire : « La répétition générale étend cette borne du juge seul à la chaîne entière, **pour la loi des objets joués** (proposeurs scriptés, tricheurs connus), ligne par ligne. Elle ne borne rien pour un proposeur adaptatif ni pour une stratégie non jouée : la chaîne en usage exige en plus une épreuve adversative (attaquant informé) et des mondes renouvelés. »

## Majeur 2 (Q1-M2, accepté sous la condition dite) : l'ordre d'épreuve fixé par un lecteur entre dans la sélection

**Texte fautif** (section 3, tableau, ligne « Accord entre lecteurs, second classement… ») : « Le second classement peut orienter l'ordre d'épreuve des fiches, jamais compter comme preuve ni toucher au choix d'une composition. »

**Vérification.** `decision-N-058-v1.md` (point 1) juge toute composition des proposeurs sur l'oracle du monde planté (structures retrouvées, témoins promus ou rejetés) et le coût, seuls ; `decision-N-053-v1.md` (point 5) interdit qu'un score de moniteur ou de juge entre dans un signal de sélection d'un agent. Quand l'oracle est un programme qui éprouve toutes les fiches, l'ordre est sans effet. Mais la colonne A de la pièce (lecture de couverture par des lecteurs) est « sur devis » : son budget est fini, et alors l'ordre décide quelles fiches sont éprouvées, donc les décomptes qui jugent les compositions. Le classement d'un lecteur entrerait dans la sélection par l'ordre. Le constat tient dès que le budget d'oracle contraint, ce qui est le cas prévu.

**Correction.** Lire : « L'ordre d'épreuve des fiches qui alimentent le choix d'une composition est fixé par une règle indépendante de tout lecteur (tirage au sort scellé, ou épreuve exhaustive). Le second classement n'ordonne que des fiches hors du décompte des compositions, et il est rapporté comme mesure. » Si une session veut un ordre guidé par un lecteur dans le décompte, c'est un nœud pour Lazar (lettre de N-053, point 5).

## Mineur (Q1-m1, accepté) : le cas sain de la courbe de capacité

**Texte fautif** (tableau, colonne C, ligne « Cas sain ») : « Proposeur scripté qui connaît la graine : toute dose non nulle est retrouvée, donc le monde est soluble ; la courbe croît avec la dose. » Un proposeur qui tient la graine donne une marche (1 à toute dose non nulle), non une courbe croissante.

**Correction.** Deux cas sains distincts : (a) l'oracle à graine, qui éprouve la solubilité (marche à 1) ; (b) un détecteur de référence de puissance connue, par exemple le test statistique optimal du monde, dont la courbe théorique doit être retrouvée.

## Apport noté, sans changement de la pièce

La contre-lecture propose de prendre comme axe de dose la **rareté au hasard** r du puits planté ; la référence du hasard devient exacte, `1 − (1 − r)^B` pour B candidats tirés avec remise. Proposition utile pour le plan Turing ; elle relève d'une conception future, non d'un erratum.

## Conséquence sur le verdict

Le verdict de la pièce, « tient », est maintenu, avec deux réserves de portée : la borne de la répétition générale ne vaut que pour les objets joués ; l'ordre d'épreuve des fiches qui comptent pour les compositions ne vient d'aucun lecteur. La recommandation (b) du nœud posé (extraction entièrement programmatique) est renforcée : elle supprime aussi le canal de l'ordre.
