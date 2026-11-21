# Note de livraison 4 — programme des deux essais d'admission du bras A, version 3

- État : LIVRÉE à la session le 21 novembre 2026. Rien scellé, rien committé, rien poussé : la session scelle.
- Auteur : sous-agent rédacteur de code (Claude Fable 5.2). Aucun réseau, aucun appel à un fournisseur, aucune dépense, aucune valeur de clé lue ; `GO_ID` jamais fixé hors des essais sur le faux fournisseur local.

## Journal
1. Lus : la vérification de la livraison 3 ; l'avenant 1 en version 3 (`5e255c5f…`), sections 0, 2.3 à 9 et 13 ; la seule ligne GO-2026-11-21-68 du registre, par `git show origin/main:registres/go.md | grep`, sur consigne de la session (hors des dix premières lignes que le mandat permettait : à déclarer).
2. Fichiers `_v3` créés depuis les `_v2` scellés (noms et références mis à jour) ; les `_v2` ne sont pas touchés.
3. **Erreur de ma part, déclarée.** En créant les fichiers `_v3`, j'ai lancé un `sed -i` dont la liste de fichiers contenait le motif trop large `scripts/*_v3.py` ; l'une de ses substitutions, `s/— version 2\./— version 3./`, a touché deux fichiers suivis et scellés hors de mon périmètre : `scripts/epreuve_temoins_seuls_v3.py` et `scripts/lancer_course_affinage_mentors_v3.py` (une ligne de docstring chacun, « version 2 » devenu « version 3 »). Vérifié par `git diff` : aucune autre ligne, aucun autre fichier suivi. Je ne les ai pas restaurés, sur consigne : la décision est à Lazar. Désormais, toute substitution nomme un à un les fichiers `*essais_admission*` que j'écris.
4. Fait dans les fichiers `_v3` : six lignes (une vérification par clé de Google), partage de la file du juge par rang, deux relais et un compteur, constat à vingt-huit clés avec six clés levées nommées, seuils de crédit de l'avenant (4.4) en décimal exact, garde 20 sur les deux projets, verrous du fournisseur tenus par l'amorce, l'ouvrier et le relais, identité du processus de l'amorce, fausse alerte de clé, âge du taux (24 heures avant, 6 heures après), `recharge_comptee` à faux (GO-2026-11-21-69). État des essais à ce point : 168 passent, 3 à reprendre. Reste : la règle des appels à Google (GO-2026-11-21-71, G-1 à G-9).
5. Règle permanente « Appels aux modèles de Google » (GO-2026-11-21-71) codée dans le chef et dans le relais de Google ; essais adaptés et sept essais neufs. Description des pièces de Lazar mise à jour au gabarit. Trois passes finales : 177 essais passent, trois fois ; aucun relais laissé vivant.

## 1. Fichiers de la livraison 4 (noms neufs, R12)

Les six fichiers `_v3` ci-dessous sont neufs ; aucun fichier `_v1` ni `_v2` n'est touché. Le gabarit des règles `regles-admission-bras-a-v1-gabarit.md` sert toujours, inchangé.

| fichier | sha256 |
|---|---|
| `scripts/chef_essais_admission_bras_a_v3.py` | `675ff1f75d3d1f7773ee2e644de0fe6ee682472713038142329e6e00a7379a66` |
| `scripts/relais_google_essais_admission_v3.py` | `df083b893010063bc7b9ec2ed3557e1303d1dc4d6ecd672c69785c6b9d1da966` |
| `scripts/relais_mistral_essais_admission_v3.py` | `f88a8159185d2792c7920f345e23b15f9552b136802db0594ab201a58ad74b30` |
| `tests/faux_fournisseur_essais_admission_v3.py` | `b9d6ddec5344ad5f05b49d8fa5c9d97971be841b6a6d36fc6e3cda9b0dfc89fa` |
| `tests/test_chef_essais_admission_bras_a_v3.py` | `1b9da75969d26b8463d35d4882780d12f18d1be69bc9569a27b193e9383bd9da` |
| `docs/notes/relance-organismes-discrets-v1/essais-admission-bras-a-v1/configuration-essais-admission-bras-a-v3-gabarit.json` | `c33fb9ee72aa0bd65b9eda139157bf3f558f8cd9d82abcb93f37af1c66dcd4a8` |
| `…/essais-admission-bras-a-v1/regles-admission-bras-a-v1-gabarit.md` (inchangé) | `4e99badef0837be28a382e0bbb674060d9c9e8f69fba9a6f6d84df9298f7520c` |

