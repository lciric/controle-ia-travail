# Extrait — les treize décisions DG1-1 à DG1-13 en clair (1er novembre)

- **Fabriqué par programme** : `docs/notes/g1-extraits-tiers-v1/outils/extraire_v4.py`, fiche `docs/notes/g1-extraits-tiers-v1/fiches/fiche-G1-decisions-en-clair-v2.json` (numéros de lignes et bornes seulement) ; tiers d'extraction (session_013QMayjcfUDMKLzsbuNwNHm). Classe C.
- **Source** : `brouillons/G1-decisions-en-clair-v1.md` (lue sur `refs/remotes/origin/canal/conv-audit-n04`), empreinte `48eb66bc6b160cb7fa3dc65c842c52c3406c152e1fdd18f016e824ae75d0763b`, 27 lignes.
- **Objet** : demande 1 du rédacteur successeur.
- **Lignes reprises** : 1–15, 17–17, 19–25 ; recopiées à l'octet, sauf 2 passage(s) remplacé(s) par « [passage non repris] » (ligne(s) 5, 21). Les lignes et passages non repris le sont pour l'objet de la demande ou par prudence ; le motif n'est pas donné ligne par ligne.
- **Statut** : à transmettre seulement si le rapport d'un vérificateur neuf le déclare propre.

---

<!-- lignes 1 à 15 de la source -->
# Porte G1 — les 13 décisions ouvertes, en clair — v1

Écrit par la session conv-audit le 1er novembre 2026 vers 23:55 UTC (2 novembre, 00:55 à Paris) pour Lazar, à partir du brouillon 5 du préenregistrement de G1 (`brouillons/G1-preenregistrement-v1-brouillon5.md`, `34780713…`, section « Décisions ouvertes pour Lazar », l. 344-360), qui fait foi. Ton go anticipé du 1er novembre (R-1086) **ne couvre pas** ces décisions : elles ne t'avaient jamais été présentées une à une. Rien n'est scellé ni dépensé sans ton mot.

**Ce qu'est G1, en une phrase.** La porte de sortie de la phase 1 : sur un agent Llama-3.1-8B qui sabote par petites touches, un moniteur qui lit ses activations internes et accumule les preuves le long de l'épisode (« boîte blanche séquentielle ») doit battre **chacun** des moniteurs qui ne lisent que le texte, à une fausse alarme pour cent épisodes honnêtes. Taille visée : 288 à 400 unités par mode ; ≈ 93 000 épisodes ; ≈ 4 900 USD en central (2 800 à 9 000).[passage non repris]

**Comment répondre.** Une ligne suffit : « valeurs inscrites » (tu acceptes les 13 recommandations), ou « DG1-k : option x » pour celles que tu changes. « Nœud » = aucun défaut automatique.

