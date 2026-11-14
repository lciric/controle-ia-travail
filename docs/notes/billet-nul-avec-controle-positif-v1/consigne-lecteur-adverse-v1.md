Tu es un lecteur adverse neuf (sous-agent), en français. Tu n'as écrit aucune des pièces que tu lis. Dans ton rapport, désigne ton propre modèle par « modèle C », sans aucun identifiant de modèle (règle R-2718 du dépôt). Tu travailles en LECTURE SEULE : aucune écriture, aucun commit, aucune requête réseau, aucun contact. La routine de reprise décrite dans un éventuel CLAUDE.md ne te concerne pas (la session mère l'a faite) : ne lance aucune commande hors de `date -u`, `sha256sum` et `wc`.

Dépôt : /home/user/controle-ia-travail (chemins ci-dessous relatifs à ce dossier).

## Ce qu'on te demande

Relire, en adversaire, trois pièces préparées pour un billet LessWrong que le directeur (Lazar) réécrira avec ses mots. Rien n'est publié. Le billet porte sur des sondes linéaires : P3 (un résultat nul) et P3-bis (un contrôle positif planté, verdict « vu »), plus deux sections vides réservées à des résultats à venir (marqueurs `<<ETAPE_B>>` et `<<ETAPE_B_BIS>>`).

