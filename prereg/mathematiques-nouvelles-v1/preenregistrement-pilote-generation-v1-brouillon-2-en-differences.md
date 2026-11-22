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
