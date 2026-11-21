# Complément 1 v5 à la pièce de contrôle du lancement du palier 0b (essai 5, à condition suspensive) — extraction v1

- Source : `docs/notes/organisme-noeuds-2026-11-21-v1/reponses-fable-noeuds-organisme-v1.md` (sha256 `dd4e1ccc53dbe142a4a64ae054114dd17feec20f07eb9d050d9de714ac3ed587`), sur main.
- Section : § 1.5 (compléments 1 v4 et 1 v5, scellés d'avance, à condition suspensive).
- Retenu par la mère, décision de routine, R-4573.
- Extrait à l'octet par programme le 2026-11-21T14:48:35Z (`date -u`), sans aucun changement ; conçu par Claude Fable 5.2.
- Note d'extraction : La pièce ne donne pas de texte assemblé de la v5 : elle donne la règle de dérivation depuis la v3 et le paragraphe de tête. Les deux sont extraits à l'octet ; aucun assemblage n'est fait ici. Pour la v5, le crochet « [3 ; pour la v5 : 4] » se lit 4.

<!-- lignes 130 à 130 de la source : règle de dérivation depuis la v3, à l'octet -->

Même texte que la v3, avec le dossier `etapes-3-a-6-essai-4` (puis `-essai-5`), le dossier de tenue `/home/user/journaux-palier-0b-essai-4-v1/` (puis `-essai-5-v1`), la branche `recuperation/palier-0b-programme-1-essai-4-v1` (puis `-essai-5-v1`), et ce paragraphe en tête, à la place du constat :

<!-- lignes 133 à 142 de la source : paragraphe de tête, à la place du constat, à l'octet -->

## Condition de validité de ce complément

Ce complément est scellé d'avance. Il ne vaut que si l'essai [3 ; pour la v5 : 4] a été coupé par un redémarrage de la machine, et l'organisme le constate par écrit, dans une pièce scellée avant la relance, sur ces cinq points :
1. l'identifiant de démarrage de la machine diffère de celui écrit au lancement de l'essai coupé ;
2. le fichier code-de-sortie.txt de l'essai coupé n'existe pas ;
3. aucun fichier arret.txt n'existe dans le dossier de l'essai coupé, et son journal ne porte aucune trace d'exception (aucune ligne qui commence par « Traceback ») ;
4. le dossier de l'essai coupé est inventorié (noms, tailles, empreintes), l'inventaire est poussé sur sa branche de récupération, et le dossier reste intact, sauf libération permise au point 4 du complément 1 v3 ;
5. la règle de départ du complément 1 v3 (place projetée plus 4 Go) est tenue, la projection étant refaite sur l'essai coupé.
Si un seul point manque (processus absent sans redémarrage, code de sortie écrit, fichier d'arrêt, trace d'exception au journal, place insuffisante) : aucune relance ; inventaire, et retour à la mère. Après l'essai 5, aucune relance sans un mot neuf : trois coupures de suite sont un nœud.
Aucune de ces conditions ne lit une sortie du palier. Tous les essais sont rapportés au complément qui suit et au registre.
