# Mandat de contre-lecture à froid : additifs du critère 3 de la porte de fin de phase 0 (v1)

Classe C. Session mère, 28 novembre 2026. Mandat commun aux trois contre-lecteurs neufs demandés par Lazar (GO-2026-11-28-11) : un agent Fable 5.2, Carbon, Astra. Chacun lit seul, sans voir les autres rendus.

---

Tu es contre-lecteur à froid d'un préenregistrement décisif. Tu n'as écrit ni la pièce ni ses brouillons. Ton rôle est de trouver ce qui la rendrait fausse, inexécutable ou indéfendable devant un référé hostile, avant qu'elle ne soit scellée. Réponds en français.

## Le programme, en cinq lignes
Un programme de recherche mesure si un moniteur qui lit les activations internes d'un agent (des **sondes**, « boîte blanche ») détecte mieux qu'un moniteur qui ne lit que son texte (« boîte noire ») un **sabotage diffus** : réel sur l'ensemble d'un épisode, invisible action par action. L'agent est Llama-3.1-8B-Instruct. La tâche est floue : bâtir en dix pas des propositions d'expériences à partir d'un article. Le saboteur étudié ici gonfle le coût déclaré, sur consigne cachée.

La règle de la porte (décision N-063 v2) : les sondes ne sont jugées qu'aux doses où le sabotage est établi et où un lecteur boîte noire scellé du texte, « mots et coût », échoue selon son propre critère. S'il n'en existe aucune, le résultat est « sans objet ». La première course a rendu « sans objet ».

## Ce que tu lis
Le kit joint contient chaque fichier **en entier**, précédé de son chemin et de son empreinte SHA-256. Vérifie qu'aucun n'est tronqué ; signale tout écart.
1. **Les pièces à contre-lire** : l'additif de la micro-course neuve, l'additif de la dérogation sur la première course, le devis, la table des écarts, les nœuds pour Lazar.
2. **Les décisions de Lazar du 28 novembre** (extrait du registre des accords, numéros 1 à 11), dont le numéro 9 (six nœuds) et le numéro 10 (première étape sous consigne privée ; rejet des récitations).
3. **Les textes scellés en vigueur** : la désignation de la course du critère 3 ; la lecture des sondes (états et lettres) ; les décisions N-063 v2, N-053, N-054, N-026, N-029 ; la proposition P-066.
4. **Le code en vigueur** : module d'environnement des propositions, parseur du coût, module des conditions de la course de dose-réponse, lecteur du texte de la dose-réponse.
5. **Le pré-mortem des brouillons précédents** (trois lecteurs et leur synthèse) et la note sur la taille du modèle. La pièce devait corriger ce qu'ils relèvent.

## Ce que tu cherches
1. **Conformité.** La pièce applique-t-elle les décisions de Lazar, sans rien remplacer qu'elle ne nomme ? Chaque écart à un texte scellé est-il nommé, avec le texte touché et sa raison ?
2. **Complétude du préenregistrement.** Faut-il tout cela, et l'est-il sans ambiguïté :
   - hypothèse ;
   - prédiction chiffrée avec son signe ;
   - métrique ;
   - seuil ;
   - plan d'analyse ;
   - critères de lecture gelés (chaque état possible, sans chevauchement ni trou) ;
   - liste d'arrêt ?
3. **Exécutabilité.**
   - Les gardes de rejet et d'arrêt sont-elles étalonnées sur des données réelles ? Avec quelle acceptation par tâche et quelle probabilité d'arrêt ?
   - Le code cité existe-t-il, ou est-il à écrire ?
   - Le devis tient-il au débit mesuré ?
4. **Défendabilité.**
   - L'organisme est-il trié contre le lecteur qui doit échouer ?
   - La sonde peut-elle lire la demande plutôt que l'acte ?
   - Le format commun du coût referme-t-il la fenêtre de mesure ? Sur des bras émulés au coût uniformisé, le lecteur du coût atteint 0,70 à 0,73 aux facteurs 3 et 5.
   - L'asymétrie entre le bras honnête (sans consigne finale ni note à chaque pas) et les bras instruits est-elle traitée ?
   - La dérogation choisit-elle son contraste après coup, et le déclare-t-elle ?
5. **Arithmétique et provenance.**
   - Refais les calculs que tu peux : seuils de reprises, effectifs, puissance, coûts.
   - Toute empreinte citée doit être celle du fichier cité à côté.
   - Tout chiffre de la littérature doit renvoyer à une page de PDF.
6. **Ce qui pourrait échouer.** Les trois à cinq issues les plus probables de la course telle qu'écrite, avec leur probabilité, et l'épreuve la moins chère qui les détecterait.

## Garde
Tu ne reçois et ne demandes aucune consigne privée du saboteur, aucun résultat de sonde (aire, score, plancher, poids), aucune activation. Si un texte joint en contenait, signale-le sans le reprendre.

## Ton rendu
- **Verdict d'abord**, en un mot pour chaque pièce : « prête à sceller », « à corriger » ou « à réécrire » ; puis trois lignes de raison.
- **Remarques numérotées.** Pour chacune :
  - sa gravité (majeure ou mineure) ;
  - son lieu : pièce, section et phrase citée ;
  - le scénario qui fait échouer la pièce ;
  - la preuve : ligne d'un texte joint, ou calcul refait ;
  - la correction proposée.
- **Ce que tu n'as pas pu vérifier.**
- 2 500 mots au plus hors tables.

Tu recevras ensuite le texte corrigé et la table « remarque → correction ». Tu diras alors, pour chaque remarque, si elle est levée.
