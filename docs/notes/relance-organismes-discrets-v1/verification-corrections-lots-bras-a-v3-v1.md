# Vérification des corrections du module des lots, version 3 — v1

- **Objet** : `lots_bras_a_v3.py` (`81dae4118be5…`, empreinte vérifiée), `tests/test_lots_bras_a_v3.py` (`d1051378fcd2…`), note `code-lots-bras-a-v3-note.md` (`ed65cd1e5709…`), contre ma contre-lecture `contre-lecture-lots-bras-a-v2-v1.md` (`c40db8a6…`). Même lecteur, même cloisonnement, aucun réseau, rien committé.
- **Essais rejoués** : `tests/test_lots_bras_a_v3.py` et `tests/test_lots_bras_a_v2.py` : 99 passés.
- **Méthode** : `diff` complet de la v2 et de la v3 du module.

## Verdict : corrections vérifiées

Le diff ne contient que les corrections ci-dessous, les commentaires et le docstring ; aucun autre changement de sens.

- **M-1** : `voie_de_service_de_l_etape_e_prime` rend `[]` sur un constat `ancre-jumeaux` (aucun arrêt), le tableau du lot sinon ; objet étranger, épreuves mêlées, ancre sur plans incomplète : `GardeArret`. Essais sain et artefacts présents.
- **M-2** : `<=` devenu `<` aux deux endroits (128 et 64) ; tirage à l'égalité exacte, essais à 127/128/129 et 63/64/65. Le tirage des génériques (≥ 64) et des relues (160) est inchangé.
- **m-3** : le lot honnête de la couverture garde `empreinte-des-plans-de-la-dose-1` (sha256 des deux listes triées) ; le lot des jumeaux la recalcule et arrête si elle diffère ou manque. Essai d'échange à mêmes effectifs.
- **m-4** : `taches-sans-plan` (plans honnêtes) et `taches-sans-plan-deplace` (plans déplacés) comptés.
- **Planchers** inchangés : 32, 24, 32, 32, 80 (seuls les commentaires changent, GO-2026-11-22-90).

## Notés, non défauts

- **Ambiguïté neuve levée à (e′)** : ancre sur plans honnêtes en constat et ancre des jumeaux construite : `AmbiguiteDuTexte`, explicite, testée. C'est ma question de texte ; elle reste à trancher par le texte. Les deux en constat : liste vide.
- **Changements d'octets déclarés, conformes au diff** : lots de la couverture (honnête et des jumeaux), par leurs seuls comptes, au cas complet aussi ; à 128 exactement, lot honnête de l'appariement. Le reste du cas complet inchangé ; le sha256 de la couverture au manifeste n'est plus celui de la v2.
- Les deux survivants équivalents déclarés par la note (comptes impliqués par l'empreinte ; empreinte non triée, listes déjà triées) sont plausibles à la lecture. Je n'ai pas rejoué les mutations.
- m-1 et m-2 restent des points de texte, non du code.

Aucun défaut restant.
