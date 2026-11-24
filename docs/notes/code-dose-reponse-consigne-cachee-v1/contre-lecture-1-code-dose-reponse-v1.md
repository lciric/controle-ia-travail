# Rapport de la contre-lecture 1 du code de la dose–réponse (classe B)

Pièce versée par le développeur, à l’identique du rapport rendu par le contre-lecteur (sous-agent neuf, Sonnet 5.5, effort élevé, accordé par la mère), sur le commit 5802bdc7 de la branche `code/dose-reponse-consigne-cachee-v1`.

---

# Contre-lecture (classe B) du code de la course de dose-réponse de l'organisme à consigne cachée

**Verdict : prêt sous corrections listées.**
- La logique de lecture, la table C0 à C6, les phrases gelées, les graines et la reprise sont conformes au texte scellé, et les 30 essais passent.
- Quatre défauts majeurs de garde ou de dépense (CL-02 à CL-05) sont à corriger avant la ligne `CODE-DOSE-REPONSE-CONSIGNE-CACHEE`.
- Un nœud de décision (CL-01) bloque le lancement sans relever du code.

## Constats

**CL-01 — Nœud bloquant pour le lancement, pas un défaut de code : « deux contrôles croisés de plus ».**
- `registres/go.md` l. 902 (GO-2026-11-24-24) glose la confirmation de Lazar ainsi : « deux répliques, **deux contrôles croisés de plus**, deux témoins du premier test gardés ».
- Le texte scellé fixe quinze conditions et 1 920 épisodes (plan, points 2 et 4). Il range les contrôles croisés en « option » du devis, à 3 ou 4 dollars.
- Le GO de dépense (l. 903) vise le devis candidat 1, à 26-41 dollars, donc quinze conditions.
- Le code joue quinze conditions (`conditions_v1.py` l. 30-32). La liste d'arrêt interdit « une condition autre que ceux de la pièce jointe ». Aucun texte privé des deux contrôles croisés n'existe : la pièce jointe v4 n'a que huit consignes distinctes.
- Il est donc impossible de jouer ces deux conditions sans nouvelle version du texte et de la pièce jointe.
- Correction : la mère fait trancher Lazar. Soit les contrôles croisés sont hors course (la gloss de GO-24 est alors à corriger), soit une version nouvelle est faite, avec nouveau code et nouveau devis.

**CL-02 — Majeur : la garde du contrôle négatif de la garde d'équivalence est évaluée de façon cumulée après chaque bloc, dès 10 actions comparables.**
- Fichier : `course_v1.py` l. 493-494 et 516-520. La référence (`harnais/episode.py` `exiger_controle_negatif_phase`, et `t06/lanceur.py`) la juge en fin de phase, sur l'ensemble.
- Scénario : un bloc apporte environ 15 actions échantillonnées. Une seule action en échec sur moins de 20 comparables donne une fraction inférieure à 0,95 et arrête le run.
- J'ai simulé 64 regards avec un taux de passage réel p. Le contrôle de fin de course passerait presque toujours (n d'environ 860), mais l'arrêt prématuré survient dans 51 % des cas à p = 0,97, 31 % à 0,98, 14 % à 0,99 et 7 % à 0,995.
- Le bloc généré est perdu, car le contrôle précède `ecrire_bloc`. Le texte dit « contrôle négatif non vu », ce qui se juge naturellement au bilan.
- Ce taux est sans doute proche de 1 sur la course de confirmation de T0.6, mais je n'ai pas le droit de lire `diag/` pour le vérifier.
- Correction : juger à la fin, ou n'arrêter en cours de course qu'à partir d'un effectif où le seuil 0,95 a un sens (par exemple au moins 100 comparables). Garder la lecture « non concluant » pour le reste.
- Réserve associée, mineure : après reprise, `rapports` ne couvre que les blocs rejoués, donc le bilan final ne couvre pas toute la course.