Le gabarit inscrit les empreintes des deux relais et de `scripts/lancer_relais_local_v1.py` (`d365affc…`) ; elles sont à jour.

## 2. Les trois chemins de la vérification de la livraison 3, et ses mineurs

| défaut | changement | essai |
|---|---|---|
| Numéro de processus de l'amorce repris par un autre processus après un redémarrage : la file passait pour vivante, ou pour close à tort | l'amorce écrit l'identité du processus (numéro, heure de départ du processus, identifiant de démarrage de la machine) ; `file_close` compare les trois | `test_m1_numero_de_processus_de_l_amorce_repris_apres_un_redemarrage` |
| Fausse alerte de clé : seule une révocation la levait | pièce de Lazar « - faux positif : la chaîne n'est pas la clé », admise seulement si aucun relais n'a vu la valeur exacte de sa clé ; sinon la révocation reste exigée | `test_m2_fausse_alerte_de_cle_levee_sans_revoquer_sauf_si_le_relais_a_vu_la_valeur_exacte` |
| Verrou tenu par l'amorce seule, par dossier | un verrou par fournisseur, plus un verrou « des vivants » ; l'ouvrier les reçoit ouverts, chaque relais tient le second en partage | `test_m3_le_verrou_est_celui_du_fournisseur_l_ouvrier_et_le_relais_le_tiennent`, `test_ma_deux_lancements_simultanes_le_second_ne_part_pas` |
| Âge du taux (mineur) | borne écrite : l'heure du taux est au plus 24 heures avant l'heure de la pièce, au plus 6 heures après, jamais après l'envoi | `test_age_du_taux_24_heures_avant_la_piece_6_heures_apres_jamais_apres_l_envoi` |
| Marge de change sans origine (mineur) | `marge_de_change` nulle au gabarit ; en définitive, 0,05 et le GO qui la fixe (`marge_de_change_go`) | `test_configuration_definitive_ce_qu_elle_exige` |
| Verrou par fournisseur (mineur) | voir la troisième ligne | idem |

Ma lecture des « trois mineurs » : âge du taux, origine de la marge, portée du verrou. Si la vérification en visait un autre, il n'est pas traité.

## 3. Avenant 1, version 3 (`5e255c5f…`)

| point de l'avenant | dans le programme | essais |
|---|---|---|
| Deux clés de Google, une vérification par clé | six lignes : `verification-google-cle-1` (`GEMINI_API_KEY`) et `verification-google-cle-2` (`GEMINI_API_KEY_2`), chacune son dossier et sa ligne de calcul | `test_garde_8_six_lignes_chaque_ligne_de_google_nomme_sa_variable_et_l_avenant`, `test_a_blanc_des_six_lignes` |
| Partage par rang | rangs impairs sous la première variable, pairs sous la seconde ; tableau écrit à la configuration, aucun défaut ; deux relais, un seul compteur ; une reprise reste sur sa clé (garde 17) | `test_partage_par_rang_…`, `test_file_du_juge_deux_relais_un_compteur_la_reprise_reste_sur_sa_cle`, `test_garde_17_entrees_et_ordre` |
| Noms servis égaux avant la file | garde 10 : deux relevés de vérification, noms et orthographes égaux, sinon la file ne part pas | `test_garde_10_sain_regime_courant_deux_releves`, `test_garde_10_artefacts_des_releves`, `test_garde_5_par_cle_et_regles_sur_les_huit_lectures_ensemble` |
| Chaque relais ne tient qu'une clé | le relais refuse de partir si l'autre variable de Google est dans son environnement | `test_garde_7_chaque_relais_de_google_lit_une_seule_variable` |
| Constat à vingt-huit clés, six levables | garde 9 : toutes et elles seules ; une clé levée vaut exactement « non constaté, levé par GO-2026-11-21-68 » ; liste fermée à la configuration ; aucune clé de Mistral levable ; relevé, rapport et manifeste recopient les clés levées | `test_garde_9_sain_la_piece_de_l_avenant_six_cles_levees`, `test_garde_9_artefacts_de_la_piece`, `test_garde_9_un_artefact_par_cle`, `test_garde_9_cles_levees_liste_fermee_aucun_repli_silencieux` |
| Seuils de crédit (4.4) | 19,76 dollars avant une vérification de Google, 16,08 avant la file, par projet ; dépense retirée : la somme des deux clés, sauf `google_deux_projets_distincts` à « oui » | `test_credit_avenant_4_4_cas_sain_et_artefact_chiffres_de_la_depense_retiree`, `test_credit_avenant_4_4_une_recharge_jamais_deux_…` |
| Euros, marge de 5 % | montants dans la devise affichée, décimal exact, taux diminué de la marge pour un crédit (centime inférieur), augmenté pour une dépense (centime supérieur) | `test_credit_en_euros_taux_diminue_de_la_marge_centime_inferieur`, `test_garde_20_en_euros_…` |
| Lecture de la console sur les deux projets | garde 20 : dépense vue et solde vu des deux projets, recharges survenues | `test_garde_20_sain`, `test_garde_20_artefacts` |

