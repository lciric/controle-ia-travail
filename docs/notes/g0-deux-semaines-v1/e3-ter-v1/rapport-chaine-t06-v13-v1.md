# Chaîne v13 de T0.6 : plus aucune ligne de GO codée en dur — rapport du développeur, v1

- **Mission** : chaîne v13 de la course T0.6, sans codage en dur de la ligne de GO (contre-lecture `docs/notes/g0-deux-semaines-v1/e3-ter-v1/contre-lecture-ordre-e3-ter-v1-cl1.md`, remarques CLE3T-01 à CLE3T-03 et CLE3T-08), pour qu'un galop d'essai E3 ter se joue sous une ligne de GO neuve (`GO-2026-11-JJ-NN`, plafond prévu 16 USD).
- **Base** : arbre `7822a65b6afb1595ce467ffeb55c8a7f736b20dc` (`origin/prep/t06-course-v12`), extrait dans un arbre de travail détaché hors du dépôt principal (`main` ne porte pas la chaîne T0.6 : `src/controle_ia/t06/` et `scripts/lancer_t06_*.sh` n'existent que sur cette branche). Règle R12 : six fichiers **neufs**, **aucun fichier existant modifié** (`git status` de l'arbre : six `??`, `git diff` vide), aucun commit, aucune poussée, aucun `.sha256`, aucun réseau, aucune commande `vastai`, aucune clé lue.
- **Heure** : fichiers écrits entre 14:55 et 15:06 UTC le 8 novembre 2026 ; rapport à l'heure de `date -u` indiquée en fin de document.

## 1. Fichiers créés (sha256 par `sha256sum`)

Les fichiers sont dans l'arbre de travail `/tmp/claude-0/-home-user/86976e6f-3fae-57b1-a905-26802f445363/scratchpad/wt-t06-v13/` (détaché à `7822a65b`), **et** réunis dans `livrables/chaine-t06-v13-v1.zip` du dépôt principal (chemins relatifs à la racine du dépôt, prêts à être déposés sur `7822a65b`), sha256 `98f7d4cd128ebba3e251796cfc0d479b5ecf22cafbbe7a8bef81988357763e4c`.

| fichier (chemin dans le dépôt) | rôle | lignes | sha256 |
|---|---|---|---|
| `scripts/lancer_t06_v13.sh` | lanceur côté session (copie de la v12) | 361 | `d23290943cc13ccfeedc5a2c4a25c71cc2ea8913d8c65d1b7edb1f2947befe0c` |
| `scripts/amorce_instance_t06_v11.sh` | amorce de l'instance (copie de la v10) | 556 | `707e101c697c253712bec9d8c3f4b5c873478a69f1d2645cd53438d4cb32ece9` |
| `src/controle_ia/t06/session_v12.py` | module de session : lecture de la ligne de GO au registre, plafond borné par la ligne | 109 | `5b4ad5e9fa39c4a803050ed118157d005bcb30551a54a6822f38a15ca0ddd90e` |
| `src/controle_ia/t06/configuration_v6.py` | validation de la configuration : plafond d'épreuve ≤ plafond de la ligne, registre obligatoire | 54 | `7899622515588284d1045c72aee95d109ff755f525d3c4bcd70df14caf6fad8e` |
| `src/controle_ia/t06/lanceur_v6.py` | lanceur de run côté instance (copie du v5 ; import de `configuration_v6`, registre passé) | 363 | `e329493b5d54fe52f6eb278b1314a78f905ca082a51ee1a0c5c3a77bd400ac80` |
| `tests/test_t06_chaine_v13.py` | essais R5 de la chaîne v13 (95 essais) | 581 | `3a469da71847db79e32900f79f00c5282208622069f2064d0ac476bb082e1c60` |

