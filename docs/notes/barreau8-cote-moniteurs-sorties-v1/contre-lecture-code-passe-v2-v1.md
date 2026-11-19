# Contre-lecture du code de la passe de recalcul de l'activité interne (barreau 8, côté moniteurs) — v1

- Contre-lecteur : Claude Opus 5.5 (`claude-opus-5-5`), sous-agent neuf. Je n'ai écrit ni le code (auteur : Fable 5.2), ni ses essais, ni sa notice, ni le texte préenregistré, ni la note d'interface. Je n'ai lu aucun résultat du programme et rien du saboteur.
- Heures (`date -u`) : début réel 2026-11-19T02:15:44Z ; fin de l'examen 2026-11-19T02:29:16Z ; heure de fin d'écriture en pied de rapport (2026-11-19T02:32:01Z).
- Je n'ai rien modifié dans le code, les essais, la notice ou le texte. Mes essais à moi sont restés dans le dossier de travail temporaire, hors du dépôt.

## Pièces lues et empreintes (vérifiées par `sha256sum`, toutes égales à celles qu'on m'a données)

| pièce | empreinte | lecture |
|---|---|---|
| texte, brouillon 10 : `brouillons/barreau8-lecture-sondes-v1/prereg-lecture-sondes-barreau8-v1-brouillon10.md` | `1676078f73bb75a7f0ce68653918fdf58943038d1344179bd5c2c38a78065fc1` | en entier (429 lignes) |
| code : `src/controle_ia/barreau8_moniteurs/passe_recalcul_v2.py` | `fc129f409f457b0d591e33de9346ba913c5453e097f171b744983650604c8538` | en entier (1 886 lignes) |
| essais : `tests/test_barreau8_moniteurs_passe_v2.py` | `763e2ebb2128a2239620a18a02faa32452f97eb77daee7c63ae9cabcf52753e7` | en entier |
| notice : `docs/notes/barreau8-cote-moniteurs-sorties-v1/notice-passe-recalcul-v2.md` | `9170713e493f1d9f5860042121dc4f306b48dc90db82d6063f2104080e56bd1f` | en entier |
| note d'interface v6 : `docs/notes/barreau8-cote-moniteurs-entrees-v1/interface-passe-cote-moniteurs-v6.md` | `20c9ed6e480646b6bf3a5f6007be5f88b439c916763a618f3880634e92ad8ce1` | en entier, renvois de provenance non suivis |
| `docs/notes/barreau8-iib-v1/identites-fichiers-sondes-t07-v1.md` | `fd7bf8352cfd2b66981aa9835ec561006bbd7b0d6255288429292747b9185da7` | en entier |
| `docs/notes/barreau8-iib-v1/identites-fichier-leger-sondes-figees-v1.md` | `36caffb4fe5519248fa133d3a02a7079d4e814d814ff3af3d0e45a7ffeb93398` | en entier |

Code relu pour le contexte (hors paquet interdit) : `harnais/activations.py` (en entier), `sondes/familles.py` (lignes 1 à 110), `premier_test_ia/figees.py` (en entier), `organismes/lora.py` (en entier), `harnais/formats.py` (en entier), `manifeste.py` (en entier), `t06/distillation_transcription.py` (lignes 154 à 192), `gardes.py` (`etat_git`), `harnais/modeles.py` (lignes 106 à 199, par recherche), `environnements/pilote_a.py` (`charger_taches`), `environnements/propositions.py` et `premier_test_ia/conditions.py` (par recherche de motif : attributs de l'environnement), `t07/sondes_neuves_v1.py` et `premier_test_ia/entrainement.py` (par recherche de motif : quelle fonction capte l'activité qui a servi à apprendre les sondes). Aussi lus : `.gitignore`, `requirements-cpu.txt` (versions). Je n'ai ouvert ni `lecture_sondes_v1.py`, ni aucun fichier interdit ; mes recherches de motif n'ont visé que `src/controle_ia` hors du paquet interdit (deux recherches récursives sur `src/controle_ia` ont été filtrées sur `/iib/` ; aucune ligne de ce paquet n'a été affichée).

## Dernière ligne des essais

Commande donnée, au premier plan : `86 passed in 81.86s (0:01:21)`. Dossier temporaire supprimé ensuite.

## Ce que j'ai éprouvé moi-même (hors du dépôt)

1. **Lancement par `python -m`** : `PYTHONPATH=src .venv/bin/python -m controle_ia.barreau8_moniteurs.passe_recalcul_v2 empreintes-modules`. La liste rendue compte 30 modules ; **`controle_ia.barreau8_moniteurs.passe_recalcul_v2` n'y est pas** (lancé ainsi, ce module s'appelle `__main__`). Voir remarque 1.
2. **Mutations du code** (copie chargée en mémoire, jamais écrite dans le dépôt), puis les deux essais du cas sain qui comparent la livraison à un recalcul :
   - début de la capture décalé d'une position (`debut = L - len(a.ids) - 1`) : attrapé par l'essai contre la passe unique du harnais (ligne 547 des essais) ; **non vu par l'essai du recalcul des scores sur l'activité livrée** (attendu : le texte dit que la garde de réception r6 ne voit ni la couche ni la position) ;
   - crochet posé sur le bloc voisin (`self.blocs[c - 1]`) : même constat ;
   - deux actions d'un lot échangées : la passe plante (forme incompatible), donc l'erreur est vue.
   Sans mutation, les deux essais passent. La convention des couches est donc tenue par **un seul essai** du code, ce que le texte déclare déjà.
