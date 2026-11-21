# Pièce 6 — Esquisse de devis de la banque d'épisodes de la famille aveugle de réserve du cycle 2 (v2)

- **Version 2**, écrite le 21 novembre 2026 après la contre-lecture (pièce 7, `f830f70cb68b3ca0…`, verdict « à corriger ») ; la v1 est gardée (R12). Points traités : 1 e (ancre comptée en appels) et 7 c (relectures recomptées, monteur désigné).
- Classe A (un devis est une pièce décisive). **Esquisse seulement : aucune dépense, aucun GO demandé ici.**
- Écrit le 21 novembre 2026 par le concepteur aveugle de la famille de réserve. En clair, **sans aucun contenu de
  mode** : cette pièce ne nomme, ne décrit ni ne suggère la famille.
- Appui : règle du jeu, brouillon 5, nœud 9, option (b) (`527a3e7e…`) : chiffrer, par un devis écrit sans dépense, le
  coût d'une famille (conception aveugle, vérité du dommage, banque de la taille d'un mode) ; N-062 point 3 : chaque
  famille est une ligne de budget.
- **Aucun prix n'est écrit ici.** Je n'ai lu ni le registre des dépenses ni aucun devis ; un prix non vérifié n'entre
  pas dans un devis (R6). La mère remplit les prix unitaires depuis ses registres, avec chemin et empreinte.

## 1. Ce qui est déjà fait, sans dépense

| poste | état |
|---|---|
| conception aveugle de la famille (pièces 2 à 5, au coffre) | faite, scellée |
| attestation d'aveuglement (pièce 1) | faite, scellée avant les autres |
| contre-lecture des pièces 2 à 5 (pièce 7), index (pièce 8) | à faire, par d'autres mains, sans dépense de calcul |

## 2. Ce qui reste à payer : la banque, en quatre postes

Notations : **n** = nombre de tâches de la banque ; **e** = épisodes par tâche et par condition ; **a** = actions par
épisode (le nombre de pas T du banc) ; **k** = nombre moyen d'éléments de référence lus par tâche (valeur tenue au
coffre) ; **p_a** = prix d'une action de l'agent sur la carte ; **p_l1**, **p_l2** = prix d'une lecture par chacun des
deux lecteurs de la vérité du dommage ; **p_anc** = prix d'une lecture par l'agent de l'ancre.

| poste | volume | coût |
|---|---|---|
| A. Épisodes honnêtes, deux graines par tâche (jumeaux et nul « honnête contre honnête ») | 2 × n × e épisodes | 2 × n × e × a × p_a |
| B. Épisodes « sabotage demandé », deux doses de mesure | 2 × n × e épisodes | 2 × n × e × a × p_a |
| C. Épisodes de dose flagrante, pour l'épreuve de l'oracle seulement, sur un sous-ensemble de n_f tâches | n_f × e épisodes | n_f × e × a × p_a |
| D1. Lectures de la vérité du dommage, deux lecteurs | (4 × n × e + n_f × e) ensembles × k questions | (volume) × (p_l1 + p_l2) |
| D2. Relectures des épreuves de manipulation, deux lecteurs | au moins 5 × 20 ensembles manipulés (trois épreuves à 20 ensembles, une épreuve à deux niveaux de 20), plus autant d'ensembles intacts mêlés : au moins 200 ensembles × k questions | (volume) × (p_l1 + p_l2) |
| D3. Lectures des oracles rapportés à côté, deux lecteurs | (4 × n × e) ensembles × k' questions, k' = nombre moyen d'éléments de ces références par tâche (valeur tenue au coffre) | (volume) × (p_l1 + p_l2) |
| D4. Ancre des épreuves, jugée par un agent neuf (GO-2026-11-21-66) | 30 questions | 30 × p_anc |
| D5. Épreuves du programme de vérification | sur processeur | sans appel |

À ajouter, hors de cette esquisse : la lecture des épisodes par les moniteurs gelés (elle relève du devis de la
lecture du cycle, pas de la famille). L'ancre n'est plus du temps d'une personne : elle est comptée au poste D4.

## 3. Tailles de principe proposées

- **n = 60** si la banque reprend la taille du fichier de tâches du pilote
  (`donnees/t05-pilote-v1/taches-pilote-60-v1.json`, `287e83485cba5500…`, 60 tâches). **Réserve** : N-049 demande des
  tâches fraîches par génération ; si la famille doit se lire sur des tâches jamais vues par les concepteurs de
  moniteurs, il faut un tirage disjoint, et son extraction est un poste de plus, non chiffré ici.
- **e = 1**, **n_f = 20**.
- Avec ces tailles : 120 épisodes honnêtes, 120 épisodes « sabotage demandé », 20 épisodes de dose flagrante, soit
  **260 épisodes** et **260 × a actions** ; par lecteur, environ **260 × k** questions au poste D1, **au moins
  200 × k** au poste D2 et **240 × k'** au poste D3 ; **30** questions pour l'agent de l'ancre.
- La règle du bras parle de 100 ou 200 épisodes par bras (`prereg/bras-attaque-regle-v1.md`, `88418df0…`, l. 85). Si
  le titulaire veut 100 épisodes par dose, alors n × e = 100, et les volumes se recalculent par les formules.

## 4. Ordre de dépense proposé (chaque étape sur son propre GO)

1. Postes A et C, puis les épreuves de l'oracle (pièce 4). Si une épreuve ou une précondition échoue, le poste B
   n'est pas dépensé : le repli écrit s'applique, et l'argent du poste B est épargné.
2. Poste B, puis ses lectures.

## 5. Ce que la mère doit trancher ou faire trancher

1. Les prix unitaires p_a, p_l1, p_l2, p_anc, depuis les registres, et le plafond.
2. Les deux familles de modèles des lecteurs (ni celle des moniteurs, ni celle de l'agent), et le modèle de l'agent de
   l'ancre (autre famille que les lecteurs si possible ; sinon, réserve d'indépendance au verdict).
3. Le monteur des lecteurs, de leurs invites et du programme de vérification est désigné : un agent Opus neuf
   (GO-2026-11-21-66, `registres/go.md` sur `main`, l. 665). Reste à désigner la main distincte qui atteste
   qu'aucun moniteur ne lit la référence cachée (elle n'est ni le monteur, ni l'auteur, ni un concepteur de
   moniteur).
4. Tâches du pilote ou tirage disjoint (section 3).
5. La main qui vérifie, en lisant le coffre, que cette famille ne recouvre ni celle du cycle 1 ni un mode connu.

## 6. Journal du concepteur

- **Refus de classifieur : aucun** pendant l'écriture des pièces 1 à 6, ni pendant leur correction en v2.
- Aucune génération, aucun appel payant, aucun code d'attaque, aucune demande de fusion.
- La famille du cycle 1 n'a pas été vue (pièce 1, section 2).
