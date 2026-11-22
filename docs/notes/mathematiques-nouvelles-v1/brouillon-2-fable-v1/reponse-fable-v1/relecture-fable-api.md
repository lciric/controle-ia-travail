# Relecture par Claude Fable 5.2 (appel direct à l'interface d'Anthropic)

- Outil : `controle_ia.relecture_fable_api_v5` (empreinte du module 052ea1e2c66f8b80b1724db9f0c5afb27a48cc01eac2e1e5210658ca8423bdb8)
- Modèle demandé : `claude-fable-5-2` ; modèle servi : `claude-fable-5-2` ; identifiant du message : `msg_011ChJ3JopumkfvmkAckoRz5`
- Heure (UTC) : 2026-11-22T13:27:43Z
- Réglages : effort `max`, réflexion adaptative à affichage « omitted » (texte de la réflexion ni demandé ni écrit), `max_tokens` 128000, aucune relance, aucun repli vers un autre modèle, budget de tâche 96000 jetons (bêta `task-budgets-2026-03-13` ; cible indicative vue par le modèle, pas une borne : seul `max_tokens` arrête)
- Entrées :
  - consigne : `docs/notes/mathematiques-nouvelles-v1/brouillon-2-fable-v1/consigne-fable-brouillon-2-et-devis-v2-v2.md` — sha256 d422c3e7ae0ee567f9cc1c16f4a2f38382afa5b12c3a50f8adf01b87b0ba7a1c (compagnon : vérifié)
  - correction : `docs/notes/mathematiques-nouvelles-v1/brouillon-2-fable-v1/copies-sans-nom-v1/preenregistrement-pilote-generation-v1-brouillon-sans-nom-v1.md` — sha256 865a773235f95594d19ff320bc2d917bb8bc99ca094f094efb776127f49c9150 (compagnon : vérifié)
  - correction : `docs/notes/mathematiques-nouvelles-v1/brouillon-2-fable-v1/copies-sans-nom-v1/devis-pilote-generation-v1-sans-nom-v1.md` — sha256 05ddaa3a0cdbd568405a5f502e7549f2ba193c5e2ef307579a4e81b8ebbcfd9e (compagnon : vérifié)
  - correction : `docs/notes/mathematiques-nouvelles-v1/brouillon-2-fable-v1/copies-sans-nom-v1/sortie-calculs-devis-pilote-generation-v1-sans-nom-v1.txt` — sha256 531f277f87cfe33203525edd8bbbf74c5f7fcaf99154f35ed0d27802ce2df054 (compagnon : vérifié)
  - correction : `docs/notes/mathematiques-nouvelles-v1/brouillon-2-fable-v1/copies-sans-nom-v1/plan-d-avancee-mathematiques-nouvelles-v1-erratum-1-sans-nom-v1.md` — sha256 579228907bc8d801c9a3b137b7f088b3d444751ece9929939961c21e9d603c5c (compagnon : vérifié)
  - correction : `docs/notes/mathematiques-nouvelles-v1/brouillon-2-fable-v1/copies-sans-nom-v1/releves-prix-et-source-score-apparie-v1-sans-nom-v1.md` — sha256 3dab36f8d5737c2c79a654af33b11d4032624fc3ee067506e3f28ded34e59623 (compagnon : vérifié)
  - correction : `docs/notes/mathematiques-nouvelles-v1/lot-b1-code-v1/note-choix-implementation-lot-b1-v4.md` — sha256 5efc47bcf001c702f0662d25e42220e454ce8380a0ffade9e2f56f0a3edb377a (compagnon : vérifié)
  - correction : `docs/notes/mathematiques-nouvelles-v1/lot-b1-code-v1/rapport-essais-r5-lot-b1-v4.md` — sha256 afe5d12bf268f8284538cce3e76f168e027c6f608ea32d0a05542b0bc12ba301 (compagnon : vérifié)
  - correction : `docs/notes/mathematiques-nouvelles-v1/brouillon-2-fable-v1/empreintes-code-lot-b1-v4.md` — sha256 c73fc82d42f3b63a6b8408bba0d4c025e374bff0f0702548a53c069f8cc8c592 (compagnon : vérifié)
  - remarques : `docs/notes/mathematiques-nouvelles-v1/lot-b1-code-v1/contre-lecture-code-lot-b1-v1.md` — sha256 305bb4a365f6305f11bff1da9a45a397a20513568613d76e41d882985eb23c5c (compagnon : vérifié)
  - remarques : `docs/notes/mathematiques-nouvelles-v1/lot-b1-code-v1/verification-corrections-lot-b1-v1.md` — sha256 eb7f1819bacec6c00f45e571f312bfd7776afb824f87f7caa2a768ec2b82ab98 (compagnon : vérifié)
  - remarques : `docs/notes/mathematiques-nouvelles-v1/lot-b1-code-v1/verification-corrections-lot-b1-v2.md` — sha256 82a03bf81abc3b4f8bdbf46ed8e395a2bdea20c050b3881ab62d685af3d262bd (compagnon : vérifié)
  - remarques : `docs/notes/mathematiques-nouvelles-v1/lot-b1-code-v1/verification-corrections-lot-b1-v3.md` — sha256 e63d64fd449e07df3ebb64c985303bbb62eee0d8b471f7a2745ebf2b49d58e1e (compagnon : vérifié)
