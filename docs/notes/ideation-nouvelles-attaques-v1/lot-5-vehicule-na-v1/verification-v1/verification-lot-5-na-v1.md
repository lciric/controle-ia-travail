# Vérification du lot 5 (lecteur et contrat des fiches, portier neuf, registres) du véhicule NA-1 — v1

Vérificateur du lot 5 du véhicule NA-1, modèle S. Pièce de travail (classe C). Processeur seul : aucun appel, aucune clé, aucune dépense, aucun relais lancé, aucune écriture dans un dépôt. Données factices ; le registre servi réel n'est pas ouvert. La liste réelle des noms refusés n'a servi qu'à un balayage en mémoire (comptes seuls) ; **aucun nom de cette liste ni aucun identifiant de modèle n'est écrit dans cette pièce**.

## Verdict

**Conforme.** Le lot 5 fait ce que le mandat demande ; les comptes rejoués sont égaux ; le balayage du livrable par la liste réelle ne trouve aucun nom. Une règle à écrire au mandat du lot 6 sur le refus écrit (§ 5), et quelques points à porter à l'additif, dont un risque de faux coffre (§ 4, point 4) à mesurer avant la course. Rien ne bloque.

## 1. Empreintes et rejeu

| pièce | sha256 | état |
|---|---|---|
| table du livrable | `c7e7bd56aa80b5ab2b90d2a172d54cdab3c0943027999040f3fdaf7817865331` | égale à l'annonce ; les 19 fichiers vérifiés OK |
| rapport | `695bdcd9695472a431a9ab05d0913419da17b83a95be71be09af8aa4aaf5f741` | égal |
| orchestrateur | commit `a41b7b50…` | copie neuve, sans `.git` |

Chaîne rejouée : copie neuve ; paquet du lot 2 v5 ; paquet du lot 3 v3 ; paquet du lot 5, chacun par son programme (`--lancer-essais`).

| | annoncé | rejoué |
|---|---|---|
| essais, en tout | 402 (200 + 202) | **402 passés**, 0 sauté |
| mutations du développeur | 74 sur 74 tuées | **74 sur 74 tuées** ; témoin non muté passe ; témoin inerte survit |
| mes mutations (51) | — | 37 tuées, 13 survivent, 1 invalide de mon fait (§ 3) |

## 2. Exigences du mandat, une à une

Lieux dans `paquet/orchestrator/pole/` ; j'ai vérifié que les lignes du rapport sont exactes. Essais dans `paquet/orchestrator/essais/test_na_lot5_v1_*.py`.

