# Lecture des fiches par Kimi, seconde tentative — journal et relevé de dépense

Opérateur : session fille, 14 novembre 2026 (heures par `date -u`), GO-2026-11-13-06, commandes `commandes-v1.md`
(scellées avant tout appel).

## Verdict

**Arrêtée après deux appels : lecture incomplète.** Les deux premiers lots de la lecture L1 rendent un statut 200, mais
avec `finish_reason` = `length` : le modèle a passé tout le budget de sortie (`max_tokens` 32 768) à raisonner
(32 765 jetons de raisonnement chaque fois) et ne rend **aucun contenu** (champ `content` vide). C'est l'anomalie bloquante
« fin autre que `stop` » de l'outil v2 (verdict E2 à venir, aucune désignation possible). Aucune relecture n'est permise, et
envoyer les quatre lots restants avec le même `max_tokens` aurait coûté environ 1,5 USD pour une lecture déjà incomplète :
arrêt, pas d'improvisation.

## Déroulé

- 06:55:17Z relais Kimi v4 lancé (environnement réduit à une liste de noms), **PID 941** (vérifié par `/relais/etat` ;
  `variable_cle_encore_presente` : false), plafond 3,5 USD, 6 appels.
- 06:55:39Z envoi `envoi-L1-lot1-v2.corps.json` → 07:12:35Z statut 200, fin `length`, 25 374 jetons d'entrée, 32 768 de
  sortie, dont 32 765 de raisonnement ; coût 0,378428 USD.
- 07:12:35Z envoi `envoi-L1-lot2-v2.corps.json` (parti automatiquement avant que je lise la fin du lot 1) ; à 07:12:55Z le
  script d'envoi a été arrêté par son PID (1014), pour qu'aucun autre lot ne parte ; le lot en vol est allé à son terme →
  07:28:09Z statut 200, fin `length`, 26 001 jetons d'entrée (dont 9 216 en cache), 32 768 de sortie, dont 32 765 de
  raisonnement ; coût 0,379682 USD.
- Lots L1-lot3 et L2-lot1 à 3 : **non envoyés**.
- 07:28:27Z relais arrêté par son PID (`kill -INT 941`), vérifié arrêté.
- `verifier` **non lancé** (lecture incomplète : quatre réponses manquent, deux sans contenu) ; condition C1 **sans objet**.
  Classement non lancé (rôle de la mère).

## Dépense (relevé du relais avant l'arrêt, `relais/etat-relais-avant-arret-v1.json`)

2 appels, statuts 200 : 2, refus 0, écart de modèle servi 0 ; **dépense 0,758110 USD** (sous le plafond de 3,5 USD et la
réserve de 4 USD du lecteur ; 0,498232 USD déjà comptés au pire cas pour la première tentative, R-2645).

## Pour la mère (nœud éventuel, non tranché ici)

Le budget de sortie que fixe l'outil v2 (32 768) ne suffit pas au raisonnement de `kimi-k3.1-pro` sur des lots de 14 ou 15
fiches. Une reprise demanderait une version de l'outil (lots plus petits, `max_tokens` plus grand, ou effort de
raisonnement réduit si l'amont le permet) et donc une nouvelle garde de dépense : décision de la mère ou de Lazar.
Les réponses contiennent le seul champ `reasoning_content` du lecteur (aucune clé, aucun identifiant de compte) ; je ne les
ai pas lues au-delà de leurs champs de forme.
