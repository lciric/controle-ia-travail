# Rapport du développeur du code de formation des familles d'adaptateurs jumeaux (barreau 5) — v1

- Développeur : Claude Opus 5.5, sous-agent de la session mère. Pièce d'instrument (classe B), à contre-lire par un autre modèle. Écrit le 20 novembre 2026 (UTC).
- Mandat : `docs/notes/barreau5-resolution-v1/plan-avant-entretien/mandat-developpeur-code-formation-v1.md`, `94c6bbb3703db96efec0fcd5dd752cec38a79bb0a253a33a9c2fa99846152cda` (vérifié).
- Texte suivi : le brouillon 2 d'abord, puis le brouillon 3, `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-brouillon3.md`, `525f338e7899e6a8f57b73fffef7f0eeef3d6a16eee0e7d6c2823cddb44c9e50`, sur ses sections figées pour la formation. Le brouillon 3 n'est pas encore vérifié par son contre-lecteur. J'ai lu aussi la table des corrections `table-corrections-plan-brouillon3-v1.md`, aux lignes qui touchent la formation.
- Arbre de travail : `/home/user/controle-ia-travail/.claude/worktrees/agent-a413b4f708eb5909b`. Aucun commit, aucune poussée, aucune dépense, aucun lancement sur carte. Je n'ai vu aucune donnée.
- **Incident : un refus d'outil.** La garde d'isolement de l'arbre a refusé une commande Python composée qui modifiait un fichier. Je me suis arrêté et l'ai rendu. La mère a précisé la suite : fichiers modifiés seulement par les outils d'édition, essais lancés par des commandes simples. Je n'ai pas rejoué la commande refusée. Aucun autre refus.
- **Incident déclaré.** Deux sorties de commande trop longues ont été déposées par l'outil sous `/root/.claude/…` : un `cat` de `t06/lanceur.py`, et un `sed` du brouillon 3. Je n'ai pas ouvert ces fichiers. Seul l'aperçu automatique s'est affiché ; je les ai relus depuis le dépôt, par morceaux.

## 1. Modules et fonctions publiques

Paquet neuf `src/controle_ia/barreau5_familles/` (R12) ; aucun module existant n'est modifié.

**`edition_cout_v1`** : l'opérateur d'édition du coût (plan, point 3).
- `mantisse`, `grille_famille` : grille de la famille.
- `valeur_sur_grille` : valeur.
- `decrire_ecriture`, `ecrire_nombre` : écriture.
- `localiser_nombre_du_cout`, `action_editable`.
- `positions_des_jetons`, `episser` : épissure des jetons.
- `controler_edition` : contrôles par action.
- `editer_action`, `editer_tirage`.
- `controler_famille` : contrôles par famille.
- `exiger_transcriptions_egales_hors_nombre`.

**`engagement_v1`** :
- sel, noms et table : `tirer_sel`, `noms_opaques`, `table_des_etiquettes`, `empreinte_table`, `exiger_table_coherente`, `ecrire_table`, `lire_table` ;
- registre propre : `lignes_du_registre`, `lire_registre`, `ligne_du_registre`, `ligne_engagement` ;
- vérifications : `verifier_engagement_avant_lecture`, `verifier_table_a_l_ouverture` ;
- entrées de la session de lecture : `preparer_entrees_de_lecture`, `exiger_entrees_de_lecture_propres`, `charger_entree` ;
- `maintenant_utc`.

**`formation_v1`**, côté instance :
- marche : `executer`, et la ligne de commande en mode réel seulement ;
- configuration et tâches : `exiger_config_b5f`, `exiger_recette`, `charger_taches_b5f`, `exiger_taches_disjointes`, `exiger_taches_d_evaluation`, `exiger_nombre_de_taches` ;
- graines et plis : `cles_de_famille`, `cles_des_graines`, `partition_plis`, `taches_d_evaluation`, `graine_entiere` ;
- génération : `jouer_sans_activations`, `jouer_scripte_jouet` (mode jouet seulement), `tirer_famille` ;
- membres et distillation : `membres_de_famille`, `empreinte_etat`, `exiger_meme_etat_initial`, `ordre_des_membres`, `distiller_famille` ;
- évaluation : `evaluer_membre` ;
- point 5 de la liste d'arrêt : `lectures_internes_interdites`, `exiger_aucun_crochet`, `proteger_modele`, `exiger_sorties_permises` ;
- dépense : `garde_depense`, `decision_coupure` ;
- versement : `inventaire_sorties`, `ecrire_inventaire`, `exiger_versement` ;
- registre propre : `lire_code_et_accord`, `exiger_code_au_commit`.

