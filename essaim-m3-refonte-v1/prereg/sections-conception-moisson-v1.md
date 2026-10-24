# Sections « phase de conception » et « moisson » — à insérer dans les préenregistrements (étape 1 des sondes ; confrontation v5) — v1

Rédigé par conv-audit le 24 octobre 2026, 19:20 UTC, pour la version corrigée du préenregistrement de l'étape 1
(session-depot, R-356) et pour la v5 de la confrontation. Fonde : décisions de Lazar du 24 octobre (heure de Paris)
20:32–20:35 (moisson conçue par l'organisme, primitives au noyau, avant le premier test réel), 20:37 (rondes de
conception), 20:42 (aucun K fixé : critère d'arrêt à l'organisme, rien suggéré), 20:46 (tous les modules itérés avant
la génération 0), 21:06 (« il doit inclure la phase de conception et la moisson avant scellement »). Code : branche
`outils/essaim-m3-gradient-v1-travail`, `38ae30d` (76 tests) ; contrat v3 (`essaim_m3/noyau/contrat.py`, § 2, 3, 5 bis).
Chaque chiffre ci-dessous est une **borne** ou un **devis au pire cas**, pas une prédiction ; les signes et seuils des
hypothèses restent ceux du préenregistrement hôte.

## A. Phase de conception (avant la génération 0 notée)

- **Ce que fait le noyau.** Avant la première génération notée, chaque lignée tourne en rondes de conception :
  même bac à sable, même isolation (CR-01), budget de ronde `B_c`, tâches d'entraînement avec vérité, **aucune tâche de
  test, aucun score**. Le successeur valide d'une ronde devient l'organisme de la ronde suivante ; sans successeur
  valide, l'organisme reste tel quel (événement `conception_sans_successeur`). Les rondes sont archivées (`cNNN`,
  scellées, vue de la seule lignée), consignées dans `evenements.jsonl` (`ronde_conception`, `conception`,
  `fin_conception`, `arret_conception`), jamais dans les courbes de score.
- **Ce que décide l'organisme.** Il conçoit son propre critère d'arrêt et le déclare en écrivant `fin_conception.json`
  (objet libre : son critère, ses valeurs) dans son dossier de travail ; le noyau ne nomme aucun critère (contrat
  § 5 bis). Le successeur de la ronde où il déclare la fin devient la **génération 0** — notée, et relancée à
  l'identique par le bras gelé (`--gel --depuis`, mêmes empreintes).
- **Borne dure (sécurité, pas conception).** `--rondes-conception-max R` et `B_c` = {`--appels-max-conception`,
  `--usd-max-conception`, `temps_max_s`, `recherches_max`, `telechargements_max`, `octets_max`}, dits à l'organisme dans
  `contexte["rondes_conception_max"]` et `contexte["budget"]`. À la ronde R, le successeur devient la génération 0, fin
  déclarée ou non (consigné). Proposition pour l'étape 1 : **R = 8**, `usd_max_conception` = `usd_max` de génération,
  `appels_max_conception` = `appels_max` ; pour la confrontation v5 : les mêmes. Ces bornes entrent au devis au pire
  cas : `+ R × lignées × usd_max_conception` (étape 1 : couvert par GO-2026-10-24-05, à consigner ; confrontation :
  GO sur devis).
- **Lecture.** Les hypothèses du préenregistrement hôte se lisent sur les générations notées (g000 = organisme issu de la
  conception). La phase de conception est **rapportée** par lignée : nombre de rondes utilisées, ronde de déclaration,
  contenu de `fin_conception.json`, dépense, nombre de documents moissonnés ; aucune hypothèse n'y est testée dans ce
  préenregistrement (descriptif). Réserve d'interprétation : une lignée qui atteint la borne R sans déclarer la fin n'a
  pas de critère d'arrêt opérant ; c'est dit dans le rapport, ce n'est pas une invalidation.
