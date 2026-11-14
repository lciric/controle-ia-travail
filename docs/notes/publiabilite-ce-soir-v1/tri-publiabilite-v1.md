# Tri de publiabilité des pièces jugées — ce soir, 13 novembre 2026 — v1

- **Demande** : Lazar, `registres/decisions.md`, R-2572 et R-2575 (lancée à 19:34 UTC).
- **Rédacteur** : sous-agent analyste neuf (Claude Opus 5.5), qui n'a écrit aucune des pièces triées ; écrit entre 19:35 et
  19:55 UTC (`date -u`). Lecteur **non neutre** pour le billet, qu'il a écrit lui-même.
- **Rien n'est publié, poussé ni envoyé.** Aucune dépense ; aucune écriture git ; clone public lu en lecture seule (tête
  `origin/main` = `be6b5af96c9e19812569d8dab55d6ce3978a3823`, 13 novembre 2026, 10:35 UTC).
- **Lecture interdite respectée** : aucun fichier de 7a, 7b, T0.7, P3-bis, du bras d'attaque, de la famille tenue à l'écart ;
  aucune recherche récursive ; aucune requête réseau contenant nos énoncés, le nom du directeur ou celui du projet (les seules
  requêtes sont les six adresses fixes des règles extérieures, section 4).
- **Lecteur neuf adverse du billet : non fait** (section 6) — ce sous-agent n'a pas d'outil pour lancer un sous-agent ; à
  lancer par la session mère avant de montrer le texte à Lazar.

## 1. Pièces lues, empreintes vérifiées contre leur compagnon (toutes égales)

| clé | pièce | sha256 |
|---|---|---|
| T03 | `docs/verdicts/verdict-T0.3-simulation-lemme-theoreme-v1.md` | `bc53b746f0c9918beff8a2267d5652a730985adee76a807cc670c1a1811e61de` |
| P3 | `docs/verdicts/verdict-P3-premier-test-i-a-v2.md` | `05e896daed17cdb089cd10641878a5014b505eab0aa3d45d0dd7a60d87435751` |
| FU | `docs/verdicts/verdict-audit-fuite-r1-v4-v1.md` | `320463e6c03189178a2436742fe78e1edeae59d6a738a52de581924d837929d7` |
| T04 | `docs/verdicts/verdict-T0.4-critere-1-G0-v3.md` | `63444faa4ce253fcfc19981224ab95bc243e9b2c74bf83daf181d0059d5b4a13` |
| T05a | `docs/verdicts/verdict-T0.5-pilote-v1.md` | `b9a072302d6514c0df80c950317012498c7af62b6440e37045a43de46a3faabc` |
| T05b | `docs/verdicts/verdict-T0.5-pilote-notations-v1.md` | `d861605c178e1fb0c43c05e62782200ba936ddd00982230b3013e5cc3d60a8cc` |
| T05c | `docs/verdicts/verdict-T0.5-revalidation-v2.md` | `f98b56841d2c9f93c84381d16dcdf9f438c5380dfc36b14654c0dba152a8a018` |
| T05d | `docs/verdicts/audit-R4-T0.5-pilote-v1.md` ; `audit-R4-T0.5-pilote-notations-v1.md` | `f557402b…0c2d` ; `d69a8700…2c20` (complètes au compagnon) |
| A1 | `docs/notes/ideation-organisme-v1/a1-v4-reprise-v9/verdict-a1-v4-v1/verdict-officiel-a1-v4-v1.md` | `e6e2f17076fab16f2684553765517937d528c657367075c126945c3ae3741cda` |
| N67 à N70 | `docs/decisions/decision-N-067-v1.md` … `decision-N-070-v1.md` | `966dd9dc…`, `ba6b2db3…`, `6e0d9d40…`, `7c4ce221…` (complètes au compagnon) |
| CLE | `docs/etat-de-l-art/etat-de-l-art-verifie-niveau3-v1-contre-lecture-v1.md` | `f1580ddcedd495b5ce46391620f0d49ccf309d81f6ff1960cc5f4835776e5430` |
| VE | `docs/notes/contre-lecture-veille-2611.04556-v1.md` ; lecture contre-lue `lecture-veille-2611.04556-influence-inter-agents-v1.md` | `af2fcb07…aadf` ; `211a6448…5257` |
| PUB | page publique de l'organisme, `README.md` et `resultats/controle-r1-blanche-noire/README.md` à `be6b5af9` | `e81b96383bc3a387e45f3f7e89f1590f175a968fb24e77a3a66f471a45e051e3` ; `98378e6e495a16dfbc06ada8e4770764c75e7f463950986a66b3c5b8a24732ef` (contenu de `git show`) |

