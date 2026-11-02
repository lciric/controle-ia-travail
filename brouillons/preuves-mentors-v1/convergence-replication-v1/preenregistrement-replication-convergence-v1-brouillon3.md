# Préenregistrement — réplication sur graine neuve de la course de convergence des règles de défense (mélange d'équilibre, défense figée, historique) — v1

**Statut** : texte scellé (date à la ligne « Date ») ; issu du brouillon 3, lui-même issu des brouillons 1 (`f0fd07874c6bba5dfb71c845a693749015caaee2b554ae5772c93b2a82dd7c76`) et 2 (`74c66bd38e5288c65128ffddcd08d5ba7442cde9797c8fb7b58308b01ae32a0d`), archivés sans modification ; corrections CL-01 à CL-14 (contre-lecture 1) et CL2-01 à CL2-13 (contre-lecture 2) traitées une à une, puis contre-lecture 3 courte sur les différences du brouillon 2 au brouillon 3 (§ Contre-lecture) ; ni la spécification v2, ni le code v3, ni ses essais, ni l'implémentation B v2 n'ont changé après la contre-lecture 2 ; aucune racine de réplication dérivée avant le scellement, aucune exécution du jeu sur une telle racine.

Pièces d'appui, dans le même dossier : `etat-des-lieux-v1.md`, `specification-statistique-decisive-v2.md` (ci-après « la spécification »), `contre-lecture-preenregistrement-replication-v1.md`, `contre-lecture-2-preenregistrement-replication-v1.md`, `code/`, `journaux/`, `puissance-replication-v1.py` et sa sortie, `consigne-implementation-b-v2.md`, `implementation-b/` (implémentation B, v1 archivée et v2).