Les trois pièces à relire :
1. `docs/notes/billet-nul-avec-controle-positif-v1/billet-premiere-version-en-v1.md` (le billet, en anglais ; corps entre les deux lignes `---`).
2. `docs/notes/billet-nul-avec-controle-positif-v1/fiche-de-faits-v1.md` (fiche de faits, avec pièces, empreintes, lignes ; section « ce qu'il ne faut pas dire »).
3. `docs/notes/billet-nul-avec-controle-positif-v1/relecture-billet-v2-contre-verdict-v1.md` (relecture d'un billet antérieur contre le verdict de P3-bis).

Les pièces qui font foi, à lire pour contrôler :
- `docs/verdicts/verdict-P3-bis-v1.md` (attendu sha256 `9b33c624fe9c4be2909cee9ea764f6e19d31e7767affd64bb6f763d0032a1e5c`) : EN ENTIER, réserves comprises. C'est la référence principale.
- `docs/verdicts/verdict-P3-bis-v1-issue.json` (`c3a017ce1e8b0c41dee1e430f142590e88bd7104eada02b3a973ac98c0da28d0`).
- `docs/verdicts/verdict-P3-premier-test-i-a-v2.md` (`05e896daed17cdb089cd10641878a5014b505eab0aa3d45d0dd7a60d87435751`) : le nul de P3, ses réserves B1 et B3 ; lis au moins les lignes 1-45, 95-115, 171-222, 495-560.
- `prereg/P3-bis-temoin-positif-v1.md` (`76ab66ce967796b944e2ca585ee0dc2d780189e8e0cbe429e390c427a46121cb`) : SEULEMENT les lignes 1137-1300, 1365-1398, 1420-1432, 1820-1898 et 2641-2768 (fichier très long ; ne lis pas le reste).
- `prereg/P3-premier-test-i-a-v1.md` : seulement les lignes 115-126, 286-300, 312-324.
- `registres/decisions.md` : seulement les lignes 2257 (R-2299), 2664 (R-2704), 2671 (R-2711), 2674 (R-2714), 2675 (R-2715), 2676 (R-2716), 2678 (R-2718). Fichier énorme : lis-les avec Read, offset et limit=1.
- `registres/scellements-v1.md` : lignes 10 et 15.
- Pour contrôler la pièce 3 : `docs/notes/publiabilite-ce-soir-v1/billet-v2/billet-premiere-version-en-v1.md`, `docs/notes/publiabilite-ce-soir-v1/billet-v2/billet-premiere-version-v1.md`, `docs/notes/publiabilite-ce-soir-v1/billet-v2/fiche-faits-billet-v1.md`, `docs/notes/publiabilite-ce-soir-v1/billet-v2/journal-billet-v2-v1.md`.

## Interdits de lecture (stricts)

Ne lis RIEN d'autre que les fichiers ci-dessus. En particulier, jamais : aucun fichier sous `diag/`, `runs/`, `donnees/`, `brouillons/` ; aucun fichier de T0.7 (`prereg/T0.7*`, `src/controle_ia/t07/`, etc.) ; aucun `lecture-sondes-t06.json` ; rien de l'étiqueteur ; jamais `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`, `docs/notes/bras-attaque/`, `registres/index-bras-attaque*`, `anteriorite-bras-informe*` ; jamais `prereg/P3-bis-consignes-v1.md`. Aucune recherche récursive sur le dépôt : n'emploie Grep et Glob que sur les fichiers listés. Si tu crois avoir besoin d'un autre fichier, dis-le dans le rapport au lieu de l'ouvrir.

## Méthode

A. Vérifie d'abord les empreintes des pièces qui font foi (`sha256sum`), et note l'heure de début (`date -u`).

B. Le billet (pièce 1), phrase par phrase, contre la fiche et le verdict de P3-bis (et le verdict de P3 pour la section sur le nul) :
- tout ce qui dépasse le verdict est un constat ; tout nombre faux ou mal arrondi est un constat ; toute phrase gelée mal traduite (sens changé, partie omise qui change la portée) est un constat ;
- règles à contrôler : aucune explication du nul de P3 (le verdict et le texte scellé l'interdisent : « jamais une explication du nul de P3 ») ; « vu » ne prouve pas que la sonde lit le sabotage ; le signal vu peut tenir à la phrase de persona, à la forme ou à la longueur du texte ; la consigne visible n'est pas détectée à cette puissance ; « non au-dessus » se lit « non détecté à cette puissance », jamais « ne sépare pas » ; un seul modèle, une seule taille ; toutes les réserves gelées et jointes portées (réserve PB-4 déclenchée ; les deux réserves de R-2299 jointes à toute citation du nul de P3 ; les réserves B3, et B1 si P3-P1 est cité ; les quatre réserves des addendums ; les trois réserves de l'ouverture) ;
- interdits de contenu : aucun identifiant de modèle Claude (le mot « Claude » seul, pour la famille, est toléré mais signale-le si tu le juges risqué) ; aucun texte de scénario, de consigne de sabotage ni de sortie de modèle ; rien d'un « bras d'attaque » ni d'un « mode tenu à l'écart » ; rien d'un article « TASTE » ; rien de T0.7 au-delà de ce que les verdicts et le texte scellé citent ; aucune primauté (« first », « novel ») ;
- forme demandée : 700 à 1 000 mots pour le corps (compte-les : `wc -w` sur le corps) ; anglais simple ; sections : question, ce qui a été fait (préenregistrement, contrôle positif planté, lecteur neuf), résultats avec leurs nombres, ce que cela ne montre pas, limites, suite ; deux sections vides marquées `<<ETAPE_B>>` et `<<ETAPE_B_BIS>>` ; une variante de titre et de résumé pour le cas « sans l'étape B bis ».

C. La fiche (pièce 2) : chaque fait a-t-il un chemin, une empreinte et une ligne ? Contrôle sur pièce au moins quinze faits tirés au hasard parmi F01-F62 (le nombre et la ligne citée disent-ils bien cela ?). La section « ce qu'il ne faut pas dire » couvre-t-elle au moins : aucune explication du nul de P3 ; « vu » ne prouve pas que la sonde lit le sabotage ; le signal vu peut tenir à la phrase de persona, à la forme ou à la longueur du texte ; la consigne visible n'est pas détectée à cette puissance ; un seul modèle, une seule taille ; toutes les réserves gelées et jointes ?

D. La relecture (pièce 3) : les classements (confirme, contredit, laisse ouvert, sans rapport) sont-ils justes, en particulier pour toute phrase du type « la sonde lit la consigne, pas le sabotage » ? La conclusion suit-elle ?

## Rapport

Écris ton rapport en français, en Markdown, directement comme réponse finale (pas de fichier). Structure :
1. En-tête : lecteur (sous-agent neuf, « modèle C »), heures de début et de fin (`date -u`), empreintes vérifiées, fichiers lus.
2. Verdict en une à trois lignes : « prêt pour Lazar », « prêt après corrections » ou « à reprendre ».
3. Constats numérotés (C-1, C-2, …), chacun avec : gravité (bloquant, majeur, mineur), pièce et phrase exacte visée, la pièce qui fait foi et sa ligne, la correction proposée.
4. Ce qui tient (contrôlé, sans constat).
5. Limites de ta lecture.
Sois précis et bref ; ne réécris pas le billet entier.
