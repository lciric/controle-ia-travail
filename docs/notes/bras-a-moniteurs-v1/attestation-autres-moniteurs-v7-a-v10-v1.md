# Attestation — aucun calcul de moniteur ne change de la version 7 à la version 10 du module des autres moniteurs du bras A (demande 24 a) — v1

**Pièce habilitée** (elle cite le différentiel, qui porte du code de moniteur). Ce qui est transmissible est dans `reponses-sans-interne-demandes-18-19-24a-v1.md`, même dossier.

Écrit par le développeur habilité côté moniteurs (agent neuf, mandat v3, `374af248…`), le 20 novembre 2026, sous GO-2026-11-20-21. Classe B. Aucun résultat lu, aucun poids chargé, aucune dépense.

## 1. Pièces comparées

| pièce | chemin | empreinte | commit |
|---|---|---|---|
| version 7 | `src/controle_ia/organismes_discrets/bras_a_v2_habilite/autres_moniteurs_v7.py` | `3b5dccc931c1ed54816a703bbc774371518ecea3fd825dfa384026cabf461531` | sur la branche |
| version 8 | `…/autres_moniteurs_v8.py` | `61105129f58f5df590b033c183e7ab334f56a51cc03bb04e86ebdb52e6e53760` | `18f63f40` |
| version 9 | `…/autres_moniteurs_v9.py` | `08a8f5c532e350045b0ab8a640525f6f839f47a2a9dc48dad6655b1dec9b13d2` | `92842ac54` |
| version 10 | `…/autres_moniteurs_v10.py` | `42c78bd5b10e970d98adf2b388f290d92e79d0a62b3de82937c91bb70949bd6c` | `d5602cd57` |
| différentiel 7 → 10 (`diff -u`, 853 lignes) | `docs/notes/bras-a-moniteurs-v1/attestation-autres-moniteurs-v7-a-v10-v1/differentiel-autres-moniteurs-v7-a-v10.diff` | `aacb9f64341c3278400f34ed8af8843cdabf265bc67653b390a137a1a1b9a402` | — |
| essai d'équivalence : script | `…/attestation-autres-moniteurs-v7-a-v10-v1/essai_equivalence_v7_v10.py` | `8cd371e3ece20dd84e7ccec8eda61b020b9fe3f8281bdd6479e01a67692281fd` | — |
| essai d'équivalence : relevé de la première passe | `…/attestation-autres-moniteurs-v7-a-v10-v1/releve-essai-equivalence-v7-v10.md` | `8c224b267e3c4f2def650ccfb026435d2f527059f398c611805c8fcc41eddcfb` | — |
| essai d'équivalence, version 2 : script et relevé | `…/essai_equivalence_v7_v10_v2.py` ; `…/releve-essai-equivalence-v7-v10-v2.md` | `c24d17ff4cbf8f9061f545d1382a049855234c089ce957c59b493e60491dfb21` ; `f36336132e2e11606d08aef9722bb2eafd83952766e620c756bfcd14d8bcb8c7` | — |
| version 11 (pour le lanceur) et différentiel 10 → 11 (26 lignes) | `…/autres_moniteurs_v11.py` ; `…/attestation-autres-moniteurs-v7-a-v10-v1/differentiel-autres-moniteurs-v10-a-v11.diff` | `e1130dadd1ee7f7ac1c8c19ab3edf69ca837f0fc016d681f0ef3e6956a927fda` ; `b7ac6de62b8e0c7c5c8619dd29cd7af2b56a6b07fe2cfba27e15639fb4a19d0a` | — |

## 2. Attestation

