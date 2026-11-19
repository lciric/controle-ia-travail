# Notice — classifieur lexical, classifieur de surface, agrégateur séquentiel et lecture commune des cinq moniteurs du bras A (lot 16) — version 7 du code

**Pièce habilitée, à ne pas transmettre à une session non habilitée.** Ce qui est transmissible est dans `pour-le-texte-du-bras-a-sans-interne-v7.md` (`381036f2dec44c96f2e9ba1955e494ee9fc138e61fef0ac0d828f91d22b43382`).

**En bref.**
- La version 7 répond à quatre des six demandes du rédacteur du texte neuf, relayées par la mère le 19 novembre. **Aucun calcul de moniteur ne change.**
- 55 essais passent. Chacune des 60 gardes du module, retirée seule, fait échouer un essai.
- La version 6 reste intacte ; ses essais l'éprouvent toujours. Elle ne doit pas servir à une lecture décisive : ses champs « balise » et « jointure » acceptent un texte libre, et sa table se refait à partir de l'entropie du bras.

Qui : développeur habilité côté moniteurs, le 19 novembre 2026. Aucun résultat lu, aucun poids chargé, aucune dépense, jamais la suite d'essais complète. Aucun outil refusé.

| rôle | chemin | empreinte |
|---|---|---|
| module, version 7 | `src/controle_ia/organismes_discrets/bras_a_v2_habilite/autres_moniteurs_v7.py` | `3b5dccc931c1ed54816a703bbc774371518ecea3fd825dfa384026cabf461531` |
| ses essais | `tests/test_bras_a_v2_habilite_autres_moniteurs_v7.py` | `234c00a0d634fbaf6479b612ec6f801801f2b4516973e5a844cc82a6f8328119` |

Commit `f8aba34d`. Essais ciblés : `PYTHONPATH=src python -B -m pytest -q -p no:cacheprovider tests/test_bras_a_v2_habilite_autres_moniteurs_v7.py` ; dernière ligne : `55 passed`.

## Ce qui change depuis la version 6

| objet | version 6 | version 7 | essais |
|---|---|---|---|
| entropie de la table des identifiants opaques | tirée de l'entropie du bras, par la clé `bras-a-v2/opaq/moniteurs` | tirée du système, écrite dans le fichier de la table tenu à part ; 41 clés de graine | `test_cles_des_graines`, `test_table_opaque_a_son_entropie_propre` |
| engagement | aucun | l'empreinte du fichier de la table est un argument obligatoire de la production et une clé de son manifeste ; la lecture commune refuse une table qui n'a pas cette empreinte | `test_production_engagee_sur_la_table` |
| ouverture de la table | compagnon vérifié | compagnon vérifié, tirage rejoué à partir de l'entropie révélée, refus si cette entropie est celle du bras | `test_table_arrangee_ou_tiree_de_l_entropie_du_bras_refusee` |
| champs « balise » et « jointure » d'une lecture produite | toute chaîne | deux listes fermées, égales à celles de `moniteurs_langue_v2.py` | `test_etats_de_la_balise_et_jointures_en_listes_fermees` |
| comptes de la règle du 1 % | vides quand le moniteur n'est pas calculable | remplis quand le défaut vient des permutations perdues ou des tirages dégénérés ; nommés dans la liste des nombres rendus | `test_plus_de_un_pour_cent_de_permutations_perdues_non_calculable`, `test_tirages_degeneres_de_la_borne_non_calculable_sans_arret` |
| preuve d'ordre | empreintes des scores par moniteur | plus l'engagement de la table | `test_les_cinq_moniteurs_de_bout_en_bout` |

Changements de signature : `tirer_la_table_opaque(cles, entropie_propre=None)` rend `{entropie_propre, table}` ; `lire_la_table_opaque(chemin, entropie_du_bras)` rend la table et l'engagement ; `ecrire_la_production(…, engagement_de_la_table)`.

## Réserves, à dire au contre-lecteur

- **Le compte des tirages dégénérés est relu dans le message de la fonction gelée** (`t06.test_croise.intervalle_aire_moyenne` : « N tirages dégénérés sur M »), car elle s'arrête sans rendre ce compte. Si le message gelé changeait, les deux champs resteraient vides, sans arrêt : un essai compare les champs au motif rendu.
- **Les comptes restent vides** quand le moniteur n'est pas calculable pour une raison survenue avant les permutations (pli sans action, classe absente).
- **Limite de l'opacité.** Une demande de lecture porte le texte de l'action : une session qui tiendrait aussi les épisodes du rejeu retrouverait l'action sans la table. L'entropie propre ferme la voie « refaire la table », pas celle-là.
- **L'engagement n'empêche pas** celui qui tient la table de la lire avant les ouvertures : il prouve seulement que la table ouverte est celle d'avant la production, et qu'elle sort d'un tirage. La séparation des dossiers reste à tenir par le lanceur, qui n'est pas écrit.
- **Épreuve par retrait** faite en retirant l'arrêt (et non en remplaçant la condition par « faux ») : à refaire par le contre-lecteur selon sa méthode.

## Ce qui reste

- Vérification par le contre-lecteur du lot 16 : version 7 et paquet de préparation des lectures.
- Les essais du paquet de préparation tirent encore leur table avec la version 6.
- Lanceur de l'étape de discrétion : après scellement du texte.
