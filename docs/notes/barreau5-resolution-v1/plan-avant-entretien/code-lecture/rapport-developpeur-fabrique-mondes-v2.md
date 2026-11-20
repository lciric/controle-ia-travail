# Rapport du développeur de la fabrique des mondes de l'épreuve à vérité plantée (barreau 5) — v2

- **Auteur** : développeur de la fabrique, sous-agent de la session mère (`session_01XJ6Mgr8BN6UanALsQatc5E`), Claude Opus
  5.5 (`claude-opus-5-5`) ; même mandat (`mandat-developpeur-fabrique-mondes-v1.md`, `d8977676…61e4`).
- **Date** : 20 novembre 2026 (horloge du conteneur). Pièce d'instrument (classe B). Remplace le rapport v1 (`421bc554…`)
  pour ce qu'il change ; le v1 reste, non modifié.
- **Pièce suivie** : la contre-lecture `contre-lecture-fabrique-mondes-v1.md` (`e6ddb470…a59fd`, Claude Fable 5.2, verdict
  « conforme après ces corrections »), lue en entière, empreinte vérifiée, avec ses outils (`couples_corrections_v1.py`
  `b73e203e…`, `traducteur_resultat_vers_rendu_v1.py` `d8355011…`, `verifier_couples_v1.py`,
  `mutations_contre_lecture_v1.py`, `resultats-verification-couples-v2.json`). Le programme de lecture n'est ni lu, ni
  importé, ni joué ; des signatures seules de `engagement_v1.py` ont été lues (six lignes `def`, ses imports).

## 1. Les 21 couples

Tous appliqués à la lettre, par l'outil d'édition, dans l'ordre. **Preuve** : après les 21 couples, la fabrique et le juge
ont exactement les empreintes de la copie corrigée du contre-lecteur (`resultats-verification-couples-v2.json`,
`corrige_sha256`) : fabrique `520b8215…69317`, juge `b35f0a7f…d80f6`. Je n'en juge aucun faux.

| couple | constat | fichier | traitement |
|---|---|---|---|
| F-1 | imports (hmac, re) | fabrique | appliqué |
| F-2 | B-1, B-2, B-3, B-5 : dix lignes, instants à secondes, pli gelé, noms opaques, forme canonique | fabrique | appliqué |
| F-3 | B-5 : pli gelé par défaut | fabrique | appliqué |
| F-4 | B-6 : `sur_saboteur` | fabrique | appliqué |
| F-5 | B-2 : instant des scores tardifs | fabrique | appliqué |
| F-6 | B-1 : ligne « \| CLÉ \| instant \| contenu \| référence \| » | fabrique | appliqué |
| F-7 | B-1 : `ENGAGEMENT-B5F` « sha256 <64> » | fabrique | appliqué |
| F-8 | B-3, B-5 : entropie, commit et accord de formation | fabrique | appliqué |
| F-9 | B-5 : identifiants de tâches admis | fabrique | appliqué |
| F-10 | B-3 : commit de la formation contrôlé | fabrique | appliqué |
| F-11 | B-2, B-3, B-5 : contrôles des instants, de l'entropie, des accords, du pli | fabrique | appliqué |
| F-12 | B-4 : un seul sel de 256 bits, noms redérivés | fabrique | appliqué |
| F-13 | B-4 : table en forme canonique | fabrique | appliqué |
| F-14 | M-1 : V7, premier cas, table sous `scores/etiquettes-pli0.json` | fabrique | appliqué |
| F-15 | B-4 : V7, deuxième cas, table cohérente sous un autre sel | fabrique | appliqué |
| F-16 | B-3 : quatre lignes de la formation | fabrique | appliqué |
| J-1 | M-2 : motif du refus de V7 confronté à l'artefact | juge | appliqué |
| J-2 | M-3 : V0 refusé ou sans E3 : règles de V0 manquées | juge | appliqué |
| J-3 | m-1 : borne de la phrase E à trois chiffres | juge | appliqué |
| J-4 | m-5 : w(6) = 0 à 95 % | juge | appliqué |
| J-5 | M-4 : accord exact avec la seconde programmation, dans tous les mondes | juge | appliqué |

**Erratum de texte (m-3, m-4), sans couple, après les couples** : l'en-tête de la fabrique est récrit (les lacunes de
l'interface que déclarait le v1 sont tranchées par la contre-lecture ; seule `GO-RELANCE-FORMATION-B5F` est admise dans
`lignes_supplementaires` ; aucune raison écrite à fabriquer pour le cinquième cas de V7), et le commentaire du paramètre
`lignes_supplementaires` le dit. Aucune ligne de code ne change par cet erratum ; d'où l'empreinte finale `22560d9f…`
de la fabrique, différente de celle de la copie du contre-lecteur. Le juge est resté à `b35f0a7f…`.

## 2. Le traducteur

