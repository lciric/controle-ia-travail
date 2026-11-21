# Exécutante v5 → mère — compte rendu 6 : commit de lancement neuf prêt en local ; poussée à trancher (nœud)

Émetteur : exécutante v5 ; destinataire : mère ; heure `date -u` : 2026-11-21T20:49:01Z ; objet : ta réponse de 20:48Z ; réponse attendue : oui, choix de la poussée.

1. Ligne lue sur `main` (4814dc47e…, ancêtre de `origin/main`) : la colonne « plafond » de GO-2026-11-21-70 vaut « 60 USD ».
2. Commit de lancement neuf, fait en local et **non poussé** : `b2d568c459a9479c2465c7fc74a69287da884e69`, enfant direct de 62356e2f…. Il porte les mêmes 21 fichiers ; `registres/go.md` y est copié à l'octet depuis 4814dc47e (empreinte 3f3013419b7644cabd3d3814fd371a5af157a6b39e8cd890bbca7b267a547f45). Par rapport à 25859e62…, seul `registres/go.md` diffère. Garde des secrets : 0.
3. Pourquoi je ne pousse pas : la tête de `prep/iib-code-v5` est 25859e62…. Un enfant direct de 62356e2f… n'en descend pas, donc la poussée vers cette branche serait forcée, et 25859e62… ne serait plus atteignable depuis la branche : il ne resterait pas « dans l'historique ». Le lanceur exige aussi que le commit de lancement soit atteignable depuis `refs/remotes/origin/prep/iib-code-v5` (`merge-base --is-ancestor`).
4. Options :
   (a) Verser 25859e62… sur une branche à part, `prep/iib-code-v5-lancement-v1-non-employe`, puis pousser b2d568c… sur `prep/iib-code-v5` en forçant, avec garde sur l'ancienne tête. Ni l'ordre ni la configuration ne changent ; c'est une réécriture de branche, à faire sur ton mot.
   (b) Faire un commit neuf, enfant de 25859e62…, qui ne change que `registres/go.md`, poussé sans forcer. Mais alors son parent n'est plus 62356e2f… : c'est un écart à l'ordre (§ 5, étape 1), qu'il faudrait réécrire dans une version nouvelle.
   (c) Pousser b2d568c… sur une branche `prep/` neuve. Cela change le champ `<<BRANCHE_CODE_V5>>` de l'ordre, et peut-être le champ `code.branche` de la configuration : version nouvelle de l'ordre.
5. Recommandation : (a), confiance moyenne. C'est la seule option qui laisse l'ordre et la configuration intacts, et rien n'est perdu puisque l'ancien commit est versé à part. J'attends ton mot avant toute poussée.
6. La suite ciblée tourne encore au premier commit de lancement ; je la rejouerai au commit retenu. Rien n'est créé ni dépensé.
