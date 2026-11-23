# Fiche de lecture — 2307.09476 v3 — « Overthinking the Truth: Understanding how Language Models Process False Demonstrations »

- **Auteurs** : Danny Halawi, Jean-Stanislas Denain, Jacob Steinhardt (Berkeley), conférence ICLR 2024 ; arXiv 2307.09476 v3.
- **PDF** : `docs/sources/pdf/mecanisme-adjudant-v1/2307.09476v3.pdf`, sha256 `f58b18ba38cea49b751a61cb5e3d8f1876f291854568502a1cf2ecb778b0b433` (recalculée, concorde avec le registre, R11).
- **Décision lue** : `docs/decisions/contre-lecture-decision-N-075-v1.md`, l. 131 (correction C7, l. 155 de N-075 v1) ; usage vérifié dans la v3 en vigueur (`decision-N-075-issue-plancher-et-deux-regards-v3.md`, l. 169, 173, 215), non touché par ses errata 1 à 3.
- **Lecteur** : Claude Opus 5.5, effort élevé. **Date** : 2026-11-23T08:46:50Z.

---

**(a) Ce que le papier établit.** Sur une tâche de classification où les démonstrations du contexte portent des étiquettes fausses, la justesse décodée couche par couche (lecture du flux résiduel par la « lentille des logits ») est la même pour démonstrations justes et fausses jusqu'à une « couche critique », puis diverge (p. 1 du PDF). Les auteurs posent en conjecture que le modèle « knows the right answer, but imitates and says the wrong answer » (p. 1). Cinq têtes d'attention tardives qui recopient le faux (1 % des têtes), une fois retirées, réduisent l'écart de justesse de 38,9 % en moyenne sur 14 jeux, 32,6 % sur Financial-Phrasebank (p. 2). Huit modèles préentraînés, de 410 millions à 20 milliards de paramètres, dont Llama-2-7B (p. 3) ; pour GPT-J, la divergence se fait entre les couches 13 et 14 sur tous les jeux sauf deux (p. 6). Limite dite : classification, beaucoup d'exemples faux (p. 9).

**(b) Ce que voulait la décision.** La ranger parmi « ce qui n'est pas revendiqué, et par qui c'est pris » : la signature « sait, puis dit autre chose ». **Le permet** : la forme est publiée, et prolongée par Belrose et al. à la détection d'injections (p. 2, 9). Au sens de R8, l'absence de sabotage et d'agent dans ce papier est sa limite, non un trou : appliquer la couche critique au saboteur reste une question, jamais une première. Réserve : la « connaissance » y est une conjecture, mesurée par décodage, non établie.

**(c) Usage.** Pour l'entretien : si l'on demande « vos sondes lisent-elles que l'agent sait ? », ce papier donne l'antériorité honnête et l'épreuve (justesse décodée par couche, ablation de têtes), sans rien promettre sur nos organismes. Pour le billet sur les lentilles : il fonde l'emploi « suivre la bonne action connue et non émise » (réponse du concepteur, § 2.4, l. 57) et sa base nommée, la lentille des logits sans apprentissage.

**(d) Plus petite action.** Porter dans la prochaine version de N-075 les pages 2, 3 et 6 à côté de la page 1 (table de provenance, point 5), et écrire « conjecture » à côté de « sait ». Coût : un quart d'heure de session, aucune dépense.
