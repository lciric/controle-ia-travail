# Contre-lecture de la fiche de lancement de la course Heimersheim (brouillon 2) — v1

Contre-lecteur neuf (règle R2), sous-agent sans part à l'écriture du kit ni de la fiche. 3 novembre 2026, 08:15 UTC (`date -u`).
Aucun appel payant, aucun réseau, aucune clé cherchée ni lue, aucun fichier existant modifié. Seul fichier écrit : ce rapport
(non scellé, non commité).

Objet : `docs/notes/ideation-organisme-v1/course-heimersheim-v1/fiche-lancement-course-heimersheim-v1-brouillon2.md`,
sha256 `a7d3402485f1a86d6f0bdac3bd1657e7ecca0f7b7f9f0f0edc0cde6dfd330ea2` (compagnon `.sha256` vérifié : OK), arbre
`wt-heimersheim`, branche `outils/course-heimersheim-v1`, commit `8fc23349`. Les numéros de ligne renvoient à ce brouillon.

## Verdict

**Scellable après corrections.** Aucun constat bloquant. Cinq constats majeurs : trois se corrigent dans le texte de la fiche
seulement (CLH-01, CLH-02, CLH-04). Deux portent sur le kit (CLH-03 garde lexicale, CLH-05 source du substitut) : correction
recommandée, sinon déclaration nominative dans la fiche. Le gros du kit est conforme (voir « Vérifié conforme »). Si une
pièce du kit change, il faut un nom neuf (R12), de nouvelles empreintes dans les trois configurations, une nouvelle table et une
nouvelle répétition.

## Vérifié conforme

- **Pièces gelées** : les 41 lignes de la table (l. 138-180) ont été recalculées par `sha256sum -c` dans l'arbre : toutes OK.
  Elles couvrent les trois configurations, les cinq consignes, la question, la pièce, la spécification, la source du substitut,
  la liste fermée et les deux lanceurs shell. Il ne reste aucun marqueur de remplissage, sauf `Contre-lecture : <<EMPREINTE_RAPPORT>>` (l. 12).
- **Textes de conv-audit** : les trois copies du kit (`pieces/conv-audit/`) sont identiques à l'octet (`cmp`) aux copies servies
  (`heimersheim-v1/pieces/`). Empreintes : 0e2fd5bc…, e9528e25…, 6445fd6f….
- **Fidélité de la consigne du proposeur** : `construire_consigne_proposeur_heimersheim_v1.py --verifier` rend « conforme ».
  Contrôle indépendant : les trois sections servies de la question (2 572 caractères) et la pièce entière (7 397 caractères) y
  figurent à l'octet. Les règles d'intégrité y sont toutes : niveau méthode, aucune conduite d'agent pour tromper une
  évaluation, chiffre repris cité par pièce et section, « calcul » et « supposé », pas de web.
- **Sections non servies** : le titre, le paragraphe de provenance (mots de Lazar, « brouillon ») et « Lecture prévue de la
  sortie » (règle « 100% human-written » du mentor, réserve κ = 0) s'adressent au lecteur de la sortie. Leur absence ne change
  pas la tâche des proposeurs. L'écart est déclaré (l. 85-87, l. 189).
- **Configurations** : les trois ne diffèrent que par la variante, les proposeurs, les fournisseurs, les relais et le budget.
  Pièces, garde lexicale et bisociateur sont identiques. S17 = 244 USD partout, et la somme des relais fait 244 dans chaque
  variante.
