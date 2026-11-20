# Contre-lecture — partie servie dérivée de la question v5 : rejeu et lecture entière — v1

Pièce de travail (classe C), 2026-11-20, sur le mandat `mandat-contre-lecteur-partie-servie-v5-v1.md` (`be118b0121dc4cd6e7d4c7145f9634a10e7f84fec76475cc033400e8de2d9336`, vérifié contre son compagnon). Processeur seul : aucun appel, aucune dépense, aucune écriture dans le dépôt. Aucune méthode d'attaque.

## 0. Verdict

**Conforme, à sceller**, gabarit `4cd360baea1076ec2b19b2c7ba85675e739bc3104c709d4fd57c0769975b1cf1` tel quel (2 957 octets, 21 lignes). Rejeu égal à l'octet ; extraction indépendante égale à l'octet ; empreintes des cinq zones égales au journal ; emplacement unique ; relevé interne à 0. L'écart de la colonne est exact et suit la lettre de la règle retenue : je recommande de le garder (confiance haute). Les remarques 2 à 4 n'appellent aucune correction du gabarit ; elles appellent trois consignes au mandat du véhicule et à la sonde de refus (§ 5). Aucun refus de permission, de classifieur ni de garde.

## 1. Pièces vérifiées

- Dossier P : les sept pièces du mandat, chacune `OK` contre son compagnon ; les préfixes du mandat (`cef4e600`, `d22e6f55`, `4cd360ba…`, `944188dc`, `28c51483`, `a12f03e7`, `e7592c56`) égaux aux compagnons.
- Après `fetch`, `origin/main` est à `81950c45f` (le dériveur lisait `486cae2d4`). Tirées par `git show … >` dans `sources/` : la question v5, `eaf5db8a558547aa8f5df45008a34eebf4cb7a163e12ca400176401de6f5ce0f` (74 lignes, 15 246 octets), égale à son compagnon sur `origin/main` ; la note de périmètre v3, `dd6fea0e176b019c46386d0d000d059085036d2b20a82fe59c26549b41380580`, égale à son compagnon, lue en entier (§ 7 et § 8, point 7 en particulier).

## 2. Rejeu

Copie du programme dans mon dossier ; `diff` contre l'original : deux lignes seulement, les constantes `SOURCE` (ma copie `sources/question-v5.md`) et `DOSSIER` (mon dossier). Joué par `env -C /home/user/controle-ia-travail python3 -I -B …/contre-lecture-partie-servie-v5/deriver_partie_servie_v5_v1.py`, Python 3.13.18, sans message.

- Gabarit : `4cd360ba…1cf1`, `cmp` muet contre le gabarit rendu : **égal à l'octet**.
- Journal : `diff` contre le journal rendu : trois lignes, toutes des chemins (`commande`, `sortie.chemin`, `source.copie_lue`) ; empreintes des zones, de l'emplacement et de la sortie **égales**.

## 3. Vérification indépendante

Programme `verifier_partie_servie_v5_v1.py`, écrit sans reprendre le code du dériveur (lignes par `splitlines`, retrait de colonne par découpage des cellules, non par position de la troisième barre), sortie `verification-partie-servie-v5-v1.json`, `conforme : true`, aucun échec.

- Extraction des lignes 42–51, 55, 56–60 (deux colonnes), 61, 64–66, emplacement inséré après 51 : **égale à l'octet** au gabarit rendu. Empreintes extraites et servies des cinq zones égales au journal.
- Chaque ligne du gabarit renvoie à une ligne de la v5 (exacte), à l'emplacement, ou, pour les lignes 13 à 17, à la ligne 56 à 60 dont elle est le début exact. Aucune ligne de 1 à 41, 52 à 54, 62, 63, 67 à 74 n'entre (les lignes vides servies sont des octets de la v5).
- Accolades dans la v5 : 0. Dans le gabarit : `{{CASE}}` une fois, 2 ouvrantes, 2 fermantes, sur une ligne propre (ligne 11). Ni retour chariot, ni caractère de contrôle, ni caractère invisible, ni espace insécable.

