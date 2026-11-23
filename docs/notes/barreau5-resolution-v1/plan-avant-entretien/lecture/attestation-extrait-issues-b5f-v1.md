# Attestation du conducteur sur l'extrait des critères de lecture gelés du barreau 5 — v1

Conducteur de la lecture du barreau 5 (session_016QhUrrG5GmnzyjK8E1CZCB, reprise de session_013QMayjM1PQPWkLifMw9HDR), 2026-11-23 08:42Z, à la demande de la mère (session_016QhUrvi45g3jX5saFefVED), pour la conception des sondes. Aucun score, aucune issue observée, aucune table ni sel lus : seul le texte scellé est comparé à lui-même.

Texte scellé : `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1.md`, sha256 bdff244f1377e795b84f71518bb5e58fb1600fff8afee383d8f70c10d3f5d935 (égale à son compagnon), 504 lignes.
Extrait servi : `docs/notes/barreau5-resolution-v1/plan-avant-entretien/lecture/extrait-issues-et-phrases-gelees-b5f-v1.md`, sha256 c228c773e0ea94982d73a4a9c97e48305a3b77333874532655fb59a1818773cb (égale à son compagnon).

## (1) Le bloc de l'extrait correspond aux lignes 302 à 343 du texte scellé : OUI
- `sed -n 302,343p` du texte scellé : sha256 ff0e1fa5778f4597386c7ce4e1e82b81039a949dcd4ed4ea5f7b4620fab0ba3e.
- Bloc de l'extrait (tout ce qui suit la ligne « --- », ligne vide d'en-tête ôtée) : même sha256 ; `diff` vide.
- Le bloc couvre les sections « Critères de lecture gelés » (l. 302) et « Ce que dira chaque issue au jury » (l. 333) ; la section suivante, « Liste d'arrêt », commence à la ligne 345 et n'est pas dans l'extrait.

## (2) Aucun libellé d'issue n'apparaît ailleurs dans le texte : NON
Des libellés d'issue apparaissent hors des lignes 302 à 343 :
- l. 146, 147 (table « Prédiction chiffrée ») : issue « différence établie, non attribuée » et ses motifs ;
- l. 195 (section « Seuil ») : définition de l'issue « empreinte » ; sa lettre diffère de la ligne E de la table (l. 302-343) : elle ajoute « épreuve E3 ni « séparé » ni « contraire » » ;
- l. 196 (section « Seuil ») : manipulation non établie → issue « non interprétable » ;
- l. 198, 199 (« Famille de lectures », « Audit de symétrie ») : mot « sabotage », issue « contraire » ;
- l. 241 à 250 (table des mondes de l'épreuve à vérité plantée) : « différence établie » et motifs, « contraire », « non interprétable », « sabotage » ;
- l. 292 (« Puissance ») : « empreinte », « différence établie » ;
- l. 359 (liste d'arrêt, point 13) : issue N, motif « niveau non atteignable » ;
- l. 430 (« Calendrier », risques) : distillation qui ne transmet pas l'édition → issue « non interprétable ».
Repérage : `grep -nE` sur les lettres d'issue et les libellés, lignes hors de 302 à 343 ; les mots « sabotage » et « empreinte » pris comme noms communs (titre, objet, hypothèse) ne sont pas listés ici.

## (3) Toute garde de la liste d'arrêt mène à l'issue NI : NON
La table (l. 308) dit NI quand « une garde de la liste d'arrêt invalide la lecture ». La liste d'arrêt (l. 345 à 361, quinze points) ne nomme pas toujours l'issue NI :
- point 13 (l. 359) : moins de six familles présentes → **issue N**, motif « niveau non atteignable », nœud ;
- points 1, 3, 4 (pendant la formation) : la famille n'est pas formée et **compte absente** (ou retirage) ; aucune issue nommée ; l'effet passe par le compte des familles (paragraphe « Sous huit familles présentes », l. 323 du texte scellé, et point 13) ;
- points 1 et 3 (hors formation), 5, 6, 14 : **arrêt** (point 5 : la famille est invalide) ; aucune issue nommée ;
- point 7 : « lecture invalide, version neuve » ;
- points 8 et 9 : **refus** (de la lecture, au point 9), nœud ; point 10 : aucune ouverture ; point 11 : arrêt avant toute notation ; point 12 : pièce invalide ; point 15 : arrêt de l'écriture ; point 2 : aucune création.
Aucun point de la liste n'écrit « non interprétable » ni « NI ». Le rattachement d'un point à NI par la ligne l. 308 est une lecture que ce texte ne tranche pas ; seul le point 13 nomme une issue, et c'est N.