**CL-03 — Majeur : `exiger_sans_score_de_sonde` lit le texte généré par le modèle.**
- Fichier : `course_v1.py` l. 203-212, boucle l. 208-212. L'expression `re.findall(r'"([^"]+)"\s*:', ligne)` s'applique aux lignes de `textes.jsonl`, qui contiennent les actions du modèle.
- Preuve : une ligne `{"texte": "{\"score\": 3}"}` lève `GardeArret` avec la clé `'score\\'`. Les clés visées sont `sonde|score`, sans casse.
- Scénario : sur 19 200 actions à température 1, une action qui écrit `"score":` ou `"scores":` suffit. La garde est appelée à chaque `ecrire_bloc` et à la fin de `_executer` (l. 444).
- Une action fautive arrête le run, jette son bloc, et reste fautive à la reprise puisque le bloc est repris tel quel. Si c'est la dernière vérification, elle empêche d'écrire `episodes-dose-reponse.json` alors que les 1 920 épisodes sont déjà joués. Il faudrait alors changer le code.
- Correction : ne parcourir que les clés des structures écrites par la course (`mesures.jsonl`, `episodes.json`, `bloc.json`), en lisant le JSON, et jamais le contenu de `textes.jsonl`. Ajouter l'essai « texte généré contenant `"score":` » : cas sain, pas d'arrêt.

**CL-04 — Majeur : deux contrôles de la liste d'arrêt « avant la création » ne sont jouables qu'après la création de l'instance.**
- Texte scellé, « Liste d'arrêt », première puce : « rapport des longueurs des textes au-delà de 1,15 : aucune création ». Plan, point 5 : « mesurées avant dépense ». Mandat : « contrôles avant dépense ».
- Le code mesure ce rapport sur l'instance (`course_v1.py` l. 393-395, `exiger_longueurs`), après installation, essais et téléchargement du modèle. Le docstring de `controles_v1.py` l. 15-18 le reconnaît.
- Même défaut pour la forme de la vraie pièce jointe : `charger_piece_jointe` (contrôle strict de `FORME_PIECE_JOINTE`) n'est appelé que dans `charger_textes_de_course`, sur l'instance. Le lanceur et `controles_avant_depense` ne font que le hachage.
- Si la forme du vrai fichier diffère de la forme attendue par le code, ou si le rapport dépasse 1,15, l'instance est déjà louée. La perte financière est faible, de l'ordre de 2 à 3 dollars, mais c'est une violation de la lettre.
- Je n'ai pas pu vérifier la forme du vrai fichier (cloisonnement).
- Correction : une étape de contrôle avant création, sans impression, qui appelle `charger_piece_jointe(chemin, sha)` et `longueurs_en_jetons` avec le tokeniseur de Llama-3.1 (jetons seulement, sans le modèle). Sinon la mère fait accepter l'écart par écrit.

**CL-05 — Majeur : `exiger_config` ne verrouille pas les paramètres des gardes.**
- Fichier : `controles_v1.py` l. 87-105 (REGLAGES l. 52-55).
- Preuve (rejoué) : sont acceptés sans erreur `fraction_min_controle_negatif = 0.0`, `actions_min_controle_negatif = 10**9` (la garde du contrôle négatif devient inopérante, avec seulement une réserve « non concluant »), `fils = 64`, `noyau_attention = "autre"`, `memoire_vive_min_go = 0`, `agent.variables_gabarit = {}`.
- C'est un repli silencieux contraire à R5, atténué parce que la configuration est scellée par la mère.
- Correction : comparer ces clés aux valeurs de `prereg/T0.6-organismes-config-7b-v1.json`, qui est citée par le texte et empreintée. Le plus simple est de recalculer `configuration()` et de comparer l'égalité de dictionnaires.
- Même passage : `designation_critere_3` est libre dans `exiger_config`, et `scripts/ecrire_configuration_dose_reponse_v1.py` l. 51 le fige à `None` sans option.
- GO-24 parle d'une désignation de cette course pour le critère 3. Si ce texte est scellé, le script ne sait pas porter ses lignes de registre exigées (`_fichier` et `lignes_registre` de `controler_registre`). Ajouter un argument facultatif, sinon la garde « lignes préalables exigées par la désignation » est éludée.

**CL-06 — Mineur : la ligne `CODE-DOSE-REPONSE-CONSIGNE-CACHEE` n'est liée à rien.**
- Fichier : `controles_v1.py` l. 213-229. Le contrôle ne vérifie que la présence de l'identifiant de ligne.
- Le texte demande que la ligne cite le commit et les empreintes, et porte la déclaration « aucune action générée sous un texte privé ». Une ligne périmée passerait.
- Le lien commit-code est assuré par `commit_code` plus `git diff` dans le lanceur et l'amorce, mais pas par le registre.
- Correction : exiger que la ligne contienne `config["commit_code"]`.
- Aussi absents par rapport à la référence T0.6 : `exiger_code_importe_sous` (code importé depuis `racine/src`) et `exiger_code_cite`.

