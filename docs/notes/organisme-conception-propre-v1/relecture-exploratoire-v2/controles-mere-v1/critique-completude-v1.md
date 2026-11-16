# Critique de complétude avant le feu de la relecture exploratoire v2 (v1)

Début : 2026-11-14 23:12:08 UTC. Fin : 2026-11-14 23:15:44 UTC (`date -u`, relevée juste avant l'écriture).
Contrôleur neuf (sous-agent de la session mère). Il n'a pas refait le travail des trois contrôleurs : il juge sa couverture.
Chemins relatifs à `docs/notes/organisme-conception-propre-v1/` ; `RE/` = `relecture-exploratoire-v2/` ; `OUT/` = `RE/lecture-classement-v3-2/`.

## Verdict

**Go avec réserves.** Aucun bloquant : rien de ce qui a été lu ne permet de dépasser 6,50 USD, de divulguer la clé ou de
perdre une réponse payée en silence. Mais **deux majeurs restent ouverts** et ne se lèvent que par un geste de la mère
avant le feu : (C1) le § 6 n'a pas été corrigé, et les corrections des trois contrôleurs ne sont dans aucune pièce scellée ;
(C2) les deux risques qui tuent le dossier unique (route du mandataire, crédit du compte OpenAI) ne sont ni éprouvés ni
tranchés. Le feu peut partir dès que ces deux points sont levés ou acceptés par écrit.

## Ce que j'ai fait, et pas fait

- Lu les trois rapports ; sceaux vérifiés par `sha256sum -c` depuis `controles-mere-v1/` : les trois `OK`. Lu le § 4 à § 7
  de `rapport-v1.md`, le devis v2, `regle-v2-1.md` (§ 4 et statut des relecteurs), les lignes R-2726, R-2759, R-2804, R-2663,
  R-2713, la ligne de GO-2026-11-13-06 et celle de GO-2026-11-14-12, le premier mode d'emploi (`lecture-g1-v3-1/commandes-exactes-v1.md`).
- Rejoué (lecture seule, sans réseau) : K1 (six `OK`), attestation v2 (`OK`), K8 (une seule ligne, le manifeste v3.1),
  `lecture-g1-v3-2` **absent**, à 23:14 UTC. **Point 12 du § 6, que personne n'avait joué** : `bilan` de la v3.1 sous
  `unshare -n`, code 0, `pret_pour_verifier: true`, `clos: 18`, `attendus: 18`, `en_vol: []`, `anomalies: []`, dépense comptée
  2,556635, plafond 14,2, palier flex ; rien d'écrit dans le dépôt (`git status` inchangé).
- Jamais fait : `envoyer`, appel réseau, lecture d'une clé ou d'un texte de fiche ou d'envoi. Seul fichier écrit dans le dépôt :
  ce rapport. Deux fichiers temporaires hors du dépôt, effacés par chemin exact.

## Constats

### Majeur

**C1. Les corrections des contrôleurs ne sont dans aucune pièce ; le § 6 reste faux ou muet sur six points.** Il n'existe
aucune pièce « commandes exactes v2 » (la première lecture en avait une, `lecture-g1-v3-1/commandes-exactes-v1.md`, écrite avant
tout lancement, avec son numéro au registre). Il faut une pièce neuve scellée (R12 : `rapport-v1.md` ne se réécrit pas), versée
avant le feu, qui porte au moins :
1. **Point 7 (M1 de la revue adverse)** : mode de lancement et durée. Les 17 appels ont pris 578 s à la première lecture, la pile
   est 11,9 % plus lourde ; une commande de premier plan est tuée à 600 s au plus, et un processus tué entre « envoi » et « clos »
   laisse un appel en vol, plus aucun envoi possible, dossier unique perdu. Arrière-plan avec attente du code de sortie, ou
   tranches `--envois-max 6` avec `bilan` entre chaque ; délai d'au moins 300 s au point 6. Aucun contrôleur ne le contredit.
2. **Point 3** : « 247 passés, ou 246 passés et 1 sauté sans le clone de l'orchestrateur » (concordance des deux contrôleurs sur
   le fait ; ils divergent seulement sur la gravité, voir C5).
3. **Point 4** : la commande écrite est bonne pour le feu (le dossier fixe est le seul accepté), mais elle ne peut pas se jouer à
   blanc ; le blanc a été fait par `--racine` sur une racine temporaire. À écrire pour que l'opérateur ne tente pas un blanc hors dépôt
   (refus de la garde C6, sans dommage) et pour que la lecture du résultat du blanc soit déclarée.
4. **K6 après le point 10** (rejouer sur `lecture-g1-v3-2` entier), origine de la clé dans l'environnement de l'opérateur (jamais
   `export …=` en ligne), et la phrase à dire à Lazar : le mandataire de la session re-termine TLS et voit l'en-tête d'autorisation
   (le commentaire de `transport_reel` est faux ici).
