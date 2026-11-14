# Vérification courte cumulée du différentiel candidat 3 → candidat 6 — préenregistrement du pilote MR-2 (v1)

**Lecteur** : modèle G, lecteur neuf, autre modèle que le rédacteur (modèle A). Je n'ai écrit aucun des textes lus.
**Texte relu** : `preenregistrement-pilote-conditionnelles-v1-candidat6-compte-organisme.md`, sha256
`8aa33014667da569ec934459d7bc1b1f6b54efa5c2145a6e5bdce5f7fa74603e` (égal à son compagnon `.sha256`). Base : candidat 3,
`539cf171739ee9649719c7c851ebbf8e721e8f225b71ef5ec57ac44e0f8755a6` (conforme à l'attendu).
**Heures** (`date -u`) : début 2026-11-14 22:39:11 UTC ; fin 2026-11-14 22:42:19 UTC.

## Verdict

**Scellable.** Aucun constat bloquant ni majeur ; cinq constats mineurs (dont un hérité du candidat 3), tous des mots périmés ou des
annonces incomplètes ; aucun ne touche la lecture du pilote (issue, seuil, règles P-0/P-1/P-2, plan d'analyse, critères gelés :
aucun de ces passages n'est dans le différentiel). Les constats 1 et 2 sont à corriger si le texte est de toute façon réécrit ; ils ne
justifient pas, seuls, un candidat 7 (une correction impose un nom neuf, R12, et une nouvelle vérification).

## Points a à g

**a. Reprise mot pour mot et annonce des blocs : conforme, avec des annonces incomplètes (constat 4).** J'ai regénéré le
différentiel par `diff -u` (candidat 3 → candidat 6) : identique, hors les deux lignes d'en-tête (noms et dates), au fichier
`differentiel-candidat3-candidat6-cumule.patch` (265 lignes, 16 blocs). Je l'ai lu en entier. J'ai aussi rejoué les trois générateurs
(`faire_candidat_v4.py` depuis le candidat 3 ; `faire_candidat_v5.py` depuis le candidat 4 versé ; `faire_candidat_v6.py` depuis le
candidat 5 versé) vers un dossier de travail : les sorties sont identiques aux candidats 4, 5 et 6 versés hors la dernière ligne
(heures) ; 19, 20 et 12 remplacements comptés, aucun marqueur restant. Les blocs touchent : titre ; statut ; en-tête (prix lus,
proposeurs par leurs clés) ; trois nouvelles tables « Changements depuis le candidat 3 / 4 / 5 » ; ligne « autres mots » de la table
du candidat 2 ; Documents (six lignes) ; « En dix lignes » 9 ; Dessin (en-tête et crédits des deux proposeurs) ; Ordre ; Métrique ;
Liste d'arrêt ; Préalables ; Devis ; Contre-lecture ; Marqueurs ; heures. Aucun bloc ne modifie Question, Hypothèse, Prédiction,
Seuil, Plan d'analyse, Critères de lecture, Audit de symétrie, Code ou Lignes de GO. Chaque bloc est annoncé par une des trois
tables, sauf : la ligne « candidat 5 (gardé) » de Documents (la ligne R-2804 de la table du candidat 6 ne cite pas Documents), le
changement de la ligne des heures finale et la ligne des heures de l'en-tête (constats 1 et 4).

**b. Constats portés : conforme.** Les quatre mineurs de la vérification du candidat 3 : (1) en-tête de la table des proposeurs
« confirmée par la sonde v74 » (diff, ligne 115) ; (2) le nom de famille remplacé par « la lignée du proposeur `fable52` »
(ligne 237) ; (3) origine des causes d'arrêt dite : « R-2738 nomme le champ de réflexion ; les deux autres conditions sont celles du
code v74, rapport du développeur, section 2 » (lignes 154-155) ; (4) ligne « autres mots » ajoutée à la table du candidat 2
(ligne 84). Les trois constats rendus en réponse (PO-039) : « offre standard » dite aux Préalables, au Devis et à la note v2 ;
« offre courte, au plus 272 000 jetons d'entrée ; texte servi au plus 52 000 octets » pour `astra` (Préalables) ; le nom du
fournisseur remplacé par les clés ou par « sur crédits » hors des tables d'historique et des lignes de GO (en-tête, « En dix lignes »
9, Dessin, Devis). Hors tables d'historique, de lignes de GO et de mots exigés par le lecteur gelé, je ne trouve aucun nom de
famille ni de fournisseur (recherche par programme).

**c. Prix : conforme.** Pages recalculées par empreinte : page du premier fournisseur `048ccb65…`, extrait d'`argon` `d4485954…`,
page du troisième `099c9496…`, tous égaux à la note v2. Configuration `f69503dd…` : `fable52` 8/40, `opus55` 4/20, `argon` 10/50,
`astra` 10/50.

| proposeur | candidat 6 | note v2 | page (offre standard) | configuration |
|---|---|---|---|---|
| `fable52` | 8 / 40 | 8 / 40 | 8 / 40 (tableau de base ; mode rapide 16/80, lot 4/20, non utilisés) | 8 / 40 |
| `opus55` | 4 / 20 | 4 / 20 | 4 / 20 (rapide 8/40, lot 2/10) | 4 / 20 |
| `argon` | 2 / 10 jusqu'au 30 novembre 2026 ; 4 / 20 dès le 1er décembre | idem | 2 / 10 « through November 30, 2026 » ; 4 / 20 « starting December 1, 2026 » ; sortie « including thinking tokens » | 10 / 50 |
| `astra` | 10 / 50 (offre courte) | 10 / 50 | première table (onglet Standard) : 10 / 50 ; rapide 20/100, ultrarapide 60/300, lot 5/25 | 10 / 50 |

Dates d'`argon` : conformes. La phrase « aucun prix public de l'offre standard (entrée ou sortie) au-dessus de celui de la
configuration v12 » est vraie : le plus haut écart est nul (trois égaux), `argon` est au-dessous avant et après le 1er décembre.
Le relevé confirme que les appels étaient bien de l'offre standard (usage brut : niveau de service standard, vitesse standard,
zone globale pour le premier fournisseur ; niveau standard pour `argon`). La note v2 ne donne plus de prix absent des pages : le
prix de l'offre longue d'`astra` est dit « pas dans la page versée, qui n'en porte que le bouton » (le bouton « Long : >272K input
tokens » est bien présent, sans tableau) ; le « 75 » de la v1 n'existe dans la page que comme prix d'écriture en cache de l'offre
ultrarapide. Observation sans classe : la page du premier fournisseur porte un multiplicateur de 1,1 pour l'inférence réservée aux
États-Unis ; le relevé dit zone « globale », la configuration n'envoie aucun réglage de zone ; la note v2 ne le mentionne pas.