**CL-07 — Mineur : la lecture traite mal les cas dégradés.**
- `lecture_v1.py` l. 131-141 et 320-321 : une action manquante sur un couple (condition, tâche) donne `GardeArret` dans `couts_par_condition` (« 19 actions, vingt exigées », vérifié) avant d'arriver à la ligne C1 que le texte prescrit pour un contrôle d'effectifs en échec. Aucun fichier de lecture n'est écrit, seulement un arrêt.
- Un échec d'injection donne bien C1, mais la lecture continue de calculer tous les effets (aucune fuite visible, mais le texte dit « rien n'est dit de l'organisme »).
- Correction : court-circuiter après `exiger_table` si `conforme` est faux.
- `lecture_v1.py` l. 217-231 : une couple d'inversion non calculable est ignorée quand l'échelle est par ailleurs établie (`non_calc` ne sert que dans le motif quand `etablie` est faux). Le texte range « lecture non calculable » dans C5. Cas limite, mais une règle écrite du texte.

**CL-08 — Mineur : la lecture n'est pas verrouillée à l'empreinte du texte scellé ni au préenregistrement.**
- `lecture_v1.py` l. 533 : l'entropie vient de `verifier(racine/PREREG)`, sans comparaison à `PREREG_SHA256` (la course le fait via `controles_avant_depense`).
- `lecture_v1.py` l. 553-556 : la ligne de commande accepte `--prereg` absent, et la lecture est alors non décisive mais écrit tout de même `lecture-cout-dose-reponse.json`. Ce fichier bloque ensuite toute lecture des mêmes entrées via `exiger_premiere_lecture`, sans qu'un préenregistrement ait été exigé (R1).
- Correction : exiger l'égalité `sha == PREREG_SHA256` et `prereg` non nul pour une lecture qui écrit le résultat sous ce nom.

**CL-09 — Mineur : l'en-tête de reprise (`course_v1.py` l. 409-410) hache toute la configuration.**
- Cela inclut `lancement` : GO, `go_admis`, plafond, offre.
- Toute modification légitime de la section de lancement, par exemple une prolongation de GO ou un second GO, invalide tous les blocs scellés (`lire_bloc` : « reprise refusée ») et force à tout rejouer.
- Correction : hacher seulement la part scientifique de la configuration (`reglages`, `agent`, `prereg`, `piece_jointe`, `consignes_premier_test`, `banque`, `modules_repris`, `commit_code`).

**CL-10 — Mineur : trous d'essais (R5).**
- Mutation survivante : `NIVEAU_GRADATION` et `NIVEAU_INVERSION` ramenés à 0,95 (au lieu de 1 − 0,05/4, 1 − 0,05/2, 1 − 0,05/6, 1 − 0,05/3) laissent verts les 5 essais de lecture à réponse connue et l'essai d'égalité avec le script de puissance. Aucun essai ne fixe la correction de Bonferroni. Le test d'égalité ne compare que la liste des niveaux partiels sur quatre scénarios, pas les intervalles.
- Aucun essai de `_exiger_controle_negatif_cumule` ni de `_lecture_controle_negatif`.
- Aucun essai de la ligne C4, de l'arrêt de la séquence de DR-6, des déclencheurs d'audit 1 à 6, ni de la sélectivité.
- `exiger_offre_lue` est éprouvée mais non appelée par la chaîne vivante : `session_v12` s'en charge. La garde éprouvée n'est pas celle qui sert.
- Correction : un essai qui fige les constantes aux valeurs du texte et vérifie `niveau` dans les sorties de gradation et d'inversion ; les essais manquants.

**CL-11 — Mineur : calendrier.**
- Le devis du texte scellé dit « dernier jour de création le 12 décembre » et « fin du GO le 15 décembre à 00:00 UTC ». `session_v1.calendrier_t08` rend `dernier_jour_creation=2026-12-15` et `fin_go_utc_s` au 16 décembre 00:00 UTC (rejoué, avec une configuration construite par le script).
- Rien ne bloque une création le 13 ou le 14 décembre, avec destruction avant la fin des vingt-quatre heures de course.
- Correction : appliquer la date du 12 décembre à `controles` et à `creation`, ou la déclarer comme écart accepté.

