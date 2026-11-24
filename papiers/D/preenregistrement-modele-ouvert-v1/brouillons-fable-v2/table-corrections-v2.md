# Table des corrections — préenregistrement et devis du modèle ouvert, v1 → v2

Rapport traité : `papiers/D/preenregistrement-modele-ouvert-v1/contre-lectures/contre-lecture-prereg-devis-modele-ouvert-v1.md`, SHA-256 `22f0fd697697c29998eaf20b933ab3429286ce849ac87aac7958fb95956f22e3`. Écrite par Claude Fable 5.2 le 24 novembre 2026. « P » : `preenregistrement-modele-ouvert-v2.md` ; « S » : `specification-instruments-v1.md` ; « D » : `devis-modele-ouvert-v2.md`. Aucun point n'est refusé ; trois sont corrigés autrement que proposé, et un reste ouvert par nature (ligne 1).

## Préenregistrement

| N° | Gravité | Correction | Endroit |
|---|---|---|---|
| 1 | bloquant | La consigne, l'invite du juge, le lexique et les phrases d'aveu sont écrits verbatim ; mutation, détecteurs, cas plantés, harnais, amorçage, sondes sont spécifiés sans choix libre. Licence et comptes d'EvalPlus cités. Décisions de Lazar inscrites comme décisions ouvertes O1 à O6, chacune avec repli ; moniteur d'audit de repli nommé. **Reste ouvert** : les programmes n'existent pas encore ; leurs empreintes et les références des GO sont inscrites au scellement, qui est interdit tant qu'une ligne manque | P, en-tête, « Décisions ouvertes », liste d'arrêt 1 ; S entière |
| 2 | bloquant | Script `fiche_calc` spécifié, déterministe, scellé avec le texte. Les cinq choix sont fixés : γ choisi avant le pilote, qui court à ce γ ; graines du pilote mises en commun par concaténation ; puissance calculée exactement sous loi normale, contrôlée par 200 000 tirages à clé fixée ; borne haute à 80 % par le khi-deux à 3 degrés de liberté ; mise à jour simultanée de la loi factorisée. L'additif ne recopie que la sortie et son empreinte. Script de lecture spécifié, scellé avant l'étage 2 | S (a), (b) ; P « Fiche de prédictions », « Plan d'analyse » |
| 3 | majeur | Deux bornes, par strate et par épisode ; une prédiction n'existe que si elles ont le même signe et valent chacune au moins 60 ; τ rapporté pour les deux | S a.3 à a.5 ; P « Prédiction » |
| 4 | majeur | n de 8 à 12. Famille secondaire fixée par la fiche avant l'étage 2 (H3 ; les deux comparaisons si elles ont une prédiction ; H2 si lancée). « Non concluant » déclaré issue attendue | P « Règles de la fiche », « Tests » ; S a.5, a.9 |
| 5 | majeur | Table unique ordonnée, la première ligne vérifiée l'emporte ; seuils propres à H3 (0,03 et bande ±0,03) ; « ne monte pas » défini pour H2 ; « significatif » défini (Holm pour la famille secondaire) ; τ descriptif, rapporté à la différence de la fiche | P « Critères de lecture gelés » ; S b.3 à b.5 |
| 6 | majeur | La sonde n'écarte plus aucune graine : H3 « non évaluable » pour la graine. La part de triche c* vaut pour les deux doses ; sans amorçage (c* = 0), ni dose forte ni H2 | P « Seuil », « Dispositif » ; S b.1, (g), (h) |
| 7 | majeur | Mutation vers une valeur lointaine (plus mille au moins), sorties booléennes exclues ; négatifs naturels du modèle de base et règle d'exclusion ; assertion mutée hors exemples de la docstring ; harnais à témoin d'exécution, éprouvé sur `sys.exit(0)` et objet toujours égal ; champs fixés par type de tâche ; récompense des témoins écrite ; contamination déclarée ; 542 tâches et règle de réduction jusqu'à 0,80 ; dix épisodes pour le critère « neuf sur dix ». **Autrement que proposé** : l'exclusion ne peut précéder le scellement, la génération demandant une carte ; elle se fait à l'étage 1 par règle scellée, et sa liste est empreintée dans la fiche. Le détecteur principal est en outre validé sur 1 000 négatifs frais, distincts de ceux de l'exclusion | S 1.4, (c), d.1 ; P « Dispositif », limites 5 et 7 |
| 8 | majeur | 768 jetons au plus ; « illisible » = sans code extractible, seul cas ; ces épisodes restent au dénominateur, sans réussite ; parts illisible et tronquée rapportées par bras. **Autrement que proposé** : aucun épisode n'est exclu, illisibles compris ; au-delà de 10 % d'illisibles dans un bras, « non évaluable » | S 1.3, b.2, b.5 ; P « Dispositif », « Conditions de lecture » |
| 9 | majeur | Juge dans un processus distinct, sans adaptateur ; garde sur 50 textes fixes avant chaque passe, éprouvée avec un adaptateur actif ; jetons « YES » et « NO », normalisation écrite ; biais d'autopréférence déclaré ; revalidation du lexique par deux lecteurs sur de vrais épisodes, à l'étage 1 avant la fiche et à l'étage 2 avant lecture. **Autrement que proposé** : invites en anglais, langue des tâches, d'où « YES » et « NO » au lieu de « OUI » et « NON » | S (e), (f) ; P « Dispositif », limite 4 |
| 10 | majeur, puis mineur | Trajectoire de la part sans mention préenregistrée comme observable descriptive, comparée à γD et à γDq ; dérive non spécifique nommée comme explication rivale ; verdicts de H2 reformulés en « compatible avec ». P emploie la survie attendue, R une interception tirée : écrit dans la table des bras. Table de correspondance avec la carte dans le texte | P « Hypothèses », table des bras, « Correspondance avec la carte », critères de H2 ; S a.6, b.5 |
| 11 | mineur | H3 dite conjecture, le théorème portant sur un gradient absent ici ; sonde témoin sur un trait sans rapport et réserve « dérive générique » | P H3, « Métrique », critères de H3 ; S (h), b.4 |
| 12 | mineur | 30 pour mille présenté comme une convention | P « Prédiction », dernier alinéa |
| 13 | mineur | Arguments passés explicitement (`max_false`, `max_mention`) ; 1 000 négatifs et quatre faux positifs au plus, soit une borne sous 1 % ; unité du terme de sélection écrite ; graine en `GuardError` « non lue » | P « Seuil », limite 3 ; S d.1, b.5 |
| 14 | mineur | La racine 2026112404 régit tous les tirages ; celle de la chaîne ne sert qu'à son essai à blanc ; clé du tour 0 sans bras ; table des codes entiers | S 0.3 ; P « Graines » |
| 15 | mineur | Décision ouverte O6 ; repli : deux agents neufs de la session, qui ne sont pas des appels d'interface de la chaîne de mesure | P « Décisions ouvertes », liste d'arrêt 8 |

