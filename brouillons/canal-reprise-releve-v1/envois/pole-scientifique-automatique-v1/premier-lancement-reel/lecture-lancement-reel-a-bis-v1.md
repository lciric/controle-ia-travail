# Course de contrôle « (a) bis » (moteur réel, v7 version 5) — lecture dans les deux sens — v1

Lignée conv-audit (instance du 27 octobre 2026), écrit à partir de 15:47 UTC (heure lue sur `date -u` : 15:47:21).
Source : branche `donnees/pole-lancement-reel-a-bis-v1`, commit `8533de8`, versée par session-depot (GO-2026-10-27-10,
orchestrateur v7 version 5 au commit `5ac9cb6`, empreintes `81bd0204…`, sans modification). Empreintes de la sortie
vérifiées : `EMPREINTES-v1.txt` (`d73c8cc3…`), aucun écart. Fichiers lus : `course/bilan.json` (`3467f21b…`),
`course/manifeste.json` (`1c2e75ab…`), `course/journal/generation-00.json` (`659a34ea…`) et `-01.json` (`8edc1e5f…`),
`RELAIS.jsonl` (`4407a2bf…`), les réponses des vérificateurs (`traces-verification/`), les leçons
(`traces-synthese/lecons.json`), les dossiers des agents. Lecture L1 à L6 fixée avant la course (message n° 112, point 3).

## Verdict

1. **Les six lectures fixées tiennent.** Aucune erreur de l'orchestrateur ; les deux témoins vrais jugés et promus, les
   deux témoins faux jugés et éliminés (« dents ») ; aucune vérification bloquée par la garde ; bac à sable actif ; aucun
   appel au-dessus de la réserve du relais. 136 appels, 5,89 USD, de 15:37:35 à 15:42:20 UTC.
2. **La condition (i) de la porte P3 est remplie** : la plomberie réelle passe sans incident. Restent (ii) des dents sur
   la banque v3 en simulation et (iii) mon devis.
3. **Réserve (R4)** : le résultat est propre parce que le monde est tautologique — la loi d'un témoin vrai est la loi du
   monde (log W de 74 et 84). Cela montre que la machine laisse passer un vrai, pas que le juge trouve un effet difficile.
   Deux témoins vrais seulement, même monde que (a).

## Les lectures fixées

| lecture | attendu | observé |
|---|---|---|
| L1 erreurs de l'orchestrateur | aucune | **0** (8 fiches à lancer en génération 0, dont une renvoyée hors budget ; 4 en génération 1) |
| L2 témoins vrais jugés, `etat_dents` | au moins un | **2 jugés, 2 promus** (S-V1 : log W 73,9 ; S-V4 : 84,2) ; « dents » |
| L3 témoins faux promus | aucun | **0** sur 2 jugés (S-F4, S-F1) |
| L4 vérifications bloquées par la garde | au plus une | **0** : aucune réponse de vérificateur ne parle de refus, de garde ou de blocage ; 11 rejeux confirmés sur 11 |
| L5 bac à sable | actif | **actif** (manifeste et bilan : « bwrap et socat présents ; bwrap s'exécute, réseau isolé ») |
| L6 relais | dépassements comptés | **0** appel au-dessus de la réserve de 0,40 (le plus cher : 0,245) ; Opus 5.5 79 appels, 2,09 USD ; Fable 5.1 57 appels, 3,80 USD |

## Dans l'autre sens : l'audit d'un résultat propre (R4)

- **Rien de l'orchestrateur dans les dossiers des agents** : aucun `reponse.txt`, `consigne.txt` ni `lecons.json` dans un
  dossier `experience/` ; les traces sont dans les dossiers voisins `traces-…`.
- **Issues conformes aux dépôts du noyau** : 11 fiches sur 11. Graines du noyau écrites après les évaluations (deux
  générations).
- **Vérifications** : chaque vérificateur dit avoir rejoué le code et reproduit exactement les tirages déclarés
  (empreintes d'ordre recalculées) ; aucun verdict de « confirmation par lecture ».
- **Règle e-BH** : m = 7 puis 4 ; les e-valeurs retenues sont arrêtées juste au-dessus de log(m/α) (5,03 à 5,14 pour un seuil
  de 4,94 ; 4,78 et 5,49 pour 4,38) : c'est la construction (arrêt au premier franchissement), pas une coïncidence.
- **Leçons de la mémoire** : elles parlent maintenant de science (« une intuition plausible ne suffit pas : il faut un
  effet assez fort… »), plus de fichiers.
- **Une fiche « hors budget »** en génération 0 (G0-F08) : le plafond de génération (7,5 USD, la moitié de 15) réserve le
  pire cas par fiche (1,00 + 0,50) ; la huitième n'a pas trouvé de place, elle a été rejouée en génération 1 et promue.
  Pas un défaut (le plafond tient) ; une inefficacité à connaître pour dimensionner (prévoir 1,5 USD de réservation par
  fiche et par vague).
- **La fille de la génération 1** (G0-F05 × G0-F07) est passée par la garde de redite cette fois et a été éliminée (log W
  −135 sous le nul des filles v2) ; deux filles de fin de course n'ont pas été jouées (nombre de générations atteint).

## Suite

- P3 : (ii) se jouera sur la banque v3 (couche 1 bis), en simulation, après la correction du défaut de témoins que
  signale le collisionneur (témoins vrais et nul informé ajustés sur les mêmes 40 épisodes : voir mon message n° 113).
- Le premier monde non tautologique avec de vrais agents reste la couche 1 (banque réelle) : devis après (ii).
