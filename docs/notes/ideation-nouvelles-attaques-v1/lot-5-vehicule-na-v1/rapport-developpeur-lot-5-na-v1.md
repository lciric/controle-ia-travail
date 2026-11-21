# Rapport du développeur — véhicule NA-1, lot 5 (lecteur et contrat des fiches, portier neuf, identifiants, registres) — v1

- Développeur du lot 5 du véhicule NA-1, modèle O. Je n'ai écrit ni la conception, ni les lots 1 à 4, ni aucun orchestrateur.
- Date (UTC) : 2026-11-21 ; runs finaux sur la base neuve entre 10:18:23Z et 10:28:49Z (`date -u`).
- Mandat : `mandat-developpeur-vehicule-na-lot-5-v1.md`, `f97fda31bf56b3ef29f3dd28b727d07915327462bbf2d9c9f006f58413b4e7d8`, égal à son compagnon, lu en entier.
- Processeur seul : aucun appel, aucune clé, aucune dépense ; aucune écriture dans un dépôt, aucun commit ; données factices seules. Le registre servi réel n'est pas ouvert ; aucune branche de quarantaine ni de matière première ouverte ; la liste réelle des motifs n'est ni copiée ni lue par mon code.
- **Un refus du classifieur au départ** : une commande de liste sur le dossier parent des dossiers des lots (hors de mon dossier et des dossiers des lots 1 à 3). Je me suis arrêté et l'ai rendu ; la mère a accordé la reprise, le refus consigné et sans effet. Aucun autre refus ensuite.
- **Base** : sur la décision de la mère transmise en cours de travail, le code est écrit et éprouvé contre le **lot 2 v5** (`tirage_na_v4`, `garde_motifs_na_v4`, `identifiants_na_v1` inchangé) et le **lot 3 v3** (`requete_na_v3`, `journal_na_v3`), posés par leurs programmes sur une copie neuve de l'orchestrateur (commit `a41b7b50…`, sans `.git`). Une première écriture, contre le lot 2 v3 et le lot 3 v2, est gardée telle quelle dans le sous-dossier `brouillon-contre-lot-2-v3-et-lot-3-v2/` (non livrée ; § 9).

## 1. Verdict

- **Essais du lot 5 : 202 passés, 0 échec, 0 sauté** (lecteur 37, contrat 18, portier 68, registres 50, identifiants 29 ; journal `journal-essais-na-lot-5-v1.txt`).
- **Chaîne entière** sur une copie neuve, lots 2 v5, 3 v3 et 5 posés par leurs programmes (`--lancer-essais`) : **402 passés** (200 des lots 2 v5 et 3 v3, leurs propres comptes ; 202 du lot 5).
- **Mutations : 74 sur 74 tuées** ; le témoin non muté passe ; le témoin inerte survit (journal `journal-mutations-na-lot-5-v1.json`).
- Refus du programme d'application éprouvés : copie nue (« `identifiants_na_v1.py` absent »), seconde application (R12), dépôt de l'orchestrateur comme destination.

## 2. Pièces lues

| pièce | empreinte | état |
|---|---|---|
| conception v5 | `1b7f6822af20417e997b80290f05e7a4d70aa69c3d65f4139b5b3673cd98a863` | égale au compagnon ; lue en entier |
| contrôle de la conception v5 | `4b369004733fb4c55bb75deaeac19c4cc4e5dacaa8604f8082f63096c2956156` | égal au compagnon ; « Conforme » |
| v9 scellée (`origin/main`, tirée par `git show` redirigé) | `864f39a7ecd41a613f8892efbf66607c14da34252d643a4fd40032b5d2b500c2` | égale au compagnon du dépôt ; l. 55 à 125, 144 à 180, 296 à 395 lues |
| relevé du lot 0 | `10ac79ecb0e064f5b5ea80ddb060ae37e303d2d84ff242f653f4cccbd7ff753e` | Q4 et Q6 lues |
| table du lot 2 v5 | `6a5b5400aa9209f32f9cbd5a14116b5ddff929eac3886aec3753643c8282a2ce` | égale au compagnon ; rapport lu |
| table du lot 3 v3 | `1be0ffd48b8ade5f0accd106c9682c0b1e3db36bc208046ef66946598bbbed7f` | égale au compagnon ; rapport lu (§ 6, interface) |
| tables du lot 2 v3 et du lot 3 v2 | `77590698…`, `672f76ac…` | égales ; base de la première écriture |
| code lu dans la copie | `identifiants_na_v1`, `requete_na_v2`/`v3`, `journal_na_v2`, `garde_motifs` (interface), `tirage` (légende, ligne de case, permutation), `noyau_v56.appel` et `juger`, `aiguilleur_v53`, `fiches_v53`, `caviardage` | — |

