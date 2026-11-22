# Contre-lecture du code de la première passe accordé à l'addendum de concentration — v1

Rendu du contre-lecteur neuf (Opus 5.5), versé tel quel par la session des lentilles le 2026-11-20.
- Mandat : `docs/notes/lecture-sondes-bbis-par-lentilles-v1/mandats/mandat-contre-lecteur-code-premiere-passe-addendum-v1.md` (`bdcc0d96…`), commit `e89fc392`.
- Code jugé : commit `2e15977b`, branche `claude/brave-galileo-jhp684`.

---

## 1. Verdict

**Conforme. Aucun écart bloquant.** Le code peut être fixé au registre tel quel.
- Chaque calcul, chaque garde et chaque arrêt fait ce que disent :
  - le texte de lecture v1 ;
  - l'addendum de concentration scellé ;
  - le mot de Lazar sur la garde d'égalité (option 3).
  Ni plus ni moins.
- Chaque garde est éprouvée sur un cas sain et sur un artefact (R5).

Le rendu donne aussi quatre corrections non bloquantes et deux nœuds pour Lazar. Le premier nœud (ce que l'opérateur voit dans les messages d'arrêt) est à trancher avant de lancer le calcul, pas avant de fixer le code.

## 2. Empreintes vérifiées

- **Textes qui font loi** : tous OK, lus par `git show origin/main:…`.
  - texte de lecture v1 : `ca5066d757df604c…6d572` ;
  - addendum : `7c7387088dd5956d…c22970`, identique sur la branche du développeur ;
  - mot de Lazar sur la garde d'égalité : `dbd1e5140b987ed2…3fb52fff`.
- **Code et essais** : `empreintes-code-v4.txt` contre le disque, 24 sur 24 OK.
  - Les dix modules dits inchangés ont l'empreinte de la v3.
  - `2e15977b` n'ajoute sous `src/` que `entrees_v3`, `statistiques_v3` et `lanceur_v4`.
- **Notes** : les dix compagnons `.sha256` sont OK.

## 3. Décompte des essais lancés

**Essais du paquet** : 1 125 réussis, aucun sauté, aucun en échec.
- Durée 636,9 s, de 12:50:05Z à 13:00:44Z.
- Versions : torch 2.14.1+cpu, numpy 2.4.6, scipy 1.17.1, transformers 5.18.0, pytest 9.1.1, Python 3.13.18.

**Essais jetables**, dans le bloc-notes :
1. **Les 41 bornes de calibration** :
   - recalculées par un programme indépendant en Python pur : bêta-binomiale (100 ; 1 901), convolutions, niveau 10⁻⁴ ;
   - aucun écart avec le texte, ni avec la table de l'essai : 40 bornes pour 200 témoins, et [23, 85] pour 1 000.
2. **Énumération indépendante de tous les départages** :
   - 296 nuls jouets, 3 151 directions nulles marquées, 295 nuls à au moins deux directions marquées ;
   - grandeurs comparées : marquage, S_min et S_max de la part et d'une famille, p_bas et p_haut contre les extrêmes de l'énumération conjointe, attendu sur les seules directions non marquées ;
   - 0 écart.
3. **Clé de l'addendum** : huit cas en plus des essais du développeur, 8 sur 8 conformes.
4. **Fabrique du lanceur** : rejouée sur une copie de `lanceur_v3`, elle rend `lanceur_v4` à l'octet près (`dc74be00…`).
5. **Essai du taux à petite taille** : 0,044 sous la statistique corrigée, 0,4755 sous celle du texte d'origine.

## 4. Les points 1 à 9 du mandat

**1. Les quatre précisions du développeur**
- **« Inscrite avant »** : place dans le registre **et** heure non postérieure.
  - Le texte est muet. La lecture est permise, dans le sens sévère.
- **Champ `addendum_concentration`** : permis.
  - L'addendum ne nomme pas le champ.
  - C'est une convention que la fiche doit suivre à la lettre (coordination, non nœud).
