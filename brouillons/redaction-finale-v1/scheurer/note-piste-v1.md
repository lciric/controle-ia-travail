# Note de piste — réponse à Jérémy Scheurer (tendance d'échelle) — v1

Rédacteur neuf, 3 novembre 2026, de 15:13 à 15:35 environ (temps universel, `date -u`). Je n'ai écrit aucune version antérieure des réponses de Lazar. Consigne scellée `brouillons/reprise-conv-audit-2026-11-02-nuit/prompts-sous-agents/redaction-finale-scheurer-v1.md`, sha256 `0e8b5fc9b4c26865532e0343fab1adb587b175ad8d20c74acf71ed2eee986000`, vérifiée avant lecture. Dossier de piste vérifié (`063eae8f…d838`), recoupement vérifié (`bea573aa…e0a`).

Piste imposée par la règle gelée : groupe **« Seuil du moniteur »** (on fige l'attaque, on fait varier le moniteur, on lit un point de croisement continu, ajusté sur la date de sortie). Je ne l'ai pas changée. La réponse actuelle de Lazar n'a servi que de réservoir ; sa tendance 2 (horizon côté attaquant) n'est pas reprise.

## 1. Les trois arguments retenus

**A. Figer la malveillance, faire varier le seul moniteur, vérité par exécution.**
Raisons : (1) une tendance de propension sur les dates mesurerait en partie la conscience d'évaluation, que le papier du mentor montre en hausse sous entraînement de capacités (2,0 % → 20,5 %, 2509.15541 § 6.1) ; (2) une porte dérobée vérifiée à l'exécution ne dépend d'aucun juge ; (3) un corpus gelé, privé et publié par son empreinte, ne peut pas entrer dans l'entraînement des moniteurs suivants ; (4) Martin et Roger (2605.12366, vérifié sur le résumé) montrent que la courbe existe : la détection baisse avec la longueur ; (5) Control Tax § 2.3 : les modèles plus forts surveillent mieux, il y a donc une pente à trouver.
Appui public de Lazar : P3 (deux sondes génériques sous leur plancher de 200 sondes aléatoires) — un moniteur plausible peut échouer devant un plancher mécanique. **Mesure qui tue** : sur un générateur d'attaques réservé, battre de 10 points les détecteurs de longueur seule et de style seul, à fausses alertes égales ; sinon l'instrument est abandonné.

**B. Calibrer sur des transcriptions honnêtes entières, à chaque longueur.**
Raisons : (1) l'horizon n'a de sens que si le taux de fausses alertes est tenu à toute longueur ; (2) sinon la pente n'est qu'une reparamétrisation des fausses alertes (objection 1 de SC-03) ; (3) Lazar a un résultat public exactement là-dessus : T0.3, seuil séquentiel de Ville 0,21 à 0,35 de fausses alertes sous les plus forts effets d'épisode, contre 0,046 à 0,055 pour une calibration sur 1 000 épisodes honnêtes entiers ; (4) c'est la notation de trajectoire entière d'Apollo ; (5) la longueur est en pas d'agent, pas en jetons (les tokeniseurs diffèrent).
**Mesure qui tue** : fausses alertes sur des transcriptions honnêtes neuves hors d'une bande préfixée autour de 5 % à une longueur quelconque, et l'horizon du moniteur est nul.

**C. Un premier point existe, et il prévient sur le signe.**
Raisons : (1) R7 est une tendance de taille d'une capacité de surveillance, publiée, préenregistrée : −0,19 [−0,24 ; −0,11] par décuplement sous note négative standard ; (2) le 72B a un gain presque nul mais ses lectures bougent : un seul nombre aurait dit « robuste », d'où les courbes entières ; (3) une seule date de sortie pour les sept tailles : pente de taille, pas de temps, d'où un panel multifamille daté ; (4) 2510.09462 : le moniteur le plus fort sans injection (GPT-4.1) est entièrement capturé sous injection, d'où une strate à attaquants contemporains rapportée à part, jamais moyennée ; (5) le rapport des deux horizons donne une forme mesurable d'« une » voie par laquelle la détection deviendrait plus difficile (mise à jour d'Apollo de mai 2026).
**Mesure qui tue** : le facteur annuel ne compte que si son intervalle est entièrement d'un côté d'un seuil préfixé ; sinon « non concluant » (règle de SC-10, que R7 applique déjà : M3 faux, pente dans un seul bras).

## 2. Usage des fiches de la piste