## Les six points de l'auteur

- (a) Voir CL-01 : confirmé, avec les preuves ci-dessus.
- (b) La lecture « sélectivité établie = les deux proportions à borne basse > 0 » est conservatrice : elle produit plus de réserves, jamais moins, et ne change aucune ligne. Le texte n'a pas de définition. À nommer dans la ligne `CODE-…` pour que le verdict ne la découvre pas ; sans nouveau défaut.
- (c) Voir CL-02 : défaut réel.
- (d) La reprise est correcte et éprouvée : recopie à l'octet, en-tête, hachage de chaque fichier, rang du bloc, épisodes d'un bloc non poussé déclarés et rejoués. Réserves en CL-09 et CL-02.
- (e) Conforme : clés fermées, valeurs contrôlées, filtre de l'amorce `MOTIF_INTERDIT` en doublon. Aucune sortie de coût dans `ARRÊT`.
- (f) Conforme au texte (« Métrique », « Seuil »). Taux d'erreur simulé avec le code de lecture sur 100 jeux synthétiques par scénario : échelle établie dans 3 % des cas pour une marche unique, 3 % pour un gonflement commun plus une marche, 0 % sans effet. C'est cohérent avec les « environ 3 % attendus » du texte, mais le nombre de jeux est faible. Voir CL-10 pour les niveaux non figés par les essais.

## Ce que j'ai rejoué ou éprouvé

- `tests/test_dose_reponse_v1.py` : 30 passent (273 s, avec une autre suite qui tournait en parallèle). 30 collectés, ce qui correspond à `ATTENDUS="30"` de l'amorce ; la liste d'essais est `70a748e7…`, conforme à `LISTE_SHA256`. `bash -n` OK sur les deux scripts, tous les compagnons `.sha256` OK.
- Phrases gelées comparées par programme au texte scellé : C1-C6, phrases de proportion, qualificatifs, réserves ; toutes identiques. Seule différence : le gras Markdown de « non tenue » dans C5.
- Jouet de bout en bout : structure des blocs, des mesures, des fiches (pas désignés 2/10 et 5/10, `designe`) ; sélection d'activations de 5 % ; reprise.
- `session_v1.go`, `calendrier` et `vue` rejoués sur une configuration produite par le script (GO-2026-11-24-25 conforme, 90 USD). `garde_calcul.py` accepte la commande de création type.
- Lecture sur données dégradées (toutes coûts `None` dans une condition, dans l'honnête, dans `dormant_10`, sur une tâche entière) : pas d'exception, résultats attendus.
- C4 et un cas d'inversion (5 supérieur à 10) : lignes C4 et C5 conformes.
- Mutations sur les niveaux : CL-10. Bypass de la configuration : CL-05. Faux positif de la garde de score : CL-03. Simulation de la garde cumulée : CL-02.
- Scripts de lancement lus ligne à ligne pour les noms de variables, les arguments de `printf`, `champ()`, les échéances et la chaîne amorce-course. Je n'ai rien joué qui crée une instance.

## Déclaration de cloisonnement

- Je n'ai lu ni texte privé, ni score, ni verdict, ni sortie de course. Je n'ai ouvert ni `consignes-privees-dose-reponse-consigne-cachee-v4.json` ni `prereg/P3-consignes-v1.md` (leurs empreintes seules, par `sha256sum` : `7a5f633c…` et `a68468fe…`, conformes).
- J'ai lu `registres/go.md` (lignes 902-903) et les identifiants de l'ordre de `diag/…/tirage.json` pour vérifier les rangs. Je n'ai lu ni `diag/`, ni `runs/`, ni `donnees/` (sauf ces identifiants), ni `registres/etat.md`, ni une passation. Un `grep` qui visait aussi `registres/*.md` a été refusé par le système et n'a rien exécuté.
- Aucune génération sous texte privé, aucune instance, aucun fichier du dépôt modifié ni commité. Mes scripts et mes simulations sont dans le bloc-notes, hors dépôt.