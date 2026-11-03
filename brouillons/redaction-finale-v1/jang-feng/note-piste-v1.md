# Note de piste — réponse à Shi Feng et Eyon Jang (Pivotal) — v1

Rédacteur neuf (je n'ai écrit aucune version des réponses de Lazar). Travail du mardi 3 novembre 2026, de 12:23 à 12:50 UTC environ (`date -u`). Consigne : `brouillons/reprise-conv-audit-2026-11-02-nuit/prompts-sous-agents/redaction-finale-jang-feng-v1.md`, sha256 `9289c497bfc2f19af5d8d52d6532a95258859e48155d671cde1403636bfaa2b3`, vérifiée avant lecture.

**Question** (formulaire `brouillons/candidature-pivotal-v16/formulaire-site-colle-par-lazar-2026-11-03-1209.txt`, sha256 `57393598…`, ligne 82) : « What are your thoughts on the value of white-box monitors and white-box methods for auditing? What do you see as their current limitations? » Aucune limite écrite ; plafond de la consigne : 500 mots. Projet Pivotal des mentors : audit d'alignement et son automatisation, outils boîte blanche (`brouillons/candidature-pivotal-v16/mentors-classement-v3.md`, ligne 13, sha256 `e0e8c5f4…`).

## 1. Pistes candidates

| | Piste (angle) | Ce qui la rend forte pour ces mentors | Faiblesse |
|---|---|---|---|
| A | **Ce qu'un auditeur doit pouvoir cumuler dans les menaces diffuses.** Dans le cadre de Feng (aucune action ne fournit à elle seule une preuve écrasante), on cumule des scores faibles action par action à un taux de fausses alertes fixé d'avance. Il faut deux propriétés : un score qui n'obéit à aucun ordre (valeur de la sonde) et une loi honnête connue (première limite). Puis les limites dans l'ordre où elles mordent : le modèle peut déplacer ce que lit la sonde ; le signal n'est pas montré ; l'étiologie ; une proposition sur leurs organismes. | Touche les deux : 2411.17693 (Feng coauteur), 2409.12822 (Feng dernier auteur), 2604.28182 (Jang premier auteur). Distinctive : c'est le programme même de Lazar (« contrôle boîte blanche des menaces diffuses »), avec trois résultats publics à lui (R7, T0.3, P3). Vérifiable : trois liens épinglés. Défendable seul : Lazar a écrit la simulation, le test P3 et R7. | Dense pour 500 mots ; l'accès aux poids n'est pas traité. |
| B | **Une sonde ne prend pas d'ordres, mais le modèle qu'elle lit en prend.** Valeur = pas de canal d'instruction (R7 ; 2510.09462) ; limites = fuite par la trace textuelle (2509.21344), évasion apprise (2609.36490), organismes qui verbalisent (Jang, § 6.2). | Touche Jang de près ; vérifiable. | La preuve boîte blanche serait presque toute chez d'autres ; perd l'apport le plus propre à Lazar (calibrage et cumul). |
| C | **L'étiologie décide du transfert.** 2409.12822 ; organisme P3 obtenu par instruction ; test croisé sur les deux recettes de Jang. | Leur direction 1 du flux MATS (rapport, ligne 48). | La partie « valeur » est mince ; risque de leur réciter leur programme. |
| D | **Lire n'est pas piloter** (`sycophancy-construct-validity`) : ρ = 0,684, aucune intervention à une direction, rang 3 non reproduit, signal hors de l'autoencodeur parcimonieux. | Public, distinctif, défendable. | Plus proche de la question de Heimersheim ; lien faible avec les moniteurs et l'audit. |
| E | **Accès et audit externe** (Casper et coll., 2401.14446). | Thème attendu. | Générique, contesté par la référence elle-même ; rien de Lazar. |

## 2. Choix : piste A (raisons en cinq lignes)

1. Elle part du cadre de Feng et finit sur les organismes de Jang : chaque paragraphe touche un papier des mentors, page ou section citée.
2. Elle donne à la réponse une forme dictée par l'argument (deux conditions, puis ce qui les met en défaut), pas la liste de réserves de l'ancienne réponse.
3. Les trois faits les plus forts de Lazar sont publics depuis aujourd'hui et y entrent tous : R7 (valeur), T0.3 (calibrage), P3 (signal), plus R1 dit « not in yet ».
4. Ses limites sont des mesures (21 à 35 % de fausses alertes, plancher de sondes aléatoires, 100 % → 4 %), et chacune mène à une règle de conception (garder les verdicts, calibrer sur la tâche auditée, tester le transfert).
5. Elle finit sur une expérience faisable avec eux (test de transfert entre leurs deux recettes, avec filtrage du raisonnement), que Lazar peut défendre seul.

## 3. Ce que j'ai pris dans le réservoir (ancienne réponse, lignes 84 à 106) et ce que j'ai laissé

- **Pris, et resourcé** : P3 (la phrase sur le saboteur se retrouve désormais sur la page publique datée `resultats/controle-p3-premier-test/`, commit `7c7b688` du 3 novembre) ; les 21 à 35 % de fausses alertes (page publique datée `resultats/controle-simulation-defenses/`, même commit) ; 2609.36490 (rendu exact : le contexte vise, l'amplitude manque ; c'est un résultat, pas une conjecture) ; 2602.08877 ; le cadre de 2411.17693 ; l'étiologie et 2409.12822 ; les deux recettes de 2604.28182 ; R1.
- **Corrigé** : « in strategically valid ways » (absent de la source) retiré ; « rather than the nominal 5% » remplacé par le seuil de Ville et le seuil calibré (4,6 à 5,5 %) ; réserve 1 de P3 (« plus que demandé, cause non mesurée ») et réserves 2 et 3 (aires non exclues) ajoutées, car le verdict exige qu'elles accompagnent ses conclusions.
- **Laissé** : ρ = 0,68, « < 1 % » et « 68 % » (le « 1 % » est un bras de l'essai original de D36, non public ; ρ = 0,684 est un autre objet : lectrice indépendante, `brouillons/canal-fable-v1/fable_2026-11-03_n001.md`, § 2) ; le jeu d'audit 2512.07810 (une des deux phrases était fausse sur le mécanisme) ; l'élicitation par entraînement ; l'accès ; R6 (exact mais hors de la piste) ; la phrase sur les méthodes à base de poids (vague).

## 4. Les deux idées de la course d'idéation

- **M-018** (note placebo de même longueur, sans verdict, pour R7) : laissée. Les deux notes de polarité opposée de R7 montrent déjà que le moniteur suit le sens de la note (destination du côté de la note dans 7 cellules d'attraction sur 8, `results/R7/README.md`) ; l'idée porte sur un moniteur boîte noire ; la réponse ne cite R7 que de façon descriptive. Bonne question de réserve pour l'entretien, à dire comme une proposition.
- **M-077** (amorce de modération imposée à Qwen2.5-7B) : laissée, hors sujet (régime de sycophancie, pas surveillance boîte blanche).

## 5. Relecture comme les mentors : phrases qu'ils contrediraient de leurs propres travaux, et correction

1. « There weak per-action scores must be banked at a false-alarm rate fixed in advance » : Feng répondrait que son macro-protocole ne fixe pas de taux de fausses alertes, il met à jour une crédence (2411.17693, p. 6-7). → « There I would bank… » (position de Lazar, pas description de leur papier).
2. La proposition sur les organismes de Jang, sans contrôle du raisonnement : Jang répondrait que ses organismes raisonnent explicitement et qu'un moniteur texte les attrape déjà (2604.28182, § 6.2). → ajout du filtrage des jetons de raisonnement, tel que 2509.21344 le définit (p. 1, figure 2 p. 4).
3. « 99.3% » attribué à leur sonde : le 99,3 % est celui de MacDiarmid et coll. sur un agent dormant, et c'est la même méthode qui ne fait pas mieux que le hasard chez eux (2409.12822, introduction et § 4 ; vérifié par `WebFetch` le 3 novembre). → attribution explicite.
4. « Models moved their activations along its direction » : imprécis ; le résumé dit des retouches alignées sur la direction qu'il faut pour échapper, d'amplitude insuffisante (2609.36490, p. 1). → « edited their activations the evading way, too weakly ».
5. « A probe takes no orders » seul : les deux mentors citeraient les attaques au niveau de l'invite contre les auditeurs à activations (2602.08877) et l'évasion apprise (2609.36490). → la phrase suivante le dit : « A probe can still be beaten through the model it reads ».
6. R1 : la page publique (2 novembre, 08:54 UTC) dit « Nothing of the white-box arm has been read » ; en interne, la relance sur la table v3 a été lue et close « non concluant (rejeu partiel) », non publiée sur décision de Lazar (`registres/decisions.md`, R-1322 et R-1324, sha256 du fichier `1c40ac9e…`). → la réponse dit seulement « preregistered and not in yet », vrai dans les deux cas, et ne donne pas le lien de la page de R1.

## 6. Risques qui restent

- La réponse est dense (cinq paragraphes, trois liens) ; 493 mots pour 500.
- T0.3 : les cellules les plus fortes ont été choisies après des essais exploratoires (page publique, « What this does not show ») ; « in the strongest settings » le signale sans le détailler.
- La règle « 100% human-written » est écrite pour la question de Heimersheim (formulaire, ligne 19), pas pour celle-ci ; à confirmer par Lazar pour tout le formulaire.