- **Liste fermée** : 37 concepts distincts, tous tirés de la question ou de la pièce. **Source du substitut** : 11 œuvres, une par
  source citée par la pièce, aucun concept hors de la liste. Les quatre concepts sans œuvre (« concept binaire à deux
  centroïdes », « marqueur de vérité neutre en registre », « paire de registre à statut constant », « modèle réellement conscient
  d'être évalué ») sont ceux que la pièce donne comme non faits : c'est juste.
- **Garde lexicale sur les textes servis** : j'ai passé `pole/fiches_v54.trouver` (mode « prefixe ») sur les cinq consignes, la
  liste fermée, la question et la pièce. Rien n'est trouvé. « Claude Sonnet 4.5 », « Opus 4.6 », « Anthropic », « GLM-5 »,
  « Llama-3.1-8B-Instruct » et « Llama 3.3 Nemotron Super 49B » passent.
- **Dépense** :
  - Plafond technique : 244 ≥ 1,2 × 203,15 = 243,78 (calcul).
  - Chaque plafond de session dépasse le pire cas d'un appel de son rôle (devis) : proposeur 3,5 > 3,2408 ; aiguilleur
    0,4 > 0,3379 ; juge 0,9 > 0,8484 ; lecteur 0,9 > 0,8468 ; fusion 3,5 > 3,2872.
  - Relais : Kimi 2 ≥ 0,76 ; Argon 3 ≥ 1,69 ; Claude 106,8 ≥ 90,54 ; Astra 132,2 ≥ 110,16.
  - Nombre d'appels permis par relais : Claude 193 pour 188 au plan ; Astra 135 pour 130 ; Kimi et Argon 7 pour 2. Le noyau
    v56 ne relance aucun appel (une fiche `a_corriger` est retenue sans nouvel appel), donc ces nombres sont fixes.
- **La fiche dit** : course non décisive (l. 16-17), aucun témoin planté (l. 47-49), juge réécrit en écart à « consigne
  inchangée » (l. 50-57, l. 185), bras méta hors course et pourquoi (l. 67-72), source du substitut écrite pour la course
  (l. 61-64, l. 187), espèces (l. 34), plafond technique (l. 89-92), sortie scellée avant lecture (l. 121-122), lecture prévue
  (l. 115-122).

## Constats

### CLH-01 — majeur — liste d'arrêt incomplète : un nœud C13 arrête la course sans rendre une seule fiche

- **Où** : fiche l. 109-113 (§ 5) et l. 124-134 (§ 7). Code : `pole/noyau_v56.py` l. 272-279 ; `pole/budget_v56.py` l. 240-242 ;
  `pole/course2_v56.py` l. 340-367.
- **Le mécanisme** :
  - Après chaque étape, un rôle dont plus de 25 % des appels sont sans sortie exploitable (`arrets.a14_part_max` = 0,25) fait
    marquer l'étape « non mesurée, technique ». C13 tombe alors et un nœud est posé. La génération sort par
    `if self.noeud: return`, avant d'écrire `memoire.json`, `classement.json` et `fiches.json`.
  - Chaque proposeur ne fait qu'**un** appel. Une seule réponse inexploitable de l'un des cinq suffit donc : format réel non
    éprouvé, délai de 1 750 s dépassé, réponse coupée.
  - Trois échecs sur huit chez le metteur suffisent aussi (37,5 %). La règle vaut pour toutes les étapes, fusions comprises.
  - Le LISEZMOI v2 dit qu'un arrêt par délai « ne rend aucune fiche ». C'est vrai de **tout** arrêt et de tout nœud survenu après
    la proposition.
  - La liste du § 5 ne nomme pas ce nœud.
- **Correction (texte)** :
  - Ajouter au § 5 : « nœud C13 (A14 : plus de 25 % d'appels inexploitables pour un rôle ; pour un proposeur, un seul échec
    suffit) ».
  - Ajouter au § 7 : « tout arrêt ou nœud après la proposition ne rend ni `fiches.json` ni classement, qui ne s'écrivent qu'en
    fin de génération ».
  - session-depot dit en une ligne ce qui reste alors lisible dans le run scellé : journaux, manifestes, coffre. Ma lecture n'a
    pas établi si les réponses brutes des proposeurs y survivent.
  - Dire que la variante à cinq espèces multiplie les points de rupture uniques (cinq appels proposeurs, dont deux interfaces
    au format non éprouvé). Le choix de la variante reste à session-depot et Lazar.

### CLH-02 — majeur — Lazar ne lira que les fiches munies d'un passeport ; l'aiguilleur peut en écarter beaucoup

- **Où** : fiche l. 117-118 (§ 6). Code : `course2_v56.lot_mesure` l. 264-268 ; `noyau_v54.py` l. 246-253 (journal de
  l'aiguillage, « contenu : non copié (R-575) »). Consigne : `pieces/consigne-aiguilleur-heimersheim-v1.md` l. 10-13.
  Garde Kimi : `pole/course2_nuit_v1.py` l. 83-88.
- **Qui disparaît** : `fiches.json` ne contient que les fiches classées `niveau_methode`. Les fiches exclues par la garde
  lexicale, classées `a_corriger` ou `concret`, ou refusées par l'aiguilleur sont comptées, mais leur contenu n'est copié
  nulle part. Le § 6 dit « Lazar lit les fiches » sans dire qu'il s'agit de ce sous-ensemble.
- **Trois pentes vers l'écart** :
  - L'exemple de `a_corriger`, « un axe qui ne correspond pas à son contenu », se déclenchera souvent : les axes se recoupent
    par construction. Le livrable impose à **chaque** fiche une prédiction chiffrée et un coût sur Llama-3.1-8B, donc
    `prediction_chiffree_8b` convient à presque toutes.
  - `concret` couvre « des détails opérationnels qui dépassent la méthode », et la règle dit « en cas de doute, choisis
    concret », alors que le livrable demande « modèle, intervention, dose, lecture ».
  - Plus de 4 fiches `concret` sur 8 chez Kimi (S12 = 0,5) arrêtent la course après l'aiguillage, sans aucune fiche (CLH-01).
- **Correction** :
  - Texte : déclarer au § 6 que la sortie lisible = les fiches à passeport, et faire rapporter les nombres par classe et par
    espèce.
  - Option kit (consigne v2, nom neuf) : écrire que le protocole d'expérience relève de `niveau_methode` (modèle, couches,
    doses, lectures, nombre de tirages). Écrire aussi qu'un axe parmi plusieurs plausibles n'est pas `a_corriger`.
  - La même phrase « détails opérationnels » figurait dans la consigne de la mini-course (`nuit/pieces/consigne-aiguilleur-mini-course-v1.md`
    l. 11), éprouvée au second tour. Le risque est donc hérité et non prouvé ; c'est pourquoi il est majeur et non bloquant.

### CLH-03 — majeur — garde lexicale : « gpt » en mode préfixe exclut à tort des fiches de niveau méthode

- **Où** : `configuration-course-heimersheim-v1-cinq-especes.json` l. 217 (`avec-kimi` l. 211, `sans-kimi` l. 205) ; fiche
  l. 73-79.
- **Ce qui est exclu** : vérifié avec la fonction du noyau, « comme sur GPT-2 small (Heimersheim et Mendel 2024) » donne
  ['gpt'] et « GPT-J » donne ['gpt']. Sont donc exclues toute fiche qui nomme un modèle GPT comme banc ou comme juge, et
  notamment GPT-2. Je me souviens de GPT-2 comme d'un modèle courant des travaux sur les plateaux, sans vérification (R7) ; la
  pièce ne le dit pas. Ce serait l'axe 4, la ligne de recherche du mentor. Une fiche exclue disparaît de la sortie (CLH-02).
- **Mots gardés exprès** : « exploratoire » protège la marque des fusions (`course2_v56.py` l. 224) et « fusion » protège leur
  origine, donc ils sont justifiés. Mais ils attrapent aussi « étude exploratoire » et « fusionner les deux directions »,
  vérifié.
- **Correction recommandée** (nouvelles configurations, nom neuf) :
  - Remplacer « gpt » par « gpt 6 » et « gpt6 ». La normalisation change « gpt-6-astra » en « gpt 6 astra » ; « astra »,
    « openai » et « chatgpt » restent.
  - Revérifier par `fiches_v54.trouver`, puis rejouer la table et la répétition.
  - Sinon, déclarer le risque au § 3.4 et faire rapporter les exclusions A4 par étiquette.
  - Pour « exploratoire » et « fusion » : déclaration seulement.

### CLH-04 — majeur — le relèvement du plafond technique de 60 à 244 USD revient au mot de Lazar, pas à conv-audit

- **Où** : fiche l. 89-92 (§ 3.8) et l. 190 (§ 8.7). Spécification, § 2 : « plafond technique 60 USD […] à relever sur son mot si
  le devis le dépasse ». « Son » renvoie à Lazar, sujet de la phrase.
- **Le problème** : la fiche range ce relèvement parmi les écarts « à trancher par conv-audit ». Or le « pas de plafond » de
  Lazar (07:45, heure de Paris) précède le devis, dont le pire cas (203,15) fait plus de quatre fois le « ≈ 45 » de la
  spécification. Le relèvement est un nœud de décision (dépense).
- **Correction (texte)** :
  - § 3.8 et § 8.7 : « relevé à 244 USD sur le mot de Lazar (spécification § 2), cité dans la ligne de GO (texte et heure) ».
  - Ce mot est soit le « pas de plafond » de 07:45, que Lazar confirme comme couvrant 244 USD au vu du devis, soit un mot neuf
    sur le devis.

### CLH-05 — majeur — source du substitut Gu-Krenn : un lien absent de la pièce

- **Où** : `pieces/source-gu-krenn-heimersheim-v1.json` l. 38-47 (œuvre `replication-glm-5`, concept « incohérence hors
  variété »).
- **Le lien inventé** : la pièce, en A3, dit seulement que le modèle « devient souvent incohérent au-delà de 0,025 ».
  « Hors variété » est l'explication donnée en B9, chez Wurgaft. La pièce ne relie jamais l'incohérence de GLM-5 à la variété,
  et la question (demande 4) range le pilotage sur variété parmi les objets « que la littérature citée ne relie pas ».
- **Effet** : quatre paires ne peuvent plus être proposées comme jamais reliées, car un lien inventé les compte comme
  « reliées ». Ce sont « incohérence hors variété » × « direction de conscience d'évaluation », × « paires contrastives »,
  × « témoin contrastif sans rapport » et × « conscience verbalisée ». Or c'est exactement la famille de liens que la question
  demande.
- **Correction recommandée** : retirer ce concept de `replication-glm-5`. Cela demande une source v2 (nom neuf), de nouvelles
  empreintes dans les trois configurations, la table et la répétition. Sinon, le déclarer nommément au § 3.3 et au § 8.4 comme
  un codage hors pièce.

### CLH-06 — mineur — juge : K1 et K3 imposent à toutes les fiches la forme de la demande 5

- **Où** : `pieces/consigne-juge-heimersheim-v1.md` l. 15 et l. 17 ; fiche l. 52-55. Même remarque pour le champ `cout` du
  livrable (`consigne-proposeur…` l. 94-95).
- **Constat** : la question demande à chaque fiche « l'hypothèse, l'effet prédit, et la mesure qui la tuerait ». Le chiffrage
  et l'épreuve sur un 8B ne sont demandés qu'en 5. Le classement favorisera donc les idées testables sur un 8B, au détriment
  des demandes 1 et 3 (par exemple « un modèle réellement conscient d'être évalué », section C). C'est un biais de forme, pas un
  biais vers une réponse. K4 et K5 sont fidèles à la question.
- **Correction** : déclarer au § 3.2 ou au § 6 de ne pas lire le classement d'un axe à l'autre.

### CLH-07 — mineur — citation de Lazar inexacte

- **Où** : fiche l. 27, « GO direct « sans plafond » […] (mot rapporté par la spécification) ».
- **Constat** : la spécification rapporte « pas de plafond » (07:45, heure de Paris).
- **Correction** : citer le mot exact.

### CLH-08 — mineur — garde lexicale : écart incomplet et raison inexacte

- **Écart incomplet** : le § 8.5 (l. 188) ne déclare que le retrait de « témoin ». Les ajouts (« fable », « astra », « openai »,
  « gpt », « chatgpt ») sont aussi un écart à « garde lexicale inchangée ».
- **Raison inexacte** : la raison donnée l. 75-76 (la pièce emploie « témoin ») n'est pas la raison opérante. La pièce ne passe
  pas par la garde, puisqu'elle n'est servie qu'aux proposeurs. En revanche, la liste fermée servie à chaque lecteur contient
  « témoin » trois fois, et une étiquette dans une pièce servie est un arrêt (`fiches_v54`, CL18-12).
- **Précision** : l. 78-79, « vocabulaire du substitut » est vrai des concepts. Le `_lisez_moi` de la source contient
  « Gu et Krenn », que la garde attrape, mais il n'est jamais servi : le metteur ne reçoit que les deux fiches,
  `bisociateur_v53.entree_fusion`.
- **Correction** : compléter le § 8.5, corriger la raison, préciser la l. 78.

### CLH-09 — mineur — un nom d'auteur peut passer pour les modèles Claude et Argon

- **Constat** : « claude », « opus », « sonnet », « anthropic », « google » et « deepmind » ne sont pas dans la liste.
  Vérifié : « écrit par Claude Opus 5.5 » et « modèle de Google DeepMind » passent. Une fiche d'Opus 5.5, de Fable 5.1 signée
  « Claude » ou d'Argon qui nommerait son auteur atteindrait donc les juges, dont Opus 5.5. Seule la dernière phrase de la
  consigne du proposeur l'interdit.
- **Ce qui est juste** : les noms d'auteurs humains des sources (Hua, Heimersheim, Nanda…) passent, et ils doivent passer.
- **Correction** : la déclarer au § 3.4. Option kit : ajouter « opus 5 », « claude opus 5 », « claude fable », « google »,
  « deepmind », absents des textes servis, à revérifier par `fiches_v54.trouver`.

### CLH-10 — mineur — source du substitut : autres choix de codage à déclarer

- **« fenêtre de dose »** : attribuée à Heimersheim et Mendel seuls (l. 80), alors que B7 attribue le paragraphe des plateaux et
  de la dose aux trois sources ensemble, 2606.24964 fig. 1 comprise. « fenêtre de dose » × « exposant p » devient ainsi une
  paire jamais reliée.
- **« réinférence de la croyance à chaque jeton »** : attribuée à Hua seul (l. 20). La pièce, en B10, la relie de sa propre voix
  à la correction d'erreur des plateaux.
- **Règle de codage** : la règle « une œuvre par source » ne code aucun lien posé par la pièce elle-même (B10, C).
- **Correction** : le déclarer au § 3.3.

### CLH-11 — mineur — le lecteur cherche un « témoin » que les fiches n'ont pas

- **Où** : `pieces/consigne-lecteur-heimersheim-v1.md` l. 5, « son hypothèse, son épreuve, son témoin, sa prédiction ou son test
  de mort ».
- **Constat** : le champ des fiches s'appelle `controle`. Le lecteur risque de négliger ce champ, celui qui porte les témoins
  exigeants.
- **Correction** : consigne v2 si le kit est refait, sinon déclarer.

### CLH-12 — mineur — deux précisions

- **l. 8** : « Le lanceur v1 exige ce texte scellé » ; le lancement se fait par le lanceur v2, qui a la même exigence. Écrire
  « le lanceur (v1 comme v2) ».
- **l. 34** : la spécification (§ 1) fait entrer Argon « après la fin d'A1-v3 (rapport de la fille) ». Citer ce rapport
  (chemin et empreinte), pas seulement le mot de session-depot de 07:25.

### CLH-13 — mineur — marge mince à l'étape « proposition »

- **Constat** : le plafond dur de l'étape vaut 8,53 USD, pour une somme des pires cas de 8,525 (devis). Dans le pire cas,
  Astra, dernier proposeur, reçoit min(3,5, reste) ≈ 1,645 pour un pire cas de 1,6408 (calcul). Il n'y a pas d'arrêt, mais
  sans marge. La durée réelle du proposeur Kimi (jusqu'à 65 536 jetons sous 1 750 s) n'est pas éprouvée, et un délai dépassé
  chez un proposeur donne le nœud de CLH-01.
- **Correction** : rien à changer, sauf si c'est bon marché ; le dire au § 7, avec CLH-01.
