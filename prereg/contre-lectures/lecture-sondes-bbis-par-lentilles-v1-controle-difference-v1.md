# Contrôle de la différence, avant scellement, du texte « lecture des sondes de l'étape B bis par la lentille publique » (brouillon 3 → version) — rapport v1

- **Contrôleur** : sous-agent neuf, modèle Sonnet 5.5, session mère `session_013QMayjsoZJFBUCqcnvD5h1`, le 2026-11-18. Je n'ai écrit aucune pièce de ce texte ni de ses contre-lectures. Je n'ai lu aucun résultat du programme. Je n'ai modifié aucun fichier existant ; je n'ai pas exécuté la fonction de scellement des préenregistrements.
- **Mandat** : `docs/notes/neuron-lens-v1/mandat-controle-difference-texte-lentille-publique-v1.md`, `4e3d4860299e2219b740428b1ff31c5e18d5753efaa9abd6511babb3e804d870` (empreinte vérifiée : accord).
- **Pièces** (empreintes recalculées, accord) : texte candidat `prereg/lecture-sondes-bbis-par-lentilles-v1.md` `001fd5c0ee431dfaf9ec83c2d803dceed3d85be3fbf8bbb0360d6009dea268ff` ; brouillon 3 `49b0921d…f256a` ; rapport de vérification `5398f2e9…aedc` ; liste des différences v3 `fe3122a9…5733f5e04` (le dossier porte aussi les listes v1 `67ae1706…` et v2 `9dac5875…`).

## Verdict : à sceller après ces couples exacts

La différence est celle que dit la liste v3, et chaque ligne se rattache. Un seul défaut : la phrase « rien d'autre » de la déclaration de la session mère est inexacte avec les changements 43 à 46, et le texte renvoie deux fois à la liste v1 (42 changements), qui ne contient ni ces changements ni la sortie de `diff` du texte candidat actuel. Trois couples, ci-dessous, suffisent. Aucune échappatoire neuve.

## Point 1 — la différence

- `diff -u brouillon3 candidat` rejoué : 470 lignes. Comparé octet pour octet au bloc « Sortie de `diff` » du fichier v3 : **identique**, en-têtes et dates comprises.
- Rattachement de chaque hunk (une vingtaine) : tous tombent dans les couples V-B1, V-M1, V-M2, V-M3, V-m1 à V-m13, dans les points 2 à 6 de « ce que la version finale doit porter » (entrée « Contre-lecture 2 », nœuds N8, N9, N10 tranchés, déclaration de la mère, marqueurs, section de changements, ordre du scellement) ou dans les changements 43 à 46. **Aucun changement hors de ces trois familles.**
- Deux ajouts du rédacteur, déclarés, qui ne sont dans aucun couple : (i) l'égalité des empreintes du code cité à la tête `19947280…` ; je l'ai vérifiée : les neuf fichiers de code cités et `plis_v1.py` ont, à cette tête comme à `70bdd769…`, l'empreinte écrite dans le texte (accord). (ii) la mention « (valeur du brouillon 3 ; dans la version, ≈ 14 min…) » : c'est le changement 45. Aucun n'affecte une mesure.

## Point 2 — chaque couple appliqué