## 2. Table des pièces candidates × critères

Critères : (1) verdict scellé par un lecteur neuf ; (2) contre-lu (second lecteur du verdict, ou sceptiques) ; (3) hors
embargo ; (4) ne révèle pas la feuille de route ; (5) chiffres vérifiables par chemin et empreinte ; (6) déjà public.

| pièce | (1) | (2) | (3) | (4) | (5) | (6) | classe |
|---|---|---|---|---|---|---|---|
| FU, audit de fuite (R1 v4) | oui (Sonnet, autre lignée) | préenregistrement contre-lu (R-1651) ; verdict : un lecteur, relance à l'octet | oui (données de P3, pas de P3-bis) | **oui pour l'issue ; non pour la phrase « Next: … » de la page publique** | oui (`diag/20261107-094957-…`, V l. 22-30) | **oui**, page publique, mais **plus fort que le verdict** | 1 (correction) et 2 (billet) |
| T03, simulation du lemme et du théorème | oui (10 nov.) | préenregistrement : 3 contre-lectures ; verdict : un lecteur, recalcul indépendant | oui | oui si L et T ne sont pas dits libres (CLE § 6) | oui (`diag/20261004-080257-t03/`) | oui, mais la page dit « no fresh-reader verdict » (périmé) | 1 (mise à jour) et 2 (note) |
| A1, attaque de Goodhart A1-v4 (organisme) | oui (Opus, autre lignée que l'auditeur) | oui (audit Fable + verdict Opus) | **limite** : aucune recette d'attaque d'un juge ne doit sortir ; l'issue seule, oui | oui | oui (lecture `58008ea0…`) | oui (page d'état publique) | 1 (travaux voisins de la page) et 2 (note, après lecture de SSRN 6569258) |
| N67, resserrement de l'organisme | décision, pas verdict ; contre-lue (R-2565) | oui | oui | oui pour O2, O11, O12 ; **O4 non déclarable** | oui | non | 1 (correction des travaux voisins de la page publique) |
| P3 v2, premier test boîte blanche | oui | oui (deux sceptiques, correcteur) | **non en pratique** : sa lecture appelle le témoin positif (P3-bis, sous embargo) | non : toute discussion appelle la suite | oui | oui (page publique) | 3 |
| T04, harnais sur modèle réel (critère 1 de G0) | oui | non | oui | **non** (porte G0, devis) | oui | non | 3 |
| T05 a-d, pilote 8B, notations, revalidation, audits | oui | oui (sceptiques) | oui | **non** (juges de T0.6 et T0.8, nœuds ouverts, plan B) | oui | non | 3 |
| N68, N69, N70 | décisions | contre-lues | oui | **non** : HC2, statistique du papier B, H9 sont la feuille de route | — | non | 3 (hors engagement sous embargo) |
| VE, veille 2611.04556 | lecture + contre-lecture | oui | oui | **non** (revendications confrontées) | — | non | 3 |

## 3. Classement en trois

### Classe 1 — publiable ce soir sur un lieu que nous tenons (page publique corrigée ; engagement horodaté sous embargo)

Condition commune : GO de Lazar sur le différentiel (N-067, § 10 ; R-2575, tâche 2) ; cette classe **retire** ou **resserre**
du texte déjà public, elle n'ajoute aucune revendication.

**1-a. Fuite de la sonde W : phrase de la page publique resserrée, et phrase de feuille de route retirée.**
- Constat : `README.md` l. 128 (« … rather than the sabotage itself … ») et `resultats/controle-r1-blanche-noire/README.md`
  l. 9 (« reads the instruction, not the sabotage ») sont **plus forts que le verdict** (réserve 2, FU l. 7 ; recommandation
  du lecteur, FU l. 65 : citer avec la réserve 2). Et `README.md` l. 128 (dernière phrase, « the next test uses organisms whose
  sabotage is trained into the weights … ») et la page R1, l. 11 (« Next: organisms whose sabotage is trained into the
  weights (low-rank adapters …) … decisive run … probes tested across the two origins of sabotage … ») **publient un plan non
  exécuté** : contraire à l'embargo « aucun plan non encore exécuté ». À retirer ce soir (l'historique git public les garde).
- **Phrase exacte publiable** : « A preregistered leak audit returned the frozen outcome "leak (reading the instruction)": the
  trained probe separates the saboteur's actions that do not inflate the cost (area 0.9967 [0.9930, 0.9991], 46 actions from
  12 of 60 tasks) as well as those that do (0.9977 [0.9958, 0.9993]). "Not inflated" is not "no sabotage": the probe may also
  read another trace of sabotage, and the arm that would separate the two was not run. »
