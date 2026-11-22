# Erratum 1 du code de l'audit après coup, v2 (classe B)

- **Date** : 2026-11-22, vers 14:00 UTC. **Auteur** : session des chantiers du 21 (Opus 5.5), qui consigne. Erratum de classe B, selon l'allègement de la procédure (GO-2026-11-19-26).
- **Vise** : `src/controle_ia/audit_apres_coup_v2/` (rapport v2 `6947c180…`), après la vérification du même contre-lecteur, `verification-code-audit-apres-coup-v2-opus-v1.md` (`ac1d304a…`), qui rend « conforme après corrections ». Vingt constats sur vingt et un sont fermés ; I-9 est renvoyé au concepteur.
- Les fichiers scellés de la v2 ne sont pas réécrits (R12). La correction r-1 se porte à la prochaine version du paquet. D'ici là, cet erratum la déclare.

## r-1, mineur : l'artefact de l'épreuve 1 ne plante pas le cas visé par I-1

Dans `src/controle_ia/audit_apres_coup_v2/epreuves_boucle.py`, fonction `epreuve_1`, correction mot pour mot donnée par le contre-lecteur :
- remplacer `_episode(h, entropie, 2, "verdict", "porte_A", organisme="org_porte")` par `_episode(h, entropie, 2, "verdict", "porte_A", organisme="org_verdict")` ;
- remplacer `_episode(h, entropie, 7, "flux", "flux_F", bras="flux_1", organisme="org_porte")` par `_episode(h, entropie, 7, "flux", "flux_F", bras="flux_1", organisme="org_verdict")`.

Raison : `org_porte` est déjà refusé comme organisme de porte. Le cas que la v1 laissait passer, un organisme de verdict qui n'est pas un organisme de porte, n'est donc pas planté. Le contre-lecteur a essayé la correction dans une copie : les essais passent, et ils cassent si l'on retire la garde I-1.

Portée : la garde I-1 est appliquée par le code (`harnais_simule.py`, l. 206-208). Seul l'essai qui la prouve est trop faible. D'ici la prochaine version, la garde I-1 se lit « appliquée, non prouvée par un essai de l'épreuve 1 ».

## Écarts acceptés par le contre-lecteur, consignés ici (points ouverts 1 et 10)

- **Point 1 : clé de graine.** La spécification demande une clé par épisode. Le simulateur vectorisé tire un flux par monde, tâche et canal, dans un espace nommé depuis I-4 ; l'épisode est son rang dans ce flux. La reproductibilité est entière, et aucune collision n'existe entre espaces (essai de I-4). Écart d'écriture, accepté.
- **Point 10 : loi de score « signal ».** Pour l'épreuve 4, le développeur a ajouté au monde planté une loi de score « signal », que la spécification ne nomme pas. C'est la seule manière de planter « signalés audités une fois sur deux ». Écart d'écriture, accepté ; il est déclaré dans la docstring de la v2.

## Ce qui reste ouvert, renvoyé au concepteur

Les points ouverts 2, 3, 4, 9, 11 et 13, la part renvoyée du 14, un membre du 16, et le constat I-9 (le pli consommé et la clause 4 de la boucle).
