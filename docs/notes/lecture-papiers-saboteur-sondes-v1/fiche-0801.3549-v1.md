# Fiche de lecture — 0801.3549 — v1

- **Titre** : The Danger Theory and Its Application to Artificial Immune Systems (actes de la conférence ICARIS 2002, p. 141-148).
- **Auteurs** : Uwe Aickelin, Steve Cayzer. **Identifiant** : arXiv 0801.3549 v3.
- **PDF** : `docs/sources/pdf/mecanisme-adjudant-v1/0801.3549v3.pdf`, sha256 `2ed1982884f0d272e182b22f8b49f89db76697de0ca4ca317a3ddad138badad0` (vérifiée par `sha256sum`, 8 pages).
- **Décision lue** : `docs/decisions/decision-N-075-issue-plancher-et-deux-regards-v1.md`, ligne 112 ; puis la v3 (section 4, l. 108-130) et ses errata 1 à 3, le 3 v2 primant (point 8 retenu).
- **Lecteur** : Opus 5.5, effort élevé. **Date** : 2026-11-23T08:45Z (`date -u`).

## (a) Ce que le papier établit

C'est un papier de concepts, sans expérience ni chiffre. Les auteurs ne défendent pas la théorie du danger, qu'ils disent « still controversial » (p. 1 du PDF). Le système immunitaire ne répondrait pas au non-soi mais au danger (p. 2). La loi 1 exige deux signaux ensemble : reconnaissance du motif et co-stimulation. Le premier signal reçu seul tue la cellule qui reconnaît, c'est la tolérance (p. 3). Les antigènes voisins du dommage « are not necessarily the culprits » (p. 3). En détection d'anomalies, la proximité est « a proxy measure for causality » (p. 6), et la présence de non-soi figure parmi les signaux de danger possibles (p. 6). Tout dépend du choix du signal de danger, choix aussi critique que celui de la fonction d'adaptation d'un algorithme évolutionnaire (p. 7).

## (b) Ce que voulait la décision, et si le papier le permet

La v1 lisait la règle « alerte = nouveauté et preuve de dommage ; nouveauté seule = mise à jour des témoins » comme « occupée dans sa forme ». La v3, sur la lecture entière de ce PDF, a corrigé : la première clé est un motif reconnu, pas la nouveauté, et la forme a été retenue (erratum 3 v2, point 8 a). **Le papier le permet** pour la forme à deux signaux, qui est publiée, et seulement pour elle. Il ne permet pas de dire la règle prise en contrôle des agents : il ne contient aucune mesure, et la pièce de 2026 sur les cellules dendritiques reste absente du dépôt (R8 : zone séduisante, question ouverte).

## (c) Usage pour l'entretien et pour le billet

Il prévient l'objection « votre règle à deux clés est neuve ? » : non, sa forme a vingt-quatre ans. Il fournit une épreuve, puisque sa tolérance est aussi la voie par laquelle un saboteur se fait accepter. Le témoin « motif sans dommage, jamais dans les témoins » du banc en sort. Pour le billet, il donne une phrase : une sonde aiguille vers le lieu du dommage, et les voisins du dommage ne sont pas forcément coupables (p. 3).

## (d) Plus petite action

Ajouter la page 3 (« not necessarily the culprits ») aux citations du point 3 dans la prochaine version de la note d'entretien, si la règle y est nommée. Coût : dix minutes de session, aucune dépense.