Versé sous `src/controle_ia/barreau5_familles/traducteur_verite_plantee_v1.py`. Seule sa docstring change (provenance,
chemin d'appel, ligne sur `--accord`) ; le code qui la suit est identique à l'octet à `d8355011…` (vérifié par programme :
sha256 du corps `56fbb4ba…` des deux côtés). L'option `--accord` est gardée : elle recopie `verdict` et
`arret_par_une_garde` du comparateur de la seconde programmation dans le rendu (J-5). Il n'importe ni le paquet ni le
programme de lecture. Ses essais ne portent que sur des résultats fabriqués.

## 3. Les essais

`tests/test_barreau5_familles_epreuve_verite_plantee_v1.py` : **155 passés en 127 s**, aucun sauté.
- **Les onze essais en échec sur la copie corrigée, repris** comme la contre-lecture l'attend : garde factice récrite
  sur ses règles recopiées (dix lignes lues dans leur forme écrite, contenus, ordre des dates, épreuve et code de lecture
  à la même empreinte, sel unique de 64 signes, noms redérivés, forme canonique, engagement « sha256 », ouverture « table
  sha256 », liste blanche, inventaire, table dans l'arbre, pli gelé, séries de la table) ; `test_arbre_conforme`,
  `test_v7_quatre_refus` (chaque refus au fragment du motif du programme), `test_v7_deuxieme_cas_deux_variantes`,
  `test_options_de_l_agent_de_l_epreuve` (ligne `GO-RELANCE-FORMATION-B5F`), `test_tables_du_texte_et_de_l_addendum`
  (w(6) = 0), le programme qui rend la vérité (refus au motif du programme, accord de la seconde programmation, borne à
  trois chiffres), `test_juge_passe_sur_programme_juste_au_hasard`, `test_juge_rendu_manquant_ou_invalide`,
  `test_juge_v12_motif_force_partiel_admis`, `test_juge_nombres_de_mondes_et_cas`, `test_juge_ligne_de_commande` ; et
  `test_parametres_et_ecrasement` (pli non gelé, entropie, accords, commit, instants sans secondes, tâches illisibles).
- **Les cinq qui tuent les survivantes de la contre-lecture** : `test_v0_bruits_par_jeton_independants` (c1),
  `test_v0_trois_membres_de_meme_loi` (c2), `test_v7_premier_cas_table_inventoriee` (c4), `test_juge_v10_niveau_de_d`
  (c6), `test_juge_v3_d_sans_motif_ne_compte_pas` (c7).
- **Ajoutés** : égalité des trois règles recopiées avec les modules du dépôt (`test_pli_gele_suit_le_manifeste`,
  `test_table_et_registre_suivent_engagement_v1` : noms opaques, forme canonique, table cohérente, lignes du registre) ;
  un essai par couple du juge (`test_juge_v7_refus_pour_une_autre_raison`, `test_juge_v0_non_lu`,
  `test_juge_accord_avec_la_seconde_programmation`) ; deux du traducteur
  (`test_traducteur_essais_sur_resultats_fabriques`, `test_traducteur_ligne_de_commande_et_accord`).
- Le programme de lecture n'est ni importé ni joué ; `manifeste` et `engagement_v1` ne sont importés que par les essais
  d'égalité, sautés dans un paquet minimal.

## 4. Passage de mutations v2

`outils-developpeur-fabrique-mondes-v1/mutations_fabrique_juge_v2.py` (`f5b15ee3…`, scellé) ; résultats
`resultats-mutations-v2.json` (`da54907a…`, scellé). Le paquet de chaque mutation copie tout `src/controle_ia`, pour que
les essais d'égalité y jouent. Témoins : sans mutation, 155 passés, aucun sauté ; import cassé, échec. **74 mutations,
74 tuées**, chacune par l'essai qui la vise : les 49 de la v1 dont le texte existe encore, j10 récrite (j10b) ; les huit du
contre-lecteur (c4 récrite sur le nom neuf de la table) ; seize neuves sur les couples et le traducteur (pli gelé sous une
autre clé, ordre des noms opaques, forme non canonique, sel court, table reçue sous le même sel, anciennes formes de
l'engagement et du membre, scellement illisible, épreuve à une autre empreinte, entropie de formation désaccordée,
fragment trop large, J-2, J-3 et J-5 retirés, deux défauts du traducteur). Réserve (R4) : k02 (ordre des noms opaques)
n'est tué que par l'essai d'égalité avec `engagement_v1` ; dans un paquet minimal il survivrait. Mes mutations restent
les miennes ; j'en ai écarté une comme équivalente avant le passage (ordre des dates encore admis par la garde).

## 5. Ce qui reste, pour la mère

Ce que la contre-lecture lui renvoie (section 10 de sa pièce) est inchangé : l'essai de raccord sur la vraie garde avant
le gel, le lieu de l'engagement des vérités, l'entropie du premier passage. Et : la fabrique, le juge, le traducteur et
leurs essais sont dans l'arbre gelé ; ils doivent être commis avant `CODE-LECTURE-B5F`.

## 6. Empreintes

| fichier | sha256 |
|---|---|
| `src/controle_ia/barreau5_familles/epreuve_verite_plantee_v1.py` | `22560d9f4f814ef008ef050bdca626d4bcdcc5ffc139d8f88e8c7ce39c965dca` |
| `src/controle_ia/barreau5_familles/juge_verite_plantee_v1.py` | `b35f0a7ff34c2a30b06f85760e7c04db16589a0b6010dd4d61ff66a9fb1d80f6` |
| `src/controle_ia/barreau5_familles/traducteur_verite_plantee_v1.py` (neuf) | `48fbfd88a004e7b6ef5f4df226c49e0e3bbed70f8e18a2a25baa0b5c9350d419` |
| `tests/test_barreau5_familles_epreuve_verite_plantee_v1.py` | `826b3c0300f4c1e7ab9ce7c14ca9fa255e46bc9b4b5fdeeb46feb38eaddbbf79` |
| `…/outils-developpeur-fabrique-mondes-v1/mutations_fabrique_juge_v2.py` (scellé) | `f5b15ee346179b6d247386491bff6b0bef66b5fae3a7ef91cd1f6e3f804fc1b2` |
| `…/outils-developpeur-fabrique-mondes-v1/resultats-mutations-v2.json` (scellé) | `da54907ab1f2f4b41c9d53f1afd7591eebd25f5a64d4e2c57f9e1c151d5b7562` |

Temporaires `/dev/shm/b5f-mutations-v2` et `/dev/shm/b5f-fabrique-essais-v1` effacés. Aucun commit, aucun réseau, aucune
dépense ; aucun outil refusé.
