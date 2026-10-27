# Passation de la lignée « conv-audit » — 27 octobre 2026 — v7 (intermédiaire, fin d'après-midi)

Écrite par l'instance du 27 octobre (session `https://claude.ai/code/session_01XJ6MgqzevAiJX5udWW4j4M`, servie par Fable
5.1 depuis 14:05 heure de Paris), le 2026-10-27 à 14:09 UTC (heure lue sur `date -u` : 14:07:54, dans la commande qui
précède). **Les v2 (§ 1), v5 (§ 1, § 2) et v6 (§ 0 à § 3) valent mot pour mot** ; ceci n'ajoute que ce qui s'est passé
depuis la v6 (13:46 UTC). Tout est au commit qui porte ce fichier, sur `canal/conv-audit-n04`.

## 0. L'essentiel (verdict)

1. **Première course du pôle sur données réelles** (couche 1 en simulation d'agents, zéro dépense, 21 s ; orchestrateur
   v7 pièces 1 à 3 : monde sur banque, nul informé, sans urne ; banque = pilote T0.5, 120 épisodes, 13 moniteurs ;
   lecture `envois/pole-scientifique-automatique-v1/demonstration-couche1-v7/lecture-couche1-v7-v1.md`, `e21f8611…`) :
   une promue sur 104 en nul aveugle, zéro avec le nul informé (« que du connu »), zéro avec l'urne ; aucun témoin faux
   promu ; **témoins vrais éliminés : pas de dents** (banque trop petite) ; **leçon** : une promotion isolée n'est pas une
   découverte (multiplicité) → option e-BH codée (`--multiplicite e-bh`), défaut à décider (recommandé e-bh ; défaut
   appliqué le 29 octobre vers 14:05 UTC si Lazar ne dit rien).
2. **Programme de conception de l'organisme v2** (`programme-conception-organisme-v2.md`, `353515ff…`) : pari de signe,
   règle de multiplicité, témoins sans agents, signal « pas de dents », proposeur ; distinct du programme v2 du fonds.
3. **Décisions de Lazar depuis la v6** (heure de Paris) : 14:48 et 14:57 « parfait » (tour du collisionneur sur les
   questions à fort impact ; proposeur qui génère des questions ; v3 des questions après la couche 1) ; 15:05 pari de
   signe inscrit au programme de l'organisme ; il choisira une date dans le calendrier du fonds (scénarios donnés : deux
   à trois semaines recommandées) ; courriel au responsable du fonds rédigé dans la session (Lazar envoie ; rien de
   versé) ; parler de l'organisme au fonds comme instrument, pas comme produit.
4. **En attente de Lazar** : plafond de (a) (50 USD proposé) ; règle de multiplicité par défaut ; question de la couche 1
   (H2 proposé) ; tours du collisionneur (proposeur ; questions) ; décision n° 1 (produit strict, défaut 29 octobre
   10:34 UTC).

## 1. Reste à faire (ordre)

1. Corrections immédiates (programme de conception v2, § 6) : témoins jugés sans agents sur un monde à banque ; signal
   « pas de dents » automatique ; trait redondant retiré de la banque T0.5 (`log_jetons_total` ≡ `jetons_par_action_moyenne`).
2. v7, pièce 4 : le **proposeur** (rôle, gabarit de fiche, catalogue de stratégies, enfichable) ; pièce 5 : moissonneur
   par le relais ; pièce 6 : canaux de texte, lignée, aptitude = preuve ; **pari de signe** (second type d'engagement,
   contrôles fatals en simulation).
3. Lire la sortie de (a) quand session-depot l'aura versée ; devis de la couche 1 avec vrais agents.
4. Préparer la couche 2 (T0.6, T0.7, T0.8 : banque avec sabotage) : préenregistrement (R1 : décisif), devis.
5. Journal : entrée de fin d'après-midi (faite dans le même commit que ce fichier, si le temps le permet ; sinon à
   écrire d'abord à la reprise).

## 2. Réserves

- Les résultats de la couche 1 sont exploratoires, non opposables ; « pas de dents » : rien à conclure sur les juges.
- La banque T0.5 contient des épisodes dépendants (même tâche) : limite déclarée dans la banque ; la validité du pari
  suppose que le nul contienne la vraie loi, ce que la dépendance peut violer — à traiter en couche 2 (une instance par
  tâche, ou nul avec effet de tâche).
- `EMPREINTES-orchestrateur-pole-v7-v1.txt` (commit `7c1806c`) ne correspond plus à trois fichiers modifiés depuis
  (`cycle.py`, `pole.py`, `test_v7_banque.py`, pour la règle de multiplicité) : la v2 des empreintes et du LISEZMOI fait
  foi ; la v1 est gardée (R12), sa non-correspondance est la trace du changement.

## 3. Instances et sous-agents

Aucune instance de calcul ; aucun sous-agent en cours ; aucune clé lue, affichée ni demandée.
