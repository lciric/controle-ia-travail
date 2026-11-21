# Brouillon de travail — nœuds et précisions de lecture du développeur de la seconde passe (non scellé, complété au fil de l'eau)

## Nœuds (ambiguïtés qui obligent à choisir ; datés ; le reste continue)
- N-dev-1 (2026-11-21) — **corpus des jetons gardés, arbre paginé** : message de la session des lentilles : `montage_v1.cibles_corpus`
  ne lit que la première page de l'arbre d'un jeu de données ; un correctif est écrit ailleurs sous les noms réservés
  `corpus_pagine_v1.py`, `lanceur_v8.py`, `tests/test_lentilles_sondes_bbis_corpus_pagine_v1.py`. Le lanceur de la seconde passe ne
  réemploie pas `cibles_corpus` de `montage_v1` tel quel : la fonction des cibles du corpus y est un point de branchement nommé, à
  brancher sur `corpus_pagine_v1` quand il sera poussé. Je ne touche aucun de ces trois fichiers.
- N-dev-2 (2026-11-21) — **forme de la fiche de rangement** : le texte dit ce que la fiche porte, non sa forme. Le code attend un JSON
  (`nos_lentilles_v1.CHAMPS_FICHE`). La session principale doit l'écrire dans cette forme, sinon rien ne part.
- N-dev-3 (2026-11-21) — **comment la ligne `NOEUD-PALIER-2-AJUSTEMENT-SEUL-LENTILLES-BBIS` nomme la lentille** : le texte dit « qui
  nomme la lentille » sans forme. Le code lit, dans la pièce citée par la ligne (empreinte vérifiée), une ligne « Lentille nommée : R »,
  « Lentille nommée : S » ou « Lentilles nommées : R et S ». Sans elle : non lue (sens sévère). « Postérieure à l'avertissement » :
  place et heure strictement après toute ligne d'avertissement.
- N-dev-4 (2026-11-21) — **couche écartée par la lecture de la seconde course** : la fiche recopie des mots ; le code ne les
  interprète pas : il attend, par couche, `{"limite": mots, "ecartee": vrai|faux}`.
