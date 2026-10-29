# Avis de conv-audit — règle de repli si la porte G0 n'est pas franchie fin novembre 2026 — v1

Lignée conv-audit (instance de reprise, Fable 5.1), 29 octobre 2026, relevé `date -u` 09:38 UTC. Sur le mot direct de Lazar (≈ 09:31 UTC, session
de session-depot, relayé n° 176) : « Pour la porte : les critères ne bougeront pas, mais aucune règle de repli n'est écrite : il en faut une ;
lance le collisionneur et agent neuf Fable + conv dessus ». Cet avis est écrit **avant** de voir la synthèse du collisionneur (GO-07) et l'avis du
Fable neuf ; il est matériau pour Lazar, ne tranche rien. Pièces : critères de G0 (programme v2, l. 180 : harnais validé ; organismes avec
dose-réponse ; sondes au-dessus du plancher ; base boîte noire opérationnelle ; agrégateurs validés en simulation ; préenregistrements de G1 et
du papier C scellés et contre-lus ; état de l'art vérifié), N-027 (porte au plus tard fin novembre, critères inchangés), état au 29 octobre
(prouvés : 1 et 5 ; ouverts : 2, 3, 4, 6, 7, 8), R13 (verdict de porte par un sous-agent neuf, scellé, GO de Lazar).

## 1. Ce qu'une règle de repli doit être, et ne pas être

Une règle de repli est **une clause scellée avant le verdict**, qui dit ce qui se passe **mécaniquement** si le verdict R13 de G0 n'est pas
« franchie », **sans qu'aucune décision soit laissée à qui lit les résultats**. Elle ne touche aucun critère (N-027), ne crée pas de « G0 bis »
plus facile, et ne transforme pas un échec en succès par renommage. Ce qu'elle doit fixer : (i) le **déclencheur** et **qui prononce** ;
(ii) **l'action unique** qui suit, avec sa **borne** (temps, dépense) ; (iii) ce qui est **permis** et **interdit** pendant le repli ; (iv) ce qui
arrive **à la fin de la borne** si rien n'a changé.

## 2. Déclencheur et prononcé

- **Déclencheur** : le verdict R13 de G0, prononcé par un sous-agent neuf sur les critères gelés, au plus tard le **30 novembre 2026 à
  23:59 UTC**, rend autre chose que « franchie » — soit « non franchie » (au moins un critère établi comme non tenu), soit « non concluante »
  (au moins un critère sans verdict possible : préenregistrement non scellé, expérience non jouée, état de l'art non vérifié). **Les deux
  déclenchent la même clause** ; la distinction est consignée au verdict, elle ne change pas le repli (sinon la lecture du résultat choisit
  le repli).
- **Qui prononce** : le sous-agent de verdict (R13) ; Lazar donne le GO du verdict, pas du repli : **le repli s'applique seul**, par la clause.

## 3. Options de clause

| option | clause | avantage | inconvénient |
|---|---|---|---|
| (a) **Report borné, une fois** | G0 reportée **une seule fois**, au plus tard au **31 décembre 2026** ; critères inchangés ; pendant le report, seules les tâches des critères non tenus peuvent dépenser, sur devis ; à la fin, verdict R13 ; si encore non franchie → clause (d) s'applique automatiquement | simple ; garde la porte entière ; borne claire | si la cause est structurelle (un critère hors d'atteinte), un mois ne la lève pas ; risque de « report du report » si la clause n'est pas verrouillée |
| (b) **Travail continu sans phase 1** | la phase 0 continue sans date ; aucune expérience décisive de G1 ni du papier C ne se lance tant que G0 n'est pas franchie | aucun artefact de calendrier | pas de borne : c'est l'absence de règle sous un autre nom ; incompatible avec un financeur |
| (c) **Bascule vers ce qui ne dépend pas des critères manquants** | les critères tenus (1, 5 ; et ceux tenus à la date) ouvrent **seulement** les travaux qui ne dépendent d'aucun critère manquant (par exemple : simulations, état de l'art, papier C partie théorique) ; tout ce qui dépend d'un critère manquant reste fermé ; borne au 31 décembre, puis (d) | ne gaspille pas le temps ; honnête sur ce qui est prêt | demande une **table de dépendance** critères → travaux, à sceller maintenant ; tentation de reclasser un travail comme « indépendant » après lecture — d'où la table scellée d'avance |
| (d) **Arrêt et rapport** | la phase 0 est close « non franchie » ; un **rapport de porte** scellé (ce qui est tenu, ce qui manque, pourquoi, coût) ; aucune expérience décisive ; reprise seulement par une **nouvelle version du programme** (nœud, mot de Lazar, nouveau calendrier) | la plus propre ; aucune porte de sortie | perd l'élan ; pour le financeur, un « arrêt » le 30 novembre, à un mois du début financé, est le pire signal s'il n'est pas accompagné de (c) |

