# Notes du développeur — code de la lecture des directions des sondes de l'étape B bis par la lentille publique — v1

Pièce de travail (classe C) qui accompagne un code de classe B. Développeur neuf, session `session_013QMayj4Cr6sUZxiFq3rA8W`,
branche `claude/lentilles-bbis-developpeur-v1`, 2026-11-19 (UTC). Mandat : `docs/notes/lecture-sondes-bbis-par-lentilles-v1/mandats/mandat-developpeur-lecture-sondes-bbis-par-lentilles-v1.md`
(`ba6d01c61588ed6219b1664a480c2348893b1e6f4dc7008ad2bc7b05d9d111f4`, vérifiée). Texte scellé : `prereg/lecture-sondes-bbis-par-lentilles-v1.md`
(`ca5066d757df604cbf642db84f8a8fc56a0db8b6cc183f734842b7abdaf6d572`, vérifiée ; lu sur la branche principale, par `git show`).

## 1. Ce qui est rendu

| pièce | chemin |
|---|---|
| paquet | `src/controle_ia/lentilles_sondes_bbis/` : `constantes_v1` (valeurs du texte, sans choix), `entrees_v1`, `montage_v1`, `lecture_v1`, `nuls_v1`, `statistiques_v1`, `audits_v1`, `phrases_v1`, `lanceur_v1` |
| essais | `tests/test_lentilles_sondes_bbis_{entrees,montage,lecture,nuls_statistiques,procedure}_v1.py` ; jouets : `tests/lentilles_sondes_bbis_jouets_v1.py` |
| table des essais | `table-essais-v1.md` (ce dossier) |
| sortie des essais | `sortie-essais-v1.txt` (ce dossier) : 258 essais, tous verts |
| empreintes du code | `empreintes-code-v1.txt` (ce dossier) |

Le lanceur (`python -m controle_ia.lentilles_sondes_bbis.lanceur_v1`) a quatre sous-commandes : `montage` (plan, point 4, puis garde de
la fonction de lecture du point 5 ; ne touche aucune sonde), `recuperer` (clone partiel sans contenus, puis E-1, E-2 et leurs compagnons
seuls), `calcul` (point 6, puis nettoyage du point 10), `phrases` (phrases gelées rendues à partir des tables : étape du lecteur). Il
n'inscrit aucune ligne de registre et ne pousse rien : il rend les lignes proposées (`MONTAGE-`, `ENTREES-`, `TABLES-LENTILLES-BBIS`).

## 2. Ce que j'ai lu (déclaration)

- Le mandat ; le texte scellé, en entier ; son registre propre (deux lignes) ; le programme des bornes de calibration et sa sortie.
- Du registre `registres/t07-etape-b-bis-v1.md` : les seules lignes `CODE-BBIS`, par recherche de la clé (deux lignes ; la dernière :
  2026-11-17T11:05:29Z, `registres/t07-etape-b-bis/code-bbis-v2.json`, `4b28535c…`). **Précision** : la ligne ne porte pas de commit ; je l'ai
  tiré de la fiche qu'elle cite, par programme, en n'en sortant que le champ `commit` (`05cd22aa15382f61eb62b9e7817890dde728dd5f`), sans
  lire le reste de la fiche.
- Le **code** qui écrit les deux fichiers lus, vérifié à ce commit (empreintes égales à celles du texte, au commit `05cd22aa…`, sur la
  branche principale et sur cette branche) : `t07bbis/marche_v4.py` (l. 125-200), `validation_imbriquee_v1.py` (l. 205-265, 345-400),
  `validation_imbriquee_v4.py` (l. 215-262), `commun_v1.py` (constantes, `cellules`, `reglage_nom`, `grille`), `apprentissage_carte_v1.py`
  (l. 105-125), `t06/configuration.py` (l. 36-50), `sondes/familles.py` (l. 1-100, 225-240), `harnais/activations.py` (l. 1-30) ; `nom_tableau`
  par recherche. **Les noms des clés et des champs du texte sont ceux du code** : aucun écart trouvé.
