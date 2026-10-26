# Décision de Lazar sur les graines du pilote 4 : (c) — v1

Note écrite par conv-audit le 2026-10-26 à 09:09:29 UTC (heure lue sur `date -u` dans la commande qui écrit cette ligne).
Aucun score n'est lu ici. Aucune dépense n'est décidée.

## Mots de Lazar, verbatim

Session de conv-audit, 26 octobre 2026, 10:07 heure de Paris (09:07 UTC) :

> graines : c

En réponse à la décision posée par conv-audit après la synthèse du tour « graines »
(`envois/synthese-collisionneur-graines-v1/synthese-collisionneur-graines-v1.md`,
`b8cdeb5c18335b1c94417ca2f820404a07b68309550a5fe11ec52bc8c3a2df2a`), rappelée dans la pièce des points pour Lazar
(`envois/points-boucle-exterieure-pilote4-pour-lazar-v1.md`, `ac105262…`, point 2) et dans le bilan de la nuit (10:04
heure de Paris). L'option (c) y était : **aucune graine de plus sur la banque v3 ; la lecture de `test` s'ouvre (N-050) ;
le bruit entre graines se mesure dans le pilote (b), sur la banque v6, avec les deux objets ; le contrôle « organisme figé
rejoué » entre dans le texte de (b), à côté de l'étalon de dérive déjà prévu.** Recommandation de conv-audit : (c),
confiance moyenne.

## Effets

1. **La retenue de lecture est levée** pour la part `test` et les faits mécaniques des courses M et S du pilote 4 (texte
   v5 du pilote, § Plan, point 3 ; N-050). La part `test_final` reste fermée jusqu'à la fin du compteur de rondes de la
   boucle extérieure, et n'est lue qu'une fois.
2. **Aucune course de plus** sur la banque v3 dans le pilote 4 ; aucune dépense ; le reste de `GO-2026-10-25-02` n'est
   pas engagé par cette décision.
3. **Pilote décisif (b)** : son texte devra prévoir plusieurs graines par objet (nombre fixé à son devis ; la lecture de
   AIRA recommande 10 à 20 graines par tâche, synthèse `f13a6d68…`) et le contrôle de l'organisme figé rejoué. Les
   hypothèses de (b) (`903c6b51…`) ne changent pas par cette décision.
4. **Boucle extérieure** : la lecture ouverte, elle démarre quand les conditions de son protocole (v4, § 1) sont remplies :
   relevé (B) écrit et essayé puis exécuté par session-depot, pièces v6, dossiers d'audit et étalonnage à blanc. Les
   fichiers de lecture ne sont lus que par les agents de la boucle, par leurs dossiers ; conv-audit ne les ouvre pas
   (protocole, § 2) : il continue d'écrire les règles.
5. Le registre v5 de la boucle n'a pas à changer : cette décision n'ajoute aucun texte et ne change aucune règle de
   lecture (registre v3, § 5, point 12, condition non remplie).

Numéro proposé pour l'inscription chez session-depot : N-051 (proposé).
