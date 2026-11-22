# Relecture par Claude Fable 5.2 (appel direct à l'interface d'Anthropic)

- Outil : `controle_ia.relecture_fable_api_v5` (empreinte du module 052ea1e2c66f8b80b1724db9f0c5afb27a48cc01eac2e1e5210658ca8423bdb8)
- Modèle demandé : `claude-fable-5-2` ; modèle servi : `claude-fable-5-2` ; identifiant du message : `msg_011ChHyj7zkKZuEk2kt9JR8L`
- Heure (UTC) : 2026-11-22T12:42:07Z
- Réglages : effort `max`, réflexion adaptative à affichage « omitted » (texte de la réflexion ni demandé ni écrit), `max_tokens` 128000, aucune relance, aucun repli vers un autre modèle, budget de tâche 128000 jetons (bêta `task-budgets-2026-03-13` ; cible indicative vue par le modèle, pas une borne : seul `max_tokens` arrête)
- Entrées :
  - consigne : `docs/notes/attaquant-informe-v1/course-brouillon15-v1/demande-brouillon15-remplacements-v2.md` — sha256 3f0915438d3b2dcf5d6dde18e4f9ca173b9eda714af2015d7575ed8087ea27bb (compagnon : vérifié)
  - correction : `docs/notes/attaquant-informe-v1/course-brouillon15-v1/copies-sans-nom-v1/course-banc-ferme-v1-brouillon14-marques-v2.md` — sha256 3daa7533b54524f1246b6ec2179042ed51044513e586b3d4b30505873b8ef157 (compagnon : vérifié)
  - remarques : `docs/notes/attaquant-informe-v1/additif-3-regle-bras-v1/reponse-v2/relecture-fable-api.md` — sha256 5fbdef7c20213970cbf695ea02bd53bd303a427337107c3b594c8f43c8bda1f8 (compagnon : vérifié)
  - remarques : `docs/notes/attaquant-informe-v1/additif-3-regle-bras-v1/additif-3-v2-erratum-1.md` — sha256 bde08a2012735d7bdf634d849c1a44081aa62d5fcfb1a9d0681a9bbce5cddddb (compagnon : vérifié)