3. **Garde des chemins sur une sortie dont le nom porte « iib »** : écrire `passe-iib-sortie/x.npz` sous surveillance donne « garde P8 non tenue : ouverture d'un chemin privé refusée » et « chemin privé lu : oui ». Voir remarque 2.
4. **Décodage avec le paramètre explicite** sous `transformers` 5.18.0 / `tokenizers` 0.23.2 (jetoniseur rapide minimal construit sur place, sans téléchargement) : le paramètre `clean_up_tokenization_spaces` est accepté et change la sortie (`'a,b'` contre `'a ,b'`).
5. **Essai de la garde du contrôle du contexte sans modèle ajusté**, avec des vraisemblances simulées : 4 essais passent en 1,3 s (voir « Jugement sur la fragilité »).

## Table de conformité, section par section

« Conforme » veut dire : le code calcule ce que le texte écrit, sans rien ajouter qui compte. Les numéros de ligne renvoient au texte (T) et au code (C).

| passage du texte | fonction (C) | verdict |
|---|---|---|
| Entrées : extrait du côté exposé à forme fermée, six clés, clés répétées refusées (T98) | `lire_extrait_du_cote_expose` (C677-732), `garde_p1` (C735-764) | conforme, avec un choix en plus : les lignes `etats_par_lot_evaluation` doivent être **strictement** croissantes (C727-730) ; le texte dit « rangées » (remarque 5) |
| Quatre fichiers de la course pris aux chemins de l'extrait, comparés par empreinte (T98, T289) | `garde_p1` (C745-752) | conforme |
| Tâches à l'empreinte de la note (T289) | `garde_p1` (C753-756) | conforme |
| Fichiers de sondes et de planchers à leurs empreintes entières ; arrêt si absent ou différent (T289, T324) | `garde_p1` (C757-762), `regle_des_sondes_lues` (C919) | conforme |
| Contextes rebâtis par la recette de la question (6) (T236 ; note d'interface, question 6) | `rebatir_episodes` (C1159-1189) | conforme ; l'essai `test_reconstruction_egale_a_la_fonction_du_depot` le compare à `transcription_honnete` |
| Contexte sans texte privé (T236, P8) | C1173-1174 | conforme |
| Conditions et doses : H 0, B50 0,5, B100 1, TJ100 1 (témoin-jumeau) ; rang 16, alpha 32, quatre projections (T63) | `SPECIFICATION_TEXTE` (C172-174), `Adaptateurs` (C1086-1135) | conforme |
| Pose : injecter, simple précision, charger l'état, fixer la dose (note, question 5) | C1092-1093, C1110-1117 | conforme |
| Lots de 8 de la même condition, ordre des clés, H puis B50 puis B100 puis TJ100, seules les actions d'au moins un jeton noté (T238) | `lots_par_condition` (C1362-1368), C1709-1713 | conforme |
| Remplissage à gauche, jeton 128001, masque et positions (T65, note question 7) | `lot_a_gauche` (C1210-1221), `pad = min(fmt.fins)` (C1694) | conforme |
| Couches 7, 15, 23 : sortie du bloc d'indice ℓ à partir de 0, définition de `harnais/activations.py` (T239) | `CrochetsSurCarte` (C1224-1251) | conforme (voir « Exactitude ») |
| Positions : jetons notés, jeton final exclu s'il est de fin (T240) | C843, C1280-1286 | conforme |
| Précision : capture en simple précision, produit en double précision sur la carte, scores en `float64` (T242) | `type_de_capture` (C1286), `produit_sur_carte` (C1297-1302) | conforme |
| Score par action : w·h + b, w et b par `lire_sondes` seul, maximum (production) et moyenne (bras de diagnostic) (T243) | `regle_des_sondes_lues` (C919), `noter_action` (C1345-1359) | conforme ; le maximum est la seule agrégation de production ; la moyenne n'apparaît que dans `moyenne_du_bras_de_diagnostic_jamais_en_production` (C1310-1314), appelée une seule fois (C1355) ; aucune médiane |
| Scores par jeton des neuf sondes, sans planchers (T245) | C1337, C1356-1357, C1533 | conforme |
| Liste fermée des directions et ordre des colonnes (T244, T261) | `SPECIFICATION_TEXTE` (C177-196), `regle_des_sondes_lues` (C921-956) | conforme ; un écart mineur : le compte des 800 directions de plancher par préfixe ne refuse pas une 801e entrée du même préfixe (remarque 11) |
| Sous-échantillon : clés triées des actions notées, rangs multiples de 16 (et 128) et la dernière ; première passe (T246) | `sous_echantillons` (C1192-1203), C1724-1726, C1744-1745 | conforme (161 et 21 vérifiés par l'essai `test_specification_du_texte`) |
| Action sans jeton noté : aucune passe, `NaN` partout, aucune ligne de scores par jeton, hors du sous-échantillon, de P7, de P10 (T241) | C1709-1710, C1196, C1462 | conforme |
| P0 (T288) | `garde_p0` (C587-645), `verifier_modules_inchanges` (C648-653) | **écart** : le module de la passe lui-même n'est pas contrôlé quand il est lancé par `python -m` (remarque 1) |
| P1 (T289) | `garde_p1`, `regle_des_sondes_lues`, C1700-1703 | conforme |
| P2 (T290) | `garde_p2` (C1026-1060) | conforme, **et plus strict** que le texte : type des poids, attention, jeton de début, date du gabarit (remarque 7) |
| P3 (a) à (d), avant les poids (T291) | `garde_p3_structure` (C811-849), `lire_nettoyage_des_espaces` (C852-872), `garde_p3_decodage` (C880-891), ordre C1661-1684 | conforme |
| P4 avant et après chaque lot (T292) | `Adaptateurs.relire` (C1119-1135), `capturer_lot` (C1261-1266, C1277) | conforme |
| P5, P6 (T293-294) | `capturer_lot`, `noter_action`, `ecrire_fichiers_de_donnees` | conforme |
| P7 : seconde passe du sous-échantillon, ordre inverse, 99e centile ≤ 0,2, contrôle négatif décalé d'un jeton, au moins 10 actions d'au moins 5 jetons, 95 % (T295) | C1728-1741, `garde_p7` (C1390-1423) | conforme |
| P8 : liste fermée des chemins lus, motifs privés hors de la liste (T296) | `SurveillanceLectures` (C354-400), C1625-1632 | **écart** : la règle des motifs s'applique aussi aux **écritures** et aux sous-arbres permis (sortie, fichiers du modèle), qui ne sont pas dans la liste fermée du code ; et la liste réellement permise est plus large que celle du texte (remarques 2 et 8) |
| P9 : durée, dépense, taille, réserve de 4 000 000 octets (T297) | `garde_p9_duree`, `garde_p9_taille`, C1752-1755, C1798-1801 | conforme sur le fond ; le second contrôle de taille arrête **sans** marquer P9 « non tenue » (remarque 3) |
| P10 : sous-échantillon de 4 jetons notés ou plus, (i) contre (ii), 95 % et au moins 10, artefact décalé d'une tâche, avant la passe (T298) | `garde_p10` (C1447-1495), `log_vraisemblances` (C1426-1444) | conforme ; essai fragile (voir « Jugement ») |
| Livraison « Noms et champs » : morceaux, archives déterministes, listes nommées en `uint8` JSON (T260) | `ecrire_npz_deterministe`, `decouper_en_morceaux`, `json_en_octets` (C422-483) | conforme |
| (1) scores par action, libellés exacts `"maximum (production)"` et `"moyenne (bras de diagnostic, jamais en production)"` (T261) | C1544-1549 | conforme |
| (2) scores par jeton, `colonnes` (T262) | C1550-1552 | conforme |
| (3) index, dix champs, clés triées (T263) | `lignes_de_l_index` (C1502-1512), C1553-1557 | conforme |
| (4) activité brute, tableaux `a` + valeur du champ `rang` sur cinq chiffres (T264, changement du brouillon 10) | C1558-1561 | conforme |
| (5) trace, vingt clés (T265) | C1767-1789 | conforme ; `egale_a_l_extrait` est écrit « oui » en dur (remarque 10) |
| (6) bordereau (T266) | C1793-1802 | conforme |
| Taille et réserve (T267, changement du brouillon 10) | C80, C1753 | conforme |
| Graines : `repetabilite-passe`, `injection-adaptateurs` ; graine entière = premier mot de 64 bits de `generate_state` (T170) | C64-65, C1672, `_graine_entiere` (C1606-1609) | conforme ; le commentaire C65 (« clé propre à ce code ») est périmé : le texte la nomme désormais (remarque 12) |
| Registre propre : quatre colonnes, une ligne par clé, clé hors des six refusée, scellement en premier, code postérieur strictement (T302-305, changement du brouillon 10 « une ligne par clé ») | `lire_registre_propre` (C511-539), `garde_p0` (C604-617) | conforme |
| Bordereau du code à sept clés (T306) | `contenu_du_bordereau_du_code`, `lire_bordereau_du_code` (C548-577) | conforme sur la forme ; incomplet sur le fond (remarque 1) |
| Condition de départ D-13 : ce que la passe tire de l'extrait, et rien d'autre (T98) | C731-732, C1658, C1770 | conforme |
| Ce que la passe ne calcule jamais (T247) | ensemble du module | conforme : aucune aire, aucune statistique par condition |
| Garde de P8 sur « iib » seulement hors de la liste fermée (changement du brouillon 10) | C382-389 | conforme pour la liste fermée du code ; écart pour les fichiers du modèle et l'invite que le texte met dans sa liste fermée (remarque 2) |
| Trace d'arrêt, non livrée, avec la cause et « non jouée » (T256) | C1639-1649 | conforme |

## Exactitude du calcul

- **Indice des couches.** Le code des sondes existant définit l'activité de la couche ℓ comme la sortie du bloc de décodeur ℓ, indice à partir de 0 (`src/controle_ia/harnais/activations.py`, lignes 3 à 5 ; `blocs_decodeur`, lignes 27 à 29 ; crochet posé sur `blocs[c]`, ligne 73). Les sondes ont été apprises par cette même voie (`src/controle_ia/t07/sondes_neuves_v1.py`, lignes 177 et 178 : `passe_unique` ; `src/controle_ia/premier_test_ia/entrainement.py`, ligne 21). La passe pose son crochet sur `blocs_decodeur(modele)[c]` (C1229, C1244). Aucun usage de `output_hidden_states` dans `src/controle_ia` hors du paquet interdit. **La « couche 15 » de la passe est donc celle des sondes.** Une erreur d'un rang n'est vue que par l'essai `test_cas_sain_couche_contexte_et_adaptateur_contre_la_passe_unique_du_harnais` (je l'ai vérifié par mutation).
- **Positions dans un lot rempli à gauche.** La transcription de chaque action finit par ses identifiants (C1270) ; `debut = L - len(a.ids)` (C1280) ; les `jetons_notes` premiers jetons de l'action sont pris (C1286). Exact ; une mutation d'une position est attrapée par le même essai.
- **Biais des directions de plancher.** `b` est lu tel quel dans l'index par `lire_sondes` (`figees.py`, ligne 68) et passé sans transformation (C943-945) ; le score est `capture @ w.T + b` en `float64` (C1302), même formule que `SondeLineaireJetons.scores_par_jeton` (`familles.py`, ligne 76).
- **Type numérique du produit.** Capture convertie de `bfloat16` en `float32` (exacte), puis en `float64` ; vecteurs et biais exigés en `float64` (C1300).
- **Adaptateurs et dose.** L'empreinte relue sur le modèle (`empreinte_adaptateurs`, `lora.py`, lignes 123 à 128) est comparée à celle de l'état du fichier converti en `float32` (C1076-1083) : même recette. Dose relue sur chaque module avant et après chaque lot.
- **Ordre des actions.** Lignes du tableau indexées par `rang` (ordre du fichier) ; lots par condition dans l'ordre du fichier ; un échange de deux actions dans un lot est vu.
- **Tirage du sous-échantillon.** Tri des clés par le tri des chaînes de Python, rangs multiples de 16 (128) et la dernière : exact, sans graine.
- **État qui survivrait d'un lot à l'autre.** Les crochets et leur dictionnaire sont neufs à chaque lot ; la dose est refixée à chaque pose ; aucune fuite entre conditions trouvée. Les sorties de couche sont gardées par référence (`h.detach()`, C1240) et non copiées ; sans opération en place dans le modèle, c'est sans effet (MINEURE, remarque 13).

## Remarques numérotées

**1. BLOQUANTE — le module de la passe n'est jamais contrôlé par son empreinte quand on le lance comme la notice le dit.** Fichier : `passe_recalcul_v2.py`, `modules_charges`, lignes 490 à 496 ; appelée par `contenu_du_bordereau_du_code` (C555), `garde_p0` (C627) et `verifier_modules_inchanges` (C649). Défaut : lancé par `python -m controle_ia.barreau8_moniteurs.passe_recalcul_v2` (notice, section « Ligne de commande exacte »), le module s'appelle `__main__` dans `sys.modules` ; `modules_charges` ne garde que les noms qui commencent par `controle_ia`, donc le module qui fait tout le calcul n'est **ni porté au bordereau du code, ni comparé à l'ouverture, ni relu à la fin**. Constaté : la liste imprimée par `empreintes-modules` lancée ainsi ne le porte pas. Le texte exige « les modules `controle_ia` chargés par la passe sont exactement ceux du bordereau, aux mêmes empreintes » (T288) et que les empreintes des modules chargés soient comparées à la ligne `CODE-PASSE-IIB` (T191). L'essai `test_ligne_de_commande_refuse_un_parametre_absent_et_liste_les_modules` (essais, ligne 667) donne une fausse assurance : il appelle `principal` dans le processus des essais, où le module est importé sous son vrai nom. Correction proposée :

```python
def modules_charges() -> dict[str, str]:
    """Empreinte de chaque module du paquet `controle_ia` chargé dans ce processus, y compris le module lancé par
    `python -m` (nommé `__main__` dans `sys.modules`), porté sous le nom de son paquet."""
    sortie = {}
    for nom, m in sorted(sys.modules.items()):
        if nom == "__main__":
            spec = getattr(m, "__spec__", None)
            nom = getattr(spec, "name", None) or ""
        if (nom == "controle_ia" or nom.startswith("controle_ia.")) and getattr(m, "__file__", None):
            if nom in sortie and sortie[nom] != empreinte(m.__file__):
                raise GardeArret(f"module {nom} chargé deux fois avec deux empreintes")
            sortie[nom] = empreinte(m.__file__)
    return sortie
```

et dans `contenu_du_bordereau_du_code`, prendre le fichier par `modules_charges()` plutôt que par `sys.modules[nom].__file__` (C556, qui lèverait `KeyError` pour ce nom). Essai à ajouter : lancer en sous-processus `python -m controle_ia.barreau8_moniteurs.passe_recalcul_v2 empreintes-modules` et exiger la ligne `<empreinte du fichier>  controle_ia.barreau8_moniteurs.passe_recalcul_v2`.

**2. À CORRIGER (risque de perdre une passe payée) — la règle des motifs privés de P8 s'applique aux écritures et aux sous-arbres permis, et la sortie n'est écrite qu'à la fin.** Fichier : C376-395 (`noter`), C1628 (sous-arbres), C1742-1748 (première écriture dans la sortie). Défaut : `noter` teste les motifs (« iib », « ii-b », …) **avant** les sous-arbres permis et pour tout mode d'ouverture. Une sortie dont un composant porte « iib » (plausible chez l'exécutante de la course « ii-b ») est refusée à la première écriture, c'est-à-dire **après** la première et la seconde passe ; la trace d'arrêt dit alors « chemin privé lu : oui », ce qui est faux (c'est une écriture). Constaté par mon essai. De même pour un cache du modèle dont le chemin porte un motif, alors que le texte met « les fichiers du modèle » dans sa liste fermée et dit qu'un chemin de la liste fermée n'est jamais refusé par ce motif (T296). Correction proposée : (a) à l'ouverture, avant P0, refuser (garde P8 non tenue, cause écrite) toute sortie, `runs/<run_id>`, `diag/<run_id>` ou dossier de cache dont un composant porte un motif privé, de sorte que l'arrêt coûte zéro minute de carte ; (b) ne pas compter comme « lu » une ouverture en écriture dans la sortie, `runs/<run_id>` ou `diag/<run_id>` :

```python
_ECRITURE = ("w", "a", "x", "+")
def noter(self, chemin, mode=None, drapeaux=None) -> None:
    ...
    c = _abs(chemin)
    ecrit = (isinstance(mode, str) and any(x in mode for x in _ECRITURE)) or (
        isinstance(drapeaux, int) and drapeaux & (os.O_WRONLY | os.O_RDWR | os.O_CREAT))
    if ecrit and any(_sous(c, a) for a in self.sorties):      # sortie, runs/<run_id>, diag/<run_id>
        return
    ...
```

Essais à ajouter : sortie nommée `…-iib-…` refusée **avant P0** ; écriture dans une sortie saine permise ; « chemin privé lu » reste « non » pour une écriture. La notice doit le dire en une ligne.

**3. À CORRIGER — un arrêt de taille sans garde « non tenue ».** Fichier : C1798-1801. Défaut : le second contrôle de taille (après la trace et avant le bordereau) lève `GardeArret` directement, **après** `trace.clore("P9")` (C1755) ; la trace d'arrêt porte alors P9 « tenue » alors que la passe s'est arrêtée sur la taille. Contraire à « aucun repli silencieux » et à l'esprit de « aucune ligne tenue ne peut s'écrire sans que la garde ait tourné ». Correction : avant `raise`, `trace._g["P9"]["etat"] = "non tenue"` n'est pas permis par l'objet ; ajouter à `TraceGardes` une méthode `rouvrir_non_tenue(nom, cause)` qui force l'état « non tenue » même après clôture, et l'appeler ici ; ou déplacer la clôture de P9 après l'écriture du bordereau. Essai : spécification jouet dont `taille_max` laisse passer le premier contrôle et pas le second ; exiger P9 « non tenue » dans la trace d'arrêt.

**4. À CORRIGER — l'essai à blanc de la notice ne voit rien avant de louer la carte au-delà des entrées.** Fichier : notice, section « Ce qui n'a pas pu être éprouvé ici, et l'essai à blanc » ; code C1666-1668. Défaut : `verifier-entrees` s'arrête après la règle des sondes. Or le chargement du jetoniseur, la lecture du réglage du nettoyage des espaces, la clause (b) de P3 sur les 2 560 actions, les pièces du gabarit et la reconstruction des 256 épisodes n'ont besoin que du jetoniseur et des fichiers de configuration, **pas de la carte**. La notice dit qu'il n'existe pas de mode « une action » et renvoie ces contrôles sur la carte. Correction proposée : étendre `verifier-entrees` (sans manifeste, sans aucune écriture) à `chargeur.jetoniseur()`, `lire_nettoyage_des_espaces`, `garde_p3_decodage`, les pièces de P2 qui ne demandent pas les poids (premier jeton de clôture, jeton de début, marque de la date), `rebatir_episodes`, `sous_echantillons`, et au contrôle d'ouverture de la remarque 2 ; rendre en plus la plus grande longueur de transcription d'un lot (utile pour la mémoire de la carte). Essai : sur le jouet, `verifier-entrees` rend la plus grande longueur et ne charge aucun poids. Préciser aussi que `--debut-location` doit être une heure passée pour `verifier-entrees` (sinon P9 refuse).

**5. À CORRIGER (lacune du texte ou choix du code) — ordre strict des lignes `etats_par_lot_evaluation`.** Fichier : C727-730. Défaut : deux lignes de même condition et de même lot sont refusées ; le texte dit « rangées par condition dans cet ordre, puis par lot » (T98), sans « strictement » ni « une ligne par lot ». Ce refus arrive à P1, avant la carte (et `verifier-entrees` le voit). Correction : soit le texte écrit « strictement croissantes : une ligne par (condition, lot) », soit le code accepte l'égalité (`if precedent is not None and rang < precedent`). Je recommande d'écrire le texte (le code a raison sur le fond si la course écrit une ligne par lot), confiance moyenne.

**6. À CORRIGER — l'artefact de la garde du contrôle du contexte n'éprouve pas la reconstruction.** Fichier : essais, `test_p10_artefact_contextes_decales_d_une_tache` (ligne 1411) ; code C1472-1473. Défaut : le défaut injecté (`decalage_de_tache_p10`) décale seulement les contextes **choisis par la garde**, pas ceux que `rebatir_episodes` construit et que la passe emploie. Rien n'éprouve que P10 voit une reconstruction fausse. Essai à ajouter : remplacer, par `monkeypatch`, `FormatChat.tour` ou l'environnement de `rebatir_episodes` de sorte que chaque épisode reçoive l'observation d'une autre tâche ; exiger « garde P10 non tenue : contexte rebâti » et P7 « non jouée ». Voir aussi l'essai sans réglage proposé plus bas.

**7. MINEURE (lacune du texte) — P2 contrôle plus que le texte.** Fichier : `garde_p2` (C1043-1059). Le texte (T290) dit : révision, 32 couches, 4 096, jetons de fin, premier jeton de clôture. Le code refuse aussi un type des poids autre que `bfloat16`, une attention autre que `sdpa`, un jeton de début autre que 128000, une ouverture du gabarit sans « Today Date: 26 Jul 2024 ». Ces valeurs viennent de I-2 et I-7 et la notice les liste ; c'est plus strict, sans danger, mais non écrit dans la garde du texte. Phrase proposée pour le texte, ligne P2 : « …et, d'après I-2 et I-7, poids en `bfloat16`, attention `sdpa`, jeton de début 128000, ouverture du gabarit portant la date figée ».

**8. MINEURE — liste réellement permise par P8 plus large que celle du texte.** Fichier : C1628-1630. Le code permet en entier `src/`, `.venv/`, `.git/`, le dossier des invites publiées (et non la seule invite `H1-classification`), `sys.prefix`. Lire le code et les bibliothèques est nécessaire ; mais `.git/` en entier permettrait de lire des objets git de n'importe quelle branche sans que les motifs privés ne se voient (les noms d'objets sont des empreintes). Le code n'en lit aucun. Correction : retirer `.git` des sous-arbres (le commit est lu par `git` en sous-processus, qui ne passe pas par le crochet) et restreindre les invites au fichier de `H1-classification` ; ou déclarer cette liste dans la notice et le texte.

**9. MINEURE — mémoire annoncée par la notice : le compte est à refaire.** Notice, sections « Exigence posée à la machine » et « Durée et mémoire attendues ». Mon compte, pire cas : captures de la première passe gardées pour le sous-échantillon, trois couches : 161 × 400 × 4 096 × 4 × 3 = 3 165 388 800 octets (3,17 Go) ; seconde passe : autant ; scores par action 98 672 640 octets ; scores par jeton 73 728 000 octets, plus autant pour leur concaténation (C1533) ; fichier des sondes neuves chargé en entier par `lire_sondes` : environ 0,43 Go, temporaire ; l'écriture des archives est en flux (pas de copie de 1,1 Go). Soit **environ 7 Go** pendant la passe, plus le processus et les bibliothèques de la carte (2 à 3 Go). Mais `ChargeurReel.poids` (C1017-1019) charge le modèle **en mémoire vive d'abord** puis le déplace sur la carte : environ 16 Go transitent par la mémoire vive au chargement. Phrase proposée pour la notice : « au moins 24 Go de mémoire vive au total : le modèle (16 Go) transite par la mémoire vive au chargement ; la passe garde ensuite environ 7 Go ». Disque : 1,5 Go de livraison, plus l'archive entière de la couche 15 (1,06 Go) le temps de son découpage : environ 2,6 Go au plus ; les 3,5 Go de la notice suffisent.

**10. MINEURE — `egale_a_l_extrait` écrit « oui » en dur.** Fichier : C1780. C'est vrai par construction (P1 arrête sinon, C750 et C1701), mais la trace doit être écrite par les gardes. Correction : garder le résultat de la comparaison de P1 et l'écrire.

**11. MINEURE — 800 directions par préfixe : une 801e ne serait pas refusée.** Fichier : C933-938. Le texte (T324, condition (iv)) dit que le fichier « porte exactement 800 directions de famille plancher … désignées comme dans la table ». Pour les planchers par préfixe, le code prend les noms 0 à 799 sans vérifier qu'aucune autre entrée ne porte ce préfixe. Correction : `conforme = conforme and sum(p.nom.startswith(d.prefixe_plancher) for p in source) == spec.n_plancher`. Essai : fichier jouet avec une direction `…-plancher-5` en plus, sonde « sans objet ».

**12. MINEURE — commentaire périmé.** C65 : « clé propre à ce code, sans effet sur les sorties (notice) » ; le texte (T170) nomme maintenant `injection-adaptateurs`. Écrire « clé du texte (plan, point 5) ».

**13. MINEURE — sorties de couche gardées par référence.** C1240 : `self.sorties[couche] = h.detach()` sans copie ; si une version future des bibliothèques modifiait le flux résiduel en place, les captures seraient fausses et P7 (même mécanisme aux deux passes) ne le verrait pas. Le harnais copie (`activations.py`, ligne 69). Correction : `h.detach().clone()` (coût : trois tenseurs du lot, sur la carte).

**14. MINEURE — condition sans aucun lot.** C1764 : si toutes les actions d'une condition sont sans jeton noté, `egaux` reste `None` et la trace dit « non » : la livraison serait refusée à la réception (r4), alors que le texte prévoit pour `H` la ligne S4 (sans objet) sur une livraison reçue. Cas limite ; écrire « sans objet : aucun lot » ou le dire au texte.

## Lacunes du texte (phrases proposées)

- **P10 ne voit pas une erreur commune à tous les contextes.** Les contextes (i) et (ii) sont rebâtis par la même recette : une erreur de gabarit, d'invite, de date ou de mise en forme des observations, commune à toutes les tâches, laisse (i) au-dessus de (ii). Phrase proposée, fin de la ligne P10 : « Limite déclarée : la garde ne voit que l'appariement d'un contexte à sa tâche ; une erreur de reconstruction commune à toutes les tâches lui échappe, et n'est tenue que par l'essai du code contre `transcription_honnete` et par P3 (b). »
- **Module lancé par `python -m`** (remarque 1) : phrase proposée pour P0 : « …les modules `controle_ia` chargés par la passe, **y compris le module lancé**, sous le nom de son paquet… ».
- **P8 et les écritures** (remarque 2) : « la liste fermée porte sur les lectures ; les écritures de la passe ne se font que dans la sortie, `runs/<nom de la passe>` et `diag/<nom de la passe>`, dont aucun composant ne porte un motif privé, contrôlé à l'ouverture ».
- **Lignes `etats_par_lot_evaluation`** : « strictement croissantes, une ligne par (condition, lot) » (remarque 5).
- **P2** : la phrase de la remarque 7.

## Jugement sur la fragilité de l'essai du contrôle du contexte

Le modèle jouet est ajusté 110 pas, sous graine, **sur les suites mêmes que chaque tâche doit produire** (essais, lignes 75 à 107) ; les actions de la course jouet sont tirées de ce modèle (lignes 180 à 224). Le nombre de pas a été choisi **après** un échec du cas sain à 70 pas (0,88). La garde n'a pas été touchée (ses seuils sont ceux du texte), mais le **cas sain** a été réglé jusqu'à passer, avec une marge d'une action (24 sur 25 contre 95 %). Ce que l'essai prouve honnêtement : la voie entière de la garde tourne, et l'artefact (contextes décalés d'une tâche, 0,24) est vu avec une grande marge. Ce qu'il ne prouve pas : que le seuil est appliqué juste à sa frontière, que l'égalité ne passe pas, que les contextes (ii) sont ceux du même pas et de la même condition pour la tâche suivante. Il est aussi exposé à un changement de noyau de calcul (une version de `torch` peut faire basculer une action). Il ne dit **rien** du modèle réel, où des actions courtes et génériques peuvent avoir une vraisemblance presque indépendante de la tâche.

**Essai proposé, sans aucun réglage** (écrit et lancé ici, 4 essais passés en 1,3 s ; texte complet ci-dessous, à verser dans les essais) : la vraisemblance est remplacée par une fonction qui vaut 1 si le contexte appartient à l'épisode de l'action, 0 sinon ; on fixe exactement le nombre d'actions qui passent.

```python
SPEC = dataclasses.replace(P.SPECIFICATION_TEXTE, n_taches=20, pas_par_episode=1)

class AdaptateursFactices:
    def poser(self, condition): pass
    def relire(self, condition, actions=0): pass

def monde(n_taches, fautives):
    actions, episodes = [], {}
    for k in range(n_taches):
        t = f"t{k:02d}"
        actions.append(P.Action(k, f"evaluation-H/{t}/pas0", "evaluation-H", t, t, "H", 0, "", [10 + k] * 5 + [1], 5))
        episodes[("H", t)] = P.Episode("H", t, [-1 if k in fautives else 1000 + k, 7], [(2, 8)])
    return actions, episodes

def appel(actions, episodes, monkeypatch):
    vus = []
    def vraisemblances(modele, pad, contextes, suites):
        vus.extend((c[0], s[0]) for c, s in zip(contextes, suites))
        return [1.0 if c[0] == 1000 + (s[0] - 10) else 0.0 for c, s in zip(contextes, suites)]
    monkeypatch.setattr(P, "log_vraisemblances", vraisemblances)
    r = P.garde_p10(SPEC, None, 0, AdaptateursFactices(), actions, episodes, {a.rang for a in actions}, P.TraceGardes())
    return r, vus

def test_frontiere_tenue(monkeypatch):            # 19 sur 20 = 0,95 : tenue (borne comprise)
    r, vus = appel(*monde(20, {3}), monkeypatch)
    assert r["fraction"] == 0.95 and r["artefact"]["fraction"] == 0.0 and len(vus) == 60

def test_frontiere_non_tenue(monkeypatch):        # 18 sur 20 = 0,90 : non tenue
    with pytest.raises(GardeArret, match="contexte rebâti"):
        appel(*monde(20, {3, 4}), monkeypatch)

def test_moins_de_dix(monkeypatch):
    with pytest.raises(GardeArret, match="9 action"):
        appel(*monde(9, set()), monkeypatch)

def test_egalite_ne_passe_pas(monkeypatch):
    actions, episodes = monde(20, set())
    monkeypatch.setattr(P, "log_vraisemblances", lambda m, p, c, s: [0.5] * len(c))
    with pytest.raises(GardeArret, match="garde aveugle|contexte rebâti"):
        P.garde_p10(SPEC, None, 0, AdaptateursFactices(), actions, episodes, {a.rang for a in actions}, P.TraceGardes())
```

Recommandation : verser cet essai, garder l'essai du jouet comme essai de bout en bout (sans en faire l'essai du seuil), et ajouter l'artefact sur la reconstruction de la remarque 6. Déclarer dans la notice que la marge du jouet est d'une action et que le réglage a été choisi après un échec (c'est fait : section « Sur les essais »).

## Gardes et règle R5 : ce que j'ai vérifié

- Chaque garde P0 à P10 a un cas sain (la passe entière du jouet, toutes gardes « tenue ») et au moins un artefact qui la rend « non tenue » **elle**, vérifié dans la trace d'arrêt pour P1, P2, P4, P7, P8, P9, P10 dans la passe entière, et dans la trace de la fonction pour P0, P3, P5, P6.
- Une garde ne peut pas être écrite « tenue » sans contrôle (`TraceGardes.clore`, C309-314, éprouvé). Exception : la remarque 3.
- Replis : aucun `try`/`except` large dans le chemin de calcul ; `except ValueError` (C689, C866) conduit à un refus ; `except BaseException` (C1639) écrit la trace d'arrêt puis relève l'erreur ; aucun `warnings`. `ChargeurReel.poids` saute le contrôle de la révision relue si `_commit_hash` est absent (C1020-1022) ; la révision reste tenue par le nom du dossier (C986) : acceptable.

## Ce qui peut casser au premier lancement réel

1. **Contrôle du code incomplet sans que rien ne casse** : remarque 1 ; P0 sera « tenue » sur un module de la passe non contrôlé.
2. **Sortie, `runs/<nom>` ou cache dont un composant porte « iib » ou « ii-b »** : la sortie fait tout perdre **à la fin** (remarque 2) ; le cache arrête au chargement du jetoniseur (peu coûteux).
3. **Fichiers de sondes** : les fichiers des sondes neuves et des planchers sont sur la branche `origin/donnees/t07-etape-a-v1`, absents de `main` ; le premier est versé en neuf morceaux. La notice ne parle que de reconstituer le premier, sans commande, et ne dit pas d'aller chercher le second sur cette branche, ni de vérifier les deux compagnons `.sha256` (`sha256sum -c`). `verifier-entrees` le verra avant la carte, à condition de le jouer.
4. **Dépôt non propre** : `creer_manifeste` refuse un arbre non propre (fichiers non suivis compris, `gardes.etat_git`), sauf `--autoriser-depot-sale`. `donnees/` est ignoré par git ; mais un extrait, un registre ou un bordereau posé sans être committé arrête la passe après les gardes d'entrée (peu coûteux, sans carte) ; la notice ne le dit pas.
5. **Contrôle du contexte sur le modèle réel** : la marge sur le jouet est d'une action ; sur le modèle réel, une action générique peut ne pas dépendre de sa tâche ; un refus à 95 % arrête avant la première passe (minutes de carte) et devient un écart, nœud de Lazar.
6. **Mémoire vive** : le modèle transite par la mémoire vive au chargement (remarque 9).
7. **Mémoire de la carte** : passe avant sans cache sur des lots de 8 transcriptions qui vont jusqu'au pas 9 ; longueur non connue ici (la note d'interface ne l'estime pas). Les lots de P10 portent des actions de tous les pas et passent en premier : un dépassement se verra donc tôt. `logits_to_keep=1` (C1275) évite les logits de toute la séquence ; P10 ne calcule les logits que sur les positions de l'action (C1437) : bien.
8. **Noms d'arguments des bibliothèques** : `dtype=`, `attn_implementation=`, `logits_to_keep=` et le paramètre de décodage sont ceux de `transformers` 5.18.0 (version du dépôt et de la course, note d'interface, question 2) ; je l'ai vérifié pour le décodage. La passe ne compare pas les versions chargées à celles de l'extrait (le texte ne le demande pas) ; P3 (b) tient le jetoniseur.
9. **Heure de début de location** : doit être passée et à la seconde pour `verifier-entrees` et la passe (P9 refuse une durée négative).
10. **Fin de passe** : contrôles de taille, relecture des modules, écriture du journal sous `diag/<nom>` ; un échec à ce moment perd la passe. Aucun essai à blanc ne les joue avant (remarque 4).