- Lentille publique et code voisin : copie versée de `readout.py` (entière), de `weights.py`, de `catalog.py` (l. 25-170), de `arch.py`
  (l. 30-60, 140-155) ; configuration `neuronpedia-llama3.1-8b-it-rlens-config.yaml` ; les entrées `llama3.1-8b-it/` de l'arbre versé ;
  correctifs (2) et (4) entiers, tête du correctif (6) ; addendum des empreintes v3 (l. 1-120) ; inventaire du code voisin (l. 1-125).
- **Hors de la liste du mandat, déclaré** : pour savoir de quels octets est faite l'empreinte de la liste des jetons gardés et comment la
  tranche des lentilles appelle les scripts du voisin, j'ai lu, par recherche de lignes, du **code** de cette tranche (aucune sortie) :
  `src/controle_ia/neuron_lens/controles_b_beta_v2.py` (`empreinte_liste_gardee`, l. 389-394 ; `jeton_de_debut`, l. 545-560 ; la ligne
  `KEPT_N, KEPT_SHA256`) et des lignes de `b_beta_lancer_v3.py` (noms des variables d'environnement des processus enfants, commandes
  `05_act_corpus.py` et `03_token_counts.py`, clone et `git apply`). J'ai aussi listé les **noms** des fichiers de
  `docs/notes/neuron-lens-v1/` (dont des noms de dossiers de lecture et de journaux), sans en ouvrir un seul hors de ceux nommés ci-dessus.
- **Jamais lu** : rien sous `diag/`, `runs/`, `donnees/`, `docs/verdicts/` ; aucune branche `donnees/*` ou `calcul/*` ; aucun fichier dont
  le nom contient « consigne-privee » ou « conception-ii-b » ; aucun verdict, aucune lecture, aucune sortie d'aucune chaîne ; aucun autre
  registre. Aucune exposition involontaire à déclarer.
- **Aucun téléchargement** de Llama, de la lentille publique, du corpus ni du code voisin ; la clé de la plateforme de modèles n'a été ni
  lue ni testée (les essais emploient une fausse clé, dans un environnement passé en argument). Aucune machine, aucune dépense.
  Installé dans mon bloc-notes, pour les essais : torch 2.14.1 (processeur), transformers 5.18.0, tokenizers 0.23.2, safetensors 0.8.0,
  huggingface_hub 1.33.0 (versions de `requirements-cpu.txt`) ; numpy 2.5.3 et pytest 9.1.1 du conteneur.

## 3. Précisions de lecture prises pour coder (aucune n'ajoute une règle ; à contre-lire)

1. **Clés de graines** : `<couche>` = l'entier (`7`) ; `<pli>` = `e0` ou `e1` ; `<rôle>` = `sonde` ou `enc` ; `<vecteur>` = `w` ou `q` ;
   `<nul>` = `nul-isotrope` ou `nul-signes` (et `nul-isotrope-par-direction`, écrit en toutes lettres par le texte) ; nul isotrope partagé :
   `lentilles-bbis/temoins-calibration/<couche>/nul-isotrope/couche`. Tirage : un seul tableau `(M, largeur)` par clé (ligne j = direction
   j). Nul des signes : `rng.integers(0, 2)` puis `2x − 1`. Colonnes de la garde : `choice` sans remise, triées. Relecture de l'audit :
   deux directions tirées par la clé `lentilles-bbis/essai/audit-chemin-independant`.
2. **Statistiques** : écart type de population (diviseur M) ; quantile 0,99 par interpolation linéaire ; rang empirique = 1 + nombre de
   scores nuls du même jeton strictement plus grands ; part et familles d'une direction nulle : sur **ses** vingt premiers jetons, avec les
   quantiles communs ; « attendu sous le nul » d'une famille = moyenne de ses comptes sur les M directions nulles ; « ramenées à la norme
   de v » = même norme euclidienne ; écart type nul d'un jeton sous un nul : arrêt (z non fini).
3. **Pôles** : « rang parmi les maxima nuls » = 1 + nombre de maxima nuls strictement plus grands que le cosinus du pôle ; p de la
   concentration des pôles sur le maximum de |cosinus| de chaque direction nulle.