**`formation_v1`**, côté session (sous-commande `session`, appelée par le lanceur) :
- `etiquette`, `charger_garde_de_calcul`, `exiger_garde_de_calcul` ;
- `commande_de_creation`, `exiger_etiquette`, `commande_de_destruction`, `absence_prouvee`, `depense_session`.

**`scripts/lancer_b5f_formation_v1.sh`** : sous-commandes `plan`, `commande`, `depense`, `detruire`, `verifier-destruction`. Le lanceur ne crée, n'arrête ni ne détruit rien : il contrôle et imprime les commandes, que la session de formation joue.

## 2. Garde → essai sain → essai artefact

Fichiers d'essais :
- (E) `tests/test_barreau5_familles_edition_cout_v1.py` ;
- (G) `tests/test_barreau5_familles_engagement_v1.py` ;
- (F) `tests/test_barreau5_familles_formation_v1.py` ;
- (L) `tests/test_lancer_b5f_formation_v1.py`.

| garde | cas sain | artefact |
|---|---|---|
| édition : nombre simple, milliers (virgule, espace), suffixe « k », virgule décimale | E `test_edition_cas_sains_…` (2 tokeniseurs, dont un à jetons de 1 à 3 chiffres) | E `test_edition_artefacts_intervalle_champ_sans_nombre_multiplication_refuses`, `…_intervalle_a_un_seul_nombre…`, `…_action_non_valide…` |
| φ = 1 rend les identifiants d'origine | E `test_facteur_1_rend_les_identifiants_d_origine_et_la_valeur` | E `test_artefact_facteur_autre_que_1_change_les_identifiants` |
| φ = 3 puis φ = 1/3 sur la grille rendent la valeur de départ | E `test_facteur_3_puis_un_tiers_…` (10 mantisses × 5 puissances, dans les deux sens) | E `test_artefact_aller_retour_hors_grille_ne_rend_pas_la_valeur` |
| contrôles par action | E `test_controle_par_action_cas_sain_et_artefacts` (passe) | même essai : valeur relue fausse, identifiants tronqués, autre champ changé |
| localisation du nombre | E `test_artefact_nombre_brut_…` (occurrence vide sautée) | même essai : aucun champ du coût |
| contrôles par famille (médianes ± 0,08 ; part ≤ 10 %) | E `test_controle_par_famille_cas_sain_et_artefacts` | même essai : part trop haute ; médiane du jumeau hors tolérance |
| action non éditable pour un membre : non éditée pour tous | E `test_action_non_editable_…` | (même essai) |
| égalité des transcriptions hors des jetons du nombre | E `test_egalite_des_transcriptions_…` | même essai : un jeton du titre changé ; actions éditées différentes |
| même état initial dans une famille | F `test_meme_etat_initial_…` (même graine) | même essai (autre graine) |
| tâche de réserve dans une évaluation | F `test_taches_cas_sains_…` | même essai, au chargement et au moment de jouer |
| nombre de tâches d'évaluation (garde ajoutée) | F `test_nombre_de_taches_…` | même essai ; F `test_artefact_jouet_fichier_d_evaluation_au_mauvais_compte_…` (arrêt avant tout manifeste) |
| score de sonde ou activation sur une instance de formation (point 5) | F `test_point_5_generation_sans_activations_saine_dans_le_bloc_…` (égale, jeton pour jeton, à la génération du harnais) | F `test_point_5_artefacts_capture_sonde_et_import_refuses_puis_restaures` ; F `test_jouet_artefact_activation_lue_pendant_la_marche_arret_consigne` |
| crochets, états cachés | F `test_point_5_crochets_…` (modèle propre, appel normal) | même essai : crochet sur une couche, crochet global, `output_hidden_states` |
| sorties permises | F `test_point_5_sorties_permises_…` | même essai : `.npy`, `.npz`, « scores », « activations » |
| configuration et recette égales à la configuration scellée | F `test_configuration_reelle_cas_sain_…` | F `test_configuration_artefacts_…` : lot, familles hors plan, coupure, 8 par pli, clé « sonde » |
| mode réel sans texte ou avec générateur scripté | — | F `test_artefact_mode_reel_…` |
| plis et tâches d'évaluation (16 par pli, mêmes pour tous) | F `test_taches_d_evaluation_seize_par_pli_…` | même essai : 40 par pli refusé |
| arrêt au cumul plus un quart d'heure | F `test_arret_au_cumul_…` ; L `test_depense_cas_sain_…` | mêmes essais : coupure atteinte, égalité, valeur illisible, plafond commun, instance hors plan |
| décision de coupure (complet, réduit, abandon) | F `test_decision_de_coupure_…` | (même essai) |
| versement prouvé avant destruction | F `test_versement_prouve_…` ; L `test_detruire_cas_sain_…` | mêmes essais : contenu changé, fichier retiré ; L : étiquette d'une autre chaîne, identifiant illisible, instance absente, sans GO_ID |
| registre propre : code et accord | F `test_registre_code_et_accord_…` | même essai : ligne absente, accord avant le code, entropie de plus de 128 bits |
| commande de création : GO_ID, commit, accord, amorce, garde de calcul | L `test_commande_cas_sain_…` (la garde de calcul du dépôt laisse passer) | L `test_commande_artefacts_…` (7 cas, motif vérifié) |
| vérification de la destruction | L `test_verifier_destruction_…` | même essai : instance présente, témoin absent |
| engagement : sel, noms, table | G `test_sel_…`, `test_table_…` | mêmes essais : sel illisible, doublon, table retouchée, réécriture (R12) |
| engagement postérieur à la création de l'instance de lecture | G `test_engagement_anterieur_…` | G `test_artefact_engagement_posterieur_ou_simultane_refuse`, `…_engagement_absent_refuse` |
| empreinte de la table différente de l'engagement, dates | G `test_ouverture_cas_sain_…` | G `test_artefact_empreinte_de_la_table_differente_…`, `test_artefacts_scores_absents_ou_dates_hors_d_ordre_refuses` |
| entrées de lecture : noms opaques, tenseurs seuls | G `test_entrees_de_lecture_…` (aucune étiquette dans les octets) | G `test_artefacts_entrees_de_lecture_…` : adaptateur manquant, étiqueté hors apprentissage, table glissée |
| jouet de bout en bout | F `test_jouet_de_bout_en_bout_…` : deux familles formées, une tenue à l'écart et une d'apprentissage ; trois membres distillés, identité passée ; aucune activation ; inventaire ; fonctions restaurées | F `test_jouet_artefact_famille_refusee_deux_fois_…` (retirage, puis famille absente, sans distillation) |