- N-dev-5 (2026-11-21) — **code d'entrée réemployé tel quel** : `entrees_v3.ouvrir_entrees` exige les lignes de la première passe
  (`SCELLEMENT-`, `GO-`, `CODE-LENTILLES-BBIS`, relevé d'absence antérieur au verdict, addendum avant le code). Le texte dit « même
  code d'entrée », et que seule la première ligne de la liste d'arrêt de la v1 ne vaut pas pour la seconde passe. Réemployé tel quel :
  si ces lignes manquent, la seconde passe refuse (sévère). Autre lecture possible : une version neuve du module d'entrée.
- N-dev-6 (2026-11-21) — **`lenses.load_fits` du voisin** : aucune copie du code voisin n'est versée et rien ne se télécharge ;
  l'essai « extraction en flux égale au chargement entier par `lenses.load_fits` » compare à `torch.load` du fichier entier et à la
  formule `Accumulator.mean` écrite dans le texte.

## Précisions de lecture (aucune n'ajoute une règle de décision ; à contre-lire)
- Comptes d'égalités : la liste par score d'une direction lue est comptée sous « liste par score ».
- « Versé scellé » (verdict d'identité, audit) : la fiche en donne le chemin et l'empreinte entière ; audit « sans contrôle
  manqué » : champ `controles_manques` égal à 0.
- Écart relatif de Frobenius : ‖A − B‖ / ‖B‖, B la référence (identité, lentille publique, notre R, sa transposée).
- Contrôle de notre S contre notre R quand notre R n'est pas décodée : « sans objet », écrit.
- `ABANDON-LENTILLES-BBIS-V2` ou `NON-LUES-NOS-LENTILLES-BBIS` inscrite : rien de la seconde passe ne part.
- Plusieurs lignes `RANGEMENT-NOS-LENTILLES-BBIS` : la dernière désigne la fiche en vigueur (fiche neuve sous un nom neuf).
- Taille des enregistrements de l'archive : torch 2.14.1 n'écrit pas la taille dans l'en-tête local (descripteur de données) ; le
  code la tire de `data.pkl` pour les stockages, du descripteur vérifié par sa somme de contrôle pour les petits enregistrements.
- Descripteur de données d'un enregistrement de plus de 4 Gio, ou d'une archive de plus de 4 Gio : forme (16 ou 24 octets) non
  éprouvée sur un vrai fichier (aucun n'est téléchargé) ; le code accepte les deux et arrête sur toute autre (réserve).
- Essai des essais de `nos_lentilles_v1` : 29 altérations vues sur 30 ; la trentième (« enregistrement compressé accepté » par la
  seule méthode) est équivalente : une seconde garde (taille compressée différente de la taille) rend le même arrêt.
- « Indépendance exacte de S à la norme » : exacte en mathématiques ; en simple précision, c et 10⁻⁴·c rendent les mêmes scores à
  l'arrondi près (essai : écart relatif sous 10⁻⁵, mêmes vingt premiers jetons).
- Essai des essais : `lecture_entree_v1`, 10 altérations vues sur 10 ; `comparaisons_lentilles_v1`, 12 sur 13, la treizième
  équivalente (notre S refusée par une seconde garde, la liste des paires du texte). Outil : `outils/essai-des-essais-seconde-passe-v2.py`
  (la v1 ne voyait pas les copies versées sous `docs/`).
- Constat, non corrigé : un dossier `__pycache__` daté de 16:00:15Z, antérieur à mon départ, est présent à côté de la copie versée
  de `readout.py` sous `docs/sources/` (ignoré par git) ; je ne l'ai ni créé ni retiré.
- N-dev-7 (2026-11-21) — **dernier crochet de la phrase permise du deuxième palier quand il ne peut pas être dit** : fiche muette
  sur l'achèvement de la seconde course, ou course menée en entier dont la ligne de lecture n'est pas inscrite. Le texte dit qu'une
  lentille non lue reçoit quand même la phrase de son verdict ; mais aucun des deux mots du crochet ne peut alors être écrit sans
  risque d'être faux. Le code n'écrit pas la phrase et pose une note (`phrases_v2.NOTE_DERNIER_CROCHET`), à côté de la ligne « Non lue ».
- Crochets de chiffres de la phrase permise : « [écart mesuré] » = `ecart_max_abs_diffs_float64` (le plus grand des deux lentilles
  dans la forme au pluriel) ; « [valeur] et [valeur] » = `ecart_max_abs` de la série d'écart à la lentille publique puis de celle à
  l'identité ; « de [valeur] à [valeur] » = le plus petit `ref_min` et le plus grand `ref_max` des deux séries. Trois chiffres
  significatifs, virgule décimale, aucun qualificatif. « (empreinte …) » : l'empreinte entière du fichier.
- Lignes du verdict d'ensemble : choisies d'après les paliers des lentilles **lues** ; la forme de la phrase permise, elle, d'après
  les verdicts. La ligne « Verdict d'ensemble » de V et les mots des réserves restent entre crochets, à recopier par le lecteur.
- Première passe jamais lancée : le texte dit « c'est écrit » sans phrase gelée ; le code pose une note (`NOTE_PREMIERE_PASSE_REMPLACEE`).
- Reproduction : « vingt premiers jetons » comparés comme ensembles d'identifiants ; un même ensemble dans un autre ordre est compté
  à part, sans réserve (l'ordre entre jetons de même score à l'intérieur de la liste peut différer entre les deux modules).
- Essai des essais : `phrases_v2` 15 sur 15 ; `reproduction_v1` 8 sur 8 ; `audits_v2` 8 sur 8 (outil `essai-des-essais-seconde-passe-v3.py`).
