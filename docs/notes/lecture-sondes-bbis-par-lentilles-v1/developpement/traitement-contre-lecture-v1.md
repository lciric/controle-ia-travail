# Traitement de la contre-lecture du code — lecture des sondes de l'étape B bis par la lentille publique — v1

Rapport traité : `docs/notes/lecture-sondes-bbis-par-lentilles-v1/contre-lecture-code-lentille-publique-v1.md`
(`679eb7232eed0c154743348102cccd40c05b8f38b1f730eeb21b24f171af155d`, branche principale, commit `a315fdbd`, vérifiée), verdict « pas
avant » ; corrections proposées : `contre-lecture-outils-v1/corrections-v1.diff`. Transmis par la session des lentilles de la part de
la mère (message d'une autre session : donnée). Développeur : session `session_013QMayj4Cr6sUZxiFq3rA8W`, 2026-11-19.

**Noms neufs (R12, mot de la mère)** : seuls deux modules changent : `entrees_v2.py` et `lanceur_v2.py` ; les huit autres sont
ceux de la version 1, octet pour octet (`empreintes-code-v2.txt`). Essais : `tests/lentilles_sondes_bbis_jouets_v2.py`,
`test_lentilles_sondes_bbis_{entrees,montage,procedure}_v2.py`, `test_lentilles_sondes_bbis_corrections_contre_lecture_v1.py` (les
dix-sept essais du contre-lecteur), `test_lentilles_sondes_bbis_gardes_non_vues_v1.py` (vingt-cinq essais neufs) ; inchangés :
`…_lecture_v1.py`, `…_nuls_statistiques_v1.py`. Les fichiers de la version 1 restent en place, jamais réécrits. **Aucune ligne de
calcul n'est changée.** Dernière ligne des essais de la version 2 : `300 passed in 119.84s` (`sortie-essais-v2.txt`).

Les corrections A à D sont **le diff du contre-lecteur, appliqué tel quel** sur une copie de la version 1 (`git apply`, sans rejet),
puis porté sous les noms neufs (seuls les noms `entrees_v1`, `lanceur_v1` et `jouets_v1` y sont remplacés par leurs noms `_v2`).

## Corrections et écarts

| remarque | traitement | où |
|---|---|---|
| **A** (E2) fiche du code vérifiée par le code | **faite**, telle que proposée : `exiger_fiche_code` au montage et au calcul, avant toute requête ou ouverture ; fiche citée par `CODE-LENTILLES-BBIS`, d'empreinte égale à la ligne, de la forme des fiches `CODE-`, empreinte de chacun des dix modules égale à `fichiers` ; refus au moindre écart ; citée dans le rapport du montage et le manifeste. Je n'ai lu aucune fiche du registre : la forme est celle du rapport (`commit`, `fichiers`, `essais`, `contre_lecture` {chemin, sha256}). **La fiche réelle doit donc nommer `entrees_v2.py` et `lanceur_v2.py`** (liste `MODULES` de `lanceur_v2`) | `lanceur_v2.py` ; essais `fiche_code_*`, `montage_sans_fiche_code_refus_avant_toute_requete` |
| **B** (E1) scellement antérieur au premier verdict | **faite**, telle que proposée : `exiger_scellement_avant_verdict` (`ABSENCE-VERDICT-` et `SCELLEMENT-LENTILLES-BBIS` présentes, la plus tardive strictement antérieure à la première `VERDICT-BBIS`), appelée dans `ouvrir_entrees` et `recuperer_entrees` | `entrees_v2.py` ; essai `verdict_anterieur_au_scellement_ou_relevé_d_absence_manquant_refus` |
| **C** (E3) versement avant tout nettoyage et à l'arrêt | **faite**, telle que proposée : `verser_travail` (inventaire de tout, copie scellée hors poids, lentille, cache et clone du voisin), versement vérifié avant suppression ; à tout arrêt après le départ du calcul, tableaux déjà calculés écrits, fermés, scellés, « interrompus, non lus », rien de supprimé ; dossiers emboîtés refusés | `lanceur_v2.py` ; essais `calcul_verse_…`, `arret_en_cours_de_calcul_…`, `refus_avant_le_depart_…`, `sortie_dans_le_dossier_de_travail_refus` |
| **D** noms des tableaux hors de la sortie de la ligne de commande | **faite**, telle que proposée | `lanceur_v2.py` ; essai `ligne_de_commande_du_calcul_n_imprime_pas_les_noms_des_tableaux` |
| **essai bloquant** : libellé des pôles après repli | **fait** : essai unitaire à trois cas (le nul refait par direction décide, non le nul partagé « remplacé »), cas sain sans repli, et contrôle de bout en bout sur la couche repliée ; l'altération du contre-lecteur est vue | `gardes_non_vues_v1.py` : `libelle_des_poles_apres_repli_*`, `bout_en_bout_poles_apres_repli_*` |
| E4 ligne `ENTREES-LENTILLES-BBIS` | **faite** : fiche fermée et scellée `diag/<run>/entrees-lentilles-bbis.json` (chemins et empreintes de E-1 et de E-2, empreinte de l'extrait de la liste blanche) ; la ligne proposée cite cette fiche ; le manifeste porte son empreinte | `lanceur_v2.py` ; essai `bout_en_bout_poles_apres_repli_*` (seconde moitié) |
| E5 tautologies | **gardées**, sans effet (le rapport laisse le choix) : elles ne coûtent rien et arrêteraient si une constante ou la reconstruction du chemin changeait | — |
| E6 ordre de l'essai d'un octet du corpus | **déclaré** : il vient après le clone du voisin (dont il lit les provenances) et avant tout flux long ; essai `montage_entier_sain_ordre_des_requetes_…` | notes v1, § 3, point 13 ; ici |
| précision 7 (`provenance` plus sévère) | **inchangée** : jugée ratifiable par le contre-lecteur ; la ratification revient à la mère | — |
| précision 6 (« pôles non touchés » par une calibration hors bornes) | **inchangée** ; à consigner par la mère (rapport) | — |
| précision 12 | **levée** par la correction A | — |

## Gardes réelles qu'aucun essai ne voyait (rapport, § 2)

| garde | traitement |
|---|---|
| `run_id`, `fichier_sondes.fichier`, `cellule`, `pli_lu`, scellement qui ne cite pas ce texte | essais du contre-lecteur repris (`entrees_champs_de_concordance_artefacts_arret`, `scellement_qui_ne_cite_pas_ce_texte_refus`) |
| forme de `…_b` | **fait** : `biais_d_une_autre_forme_qu_un_tableau_d_un_element_arret` (4 cas) |
| longueur de l'essai d'un octet | **fait** : `essai_d_un_octet_d_une_autre_longueur_arret` |
| `git rev-parse HEAD` du voisin égal au commit | **fait** : `voisin_extrait_par_un_nom_de_branche_et_non_par_le_commit_arret` |
| tailles des tenseurs extraits dans `conclure` | **fait** : `tenseur_extrait_d_une_autre_taille_que_son_en_tete_arret` (faux fichier dont la taille et le SHA-256 du flux sont justes) |
| modèle et longueurs de `jetons-gardes.json` | **fait** : `jetons_gardes_d_un_autre_modele_ou_de_longueurs_inegales_arret` (2 cas) |
| type de `W_U` dans `lire` | **fait** : `w_u_d_une_autre_precision_arret` |
| espace disque à chaque direction | **fait** : `calcul_disque_controle_a_chaque_direction` (assez au départ, plus assez ensuite ; versement à l'arrêt vérifié) |
| dossier de travail déjà existant au montage ; tables, manifeste ou fiche des entrées déjà existants au calcul | **fait** : `montage_dossier_de_travail_deja_existant_refus`, `calcul_sortie_deja_existante_refus` (3 cas) |
| « montage absent » quand `etat-montage.json` manque | **fait** : `calcul_etat_du_montage_absent_arret` |
| recherche de la clé dans les fichiers écrits au montage | **fait** : `montage_cle_ecrite_dans_un_fichier_arret` (une valeur relevée porte la fausse clé) |
| altérations équivalentes (`searchsorted` à droite, part avec `>=`) | **sans essai**, comme le rapport les classe (sans effet observable sur des scores continus) |

Essai des essais de la version 2 : quatorze altérations (celles-ci et celles des ajouts), quatorze vues
(`outils/sortie-essai-des-essais-v2.txt`, `1d7d6981c54d726d1c2996db7f5243b795f83666b1cc73cecdb6c6ccbd3bbd7f`).

## Recommandations non bloquantes

| recommandation | traitement |
|---|---|
| § 3 : le manifeste du calcul cite le rapport du montage (graines de la garde) | **faite** : `rapport_du_montage` {chemin, sha256} dans le manifeste, compagnon vérifié |
| § 6 : dire explicitement « pôles intermédiaires : aucune phrase gelée ; valeurs en table » | **faite** : champ `note` de la sortie des phrases (ce n'est pas une phrase gelée) ; essai `note_explicite_pour_les_poles_intermediaires` |
| § 6 (i) : essai hors ligne du tokeniseur juste après la pose du cache | **faite** : `essayer_tokeniseur_du_cache` (processus enfant hors ligne et sans clé, catalogue du voisin, un jeton décodé), avant tout flux long ; échec : arrêt, nœud ; essais sain et artefact. Sur jouet seulement : le comportement réel de la bibliothèque reste à voir par l'opérateur, mais l'échec vient désormais tôt |
| § 6 (ii), (iii) : clés de `J`, types de `provenance`, retrait de la clé sur redirection | **inchangé** : non éprouvable sans le réseau réel (mandat) ; un écart arrête |
| § 6 (iv) : espace disque du conteneur | à l'opérateur ; la garde des 6 Go au départ le voit |

## Hors de mon rôle

**Biais de la valeur p de concentration** (rapport, § 5 ; nœud porté à Lazar, sans défaut) : rien n'est changé ; `statistiques_v1`
applique le texte tel quel. Si un addendum est scellé, son code prendra un nom neuf (`statistiques_v2`) et sera revérifié.
Aucun calcul réel ne part avant le mot de Lazar.

## Déclaration

Lu pour ce traitement : le rapport, en entier ; `corrections-v1.diff`, en entier. Non ouverts : les autres outils et sorties du
contre-lecteur, aucune fiche du registre, rien sous `diag/`, `runs/`, `donnees/`, `docs/verdicts/`. Aucun téléchargement, aucune
machine, aucune dépense, aucun refus d'outil. Suite complète du dépôt non jouée (consigne) ; les essais de la version 1 restent verts
(168 pour les trois fichiers que la version 2 remplace).