**Résultat : 129 essais, 129 passés** (72 E, 14 G, 25 F, 18 L ; 82 s au processeur). Le passage net du premier coup appelle la réserve de R4. J'ai donc vérifié à part que les artefacts du lanceur échouent pour leur motif annoncé : les motifs sont désormais exigés dans les essais. Le jouet de bout en bout vérifie aussi que les trois adaptateurs appris diffèrent.

## 3. Réemplois et fonctions neuves

**Réemployés sans modification :**
- `organismes/lora.py` : `injecter`, `charger_etat`, `fixer_dose`, `etat_lora`, empreintes ;
- `t06/distillation_transcription.py` : `transcription_honnete`, `exemple_de_transcription`, `distiller_transcriptions`, `exclure_mentions`, `adaptateurs_en_simple_precision`, `etat_initial`, `etat_en` ;
- `t06/identite.py` : `controle_identite`, `exiger_etat_de_phase`, `logits_de_controle` ;
- `t06/cout.py` : lecteur gelé et motifs ;
- `harnais.episode.generer_lot` et les classes `Action`, `Transcription`, `Episode` ;
- `pilote_a` : `charger_taches`, `graines_des_actions`, `tache_de` ;
- `premier_test_ia.conditions` : `charger_consignes`, `environnement`, `mesures_action` ;
- `lancer_pilote_a` : `charger_modele_et_format`, `conversation_de_controle` ;
- `controler_format_agent`, `regler_determinisme` ;
- `validation_reelle` : `CHEMINS_GELES`, `exiger_memoire_vive`, `noyau` ;
- `manifeste`, `scellement` ;
- `.claude/hooks/garde_calcul.py`, chargé depuis son fichier et rejoué sur la commande imprimée.

**Écrites à neuf à la place d'une fonction existante :**
- `jouer_sans_activations` remplace `jouer_episodes` et `jouer_distillation`. `jouer_episodes` fait toujours la passe unique et lit les activations (constat M-5). La boucle est la même : la génération est égale jeton pour jeton, ce qu'un essai vérifie.
- `tirer_famille` remplace `jouer_distillation` : une seule condition, la condition « saboteur », avec les graines de la famille.
- `membres_de_famille` remplace `exemples_honnetes` : elle retire les actions non éditables.
- `evaluer_membre` remplace `jouer_evaluation` : aucune activation écrite.
- `graine_entiere` est réécrite, même formule : `harnais.run_harnais_factice` importe des modules de sondes. Un essai compare les deux formules.
- **Écart au brouillon 3, « Code neuf »** : le texte dit « `distiller_adaptateur` de `t06/lanceur.py` » réemployé. J'appelle `dt.distiller_transcriptions`, la fonction gelée qu'il appelle en mode « transcription », avec les mêmes arguments. Importer `t06/lanceur.py` charge les modules de sonde et du test croisé, que la garde du point 5 met hors d'usage pendant la marche, et elle mettrait aussi `distiller_adaptateur` hors d'usage. Le calcul est le même ; seule la journalisation du progrès diffère.