## Devis

| N° | Gravité | Correction | Endroit |
|---|---|---|---|
| 1 | majeur | Plafond de l'étage 1 porté à 86 heures, marge comprise (cas lent recalculé : 68 heures, plus 25 %). Le pilote passe avant tout poste qui ne conditionne pas la fiche ; seul le départ à dose forte est abandonné si le plafond approche ; le pilote n'est jamais réduit ; contrôle du total après la mesure des débits | D § 4 ; S (a), ordre de l'étage 1 |
| 2 | majeur | Hypothèse de débit du bac à sable (5 à 30 épisodes par seconde), comptée sans recouvrement ; recouvrement et nombre de cœurs mesurés à l'étage 1 | D § 2, § 3 |
| 3 | mineur | Supplément du témoin positif supprimé (c'est un départ) ; installation et remplacements de graines comptés dans l'étage 2 ; démonstrations construites par programme, retirées pour chaque graine ; temps fixe ajouté aux postes du modèle de base ; 950 jetons des sondes au § 2 ; épisodes du témoin positif dans le compte ; négatifs naturels et négatifs frais chiffrés à l'étage 1 | D § 2 à § 6 ; `calc/devis_calc_v2.py` |
| 4 | mineur | Affinage abaissé à 1 200 à 5 000 jetons par seconde ; rechargement à chaque phase écrit ; passage à 48 Go renvoyé à un complément de devis | D § 1, § 2 |
| 5 | mineur | Garde de plafond lisant les heures facturées, éprouvée sur un cas sain et deux artefacts | D § 4 ; S (j) |
| 6 | conforme | Le GO consigne prix daté, fournisseur, carte, plafond en euros, disque, lieu des adaptateurs | D § 1 |

## Changements hors rapport

- Faits transmis intégrés : EvalPlus sous Apache 2.0, 164 et 378 tâches aux révisions citées.
- Démonstrations d'amorçage construites par programme (raisonnement honnête du modèle de base, code à cas particulier, phrase d'aveu pour la triche annoncée), et non plus générées sous consigne : l'omission est plantée par construction, le coût sur carte disparaît.
- Répartition des tâches unique et non plus par graine, pour que les exclusions et les détecteurs soient validés une fois (limite 7 de P).
- Contrôle positif : condition de lecture maintenue aux deux étages.
