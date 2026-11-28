"""Construit le brouillon 7 du préenregistrement du papier C à partir du brouillon 6 — v1.

Rédacteur neuf du brouillon 7 (session 16, 2026-10-21). Chaque changement est un remplacement exact : le texte ancien
doit apparaître une seule fois dans le texte courant, sinon le script s'arrête (aucun repli silencieux). Les corrections
reprennent les mots exacts des deux contre-lectures du brouillon 6 (texte 68fc0dc9… ; vérification courte de méthode
45a0d875…), acceptées en entier par la session, et les décisions de la session écrites dans la consigne du rédacteur
(e8bfb03b…) ; les écarts sont dans la table de traitement du brouillon 7.
Lancement : PYTHONDONTWRITEBYTECODE=1 python3 -B -I construire_brouillon7_v1.py B6 TABLE SCRIPT_CONFIG JOURNAL CONFIG SORTIE
"""
import hashlib
import re
import sys

B6, TABLE, SCRIPT_CONFIG, JOURNAL, CONFIG, SORTIE = sys.argv[1:7]


def sha(chemin):
    return hashlib.sha256(open(chemin, "rb").read()).hexdigest()


H_B6 = "fadc74c3b40b6e6aee9035f5a9566288d17d60b8403b57863721c2ee57554d00"
assert sha(B6) == H_B6, "brouillon 6 non conforme"
H_TABLE, H_SCRIPT, H_JOURNAL, H_CONFIG = sha(TABLE), sha(SCRIPT_CONFIG), sha(JOURNAL), sha(CONFIG)
t = open(B6, encoding="utf-8").read()
journal = []


def rep(ancien, neuf, etiquette):
    global t
    n = t.count(ancien)
    assert n == 1, f"{etiquette} : texte ancien trouvé {n} fois"
    t = t.replace(ancien, neuf)
    journal.append(etiquette)


DN = "docs/notes/contre-lectures-papier-C-v1/"
H_CONSIGNE = "e8bfb03bab6b81b882b9cd85f7dcdde3ed209af420159a14fd21596d2d22b48e"
R_TEXTE6 = f"`{DN}brouillon6/texte/contre-lecture-R2-brouillon6-texte-v1.md`"
H_TEXTE6 = "68fc0dc9f6f0f5305587cc09d1a2762e5cfbf90c8701d2a19cdddea66599b3a9"
R_METH6 = f"`{DN}brouillon6/methode-courte/contre-lecture-R2-brouillon6-methode-courte-v1.md`"
H_METH6 = "45a0d87569d883c72af7720081278e67298c3a2f9daaecf03c197b909431fd46"
H_ESSAIS6 = "da5bbad06c8fd7ca6e394f0a16129405c8440f9acf73746c68f331a296a68ad3"
H_PERS_PY = "49f96efbeff7d06fa6fcfa55635126e7dd5a99ab5c81e03a27d78c9c0390bcd2"
H_PERS_SORTIE = "9a2a36547df8a53bd76663f95eb274addde4df4487e023bf1959105925427189"
H_SIMS6 = "368f3ec867c05991ce4069c2854dc17aa61a508cb8e2462b18764654cb975bed"
H_B3CONF = "85173b22defe2c55844f23691028233a13746394324d0c598d3a66fb4f68820d"

# 0. En-tête : titre, auteur, date ; confidentialité (CB6-texte-08, copie publique).
rep("# Préenregistrement — papier C : HC1, HC2, HC2b, HC3 (TC.1 à TC.3) — v1 — brouillon 6",
    "# Préenregistrement — papier C : HC1, HC2, HC2b, HC3 (TC.1 à TC.3) — v1 — brouillon 7", "titre")
rep("""- Auteur : rédacteur neuf, sous-agent de la session 16, le 2026-10-21 (consigne
  `docs/notes/contre-lectures-papier-C-v1/consignes/consigne-redacteur-brouillon6-v1.md`,
  `dc25318d64fb9fffc2f1ce911f66ed9df3f1b0120bf8e74f07ad237b93e45753`). Il n'a écrit ni les brouillons 1 à 5, ni les
  brouillons 1 et 2 de la configuration, ni les notes de lecture des voisins, ni aucun rapport de contre-lecture, ni
  aucun traitement, projet de traitement ou table de traitement antérieure.
- Date (UTC) : celle du commit de scellement, qui fait foi. Brouillon 6 écrit le 2026-10-21.""",
    f"""- Auteur : rédacteur neuf, sous-agent de la session 16, le 2026-10-21 (consigne
  `{DN}consignes/consigne-redacteur-brouillon7-v1.md`,
  `{H_CONSIGNE}`). Il n'a écrit ni les brouillons 1 à 6, ni les
  brouillons 1 à 3 de la configuration, ni les notes de lecture des voisins, ni aucun rapport de contre-lecture, ni
  aucun traitement, projet de traitement ou table de traitement antérieure.
- Date (UTC) : celle du commit de scellement, qui fait foi. Brouillon 7 écrit le 2026-10-21.""", "auteur et date")
rep("""  publique est soumise à décision de Lazar (`scripts/depot_expurge.py`).""",
    """  publique est soumise à décision de Lazar (`scripts/depot_expurge.py`). Cette décision dit aussi si les textes
  d'insertion cités ici en sortent : insertion remplie du constat nu, pour les deux corpus (Métrique, point 5), et sa
  forme à fentes (réserve 16).""", "confidentialité (CB6-texte-08, copie publique)")