## 4. Recharge non comptée (GO-2026-11-21-69) — écart déclaré à l'avenant

L'avenant (4.4) compte « le solde plus une recharge ». Sur consigne de la session, la configuration porte le champ fermé `recharge_comptee` : `false` au gabarit, **exigé à `false` en définitive**, aucune valeur par défaut. Chaque projet est alors borné par son solde vu seul ; la recharge automatique reste admise au constat, comme marge non comptée. Le chemin de l'avenant (solde plus une recharge, jamais deux) reste dans le code, atteint seulement sous `recharge_comptee` vrai, que la configuration définitive refuse. Essais : `test_recharge_non_comptee_le_solde_seul_borne_chaque_projet`, `test_configuration_definitive_ce_qu_elle_exige`. Aucune ligne de Mistral ne part sans les deux limites de débit au constat (`test_garde_9_un_artefact_par_cle`).

## 5. Règle permanente « Appels aux modèles de Google » (GO-2026-11-21-71)

| point | dans le programme | essai (cas sain et artefact dans le même essai) |
|---|---|---|
| G-1 garde commune | reproduite dans le chef (`garde_google_avant_envoi`, `defaut_de_reponse_google`) et dans le relais (`defaut_du_corps`) ; **aucun module commun écrit sous `src/controle_ia/`** : hors de mon périmètre | tous ceux de la section |
| G-2 plafond ≥ réflexion + 16 000 | forme « budget » : budget explicite au corps, plafond ≥ budget + 16 000 ; forme « niveau » : borne de réflexion déclarée à la configuration, plafond ≥ borne + 16 000 ; sinon l'envoi est refusé | `test_regle_google_g2_plafond_reflexion_plus_16000_les_deux_formes` (à un jeton près, dans les deux formes ; options (a) et (b)) |
| G-3 limite de mots | `consignes.<nom>.limite_de_mots` × `fournisseurs.google.jetons_par_mot` ≤ plafond − réflexion | `test_regle_google_g3_la_limite_de_mots_tient_dans_le_plafond_de_texte` |
| G-4, G-5 file | zéro jeton de pensée (ou compte absent), texte vide, `MAX_TOKENS`, `SAFETY`, `RECITATION`, blocage : défaut journalisé (`defaut_google`), la file s'arrête, l'envoi n'est ni jugé ni compté parmi les réponses | `test_regle_google_g4_g5_dans_la_file_un_defaut_n_est_jamais_une_reponse` (huit artefacts) |
| G-6 vérification | saine seulement avec au moins un jeton de pensée ; sinon ligne 13 du classement, nœud de Lazar | `test_regle_google_g6_verification_sans_jeton_de_pensee_non_saine` |
| G-7 sonde | envoyée seulement sous `exemption_de_la_sonde` vrai et son GO ; l'exemption ne couvre que le corps exact de la sonde ; sans elle la sonde n'est pas envoyée et la file ne part pas | `test_regle_google_g7_la_sonde_ne_part_que_sous_une_exemption_inscrite` |
| G-8 relais | refuse, sans joindre l'amont, un corps sans réglage explicite ou sous le plafond ; `--borne-reflexion` obligatoire, `--plafond-exempte` à la seule vérification | `test_regle_google_g8_le_relais_controle_lui_aussi_le_corps` |
| G-9 gabarit | `sortie_max`, `reflexion`, `exemption_de_la_sonde`, `exemption_de_la_sonde_go`, `jetons_par_mot`, `limite_de_mots`, réserve des lignes de Google : `null` ; `marge_de_texte_jetons` : 16 000 ; rien ne part tant qu'un champ est nul | `test_gabarit_complet_et_refuse_par_le_chef`, `test_regle_google_de_bout_en_bout_aucun_envoi_sous_une_configuration_sans_reglage` |

