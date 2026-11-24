# Notice de l'amorce du rejeu des activations du saboteur, voie (A) — v1

Pièce d'instrument (classe B), écrite le 2026-11-24 par l'exécutante v8 (Opus 5.5, côté exposé). Accord : GO-2026-11-24-06 (11,00 USD) ; devis v2 (`devis-passe-activations-saboteur-voie-a-v2.md`, 9a4a794c…). Le code de la passe (côté moniteurs) n'a pas été ouvert : sa ligne de commande vient de sa notice v6 (`docs/notes/barreau8-cote-moniteurs-sorties-v1/notice-passe-recalcul-v6.md`, lignes 25 à 61).

## Pièces
- Code : `src/controle_ia/rejeu_activations_voie_a_v1.py` (bibliothèque standard seulement ; tourne dans la session et sur la machine).
- Essais : `tests/test_rejeu_activations_voie_a_v1.py` (52 essais, chaque garde sur un cas sain et un faux cas ; machine simulée de bout en bout, passe remplacée par un bouchon qui écrit des zéros aux noms de la notice v6).
- Contre-lecture (classe B, agent neuf Sonnet) : `contre-lecture-amorce-rejeu-v1.md` (à corriger : 3 bloquants, 7 majeurs, 7 moyens), vérification des corrections `contre-lecture-amorce-rejeu-v1-verification-1.md` (tout fermé sauf un défaut neuf, corrigé ensuite ; voir la passation).
- Ordre de lancement à remplir : `ordre-lancement-rejeu-voie-a-v1-gabarit.json`. Il porte encore des valeurs « A_FIXER » (entropie du texte scellé, extrait du côté exposé, entrées de la course selon l'additif 2) : le code refuse de partir tant qu'il en reste une.

## Gardes, et leur essai (R5)
| garde | où | cas sain | faux cas |
|---|---|---|---|
| filtre bloquant des offres (devis § 2.3) | `motifs_offre`, `choisir_offre` | offres 29019348 et 59588540 du relevé scellé | 60992141 (stockage), 61733634 (prix, fiabilité), A100 de 40 Go, neuf bornes mutées une à une |
| accord (crochet du dépôt appelé tel quel, plafond exact 11 USD) | `verifier_go` | registre « calcul » | type « dépense », plafond 15, hors validité, autre identifiant |
| horloge 4,5 h et dépense tout compris coupée à 9,60 USD (externe, R10) | `decision_surveillance`, `surveiller` | 1 h, 1,17 USD/h | 4,5 h ; crédit lu en baisse de 9,60 ; prix illisible ; destruction effective après coupure |
| minuterie de la machine (destruction dans un bloc final, quoi qu'il arrive) : passe coupée par son PID 30 min avant l'échéance, versement, destruction par l'identifiant à l'échéance ; vivante avant tout départ ; minuterie de secours du script de démarrage, avant le clonage | `minuterie`, `armer_minuterie`, `script_de_demarrage` | — | passe lente coupée, versée, machine détruite ; PID illisible ; minuterie morte ou clé d'instance absente : refus de départ ; intouchable refusée |
| écriture : sonde écrite, relue, retirée ; place libre | `garde_ecriture` | dossier inscriptible | dossier impossible, place insuffisante |
| refus du départ si les activations ne s'écrivent pas : vérification des entrées et essai à blanc en code 0, rapport de l'essai nommant les trois archives d'activité brute | `garde_rapport_essai`, `Machine.executer` | rapport complet | rapport sans activité brute, vérification en échec : la passe ne part pas |
| activations écrites après la passe : chaque archive décrite, chaque morceau présent à sa taille et à son compagnon, fichiers de fin présents, aucune trace d'arrêt | `garde_activations` | livraison complète | code 1, couche 15 absente, morceau altéré, morceau manquant, bordereau absent, trace d'arrêt |
| entrées tirées et assemblées à leurs compagnons | `Machine.tirer` | trois morceaux dans l'ordre | ordre des morceaux faussé : refus de départ |
| arbre propre avant la passe | `arbre_propre` | — | fichiers non suivis : refus de départ (vu à l'essai) |
| branche de versement neuve (R12) | `Machine.executer` | branche absente | branche existante : refus, versement sous un nom neuf |
| aucun secret pour la passe ; secrets masqués au journal ; fichier portant un secret retiré du versement | `env_sans_secret`, `Journal`, `secret_dans` | la passe écrit « aucun secret » | — |
| redémarrage du conteneur : rien n'est relancé | `Machine.executer` | — | second démarrage : versement de l'état seulement |
| rapatriement prouvé : clone séparé, commit annoncé, inventaire scellé, taille et empreinte de chaque fichier, compagnons, aucun fichier de trop | `rapatrier` | versement intact | fichier altéré après poussée |
| destruction par l'identifiant de la fiche seulement, étiquette exacte, rapatriement attesté (y compris pour un refus de départ) ou coupure d'horloge ou de dépense, absence relue deux fois | `detruire` | instance de la fiche | intouchable, autre identifiant, sans attestation, attestation « non », raison hors liste, étiquette étrangère |
| surveillance : relevé vide ou en erreur jamais pris pour une absence ; horloge jugée sans relevé ; coupure retentée, puis destruction sans relevé après trois échecs ; fiche sans identifiant résolue par l'étiquette ou refusée | `surveiller`, `resoudre_fiche` | — | relevé vide une fois, relevés en erreur, destruction refusée une fois, fiche sans identifiant |
| création : fiche provisoire avant la création ; création incertaine retrouvée par l'étiquette ; fiche, étiquette, mot de feu | `creer` | création simulée | mot de feu inexact, fiche existante, étiquette prise, création incertaine |
| filet : toute erreur imprévue finit par un versement et l'arrêt | `Machine.executer` | — | erreur d'entrée-sortie au tirage |
| fichier de plus de 95 Mo coupé en morceaux de 50 Mo décrits avant la poussée | `Machine.verser` | — | archive entière laissée dans la sortie |

Ce que les essais ne voient pas : la vraie passe, la carte, le vrai téléchargement du modèle, la vraie poussée vers GitHub, l'interface réelle de Vast (création, arrêt, destruction), la durée.

## Phase 2 (seulement sur « feu, additif 2 scellé » de la mère)
Préalables à lever par la mère et le côté moniteurs avant le feu :
1. **Le crochet refuse aujourd'hui toute création sous GO-2026-11-24-06** : la ligne est de type « dépense », le crochet `.claude/hooks/garde_calcul.py` exige « calcul » (essayé sur un registre de copie). Il faut une ligne de type « calcul » au même identifiant ou une décision de la mère.
2. **La garde P0 de la passe exige la ligne d'accord portant l'empreinte entière (64 caractères) du devis** (notice v6, « Entrées attendues ») ; la ligne GO-2026-11-24-06 ne porte que « 9a4a794c… ». À vérifier côté moniteurs avant le bordereau du code.
3. L'ordre de lancement rempli (valeurs « A_FIXER » remplacées selon l'additif 2 scellé), contre-lu, scellé, committé au commit de lancement, avec l'extrait du côté exposé, le registre propre (`CODE-PASSE-IIB`), le bordereau du code et ce module.

Suite des gestes (bloc-notes `S`, outil `S/vast11/bin/vastai` 1.11.0) :
1. Recherche d'offres en lecture seule vers `S/offres.json`, puis `creer --verifier-seulement`, puis `creer` (la commande cite `GO_ID=GO-2026-11-24-06` ; le code appelle le crochet lui-même avant toute création ; fiche écrite).
2. `surveiller --fiche …` détaché (`setsid nohup`), son PID consigné au registre des arrêts ; relevés réguliers par la session.
3. À la ligne « FIN » du journal de l'amorce : `rapatrier --commit-attendu <commit> --dossier <dossier neuf>` (commit obligatoire) (aucun fichier de scores ouvert au-delà du hachage).
4. `detruire --raison rapatriement-verifie --attestation …` ; registre des arrêts et des dépenses ; passation.

## Réserves
- La dépense « lue » est la baisse du crédit du compte : une dépense parallèle d'une autre session sur le même compte la grossit et peut couper tôt (sens prudent).
- La machine se met elle-même à l'arrêt après son versement : si la session pilote meurt, seul le stockage reste facturé (≈ 0,03 USD/h) jusqu'à la destruction par la routine de reprise.
- Restent de la contre-lecture, acceptés : la minuterie de la machine ne relit pas sa destruction (la surveillance externe le fait) ; la poussée s'arrête au premier lot refusé après cinq essais (ce qui précède est poussé) ; une passe déjà finie mais non récoltée fait attendre la coupure 60 s sans effet ; les secrets de création passent par la ligne de commande d'un sous-processus de la session (forme du dépôt).
- Une coupure de dépense externe détruit la machine sans attendre le versement ; sous le filtre du devis, la dépense ne peut atteindre 9,60 USD avant 4,5 h (8,21 USD au plus).