**Aucun calcul de moniteur ne change de la version 7 à la version 10.** Le score de chaque unité de chaque moniteur (sac de mots, traits de surface, ajustement et notation des deux moniteurs appris ; scores reçus du moniteur boîte noire, de l'agrégateur et du juge ; statistique d'épisode de l'agrégateur), l'aire et les aires des deux plis, la borne haute et ses tirages, les plis et les graines sont calculés par les mêmes fonctions, sur les mêmes arguments, dans le même ordre de tirage. Sous la permutation « libre par épisode », la seule de la version 7, les valeurs p le sont aussi : la branche libre de `_permuter` est le code de la version 7, mot pour mot, et consomme le générateur dans le même ordre.

Trois précisions, sans lesquelles l'attestation serait trop large :
1. **Un calcul neuf, ajouté et non changé** : la permutation « échange par paire » (version 8), retenue pour le bras A. Sous elle, les valeurs p viennent d'un schéma de permutation que la version 7 n'avait pas. L'aire, les scores et la borne n'en dépendent pas. Ce schéma est couvert par les gardes `exiger_etiquettes_par_paire` et `exiger_permutation`, et par les épreuves par retrait des versions 9 et 10.
2. **Ce qui est rendu change, non ce qui est calculé** : aux cas C, D et E, la version 10 rend des nombres que la version 7 calculait (aire et aires des plis ; aux cas D et E, valeurs p et nombre d'aires au moins égales) puis ne rendait pas ; l'aire observée est calculée avant les permutations au lieu d'après, par la même fonction, qui ne lit pas le générateur ; les motifs d'un moniteur appris non ajusté sont une étiquette neutre ; le fichier par unité peut porter le rang de l'unité dans son pli au lieu de son score (forme « rang ») ; la sortie est écrite et gardée par le module.
3. **Un nombre rapporté sans état change de choix** : en version 7, les deux champs de sensibilité de l'agrégateur portaient l'aire sous les deux statistiques non retenues ; depuis la version 9, ils portent toujours les deux mêmes, quelle que soit la statistique retenue. Chaque aire est calculée de la même façon ; seul change lequel des trois calculs est rapporté dans ces deux champs, qui n'entrent dans aucun état.

## 3. Le différentiel, morceau par morceau

| morceau du différentiel | nature | calcul changé ? |
|---|---|---|
| en-tête : paragraphes des versions 8, 9 et 10 ; phrase sur les cas D et E | texte | non |
| `PROGRAMMES_DE_PRODUCTION` | provenance (empreintes des deux programmes de production) | non |
| `CHAMPS_RANG`, `FICHIER_RANGS`, `FORMES` | forme du fichier par unité | non |
| `PERMUTATION_LIBRE`, `PERMUTATION_PAR_PAIRE`, `PERMUTATIONS` | noms des deux schémas | non |
| `NOMBRES_RENDUS` (trois phrases) | liste des nombres rendus | non |
| `MOTIFS`, `MOTIF_CLASSE_ABSENTE`, `NON_AJUSTABLE`, `ETIQUETTE_STATISTIQUE`, `FICHIER_SORTIE`, `CLES_REGLAGES` | listes fermées, étiquettes, nom de la sortie | non |
| `ETATS_BALISE` : cinquième état | liste fermée des lignes de production (suit le module des deux moniteurs, version 3) | non |
| `_paires_de_la_tache`, `exiger_etiquettes_par_paire`, `exiger_permutation` ; `_permuter(rng, pp, permutation)` | branche libre : code de la v7 ; branche par paire : **neuve** ; gardes | libre : non ; par paire : calcul neuf (précision 1) |
| `exiger_forme`, `rangs_dans_le_pli`, `ecrire_les_scores(…, forme)` | forme du fichier par unité ; le rang est calculé sur les scores déjà calculés | non (forme de ce qui est écrit) |
| `_conclure(…, a, …)` | aire reçue (calculée avant les permutations) ; nombres rendus aux cas C, D, E ; motif « tirages dégénérés » illisible : arrêt | non (précision 2) |
| `lire_moniteur_appris`, `lire_scores_fixes` | paramètre `permutation` transmis ; motifs neutres ; `a = _aire(M, scores, pp)` avant la boucle | non |
| `exiger_ordre_des_identifiants`, `empreintes_des_programmes`, `exiger_programmes`, `ecrire_la_production`, `lire_la_production` | gardes et provenance de la production | non |
| `STATISTIQUES_RAPPORTEES`, `autres_statistiques` | choix des deux statistiques rapportées sans état | non (précision 3) |
| `exiger_resultat`, `cas_de_la_lecture`, `cas_du_motif`, `exiger_forme_du_cas`, `exiger_sortie`, `exiger_preuve_d_ordre`, `exiger_comptes_des_lectures`, `exiger_dossiers_disjoints`, `_entier`, `_que_des_entiers` | gardes de forme | non |
| `empreinte_du_module`, `assembler_la_sortie`, `ecrire_la_sortie` | provenance, assemblage et écriture de la sortie | non |
| `lire_les_cinq` | paramètres `permutation`, `forme_du_fichier_par_unite`, `dossier_de_la_sortie` ; gardes de dossiers ; assemblage par `assembler_la_sortie` | non |

Aucune ligne de `former_pp`, `Lexical`, `traits_de_surface`, `Surface`, `_episodes_de_la_tache`, `exiger_etiquettes_par_episode`, `_aire`, `_borne_haute`, `exiger_ligne_de_score`, `collecter_les_scores`, `_resultat`, `unites_avec_scores`, `episodes_agreges`, `empreinte_des_scores`, des fonctions du journal et du registre, de `tirer_la_table_opaque`, `lire_la_table_opaque`, `comptes_des_lectures`, `plis_communs`, `cles_des_graines`, `charger_piece_source` n'est dans le différentiel : ces fonctions sont identiques. Les constantes des réglages (2 000, 2 000, quinze, 0,05, 1 %) et des traits de surface sont hors du différentiel.

## 4. Essai d'équivalence

Mêmes entrées construites à la main, mêmes plis, mêmes graines, permutation libre, 300 permutations et 300 tirages ; un moniteur lu sur des scores et les deux moniteurs appris, deux doses, deux jeux (tout calculable ; intervalle impossible faute de tâches). Relevé :

| jeu | lectures (3 moniteurs × 2 doses) | nombres comparés par lecture | différents |
|---|---|---|---|
| tout calculable (cas A en v10) | 6 | 14 : aire, deux aires des plis, deux valeurs p, valeur de la famille, aires au moins égales, deux comptes de permutations, borne haute, quantile, deux comptes de tirages, effectifs | **aucun**, au bit près |
| intervalle impossible faute de tâches (cas E en v10) | 6 | 3 que les deux versions rendent : deux comptes de permutations, effectifs | **aucun** ; la valeur de la famille vaut 1 en v7 et la valeur p haute en v10, comme la forme du cas E le veut (vérifié à part, les six fois) ; aire et valeurs p rendues par la v10 seule |

Verdict de l'essai : aucun nombre commun ne diffère.

**Audit d'un écart de la première passe (R4).** La première version du script (`essai_equivalence_v7_v10.py`, `8cd371e3…` ; relevé `releve-essai-equivalence-v7-v10.md`, `8c224b267e3c4f2def650ccfb026435d2f527059f398c611805c8fcc41eddcfb`, gardés tels quels) comptait au cas E la valeur de la famille parmi les nombres communs et rendait « NON » sur les six lectures du cas E. Cause : ce nombre change de règle par décision (1 en v7, valeur p haute en v10, GO-2026-11-19-70), ce n'est pas un calcul de moniteur. La version 2 du script (`essai_equivalence_v7_v10_v2.py`, `c24d17ff4cbf8f9061f545d1382a049855234c089ce957c59b493e60491dfb21`) le sort de la comparaison, vérifie la règle à part, et écrit pour chaque lecture la liste des nombres comparés et des nombres différents ; relevé `releve-essai-equivalence-v7-v10-v2.md`, `f36336132e2e11606d08aef9722bb2eafd83952766e620c756bfcd14d8bcb8c7`.

## 5. De la version 10 à la version 11

Le différentiel (26 lignes) ne porte que le paragraphe « Version 11 » de l'en-tête et les deux lignes de la préparation dans `PROGRAMMES_DE_PRODUCTION` (version 3 et son empreinte). Aucun calcul, aucune garde ne change ; un essai (`tests/test_bras_a_v2_habilite_autres_moniteurs_v11.py`, `test_la_seule_difference_avec_la_version_10`) le vérifie sur les fichiers.