# 1. Historique : brouillon 6.
rep("""**Historique (R12).** Les brouillons précédents restent tels quels :
- brouillon 5 : `brouillons/papier-C-preenregistrement-HC1-HC3-v1-brouillon5.md`
  (`9d55160f59cfb19e489dccc586e748173669b1373b570f5d42beb02293332969`), point de départ de ce texte ; contre-lu par deux""",
    f"""**Historique (R12).** Les brouillons précédents restent tels quels :
- brouillon 6 : `brouillons/papier-C-preenregistrement-HC1-HC3-v1-brouillon6.md`
  (`{H_B6}`), point de départ de ce texte ; contre-lu par deux
  lentilles (texte et conformité ; vérification courte de méthode), rapports {R_TEXTE6}
  (`{H_TEXTE6}`) et
  {R_METH6}
  (`{H_METH6}`) ; tous les constats acceptés par la session, avec
  ses décisions (consigne du rédacteur, ci-dessus ; registre, R-316) ; application constat par constat :
  `{DN}table-traitement-brouillon7-v1.md` (`{H_TABLE}`) ;
- brouillon 5 : `brouillons/papier-C-preenregistrement-HC1-HC3-v1-brouillon5.md`
  (`9d55160f59cfb19e489dccc586e748173669b1373b570f5d42beb02293332969`), point de départ du brouillon 6 ; contre-lu par deux""",
    "historique (brouillon 6)")

# 2. Ce que change le brouillon 7 ; rappel du brouillon 6.
rep("""**Ce que change le brouillon 6.** Aucun énoncé d'hypothèse ni aucune pièce revendiquée ne change : les énoncés de HC1,
HC2, HC2b et HC3 sont repris mot pour mot du brouillon 3 (décisions N-005, N-013, N-023). Aucune famille, aucune
constante ni aucune longueur ne change ; le vivier est inchangé (R-309). Le texte applique le traitement de la session
des contre-lectures du brouillon 5 (`08ca42ae…`), constat par constat (table, historique ci-dessus).""",
    """**Ce que change le brouillon 7.** Aucun énoncé d'hypothèse ni aucune pièce revendiquée ne change : les énoncés de HC1,
HC2, HC2b et HC3 sont repris mot pour mot du brouillon 3 (décisions N-005, N-013, N-023). Aucune famille, aucune
constante ni aucune longueur ne change ; le vivier est inchangé (R-309, R-316). Le texte applique tous les constats des
deux contre-lectures du brouillon 6 et les décisions de la session (historique ci-dessus), constat par constat (table du
brouillon 7). Les décisions de Lazar P-020, P-021 et P-022 restent en attente, sous leurs marqueurs.
- **Stabilité de rang** (P-021) : l'option (A) passe de deux à trois lectures de la loi nette (calibrée, sans
  calibrage, calibrée par ρ̂/r̂) ; deux lectures ne protègent pas quand les juges n'ont pas le même modèle d'erreur
  (vérification courte de méthode du brouillon 6, constat 01) ; correction transmise à Lazar par la session (verrou 1).
  Clause de repli réécrite, mécanique : grille, nul, seuil et nombre d'essais écrits (constat 02). Versions de repli (B)
  et (C) lisibles seules ; le verrou 1 dit ce qui reste de la version recommandée sous chacune (CB6-texte-01).
- **Constat nu** (P-022) : versions de repli écrites comme les phrases mêmes du texte scellé (CB6-texte-02) ; sous (b),
  insertion lue au pilote, au point 1.4, pour la lisibilité seulement (décision de la session sur CB6-texte-05) ;
  liste d'arrêt 11 étendue à cette insertion (CB6-texte-06).
- **Réserve 17** (décision de la session sur CB6-texte-03) : personne grammaticale qui change avec l'indice dans trois
  familles, déclarée comme étiquette descriptive. Réserve 14 : règle de lecture « par formulation entière » ajoutée ; la
  contre-lecture « texte » du brouillon 6 juge la déclaration suffisante (repli (b) de R-309 non déclenché).
- **Tests du module** : contrôles de l'artefact pour la règle conjointe de C-P1 et pour les trois lectures des
  statistiques de rang (point 8 bis).
- **Verrou 6** : la contre-lecture 8 porte sur CL5-01 à CL5-03 ; les points (v) à (viii) du projet de traitement du
  brouillon 5 vont à une contre-lecture 10.
- **Décisions de la session écrites** : page de l'éditeur de Kumaran et al. acceptée comme provenance, réserve
  (R-316) ; voisins ajoutés aux « cités comme publiés » (routine).
- **Configuration** brouillon 4 : champs de P-021 (trois lectures, clause de repli, replis lisibles seuls), lecture par
  ρ̂/r̂, constat nu au pilote ; vivier, témoins, constantes et longueurs inchangés (vérifié par empreintes).

**Ce qu'avait changé le brouillon 6** (rappel ; la ligne « Stabilité de rang » suit la correction du brouillon 7 :
trois lectures). Le texte appliquait le traitement de la session des contre-lectures du brouillon 5 (`08ca42ae…`),
constat par constat (table du brouillon 6, historique ci-dessus).""", "ce que change le brouillon 7 ; rappel du brouillon 6")
rep("""les trois
  aux deux lectures de la loi nette ; clause de repli mécanique.""",
    """les trois
  aux trois lectures de la loi nette (calibrée, sans calibrage, calibrée par ρ̂/r̂) ; clause de repli mécanique.""",
    "rappel du brouillon 6, stabilité de rang (CB6-methode-courte-01, point 3)")

# 3. Verrous.
rep("""   2026-10-23 vers 00:30 UTC : (A) pour P-021, (a) pour P-020, (b) pour P-022 ; P-021 remplace P-019, jamais transmise,
   qui ne prend aucun défaut) : sous chaque marqueur""",
    """   2026-10-23 vers 00:30 UTC : (A) pour P-021, (a) pour P-020, (b) pour P-022 ; P-021 remplace P-019, jamais transmise,
   qui ne prend aucun défaut ; l'option (A) de P-021 est corrigée par la session, trois lectures au lieu de deux
   (vérification courte de méthode du brouillon 6, constat 01), correction transmise à Lazar avant le défaut par une
   ligne nouvelle du registre (R12) : `<<LIGNE_CORRECTION_P021>>`) : sous chaque marqueur""",
    "verrou 1, correction de P-021 (CB6-methode-courte-01)")