Les deux décisions ouvertes ne sont pas prises par le programme. Les essais emploient des valeurs d'essai (plafond 32 768, niveau à la borne déclarée de 16 768, sonde exemptée), qui ne préjugent de rien.

Conséquences à dire à Lazar :
- Sans exemption de la sonde, la file du juge ne peut pas partir (la garde 10 exige une sonde jouée).
- Sur « Reply with the single word: OK », un modèle peut ne pas réfléchir : la vérification serait alors non saine (G-6), et c'est un nœud.
- Si le plafond de sortie passe à 65 536 (option b), les réserves et les plafonds en dollars du devis sont à refaire : le programme calcule la réserve depuis la configuration, mais les plafonds des lignes de calcul restent ceux du devis.
- `limite_de_mots` et `jetons_par_mot` doivent être inscrits par quelqu'un d'habilité à lire les consignes ; je ne les ai pas lues. Pour l'appel « OK » de la vérification, la limite est prise à un mot.
- « Mutations » de la règle : seulement celles des essais ci-dessus (bornes déplacées d'un jeton, champs retirés). Pas de campagne de mutations par outil.

## 6. Table des vingt gardes → essais

Chaque garde garde son nom `garde N` dans le code et ses essais `test_garde_N_…` (cas sain et artefact, sur le faux fournisseur local) : gardes 1 à 20, lignes 587 à 2027 du fichier d'essais. Essais ajoutés ou réécrits en livraison 4 : gardes 5, 7, 8, 9, 10, 17, 20 (ci-dessus). Les essais `test_c1…` à `test_c5…`, `test_m…`, `test_v1…`, `test_ma…`, `test_mc…` des livraisons 2 et 3 sont gardés, adaptés aux six lignes.

## 7. Écarts et lectures, à juger

1. Recharge non comptée : écart à l'avenant 4.4, voulu (section 4).
2. La devise est une clé du tableau du constat et les montants restent dans la devise affichée (avenant 5.4) ; la livraison 3 les portait hors tableau.
3. Âge du taux : 24 heures avant, 6 heures après l'heure de la pièce (au constat : la plus tardive des heures des valeurs vues), jamais après l'envoi. La borne de 6 heures est mon choix.
4. Un solde vu après le constat (mot sur la sonde, lecture de la console) : le programme prend la plus prudente des deux lectures possibles.
5. Le seuil de crédit de Mistral (8,23 dollars) reste une règle du constat, appliquée à toute ligne ; les seuils de Google ne s'appliquent qu'aux lignes de Google.
6. Le relevé de vérification vit dans un dossier par lancement ; la configuration de la file cite un relevé par clé (`releves_verification`).
7. Formes des pièces de Lazar fixées par le programme (section 8) : le devis et l'avenant n'en donnent pas la lettre.
8. La commande `regles` recoupe le rapport et le journal.
9. Le gabarit des règles n'est pas changé : les lectures de la section 4.2 du texte ne sont pas les miennes.
10. Aucun module commun de la règle de Google sous `src/controle_ia/` (G-1).
11. Les nouveaux essais n'ont pas été rejoués contre la livraison 3 pour montrer qu'ils y échouent (les fichiers `_v2` ignorent les six lignes).

## 8. Ce que le programme attend de Lazar

**Lignes de calcul au registre (garde 8).** Six lignes, huit colonnes : identifiant | date d'accord | `calcul` | périmètre | plafond | échéance | `Lazar` | référence. Le périmètre nomme la ligne par ses marques et cite l'empreinte du devis (`421ee2e6…`) ; périmètre ou référence citent la vérification du devis (`0bec479f…`) et l'avenant (`5e255c5f…`). L'identifiant est inscrit à la configuration, et `GO_ID` l'égale.

| ligne | plafond, à la lettre | marques du périmètre |
|---|---|---|
| vérification de la clé de Mistral, Europe | `0,25 USD` | « vérification de la clé de `mistral-large-4-0` sur `api.eu.mistral.ai` », « trois appels au plus » |
| vérification de la clé de Mistral, point d'accès général | `0,25 USD` | « vérification de la clé de `mistral-large-4-0` sur `api.mistral.ai` », « trois appels au plus » |
| vérification de la première clé de Google | `1,50 USD` | « vérification de la clé de `gemini-4-neon` lue sous `GEMINI_API_KEY` », « trois appels au plus » |
| vérification de la seconde clé de Google | `1,50 USD` | « vérification de la clé de `gemini-4-neon` lue sous `GEMINI_API_KEY_2` », « trois appels au plus » |
| essai du second lecteur (Mistral) | `4,75 USD` | « essai d'admission du second lecteur », « 24 appels » |
| essai du juge des deux ancres (Google) | `8,50 USD` | « essai d'admission du juge des deux ancres », « 8 appels », « rangs impairs sous `GEMINI_API_KEY` », « rangs pairs sous `GEMINI_API_KEY_2` » |

**Pièces.** Leur forme exacte est écrite au gabarit, sous `pieces_de_lazar` : constat (tableau à quatre colonnes, vingt-huit clés, heure de la transcription, ligne de taux), mot sur la sonde (par clé chez Google, avec le crédit vu par projet), lecture de la console après un envoi coupé (les deux projets chez Google), levée d'une alerte de clé (révocation, ou faux positif).

**Configuration définitive.** À inscrire : les six identifiants de lignes de calcul, la pièce de constat, `marge_de_change` 0,05 et son GO, `recharge_comptee` faux, `google_deux_projets_distincts` au constat, les deux décisions de la règle de Google (plafond et réflexion ; exemption de la sonde et son GO), `jetons_par_mot`, les limites de mots, les réserves de sortie des lignes de Google si elles ne sont pas déduites.

## 9. Reste ouvert

- Les deux décisions de Lazar sur la règle de Google ; les limites de mots.
- Les deux fichiers suivis touchés par mon erreur (journal, point 3) : toujours modifiés (`git status` : ` M` sur les deux), non restaurés, sur consigne.
- Rien n'a été joué sur un vrai fournisseur ; le comportement réel des deux points d'accès n'est connu que par le devis.

## 10. Commande d'essai et sa sortie

`env -u MISTRAL_API_KEY -u GEMINI_API_KEY -u GEMINI_API_KEY_2 -u OPENAI_API_KEY_2 PYTHONPATH=src .venv/bin/python -m pytest -q -p no:cacheprovider tests/test_chef_essais_admission_bras_a_v3.py`

Trois passes sur l'état livré : `177 passed in 90.17s`, `177 passed in 90.62s`, `177 passed in 92.48s`. Aucun processus de relais vivant après. La suite entière du dépôt n'a pas été lancée (mandat).

## 11. Chemins ouverts, déclarés

- Sur consigne de la session, hors de la liste du mandat : une ligne du registre (`git show origin/main:registres/go.md | grep GO-2026-11-21-68`) ; la section « Appels aux modèles de Google » des consignes (`git show origin/main:CLAUDE.md | awk …`) ; aucun `git fetch`.
- Lus : la vérification de la livraison 3, l'avenant 1 (versions 2 puis 3) et sa contre-lecture, la confrontation de la règle de Google à la livraison 3.
- Écrits : les six fichiers `_v3` et cette note. Modifiés par erreur : les deux fichiers du point 3 du journal.
- Lus par le programme pendant les essais, comme avant : le lot des entrées nommé par le devis, les consignes et les règles par empreinte, les modules du programme de forme.
- Aucun chemin interdit ouvert, listé ni empreinté.
