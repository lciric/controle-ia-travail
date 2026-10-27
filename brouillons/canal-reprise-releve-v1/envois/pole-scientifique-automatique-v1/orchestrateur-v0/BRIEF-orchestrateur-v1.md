# Brief — orchestrateur du pôle « scientifique automatique », version 0 (code et essais en simulation) — v1

Écrit par la lignée conv-audit le 2026-10-26 à 18:09 UTC pour un sous-agent (Opus 5.5). Français, sans acronymes. Tu lis
`/var/tmp/orchestrateur-pole-v1/fournis/` et tu écris seulement sous `/var/tmp/orchestrateur-pole-v1/sortie/`.

## Le besoin (mots de Lazar, 26 octobre, heure de Paris)

18:30 : « des agents qui font leurs propres expériences sur les hypothèses formulées et les éliminent au fur et à mesure,
genre darwinisme, et après recombinent celles qui ont survécu sur le mode bisociatif » ; 19:08 : « il nous faut absolument
un AI scientist qui puisse lancer des agents et tester ses hypothèses comme tu le fais […] le meilleur compromis rapidité de
conception / qualité des réponses / originalité des associations / solidité et rigueur des hypothèses pré-testées ».

Lis d'abord `fournis/conception-pole-scientifique-v1.md` (le cœur à implémenter : § 1), puis la relecture
(`relecture-meta-conception-v6-3-v1.md`, brique 2 : la forme corrigée du tirage) et les essais de la brique 1
(`essais-brique1-spectre-v1.md`, pour l'exemple d'une génération réelle avec verdicts « survit / éliminée / indécise »).
Le moteur des agents sera le **Claude Agent SDK** (`fournis/claude-agent-sdk-python/`, lis `README.md` et
`src/claude_agent_sdk/types.py` : `query()`, `ClaudeAgentOptions` avec `cwd`, `allowed_tools`, `disallowed_tools`,
`permission_mode`, `max_turns`, `max_budget_usd`, `model`, crochets `PreToolUse`, réglages de bac à sable). **Tu n'as ni
clé ni réseau** : le moteur réel n'est jamais appelé ici ; tout se teste avec un moteur simulé.

## Ce que tu écris (Python ≥ 3.10, bibliothèque standard seule pour le cœur ; `claude_agent_sdk` importé paresseusement par l'adaptateur réel)

Un paquet `sortie/pole/` :
1. `fiche.py` — la **fiche d'hypothèse** (dataclass + validation) : identifiant, énoncé, prédiction signée et chiffrée,
   métrique, nul, seuil, sévérité attendue (probabilité de passer le seuil sous le nul, dans ]0 ; 1[), coût borné,
   protocole, parents, domaines, opérateurs, contraintes, statut, `temoin` (None ou la vérité connue : « vraie » ou
   « fausse »). **Gel** : empreinte sha256 de la fiche canonique (JSON trié) écrite avant l'expérience ; toute exécution
   vérifie l'empreinte ; une fiche modifiée après gel est refusée.
