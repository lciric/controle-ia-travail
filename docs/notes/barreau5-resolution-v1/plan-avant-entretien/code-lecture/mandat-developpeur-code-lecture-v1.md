# Mandat du développeur du code de lecture (barreau 5, plan « sabotage ou empreinte ») — v1

Écrit par la mère (`session_01XJ6Mgr8BN6UanALsQatc5E`) le 20 novembre 2026 vers 00:05Z. Pièce de travail. Destinataire : un développeur neuf, Claude Opus 5.5. C'est une pièce d'instrument : la contre-lecture sera faite par un autre modèle (Fable 5.2), puis la vérification des corrections par le même contre-lecteur.

---

Le texte du plan est scellé :
- texte : `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1.md` (`bdff244f1377e795b84f71518bb5e58fb1600fff8afee383d8f70c10d3f5d935`) ;
- devis : `docs/notes/barreau5-resolution-v1/plan-avant-entretien/devis-adaptateurs-tenus-a-l-ecart-v1.md` (`dc886195…`).

Le code de formation est en dernière vérification et part au plus tôt. **Le chemin critique du verdict est maintenant le code de lecture** (section « Calendrier et chemin critique ») : il doit être figé (`CODE-LECTURE-B5F`) à la fin de la formation, soit vers H + 30 heures après un départ que l'on vise le 20 ou le 21. Tu l'écris.

## Ce que tu écris
Dans le paquet `src/controle_ia/barreau5_familles/`, noms neufs (R12), selon la section « Code neuf » du texte :
1. **`relecture_v1`** et **`scripts/lancer_b5f_lecture_v1.sh`** : le point 8 du plan d'analyse.
   - État imposé pour un adaptateur nommé, sur la forme de `t07bbis/etat_impose_v1`, sans le modifier.
   - Chemin éprouvé (cas sain, artefact).
   - Série du modèle nu relue par le même chemin forcé.
   - Divergence, norme, déplacement moyen δ̄, direction ĝ tirée des saboteurs d'apprentissage, produits P de toutes les paires et poussées le long de ĝ (couche 15).
   - Écriture des activations selon « Données gardées », avec ses replis.
   - Ce que reçoit l'instance de lecture : point 7, deuxième tiret. Elle ne reçoit ni la table, ni la branche de la formation, ni un coût d'un adaptateur tenu à l'écart.
2. **`sondes_v1`** : les points 9 et 10.
   - Sondes décisive, de comparaison et du diagnostic, et couches 7 et 23.
   - Même calcul que `t07bbis/apprentissage_carte_v1`, importé sans modification.
   - Contrôle carte-processeur. Une sonde en échec rend ses épreuves « non calculables ».
   - **Notation fermée**, par action et par jeton. Aucune statistique d'adaptateur tirée d'un score de sonde, aucune aire, aucun résumé sur l'instance ni dans ses journaux. Seuls les produits P et les poussées, qui ne lisent aucun score, y sont calculés.
3. **`lecture_v1`** : les points 12 et 13, au processeur seulement.
   - L'ordre est (a) à (h) : garde d'ouverture, vérification de manipulation, séparation apprise, épreuves E3, E2a, E2b et E1, diagnostic, descriptifs, issue, phrases, audit de symétrie, résultat scellé.
   - Mises à l'échelle après coup de E2a et de E2b (« Métrique »). Le maximum sur les jetons d'un score mis à l'échelle n'est calculé qu'ici.
   - Dénombrement exact des rangs signés (« Seuil »). Issues et phrases selon « Critères de lecture gelés » et « Ce que dira chaque issue au jury ». Règle du nœud 6 sous huit familles.
   - Le programme doit pouvoir être joué tel quel, au même fichier et à la même empreinte, sur des fichiers fabriqués (point 11). Écris et documente ces interfaces d'entrée : scores par action et par jeton, déplacements moyens, coûts, étiquettes, lignes de registre.
4. **Le point 18** : la répétition générale et les points d'ancrage sur les quatre adaptateurs existants (`GO-2026-11-19-88`, point 5), en mode descriptif. Ils sont accordés si le code est prêt à temps ; sinon, la répétition se fait sur le modèle jouet. Prévois les deux modes.

## Ce que tu n'écris pas
- **La fabrique des mondes de l'épreuve à vérité plantée** (`epreuve_verite_plantee_v1`). Le point 11 veut que les mondes soient tirés par un agent qui n'a pas écrit le programme. Tu fournis les interfaces ; un autre agent écrira la fabrique.
- **La seconde programmation du dénombrement exact et de la table des issues** : elle revient à l'autre modèle (point 11). Écris la tienne comme si elle devait être recoupée à l'exact.
- Rien du code de formation : `edition_cout_v1`, `formation_v1`, `engagement_v1` et leurs scripts sont en dernière vérification. Tu les lis pour les conventions (gardes `GardeArret`, lecture du registre propre, liste blanche, manifeste). Tu ne les modifies pas. Si ton code exige d'eux un changement, dis-le dans ton rapport.

