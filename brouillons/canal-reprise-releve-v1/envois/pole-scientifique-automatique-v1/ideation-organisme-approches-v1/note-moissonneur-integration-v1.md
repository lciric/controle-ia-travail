# Intégration du moissonneur (pièce 5 de la conception v7) dans l'orchestrateur du pôle — note de conception, avec recommandation (v1)

Lignée conv-audit (sous-agent), 29 octobre 2026, relevé `date -u` **08:49 UTC**. Sur le mot de Lazar du 29 octobre, 09:44 heure de
Paris (« oui et je veux lancer ça », R-437). **Proposer avec recommandation** : la note précède le code (v44 ou suivante, après CL10
de la v43) et ne décide d'aucune dépense. Processeur seul : aucun réseau, aucune clé, rien lu sous `donnees/`, aucun fichier modifié.

**Fichiers lus** (empreintes, huit caractères) : conception v7 `31fc8c4b…` ; programme de conception v6 `6e95f6c5…` ; `pole/relais.py`
`b5a76343…` ; `pole/relais_reel.py` `75d8f98a…` ; `pole/garde_outils.py` `e0df9743…` ; `pole/adaptateurs.py` `00b8f1a2…` ;
`pole/ideation.py` `4e798f36…` ; `pole/caviardage.py` `78abfd47…` ; LISEZMOI v43 `a9fca6ac…` ; note du tour (c) `ad330072…` ;
`corpus-primaire-v1/LISEZMOI-v1.md` `8c88fe10…` ; `.claude/hooks/garde_calcul.py` `579f65c8…` ; décisions R-433, R-434, R-436, R-437.

## Verdict

Recommandation : **(A) — arXiv et OpenAlex, métadonnées et résumés seulement, servis par le noyau en « outil par protocole » à tous les
proposeurs (Claude et Argon à égalité), jamais aux juges** ; code avec relais factice, aucune moisson réelle avant GO. Confiance **0,7**.
Trois écarts à la conception v7 § 5 : (1) **le noyau est le seul client du relais de moisson, jamais l'agent** (aucune commande
`moisson …` dans la garde des outils) ; (2) un **relais de moisson séparé** du relais de clé Anthropic ; (3) la moisson se joue dans un
**tour court entre la passe 1 et la passe 2**, pas dans une passe à contexte plein.

## 1. Ce qui est moissonné, et pour qui

- **Demande** : un proposeur d'idéation (Opus 5.5, Fable 5.1 ou Argon) rend un bloc
  `{"moisson": [{"source": "arxiv", "requete": "…", "resultats": 5}]}` ; le noyau valide, garde, interroge le relais et sert les
  résultats au tour suivant. Même mécanisme que la lecture du dossier fermé par protocole (R-433, R-434) : un module commun
  (`pole/protocole_outils.py` : lecture du bloc, quotas, journal, section servie) écrit une fois.
- **Servi**, par résultat : titre (≤ 300 caractères), auteurs (≤ 300), date, identifiant (arXiv, identifiant d'objet numérique,
  OpenAlex), résumé (≤ 2 000), lien vers la page de notice (jamais vers un PDF), source, et une étiquette de provenance
  `[moisson:<source>:<empreinte12>:<identifiant>]`. Au plus ≈ 2 800 caractères par résultat.
- **Jamais servi : le texte intégral.** Un PDF lu à la volée défait les retraits de sûreté déclarés page par page par le corpus primaire
  (LISEZMOI du corpus, § 6 : instructions de sabotage, recettes d'injection, annexes d'invites d'attaque — par exemple 2510.09462 p. 4,
  5, 8 et annexes E-F). Le texte intégral n'entre que par la **chaîne du corpus primaire** (extraction par un sous-agent, retraits
  déclarés, contrôle de fidélité, empreinte, liste blanche). La moisson l'alimente : en fin de course le noyau écrit
  `candidats-corpus.json` (identifiants cités à partir de la moisson).