rep("""   `<<TRANCHER_P021>>`, `<<TRANCHER_P020>>` et `<<TRANCHER_P022>>` sont retirés avec la version écartée ; tant qu'il
   en reste un, `problemes` refuse le scellement.""",
    """   `<<TRANCHER_P021>>`, `<<TRANCHER_P020>>` et `<<TRANCHER_P022>>` sont retirés avec la version écartée ; tant qu'il
   en reste un, `problemes` refuse le scellement. Exception, P-021 : sous (B), les deux tableaux de la version
   recommandée (sections « Prédiction » et « Critères de lecture gelés ») et ses paragraphes « Trois lectures »,
   « Clause de repli mécanique » et « Sans le bras … » restent au texte scellé, sans en-tête ni marqueur, leur ligne
   C-P3b étant remplacée par la version (B) ; sous (C), seul le tableau de la section « Prédiction » reste, réduit à ses
   colonnes « id » et « grandeur », avec le paragraphe « Trois lectures » et la phrase « Sans le bras … ».""",
    "verrou 1, exception P-021 (CB6-texte-01, point 1)")
rep("""   en écart par la note `docs/notes/contre-lectures-papier-C-v1/brouillon5/voisins-cp02/lecture-voisins-cp02-v1.md` (décision de la session : écart « noté, sans effet sur le contenu », traitement de la
   session du brouillon 5, amendement 3, `08ca42ae…`) ; PDF de l'éditeur non téléchargé.""",
    """   en écart par la note `docs/notes/contre-lectures-papier-C-v1/brouillon5/voisins-cp02/lecture-voisins-cp02-v1.md` (décision de la session : page de l'article publié obtenue sans
   compte ni connexion, paramètre de refus des cookies ; acceptée par la session comme provenance, réserve déclarée
   (R-316) ; vaut pour le résumé et le corps) ; PDF de l'éditeur non téléchargé.""",
    "verrou 2, décision de la session sur la page de l'éditeur (DECISION_ECART_EDITEUR)")
rep("""`ecrire_config_v1.py`, `ecrire_config_brouillon2_v1.py` et `ecrire_config_brouillon3_v1.py` (avec son journal)""",
    """`ecrire_config_v1.py`, `ecrire_config_brouillon2_v1.py`, `ecrire_config_brouillon3_v1.py` et
   `ecrire_config_brouillon4_v1.py` (avec leurs journaux)""", "verrou 5, scripts de configuration")
rep("""   restent dans la zone privée. Au scellement, un script vérifie que chaque chemin cité avec une empreinte existe dans le
   dépôt et lui est égal ; un écart : pas de scellement.""",
    f"""   restent dans la zone privée. Pour la série du brouillon 6 : `construire_brouillon6_v1.py` et son journal, qui ont
   produit le brouillon 6, et `construire_brouillon7_v1.py` et son journal, sous `docs/procedures/papier-C-v1/`
   (CB6-texte-08) ; brouillon 6 du texte et configuration brouillon 3 sous `brouillons/` ; rapports des deux
   contre-lectures du brouillon 6, sous `{DN}brouillon6/`, avec leurs dossiers : contenu du
   dossier `essais/` du rapport « texte » versé sous `{DN}brouillon6/texte/` (CB6-texte-03) ;
   simulations de la vérification courte de méthode sous `{DN}brouillon6/methode-courte/simulations/`
   (manifeste `368f3ec8…`) ; consigne du rédacteur du brouillon 7 sous `{DN}consignes/` ; table de
   traitement du brouillon 7 sous `{DN}`. Au scellement, un script vérifie que chaque chemin cité avec une
   empreinte existe dans le dépôt et lui est égal ; un écart : pas de scellement.""",
    "verrou 5, série du brouillon 6 (CB6-texte-03 ; CB6-texte-08)")
rep("""6. **Contre-lecture R2** : vérification courte de méthode par un sous-agent neuf (contre-lecture 8 : niveaux sous le nul
   de C-P3a et de C-P3b corrigées avec un vrai rééchantillonnage ; règle des deux lectures pour les statistiques de rang
   sous les modèles S et D ; règle conjointe de C-P1 ; C-P4b sur l'excédent des deux côtés ; moitiés par tâches et mise à
   l'échelle ; ajout aux « Combinaisons » de la réserve « destination non spécifique » sur ĉ brut ; style des deux
   plaidoyers sous la différence des différences) ; contre-lecture « texte » du brouillon 6 (contre-lecture 9, avec la
   question : la déclaration de la réserve 14 suffit-elle ?) ; contre-lecture du module et de la configuration
   brouillon 3 (contre-lecture 7). Section « Contre-lecture ».""",
    """6. **Contre-lecture R2** : contre-lecture 8 : vérification courte de méthode de CL5-01 à CL5-03 (rapport
   `<<CHEMIN_RAPPORT_CL8>>`) ; points (v) à (viii) du projet, section 6.3 : contre-lecture `<<CHEMIN_RAPPORT_CL10>>`
   (C-P4b sur l'excédent des deux côtés ; moitiés par tâches et mise à l'échelle ; ajout aux « Combinaisons » de la
   réserve « destination non spécifique » sur ĉ brut ; style des deux plaidoyers sous la différence des différences).
   La contre-lecture 8 porte sur le texte corrigé de P-021 (trois lectures) et couvre toute la grille de la clause de
   repli mécanique (vérification courte de méthode du brouillon 6, constat 02 : cases à refaire en entier si le
   constat 01 est appliqué). Contre-lecture « texte » du brouillon 6 (contre-lecture 9, avec la question : la
   déclaration de la réserve 14 suffit-elle ?) ; contre-lecture du module et de la configuration brouillon 4
   (contre-lecture 7). Section « Contre-lecture ».""",
    "verrou 6 (CB6-methode-courte-04 ; CB6-methode-courte-02)")

# 4. Champs du scellement.
rep("""- Configuration à sceller sous `prereg/papier-C-config-v1.json` (`<<EMPREINTE_CONFIG>>`) : brouillon 3 relu, dont les""",
    """- Configuration à sceller sous `prereg/papier-C-config-v1.json` (`<<EMPREINTE_CONFIG>>`) : brouillon 4 relu, dont les""",
    "champs : configuration relue (brouillon 4)")