- **Aucun arrêt sur la relecture indépendante de l'audit de symétrie** : permis si l'énumération de l'étage (i) est exhaustive.
  - Mais cette liste entre dans une comparaison écrite : ambigu, c'est le nœud 2.
- **Arrêt quand toutes les directions d'un nul sont marquées** : permis.
  - La liste d'arrêt dit « valeur non finie dans une lecture ou un nul ».
  - Le cas est sans objet à M = 2 000.

**2. `bornes_de_departage` et les 41 bornes** : conformes.
- Les deux contrôles ont été faits : les 41 bornes, et les départages par force brute.
- Le retrait se fait par valeur, ce qui est exact même quand des valeurs sont égales.

**3. Place de la garde d'égalité dans `lanceur_v4`** : conforme aux trois étages de l'option 3.
- **Étage (i)** : `EgaliteDirectionLue`, levée dans `_Couche.calculer`.
  - Elle vient avant `_etiqueter`, avant `ecrire_morceaux` (l. 974) et avant les tables (l. 993).
  - Listes gardées : `lecture_signe` (l. 293 et 315, via `_signes` l. 648, repli l. 730), `poles_alignes` (l. 350, appels l. 675 et 737), lecture des pôles (l. 680), témoin de couche (l. 703 et 705).
- **Étage (ii)** :
  - `resumer_nul` (l. 610, 637 et 722) ;
  - p_bas et p_haut dans `lecture_signe`, où la valeur écrite est p_haut ;
  - `libelle_sous_departage` (l. 782 et 788), dans `_etiqueter` (l. 968), avant toute table.
- **Étage (iii)** : `_compter` (l. 613, 640 et 725). Le compte de calibration n'est pas touché.
- **Lignes de sortie égales (couple H2)** : comptées au montage (l. 444), sans arrêt.

**4. Clé de l'addendum (`entrees_v3.exiger_addendum`)**
- **Elle refuse** :
  - ligne absente ;
  - ligne en plusieurs lignes ;
  - ligne inscrite après la ligne du code ou après celle des entrées ;
  - empreinte ou chemin différents de la fiche ou de l'addendum scellé.
- **Elle est appelée avant toute requête** :
  - via `exiger_fiche_code`, en tête de `monter`, `_calculer` et `recuperer` ;
  - de nouveau dans `ouvrir_entrees` et `recuperer_entrees`.

**5. De `lanceur_v3` à `lanceur_v4`** : tout vient de l'addendum, sauf deux changements.
- **Le rapport du montage exigé au départ du calcul** : permis.
  - Il fait respecter le plan, point 1, et la règle R9.
  - Il ne change aucun calcul et il est éprouvé.
- **Un second ajout, non compté par le développeur** : le champ `egalite_au_vingtieme_rang_de_la_relecture_en_double_precision` (l. 872).
  - Il écrit seulement, sans arrêt.
  - Voir la correction 1.

**6. Essais de l'addendum (EC-5)** : tous joués, avec un cas sain et un artefact.
- **Artefact de taux** : 0,044 observé, dans l'intervalle [0,03 ; 0,065] ; 0,4755 sous la statistique d'origine.
- **Bornes du § 7** : jouées, sans saut.
- **Autres essais** : joués.

**7. Comparaison en simple précision (couple C5)** : conforme.
- Le calcul se fait en double précision et le résultat est rendu en simple.
- La comparaison `>=` compte une égalité contre v.
- Pour les témoins, `searchsorted` à gauche.
- Un essai porte sur un écart de 10⁻¹².

**8a. Le message de l'arrêt (i)**
- L'addendum exige les deux identifiants de jeton et la valeur commune ; le code les donne.
- Mais le texte v1, section « Qui », restreint l'opérateur aux codes d'arrêt, alors que le message entier sort sur la sortie d'erreur et dans `arret.json`.
- De plus, l'arrêt (ii) imprime p_bas et p_haut d'une direction lue, et le nom de la statistique.
- Aucun texte ne dit par quel canal le message passe : c'est le nœud 1.

**8b. La docstring « loi exacte » de `audits_v1`** : conforme à l'addendum, § 4, hypothèse 5.
- Les tables écrivent « de référence … approchée, non exacte », et un essai le tient.

