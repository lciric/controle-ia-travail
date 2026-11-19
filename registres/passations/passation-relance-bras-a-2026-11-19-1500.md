# Passation — relance du bras A des organismes discrets — 2026-11-19, 15:00Z

Session sortante : la session de relance de l'organisme d'idéation sur les organismes discrets (compte actuel), branche `claude/pensive-bardeen-1fv7hw` de `lciric/controle-ia-travail`, demande de fusion brouillon lciric/controle-ia-travail#21. Sommet de la branche à l'écriture : `9490df3a0b7b0ed3e647bdf833e28a73d8d4a5c6`, puis le commit de cette passation.
Motif : mot de Lazar, 2026-11-19 vers 14:58Z, dans la session sortante : « fais la passation sur un autre compte nouvelle session ou fable a des credits ». La limite d'usage de Claude Fable 5.2 est atteinte sur le compte actuel jusqu'au 22 novembre 18:00Z, et la règle « qui conçoit » (R-3735) exige Fable pour toute conception délicate.
Continuité : elle vit dans les fichiers. Le journal `docs/notes/relance-organismes-discrets-v1/journal-relance-organismes-discrets-v1.md` va de OD-001 à OD-143 et fait foi pour l'historique.

## 1. Ce qui est fait (bras A, texte neuf et code)

- **Texte du préenregistrement** : le dernier brouillon est le **brouillon 20**, `prereg/T0.7-organismes-discrets-v-a-v2-brouillon20.md` (b076e3f942d6252883ab5008993cd0fb9d5ac9788171e3c52975b2b38229d697).
  - Rédigé par Opus 5.5 en **recopie seulement**, pendant la limite de Fable.
  - Note du brouillon 20 : 5cba8c8d…, avec 16 points « à trancher » dans sa partie 3.
  - Les brouillons 15 à 19 sont de Fable 5.2. Le brouillon 19 (224aca70…) traite les 26 défauts relevés en codant le code v4.
  - Huit cases de 13.1 restent marquées « À REMPLIR ».
  - Le validateur `problemes()` de `src/controle_ia/prereg.py` rend les deux problèmes attendus : les cases marquées, et la contre-lecture 10 sans ses empreintes.
- **Code de l'instrument et de l'analyse, version 4** : écrit par Fable 5.2, aligné sur le brouillon 17, commit `5031865b`, 237 essais passés.
  - Modules : `src/controle_ia/organismes_discrets/{graines,mesures,analyse,verdicts}_bras_a_v4.py`, `instrument_appariement_v4.py`, `reponses_lecteurs_v4.py`, et le module neuf `permutation_etiquettes_bras_a_v4.py`. Les épreuves de couverture sont en v3.
  - Commande des essais, à lancer seule, jamais la suite entière, car le disque est presque plein :
    `PYTHONPATH=src python -m pytest -q -p no:cacheprovider tests/test_{graines_bras_a,mesures_bras_a,analyse_bras_a,verdicts_bras_a,instrument_appariement,reponses_lecteurs,permutation_etiquettes_bras_a}_v4.py tests/test_epreuves_couverture_bras_a_v3.py`
- **Contre-lecture du code v4** (Opus 5.5 neuf) : `docs/notes/relance-organismes-discrets-v1/contre-lecture-code-v4-bras-a-v1.md` (2a623d38…). Verdict : **engageable après corrections**.
  - **Défaut bloquant B-1** : une valeur p haute absente, alors que l'aire est calculable, fait retomber l'option (b) en option (a) sans arrêt.
  - **Dix défauts à corriger**, C-1 à C-10.
  - **Onze défauts mineurs**.
- **Défauts du texte trouvés en codant** : `defauts-du-texte-trouves-en-codant-v4.md` (be2023ef…).
- **Essai de mesure des lecteurs** : fini, environ 2,0 USD comptés.
  - La règle de choix, scellée (`runs/essai-mesure-lecteurs-bras-a-v1/regle-de-choix-claude-carbon-v1.json`), désigne Opus 5.5 à l'effort moyen et Carbon au budget de réflexion 1 024.
  - Coût projeté des lectures de la course : environ 146 USD pour Opus et 97 USD pour Carbon, à porter au devis de la course.
  - Dossier de l'essai : 5,6 Mo, textes synthétiques seulement. Personne n'a lu les réponses brutes et elles ne doivent pas être lues. La mère le porte sur main.
