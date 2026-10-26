# Lot A — moisson de la littérature récente et grise sur les modes d'échec du contrôle — LISEZMOI v1

De : sous-agent neuf de la lignée conv-audit (lot A), le 2026-10-26, de 10:30 à environ 12:15 UTC (heures lues sur
`date -u` ; le détail horodaté est dans `journal-moisson-v1.txt`). Je n'ai rien écrit du programme ni de l'audit de
session-depot.

## 1. Objet

- Brief : `../LISEZMOI-brief-audit-v1.md`, SHA-256 `1785c74df8950f7af449012dbe4f58bd4e76ae113fe7aae93df2447b0528c97e`,
  vérifié ; § 1 à 3 et lot A du § 4 lus en entier. `fournis/` vérifié par `../EMPREINTES-fournis-v1.txt` : 47 sur 47.
  Programme v2 lu en entier (§ 0 à 16).
- **Recentrage du coordinateur reçu vers 10:55 UTC** (journal, 10:56:37) : lire l'audit de session-depot
  (`../fournis-complement/audit-litterature-session-depot-v1.md`, SHA-256
  `29b32f620cb2310fad83166fd4f2957b3ce43b1c3dea090834d8c28f86e4823b`, lu en entier) ; ne pas retélécharger ni reficher
  ses 46 sources ; viser la littérature grise, ses « sources restant à lire » et les modes qu'il ne couvre pas ; ajouter
  une colonne « chez session-depot » ; contrôler par sondage trois de ses affirmations « vérifiées ».

## 2. Ce qui est livré

| pièce | contenu |
|---|---|
| `modes-d-echec-documentes-v1.md` | table de 47 modes d'échec (sections A à G), colonne session-depot, divergences, sondage R4 |
| `fiches/*.md` | 33 fiches : 30 sources nouvelles, 3 sources déjà tenues (préfixe `tenu-`) |
| `journal-moisson-v1.txt` | chaque requête de téléchargement, avec adresse, heure, code HTTP, taille, empreinte |
| `EMPREINTES-moisson-v1.txt` | empreintes de toutes les pièces et de tous les fichiers téléchargés |
| ce fichier | méthode, requêtes, manques, écarts |

Chaque pièce de `sortie-moisson/` a son compagnon `.sha256` (« empreinte, deux espaces, nom nu ») ; chaque fichier
téléchargé aussi, dans son dossier. Contrôle d'ensemble, chemins relatifs à la racine de l'audit :
`cd /var/tmp/audit-failles-controle-v1 && sha256sum -c sortie-moisson/EMPREINTES-moisson-v1.txt`.

**En chiffres.**
- Sources nouvelles lues et fichées : **30** (19 PDF, 11 pages web ; la note de l'institut britannique compte pour une
  source en deux fichiers). Hors des 46 de session-depot et des 146 PDF de `pdf-main/`.
- Sources déjà tenues lues : **5** — 3 fichées (`pdf-main/` 2601.11516, 2610.04575, 2605.16626) et 2 relues pour le
  sondage (`pdf-main/` 2509.21344, 2607.06596).
- Sources de session-depot relues pour le sondage : **2** (2509.15541, 2511.16035), sur mes copies d'empreinte identique.
- Modes d'échec relevés : **47** ; chez session-depot : 16 « oui », 9 « oui en partie », **22 « non »**.
- Sondage R4 : 4 affirmations contrôlées (3 demandées) : 2 conformes, 2 conformes sur les chiffres avec portée à
  préciser ; détail en fin de table.

## 3. Méthode

1. Identifiants vérifiés par l'interface d'arXiv (`export.arxiv.org/api/query`, trois appels groupés : 10:33, 10:34 et
   10:57 UTC) avant tout téléchargement ; titres de première page comparés à l'interface après téléchargement : 26 sur
   26 conformes pour arXiv.
