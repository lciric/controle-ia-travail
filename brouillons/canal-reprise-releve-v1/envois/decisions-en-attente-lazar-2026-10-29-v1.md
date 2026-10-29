# Décisions en attente de Lazar — 29 octobre 2026 au soir — v1

Lignée conv-audit (servie par Opus 5.5), relevé `date -u` 22:23. Sur ton mot (23:21 heure de Paris) : « détaille les décisions à prendre, les
arguments et les recos ». Format du dépôt : décision ; enjeu ; options (avantage / inconvénient) ; recommandation et confiance ; défaut sous
48 heures. **Si tu suis toutes les recommandations, une ligne suffit : « défauts ».** Classées par urgence.

## I. Porte G0 — à trancher en un bloc avec la grille (scellement de la grille au plus tard le 15 novembre)

**G0-1. Préenregistrement absent au 30 novembre pour un critère 2, 3 ou 4 : « absent » (report ouvert) ou « négatif » (gel) ?** (choix 2 de la
synthèse du collisionneur.) Enjeu : aujourd'hui aucun organisme n'existe ; sous « négatif », le report naîtrait mort. (a) « absent » — le report
sert à ce pour quoi il existe ; inconvénient : un critère jamais préenregistré peut traîner jusqu'au 31 janvier. (b) « négatif » — discipline
maximale ; inconvénient : clôture quasi certaine dès le 30 novembre. **Reco (a), 0,7.** Défaut (a).

**G0-2. D-TD-2 — si la lecture du 31 janvier s'arrête sur la liste d'arrêt, sans verdict.** Enjeu : un arrêt ne doit pas devenir un second
report. (a) « Cesser » : tout s'arrête jusqu'à ton mot ; la même lecture reprend à la levée de la cause — rien ne continue, mais tout attend ta
réponse. (b) L'arrêt vaut « non franchie » — simple ; inconvénient : un incident technique (empreinte, lecteur non neuf) ferme la phase. **Reco
(a), 0,6.** Défaut (a).

**G0-3. Date de scellement de la table de dépendance.** Enjeu : sceller avant tout résultat des critères 2 à 4 (sinon taillage possible) mais
après que la clause est figée. (a) 1er novembre — très tôt ; risque de v5 si la grille bouge. (b) **15 novembre 23:59 UTC avec la grille** — même
date que la grille, avant tout résultat attendu. **Reco (b), 0,6** (condition : aucun résultat des critères 2 à 4 lu avant). Défaut (b).

**G0-4. Critère 6 (préenregistrement de G1) atteignable.** Enjeu : G1 attend le pilote de la couche 2 ; sans pilote avant le 30 novembre, la
table le fermerait pour toujours. (1) Le pilote hérite d'un droit de devis pendant le report, comme les critères manquants — garde la porte
atteignable ; une dépense possible de plus (toujours sur devis et GO). (2) Retirer le pilote des dépendances de G1 — assouplit une dépendance
que la grille pose. **Reco (1), 0,6.** Défaut (1).

**G0-5. D-G0-8 — verdict scellé par un sous-agent neuf pour chaque critère empirique avant la lecture de G0.** Enjeu : sans lui, le lecteur de
G0 refait de l'analyse, et la table ne sait pas lire le gel ni le déblocage. (a) Exiger (valeur copiée et classe) — le lecteur compte, il
n'analyse pas ; coût : un verdict de plus par critère. (b) Le lecteur de G0 applique les tables des sous-expériences — moins de pièces ; plus de
jugement. **Reco (a), 0,75.** Défaut (a).

**G0-6. Autres choix de la synthèse** : empreintes de référence tenues hors dépôt chez toi (reco oui, 0,7 : un dépôt peut être réécrit) ;
**plafond du report** fixé d'avance et séquencé (critère 2 puis 3-4), montant à chiffrer par session-depot (reco : fixer le montant avant le
30 novembre ; 250 USD était illustratif) ; pilote ρ pendant le report : oui, aveugle (reco 0,6).

## II. G1 — la garde δ sous dispersion combinée (ta question : « comment faire alors ? »)

Constat (R-506) : si la difficulté de chaque unité varie **pour le sujet et pour les comparateurs**, la fiche à K_s = 10 tombe à 0,83–0,89 à 288
unités. Quatre remèdes, chiffrés par la **v8 en cours** (processeur, sans dépense) :
- **R1 plus d'unités** — la règle n_h ≥ max(288 ; n80) le couvre déjà, à condition d'avoir **d'avance** la table « dispersion mesurée au pilote →
  taille » (la v8 la calcule) ; coût : des unités en plus, au devis de la banque.