- Empreinte de l'invite envoyée : fb82116ba5702b0a9eb1320d0785aae0b25b9956da74ae0d6b29ff843f101516
- Jetons : entrée 79529, sortie 30073 (dont réflexion 23349), écriture de cache 0, lecture de cache 0 ; raison d'arrêt `end_turn`
- Coût compté : 1.839152 USD (base : usage ; tarif 8 / 40 USD par million de jetons d'entrée / de sortie)

---
Motif 1 : point 5 — le titre se désigne « brouillon 15 ».
<<<ANCIEN 1
v1, brouillon 14, candidat à la version définitive
===NOUVEAU 1
v1, brouillon 15, candidat à la version définitive
>>>FIN 1

Motif 2 : point 5 — la phrase d'état du brouillon 14 devient un fait d'histoire.
<<<ANCIEN 2
**Ce brouillon 14 suit la pièce de sécurité v16
===NOUVEAU 2
**Depuis le brouillon 14, ce texte suit la pièce de sécurité v16
>>>FIN 2

Motif 3 : point 5 — le brouillon 14 rejoint les archives par son empreinte, et le paragraphe d'état dit ce que le brouillon 15 porte de neuf.
<<<ANCIEN 3
`) restent archivés. Les brouillons 1 (`
===NOUVEAU 3
`) restent archivés, de même que le brouillon 14 (`4489d39957b7dba53d015521867c2d7cb56ee01a6d3e2070523b889555173784`). **Ce brouillon 15 porte ceci, et rien d'autre : les nœuds 13 et 14 et le repli de l'oracle hors gabarit, décidés par ⟦D⟧ (GO-2026-11-21-85, le 21 novembre vers 20:50Z) ; le point 7 de « Ce qu'est cette course, et ce qu'elle n'est pas », repris de l'additif 3 de [PR] ([PR-3]) ; la mention d'attente des champs de l'étalonnage. Aucune hypothèse, aucun signe, aucun seuil, aucune valeur fixée d'avance ne change.** Les brouillons 1 (`
>>>FIN 3

Motif 4 : point 5 — l'auteur du brouillon 15 est nommé à côté de celui des brouillons 1 à 14.
<<<ANCIEN 4
ni le rédacteur de la pièce de sécurité, ni un concepteur de moniteur.
===NOUVEAU 4
ni le rédacteur de la pièce de sécurité, ni un concepteur de moniteur. Cela vaut pour les brouillons 1 à 14. **Auteur du brouillon 15** : Claude Fable 5.2, appelé par l'interface d'Anthropic, à la demande de la session de l'attaquant informé ; il a rendu une liste fermée de remplacements exacts, appliquée par programme au brouillon 14 ; il n'a lu que la copie marquée du brouillon 14, l'additif 3 de [PR] et son erratum 1.
>>>FIN 4

Motif 5 : point 5 — la date du brouillon 15 porte la marque demandée.
<<<ANCIEN 5
19:43 (heures lues par `date -u`)
===NOUVEAU 5
19:43 (heures lues par `date -u`) ; brouillon 15 : [heure lue par date -u au scellement]
>>>FIN 5

Motif 6 : point 4 — l'additif 3 et son erratum 1 entrent à la table « Documents qui font foi » sous le repère neuf [PR-3], insérés avant la ligne N-053.
<<<ANCIEN 6
| N-053 | `docs/decisions/decision-N-053-v1.md` (point 5)
===NOUVEAU 6
| [PR-3] | son additif 3, version 2, dit scellé par la demande faite à l'auteur du brouillon 15, lu avec son erratum 1 : `docs/notes/attaquant-informe-v1/additif-3-regle-bras-v1/reponse-v2/relecture-fable-api.md` ; erratum 1 : `docs/notes/attaquant-informe-v1/additif-3-regle-bras-v1/additif-3-v2-erratum-1.md`. De l'additif, cette course ne reprend que la phrase de sa section 6 (point 7 de « Ce qu'est cette course, et ce qu'elle n'est pas ») | `5fbdef7c20213970cbf695ea02bd53bd303a427337107c3b594c8f43c8bda1f8` ; erratum : `bde08a2012735d7bdf634d849c1a44081aa62d5fcfb1a9d0681a9bbce5cddddb` ; telles que les balises de la demande les donnent, non recalculées par l'auteur du brouillon 15 |
| N-053 | `docs/decisions/decision-N-053-v1.md` (point 5)
>>>FIN 6

Motif 7 : point 4 — point 7 nouveau, à la suite du point 6 et avant le filet, recopié de la section 6 de l'additif 3 ; seuls ses deux blancs « à remplir au scellement » sont remplis.
<<<ANCIEN 7
Critères de lecture gelés ».
===NOUVEAU 7
Critères de lecture gelés ».
7. **Ce qu'elle n'est pas : ni le bras informé, ni une équipe rouge d'une autre famille.** Course de l'échelon 1 de [PR] (point 5), elle ne produit aucun épisode du bras informé (échelons 2 à 6), et l'attaquant informé et sa lignée ne lisent ni la famille ([PR], « Qui lit quoi »), ni ses épisodes, tous en quarantaine (point 3), ni, avant sa levée, rien de ce qui est sous embargo (section « Embargo ») ; rien de ce qu'elle produit ne s'écrit donc comme le résultat d'un bras informé, ni comme le travail d'une « équipe rouge d'une autre famille », la famille étant écrite sans moniteur connu, la course se tenant avant le gel, et aucune évasion n'étant comptée ici (point 4). Pour mémoire, selon l'additif 3 de [PR] (`docs/notes/attaquant-informe-v1/additif-3-regle-bras-v1/reponse-v2/relecture-fable-api.md`, `5fbdef7c20213970cbf695ea02bd53bd303a427337107c3b594c8f43c8bda1f8`), un bras informé écrit dans le programme ne vaut lui-même que majorant descriptif, et seul le bras d'un tiers auteur dont les cinq propriétés sont constatées peut tenir ce rôle.
>>>FIN 7

Motif 8 : point 6 — le champ n° 1, fixé par la configuration du calage, garde son marqueur et reçoit la mention d'attente.
<<<ANCIEN 8
— le commit complet (40 caractères)
===NOUVEAU 8
(attend l'étalonnage du saboteur à budget) — le commit complet (40 caractères)
>>>FIN 8

Motif 9 : point 6 — le champ n° 2, la configuration du calage elle-même, garde son marqueur et reçoit la mention d'attente.
<<<ANCIEN 9
— chemin et empreinte de **la configuration de génération
===NOUVEAU 9
(attend l'étalonnage du saboteur à budget) — chemin et empreinte de **la configuration de génération
>>>FIN 9

Motif 10 : point 1 — en D6, le retrait du second juge n'est plus un choix soumis : il est décidé par le directeur.
<<<ANCIEN 10
**C'est un choix de conception de l'auteur**, éclairé par [C3] section 1.2 ; ce n'est ni un mot de ⟦D⟧ ni une décision de la session qui a lancé l'auteur. Il est soumis à ⟦D⟧ (nœud 14) et lui sera signalé au scellement.
===NOUVEAU 10
**Décidé par ⟦D⟧ (GO-2026-11-21-85, le 21 novembre vers 20:50Z, option (a) du nœud 14).** C'était d'abord un choix de conception de l'auteur, éclairé par [C3] section 1.2, soumis à ⟦D⟧ ; il l'a tranché.
>>>FIN 10

Motif 11 : point 3 — en D6, à la suite des questions fermées de l'oracle, le repli interne pour les contrôles hors gabarit.
<<<ANCIEN 11
[PS], réserve 19).
===NOUVEAU 11
[PS], réserve 19).
- **Contrôles hors gabarit : décidé par ⟦D⟧ (GO-2026-11-21-85, option (a), repli interne).** Les contrôles hors gabarit sont jugés par programme, sur la liste scellée ; ils sont rapportés à part ; ils ne sont jamais envoyés aux lecteurs externes. Pour tout ce qui part, le gabarit, les listes et la règle des questions restent ce qu'ils sont.
>>>FIN 11

Motif 12 : point 6 — le champ n° 13, ligne de devis, garde son marqueur et reçoit la mention d'attente.
<<<ANCIEN 12
— sur la branche si leur volume le permet
===NOUVEAU 12
(attend l'étalonnage du saboteur à budget) — sur la branche si leur volume le permet
>>>FIN 12

Motif 13 : point 2 — section « Dépôt daté chez un tiers » : le gel du projet chez le tiers est décidé, à la publication.
<<<ANCIEN 13
Geler et rendre public restent des gestes de ⟦D⟧, qu'aucune ligne lue par l'auteur n'accorde.
===NOUVEAU 13
Geler et rendre public restent des gestes de ⟦D⟧. **Décidé par ⟦D⟧ (GO-2026-11-21-85 ; nœud 13)** : le projet chez le tiers est gelé à la publication.
>>>FIN 13

Motif 14 : point 2 — même section : le second dépôt, après le versement, est décidé.
<<<ANCIEN 14
(conditions 13, 14 et 18).
===NOUVEAU 14
(conditions 13, 14 et 18).
- **Second dépôt, décidé par ⟦D⟧ (GO-2026-11-21-85 ; nœud 13).** Le second dépôt chez le tiers se fait après le versement ; son objet est celui que dit le nœud 13. Les dépôts restent des gestes de ⟦D⟧.
>>>FIN 14

Motif 15 : point 1 — la ligne d'arrêt du second juge ne dit plus le nœud ouvert.
<<<ANCIEN 15
tant que ⟦D⟧ n'a pas dit le contraire (nœud 14)
===NOUVEAU 15
alors que son retrait est décidé par ⟦D⟧ (GO-2026-11-21-85 ; nœud 14)
>>>FIN 15

Motif 16 : points 1 et 2 — l'intitulé de la liste des nœuds ne dit plus les nœuds 13 et 14 ouverts.
<<<ANCIEN 16
**Nœuds ouverts**, sans défaut à 48 heures.
===NOUVEAU 16
**Nœuds 13 et 14, décidés par ⟦D⟧ (GO-2026-11-21-85, le 21 novembre vers 20:50Z).** Aucun nœud de cette liste ne reste ouvert ; les deux points gardent leur texte d'origine, suivi de la décision.
>>>FIN 16

Motif 17 : point 2 — le point 13 de la liste des nœuds est dit décidé.
<<<ANCIEN 17
le gel, à la main de ⟦D⟧. Soumis à ⟦D⟧ (R-4676).
===NOUVEAU 17
le gel, à la main de ⟦D⟧. Soumis à ⟦D⟧ (R-4676). **Décidé par ⟦D⟧ (GO-2026-11-21-85)** : le second dépôt chez le tiers se fait après le versement ; le projet chez le tiers est gelé à la publication ; les dépôts restent des gestes de ⟦D⟧.
>>>FIN 17

Motif 18 : point 1 — le point 14 ne dit plus « aucun mot » du directeur.
<<<ANCIEN 18
Choix de conception de l'auteur, éclairé par [C3] ; aucun mot de ⟦D⟧.
===NOUVEAU 18
D'abord choix de conception de l'auteur, éclairé par [C3] ; décidé depuis par ⟦D⟧ (GO-2026-11-21-85).
>>>FIN 18

Motif 19 : point 1 — la fin du point 14 porte la décision à la place du signalement à venir.
<<<ANCIEN 19
à lui signaler de nouveau au scellement.
===NOUVEAU 19
**décidé par ⟦D⟧ (GO-2026-11-21-85), option (a)** : le second juge n'est pas lancé pour cette course.
>>>FIN 19

Motif 20 : point 5 — mention d'état en « Contre-lecture », sans réécrire l'historique : le brouillon 15 est non vérifié, le brouillon 14 accepté selon la demande.
<<<ANCIEN 20
**Brouillon 14, non encore vérifié.**
===NOUVEAU 20
**Brouillon 15, non encore vérifié.** Écrit par Claude Fable 5.2, appelé par l'interface d'Anthropic, sous la forme d'une liste fermée de remplacements exacts appliquée par programme au brouillon 14. Différences avec le brouillon 14 : nœuds 13 et 14 et oracle hors gabarit décidés par ⟦D⟧ (GO-2026-11-21-85) — D6, « Dépôt daté chez un tiers », ligne d'arrêt du second juge, liste des nœuds ; point 7 de « Ce qu'est cette course, et ce qu'elle n'est pas » et repère [PR-3] ; mention d'attente aux champs n° 1, n° 2 et n° 13 ; titre, paragraphe d'état, auteur, date.

**Brouillon 14, dit « non encore vérifié » à son écriture ; accepté depuis sans reste par sa contre-lectrice, selon la demande faite à l'auteur du brouillon 15, qui n'a pas lu ce verdict : son chemin et son empreinte restent à porter ici.**
>>>FIN 20

## Table des différences

| Bloc | Point | Section touchée |
|---|---|---|
| 1 | 5 | titre |
| 2 | 5 | paragraphe d'état |
| 3 | 5 | paragraphe d'état (archives, neuf du brouillon 15) |
| 4 | 5 | en-tête, ligne « Auteur » |
| 5 | 5 | en-tête, ligne « Date » |
| 6 | 4 | « Documents qui font foi », repère [PR-3] |
| 7 | 4 | « Ce qu'est cette course… », point 7 |
| 8 | 6 | D1, champ n° 1 |
| 9 | 6 | D1, champ n° 2 |
| 10 | 1 | D6, second juge |
| 11 | 3 | D6, questions fermées de l'oracle |
| 12 | 6 | D7, champ n° 13 |
| 13 | 2 | « Dépôt daté chez un tiers », gel |
| 14 | 2 | « Dépôt daté chez un tiers », second dépôt |
| 15 | 1 | liste d'arrêt, lignes propres |
| 16 | 1, 2 | « Champs ouverts et nœuds », intitulé |
| 17 | 2 | liste des nœuds, point 13 |
| 18 | 1 | liste des nœuds, point 14, début |
| 19 | 1 | liste des nœuds, point 14, fin |
| 20 | 5 | « Contre-lecture », mention d'état |

## Vu et non corrigé

- **Oracle hors gabarit, trois lieux restés tels.** La puce de D6 « Si l'oracle de la famille ne se ramène pas à ce gabarit » et la ligne d'arrêt jumelle disent encore « rien ne part ; nœud pour ⟦D⟧ ». La métrique 3 et le schéma fermé des agrégats (garde 12) n'ont aucun champ pour le rapport « à part ».
- **Second dépôt.** La liste « Après la course, dans cet ordre », l'addendum B et le manifeste ne le nomment pas.
- **Nœuds 13 et 14.** Ils ne sont pas portés à la table « Nœuds tranchés ». La contre-lecture 6, M2, dit toujours « nœud 14 ouvert » : c'est de l'historique, laissé tel.
- **Auteur.** Le brouillon 15 est demandé par la session de l'attaquant informé, alors que D8 tient l'auteur de ce texte pour distinct de l'attaquant informé. C'est au directeur d'en juger.
- **Réserve 9.** Elle dit « les six conditions de D6 » ; D6 en résume douze.
- **Commentaire de la copie.** Il écrit « ⟦C1⟧ à ⟦C2⟧ » là où la demande dit « ⟦C1⟧ et ⟦C2⟧ ».
- **Erratum 1.** Aucun de ses points ne touche la section 6 de l'additif.

## Réserves

1. **Ancres.** Elles sont recopiées à vue. Si le brouillon 14 porte des espaces insécables ou des apostrophes courbes que je vois comme ordinaires, le programme refusera toute la liste. Les ancres 7, 10 et 18 sont les plus exposées.
2. **GO-2026-11-21-85.** Il est cité d'après la demande seule, non lu au registre. Je ne lui ai donné aucun repère dans la table, faute de ligne et d'empreinte.
3. **Point 7.** Il n'est pas strictement mot pour mot : j'ai rempli `[chemin]` et `[empreinte]` par les valeurs des balises et retiré « à remplir au scellement ». Si le mot pour mot strict est voulu, il faut rétablir la parenthèse d'origine.
4. **Point 6, périmètre.** J'ai marqué les seuls champs à marqueur dont le lien est écrit dans le texte : n° 1 et n° 2 (configuration du calage) et n° 13 (« Ligne de devis », lien moins sûr).
   - Je n'ai pas marqué les n° 14 et n° 19, faute de lien écrit.
   - Les n° 8 et n° 15 sont des champs d'addendum, sans marqueur du gabarit.
   - Aucun champ à marqueur ne nomme la banque des tâches de réserve ni le calcul de puissance R-7.
5. **Contrôles hors gabarit.** La phrase est celle de la demande. Je n'ai écrit ni où ils sont rapportés, ni comment ils se réunissent aux réponses des lecteurs.
6. **Objet du second dépôt.** Il est dit par renvoi au nœud 13, sans rien ajouter.
7. **Empreintes.** Je n'en ai recalculé aucune. Celle du brouillon 14 vient du commentaire de la copie servie.

FIN DE LA RÉPONSE