## 4. Clause recommandée (une seule, avec borne)

**(c) + (a) verrouillée, puis (d)** — confiance **0,6** :

> « Si le verdict R13 de G0, prononcé au plus tard le 30 novembre 2026 à 23:59 UTC, n'est pas « franchie », la porte est **reportée une seule
> fois au 31 décembre 2026 à 23:59 UTC**, critères inchangés. Pendant le report : (1) seules les tâches des critères déclarés non tenus ou non
> concluants au verdict peuvent dépenser, chacune sur devis et GO ; (2) les travaux listés dans la **table de dépendance scellée** comme
> indépendants des critères manquants continuent ; (3) **aucune expérience décisive de G1 ni du papier C** n'est lancée, aucun
> préenregistrement de G1 n'est exécuté. Au 31 décembre, un second verdict R13 ; s'il n'est pas « franchie », **la phase 0 est close « non
> franchie »**, un rapport de porte scellé est rendu, et toute reprise exige une nouvelle version du programme (nœud). Aucun second report. »

Pourquoi : (a) seule laisse le report se répéter ; (d) seule jette un mois utile ; (c) seule n'a pas de fin. La combinaison a une borne dure
(un report, puis clôture), ne touche aucun critère, et laisse travailler ce qui est prêt. **Confiance 0,6** parce que la borne du 31 décembre
est un choix de calendrier (un mois), pas une mesure : si les critères 2 à 4 demandent des campagnes de plusieurs semaines chacune, un mois
peut être trop court — c'est à Lazar de dire si la borne est le 31 décembre ou le 31 janvier ; la forme de la clause ne change pas.

## 5. Ce qui doit être décidé maintenant (avant tout verdict)

1. La clause (forme et borne) — scellée dans `docs/decisions/` avec N-027 ; **aucune modification après le 1er novembre**.
2. La **table de dépendance** critères → travaux (ce qui continue sous repli), scellée avant le verdict, par une main qui n'a pas vu les
   résultats des critères ouverts (un sous-agent neuf sur la seule liste des tâches).
3. Qui rend le **rapport de porte** en cas de clôture (sous-agent neuf, R13), et son gabarit.
4. Le mot de Lazar sur la **borne** (31 décembre ou 31 janvier).

## 6. Phrase pour le financeur (anglais, courte)

« Gate G0 has fixed, pre-registered criteria and a fixed deadline (30 November 2026). If it is not passed, a sealed fallback clause applies
automatically: one bounded extension (to 31 December 2026, criteria unchanged, no decisive experiment started), after which the phase is
closed with a sealed gate report and can only be reopened by a new program version. No criterion is relaxed and no decision is left to
whoever reads the results. »

## 7. Réserves

- Écrit avant la synthèse du collisionneur et l'avis du Fable neuf ; divergences possibles sur la borne et sur (c).
- Le coût du report (devis des critères 2 à 4) n'est pas chiffré ici ; il entre dans la décision de la borne.
- Non contre-lu (R2).