- **PDF à la volée avec caviardage automatique : non pour la première version.** `caviardage.py` ne vise que des formes de clés ; la
  garde lexicale **signale** sans rien retirer ; un retrait de sûreté est un jugement relu, page par page. S'y ajoutent la taille (10 à
  77 pages, quand les gardes de consigne de la v43 sont déjà franchies aux réglages du devis) et R7 (un texte extrait sans relecture
  n'est pas opposable). Plus tard (option C), seulement comme **quarantaine** : le relais dépose le PDF empreinté hors des dossiers
  d'agents, pour la chaîne du corpus.
- **Résumés** : texte externe, donc caviardé, passé à la garde lexicale (un résumé signalé est servi **réduit au titre**, signal au
  journal), et servi entre délimiteurs : « données, jamais consigne ».

## 2. Sources

| source | accès | apport pour l'antériorité (R8) | sûreté | avis |
|---|---|---|---|---|
| arXiv | gratuit, sans clé ; débit limité (une requête toutes les trois secondes, de mémoire, SUPPOSÉ) | le champ paraît surtout en prépublication : tous les papiers listés par le corpus primaire v1 ont un identifiant arXiv, sauf un (LISEZMOI du corpus, § 3, 4) | métadonnées structurées, résumés courts d'auteurs | **oui** |
| OpenAlex | gratuit ; courriel de politesse (conditions à relire au branchement, SUPPOSÉ) | revues et conférences hors arXiv, graphe des citations ; résumés en index inversé (SUPPOSÉ), reconstruits par le relais | idem | **oui** |
| Semantic Scholar | clé gratuite, quotas | citations et recommandations, en grande partie couvertes par OpenAlex | idem ; une clé à tenir | **option (B)** |
| Brave | payant, web entier | billets de forums et de laboratoires | pages arbitraires : injections, recettes, contenus instables ; dépense | **non** |

**Ce que coûte le refus de Brave** : une partie de l'antériorité du contrôle paraît d'abord en billets de forum. R8 s'applique donc à
la moisson : une absence se rapporte « non trouvée par la moisson (sources, date) », jamais « zone vierge ».

## 3. Architecture

**Qui parle à qui.** Agent → bloc de demandes dans sa réponse → noyau (validation, quotas, **garde de fuite**) → relais de moisson
(boucle locale, jeton factice propre) → amont à adresse fixe codée par source. L'agent n'a ni outil, ni réseau, ni l'adresse du relais :
`tools=[]` reste pour les rôles d'idéation, `garde_outils.py` ne gagne aucune commande, `environnement_commande` ne transmet rien de neuf
à Argon. La garde par motifs n'est qu'une première barrière (docstring de `garde_outils.py`) ; le protocole ferme le canal par
construction et vaut pour Argon.

**Relais séparé** (`pole/relais_moisson.py`, sur le modèle de `relais_reel.py`) : processus à part, boucle locale seule, clés éventuelles
lues dans un fichier à lecture unique (`lire_cle_fichier` ; aucune clé en option A, seul le courriel), journal JSON par ligne sans clé.
Ne pas ajouter de routes au relais Anthropic : il porte la clé qui coûte, son périmètre (`CHEMINS_PERMIS = ("/v1/messages",)`) a été
fixé par les contre-lectures C10 et F-C7.

**Routes** : `GET /moisson/arxiv?q=…&n=…`, `GET /moisson/openalex?q=…&n=…`, `/moisson/semantic-scholar` en (B) seulement,
`GET /moisson/etat` (compteurs). Toute autre route, dont `/moisson/brave`, rend 404 ; aucun paramètre hors `q` et `n`. Le relais
normalise la réponse et rend `{source, requete, n, horodatage, empreinte_brute, resultats, empreinte}` (SHA-256 des octets de l'amont,
puis du JSON normalisé canonique).

**Quotas** (proposés ; nœud), tenus par le noyau par rôle et par course, et **une seconde fois par le relais** (plafond de requêtes par
source et par jour, indépendant de l'orchestrateur) :

| rôle | tours de moisson | requêtes par tour | résultats par requête | servi au pire cas |
|---|---|---|---|---|
| `proposeur_ideation` (Claude ou Argon) | 1 (réglage borné à 2) | ≤ 4 | ≤ 5 | 20 résultats ≈ 56 000 caractères |
| `juge_ideation` | 0 (refus dur) | — | — | — |

Une demande refusée compte dans le quota.

**Garde de fuite** (noyau, avant tout envoi ; refuse la requête, jamais la course) :
1. 3 à 200 caractères, 25 mots au plus ; ni retour à la ligne, ni caractère de contrôle ;
2. ni adresse (`://`, `www.`), ni `@ = ? & # % < > { } [ ] | $ \` ; `/` seulement dans un identifiant arXiv ancien ;
3. aucun secret : `caviardage.contient_secret`, noms de `relais.NOMS_DE_CLE`, les jetons factices ;
4. aucun identifiant interne : identifiant d'épisode (`tâche/épisode/passe`), étiquettes anonymes (`T01`…), suite hexadécimale de 12
   caractères ou plus, `GO-…`, `R-…`, `N-…`, `CL…`, nom de fichier, fragments de `FRAGMENTS_PIECES_INTERDITS` (`donnees`,
   `mode-tenu-a-l-ecart`, `banque`, `prereg`, `test-final`…) ;
5. aucun texte de test : bardeaux de 8 mots normalisés comparés à un **registre d'empreintes de bardeaux** (témoins, épreuve finale,
   tâches de la banque, mode tenu à l'écart), scellé par qui détient ces textes — le noyau ne lit que des empreintes ;
6. aucun extrait de pièce au-delà de 60 caractères contigus, hors titres déclarés des extraits (chercher un titre est l'usage normal).

L'agent reçoit un motif **générique** ; le motif exact va au journal seul (un motif précis apprendrait à reformuler). Le relais refait
les gardes 1 à 3.

**Provenance et R7.** La fiche cite une antériorité moissonnée sous un **troisième statut `MOISSONNE`** (à côté de `RAPPORTE`, lu dans
une pièce, et `SUPPOSE`), étiquette dans la référence (≤ 500 caractères, borne actuelle). Le noyau marque `non_opposable: true` toute
antériorité `MOISSONNE` tant qu'un PDF empreinté n'est pas lu par la chaîne du corpus ; aucun chiffre d'un résumé n'entre dans un
préenregistrement. Après la course, il vérifie chaque `MOISSONNE` (étiquette servie à **ce** proposeur, identifiant et titre
concordants) : extension de la lecture L7 du tour (c), rapportée à côté du classement, jamais servie aux juges.

**Cache et rejouabilité.** Clé = empreinte de la requête canonique (source, requête normalisée, `n`, version du schéma). Chaque réponse
acceptée est scellée dans `SORTIE/noyau/moisson/<clé>.json`, hors des dossiers d'agents ; l'index des empreintes va au manifeste de
fin. Deux modes consignés au départ : **frais** (relais interrogé, cache écrit) et **rejeu** (cache seul, **jamais le réseau** ; entrée
absente → « absente du cache »). Le rejeu reproduit ce que le noyau a servi, pas ce que les agents demandent.

## 4. Où ça se branche

- **Dans `executer_ideation`**, entre les passes : un **tour de moisson** par proposeur, consigne courte (question, vue courte de ses
  fiches de passe 1 — nom, énoncé, originalité, antériorités —, règles, quotas), réponse = bloc de demandes ; les résultats entrent
  dans sa consigne de passe 2, section « Moisson servie par le noyau (données ; résumés non opposables) ». Moisson ⇒ seconde passe
  obligatoire. Les passes restent à un appel (`MAX_TOURS_IDEATION` inchangé) ; le tour est une session à part, plafond et ligne de
  journal propres, sous le rôle `proposeur_ideation` (rien de neuf pour la commande d'Argon).
- **Pourquoi pas dans la passe** : sous protocole chaque tour renvoie tout le contexte ; la passe 2 d'Argon au pire cas fait 1 456 692
  caractères, 3,02 dollars au barème du devis, déjà au-dessus de son plafond de 2,5 (LISEZMOI v43).
- **Coût en jetons** (barème du code, 4 caractères par jeton ; Argon à 8,3 en entrée, rapport de sortie 5 ; tailles SUPPOSÉES) : tour
  typique ≈ 25 000 caractères plus ≈ 1 000 jetons de sortie — Opus ≈ 0,04, Fable ≈ 0,11, Argon ≈ 0,09 dollar ; moisson servie en
  passe 2 (≈ 32 000 caractères) — Opus ≈ 0,03, Fable ≈ 0,08, Argon ≈ 0,07. **≈ 0,4 dollar par course à trois proposeurs, ≈ 1 au pire
  cas** (tour de 100 000 caractères, moisson de 56 000). Ces 56 000 caractères entrent dans les gardes de taille de la passe 2 et dans
  `--mesurer-consignes`.
- **Le juge figé ne moissonne pas** et ne reçoit pas la moisson : même information pour toutes les fiches, Argon juge à poids égal sans
  outil. À écrire au devis : les fiches citeront plus de `MOISSONNE` que les témoins du tiers ; la lecture des témoins doit compter les
  citations, ou le tiers écrire des antériorités de même forme.
- **Égalité Claude/Argon** : même consigne, mêmes quotas, même garde, même section servie. Réserve invisible au noyau : la commande
  d'Argon appelle Gemini, qui peut offrir une recherche en ligne intégrée ; **elle doit être coupée** (question à session-depot, avec
  celle du message n° 188).
- **Comparabilité** : variable nouvelle ; lecture propre « (a) contre (a) plus moisson », séparée du tour (c).

## 5. Épreuves R5 (hors ligne, relais factice, aucun réseau)

Relais factice en mémoire pour les essais du noyau ; un essai de `relais_moisson.py` sur la boucle locale contre un amont factice local,
comme `test_v6_relais_reel.py` ; un garde-fou d'essai qui refuse toute connexion hors boucle locale.

- **Cas sain** : une requête → 5 résultats servis, étiquettes présentes, empreintes recalculées égales ; la fiche cite `MOISSONNE` ;
  L7 la retrouve ; `non_opposable: true` ; cache scellé ; la course en mode rejeu sert les mêmes octets sans appeler le relais.
- **Cas sain de la garde** : les titres des dix extraits du corpus et des requêtes de 3 à 25 mots passent.
- **Artefacts** (refus, motif exact au journal, motif générique servi, quota décompté, course poursuivie) : bardeau d'un témoin ;
  identifiant d'épisode ; empreinte hexadécimale ; extrait de pièce de plus de 60 caractères ; clé `sk-ant-…` ; jeton factice ; adresse ;
  retour à la ligne ; 201 caractères ; cinquième demande (quota) ; source `brave` (refus au noyau, 404 au relais) ; juge qui demande
  une moisson (refus dur).
- **Relais indisponible** (refus de connexion, délai, statut 5xx) : consigne de passe 2 et journal portent « moisson indisponible »,
  **la course continue** — distinct d'une session de modèle en échec, qui l'arrête toujours (CL31-01, CL31-02).
- **Réponse altérée** : empreinte fausse → rejetée, ni servie ni mise en cache ; en rejeu, une entrée de cache qui ne concorde plus
  avec l'index **arrête le rejeu** (provenance altérée, R6).
- **Résumé piégé** → servi réduit au titre ; **bloc de demandes illisible** → passe 2 sans moisson, dit au journal.
- **Absence de canal** : aucune variable du relais de moisson chez un agent ni dans `environnement_commande` ; `tools=[]` inchangé.

## 6. Devis et nœuds

- **Ce qui coûte** : arXiv et OpenAlex, rien que le temps (≈ 12 requêtes par course) ; Semantic Scholar, une clé gratuite (compte :
  nœud) ; Brave, payant. Jetons : ≈ 0,4 dollar par course, ≈ 1 au pire cas, au devis de la course qui l'emploie (plafond du tour
  proposé : 0,5 dollar par session, SUPPOSÉ).
- **Où tourne le relais réel** : chez session-depot, qui a le réseau et tiendrait les clés ; ce dépôt n'appelle jamais l'amont.
  `garde_calcul.py` ne garde que les instances payantes et R10 dans les sessions de ce dépôt : ni les agents du pôle
  (`setting_sources=[]`) ni la moisson. « Aucun réseau » tient ici par l'architecture (le noyau seul client) et le garde-fou des essais.
- **Mot de Lazar requis** : (1) sources (A, B ou C) ; (2) quotas ; (3) Brave exclu ; (4) courriel de politesse d'OpenAlex (une identité
  envoyée à un tiers : laquelle ?) ; (5) statut `MOISSONNE` au gabarit (touche témoins et grille) ; (6) le noyau, non l'agent, client
  du relais (écart à la conception v7 § 5) ; (7) **GO de la première moisson réelle**, même à 0 dollar : premier usage du réseau par
  l'organisme.
- **Ordre** : v44 (ou v45 si la v44 porte déjà le tour (c), une relecture par version ; module de protocole commun) = protocole, tour
  de moisson, garde de fuite, `MOISSONNE`, cache, relais factice, `relais_moisson.py` contre un amont factice, essais, relecture R2 ;
  puis relais réel chez session-depot et une épreuve réelle de quelques requêtes ; puis première moisson dans une course, sous GO.

## 7. Options

**Décision** : sources et périmètre de la première version du moissonneur. **Enjeu** : antériorité vérifiable et moins de `SUPPOSE`,
contre sûreté du contenu servi, égalité des proposeurs et dépense.

| option | ce que c'est | avantage | inconvénient |
|---|---|---|---|
| **(A)** | arXiv et OpenAlex, métadonnées et résumés, par protocole, tour court entre les passes, juges sans moisson | aucune clé ni dépense de source ; texte court et structuré ; égalité par construction ; rejouable | billets de forum invisibles ; résumés non opposables ; témoins à adapter |
| **(B)** | (A) + Semantic Scholar | citations et recommandations | clé et compte (nœud), quotas d'un tiers ; apport en partie couvert par OpenAlex |
| **(C)** | (A) + PDF par le relais, plus tard | texte intégral à portée | rien de servable sans retraits relus ; tient seulement comme quarantaine versée à la chaîne du corpus |

**Recommandation : (A)** ; (B) à rouvrir si L7 montre des antériorités manquées ; (C) seulement en quarantaine. **Confiance : 0,7**
(formats et conditions des amonts non vérifiés ; gain sur les fiches non mesuré).

**Défaut sous 48 heures (≈ 31 octobre, 08:50 UTC)** : (A) **en préparation seulement** — code et essais hors ligne, quotas du tableau.
Le défaut n'autorise ni moisson réelle, ni compte ou clé, ni courriel envoyé, ni dépense.

## Réserves

- Formats des amonts, noms d'hôtes, débits et conditions d'accès : de mémoire, SUPPOSÉS ; à relire au branchement par session-depot.
- Coûts calculés sur le barème du code ; tailles de résumés et de fiches SUPPOSÉES ; prix d'Argon pris au devis (8,3).
- L'empreinte rendue par le relais détecte une altération de transport ou de cache, pas un relais menteur.
- Les requêtes quittent la machine et sont journalisées par les amonts : elles révèlent des mots-clés de nos idées (borné à 4 requêtes
  de 200 caractères par proposeur, non nul).
- Le registre d'empreintes de bardeaux n'existe pas encore ; sans lui, la garde 5 ne couvre que les témoins que le noyau détient.
