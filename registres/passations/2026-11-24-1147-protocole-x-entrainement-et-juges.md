# Passation — session du protocole X « faut-il aborder l'entraînement ; juges boîte noire qui n'alertent pas » (2026-11-24, 11:47 UTC)

Classe C. Session `session_01Qi7Gr31b1s4znXx53GF1ik` (Claude Fable 5.2, effort maximal), fille de la mère `session_01Qi7Gr3Ggccg85kjmP654WC`. Branche `protocole-x/entrainement-et-juges-v1`, demande de fusion en brouillon n° 102. Tout est dans `docs/notes/protocole-x-entrainement-et-juges-v1/`. Session exposée à des résultats de la base boîte noire par action : exclue de toute conception de moniteur, de sonde ou de saboteur (`inscription-qui-a-lu-quoi-v3.md`).

## Fait

1. **Reformulation en quatre points** des deux demandes de Lazar (`demandes-reformulees-quatre-points-v1.md`, `2fa3765f…`), sur deux dossiers de faits relus à la page (`dossier-faits-demande-1-v1.md`, `a6507835…`, et son erratum 1 ; `dossier-faits-demande-2-v1.md`, `a31e8b4d…`, cloisonné).
2. **Réponses de Fable** : demande 1 (`reponse-fable-demande-1-v1.md`, `cc167c06…`) ; demande 2 (`reponse-fable-demande-2-v1.md`, `192eca94…`, et son erratum 1 qui prime ; cloisonnées).
3. **Carbon**, par la garde commune (script `appel_carbon_protocole_x_v3.py`, contre-lu, 50 essais de gardes) : demande 1 rendue (`reponse-carbon-demande-1-v1.md`, `aa55515e…`) et comparée (`comparaison-fable-carbon-demande-1-v1.md`, `c596b02c…`) ; demande 2 : **appel coupé avant tout en-tête, panne technique, aucune réponse** (`journal-appel-carbon-demande-2-v1.txt`, verrou gardé).
4. **Collisionneur** : faits et questions neutres, test de neutralité à l'aveugle (admis, scores de 0,20 à 0,30), devis en troisième version, contre-lu et vérifié (`devis-collisionneur-entrainement-et-juges-v3.md`, `2249c61b…`). **Envoyé à la mère à 11:43 UTC ; rien n'est lancé.**
5. **Notes de fin de dossier pour Lazar**, Markdown et PDF : `note-fin-de-dossier-demande-1-entrainement-v1` (`b8fcfff6…`, PDF `bf39a537…`) ; `note-fin-de-dossier-demande-2-juges-v1` (`d89d7b06…`, PDF `122f6a16…`), cloisonnée, **à une seule voix** tant que Carbon n'a pas répondu.

## Dépenses (lignes à verser par la mère)

- `GO-2026-11-24-16`, appel à Carbon de la demande 1, 11:17:24Z à 11:29:17Z : 5 186 jetons en entrée, 8 853 de texte, 30 274 de réflexion, fin normale ; **1,67 USD** au tarif haut (8,3 / 41,5 USD par million).
- `GO-2026-11-24-16`, appel à Carbon de la demande 2, 11:21:25Z : coupé à 11:26:26Z avant tout en-tête (`RemoteDisconnected`) ; **coût inconnu, de 0 à 2,78 USD**, à compter au pire tant que la facture ne le dit pas. Faux échec, cause réseau ; issue proposée au registre des idées : « non évaluable ».
- Collisionneur : 0. Aucune instance de calcul ouverte par cette session.

## En attente d'un mot

1. **Relance de l'appel à Carbon sur la demande 2** (demandée à la mère à 11:30 UTC) : même réglage, 2,78 USD de plus au pire ; compté au pire, la demande dépasserait son plafond de 3 USD et l'accord de 6 USD. Le verrou du script refuse toute relance sans décision nommée. Commande, une fois le verrou levé par décision : `python appel_carbon_protocole_x_v3.py DOSSIER 2 --envoyer GO-… ba44084a…` (empreinte entière au journal).
2. **Arbitrage du devis du collisionneur** par la mère : un ou deux dossiers, part de la clé Anthropic partagée, identifiant d'accord, ligne de 18 ou de 21 USD. Le dossier 2 seulement sur le mot de Lazar.