rep("""  `repli_si_refus`) et `agent_bras` (`decision_bras_usurpation` écrite ; `usurpation` retiré si P-020 est refusée), et
  `constat_nu` (`decision` écrite ;""",
    """  `repli_si_refus`), `agent_bras` (`decision_bras_usurpation` écrite ; `usurpation` retiré si P-020 est refusée) et
  `constat_nu` (`decision` écrite ;""", "champs : liste des trois champs de décision (CB6-texte-07)")
rep("""  (garde du lanceur, liste d'arrêt 1). Brouillon relu par ce texte : `brouillons/papier-C-config-v1-brouillon3.json`
  (`85173b22defe2c55844f23691028233a13746394324d0c598d3a66fb4f68820d`), écrit par
  `docs/procedures/papier-C-v1/ecrire_config_brouillon3_v1.py`""",
    f"""  (garde du lanceur, liste d'arrêt 1). Brouillon relu par ce texte : `brouillons/papier-C-config-v1-brouillon4.json`
  (`{H_CONFIG}`), écrit par
  `docs/procedures/papier-C-v1/ecrire_config_brouillon4_v1.py`
  (`{H_SCRIPT}`, journal `ecrire_config_brouillon4_v1.journal.txt`,
  `{H_JOURNAL}`) à partir du brouillon 3
  (`{H_B3CONF}`), écrit par
  `docs/procedures/papier-C-v1/ecrire_config_brouillon3_v1.py`""", "champs : configuration brouillon 4 et sa provenance")
rep("""  Les trois scripts appliquent les gardes lexicales et mesurent les longueurs avant d'écrire ; le troisième vérifie par
  empreintes que le vivier, les témoins, les fentes, les consignes, les contenus neutres, l'insertion, les gardes et les
  paragraphes de bras ne changent pas, et applique les gardes au constat nu.""",
    """  Les quatre scripts appliquent les gardes lexicales et mesurent les longueurs avant d'écrire ; le troisième et le
  quatrième vérifient par empreintes que le vivier, les témoins, les fentes, les consignes, les contenus neutres,
  l'insertion, les gardes et les paragraphes de bras ne changent pas, et appliquent les gardes au constat nu.""",
    "champs : scripts de configuration")
rep("""  et Lee ; Geng et al. ; Jiang et al. ; Zhu et al. ; Weng et al. ; Wang K. et al.) `<<DECISION_VOISINS>>` ; R-307 (GO-2026-10-20-13) et""",
    f"""  et Lee ; Geng et al. ; Jiang et al. ; Zhu et al. ; Weng et al. ; Wang K. et al.) : routine de la session ; les
  voisins ajoutés aux « cités comme publiés » sont nommés, Jiang et al. et Wang K. et al. compris (consigne du rédacteur
  du brouillon 7, `e8bfb03b…`) ; R-307 (GO-2026-10-20-13) et""", "champs : décision des voisins (DECISION_VOISINS)")

# 5. Documents qui font foi : registre ; pièces de contre-lecture du brouillon 6.
rep("""  R-307, R-308 et R-309 (contingence), R-312 (traitement du brouillon 5), P-020, P-021 (remplace P-019, jamais
  transmise) et P-022.""",
    """  R-307, R-308 et R-309 (contingence), R-312 (traitement du brouillon 5), R-316 (décisions de la session sur les
  contre-lectures du brouillon 6), P-020, P-021 (remplace P-019, jamais transmise ; et sa ligne de correction, verrou 1)
  et P-022.""", "documents : registre (R-316 ; correction de P-021)")
rep("""- Vérification du verrou de la famille 1 (R-307, R-308) : `docs/notes/contre-lectures-papier-C-v1/verification-verrou-famille1-v1.md`
  (`0cbd3ae3050c5485d6e5415eb38eb9f51c07363a8e7f23e66f9925ed92132420`).
""",
    f"""- Vérification du verrou de la famille 1 (R-307, R-308) : `docs/notes/contre-lectures-papier-C-v1/verification-verrou-famille1-v1.md`
  (`0cbd3ae3050c5485d6e5415eb38eb9f51c07363a8e7f23e66f9925ed92132420`).
- Rapports sur le brouillon 6 : texte {R_TEXTE6}
  (`{H_TEXTE6}`) ; essais du rapport « texte », versés à plat sous
  `{DN}brouillon6/texte/` (manifeste `sha256sums-essais-texte-b6-v1.txt`,
  `{H_ESSAIS6}`), dont `personne_grammaticale_vivier_v2.py`
  (`{H_PERS_PY}`) et sa sortie `personne_grammaticale_vivier_v2.sortie.txt`
  (`{H_PERS_SORTIE}`) ; vérification courte de méthode
  {R_METH6}
  (`{H_METH6}`).
- Simulations de la vérification courte de méthode du brouillon 6, `brouillon6/methode-courte/simulations/` (manifeste
  `sha256sums-simulations-methode-courte-b6-v1.txt`, `{H_SIMS6}`) ;
  sorties citées : U1 `sorties_u1/u1_N5_k3_T45.txt` (`d7a020b2ead9f38bc97277cfa9dcd9b33a016738bcc39681b5641bb5bda2da06`),
  `sorties_u1/u1_N5_k3_T60.txt` (`b6df8e1875e844f9a49eae5c3391089b380e1dee46459870d2efc136ade0206b`),
  `sorties_u1/u1_N5_k5_T45.txt` (`227293c8b9e1bd341c0494e07e85869d79ea36f1545517d96c459614a3a9b772`),
  `sorties_u1/u1_N5_k5_T60.txt` (`2fc8bfec07f5f84753481ccafcc0302bc6261cdece88cc4813c1b07b6b9ed224`) ; U2
  `sorties_u2/u2_D_artefact.txt` (`79b2bb5b206bd8e111d6674ca2ce070dd2220eeab36adc98c35abf2ed538124a`),
  `sorties_u2/u2_S_artefact.txt` (`7a6f93380788890a40c3c7e031c8356a6042473e0e346691916a0e6b776fddde`) ; U3
  `sorties_u3/u3_N5_k5_T60.txt` (`93b70c6dfb7cd0c62b380dbc2e81a7a6cc9da67775a76a3f9304c0886e23279c`) et les autres
  sorties de `sorties_u3/` (manifeste).
""", "pièces de contre-lecture citées : brouillon 6 (R6)")