- **SC-03** (rang 1, lecture de contrôle concordante) : instrument repris — une anomalie par épisode positif, position uniforme, notation de la trajectoire entière, calibration par épisodes entiers, duel de validité contre les références de style et de localité (δ = 10 points, dit paramètre). Drapeau faible corrigé : dernière phrase de la réponse (« detection of frozen, non-adaptive sabotage, not of misalignment »). Ses tâches synthétiques à état caché ne sont pas reprises : la menace principale qu'elle déclare est le style du générateur ; les portes dérobées vérifiées à l'exécution sont plus sûres et déjà employées par la littérature que le mentor connaît.
- **SC-10** (rang 2, sans drapeau) : vérité par exécution, axe de taille d'abord puis panel daté, corpus non contaminable, strate d'attaquants contemporains et duel de transport (ici : le rapport des horizons), règle « intervalle d'un côté ».
- **SC-13**, **SC-04**, **SC-06** : non repris. SC-13 (confinement) est l'inverse du risque par occasion, sans appui public de Lazar propre ; SC-04 exige un panel humain coûteux (20 à 50 k€ illustratifs) et porte le même drapeau que SC-03 ; SC-06 (budget minimal) souffre du biais du minimum et n'a pas de coût chiffré.
- **Retiré en relecture** : le contrôle de dilution de SC-10 (« même porte dérobée entourée de code honnête ») ; dans ce plan, la longueur est elle-même faite de travail honnête, le contrôle serait circulaire. Remplacé par le contrôle de calibration (argument B), qui a l'appui de T0.3.
- **Drapeau SC-08** (précédent public abandonné : horizon de capacité trompeuse contre un protocole de contrôle, billet de Sean Peters du 8 août 2025, vu dans la moisson, non lu) : il vise l'horizon côté attaquant, qui dépend du modèle et du moniteur. La piste fige l'attaquant ; rien de SC-08 n'est repris, et le billet n'est pas cité.

## 3. Relecture en mentor (phrases qu'il pourrait contredire, et ce que j'ai fait)

1. « the horizon … grows » contre « la détection deviendra plus difficile » (son groupe) : gardé comme énoncé sur des attaques gelées, avec la portée dite en dernière phrase, et la strate contemporaine qui teste le sens inverse.
2. « as METR adds longer tasks » : affirmation sur la pratique du METR qu'aucune source ne donne ; **retirée**.
3. « The horizon does not saturate » contredisait « Lengths stay inside every monitor's context window » ; **retirée**, remplacée par « keeps headroom ».
4. « capture gain » : le README public de R7 dit « deference gain » ; **remplacé**, pour qu'il retrouve le nombre.
5. « dilution » : test circulaire dans ce plan ; **remplacé** (voir 2).
6. « X being the slope » : X est un facteur, lu sur la pente du logarithme ; **corrigé**.
7. « as Apollo's May update expects » : leur raison est la conscience situationnelle, pas l'attaquant ; la phrase dit « one way detection could get harder », sans prétendre tester leur raison.
8. « elicitation problem » rattaché à son propre papier (2412.04984 § 4, sous-estimation des capacités, surtout des plus capables).
9. 5 % de fausses alertes : un mentor de contrôle pourrait préférer 1 % (budget d'audit) ; gardé à 5 % parce que c'est le niveau que T0.3 a tenu et qu'un pilote le certifie à moindre coût ; à toi de trancher (paramètre).

## 4. Ce qui reste à confirmer par Lazar

- Que `faff48b` (ou plus récent) est bien sur le `main` public d'`ideation-organism`, pour le lien vers `resultats/controle-simulation-defenses/` (je n'ai fait aucun appel réseau à git).
- Le chiffre de Martin et Roger (2× à 30× après 800 000 jetons) est vérifié sur le résumé arXiv par `WebFetch` seulement (niveau transcription) ; si tu veux l'opposabilité, PDF empreinté.
- Le seuil de 10 points et la bande autour de 5 % sont des paramètres : à figer dans un préenregistrement, pas des résultats.
- L'énoncé cible entre guillemets (17 mots) est le tien, pas une citation ; si le formulaire est lu par une règle mécanique de citation, enlever les guillemets ne coûte aucun mot.
- Le plan suppose un panel daté de moniteurs ouverts (trois familles ou plus, plusieurs dates chacune) qui n'est pas constitué, et un coût de calcul pour des transcriptions longues qui n'est pas chiffré (R7 a coûté environ 3 dollars, mais sur des réponses courtes).

## 5. Fichiers

- `reponse-v1.md` : réponse seule, puis compte par script — 492 mots (espaces), 496 (motif) ; texte seul sha256 `1277345560d3c29486a8a65776ece767344cf49a573130841889f284187baf78`. Fichier régénéré une fois par moi pendant la tâche (retrait de la phrase sur le METR), jamais préexistant.
- `registre-affirmations-v1.md` : 29 lignes, sources et forces.
- Jets intermédiaires et script de compte, hors du dépôt : `/tmp/redaction-scheurer-brouillons/` (`jet-1.txt` à `jet-9.txt`, `compte_mots.py`).