## 4. L'écart de la colonne

**Exact.** Cellule retirée de l'en-tête : « source » ; du séparateur : des tirets seuls ; 256 octets retirés ; pour chaque ligne 56 à 60, la ligne servie est le début exact de la ligne source, et ce qui manque est exactement la troisième cellule et sa barre. Les deux colonnes gardées sont égales à l'octet. La table servie reste une table bien formée (`| axe | valeurs |`, `|---|---|`).

**Contre la règle.** La règle retenue (note v3, § 7, recommandation reprise au § 8, point 7 (b)) veut la légende « sans la colonne « source » », et la note ajoute : « Le journal de dérivation de l'option (b) porte exactement ce retrait, rejouable par un autre modèle. » Le retrait n'est donc pas un écart à la règle : c'en est la lettre. Il n'est un écart qu'à la décision de la mère « sans transformation », et le mandat du dériveur prévoyait ce cas même (« retrait d'une colonne nommée, par programme »). L'opération est la plus petite possible, écrite, gardée (arrêt si une ligne n'a pas quatre barres ou si la cellule d'en-tête retirée n'est pas « source ») et rejouée ici par deux voies.

**Contre le repli** (lignes 55 à 60 retirées, sans transformation : `15bf001e4683daeccde923f7fe34bfe4581b061e702d725b978734a6f0d837b3`, 2 477 octets, 15 lignes, calculé par mon programme). Le repli est l'option (c) du point 7, non retenue ; le choisir serait un écart au point 7 (b) de GO-2026-11-20-46 pour éviter un écart à une décision de forme. Il coûte aussi des fiches « hors case » (note § 7).

**Recommandation : garder le retrait, sceller `4cd360ba…`. Confiance : haute.**

## 5. Lecture entière par le sens

**Rien d'interne.** Mon relevé, 41 motifs (ceux du mandat du dériveur, plus : la fonction de directeur, la mère, règle `Rn` sans tiret, dépôt, `scripts/` et `src/`, extensions de fichier, chaîne hexadécimale dès 8 caractères, signe de section, provenance, tirage, génération, ordre de course, préenregistrement, devis, décision, hypothèses et consignes du programme, version `vN`, noms de maisons et de modèles), chacun éprouvé sur un témoin qui mord : **0**. Même relevé sur la requête assemblée pour chacune des cases de la légende, sous une forme d'essai de la ligne de case (« case servie : valeur / valeur / valeur ») : pire total **0**. Le texte servi ne nomme ni personne, ni pièce, ni identifiant, ni le compte des cases, ni la famille de cases mise de côté.

**Remarque « rouages nommés »** (remarque 1 du rapport, que le mandat appelle remarque 2). Compte informatif : portier 2, coffre 1, « hors case » 1, « registre servi » 1, « glisse vers le concret » 1, `piece_produite` (« publique ou scellée ») 1. Jugement : **à garder, et à signaler à la mère pour information, sans correction**. (a) Ce ne sont pas des « renvois internes » au sens de la règle (règle, décision, GO, chemin) : ils nomment des rôles de la course, ni une pièce ni une personne. (b) Ils portent le contrat : champs fermés égaux à la case sous peine de refus, aucun champ « comment faire ». (c) Les couper serait une seconde transformation d'un texte scellé, donc une v6 et un nœud. Ce que la mère doit savoir : ces mots partent chez les maisons dont on appelle les modèles (la note v3, § 4, point 2, le dit déjà du sceau) ; « coffre » et « glisse vers le concret » peuvent peser sur un classifieur de sûreté, donc **la sonde de refus et les témoins plantés se jouent sur la requête assemblée** (gabarit plus ligne de case), non sur le § 4 seul. `filiation` et « registre servi » n'ont d'objet qu'aux générations 2 et 3 (à la première, la réponse attendue est « aucune ») ; `piece_produite` n'a de sens que pour la course. Bruit possible, sans fuite ; contenu de la v5, hors de la dérivation.

