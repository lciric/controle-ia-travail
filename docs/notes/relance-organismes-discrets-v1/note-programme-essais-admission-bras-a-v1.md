# Note de livraison — programme des deux essais d'admission du bras A (Mistral Large 4, second lecteur ; `gemini-4-neon`, juge des deux ancres) — v1

- **Rédacteur** : Claude Fable 5.2, agent neuf, le 2026-11-21 (15:45 à 16:15 UTC), sous le mandat `mandat-redacteur-fable-programme-essais-admission-v1.md` (`d3bc3628…`, empreinte vérifiée avant lecture).
- **Devis qui fait foi** : `devis-essais-admission-mistral-neon-bras-a-v1.md` (`421ee2e6…`, empreinte vérifiée). Lus aussi : sa vérification et l'inventaire du programme inachevé.
- **État** : **programme fini, 121 essais passent.** Rien n'est scellé, rien n'est committé ni poussé : la session s'en charge. Non contre-lu : la contre-lecture par un agent d'un autre modèle reste due (devis, section 12, point 11).
- **Interdits tenus** : aucun réseau hors de `127.0.0.1` ; aucun appel à un fournisseur ; aucune dépense ; aucune clé lue, affichée ni écrite (valeurs factices dans les essais) ; `GO_ID` jamais fixé dans l'environnement du poste ; le chef d'essai n'a été lancé sur aucune vraie ligne. Aucun fichier écrasé hors des sept et de cette note ; rien supprimé.

## 1. En bref

Le prédécesseur avait écrit tout le programme et tous les essais, sans les avoir lancés. Au premier lancement : 80 essais sur 117 passaient. Ce qui a été trouvé et corrigé :

1. **Relais de Google : toujours en panne** (« 502, coupure de l'amont »). Il réglait son délai sur une prise que la bibliothèque standard détache après toute réponse qui annonce la fermeture. Corrigé : prise doublée, délai total tenu par une minuterie qui coupe l'amont, fermeture explicite.
2. **Relais de Mistral : la fermeture du client ne fermait pas toujours l'amont** (même cause ; l'essai de la garde 19 échouait une fois sur deux en suite entière). Corrigé de même. Le chef ferme aussi sa réponse explicitement.
3. **Défauts des essais** : quatre tolérances trop serrées devant des chiffres que le devis arrondit par excès ; plusieurs cas jouaient la même ligne de calcul et héritaient d'un relevé clos (un cas passait à vide). Corrigés.
4. **Ajouts** : le chef refuse de jouer une ligne close ; il garde la configuration au dossier (devis, section 8) ; garde de voie d'essai ; quatre essais neufs (relais, clé dans une pièce gardée, fermeture en silence, chaîne entière chez Mistral).

## 2. Table des vingt gardes : essai du cas sain, essai de l'artefact

Tous les essais sont dans `tests/test_chef_essais_admission_bras_a_v1.py` et passent par le faux fournisseur local (`tests/faux_fournisseur_essais_admission_v1.py`). Durées réduites 2 000 fois, débit déclaré mis à l'échelle (devis, gardes 1 et 2).

