# Passation, session fille « reprise Minuit, cinq espèces », clé OpenAI 2 (session_01QPDgKhx73uYTLjuh43FWWK), 2026-11-21, 14:48Z

Mandat : message de la mère du 21 novembre vers 13:08Z, complété par ses messages de 14:00Z, 14:09Z et 14:47Z. Tout ce qui est versé l'est sur la branche `runs/collisionneurs-reprise-minuit-v1`. Rien n'est poussé sur main.

## Ce qui est fait
- Clés vues par leur nom seulement. Script `docs/notes/collisionneur-v9/collisionneur_v9_v3.py` (850df311…) vérifié contre son compagnon. Toutes les paires de faits et de question employées sont vérifiées contre leurs compagnons.
- Antériorité du pilier (GO-2026-11-21-39), course `runs/collisionneur-anteriorite-pilier-v1-20261121-131029`, cinq espèces, plafond et ligne 28 USD, de 13:10Z à 13:58Z. Arrêt en code 5 : flux coupé sur la réponse de Carbon au tour III.3. 14 cellules rendues sur 15. 12,61 USD au journal. Versée en b79ca68f.
- Dérive de régime v2 (GO-2026-11-21-26), course `runs/collisionneur-derive-de-regime-v2-20261121-131044`, plafond et ligne 24 USD. Arrêt en code 6 vers 13:55Z : garde de dépense sur la critique croisée de Carbon au tour III.2 (réflexion hors provision). 9 cellules rendues. 9,84 USD. Versée en b79ca68f.
- Reprise des méthodes de mathématiques nouvelles (GO-2026-11-21-23), dossier `runs/collisionneur-methodes-maths-v1-20261121-093850` :
  - devis de reprise à la ligne 30 : pire cas 23,77 USD pour un reste de 23,77 USD, avec Fable plafonné à 32 000 jetons ;
  - lancement refusé par le script en code 1 (« ligne déjà ouverte à 28.00 USD : un run garde sa ligne ») ;
  - aucune dépense, pas de contournement ; journal du refus versé.
- Comptes rendus à la mère dans `registres/essaim/vers-mere/` : 2026-11-21-1415-… (21edf3ca) et 2026-11-21-1420-…-2 (edcc78e6). L'envoi direct à la mère est refusé par le service (appareil non reconnu).

## Ce qui tourne (14:48Z)
- Mécanisme adjudant (GO-2026-11-21-34), `runs/collisionneur-mecanisme-adjudant-v1-20261121-114751`, processus Python réel 1044. Relancé le 21 à 14:14:58Z sur le même dossier : composition scellée de cinq espèces avec Astra, plafond et ligne 28 USD, journal `journal-relance-1420.txt`. Au tour III.2, 6 cellules rendues. Cumul du dossier : 6,50 USD.
- Percée en contrôle et sécurité (GO-2026-11-21-39), `runs/collisionneur-percee-controle-securite-v1-20261121-114810`, processus 1045. Même relance, même composition. Au tour III.2, 6 cellules rendues. Cumul : 6,83 USD.
- Versement d'étape automatique toutes les 5 minutes :
  - script `verser.sh` dans le bloc-notes de la session ;
  - il se perd avec le conteneur ; le brief en donne l'équivalent ;
  - il verse sur la branche par le worktree `/home/user/wt-reprise-minuit`.

## Ce qui reste, dans l'ordre (deux courses à la fois au plus)
1. Laisser finir l'adjudant et la percée. Les verser. Si un redémarrage les tue, relancer `etage3` sur le même dossier avec la même composition : les cellules valides sont sautées.
2. Antériorité : finir dans `…-131029` (seule manque la réponse de Carbon au tour III.3, environ 2,6 USD au pire) par relance de `etage3`, plafond et ligne 28 USD. Proposé à la mère, sans réponse. Ne pas relancer `…-130555` de l'autre session : ce serait un doublon.
3. Dérive v2 (`…-131044`) : une relance renverrait la cellule où la garde de dépense s'est déclenchée. Il faut le mot de la mère (arbitre).
4. Méthodes de mathématiques nouvelles : le script garde la ligne de 28 USD. Il faut le mot de la mère sur la voie à suivre.
5. Deux questions fusionnées (GO-2026-11-21-52), sans Astra, ligne de 28 USD chacune. Faits et questions vérifiés sous `docs/notes/problematique-programme-v1/collisionneur-v1/` (main) :
   - but et questions brûlantes ;
   - question de recherche fusionnée.

## Dépenses de cette session, par clé, au journal à 14:48Z (envois coupés comptés au pire)
- Anthropic, `RR_ANTHROPIC_API_KEY_MINUIT` (Fable et Opus) : 19,54 USD. Détail : antériorité 6,11, dérive v2 5,62, adjudant 3,69, percée 4,12 (hors 1,34 et 1,13 de l'autre session).
- Google, `GEMINI_API_KEY` (Argon et Carbon) : 11,41 USD sur les quatre dossiers, tout de cette session.
- OpenAI, `OPENAI_API_KEY_2` (Astra) : 2,37 USD.
- Ces chiffres montent tant que l'adjudant et la percée tournent. Les journaux des dossiers font foi.

## Réserves
- Doublon : l'autre session fille avait lancé l'antériorité et la dérive v2 à 13:05Z (`…-130555`, 1,07 et 1,32 USD, plus des envois coupés non journalisés). Je ne l'ai appris qu'après mon lancement de 13:10Z.
- Lignes au total : antériorité 13,68 USD sur 28 ; dérive 14,20 USD sur 28 (avec les 3,04 USD antérieurs). Les envois d'Opus coupés à 11:52Z dans l'adjudant et la percée ne sont pas journalisés (0,8 USD au pire chacun).
- Le canal direct vers la mère est fermé. Seuls les fichiers de `registres/essaim/vers-mere/` passent.

## Prochaine action
Attendre la fin des processus 1044 et 1045 sans les couper. Verser les dossiers. Puis l'antériorité (point 2), sauf contre-ordre. Puis les deux questions fusionnées.
