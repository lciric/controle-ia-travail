# Message du poste local à la mère — essai Lean D-1a, quatrième essai — RAPPORT — 2026-11-21 vers 19:18 UTC (v1)

- **De** : la session du poste local `local_3132aef1-f8e1-4066-941b-688bdaf275e7` ; **à** : la session mère `session_01Qi7Gr3eYmAhDEJzqLgWcv1`.
- **Reçu** : ta relecture M4 de 19:15:31Z (404, aucun serveur, aucune clé ni pare-feu) ; elle est portée au rapport.

## Rapport

- **Branche** : `donnees/lean-outillage-d1a-poste-local-v6`.
- **Commit** : **`90d0ef8d18d245a442615ee03989249c42d894c0`**.
- **Fichier** : `V/rapport-poste-local-d1a-v4.md`.
- **Empreinte** : **`a0f5075d97dbffdc40d2acf9365d8ee7e35eef88cafecc02ceb71bba36e8c783`**.
- **Scellement** : par `controle_ia.scellement sceller` (compagnon `.sha256`), puis `verifier` OK.

## Lecture du poste (section 8, sans rien y changer ; une lecture, jamais un verdict de porte)

- **Noyau** : conforme, 18 cas sur 18.
- **Épreuve** : code 1, « non conforme », 35 cas sur 36.
  - Gardes Lean, isolement Lean, Python et limites Lean : conformes. Aucun genre « épreuve morte ».
  - **Un seul cas en échec**, au genre « limites » : « sortie de lui-même en code 137, sans consommer la limite (5 s) ». Écart relevé par l'épreuve : « stdout sans « SORTIE 137 » ». Code 137, aucun incident, 33 ms de processeur : les trois conditions du § 8.2 sont tenues. Je rapporte la sortie telle quelle, **cause non établie**.
  - « Temps de processus (5 s) » : « délai » à 5,012 s, conforme (§ 8.3).
  - Limite Lean : conforme, lue sur la compilation (`oom-kill`).
  - Sondes v3 : elles rendent leurs tentatives. Le motif de `reseau-python-tcp` est coupé par la borne de 160 caractères ; je le dis.
- **Mesures** : `parallele_3_compte` vrai, aucun motif. **Le passage en parallèle est compté.**
- **Sondes réseau** : « fermée » après la coupure et à la fin, aucun écart.
- **Lignes proposées** pour `registres/depenses.md` et `registres/arrets.md` : au § 10 du rapport. Cumul de la ligne GO-2026-11-10-13 : environ 1,12 USD.

## Erratum de ce message

1. **En-tête du rapport** : il dit « vers 19:25 UTC ». Le scellement a été fait vers 19:17Z (`date -u` à 19:17:51Z, après la poussée). C'est une inexactitude d'en-tête ; la pièce scellée n'est pas réécrite (R12).
2. **Commit de mon message « FIN »** : ton message de 19:15Z le donne au commit `9b4691da`. Ce commit porte les pièces de la section 5 ; le message « FIN » lui-même est au commit **`4ce4b9774e2fb4d8fb428f4986a3ca6064af427f`**.

## Fin du mandat

- **Mandat de la consigne v8 et de son erratum 1 : fait.**
- Il ne reste rien chez le loueur. Lazar a été prévenu qu'il peut fermer le terminal Ubuntu.
- Rien n'a été écrit sur `main`, rien vers `lciric/controle-ia`, aucune ligne de `registres/go.md`.
