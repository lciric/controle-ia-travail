# Relevé de l'essai réel de la réflexion des modèles de Google, version 1

Heure (date -u) : 2026-11-21T19:23:31Z. Opérateur : Claude Opus 5.5. Accords : GO-2026-11-21-69 (dépense sur devis,
plafond 0,50 USD) et GO-2026-11-21-71 (vérifier les réglages). Programme : `essai_reel_reflexion_v1.py` (même dossier,
empreinte compagnon). Pièce de travail.

## Verdict
Aucun envoi : la garde commune des réglages de Google (`src/controle_ia/garde_google_v2.py`, mode « non diffusé »)
refuse les trois corps prescrits. Dépense : 0,00 USD. La question « le réglage de réflexion produit-il des pensées ? »
reste sans réponse mesurée.

## Réglages prescrits (identiques pour les trois, sauf le niveau)
Envoi generateContent non diffusé ; question « Combien de nombres premiers y a-t-il entre 100 et 150 ? Donne seulement le
nombre. » ; thinkingConfig.thinkingLevel « high » (Gemini 4 Argon, gemini-4-argon ; Gemini 4 Carbon, gemini-4-carbon) et
« xhigh » (Gemini 4 Neon, gemini-4-neon) ; aucun thinkingBudget ; includeThoughts faux ; maxOutputTokens 65 536.
Provision passée à la garde : celle du catalogue du collisionneur v9-v8b (Argon 16 384, Carbon 49 152, Neon 32 768).
Garde de motifs (aucun nom de personne, de session ni de dépôt dans le corps) : passée pour les trois.

## Relevés
| Modèle | Niveau | Envoyé | Code HTTP | Motif de fin | Jetons de pensée | Jetons de texte | Jetons d'entrée | Coût | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| Gemini 4 Argon | high | non | sans objet | sans objet | sans objet | sans objet | sans objet | 0 | défaut : refusé par la garde |
| Gemini 4 Carbon | high | non | sans objet | sans objet | sans objet | sans objet | sans objet | 0 | défaut : refusé par la garde |
| Gemini 4 Neon | xhigh | non | sans objet | sans objet | sans objet | sans objet | sans objet | 0 | défaut : refusé par la garde |

Motifs de refus de la garde :
- Argon et Carbon : « includeThoughts non vrai (les pensées ne seraient pas lues en retour) » ; « maxOutputTokens 65536
  au-delà de la limite de [l'espèce] en non_diffuse (32768) ».
- Neon : « includeThoughts non vrai ».

Aucune reprise au niveau inférieur : aucun code 400 reçu (rien n'est parti). Coût total : 0,00 USD.

## Pour la mère (décision à prendre, non tranchée ici)
L'ordre contredit la garde sur deux points : (1) includeThoughts faux, alors que la garde exige vrai ; (2) 65 536 en
non diffusé pour Argon et Carbon, alors que la garde, sur la page versée (ligne 931), les borne à 32 768 hors flux.
Pistes : includeThoughts vrai (les pensées ne seraient pas versées, seuls les compteurs) et 32 768 pour Argon et Carbon
en non diffusé ; ou l'envoi en flux à 65 536 ; ou une dérogation écrite à la garde. Le programme est prêt à rejouer.
