# Rapport — dérivation de la partie servie de la question v5 (course « nouvelles attaques ») — v1

Pièce de travail (classe C), 2026-11-20, sur le mandat `mandat-derivation-partie-servie-v5-v1.md` (`cef4e600a90b96cebc26856ba46bcf3acca0d68267ad005599e55e7f327296a4`, vérifiée contre son compagnon). Processeur seul : aucun appel, aucune dépense, aucune écriture dans le dépôt. Aucune méthode d'attaque ; aucun mot du texte récrit.

## 0. Verdict

Le gabarit est écrit : 21 lignes, **2 957 octets**, empreinte `4cd360baea1076ec2b19b2c7ba85675e739bc3104c709d4fd57c0769975b1cf1`. Deux jeux du programme, sorties égales à l'octet (gabarit et journal). Relevé des motifs : 0 sur 25 motifs, chaque motif éprouvé sur un témoin positif. **Un écart à « sans transformation », à trancher par la mère** : le retrait de la colonne « source » de la table des axes, par programme (§ 3). Aucun refus de permission, de classifieur ni de garde.

## 1. Pièces lues, empreintes recalculées

- Question v5, tirée de `origin/main` après `fetch` (commit de tête `486cae2d4`) : `eaf5db8a558547aa8f5df45008a34eebf4cb7a163e12ca400176401de6f5ce0f`, 74 lignes, 15 246 octets, lue en entier. Elle n'est pas dans l'arbre de travail local : le programme lit la copie tirée par `git show`, dont il vérifie l'empreinte.
- Note de périmètre v3 : `dd6fea0e176b019c46386d0d000d059085036d2b20a82fe59c26549b41380580`, § 7 et § 8, point 7.
- Avis sur la forme : `e052b7a932b5c30aef6c43c063f39ef17dda34ab4620bd2e1323de34760d960f`.
- Registre des accords, lignes GO-2026-11-20-44 et -46.
- **Non lu** : le compagnon `avis-partie-a-servir-v2.md`. Il n'existe pas sur `origin/main` au chemin que donne la note (même dossier que la note) ; je ne l'ai pas cherché ailleurs (aucune commande de liste).

## 2. Zones choisies, par la règle du point 7 (b)

Lignes de la question v5, bornes comprises, mises bout à bout dans cet ordre.

| pièce | lignes de la v5 | octets servis | pourquoi |
|---|---|---|---|
| question servie | 42 à 51 | 1 590 | « le § 4 (texte de la v5) » : la citation entière, chevrons gardés, et la ligne vide qui la suit (sans elle, la ligne suivante se lirait comme la suite de la citation) |
| emplacement de case | (inséré) | 9 | « la seule case tirée du proposeur » |
| ligne vide | 55 | 1 | séparation, octet de la source |
| légende des axes | 56 à 60 | 479 (735 extraits) | « les noms des trois axes et la liste des valeurs de chaque axe sans la colonne "source" » : seule zone transformée |
| ligne vide | 61 | 1 | séparation, octet de la source |
| champs d'une fiche | 64 à 66 | 877 | « la liste des champs d'une fiche (§ 5, le contrat de sortie) » : les deux alinéas que l'avis sur la forme nomme (§ 1) |

L'empreinte de chaque zone, avant et après opération, est au journal.

## 3. Le seul écart à « sans transformation »

La table des axes (lignes 56 à 60) porte trois colonnes ; la règle en veut deux. Elle n'est donc pas extractible à l'octet. Plus petite opération écrite et rejouable : **chaque ligne de la zone est gardée jusqu'à sa troisième barre verticale comprise, puis le saut de ligne**. Le programme s'arrête si une ligne n'a pas exactement quatre barres, ou si ce qui est retiré de la première ligne n'est pas exactement la cellule « source ». Les deux colonnes gardées sont égales à l'octet à celles de la source. 256 octets retirés. Aucune autre zone n'est touchée.

Si la mère refuse cet écart, le repli sans aucune transformation est le « repli plus étroit » de la note (§ 7) : les mêmes zones sans les lignes 55 à 60, soit la question, la case et les champs.

## 4. Ce qui n'est pas servi

- L'en-tête (lignes 1 à 10) et le § 1 : chemins, empreintes, accords.
- Les § 2, § 3, § 6 et § 7 : écrits pour la mère, le portier et les lecteurs.
- Le titre du § 4 (ligne 40) et celui du § 5 (ligne 52).
- La ligne 54, qui ouvre le § 5 : elle dit que les valeurs « viennent de pièces du dépôt », un renvoi interne. La légende part donc sans phrase d'introduction (remarque 2).
- La colonne « source » de la table.
- La ligne 62 : le compte des cases, le tirage, la famille de cases mise de côté, le renvoi à l'ordre de course.