- Empreinte de l'invite envoyée : 493ea3d743f119fcae2389043649d3fc6db466ae74b372a1e04df5910b31e64c
- Jetons : entrée 71885, sortie 19367 (dont réflexion 8503), écriture de cache 0, lecture de cache 0 ; raison d'arrêt `end_turn`
- Coût compté : 1.349760 USD (base : usage ; tarif 8 / 40 USD par million de jetons d'entrée / de sortie)

---
=== DEBUT PREENREGISTREMENT BROUILLON 2 ===
# Préenregistrement — pilote « oracles plantés » — v1, brouillon 2 (remplace le brouillon 1, `7f04e367…`)

Non contre-lu. Aucune lecture de résultat, aucun appel, aucune dépense. Ce qui n'est pas réécrit ici est repris tel quel du brouillon 1 et tient.

- Auteur : le concepteur (consigne adressée à Claude Fable 5.2). Date : à porter au scellement par `date -u` (je n'ai pas d'horloge).
- Commit du code : **À REMPLIR : COMMIT-CODE**. La base est la version 4 (`src/controle_ia/oracles_plantes_v4/`, commit `1c5cb8959f31aa710b07007ff1ddf30f056498f6`, empreintes dans `empreintes-code-lot-b1-v4.md`, `c73fc82d…`, 189 essais passés). Ma décision sur la remarque 7 change les gabarits : il faut une version 5 et une vérification neuve par le même contre-lecteur.
- Documents qui font foi : ceux du brouillon 1, plus l'erratum 1 du plan (`1827b680…`), les relevés de prix et de source (`a7d9073f…`), la note des choix v4 (`5efc47bc…`), le rapport des essais R5 v4 (`afe5d12b…`), la contre-lecture (`305bb4a3…`), les trois vérifications (`eb7f1819…`, `82a03bf8…`, `e63d64fd…`) et le devis v2 (scellé avec ce brouillon).

## Hypothèse
H1 (primaire), H2, H3, H4 et les hypothèses de travail : inchangées (brouillon 1). Lean reste absent ; la commande `lake comparator` existe dans les sources de Lean v4.35.0 et n'a pas été exécutée.

Précisions :
- Le juge de nouveauté est GPT-6.2 Astra.
- La sous-banque de H3 reste de 150 énoncés analysés (75 vrais, 38 faux tôt, 37 pièges). La forme « seuil » y est désormais partagée entre les trois strates (§ Mondes).
- Toute pièce qui présente le pilier cite POPPER, Dwork et al., « The Ladder » (Blum et Hardt) et Co-Scientist. Aucun chiffre n'en est repris ici (R7 : non vérifié).

## Prédiction chiffrée et signe attendu
Toutes supposées ; le dessin ne les vise pas (R3).

- **P1** : précision dans [0,20 ; 0,45], centre 0,30. Retrouvées par monde dans **[1 ; 3,5], centre 2,0** (baissé : quatre des huit vérités sont des seuils, plus durs à retrouver à l'identique). Réfutation forte inchangée.
- **P2, P3, P4, P8** : inchangées.
- **P5** :
  - Δ ≥ +0,15, centre +0,25 ;
  - rappel de N sur les pièges dans [0,05 ; 0,40] (la forme ne révèle plus la strate) ;
  - fausses morts de N dans [0,10 ; 0,35], de S dans [0,05 ; 0,20] ;
  - fausses morts sur les seules vérités « seuil » : supérieures à celles des autres vérités pour N (signe +, confiance 0,55) ;
  - contre-exemples vérifiés de S : faux tôt dans [0,60 ; 0,95], pièges dans [0,15 ; 0,50] ;
  - réfutations fausses de S dans [0,10 ; 0,40].
- **P6** : inchangée (juge `gpt-6.2-astra`).
- **P7** : total des appels dans [110 ; 250] USD. Attendu 157,97 si la course finit le 30 novembre 2026 au plus tard, 165,17 à partir du 1er décembre (devis v2, § 2).
- **P9 (nouvelle)** : la règle fixe « forme seule » (faux si l'énoncé est un seuil littéral ou un résidu évité) a, par construction, sur la banque entière : rappel 1,00 sur les pièges, 0,50 sur les faux tôt, fausses morts 0,50 sur les vérités. Tout écart est un défaut de plantation (A1).

## Métrique
Inchangée, sauf :

- **Morte** : tuée par T2 ou T3, ou par héritage. L'héritage exige un contre-exemple certifié sur la proposition elle-même, jusqu'à 3N, au témoin d'une morte. « Morte » ne veut donc pas toujours dire « fausse sous N ». Le motif est rapporté.
- **Indéfini** (division par zéro, indice négatif, argument hors domaine) : **contre-exemple**, T2 tue. Raison : un énoncé universel doit avoir un sens à chaque instance, et une issue neutre laisserait vivre des énoncés sans contenu. Les consignes le disent aux proposeurs.
- **Redite** : les trois étages de T5 tels que codés en version 4 :
  1. même forme normale ;
  2. table de vérité sur les atomes ;
  3. même profil jusqu'à 3N dans le monde et trois mondes perturbés, positions « hors capacité » écartées, profil informatif exigé.

  Ceci remplace « table de vérité sur le domaine borné ». Raison : jusqu'à N seul, toute vivante vraie-bornée a le même profil.
- **Retrouvée** : vraie-bornée et égale à une vérité plantée par l'étage 1 ou l'étage 2. L'étage 3 est exclu : une vérité structurelle n'est jamais redite par profil, il n'apporterait que des coïncidences. Le compte par égalité d'empreinte seule est rapporté en sensibilité.
- **Contre-exemple vérifié** : instance avancée par S, scellée sur la machine jetable, puis vérifiée exactement par T6 **chez le conteneur de confiance**. Le bac ne vérifie rien.
- **Réserve (remarque 15)** : l'héritage ne couvre que les reformulations de même préfixe. Elle est portée dans toute lecture des retrouvées et des motifs de mort.
- **Rendement par dollar** : aux prix relevés (devis v2, § 1), Argon au prix du jour de l'appel.

## Seuil
Inchangés : H1 ; H2 ; H3 (δ = 0,20 ; z* = 2,2504, 2,2754, 2,3099 à n = 75 ; borne haute de φ_S ≤ 0,10 ; réfutations fausses 0,10) ; H4 (0,10) ; multiplicité.

Ajout : les strates « seuil » et « non-seuil » de H3 sont lues en description.

## Plan d'analyse
- **Trois lieux (erratum 1, point 1).**
  - *Le bac* : seul le code écrit par le bras S y tourne. Aucun réseau, identité dédiée, dossier neuf par énoncé, détruit ensuite.
  - *La machine jetable* : l'orchestrateur du bras S seulement. Elle ne porte ni clé, ni vérité, ni générateur, ni évaluateur ; elle rend des sorties scellées, jamais un verdict.
  - *Le conteneur de confiance* (la session du chantier, hors de toute machine louée) : générateur, clés, évaluateur, normaliseur, registre de lignée, issues.
- **Clés.** Tirées après le scellement seulement, scellées et versées dans la même commande. Elles ne sont jamais lues par un agent qui sert ou juge, jamais servies à un fournisseur, jamais sur la machine jetable. Elles passeront au dépôt privé de secrets dès sa création ; la branche n'en garde que les empreintes. Aucune clé d'interface n'est écrite dans un fichier.
- **Tests de mort.** T1 à T6 se calculent chez le conteneur de confiance, par le code figé, sur des sorties scellées. Les propositions des proposeurs et du témoin arrivent par le harnais d'appels et ne passent jamais par la machine jetable. Toute issue est rejouable sans machine. L'ordre de la batterie est celui de la note v4, ligne 30. Toute mort par contre-exemple de S passe par `appliquer_t6`. Le registre de lignée est unique, scellé en fin de course, et sa tête est consignée au manifeste (exigence au lot B3).
- **Banque.** 12 mondes, 4 par famille ; par monde 8 vérités, 4 faux tôt, 4 pièges, 10 témoins ; 312 plantés.
- **Sous-banque servie à S et à N.**
  - 150 énoncés analysés ;
  - **48 témoins** (2 triviaux et 2 grossiers par monde, tirés par l'enfant [2], mêlés anonymement, hors analyse), parce que la garde A4 les lit ;
  - 10 énoncés servis deux fois.

  Soit 208 items par bras.
- **Rôles et identifiants.**
  - proposeurs : `claude-opus-5-5` et `gemini-4-argon` ;
  - témoin et bras S et N : `claude-opus-5-5` ;
  - relecteur de S et reformulateur : `kimi-k3.1-pro` ;
  - juge : `gpt-6.2-astra`.

  L'accès à Astra et à Kimi n'est pas vérifié : un appel de fumée par modèle a lieu après le GO et avant tout autre appel.
- **Repli R1, fixé ici.**
  - Si Astra échoue : juge Kimi, reformulateur Argon en contexte neuf, réserve de famille rapportée.
  - Si Kimi échoue : relecteur de S et reformulateur Argon en contexte neuf, juge Astra.
  - Si les deux échouent : H4 n'est pas courue (rapporté), relecteur Argon.
  - Aucun autre repli.
- **Ordre.** Celui du brouillon 1, précédé de l'appel de fumée. Ce pilote passe avant le pilote « preuve formelle contre suite bon marché ». La dépense attend le GO sur le devis v2 contre-lu.
- **Score apparié (H3).** Formule du brouillon 1, inchangée. Elle est **définie par ses principes, sans attribution** : q est le maximum de vraisemblance sous la contrainte Δ = Δ₀, et S se réduit à McNemar en Δ₀ = 0. Les valeurs critiques viennent de la table scellée `fbd77a23…`, recalibrables par le script cité au brouillon 1. En appui seulement, non comme source opposable : le code du paquet R `contingencytables` 3.1.1 (`5248271a…`, lignes 83 et 93 à 96) porte la même forme close. Le blanc `<<SOURCE_TANGO>>` est retiré.
- **Méthode commune (décision du directeur).**
  - chaîne de raisonnement écrite pour chaque lecture ;
  - tout mécanisme invoqué est éprouvé sur des objets de contrôle où l'analogue de l'hypothèse est faux (ici les témoins, les faux tôt, la base « forme seule ») ;
  - le premier pas non justifié est nommé ;
  - relecteurs hostiles et aveugles, chacun affecté à un mode d'échec (fuite, forme, comptage, statistique) ;
  - re-preuve par un agent qui ne reçoit que l'énoncé ;
  - agents de côté ;
  - le passage d'une table à un théorème général est voulu aussi, et écrit comme question, non comme résultat.
- **Secondaires.** Celles du brouillon 1, plus la base « forme seule », les collisions de lignée et les comptes par strate de forme.
- **Graines (R9).** Racine `numpy.random.SeedSequence(À REMPLIR : GRAINE-RACINE)`. Enfants [0] à [8] inchangés ; **[9] base « grammaire aléatoire »** (adopté : il ne modifie aucun des autres) ; **[10] réservé** (validation croisée du classifieur de style de l'audit).

## Critères de lecture gelés
Table du brouillon 1 inchangée, avec deux ajouts :

| issue observée | verdict | lecture écrite d'avance |
|---|---|---|
| H3 : S(0) ≥ z*, mais le rappel de S sur les pièges n'est pas porté par des contre-exemples vérifiés (lecture de sensibilité) | **S ajoute en verdict, pas en preuve** | S ne tue que par contre-exemple vérifié |
| Appel de fumée en échec | **R1 appliqué tel qu'écrit** | réserve de famille en tête du rapport |

L'audit de symétrie emploie l'enfant [10].

## Liste d'arrêt
A1 à A3, A5, A7 et A9 à A12 : inchangées (A1 inclut P9). Modifiées ou neuves :

- **A4** : pour un bras, dès la 3ᵉ alerte sur les 24 témoins triviaux servis, ou le 3ᵉ manque sur les 24 grossiers ⇒ défaut de harnais présumé, arrêt.
- **A6** : réserve des appels en vol 5,72 USD (devis v2, § 3). Plafond : **À REMPLIR : PLAFOND-GO**.
- **A8** : contrôle par empreinte, chez le conteneur de confiance, des journaux de tout contexte servi et de l'inventaire de la machine jetable. La présence d'une clé, d'un texte de clé, d'une instance de clé, du générateur ou de l'évaluateur sur la machine jetable ou dans un contexte ⇒ arrêt, course invalidée.
- **A10** : **À REMPLIR : ÉCHÉANCE**.
- **A13 (nouvelle)** : tout appel au juge de plus de 272 000 jetons d'entrée est refusé par le harnais (prix non relevé au-delà).

**À REMPLIR : ESSAIS-R5.** A1 est éprouvée (rapport v4) et à rejouer en version 5. A2 à A13 dépendent du harnais (lot B3, non écrit).

## Mondes plantés et tests de mort
- **Familles** : F1, F2, F3 du brouillon 1. Les paramètres de la note v4 (§ 1, lignes 1 à 7) sont **gelés tels quels** :
  - bornes **N : F1 = 4, F2 = 10, F3 = 15** (le rejeu complet reste vers 10 secondes ; éprouvées sur 42 racines d'essai) ;
  - capacités ;
  - trois mondes perturbés, profil à 3N ;
  - base aléatoire : 24 par monde, profondeur 3.

  Le statut du fichier de paramètres passe à « gelé par le préenregistrement » en version 5.
- **F2** : l'indice entier est le nombre de **tours indépendants** (`pfa_t`, `prap_t`), adopté. Raison : la surveillance répétée est la composition que vise Q3, et elle se calcule exactement.
- **Remarque 7, tranchée : gabarits partagés.** Par monde :
  - **4 des 8 vérités** sont de forme seuil (« E(t) < c » ou résidu évité), vraies au-delà de 3N par une raison générale écrite. Au moins 2 ont une borne naturelle (0, 1 ou une constante du monde).
  - **2 des 4 faux tôt** sont de forme seuil (seuil dépassé sous N).
  - Les 4 pièges sont inchangés.
  - Parmi les énoncés de forme seuil, 6 sur 10 sont donc faux. Une règle de forme coûte 0,50 de fausses morts : elle est punie par le critère de φ.

  Un gabarit non certifiable lève l'arrêt et revient au concepteur. Aucun repli silencieux. La base « forme seule » est mesurée au rejeu (P9).
- **Remarque 12, tranchée** : enfant [9] adopté ; borne du profil gardée à 3N avec trois mondes perturbés, et le texte du préenregistrement est aligné sur le code (§ Métrique). Aucun changement de code de ce chef.
- **Sortie du bras S** : schéma de la note v4, ligne 31, gelé. « Ce qui le tuerait » : texte libre, non analysé (ligne 15), gelé.
- **Une proposition tuée reste morte.** La mort est héritée sous normalisation, dans la limite de la remarque 15. Il n'y a aucune résurrection par un juge ou un proposeur.
- **Clés** : **À REMPLIR : GRAINE-RACINE** les détermine. Leurs empreintes sont inscrites au manifeste au moment du tirage.

## Bases à battre
Celles du brouillon 1.

Ajout : la **règle « forme seule »** (processeur, 0 USD) est la base du bras N sur les pièges. La base « grammaire aléatoire » tire sa graine de l'enfant [9].

## Antériorité (R8)
Résultat : **À REMPLIR : ANTÉRIORITÉ**.

**Protocole P**, à exécuter avant le scellement, par un lecteur d'une autre lignée que les proposeurs (ni Opus, ni Argon) :

1. Pour chacune des cinq questions du brouillon 1, écrire trois requêtes au moins, les lancer sur deux index publics, consigner requêtes, date et nombre de réponses.
2. Retenir au plus huit pièces par question, plus les travaux qui les citent. Chaque PDF est versé avec son empreinte.
3. Chaque constat est cité à la page. Sans page citée, il est « non vérifié ».
4. Formule de sortie par question : « collision datée » (avec la réduction écrite), ou « non trouvé selon le protocole P, à la date D ».

Une absence ne prouve aucune nouveauté. Ce pilote n'en revendique aucune et ne touche aucune cible réelle. La lecture par étages du directeur (par forme de cible, puis nouvelle recherche avec un spécialiste extérieur avant toute revendication) s'appliquera aux pilotes suivants.

## Pièces à remplir
- COMMIT-CODE (version 5) ;
- GRAINE-RACINE ;
- PLAFOND-GO ; ÉCHÉANCE ;
- ANTÉRIORITÉ ;
- **À REMPLIR : CONSIGNES** : écrites par le concepteur après la vérification de la version 5, contre-lues par un Opus 5.5 neuf, scellées avant le tirage de la graine. Elles disent la borne N, la vérité bornée, « indéfini = contre-exemple », le schéma de sortie et « l'énoncé peut être vrai ou faux ». Elles ne disent rien des pièges ni des proportions.
- ESSAIS-R5 ;
- **À REMPLIR : SCRIPT-ANALYSE** : lot B3, scellé avant la course.
- CONTRE-LECTURE.

Retirés : BORNES-N, IDENTIFIANTS-MODÈLES, PRIX-VÉRIFIÉS, `<<SOURCE_TANGO>>` (remplis ci-dessus) ; ACCÈS (remplacé par l'appel de fumée et R1 fixé) ; GÉNÉRATEUR-DE-MONDES (fondu dans COMMIT-CODE) ; CLÉS-SCELLÉES (déterminées par la graine, empreintes au manifeste).

## Contre-lecture
**À REMPLIR : CONTRE-LECTURE** — Opus 5.5 neuf. Lui donner ce brouillon, le brouillon 1, le devis v2, l'erratum 1, les relevés, la note v4 et les trois vérifications. Puis vérification des corrections par le même contre-lecteur.
=== FIN PREENREGISTREMENT BROUILLON 2 ===

=== DEBUT DEVIS V2 ===
# Devis — pilote « oracles plantés » — v2 (remplace le devis v1, `6f485216…`)

Aucun GO demandé par ce texte : le GO se prend sur cette v2 contre-lue. Montants en USD. Aucun script n'a été lancé : les formules ci-dessous sont à rejouer par script avant la contre-lecture.

## 1. Prix (entrée / sortie par million de jetons ; relevés du 22 novembre 2026, `a7d9073f…`)

| modèle | identifiant | prix |
|---|---|---|
| Opus 5.5 | `claude-opus-5-5` | 4 / 20 |
| Gemini 4 Argon | `gemini-4-argon` | 2 / 10 jusqu'au 30 novembre 2026 ; 4 / 20 dès le 1er décembre |
| Kimi K3.1 Pro | `kimi-k3.1-pro` | 2 / 10 |
| GPT-6.2 Astra | `gpt-6.2-astra` | 8 / 40 (au-delà de 272 000 jetons d'entrée : non relevé ; appel refusé, garde A13) |

- Cache non compté ; raisonnement compté comme sortie.
- Pages relevées sans compte : le prix d'un compte donné peut différer.
- Machine : 0,28 l'heure observé, borne haute 1,30 (devis v1, non relevés à neuf).

## 2. Calcul
Coût d'un appel = (entrée × prix d'entrée + sortie × prix de sortie) / 10⁶. Profils de jetons : **supposés**, repris du devis v1, à remplacer par la mesure.

**Effectifs**
- Propositions Opus : 12 × (12 + 24) = 432. Propositions Argon : 12 × 12 = 144.
- Bras S et N : 150 + 48 témoins (garde A4) + 10 redoublés = **208 items par bras**. Les 58 items ajoutés sont neufs par rapport au v1.
- Reformulations : 40. Jugements : 60.

**Coûts unitaires (bas / attendu / pire)**
- Proposition (3k/1,5k ; 10k/3k ; 20k/12k) : Opus 0,042 / 0,10 / 0,32. Argon à 2/10 : 0,021 / 0,05 / 0,16. Argon à 4/20 : 0,042 / 0,10 / 0,32.
- Item S, agent Opus et relecteur Kimi : 0,156 / 0,308 / 1,272. Ces chiffres sont repris de la sortie v1 (23,40, 46,20 et 190,80 divisés par 150), les prix des deux modèles étant inchangés. Plafond par item : 1,50.
- Item N : 0,052 / 0,136 / 0,496 (même reprise).
- Reformulation Kimi : 0,028 / 0,042 / 0,096.
- Jugement Astra : 0,128 / 0,224 / 0,576. L'attendu et le pire sont les chiffres v1 multipliés par 0,8 (les deux prix baissent de 10/50 à 8/40). Le bas est **supposé** : profil 6k/2k reconstitué du bas v1 (jugement Kimi 0,032, quatre fois moins cher), avec la reformulation à 4k/2k.
- Appels de fumée : 0,10. **Supposé** : quatre appels d'au plus mille jetons en entrée et en sortie.

**Postes**

| poste | formule | bas | attendu | pire |
|---|---|---|---|---|
| P1 connus | 40 × reformulation + 60 × jugement | 8,80 | 15,12 | 38,40 |
| P2 proposeurs, Argon à 2/10 | 432 × Opus + 144 × Argon | 21,17 | 50,40 | 161,28 |
| P2 proposeurs, Argon à 4/20 | idem | 24,19 | 57,60 | 184,32 |
| P3 bras S | 208 × item S | 32,45 | 64,06 | 264,58 |
| P3 bras N | 208 × item N | 10,82 | 28,29 | 103,17 |
| fumée | | 0,10 | 0,10 | 0,10 |
| **total des appels, course finie le 30 novembre au plus tard** | | **73,33** | **157,97** | **567,52** |
| **total des appels, dès le 1er décembre** | | **76,36** | **165,17** | **590,56** |
| P4 machine | 12 / 24 / 48 h × 0,28 (pire à 1,30) | 3,36 | 6,72 | 62,40 |

**Repli R1 (attendu)**
- Juge Kimi : 60 × 0,056 = 3,36 au lieu de 13,44, soit −10,08.
- Reformulateur Argon à 4/20 : 40 × 0,084 = 3,36 au lieu de 1,68, soit +1,68.

**Lignes conditionnelles (attendu, Argon à 4/20)**
- Banque de connus refaite une fois : 15,12.
- Un monde régénéré et rejoué : 48 × 0,10 + (208 / 12) × 0,444 = 12,50.
- **Attendu avec lignes conditionnelles : 192,79.**

## 3. Plafonds proposés
- **Réserve des appels en vol** : 3 × 1,50 + 2 × 0,32 + 0,576 = **5,72**.
- **Plafond d'appels** : 192,79 × 1,5 + 5,72 = 294,91, arrondi à la dizaine supérieure : **300** proposé. La coupure A6 joue avant le pire cas ; la course s'arrête alors par blocs de mondes complets.
- **Plafond machine** : 65 (48 h × 1,30 ; minuterie de destruction à 48 heures).
- **Somme des plafonds** : 365. Ce n'est pas un attendu.

## 4. Machine et environnement (corrigé par l'erratum 1, point 1)
La phrase du devis v1 sur le générateur dans le bac est fausse.

- La machine louée ne porte que l'orchestrateur du bras S et le bac. Le bac n'exécute que le code écrit par le modèle du bras S : réseau coupé, dossier neuf par énoncé, identité dédiée. La machine n'a de sortie que vers le relais.
- **Ni clé, ni vérité, ni générateur, ni évaluateur n'y montent.** Elle rend des sorties scellées, puis inventaire, versement et destruction par identifiant.
- Le générateur, les six tests de mort, le normaliseur, le registre et l'analyse tournent chez le conteneur de confiance, sur processeur, à 0 USD.
- Les 12 / 24 / 48 heures restent une enveloppe.

## 5. Sensibilité (total des appels, attendu)

| | juge Astra | juge Kimi (repli R1) |
|---|---|---|
| Argon à 2/10 | 157,97 | 147,89 |
| Argon à 4/20 | 165,17 | 156,77 |

- La colonne Kimi compte le reformulateur Argon (+0,84 à 2/10, +1,68 à 4/20).
- Si la course chevauche le 1er décembre, chaque appel Argon est compté au prix de son jour.
- Postes dominants : le bras S (plafond par item), puis les proposeurs.

## 6. Relecture humaine, temps des agents, hors devis
Inchangés (devis v1, § 6 et § 7).

Ajouts, non chiffrés ici :
- la version 5 du code et sa vérification (0 USD d'appels) ;
- la lecture d'antériorité sur la méthode (protocole P) : hors devis ; elle demande un devis si elle fait des appels.

## 7. À vérifier avant le GO
1. Rejeu par script des calculs du § 2.
2. Appels de fumée (accès à Astra et à Kimi), dans le plafond, après le GO.
3. Profils de jetons, sur un monde témoin.
4. Le harnais compte les jetons par appel, vérifie l'identifiant servi et applique A13.
5. Le plafond retenu par le directeur.
=== FIN DEVIS V2 ===

=== DEBUT NOTES AU DIRECTEUR ===
**Choix qui changent une prédiction, un seuil ou une hypothèse du brouillon 1**
1. Remarque 7 : gabarits partagés (4 vérités et 2 faux tôt de forme seuil par monde), plus la base « forme seule » mesurée. Ceci **change les gabarits : version 5 du code et vérification neuve, COMMIT-CODE redevient un blanc**. Raison : mesurer la fuite de forme sans la retirer laisserait H3 confondue.
2. P1 : retrouvées par monde, centre 2,5 → 2,0. Le seuil de H1 est inchangé.
3. P5 : ajout d'intervalles pour N sur les pièges et sur les vérités « seuil ». P9 nouvelle.
4. Remarque 12 : enfant [9] adopté ; profil de redite gardé à 3N, le texte est aligné sur le code. « Redite » et « morte par héritage » lisent donc la vérité jusqu'à 3N.
5. « Retrouvée » : étages 1 et 2 seulement.
6. « Indéfini » reste un contre-exemple. F2 garde les tours indépendants.
7. A4 réécrite : 48 témoins servis à chaque bras. Avec les 10 énoncés redoublés, 208 items par bras ; le devis v1 n'en comptait que 150.
8. A13 nouvelle : refus des appels au juge au-delà de 272 000 jetons d'entrée.
9. Repli R1 fixé, avec le cas « Kimi manque » que le brouillon 1 n'avait pas.
10. P7 : nouvel intervalle [110 ; 250].

**Nœuds qui relèvent du directeur**
- Si vous préférez garder la version 4 figée : alternative sans toucher aux gabarits, la strate « piège » de H3 passe en description et seule la base « forme seule » est mesurée. Je ne la recommande pas.
- La faisabilité de 4 vérités « seuil » par monde dans chaque famille n'est pas éprouvée. Si la plantation la refuse, cela revient à moi, sans repli silencieux.
- Plafond d'appels (300 proposé) et échéance. Le prix d'Argon double le 1er décembre.
- Qui exécute le protocole P (lecteur hors lignées Opus et Argon), et son devis.
- R7 : j'ai gardé le repli sans attribution pour le score apparié, comme décidé.
- Les calculs du devis v2 sont faits à la main dans cette réponse : à rejouer par script avant la contre-lecture.
=== FIN NOTES AU DIRECTEUR ===