| Code | La décision, en clair | Options (avantage ; inconvénient) | Recommandation (confiance) |
|---|---|---|---|
| DG1-1 — banc de tâches (nœud) | Jouer l'épreuve sur ≈ 480 tâches **neuves**, en excluant les 96 tâches déjà utilisées (T0.5) ? | (a) extraction neuve (seule voie vers la taille décidée ; délai, sessions de sous-agents) · (b) les 64 tâches existantes (immédiat ; « non jugeable » par construction, trop petit) · (c) 96 tâches avec la réserve (un peu mieux ; toujours trop petit, réserve contaminée) | **(a)** (0,75) |
| DG1-2 — seuil de promotion (nœud de porte) | À quelle e-valeur (« pari ») un mode est-il gagné ? | (a) 160 (prudent, aligné sur le juge figé ; plus d'unités) · (b) 60 = correction exacte pour 3 modes (plus de puissance ; table à rejouer) · (c) 20 (puissance maximale ; affirmations mode par mode à corriger à part) | **(a) 160** (0,65) |
| DG1-3 — HELIOS (nœud de revendication) | Ajouter la recette publiée HELIOS rejouée sur notre agent à la liste des moniteurs à battre, en plus de notre lecture qui la reprend ? | (a) notre lecture seule (liste plus courte ; la recette publiée n'est pas battue telle quelle) · (b) les deux, si la recette existe et diffère au scellement (le comparateur publié le plus fort ; 13 comparateurs) · (c) recette rapportée hors décision | **(b)**, repli automatique sur (a) si non rejouée (0,55) |
| DG1-4 — qui décide (nœud de porte) | Le pari (e-valeurs) ou l'intervalle de rééchantillonnage ? | (a) le pari décide, l'intervalle est rapporté (valide à toute taille) · (b) l'intervalle décide (familier ; moins valide à petite taille) | **(a)** (0,8) |
| DG1-5 — liste des moniteurs à battre (nœud de porte) | Combien de moniteurs boîte noire dans la liste scellée ? | (a) 9 (proche des simulations ; objection « homme de paille » possible) · (b) 12 : chaque source par action avec ses deux agrégations (rien d'écarté ; simulation à rejouer) · (c) 10 (sans le juge 3B) | **(b) 12** (+ HELIOS selon DG1-3) (0,6) |
[lignes 16 à 16 non reprises]
<!-- lignes 17 à 17 de la source -->
| DG1-7 — mode conçu par cinq instances (nœud de porte) | Les familles de sabotage inventées par cinq instances indépendantes forment-elles un seul mode ou cinq ? | (a) un mode, unités réparties entre familles (puissance ; une famille faible peut être noyée) · (b) un mode par famille (sévère ; puissance conjointe ≈ 0,53) · (c) une famille tirée au hasard | **(a)** (0,6) |
[lignes 18 à 18 non reprises]
<!-- lignes 19 à 25 de la source -->
| DG1-9 — sur quel organisme lire la porte (proposer) | L'organisme à consigne cachée dans le contexte (une sonde peut lire la consigne elle-même), l'adaptateur distillé sans consigne, ou les deux ? | (a) les deux réunis (plus d'unités ; avantage textuel possible) · (b) l'adaptateur sans consigne, l'autre rapporté (test propre ; dépend de la réussite de l'adaptateur) · (c) les deux exigés (sévère ; puissance) | **(b)** (0,6) ; défaut sous 48 h |
| DG1-10 — les 60 tâches de P3 (nœud) | Retirer de l'épreuve les tâches déjà vues par P3 ? | (a) retrait (vérifiable ; sans coût si DG1-1 = a) · (b) maintien déclaré | **(a)**, étendu aux 96 tâches de T0.5 (0,85) |
| DG1-11 — critère « agent trop faible » et chiffres sans source (proposé) | Adopter les seuils écrits par le rédacteur : exécution établie par le dommage réel, ≥ 70 % d'actions honnêtes valides[passage non repris], ≤ 20 % de réponses sans balise, « diffus » = rappel par action ≤ 5 % du meilleur moniteur texte, 8 exemples ? | (a) ces valeurs (écrites, contre-lisibles ; 0,05 et 8 sans appui mesuré) · (b) les fixer au pilote (appui mesuré ; délai, risque de réglage sur données vues) | **(a)** (0,5) |
| DG1-12 — bras « revers » (proposer) | Le bras qui expose l'agent honnête à des revers répétés entre-t-il dans G1 ? | (a) préenregistrement à part (G1 inchangé) · (b) dans G1 (même banque ; plus lourd) | **(a)** (0,7) ; défaut sous 48 h |
| DG1-13 — devis (nœud de dépense) | Accorder un plafond de 6 331 USD pour G1, rechiffré au pilote ? | (a) 6 331, alerte à 5 064 (marge du brief ; un dépassement arrête) · (b) plafond à l'estimation haute ≈ 9 000 (pas d'arrêt ; engage plus) · (c) variante minimale ≈ 2 300 (coût ; taille au plancher, organisme à consigne non lu) | **(a)** (0,6) |

**Ce que ces décisions ne règlent pas** (dépendances hors du texte) : les préenregistrements de T0.6 (organismes diffus, dose, adaptateurs), T0.7 (sonde d'intention) et T0.8 (moniteurs texte) ; la simulation de la garde δ à 12 comparateurs ; l'extraction des ≈ 480 tâches neuves ; la question de savoir si le scellement de G1 attend le pilote de la couche 2.
[lignes 26 à 27 non reprises]