**L'essai à blanc de la notice ne suffit pas** à voir les points 2, 5, 6, 7 et 10 avant de payer la passe entière ; avec la remarque 4 et le contrôle d'ouverture de la remarque 2, les points 2, 3, 4 et une bonne part de 10 se verraient sans carte, et 5 et 7 dans les premières minutes de carte.

## Séparation

- **Lectures** : liste fermée des pièces de P0 et des entrées de P1 ; les quatre fichiers de la course pris aux chemins de l'extrait ; tâches ; sondes ; jetoniseur et modèle ; invites publiées. Aucun fichier d'oracle ni de l'étalonnage n'est nommé par le code ; tout autre fichier du dépôt est refusé à l'ouverture (éprouvé). Réserves : remarques 2 et 8.
- **Livraison** : scores (`scores`, `directions`, `agregations`), scores par jeton (`scores`, `colonnes`), index (dix champs), activité brute, trace (vingt clés, sans chemin, texte ni identifiant de jeton : vérifié par l'essai, ligne 591), bordereau. Je n'ai trouvé dans la livraison aucun identifiant de jeton, texte d'action, contexte ni champ de configuration. La trace d'arrêt, non livrée, peut porter un chemin dans sa cause (P1, P8) : conforme au texte, qui la garde du côté exposé.

## Notice

- Exacte sur la ligne de commande, les entrées, les noms et formats de la livraison et les codes de refus, sauf : (a) la promesse « c'est le module de version 2 qui se porte au bordereau du code » est fausse sous `python -m` (remarque 1) ; (b) la mémoire (remarque 9) ; (c) l'essai à blanc (remarque 4) ; (d) les fichiers de sondes sur une autre branche (point 3 ci-dessus) ; (e) aucun mot sur les motifs privés dans les chemins de sortie (remarque 2) ni sur l'arbre propre (point 4) ; (f) elle se dit alignée sur le brouillon 9 : les cinq remplacements du brouillon 10 sont tenus par le code (table), la notice peut le dire.
- Suffisante pour quelqu'un qui n'a pas écrit le code, une fois ces points ajoutés.

## Conclusion

**Pas encore « conforme au texte, prêt pour la ligne de registre du code ».** Liste fermée des corrections :

1. remarque 1 (BLOQUANTE) : porter et contrôler le module lancé par `python -m`, avec son essai en sous-processus ;
2. remarque 2 (À CORRIGER) : contrôle d'ouverture des chemins de sortie et de cache, écritures hors de la règle des lectures ;
3. remarque 3 (À CORRIGER) : second contrôle de taille qui marque P9 « non tenue » ;
4. remarque 4 (À CORRIGER) : étendre `verifier-entrees` aux contrôles sans carte, et la notice en conséquence ;
5. remarque 5 (À CORRIGER) : ordre strict des lignes par lot, à écrire au texte ou à relâcher dans le code ;
6. remarque 6 et essai sans réglage (À CORRIGER) : artefact sur la reconstruction ; essai de P10 sans modèle ajusté ;
7. notice : remarque 9, fichiers de sondes sur l'autre branche, arbre propre ;
8. mineures 7, 8, 10 à 14 : à corriger ou à déclarer, au choix de l'auteur, sans bloquer.

Le calcul lui-même (couches, positions, biais, précision, agrégations, ordre, sous-échantillon, liste fermée de la livraison) est conforme au texte ; je n'ai trouvé aucune erreur d'un rang.

## Refus d'outil

Aucun.

Fin réelle d'écriture : 2026-11-19T02:32:01Z (`date -u`).