5. **Un seul processus `envoyer` à la fois** (aucun verrou de fichier) ; **seconde préparation** : « déplacer hors de `docs/` et
   `runs/` », non « supprimer » (R12), sous nœud de Lazar, avec la somme des `depense_comptee_usd` en `--depense-anterieure-usd`.
6. **Arbre git** : la condition 2 de la contre-lecture (« arbre git propre ») n'est pas dans le § 6 ; elle n'est pas tenue (le rapport
   des essais est non suivi, le mien le sera). Ou l'ajouter au point 2 après versement des quatre rapports, ou la retirer des conditions
   par une ligne. Dire aussi que « 0 mutant vivant » n'est pas tenu (2 survivants du générateur, 2 inapplicables de l'outil).

**C2. Deux causes de perte du dossier unique, jamais éprouvées et jamais tranchées.** R-2804 a décidé « si le premier appel
s'arrête : nœud » ; il n'a pas décidé s'il faut les écarter d'abord, et les contrôleurs n'ont pas pu les mesurer (interdit de réseau).
- **Route** (mandataire de la session, TLS, palier Flex, délai de 1800 s) : le blanc et la revue adverse recommandent chacun le même
  geste gratuit, un `GET` de la liste des modèles sans clé (401 attendu), déjà fait avant le premier appel de la première lecture
  (10:36:20, `journal-et-releve-v1.md`) et absent du § 6. Il faut que la mère le joue (ou le fasse jouer) dans la session qui
  portera les appels, ou écrive qu'elle l'écarte parce que la première lecture a passé par la même route (R-2713) ; je n'ai pas
  vérifié que c'était la même session ni le même type de mandataire.
- **Crédit du compte OpenAI** : aucun des trois contrôleurs n'en parle. R-2663 : compte rechargé, « montant non dit » ; il a payé
  2,556635 USD à la première lecture, et d'autres sessions tirent sur le même compte (sondes d'Astra du pilote, R-2712, R-2731, lignes
  -10 et -11). Ce même chemin a déjà échoué par épuisement de crédit (2026-11-01 : `credit_balance_exhausted` ; 2026-11-14 matin :
  deux 429 `insufficient_quota`, R-2621). Un 429 de ce genre au premier appel, ou au dixième, arrête l'outil (code 3), perd le droit
  d'envoyer et laisse une lecture incomplète (E2 v2). Aucun appel gratuit ne prouve le crédit : il faut que Lazar le confirme (≥ 6,50
  plus la marge du pilote) ou que la mère déclare qu'elle accepte le risque, au registre, avant le feu.

### Mineur

**C3. Contradiction entre contrôleurs sur la normalisation typographique : tranchée.** Le contrôleur des essais écrit que l'essai sauté
« intervient dans la vérification des citations, pas dans la dépense ni l'arrêt » ; la revue adverse écrit qu'il « fixe la vue servie ».
Lu dans l'outil : `normaliser_objet` est appliquée à la vue envoyée au lecteur (`outil_…v3_2_1.py`, retour de la fonction de vue,
ligne 340) : la revue adverse a raison, c'est le texte reçu par le lecteur. Le risque reste faible : le même essai a passé sur la
machine du préparateur (`resultat-essais-lecture-classement-v3-2-1.txt` : « 229 passed », sans saut, 13:08 UTC), la fonction est
dans les 50 objets dont l'arbre syntaxique est comparé à la v3.1 qui a servi la première lecture, et l'essai ne compare que trois
chaînes à un clone absent d'ici. À écrire : le résultat sain ici est « 246 passés, 1 sauté » ; l'égalité avec l'orchestrateur n'a
été jouée par aucun tiers.

**C4. La phrase de la règle sur les sous-agents et la décision de la mère ne se rejoignent pas tout à fait.** La revue adverse écrit
que l'ambiguïté du § 4 n'est « pas levée dans la règle » : c'est inexact, la règle v2.1 porte déjà un « statut des relecteurs »
(`regle-v2-1.md`, après le tour 2) qui renvoie à la mère l'inscription au registre, et R-2804 a répondu (hors dépenses). Reste ceci,
vu par personne : R-2759 et R-2804 disent que les relecteurs lancés par la ligne de commande du client « ne sont pas repris », or les
valeurs attendues des témoins du lecteur ont été éprouvées par des relecteurs de cette voie (tours 1 et 2 de l'épreuve) ; et la phrase
« aucun appel payant (sous-agents de la session) » subsiste dans la règle. Une ligne de la mère suffit : épreuve passée conservée comme
information déclarée (voie non prévue, même compte) ou à refaire ; en l'état la lecture de « pas repris » est ambiguë.

**C5. Gravité de l'écart de compte (essais) : mineur retenu.** Le contrôleur des essais le classe mineur, la revue adverse majeur.
Les faits concordent. Retenu : mineur, car le test sauté ne touche ni la dépense ni l'arrêt, mais correction de texte exigée (C1,
point 2) pour que l'opérateur ne prenne pas l'habitude de passer outre un écart de compte.