| garde | essai du cas sain | essai de l'artefact |
|---|---|---|
| 1. plafond avant l'envoi, compte d'un envoi sans compteur lisible | `test_garde_1_sain_cumul_bas_et_seuils_de_la_file_mistral` ; `test_garde_1_sain_prudent_connexion_coupee_breve_comptee_a_sa_reserve_et_refaite` ; `test_garde_1_sain_courant_envoi_neon_coupe_au_delai_compte_a_sa_reserve_la_reprise_part` ; chiffres : `test_chiffres_reserves_du_devis_6_4`, `test_chiffres_regime_prudent_du_devis_6_4`, `test_chiffres_garantie_du_compteur_6_4` | `test_garde_1_artefact_cumul_a_un_centime_du_plafond` ; `…_refus_du_mandataire_compte_zero_et_panne_sans_signature_comptee` ; `…_verification_google_delai_la_ligne_s_arrete_au_premier` ; `…_verification_mistral_flux_muet_jusqu_au_silence` ; `…_file_neon_sur_mot_de_lazar_envoi_coupe_la_reprise_est_refusee` ; file Mistral à 4,20 : dans l'essai sain des seuils |
| 2. délais | `test_garde_2_sain_reponse_rapide_et_flux_lent_mais_vivant` ; délai global sain, par le calcul : `test_garde_2_delai_global_sain_et_artefact`, `test_chiffres_delais_globaux_du_devis_5_6` | `test_garde_2_artefact_flux_muet_coupe_reprise_unique_puis_seconde_panne` ; `test_garde_2_artefact_verification_google_coupee_sans_reprise_mais_pas_la_file` ; `test_garde_2_delai_global_sain_et_artefact` (programme bloqué coupé, file rapportée interrompue) |
| 3. champs du corps et motif de sortie maximale | `test_garde_3_corps_sain_et_artefacts` ; `test_garde_3_sain_sortie_facturee_au_dela_sous_fin_normale_la_file_continue` | `test_garde_3_corps_sain_et_artefacts` (sans sortie maximale, 65 536, champ de plus, sans `stream`, température chez Google) ; `test_garde_3_artefact_motif_de_sortie_maximale_arrete_la_file` (quatre motifs) |
| 4. codes et motifs | `test_garde_4_sain_et_artefacts_sur_le_faux_fournisseur` (200, fin normale ; 429 puis 200) | `test_garde_4_codes_arret_reprise_attente` ; `test_garde_4_sain_et_artefacts_sur_le_faux_fournisseur` (500 puis 504 : deux envois, pas trois ; 429 puis 429 ; 401 ; motif de refus ; `Retry-After` de 900) |
| 5. nom servi | `test_garde_5_nom_servi` (nom égal, dernier événement sans `model`) | `test_garde_5_nom_servi` (autre nom ; un seul événement d'un autre nom ; préfixe `models/`) |
| 6. rien de personnel dans ce qui part | `test_garde_6_rien_de_personnel` (entrée synthétique ; lot à son empreinte) | `test_garde_6_rien_de_personnel` (courriel, chemin du poste, identifiant de session, terme de la liste, agent d'utilisateur, liste absente, lot changé) |
| 7. clés par leur nom | `test_garde_7_les_relais_tiennent_la_cle_et_elle_seule` ; les deux essais de bout en bout (clé factice dans le seul relais, absente de tout ce qui est écrit) | `test_garde_7_cles_par_leur_nom` (nom absent : rien ne part ; ouvrier avec un nom de clé : refus ; forme de clé dans un journal : trouvée) ; `test_garde_7_artefact_forme_de_cle_dans_une_piece_gardee_code_de_sortie_7` |
| 8. ligne de calcul | `test_garde_8_ligne_de_calcul` (identifiant valide, cinq lignes) | `test_garde_8_ligne_de_calcul` (absent ; ligne de l'autre file ; échue ; sans l'empreinte du devis ; absente du registre) ; fin de `test_bout_en_bout_verification_puis_file_neon` |
| 9. conditions d'envoi constatées, lues | `test_garde_9_sain` (23,00 ; `désactivée` puis `non proposée`) | `test_garde_9_artefacts_de_la_piece` ; `test_garde_9_un_artefact_par_cle` (les seize artefacts du devis, « ni vérification ni file ») |
| 10. clé vérifiée, point d'accès fixé | `test_garde_10_sain_regime_courant_et_regime_prudent` ; `test_garde_10_sain_sonde_indecidee_avec_le_mot_de_lazar` | `test_garde_10_artefacts_du_releve` ; `test_garde_10_artefacts_de_la_piece_du_mot` ; `test_garde_10_artefact_controle_par_la_depense_comptee` (15,90) |
| 11. signe de « ne sert pas ce modèle » | `test_garde_11_signe` ; `test_garde_11_sur_le_faux_fournisseur` (signe constaté ; liste sans l'identifiant et code 200 : saine) | `test_garde_11_signe` (401, 200, liste qui porte l'identifiant, corps autre, `max_tokens`, `model_config`, liste illisible) ; `test_garde_11_sur_le_faux_fournisseur` (point d'accès global ; refus du mandataire) |
| 12. fichier des règles | `test_garde_12_fichier_des_regles` ; `test_garde_12_fichier_change_apres_la_file_le_programme_des_regles_refuse` (règles appliquées) ; `test_regles_du_gabarit_copie_a_la_lettre_du_devis_et_du_texte` | `test_garde_12_fichier_des_regles` (absent, autre brouillon, gabarit, résumé, non scellé) ; `test_garde_12_fichier_change_apres_la_file_…` (refus) |
| 13. une file ne se rejoue pas | `test_garde_13_une_file_ne_se_rejoue_pas` (premier départ) | le même (second départ) ; `test_bout_en_bout_verification_puis_file_neon` (second départ : code 2, rien ne part) |
| 14. identifiant figé et voie d'accès | `test_garde_14_identifiant_fige_et_voie_d_acces` | le même (trois alias, hôte autre, hôte global sous la ligne européenne, relais d'essai sous une ligne réelle, voie d'essai) |
| 15. repli lié au signe | `test_garde_15_repli_lie_au_signe` (signe constaté) | le même (relevé absent ; trois relevés sans signe ; relevé d'une autre ligne ; ligne entière : code 2) |
| 16. forme de la réponse à la vérification | `test_garde_16_sain_formes_completes_et_sondes_comprises` ; `test_garde_16_google_sans_thoughtstokencount_vaut_zero` | `test_garde_16_artefacts_de_forme` (14 cas) ; `test_garde_16_classement_ligne_2_…`, `…_lignes_7_et_8`, `…_ligne_10_…`, `…_ligne_11_les_deux_temps`, `…_ligne_12`, `…_ligne_13`, `…_classement_unites` ; `test_garde_16_sonde_de_mistral` (9 cas), `test_garde_16_sonde_de_google` (7 cas), `test_garde_16_sonde_a_refaire_sur_un_code_429`, `test_garde_16_troisieme_appel_a_prime_…` ; `test_garde_16_majorant_par_octets` ; `test_majorant_dementi_en_file_…` |
| 17. les huit entrées de Neon | `test_garde_17_entrees_et_ordre` (les huit, dans l'ordre ; les 24 du lot) | le même (neuvième entrée, entrée autre, autre ordre, sept entrées) |
| 18. aucun morceau de réponse dans le rapport | `test_garde_18_aucun_morceau_de_reponse` (rapport et relevé rendus) | le même (extrait du texte jugé, puis de la pensée, glissés : pièce non rendue) |
| 19. borne dure en octets par envoi (Mistral) | `test_garde_19_sain_flux_de_200_000_octets` | `test_garde_19_artefact_file_coupee_a_sa_borne` ; `test_garde_19_la_fermeture_du_client_ferme_l_amont_meme_en_silence` ; vérification coupée : `test_garde_16_classement_ligne_13`, `test_garde_16_sonde_de_mistral` ; `test_garde_19_google_ne_porte_aucune_borne_en_octets` |
| 20. lecture de la console après un envoi coupé | `test_garde_20_sain` (quatre cas du devis) | `test_garde_20_artefacts` ; `test_garde_20_connexion_coupee_puis_refait_sain_sans_piece_la_file_ne_part_pas` |

Hors des gardes : critères de la section 7 (`test_criteres_recopies_du_devis_section_7`), chiffres du devis (`test_chiffres_*`), gabarit (`test_gabarit_complet_et_refuse_par_le_chef`), files entières (`test_file_mistral_entiere_rapport_et_regles`, `test_file_mistral_sans_temperature_apres_retrait`), deux chaînes de bout en bout avec amorce, relais lancé par le lanceur du dépôt et ouvrier sans clé (`test_bout_en_bout_verification_puis_file_neon`, `test_bout_en_bout_verification_puis_file_mistral`), ligne de commande.

## 3. Écarts au devis et lectures retenues

Aucun critère, seuil, plafond ni délai du devis n'est changé. Sont à juger par le contre-lecteur :

1. **Chemin du relevé de vérification** : `runs/verification-cle-<fournisseur>-bras-a-v1/<horodatage>-<ligne>/releve-verification-v1.json`, un dossier par lancement, relevé cumulé sur la ligne de calcul. Le devis écrit le relevé directement sous `runs/verification-cle-<fournisseur>-bras-a-v1/`. Raison : un lancement refait sous la même ligne n'écrase rien (R12).
2. **Cinq lectures du prédécesseur**, gardées, écrites en tête du chef : un flux de code 200 sans son marqueur de fin est une connexion coupée (ligne 6) ; une sonde sur un code 429, 5xx ou une coupure se refait par un lancement nouveau ; sans sonde jouée, aucune file, même avec un mot de Lazar ; dans une file, le refus du mandataire à sa signature est une panne de transport comptée zéro ; un refus écrit par le relais arrête la ligne.
3. **Sonde coupée par son délai** : issue « indécidée », ligne close (la ligne s'arrête par le compteur, devis 4.4, ligne 6) ; la lecture de la console est due.
4. **Le constat est lu en entier pour toute ligne** : un défaut d'une clé de Google arrête aussi les lignes de Mistral. C'est la lettre de la garde 9 (« ni vérification ni file ») ; le devis dit par ailleurs les deux files indépendantes.
5. **État de la configuration fermé** (ajout) : « definitive » ou « essai ». Une configuration « essai » ne joint que le faux fournisseur local ; une « definitive » ne porte aucune adresse d'essai. Le gabarit annonçait déjà « definitive ».
6. **Forme des pièces de Lazar, fixée par le programme** (le devis fixe leur contenu, non leur forme). La session les écrit ainsi :
   - toutes : une section `## Mot de Lazar` suivie d'au moins une ligne citée (`> …`) ;
   - constat : un tableau à cinq colonnes `| clé | valeur vue | page | date | qui a vu |`, dates à la forme `AAAA-MM-JJTHH:MMZ` ; une ligne `- heure de la transcription (UTC) : …` ;
   - mot sur la sonde : `- issue de la sonde visée : …`, `- empreinte du relevé de vérification : …` ; chez Mistral `- majorant visé : …` ; chez Google `- crédit prépayé vu après la vérification (USD) : …`, `- page : …`, `- heure (UTC) : …` ;
   - lecture de la console : `- empreinte du relevé ou du rapport : …`, `- dépense vue (USD) : …`, `- page : …`, `- heure (UTC) : …` ; chez Google `- solde prépayé vu (USD) : …` ;
   - fichier des règles : le gabarit sans sa ligne `- état : gabarit`, avec `- empreinte du texte en vigueur : …` ;
   - ligne du registre des GO : huit colonnes, type `calcul`, plafond écrit comme au gabarit (`0,25 USD`…), périmètre qui porte les marques du gabarit et l'empreinte du devis.
7. **Essais des relais** : dans le seul fichier d'essais ; les deux relais citaient un fichier d'essais à part, qui n'existe pas (en-têtes corrigés).

## 4. Ce qui reste ouvert

1. **Contre-lecture du code** par un agent neuf d'un autre modèle, puis vérification de ses corrections (devis, 12.11). Rien ici ne la remplace.
2. **La voie réelle des relais n'est pas éprouvée** : connexion chiffrée vers l'amont et tunnel par le mandataire du réseau. Les essais ne joignent que la boucle locale ; seul le refus de tunnel est éprouvé (faux mandataire). Le premier contact réel sera l'appel de liste, gratuit, de la vérification.
3. **Formes réelles des deux services** : supposées par le devis (type `thinking`, bloc `usage` dans le flux, corps d'erreur). Le faux fournisseur suit le devis, non les services.
4. **Lancement réel** : avec le Python de `.venv` (`.venv/bin/python -I -B scripts/chef_essais_admission_bras_a_v1.py …`), non le `python3` du système que cite l'en-tête du chef : le programme de forme de l'instrument importe `controle_ia` et ses dépendances. Les deux chaînes de bout en bout l'éprouvent ainsi.
5. **Garde 7, clé de Mistral** : la relecture cherche des formes de clé connues (`sk-…`, `AIza…`, `Bearer …`). Une clé sans préfixe ne se reconnaît pas par sa forme. Les relais ne l'écrivent nulle part (éprouvé sur la valeur factice).
6. **Garde 18, faux positif possible** : si une réponse reprend plus de 20 caractères d'un champ technique du rapport, le rapport n'est pas rendu (code 8) et la file ne se rejoue pas. Non observé.
7. **Commande `regles`** : elle imprime son résultat et rend un code de sortie ; elle n'écrit aucun fichier (l'inventaire de la file est déjà scellé). La session garde la sortie.
8. **Pièces à faire par la session** (rien de payant) : configuration définitive tirée du gabarit par ligne, scellée ; fichier des règles définitif ; constat ; lignes de calcul ; liste locale des interdits au chemin du gabarit (`/home/user/hors-depot/essais-admission-bras-a-v1/interdits-v1.txt`).
9. **Durée** : le délai global de la file Mistral est de 40 heures au pire ; l'amorce et le relais doivent vivre ce temps.
10. **Essais sensibles au temps** : marges de 0,1 à 0,3 seconde à l'échelle réduite. Stables sur huit lancements de suite ici ; une machine chargée peut en faire échouer un.
11. Les quatre mineurs de la vérification du devis (v-1 à v-4) visent le texte des lignes de calcul, non le programme. Pour v-4 : la garde 12 compare le fichier des règles à la configuration, tirée par ligne ; rien à changer au code.

## 5. Commande d'essai et sa sortie

```
env -u MISTRAL_API_KEY -u GEMINI_API_KEY PYTHONPATH=src .venv/bin/python -m pytest -q -p no:cacheprovider tests/test_chef_essais_admission_bras_a_v1.py
```

Dernier lancement, 2026-11-21 vers 16:12 UTC, sur ce seul fichier :

```
........................................................................ [ 59%]
.................................................                        [100%]
121 passed in 55.11s
```

La suite entière du dépôt n'a jamais été lancée. Aucun relais n'est resté vivant après les essais (vérifié par la liste des processus).

## 6. Empreintes sha256 des fichiers livrés

| fichier | lignes | sha256 |
|---|---|---|
| `scripts/chef_essais_admission_bras_a_v1.py` | 2 369 | `4e4c9faeddd7e36852514716bdb7f14847c88fb8c91d9e49e74dd8eb6d286b48` |
| `scripts/relais_mistral_essais_admission_v1.py` | 530 | `9aa1cc859f53a6d56f147d04715a8ab9b96cca3af9a840295e1927804a3aea94` |
| `scripts/relais_google_essais_admission_v1.py` | 389 | `d24a477334277b6b63a8f201bbfffdafe5808c74db58f1f7a596ceb3b6a74cda` |
| `tests/faux_fournisseur_essais_admission_v1.py` | 321 | `311f9a89d1e96fb4504590e5c100a138c77e89ac9997e95dc0bd2b15014306fe` (inchangé) |
| `tests/test_chef_essais_admission_bras_a_v1.py` | 1 865 | `8049202ee9969878681435045e908ecd964768447052cf8ec4493c814df5b769` |
| `…/essais-admission-bras-a-v1/configuration-essais-admission-bras-a-v1-gabarit.json` | 472 | `383228b977a74122db78c294bd5466014b0d8e5497c8ea3f605bc3f10d66e6d5` (seules les empreintes des deux relais y changent) |
| `…/essais-admission-bras-a-v1/regles-admission-bras-a-v1-gabarit.md` | 23 | `4e99badef0837be28a382e0bbb674060d9c9e8f69fba9a6f6d84df9298f7520c` (inchangé) |

Cette note n'a pas d'empreinte ici : la session la scelle.

## 7. Chemins ouverts, déclarés

- **Ouverts par moi, dans la liste permise** : le mandat ; le devis (sections 0 à 13 ; sections 14 à 19 non lues) ; sa vérification ; l'inventaire ; les sept fichiers ; `scripts/lancer_relais_local_v1.py` ; `.claude/hooks/garde_calcul.py` (une recherche de lignes sur la forme du registre) ; `registres/go.md`, dix premières lignes seulement ; le texte du préenregistrement, lignes 521 à 529 seulement, par `sed -n '521,529p'`, tronquées à 60 caractères.
- **Non ouvert** : `scripts/chef_essai_mesure_lecteurs_bras_a_v1.py` (permis en lecture, pas eu besoin).
- **Lus par le programme pendant les essais, jamais affichés ni ouverts par moi** — à déclarer selon le mandat :
  - le lot des entrées `docs/notes/relance-organismes-discrets-v1/essai-mesure-lecteurs-bras-a-v1/entrees-essai-mesure-lecteurs-bras-a-v1.json`, dossier interdit « sauf si le devis en demande un fichier nommé » : le devis le nomme (sections 2 et 3, `15b62bb4…`) ; le chef et les essais le chargent et le contrôlent par empreinte ; les réponses factices des essais en tirent les seuls identifiants ;
  - le texte du préenregistrement : les deux blocs de consigne (lignes 398 à 423 et 445 à 479) et les règles (521 à 529), extraits et comparés par empreinte ;
  - les modules du programme de forme de l'instrument, nommés au gabarit (`src/controle_ia/organismes_discrets/reponses_lecteurs_v5.py`, `instrument_appariement_v4.py`, `fabrication_v3.py`, `graines_bras_a_v4.py`, `__init__.py` ; `verite_dommage/artefacts_v1.py` ; `environnements/propositions.py` ; `gardes.py`, `manifeste.py`, `scellement.py`) : importés et empreintés, non lus par moi ; je n'ai pas vérifié ce qu'ils importent à leur tour ;
  - les trois pages de prix et les deux relevés documentaires du gabarit : empreintés par un essai, non ouverts.
- **Renvois vers des chemins interdits, non suivis** : le devis et sa vérification nomment `runs/essai-mesure-lecteurs-bras-a-v1/`, le journal, `registres/depenses.md`, `docs/notes/bras-a-contre-lecture-habilitee-v1/`. Aucun n'a été ouvert, listé ni empreinté.
- **Hors du dépôt** : dans mon bloc-notes de session, trois fichiers de débogage (`dbg1.py`, `dbg2.py`, et `relais_google_dbg.py`, copie du relais de Google avec une trace) ; les essais écrivent sous le dossier temporaire de `pytest`. `.git/info/exclude` lu une fois par une commande `git check-ignore` (pour comprendre un arbre de travail « propre »).
- **Aucun chemin interdit ouvert, même par erreur.**

## 8. Journal du travail (au fil de l'eau)

1. Mandat, devis (sections 0 à 13), vérification du devis et inventaire lus. Les sept fichiers du prédécesseur sont à leurs empreintes de l'inventaire.
2. Premier lancement de la commande d'essai avant toute retouche : arrêt au premier échec (`test_chiffres_reserves_du_devis_6_4` : 0,6242 calculé contre 0,625 attendu à 0,0006 près — tolérance de l'essai trop serrée, le devis arrondit au millième supérieur).
3. Chef d'essai (`scripts/chef_essais_admission_bras_a_v1.py`, 2 336 lignes) lu en entier : il paraît complet de bout en bout (gardes d'avant départ, vérification, files, rapport, règles, relais, inventaire).
4. État trouvé : 117 essais, 80 passent, 37 échouent. Cause principale : le relais de Google rendait toujours « 502, coupure_amont » — il réglait le délai sur une prise que `http.client` détache après toute réponse qui annonce la fermeture (`Bad file descriptor`). **Corrigé** dans `scripts/relais_google_essais_admission_v1.py` : la prise de l'amont est doublée (`os.dup`), le délai total est tenu par une minuterie qui coupe l'amont, la fermeture du client coupe l'amont. Même doublement dans `scripts/relais_mistral_essais_admission_v1.py` (la fermeture du client pendant un silence de l'amont ne fermait pas l'amont quand la réponse annonçait la fermeture).
5. Relais : la réponse, la connexion et le double de la prise sont fermés explicitement en fin d'envoi (sans cela, l'essai de la garde 19 « le faux fournisseur voit la connexion fermée » échouait par intermittence, une fois sur deux en suite entière).
6. Défauts des essais du prédécesseur, corrigés dans `tests/test_chef_essais_admission_bras_a_v1.py` :
   - quatre tolérances trop serrées devant des chiffres que le devis arrondit au millième ou au centime supérieur (0,6242 écrit 0,625 ; 2,67045 écrit 2,68 ; 0,2727 écrit 0,28 ; 8,142 écrit 8,15) ;
   - plusieurs cas d'un même essai jouaient la même ligne de vérification sous la même ligne de calcul : le second héritait du relevé clos du premier (un cas passait même à vide, celui du majorant démenti à la sonde). Chaque banc suivant d'une même ligne joue maintenant sous une ligne de calcul à lui ;
   - en regard, `jouer_verification` refuse maintenant de jouer une ligne close (auparavant seul `gardes_avant_depart` le refusait).
7. Après ces corrections : 116 essais sur 117 passent, quatre lancements de suite ; le dernier (empreintes des pièces du gabarit) attend la régénération des empreintes des deux relais au gabarit, faite en fin de travail.
8. Ajouts au chef : la réponse est fermée explicitement en fin d'envoi (la coupure atteint le relais, puis l'amont) ; la configuration de la ligne est copiée au dossier (devis, section 8, « Gardé ») ; garde de voie d'essai (garde 14) : une configuration qui n'est pas « definitive » ne joint que le faux fournisseur local, une configuration définitive ne porte aucune adresse d'essai ; état de configuration fermé (« definitive » ou « essai ») ; échec propre si le dossier de la ligne existe déjà. Les vingt gardes sont nommées « garde N » en minuscules (les gardes 2, 11 et 16 ne l'étaient qu'avec une majuscule).
9. Essais ajoutés : les relais tiennent la clé et elle seule (clé du client retirée, variable effacée, borne d'appels, plafond en dollars du relais de Mistral, chemins refusés) ; forme de clé dans une pièce gardée, de bout en bout, code de sortie 7 ; la fermeture du client ferme l'amont pendant un silence (les deux relais) ; voie d'essai. **120 essais passent**, deux lancements de suite. Empreintes des deux relais régénérées au gabarit de configuration.
10. Chaîne de bout en bout ajoutée chez Mistral (vérification, puis file de 24 lectures) : 121 essais passent, trois lancements de suite. Note achevée.