Non ouvert : le paquet v68 (son manifeste n'a pas été trouvé par chemin complet donné, et le lot 5 n'appelle rien de la v68) ; la manière de la v68 pour les mutations est prise dans les programmes des lots 2 et 3, qui la suivent.

## 3. Exigences et code (fichier : ligne, dans `paquet/orchestrator/pole/`)

| exigence (conception v5, V9) | lieu |
|---|---|
| lecteur neuf, ni `preparer` ni `valider_contenu` ni `fiches_du_texte` ; syntaxes déclarées (§ 2.4, § 5.4) | `lecteur_fiches_na_v1.py:241` (`lire_fiches`), `:188` (morceaux), `:177` (objet structuré) |
| grammaire par étiquettes ancrées, sans ordre exigé (mot 3 ; « dans l'ordre » retiré) | `lecteur_fiches_na_v1.py:56` (motif), `:120` (`_etiquette`), `:144` (douze noms, une fois chacun, ordre libre) |
| un champ en double, onze champs : non reconnue ; jamais complétée ni réparée ; jamais lue fausse | `lecteur_fiches_na_v1.py:157` à `:163` |
| la lecture rend toujours un objet dès qu'un texte est rendu (§ 2.13) | `lecteur_fiches_na_v1.py:241` à fin |
| validateur neuf : type de chaîne, borne en octets, champ en plus ; aucun caviardage (§ 2.4, D13) | `contrat_fiche_na_v1.py:94` (`verifier`), `:59` (bornes, les douze) |
| arrêt n° 4 : comparaison à l'octet aux trois chaînes de la ligne de case ; « autre, à nommer » (V9, l. 75, 110, 375) | `contrat_fiche_na_v1.py:120`, `:107` |
| champ `case` différent : consigné, compté, classe inchangée (mot 2) | `contrat_fiche_na_v1.py:131` ; `portier_na_v1.py:423`, `:524` (comptes) |
| portier, code neuf ; l'aiguilleur du noyau jamais appelé (§ 2.4, 07:51Z) | `portier_na_v1.py:339` (`PortierNA`) |
| lecture des seules étiquettes de D3 ; hors liste, absente ou double : illisible | `portier_na_v1.py:160` (`lire_etiquette`), `:134` (déclaration) |
| deux sortes d'appel : « fiche », « réponse sans fiche » (forme tranchée : `## La réponse`, `{"reponse": texte}`) | `portier_na_v1.py:415`, `:456`, `:477` |
| ordre D6 : forme, modèle, hors case ; illisible ou refus du modèle portier : au coffre, compté à part | `portier_na_v1.py:428` (i), `:438` (ii), `:443` (iii), `:445` (iv) |
| refus écrit : fiche « au coffre », classe écrite, comptée ; réponse sans fiche : « réponse illisible », sous-compte (§ 2.13) | `portier_na_v1.py:382` (`_appeler_modele`), `:466` |
| passeports : identifiant et empreinte du texte classé, à la seule fiche « passée » ; exigés (A17) | `portier_na_v1.py:187`, `:227`, `:494` (`exiger_passeport`), `:102` (`ArretSansPasseportNA`) |
| journal du portier, sans contenu, scellé à la fin de la génération | `portier_na_v1.py:329`, `:242` (ajout seul), `:536` |
| identifiants réencodés, dans les deux sens (§ 5.2) | module du lot 1, `identifiants_na_v1.py` (`38d9860b…`), repris tel quel ; exigé par le portier `portier_na_v1.py:366` |
| registre des tentatives ; nom = identifiant, énoncé = `idee` sur une ligne, sans coupe (D5) | `registre_na_v1.py:81`, `:71` |
| registre servi : une ligne par passée ; lignes de compte toujours, zéro compris (07:21Z, règle 2) ; rangées puis permutées (clés 12, 13) | `registre_na_v1.py:137` (`fabriquer_registre_servi`), `:181` (comptes), `:186` à `:193` |
| arrêt n° 5 : strictement plus d'un quart au coffre ; à la troisième, consigné | `registre_na_v1.py:210` (`garde_du_coffre`), `:218` |
| arrêts n° 8, n° 9, n° 19 sur le fichier entier, avant envoi ; aucune ligne retirée ; les arrêts s'ajoutent | `verifier_registre_servi_na_v1.py:137`, `:87` (`verifier_enonce`, pour le lot 10 a aussi) |

## 4. Essais (lot 5 : 202)

| exigence du mandat | essais (cas sain ; artefact) |
|---|---|
| arrêt n° 4 | une fiche dans sa case passe ; le témoin « hors case » (champs fermés d'une autre case), puis un champ fermé qui diffère d'un octet : « hors case », comptés, sans passeport ; une fiche hors case à champ de plus : au coffre ; hors case et « concret » : au coffre (ordre D6) ; le modèle est appelé avant la comparaison ; un blanc, une casse, une autre forme Unicode : hors case |
| arrêt n° 5 | un quart exactement : la suivante part ; une de plus : `ArretGardeCoffre` aux générations 1 et 2 ; à la troisième : consigné ; seules les fiches de la génération ; fiches hors longueur et refus du portier au dénominateur |
| arrêt n° 8 | registre égal à sa borne : passe ; un octet de moins à la borne : arrêt n° 8 seul ; consigne, registre compris, à sa borne puis un octet au-dessus (`verifier_borne` du lot 3) |
| arrêt n° 9 | registre sans étiquette : passe ; note, rang, verdict de juge, étiquette d'antériorité, coût, tour à tour : arrêt n° 9 ; un coût en chiffres |
| arrêt n° 19 | registre aux seuls champs permis : passe ; un champ de plus (avant et après l'énoncé), deux lignes pour une tentative, un énoncé d'un octet de trop (et à sa borne exacte : passe), une marque de code (cinq formes), une étape numérotée (quatre), une marque de consigne (trois), un énoncé sur deux lignes (et en appel direct : quatre fins de ligne), une classe autre que « passée », une ligne d'une autre forme, un compte non entier, une ligne manquante ; les octets sont inchangés après le refus (aucune ligne retirée) ; le message ne recopie rien |
| classes d'appel | réponse à fiches : « fiches rendues » par programme ; chacune des trois étiquettes à sa classe, jamais l'arrêt n° 1 ; le témoin « réponse vide motivée » et son artefact ; étiquette illisible : « réponse illisible », sous-compte ; morceau non reconnu compté |
| champ `case` | fiche aux douze champs, `case` en tête, reconnue ; la même au validateur du noyau : refusée (témoin du défaut) ; `case` différent : consigné, compté, classe « passée » inchangée ; champ fermé qu'un caviardage changerait : lu tel que rendu |
| « autre, à nommer » | la supposition nommée dans `idee` : passe ; dans le champ fermé : « hors case » |
| hors contrat de longueur | chaque champ à sa borne : suit son chemin ; un octet de trop sur `idee` puis sur `filiation` : au coffre, compté, sans appel, texte inchangé ; compté parmi les fiches rendues |
| lignes de compte à zéro | une case sans fiche : ses deux lignes, à zéro ; comptes à un ; génération 3 sur les générations 1 et 2 seules |
| passeport exigé | passée : rendu ; « concret », illisible, refus écrit, hors case : `ArretSansPasseportNA` ; texte changé après classement ; passeport de l'aiguilleur du noyau ; passeport d'un autre portier |
| portier neuf | étiquette du noyau (`a_corriger`, `niveau_methode`), bloc `{"classe": …}`, hors liste, double, absente : illisible ; l'aiguilleur du noyau jamais appelé (espion à zéro) ; ses requêtes passent la garde d'essai et le journal du lot 3 ; identifiant hexadécimal ou redit refusé |
| gardes héritées, part du portier | trois réponses illisibles de suite et une quatrième : aucun arrêt, chacune classée et comptée ; la lecture rend toujours un objet |
| ce que rend un refus écrit | fiche au coffre, classe écrite, comptée ; réponse sans fiche illisible ; refus écrit d'une autre sorte : refusé ; non lancé, non lu : au coffre ; issue inconnue, lecture d'une autre fonction : refusées ; aucune fiche rendue sans classe |
| journal sans contenu | marqueurs inertes absents du journal scellé ; champs dans la liste fermée ; fichier réécrit d'une autre main : refusé |
| réencodage, deux sens | six et cinq octets : encoder puis décoder ; décoder puis encoder ; bornes ; ordre des octets ; aucune suite hexadécimale ; hors alphabet, mauvaise longueur, entier au-delà de la borne : refusés |
| registre servi | forme déclarée ; permutation par la clé 12 ; comptes permutés ou non, selon ce que dit l'appelant ; case non servie refusée ; passe la vérification et la garde d'essai ; entre dans la requête d'un proposeur de génération 2 |

## 5. Mutations (74, toutes tuées)

`essais/mutations_na_lot5_v1.py`, à la manière des lots 2 et 3 (copie temporaire, remplacements à texte exact, essais nommés). Lecteur 13 (L5-01 à L5-13), contrat 9 (C5-01 à C5-09, dont « couper à la borne »), portier 22 (P5-01 à P5-22, dont « lecture qui rend rien sans étiquette », « ordre D6 inversé », « passeport non exigé »), registre 11 (R5-01 à R5-11, dont « ligne omise à zéro »), vérification 15 (V5-01 à V5-15, dont « retrait silencieux » et « les arrêts ne s'ajoutent plus »), identifiants 4 (I5-01 « ordre des octets inversé » à I5-04, sur la seule copie temporaire du module du lot 1). Une première passe avait laissé survivre deux mutations (L5-04, V5-13) : les essais ont été renforcés (valeur sur deux lignes portant un autre nom hors tête de ligne ; appel direct de `verifier_enonce`), sans toucher au code ; la passe finale les tue.

## 6. Ce que la lettre ne fixe pas (remarques ; rien n'est tranché ici)

1. **Forme des syntaxes déclarées.** Objet JSON (bloc clôturé ou nu ; enveloppe `fiches`) et étiquettes ancrées (parures listées au module). Les noms doivent être écrits à l'octet (`ce_que_le_moniteur_suppose`, non « ce que le moniteur suppose »). À fixer à l'additif.
2. **Morceaux.** Plusieurs fiches dans une réponse se séparent par une règle, un titre qui n'est pas une étiquette ou un bloc. Deux fiches sans séparateur font un nom en double : refusées, jamais lues fausses.
3. **Prose finale.** Les lignes qui suivent la dernière étiquette s'ajoutent à sa valeur (rien n'est retiré ni deviné). Les fins de ligne `\r\n` et `\r` sont lues `\n`.
4. **Champ en plus dans la grammaire.** Toute ligne « nom en minuscules ASCII, deux-points, blanc » est une étiquette ; si le nom n'est pas l'un des douze, c'est un champ en plus, donc au coffre. Une ligne de suite comme `voir : …` envoie la fiche au coffre : c'est conservateur (jamais lue fausse), mais un faux coffre possible ; le taux est à lire au faux fournisseur.
5. **Morceaux non reconnus.** Ils ne sont pas des fiches rendues et sont comptés à part. Une réponse avec une fiche reconnue est « fiches rendues », même si d'autres morceaux ne le sont pas.
6. **Valeur qui n'est pas une chaîne** (objet JSON) : rangée avec les fiches hors contrat, au coffre par la forme, cause à part.
7. **Ordre des causes de forme** : champ en plus, puis type, puis longueur. Toutes sont comptées.
8. **Étiquettes du portier.** La forme est une brouillon « ligne ancrée » (`étiquette : <texte>`, à l'octet, une seule ligne). La consigne de D3 et sa déclaration fixeront la forme réelle.
9. **Appel du portier non lancé ou réponse non lue** (statut autre que « ok »). La lettre ne fixe que le refus écrit et l'illisible. Pour une fiche : au coffre, sous sa cause. Pour une réponse sans fiche : « réponse illisible », sous-compte « étiquette du portier illisible », sous sa cause.
10. **Identifiant d'une réponse sans fiche** : un mot réencodé de dix-huit lettres, que le lot 6 fournit (par exemple les six octets d'un jeton du noyau). La lettre n'en dit rien.
11. **Texte vide** : un texte rendu de zéro octet va à l'appel « réponse sans fiche ».
12. **Empreinte du passeport** : celle des octets de la fiche servie au portier (forme du noyau, déclarée).
13. **Forme d'une ligne du registre servi** (brouillon) : énoncé en chaîne JSON, pour qu'aucun champ en plus ne s'y cache. À fixer à l'additif.
14. **Lignes de compte permutées** (§ 9, point 3, ouvert) : un argument sans défaut, `permuter_comptes`, que l'additif doit fixer.
15. **Listes des marques et étiquettes** des arrêts n° 9 et n° 19 : un brouillon (motifs au module), à fixer à l'additif ; leur taux de faux refus est à mesurer.
16. **Contrôle croisé** des noms et des cases attendus : facultatif dans la vérification ; je recommande que le lot 6 le passe toujours.
17. **Garde du coffre à zéro fiche rendue** : aucune part, aucun arrêt.
18. **« `identifiants` » au mandat** : aucun module neuf n'est écrit. Le module du lot 1 est repris tel quel (mot de la mère : « repris, jamais réécrit ») ; le lot 5 en porte les essais dans les deux sens et les mutations.
19. **Le constat mineur du lot 3** (`FileNotFoundError` sur un journal supprimé) ne touche pas mes fichiers : mon ajout seul convertit l'erreur de lecture en `AjoutSeulRefuse`.
20. **Composition.** La v9 est à six espèces ; la conception v5 est à cinq. Le lot 5 ne lit pas l'espèce ; sans objet ici.
21. **Brouillon d'essai.** Les bornes (300 octets par champ, 1 200 pour `idee`), la consigne et la déclaration des essais sont factices, déclarées comme telles.

## 7. Interface pour les lots 6, 7 et 10 a

**Lot 6 (génération, surcharge de `juger`).**
- Construire, pour chaque génération : `pt.PortierNA(consigne=rq.charger_piece("consigne du portier", octets, empreinte), declaration=pt.declaration_de(forme=…, cle=…, fiche={…}, reponse_sans_fiche={…}, statut=…), bornes=ct.bornes_de({…douze…}, statut), appeler=f, dossier_sortie=…, nom_journal="….jsonl", generation=g)`.
- `appeler(requete, lire)` reçoit la `RequeteAssemblee` du lot 3 (sorte `portier_fiche` ou `portier_reponse_sans_fiche`) et la lecture du portier. Il la passe à `self.appel(…, consigne=<chaîne de la requête>, plafond_role=…, lire=lire)`, donc à la surcharge du lot 4, qui journalise **cet objet**. Il rend l'une de trois choses :
  - `None` : non lancé ;
  - un `journal_na_v3.RenduRefusEcrit` : refus écrit, de la même sorte que la requête ;
  - le dictionnaire du noyau, avec la clé `lu`.

  Un `ArretMotifInterdit` ou un arrêt de course levé dedans traverse le portier.
- Pour chaque réponse de proposeur où un texte est rendu : `portier.traiter_reponse(texte, case=<rq.CaseServie>, identifiant_reponse=<mot de 18 lettres>, identifiant_fiche=lambda rang: <mot de 18 lettres>)` → `IssueReponse`, qui porte `classe_appel`, `sous_compte`, `fiches` et `non_reconnus`. L'identifiant d'une fiche s'obtient par `ident.reencoder_jeton_noyau(jeton, prefixe, 6)`. Sans texte rendu (statut d'erreur), le lot 6 compte lui-même, hors du portier.
- Chaque `IssueFiche` va au registre : `rg.RegistreTentatives(dossier, "….jsonl").ajouter_fiche(issue)`.
- À la fin de la génération : `portier.comptes()` (ligne de la génération), `portier.sceller()`, `registre.sceller()`, puis `rg.garde_du_coffre(rg.lire_registre_tentatives(chemin, exiger_sceau=True), g)`. Elle lève `ArretGardeCoffre` (n° 5) aux générations 1 et 2 ; à la troisième, elle rend un `ConstatCoffre` avec `consigne=True`.
- **Passeport du portier** (surcharge de `juger`), avant tout appel d'un juge : `p = portier.exiger_passeport(issue.identifiant, issue.contenu)`.
  - Sans passeport de **ce** portier, ou si le texte a changé, l'appel lève `pt.ArretSansPasseportNA` (A17, arrêt nommé de la course ; numéro à l'additif).
  - Le passeport de l'aiguilleur du noyau n'est pas lu.
  - Puis `rq.assembler_juge(consigne_juge, issue.contenu, ident.reencoder_jeton_noyau(jeton_juge, "F", 5), issue.identifiant_case, g)`.
- **Registre servi**, au départ des générations 2 et 3 :
  1. `s = rg.fabriquer_registre_servi(lignes des générations précédentes, {g': [identifiants des cases servies]}, g, permuter_comptes=<additif>, racine=tn.RACINE_ECRITE)` ;
  2. `vr.verifier_registre_servi(s.octets, borne_registre_octets=…, borne_enonce_octets=…, noms_attendus=…, cases_attendues=…)`, qui lève `RegistreServiNonConforme` (`.numeros`, `.defauts`) ;
  3. `rq.charger_piece("registre servi", s.octets, s.sha256)`, puis `rq.assembler_proposeur(…)` ;
  4. sur la ligne de la génération : `s.sha256`, `s.lignes`, et `requete.registre` (section servie ou omise).

**Lot 7 (mesures, export).**
- Le registre des tentatives se lit par `rg.lire_registre_tentatives(chemin, exiger_sceau=True)`. Ses champs : `identifiant`, `generation`, `case`, `classe`, et pour une fiche passée les trois champs fermés, `nom` et `enonce`.
- Le journal du portier se lit par `pt.relire_ajout_seul(chemin, exiger_sceau=True)`. Ses champs : `identifiant`, `sorte`, `generation`, `case`, `empreinte`, `classe`, `cause`, `case_differe`, `appel_au_modele`.
- M3 : toutes les lignes de la génération au registre, hors longueur et refus du portier compris.
- M6 : `classes_appel` et le sous-compte `étiquette du portier illisible` des `comptes()`.
- M7 : le registre ne porte que l'identifiant de la case ; le premier axe se lit au tirage scellé.
- M1 : les noms du registre servi sont les identifiants des fiches passées.

**Lot 10 a (colonne « matière première »).**
- `vr.verifier_enonce(enonce, borne_octets)` rend la liste des défauts `(numéro, cause)`, vide si l'énoncé est conforme. C'est la forme de l'arrêt n° 19, à laquelle s'ajoutent les étiquettes de l'arrêt n° 9 ; le lot 10 a peut filtrer par numéro.
- Les identifiants de ligne s'encodent par `identifiants_na_v1`.

## 8. Écarts de procédure, dits

1. **Une commande composée** (`cd … && pytest …`) a été passée une fois, en début d'écriture, contre la règle « une commande simple par appel ». Elle n'a fait que jouer des essais. Toutes les autres sont simples.
2. **La base de la première écriture** a été copiée dans `copie-orchestrateur`, puis déplacée sous `base/orchestrator`. Les programmes d'application exigent le dossier parent d'`orchestrator`. La base neuve est faite directement sous cette forme (`base-v2/orchestrator`, `application-v2/orchestrator`).
3. **Un journal d'essais aux chemins complets** a été écarté dans le dossier de brouillon (`journal-essais-chemins-complets-base-neuve-ecarte.txt`). Le journal livré est écrit par `jouer_essais_lot_5_v1.py`, en noms relatifs.

## 9. Livré

Dossier `dev-vehicule-na-lot-5/` du bloc-notes de la session ; le chemin complet est donné au message de remise, et n'est écrit dans aucun fichier livré. Un compagnon `.sha256` par fichier ; table `table-empreintes-dossier-na-lot-5-v1.txt`.

| fichier | sha256 |
|---|---|
| `paquet/orchestrator/pole/lecteur_fiches_na_v1.py` | `75dcad76c39f863a2857d2ec74970e244747ee8a67db5c6cbb5260750b26a1bb` |
| `paquet/orchestrator/pole/contrat_fiche_na_v1.py` | `4d023526e3a45aadcb58da3425e1e5950b7b659b307208bed6f03eaba4858c5c` |
| `paquet/orchestrator/pole/portier_na_v1.py` | `702a50cfd33e57a26ef1ef909d8c973e84a93c3f44071d6483f7e5c92c8f5a04` |
| `paquet/orchestrator/pole/registre_na_v1.py` | `a2a359852e23bc2728d9ad32a525137c1282cffa02dab27388833a2f62451744` |
| `paquet/orchestrator/pole/verifier_registre_servi_na_v1.py` | `90d6bcea8a1360f157258c5665f1ba977b4bc50f64b23bae537eaac48f6fa626` |
| `paquet/orchestrator/essais/aides_na_lot5_v1.py` | `76d1c0f7a2e68690cf487e399a1d239b3c8fee015f0799a28f96fccd799f3b27` |
| `paquet/orchestrator/essais/test_na_lot5_v1_lecteur.py` | `fb40dc987fbb0687f91101ea1334acd0f93d55a5b65daa5cfcc5091fac584904` |
| `paquet/orchestrator/essais/test_na_lot5_v1_contrat.py` | `530fd2ff8b72927e27241d9b37492c80405e50ca56b6f442d256701c805bd91a` |
| `paquet/orchestrator/essais/test_na_lot5_v1_portier.py` | `1b0402d0f02793812407c269cc8dec01e9d110008e8d384e0bcfdf879a710159` |
| `paquet/orchestrator/essais/test_na_lot5_v1_registre.py` | `4fe322eb8835b4bad33221390c620658f77b6efc84b61814c730448cf105fc1a` |
| `paquet/orchestrator/essais/test_na_lot5_v1_identifiants.py` | `dccf860fa1ad6de214e1a8f2e703904682394b7f2a9127ba8f57a3b7f96140c1` |
| `paquet/orchestrator/essais/mutations_na_lot5_v1.py` | `2062bd5c37788ea44127e9308d1d6d3823970165567c9e76a252ea6ce0ec4b80` |
| le manifeste, le programme d'application, le programme d'essais, le programme des compagnons, les deux journaux, ce rapport | voir la table |

Hors de la table, dans le dossier : les copies `base-v2/` et `application-v2/` (lots 2 v5, 3 v3 et 5 posés ; ce ne sont pas des dépôts ; elles ne contiennent aucune copie de la liste réelle) ; `v9.md` et son compagnon du dépôt (tirés de `origin/main`) ; le sous-dossier `brouillon-contre-lot-2-v3-et-lot-3-v2/` (première écriture, non livrée, gardée pour être récupérable).

— développeur du lot 5 du véhicule NA-1, modèle O