- Identifiant : **PREREG-REPLICATION-REGLES-DEFENSE-V1**
- Auteur : sous-agent neuf (Claude Opus 5.5) pour le brouillon 1 ; corrections de la contre-lecture 1 appliquées (brouillon 2) par un autre sous-agent de la session principale (Claude Opus 5.5), auteur aussi de la spécification v2, des essais complémentaires et du script de puissance, sans autre changement de fond. Brouillon 3 (corrections de la contre-lecture 2) : rédacteur neuf, sous-agent de la session conv-audit (Claude Opus 5.5 ; identifiant non fourni par l'environnement), qui n'a écrit ni les brouillons 1 et 2, ni la spécification, ni le code v3, ni B, ni les contre-lectures 1 et 2.
- Date (UTC) : brouillon 1 le 2026-11-01 ; brouillon 2 le 2026-11-01 ≈ 22:25 ; brouillon 3 le 2026-11-02 ≈ 00:43 ; texte scellé le À REMPLIR (date et heure UTC relevées par `date -u` au scellement, non estimées).
- Commit du code d'analyse : `6151e59702fa887bad0c741f1d33a4a435709869` (2 novembre 2026, 00:14:52 UTC, branche `canal/conv-audit-n04`) — contient, aux empreintes de ce texte, `code/arene_regles_defense_v3.py`, ses deux fichiers d'essais, le journal des essais, la spécification v2 (et sa copie d'entrée de B) et l'implémentation B v2 avec ses compagnons (vérifié par `git show 6151e597:<chemin> | sha256sum`, contre-lecture 2, et de nouveau pour le brouillon 3 le 2 novembre à ≈ 00:38 UTC) ; ancêtre du commit de scellement (`git merge-base --is-ancestor 6151e597 <commit de scellement>` rend 0, à vérifier au scellement ; rend 0 sur `HEAD` = `0348a83d` le 2 novembre à ≈ 00:35 UTC).
- Documents qui font foi (chemin + empreinte) :
  - préenregistrement scellé de la course originale `prereg/preregistrement-regles-defense-convergence-v1.md` — `d82dea3388684dd369520b4f394c53b9e5f71159b9c056a6f739ef32c73d025d` (monde, règles, mesures, tables A et B dont ce texte reprend les classes) ;
  - code de la course originale `docs/notes/convergence-defense-v1/regles-defense-v1/arene_regles_defense_v2.py` — `9f0dcf5e0d10fe93dd19c318f076728d62b64734161dc72b40a812a817340da3` (référence du diff v2 → v3) ; essais `test_arene_regles_defense_v2.py` — `78d979ab76bbe4b3ad6b55be77bf2b745a4457940eb9cb4c16a3ee87ef324b81` ;
  - gel v2 `docs/notes/convergence-defense-v1/regles-defense-v1/gel-regles-defense-v2.md` — `9977d7df7f87f081f3c89709c6f36ab2c3861cb06c972dffbabe0e777e9910f3` (définition des règles, inchangée) ;
  - arène v4 `brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/arene-melange-equilibre-v1/arene_melange_v4.py` — `70c77fd5c0ec72b63ae4c10e1e6b2fc423aacfedce9a4a0792869d92c5a2ae61` (copie suivie par git, identique au bit au fichier `donnees/argon-seul-convergence-v1/arene_melange_v4.py` chargé par la course originale) ;
  - résultats de la course originale `diag/20261101-160323-regles-defense-convergence/resultats-regles-defense.json` — `d07ece476cc1f33b6179c6395ec486e944a170dc6d4f77bae42b153038d5f93b` ; analyse `…/analyse-regles-defense.json` — `18b801123040c28894ccd2601f8da93b1ed8bc87d015b3db1b1603a91e680e42` ; manifeste `runs/20261101-160323-regles-defense-convergence/manifeste.json` — `36db58cfac9bfc4cf199ca5cdf74ac17ea24afab84b95ffd0aac945b922a6720` ; PID `…/pids-travail.txt` — `767aa28fb8cee94a1a130c151d7ed4487985d8f4fb2efdcd7ab805efc59e4bcd` ;
  - lecture préenregistrée originale `lecture-course-regles-defense-v1.md` — `24081eed65cebd8dd01d6e17ec76c5a6433d171da68ccbaa50657421cd7c4a23` ; audit « trop beau » — `7e81d094868e0d9cd2c03b73b5ca80cd0cd028b717a8085e027182fb57bd9966` ;
  - gabarit `prereg/gabarit-preregistrement-v1.md` — `8cad43714b562e28238a92200d6315b1769d8bdf7e9f0a8d72dfe2bc9b37700e` ;
  - spécification v2 `brouillons/preuves-mentors-v1/convergence-replication-v1/specification-statistique-decisive-v2.md` — `977dd9092cbd3715bd2cc9b5d5839f276242ad3f9df6302d383555f2b2ff511a` (version finale, inchangée après la contre-lecture 2 ; revérifiée au scellement) ; v1 archivée, lue par B v1 : `specification-statistique-decisive-v1.md` — `2a1ad6d356ab60d44aebbf8d92ee9ba932bd24f925ae4fb86538545e0706e0e5` ;
  - code v3 `brouillons/preuves-mentors-v1/convergence-replication-v1/code/arene_regles_defense_v3.py` — `3519123b7297df93ea07ec3ef72ca1f84947e2d8c9950094acaeddf8288d24d9` ;
  - essais du code v3 `…/code/test_arene_regles_defense_v3.py` — `d1afa9db925af7265c8aad1b238288229fb5b6f2977803a43411e27c4b96c849` ; essais complémentaires (CL-06) `…/code/test_arene_regles_defense_v3_complements.py` — `cad209394bf7fd6a84c905bec31fd6550e5bb6f0fcea858ce3ff50e726152328` ;
  - journal des essais (E1 à E10, lents compris : 43 essais passés, 127,5 s de mur) `brouillons/preuves-mentors-v1/convergence-replication-v1/journaux/journal-essais-code-v3-v1.log` — `a506cd447038dc0fe5dc4a0ba92edad915d7e02be34b7cea0fe07e73eaf31f83` (écrit avant le scellement ; à rejouer si un des trois fichiers change) ;
  - script de puissance `brouillons/preuves-mentors-v1/convergence-replication-v1/puissance-replication-v1.py` — `1af564c3319761e7193115a770a82fd13ea12e7d72fa6008efb772a6c2fb1638` ; sa sortie `…/puissance-replication-v1-sortie.txt` — `4ac975e3608b0725d83b1fc2ca9affca0584bbd90d3a62046b0bb698f3b165fa` ;
  - contre-lecture 1 `brouillons/preuves-mentors-v1/convergence-replication-v1/contre-lecture-preenregistrement-replication-v1.md` — `2a1cf1af4b5ee757aef979726dd3ed7ccc7661d2fe556ae249c1f87f77d5843d` ;
  - source des chiffres du pilote cités (CL-12) `docs/notes/convergence-defense-v1/argon-seul-convergence-v1/reponse-argon-convergence-v2-v1.md` — `fa49440fb82f4eec528a712ee619fe5359cb94b47bbdd91b8e2ab262004ace49` ;
  - consigne de B v2 `brouillons/preuves-mentors-v1/convergence-replication-v1/consigne-implementation-b-v2.md` — `14bfa3b44d3d0ab0930847feac7df12f0fd03321bbf1b14a14a3bf0d93df15c5` ; état des lieux `…/etat-des-lieux-v1.md` — `445b31ad9ef283420fcec75b5e78359ebcf989ed0eb5fe30af67ecc25ebae1bc` ;
  - implémentation B v2 : code, essais et rapport de validation à la ligne « Implémentation indépendante B (v2) » du bloc d'identité ; sortie de validation sur la course originale `…/implementation-b/sortie-b-originale-v2.json` — `11582b6db4aaec236952ef28756d72c1cdf7b46fa6f2587d85aa02d64af95d1d` ;
  - contre-lecture 2 `brouillons/preuves-mentors-v1/convergence-replication-v1/contre-lecture-2-preenregistrement-replication-v1.md` — `121154a45bab67bc217988ac7fc0300448931cc9c22b3ae015fa80cde76f8b5d` (compagnon présent ; commit `3221a7b4`) ;
  - chaque pièce de ce dossier, sous-dossiers compris (`code/`, `journaux/`, `implementation-b/`, `implementation-b/entrees/`), a son compagnon `.sha256` (R6), écrit par `controle_ia.scellement sceller` avant le scellement de ce texte.

### Bloc d'identité (régénéré par `arene_regles_defense_v3.py identite` ; vérifié par le code à la décision)

- Identifiant : PREREG-REPLICATION-REGLES-DEFENSE-V1
- Racines : RACINES_REPLICATION = règle D (dérivées de l'empreinte SHA-256 de ce texte scellé ; jamais écrites dans ce texte ; § Plan 3)
- Code : `arene_regles_defense_v3.py` — 3519123b7297df93ea07ec3ef72ca1f84947e2d8c9950094acaeddf8288d24d9
- Code de la course originale (référence du diff) : `arene_regles_defense_v2.py` — 9f0dcf5e0d10fe93dd19c318f076728d62b64734161dc72b40a812a817340da3
- Arène v4 : `arene_melange_v4.py` — 70c77fd5c0ec72b63ae4c10e1e6b2fc423aacfedce9a4a0792869d92c5a2ae61
- Gel : `gel-regles-defense-v2.md` — 9977d7df7f87f081f3c89709c6f36ab2c3861cb06c972dffbabe0e777e9910f3
- Configuration (empreinte de la forme canonique) : 3fbb27fc0824b7a9d13a0036c975c43e00e4dc7ece9f0231dfca7c0234785098
- Bibliothèque `src/controle_ia/gardes.py` — a83c48ceba4877a2e226c3fd43669b464152f18169bb082e9b1c48ed92179439
- Bibliothèque `src/controle_ia/prereg.py` — 3b2e3ee56463f30ffd3c549e7fe480fea574c707581bcf30098bf38f4980c306
- Bibliothèque `src/controle_ia/scellement.py` — 93beeb1c8aae75463afc98e76ffb330b1e4f26be9c08ae8fee539a2df6a94ef2
- Bibliothèque `src/controle_ia/manifeste.py` — 1a5c7464523e224ca29d62ab70d83f9e7043d9bde3000ef1a4adc9ed74c8188d
- Versions : numpy 2.4.6 ; scipy 1.17.1 ; Python 3.13.18
- Implémentation indépendante B (v2) : code `brouillons/preuves-mentors-v1/convergence-replication-v1/implementation-b/implementation_b_v2.py` — 1e32e3b6d63791b434c894cb597ed381e7920451ba2ffc79576f8c1d1231e445 ; essais `brouillons/preuves-mentors-v1/convergence-replication-v1/implementation-b/test_implementation_b_v2.py` — fdffedce3ea96d13bd02c98d3df40b2ed562be6e93117846fbf22c42f43c5c56 ; rapport de validation `brouillons/preuves-mentors-v1/convergence-replication-v1/implementation-b/validation-b-v2.md` — a29437b0b1741ea08407d2ae85415169ce508d580dd0476ade3073e1077518e2 et `brouillons/preuves-mentors-v1/convergence-replication-v1/implementation-b/validation-b-v2.json` — bbe0118557749c4fa852261a5179de54c548cbc938b7d171fa72155e2aea36be (compagnons `.sha256` présents et conformes ; commités en 6151e597, avant la création du manifeste de la course ; § Plan 4)

<!-- configuration-canonique-debut -->
```json
{
 "K": 3,
 "T": 8,
 "alpha": 0.01,
 "audit_critere": 0.01,
 "audit_departs": 100,
 "audit_es_generations": 400,
 "audit_es_lambda": 12,
 "audit_iter": 300,
 "audit_k": 10,
 "audit_n_mc": 1024,
 "audit_quantile_t": 0.995,
 "boite_mu": 5.0,
 "d": 6,
 "deltas": [
  1.4,
  1.6
 ],
 "departs": 4,
 "departs_cout": 3,
 "departs_entr": 8,
 "departs_final": 12,
 "departs_renforce": 48,
 "entrainement": "detection",
 "fractions_courbe": [
  0.25,
  0.5,
  0.75
 ],
 "grille_calibrage": [
  0.6,
  0.8,
  1.0,
  1.2,
  1.4,
  1.6,
  1.8,
  2.0,
  2.4
 ],
 "iter_entr": 300,
 "iter_max": 100,
 "iter_renforce": 200,
 "kappa_contournement": 0.5,
 "l2": 0.001,
 "lambda_ou": 8.0,
 "n_attaque_entr": 2001,
 "n_cal": 20000,
 "n_calibrage": 48,
 "n_eval": 19998,
 "n_eval_tenue": 3999,
 "n_fpr": 20000,
 "n_instances": 100,
 "n_mc": 256,
 "n_mc_final": 512,
 "n_propre_entr": 2000,
 "n_tenue": 50,
 "pas_bissection": 3,
 "plafond_cpu_tache_s": 600.0,
 "r_cible": 4.0,
 "schema_graines": "SeedSequence(entropy=racine, spawn_key=(code_delta, instance, code_bras, tour, role, ...)) ; bras commun 0, A 1, B 2, D 4, C1 5, C2 6, C3 7, B' 8, C3' 9 ; roles cible 0, propre 1, attaques d'entrainement 2, calibration 3, fausses alertes 4, Monte-Carlo 5, departs 6, evaluation 7, init maxout 8, lois tenues 9, echantillons tenus 10, final 11, cout 12, Dirichlet 13, courbe 14, attaquant independant 15 ; reechantillonnage (code_delta, code_contraste, 0, 0, 99)",
 "seuil_calibrage_bas": 0.1,
 "seuil_calibrage_haut": 0.03,
 "sigma_cible": 1.0,
 "sigma_max": 1.5,
 "sigma_min": 0.5,
 "tau": 0.25,
 "taux_departs_non_finis_max": 0.05,
 "taux_nonconv_max": 0.1,
 "tol_fpr": 0.005,
 "unites_Bp": 9
}
```
<!-- configuration-canonique-fin -->

Réglages de R4 (inchangés de la course originale, vérifiés par le code à la décision) :

- LAMBDA_RETENU = 0.3
- REFERENCE_RETENUE = moyenne

Codes de graine des règles (inchangés) : R0 20, R1 21, R2 1, R3 2, R4 24 ; rangs à l'analyse : R0 0, R1 1, R2 2, R3 3, R4 4.

## Résumé pour Lazar

1. **Ce qu'on refait** : la course du 1er novembre, avec le même monde synthétique, les mêmes cinq règles, la même configuration au bit et le même N, et un code dont aucun calcul ne change (le diff avec le code de la course est une liste fermée : chemin de l'arène, racines, identité du préenregistrement, sortie supplémentaire ; § Plan 2), sur une **graine neuve que personne ne choisit** : elle est dérivée de l'empreinte de ce texte une fois scellé (règle D, § Plan 3). Le but est de **vérifier si** l'un ou l'autre des deux constats présentés aux mentors tient à la graine de la course originale ; la réplication peut aussi échouer, et chaque issue est écrite d'avance.
2. **Les deux constats testés** : (a) **« le mélange bat l'historique »** (HR1) : la défense qui tire au hasard, aux poids d'équilibre, parmi ses moniteurs passés détecte mieux, face à un attaquant qui répond en dernier, que le moniteur unique réentraîné sur toutes les attaques passées : +0,10 et +0,12 de détection à la course originale ; (b) **« ne rien faire fait aussi bien »** (réfutation de HR0) : à la course originale, le moniteur initial jamais réentraîné est équivalent, à 0,02 près, au moniteur réentraîné sur l'historique, aux deux budgets ; la réplication demande qu'il n'y soit démontré moins bon à aucun budget. En secondaire : la régularisation vers le passé ne nuit pas (HR3), et la défense figée détecte mieux les lois tenues à l'écart.
3. **Ce qui comptera comme réplication** : (a) une estimation d'au moins **+0,05** aux deux budgets, avec un intervalle B2 (98,75 % bilatéral) dont la borne basse est au-dessus de zéro (le signe est démontré, la taille est estimée) ; (b) aux deux budgets, la classe de l'original, « équivalentes à 0,02 près », ou une classe en faveur de la défense figée (qui déclenche alors un audit, TR3) ; une classe en faveur du réentraînement donne « non répliquée », une classe imprécise « non jugeable ». Probabilités calculées d'avance si la course originale dit vrai : ≈ 1 pour (a), ≈ 0,90 pour (b), ≈ 0,82 en tenant compte de l'incertitude de l'original (script versé, § Seuil).
4. **Garde-fous** : la statistique est recodée par un **autre agent qui ne voit pas le code**, d'après la spécification ; les deux calculs doivent concorder à 10⁻⁹ près, sinon arrêt. Un résultat **plus beau** que l'original déclenche le même audit qu'un résultat plus faible (règle de symétrie). Un contrôle vérifie que les graines sont bien neuves.
5. **Coût** : processeur seul, **0 USD**, ≈ 28 min de mur sur les 2 cœurs d'une machine libre (1 693 s à l'original ; davantage si d'autres tâches tournent), `timeout 7200`.
6. **Ce que la réplication ne dit pas** : rien sur la capacité déployée (le mélange déploie jusqu'à 9 moniteurs contre 1), rien sur un attaquant plus fort que l'attaquant local, rien sur d'autres budgets ou d'autres mondes, rien sur l'exactitude du simulateur, qui est rejoué tel quel (§ suivant). Ce sont les attaques suivantes d'un mentor ; elles demandent d'autres courses.
7. **Décisions** : N = 100, le seuil « graines neuves » à plus de 2 tâches sur V, X̄ ou (ii), et l'implémentation B par un autre modèle (Claude Sonnet 5.5) ont été retenus par toi le 1er novembre à 23:50, heure de Paris (« go pour toutes tes recos par anticipation », R-1086, point 5) ; N avait d'abord été retenu par défaut de la session (R-1079). Ils peuvent changer avant le scellement, jamais après (un texte modifié est une course nouvelle). **GO de la course** : ton « go » du 1er novembre (21:36, heure de Paris), consigné en R-1075, porte nommément sur la réplication de la course de convergence, et R-1086 le confirme ; il vaut GO de cette course (processeur seul, 0 USD : aucun devis ni identifiant `GO-…`, réservés aux dépenses).

## Ce que l'expérience n'autorise pas

- **Rien au-delà de la robustesse à la graine.** Même monde (d = 6, K = 3, T = 8), mêmes deux budgets δ (1,4 ; 1,6) **choisis à l'origine sur la seule règle historique**, même oracle, même attaquant local, même λ* : une réplication réussie dit « ce n'est pas la graine », pas « c'est général ».
- **Ce que la réplication peut encore apprendre (lectures préalables déclarées)** : personne dans la chaîne n'est aveugle à la course originale — auteurs des brouillons et de la spécification, auteur du code v3 (qui en a rejoué trois tâches), implémentation B (validée sur ses résultats et son analyse), contre-lecteurs, lecteur et auditeur ; la protection repose sur le gel (texte, code, B et règle des racines fixés avant la course), non sur l'aveuglement. Pour HR1, la course originale rend déjà très peu plausible qu'une graine favorable explique l'effet (estimations à ≈ 18 et ≈ 29 erreurs-types de zéro ; probabilité de réplication calculée ≈ 1) : une réussite apporte surtout une preuve de procédure (graine non choisie, statistique recodée, chemin de code rejoué) et écarte une erreur propre à la graine 20266201 ; c'est un échec qui serait informatif. Pour HR0, l'issue est réellement incertaine (≈ 0,90 ; ≈ 0,82 avec l'incertitude de l'original) : c'est là que la réplication apprend le plus.
- **Capacité déployée** : R3 déploie un mélange aléatoire de jusqu'à 9 moniteurs linéaires (63 paramètres ; 7 par requête), R2 un seul (7). HR1 compare un mélange d'équilibre à un hyperplan pur ; qu'un mélange d'équilibre batte une stratégie pure face à un attaquant qui joue en dernier est attendu du théorème du minimax sans point-selle pur (le texte original appelle HR1 « plomberie »). Au pilote de l'arène v4 (chiffres cités, non vérifiés sur la pièce d'origine, par `docs/notes/convergence-defense-v1/argon-seul-convergence-v1/reponse-argon-convergence-v2-v1.md`, `fa49440f…`, l. 102 : B − C3 = −0,1935 et −0,1443, B − D = −0,2341 et −0,1795), des combinaisons déterministes des mêmes moniteurs faisaient nettement mieux que le mélange. Aucune phrase « le mélange est la bonne façon d'employer plusieurs moniteurs » n'est autorisée.
- **Attaquant** : V est la meilleure de deux réponses du **même** optimiseur local ; contre un mélange, l'objectif de l'attaquant est plus multimodal et l'optimiseur local pourrait y être plus faible que contre un hyperplan, ce qui gonflerait HR1. L'attaquant indépendant de l'arène v4 n'est pas branché ici ; la sérialisation des défenses finales (§ Plan 2, changement C10) permet de l'appliquer ensuite **sans rejouer la course**, dans un préenregistrement séparé (recommandé).
- **Même simulateur, jeu non recodé** : le code v3 rejoue le jeu, l'attaquant, l'oracle et la finale de v2 sans changement ; seule la statistique est recodée par une seconde implémentation (B). Une erreur du simulateur, commune aux deux courses, se retrouverait dans la réplication et serait prise pour de la robustesse. Une réplication sur graine neuve teste la dépendance à la graine, pas l'exactitude du jeu.
- **Indépendance de B** : B est un autre modèle (Claude Sonnet 5.5) que les auteurs de la spécification et du code v3 (Claude Opus 5.5), du même fournisseur (Anthropic) ; elle a été écrite d'après la spécification seule (elle-même écrite d'après le code v2), sans voir le code. La concordance A/B montre que le code et la spécification disent la même chose et que la statistique est recalculable sans le code ; elle ne montre pas que la statistique est la bonne. Dans les textes pour les mentors, écrire « un autre modèle », plutôt que « une autre famille ».
- **HR0** : « ≈ » veut dire « pas d'avantage de plus de m = 0,02 » (≈ 16 % du niveau de V au δ 1,4, ≈ 30 % au δ 1,6), pas « aucune différence » ; la défense figée est M0 (entraîné contre la cible seule), pas le meilleur moniteur figé ; l'équivalence peut refléter un plancher de la classe linéaire dans ce monde (audit original, § 3).
- **Deux budgets, une seule famille de cibles** : les deux budgets partagent la loi cible de chaque instance (corrélation entre budgets du contraste R3 − R2 : 0,45 ; R0 − R2 : 0,20 à l'original) ; « aux deux budgets » n'est pas deux réplications indépendantes.
- Rien sur les vrais modèles ni sur des moniteurs d'activations réels. Aucune revendication d'antériorité ni de nouveauté (R8). Aucune porte, aucune dépense, aucune modification du programme.

## Hypothèse

Renvoi : préenregistrement scellé de la course originale (`d82dea33…`), hypothèses HR1, HR0, HR3 ; lecture (`24081eed…`) et audit (`7e81d094…`) ; verdicts finals consignés en R-976 (session-depot) : HR1 confirmée, HR0 réfutée, HR3 confirmée, HR2 non tranchée. Monde, règles, oracle, attaquant, mesures : ceux de la course originale, sans changement (§ Plan 1).

- **HRép1 (primaire) — « le mélange bat l'historique » tient sur graine neuve** : Δ(R3, R2) = moyenne sur les instances de V(R3) − V(R2) a, à chaque budget, une estimation d'au moins τ = **+0,05** et une borne basse de B2 strictement positive : le **signe est démontré** (98,75 % bilatéral), la **taille est seulement estimée** (une borne basse entre 0 et 0,05 est permise ; « répliquée » ne dit pas que l'effet vrai atteint 0,05). Réfutation : signe inversé démontré (borne haute B2 < 0) ou effet démontré inférieur à 0,05 (borne haute B2 < 0,05) à un budget.
- **HRép0 (primaire) — « ne rien faire fait aussi bien » tient sur graine neuve** : à chaque budget, la classe de Δ(R0, R2) sur V par la Table B originale est « ≈ » (équivalentes à m = 0,02 près) ou en faveur de la défense figée (« R0 ≳ R2 », « R0 > R2 »). Réfutation : à un budget, le réentraînement l'emporte de façon démontrée (« R2 > R0 » ou « R2 ≳ R0 »).
- **HRép3 (secondaire) — « la régularisation ne nuit pas » tient** : à chaque budget, classe de Δ(R4, R2) sur V « R4 > R2 », « R4 ≳ R2 » ou « ≈ », dégénérescence S12 non déclenchée. Réfutation : « R2 > R4 » ou « R2 ≳ R4 » à un budget.
- **HRép-ii (secondaire) — la défense figée détecte mieux les lois tenues à l'écart** : Table C ligne 4 (borne basse B8 de Δ(R0, R2) sur (ii) > 0) aux deux budgets. Réfutation : régression démontrée (lignes 1 à 3) à un budget.
- **Descriptifs (recopiés, sans verdict de réplication)** : HR2 (« oublier coûte » : D̄(R1, R2) sur X̄, Table B′) — son verdict original « non tranchée » et sa fragilité à la parité de T (audit, § 5) rendent une réplication de verdict sans objet ; les autres classes des Tables B, B′, C, la Table D, R3′, le coût.
- **Hypothèses de travail** : le code v3 calcule exactement ce que calculait le code v2 (vérifié avant la course : diff restreint E5 sur tous les nœuds de niveau module, preuve mécanique pour C10, non-régression au bit E6 sur trois tâches de la course originale, dont une du budget 1,6, sur le chemin de production ; § Plan 2) ; l'implémentation B suit la spécification (vérifié sur la course originale, écart ≤ 10⁻⁹, et sur des branches synthétiques) ; la variabilité de la réplication est celle d'un rééchantillonnage de la course originale (base du calcul de puissance).

## Prédiction chiffrée et signe attendu

Les prédictions sont, **par construction**, tirées de la course originale (c'est l'objet d'une réplication) ; les probabilités viennent d'un calcul de puissance déclaré et versé (§ Seuil). Confiance = probabilité subjective arrondie.

| # | Contraste | Budget | Signe | Classe ou issue prédite | Ordre de grandeur | Confiance | Ce qui réfute |
|---|---|---|---|---|---|---|---|
| PR1 | Δ(R3, R2) sur V (HRép1) | 1,4 ; 1,6 | + | « répliquée » (est ≥ 0,05 ∧ bas(B2) > 0 aux deux) | +0,09 à +0,13 (original +0,1045 ; +0,1236) | 0,95 | haut(B2) < 0 ou haut(B2) < 0,05 à un budget |
| PR0 | Δ(R0, R2) sur V (HRép0) | 1,4 ; 1,6 | ≈ 0 | « ≈ » aux deux budgets (ou en faveur de R0) | entre −0,009 et +0,012 (original +0,0024 ; +0,0037) | 0,8 | « R2 > R0 » ou « R2 ≳ R0 » à un budget |
| PR3 | Δ(R4, R2) sur V (HRép3) | 1,4 ; 1,6 | ≥ 0 | « R4 ≳ R2 » ou « ≈ » ; S12 non déclenché | 0 à +0,03 (original +0,0202 ; +0,0142) | 0,9 | « R2 > R4 » ou « R2 ≳ R4 » à un budget |
| PRii | Δ(R0, R2) sur (ii) | 1,4 ; 1,6 | + | Table C ligne 4 aux deux | +0,03 à +0,08 (original +0,0516 ; +0,0600) | 0,9 | lignes 1 à 3 à un budget |
| PRz | écarts de réplication z_π des quatre contrastes primaires | — | — | aucun \|z_π\| > 2,4977 (TR1 non déclenché) | \|z_π\| ≈ 0 à 2 | 0,9 | TR1 déclenché (audit, pas une réfutation) |
| PRs | contrôles de santé T2 à T6 | 1,4 ; 1,6 | — | aucun déclenché ; fausses alertes à α ± 0,001 | comme l'original | 0,95 | un contrôle déclenché (non jugeable) |
| PR2 | D̄(R1, R2) sur X̄ (descriptif) | 1,4 ; 1,6 | + | recopiée | +0,01 à +0,03 | 0,8 (signe) | — (aucun verdict) |

**Déclaré.** (1) Les consignes de la tâche proposaient « HR1 : écart ≥ +0,05 avec intervalle à 95 % excluant 0 » et « HR0 : intervalle de l'écart fixe − réentraînée contenant 0 ou en faveur de la fixe ». Ce texte garde le seuil de taille +0,05 (qui est aussi l'ordre de grandeur de P1 dans le texte original) mais prend l'intervalle **B2** de l'original (98,75 % bilatéral, plus strict que 95 %) pour la comparabilité ; pour HR0, « intervalle contenant 0 » seul ferait passer une réplication imprécise pour une réussite (absence de preuve), alors que l'original a conclu par **équivalence** (E8 dans ]−0,02 ; +0,02[) : la réplication exige la même classe ou mieux pour la défense figée ; la classe « ? » (imprécise) donne « non jugeable ». (2) Les auteurs des brouillons 1 et 2 ont vu tous les résultats de la course originale (résultats bruts, analyse, lecture, audit) ; l'auteur du brouillon 3 a lu les chiffres de l'original cités par les brouillons et les contre-lectures, et les résultats bruts (recalcul des erreurs-types citées au § Ce que l'expérience n'autorise pas) ; aucune racine de la réplication n'existe encore (elle dépend de l'empreinte finale de ce texte) ; aucune exécution du jeu n'a été faite sur une racine dérivée d'un brouillon de ce texte. L'auteur du brouillon 2 a rejoué, pour les essais, trois tâches de la course originale sur ses racines d'origine (aucune information neuve : résultats déjà scellés et lus) et des tâches réduites sur des racines d'essai du gel v2 et sur des racines dérivées de textes synthétiques scellés dans un dossier temporaire (journal des essais). (3) Les probabilités de PR1 et PR0 viennent d'un rééchantillonnage des 100 instances originales (§ Seuil), non d'une course. La confiance de PR0 passe de 0,85 (brouillon 1) à 0,8, alignée sur le calcul à deux niveaux (0,818), seule modification de prédiction du brouillon 2. (4) Le brouillon 3 ne change aucune hypothèse, prédiction, confiance, métrique, aucun seuil ni aucune table : il applique la contre-lecture 2 (provenance, procédure, suites écrites d'avance, déclarations).

## Métrique

Celles de la course originale (texte scellé `d82dea33…`, § Métrique), sans changement ; définitions mathématiques complètes dans la spécification (§ 1 à 5) :
- **V** = détection finale de la défense figée après T = 8 tours, la plus basse des réponses standard et renforcée de l'attaquant, sur 19 998 échantillons frais ; **(ii)** = détection moyenne sur 50 lois tenues à l'écart ; **X̄** = moyenne sur les tours de 1 − (iii)_t.
- **Contraste apparié** à budget fixé : est = moyenne sur les 100 instances (triées par instance) de la différence « variante − R2 » ; écart-type de l'échantillon (dénominateur n − 1).
- **Intervalles** : rééchantillonnage apparié des instances, B = 20 000 tirages, générateur `SeedSequence(entropy=ρ, spawn_key=(code_budget, 200 + 100 × code_mesure + rang, 0, 0, 99))` avec ρ la racine principale de la règle D, quantiles linéaires (type 7) aux dix niveaux 0,3125 % … 99,6875 % ; B2 = [q0,00625 ; q0,99375] ; B8 = [q0,003125 ; q0,996875] ; E8 = [q0,00625 ; q0,99375] (spécification § 2, § 5).
- **Écart de réplication** (neuf) : pour chacun des quatre contrastes primaires π (R3 − R2 et R0 − R2 sur V, deux budgets), g_π = est_réplication − est_original, σ_π = √(s_rép²/100 + s_orig²/100), z_π = g_π / σ_π ; est_orig et s_orig lus dans l'analyse originale `18b80112…` (spécification § 10.2).
- **Graines neuves** (neuf) : pour chaque variante et chacune des mesures V, X̄ et (ii), nombre de tâches où la valeur de la réplication est égale au bit à celle de l'original à la même tâche (spécification § 10.3).

## Seuil

Tous les seuils de la course originale sont **repris sans changement** (S1 m = 0,02 ; S5 = 0,02 ; S9 α = 0,01, garde ± 0,005, déclencheur 0,001 ; S10 trop beau / trop mauvais ; S12 = 0,999 sur plus de la moitié des tâches ; bornes B2, B8, E8). Les bornes de l'original sont gardées **telles quelles**, sans recalcul de la multiplicité pour la famille plus petite de la réplication (conservateur ; déclaré). Réserve héritée : B2 a les quantiles d'un Bonferroni à quatre tests (commentaire de l'arène v4, l. 159–161), plus large que nécessaire pour deux budgets.

**Seuils neufs** :
- **τ = 0,05** — taille minimale de l'estimation de Δ(R3, R2) pour « HR1 répliquée » ; posé par principe à environ la moitié de l'effet original (+0,10 ; +0,12) et égal à l'ordre de grandeur de P1 dans le texte original.
- **z* = 2,497705474412374** (quantile 0,99375 de la loi normale) — déclencheur TR1 : Bonferroni à 5 % bilatéral sur les quatre contrastes primaires.
- **0,001** — déclencheur TR2 « trop propre » (les quatre |g_π| sous 0,001 ; probabilité ≈ 2,5 × 10⁻⁴ avec des graines indépendantes, en traitant les quatre écarts comme indépendants).
- **G = 2** — arrêt « graines non neuves » : **plus de 2 tâches** égales au bit à l'original, pour une variante, sur V, X̄ ou (ii) (CL-10 ; décision de Lazar R-1086, point 5 ; brouillon 1 : plus de 10 sur V seul). Dans la course originale, les coïncidences au bit entre deux tâches d'une même variante, d'un même budget et d'une même mesure donnent au plus 0,081 coïncidence attendue par hasard sur 200 tâches ; P(plus de 2) ≤ 8,3 × 10⁻⁵ par compte (loi de Poisson ; spécification § 10.3).
- **ε = 10⁻⁹** — concordance des implémentations A et B, largeur de la frontière numérique (spécification § 8, § 11).
- **S8 : `timeout 7200`** (quatre fois la durée observée à vide, 1 692,7 s : la machine est partagée avec d'autres sessions), 2 processus, 600 s de processeur par tâche (garde interne inchangée). Condition de départ : charge à une minute ≤ 1,0 relevée par `uptime` et consignée, et aucune autre tâche de calcul lancée pendant la course.

**S-N — nombre d'instances par budget** — Valeur : **N = 100** (option (a)), retenue le 1er novembre 2026 par défaut de la session (R-1079 ; travail sur processeur, R-147), puis par Lazar (R-1086, point 5) ; jamais modifiable après le scellement.
- Décision : combien d'instances par budget pour la réplication.
- Enjeu : la puissance de HRép0 (la classe « ≈ » de l'original est à 1,5 à 1,7 erreur-type de sa frontière) contre l'identité de configuration avec l'original.
- Option (a) **N = 100** : configuration identique au bit à l'original (`3fbb27fc…`), réplication directe, ≈ 28 min ; P(HRép1 répliquée) ≈ 1,00 ; P(HRép0 répliquée) ≈ 0,90 si l'original dit vrai (≈ 0,82 en comptant l'incertitude de l'original, rééchantillonnage à deux niveaux du script versé), « non jugeable » ≈ 0,10. Inconvénient : une chance sur dix que HR0 reste imprécise.
- Option (b) **N = 200** : P(HRép0 répliquée) ≈ 0,999 (approximation normale), ≈ 57 min ; inconvénient : le champ `n_instances` change, donc l'empreinte de configuration ; ce n'est plus la course originale au bit (seulement à la taille près) ; instances 0 à 199.
- **Recommandation : (a), confiance 0,6** — l'argument présenté aux mentors est « même course, au bit près, seule la graine change » ; la limite de puissance de HR0 est celle de la course originale elle-même et sera déclarée. Décision : (a), appliquée par défaut le 1er novembre (R-1079), retenue par Lazar (R-1086, point 5). GO de la course : R-1075, confirmé par R-1086 (Résumé, point 7).

**Calcul de puissance (déclaré)** — rééchantillonnage, 20 000 fois, de 100 instances parmi les 100 de la course originale (les mêmes instances aux deux budgets et pour les trois contrastes, pour garder les corrélations), différences par tâche décalées selon le scénario, bornes par approximation normale (z = 2,4977 pour B2 et E8, 2,7344 pour B8) ; graine de calcul sans lien avec la course (`SeedSequence(314159, (1,))`) ; script `brouillons/preuves-mentors-v1/convergence-replication-v1/puissance-replication-v1.py` (`1af564c3…`, versé avant le scellement ; il relit `d07ece47…` et vérifie son empreinte), sortie `puissance-replication-v1-sortie.txt` (`4ac975e3…`) ; recalcul du contre-lecteur par un script distinct (rapport de contre-lecture, annexe) : HRép1 1,000, HRép0 0,903 (approximation normale) et 0,918 (percentile réel), 0,82 avec l'incertitude de l'original. Les chiffres ci-dessous sont ceux du script versé (ils diffèrent du brouillon 1 d'au plus 0,008, sur les lignes « réduit de moitié » et « −0,01 »).

| Scénario (vérité supposée) | HRép1 répliquée | HRép1 non jugeable | HRép0 répliquée | HRép0 non jugeable | HRép0 non répliquée | HRép3 répliquée | TR3 (défense figée plus belle) |
|---|---|---|---|---|---|---|---|
| celle de la course originale | 1,000 | 0,000 | 0,903 | 0,096 | 0,000 | 1,000 | 0,034 |
| celle de la course originale, incertitude de l'original (deux niveaux) | 1,000 | 0,000 | 0,818 | 0,173 | 0,009 | 1,000 | 0,114 |
| effet de HR1 réduit de moitié (+0,052 ; +0,062) | 0,648 | 0,350 | — | — | — | — | — |
| effet de HR1 = +0,06 aux deux budgets | 0,954 | 0,046 | — | — | — | — | — |
| vrai Δ(R0, R2) = −0,01 (le réentraînement aide un peu) | — | — | 0,320 | 0,147 | 0,534 | — | 0,000 |
| vrai Δ(R0, R2) = −0,02 (= −m) | — | — | 0,000 | 0,001 | 0,999 | — | 0,000 |

## Plan d'analyse

### 1. Monde, règles, mesures
Ceux de la course originale, inchangés : configuration `3fbb27fc…` (N = 100), cinq variantes R0 (défense figée), R1 (dernière attaque), R2 (historique), R3 (mélange d'équilibre), R4 (régularisation, λ* = 0,3, référence « moyenne ») ; T = 8 ; δ = (1,4 ; 1,6) ; oracle « détection » ; finale « légère » de l'arène v4 plus (ii) finale et (i) sur les attaques vues ; codes de graine 20, 21, 1, 2, 24.

### 2. Code v3 (écrit par un sous-agent neuf ; liste fermée de changements par rapport à v2 `9f0dcf5e…`)
Fichier `brouillons/preuves-mentors-v1/convergence-replication-v1/code/arene_regles_defense_v3.py` (`3519123b…`), copie de v2, **avec ces seuls changements** (inventaire vérifié par E5 étendu : 95 nœuds de niveau module en v2, 108 en v3 ; 80 nœuds de v2 identiques au texte près, 15 modifiés, tous dans la liste ; 8 affectations et 5 fonctions ajoutées, toutes dans la liste) :
- **C1** en-tête : ce qui change et pourquoi (texte) ;
- **C2** `VERSION = "arene_regles_defense_v3"` ; `IDENTIFIANT_PREREG = "PREREG-REPLICATION-REGLES-DEFENSE-V1"` ;
- **C3** chemins : l'arène v4 est chargée depuis la copie suivie par git (`brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/arene-melange-equilibre-v1/arene_melange_v4.py`), empreinte épinglée inchangée `70c77fd5…` ; le code n'étant plus rangé à côté du gel v2, le gel est désigné par son chemin dans le dépôt (`DOSSIER_V2`, `GEL` : même fichier, même empreinte épinglée `9977d7df…`). Le code se lance donc depuis `code/`, sans copie à côté du gel (le point 2 de CL-08 est sans objet ; vérifié par une copie propre du dépôt, § Plan 5) ;
- **C4** racines : fonctions neuves de la règle D (spécification § 4 : `etat_regle_D`, `exiger_racines_regle_D`, `deriver_racines_regle_D`, constantes `REGLE_D`, ensemble interdit, vecteurs d'essai) ; les racines dérivées remplacent les racines de décision ; 20266201 et 20266202 rejoignent les racines employées (refusées) ;
- **C5** `exiger_racine_permise_regles` : une racine dérivée n'est permise qu'une fois posée par l'autorisation (texte scellé) ;
- **C6** `exiger_identite_prereg_regles` : identifiant neuf ; exige la ligne « RACINES_REPLICATION = règle D » à la place de « RACINE_DECISION = … » ; exige aussi l'empreinte du code v2 (constantes `CODE_V2`, `CODE_V2_SHA256`) ;
- **C7** `autoriser_decision_regles` : dérive et pose les racines après `exiger_prereg_scelle` ; refuse un second texte ;
- **C8** `_travail` : dans chaque processus de travail, l'autorisation dérive les racines du même texte et vérifie leur égalité avec celles de la tâche ; en décision, la tâche est sérialisée ;
- **C9** `main`, mode `decision` : gel v2 vérifié par son empreinte seule ; manifeste : racines (entiers et chaînes), règle D, empreinte du code v2 ; course et analyse sur les racines dérivées (`analyser_regles(res, ρ)`) ;
- **C10** sérialisation, **sortie seulement** : pour chaque variante, la défense finale (W, b, seuil t, échelle e, poids de chaque moniteur), les attaques de la trajectoire et les deux attaques finales (option `rendre_attaques` de `phase_finale`) ; la loi cible par tâche ;
- **C11** `bloc_identite` : identifiant, ligne de la règle D, empreinte du code v2 ; **C12** `__all__` ;
- **rien d'autre** : règles, oracle, attaquant, lois tenues, finale, `analyser_regles`, `_boot`, `MESURES_CONTRASTE`, compteurs, gardes, mode `essai` et ses racines d'essai v2 restent identiques.

Essais (deux fichiers ; journal `journaux/journal-essais-code-v3-v1.log`, `a506cd44…` : **43 essais passés**, dont 5 lents, 127,5 s de mur, 95 s de processeur, charge ≈ 3 sur 2 cœurs) :
- `code/test_arene_regles_defense_v3.py` (`d1afa9db…`, 34 essais) : les 25 essais de v2 adaptés, plus **E1** règle D (trois vecteurs ; gardes sur cas sain et artefacts : racines égales, racine dans l'ensemble interdit, racine égale à un vecteur d'essai, empreinte mal formée) ; **E2** 20266201 et 20266202 refusées hors de l'essai E6 (cas sain : une racine dérivée posée est acceptée) ; **E3** identité v3 (cas sain ; artefacts : identifiant v2, ligne de la règle D absente, empreinte du code v2 absente) ; **E4** décision refusée sans texte scellé (non scellé, scellé puis modifié, compagnon d'un autre texte, second texte) et acceptée avec un texte temporaire scellé ; essais de C8 et C9 avec témoins ; **E5** diff restreint par l'arbre syntaxique ; **E6 (lent)** non-régression au bit, chemin de production, (δ 1,4 ; instances 0 et 1) ; **E6 bis** l'analyse v3 des 200 tâches originales rend `18b80112…` au bit (c'est **E8** de CL-06) ; **E7** la sérialisation ne change aucune valeur et restitue les défenses ;
- `code/test_arene_regles_defense_v3_complements.py` (`cad20939…`, 9 essais, CL-06) : **E5 étendu** (inventaire de tous les nœuds de niveau module par type — fonctions, affectations dont `MESURES_CONTRASTE`, `MESURES_INDICATEUR`, `REGLES`, `CODES`, `NOMS`, `GRILLE_LAMBDA`, `REFERENCES`, `TOLERANCE_CHOIX_LAMBDA`, boucles, conditions, assertions, 16 imports, docstring — ; diff unifié imprimé dans le journal pour chacune des 28 entrées de la liste fermée, à lire par la contre-lecture 2 ; preuve mécanique pour C10 : `finale_regle` et `executer_tache_regles` de v3, privées du paramètre de sortie, des blocs `if` qui en dépendent et du mot-clé transmis, ont l'arbre de v2 ; artefact : une ligne de calcul changée est vue) ; **E6 (lent)** trois tâches de la course originale, (δ 1,6 ; instance 0), (δ 1,4 ; instances 0 et 1), chemin de production (sérialisation active), au bit, **avec la règle de repli** : si l'égalité au bit avec le fichier original échoue, v2 inchangé rejoue la même tâche sur cette machine (copie miroir, processus neuf) ; v3 = v2 ici suffit (l'écart au fichier est consigné comme différence de plate-forme, avec sa taille maximale) ; v3 ≠ v2 arrête — résultat : les trois tâches égales au fichier original, repli non employé ; **E6 repli** (rapide) : v3 = v2 au bit sur une tâche réduite du budget 1,6 ; règle de repli sur cas sain et deux artefacts ; **E8** statistique de A contre le texte de la spécification (indices du générateur, tableau du § 12, 16 libellés × 2 budgets, classes des Tables B et C recalculées, racine de plus de 2⁶³) ; **E9** garde de C8 dans de **vrais** processus de travail neufs (pool `spawn`) : racine de tâche décalée d'une unité, racine tenue décalée d'une unité, racines originales, racines échangées → arrêt avant tout calcul, aucun orphelin ; **E10** bout en bout `main decision` (configuration réduite : 2 instances, T = 2 ; texte temporaire scellé dont les **deux** racines dérivées dépassent 2⁶³ ; dépôt git temporaire propre ; deux processus `spawn`) : manifeste, PID, résultats et analyse écrits et scellés, racines relues exactement (entiers JSON et chaînes, aucune conversion en binaire64), analyse écrite = recalcul au bit.

### 3. Graines (R9) — règle D
(ρ, ρ_t) = les deux premiers mots de 64 bits de `numpy.random.SeedSequence(entropy=int(H, 16))`, H = empreinte SHA-256 de ce texte scellé (spécification § 4 ; vecteurs d'essai : l'empreinte du texte original `d82dea33…` donne (11786724493248295725, 9136419304016434890), jamais employés). ρ est la racine principale (jeu et rééchantillonnage), ρ_t celle des lois tenues à l'écart. Toute modification du texte change H, donc les racines : **un texte modifié est une course nouvelle** (R12). **Ce que la règle D garantit et ne garantit pas.** Elle est déterministe et publique : n'importe qui peut calculer ρ d'un texte candidat ; la graine n'est donc pas imprévisible, elle est **non choisie** : personne ne peut savoir si une graine arrange un résultat sans jouer le jeu dessus (≈ 28 min), et jouer le jeu, même réduit, même sur une seule tâche, sur une racine dérivée d'un texte non scellé est interdit (R1). Cette interdiction est une règle de procédure, non un verrou technique ; est interdit au même titre le fait de sceller hors du dépôt (dossier temporaire) une variante de ce texte ou d'un de ses brouillons pour en dériver des racines : les seuls textes temporaires scellés permis sont les textes synthétiques des essais du code v3 (E4, C8, C9, E9, E10), sans lien avec ce texte ; jouer k tâches sur une racine candidate renseigne déjà sur k/100 de la moyenne d'un budget, donc le coût d'une sélection croît avec l'information cherchée et n'est pas « 28 min par graine » ; la trace décrite ci-après ne voit que les versions scellées dans le dépôt. La trace de l'interdiction est vérifiable : (1) `arene_regles_defense_v3.py` ne dérive de racine qu'après `exiger_prereg_scelle` (E1, E4) ; (2) le lecteur (V0 (k)) compte dans l'historique git les versions scellées de ce texte sous ce nom (`git log --oneline -- prereg/preregistrement-replication-regles-defense-convergence-v1.md` : une seule lancée) et lit dans `registres/decisions.md` l'empreinte de chacune, consignée **avant** la course ; (3) un seul manifeste de réplication existe sous `runs/` (plus, au plus, celui d'une course interrompue et consignée, § Plan 7). **Aucune seconde course pour changer l'issue** : si l'issue n'est pas « réplication réussie » (échec, partielle, imprécise, artefact), aucune autre réplication n'est lancée sur une autre graine pour en obtenir une autre ; une seconde course, si Lazar la décide, est un préenregistrement nouveau (nouveau texte, nouvelles racines) **rapporté avec** la première, jamais à sa place ni sans elle. Schéma de dérivation des tirages inchangé : `SeedSequence(entropy=ρ, spawn_key=(code_budget, instance, code_règle, tour, rôle, …))`.

### 4. Implémentation indépendante B (procédure vérifiable, CL-07)
**Version.** B v1 (`implementation-b/implementation_b.py`, validée au bit sur la course originale avec la spécification v1, rapport `validation-b-v1.md`) reste archivée sans modification. La course emploie **B v2**, écrite par le même agent B sur la consigne `consigne-implementation-b-v2.md` (qui ne lui donne que la spécification v2 et la liste des exigences, rien du code), dans des fichiers neufs (`implementation_b_v2.py`, `test_implementation_b_v2.py`, `validation-b-v2.md` et `.json`, sorties `…-v2.json`).
**Entrées (listes fermées).** Pour la validation : les trois fichiers de `brouillons/preuves-mentors-v1/convergence-replication-v1/implementation-b/entrees/` : la spécification **v2** (copie octet pour octet, `977dd9092cbd3715bd2cc9b5d5839f276242ad3f9df6302d383555f2b2ff511a`, version finale, inchangée après la contre-lecture 2), les résultats originaux `d07ece476cc1f33b6179c6395ec486e944a170dc6d4f77bae42b153038d5f93b`, l'analyse originale `18b801123040c28894ccd2601f8da93b1ed8bc87d015b3db1b1603a91e680e42` ; la spécification v1 qui y est déjà reste lisible par B (B l'a écrite d'après elle). Pour la course : en plus, E1, E2, E3 et E5 de la réplication (spécification § 3 : résultats, manifeste, ce texte scellé, analyse de A) et leurs compagnons, à leurs chemins du dépôt. **Fichiers que B peut ouvrir en outre (liste fermée)** : sa consigne `brouillons/preuves-mentors-v1/convergence-replication-v1/consigne-implementation-b-v2.md` (`14bfa3b44d3d0ab0930847feac7df12f0fd03321bbf1b14a14a3bf0d93df15c5`) ; ses propres fichiers sous `implementation-b/` (v1 et v2) ; les fichiers temporaires qu'elle a écrits elle-même (dossier temporaire de la session, dont son script de mutations de la v1 ; `/tmp/pytest-of-root/`), supprimés à la fin selon son rapport ; les consignes permanentes `CLAUDE.md`, injectées par l'environnement ; l'interpréteur `/home/claude/controle-ia-travail/.venv/bin/python` et ses bibliothèques ; le listage des noms, sans ouverture de fichier, du dossier de la réplication, de `implementation-b/` et du dossier temporaire de la session. **B n'a pas accès** au code v2, au code v3, à l'arène v4, au préenregistrement original, à sa lecture, à son audit, aux contre-lectures ni à ce texte avant son scellement : elle travaille dans `implementation-b/`, avec la consigne écrite de ne rien ouvrir hors de ces listes, et son rapport donne la **liste de tous les fichiers qu'elle a ouverts** (lecture ou exécution), comparée par le lecteur à ces listes. **Réserve déclarée** : cet isolement est déclaratif ; le dossier temporaire de la session, que B v2 a listé (noms seulement, selon son rapport), contient une extraction de la branche n67 (code v2, préenregistrement original) ; la protection effective est la validation de B sur des branches synthétiques (spécification § 12.2) et la concordance A/B. Famille du modèle de B : Claude Sonnet 5.5 (identifiant `claude-sonnet-5-5`, déclaré dans `validation-b-v2.md`, `a29437b0…`, l. 5 et 271) — autre modèle que l'auteur de la spécification et du code v3 (Claude Opus 5.5), même fournisseur (Anthropic) ; retenu par Lazar comme « autre famille » (R-1086, point 5). La famille de B v1 n'est pas déclarée dans `validation-b-v1.md` ; la course n'emploie que B v2.
**Environnement.** B v2 est validée et lancée avec `/home/claude/controle-ia-travail/.venv/bin/python` (Python 3.13.18, numpy 2.4.6, celui de la course) ; B v1 avait été validée avec numpy 2.5.3 (rapport v1).
**Validation avant scellement** (rapport scellé avec le code ; spécification § 12) : (1) sur la course originale : écart ≤ 10⁻⁹ sur les 16 contrastes de chaque budget, classes et verdicts originaux retrouvés ; (2) **branches que la course originale n'exerce pas** : une ligne de test par ligne de chaque table (A, B, B′, C, R1, R0, R3, Rii, issues brute et après déclencheurs), sur des entrées synthétiques dont la ligne attendue est connue d'avance, en particulier **« R0 > R2 », « R0 ≳ R2 », « R2 ≳ R0 », « R2 > R0 »**, « R4 > R2 », « R2 > R4 », les lignes 2, 3, 5, 6 de la Table C, **TR3 et TR4**, la ligne inatteignable de « HR1 répliquée ? » et la frontière numérique (marque et héritage) ; (3) **gardes de réplication, cas sain et artefact**, sur des variantes de la course originale : (a) original contre lui-même : g_π = 0, TR2 déclenché, 200 égalités par variante et par mesure, arrêt « graines non neuves » (code 3) ; (b) cas sain : V (trois champs), X̄ et (ii) de toutes les variantes décalés de +10⁻⁶ et V de R3 de +0,01 de plus : aucune égalité, ni TR1, ni TR2, ni arrêt ; (c) R3 décalé de +0,06 : TR1 déclenché vers le haut ; (d) R3 décalé de −0,03 borné à zéro : TR1 déclenché vers le bas ; (e) 3 tâches gardées à l'identique pour une variante : arrêt ; 2 tâches : pas d'arrêt ; (4) **lecture exacte des entiers de 64 bits** : fichiers synthétiques dont les racines dépassent 2⁶³, et règle D sur les trois vecteurs d'essai ; (5) gardes d'entrée (spécification § 12.5), cas sain et artefact, code 2. Le rapport de validation ne cite pas l'empreinte du code validé : la contre-lecture 2 a rejoué `implementation_b_v2.py` (`1e32e3b6…`) en mode essai sur la course originale (sortie identique, hors `meta_non_deterministe`, à `sortie-b-originale-v2.json`, `11582b6d…` ; code 3 attendu) et `test_implementation_b_v2.py` (`fdffedce…`) : 560 essais passés.
**Ordre et scellement** : code, essais, rapport de validation de B v2 et leurs compagnons `.sha256` sont commités **avant** la création du manifeste de la course ; V0 (h) le vérifie mécaniquement : le commit de B est l'ancêtre du commit enregistré au manifeste (`git merge-base --is-ancestor <commit de B> <commit du manifeste>` rend 0). Plus aucune modification de B ensuite. Fait : commit `6151e597` (§ Plan 5, étape 3).

### 5. Ordre d'exécution, commandes, durée (2 cœurs de cette machine)
0. **Préparation** (dans `/home/claude/controle-ia-travail`, aucune ref `donnees/*`, aucun `git fetch` sans refspec) : `docs/notes/convergence-defense-v1/`, `diag/20261101-160323-regles-defense-convergence/`, `prereg/preregistrement-regles-defense-convergence-v1.md` (R-1079) et `runs/20261101-160323-regles-defense-convergence/` (commit `bec4eb6d`) sont dans l'arbre avec leurs compagnons ; à revérifier juste avant le scellement : `PYTHONPATH=src .venv/bin/python -m controle_ia.scellement verifier runs/20261101-160323-regles-defense-convergence/manifeste.json runs/20261101-160323-regles-defense-convergence/pids-travail.txt diag/20261101-160323-regles-defense-convergence/resultats-regles-defense.json diag/20261101-160323-regles-defense-convergence/analyse-regles-defense.json` (attendus `36db58cf…`, `767aa28f…`, `d07ece47…`, `18b80112…` ; conformes le 2 novembre à ≈ 00:25 UTC, contre-lecture 2, et à ≈ 00:39 UTC par `sha256sum -c`, brouillon 3). Ne déplacer ni renommer, jusqu'à la fin de la course, les chemins que ce texte cite sous `brouillons/` (l'arène v4 de `canal-reprise-releve-v1`, le dossier de la réplication).
1. **Essais du code v3** (joués avant le scellement : journal cité ; à rejouer si un des trois fichiers change ; ≈ 2 min de mur, ≈ 95 s de processeur) — aucune copie de v3 à côté du gel (C3) :
   `cd /home/claude/controle-ia-travail/brouillons/preuves-mentors-v1/convergence-replication-v1/code && PYTHONPATH=/home/claude/controle-ia-travail/src OMP_NUM_THREADS=1 REGLES_ESSAIS_LENTS=1 /home/claude/controle-ia-travail/.venv/bin/python -B -m pytest -q -rP --durations=0 -p no:cacheprovider test_arene_regles_defense_v3.py test_arene_regles_defense_v3_complements.py` ; journal et empreinte consignés (lignes « essais » et « journal » des documents qui font foi).
2. **Bloc d'identité** : `cd /home/claude/controle-ia-travail && PYTHONPATH=src OMP_NUM_THREADS=1 .venv/bin/python -B brouillons/preuves-mentors-v1/convergence-replication-v1/code/arene_regles_defense_v3.py identite`, comparé ligne à ligne au bloc de ce texte, hors la ligne « Implémentation indépendante B (v2) », écrite à la main (aucune autre différence admise ; identique le 2 novembre à ≈ 00:20 UTC, contre-lecture 2, et à ≈ 00:36 UTC, brouillon 3).
3. **Implémentation B v2** — fait : spécification v2 (`977dd909…`, finale) copiée octet pour octet dans `implementation-b/entrees/` (empreinte vérifiée) ; B v2 écrite, essayée (560 essais passés), validée (§ Plan 4), avec la liste des fichiers ouverts ; ses fichiers et leurs compagnons commités en `6151e59702fa887bad0c741f1d33a4a435709869` (C_B) ; ligne « Implémentation indépendante B (v2) » du bloc d'identité remplie.
4. **Contre-lecture 2** — faite (sous-agent neuf ; rapport `121154a4…`, commit `3221a7b4`) ; **brouillon 3** (corrections CL2-01 à CL2-13) ; **compagnons** `.sha256` de toutes les pièces de ce dossier (R6, CL2-04), écrits par `controle_ia.scellement sceller` et commités ; **contre-lecture 3** courte (R2 ; sous-agent neuf, sur `differences-brouillon2-brouillon3-replication-v1.diff`) ; puis **scellement** : le brouillon 3, complété de la seule date de scellement (relevée par `date -u`) et de l'entrée « Contre-lecture 3 », est écrit sous `prereg/preregistrement-replication-regles-defense-convergence-v1.md` et scellé (`controle_ia.prereg.sceller_prereg`, `problemes` muet) ; empreinte H consignée dans `registres/decisions.md`, avec la mention « GO de la course : R-1075, confirmé par R-1086 » ; commit (C_S) ; `git merge-base --is-ancestor C_B C_S` rend 0.
5. **Copie propre** : le manifeste exige `git status --porcelain --untracked-files=all` vide, et l'arbre partagé reçoit les fichiers d'autres sessions ; la course part donc d'une copie propre du dépôt au commit scellé : `git -C /home/claude/controle-ia-travail worktree add -b replication-regles-defense-v1 /home/claude/replication-regles-defense-v1 C_S` (essayé le 1er novembre à ≈ 22:14 UTC sur une copie temporaire : arbre propre avant et après le chargement du module, copie retirée ensuite) ; dans la copie : `git status --porcelain --untracked-files=all` vide, sortie consignée ; `uptime` : charge à une minute ≤ 1,0, consignée ; aucune autre tâche de calcul lancée pendant la course.
6. **La course — une seule invocation** (≈ 28 min de mur à vide ; 1 692,7 s à l'original ; plafond 120 min) :
   `cd /home/claude/replication-regles-defense-v1 && PYTHONPATH=src OMP_NUM_THREADS=1 timeout 7200 /home/claude/controle-ia-travail/.venv/bin/python -B brouillons/preuves-mentors-v1/convergence-replication-v1/code/arene_regles_defense_v3.py decision --prereg prereg/preregistrement-replication-regles-defense-convergence-v1.md --instances 0:100 --run-id "$(date -u +%Y%m%d-%H%M%S)-replication-regles-defense" --lambda 0.3 --reference moyenne --processus 2`
   Sorties scellées (dans la copie propre) : `runs/<run-id>/manifeste.json`, `runs/<run-id>/pids-travail.txt`, `diag/<run-id>/resultats-regles-defense.json`, `diag/<run-id>/analyse-regles-defense.json` (implémentation A). Puis `orphelins --pids runs/<run-id>/pids-travail.txt` sain ; commit des sorties sur la branche de la copie (C_R), fusion dans la branche de travail, retrait de la copie (`git worktree remove`).
7. **Implémentation B v2** sur la course (secondes), après la fusion des sorties de la course dans la branche de travail (étape 6), depuis `/home/claude/controle-ia-travail`, `<run-id>` étant l'identifiant du manifeste (commande du rapport de validation de B v2, `a29437b0…`, § « Commande exacte », chemins complétés, sans `--plomberie-fausse`) :
   `/home/claude/controle-ia-travail/.venv/bin/python /home/claude/controle-ia-travail/brouillons/preuves-mentors-v1/convergence-replication-v1/implementation-b/implementation_b_v2.py replication --resultats /home/claude/controle-ia-travail/diag/<run-id>/resultats-regles-defense.json --manifeste /home/claude/controle-ia-travail/runs/<run-id>/manifeste.json --prereg /home/claude/controle-ia-travail/prereg/preregistrement-replication-regles-defense-convergence-v1.md --analyse-A /home/claude/controle-ia-travail/diag/<run-id>/analyse-regles-defense.json --analyse-originale /home/claude/controle-ia-travail/brouillons/preuves-mentors-v1/convergence-replication-v1/implementation-b/entrees/analyse-regles-defense.json --resultats-originaux /home/claude/controle-ia-travail/brouillons/preuves-mentors-v1/convergence-replication-v1/implementation-b/entrees/resultats-regles-defense.json --sortie /home/claude/controle-ia-travail/brouillons/preuves-mentors-v1/convergence-replication-v1/implementation-b/sortie-b-replication-v2.json`
   Code de sortie consigné ; la sortie est scellée (`controle_ia.scellement sceller`) et commitée par la session avant que le lecteur l'ouvre ; code 0 → sortie lisible ; code 2 ou 3 → arrêt (§ Liste d'arrêt), la session ne lit que le code, `lecture_autorisee` et les motifs.
8. **Lecture** par un sous-agent neuf (R13), une fois la sortie de B scellée : V0 (dont le rejeu de deux tâches, (l)), recalcul des contrôles de santé depuis E1, recompte « graines neuves », comparaison A/B (spécification § 11), critères gelés ci-dessous ; audit si un déclencheur l'exige ; verdict scellé ; soumis à Lazar.

### 6. Comparaisons et multiplicité
Deux primaires (HRép1, HRép0), chacune aux deux budgets (intersection : « répliquée » exige les deux budgets) ; deux secondaires (HRép3, HRép-ii), lues à part, sans effet sur l'issue globale ; descriptifs recopiés. Bornes de l'original gardées (B2 pour HRép1 ; B8 et E8 pour HRép0, HRép3 ; B8 pour HRép-ii). Déclencheur d'écart de réplication corrigé par Bonferroni sur les quatre contrastes primaires.

### 7. Reprise après arrêt
Arrêt externe (`timeout`, signal) : arrêt par PID des processus consignés (R10), `orphelins --pids runs/<run-id>/pids-travail.txt` sain, puis **une** reprise complète : même code, même texte scellé (donc mêmes racines), nouvel identifiant de run, nouvelle copie propre si la première a été salie (le manifeste interrompu est commité et consigné) ; seconde interruption → « non jugeable (plomberie) ». Arrêt par garde interne → « non jugeable », version nouvelle (nouveau texte, nouvelles racines), rapportée avec celle-ci. Aucun point de reprise partiel.

### 8. Historique de conception (déclaré)
1. Demande de conv-audit (1er novembre 2026, R-1075 : « go » de Lazar sur le dossier de preuves pour les mentors, réplication de la course de convergence comprise), premier sous-agent coupé par une panne de crédits (R-1076), relance. 2. Lecture des pièces de la branche n67 et de la copie suivie de l'arène v4 ; rien sous `donnees/`. 3. Recodification de la statistique depuis la spécification écrite, sans importer le code : écart 0,0 avec l'analyse scellée. 4. Calcul de puissance. 5. Brouillon 1, état des lieux, spécification v1 (R-1079). 6. Code v3 et 34 essais (autre sous-agent neuf, commit `7d9825dd`). 7. Implémentation B v1 depuis la spécification v1 seule, validée au bit, 15 ambiguïtés relevées (commit `96a071ac`). 8. Contre-lecture 1 (commit `9fe5df65`) : scellable après 14 corrections. 9. Brouillon 2 : corrections CL-01 à CL-14, spécification v2, essais complémentaires (9 essais), script de puissance versé, consigne de B v2. 10. Implémentation B v2 (Claude Sonnet 5.5), d'après la spécification v2 seule : 560 essais passés, 150 mutations sur 150 détectées, écart 0 sur 32 contrastes ; commit `6151e597`. 11. Contre-lecture 2 (sous-agent neuf, Claude Opus 5.5) : scellable après corrections mineures (CL2-01 à CL2-13), sans changement de la spécification, du code v3, des essais ni de B. 12. Brouillon 3 (rédacteur neuf, Claude Opus 5.5) : corrections de la contre-lecture 2, soumises à une contre-lecture 3 courte (§ Contre-lecture). Aucune racine de réplication dérivée, aucune exécution du jeu sur une telle racine.

## Critères de lecture gelés

Un sous-agent neuf (R13) applique ces règles telles qu'écrites, dans l'ordre ; la première ligne vraie décide. Notations et définitions : spécification v2 § 2, § 5, § 7, § 8, § 10, § 11 (copiées ici) ; « budget » = δ 1,4 (code 1) ou δ 1,6 (code 2).

**V0 de la réplication** = (a) aucune condition de la liste d'arrêt ; (b) 200 tâches, instances 0 à 99 à chaque budget, sans doublon, cinq variantes aux noms exacts ; (c) racines du manifeste et de chacune des 200 tâches = règle D appliquée à l'empreinte de ce texte scellé (recalculée par le lecteur et par B), différentes de 20266201 et 20266202 ; (d) empreintes du code v3, de l'arène v4, du gel v2, de la configuration et de la bibliothèque = celles du bloc d'identité, versions conformes ; (e) λ = 0,3 et référence « moyenne » (commande, manifeste, chaque tâche) ; (f) une seule invocation ayant écrit des résultats (au plus une reprise complète consignée) ; (g) essais du code v3 passés avant la course (les deux fichiers, E1 à E10, lents compris ; journal consigné avec les empreintes des fichiers essayés, égales à celles de ce texte) ; (h) implémentation B v2 : code, essais, rapport de validation et leurs empreintes (celles de la ligne « Implémentation indépendante B (v2) » du bloc d'identité) présents dans le commit du manifeste ou l'un de ses ancêtres (`git merge-base --is-ancestor`) ; validation passée (§ Plan 4, points (1) à (5)) ; fichiers ouverts par B pendant son écriture et sa validation (liste de son rapport) contenus dans les listes fermées du § Plan 4 (entrées et « fichiers que B peut ouvrir en outre ») ; fichiers lus par B pendant la course (`empreintes_fichiers` de sa sortie) : exactement six, E1, E2, E3 et E5 de la réplication (chacun vérifié par son compagnon) et les deux fichiers E4 de `entrees/` (empreintes épinglées `18b80112…` et `d07ece47…`) ; (i) concordance A/B (spécification § 11.2) et concordance des états de santé entre B et le recalcul du lecteur (§ 11.3) ; (j) contrôle « graines neuves » passé (aucun des quinze comptes au-dessus de 2), comptes de B égaux au recompte du lecteur ; (k) un seul fichier scellé de ce texte dans l'historique git, l'empreinte de chaque version scellée antérieure consignée dans `registres/decisions.md` avant la course, un seul manifeste de réplication sous `runs/` (plus, au plus, celui d'une course interrompue consignée) ; (l) quelle que soit l'issue, deux tâches de la réplication (δ 1,4 ; instances 0 et 1) rejouées par le lecteur dans un processus neuf (code v3, texte scellé, racines du manifeste ; autorisation par `autoriser_decision_regles` sur le texte scellé, puis `executer_tache_regles` avec sérialisation, comme E6 ; ≈ 35 s de processeur ; rien n'est écrit sous `runs/` ni `diag/`), égales au bit au fichier de résultats sur tous les champs déterministes (hors temps processeur) : point (4) de l'audit appliqué à toutes les issues ; ce contrôle ne dépend pas du sens du résultat.

**Contrôles de santé** (spécification § 7, seuils de l'original ; chacun évalué par budget, **déclenché s'il l'est dans au moins un budget**) : T2 trop beau / trop mauvais ; T3 mélange dégénéré (bloque HRép1) ; T4 dégénérescence de R4, S12 (bloque HRép3 seulement) ; T5 optimiseur ; T6 dérive des fausses alertes. T2, T5, T6 bloquent toutes les lectures.

### Table R1 — HRép1, « le mélange bat l'historique » tient-il ? (Δ(R3, R2) sur V, bornes B2, par budget c : est_c, bas_c, haut_c)

| # | Condition | Verdict brut |
|---|---|---|
| 0 | V0 fausse | **non jugeable (plomberie)** ; aucune lecture |
| 1 | T2, T3, T5 ou T6 déclenché | **non jugeable (santé)** |
| 2 | il existe un budget où la moyenne de V ≤ 2α pour chacune des cinq variantes | **non jugeable (jeu dégénéré)** — ligne inatteignable (sa condition fait partie de T2, ligne 1), gardée pour correspondre à la Table A originale |
| 3 | aux deux budgets : est_c ≥ 0,05 ∧ bas_c > 0 | **répliquée** |
| 4 | à au moins un budget : haut_c < 0 | **non répliquée (signe inversé)** |
| 5 | à au moins un budget : haut_c < 0,05 | **non répliquée (effet démontré inférieur à 0,05)** |
| 6 | sinon | **non jugeable (imprécis)** |

### Table R0 — HRép0, « ne rien faire fait aussi bien » tient-il ? (classe κ_c de Δ(R0, R2) sur V par la Table B originale, B8 et E8, m = 0,02)

Table B originale (première condition vraie) : bas(B8) > m → « R0 > R2 » ; haut(B8) < −m → « R2 > R0 » ; bas(E8) > −m ∧ haut(E8) < m → « ≈ » ; bas(B8) > 0 → « R0 ≳ R2 » ; haut(B8) < 0 → « R2 ≳ R0 » ; sinon « ? ».

| # | Condition | Verdict brut |
|---|---|---|
| 0 | V0 fausse | **non jugeable (plomberie)** |
| 1 | T2, T5 ou T6 déclenché | **non jugeable (santé)** |
| 2 | à au moins un budget : κ_c = « R2 > R0 » | **non répliquée (le réentraînement l'emporte d'un effet d'intérêt)** |
| 3 | à au moins un budget : κ_c = « R2 ≳ R0 » | **non répliquée (le réentraînement l'emporte, effet démontré non nul)** |
| 4 | aux deux budgets : κ_c ∈ {« ≈ », « R0 ≳ R2 », « R0 > R2 »} | **répliquée** |
| 5 | sinon (« ? » à un budget) | **non jugeable (imprécis)** |

### Table R3 — HRép3, secondaire (classe κ′_c de Δ(R4, R2) sur V par la Table B)

| # | Condition | Verdict brut |
|---|---|---|
| 0 | V0 fausse | non jugeable (plomberie) |
| 1 | T2, T5 ou T6 | non jugeable (santé) |
| 2 | T4 (S12) à au moins un budget | sans verdict (R4 ≈ défense figée), classe de R0 recopiée à côté |
| 3 | à au moins un budget : κ′_c ∈ {« R2 > R4 », « R2 ≳ R4 »} | non répliquée |
| 4 | aux deux budgets : κ′_c ∈ {« R4 > R2 », « R4 ≳ R2 », « ≈ »} | répliquée |
| 5 | sinon | non jugeable (imprécis) |

### Table Rii — HRép-ii, secondaire (ligne ℓ_c de la Table C originale pour Δ(R0, R2) sur (ii), bornes B8, S5 = 0,02)

Table C originale : 1 haut < −S5 ; 2 haut < 0 ∧ bas > −S5 ; 3 haut < 0 ; 4 bas > 0 ; 5 bas > −S5 ; 6 sinon.

| # | Condition | Verdict brut |
|---|---|---|
| 0 | V0 fausse | non jugeable (plomberie) |
| 1 | T2, T5 ou T6 | non jugeable (santé) |
| 2 | aux deux budgets : ℓ_c = 4 | répliquée |
| 3 | à au moins un budget : ℓ_c ∈ {1, 2, 3} | non répliquée (signe inversé) |
| 4 | sinon | non jugeable (imprécis) |

**Frontière numérique** (spécification § 8) : une comparaison du chemin de décision dont la quantité est à au plus 10⁻⁹ de son seuil marque la classe, le contrôle ou le déclencheur, et tout verdict qui en dépend ; la valeur retenue est celle calculée sur les nombres de A ; la lecture le signale.

### Déclencheurs d'audit (R4), symétriques — un seul suffit

- **TR1 — écart de réplication, dans les deux sens** : |g_π| > z* × σ_π (soit |z_π| > z* = 2,497705474412374) pour au moins un des quatre contrastes primaires. **Un résultat plus beau que l'original (écart vers le haut pour R3 − R2, ou vers la défense figée pour R0 − R2) déclenche exactement comme un résultat plus faible.**
- **TR2 — trop propre** : |g_π| < 0,001 pour les quatre contrastes primaires.
- **TR3 — défense figée plus belle que l'original** : κ_c ∈ {« R0 > R2 », « R0 ≳ R2 »} à au moins un budget (l'original rendait « ≈ » aux deux).
- **TR4 — non-réplication** : verdict brut de HRép1 ou de HRép0 « non répliquée (…) ».

L'arrêt « graines non neuves » (liste d'arrêt) entraîne lui aussi l'audit, avant toute lecture, quel que soit le sens des écarts.

**Effet** : tant que le rapport d'audit n'est pas scellé, les verdicts de HRép1, HRép0, HRép3 et HRép-ii sont « non jugeable (audit en attente) ». Rapport « pas d'artefact » → verdicts bruts rétablis, avec la mention « après audit » ; « artefact trouvé » → « non jugeable (artefact) », version nouvelle.

**Contenu de l'audit** (sous-agent neuf, ni auteur de ce texte, ni du code v3, ni de B, ni lecteur) : (1) recalculer la règle D sur l'empreinte du texte scellé et la comparer aux racines du manifeste et des 200 tâches ; (2) recompter les égalités au bit avec la course originale pour V, X̄ et (ii), toutes variantes ; (3) rejouer les deux fichiers d'essais du code v3, dont E5 étendu et E6 (non-régression au bit, trois tâches) ; (4) rejouer deux tâches de la réplication (δ 1,4 ; instances 0 et 1) dans un processus neuf et vérifier l'égalité au bit avec le fichier de résultats ; (5) pour HR0 : relecture du code de R0 et du compteur d'entraînements (zéro entraînement, M0 déployé) ; pour HR1 : poids de R3 issus du programme linéaire, part pure, support ; (6) recalculer A et B. **Issue** : « artefact trouvé » si erreur de code, chemin non exercé, graines non neuves ou discordance ; sinon « pas d'artefact ». Option, hors verdict : attaquant indépendant de l'arène v4 sur les défenses finales sérialisées (C10), dans un préenregistrement séparé.

### Issue globale (première ligne vraie)

Deux issues sont calculées (spécification § 10.4) : l'**issue après déclencheurs** (verdicts après l'effet des déclencheurs) vaut avant tout audit ; l'**issue brute** (verdicts bruts) vaut après un audit « pas d'artefact », avec la mention « après audit ». La ligne 1 est appliquée par le lecteur (B ne peut pas évaluer V0).

| # | Condition | Issue |
|---|---|---|
| 1 | V0 fausse, condition d'arrêt, ou discordance A/B | **non jugeable (plomberie)** |
| 2 | HRép1 ou HRép0 « non jugeable (audit en attente) » | **en attente d'audit** |
| 3 | HRép1 ou HRép0 « non jugeable (artefact) » | **non jugeable (artefact)** |
| 4 | HRép1 « non répliquée (…) » | **échec de réplication du résultat positif** |
| 5 | HRép1 « répliquée » ∧ HRép0 « répliquée » | **réplication réussie** |
| 6 | HRép1 « répliquée » ∧ HRép0 « non répliquée (…) » | **réplication partielle : le mélange tient, l'équivalence de la défense figée ne tient pas** |
| 7 | HRép1 « répliquée » ∧ HRép0 « non jugeable (…) » | **réplication partielle : le mélange tient, l'équivalence de la défense figée reste imprécise** |
| 8 | sinon | **non jugeable** |

### Issues écrites d'avance (phrases à reprendre telles quelles, chiffres remplis par le lecteur)

- **Réplication réussie, défense figée équivalente (classes « ≈ » aux deux budgets)** : « Sur une graine neuve que personne n'a choisie — dérivée de l'empreinte du texte scellé —, le mélange d'équilibre reste plus détecteur que la défense réentraînée sur l'historique (+a et +b ; signe démontré, B2 [ … ] et [ … ] ; taille estimée d'au moins 0,05 aux deux budgets) et ne rien faire reste équivalent à réentraîner sur l'historique à 0,02 près (classes « ≈ » ; E8 [ … ] et [ … ]) ; la statistique, recodée par un agent qui n'a pas vu le code, concorde à 10⁻⁹. Les deux constats de la course du 1er novembre ne tiennent donc pas à sa graine. Portée inchangée : même code de simulation, monde synthétique de l'arène v4, deux budgets, huit tours, attaquant local ; la capacité déployée et la force de l'attaquant restent à tester. »
- **Réplication réussie, défense figée meilleure qu'à l'original** (une classe « R0 ≳ R2 » ou « R0 > R2 » à au moins un budget ; l'audit TR3 est rendu) : « … le mélange d'équilibre reste plus détecteur que la défense réentraînée (+a et +b ; … ) et ne rien faire n'est démontré moins bon que réentraîner à aucun budget : classes … ; à tel budget il est meilleur d'au moins […], ce que la course originale ne montrait pas. La phrase « équivalent à 0,02 près » ne vaut que pour les budgets classés « ≈ ». Portée inchangée : même code de simulation, monde synthétique de l'arène v4, deux budgets, huit tours, attaquant local ; la capacité déployée et la force de l'attaquant restent à tester. »
- **Réplication partielle, équivalence non tenue** : « Le mélange d'équilibre bat toujours l'historique (+a, +b) ; en revanche, sur cette graine, réentraîner sur l'historique fait mieux que ne rien faire (classe … , est … ) : la phrase « ne rien faire fait aussi bien » ne sera plus présentée ; on rapporte les deux courses et leur écart. »
- **Réplication partielle, équivalence imprécise** : « Le mélange d'équilibre bat toujours l'historique ; la seconde course ne tranche pas l'équivalence de la défense figée (classe « ? » au budget … ) : cette phrase reste celle d'une seule course, avec sa marge de 0,02. »
- **Échec de réplication du résultat positif** (après un audit « pas d'artefact ») : « Sur une graine neuve, l'avantage du mélange d'équilibre ne se retrouve pas à la taille de 0,05 (ou s'inverse) : le constat de la course du 1er novembre ne tient pas à la réplication ; il n'est plus présenté comme acquis ; l'écart entre les deux courses devient l'objet d'une enquête (nœud de décision pour Lazar). »
- **En attente d'audit** : « La réplication a déclenché l'audit de symétrie (motif : … ) ; aucune phrase sur la réplication avant le rapport scellé. »
- **Non jugeable (plomberie, santé, artefact)** : « La réplication n'a pas pu être lue (motif : … ) ; aucune phrase sur la réplication ; suite selon le motif (Conséquence de chaque issue, point 1). »
- **Discordance A/B ou arrêt de B (non jugeable, plomberie)** : « Les deux calculs de la statistique, écrits indépendamment (le code de la course et l'implémentation B, d'après la spécification seule), ne concordent pas, ou B a refusé ses entrées (motif : … ) ; aucune phrase sur la réplication. » **Suite, écrite d'avance** : (a) un sous-agent neuf fait le diagnostic ; pour un code 3, il est seul à lire la sortie de B ; pour un code 2, il ne lit que le motif ; son rapport, scellé, dit si l'écart vient de A, de B, de la spécification ou d'un format ; (b) si la cause est une erreur de B, ou un format écrit par le code de la course que B lit trop strictement : une version neuve de B (fichier neuf), validée comme B v2 (§ Plan 4) et commitée, est lancée **sur décision de Lazar** (nœud), et la lecture porte la mention « après correction de l'implémentation B, écart au préenregistrement » ; (c) si la cause est dans l'analyse du code de la course (A) : la même fonction a produit l'analyse de la course originale (E6 bis) ; l'erreur est rapportée à Lazar pour les deux courses et aucune lecture n'a lieu sans sa décision ; (d) dans tous les cas, aucune seconde course sur ce texte.
- **Non jugeable, mélange non tranché** (issue ligne 8 ; HRép1 « non jugeable (imprécis) », ou « (santé) » par T3 seul) : « La réplication est lue, mais l'avantage du mélange n'y est pas tranché (motif : … ; est … et … ; B2 [ … ] et [ … ]) : le constat « le mélange bat l'historique » reste celui d'une seule course. »
- Secondaires, à ajouter après la phrase principale : « La régularisation vers le passé ne nuit toujours pas (classes … ) / ne tient pas (… ) » ; « La défense figée détecte toujours mieux les lois tenues à l'écart (+…, +…) / ne le fait plus (… ) ».

**Conséquence de chaque issue (rien d'autre n'est autorisé)** :
1. non jugeable (plomberie) : aucune phrase sur la réplication ; Lazar informé du motif ; suite selon le motif : interruption → Plan 7 ; « graines non neuves » → audit obligatoire, aucune reprise sur ce texte (liste d'arrêt) ; discordance A/B ou arrêt de B → suite écrite d'avance (§ Issues écrites d'avance) ; autre condition de la liste d'arrêt → l'action de sa ligne.
2. en attente d'audit : aucune phrase ; audit confié à un sous-agent neuf ; le rapport scellé rétablit ou non les verdicts bruts.
3. non jugeable (artefact) : aucune phrase ; version nouvelle du texte (nouvelles racines), rapportée avec celle-ci (§ Plan 3).
4. échec de réplication du résultat positif : le constat « le mélange bat l'historique » n'est plus présenté aux mentors comme acquis ; enquête sur l'écart (nœud de décision pour Lazar) ; aucune seconde graine pour changer l'issue.
5. réplication réussie : les deux constats peuvent être présentés par Lazar (contact externe : Lazar décide et envoie) avec la mention « réplication sur graine neuve, même code, même monde » et la portée du § Ce que l'expérience n'autorise pas ; aucune généralisation.
6. réplication partielle (équivalence non tenue) : la phrase « ne rien faire fait aussi bien » est retirée ; HR1 est présenté avec sa réplication.
7. réplication partielle (équivalence imprécise) : « ne rien faire fait aussi bien » reste la phrase d'une seule course, dite comme telle.
8. non jugeable : aucune phrase de réplication ; la phrase d'issue dit seulement ce qui n'est pas tranché.

**Phrase de synthèse** (lecteur R13, sans rien omettre) : « Réplication de la course de convergence sur racines dérivées (règle D, ρ = …, ρ_t = …) : V0 … ; santé : T2 … T6 … ; HRép1 : Δ(R3, R2) +… [B2 … ; … ] et +… [ … ] → … ; HRép0 : Δ(R0, R2) +… [B8 …] [E8 …], classe … et … → … ; écarts de réplication z : … ; déclencheurs TR1 à TR4 : … ; audit : … ; HRép3 : … ; HRép-ii : … ; HR2 (descriptif) : … ; concordance A/B : écart maximal … ; frontière numérique : … ; graines neuves : comptes … ; issue globale (après déclencheurs ; brute) : … ; portée : robustesse à la graine seulement. »

## Liste d'arrêt

| Condition | Action | Garde ou essai |
|---|---|---|
| Lancement sans texte scellé, conforme, identifié (identifiant v3, ligne de la règle D, empreintes du code v3 et v2, de l'arène v4, du gel v2, de la configuration, de la bibliothèque, versions, N, λ*, référence) | pas de départ ; aucune racine dérivée | `autoriser_decision_regles`, `exiger_identite_prereg_regles` ; E3, E4, E10 |
| Racines dérivées égales entre elles, dans l'ensemble interdit, ou égales à un vecteur d'essai | arrêt, aucun repli | règle D ; E1 |
| Racines 20266201 ou 20266202 demandées hors de l'essai E6 | arrêt | `exiger_racine_permise_regles` ; E2 |
| Racines d'une tâche ≠ règle D du texte, dans un processus de travail | arrêt avant la tâche | `_travail` (C8) ; essai C8, E9 |
| Arène v4 absente ou d'empreinte ≠ `70c77fd5…` ; gel v2 ≠ `9977d7df…` | pas de chargement / arrêt | `charger_arene_v4`, `exiger_gel_regles` |
| Code v3 ≠ empreinte du bloc ; différence avec v2 hors de C1 à C12 ; un essai du code v3 non passé (E6 compris, avec sa règle de repli) | pas de départ | E5, E5 étendu, E6 ; journal |
| Implémentation B v2 non commitée avant le manifeste, non validée (§ Plan 4), ou fichiers ouverts hors des listes fermées du § Plan 4 | pas de lecture | V0 (h) |
| Copie propre non propre ; fichier de sortie existant | pas de départ (R12) | `creer_manifeste`, `_exiger_absent` |
| Charge à une minute > 1,0 au départ, ou autre tâche de calcul lancée pendant la course | pas de départ / consignation (une interruption est traitée au Plan 7) | `uptime` consigné |
| Gardes de l'arène et du code v2, inchangées : processeur d'une tâche > 600 s ; fausses alertes d'une défense finale hors α ± 0,005 ; entraînements non convergés > 0,10 par tâche ; départs non finis > 5 % ; moniteur du tour 0 non reproductible ; programme linéaire non résolu ; loi inadmissible ; moniteur non fini ; R0 modifié | arrêt | gardes et essais repris de v2 |
| `timeout 7200` atteint ou signal | arrêt par PID (R10), `orphelins` sain, une reprise complète au plus | `_lancer`, `arreter_par_pid`, `exiger_aucun_orphelin` |
| B rend le code 2 (arrêt d'entrée : empreinte, compagnon, format, garde d'entrée, racines, champ de E2) | arrêt ; aucune lecture ; diagnostic par un sous-agent neuf, qui ne lit que le motif ; suite écrite d'avance (§ Issues écrites d'avance, « Discordance A/B ou arrêt de B ») | spécification § 3, § 11.1 |
| Graines non neuves : plus de 2 tâches égales au bit à l'original, pour une variante, sur V, X̄ ou (ii) (cas extrême : réplication identique à l'original au bit près) | arrêt après la course et avant toute lecture (B : code 3, `lecture_autorisee: false`) ; issue globale ligne 1 (« non jugeable (plomberie) ») ; **audit obligatoire** par un sous-agent neuf (contenu de l'audit, points (1), (2), (4) et (6)), rapport scellé, qui peut requalifier l'issue en « non jugeable (artefact) » ; **aucune reprise sur ce texte** (mêmes racines, même défaut) ; version nouvelle seulement sur décision de Lazar, rapportée avec celle-ci | calculé par B, recompté par le lecteur ; spécification § 10.3 ; testé cas sain et artefact (§ Plan 4, point (3)) |
| Discordance A/B > 10⁻⁹ sur l'un des cinq contrastes de concordance exigée (spécification § 11 : (R3, V), (R0, V), (R4, V), (R0, (ii)), (R1, X̄)) ou sur z_π ; classe, ligne de table, contrôle de santé ou verdict brut différent hors « frontière numérique » (spécification § 8) ; une discordance sur l'un des 11 autres contrastes est une alerte consignée, non un arrêt | arrêt ; aucune lecture (B : code 3) ; diagnostic par un sous-agent neuf ; suite écrite d'avance (§ Issues écrites d'avance, « Discordance A/B ou arrêt de B ») ; toute correction après lecture = écart au préenregistrement (nœud de Lazar) | spécification § 11 |
| Lecture d'un résultat de la réplication avant scellement de ce texte et de B | arrêt et consignation (R1) | — |
| Modification de ce texte après scellement | interdite (R12) ; nouveau texte = nouvelles racines = nouvelle course | règle D |
| Seconde course de réplication lancée pour changer l'issue ; version scellée non consignée | interdit (R1, R12) ; consignation et rapport conjoint des deux courses | V0 (k) |
| Appel de modèle, réseau, dépense | arrêt (devis et GO exigés) | — |
| `git fetch` sans refspec explicite ; lecture d'une ref `donnees/*` | interdit (quarantaine) | — |
| Marqueur de gabarit restant ; contre-lecture sans ses deux empreintes | pas de scellement | `controle_ia.prereg.problemes` |

Les lignes « Lecture d'un résultat de la réplication avant scellement », « Appel de modèle, réseau, dépense » et « `git fetch` sans refspec » sont des interdits de procédure (vérifiés par le lecteur sur les registres et l'historique git), non des gardes de code au sens de R5.

## Rôles

- Auteur du brouillon 1, de l'état des lieux et de la spécification v1 : sous-agent neuf (Claude Opus 5.5).
- Auteur du brouillon 2, de la spécification v2, des essais complémentaires, du script de puissance et de la consigne de B v2 : un autre sous-agent de la session principale (Claude Opus 5.5) ; n'a écrit ni le code v2, ni le code v3, ni B, et n'a ouvert de B que son rapport de validation v1.
- Auteur du brouillon 3 (corrections de la contre-lecture 2) : rédacteur neuf (Claude Opus 5.5), sous-agent de la session conv-audit ; n'a écrit aucune autre pièce de la chaîne.
- Code v3 et ses 34 essais : sous-agent neuf, qui n'écrit pas B.
- Implémentation B (v1 puis v2) : agent neuf Claude Sonnet 5.5 (`claude-sonnet-5-5`), autre modèle que les auteurs de la spécification et du code v3 (Claude Opus 5.5), même fournisseur ; « autre famille » au sens de R-1086, point 5 (la famille de B v1 n'est pas déclarée dans son rapport), qui n'ouvre que les fichiers des listes fermées du § Plan 4 (la spécification et les deux fichiers originaux pour la validation ; les fichiers de la réplication pour la course), ni v2, ni v3, ni l'arène, ni ce texte avant son scellement.
- Contre-lecture 1 (R2) : sous-agent neuf (Claude Sonnet 5.5). Contre-lecture 2 : sous-agent neuf (Claude Opus 5.5), qui n'a écrit ni ce texte, ni la spécification, ni le code v3, ni B ; rapport `brouillons/preuves-mentors-v1/convergence-replication-v1/contre-lecture-2-preenregistrement-replication-v1.md` (§ Contre-lecture). Contre-lecture 3 : sous-agent neuf, courte, qui n'a écrit aucune pièce de la chaîne ; elle lit les différences du brouillon 2 au brouillon 3 et juge que chaque correction CL2-01 à CL2-13 est appliquée sans autre changement de fond (§ Contre-lecture).
- Lecteur R13 : sous-agent neuf ; rejoue deux tâches (V0 (l)) ; applique les tables ; verdict scellé, soumis à Lazar.
- Auditeur (si un déclencheur l'exige) : sous-agent neuf.
- Lazar : N = 100, seuil « graines neuves » > 2, B par Claude Sonnet 5.5 (R-1086, point 5 ; N d'abord par défaut, R-1079) ; GO de la course : donné le 1er novembre (21:36, heure de Paris), consigné R-1075, confirmé par R-1086 (processeur, 0 USD, ≈ 28 min).

## Contre-lecture

**Contre-lecture 1** — sous-agent neuf (Claude Sonnet 5.5), 1er novembre 2026 ; brouillon relu : `brouillons/preuves-mentors-v1/convergence-replication-v1/preenregistrement-replication-convergence-v1-brouillon1.md`, empreinte `f0fd07874c6bba5dfb71c845a693749015caaee2b554ae5772c93b2a82dd7c76` ; rapport : `brouillons/preuves-mentors-v1/convergence-replication-v1/contre-lecture-preenregistrement-replication-v1.md`, empreinte `2a1cf1af4b5ee757aef979726dd3ed7ccc7661d2fe556ae249c1f87f77d5843d` ; verdict : scellable après corrections mineures ; traitement (brouillon 2) :
- CL-01 (statut, auteur, date, pièces épinglées) : accepté ; liste des restes réécrite pour le brouillon 2 ; essais, essais complémentaires et journal épinglés et remplis.
- CL-02 (S-N et GO) : accepté ; N = 100 (R-1079) ; GO = « go » de Lazar du 1er novembre, 21:36 heure de Paris, consigné R-1075, qui nomme la réplication de la course de convergence.
- CL-03 (Résumé) : accepté tel quel ; 0,82 confirmé par le script versé (0,818).
- CL-04 (phrases écrites d'avance) : accepté tel quel (deux puces de réussite ; échec réécrit).
- CL-05 (règle D, parade vérifiable, non-rejeu) : accepté ; V0 (k) et ligne de la liste d'arrêt ajoutées ; V0 (k) admet le manifeste d'une course interrompue consignée (cohérence avec V0 (f) et le Plan 7).
- CL-06 (essais) : accepté ; E1 à E7 et E8 (« E6 bis ») étaient déjà dans le fichier principal ; E5 étendu, E6 sur trois tâches dont une du budget 1,6 avec la règle de repli, E8 contre le texte de la spécification, E9 dans de vrais processus neufs et E10 de bout en bout (racines de plus de 2⁶³) ajoutés dans un fichier neuf ; tous passés.
- CL-07 (B vérifiable) : accepté ; § Plan 4 réécrit pour B v2 (entrées fermées, liste des fichiers ouverts, environnement, validation (1) à (5), ordre par `git merge-base --is-ancestor`) ; consigne de B v2 écrite.
- CL-08 (Plan 5) : accepté, sauf le point 2 (copie de v3 à côté du gel), sans objet : le code v3 désigne le gel v2 par son chemin dans le dépôt (C3), vérifié par une copie propre ; `timeout 7200`, charge ≤ 1,0, copie propre par `git worktree` (essayée).
- CL-09 (signe démontré, taille estimée) : accepté tel quel.
- CL-10 (liste d'arrêt, concordance, graines neuves) : accepté, option « plus de 2 tâches sur V, X̄ ou (ii) » retenue (réversible par Lazar avant le scellement) ; spécification v2 § 6 et § 10.3 corrigées ; note sur les interdits de procédure ajoutée.
- CL-11 (puissance, sources) : accepté ; script versé (`1af564c3…`) et sortie (`4ac975e3…`) ; table remplacée par ses chiffres ; « ≈ 16 % ».
- CL-12 (jeu non recodé, source du pilote) : accepté tel quel.
- CL-13 (conséquence de chaque issue) : accepté tel quel.
- CL-14 (contre-lecture 2) : accepté ; entrée ci-dessous.

**Contre-lecture 2** — sous-agent neuf (Claude Opus 5.5 ; identifiant non fourni par l'environnement ; n'a écrit ni ce texte, ni la spécification, ni le code v3, ni B), 2 novembre 2026 ; brouillon relu : `brouillons/preuves-mentors-v1/convergence-replication-v1/preenregistrement-replication-convergence-v1-brouillon2.md`, empreinte `74c66bd38e5288c65128ffddcd08d5ba7442cde9797c8fb7b58308b01ae32a0d` ; rapport : `brouillons/preuves-mentors-v1/convergence-replication-v1/contre-lecture-2-preenregistrement-replication-v1.md`, empreinte `121154a45bab67bc217988ac7fc0300448931cc9c22b3ae015fa80cde76f8b5d` (compagnon `.sha256` présent ; commit `3221a7b4`) ; verdict : scellable après corrections mineures ; traitement (brouillon 3, rédacteur neuf, Claude Opus 5.5) :
- CL2-01 (fichiers que B peut ouvrir, V0 (h)) : accepté ; précisions de l'auteur : la liste fermée nomme aussi le listage des noms de dossiers (sans ouverture) que B déclare ; V0 (h) compte exactement six fichiers dans `empreintes_fichiers` (E1, E2, E3, E5, vérifiés par leurs compagnons ; les deux E4, épinglés, sans compagnon lu) ; la ligne de B de la liste d'arrêt et la ligne de B des Rôles sont alignées sur les listes fermées.
- CL2-02 (graines non neuves, réplication identique à l'original : audit, aucune reprise sur ce texte) : accepté tel quel.
- CL2-03 (issue « discordance A/B ou arrêt de B » et sa suite) : accepté tel quel ; la phrase « Non jugeable (plomberie, santé, artefact) » renvoie désormais à la suite selon le motif (Conséquence, point 1), au lieu de « reprise selon la liste d'arrêt » (aucune reprise après « graines non neuves »).
- CL2-04 (compagnons `.sha256`, consigne et état des lieux cités par empreinte) : accepté ; compagnons étendus à toutes les pièces du dossier, sous-dossiers compris (entrées de B et fichiers de B v1 en plus de la liste de la contre-lecture 2), pour que la phrase « chaque pièce de ce dossier » soit vraie ; écrits par la session avant le scellement (liste et commande : rapport de rédaction du brouillon 3) ; l'empreinte de la contre-lecture 2 est écrite en clair.
- CL2-05 (décisions de Lazar R-1086, point 5) : accepté tel quel.
- CL2-06 (étapes 0, 2, 3, 7 ; commande de B figée) : accepté ; étape 0 revérifiée, étape 2 rejouée (bloc identique) pour le brouillon 3 ; étape 4 (contre-lecture 3, compagnons, scellement) et étape 8 (rejeu de V0 (l)) mises à jour par cohérence.
- CL2-07 (titre, statut, date, mentions « ce brouillon », Plan 8, rôles) : accepté ; titre et statut mis à leur forme finale dès le brouillon 3, et non au scellement : il ne reste à écrire que la date de scellement et l'entrée « Contre-lecture 3 », toutes deux vues par le validateur.
- CL2-08 (ce que la réplication peut encore apprendre) : accepté ; « ≈ 18 et ≈ 29 erreurs-types » recalculées par l'auteur sur `d07ece47…` (18,5 et 28,9) ; formulation resserrée.
- CL2-09 (indépendance de B : autre modèle, même fournisseur) : accepté ; « elle n'a lu que la spécification » écrit « écrite d'après la spécification seule, sans voir le code » (B a aussi lu sa consigne et ses fichiers v1, CL2-01).
- CL2-10 (parade contre le choix de la graine : deux précisions) : accepté ; liste corrigée : les essais du code v3 qui scellent un texte synthétique temporaire sont E4, C8, C9, E9 et E10, non seulement E4, E9 et E10.
- CL2-11 (rejeu de deux tâches pour toutes les issues, V0 (l)) : accepté ; chemin du rejeu précisé (comme E6), rien d'écrit sous `runs/` ni `diag/`.
- CL2-12 (phrase pour un « non jugeable » lu) : accepté tel quel.
- CL2-13 (empreinte du code de B rattachée par rejeu) : accepté tel quel.

**Contre-lecture 3** — À REMPLIR (sous-agent neuf, courte, sur les différences du brouillon 2 au brouillon 3, `differences-brouillon2-brouillon3-replication-v1.diff` ; identifiant ; brouillon relu : chemin et empreinte du brouillon 3 ; rapport : chemin et empreinte ; verdict ; traitement de chaque remarque ; si aucune correction n'est demandée : « aucune autre modification du texte que la date de scellement et cette entrée »).
