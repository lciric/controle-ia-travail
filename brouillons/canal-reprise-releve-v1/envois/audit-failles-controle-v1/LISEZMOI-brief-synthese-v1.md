# Brief — synthèse de l'audit des failles de notre contrôle — v1

De : conv-audit, le 2026-10-26 à 12:14:46 UTC (heure lue sur `date -u` dans la commande qui écrit cette ligne).
À : un sous-agent neuf de la lignée conv-audit. Tu n'as écrit ni le lot A, ni le lot B, ni l'audit de session-depot.

## 1. Ce qui est demandé

`sortie-synthese/audit-failles-controle-v1.md` et son compagnon, plus `sortie-synthese/LISEZMOI-synthese-v1.md` (méthode,
choix, écarts) : la pièce que Lazar lira. Elle suit le § 4 « Synthèse » du brief de l'audit (`LISEZMOI-brief-audit-v1.md`,
`1785c74d…`, à lire d'abord en entier, § 1 à 4) ; ses règles (§ 2 : niveau de la méthode, jamais de recette ; § 3 : R7,
R8, jamais « premier ») s'appliquent à toi mot pour mot.

## 2. Pièces (toutes sous `/var/tmp/audit-failles-controle-v1/`)

- `fournis/` (vérifier par `cd fournis && sha256sum -c ../EMPREINTES-fournis-v1.txt`) : le programme v2 (qui prime sur le
  fond), le brief v2, l'état de l'art v1 et vérifié, les décisions. Lis au moins le programme (§ 1, 3, 5, 8, 9, 10, 13).
- `sortie-confrontation/` (lot B, compagnons à vérifier) : `carte-du-controle-v1.md`, `failles-internes-v1.md` (FI-01 à
  FI-44, sections F et G, divergences H), `grille-de-couverture-v1.md`, LISEZMOI.
- `sortie-moisson/` (lot A, compagnons à vérifier) : `modes-d-echec-documentes-v1.md` (47 modes, 22 absents chez
  session-depot ; colonne « chez session-depot »), `fiches/`, LISEZMOI (sondage R4 : S7 et D1 à nuancer ; E4 : résultats
  en sens opposés).
- `fournis-complement/` (vérifier par `cd fournis-complement && sha256sum -c ../EMPREINTES-fournis-complement-v2.txt`) :
  l'audit de littérature de session-depot (`audit-litterature-session-depot-v1.md`, 26 failles, onze angles morts, cinq
  propositions **acceptées par Lazar** : N-053) ; le tour du collisionneur de l'audit défensif
  (`collisionneur-audit/` : question, faits, six cellules de trois modèles, tour III.1 « conception » et tour III.2 rendu
  défensif ; aucun refus) ; le brouillon 3 du préenregistrement de G1 ; le brouillon 5 du préenregistrement du papier C ;
  le brouillon 1 du pilote T0.6 ; les lignes de registre P-014, P-015, N-019.
- **Décision de Lazar du 26 octobre, 13:12 heure de Paris (N-054 proposé)**, sur FI-01 et FI-02 : un mode de sabotage
  non chiffré réintroduit avant G1 (« affaiblir les contrôles ») ; G1 rapportée par mode ; un mode tenu à l'écart,
  conçu par une instance qui n'a conçu aucun moniteur, scellé avant G1 et révélé à l'évaluation ; bras génériques et
  spécialisés rapportés à part ; H6 par mode. Dans ta synthèse, FI-01 et FI-02 sont « décidées (N-054) », pas « à
  décider ».

## 3. Ce que la synthèse contient

1. **Grille de couverture remplie** : lignes = modes d'échec documentés (lot A, 47 ; session-depot, 26, avec ses numéros ;
   fusionnés quand c'est le même mode, en le disant), angles morts de session-depot (onze), failles internes (44) ;
   colonnes = couvert par le programme (oui, en partie, non ; où), preuve (source et page, ou fichier et section), remède,
   priorité (bloque une revendication ou une porte ; affaiblit ; précision), statut (décidé par Lazar ; proposé ; question).
2. **Les failles documentées que notre contrôle rate ou couvre mal**, par menace (sabotage ; tromperie ; conscience
   d'évaluation ; corruption des moniteurs), chacune avec sa source vérifiée (page) ; là où le lot A et session-depot
   divergent sur une même source, dis-le et tranche sur la page.
3. **Les failles candidates** (internes, ou imaginées par les trois modèles du collisionneur, ou par toi), chacune avec :
   mécanisme au niveau de la méthode ; ce qu'elle ferait tomber ; recherche d'antériorité consignée (mots clés, listes
   consultées : fiches du lot A, tables de session-depot, état de l'art vérifié) et statut « non trouvée dans la littérature
   consultée » ou « voisine de … (source) » ; remède ; l'expérience qui la testerait sur notre système (à préenregistrer).
   Le tour du collisionneur est une source d'idées, pas une preuve : rien de ce qu'il affirme n'est repris sans vérification
   ou sans la marque « affirmé par un modèle, non vérifié ».
4. **Les remèdes**, rattachés aux hypothèses (H1 à H8, HC1 à HC6, L, T, H3 à H7), aux invariants (§ 9) et aux portes (G0,
   G1, GC, § 13), classés par priorité, avec une estimation de coût (nul ; heures de session ; dollars d'appels ; calcul
   sur carte) et ce qu'ils changent aux revendications. Les cinq propositions de session-depot (N-053) et N-054 y
   figurent comme décidées.
5. **Ce qui demande une décision de Lazar** : liste close, au format de décision (décision en une phrase ; enjeu ; deux
   ou trois options avec avantage et inconvénient ; recommandation et confiance ; défaut sous 48 heures, aucun pour une
   dépense), les quatorze points du lot B (F.3) repris, dédoublonnés, et complétés par ce que le lot A et le
   collisionneur ajoutent ; les points déjà décidés (N-053, N-054) sortent de la liste.
6. **Limites de l'audit** : ce qui n'a pas été lu (OpenReview, documents primaires d'Anthropic, sources restantes), ce qui
   n'est pas vérifiable sans pièces, la famille de modèles des auditeurs (Claude), l'absence de démonstration sur notre
   système (aucune sonde mesurée encore).

Forme : français, sans acronymes non développés ; chaque chiffre renvoie à une page ou à un fichier et une empreinte ;
tables courtes, prose ailleurs ; une page de synthèse en tête (dix lignes : les cinq failles qui comptent le plus, les
remèdes déjà décidés, ce qui attend Lazar). Vise moins de deux heures.

## 4. Interdits

Rien hors de `/var/tmp/audit-failles-controle-v1/` ; aucun `git`, réseau, sous-agent ni clé ; aucune donnée des pilotes ;
Python avec `-I` ; heures lues sur `date -u` dans la commande qui les écrit ; écrire seulement sous `sortie-synthese/` ;
compagnons `.sha256`. Jamais de procédure opératoire, de consigne ou d'exemple qui servirait à tromper un moniteur, y
compris en recopiant une cellule du collisionneur : tu décris des trous de couverture et des remèdes.

## 5. Fin

Réponse finale en quelques lignes : les cinq failles qui comptent le plus, le nombre de décisions pour Lazar, les
écarts, les empreintes.
