# Corrections de l'organisme écrit par Gemini — v3 des corrections, sur la v5 de Gemini

Écrit le 25 octobre 2026 par la lignée « conv-audit ». Les corrections C-01 à C-11 (`CORRECTIONS-v1.md`,
`CORRECTIONS-v2.md`) valent toujours ; Gemini les a gardées dans sa v4 puis dans sa v5. Celle-ci s'y ajoute. La
conception de Gemini ne change pas : seuls deux appels de consignation changent de place.

- **Source** : la v5 de Gemini (`organisme-gemini-m3-v5`, 5.0.0), relayée par Lazar le 25 octobre 2026 à 08:20 (heure
  de Paris), reconstituée sans exécuter son script ; empreinte d'arbre `28b9d4c3b5221f537028178b9d2a074fc7d3a2afd2eceef58375962b7bae26e0`.
- **Exécutions** : seulement en isolation (utilisateur `nobody`, réseau coupé par `unshare -n`, environnement vide,
  `python -B`), et sous le noyau en simulation, avec isolation réseau.

## C-12 — un statut non « OK » de la moisson bloquait l'organisme

| où (v5) | défaut | correction | test |
|---|---|---|---|
| `principal.py`, `_enregistrer_recherche` (bloc verrouillé l. 281, appel l. 288) et `_enregistrer_telechargement` (bloc l. 335, appel l. 343) | `_consigner_erreur` est appelé en tenant `_VERROU`, qu'il reprend ; `threading.Lock` n'est pas réentrant : au premier statut non « OK » (`PLAFOND`, `REFUSE_FUITE`, `ECHEC_RECHERCHE`, `SOURCE_INCONNUE`, `ANOMALIE`, `INDISPONIBLE`, `SANS_TEXTE`, `ECHEC_TELECHARGEMENT`), le fil se bloque pour toujours. Mesuré : pile du fil arrêtée à `principal.py` l. 73 (`with _VERROU` de `_consigner_erreur`) ; l'essai de Gemini `test_v5_tous_les_statuts_de_moisson_traites_et_comptes` ne finit jamais ; sous le noyau (simulation, `--octets-max 100`), deux générations `DELAI_DEPASSE`, aucun successeur, aucune réponse à la question | les deux appels sortent du bloc verrouillé et le suivent aussitôt, même message ; rien d'autre ne change | `test_corrections_v3.py::test_c12_…` (chaque statut des deux primitives, appel surveillé 5 s dans un fil à part) ; l'essai de Gemini passe |