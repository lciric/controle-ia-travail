# Brief — graine du pôle théorique : la carte des hypothèses des moniteurs — v1

Tu es un sous-agent **neuf** (Opus 5.5) de la lignée conv-audit. Tu n'as écrit ni l'audit des failles, ni le programme,
ni les conceptions du pari. Français, presque sans sigles, verdict d'abord. Aucune clé, aucun jeton ; aucun `git` ; aucune
lecture dans `donnees/`, `diag/`, `runs/`, `pilotes/` ; processeur seul ; relevé `date -u` au début et à la fin, dans un appel
séparé de toute écriture d'heure (le conteneur est en heure de Paris).

## Pourquoi

Lazar (directeur) veut que le programme **prédise** les failles de contrôle avant de les rencontrer par hasard, et propose
des réponses — par la théorie, pas par l'essai. Une instance de Claude ne conçoit aucune recette de contournement (position
tenue le 28 octobre ; R-597 : un lanceur de « bras d'attaque » a été arrêté par un classifieur de sécurité ; on ne reformule
pas). Le chemin compatible est la **carte des hypothèses** : pour chaque statistique de contrôle du programme, les
hypothèses qu'elle fait sur l'agent et sur les données ; pour chaque hypothèse, la **classe d'écart** qui rend la
statistique aveugle, énoncée comme un **lemme d'indistinguabilité** (invariance ou suffisance : « si l'écart appartient à la
classe K et que le moniteur ne lit que la statistique S, alors le taux de détection égale le taux de fausses alertes »),
avec la preuve quand elle est courte ; puis ce qui, dans la littérature déjà auditée, **instancie** cette classe ; puis le
**témoin de mesure** qui vérifierait la prédiction (famille documentée réimplémentée à vérité connue ; simulation au niveau
des scores, comme la mesure unanime ; mode conçu à l'écart par une personne, N-054) ; puis l'**hypothèse de défense** déjà
posée (audit, § 1 ter) ou à poser. Le théorème négatif du programme (§ 3 : dommage porté par la corrélation, pas par la
marginale ; délai Θ(γ) sous furtivité par action) est l'exemple existant de ce qu'on veut : une classe d'écart (la
dépendance), une statistique aveugle (le seuil par action), un lemme, une mesure.

## Règles absolues (celles du brief de l'audit, § 2 et § 3, mot pour mot)

On n'écrit **jamais** une procédure opératoire, une consigne, un exemple de texte, de code ou de réglage qui servirait à
tromper un moniteur ou à échapper à une détection ; aucune recette ; aucun pseudo-code d'agent. Une classe d'écart s'écrit
au **niveau des hypothèses et des lois** (« la loi des scores par action a la même marginale et une autre structure de
dépendance »), jamais au niveau de ce qu'un agent ferait. Si un lemme ne peut s'écrire sans décrire un procédé, on écrit
l'hypothèse et le trou, pas le procédé. R7 : aucun chiffre attribué à un papier sans la page vérifiée dans l'audit (sinon
« non vérifié ») ; R8 : une classe sans instance documentée est une **question**, jamais une « faille inédite » ; jamais
« premier », « nouveau », « inédit ». La pièce reste **confidentielle** (dépôt privé ; jamais dans la copie publique ; jamais
servie à un organisme).

## Pièces à lire (depuis `/home/claude/canal-conv-audit-n04/`)

- Programme : `docs/programme-controle-ia-v2.md` (§ 3 thèse centrale et théorème négatif ; § 5 hypothèses ; § 8
  moniteurs ; § 9 invariants) — s'il n'est pas dans ce dépôt de travail, `git show origin/main:docs/programme-controle-ia-v2.md`
  est **interdit** (aucun git) : lis la copie fournie à l'audit, `brouillons/canal-reprise-releve-v1/envois/audit-failles-controle-v1/`
  n'en contient pas ; la copie est dans `/home/claude/controle-ia-travail/docs/programme-controle-ia-v2.md` (lecture seule).
- Décisions qui fixent la lecture : `/home/claude/controle-ia-travail/docs/decisions/` — N-007 (bases (i) à (iv)), N-029,
  N-053, N-054, et `brouillons/canal-reprise-releve-v1/envois/decision-N-056-noeuds-G1-bras-attaque-mesures-fortes-v1.md`.