**C6. Ce qui reste « trop propre » (R4), et la décision à écrire.** Le contrôleur des essais montre que le « tout tué » du banc v3.2.1
tient à un essai de texte (arbre syntaxique contre la v3.1) pour les gardes de dépense, d'arrêt, de modèle, de palier et de dossier
existant ; sans lui les essais de comportement tuent tout le reste, sauf six survivants dont quatre trous réels (codes de sortie de
`envoyer`, `--envois-max 0`, compagnon `.sha256` seul, « lisibilité sans complétude »). Rien ne touche l'argent, mais le dernier
(une lecture incomplète classée lisible) agit sur la lecture du verdict, et il est plus probable si C2 se réalise à mi-course. Le
code du classement est juste selon la revue adverse (lecture ligne à ligne) : le trou est dans l'essai. À décider par la mère :
l'accepter et le déclarer, ou le corriger dans les seuls essais (nouveau nom, R12) avant le feu ; à ne pas laisser sans mot.

**C7. Chaîne d'après-envoi jamais jouée à la taille réelle.** Les essais font un bout en bout en ligne de commande sur des pièces
factices (28 fiches, 12 appels) ; le blanc a joué `preparer` réel (43 fiches, 18 appels) mais ni `envoyer`, ni `verifier`, ni
le classement. Aucun contrôleur n'a rejoué la préparation réelle contre un serveur local avec 18 réponses factices. Si le classement
échoue après la dépense, les réponses sont gardées et l'argent n'est pas perdu, mais une version neuve du classement serait alors à
écrire sous R12. Répétition générale facultative, gratuite (serveur local, `URL_AMONT` des essais), recommandée.

**C8. Préalables et fin de marche non écrits au § 6.**
- Les K3 et K7 de la première lecture (mot de Lazar consigné avant `preparer` ; attestation égale à son compagnon) n'ont pas de
  ligne au § 6 ; ils sont tenus de fait (R-2804, 22:32 UTC ; compagnon de l'attestation `OK` à 23:14) : les nommer dans la pièce de C1.
- Ligne de GO : GO-2026-11-13-06 existe, 21 USD, échéance 30 novembre, cumul 9,347722 : reste 11,652278 > 6,50 ; aucune autre
  dépense inscrite à cette ligne après la première lecture. La condition de GO-2026-11-14-12 (« ligne de GO valide sur `main` ») ne
  se vérifie pas ici sans réseau : la mère doit s'assurer que R-2804 et la ligne sont sur le `main` distant avant le feu.
- Prix Flex 5 / 0,5 / 25 : repris de `prix-astra-v2.md`, non revérifiés chez le fournisseur (R7 du programme) ; le point 13 devrait
  ajouter « rapprocher le relevé de la console du fournisseur » (la console fait foi).
- Quota du compte de session : R-2759 avait différé la course parce que le quota approchait 97 % ; R-2804 la reprend et les trois
  contrôleurs plus celui-ci l'ont consommé. Nul ne dit l'état du quota. Avec l'arrière-plan de C1(1) une coupure de session ne tue pas
  l'appel en cours, mais la mère doit lire son quota avant le point 6 et ne pas commencer si une coupure est probable.
- Réserves du § 7 (r1 à r13), couverture : r1 levée pour les essais, non pour l'indépendance des bancs (C6) ; r5 : lots confirmés par le
  blanc (7 de 5 et 2 de 4), étiquettes non comparées à la première lecture par un tiers (conservées par construction, graines gardées) ;
  r6 : voir C2 ; r12, r13 : levées (R-2804, essais rejoués) ; r2, r3, r4, r7, r8, r9 : limites déclarées, non contrôlables avant le feu,
  elles s'écrivent dans le rapport final ; r10, r11 : sans effet sur le feu.

### Information

- Aucun contrôleur ne contredit les autres sur l'argent, la clé ou les arrêts : tous trois concluent que 6,50 USD ne se dépasse pas par
  l'outil seul (écarts bornés : palier servi autre, un appel ; reprise invisible du mandataire, non éprouvée ; seuil du premier appel
  ≤ 0,33 qui n'assure pas le dix-huitième si la moyenne passe 0,32).
- Les trois rapports et le mien déclarent le même état du dépôt : dossier absent avant et après, rien envoyé.

## Ordre proposé avant le feu

1. Mère : lire le quota ; décider C2 (GET sans clé joué ou écarté par écrit ; crédit confirmé par Lazar ou risque accepté par écrit).
2. Mère : écrire et sceller la pièce « commandes exactes v2 » (C1 en entier, C3, C4, C8), l'inscrire au registre, verser les quatre rapports,
   vérifier que `main` distant porte R-2804 et la ligne de GO.
3. Facultatif, gratuit : répétition générale locale à pleine taille (C7) ; correction des essais (C6) sous un nom neuf.
4. Puis les points 1 à 13, le point 7 en arrière-plan ou par tranches.