**9. Écart d'empreinte du fichier d'essais de l'addendum**
- Le fichier commité est `cf92419d…`.
- `1abbe232…` est la version d'avant le dernier changement : le contre-lecteur l'a reconstruite.
- `sortie-essais-v4.txt` a été produite avant ce changement, comme la note de développement, § 5, le déclare.
- La course entière du contre-lecteur, sur `cf92419d`, est verte.

## 5. Corrections

**Bloquantes** : aucune.

**Non bloquantes** :
1. **Note de conformité, § 6** : « seul changement qui ne vienne pas de l'addendum » est inexact.
   - Le champ d'égalité de la relecture de l'audit (l. 872 et 874) est un second ajout.
   - Il faut le nommer dans la version suivante de la note. Aucun changement de code.
2. **Essai souhaitable** : plusieurs directions marquées dans un même nul (addendum, § 12 bis), dans `test_lentilles_sondes_bbis_garde_egalite_v1.py`. Non exigé.
3. **Essai de l'artefact de EC-4** : « ligne des entrées placée après la ligne de l'addendum mais d'heure antérieure ».
   - Le code le refuse, mais aucun essai du dépôt ne le joue seul.
4. **Docstring de `audits_v1`** : ne rien changer dans le code. La fiche du code, ou la ligne qui la cite, reprend la lecture « de référence, approchée ».

**Remarque** : à un arrêt d'égalité, l'enveloppe verse des tableaux bruts marqués « lectures interrompues, non lues » et `arret.json`, mais aucune table du texte. C'est conforme à « avant toute écriture de table ».

## 6. Nœuds à trancher par Lazar

1. **Par quel canal passe le message d'arrêt d'égalité, face au cloisonnement de l'opérateur**
   - **Contenu** : l'addendum exige des identifiants, la valeur commune, p_bas et p_haut.
   - **Opérateur** : le texte v1 le restreint aux codes d'arrêt.
   - **Aujourd'hui** : le message entier sort sur la sortie d'erreur.
2. **Portée de l'étage (i) sur la relecture indépendante de l'audit de symétrie**
   - **Question** : l'énumération est-elle exhaustive ?
   - **Aujourd'hui** : le code écrit l'égalité sans s'arrêter.
   - **Enjeu** : une réserve d'audit, aucun libellé.

## 7. Expositions et refus d'outil

- **Ouvert hors de la liste, en lecture**, ce que le mandat permet :
  - les sections « Critères de lecture gelés », « Qui », « Frontière » et « Données gardées » du texte v1 ;
  - une ligne (l. 246) de la section « Entrées exactes, et ce qui n'est jamais ouvert », vue par `grep`. Ce n'est pas la liste « Jamais ouverts » (l. 252 et suivantes). Fragment vu : « commit sert au développeur à vérifier les noms ci-dessus. **Des registres, l'opérateur ne lit que ces clés et » ;
  - une ligne de chacun des mandats du développeur et du rédacteur de la v2, vue par `grep` ;
  - l'en-tête de `table-essais-v2.md` ;
  - `empreintes-code-v3.txt` ;
  - les lignes 27 à 85 de `entrees_v1.py`.
- **Par mégarde** : un `grep -rn` de deux empreintes a parcouru `registres/` de la branche de travail. Aucune ligne n'a été affichée et aucun intitulé n'a été vu.
- **Jamais ouverts** : `diag/`, `runs/`, `donnees/`, `docs/verdicts/`, les branches `donnees/*` et `calcul/*`, et toute sortie, tout score, tout verdict, toute table.
- **Refus d'outil** : `sleep 200`, refusé. Il n'a été ni rejoué ni contourné.
- **Installation** :
  - une installation de torch depuis PyPI (bibliothèques de cartes graphiques) a été arrêtée par son identifiant de processus (25200) ;
  - torch 2.14.1+cpu a été installé dans le bloc-notes.
- **Dépôt** : aucun commit, aucun push, `git status` propre au début comme à la fin.