Référence v12 à `7822a65b`, inchangée : `lancer_t06_v12.sh` `8b91be97…ee7ff`, `amorce_instance_t06_v10.sh` `69b669e1…308b3`, `session_v11.py` `c3989859…b676e`, `configuration_v5.py` `0f75e16f…d7d2b`, `lanceur_v5.py` `17efa881…f34c0`.

**Sixième fichier, non prévu par la commande** : `lanceur_v6.py`. Le lanceur de run `lanceur_v5.py` ne porte pas l'identifiant en dur, mais il importe `configuration_v5.est_epreuve` (liste fermée) : sur l'instance, une configuration au `go_id` neuf serait lue comme une configuration de course et refusée au démarrage du run (« seul GO-2026-11-02-28 est accepté », `configuration.py` l. 120). L'amorce v11 joue donc `controle_ia.t06.lanceur_v6`, copie du v5 dont seuls changent l'import, l'appel de la validation (registre du commit passé), le nom de la commande du manifeste et deux messages (essai `test_le_lanceur_v6_ne_differe_du_v5_que_par_l_import_la_validation_la_commande_et_deux_messages` : 5 lignes de différence, aucun calcul touché).

## 2. Où la v12 codait l'identifiant, et ce que la v13 met à la place

| v12 (à `7822a65b`) | lignes exactes | v13 |
|---|---|---|
| `scripts/lancer_t06_v12.sh` : `GO_EPREUVE=GO-2026-11-06-01`, `GO_EPREUVE_BIS=GO-2026-11-07-08`, `go_epreuve()` (plafonds 5 et 3 en dur) | l. 83–85 | `GO_ID_ENV="${GO_ID:-}"` (l. 82, relevé avant que `GO_ID` prenne la valeur de la course), `MOTIF_GO`, `plafond_ligne_go()` qui appelle `session_v12 plafond-ligne "$REG" GO [JOUR]` (l. 85–87) |
| `controles-epreuve` : `PGL=$(go_epreuve "$GOC") \|\| … « cette sous-commande ne sert que les épreuves à blanc »` | l. 155 | `GO_ID` de l'environnement exigé et lisible ; `go_id` de la configuration = `GO_ID` ; `go_id` ≠ GO de la course ; `PGL` = plafond **lu** sur la ligne du registre `T06_REGISTRE_GO` (type calcul, Lazar, non échue au jour donné, non révoquée) (l. 157–160) |
| `controles-epreuve` : `session_v11 plafond PLC ANT GOC` (totaux 5/8 en dur) | l. 158 | `session_v12 plafond PLC ANT GOC REG JOUR` : plafond + dépense antérieure ≤ plafond de la ligne (l. 163) |
| `controles-epreuve` : seconde ligne des « 5 premiers USD » vérifiée pour E3 bis | l. 161–162 | supprimé (propre aux deux lignes cumulées) |
| `controles-epreuve` : « sur 8 / sur 5 » dans la ligne de fin | l. 172 | « sur `$PGL`, plafond de la ligne du registre » |
| `creation` : `PGL=$(go_epreuve "$GOC") && …` | l. 184 | `go_id` = `GO_ID` de l'environnement ; `PGL=$(plafond_ligne_go "$GOC")` relu **au jour de la création** ; puis le contrôle inchangé GO/plafond = ceux des contrôles (l. 187–189) |
| `creation` : `session_v11 plafond … "$GOC"` | l. 187 | `… "$GOC" "$REG"` (l. 192) |
| `creation` : revérification de GO-2026-11-06-01 pour E3 bis | l. 198 | supprimé |
| `src/controle_ia/t06/session_v11.py` : `GO_EPREUVE`, `GO_EPREUVE_BIS`, `TOTAL_PAR_GO = {…: "5", …: "8"}`, `DEPENSE_ANTERIEURE_MIN_BIS`, `verifier_plafond_epreuve` qui refuse tout autre GO | l. 24–28, 36–45 | `session_v12.py` : `plafond_de_la_ligne`, `ligne_go_calcul` (= `session_v3.verifier_go_v3` au plafond lu sur la ligne), `verifier_plafond_epreuve(plafond, anterieures, go_id, registre, jour)` ; sous-commandes `go-ligne`, `plafond-ligne`, `plafond` à 5 ou 6 arguments ; l'ancien appel à 4 arguments rend 2 (usage), jamais un repli ; le reste importé de la v11 |
| `src/controle_ia/t06/configuration_v5.py` : `GO_EPREUVE_BIS`, `GO_EPREUVES`, `PLAFOND_EPREUVE_MAX_USD = 8.0`, `est_epreuve` (liste fermée), plafond borné à 8 | l. 16–18, 22–23, 35–36 | `configuration_v6.py` : `est_epreuve` = `go_id` lisible et ≠ GO de la course ; `exiger_config_t06_v6(config, registre_go, jour)` : plafond fini > 0 **et ≤ plafond de la ligne** lue au registre ; registre absent ⇒ `GardeArret` (aucune validation sans lui) |
| `scripts/amorce_instance_t06_v10.sh` : `case "$EPREUVE_GO" in GO-2026-11-06-01) PLAFOND_LIGNE_GO=5;; GO-2026-11-07-08) PLAFOND_LIGNE_GO=3;; *) refus …` | l. 233 | identifiant lisible exigé, ≠ GO de la course (l. 234–236) ; après le clonage, `PLAFOND_LIGNE_GO=$(session_v12 plafond-ligne registres/go.md "$EPREUVE_GO")` sur le registre **du commit cloné**, refus sinon (l. 367, 369) ; la vérification v3 du GO et le calendrier (l. 370, 397) reçoivent ce plafond, inchangés |
| amorce v10 : message « … sous GO-2026-11-06-01 » | l. 239 | message sans identifiant (l. 242) |
| amorce v10 : `lanceur_v5` | l. 492, 494 | `lanceur_v6` (l. 497, 499) |