**Remarque 2 du rapport** (légende sans titre, emplacement sans libellé). D'accord : la dérivation n'écrit aucun mot. Le § 4 servi nomme les trois axes dans le même ordre et les mêmes termes que l'en-tête de colonne « axe », ce qui suffit à lire la table. Un libellé éventuel vient du véhicule et passe la garde.

**Remarque 3** (triplet). D'accord, et je la renforce : le champ `case` attend un « identifiant servi » et les trois champs fermés doivent être « égaux à ceux de la case servie » ; un identifiant seul rendrait chaque fiche invérifiable ou « hors case ». La ligne de case doit donc porter **l'identifiant et les trois valeurs, écrites à l'octet comme dans la légende** (le portier compare à ces chaînes). L'identifiant ne doit laisser déduire ni le compte des cases, ni l'ordre du tirage, ni la famille mise de côté (pas de rang numéroté sur un total), ni nom de fichier, ni graine, ni chaîne hexadécimale de 8 caractères et plus (la garde la refuserait). À porter au mandat du véhicule. Confiance : haute.

**Remarque 4** (ligne 66). **Dans la liste des champs** : la règle nomme cette liste « le contrat de sortie », et la ligne 66 en est la clause de fermeture (aucun champ de plus, refus par le portier) ; elle double, côté contrat, le « N'écris aucun procédé » du § 4. La retirer relâcherait la garde « niveau de l'idée ». Garder 64–66. Confiance : haute. (Que l'avis sur la forme nomme ces deux alinéas, je le tiens du rapport : cet avis n'est pas dans ma liste.)

## 6. Points que la mère tranche

1. **L'écart de la colonne** : garder le retrait (recommandé, confiance haute) ou le repli `15bf001e…` (option (c), non retenue par GO-2026-11-20-46).
2. **Rouages nommés** : garder sans toucher (recommandé) ; en prendre acte pour la sonde de refus et les témoins, joués sur la requête assemblée.
3. **Ligne de case** : identifiant neutre plus les trois valeurs à l'octet, sous les contraintes du § 5, au mandat du véhicule ; la garde de motifs court sur la requête assemblée.
4. **Ligne 66** : servie (recommandé).

## 7. Observations hors de la dérivation (information)

- La v5 servie à la case « autre, à nommer » : le champ fermé `ce_que_le_moniteur_suppose` doit être égal à « autre, à nommer », et aucun champ ne reçoit la supposition nommée, sinon `idee`. Contenu de la v5 ; à voir par qui écrit le portier.
- Le titre et le statut de la v5 disent encore « à sceller », « non scellée » (rapport, remarque 6) ; son empreinte est celle du compagnon sur `origin/main`. Lignes non servies : sans effet sur le gabarit.
- Écart de numérotation dans mon mandat : la « remarque 2 » qu'il décrit est la remarque 1 du rapport ; j'ai jugé les deux (§ 5).
- Le relevé du dériveur ne prend les chaînes hexadécimales qu'à 16 caractères ; le mien, dès 8 : 0 aussi.

## 8. Fichiers (mon dossier, chacun avec son compagnon)

- `contre-lecture-partie-servie-v5-v1.md` (cette pièce)
- `verifier_partie_servie_v5_v1.py` et sa sortie `verification-partie-servie-v5-v1.json`
- Rejeu : `deriver_partie_servie_v5_v1.py` (copie, deux constantes changées), `partie-servie-question-v5-v1.md`, `journal-derivation-partie-servie-v5-v1.json`
- `sources/` : `question-v5.md`, `note-perimetre-v3.md`, et leurs compagnons tirés de `origin/main`

— contre-lecteur neuf, modèle O