| exigence | faite | où | essai qui la tient (échoue sans la garde) |
|---|---|---|---|
| lecteur neuf, ni `preparer`, ni `valider_contenu`, ni `fiches_du_texte` ; syntaxes déclarées | oui | `lecteur_fiches_na_v1.py:241` (`lire_fiches`), `:188`, `:177` | essais du lecteur (37) ; Z5-46 à Z5-51 tuées |
| grammaire par étiquettes ancrées, **sans ordre exigé** | oui | `lecteur_fiches_na_v1.py:56`, `:120`, `:144` | `TestGrammaireParEtiquettesAncrees` ; L5-03 « dans l'ordre » tuée |
| champ en double, onze champs : non reconnue ; jamais complétée ni réparée | oui | `lecteur_fiches_na_v1.py:157-163` | L5-01, L5-02 tuées |
| la lecture rend toujours un objet dès qu'un texte est rendu (§ 2.13) | oui | `lecteur_fiches_na_v1.py:241` | essai « mutation lecture qui rend rien » |
| validateur neuf : type, borne en octets, champ en plus ; aucun caviardage | oui | `contrat_fiche_na_v1.py:94`, `:59` | essais du contrat (18) ; C5-01 à C5-09 (« couper à la borne » comprise) ; Z5-42, Z5-45 tuées |
| arrêt n° 4 : champs fermés à l'octet ; « autre, à nommer » | oui | `contrat_fiche_na_v1.py:120`, `:107` | Z5-43 tuée ; essais du portier |
| champ `case` différent : consigné, compté, classe inchangée | oui | `contrat_fiche_na_v1.py:131` ; `portier_na_v1.py:423`, `:524` | Z5-44 tuée |
| portier neuf ; l'aiguilleur du noyau jamais appelé | oui | `portier_na_v1.py:339` | espion à zéro ; P5-* (22) |
| lecture des seules étiquettes de D3 ; hors liste, absente ou double : illisible | oui | `portier_na_v1.py:160`, `:134` | Z5-09, Z5-10 tuées |
| deux sortes d'appel : « fiche » et « réponse sans fiche » | oui | `portier_na_v1.py:415`, `:456`, `:477` | essais du portier (68) |
| ordre D6 : forme, modèle, hors case ; illisible ou refus : au coffre, compté à part | oui | `portier_na_v1.py:428`, `:438`, `:443`, `:445` | P5 « ordre D6 inversé » ; Z5-01 à Z5-03 tuées |
| refus écrit : fiche « au coffre », classe écrite, comptée ; réponse sans fiche : « réponse illisible », sous-compte | oui | `portier_na_v1.py:382`, `:466` | Z5-08, Z5-15, Z5-16 tuées |
| passeports : identifiant et empreinte du texte classé, à la seule fiche « passée » ; exigés (A17) | oui | `portier_na_v1.py:187`, `:227`, `:494`, `:102` | P5 « passeport non exigé » ; Z5-04, Z5-06, Z5-07 tuées |
| journal du portier : sans contenu, ajout seul, scellé | oui | `portier_na_v1.py:329`, `:242`, `:536` | Z5-11 tuée ; **Z5-12, Z5-13 survivent** |
| identifiants réencodés, dans les deux sens (repris du lot 1, non réécrits) | oui | `identifiants_na_v1.py` (module du lot 1) | essais d'identifiants (29), I5-01 à I5-04 |
| registre des tentatives : nom = identifiant, énoncé = `idee` sur une ligne, sans coupe (D5) | oui | `registre_na_v1.py:81`, `:71` | Z5-25 tuée |
| registre servi : une ligne par passée ; **lignes de compte toujours, zéro compris** ; rangées puis permutées (clés 12, 13) | oui | `registre_na_v1.py:137`, `:181`, `:186-193` | R5 « ligne omise à zéro » ; Z5-21, Z5-22, Z5-24, Z5-28 tuées |
| arrêt n° 5 : strictement plus d'un quart ; à la troisième, consigné | oui | `registre_na_v1.py:210`, `:218` | Z5-19, Z5-20 tuées |
| arrêts n° 8, n° 9, n° 19 sur le fichier entier, avant envoi ; aucune ligne retirée ; les arrêts s'ajoutent | oui | `verifier_registre_servi_na_v1.py:137`, `:87` | V5-01 à V5-15 ; Z5-29, Z5-32, Z5-35, Z5-37, Z5-38 tuées |
| aucun identifiant de modèle, aucune clé, aucune recette ; liste réelle non copiée | oui | balayage du livrable : 0 nom en mot entier dans les 16 fichiers balayés | — |

## 3. Mes mutations (51)

Survivantes (14, dont une invalide de mon fait) : aucune ne touche une exigence de la lettre ; à renforcer, non bloquant.