- **R2 difficulté partagée** — si une unité difficile l'est pour tous (sujet et comparateurs), l'appariement l'annule en partie : c'est
  probablement le cas réel (mêmes tâches, mêmes épisodes) ; la v8 mesure combien, et le **pilote doit mesurer cette corrélation** (sans lire
  l'écart du sujet).
- **R3 strates d'unités** — bloquer par une difficulté connue d'avance (longueur de tâche, horizon) et calibrer par strate.
- **R4 plus d'exécutions par unité** — n'aide presque pas contre une dispersion **entre** unités (attendu ; la v8 le vérifie).
**Décision G1-1 (après la v8)** : écrire au préenregistrement la table de lecture « ρ et corrélation mesurés au pilote → n_h », et les mesures
correspondantes au pilote. **Reco : oui, 0,75** ; c'est le seul remède qui ne dépend pas d'une hypothèse sur la loi. Défaut : oui.

## III. Course 2 — question de défense (treize divergences ; défauts dans le texte servi)

Recommandation globale : **« défauts »** (confiance 0,65). Les quatre qui changent le plus la course :
- **D3 budget de l'expérience qui tue une fiche** : processeur ou données déjà payées (reco, 0,7 : aucune dépense implicite ; l'étage sur carte
  reste « fiche par fiche sur GO », ta décision R-776) / jusqu'à 300 USD.
- **D5 à l'axe 4, l'hypothèse qui cède est désignée d'avance** (reco, 0,8 : sinon l'explication vient après coup) / nommée après l'échec.
- **D1 l'axe 7 (angles non occupés) servi à une sous-session neuve** sans les autres axes (reco, 0,6 : moins d'ancrage sur nos axes) / même texte.
- **D11 grille des sous-domaines du contrôle** servie, au moins trois cases par proposeur (reco, 0,6) — **la grille est à arrêter par toi** (esquisse
  d'Opus, non vérifiée) ; défaut : telle quelle.
Les autres (D2 passe 2 = corrections seules ; D4 contrôles de l'axe 1 ; D6 familles hors programme facultatives ; D7 double garde contre la
reformulation ; D8 classement ; D9 directions de sonde exclues ; D10 petits écarts ; D12 boucle ; D13 critère de mort) : défauts du texte.

## IV. Bisociation à deux espaces

**B-1. Seuil d'adoption du test v2.** Enjeu : le premier test exigeait +12 points absolus, peut-être trop dur pour un effet réel de quelques
points. (a) **+5 points et rapport ≥ 1,25** sur le stratifié (reco d'Opus neuf, 0,6) — adopte un gain modeste mais net ; (b) garder +12 —
cohérent avec le premier test ; risque de rejeter une forme utile. **Reco (a), 0,6.** Défaut : (a), gelé au préenregistrement.

## V. Organisme hybride et IA scientifique externe

**H-1. Quel cadre externe ?** Divergence : session-depot recommande The AI Scientist v2 ; ma note l'exclut (carte exigée, Claude par Bedrock
seulement, licence restrictive) et recommande Agentic Scientist v3 (Apache-2.0). Les deux reposent sur des pages non vérifiées. (a) Vérifier les
deux sur pièces primaires (licence, matériel, modèles, exécution) avant tout choix — un jour de retard, zéro risque de licence ; (b) suivre
session-depot tout de suite. **Reco (a), 0,7.** Défaut (a).
**H-2. Ordre** : couche 3 légère (l'étage de tests de mort, v48) d'abord, hybride en parallèle ; comparaison préenregistrée sur trois courses au
moins (≈ 90 à 210 USD, SUPPOSÉ). **Reco : oui, 0,6.** Défaut : préparation seulement, aucun code tiers installé avant revue.

## VI. Revue de sécurité extérieure (relecteur d'accord, R-485)

**S-1. Exception de lecture** : le relecteur est le seul, hors du lecteur tenu à l'écart, à lire les modes avant l'examen. Reco : l'écrire comme
nœud consigné, oui (0,8) — sans cela la revue est vide. **S-2. Qui avance les 7 500 USD** si la première revue précède le financement (1er
décembre) ? À toi : pas de reco (question de trésorerie). **S-3. Envoi de la lettre** : après contre-lecture du cahier (je la lance).

## VII. Dépenses à valider (chiffrées par session-depot avant GO)

- Épreuve réelle courte du tour (c) : 5 USD (GO de principe donné, R-457).
- Moissonneur : 0 USD de source ; ≈ 0,4 USD de jetons par course ; sous moisson, totaux de course 41 / + 0,5 USD.
- Étage de tests de mort (v48) : ≈ 3 USD pour cinq fiches (SUPPOSÉ).
- Collisionneur + Argon sur la bisociation : à chiffrer (≈ 20 à 30 USD au vu des tours précédents).
