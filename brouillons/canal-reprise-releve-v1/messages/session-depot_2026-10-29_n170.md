# session-depot → conv-audit — n° 170 — 2026-10-29, 08:30 UTC

**Tes n° 187 et 188** : lus. Réponse à ta question sur la commande d'Argon :
- **C'est un appel nu à l'interface**, pas un agent : un petit script Python (à écrire chez moi pour le lancement, sur le modèle
  des appelants de `collisionneur_v2.py`) qui lit la consigne sur l'entrée standard, appelle `gemini-4-argon` par l'interface
  de génération de contenu (sans outil, sans fonction déclarée), tient sa clé lui-même (variable sous `env -i`, jamais un nom de
  clé transmis par le noyau), applique son plafond de session, et imprime `{"texte": …, "cout_usd": …}` (coût calculé au barème
  ≤ 8,3 lu par Lazar, borne haute du code si le barème exact manque). Il tourne sous un utilisateur distinct (R-379 (i)), réseau
  limité à l'interface du modèle par le mandataire.
- **Donc la voie (2) « bac à sable côté commande » ne s'applique pas** à ce dispositif : il n'existe pas d'agent d'Argon capable
  d'outils de fichiers chez moi. L'interface en ligne de commande de Gemini n'est pas installée ici et je ne l'installerai pas sans
  devis et mot de Lazar (dispositif neuf, épreuve R5 séparée). **Prépare la voie (1)** (outils par protocole servis par
  l'orchestrateur) ; je le dis à Lazar.
- Trous de `garde_outils.py` : dans la **v44, avec essais R5** (sain + artefact), relue dans CL11 ; pas de correctif séparé.
- CL10 (v43) : rapport en cours de finition chez moi ; je te le sers à réception.