Tous les couples sont appliqués à la lettre, sauf les quatre écarts déclarés, que je juge fidèles à l'intention :
- V-M1, mise en forme de la ligne d'arrêt sur deux colonnes : les mots du couple y sont, rien n'est perdu ni ajouté.
- V-m6, une seule ligne pour la lentille d'une autre empreinte : le couple demandait une seule ligne ; la lentille est retirée de la ligne « SHA-256 ou taille… » et sa taille passe dans la ligne propre. Fidèle.
- V-m8, parenthèse du nul isotrope partagé accordée (`couche` à la place de `<cellule>/<pli>/<rôle>/<vecteur>`) : conséquence nécessaire de la clé neuve ; fidèle.
- V-m10, un artefact de calibration sur deux (« scores des témoins multipliés par 1,5 ») : le couple laissait le choix ; la raison donnée (la matrice d'une autre couche ne change rien pour la lentille des logits) est exacte.
- La remarque « pour mémoire » (signe + de la requête `q`) laissée de côté : elle ne change rien à la lecture ; le texte ne définit « signe + » que pour `w` et ne le mobilise pour `q` que par les pôles, sans seuil ni libellé.
- Bornes de calibration : script rejoué (`python -I`, environnement du dépôt) ; sortie identique à la sortie scellée, hors la ligne de commande d'en-tête (empreinte du script `a8763c96…`, de la sortie `61bf13cd…` : accord). Bêta-binomiale : [23, 85] pour un jeu de 1 000, [1, 24] pour 200, [12, 53] pour trois jeux de 200, [26, 79] pour cinq jeux de 200 : égales aux exemples du texte et du couple.

## Point 3 — pas d'échappatoire neuve

Aucun seuil de succès, aucun choix laissé après lecture. Les valeurs neuves (100, 32 sur 64, 10⁻⁴, 10⁻⁶, 10⁻⁴ relatif du « rang près », 200 témoins par vecteur) sont des gardes écrites avant lecture. Chaque garde neuve a son essai sur cas sain et artefact : permutation et couche suivante (garde de lecture), formes (a), (b), (c) et leurs artefacts, bord ρ = 99 / 101, scores multipliés par 1,5, `readout.py` altéré, lentille absente, registre. Graines : clés neuves de la forme `lentilles-bbis/…` (`SeedSequence` puis `PCG64`), `essai/garde-lecture-logits-c<couche>` conforme à la forme `essai/<garde>`. Un point de lecture seulement, sans effet : la ligne d'arrêt du rapport à ε dit toujours « nuls isotropes refaits par direction » alors que le plan dit « par vecteur » pour les deux lentilles de la couche ; les deux ne se contredisent pas (même opération).

## Point 4 — la déclaration de la session mère

**Non, elle n'est plus exacte** : « rien d'autre » est faux avec les changements 43 à 46 (accords de durée, hors des couples, demandés par la mère). Le texte le dit lui-même plus bas (« Écart signalé, puis corrigé (hors des couples) »). Il faut aussi corriger deux renvois à la liste v1, qui ne porte que 42 changements et dont la sortie de `diff` n'est pas celle du texte candidat actuel : le texte cite pourtant les « changements 43 et 44 du fichier des différences », qui n'existent que dans les listes v2 et v3.

## Point 5 — validateur

`prereg.problemes('prereg/lecture-sondes-bbis-par-lentilles-v1.md')` rejoué : **liste vide**. `sceller_prereg` (lue, non exécutée, `src/controle_ia/prereg.py`) appelle `problemes` puis `sceller` : elle accepterait le fichier tel quel, et après les trois couples ci-dessous aussi (ils ne touchent ni section exigée, ni empreinte de « Contre-lecture », ni marqueur de gabarit ; l'entrée « Contre-lecture 2 » garde ses deux empreintes). Je ne l'ai pas rejouée après les couples (le texte candidat n'est pas modifié par moi) : la mère rejoue `problemes` avant de sceller.

## Couples exacts

**Couple 1** — « Ce que l'auteur savait », déclaration de la session mère.
Avant (passage entier, coupures de ligne comprises) :
```
  l'étape B bis ; elle n'a fixé aucun seuil, critère ni choix d'analyse de ce texte ; les changements du brouillon 3 à la version sont
  l'application des couples du rapport de vérification et des trois options (a), rien d'autre. Le rédacteur, qui a écrit ces
```
Après :
```
  l'étape B bis ; elle n'a fixé aucun seuil, critère ni choix d'analyse de ce texte ; les changements du brouillon 3 à la version sont
  l'application des couples du rapport de vérification, des trois options (a) et des marqueurs de version, plus quatre accords de
  durée (plan, point 6 ; « Qui, quelle machine » ; deux passages de « Contre-lecture ») que la session mère a demandés pour que les
  durées suivent le couple sur le repli de la garde du rapport à ε, rien d'autre. Le rédacteur, qui a écrit ces
```
(La ligne qui précède « l'étape B bis ; … » est inchangée ; le remplacement porte sur ces deux lignes.)

**Couple 2** — section « Changements du brouillon 3 à la version ».
Avant :
```
Application des couples avant → après du rapport de la vérification 1 (V-B1, V-M1 à V-M3, V-m1 à V-m13), des trois options (a) (N8,
N9, N10) et des marqueurs de version, rien d'autre (« Déclaration de la session mère ») ; détail ligne par ligne, rattaché à chaque
remarque, et sortie de `diff` : `prereg/pieces-lecture-sondes-bbis-par-lentilles-v1/differences-brouillon3-vers-version-v1.md` ;
traitement : « Traitement des remarques de la vérification 1 ».
```
Après :
```
Application des couples avant → après du rapport de la vérification 1 (V-B1, V-M1 à V-M3, V-m1 à V-m13), des trois options (a) (N8,
N9, N10), des marqueurs de version et de quatre accords de durée demandés par la session mère (changements 43 à 46), rien d'autre
(« Déclaration de la session mère ») ; détail ligne par ligne, rattaché à chaque remarque, et sortie de `diff` :
`prereg/pieces-lecture-sondes-bbis-par-lentilles-v1/differences-brouillon3-vers-version-v3.md` ; traitement : « Traitement des
remarques de la vérification 1 ».
```

**Couple 3** — entrée « Contre-lecture 2 », dernière phrase.
Avant :
```
appliqués tels quels, le rapport demande un contrôle de la seule différence brouillon 3 → version : liste et sortie de `diff` dans
  `prereg/pieces-lecture-sondes-bbis-par-lentilles-v1/differences-brouillon3-vers-version-v1.md`.
```
Après :
```
appliqués tels quels, le rapport demande un contrôle de la seule différence brouillon 3 → version : liste et sortie de `diff` dans
  `prereg/pieces-lecture-sondes-bbis-par-lentilles-v1/differences-brouillon3-vers-version-v3.md`.
```

(Le texte candidat, à l'empreinte contrôlée, change donc d'empreinte avec ces couples ; la liste v3 porte l'ancienne : la mère la dit à l'endroit voulu, par sa propre règle de version, sans relancer ce contrôle sur autre chose que ces trois passages.)

## Lectures hors mandat

Aucune. Lus : le mandat, les trois pièces nommées, les listes v1 (cinq lignes, pour confirmer que 43 à 46 n'y sont pas) et v2 (empreinte seulement), le script et la sortie de calibration, `src/controle_ia/prereg.py`, le texte candidat et le brouillon 3 (par `diff` et par recherche ciblée), neuf fichiers de code par `git show` aux deux têtes citées (empreintes seulement). Rien sous `diag/`, `runs/`, `donnees/`, `docs/verdicts/` ; aucun registre ; aucune branche `calcul/` ou `donnees/` ; aucune recherche récursive. Fichiers de travail dans le dossier de travail temporaire de la session. Aucun refus d'outil.
