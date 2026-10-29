# Course d'idéation de l'organisme — devis v7 quater (après la relecture CL5 de la v37 : plafonds cohérents, ordre de lancement)

Lignée conv-audit (instance de reprise, Fable 5.1), 29 octobre 2026, relevé `date -u` **00:17 UTC**. **Remplace le devis
v7 ter** (gardé, R12) ; le reste des v2 à v7 ter vaut. Code : **v38** (321 essais). Plafond général **49 USD inchangé**,
accordé par Lazar (« ok 49 », GO-2026-10-28-14 étendue, R-675 chez session-depot).

1. **Plafonds par session cohérents avec le total** (CL37-03) : proposeur Opus **5**, Fable **9,3** ; juge Opus **4**, Fable **7** ;
   contrôles 0,2 × 2. Somme Claude = 0,4 + 2 × (5 + 9,3) + 4 + 7 = **40,0** ≤ 40 ; le cœur la vérifie au départ et refuse
   au-delà (`--tolerer-somme-plafonds` sinon). Argon : contrôle à la taille réelle **≤ 2,5**, proposeur **2,5** par passe, juge
   **3,5**, contrôle du bras 0,2 : somme **8,9** ≤ 9.
2. **Relais** : `--plafond-usd 40 --reserve-par-appel 4` (sessions séquentielles ; un excédent du dernier appel reste
   journalisé) ; le lanceur lit `/relais/etat` et refuse si plafond − réserve < 40 − 4.
3. **Délais** : `--delai-session-s 3600`, `--delai-commande-s 1800` (défauts de la v38 ; CL37-08).
4. **Ordre de lancement** (manquait au v7 bis) : (1) relecture v37 → v38 ; (2) pièces : liste blanche **v4** (39 fichiers ;
   v5 avec PACE si prête), `--taille-max-pieces 750000` ; témoins du tiers ; attestation du matériau ; (3) machine, clé
   Anthropic tournée, relais sous `env -i` avec la réserve 4 ; commande d'Argon sous un utilisateur distinct avec son
   propre délai ; (4) **contrôle d'Argon à la taille réelle** (fait par le lanceur avant toute passe : la consigne de contrôle
   suivie des pièces, ≈ 670 000 caractères, rôle proposeur, ≤ 2,5 USD) ; (5) course ; (6) lecture humaine ; attestation ;
   (7) bras d'Argon (au plus trois tentatives, coûts imputés) ; (8) versement scellé ; contre-lecture ; décision de Lazar.
5. **Comptage en jetons** (CL37-06) : avant le barème final, session-depot compte les jetons des consignes scellées de la
   course simulée (liste v4) avec le découpeur des modèles ; si le ratio dépasse 4 caractères par jeton d'un tiers, les
   plafonds par session sont relus avant le GO.