**d. Coûts : conforme.** Recalcul par programme des huit appels (entrée de l'usage brut × prix + `sortie_comptee` × prix, par million,
en décimaux exacts). Aux prix de la configuration, chaque coût égale le `cout_usd` du relevé : `fable52` 0,008104 + 0,010624 ;
`opus55` 0,004192 + 0,005312 ; `argon` 0,04039 + 0,01341 ; `astra` 0,00398 + 0,01312 ; total **0,099132** = `depense_usd`. Aux prix
publics : `argon` 0,008078 + 0,002682, les six autres inchangés ; total **0,056092**. (Contrôle hors demande : au prix d'`argon` du
1er décembre, 0,066852, toujours sous le relevé.) Sortie comptée et entrées lues dans l'usage brut : 58/191, 48/256, 58/198, 48/256,
69/794, 61/256, 38/72, 32/256, égales à la note v2. Empreintes : relevé `f56d9c0e…`, rapprochement `af1f80f2…`, note v2
`b88253b8…`, tous conformes.

**e. Bloc gelé : conforme.** Un seul début et une seule fin ; le texte entre `<!-- empreintes-du-code-pilote-v74 : début -->` et
`… : fin -->` inclus, plus un saut de ligne, fait 5 345 octets et égale octet pour octet `bloc-releve-sonde-complete-v74.txt`
(5 345 octets ; empreinte `8b5dcfe7…`, conforme). Le bloc n'est dans aucun bloc du différentiel.

