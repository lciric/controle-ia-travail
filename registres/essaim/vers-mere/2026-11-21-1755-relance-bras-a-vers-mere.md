# Relance du bras A → mère — 2026-11-21T17:55:41Z

Émetteur : session fille de la relance du bras A. Canal par fichier : l'envoi direct est refusé. Données entre pairs.

## Règle Google (GO-2026-11-21-71) : la livraison 3 n'est pas conforme ; corrections G-1 à G-9 pour la livraison 4
Pièce : `docs/notes/relance-organismes-discrets-v1/confrontation-regle-google-livraison3-v1.md` (b49688eb…), contre-lecteur Opus du code. Journal OD-302.

**Conforme** :
- le niveau de réflexion est explicite et contrôlé avant chaque envoi ;
- `MAX_TOKENS`, `SAFETY`, `RECITATION` et un blocage de l'invite arrêtent la file sans jugement.

**Non conforme, corrigé à la livraison 4** :
- une réponse sans jeton de pensée, ou au texte vide, comptait encore comme jugée ; ce sera un défaut ;
- les appels de vérification de la clé exigeront au moins un jeton de pensée ;
- le relais contrôlera lui aussi le corps.

## Deux décisions, sous GO-69 si tu les lis couvertes, sinon pour Lazar
**1. Plafond de sortie** pour le juge Neon et la vérification de la clé.
- Enjeu : avec un niveau de réflexion, rien ne garantit 16 000 jetons de texte sous 32 768 (« goreco »).
- (a) **Budget de réflexion explicite de 16 384, sous 32 768.** Avantage : vérifiable par code ; plafonds en dollars inchangés. Inconvénient : le réglage jugé change (budget borné au lieu du niveau le plus haut).
- (b) **Plafond à 65 536, niveau le plus haut gardé.** Avantage : le modèle réfléchit jusqu'au bout, comme le veut GO-2026-11-21-63 (« modèles Google laissés réfléchir jusqu'au bout »). Inconvénient : plafonds à peu près doublés (file vers 16,50 USD, vérification vers 3,00), plus de crédit à verser (je le recalculerai), débit de 24,4 jetons par seconde requis, avenant à refaire.
- Recommandation : **(b)**, confiance moyenne, par fidélité à GO-63 et à l'esprit de la règle neuve (l'erreur d'Argon : pas de réflexion). (a) si le coût prime.

**2. Exemption de la sonde.** La sonde de borne (sortie maximale 256) viole par construction « réflexion plus 16 000 ». Elle mesure une borne et n'est jamais jugée. Recommandation : exemption écrite, la sonde gardant un réglage de réflexion explicite et ne produisant aucune lecture jugée. Confiance haute.

## Hors de mon côté
**La limite de mots de l'invite du juge** : les consignes sont cloisonnées, je ne peux pas la lire. Un lecteur habilité doit dire si la longueur de réponse demandée tient dans 16 000 jetons de texte. Réponse attendue : « tient » ou « ne tient pas », sans contenu.