2. `adaptateurs.py` — une interface `Adaptateur.lancer(role, consigne, dossier, budget_usd, max_tours) -> Resultat`
   (texte final, fichiers produits, coût déclaré, statut) ; `AdaptateurSimule` (déterministe, graine, pour les essais :
   il sait jouer un expérimentateur honnête, un expérimentateur qui triche — change de test après coup, ou déclare un
   verdict sans l'avoir calculé — et un vérificateur) ; `AdaptateurClaudeSDK` (réel : `query()` avec `cwd` = dossier de
   l'expérience, `allowed_tools=["Read","Write","Edit","Bash"]`, `max_budget_usd`, `max_turns`, `permission_mode`
   adapté au mode sans interaction, un crochet `PreToolUse` qui refuse toute commande Bash qui sort du dossier, lit
   l'environnement (`env`, `printenv`, `/proc/*/environ`), touche au réseau (`curl`, `wget`, `pip`, `git`), ou contient
   `sudo` ; la clé n'est jamais lue ni écrite par le code de l'orchestrateur : elle vient de l'environnement du
   processus, que l'opérateur fournit). L'adaptateur réel n'est pas exécuté ici : il est seulement importable et ses
   options sont essayées par une fonction pure `construire_options(...)` testée.
3. `cycle.py` — une **génération** : (a) gel des fiches ; (b) un expérimentateur par fiche, en parallèle (bornes de
   concurrence et de budget total par génération) ; son résultat doit contenir un bloc JSON `{"verdict": "survit" |
   "eliminee" | "indecise", "statistique": …, "seuil": …, "code": "<chemin>", "empreinte_fiche": "<sha256>"}` ; (c) un
   **vérificateur** par fiche, d'un autre modèle que l'expérimentateur (paramètre), qui rejoue le code et confirme ou
   infirme ; un verdict non confirmé devient « indécise » ; une empreinte de fiche différente devient « rejetée (test
   changé) » ; (d) **sélection** : éliminée → archive ; survivante → aptitude = −ln(sévérité attendue) ; indécise → un
   nouvel essai au plus, puis retirée ; (e) **mesure de qualité du pôle** sur les témoins (taux de fausses gardées, de
   vraies éliminées) écrite à chaque génération.
4. `recombinaison.py` — la **recombinaison bisociative** des survivantes, forme corrigée : noyau de diversité de domaine
   S_ij = ⟨d_i,d_j⟩² (vecteurs de domaine à partir des étiquettes, par exemple indicateurs normalisés), qualité q_i =
   aptitude, L = diag(q) S diag(q) + γI (semi-défini positif par construction : vérifie-le par une décomposition de
   Cholesky en pur Python), sélection gloutonne du déterminant maximal de taille k ; pour chaque paire tirée qui partage
   au moins un opérateur et passe le **filtre de compatibilité** (paires de marqueurs contradictoires dans les
   contraintes : linéaire / non linéaire, stationnaire / transitoire, discret / continu, convexe / non convexe,
   indépendant / dépendant), produire une **consigne de fusion** (le texte que l'agent de recombinaison recevra) et
   exiger de la fiche fille une prédiction nouvelle (un champ `ce_que_la_fille_predit_de_plus` non vide) ; la fiche
   fille porte ses deux parents.
5. `pole.py` — la boucle : population initiale (fichier JSON), générations successives, témoins plantés (une vraie et une
   fausse par génération au moins, tirées d'une liste fournie), arrêt sur budget, sur nombre de générations, ou quand plus
   aucune fiche ne survit ; un journal JSON par génération ; une archive complète ; une ligne de commande
   (`python -I -m pole …` avec `--moteur simule|claude-sdk`, `--population`, `--generations`, `--budget-usd`,
   `--sortie`).

## Essais (R5 : un cas sain et un artefact pour chaque garde)

`sortie/essais/` avec un exécuteur `python -I -m unittest` (pas de pytest requis) : gel et refus d'une fiche modifiée ;
expérimentateur tricheur (test changé après coup → « rejetée ») ; verdict sans calcul (le vérificateur infirme →
« indécise ») ; sélection par sévérité (une fiche qui ne prédit rien a une sévérité ≈ 1 et une aptitude ≈ 0) ;
semi-définie positivité du noyau corrigé sur 1 000 tirages ; filtre de compatibilité (contradictions plantées
détectées, couples sains gardés) ; témoins (un pôle simulé honnête garde la vraie et élimine la fausse ; un pôle simulé
complaisant les garde toutes deux, et la mesure de qualité le dit) ; budget (la génération s'arrête au plafond) ;
crochet `PreToolUse` (commandes interdites refusées, commandes saines acceptées) ; `construire_options` (cwd, outils,
budget). Une démonstration de bout en bout en simulation : trois générations, une population de six fiches, journal et
archive écrits.

## Ce que tu rends

`sortie/pole/`, `sortie/essais/`, `sortie/demo/` (sortie de la démonstration), `sortie/LISEZMOI-orchestrateur-v1.md`
(architecture, comment lancer en simulation, ce qu'il faut à l'opérateur pour le moteur réel : une instance avec Docker
ou un bac à sable, une clé à plafond de dépense dans l'environnement, et les limites connues), et un fichier
`sortie/EMPREINTES-sortie-v1.txt`. Réponse finale en six lignes : ce qui est fait, résultat des essais (nombre), la
démonstration, ce qui n'est pas testé (le moteur réel), les risques, l'empreinte du LISEZMOI.

## Interdits

Aucun réseau, aucun `git`, aucun sous-agent, aucune clé ni jeton (ne cherche ni n'affiche aucune variable
d'environnement de clé) ; rien lu hors de `fournis/`, rien écrit hors de `sortie/` ; Python avec `-I` ; heures lues sur
`date -u` dans la commande qui les écrit ; n'installe rien (le paquet `claude_agent_sdk` n'est pas installé : l'adaptateur
réel l'importe paresseusement et les essais n'en dépendent pas).
