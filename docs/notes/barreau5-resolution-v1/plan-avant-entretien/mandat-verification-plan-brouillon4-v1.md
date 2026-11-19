# Mandat de vérification du brouillon 4 du plan « sabotage ou empreinte » (barreau 5) — v1

Écrit par la mère (`session_01XJ6Mgr8BN6UanALsQatc5E`) le 19 novembre 2026 vers 22:20Z. Pièce de travail. Destinataire : le contre-lecteur Opus 5.5 qui a contre-lu le brouillon 2 (`29b86657…`) et vérifié le brouillon 3 (`a1b2250d…`). Règle des pièces décisives : la vérification revient au même contre-lecteur.

---

Le rédacteur Fable a écrit le brouillon 4, selon les mots de Lazar :
- 39 adaptateurs, voie (iii), départ au plus tôt (GO-2026-11-19-79 et -82, `registres/go.md`) ;
- ton constat bloquant V-B1, traité par la voie (iii) de sa fiche (`fiche-decision-v-b1-lazar-v1.md`, `78cadfd2…`).

Lazar veut un départ le 21. C'est donc la vérification qui doit passer du premier coup, si le texte le mérite.

## Pièces (vérifie chaque sceau)
Toutes dans `docs/notes/barreau5-resolution-v1/plan-avant-entretien/`, sauf le texte :
- **le texte** : `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-brouillon4.md` (`dbe66dc9…`) ;
- **le devis** : `devis-adaptateurs-tenus-a-l-ecart-v1-brouillon4.md` (`084cd547…`) ;
- **la table des corrections** : `table-corrections-plan-brouillon4-v1.md` (`bf129b01…`) ;
- **la fiche v4 pour Lazar** : `fiche-v4-lazar-v1.md` (`a88a3a12…`) ;
- **les programmes et leurs sorties** : `fabrique-brouillon4-v1.py`, `sections_brouillon4_v1.py`, `simulation-brouillon4-regle-d-issue-v1.py`, `controle-precision-brouillon4-v1.py`, et leurs sorties ;
- **autour** :
  - le mandat du rédacteur, `mandat-redacteur-brouillon4-v1.md` (`63e8606a…`) ;
  - ses couples du code, `couples-du-code-pour-brouillon4-v1.md` (`1e929542…`) ;
  - la vérification des corrections du code, `code-formation/verification-corrections-code-formation-v1.md` (`3517677f…`), § 7 et § 8 ;
  - ta propre vérification du brouillon 3.

## Ce que tu juges
1. **La voie (iii), construction neuve que tu n'as pas vue.**
   - Ce qu'elle doit faire : la sonde est apprise sur le sur-saboteur contre le jumeau ; l'épreuve à poussée égale oppose ces deux membres édités ; le saboteur sert d'étalon ; la direction commune est tirée des saboteurs d'apprentissage.
   - Ce que tu cherches :
     - ferme-t-elle V-B1 et V-M1 ?
     - quelle explication sans sabotage passe encore les quatre épreuves ?
     - attaque la règle d'issue neuve : l'épreuve du sur-saboteur contre le jumeau en tête, quatre épreuves pour le mot, « le saboteur seul au-dessus de son jumeau » rangé en « non établi ».
2. **La simulation.**
   - Rejoue-la, puis reprends-la dans tes propres mondes inventés, par ton propre programme.
   - Vérifie le niveau sans sabotage. Le rédacteur dit 0,9 % au plus sur 1 000 mondes, et 0,44 à 0,54 % à 20 000.
   - Vérifie la puissance, et la faiblesse déclarée quand la réponse est saturée.
3. **Les couples appliqués.**
   - Tes 15 couples « toujours » du brouillon 3 : 9 à l'octet, 6 repris.
   - Les 39 couples du code.
   - Vérifie par programme ce qui est dit présent ou repris.
4. **Les choix qui touchent le code** (§ 1 de la table) :
   - le nom de carte, sans toucher au lecteur gelé du coût ;
   - les deux paliers, de 10 et 25 % ;
   - « 2k » écrit « 600 », refusé ;
   - la relance hors du plafond, dans une enveloppe à part de 56 USD ;
   - les instances 6 et 7 à trois membres.

   Le contre-lecteur du code recommandait la relance sous le plafond commun : juge le choix du rédacteur.
5. **Le devis et le calendrier en heures depuis le départ.**
   - Arithmétique : 204 USD de coupures pour un plafond de 200 ; enveloppe de 56 USD ; recharge.
   - Échéances : H + 30 et H + 54.
   - Lancement au fil des offres.
6. **Rôles et écarts** :
   - exclusions de rôles par catégorie, avec renvoi à la liste « qui a lu quoi », version 13 ;
   - écart R-3953 déclaré au point 7 ;
   - seuils posés sans donnée, déclarés.
7. **Les sept phrases marquées « [à confirmer par le rapport v4] ».** Le rapport v4 du développeur n'est pas encore rendu. Vérifie le reste. S'il arrive pendant ta vérification, la mère t'en donne l'empreinte, et tu donnes les couples qui lèvent ces marques.
8. **Une séparation demandée par la fiche v4.** Pour chaque constat bloquant ou majeur, dis s'il touche les sections figées pour la formation, ou seulement la lecture. Si rien ne touche la formation, Lazar peut choisir de sceller d'abord la formation, puis de corriger la lecture par un addendum avant l'engagement.

## Forme et sorties
- **Verdict en tête**, l'un des trois : « scellable », « scellable après ces couples », « à reprendre ».
  - Couples exacts : fichier, avant, après. Chaque « avant » doit être trouvé une fois, par programme.
  - Chaque constat est classé bloquant, majeur ou mineur, et marqué « formation » ou « lecture ».
- **Sorties**, scellées, non commises :
  - `verification-plan-brouillon4-v1.md` et ses outils dans `outils-verification-plan-brouillon4-v1/`, dans le dossier ci-dessus ;
  - commande de scellement : `cd /home/user/controle-ia-travail && PYTHONPATH=src .venv/bin/python -B -m controle_ia.scellement sceller <fichier>`.

## Règles
- **Aucune donnée ni aucun résultat.** Rien de `diag/`, aucun score, aucune transcription, aucun résultat de 7a, 7b, T0.6, de l'étape B, de l'étape B bis ou de P3-bis. Ne recopie aucun nombre de résultat dans ton rendu.
- **Fichiers interdits** : aucun fichier « consigne-privee » ou « conception-ii-b ». Rien sous `/root/.claude/`.
- **Écriture** : tes fichiers seulement par les outils d'écriture et d'édition, programmes compris.
- **Garde du dépôt** : aucun nom de commande d'arrêt ou de recherche de processus par motif dans une commande, même dans une boucle d'attente.
- Aucun réseau, aucune dépense, aucun commit.
- **Refus d'outil** : au premier refus, arrête-toi et dis-le.

## Rends
1. La phrase exacte de ton invite système qui nomme ton modèle.
2. Tes sorties, avec leurs empreintes.
3. Dix lignes au plus :
   - le verdict ;
   - les constats par classe, et par « formation » ou « lecture » ;
   - le taux à tort et la puissance, dans tes propres mondes ;
   - ce qui menace un départ le 21.
