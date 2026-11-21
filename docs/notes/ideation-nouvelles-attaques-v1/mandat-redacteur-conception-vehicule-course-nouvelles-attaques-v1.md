VERSION DE PYTHON : `python3 --version` ; AUCUN `-c`, AUCUN `-` APRÈS PYTHON3 SAUF `-B`

AUCUNE COMMANDE DE LISTE : NI `ls`, NI `find`, NI `git ls-tree`, NI `git ls-files`, NI `git status`, NI `grep -r`, NI JOKER. TOUT FICHIER S'OUVRE PAR SON CHEMIN COMPLET. UNE COMMANDE SIMPLE PAR APPEL : NI `&&`, NI `;`, NI BOUCLE, NI SUBSTITUTION. `git show` TOUJOURS REDIRIGÉ PAR `>` VERS UN CHEMIN COMPLET DE TON DOSSIER, SUR `origin/main`, APRÈS `git -C /home/user/controle-ia-travail-organisme fetch origin main`.

# Mandat du concepteur — le véhicule de la course « nouvelles attaques » : conception, découpage du code, épreuves — v1

Pièce de travail (classe C), donnée par la session du compte organisme le 2026-11-21, sur le mot de la mère (06:40Z) : « Lance la conception du véhicule (défaut accepté). » Ce mot s'appuie sur la v9 scellée, § « Ce qui reste à écrire avant l'allumage », point 1. **Aucune dépense, aucun appel, aucun code lancé.** Tu conçois ; le code sera écrit par un développeur O et vérifié par un vérificateur S, sur des mandats tirés de ta conception. **Aucune recette dans tes sorties.**

## Qui

Un concepteur neuf (modèle F). Tu n'as écrit ni la v9, ni l'inventaire, ni aucun orchestrateur. Tu signes « concepteur du véhicule, modèle F ».

## Ce qui fait foi (vérifie chaque empreinte contre son compagnon)

- **L'inventaire de l'allumage et son cahier des charges du véhicule** (dix sections, chaque fonction avec sa ligne), ainsi que le gabarit des témoins : `/home/user/controle-ia-travail-organisme/docs/notes/ideation-nouvelles-attaques-v1/inventaire-allumage-v1/inventaire-allumage-course-nouvelles-attaques-v1.md` (`0737906f9901de39ddd9b1585679b5b44e6bac67e7051a10374d3e0e496c06e0`), `gabarit-temoins-plantes-course-nouvelles-attaques-v1.md` (`a84de0bf…`) et le rapport (`c60829a5…`), même dossier. **C'est ton point de départ.**
- Sur `origin/main`, par `git show` redirigé :
  - la v9 (`prereg/ideation-nouvelles-attaques-v1/preenregistrement-court-course-nouvelles-attaques-v9.md`), l'additif 1 v5, le complément de valeurs v3 et son additif (R-4356), le devis v11, la question v5, la partie servie et la synthèse servie ;
  - l'ordre de course v3 et son erratum 1 (`docs/notes/ideation-nouvelles-attaques-v1/conception-v3/`) ;
  - les orchestrateurs existants et leurs rapports, à trouver par les chemins que citent le registre et la v9. Le dernier orchestrateur de course (v68, sa contre-lecture et celle de la fiche v68), le cadre de la v69 et de la v70 (R-4060 : additif des interrupteurs, cadre de la v70), le lanceur 11 et la course v9 (`scripts/lancer_course_auto_conception_v9.py`, son épreuve des témoins `scripts/epreuve_temoins_auto_conception_v9.py`).
- `registres/go.md` et `registres/decisions.md`. Nomme tes copies de lecture `lecture-registre-origin-main.md` et `lecture-go-origin-main.md` : elles sont exclues du versement.

## Contraintes, à la lettre de la v9

- Un nom neuf, **jamais v69 ni v70**, ces deux noms étant réservés au palier 1 de l'héritage et à sa lecture.
- Le régime : « trois générations, sans étage de tests de mort, lecture du registre des tentatives ».
- Un lanceur qui suit le lanceur 11, un additif scellé et une configuration propre.
- Trois relais et cinq clés, routés par rôle (additif 1 v5, l. 172). Le proposeur de l'espèce 3 est sur Minuit (R-4356). Rigaud est une clé hors course.
- Toutes les gardes et tous les arrêts nommés que le texte confie au véhicule, chacun avec une épreuve sur un cas sain et sur un artefact (R5).

## Ce que tu écris

1. **`conception-vehicule-course-nouvelles-attaques-v1.md`** :
   - **Le choix de base** : de quel orchestrateur et de quel lanceur existants le véhicule part (chemin et empreinte sur `main`), ce qu'il en garde, ce qu'il retire (étage des tests de mort, par exemple) et ce qu'il ajoute. Justifie le choix par la plus petite différence avec un code déjà éprouvé.
   - **Les modules**, un par fonction du cahier des charges :
     - assemblage de la requête et partie servie ;
     - garde de motifs au dernier point avant l'envoi (arrêt n° 16) ;
     - routage par rôle et par clé ;
     - portier et ses classes ;
     - juges joués pour information ;
     - registre servi et quarantaine (arrêts n° 17 à 19) ;
     - tirage des cases et de la clé n° 30 ;
     - journal ;
     - mesures M1 à M7, C1 et I1 ;
     - épreuve des témoins plantés ;
     - sondes de refus ;
     - arrêts n° 11, n° 12 étendu (avec l'artefact « envoi adressé à Rigaud »), n° 14 et n° 27.

     Chacun avec la ligne du texte qui l'impose.
   - **Les interfaces** : les entrées et sorties de chaque module, ce qui est scellé et par qui, et l'identifiant neutre des témoins, que le gabarit attend de l'additif du véhicule.
   - **Les épreuves** : pour chaque garde et chaque arrêt, le cas sain et l'artefact ; l'essai à blanc de bout en bout en moteur simulé ; la mesure des consignes sans appel.
   - **Le découpage en mandats de code**, par lots qu'un développeur O peut écrire et qu'un vérificateur S peut vérifier, avec l'ordre et les dépendances.
   - **Le calendrier** : une estimation honnête des heures de travail par lot, sans appel. Elle servira à la demande d'échéance de GO-2026-11-20-67, que la mère pose à Lazar.
   - **Ce que la lettre ne fixe pas** : les questions que l'inventaire laisse ouvertes, reprises une à une, avec une proposition marquée et jamais tranchée.
2. **`rapport-concepteur-vehicule-v1.md`** : les pièces lues avec leurs empreintes, et les décisions qui reviennent à la mère ou à Lazar, au format : décision en une phrase ; enjeu ; deux ou trois options ; recommandation et confiance ; défaut sous 48 heures.
3. Une table d'empreintes.

Ton dossier : `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/concepteur-vehicule-nouvelles-attaques/`. Chaque fichier a son compagnon (`env -C DOSSIER sha256sum F`, redirigé par `>` vers `DOSSIER/F.sha256`).

## Interdits

Voir en tête. Jamais de heredoc ni de code en ligne passé à un interpréteur. Aucun code écrit pour être lancé, aucun lancement, aucun appel à un fournisseur, aucune clé lue ni nommée, aucune dépense. Aucune écriture dans un dépôt, aucun commit. Rien sous `archives-reponses-modeles/`, rien sous `/root/.claude/`. Jamais le nom d'une commande d'arrêt ou de recherche de processus. Aucune publication. Aucun identifiant de modèle. Aucune recette. Au premier refus de permission, de classifieur ou de garde : arrête-toi et dis-le.