## 4. Choix que le texte ne fixe pas (à trancher par le rédacteur Fable)

1. **Garde d'équivalence de la génération (M-5a).** Le brouillon 3 la permet (liste d'arrêt, point 5 : elle « n'en est pas une ») mais ne l'exige pas. **Pris : aucune garde d'équivalence**, aucune activation n'est calculée. L'ajouter demanderait des crochets en mémoire, que la garde du point 5 refuse aujourd'hui. Si le texte l'exige, il faut une exception étroite et contre-lue. Écart possible avec « mêmes réglages que la course de confirmation » (point 2), si ces mots couvrent la garde.
2. **Égalité de distance sur la grille** : la plus petite des deux valeurs.
3. **Un nombre d'origine sans séparateur de milliers** reste sans séparateur, même au-delà de 1 000 (« 300 » × 3 donne « 1000 »). Le nombre de chiffres change donc avec le sens de l'édition : c'est le constat M-1, ouvert dans la table des rivales.
4. **Suffixe « k » gardé** même sous 1 000 (« 2k » donne « 0.6k »).
5. **Grille** : les mantisses des coûts lisibles de toutes les actions du tirage, y compris les actions non valides.
6. **Part d'actions non éditables** : comptée sur toutes les actions du tirage, y compris les actions non valides, sans coût, et celles à mention. Les actions à mention sortent des cibles, mais restent éditables au sens du point 3. Risque : des familles refusées si le saboteur écrit souvent sans coût.
7. **Localisation du nombre** : le premier nombre du champ brut doit être le seul du champ et égaler la lecture du lecteur gelé, sinon l'action est non éditable.
8. **Plis** : permutation des 64 identifiants triés par `b5f/lecture/plis`, première moitié au pli 0. Les 16 tâches par pli sont tirées par `b5f/evaluation/taches`. **La lecture doit réemployer `partition_plis` telle quelle.**
9. **Clés de graines hors de la liste du point 14** : `b5f/instance/<n>/injection` (graine de l'injection, sans effet : l'état initial est rechargé par famille), `b5f/modele-jouet`, et `b5f/famille/<k>-r1/…` pour le retirage.
10. **Répartition des familles sur les instances** : T01 et T02 sur l'instance 1, … T09 et T10 sur l'instance 5, A1 et A2 sur la 6, A3 sur la 7. Coupures du devis : 26, 24 et 15 USD.
11. **Format des lignes du registre propre** : « | CLÉ | AAAA-MM-JJTHH:MM:SSZ | contenu | référence | », une ligne par clé. Le contenu :
    - de `CODE-FORMATION-B5F` : « commit <40> ; entropie <entier> » ;
    - de `GO-FORMATION-B5F` : l'identifiant de l'accord ;
    - d'`ENGAGEMENT-B5F` : « sha256 <64> ».
12. **Noms opaques** : ordre des HMAC-SHA256 du sel sur « famille/membre ». Fichiers d'entrée `X-NN.safetensors`, sans métadonnée. Les noms des tenseurs (noms des couches) sont les mêmes pour tous.
13. **Coupure sur l'instance (devis, § 4)** : décidée avant l'évaluation de **chaque** famille, et non de la seule seconde. Les durées d'évaluation viennent du devis (1,07/3 heure par membre pour 32 tâches, poussée 0,2 heure). La dépense est estimée par l'horloge depuis le manifeste, sans la mise en place qui le précède. En évaluation réduite, le saboteur d'apprentissage joue lui aussi les 16 premières tâches.
14. **Mode jouet** : actions écrites par programme pour le tirage (le modèle jouet n'écrit pas d'action lisible) ; le mode réel les refuse.
15. **Sorties** : `donnees/<run>/<famille>/` contient :
    - `adaptateur-<membre>.pt` ;
    - `textes-distillation.jsonl` : identifiants et textes d'origine, table d'édition par action ;
    - `evaluation-<membre>.jsonl`.
    
    Les résultats vont dans `diag/<run>/`, par `ecrire_resultat`. Tout est scellé, et l'inventaire couvre le tout.

