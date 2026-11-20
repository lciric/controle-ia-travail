# État 03 — reprise par un second développeur ; jugement des états hérités

20 novembre 2026 (horloge du conteneur). Pièce de travail du second développeur de la fabrique (Claude Opus 5.5), même
rôle que le premier, arrêté par une interruption. Aucune donnée lue.

## Pièces lues, empreintes vérifiées avant lecture
- Mandat `mandat-developpeur-fabrique-mondes-v1.md`, `d8977676…4161e4`, en entier.
- Texte scellé `bdff244f…d935` : « Métrique », « Seuil », « Plan d'analyse » points 1 à 18 tels qu'ils tiennent dans
  les lignes 201 à 261 (dont le point 11 en entier et le point 14 des graines), « Critères de lecture gelés », « Ce que
  dira chaque issue au jury ». Titres repérés par leur seule ligne. Rien d'autre.
- Addendum 1 scellé `prereg/…-addendum-1.md`, `2afa2186…99e4`, en entier. Choix de Lazar suivis : famille sans tâche
  retenue comptée absente ; borne de la phrase « empreinte » à ½ Δ_app.
- Rapport v3 du développeur de la lecture `b9c77d67…554e`, section 1 seulement.
- `lecture_v1.py` : commentaire de tête seulement (lignes 1 à 83, il s'arrête là). Rien d'autre du programme.
- Hors programme : `barreau5_familles/__init__.py` (docstring seule, aucun import) ; `manifeste.py`, lignes 1 à 57
  (dérivation d'une graine depuis une clé) ; `pyproject.toml` et `tests/conftest.py` (configuration de pytest).

## États hérités, lus en entier
- `epreuve_verite_plantee_v1.py` `e2eb98b9…`, `juge_verite_plantee_v1.py` `c7089d17…` (ceux de l'état 02) ;
  `tests/test_barreau5_familles_epreuve_verite_plantee_v1.py` `29d6f559…` (changé après l'état 02) ; notes 01 et 02.
- Les essais hérités passent : 121 en 84 s.

## Jugement : je reprends
La construction est juste et suit le texte : scores plantés par jeton, jeton du maximum invariant sous tout facteur de
]0 ; 2] en régime fixe, bruit propre à chaque membre par action et par jeton, unité en écarts types de la différence
d'une famille à l'autre, déplacements sur coordonnées disjointes, ĝ exactement un vecteur de base, produits nuls exacts de
V10. Le juge applique la colonne « règle gelée » règle par règle. Recommencer coûterait sans rien gagner.

## Défauts trouvés, à corriger
1. **Ligne `ENGAGEMENT-B5F` absente du registre fabriqué.** Le point 7 la nomme (engagement de la table) ; l'ouvreur
   vérifie que l'empreinte de la table égale l'engagement et que « les trois dates se suivent (engagement, scores,
   ouverture) ». Sans elle, le cas V7 « empreinte de la table différente de l'engagement » n'est pas écrit au sens du
   texte. Sa forme n'est pas dans l'interface lue : paramètre, défaut déclaré.
2. **Signe de la trace dans V12.** L'état hérité met +4 sur le jumeau et le sur-saboteur : le saboteur tombe alors sous
   le jumeau (E1 manque) et « sabotage » est barré deux fois. La réunion que vise « Seuil » (constat V-B1) est celle où
   la trace fait passer E1 et la force E3 : trace du signe de V2. Le texte ne fixe pas le signe : la moitié des mondes
   porte le signe de V2, l'autre le signe littéral.
3. **Épisodes d'évaluation sur 64 tâches.** Le point 5 en joue 32 (16 par pli) ; défaut ramené à 32, paramétrable.
4. **« copie » à `T01-copie-lue`.** L'interface dit « nom formé lu » ; défaut ramené au nom de la famille.
5. **Graines.** Le point 14 fixe la clé `b5f/epreuve/<monde>` ; la dérivation suit la règle du dépôt
   (`manifeste.cle_de_tache`), flux en second élément de la clé.
6. **Passage de mutations absent** (demandé par le mandat) ; un essai ne tue pas un bruit partagé entre membres.

Prochaine action : corriger la fabrique et les essais, écrire le passage de mutations, puis le rapport.