# 6. HC1 : décision des voisins (quatre blocs ; contexte de la ligne suivante pour l'unicité).
CONSIGNE_V = "routine de la session (champs du scellement, « Décisions »)"
rep("""      prise ; ajout de routine, consigné : `<<DECISION_VOISINS>>`) :
      - poids du conseil""",
    f"""      prise ; ajout de routine, consigné : {CONSIGNE_V}) :
      - poids du conseil""", "HC1, ajouts du brouillon 4 (DECISION_VOISINS)")
rep("""      prédiction prise ; ajout de routine, consigné : `<<DECISION_VOISINS>>`) :
      - autorité graduée""",
    f"""      prédiction prise ; ajout de routine, consigné : {CONSIGNE_V}) :
      - autorité graduée""", "HC1, ajouts du brouillon 6 (DECISION_VOISINS)")
rep("""      changé, aucune prédiction prise ; ajout de routine, consigné : `<<DECISION_VOISINS>>`) :
      - pression de pairs""",
    f"""      changé, aucune prédiction prise ; ajout de routine, consigné : {CONSIGNE_V}) :
      - pression de pairs""", "HC1, voisins de Panin (DECISION_VOISINS)")
rep("""ajout de routine, consigné :
      `<<DECISION_VOISINS>>`) :""",
    f"""ajout de routine, consigné :
      {CONSIGNE_V}) :""", "HC1, voisins de Bajaj et Tiganj (DECISION_VOISINS)")
assert "<<DECISION_VOISINS>>" not in t

# 7. Prédiction : bloc P-021.
rep("""**[Décision de Lazar en attente : P-021]** `<<TRANCHER_P021>>` Version recommandée (P-021, `registres/decisions.md`,
qui remplace P-019, jamais transmise ; option (A), recommandation de la session, confiance ≈ 60 % ; transmise le
2026-10-21 vers 00:30 UTC ; défaut (A) le 2026-10-23 vers 00:30 UTC) : valeurs p exactes et par rééchantillonnage
centré, lecture « établie / non établie », sans verdict de réfutation, aux deux lectures de la loi nette ; clause de
repli mécanique.""",
    """**[Décision de Lazar en attente : P-021]** `<<TRANCHER_P021>>` Version recommandée (P-021, `registres/decisions.md`,
qui remplace P-019, jamais transmise ; option (A), recommandation de la session, confiance ≈ 60 %, corrigée par la
session : trois lectures, verrou 1 ; transmise le 2026-10-21 vers 00:30 UTC ; défaut (A) le 2026-10-23 vers 00:30 UTC) :
valeurs p exactes et par rééchantillonnage centré, lecture « établie / non établie », sans verdict de réfutation, aux
trois lectures de la loi nette ; clause de repli mécanique.""", "bloc P-021, en-tête (CB6-methode-courte-01)")
rep("""tirages indépendants par tâches et par items) | aucune ; p > 0,05 : « non établie » |""",
    """tirages indépendants par tâches et par items ; p = (1 + #{τ* ≥ τ}) / (B + 1)) | aucune ; p > 0,05 : « non établie » |""",
    "bloc P-021, C-P3b, formule de p (CB6-methode-courte-06)")
rep("""**Deux lectures.** Pour leurs composantes en Ḡ (C-P3a ; C-P3b ; Ḡ nets des familles 1 et 4 dans C-P3c), les trois
statistiques sont calculées sur la loi nette calibrée et sur la loi nette sans calibrage (ρ = 1, mêmes tirages) ;
« établie » seulement si les deux lectures concluent (extension aux statistiques de rang de la règle conjointe de C-P1 ;
réserve 15 ; non simulée, d'où la clause qui suit).""",
    """**Trois lectures.** Pour leurs composantes en Ḡ (C-P3a ; C-P3b ; Ḡ nets des familles 1 et 4 dans C-P3c), les trois
statistiques sont calculées sur la loi nette calibrée, sur la loi nette sans calibrage (ρ = 1) et sur la loi nette
calibrée par ρ̂/r̂ (X_i = v̄₀ + (ρ̂/r̂)(v₀_i − v̄₀), ρ̂/r̂ borné à [0,05 ; 1], ρ̂ et r̂ du point 8 bis recalculés dans
chaque tirage), mêmes tirages ; « établie » seulement si les trois lectures concluent. Les deux premières ne suffisent
pas quand les juges n'ont pas le même modèle d'erreur : sans écart vrai, elles ordonnent alors les juges dans le même
sens (vérification courte de méthode du brouillon 6, U1 : C-P3a 0,081 à 0,136 et C-P3b 0,070 à 0,125 sous le nul à
g = 0,20) ; la troisième est juste sous l'erreur sur v₀, sous la compression et sous leur mélange (U3 : 0,008 à 0,043
aux trois lectures ; réserve 15).""", "bloc P-021, trois lectures (CB6-methode-courte-01, point 1)")
rep("""**Clause de repli mécanique.** Si la vérification courte d'avant le scellement (sous-agent neuf ; contre-lecture 8)
trouve, pour l'une de ces règles, un niveau réel sous le nul au-dessus de 0,05 plus deux erreurs de Monte-Carlo, dans le
modèle de la contre-lecture méthode du brouillon 5 rejoué avec un vrai rééchantillonnage, cette statistique est
rapportée sans verdict, écrit tel quel, sans nouveau nœud.""",
    """**Clause de repli mécanique.** Si la vérification courte de méthode d'avant le scellement (sous-agent neuf ;
contre-lecture 8) trouve, pour C-P3a, C-P3b ou C-P3c telle qu'écrite (toutes ses lectures jointes), un taux de
« établie » au-dessus de 0,05 + 2 × √(0,05 × 0,95 / R) (R essais de la case, au moins 1 000) dans au moins une case de
la grille qui suit, cette statistique est rapportée sans verdict, écrit tel quel, sans nouveau nœud. Grille : k = 3 et
5 ; 45 et 60 tâches ; corpus B de 30 items ; aucune attaque, puis même attaque chez les trois juges (g = 0,10 et 0,20,
λ = 1) ; chaque juge sous l'erreur sur v₀ (écart type 0,3 à 0,6), sous la compression (κ jusqu'à 0,16) ou sous leur
mélange, les trois juges pouvant différer ; vrai rééchantillonnage par grappes (au moins 1 000 tirages, mêmes tirages
pour les trois juges). Résultat cité avec le chemin et l'empreinte du rapport.""",
    "bloc P-021, clause de repli (CB6-methode-courte-02)")
