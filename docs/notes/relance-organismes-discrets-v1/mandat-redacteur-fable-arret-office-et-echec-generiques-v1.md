# Mandat du rédacteur Fable — arrêt d'office sous 80 actions relues, et effet de l'échec des contrôles génériques — bras A — v1

Écrit le 2026-11-22 par la session de relance du bras A (branche `claude/pensive-bardeen-1fv7hw`), sur le mot de Lazar inscrit en GO-2026-11-22-90 (texte exact de la question et de la réponse : `registres/passations/2026-11-22-1643-additif-3-mere-bras-a.md`, `851809dbff5485abc60cf078723aaf5a06fb99387987e7d90e7bba38ad1fd0ab`). Rédacteur : Claude Fable 5.2, session neuve, dans l'abonnement. Langue : français. Nomme les choses par ce qu'elles sont, pas par un sigle seul.

Ce travail entre dans la liste de « Économie de Fable » (CLAUDE.md) : critères de décision et issues d'un préenregistrement.

## Ce que tu fais (deux choses, rien d'autre)

### 1. Écrire l'arrêt d'office sous 80 actions relues — décidé par Lazar, tu écris la règle
La règle « Effectif insuffisant » des actions d'épreuve relues (6.8, ligne 846) met le plancher à 80 par classe. Sous 80, le lot décisif n'est pas construit et la ligne A10 (« Lecture décisive invalide : rien n'est conclu », ligne 1014) s'applique. Or les deux comptes sont connus dès que l'épreuve en vigueur l'est, à l'étape (i), **avant la distillation**. Le texte va pourtant jusqu'au bout de la course alors que l'issue est déjà certaine. Lazar a accordé un **arrêt d'office** : quand une classe compte moins de 80 actions à l'étape (i), la course s'arrête là, sans dépense de plus.
Tu écris : où l'arrêt joue (étape, liste d'arrêt 8.1 ou 8.2, ordre 6.3, devis 6.11 au besoin) ; ce qui est scellé ; l'issue rapportée (A10, ou une issue nommée si le libellé de A10, qui suppose une lecture faite, ne convient pas — dis-le et justifie) ; ce qui n'est pas dépensé. Aucun seuil changé : le plancher reste 80.

### 2. Point renvoyé par Lazar : ce que l'échec des contrôles génériques plantés change aux verdicts
Ligne 806 : « Les contrôles génériques plantés ne gardent que la mesure des génériques (7.5) » ; sous 32, « son échec ne touche que la mesure des génériques ». Le texte n'écrit pas **ce que cet échec change aux verdicts de cette mesure** : mesures secondaires « hausse des contrôles génériques établie ou non » (ligne 1056), ligne B10 (ligne 1035), seuil de la ligne 648, prédiction (ligne 608). Lazar n'a pas tranché le fond : il te renvoie le point. Tranche-le par une règle, si elle ne change aucune issue du verdict principal ; si ta règle change une issue, écris-la quand même, marque-la **« nœud de Lazar »** avec deux ou trois options (avantage, inconvénient), ta recommandation et ta confiance. Le sens le plus prudent est attendu ; aucune règle choisie pour faire passer une épreuve (R3).

## Hors de ton mandat — ne pas trancher
- Les épreuves sans plancher et la corrélation du plan tronqué.
- L'épisode sans plan parmi les 896 plans, et l'absence d'action donneuse d'une autre tâche.
- Les planchers eux-mêmes : confirmés par Lazar tels quels (inscrits au brouillon 51, fin de la règle « Effectif insuffisant », ligne 806).
Si l'un d'eux te bloque, dis-le dans ta note sans l'écrire.

## Pièces à lire (rien d'autre n'est nécessaire)
1. `CLAUDE.md`, en entier.
2. Le texte : `prereg/T0.7-organismes-discrets-v-a-v2-brouillon51.md` (`6de63aabf773559b43574b25737b4b93f1d87ab3665603c462da1627cbaa97bf`) : 6.3 à 6.8 (lignes 749 à 851), 6.11, « Seuil » (ligne 632 et suivantes), « Critères de lecture gelés » (lignes 980 à 1081), « Liste d'arrêt » (lignes 1082 à 1238), et les lignes citées plus haut.
3. Tes règles d'effectif : `docs/notes/relance-organismes-discrets-v1/quatre-regles-effectifs-fable-v1.md` (`df0d2a7e6d1770fe19a87a0fde6f9d70263823bec0ce63659fa5d53d4983f24d`).

## Interdits
- Ne change aucun seuil, aucune prédiction, aucune règle d'admission (lignes 542 à 550), aucune issue hors des deux points ; rien hors des sections nommées sauf une ligne neuve de garde en 8.4 si l'arrêt l'exige (dis-le).
- Cloisonnement : n'ouvre, ne liste, ne cherche ni n'empreinte `bases/`, `sondes/`, tout chemin dont un élément commence par `t07`, rien de T0.8 ; `scripts/mots_et_cout_*`, `prereg/T0.6-organismes-v0-v1.md` ; `docs/notes/bras-a-moniteurs-v1/`, `docs/notes/bras-a-contre-lecture-habilitee-v1/`, `docs/notes/bras-a-sans-interne-v1/` ; `src/controle_ia/organismes_discrets/bras_a_v2_habilite*/`, `autres_moniteurs_v*` ; `runs/` ; `docs/sources/` ; `registres/` (sauf l'additif cité plus haut) ; tout fichier « consigne-privee » ou « conception-ii-b » ; `archives-reponses-modeles/`. Le texte cite des chemins cloisonnés : tu ne les suis pas.
- Aucun réseau, aucune clé, aucune dépense.

## Rendu attendu
Sur une branche à toi, `relance-bras-a/arret-office-generiques-v1`, un seul fichier scellé (`PYTHONPATH=src .venv/bin/python -m controle_ia.scellement sceller FICHIER`) :
`docs/notes/relance-organismes-discrets-v1/arret-office-et-echec-generiques-fable-v1.md`, qui contient :
1. Un bloc JSON `{"operations": [{"type": "remplacer", "ligne": n, "ancien": "…", "nouveau": "…", "raison": "point 1|point 2"}, …]}` : couples **ancien / nouveau mot pour mot**, chaque `ancien` copié à l'identique d'une ligne du brouillon 51 et présent **une seule fois** dans cette ligne ; `{"type": "inserer_apres", "ligne": n, "texte": "…"}` seulement si une ligne neuve est nécessaire. Donne l'empreinte sha256 du texte obtenu après application.
2. Une note de 400 mots au plus : ce que tu as écrit pour chaque point et pourquoi ; pour le point 2, règle tranchée ou nœud de Lazar (options, recommandation, confiance) ; ce que tu n'as pas pu trancher.
Ne committe que ce fichier et son compagnon ; pousse ta branche ; ne touche pas au texte lui-même : la session de relance applique tes couples par programme, puis un contre-lecteur neuf d'un autre modèle les contre-lit.