## Reste, selon ces mots

- Si la relance de Carbon est accordée : la lancer, comparer, écrire la deuxième version de la note sur les juges (Markdown et PDF).
- Si le collisionneur est accordé : le lancer selon le devis, rendre sa note de sortie obligatoire (rédacteur : un sous-agent Opus 5.5), verser ses propositions dans une deuxième version de la note.
- Service à l'organisme d'idéation : sous-questions écrites (`sous-question-organisme-demande-1-v2.md`, `-2-v2.md`), non servies ; à la mère.

## Décisions à porter à Lazar (détail et format dans les deux notes)

- Demande 1 : trancher le réapprentissage des sondes seules sur la part d'épisodes audités (nœud laissé ouvert le 21 novembre) ; devis des témoins bénins, avant ou après la porte de fin décembre ; épreuve de tenue des saboteurs à un entraînement sans contenu, après la porte ; bras déclaré « lire ce qu'un entraînement a laissé » : pas maintenant ; recherche d'antériorité par un lecteur non exposé (défaut sous 48 heures : la mère la lance).
- Demande 2 : la phrase du dossier de la porte sur les juges génériques ; sept contrôles sans carte par un lecteur habilité ; le principe des épreuves d'admission des juges (nœud).

## Réserves

- Les réponses de Fable et les notes sont des pièces de travail, non contre-lues.
- Les coûts des formes d'entraînement sont des ordres de grandeur, sans mesure. Quatre requêtes d'antériorité seulement.
- Gasteiger et al. reste repris d'une lecture antérieure, non relu.
- Deux pièces scellées portent une heure d'en-tête approchée, en avance d'une quinzaine de minutes sur l'heure réelle (`dossier-faits-demande-1-v1-erratum-1.md`, `comparaison-fable-carbon-demande-1-v1.md`) ; l'heure des commits fait foi.
- Les pièces de la demande 2 portent des chiffres du verdict : aucun versement à la branche principale ni à un concepteur sans relecture de cloisonnement (liste dans l'inscription v3).

## Trouvailles de côté, pour la mère

- À confier à une session non exposée : le protocole de dose du saboteur à consigne cachée fixe-t-il ses consignes sans regarder l'oracle ; le bras d'attaque passe-t-il un gradient à travers la sonde.
- Citation à instruire pour la décision sur le plancher d'audit : les notes de Greenblatt du 24 mars 2025 (entraînement en ligne sur des actions tirées au hasard après exécution).
- Soopal et al., relu : un témoin bénin apparié ne répare le défaut des sondes que dans une même course d'entraînement (pages 6 et 8).
- Routine de reprise, constats antérieurs à cette session sur la branche principale : dix écarts à `verifier-arbre` (compagnons mal nommés ou absents sous `registres/passations/`, un dossier de course de collisionneur, deux dossiers de notes) ; un essai en échec (`tests/test_cibles_invisibles_v4.py::test_aucun_module_hors_mesures_ne_lit_la_cle_cibles`, qui signale deux modules de `controle_ia/t08/` ; probable faux positif, non instruit).

## Rappels datés

Échu ce jour vers 18 h (Paris) : remettre à Lazar la lecture des trois sources du jugement du papier contre la surveillance (la note sur le papier n'est pas à remettre le 24). La note de fin de dossier de la demande 1 la complète.

## Instances actives

Aucune. Aucun processus en fond : les deux appels à Carbon sont finis.

## Prochaine action

Attendre le mot de la mère sur la relance de Carbon et sur le devis ; à sa réception, agir selon « Reste ». Sans mot, rien ne part.
