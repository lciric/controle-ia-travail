# Points ouverts après le portage de la version 5 des pièces de la comparaison essaim, v1

22 novembre 2026, Opus 5.5. Liste seulement : aucun point n'est résolu ici. Sources : relecture de Fable `relecture-pieces-essaim-v4/relecture-fable-api.md` (c1cebee3…), `pieces-comparaison-essaim-v5.md` (681d341c…), `epreuves-pieces-essaim-v5-v1.md`.

## A. Points que Fable laisse ouverts ou conditionnels

1. **Sceller la pièce 2 à part (décision 7).** Fable recommande l'option a, « si la règle R5, que je n'ai pas lue, le permet ». Confiance 0,6. Revient au directeur. La pièce 2 n'appelle pas l'article 4 ; elle serait scellable dès la correction 57, portée en v5.
2. **Lecture humaine des dossiers déjà joués (décision 6).** Recommandation : option a, pas de lecture ; confiance 0,75. Revient au directeur. Le coût de 140 tours est donné comme [HYPOTHÈSE].
3. **Le lot aveugle de l'article 9 n'est pas joué.** Il faut six textes, trois par tour, écrits par un agent neuf qui n'a lu que les consignes balisées. Je n'ai pas d'outil pour lancer un agent neuf. Surtout, les consignes balisées n'existent pas encore (point B1). C'est la deuxième des trois conditions que Fable met au scellement de la pièce 1.
4. **Réserves de Fable.** Il n'a exécuté aucun code et n'a lu ni les lignes 528 à 546 du collisionneur, ni la règle R5, ni aucune cellule. Son code de référence est maintenant exécuté : le lot de pièges passe. Les deux autres lectures restent non faites par lui.
5. **Coût et délai des huit questions balisées** que le verdict attend. « Non chiffrés ici » selon Fable ; ils relèvent d'un devis.
6. **Phrases de l'article 3 de la v4 qui ne passent pas à l'article 14.** La correction 49 dit : « Les clauses sur Argon passent à l'article 14. » La puce « Argon » de l'article 14 (correction 56) n'en reprend que le fond. Deux phrases de la v4 ne figurent plus dans la v5 :
   - « un premier tour affaibli gonfle l'apport apparent du troisième » ;
   - « Le tour III.1 rejoué n'est pas un ancêtre. […] Il ne sert pas de plancher de bruit : deux tirages indépendants diffèrent plus qu'une révision [HYPOTHÈSE]. »

   Est-ce voulu ? À confirmer par Fable.
7. **Citation de l'épreuve aveugle.** La correction 45, portée telle quelle, renvoie à « épreuve aveugle 5fc15fc0… », c'est-à-dire à la v1 du rapport, dont les nombres étaient faux. L'erratum est la v2 (8720522f…). Les deux versions concluent au même échec. Faut-il changer de renvoi ? Fable ne le dit pas.
8. **Tension entre l'article 9 et l'article 12.**
   - Le NOUVEAU de l'article 9 dit : « Si le lot aveugle échoue, on réécrit la consigne, non les motifs, puis on rejoue avec un agent neuf. »
   - La puce suivante de l'article 9, inchangée, dit : « Si l'une échoue, arrêt. »
   - L'article 12, inchangé, compte « Épreuve de l'article 9 échouée » dans la liste d'arrêt.

   Fable ne tranche pas laquelle prime.
9. **Places choisies pour les ajouts sans ANCIEN.** Champ de l'article 10 : première puce. Ajout au plan de la pièce 2 (a) : dernière puce. Voir la table des corrections, qui donne aussi la place de l'article 14.
10. **Ce que la forme imposée laisse non conforme.** Ces formes ne sont pas reconnues : « 1. [DUEL 1] » (balise après un numéro de liste), une balise entre accents graves, « [Duel 1] » (casse). Le tour devient alors non conforme (épreuves, suppléments 1 à 3). Combien de cellules seraient ainsi rendues invalides, contre le seuil d'une sur dix de l'article 12 et la prévision de neuf sur dix de l'article 11 ? Seul le lot aveugle le dira.

## B. Changements que la voie (b) impose ailleurs (lieux seulement, rien n'est modifié)

1. **Consignes des tours III.1 et III.3 du collisionneur.** Fichier : `docs/notes/collisionneur-v9/collisionneur_v9_v8d.py` (sha256 b780383874598f12b24c79e4087d335c8e01cda685e295f5116898fa3b1715ac), dictionnaire `CONSIGNES` (ligne 505).
   - Entrée `"E3-T1"` : lignes 528 à 534. La phrase qui demande les duels, « (b) les expériences décisives qui la trancheraient, chacune en duel H_A contre H_B, … », est aux lignes 530 à 532. Elle fait partie d'un seul paragraphe « Livrable » qui court de (a) à (d), lignes 530 à 534.
   - Entrée `"E3-T3"` : lignes 542 à 546. Aucune phrase n'y demande de duel : le point (b) dit « les expériences corrigées » (lignes 544 et 545). « Après la phrase qui demande les duels » n'a donc pas de place évidente au tour III.3.
   - Il faut fixer où va le texte de Fable. La relecture demande aussi une traduction pour les cellules en anglais, balises inchangées, et ne la donne pas.
2. **Autres lieux du même fichier qui parlent de duels, que Fable ne vise pas.**
   - Règle B4 du préambule (ligne 492) : « toute expérience oppose deux hypothèses exclusives H_A et H_B ».
   - Une autre consigne (ligne 516) demande « quatre protocoles expérimentaux, chacun en duel H_A contre H_B ».
   - Le critère `"falsifiable_duels"` (ligne 370).
3. **Mode essaim (pièce 2).** D'après `essaim-rapport-developpeur-collisionneur-v9-essaim-v1.md` :
   - `collisionneur_v9_essaim_v1.py` importe la v8d et contrôle son empreinte b7803838… au chargement ;
   - son brouillon reçoit la consigne du tour III.1 mot pour mot ;
   - sa consigne finale reprend le format du tour III.3.

   Changer la consigne de la v8d demande donc une nouvelle version du collisionneur (R12), une nouvelle empreinte attendue par le module de l'essaim et une décision pour sa consigne finale. La correction 57 fige les consignes avant le pilote. Le fichier du module de l'essaim est absent de cet arbre de travail : je l'ai cherché par son nom, sans le trouver.
4. **Gardes de motifs.** La garde `MOTIFS_INTERDITS` de la v8d (ligne 552 : noms, sessions, courriels, chemins, identifiants) ne vise aucune forme des balises. Aucune autre garde n'a été vérifiée.
5. **Population.** Les huit questions de l'article 2 sont des questions jouées en mode isolé, avec la consigne balisée et après le scellement. Les exécutions de la comparaison n'en font pas partie. Rien n'existe encore de cette population.
