# Consigne — lecteur neuf des voisins « bassins d'idées » (Fork-and-Flush, Scaling Discovery Requires Forgetting) — v1

Écrite par la session mère le 13 novembre 2026 à 12:28 UTC (`date -u`). Tu es un sous-agent neuf, lecteur ;
tu n'écris aucun code et tu ne modifies aucune pièce existante. Langue : français, presque aucun acronyme.

## 0. Interdits (à lire d'abord, sans exception)
Lis en entier `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-0500-v1/interdits-communs-v2.md`
(`1ee3b37075aacb278864e6eeda99b72e0d1babe9d6d02bd4a0c0aff26131337f`) et applique-le. En particulier : jamais `donnees/bras-attaque*`,
`donnees/mode-tenu-a-l-ecart*`, `docs/notes/bras-attaque/`, `registres/index-bras-attaque*`, `anteriorite-bras-informe*` ;
aucun `diag/` ni `runs/` de 7a ou 7b ; jamais une valeur de clé, jamais `env`, `printenv`, `set` sans argument ; jamais d'heure
écrite à la main (`date -u`) ; aucune opération git (ni commit, ni fetch, ni changement de branche) : la mère commite.
Aucun `grep -r` ni `find` à la racine du dépôt (ils traverseraient des chemins interdits) : ne lis que les fichiers nommés ici.
Mémoire du conteneur limitée : `ulimit -v 6000000`, pas de calcul lourd. Aucune dépense. Ne contourne aucun refus.

## 1. Pourquoi
Lazar a signalé le 13 novembre la page de Bespoke Labs « How models explore ideas » (10 novembre 2026), archivée sous
`docs/sources/web-bespoke-how-models-explore-ideas-20261113/` (`texte.txt`, `b1d32227…`). Elle cite deux articles que le
dépôt ne connaît pas : arXiv 2610.07447 (Cai et al., « Fork-and-Flush: Escaping Idea Basins in Autoresearch Agents ») et
arXiv 2610.20563 (Tan et al., « Scaling Discovery Requires Forgetting »). Ils touchent l'organisme d'idéation (course à
plusieurs générations, héritage, diversité des idées, regroupement des doublons). Il faut savoir, sur les PDF (R7), ce qu'ils
prennent, ce qu'ils laissent ouvert, et ce qui est à citer ou à battre (R8 : limitation d'un article ≠ trou du champ).

## 2. À faire
1. Télécharger les deux PDF (`https://arxiv.org/pdf/2610.07447` et `https://arxiv.org/pdf/2610.20563`, client générique,
   aucune donnée du projet dans la requête) vers `docs/sources/arxiv-bassins-idees-20261113/` (noms avec le numéro et la
   version servie) ; les sceller (`PYTHONPATH=src python3 -m controle_ia.scellement sceller FICHIER`) ; en extraire le texte
   (`pdftotext` s'il existe, sinon `python3 -I` avec une bibliothèque déjà installée ; ne rien installer de lourd).
   Si un téléchargement échoue : le dire, lire la page de résumé, marquer « niveau transcription » (non opposable).
2. Lire en entier : les deux articles ; `texte.txt` de la page ; nos pièces : `docs/decisions/decision-N-044-v1.md`,
   `decision-N-045-v2.md`, `decision-N-058-v1.md`, `decision-N-064-v1.md`, `decision-N-065-v1.md` ;
   `docs/notes/collisionneur-diversite-idees-v1/synthese-v1.md` ;
   `docs/notes/organisme-multi-generations-v1/conception-monde-riche-doublons-v3.md` (§3, §4, §5) et `…-v4.md` (§0 et la
   famille MR-2).
3. Écrire `docs/notes/lecture-voisins-bassins-idees-v1.md`, puis la sceller. Contenu, dans cet ordre :
   - verdict en trois lignes (collision, voisinage, ou rien) ;
   - par article : question, dispositif, mesures (définitions exactes), résultats chiffrés **avec page**, interventions
     éprouvées (remise à zéro du contexte, reprise du meilleur résultat, branches…) et leurs effets, limites dites par les
     auteurs, code ou données publiés ;
   - tableau « nos revendications × ces articles » : pour N-045 (composition apprise, héritage d'une génération récompensé,
     poids contre archive), N-064 (O2 : statistique scellée, nul des lois connues, multiplicité), N-065 (second terrain du
     papier C), N-044 (universalité, diversité), le regroupement des doublons par distance prédictive et la mesure de
     diversité par couverture d'oracle : **pris / voisin à citer / ouvert / à battre**, phrase et page à l'appui ;
   - ce que ces travaux permettraient d'emprunter, classé par coût : (a) mesures descriptives sans appel de plus (par
     exemple, par proposeur et par génération : part des propositions tombant dans un groupe déjà archivé, dans un groupe
     neuf, ou revenant à un groupe écarté) ; (b) bras ou témoins nouveaux ; (c) méthode de carte des idées par comparaisons
     en triplets jugées par un modèle, pour les idées en texte libre où nous n'avons pas de distance prédictive ; pour chacun :
     ce que cela exigerait dans un préenregistrement, et le risque (juge à modèle, Goodhart, N-053 : aucun score servi) ;
   - toute zone que nous revendiquons et que tu trouves occupée : la nommer nettement (c'est un nœud pour Lazar) ;
   - limites de ta lecture.
4. Chaque chiffre cité renvoie à un fichier empreinté et une page. Aucun chiffre de mémoire.

## 3. Rapport final à la mère (court)
Verdict ; chemins et empreintes des pièces écrites ; zones occupées s'il y en a ; ce qui n'a pas pu être lu.