## Épreuves (R5 : chaque garde avec son cas sain et son artefact)
Celles de « Code neuf » qui touchent la lecture :
- moyenne sur les jetons : refus ;
- table des étiquettes dans l'arbre de lecture : refus ;
- engagement postérieur : refus ;
- dénombrement exact contre l'énumération complète pour huit, neuf et dix familles ;
- différences nulles et égales ;
- famille sans sur-saboteur ;
- jouet de bout en bout.

Ajoute :
- les gardes de l'ouverture (point 12 a) ;
- l'identité à dose 0 et l'artefact à dose 1 de chaque adaptateur ;
- les refus du cas V7 du point 11 (les quatre premiers).

Fais aussi un passage de mutations : des défauts réintroduits un à un, comptés attrapés sur joués, sans mutation équivalente cachée.

## Règles
- **Aucune donnée.** Tout se fait sur le modèle jouet (`controle_ia.harnais.modeles.modele_jouet`, `tokeniseur_caracteres_chat`, comme les essais du code de formation) et sur des fichiers fabriqués.
  - Aucun accès à la branche de la formation ni à ses journaux de coût.
  - Aucun fichier de `diag/`, aucun score, aucune activation réelle, aucune transcription.
  - Aucun résultat de 7a, 7b, T0.6, de l'étape B, de l'étape B bis ni de P3-bis. Le code de l'étape B bis (`t07bbis/`) se lit ; ses sorties, jamais.
  - Un artefact réel que le code doit charger sur l'instance (adaptateur, modèle) se cite par chemin et empreinte. Tu ne l'ouvres pas.
- **Fichiers interdits** : aucun fichier « consigne-privee » ni « conception-ii-b » ; rien sous `/root/.claude/`.
- **Rien de réel** : aucun réseau vers un loueur de cartes ni vers Hugging Face, aucune création d'instance, aucun lancement hors des essais.
- **Écriture** : tes fichiers seulement par les outils d'écriture et d'édition, jamais par une commande. Ne modifie aucun module existant hors de tes fichiers neufs.
- **Essais** :
  - seulement tes fichiers d'essais neufs, et ceux du paquet `barreau5_familles` si tu veux vérifier que rien n'a cassé ; jamais la suite entière du dépôt ;
  - temporaires dans `/dev/shm` (`TMPDIR=/dev/shm`, `--basetemp=/dev/shm/<nom>`), effacés à la fin par chemin écrit en toutes lettres ;
  - environ 15 Go libres sur le volume du dépôt : une seule copie de travail à la fois, sous le bloc-notes.
- **Garde du dépôt** : n'écris dans aucune commande le nom d'une commande d'arrêt ou de recherche de processus par motif, ni `kill` avec ses options, même dans une recherche ou une boucle d'attente. Pas de code en ligne passé à l'interpréteur (`python -c`, `python -`) : écris un fichier et lance-le par son chemin.
- **Refus d'outil** : au premier refus, arrête-toi et dis-le, sans le contourner.
- Aucun commit, aucune dépense. La mère verse.

## Sorties
- Le code et ses essais (`tests/test_barreau5_familles_relecture_v1.py`, `…_sondes_v1.py`, `…_lecture_v1.py`, `tests/test_lancer_b5f_lecture_v1.py`).
- Le rapport scellé `docs/notes/barreau5-resolution-v1/plan-avant-entretien/code-lecture/rapport-developpeur-code-lecture-v1.md`. Il contient :
  - ce qui est fait, point par point du texte ;
  - les écarts et les questions au texte ;
  - les empreintes de chaque fichier ;
  - la commande des essais et leur compte ;
  - les mutations.
- Tes outils et sorties dans `code-lecture/outils-developpeur-code-lecture-v1/`.
- Commande de scellement : `cd /home/user/controle-ia-travail && PYTHONPATH=src .venv/bin/python -B -m controle_ia.scellement sceller <fichier>`.
- **Écris au fil de l'eau**, par morceaux. La mère verse les états intermédiaires pour ne rien perdre.

## Rends
1. La phrase exacte de ton invite système qui nomme ton modèle.
2. Les chemins et les empreintes de tes fichiers.
3. Dix lignes au plus :
   - ce qui est fait ;
   - ce qui manque ;
   - les essais et les mutations ;
   - les questions au texte ;
   - ce qui menace un gel à H + 30 heures.
