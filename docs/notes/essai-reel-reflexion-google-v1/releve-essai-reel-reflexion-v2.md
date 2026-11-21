# Relevé de l'essai réel de la réflexion des modèles de Google, version 2

Heure (date -u) : 2026-11-21T19:27:03Z (envois de 19:25:50Z à 19:26:55Z). Opérateur : Claude Opus 5.5. Accords :
GO-2026-11-21-69 (dépense sur devis, plafond 0,50 USD pour l'ensemble) et GO-2026-11-21-71 (vérifier les réglages).
Programme : `essai_reel_reflexion_v2.py` ; compteurs bruts : `releves-essai-reel-reflexion-v2.json` (même dossier,
empreintes compagnons). Pièce de travail. Version 1 inchangée (R12).

## Verdict
Les trois modèles réfléchissent au réglage prescrit, en flux : Gemini 4 Argon et Gemini 4 Carbon au niveau « high »,
Gemini 4 Neon au niveau « xhigh », tous en fin STOP avec des jetons de pensée comptés. Dépense estimée : 0,106 USD,
sous le plafond de 0,50.

## Ce qui a changé depuis la version 1 (tranché par la mère)
1. includeThoughts vrai. Seuls les compteurs sont versés, jamais le texte des pensées ni la réponse. Le programme ne
   garde que des nombres de caractères.
2. Envoi en flux (streamGenerateContent, alt=sse), comme le collisionneur, avec maxOutputTokens 65 536 pour les trois
   modèles. La garde commune `src/controle_ia/garde_google_v2.py` est appelée en mode « flux ».

Réglage inchangé : question « Combien de nombres premiers y a-t-il entre 100 et 150 ? Donne seulement le nombre. » ;
thinkingLevel « high » pour Argon et Carbon, « xhigh » pour Neon ; aucun thinkingBudget. La provision passée à la garde
est celle du catalogue du collisionneur v9-v8b (Argon 16 384, Carbon 49 152, Neon 32 768).

Ajout de l'opérateur, déclaré : un seul envoi à 65 536 jetons de sortie coûterait au pire 1,31 USD pour Argon et pour
Carbon, et 0,98 USD pour Neon. Chacun dépasse donc à lui seul le plafond. Le flux a été lu avec une coupure de dépense :
chaque modèle recevait une part, égale au reste du plafond multiplié par 0,9 puis divisé par le nombre de modèles
restants (0,15, 0,21 et 0,38 USD). La connexion devait être fermée si le coût estimé en cours de flux atteignait cette
part. La coupure n'a pas servi.

## Gardes avant l'envoi
- Garde commune en mode « flux » : aucun problème pour les trois corps.
- Garde de motifs (aucun nom de personne, de session ni de dépôt dans le corps) : passée pour les trois.

## Relevés (dernier morceau du flux)
| Modèle | Niveau | Code HTTP | Motif de fin | Jetons de pensée | Jetons de texte | Jetons d'entrée | Coût estimé (USD) | Verdict |
|---|---|---|---|---|---|---|---|---|
| Gemini 4 Argon (gemini-4-argon) | high | 200 | STOP | 1 212 | 6 | 58 | 0,024592 | réfléchit |
| Gemini 4 Carbon (gemini-4-carbon) | high | 200 | STOP | 2 462 | 6 | 58 | 0,049592 | réfléchit |
| Gemini 4 Neon (gemini-4-neon) | xhigh | 200 | STOP | 2 131 | 6 | 58 | 0,032229 | réfléchit |

Pour chaque modèle, des parties de pensée ont été reçues en flux, ainsi qu'une réponse non vide de 2 caractères. Leur
texte n'a pas été lu ni versé. Caractères de pensée reçus : Argon 501, Carbon 1 727, Neon 1 336.

Aucun code 400 n'a été reçu, donc aucune reprise au niveau inférieur. Aucune coupure de dépense ni erreur de flux. Coût
total estimé : 0,106413 USD, aux prix du catalogue (entrée et sortie, pensées comptées comme sortie). Ce coût n'est pas
relevé sur la facture.

## Réserves
- Une seule question facile, un seul envoi par modèle : l'essai montre que le réglage produit des pensées. Il ne dit
  rien de leur quantité sur des tâches longues.
- Une sortie de 65 536 jetons est permise par la garde en flux, mais elle n'a pas été atteinte (au plus 2 468 jetons de
  sortie). La limite réelle d'Argon en flux au-delà de 32 768 reste donc sans épreuve.