- **Réponses du développeur habilité**, transmises par la mère (R-3888) et recopiées à la lettre : `reponses-du-developpeur-habilite-noms-comptes-rang-v1.md` (54c8afb3…). Elles décrivent le module `autres_moniteurs_v8.py` (61105129…, commit 18f63f40) : noms rendus en listes fermées, `tirages` = nombre calculé, dénominateur du 1 % = nombre demandé, comptes `null` quand ils ne sont pas connus, dixième champ `rang`, fichier `rangs-par-unite-moniteurs-bras-a.jsonl`, hypothèse de l'échange par paire vérifiée.
- **Pièce de la mère sans interne** : `docs/notes/bras-a-moniteurs-v1/pour-la-relance-lanceur-et-appariement-sans-interne-v1.md` (3bec0ee9…). Elle porte la phrase sur le lanceur, le cloisonnement des scores et la fiche « échange dans chaque paire ».

## 2. Ce qui attend Lazar (posé dans la session sortante ; rien n'est tranché)

| décision | recommandation | défaut |
|---|---|---|
| Schéma de permutation des étiquettes : libre par épisode, ou échange dans chaque paire honnête/dosé de même rang (point 17 du texte ; posé aussi par la mère) | échange dans chaque paire, 0,75 | **aucun** |
| Choix des lecteurs (section 3.4) : Opus 5.5 effort moyen, Carbon budget 1 024 | oui, 0,85 | oui (48 h) |
| Sortie maximale du lecteur Carbon pendant la course : 8 192, ou 4 096 comme à l'essai | 8 192, 0,7 | 8 192 (48 h) |
| Fiche 9 : le 1 % de tirages dégénérés se compte sur les 2 000 demandés (a) ou sur le quotient écrit (b) ; le module v8 compte comme (a) | (a), 0,8 | (a) (48 h) |
| Écart à R9 : entropie propre de la table des identifiants opaques | accepter, 0,7 | **refusé** (48 h) ; « go R9 » suffit |
| Auteur du code v5 pendant la limite de Fable | (b) Opus applique les corrections écrites | (a) attendre Fable (48 h) |

Le dernier point est réglé par le mot de Lazar du 19 novembre vers 14:58Z : la suite passe sur un compte où Fable a des crédits. Le code v5 s'écrit donc avec Fable.
Les questions ont été posées entre 14:00Z et 14:55Z le 19 novembre ; les défauts de 48 heures échoient le 21 novembre vers 14:00 à 15:00Z. La reprise vérifie dans le registre des GO de main (`git show origin/main:registres/go.md`) si la mère a inscrit des réponses.

## 3. Ce qui attend la mère (envoyé le 19 novembre vers 14:55Z, sans réponse à l'écriture)

- **Écart sérieux à corriger dans le module v8** :
  - Sous le motif « plus de 1 % de tirages dégénérés », le module met `valeur_p_pour_la_famille` = 1, `calculable` faux et les valeurs p à `null`. Le moniteur ne peut alors plus « repérer », ce qui contredit GO-2026-11-19-70 (option (b)).
  - Correction demandée : garder la valeur p haute dans la famille, et ne mettre à `null` que la borne haute et ce qui dépend de l'intervalle.
- **Sept points de forme à accorder** :
  - tirages `null` sous deux motifs ;
  - citation v7 contre comportement v8 ;
  - dose ¼ ;
  - état du motif « intervalle impossible faute de deux tâches » ;
  - moniteur appris non ajustable ;
  - liste des valeurs de `motif` ;
  - valeurs de `reglages.permutation` et `reglages.unite_de_la_permutation`.
- **La v8 fait-elle foi à la place de la v7** pour la case du module : il faut son chemin, son empreinte complète, ses essais, et une épreuve par retrait avec sa notice.
- **Règle « un champ de plus ou de moins arrête la lecture »** : proposé de l'appliquer aux listes fermées v8.
- **Restent aussi à la mère** :
  - la lecture du juge d'une autre lignée, 2 560 ou 6 400 ;
  - le renvoi de la base (lecteur habilité, sur la version de la contre-lecture 10) ;
  - le **lanceur de l'étape de discrétion**, pas encore écrit (développeur habilité, contre-lu ensuite par Opus) ;
  - le port du dossier de l'essai sur main.
- La session mère est `session_013QMayjsoZJFBUCqcnvD5h1`, sur le compte actuel. Depuis un autre compte, `send_message` ne l'atteindra probablement pas : passer par Lazar ou par les fichiers de main.

## 4. Prochaine action (dans l'ordre)