## 5. L'emplacement de case

Une ligne propre, `{{CASE}}`, ligne 11 du gabarit, entre la question et la légende des axes : la question vient de dire « Une case t'est servie », et dans la source les cases s'ouvrent au même endroit (entre le § 4 et la table). Pourquoi il ne peut pas apparaître ailleurs : la question v5 entière ne contient **aucune accolade** (le programme le vérifie sur la source et s'arrête sinon), les seuls octets que le programme ajoute sont ceux de cette ligne, et il vérifie avant d'écrire que le gabarit porte une seule fois `{{CASE}}`, deux accolades ouvrantes et deux fermantes en tout, sur une ligne à elle. Le véhicule peut donc remplacer la ligne entière sans risque de toucher le texte, et refuser de partir si le compte n'est pas 1 avant, 0 après.

## 6. Relevé des motifs

Programme `relever_motifs_partie_servie_v5_v1.py`, sortie `releve-motifs-partie-servie-v5-v1.json` : 25 motifs, **0 occurrence**, 25 témoins positifs qui mordent. Motifs : prénom et nom du directeur (jamais écrits dans le relevé), identifiant de session, arobase, R- ou N- suivis de chiffres, identifiant d'accord, nom du compte distant, github, nom du dépôt, chemins `docs/`, `prereg/`, `registres/`, `donnees/`, chaîne hexadécimale de 16 caractères et plus, fichier des consignes permanentes, noms de clés, « famille tenue à l'écart », « tenue à l'écart », « à l'écart », « source », compte des cases (120, un produit, un nombre suivi de « cases »), accolades hors de l'emplacement. Lecture à casse repliée, accents retirés, apostrophes unifiées, sauf mention. Le relevé porte sur le gabarit ; la garde sur la requête assemblée reste à la charge du véhicule.

## 7. Remarques, pour la mère et le contre-lecteur

1. **Ce que le relevé ne voit pas : le sens.** La zone des champs, servie à l'octet comme la règle le demande, nomme « le portier », « le coffre », la classe « hors case » et « le registre servi » : aucun motif, mais des rouages de la course dits aux proposeurs. La règle retenue sert ce contrat ; je ne retire rien. À lire en connaissance de cause par le contre-lecteur.
2. **La légende part sans titre ni phrase d'introduction**, et l'emplacement sans libellé. Je n'écris aucun mot. Si un libellé est voulu (« Ta case : »), il vient du texte que le véhicule met à la place de l'emplacement, et il passe alors par la garde.
3. **Ce que le véhicule met à la place.** Les champs fermés d'une fiche doivent être « égaux à ceux de la case servie » : le proposeur a besoin des trois valeurs de sa case, pas d'un seul rang. Un identifiant neutre sous forme de triplet (les trois valeurs, écrites comme dans la légende) y suffit ; ni nom de fichier, ni graine. Le choix de la forme est au mandat du véhicule.
4. **Le second alinéa des champs** (ligne 66, « Aucun champ "comment faire" ») est servi : il fait partie du contrat de sortie. S'il est jugé hors de « la liste des champs », la zone se réduit à la seule ligne 64, sans transformation.
5. **Source du programme.** Le programme lit une copie tirée de `origin/main` dans le dossier `derivation-partie-servie-v5-sources/`, à côté du mien ; l'empreinte fait foi. Le contre-lecteur qui rejoue tire sa propre copie au même chemin, ou change la seule constante `SOURCE`.
6. **Titre de la v5.** Son titre et sa ligne de statut disent encore « à sceller » et « non scellée » ; son empreinte est bien celle que le mandat donne pour la v5 scellée. Sans effet sur le gabarit : ces lignes ne sont pas servies.
7. **Taille pour le devis et la sonde** : 2 957 octets pour le gabarit, emplacement compris (9 octets, à remplacer par le texte de la case).

## 8. Fichiers rendus (même dossier, chacun avec son compagnon)

- `deriver_partie_servie_v5_v1.py`
- `partie-servie-question-v5-v1.md`
- `journal-derivation-partie-servie-v5-v1.json`
- `relever_motifs_partie_servie_v5_v1.py`
- `releve-motifs-partie-servie-v5-v1.json`
- `rapport-derivation-partie-servie-v5-v1.md`

Commande de la dérivation, jouée deux fois : `env -C /home/user/controle-ia-travail python3 -I -B /tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/derivation-partie-servie-v5/deriver_partie_servie_v5_v1.py` ; Python 3.13.18.

— dériveur neuf, modèle F