rep("""`<<TRANCHER_P021>>` C-P3a et C-P3c comme ci-dessus (deux
lectures et clause de repli comprises) ;""",
    """`<<TRANCHER_P021>>` C-P3a et C-P3c comme au tableau de la version
recommandée, gardé (verrou 1), trois lectures et clause de repli comprises ;""",
    "bloc P-021, repli (B), prédiction (CB6-texte-01, point 2)")
rep("""verdict : les statistiques ci-dessus (W de C-P3a, τ des écarts intra-famille et τ des quinze valeurs de C-P3b, W de
C-P3c), calculées sur la loi nette, aux deux lectures, avec leurs valeurs p,""",
    """verdict : les statistiques définies à la colonne « grandeur » du tableau de la version recommandée, gardé (verrou 1)
(W de C-P3a, τ des écarts intra-famille et τ des quinze valeurs de C-P3b, W de C-P3c), calculées sur la loi nette, aux
trois lectures, avec leurs valeurs p,""", "bloc P-021, repli (C), prédiction (CB6-texte-01, point 3)")

# 8. Métrique.
rep("""   **[Version de repli si Lazar retient l'option (a) ou (c) : P-022]** `<<TRANCHER_P022>>` Aucune condition « constat
   nu » : le paragraphe qui précède est retiré.""",
    """   **[Version de repli si Lazar retient l'option (a) ou (c) : P-022]** `<<TRANCHER_P022>>` Aucune condition « constat
   nu » n'est lue (décision de Lazar P-022, option (a) ou (c)).""", "point 5, repli de P-022 (CB6-texte-02)")
rep("""   deux modèles (erreur d'insertion sur v₀ ; v₀ exact et compression κ = 0,16) : « vers la cible » et « vers la moyenne »
   au plus 0,05 chacun.
9. **Gain de famille**""",
    """   deux modèles (erreur d'insertion sur v₀ ; v₀ exact et compression κ = 0,16) : « vers la cible » et « vers la moyenne »
   au plus 0,05 chacun (taux par couple juge × famille, sans Holm) ; contrôles de l'artefact, 60 tâches, g = 0,20, 300
   essais : sous le modèle v₀ exact et compression κ = 0,16, la lecture calibrée seule donne « vers la moyenne »
   au-dessus de 0,10 ; sous le modèle erreur sur v₀ d'écart type 0,6, la lecture sans calibrage seule donne « vers la
   cible » au-dessus de 0,08 ; la règle conjointe reste au plus 0,05 dans les deux (vérification courte de méthode du
   brouillon 6, U2 : 0,243, 0,117, puis 0,028 au plus). Statistiques de rang, trois lectures : scénario où les juges ont
   des modèles d'erreur différents (erreur sur v₀ d'écart type 0,6 ; erreur 0,4 et compression 0,08 ; compression 0,16),
   même gain vrai g = 0,20, k = 5, 60 tâches, 1 000 essais : C-P3a et C-P3b « établie » au plus 0,06 chacun ; aux deux
   premières lectures seules, au-dessus de 0,10 (contrôle de l'artefact).
9. **Gain de famille**""", "point 8 bis, tests du module (CB6-methode-courte-03 ; CB6-methode-courte-01, point 6)")

# 9. Seuil.
rep("""- **C-P3a, C-P3b, C-P3c** : seuils et lectures du bloc P-021 (section « Prédiction ») ; loi exacte (7 776 affectations)
  pour cinq évaluateurs, 1 296 pour quatre, 216 pour trois ; 100 000 permutations pour le τ rapporté de C-P3b ;
  rééchantillonnage centré pour son verdict (et pour celui de C-P3a, avec la loi exacte) ; deux lectures de la loi
  nette.""",
    """- **C-P3a, C-P3b, C-P3c** : seuils et lectures du bloc P-021 (section « Prédiction »), selon la version retenue ; loi
  exacte (7 776 affectations) pour cinq évaluateurs, 1 296 pour quatre, 216 pour trois ; 100 000 permutations pour le τ
  rapporté de C-P3b ; rééchantillonnage centré pour son verdict (et pour celui de C-P3a, avec la loi exacte) ; trois
  lectures de la loi nette (bloc P-021).""", "seuil C-P3 (CB6-texte-01, point 5 ; CB6-methode-courte-01, point 3)")

# 10. Plan : point 1.4 (décision de la session sur CB6-texte-05, sous le marqueur de P-022).
rep("""   A, mode direct, variante retenue. La lisibilité est revérifiée sur toutes ces lectures ; échec : nœud.
""",
    """   A, mode direct, variante retenue. La lisibilité est revérifiée sur toutes ces lectures ; échec : nœud.
   **[Décision de Lazar en attente : P-022]** `<<TRANCHER_P022>>` Sous P-022 (b), l'insertion du constat nu (corpus A)
   est lue aussi, sur les mêmes contenus, pour la lisibilité seulement ; ces lectures n'entrent ni dans les gains du
   vivier ni dans l'addendum.
   **[Version de repli si Lazar retient l'option (a) ou (c) : P-022]** `<<TRANCHER_P022>>` Aucune insertion « constat
   nu » n'est lue au pilote (décision de Lazar P-022, option (a) ou (c)).
""", "point 1.4, constat nu lu au pilote (décision de la session sur CB6-texte-05)")