## 5. Écarts au brouillon 3, et ce qui changerait si les sections figées bougeaient

**Alignés** :
- familles T01 à T10 et A1 à A3 (m-4a) ;
- préfixe `X-` (m-4b) ;
- versement en un seul dossier, dans l'ordre des noms opaques, tenseurs seuls (m-12b) ;
- les trois enveloppes de M-5 ;
- liste d'arrêt 5 dans la forme de M-5a : rien n'est écrit sur disque ;
- points 1 à 6, 14 et 17.

**Écarts** :
- l'appel de `distiller_adaptateur` (§ 3) ;
- la garde d'équivalence non jouée (choix 1) ;
- `b5f/lecture/plis` employé dès la formation (choix 8).

**Si les sections figées bougeaient :**
- **Nœud 5 (témoin à changement bénin, quatrième membre)** : il faut un second opérateur d'édition, un membre de plus dans `FACTEURS` et dans `MEMBRES_TENUE`, un contrôle de famille propre à ce membre, et les essais correspondants. Rien d'autre ne change : les membres sont génériques.
- **Marqueur M-6 (« autre règle »)** : seule `valeur_sur_grille` du jumeau changerait.
- **Préfixe ou noms des familles** : une constante chacun.
- **Nombre de tâches, plis ou coupures** : des constantes, gardées en mode réel.

## 6. Ce qui reste à faire, et commande des essais

- **L'amorce d'instance** `scripts/amorce_b5f_formation_v1.sh` : clonage au commit de `CODE-FORMATION-B5F`, installation, configuration de l'instance, marche, poussée de chaque famille dès qu'elle est formée, inventaire. Elle n'est pas écrite : le texte ne la nomme pas, et le lanceur **refuse toute commande de création tant qu'elle manque**.
- La configuration réelle par instance, avec son champ `prix_usd_h` relevé au lancement.
- La contre-lecture de ce code par un autre modèle, puis la vérification des corrections.
- Les choix du § 4 tranchés par le rédacteur.
- Aucun essai sur carte n'a été fait. Sur la vraie chaîne, la garde « aucun crochet » suppose un modèle chargé sans `device_map` : c'est le cas de `charger_modele`, mais je ne l'ai pas éprouvé sur carte.

Commande des essais, depuis la racine de l'arbre (une seule commande) :

```
PYTHONPATH=src /home/user/controle-ia-travail/.venv/bin/python -B -m pytest -q -p no:cacheprovider tests/test_barreau5_familles_edition_cout_v1.py tests/test_barreau5_familles_engagement_v1.py tests/test_barreau5_familles_formation_v1.py tests/test_lancer_b5f_formation_v1.py
```

## 7. Empreintes des fichiers de code (calculées à la fin)

| fichier | sha256 |
|---|---|
| `src/controle_ia/barreau5_familles/__init__.py` | `ece81c5b489adcda2387390c2b368468ba046c97c76e3132ffbfb925a87b5569` |
| `src/controle_ia/barreau5_familles/edition_cout_v1.py` | `eb967ac1f1295cf05533780d9cc29e7b570c113928dc42d9708521e96dc52a89` |
| `src/controle_ia/barreau5_familles/engagement_v1.py` | `98e67bb6860bd796bf87fae2c166cb8ef54aab5b212662fb63a5ed9c1444ef70` |
| `src/controle_ia/barreau5_familles/formation_v1.py` | `d32f70381a98b346ad5794c1ea446debb755a37923e46bb2d512b6f26b628530` |
| `scripts/lancer_b5f_formation_v1.sh` | `380bbab2c50fa0731612ff61fbc5784ef12fea83b092d1f90dba1e04e6bdca60` |
| `tests/test_barreau5_familles_edition_cout_v1.py` | `95d8cc5c3c1b7b9508a09f12d03f6c2540275a583a8b7fa4afce11398db7ce04` |
| `tests/test_barreau5_familles_engagement_v1.py` | `a12ff584af0b901b8504f378b72030eaaf381f69dc6510269cadc55020b00ab4` |
| `tests/test_barreau5_familles_formation_v1.py` | `963cef77b6471d7e699b278c0f94dcc5b400f603340e72e560e45863cec09e44` |
| `tests/test_lancer_b5f_formation_v1.py` | `598c7b0a777ef00274738935db05a605c783a7c455f4c6a5aff85295359ea75d` |

Ces fichiers ne sont pas scellés par un compagnon `.sha256` : la mère les scelle au versement.