2. Téléchargements : arXiv par `https://arxiv.org/pdf/<identifiant>v<version>`, un dossier neuf par source, 5 s entre
   deux requêtes, arrêt prévu au premier 429 ou 403 (aucun reçu d'arXiv) ; pages web et PDF hors d'arXiv par `curl`,
   3 s entre requêtes. Script : `telecharger_arxiv_v1.sh` (bloc-notes de la session, hors du dossier de l'audit,
   SHA-256 `f1607bf2defedc2820b3359fb3b83d030a5128764968ed9245ec38ee708a8dfb` ; listes `liste-arxiv-lot1-v1.txt`
   `2a4524ab…`, `liste-arxiv-lot2-v1.txt` `1176c37e…`).
3. Lecture : `pdftotext -layout` page par page (numéro = page physique du PDF ; pour la fiche système Mythos, il
   coïncide avec le numéro imprimé sur les pages lues) ; texte visible des pages HTML extrait par un analyseur de la
   bibliothèque standard ; outil `cherche_v1.py` (bloc-notes, SHA-256
   `c5da5f5a1219d4a4aa58304b7865181fd5ba116b25ce4048b3d99fbfb61ed496`), lancé avec `python3 -I`, jamais depuis un
   dossier de téléchargement. Rien de téléchargé n'a été exécuté.
4. Fiches : ce que la source établit sur un mode d'échec, page ou section citée, conditions, ce qu'elle ne dit pas, ce
   que ça touche chez nous (avis), une phrase citée au plus. Pour une page web, je cite la section (intertitre).
5. Table : une ligne par mode et source principale ; force de la preuve en trois niveaux ; colonne session-depot
   remplie en relisant ses tables (a) et (b) et sa section (d).
6. Empreintes : toutes les empreintes complètes écrites dans les fiches et la table ont été recomparées aux fichiers
   (34 sur 34 conformes, vers 12:11 UTC) ; une abréviation fausse de la table a été corrigée avant scellement.

## 4. Requêtes faites

Recherche web (outil de recherche, mode standard), dans l'ordre :
1. « Liars' Bench evaluating lie detectors for language models arXiv »
2. « "Difficulties with evaluating a deception detector for AIs" arXiv »
3. « "off-policy" training data probe generalisation deception probes arXiv Kirch »
4. « "Narrow Finetuning Leaves Clearly Readable Traces in Activation Differences" arXiv »
5. « UK AISI white box control sandbagging probes update investigation »
6. « evaluation awareness unverbalized activation probes system card 2026 steering misaligned behavior increases »
7. « Optimizing AI agent attacks with synthetic data control red team attack policy elicitation arXiv »
8. « "Simple probes can catch sleeper agents" Anthropic caveat backdoor insertion artifact »
9. « "White Box Control at UK AISI" update on sandbagging investigations alignment forum »
10. « arXiv 2026 sandbagging detection probes white-box fails fine-tuned model organisms generalization »
11. « Claude Mythos system card evaluation awareness probes unverbalized »
12. « METR review Opus 4.6 sabotage risk report March 2026 monitoring limitations »
13. « Anthropic alignment blog "Automated Researchers Can Subtly Sandbag" »
14. « "Attacking the Oversight, Not the Mission" NeurIPS 2026 probe »
15. « LessWrong eval awareness steering detects the test not the sabotage Llama 8B »
16. « "Towards Measuring and Detecting Unverbalized Evaluation Awareness" ICML 2026 »
17. « "Attacking the Oversight" probe fine-tuning evasion localized position fresh probe recovers signal »

Lectures de repérage (outil de lecture web, non citées comme sources) : page ICML 76932 (ensuite sauvée et citée
d'après la copie sauvée), billet LessWrong « where we are on evaluation awareness » (Essifi, 25 avril 2026 ; utilisé
seulement pour trouver des sources, ni sauvé ni cité), billet d'Anthropic sur l'audit d'un saboteur (ensuite sauvé et
cité d'après la copie sauvée).

Candidats identifiés puis écartés par la borne de 30 ou faute de temps (non lus, R8 : ce sont des questions, pas des
trous) : arXiv 2602.05656 (indiscernabilité normative sous évaluation comportementale), 2606.27091 (vulnérabilités
d'évasion créées par réglage fin, Llama-3.1-8B), 2512.15674 (oracles d'activations), 2502.16681 (sondes sur
autoencodeurs parcimonieux) ; billets LessWrong « Rephrasing reduces eval awareness », « Measuring non-verbalised eval
awareness by implanting eval… », « Sonnet 4.5's eval gaming seriously undermines alignment », « How eval awareness
might emerge in training », « Current activation oracles are hard to use » ; billet d'Anthropic sur la conscience
d'évaluation dans BrowseComp ; billet d'Apollo Research sur Claude Sonnet 3.7 ; rapport « Frontier Risk Report » de
METR ; rapport de tendances de l'institut britannique.

## 5. Ce qui n'a pas été trouvé ou pas pu être téléchargé

- **OpenReview** : le PDF de Vu et Saunders (`VgHY8vLww3`) renvoie 403 (10:54 UTC) ; aucune autre tentative sur cet
  hôte. Les trois autres travaux de conférence (ICML 79272 et 79377, NeurIPS 168158) ne sont lus que par leur
  **résumé** sur la page de conférence ; leurs chiffres sont marqués « résumé seul ».
- **greaterwrong.com** : connexion coupée deux fois (11:10 UTC) ; les deux billets ont été sauvés depuis lesswrong.com.
- **Documents primaires non lus** : le « alignment risk update » de Claude Mythos Preview (§ 5.2.3, renvoyé par la
  fiche système p. 103), le rapport de risque d'août 2026 et le rapport de risque de sabotage d'Opus 4.6 (je n'ai lu
  que les revues de METR), la fiche système d'Opus 4.6. Les chiffres qui en viennent sont marqués « seconde main ».
- Seconde copie de la fiche système Mythos (`…/8b8380204f74670be75e81c820ca8dda846ab289.pdf`, modifiée le 7 avril
  2026) : non téléchargée ; j'ai pris la copie modifiée le 9 avril.
- Sources « restant à lire » de session-depot non lues : n° 6 (introspection, « Lindsey 2026 »), Roger et Greenblatt
  2023 (2310.18512), Motwani et al. 2024 (2402.07510), Laine et al. 2024 (2407.04694), et le corps de 2608.21664.
- Non trouvé : aucun identifiant arXiv pour les travaux ICML 2026 sur la conscience non verbalisée ni pour « Attacking
  the Oversight, Not the Mission » dans les résultats consultés (recherches 14, 16, 17).

## 6. Écarts déclarés

1. **Dix doublons avec session-depot** téléchargés de 10:35 à 10:37 UTC, avant le recentrage : 2505.23836, 2507.01786,
   2509.15541, 2510.20487, 2505.13787, 2508.00943, 2412.12480, 2410.03768, 2511.16035, 2511.17408 ; empreintes
   identiques aux siennes (`sha256-pdf-session-depot-v1.txt`). Ils restent sur disque (on n'efface rien), ne sont pas
   fichés et ne comptent pas parmi les 30 sources nouvelles ; deux ont servi au sondage R4. Au total, 41 fichiers ont
   été téléchargés (29 PDF, 12 pages).
2. **Lecture de la borne** : je compte 30 sources nouvelles hors doublons ; si la borne devait compter tous les
   téléchargements, elle serait dépassée (40 sources, 41 fichiers). Au coordinateur de trancher.
3. **Sources déjà tenues fichées** (3) alors que la consigne du recentrage visait d'abord le gris : elles documentent
   des modes absents chez session-depot (seuil et unité de risque, décalage de contexte, évasion des moniteurs d'agent).
4. **Une empreinte écrite de mémoire** : dans la fiche Minder, j'ai d'abord écrit une empreinte dont la fin était
   complétée de mémoire et non lue ; repérée à la relecture, par comparaison avec la valeur calculée, et remplacée
   avant tout scellement ; toutes les empreintes ont ensuite été recomparées (section 3, point 6).
5. **Heures approximatives corrigées** : neuf fiches portaient des heures « vers … » fausses de 1 à 38 minutes ; elles
   ont été remplacées par les heures du journal avant scellement.
6. Le journal porte deux lignes pour le même refus d'OpenReview (la ligne du script, puis la mienne).
7. Les avis « ce que ça touche chez nous » ne s'appuient que sur le programme v2 ; je n'ai pas lu l'état de l'art ni
   les décisions au-delà de ce que cite l'audit de session-depot (le lot B s'en charge).
8. Une phrase citée contient des symboles mathématiques de la page (« ≤ », « ~ ») rendus en texte (fiche Latent
   Undertow).

## 7. Règles respectées

Aucun `git`, aucune clé, aucun sous-agent ; aucune lecture des données des pilotes ; Python avec `-I` ; rien de
téléchargé n'a été exécuté ; chaque téléchargement dans un dossier neuf ; aucun fichier écrasé ; aucune procédure,
consigne, exemple de texte, code ou réglage d'évasion écrit (les familles d'évasion des sources sont nommées au plus,
jamais détaillées) ; une phrase citée au plus par source ; aucun « premier », « nouveau » ou « inédit » comme
affirmation.
