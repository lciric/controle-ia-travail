# Voie « abonnement » pour les cellules Claude du collisionneur (Fable et Opus) : note courte

Écrit à 2026-11-22T07:57:54Z (`date -u`). Classe B, Opus 5.5, session des collisionneurs, sur la demande de la mère (07:55Z) après GO-2026-11-22-32 (point 3 : part Claude sous l'abonnement Ultra, au risque de Lazar, sans contournement). Aucun appel fait ; rien ne bascule avant le feu de la mère. Faits sur l'outil : `claude --help` de la version 2.1.330 installée ici, lu seulement.

## 1. Faisabilité par `claude -p`
- **Oui, avec un adaptateur** à la place de `appeler_anthropic` : un sous-processus `claude -p --model claude-fable-5-2|claude-opus-5-5 --effort … --output-format json --tools "" --no-session-persistence --setting-sources "" --system-prompt …`, l'invite de la cellule sur l'entrée standard. Options présentes dans l'aide : `--model`, `--effort` (low à max), `--output-format json`, `--tools ""` (aucun outil), `--system-prompt` (remplace celui de Claude Code), `--no-session-persistence`, `--setting-sources`, `--fallback-model` (à **ne pas** donner : un repli de modèle est interdit sans GO).
- **Ce qui ne se règle pas comme à l'interface payante** :
  - plafond de sortie (`max_tokens`) : aucune option ; la v8d envoie des plafonds par espèce (Opus 64 000) et relance au plafond relevé : la règle de relance ne s'applique plus telle quelle ;
  - réflexion : adaptative, au réglage de Claude Code ; seul l'effort se donne ;
  - invite système : `--system-prompt` la remplace, mais rien ne garantit que Claude Code n'ajoute rien d'autre au contexte servi ; à mesurer sur une cellule témoin avant toute bascule ;
  - comptage avant envoi : la garde de la v8d compte les jetons par l'interface de comptage d'Anthropic (clé) ; sans clé, il faut garder la clé pour ce seul comptage (gratuit), ou passer à l'estimation prudente (2 caractères par jeton, comme Kimi).
- Mode non interactif compris dans la décision de Lazar ; sans compte multiplié, client modifié ni jeton recopié : l'adaptateur appelle le client tel qu'il est installé, connecté au compte de Lazar.

## 2. Consignation
- `--output-format json` rend un résultat unique ; à consigner tel quel, scellé, comme la réponse d'un essai : texte, `usage` (jetons d'entrée, de sortie, de cache), décompte par modèle servi (`modelUsage`), coût théorique, identifiant de session, durée, raison d'arrêt. **Modèle servi** : lu dans le décompte par modèle ; tout modèle autre que celui demandé (ou un second modèle, de repli) = défaut de la cellule, comme `modele_conforme` aujourd'hui. À vérifier sur une cellule témoin : que ces champs existent bien dans la version installée, et que le texte rendu est complet (marqueur `FIN-DE-CELLULE`).
- Réglages à journaliser par essai : voie (« abonnement »), version du client, modèle, effort, invite système (empreinte), outils (aucun), et l'empreinte de l'invite de la cellule, comme aujourd'hui.

## 3. Effet des quotas sur l'appariement
- Les limites de l'abonnement (fenêtres de quelques heures et plafond hebdomadaire) arrêtent un dossier au milieu d'un tour : la cellule en vol échoue, les autres attendent. Règle proposée : un refus de quota est un échec sans envoi (comme le 429), la cellule est reprise plus tard **sur la même voie** ; jamais de passage d'une cellule à l'interface payante au milieu d'un dossier.
- **Appariement** : plafond de sortie, réflexion et contexte servi diffèrent entre les deux voies. Les cellules Claude d'un dossier, et les dossiers d'une même comparaison (essaim contre isolé, pièce 2 ; huit questions balisées, pièce 1), doivent être sur **la même voie** ; la voie est une variable du dossier, scellée dans sa composition, comme les espèces. Les dossiers déjà joués (interface payante) ne s'apparient pas à des dossiers de la voie abonnement sans le dire.
- **Fable** : sa limite dans Claude Code court jusqu'au 2026-11-24T05:00Z ; sous l'abonnement, ses cellules du collisionneur puiseraient dans le même quota que les pièces décisives que Fable conçoit (« Économie de Fable »). À trancher par la mère et Lazar : Opus seul sur l'abonnement, ou les deux.

## 4. Gain chiffré par dossier (journaux des dossiers finis, champ `cout_usd` seul)
| dossier | total | part Claude (Fable + Opus) |
|---|---|---|
| antériorité | 15,52 | 6,12 (39 %) |
| dérive v2 | 14,37 | 8,14 (57 %) |
| dopamine | 14,45 | 8,72 (60 %) |
| mathématiques | 21,60 | 11,38 (53 %) |
| percée | 15,21 | 8,63 (57 %) |
| seuil des moniteurs | 14,86 | 8,71 (59 %) |
| fusionnée | 14,39 | 9,17 (64 %) |
| coercition (protocole X) | 11,99 | 6,80 (57 %) |

Gain par dossier : **6,1 à 11,4 USD, médiane 8,7 USD** (environ 57 % du dossier), dont Fable 3,9 à 9,3 USD et Opus 1,8 à 3,7 USD. Sur les sept protocoles X qui restent (plafond 45 USD chacun, environ 12 à 15 USD réels), environ 50 à 60 USD. Pilote de l'essaim : la part Claude est du même ordre (Fable et Opus portent environ 45 % du pire au devis de la v5). Ce sont des gains d'argent ; ils se paient en quota de Lazar et en temps (refus de quota).

## 5. Avant toute bascule (proposition)
Un adaptateur (classe B, contre-lu), une cellule témoin par modèle sur un texte sain (consignation complète vérifiée, modèle servi, absence d'ajout au contexte, sortie entière), une version du collisionneur qui porte la voie dans la composition scellée ; feu de la mère.