Convention de la garde `.claude/hooks/garde_calcul.py` : la commande de création imprimée commence toujours par `GO_ID=<go_id de la configuration> …` (inchangé) ; la garde relit le registre et exige une ligne de calcul valide pour cet identifiant.

## 3. Diff v12 → v13 (résumé ; `diff -U0`)

- `lancer_t06_v12.sh` → `lancer_t06_v13.sh` : 64 lignes touchées (`+` et `−`) sur 361, en 19 blocs : en-tête v13 (1 ligne ajoutée) ; deux lignes du commentaire d'usage de `controles-epreuve` ; `A=` (amorce v11) ; `GO_ID_ENV`, `MOTIF_GO`, `plafond_ligne_go` à la place des trois lignes en dur ; `SESSION7` → `session_v12` ; étiquette `controles t06 v13` ; les lignes de `controles-epreuve` et `creation` du tableau ci-dessus ; cinq libellés « amorce v10 » → « amorce v11 » ; trois renvois `lancer_t06_v12.sh` → `lancer_t06_v13.sh` (commande d'`apres-creation`, texte de `surveillance`, texte du rang suivant) ; libellé « surveillance v13 » ; sous-commande neuve `--verifier-go-seulement` (10 lignes) et sa mention dans l'usage. **Inchangés à l'octet** : `controles` (course), masquage, `vast_masque`, choix de l'offre, calcul de la dépense et de l'heure d'épuisement, encodage de l'amorce, garde de calcul rejouée, `apres-creation`, toute la boucle de `surveillance` (présence, journal, garde de dépense). L'essai `test_diff_lanceur_v12_v13_ne_porte_que_la_ligne_de_go_le_plafond_et_les_renvois` vérifie que chaque ligne du diff porte l'un de ces marqueurs.
- `amorce_instance_t06_v10.sh` → `amorce_instance_t06_v11.sh` : 17 lignes touchées sur 556, en 9 blocs : en-tête v11, « AMORCE T06 v11 DEMARRAGE », commentaire C-V4-3, les trois lignes de l'identifiant (l. 234–236), le message de `PREREG_ABSENT`, `SESSION_V12` et la lecture du plafond de la ligne (l. 367, 369), « lanceur v6 » et `lanceur_v6`. **Inchangés** : minuterie, clonage réduit, consignation, liste figée `scripts/tests-cibles-t06-v2.txt` et son empreinte `417f637e…`, bras B v4, relais des lignes PROGRES, fin de run (essai `test_diff_amorce_v10_v11_ne_porte_que_la_ligne_de_go_et_le_lanceur_de_run`).
- `lanceur_v5.py` → `lanceur_v6.py` : 1 ligne d'en-tête ajoutée, 5 lignes changées (import, `COMMANDE`, appel `exiger_config_t06_v6(config, racine / "registres" / "go.md")`, deux messages sans identifiant). La garde d'équivalence, le tirage des pas contrôlés, la distillation, la lecture du coût ne sont pas touchés (ils vivent dans `lanceur.py`, `harnais/`, `activations.py`, `cout.py`, importés tels quels).
- `session_v12.py` et `configuration_v6.py` sont des modules neufs courts qui **importent** la v11 et les v3/v4 (aucune copie du code inchangé) : `instance_seule`, `identifiants_nommes`, `filtre_recherche`, `choisir_offre`, `corriger_prix`, `instance_presente`, `absence_probable` sont les objets mêmes de la v11 (`test_artefact_la_v11_refuse_la_ligne_neuve_en_dur_et_la_v12_la_lit` : identité d'objet) ; la validation du reste de la configuration est `configuration_v3.exiger_config_t06_v3`, comme en v4 et v5.
- Aucun identifiant des deux anciennes lignes dans le **code** des cinq fichiers de la chaîne (essai `test_aucun_identifiant_d_epreuve_en_dur_dans_le_code_de_la_chaine_v13`) ; ils ne subsistent que dans les notes d'historique en commentaire héritées (« [v11 … ] », « [v9 … ] »), conservées comme toutes les versions précédentes.

## 4. Comportement de la v13 (points 1 et 2 de la mission)

1. `GO_ID` vient de l'environnement ; la chaîne vérifie dans `registres/go.md` (`T06_REGISTRE_GO`, registre d'un clone de `main` ; puis le registre **du commit lancé**, relu par le lanceur à `controles-epreuve` et par l'amorce sur l'instance) que la ligne existe, est de type `calcul`, accordée par Lazar, non échue au jour `date -u` (accord ≤ jour ≤ échéance), non révoquée, et que son plafond (colonne « plafond », « N USD », commentaire entre parenthèses admis) couvre le plafond de l'épreuve : **plafond de la configuration + `T06_DEPENSE_EPREUVES_ANTERIEURES_USD` ≤ plafond de la ligne**. Le plafond de la configuration n'est plus borné à 8 USD ; sur l'instance, `lanceur_v6` refait la même lecture sur `registres/go.md` du commit avant tout calcul.
2. Toute vérification manquée : code 2 et dernière ligne explicite au lanceur ; `refus` (destruction demandée, code 2) à l'amorce ; `GardeArret` avant le manifeste au lanceur de run. Aucun repli (R5) : registre absent ⇒ refus ; ancien appel `plafond` à 4 arguments ⇒ usage, code 2.
3. `--verifier-go-seulement PLAFOND [DEPENSE_ANTERIEURE] [JOUR]` : vérifie `GO_ID` et le plafond demandé sur `T06_REGISTRE_GO` et **ne crée rien** (ni dossier, ni fichier, ni appel à l'outil de location ; l'essai photographie l'arbre avant et après).

## 5. Essais (R5)

Commande, dans l'arbre de travail, avec `. .venv/bin/activate` et `PYTHONPATH=src` :

```
PYTHONPATH=src timeout 900 nice -n 10 python -m pytest -q -p no:cacheprovider tests/test_t06_chaine_v13.py
→ 95 passed in 26.50s
```

Contenu (cas sain et artefacts pour chaque étage) :
- `session_v12` (23 essais) : ligne neuve lue (16 USD), borne incluse (16 + 0 ≤ 16), cumul 10,3 + 5,7 ; artefacts : identifiant absent, ligne « décision », ligne échue, identifiant vide ou illisible, plafond insuffisant (16,01 ; 15 + 1,5 ; 5,7 sur une ligne à 3 USD), plafond nul, négatif, illisible, non fini, registre absent, ligne révoquée, plafond « — » illisible, doublon non conforme ; codes de la ligne de commande (0, 1, 2) ; la v11 refuse la ligne neuve, la v12 la lit.
- `configuration_v6` et `lanceur_v6` (37 essais) : plafonds de 0,01 à 16 acceptés sur la vraie configuration d'E3 (v3) au `go_id` neuf ; 16,01, 17, 200, 0, −1, nan, inf, `True`, `"15"`, `None` refusés ; ligne absente, décision, échue, trop petite refusées ; sans registre : refus ; la course se valide comme en v5 ; la v5 lit la ligne neuve comme une course et la refuse ; `lanceur_v6.executer` va jusqu'au manifeste avec la ligne au registre de la racine, s'arrête à la validation sinon (y compris sur l'arbre réel du dépôt, dont le registre ne porte pas la ligne neuve : preuve que le registre lu est `racine/registres/go.md`), la course attend son préenregistrement.
- Lanceur v13 (shell, faux `vastai` 1.8.3, faux `df`, dépôt local avec branche `prep/essai-t06`, 31 essais) : `--verifier-go-seulement` cas sain (rien créé) et 12 artefacts (`GO_ID` vide, absent, illisible ; identifiant absent du registre ; décision ; échue ; plafond insuffisant avec et sans dépense antérieure ; ligne trop petite ; GO de la course ; registre absent ; plafond illisible) ; `controles-epreuve` cas sain (ligne lue au registre de `main` et dans le commit, `lancement.txt` complet) et 11 artefacts (dont `GO_ID` ≠ `go_id` de la configuration et ligne absente du registre **du commit** → « commit postérieur au GO exigé ») ; `creation` cas sain (commande `GO_ID=GO-… vastai create instance …`, `-e EPREUVE_GO_ID=…`, garde de calcul rejouée sur le registre du dépôt d'essai, `T06_TESTS_ARGS` toujours refusé en mode réel) et 5 artefacts (`GO_ID` vide, absent, autre ; ligne retirée du registre entre les contrôles et la création ; ligne échue au jour de la création) : aucun `create instance` dans le journal du faux outil.
- Amorce v11 (essai local, aucun appel à Vast, 10 essais) : cas sain en mode jouet et réel (« GO : GO-… conforme (plafond 16 USD », « lanceur v6 », suite ciblée jouée, branche `essai/` poussée) ; artefacts : identifiant absent du registre du commit, décision, échue, GO de la course, identifiant illisible, ligne retirée du commit → `refus`, destruction demandée, aucun run ; une ligne à 23 USD passe aussi (rien en dur).
- Diffs (3 essais) : voir § 3.

Suite existante : voir § 6.

## 6. Suite T0.6 existante

<<SUITE>>

## 7. Ce que la v13 ne règle pas (relève de l'ordre, pas du code)

- **CLE3T-02** : l'amorce v11 joue **une configuration par instance**, toujours après la suite ciblée figée (`scripts/tests-cibles-t06-v2.txt`, obligatoire en mode réel, ≈ 1,1 à 1,3 h de carte) : les artefacts « sur la même instance après le cas sain » restent impossibles ; le choix B / C / D de la contre-lecture (trois instances, amorce qui enchaîne, cas sain seul) est à la mère. La liste figée v2 ne contient pas `tests/test_t06_chaine_v13.py` : l'ajouter serait une liste v3 avec une nouvelle empreinte en dur dans une amorce v12 (non fait : « rien d'autre ne change »).
- **CLE3T-03** : il faut une branche `prep/…` (par exemple `prep/t06-e3ter-v1`) = `7822a65b` + ces six fichiers + les configurations d'E3 ter et leurs compagnons + `registres/go.md` portant la ligne neuve : `controles-epreuve` exige que le commit passé soit un ancêtre de `refs/remotes/origin/<T06_BRANCHE_CODE>` et que **son** `registres/go.md` porte la ligne (l'amorce la relit sur l'instance). Le registre de `main` (`T06_REGISTRE_GO`) doit la porter aussi. Rien de cela n'est du code.
- **CLE3T-08** : l'ordre doit appeler `env -i … GO_ID=<ligne> T06_BRANCHE_CODE=prep/… T06_REGISTRE_GO=… T06_DEPENSE_EPREUVES_ANTERIEURES_USD=0 T06_BRANCHE=essai/… bash scripts/lancer_t06_v13.sh controles-epreuve DOSSIER COMMIT CONFIG`, puis `… creation auto course 0 DOSSIER` (avec le même `GO_ID`), puis `surveillance`. Avant la ligne de GO, `GO_ID=<ligne> T06_REGISTRE_GO=… bash scripts/lancer_t06_v13.sh --verifier-go-seulement 16` permet d'éprouver la ligne sans rien créer.
- Ligne de GO, devis, configuration d'E3 ter (plafond, calendrier = échéance de la ligne, étiquette `t06-e3ter`), mot de Lazar : hors du code.

## 8. Réserves et points pour la contre-lecture (R2)

1. **Marge de 0,1 USD abandonnée** : la v8 à v11 exigeait plafond + dépense antérieure ≤ total − 0,1 (marge pensée pour les lignes cumulées). La v13 applique le critère de la mission : ≤ plafond de la ligne, borne incluse (comme la course : configuration 200 = ligne 200). Si la mère veut la marge, c'est une ligne de `session_v12.verifier_plafond_epreuve` et un essai.
2. **Notion d'épreuve élargie** : `configuration_v6.est_epreuve` est vrai pour **tout** `go_id` lisible autre que celui de la course. En mode réel sans préenregistrement, `lanceur_v6` accepte donc toute configuration dont le `go_id` est une ligne de calcul valide du registre du commit (plafond couvert). Les gardes restent : `GO_ID` explicite dans l'environnement, égal au `go_id` de la configuration, ligne de calcul valide dans deux registres (clone de `main` et commit), garde de calcul, branche `essai/`, `PREREG_ABSENT=1`. Mais rien dans le code n'exige que le périmètre de la ligne parle de T0.6 : c'est la ligne de GO et l'ordre qui le disent.
3. **E3 bis sous la v13** : les deux anciennes lignes sont lues comme toute autre ; GO-2026-11-07-08 porte « 3 USD », donc un plafond d'épreuve de 5,7 y serait refusé (la règle cumulée 5 + 3 n'est pas reproduite). Sans effet pour E3 ter (ligne séparée, dépense antérieure 0, CLE3T-04).
4. **Dates** : la validité est jugée au jour `date -u` (lanceur) ou `date.today()` sur l'instance (`TZ=UTC` posé par l'amorce) ; la configuration doit toujours avoir `calendrier.fin_go_utc` = lendemain 00:00 UTC de l'échéance de la ligne (vérification v3 inchangée).
5. Les libellés `lancement.txt` « controles-epreuve t06 v4 » (inchangé depuis la v4) restent tels quels ; « controles t06 v13 » et « surveillance v13 » sont mis à jour.
6. Rien n'a été lu sous `donnees/`, `diag/`, ni dans les dossiers interdits ; aucune instance, aucune dépense, aucune clé.

Heure de fin du rapport (`date -u`) : <<DATE>>