- Pièce : FU, `320463e6c03189178a2436742fe78e1edeae59d6a738a52de581924d837929d7`, l. 3, 6-7, 42-43.
- Réserve : un seul bras (46 actions) ; résultat très propre (FU l. 8) ; le chiffre « +0.932 » de la même ligne publique vient
  du verdict des trois analyses (`dece9980…`), **non relu ici**.
- Objection la plus dure : « Votre sonde boîte blanche lisait la consigne ; pourquoi croire le reste de vos chiffres boîte
  blanche, dont le +0,932 affiché sur la même ligne ? » — réponse possible seulement par la lecture gelée : P-E1 ne se cite
  plus comme détection (préenregistrement de l'audit, l. 247) ; la ligne publique doit le dire.

**1-b. T0.3 : ligne de la page publique mise à jour avec le verdict du lecteur neuf.**
- Constat : `README.md` l. 130 dit « frozen reading by the code, no fresh-reader verdict » ; le verdict existe (10 nov.).
- **Phrase exacte publiable** : « Fresh-reader verdict (10 November 2026): "confirmed with reservations". All 886 cells
  conform; the raw counts were reproduced byte for byte from the recorded seeds by code extracted at the cited commit. Main
  reservation: most predictions are instrument checks, and the informative false-alarm magnitudes had been seen in exploratory
  runs before sealing (0.214, 0.364, 0.164); this validates the instruments in simulation, not the claim on real models. »
- Pièce : T03, `bc53b746…61de`, l. 10-28 (verdict), 217-229 (réserves).
- Réserve : verdict à un seul lecteur ; aucun énoncé L ou T dit libre (CLE § 6) ; « 31 of 31 » est un compte d'un seul run,
  déjà public, pas un taux de calibration (R-2185) — à ne pas agréger avec d'autres runs.
- Objection la plus dure : « 31 sur 31 par construction, magnitudes vues avant le sceau : c'est un essai d'outil, pas un
  essai risqué. » — exacte ; la phrase le dit.

**1-c. Travaux voisins de la page publique resserrés selon N-067.**
- Constat : `README.md` l. 7 revendique encore les quatre composantes de O2 (N-064) et dit la forme de l'attaque « not found
  in the work read so far » sans date ni mentions ; il cite déjà le nul « formed by the known laws » comme revendiqué :
  **contraire à la clause d'usage public de N-067 (§ 4, point 2) tant que SSRN 6569258 n'est pas lu.**
- **Phrase exacte publiable** (remplace « What is claimed is narrower … read so far. ») : « Computing the statistic outside the
  agents, sealing the plan by hash before the data, and controlling multiplicity (including Benjamini–Hochberg for e-values)
  are published (Qu, Chen, Wang, arXiv:2609.27051; CONFIRM, arXiv:2611.01449; Sargsyan, arXiv:2511.06701; CADS,
  arXiv:2610.24597; N×N E-valuation, arXiv:2608.06621; "Hard to Fool", arXiv:2611.06607) and are not claimed here; serving a
  statistical judge's verdicts to a language-model proposer on worlds where every promotion is false is published by CONFIRM
  (pp. 9, 22). This repository measures one narrower form: a proposer instructed to make the judge promote a false card, that
  reads the judge's exact description, with an arm that receives the verdicts and an arm that does not. »
- Pièce : N67, `966dd9dc…`, § 3 (table), § 4 points 1-3, § 6.
- Réserve : aucune priorité n'est affirmée (ni O4, ni O12) ; les quatre citations de N-064 restent ; les autres citations
  obligatoires de N-067, § 6 (PACE, REUSE, Masked Erosion, Hegazy et al., PROCTOR) sont à ajouter là où leur point est abordé.
- Objection la plus dure : « Alors qu'est-ce qui est à vous ? » — rien n'est revendiqué publiquement ce soir ; c'est voulu.

**1-d. A1-v4 sur la page publique** : la ligne publique (`README.md` l. 9 et l. 131) est conforme au verdict A1 (issues W2
« resists (at this size) », W2g « frontier crossed, robust », 10 sur 17) ; **à compléter seulement** par la phrase de N-067,
§ 7 : « The same sign is already published: zero false admissions under a frozen referee (Qu, Chen, Wang, p. 15); none of
10,716 candidates admitted (CONFIRM, p. 9). » Pièces : A1 `e6e2f170…`, l. 3-4, 46 ; N67 § 7.

**1-e. Engagement horodaté sous embargo** : lieu (OSF selon R-2555) dont l'état du compte n'est pas connu ; son contenu est
piloté par la tâche (3) de R-2575 ; **O4 et l'énoncé retenu de O2 n'y entrent pas** avant lecture de SSRN 6569258 (N-067,
§ 10). Aucune phrase proposée ici. Règles d'embargo de la plateforme **non relevées ce soir** (question 5).

### Classe 2 — publiable après une lecture externe (billet de forum, note)

**2-a (premier, le plus utile à un chercheur du contrôle) : la sonde entraînée sur un saboteur instruit lit sa consigne.**
- **Phrase exacte publiable** : « A linear probe trained to separate a prompted saboteur from an honest agent
  (Llama-3.1-8B-Instruct) also separates the saboteur's actions that do not inflate the cost, and have no inflated action
  earlier in the episode, from honest actions (area 0.9967 [0.9930, 0.9991], 46 vs 600 actions); a preregistered symmetric
  audit therefore returned "leak (reading the instruction)". »
- Pièce : FU `320463e6…d7` l. 3, 42 ; préenregistrement de l'audit `prereg/audit-fuite-r1-v4-v1.md` `910a53dc…7d84`
  l. 43-45, 76-79.
- Réserve : un bras, 46 actions, 12 tâches ; « non gonflé » ≠ « aucun sabotage » ; bras contrefactuel non fait ; témoin
  « mention » à 0,789 sans décision ; texte de l'audit écrit après lecture d'autres grandeurs (déclaré).
- Objection la plus dure : « Rien de neuf : Mohsin et Rahman (2611.10620) l'ont montré pour la collusion, Kale et Vishwanath
  (2610.18408) pour l'injection ; et votre bras décisif tient en 46 actions d'un modèle 8B, sans le contrôle contrefactuel qui
  trancherait. » — le billet le dit en tête : réplication modeste, avec règle préenregistrée et symétrique.
- Texte et registre : `billet-v1-brouillon1.md`, `billet-v1-registre-affirmations.md` (ce dossier).
- Lecture externe à demander : un chercheur des sondes (avant tout dépôt), puis la file de modération du forum.

**2-b. T0.3 : fausses alarmes du seuil de Ville sous effets d'épisode (note statistique).**
- **Phrase exacte publiable** : « In a preregistered simulation with no attack, Ville's threshold on a one-sided e-process at
  α = 0.05 gave false-alarm rates of 0.2105 (n₀ = 200) and 0.35145 (n₀ = 1,000) under the strongest episode effect tested
  (τ = 0.2), and 0.1656 under correlation c = 0.4 between agents, against 0.017 to 0.019 when well specified. »
- Pièce : T03 `bc53b746…` l. 247-249 ; `diag/20261004-080257-t03/bloc-P8.json` (compagnon conforme, T03 l. 42).
- Réserve : monde synthétique gaussien ; magnitudes vues avant le sceau (0,214 ; 0,364 ; 0,164), réglages choisis ensuite
  (T03 l. 227-229) ; ne rien dire de L ni de T comme libres (CLE § 6) ; la phrase sur 2606.10456 (T03 l. 253) **ne sort pas**
  (non vérifiée sur PDF, R7).
- Objection la plus dure : « C'est le cours : Ville suppose un nul bien spécifié ; un effet aléatoire d'épisode le casse.
  Et vous avez choisi les cases les plus fortes après exploration. »

**2-c. A1-v4 : un proposeur modèle de langue contre un juge statistique (note).**
- **Phrase exacte publiable** : « On a toy world inside the judge's null, a language-model proposer that reads the judge's
  exact description and receives its verdicts got 1 of 24 units promoted ("resists, at this size"); at the judge's declared
  frontier, where a promotion is not false by construction, 10 of 24 ("frontier crossed, robust": 10 of the 17 promoted laws
  replay above α after Holm). »
- Pièce : A1 `e6e2f170…` l. 3-4, 46, et tables § 2.1-2.2.
- Réserve : deux mondes jouets, un fournisseur, 24 unités ; course « trop propre » sans témoin négatif planté (A1 § 4,
  réserve 1, l. 82) ; aucune consigne, aucune stratégie du proposeur ne sort (embargo « recette d'attaque d'un juge ») ;
  **seulement après** la lecture sur PDF de SSRN 6569258 (N-067, § 4 point 2), car toute note sur ce juge se lira comme une
  revendication de son nul ; citations obligatoires de N-064 et N-067.
- Objection la plus dure : « Le signe "zéro promotion" est déjà publié (Qu, Chen, Wang ; CONFIRM) ; et "frontière franchie"
  à une frontière où la promotion n'est pas fausse par construction ne montre aucune faiblesse. »

### Classe 3 — à ne pas publier

| pièce | raison |
|---|---|
| P3 v2 (nul des sondes génériques) | déjà public sur la page, à laisser tel quel ; tout billet appelle « où est votre témoin positif ? », dont la réponse est sous embargo (P3-bis) ; noms de sondes et couches |
| T0.4 v3 | aucun intérêt extérieur ; rattaché au critère 1 de G0 et au devis (feuille de route) |
| T0.5 (pilote, notations, revalidation, audits R4) | nœuds ouverts ; juges destinés à T0.6 et T0.8 (feuille de route) ; leurs faiblesses renseignent sur nos juges |
| N-068, N-069, N-070 | ce qui est cédé y nomme ce qui reste revendiqué (HC2, statistique du papier B, H9) : feuille de route ; seulement sous embargo |
| N-067 au-delà de 1-c | O4 non déclarable (N-067 § 4 point 2 ; CLE § 6) |
| veille 2611.04556 et sa contre-lecture | confrontation à nos revendications |

## 4. Verrous extérieurs relevés à la source ce soir (archives scellées sous `docs/sources/web-publiabilite-20261113/`)

| verrou | règle (citée) | source archivée |
|---|---|---|
| LessWrong, texte écrit avec un modèle, compte neuf | « For first-time users, we have closer to a zero-LLM policy » ; tout « LLM output » (texte écrit par un modèle, ou écrit par un humain puis substantiellement révisé par un modèle, ou l'inverse) « must go into the new LLM content blocks » ; rejet automatique au-delà d'un seuil de détection, appliqué aussi aux comptes approuvés ; voie admise : écrire dans sa langue puis traduction mot à mot (billet du 14 mars 2026) | `lw-politique-llm-mise-a-jour/` (adresse et empreintes dans `adresse.txt`) |
| LessWrong, politique antérieure | « first-time writers are not permitted to use any AI text output in their submissions » (24 mars 2025, renvoie à la mise à jour ci-dessus) | `lw-politique-llm/` |
| LessWrong, premier billet | « We review every first post and comment before it goes live » ; exigence « particularly high » pour l'IA ; rejet affiché sans nom d'utilisateur (guide de 2023) | `lw-guide-nouvel-utilisateur/` |
| Alignment Forum | membres seuls publient sans revue ; un non-membre soumet, file de revue, décision « within three days », billet publié entre-temps sur LessWrong ; adhésion sur invitation (FAQ d'août 2021) | `af-faq/` |
| arXiv, parrainage | parrainage exigé avant le premier article d'une catégorie ; adresse institutionnelle et article revendiqué, ou parrain personnel « an established arXiv author » ; au moins un parrainage positif par catégorie | `arxiv-endorsement/` |
| arXiv, calendrier | soumis entre vendredi 14:00 et lundi 14:00 (heure de l'Est) : annoncé lundi 20:00 ; vérifications de modération « one to four days, sometimes longer » ; aucun envoi vendredi ni samedi ; jour férié 2026-11-26. **Ce soir** : il est 14 h 40 à New York (heure d'hiver, UTC − 5) : la limite de vendredi est passée ; un dépôt de ce soir paraîtrait au plus tôt lundi 16 novembre à 20:00 heure de l'Est (mardi 17 novembre, 01:00 UTC), s'il est parrainé et passe la modération | `arxiv-availability/` |
| non relevé ce soir | règles d'arXiv sur les articles de synthèse ou de position en informatique et sur l'aide d'un modèle ; règles d'embargo de l'OSF | — (à relever avant tout usage) |

Conséquence : **aucun dépôt sur un forum ne peut se faire ce soir avec ce brouillon**. Sur LessWrong, un compte neuf ne peut
pas publier un texte écrit par un modèle ; il faut que le responsable du projet l'écrive lui-même (le brouillon sert de notes et
de registre), ou l'écrive en français et le fasse traduire mot à mot. L'Alignment Forum passe par LessWrong et une revue.
arXiv : rien avant mardi 17 novembre 01:00 UTC au mieux, et pas sans parrainage.

## 5. Questions pour Lazar (l'état de tes comptes n'est pas au dépôt)

1. LessWrong : as-tu un compte ? Depuis quand, quel karma, et un billet ou commentaire y a-t-il déjà été approuvé (sinon tu
   es « first-time user » au sens de la règle) ? Sous ton nom ou un pseudonyme ?
2. Acceptes-tu d'écrire le billet toi-même (en anglais, ou en français puis traduction mot à mot), le brouillon servant de
   notes ? Sinon, le publier entier dans un bloc « LLM content » (approbation peu probable pour un compte neuf, selon la règle) ?
3. Alignment Forum : es-tu membre ? (Sinon : soumission en revue, billet d'abord sur LessWrong.)
4. arXiv : as-tu un compte ? Une adresse institutionnelle associée ? Un article déjà revendiqué ? Une catégorie visée ? Un
   parrain connu dans cette catégorie ?
5. OSF (engagement sous embargo, R-2555, R-2563) : as-tu un compte ? Quelle durée d'embargo veux-tu ?
6. Page publique : donnes-tu ton GO ce soir aux corrections 1-a à 1-d (retrait de la phrase de feuille de route ; phrase de
   fuite resserrée ; ligne T0.3 ; travaux voisins), sur le différentiel de la tâche (2) ? Le retrait n'efface pas l'historique
   git public : veux-tu le laisser tel quel ?
7. La phrase B22 du billet (ne pas lire la comparaison sonde-juges comme détection) repose sur une proposition du lecteur de
   l'audit (FU l. 63, 65) : l'as-tu adoptée ? Je n'en ai pas trouvé trace au registre.
8. `README.md` l. 202 de la page publique nomme un relecteur extérieur par sa fonction : le gardes-tu ?

## 6. Lecteur neuf adverse et texte exact

- **Non fait par ce sous-agent** : aucun outil de sous-agent dans sa session. À faire par la mère, avant de montrer le texte :
  lecteur neuf, autre que ce rédacteur, avec pour fichiers `billet-v1-brouillon1.md`, `billet-v1-registre-affirmations.md`,
  FU, `prereg/audit-fuite-r1-v4-v1.md`, `prereg/P3-consignes-v1.md`, N-068, N-069 et la lecture de veille ; consigne :
  chercher toute phrase plus forte que sa pièce, tout chiffre faux, tout élément de feuille de route, toute phrase qui
  enfreint la règle de LessWrong.
- Attaque préalable par le rédacteur (non neutre), déjà portée au brouillon : « following the audit's reader » (B22, question
  7) ; inférence de B24 (dite telle) ; la phrase d'ouverture reste « one small instance » d'un écueil publié.
- Le texte exact est `billet-v1-brouillon1.md` (scellé) ; aucun dépôt avant le lecteur neuf et ton accord.