4. **« Concentrée » pour le déclencheur « trop beau »** : une sonde est comptée concentrée par la lentille publique si l'une de ses
   lectures (vecteur `w` ou `q`, signe) l'est (lecture de l'attente A-1, « à un signe au moins »). « Tout négatif » : aucune lecture
   « concentrée » ni « intermédiaire », les deux lentilles confondues.
5. **Garde de la fonction de lecture, « au rang près »** : mêmes dix identifiants en ensemble ; si les ensembles diffèrent, l'écart est
   compté sans arrêt seulement si tous les jetons en trop ou en moins ont un score à moins de 10⁻⁴, en valeur relative, du dixième score ;
   sinon arrêt. Elle est jouée en fin de montage pour **les trois couches** 7, 15 et 23 (les couches des sondes ne sont pas connues avant
   `VERDICT-BBIS`).
6. **Calibration hors de ses bornes** : la table de ce nul, pour cette couche et cette lentille, est remplacée par
   `{"non_calculable": motif}` ; la lecture garde ses jetons et l'autre nul, mais ne porte aucun libellé (il en faut deux) ; les pôles, qui
   ne passent pas par la lentille, ne sont pas touchés.
7. **`provenance` de la lentille** : `capture_point` absent ou différent, `target_layer` présent et différent de 31 : arrêt (texte).
   `source_layers` ou `d_model` présents et différents : arrêt ; absents : rapportés (`cles_attendues_absentes`), sans arrêt.
   `source_layers` n'est accepté qu'en liste d'entiers ; une autre forme arrête (sens sévère). Matrices exigées en demi-précision.
8. **Pôles « intermédiaires »** : le texte ne gèle que deux phrases (pôles concentrés, pôles non distincts) ; pour le libellé
   « intermédiaire », le code ne rend **aucune phrase** (valeurs en table). À trancher par la mère si une phrase est voulue.
9. **Phrase de comparaison** : le nombre de jetons communs rendu est celui de la lentille publique, au signe + ; les tables portent les
   deux lentilles et les deux signes.
10. **Horloge** : la durée cumulée est tenue dans le dossier de travail (`horloge.json`), montage et calcul additionnés.
11. **Réglages** : `lanceur_v1.Reglages` porte les valeurs du texte par défaut ; seuls les essais en remplacent (tailles des jouets) ; la
    ligne de commande n'en expose aucune.
12. **`CODE-LENTILLES-BBIS`** : le code vérifie la présence de la ligne et que `SCELLEMENT-LENTILLES-BBIS` cite ce texte (chemin et
    empreinte) ; il **ne compare pas** ses propres empreintes à la fiche que citera `CODE-LENTILLES-BBIS` (forme de la fiche inconnue) : il
    écrit ses empreintes dans le montage et le manifeste ; la comparaison revient à l'opérateur ou à la mère.
13. **Essai d'un octet du corpus** : dépôts et révisions des quatre jeux lus dans les fichiers `data/corpus/act-*.provenance.json` du code
    voisin corrigé (champs `repo`, `revision`), premier fichier de données de l'arbre de chaque jeu.

## 4. Réserves (ce que les jouets ne prouvent pas)

- **Réseau réel non éprouvé** (interdit par le mandat) : `TransportRequests`, la forme de l'arbre des fichiers rendu par l'interface, les
  redirections vers les hôtes de stockage, la reprise d'un flux par intervalle. La méthode du pointeur est éprouvée sur les valeurs réelles
  de la lentille publique (SHA-256 et taille du texte → identifiant git `16780aaa…` de l'arbre versé, 135 octets), et l'identifiant git du
  contenu sur la notice versée.
- **Tokeniseur dans le cache, sans clé** : les scripts du voisin sont joués sans la clé (elle ne passe jamais à un processus enfant) ; le
  tokeniseur vérifié est posé par notre code dans le cache à la révision épinglée (`hub/models--…/snapshots/<révision>/`, `refs/main`).
  Que `AutoTokenizer.from_pretrained` du voisin le lise ainsi, en ligne pour `05_act_corpus.py`, n'est pas éprouvé ici (jouet : faux
  catalogue). Un échec arrête le montage (code de retour du script), sans effet sur une mesure.