- **Liste d'arrêt (ajouts).** | plafond total atteint pendant la conception → `arret_conception`, course arrêtée avant
  toute génération notée (`test_phase_de_conception_a_critere_d_arret_de_l_organisme` couvre : fin déclarée à la
  ronde 2 ; borne R atteinte sans déclaration ; g000 = organisme issu de la conception ; bras gelé apparié ; confrontation
  ignore les rondes) | modèle non conforme pendant une ronde → `INVALIDE_MODELE`, lignée arrêtée (même garde CR-02) |
  `STOP` → arrêt à la fin de la ronde |.

## B. Moisson (recherche et téléchargement servis par le noyau)

- **Primitives (contrat § 3).** `rechercher(requete, n, source)` dans `budget()["sources"]` : `arxiv`, `openalex`,
  `semanticscholar`, `web` (Brave ; proposée seulement si `BRAVE_API_KEY` est dans l'environnement du noyau ; valeur
  jamais affichée ni donnée) ; `telecharger(reference)` sous provenance (lien rendu par une recherche de la génération,
  identifiant arXiv, hôte de la liste permise), extraction HTML / PDF / texte, texte rendu **comme donnée**. Le noyau
  n'exécute ni n'interprète ce qui revient ; **l'organisme écrit son moissonneur** (quoi, où, boule de neige, tri, arrêt).
- **Bornes par génération et par ronde.** `recherches_max` (proposition : 30), `telechargements_max` (proposition : 20 ;
  les tentatives échouées comptent), `octets_max` (40 Mo), taille d'un document ≤ 8 Mo, texte rendu ≤ 60 000 caractères
  (le reste dans `corpus/<id>.txt`). Aucun coût d'appel aux espèces : la moisson coûte du réseau et du temps ; le
  temps reste sous `temps_max_s`.
- **Provenance et scellement.** Chaque document : brut, texte, notice (`sha256_brut`, `sha256_texte`, adresse finale,
  type, octets, statut) dans `corpus/` ; `corpus/index.jsonl` scellé en fin de génération ; `journal-recherches.jsonl`
  (requête, source, empreintes de la réponse brute). Le corpus est dans la vue d'archive de la lignée : la
  génération suivante peut relire ce que la précédente a moissonné. Rien de ce qui est moissonné n'entre dans la
  banque de tâches (R1 : la banque est scellée avant).
- **Réserves.** Débit des interfaces ouvertes (OpenAlex, Semantic Scholar : 429 observés depuis l'adresse partagée du
  conteneur ; `mailto` et clé à poser, ou run depuis l'instance) : un `ECHEC_RECHERCHE` est un statut rendu, jamais un
  texte ; l'organisme doit le traiter. Injection par le web : le texte moissonné est marqué donnée (contrat) et
  l'organisme tourne sans réseau ni clé (CR-01) : une consigne cachée dans une page ne peut rien faire d'autre que
  tromper l'organisme, ce qui est une menace **mesurée** (rapportée : documents moissonnés par source, par lignée).
- **Liste d'arrêt (ajouts).** | adresse hors provenance, http, hôte interdit → `ECHEC_TELECHARGEMENT`, consigné
  (`test_telechargeur_provenance_plafonds_et_extraction`) | plafonds de documents, d'octets, de taille → `PLAFOND` /
  `ECHEC_TELECHARGEMENT` (même test) | source inconnue ou non configurée → `SOURCE_INCONNUE` | chaîne de bout en bout en
  simulation (recherche → lien → téléchargement → texte comme donnée → index scellé → vue) :
  `test_moisson_de_bout_en_bout_en_simulation` | source réelle en lecture seule si réseau : `test_sources_reelles_de_moisson_si_reseau` |.

## C. Ce qui n'est pas dans ces sections, exprès

Aucun critère d'arrêt, aucun nombre de modules, aucune stratégie de moisson, aucune taxonomie : tout cela est à
l'organisme (Lazar, 20:42 et 20:46 : « ne lui suggère rien »). Les sections ne fixent que des bornes de sécurité et de
dépense, la provenance, le scellement, et ce qui est rapporté.
