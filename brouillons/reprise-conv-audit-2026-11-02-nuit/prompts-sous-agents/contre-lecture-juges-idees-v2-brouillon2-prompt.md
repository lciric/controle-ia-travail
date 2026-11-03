Tu es un contre-lecteur neuf (règle R2) : tu n'as écrit ni l'étage des juges d'idéation, ni le protocole v2, ni ses brouillons 1 et 2, ni la contre-lecture du brouillon 1. Français, sans sigle non développé ; heures par `date -u`.

## Objet
Juges modèles de langage de l'idéation, version 2 (GO-2026-11-02-32, 60 USD ; lis la ligne en entier : `grep '| GO-2026-11-02-32 |' /home/claude/controle-ia-travail/registres/go.md`), **brouillon 2** et code, commit public `3e7ca5c`, dans `/home/claude/ideation-organism/orchestrator/` :
- `prereg/preenregistrement-juges-idees-v2-brouillon2.md` (`c1df7e91…`) ; brouillon 1 `prereg/preenregistrement-juges-idees-v2-brouillon1.md` ;
- code : `pole/juges_idees_v2.py`, `essais/test_juges_idees_v2.py`, `essais/mutations_juges_idees_v2.py`, `demonstrations/validation_juges_idees_v2.py` (comparer à `c15a073` : `git diff c15a073 3e7ca5c -- <fichier>`) ;
- rapport du développeur `prereg/rapport-redaction-juges-idees-v2-brouillon2.md` (ses dix points d'abord, et la section 10) ;
- contre-lecture du brouillon 1 `prereg/contre-lecture-preenregistrement-juges-idees-v2-v1.md` (`1dc3c194…`) et ses 40 couples `prereg/couples-contre-lecture-juges-idees-v2-v1.json`.

## Questions
1. B1 (témoins séparables sans tables), B2 (statuts du relais lus comme réponses), B6 (choix des juges), B7 (gardes sans essai sur un artefact), la puissance (15 contre 15 par classe, trois mondes) et les trois décisions du directeur (plafond 60 USD exact, garde 48 h, bras « ancien protocole sans dossier ») : levés ? Chacun avec un essai sur un cas sain et sur un artefact (R5) et une mutation tuée pour la bonne raison ?
2. Une panne, un refus ou un quota d'un juge peut-il rendre la course non concluante « par défaut de conception » (exigence de Lazar) ? Lis la règle écrite d'avance pour les comparaisons perdues.
3. Prédictions chiffrées et signées, ouvertes dans les deux sens ; critères de lecture gelés avec l'issue « le nouveau protocole ne fait pas mieux » ; audit de symétrie ; graines depuis l'empreinte du texte scellé ; devis par juge (Astra non mesuré : borne prudente ?) ; plafond du texte exactement 60 USD.
4. Les couples du brouillon 1 : lesquels sont appliqués, lesquels refaits, et les raisons tiennent-elles ?
5. Marqueurs restants : seulement GO si nécessaire, configuration, empreintes du code au commit, `<<EPREUVE_ASTRA_8807>>` ?
6. Ce que le patch interrompu a laissé de faux ou d'inachevé.

Tu peux rejouer : `cd /home/claude/ideation-organism/orchestrator && TMPDIR=/tmp POLE_ESSAI_BAC_REEL_NON_JOUE=1 nice -n 10 python3 -I -B -m pytest -q -p no:cacheprovider essais/test_juges_idees_v2.py`, le banc de mutations **une fois**, une course à blanc dans un dossier sous `/home/claude/scratch/juges-v2/contre-lecture/`. N'ouvre pas `../resultats/banc-tricheurs-v9-validation-v1/`.

## Rendu
Fichiers neufs : `orchestrator/prereg/contre-lecture-preenregistrement-juges-idees-v2-v2.md` (verdict en trois lignes : scellable, scellable après couples, ou non scellable ; bloquants, importants, mineurs) et, s'il y a des corrections de texte, `orchestrator/prereg/couples-contre-lecture-juges-idees-v2-v2.json` (`{"ancien","nouveau"}`, chaque « ancien » présent une seule fois). Aucun commit, aucun `.sha256`, aucun fichier existant modifié, rien sous `donnees/`, aucun `git fetch`/`checkout`/`stash`, aucun appel de réseau ni de modèle, `nice -n 10`. Réponse finale : verdict, points une ligne chacun, chemins et sha256.