1. Routine de reprise R14 (CLAUDE.md) : empreintes, `verifier-arbre`, registres, défauts échus.
2. Lire ce fichier, puis le journal de OD-136 à OD-143, puis la note du brouillon 20 (partie 3, les 16 points « à trancher » ; partie 5, les deux listes pour le code v5) et la contre-lecture du code v4.
3. **Brouillon 21, par un rédacteur Fable 5.2** :
   - trancher ce qui est de la conception parmi les 16 points du brouillon 20, sans changer de règle de jugement ;
   - poser à Lazar, au format de décision, ce qui changerait une règle ;
   - porter les réponses de Lazar et de la mère dès qu'elles arrivent ;
   - écrire une version neuve de la fiche 9 (point 14 du brouillon 20).
4. **Code v5, par un rédacteur Fable 5.2** :
   - corrections de la contre-lecture du code v4 (B-1, C-1 à C-10, mineurs) ;
   - précisions des brouillons 19 et 20 (valeur p absente refusée ; seule la borne haute « non calculable » sous intervalle dégénéré ; même chose en C4 ; blancs de bord à la fermeture du bloc ; nom du fichier de l'étape (m) ; troisième état « pas au-dessus ») ;
   - listes fermées et forme `null` de la v8, champ `rang`, seuil sur le nombre demandé ;
   - schéma de permutation vérifié dans l'analyse (C-8), sans être tranché.
   Ensuite, contre-lecture du code v5 par un agent Opus 5.5 neuf. Quand Fable a écrit, le contre-lecteur est d'un autre modèle (R-3735).
5. Puis : lots, client des lecteurs, lanceur, enchaînement de l'analyse ; devis de la course (cartes, lectures, moniteurs) et lignes de GO ; contre-lecture 10 du texte aux cases remplies ; vérification habilitée ; scellement (R1, R2, R13).

## 5. Contraintes à garder telles quelles

- **Aucun interne de moniteur** : n'ouvrir ni `bases/`, ni `sondes/`, ni `t07*/`, ni rien de T0.8, ni `scripts/mots_et_cout_*`, ni `prereg/T0.6-organismes-v0-v1.md`, ni `docs/notes/bras-a-moniteurs-v1/notice-*`, `contre-lecture-code-*` ou `verification-lots-*`, ni `src/controle_ia/organismes_discrets/bras_a_v2_habilite/`, ni les modules habilités (`autres_moniteurs_v*`). Seules les pièces relues sans interne et transmises par la mère s'ouvrent.
- **Autres interdits** : aucune fiche de l'organisme d'idéation ; aucune référence cachée ni tâche réelle ; personne ne lit les réponses brutes de l'essai de mesure (`runs/essai-mesure-lecteurs-bras-a-v1/**/envois/`).
- **Clés** : lues par leur nom seulement, jamais affichées ni écrites, jamais un préfixe. Aucune clé collée dans une conversation. La clé Claude « Rigaud » est une variable de l'environnement du compte actuel : elle n'existera pas sur l'autre compte, et la file Claude de la course la demandera à Lazar.
- **Envois aux fournisseurs** : aucun nom de personne, identifiant de session ou courriel. Aucun appel payant avant sa ligne de GO de calcul, épreuve comprise.
- **Dépôts** : ne jamais pousser vers `lciric/controle-ia` ; rien vers un dépôt public.
- **Règles de permission** : une règle ne se pose que sur un mot de Lazar tapé dans la session même. Les règles posées dans `.claude/settings.json` (`permissions.allow`, deux commandes exactes déjà jouées) ne valent pas mot pour la session nouvelle. Un refus du classifieur ne se contourne pas.
- **Disque presque plein** : ne jamais lancer la suite entière d'essais ; ajouter `-p no:cacheprovider`.
- **Écriture** : R12, ne jamais écraser ; nouvelle version = nouveau nom ; tout sceller (`PYTHONPATH=src python -m controle_ia.scellement sceller FICHIER`).

## 6. Instances et dépenses

- Aucune instance de calcul ni aucun relais actif lancé par la session sortante. Les relais de l'essai de mesure sont arrêtés et consignés (`registres/arrets.md`, porté sur main par la mère).
- Aucune dépense engagée et non close. Total de l'essai de mesure : environ 2,0 USD comptés sur trois lignes (GO-2026-11-19-34, -35 et la file GPT), plus 1,5e-6 USD pour la vérification de la clé.
- Aucun agent de la session sortante ne reste au travail. Le rédacteur Fable du texte est arrêté par la limite d'usage ; les agents Opus du brouillon 20 et de la contre-lecture du code v4 ont rendu.
