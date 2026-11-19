# Mandat du rédacteur du plan : préparer les couples que le code de formation demande au texte (barreau 5) — v1

Écrit par la mère (`session_01XJ6Mgr8BN6UanALsQatc5E`) le 19 novembre 2026 vers 20:08Z. Pièce de travail. Destinataire : le rédacteur Fable 5.2 qui a écrit les brouillons 2 et 3 et la fiche de décision sur le constat V-B1.

---

## Pourquoi maintenant
- Lazar n'a pas encore tranché la fiche V-B1 (« 39 adaptateurs », voie (iii)). Son mot est attendu le 20 au matin. Le défaut sous 48 heures est 39 adaptateurs et la voie (iii).
- Le code de formation est corrigé. Rapport v3 du développeur : `code-formation/rapport-developpeur-corrections-code-formation-v3.md` (`ddaf91a8…`), §§ 5, 6 et 7. Son contre-lecteur vérifie les corrections en ce moment.
- Le code attend du texte plusieurs choses, quelle que soit la voie. Sans elles, la ligne `SCELLEMENT-B5F` ne peut pas s'écrire et rien ne part le 23.
- Les préparer ce soir, c'est gagner le 20 pour le brouillon 4.

## Ce que tu prépares
Une table de couples exacts, à verser dans le brouillon 4 quand Lazar aura parlé. Pour chaque couple :
- section ;
- texte avant, recopié du brouillon 3 ;
- texte après ;
- motif.

Tu n'écris pas encore le brouillon 4.

1. **Sens de « pièce »**, liste d'arrêt, points 1 et 3. Le code le lit dans `SCELLEMENT-B5F` : « famille » ou « instance ». La recommandation du développeur et de la contre-lecture est « famille ». Tranche dans le texte, et dis pourquoi.
2. **Relance unique d'une instance tombée.**
   - La règle : l'instance entière est reformée sous des noms suffixés `-x1`, avec des graines neuves ; la première copie est versée et jamais lue.
   - La clé `GO-RELANCE-FORMATION-B5F`, aux « Lignes de registre » et au calendrier.
   - Les clés de graines `b5f/famille/<k>-x1/…` et `…-r1/…`, au point 14.
3. **Évaluation réduite** :
   - 8 tâches communes par pli ;
   - le saboteur d'apprentissage joue ses 16 tâches communes par pli ;
   - la décision de coupure compte les tâches réellement jouées.
   - Le devis disait « les 16 premières tâches tirées » : à récrire.
4. **Suffixe « k »** : non éditable quand la valeur passerait sous 1, sauf si tu préfères l'écriture « 0.6k ». Choisis, et dis le prix de chaque branche.
5. **Écart m-4** : « encodé seul, texte relu égal », si tu l'acceptes.
6. **Risque du plafond de 10 % d'actions non éditables.**
   - Le cas : « A100 » dans le champ du coût, ou « 2k », chez le saboteur.
   - Ce que l'on sait : l'essai à blanc avec le vrai tokeniseur ne trouve aucune action non éditable hors de celles que le texte exclut. La fréquence de ces écritures chez le saboteur est inconnue.
   - Propose un remède que le texte peut adopter **sans lire aucune donnée**, ou un repli écrit d'avance pour le jour de la formation.
   - Dis si le remède touche une pièce scellée (le lecteur gelé du coût), donc un écart à porter à Lazar.
7. **Devis.**
   - **À trois membres**, si Lazar dit « 39 », pour les instances 6 et 7 : la coupure et les heures attendues. Le code refuse ces deux instances tant qu'il n'a pas ces deux nombres.
   - **Marché réel, à 20:02Z** : `code-formation/verification-champs-offre-loueur-v1.md` (`48a81bd4…`).
     - 3 offres seulement passaient toutes les bornes, sur 11 cartes A100 de 80 Go ;
     - elles coûtaient 1,12 à 1,19 USD de l'heure ;
     - sept instances sont prévues.
   - Dis ce que le calendrier et le devis doivent en tirer : lancement par vagues, attente, effet sur le coût attendu et sur le plafond de 200 USD.
8. **Tout autre point** des §§ 6 et 7 du rapport v3 qui demande un mot du texte.

## Forme et sorties
- **Fichier** : `docs/notes/barreau5-resolution-v1/plan-avant-entretien/couples-du-code-pour-brouillon4-v1.md`, scellé et non commis.
  - Commande : `cd /home/user/controle-ia-travail && PYTHONPATH=src .venv/bin/python -B -m controle_ia.scellement sceller <fichier>`.
- **En tête du fichier** :
  - les couples qui valent pour les trois voies ;
  - ceux qui ne valent qu'à 39 adaptateurs ;
  - ceux qui demandent un mot de Lazar.
- Tes calculs, s'il y en a, en programme versé à côté, sous un nom neuf.

## Règles
- **Garde du dépôt** : aucun nom de commande d'arrêt ou de recherche de processus par motif dans une commande. Tes fichiers seulement par les outils d'écriture et d'édition.
- **Interdits de cloisonnement** : inchangés depuis tes mandats précédents.
  - Aucune donnée ni aucun résultat : rien de `diag/`, aucun score, aucune transcription, aucun résultat de 7a, 7b, T0.6, de l'étape B, de l'étape B bis ou de P3-bis.
  - Aucun fichier dont le nom contient « consigne-privee » ou « conception-ii-b ».
  - Rien sous `/root/.claude/`.
- **Rien de réel** : aucun réseau vers un loueur de cartes, aucune dépense.
- **Refus d'outil** : au premier refus, arrête-toi et dis-le, sans le contourner.
- **Rendu à la mère** : aucun nombre de résultat d'expérience close.

## Rends
1. La phrase exacte de ton invite système qui nomme ton modèle.
2. Le chemin et l'empreinte de ta sortie.
3. Huit lignes au plus :
   - les couples, par classe ;
   - ce qui demande un mot de Lazar ;
   - ce qui menace encore le scellement le 21 et le gel le 22.