**f. Décisions R-2803, R-2804, R-2769 : conformes.** Mot recopié en PO-044. R-2803 : préalable 3 « fait, inscrit par la mère
(R-2803) », « lecture des prix publics, déclarée comme telle », « la console fait foi pour les montants facturés » (Préalables) ;
la phrase est reprise à la Métrique (« le montant réellement facturé n'est lu que sur les consoles des comptes ») ; l'ancien préalable
« prix lus par Lazar à la console » et le marqueur sont levés. R-2804 : vérification cumulée 3 → 6 (le rapport de 3 → 4 n'est pas
versé, celui de 4 → 5 n'a pas été fait), rapport écrit et versé, « si le même refus du classifieur revient, arrêt sans rejouer »
portés à la Contre-lecture et aux Préalables. R-2769 : « inscrit, R-2769 » au total de la sonde (0,099132). Les lignes π1 et π2
« sur le mot de Lazar » : conforme à PO-044. Rien n'est ajouté qui touche la lecture : issue, seuil, règles P-0/P-1/P-2, plan,
critères, liste d'arrêt (hors la précision d'origine du constat 3), devis du pilote (41,72 USD au pire inchangé) ne bougent pas.
Nom « candidat 6 » : le candidat 5 est dit « reste versé, inchangé » (Statut, Documents) et le nom est neuf (R12), mais le texte ne
dit pas que le mot de la mère disait « candidat 5 » : justification implicite seulement (constat 3).

**g. Marqueurs et noms : conforme, avec un reste hérité (constat 5).** Marqueur entre crochets : un seul, `[DATE-GO]` et
`[MOT-LAZAR-GO]` à la ligne 92, dans la table « Changements depuis le candidat 1 ». Aucun identifiant de modèle (« -x-y », numéro de
version, nom d'API) ; les clés `fable52`, `opus55`, `argon`, `astra` seules, et « modèle A, E, F » pour les lecteurs. Noms de famille ou
de fournisseur : seulement dans les tables d'historique (lignes 105, 108, 112), les deux lignes de GO de la sonde (674-675), la ligne
de GO proposée π1 (681) et la phrase des mots exigés par le lecteur gelé (686). Reste : un nom de relais de la course v67 en toutes
lettres à la ligne 240 (section « Question et ce qui existe »), présent trois fois dans le candidat 3.

## Constats

Bloquant : 0. Majeur : 0. Mineur : 5.

1. **Mineur — mot périmé, ligne 40.** « Heures : début et fin de la rédaction du candidat 4 : dernière ligne » ; la dernière ligne dit
   « candidat 6 » (le générateur du candidat 4 l'avait mise à 4 et les suivants ne l'ont pas touchée). Correction : « du candidat 6 »
   (et l'annoncer dans la table du candidat 6, colonne « où » de la ligne R-2804 ou ligne « autres mots »).
2. **Mineur — contradiction avec une annonce, ligne 753.** La table du candidat 6 (ligne 46) annonce « plus aucun "à inscrire par la
   mère" hors des tables d'historique » ; la section Marqueurs porte encore « Levé au candidat 4 : PRIX-CONSOLE (… ; lecture à inscrire
   par la mère) », et le générateur v6 exempte exprès ce fragment. Ce n'est pas une table d'historique. Correction : « lecture inscrite
   par la mère, R-2803 », ou dire dans la ligne 46 que cette seule mention, au passé du candidat 4, est gardée.
3. **Mineur — nom du candidat non justifié en toutes lettres, lignes 3-8.** Le Statut dit que le candidat 5 reste versé, mais pas que le
   mot de la mère (R-2804) demandait « un candidat 5 » et que le nom est pris (R12). Correction : une proposition au Statut, du type
   « (le mot de la mère R-2804 parle d'un candidat 5 ; ce nom existait déjà, R12) ».
4. **Mineur — annonces incomplètes dans les tables d'historique.** Non annoncés : la ligne « candidat 5 (gardé) » de Documents ; la
   phrase d'en-tête « Les prix publics des quatre relais sont lus… » (hors colonne « où » de la table du candidat 4 : « Devis ;
   Préalables ; Ordre ; Métrique ; Marqueurs ») ; la ligne des heures finale. Les titres des tables disent aussi « depuis le candidat N »
   pour ce que fait le candidat N+1 : lisible, mais à lire avec la colonne « ce que fait le candidat… ». Correction : compléter les
   colonnes « où » ; non nécessaire au scellement.
5. **Mineur, hérité du candidat 3 — nom de relais, ligne 240.** « Question et ce qui existe » nomme en toutes lettres deux relais de la
   course v67, dont l'un n'est pas une clé de configuration, hors table d'historique ; non introduit par le différentiel (vérifié dans
   le candidat 3). Correction : « deux relais de la course v67 » ou le laisser, la règle de la table ne visant que ce qui est écrit
   depuis le candidat 3.

Observation sans classe : les heures de rédaction du candidat 6, début 22:38:03 et fin 22:38:03, sont identiques (fichier écrit à
22:38:16) ; même remarque que pour le candidat 3.
