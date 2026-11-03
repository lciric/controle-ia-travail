# Spécification de la course d'idéation sur la question 1 de Heimersheim — v1 (pour session-depot et sa fille)

Session conv-audit (Claude), 3 novembre 2026, 06:48 UTC (`date -u`). Mots de Lazar, chez conv-audit : 07:17 Paris « lançons au collisionneur la question de Heimersheim » ; 07:23 « je veux que le collisionneur avec son bisociateur trouve des idées originales à partir de la question même de Heimersheim » ; 07:40 « je veux lancer une course d'idéation carrément sur la question de Heimersheim » ; 07:45 « pas de plafond » (en réponse à ma demande de plafond pour le GO). Lecture retenue : **une course de l'organisme d'idéation** (proposeurs, aiguilleur, mémoire, juges, **bisociateur**), une génération, sur la question servie ci-dessous. Le collisionneur v9 n'a pas de bisociateur (vérifié : aucune occurrence dans `collisionneur_v9.py`) ; le bisociateur est l'étage 5 de l'organisme (`pole/bisociateur_v5[3-5].py`, course v56).

## 1. Objet

| Élément | Valeur |
|---|---|
| Instrument | orchestrateur de l'organisme, course v56 (celle du second tour réel du 1er novembre), **planche de bisociation activée** (première exécution réelle des trois bras ; jamais joués hors essais : à déclarer dans le manifeste et dans toute lecture) |
| Question servie | `brouillons/ideation-heimersheim-v1/question-ideation-heimersheim-v1.md` (empreinte dans son compagnon) |
| Pièce servie | `brouillons/ideation-heimersheim-v1/piece-etat-de-l-art-pilotage-conscience-evaluation-v1.md` (sources publiques seulement ; aucun texte privé, aucune réponse de candidature) |
| Générations | 1 |
| Proposeurs (espèces) | A Fable 5.1 (`claude-fable-5-1`), B Opus 5.5 (`claude-opus-5-5`), E Astra (`gpt-6-astra`, commande 8807). **Exclus pour ce tour** : C Argon (relais 8805 tenu par A1-v3, un appel à la fois : jamais en même temps) ; D Kimi (Moonshot non rechargé ; 5 appels réussis sur 621 à A1). Si Lazar recharge Moonshot avant le lancement, D entre ; Argon n'entre qu'après la fin d'A1-v3 (rapport de la fille). |
| Fiches par proposeur | 8 par passe (borne [1, 12] ; 6 au second tour réel ; plus ici parce qu'on cherche des idées, pas un classement) |
| Juges | comme au second tour réel, familles disponibles (Claude et Astra), consigne figée inchangée ; **classement rapporté avec sa réserve** (plafond des juges au second tour : 11 sur 12 « notables », κ = 0 ; les juges v2 ne sont pas scellables, B8 et B9) |
| Témoins plantés | ceux du second tour réel, réutilisés tels quels (écrits par un tiers ; hors thème : déclaré ; ils ne servent qu'à lire les juges, pas les idées) |
| Aiguilleur, mémoire, caviardage, garde lexicale | inchangés |
| Moissonneur | non appelé pendant la course (nouveauté non cherchée, marquée « non cherché ») ; une moisson séparée après lecture, si Lazar la demande |
| Sortie | dossier neuf chez la fille, hors clone ; manifeste de départ scellé avant le premier appel ; **sortie scellée avant toute lecture** ; copie sur le canal (fiches, mariages, classement, lectures des témoins, journal des coûts), sans aucune clé ni identifiant de clé |

## 2. Dépense

- Lazar : « pas de plafond ». Le noyau exige un `budget.plafond_usd` : **plafond technique 60 USD** (garde contre une boucle, pas un plafond de Lazar), `arret_etape_usd` en proportion ; à relever sur son mot si le devis le dépasse.
- Attendu (calcul, à remplacer par le devis de la course à blanc) : second tour réel 62 appels pour 1,47 USD avec Kimi et Argon ; ici trois espèces plus chères (Opus 4 / 20, Fable 10 / 50, Astra 10 / 50 supposé) et le bisociateur en plus : **10 à 25 USD attendus**, pire cas ≈ 45.
- Devis chez session-depot après course à blanc (`mode_a_blanc_v59` ou l'équivalent v56), cité dans la ligne de GO, **avant** le premier appel réel.

## 3. Ce que la fille fait, dans l'ordre

1. Configuration neuve, nom neuf (R12), dérivée de celle du second tour réel : question, pièce, proposeurs, juges, témoins, dossier de sortie, plafonds ; empreintes des pièces dans `pieces` ; `verifier_configuration_generation_v56` passe.
2. Appels de contrôle par modèle (statut ok, coût > 0, modèle servi égal au modèle demandé) ; A1-v3 n'est pas touché ; aucun appel à Argon.
3. Course à blanc ; devis ; ligne de GO inscrite au registre sur le mot de Lazar (texte et heures ci-dessus) ; commande exacte au canal.
4. Lancement réel ; manifeste de départ ; sortie scellée ; copie au canal ; rapport (nombre de fiches, refus de l'aiguilleur, quarantaines, mariages par bras, coûts par espèce).

## 4. Lecture

- Lazar lit les fiches et les mariages comme matière à sa réflexion. Règle du mentor : la réponse doit être écrite par lui et ne pas suivre de près un texte écrit par une machine. Risque dit une fois : une liste de « raisons d'échec » produite par des modèles est proche d'une réponse écrite par une machine ; l'usage le plus sûr de la sortie est la partie **expériences et épreuves** (ce qu'il voudrait voir), et la mise à l'épreuve de ses trois raisons.
- Un lecteur neuf de conv-audit relit la sortie scellée : redites avec la pièce servie, fiches hors niveau méthode, chiffres inventés (toute fiche qui cite un chiffre absent de la pièce est marquée).
- Rien n'entre dans la candidature sans vérification en source (R7).