- **Paquets du voisin** (`datasets`, `pyarrow`) : à installer par l'opérateur aux versions de l'addendum v3 ; le montage les relève.
- **Mémoire** : pointe mesurée 6,0 Go sur le banc (texte : estimée ≤ 6 Go) ; 15 Go dans ce conteneur.

## 5. Banc sans données, à la taille réelle (matrices aléatoires ; aucune sonde, aucun poids, aucune lentille réelle)

89 498 jetons, largeur 4 096, 14 336 neurones, M = 2 000, 4 fils, simple précision :
- une couche, deux vecteurs, deux lentilles, nuls, témoins, pôles et témoin de couche : **51,5 s**, pointe **6,04 Go** ; soit ≈ 25 s par
  vecteur, ≈ 15 à 20 min pour quarante vecteurs ; tableaux gardés ≈ 4,8 Mo par vecteur.
- **Constat à porter à la mère (nœud possible, aucune règle changée)** : le p de concentration compare une direction (ou un témoin) à des
  directions nulles dont la concentration est calculée **avec elles-mêmes dans la moyenne et l'écart type** (« u_j compris : écart
  déclaré, négligeable à M = 2 000 », « Métrique », point 6). Sur le banc, ce n'est pas négligeable pour la calibration : 242 témoins sur
  4 000 à p ≤ 0,05 sous le nul isotrope (6,05 %, attendu 5,00 %), 232 sur 4 000 sous le nul des signes (5,80 %) ; la même statistique
  calculée sans u_j (diagnostic, non codé dans le paquet) rend 5,15 % et 4,90 %. Aux tailles du plan, les comptes attendus à ces taux
  restent dans les bornes mais se rapprochent de la borne haute (isotrope : 60 pour [23, 85] ; signes, treize vecteurs : 151 pour
  [89, 176] ; vingt vecteurs : 232 pour [149, 256]). Des scores réels à queues plus lourdes que ces matrices gaussiennes pourraient
  sortir des bornes : la règle gelée rendrait alors « non calculables » les tables de la couche, de la lentille et du nul touchés. Le même
  biais porte sur les p des directions réelles (sens : p un peu trop petits). Le code applique le texte tel quel.

## 6. Essais des essais

Quarante altérations du code, une à une (garde retirée, seuil changé, signe inversé) : trente-neuf font tomber au moins un essai ciblé. La
quarantième retire le premier des deux refus de `registres/scellements-v1.md` dans `inscrire_ligne` ; le second refus (« seul le registre
propre de ce texte reçoit ses lignes ») tient encore : l'écriture reste refusée.

## 7. Suite du dépôt

Consigne de la mère pour cette session : ne jamais jouer la suite complète (disque). Elle n'a donc pas été jouée. Ce rendu **n'ajoute que
des fichiers neufs** (un paquet, six fichiers sous `tests/`, ce dossier) et ne modifie aucun fichier existant. Les essais neufs sautent
proprement sans torch, transformers ou safetensors (`pytest.importorskip`).

## 8. Scellement du code

Les empreintes des fichiers de code et d'essais sont dans `empreintes-code-v1.txt`, scellé. Je n'ai **pas** posé de compagnon `.sha256` à
côté de chaque fichier de code avant la contre-lecture : les corrections qu'elle demandera se feront sous des noms neufs seulement si la
mère le veut (R12) ; sinon en place, avant la ligne `CODE-LENTILLES-BBIS`, l'historique git gardant chaque état. À trancher par la mère.

## 9. Fichiers à contre-lire (classe B)

`src/controle_ia/lentilles_sondes_bbis/__init__.py`, `constantes_v1.py`, `entrees_v1.py`, `montage_v1.py`, `lecture_v1.py`, `nuls_v1.py`,
`statistiques_v1.py`, `audits_v1.py`, `phrases_v1.py`, `lanceur_v1.py` ; `tests/lentilles_sondes_bbis_jouets_v1.py` et les cinq fichiers
`tests/test_lentilles_sondes_bbis_*_v1.py` ; `table-essais-v1.md` et cette note ; contre le texte scellé (branche principale).