- **Arrêt n° 19** (`verifier_registre_servi_na_v1.py`) : Z5-30 (fin de ligne finale non exigée), Z5-31 (ligne vide admise), Z5-33 (deux lignes de compte pour une case), Z5-34 (classe de compte inconnue), Z5-36 (tentative manquante non vue), Z5-39 (ligne de compte inattendue non vue), Z5-41 (nom non réencodé). Ce sont des défauts que le développeur a ajoutés à la lettre (qui nomme : champ de plus, deux lignes pour une tentative, énoncé trop long, marque de code, étape numérotée) ; ils n'ont pas d'essai.
- **Registre** : Z5-23 (nom différent de l'identifiant ou redit), Z5-26 (case servie deux fois).
- **Portier** : Z5-12 (scellement sans relire l'intégrité), Z5-13 (scellement double) ; Z5-17 (texte non chaîne) est redondant avec le lot 3.
- Z5-27 est équivalente (l'ordre par octets UTF-8 et par points de code est le même) ; Z5-40 est invalide, texte cherché erroné de ma part.

## 4. Les points que la lettre ne fixe pas (§ 6 du rapport)

Aucun n'est tranché à tort. **À l'additif** : 1 (syntaxes déclarées : objet structuré et étiquettes ancrées ; les noms s'écrivent à l'octet, par exemple `ce_que_le_moniteur_suppose`) ; 2 (séparation des morceaux d'une réponse) ; 3 (prose finale ajoutée à la valeur de la dernière étiquette) ; 4 (voir ci-dessous) ; 5 (morceaux non reconnus comptés à part) ; 8 (forme des étiquettes du portier : « ligne ancrée », à fixer avec la consigne de D3) ; 9 (appel non lancé ou non lu) ; 10 (identifiant d'une réponse sans fiche, fourni par le lot 6) ; 12 (empreinte du passeport : les octets de la fiche servie) ; 13 (forme d'une ligne du registre servi) ; 14 (`permuter_comptes`, point ouvert du § 9 de la conception) ; 15 (listes des marques et étiquettes des arrêts n° 9 et n° 19, brouillon à fixer, taux de faux refus à mesurer) ; 21 (bornes en octets et consigne de D3, factices).

Remarques sans conséquence : 6, 7, 11, 16, 17, 18, 19, 20 (la v9 est à six espèces, la conception v5 à cinq : le lot 5 ne lit pas l'espèce).

**Le point 4 mérite une mesure avant la course.** J'ai vérifié par sonde : dans la grammaire d'étiquettes, une ligne de valeur qui commence par un mot en minuscules suivi de deux-points et d'un blanc (« exemple : … », « note : … ») est lue comme une étiquette ; si ce nom n'est pas l'un des douze champs, c'est un champ en plus et la fiche va au coffre. Avec une capitale, ou avec les deux-points au milieu de la ligne, rien ne change. Le choix est conservateur (« jamais lue fausse »), mais il peut produire de faux « au coffre », et **l'arrêt n° 5 arrête la génération suivante dès que plus d'un quart des fiches y vont**. Le taux se lira à la sonde et à l'essai à blanc ; à noter à l'additif, avec le seuil d'alerte.

## 5. Interface pour le lot 6 (et 7, 10 a)

- **Construction** : `PortierNA(consigne=rq.charger_piece(…), declaration=pt.declaration_de(…), bornes=ct.bornes_de(…), appeler=f, dossier_sortie=…, nom_journal=…, generation=g)`. Cohérent avec la requête du lot 3 v3 et avec le lot 4 : `appeler(requete, lire)` reçoit la `RequeteAssemblee` du lot 3, que la surcharge d'`appel` du lot 4 journalise telle quelle (`consigne` est cet objet) et lit par la fonction `lire` du portier. La fiche servie a l'empreinte du texte classé (contrôlée dans `classer_fiche`).
- **Passeport du portier**, lu par la surcharge de `juger` du lot 6 avant tout appel de juge : `portier.exiger_passeport(issue.identifiant, issue.contenu)` rend le passeport de **ce** portier, ou lève `ArretSansPasseportNA` (A17) ; le passeport de l'aiguilleur du noyau n'est lu par personne ; puis `rq.assembler_juge(consigne_juge, issue.contenu, ident.reencoder_jeton_noyau(jeton_juge, "F", 5), issue.identifiant_case, g)`. Cohérent.
- **Refus écrit : règle à écrire au mandat du lot 6.** Le lot 4 rend, pour un rôle arrêté, un dictionnaire (`r` et `lu` à `None`, `refus_ecrit`, `issue_na`) ; le portier du lot 5 attend un `RenduRefusEcrit` lui-même. Sonde : le `RenduRefusEcrit` seul donne « au coffre », cause « au coffre par refus du portier » ; le dictionnaire du lot 4 passé tel quel donne « au coffre », cause « réponse du portier non lue », et **0** au compte « au coffre par refus du portier ». Il faut donc que la fonction `appeler` du lot 6 rende `a["refus_ecrit"]` quand il est présent, **avant** de lire `a["r"]` ou `a["lu"]`. Plus sûr : une v2 du lot 5 qui lit `refus_ecrit` avant `lu` dans `_appeler_modele` (une ligne).
- **Registre servi** : `fabriquer_registre_servi(lignes, cases_servies, g, permuter_comptes=<additif>, racine=…)`, puis `verifier_registre_servi(…)` (arrêts n° 8, 9, 19), `charger_piece(…)`, `assembler_proposeur(…)`, et `s.sha256`, `s.lignes` sur la ligne de la génération. Cohérent avec la section « registre » du lot 3.
- **Fin de génération** : `portier.comptes()`, `portier.sceller()`, `registre.sceller()`, puis `garde_du_coffre(lire_registre_tentatives(chemin, exiger_sceau=True), g)` : arrêt n° 5 aux générations 1 et 2, consigné à la troisième.
- **Comptes** : ceux du portier (lot 5), du mélange (lot 4) et du journal (lot 3) ne sont pas fusionnés ; c'est au lot 6. Le lot 7 doit lire les journaux avec `exiger_sceau=True`.

## 6. Ce que je n'ai pas fait

Je n'ai pas ouvert le registre servi réel. Je n'ai pas relu le lecteur ligne à ligne : je l'ai éprouvé par ses 37 essais, mes mutations et une sonde sur les valeurs multi-lignes. Je n'ai pas mesuré le taux de faux coffre : il demande des réponses de modèles, hors mandat.

— vérificateur du lot 5 du véhicule NA-1, modèle S