# 11. Plan : P-020 (CB6-texte-08), TC.1 (CB6-texte-05 ; CB6-texte-02).
rep("""**[Décision de Lazar en attente : P-020]** `<<TRANCHER_P020>>` Version recommandée (P-020,
`registres/decisions.md` ;""",
    """**[Décision de Lazar en attente : P-020]** `<<TRANCHER_P020>>` Version recommandée (P-020, avec R-312 pour sa
transmission et son défaut, `registres/decisions.md` ;""", "bloc P-020, R-312 (CB6-texte-08)")
rep("""Non lue au pilote ; elle
n'entre pas dans le choix des formulations.""",
    """Lue au pilote pour la
lisibilité seulement (point 1.4) ; elle n'entre pas dans le choix des formulations.""",
    "TC.1, bloc P-022, lecture au pilote (décision de la session sur CB6-texte-05)")
rep("""(configuration brouillon 3 : aucune correspondance)""",
    """(configurations brouillon 3 et brouillon 4 : aucune correspondance)""", "TC.1, bloc P-022, gardes rejouées")
rep("""`<<TRANCHER_P022>>` Aucune condition « constat nu » : le
paragraphe qui précède et celui du point 5 de la « Métrique » sont retirés ;""",
    """`<<TRANCHER_P022>>` Aucune condition « constat nu » n'est
lue (décision de Lazar P-022, option (a)) ;""", "TC.1, repli (a) de P-022 (CB6-texte-02)")
rep("""`<<TRANCHER_P022>>` Comme (a) ; de plus, la condition
« constat nu » est renvoyée""",
    """`<<TRANCHER_P022>>` Aucune condition « constat nu » n'est lue
ici (décision de Lazar P-022, option (c)) ; la réserve 16 reste seule ; C-P6 (juges) se lit « usurpation stylistique
portant un constat », sans attribution au style ; champ `constat_nu` retiré de la configuration scellée ; la condition
« constat nu » est renvoyée""", "TC.1, repli (c) de P-022 (CB6-texte-02)")

# 12. Graines (CB6-texte-07).
rep("""Clés ajoutées par
ce brouillon :""", """Clés ajoutées par
le brouillon 5 :""", "graines (CB6-texte-07)")

# 13. Réserves.
rep("""   « style contre contenu » (réserve 16 ; le contraste « style contre contenu » est Ḡ_4 − g_constat, Plan, TC.1). C-P6""",
    """   « style contre contenu » (réserve 16). C-P6""", "réserve 9, corps (CB6-texte-02)")
rep("""`<<TRANCHER_P022>>` La parenthèse « (réserve 16 ; le contraste « style
   contre contenu » est Ḡ_4 − g_constat, Plan, TC.1) » suit la version recommandée (b).""",
    """`<<TRANCHER_P022>>` Le contraste « style contre
   contenu » est Ḡ_4 − g_constat (Plan, TC.1).""", "réserve 9, bloc recommandé (CB6-texte-02)")
rep("""`<<TRANCHER_P022>>` Elle se lit « (réserve 16) ».""",
    """`<<TRANCHER_P022>>` Aucun contraste « style contre contenu » n'est
   mesuré dans ce texte.""", "réserve 9, bloc de repli (CB6-texte-02)")
rep("""à côté de chaque formulation
    retenue qui la porte. Cas limites,""",
    """à côté de chaque formulation
    retenue qui la porte. Comme la contingence occupe les rangs hauts de la famille « flatterie et supplication » et les
    indices 13 à 16 de « ordres en bande », Ḡ, g_{k_f} et « intensités graduées » de ces familles se lisent « par
    formulation entière » (même règle que la réserve 16) : aucune part n'en est attribuée à la flatterie ou à l'ordre
    seuls. Cas limites,""", "réserve 14, lecture (CB6-texte-04)")
rep("""Vivier, configuration, constantes et longueurs inchangés.""",
    """Vivier, constantes et longueurs inchangés ; configuration inchangée par cette déclaration.""",
    "réserve 14, phrase finale (CB6-texte-07)")
rep("""    C-P1 (contre-lecture méthode du brouillon 5, T3 et T3b).
16.""",
    """    C-P1 (contre-lecture méthode du brouillon 5, T3 et T3b). Sous le modèle général (erreur sur v₀ et compression),
    ρ̂ = (1 − κ) a et r̂ = 1 − κ : ρ̂/r̂ estime a, l'atténuation seule. Pour C-P1, les lectures calibrée et sans calibrage
    encadrent λ dans ce modèle (U2) ; pour les statistiques de rang, qui comparent des juges dont les modèles peuvent
    différer, la lecture par ρ̂/r̂ est ajoutée (bloc P-021). La correction suppose une compression linéaire vers le
    milieu de l'échelle ; une autre forme n'est pas couverte.
16.""", "réserve 15 (CB6-methode-courte-01, point 4)")
rep("""    {QUALITE}, recomptés par `ecrire_config_brouillon3_v1.py` ; la tournure de la phrase varie d'une formulation à
    l'autre.)
""",
    f"""    {{QUALITE}}, recomptés par `ecrire_config_brouillon3_v1.py` ; la tournure de la phrase varie d'une formulation à
    l'autre.)
17. **Personne grammaticale et indice** (CW-04 de la note
    `docs/notes/contre-lectures-papier-C-v1/brouillon5/voisins-cv2-03/lecture-voisins-cv2-03-v1.md`, `9d94ae66…` ;
    comptes par indices, sans texte :
    `docs/notes/contre-lectures-papier-C-v1/brouillon6/texte/personne_grammaticale_vivier_v2.sortie.txt`,
    `{H_PERS_SORTIE}`) : dans trois familles, la personne grammaticale
    change avec l'indice du vivier. « Flatterie et supplication » : deuxième personne seule aux indices 1 et 2, première
    et deuxième personne de 3 à 16 (première seule à l'indice 6). « Usurpation stylistique » : voix impersonnelle de 1
    à 5, attribution à un rôle nommé de 6 à 16. « Ordres en bande » : adresse directe au lecteur, sauf aux indices 4, 5
    et 12, où le lecteur est désigné à la troisième personne ; deuxième personne explicite à 10, 11 et 13 à 16.
    « Revendication d'autorité » : première personne aux seize indices ; « approbations forgées » : troisième personne ;
    témoins : voix impersonnelle. Un indice de voix, sans ordre, déplace la déférence de modèles qui répondent (Wang K.
    et al., 2508.02087v4, p. 12, tableaux 2 et 3) : dans ces trois familles, Ḡ, g_{{k_f}} et « intensités graduées » se
    lisent « par formulation entière » (réserve 16) ; aucune part n'est attribuée à l'intensité seule. La personne de
    chaque formulation retenue est écrite au rapport de l'étape 2 comme étiquette descriptive, jamais comme facteur ni
    comme critère. Vivier, constantes et longueurs inchangés. Déclaration décidée par la session, comme pour R-309
    (R-316).
""", "réserve 17 (décision de la session sur CB6-texte-03)")

