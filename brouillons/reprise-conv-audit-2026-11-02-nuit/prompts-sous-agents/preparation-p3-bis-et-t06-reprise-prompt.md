Tu reprends un travail interrompu. Lis d'abord la consigne d'origine, qui fait foi pour le fond : `/home/claude/controle-ia-travail/brouillons/passation-conv-audit-2026-11-02-soir/prompts-sous-agents/preparation-p3-bis-et-t06-prompt.md` (courses P3-bis, témoin positif planté, GO-2026-11-02-29 ; et T0.6, organisme v0 et test croisé d'étiologie, GO-2026-11-02-28). Tu n'as écrit aucun des fichiers que tu vas lire.

## Ce qui s'est passé
Le sous-agent précédent s'est arrêté le 2 novembre vers 20:29 UTC, sans rapport (probablement faute de crédits). Ses fichiers ont été committés tels quels, **jamais vérifiés** :
- `brouillons/P3-bis-temoin-positif-v1/` : `P3-bis-consignes-v1-brouillon1.md`, `P3-bis-preenregistrement-v1-brouillon1.md`, `P3-bis-temoin-positif-config-v1-brouillon1.json`, `puissance_p3_bis_v1.py` et sa sortie `puissance-p3-bis-v1.txt` ;
- `brouillons/T0.6-organismes-v0-v1-brouillon2-pieces/` : `puissance_t06_v1.py` et sa sortie `puissance-t06-v1.txt` ;
- copies de travail dans `brouillons/passation-conv-audit-2026-11-02-soir/travail-interrompu/p3-bis-partiel-2020/` et `…/p3-bis-t06-partiel-2021/`.

## Ce que tu fais
1. **Vérifie** ces fichiers contre les sources que cite la consigne d'origine (texte scellé de P3, ses consignes, sa configuration, sa chaîne de lancement, ses addenda, le code) : chaque chiffre, chaque chemin, chaque empreinte. Rejoue les calculs de puissance (`nice -n 10 python3 -I -B …`) et dis s'ils sont justes et s'ils reposent sur des variances lues sans ouvrir les données tenues à l'écart.
2. **Reprends ou recommence**, à ton jugement. Tout fichier changé prend un nom neuf (règle R12 : `…-brouillon2…` pour un brouillon 1 corrigé ; `puissance_p3_bis_v2.py` pour un script corrigé) ; les fichiers existants ne sont jamais modifiés.
3. Termine les deux livrables de la consigne d'origine : le préenregistrement de P3-bis (avec critères de lecture gelés et les deux issues, liste d'arrêt sans couperet de temps, puissance, devis, ce que le code doit changer) en priorité ; puis le brouillon 2 de T0.6 (`brouillons/T0.6-organismes-v0-v1-brouillon2.md`, fichier neuf).
4. Écris un rapport neuf `brouillons/P3-bis-temoin-positif-v1/rapport-preparation-p3-bis-t06-v1.md` : ce que tu as vérifié et trouvé dans le travail précédent (erreurs comprises), ce que tu as écrit, chemins et sha256 des fichiers neufs, pour chaque course ce qui est prêt et ce qui manque (code, données, décision de Lazar), devis, et dix lignes pour un contre-lecteur neuf.

## Règles (celles de la consigne d'origine, plus celles-ci)
- Aucun commit, aucun fichier `.sha256`, aucun fichier existant modifié, rien lu ni écrit sous `donnees/` (référence par chemin et empreinte seulement), aucune branche `calcul/…`, aucune ref `donnees/*`, aucun `git fetch`, `checkout` ni `stash`, aucun appel de réseau ni de modèle, `nice -n 10`. La machine a deux cœurs et une course décisive y tourne : reste sobre (pas de suite d'essais complète du dépôt).
- Tes fichiers de travail temporaires sous `/home/claude/scratch/p3-bis-t06/`.
- Toute heure vient de `date -u`. Français, sans sigle non développé.
- Réponse finale : chemins et sha256 des fichiers neufs ; erreurs trouvées dans le travail précédent ; pour chaque course, prêt / manque / devis ; dix lignes pour le contre-lecteur.
