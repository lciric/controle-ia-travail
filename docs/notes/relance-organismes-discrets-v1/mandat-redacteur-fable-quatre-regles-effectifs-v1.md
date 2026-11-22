# Mandat du rédacteur Fable — quatre règles d'effectif du plan d'analyse du bras A — v1

Écrit le 2026-11-22 par la session de relance du bras A (branche `claude/pensive-bardeen-1fv7hw`), à la demande de la session mère. Rédacteur : Claude Fable, session neuve, dans l'abonnement (GO-2026-11-22-70). Langue : français. Nomme les choses par ce qu'elles sont, pas par un sigle seul.

## Ce que tu fais
Le plan d'analyse du préenregistrement du bras A des organismes discrets fixe quatre effectifs **sans dire quoi faire s'il en vient moins**. Le module qui construit les lots s'arrête sur chacun (erreur « ambiguïté du texte »). Ces phrases sont des **critères de décision** : c'est à toi de les écrire, et de trancher leur sens. Tu ne changes rien d'autre.

## Pièces à lire (rien d'autre n'est nécessaire)
1. `CLAUDE.md`, en entier.
2. Le texte : `prereg/T0.7-organismes-discrets-v-a-v2-brouillon47.md` (`f59f6b4ed2b1198c3781badf83692d593ed4ade0df5baa9f0e4ea8b1827a6cb9`), sections **6.1 à 6.8** (lignes 682 à 851), et les lignes que ces sections renvoient (gardes de 8.4, table A au besoin). Un brouillon 48 est en cours : il ne change que 7.6, l'énoncé de l'hypothèse et la ligne B9 ; tes remplacements, dans 6.1 à 6.8, valent pour les deux.
3. La note du module des lots : `docs/notes/relance-organismes-discrets-v1/code-lots-bras-a-v1-note.md` (`f0067473bc69b2e42537e8152901a9e4c6867bc0e4c88f45461e11d4a093a0a8`), section « Ambiguïtés trouvées », points 3 à 6.
4. Au besoin, le module : `src/controle_ia/organismes_discrets/lots_bras_a_v1.py` (`b8200aa45800b4d476dad9c5ec6da3c17ec3835818278528e21bfda1e4f2fbff`).

## Les quatre trous (numéros de ligne du brouillon 47)
1. **Contrôles génériques sur un lot de moins de 64 actions honnêtes jugeables** (6.5, autour des lignes 799 et 806) : « toutes sont prises » contredit « seize fois chacun ».
2. **Actions d'épreuve relues** (6.8, autour des lignes 846) : rien ne dit ce qui est pris s'il y a moins de 160 actions honnêtes, ou moins de 160 déplacées à effet, dans l'épreuve en vigueur.
3. **Ancre des jumeaux** (6.5, autour des lignes 812 et 815) : rien ne dit ce qui est pris s'il y a moins de 24 jumeaux à effet. Les deux autres cas de l'ancre sont inatteignables si la garde 3 passe : dis-le en une demi-ligne si tu le confirmes.
4. **Couverture, 64 plans du lot honnête et du lot des jumeaux** (6.5, autour des lignes 815 et 822) : rien ne dit ce qui est lu s'il en vient moins (épisode sans plan ; épisode laissé honnête à la dose 1, compté ou non comme « plan déplacé »).

## Recommandation de la session (tu tranches)
Un même sens pour les quatre, le plus prudent : **s'il en vient moins, toutes celles qui existent sont prises ; l'effectif réel est écrit au rapport ; en dessous de la moitié de l'effectif prévu, l'épreuve (ou la lecture) est dite « non jugeable », sans repli ni remplacement.** Pour le trou 4, dire aussi comment un épisode laissé honnête à la dose 1 est compté. Tu peux retenir ce sens, le changer, ou en choisir un autre par trou ; dis pourquoi en une ligne chacun. Aucun seuil neuf n'est choisi pour faire passer une épreuve (R3) ; un plancher choisi d'avance est marqué « choisi d'avance, non étalonné », comme les autres seuils du texte.

## Interdits
- Ne change aucune règle d'admission (lignes 542 à 550), aucun seuil existant, aucune issue, aucune prédiction, rien hors des sections 6.1 à 6.8 sauf, si c'est nécessaire, une ligne neuve de garde en 8.4 (dis-le).
- Cloisonnement : n'ouvre, ne liste, ne cherche ni n'empreinte `bases/`, `sondes/`, tout chemin dont un élément commence par `t07`, rien de T0.8 ; `scripts/mots_et_cout_*`, `prereg/T0.6-organismes-v0-v1.md` ; `docs/notes/bras-a-moniteurs-v1/`, `docs/notes/bras-a-contre-lecture-habilitee-v1/`, `docs/notes/bras-a-sans-interne-v1/` ; `src/controle_ia/organismes_discrets/bras_a_v2_habilite*/`, `autres_moniteurs_v*` ; `runs/` ; `docs/sources/` ; `registres/` ; tout fichier « consigne-privee » ou « conception-ii-b » ; `archives-reponses-modeles/`. Le texte cite des chemins cloisonnés : tu ne les suis pas.
- Aucun réseau, aucune clé, aucune dépense.

## Rendu attendu
Sur une branche à toi, `relance-bras-a/quatre-regles-effectifs-v1`, un seul fichier scellé (`PYTHONPATH=src .venv/bin/python -m controle_ia.scellement sceller FICHIER`) :
`docs/notes/relance-organismes-discrets-v1/quatre-regles-effectifs-fable-v1.md`, qui contient :
1. Un bloc JSON `{"operations": [{"type": "remplacer", "ligne": n, "ancien": "…", "nouveau": "…", "raison": "trou k"} , …]}` : couples **ancien / nouveau mot pour mot**, chaque `ancien` copié à l'identique d'une ligne du brouillon 47 dans 6.1 à 6.8 et présent **une seule fois** dans cette ligne ; `{"type": "inserer_apres", "ligne": n, "texte": "…"}` seulement si une ligne neuve est nécessaire, jamais avant la ligne 542.
2. Une note de 400 mots au plus : le sens retenu pour chaque trou et pourquoi ; ce que tu confirmes d'inatteignable ; ce que tu n'as pas pu trancher.
Ne committe que ce fichier et son compagnon ; pousse ta branche ; ne touche pas au texte lui-même : la session de relance applique tes couples par programme, puis un Sonnet neuf les contre-lit.