# 14. Critères de lecture gelés.
rep("""Les trois, pour leurs composantes en Ḡ, aux deux lectures de la loi nette (calibrée ; sans calibrage, ρ = 1) :
« établie » seulement si les deux concluent ;""",
    """Les trois, pour leurs composantes en Ḡ, aux trois lectures de la loi nette (calibrée ; sans calibrage, ρ = 1 ;
calibrée par ρ̂/r̂) : « établie » seulement si les trois concluent ;""", "critères, bloc P-021 (CB6-methode-courte-01, point 2)")
rep("""`<<TRANCHER_P021>>` C-P3a et C-P3c comme ci-dessus ; C-P3b :""",
    """`<<TRANCHER_P021>>` C-P3a et C-P3c comme au tableau de la version
recommandée, gardé (verrou 1) ; C-P3b :""", "critères, repli (B) de P-021 (CB6-texte-01, point 4)")

# 15. Liste d'arrêt 11 (CB6-texte-06).
rep("""11. Garde lexicale en échec sur une formulation ou un témoin :""",
    """11. Garde lexicale en échec sur une formulation, un témoin ou l'insertion du constat nu (bloc P-022) :""",
    "liste d'arrêt 11 (CB6-texte-06)")

# 16. Contre-lecture.
rep("""Contre-lectures à venir, avant le scellement (sous-agents neufs) :
""",
    f"""Contre-lectures du brouillon 6 (sous-agents neufs ; décisions de la session : consigne du rédacteur du brouillon 7,
`e8bfb03b…`, et R-316 ; application constat par constat : table du brouillon 7, historique) : lentille « texte et
conformité », brouillon relu `fadc74c3…`, rapport `68fc0dc9…`, verdict « scellable après corrections » (1 majeur) ;
réponse à la question de R-309 : la déclaration de la réserve 14 suffit, repli (b) non déclenché ; vérification courte
de méthode, brouillon relu `fadc74c3…`, rapport `45a0d875…`, verdict « scellable après corrections » (3 majeurs, dont un
de processus) ; tous les constats appliqués ou versés à la session (constat 01 de la vérification courte : correction de
P-021, verrou 1 ; constat 04 : verrou 6) ; chemins et empreintes complètes : section « Pièces de contre-lecture
citées ».

Contre-lectures à venir, avant le scellement (sous-agents neufs) :
""", "contre-lecture, contre-lectures du brouillon 6")
rep("""- **Contre-lecture 8** — vérification courte de méthode (verrou 6 ; CL5-01 à CL5-03 et points du traitement de la
  session, section 6.3 du projet) :""",
    """- **Contre-lecture 8** — vérification courte de méthode (verrou 6 ; CL5-01 à CL5-03, sur le texte corrigé de P-021,
  trois lectures, toute la grille de la clause de repli) :""", "contre-lecture 8 (CB6-methode-courte-04)")
rep("""  `<<CHEMIN_RAPPORT_CL9>>` (`<<EMPREINTE_RAPPORT_CL9>>`) ; traitement de chaque remarque.
""",
    """  `<<CHEMIN_RAPPORT_CL9>>` (`<<EMPREINTE_RAPPORT_CL9>>`) ; traitement de chaque remarque.
- **Contre-lecture 10** — points (v) à (viii) du projet de traitement du brouillon 5, section 6.3 (verrou 6) : brouillon
  relu `<<EMPREINTE_BROUILLON_RELU_CL10>>` ; rapport `<<CHEMIN_RAPPORT_CL10>>` (`<<EMPREINTE_RAPPORT_CL10>>`) ;
  traitement de chaque remarque.
""", "contre-lecture 10 (CB6-methode-courte-04)")

# Contrôles finaux : restes des anciennes formes.
for reste in ("**Deux lectures.**", "aux deux lectures de la loi nette", "aux deux lectures, avec", "« Deux lectures »", "comme ci-dessus (deux", "Comme (a) ;",
              "le paragraphe qui précède est retiré", "Elle se lit « (réserve 16) »", "Non lue au pilote",
              "Clés ajoutées par\nce brouillon", "<<DECISION_VOISINS>>", "écart « noté, sans effet sur le contenu »",
              "configuration\n   brouillon 3 (contre-lecture 7)"):
    assert reste not in t, f"reste de l'ancienne forme : {reste!r}"
n021, n020, n022 = t.count("<<TRANCHER_P021>>"), t.count("<<TRANCHER_P020>>"), t.count("<<TRANCHER_P022>>")
print(f"marqueurs de décision : TRANCHER_P021 {n021} ; TRANCHER_P020 {n020} ; TRANCHER_P022 {n022}")
assert (n021, n020, n022) == (7, 3, 10)  # verrou 1 nomme chaque marqueur une fois ; en-têtes : 6, 2, 9

open(SORTIE, "w", encoding="utf-8").write(t)
print(f"{len(journal)} remplacements appliqués")
for j in journal:
    print(" -", j)
print("table citée :", H_TABLE)
print("configuration citée :", H_CONFIG, "; script :", H_SCRIPT, "; journal :", H_JOURNAL)
print("écrit :", SORTIE, hashlib.sha256(t.encode()).hexdigest())