- **L'audit des failles** (`brouillons/canal-reprise-releve-v1/envois/audit-failles-controle-v1/`) : `sortie-confrontation/carte-du-controle-v1.md`
  (la chaîne instrumentale et les hypothèses, à prendre comme base), `sortie-confrontation/failles-internes-v1.md`,
  `sortie-confrontation/grille-de-couverture-v1.md`, et la synthèse `sortie-synthese-v3/audit-failles-controle-v3.md`
  (§ 1 bis failles E à I avec leurs mathématiques ; § 1 ter hypothèses testables, 33 ; § 3 grille ; § 4 par menace ; § 5
  candidates). Cite les failles et hypothèses par leurs identifiants (RC-x.y, FI-xx, « faille E », « 1 ter.n »).
- Le pari apparié borné (ce que le pôle peut mesurer) : `brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/pari-de-signe/conception-pari-de-signe-v5.md`
  (§ 1 à 3 suffisent) et la mesure unanime comme exemple de témoin au niveau des scores :
  `brouillons/canal-reprise-releve-v1/envois/mesures-fortes-v1/mesure-unanime-v1/preenregistrement-mesure-unanime-v5.md` (Hypothèse et Métrique).
- Le code des statistiques : `/home/claude/canal-conv-audit-n04/src/controle_ia/bases/sequentiel.py` (max, somme
  terminale, somme séquentielle, Page, processus e, balayage, conforme) ; les sondes et la cascade : ce qu'en disent le
  programme § 8 et la carte du contrôle (ne cherche pas plus loin dans `src/`).

## Ce que tu rends

`/tmp/claude-0/-home-claude/c5a45195-121d-5962-9d0a-4896cc046231/scratchpad/carte-des-hypotheses-v1/carte-des-hypotheses-v1.md`
(compagnon `.sha256`), 250 à 400 lignes, structure :

0. **Verdict** (dix lignes) : combien de statistiques, d'hypothèses, de classes ; combien de classes ont une instance
   documentée, combien sont des questions ; les trois lemmes les plus utiles au programme ; ce que la carte ne couvre pas.
1. **Les statistiques de contrôle** (une table) : seuil par action calibré ; Ville (processus e) ; conformes par épisode
   (max, sommes, Page, balayage) ; cascade de portes sur sondes (ii) ; sonde sur le dernier état (iii) ; accumulation
   additive de sondes (H2) ; juge boîte noire ; plancher de sondes aléatoires appariées (N-029). Pour chacune : ce qu'elle
   lit (la fonction des données), ce qu'elle suppose (liste numérotée d'hypothèses : indépendance, échangeabilité,
   stationnarité du calibrage, marginale déplacée, lisibilité linéaire, position de lecture, longueur d'épisode, etc.).
2. **La carte** (une sous-section par hypothèse, numérotée A1, A2, … ; viser 15 à 25) : énoncé formel de l'hypothèse ;
   **classe d'écart** (la négation, au niveau des lois) ; **lemme** (« sous K, S est aveugle ») avec preuve courte ou
   « esquisse » ou « conjecture » ; **instances documentées** (identifiants de l'audit, R7) ou « aucune trouvée dans
   l'audit : question » ; **témoin de mesure** (quel objet à vérité connue, quelle quantité, quel nul — au niveau des
   scores ou des familles documentées ; jamais un procédé d'agent) ; **défense** (hypothèse de l'audit § 1 ter qui
   répond, ou « à poser », une phrase).
3. **Ce que le pôle peut mesurer tout de suite, sans dépense** (trois à cinq témoins au niveau des scores, sur le modèle
   de la mesure unanime : quel fichier existant, quelle quantité, quel nul ; ordre recommandé).
4. **Les questions** (classes sans instance) : énoncées comme questions, avec les mots clés d'une recherche d'antériorité à
   faire (R8), sans affirmer de nouveauté.
5. **Ce que la carte ne dit pas** et ce qu'une v2 devrait ajouter.

Dans ta réponse finale : le verdict, la liste des hypothèses A1…An en une ligne chacune (hypothèse → classe → lemme :
prouvé / esquisse / conjecture → instance ou question), le chemin et l'empreinte. Vise une heure.
