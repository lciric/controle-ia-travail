# Additif 1 à l'ordre de l'étalonnage, version 2 — seuil de la coupure propre relevé à 16 USD ; versement par lot dit selon le code (brouillon 2)

> **Brouillon 2, fabriqué par programme** depuis le brouillon 1 (`additif-1-ordre-etalonnage-ii-b-v5-v2-brouillon1.md`, `f546a6ea8894feb460563e19d919897d67b798b637bb2b79eaa0c00a55fb60cb`, intact, R12) par `fabriquer-additif-1-ordre-etalonnage-ii-b-v5-v2-brouillon2-v1.py`. Ce qui change : la vérification du correctif 0013 remplie ; la borne du seuil corrigée (17 USD n'est pas un plafond, voir § 1) ; la commande de relance écrite (§ 3).

Écrit le 2026-11-22 par la session de reconception. Il complète l'ordre v2 scellé par la mère (brouillon 3 : `ordre-etalonnage-ii-b-v5-v2-brouillon3.md`, `3ec3a60523bbf45c0f345c91d5bdf8e20e9bb220b39a78efa93ea7c57420cc6f`) sans le réécrire, et prime sur les passages qu'il nomme. **Il ne s'applique qu'au mot de Lazar** (le relèvement d'un seuil accordé est un nœud), porté par la mère ; tant que ce mot manque, l'ordre v2 vaut tel quel.

## 1. Le seuil de la coupure propre : 12 → 16 USD
- **Cause** : l'étalonnage en cours tourne 5 à 7 fois plus lentement que le devis, à cause de l'hôte et non du code (lecture du code à 43d6d067 : `brouillons/ii-b-saboteur-budget-v5/code-v5/contre-lecture-cl1/note-lecture-code-versement-coupure-rythme-v1.md`). La projection est de 10 à 12 heures. Coupé à 12 USD, l'étalonnage ne serait pas exploitable : le fichier des sorties d'oracle n'est écrit qu'à la fin, et l'issue serait « non calculable ».
- **Bornes** : le devis scellé (`devis-ii-b-v5-scelle-v1.md`, cb881522…, § 3) dit que 17 USD « n'est pas une seconde ligne » : c'est la dépense tenue par les gardes à la coupure de 12 si la course ne part pas (12 + consignation au plus 0,92 + 48 h de stockage à l'arrêt 3,84 = 16,76). **À 16, la dépense tenue devient 16 + 0,92 + 3,84 = 20,76 USD : au-dessus des 17 USD de l'étape 1 au devis**, toujours sous la coupure de la ligne `GO-2026-11-21-70` (55, qui reste et prime) et sous son plafond (60). La dépense de la tentative 1 (environ 1,3 USD) et celle de la première course n'y entrent pas. **Ce dépassement de l'étape 1 est à faire accepter par Lazar avec le seuil.** La documentation de `session_v5.py` au correctif 0013 dit encore « sous le plafond de 17 USD de l'étape 1 » : phrase de commentaire inexacte, sans effet sur le code ; elle n'est pas corrigée ici, pour ne pas changer l'arbre vérifié (ce paragraphe prime).
- **Où vit le seuil** : c'est une constante du code, `COUPURE_ETALONNAGE_USD` dans `src/controle_ia/iib/session_v5.py`, que la surveillance lit côté session exécutante, jamais sur la machine. La configuration scellée ne le porte pas : elle ne change pas.
- **Correctif 0013** : `brouillons/ii-b-saboteur-budget-v5/code-v5/correctif-0013/0013-…patch` (8538c203…). Il ne change que la constante, ses textes et les essais de la règle, avec les mêmes formes ; 275 essais, inchangés. Vérification par un Opus 5.5 neuf : `brouillons/ii-b-saboteur-budget-v5/code-v5/correctif-0013/note-verification-0013-cl1-v1.md` (`b8c8db48d33fd559cdde65dc6a6529430c2154f31f6a7e202a0106de03b3d6b3`), **conforme** ; seule observation de fond, m1, portée ci-dessus (« Bornes »). Commit du correctif : `530240333699579912fb8610dc12ace3e85e221a` (sur 887561b7). Appliqué sur le commit de lancement `43d6d0673edd5055917f536e5310ea99c15ab75e`, il s'applique sans conflit et rend l'arbre **`d1cc1d75b06a3c5f372ad4c1cf0f184026a23744`** (relevé à nouveau le 22 novembre par `git apply --cached` sur un index de 43d6d067). Fichiers touchés : `scripts/lancer_iib_v3.sh` (un message), `src/controle_ia/iib/session_v5.py` (constante et documentation), deux fichiers d'essais.
- **Passages de l'ordre v2 visés** : partout où l'ordre dit « 12 USD » pour la coupure propre de l'étalonnage (ligne d'accord, § 3 « Coupure propre », § 4 étape 6, § 5 étape 3, § 5 compte rendu, § 6 Arrêts, § 6 Dépense), lire « 16 USD », à partir de la relance de la surveillance sous ce correctif. L'en-tête de la version 2, qui décrit la tentative 1, reste tel quel. L'écart déclaré de dépense à la coupure (0,1 à 0,4 USD au-delà du seuil) vaut désormais au-delà de 16 USD : la dépense réelle à la coupure serait d'environ 16,1 à 16,4 USD, puis la consignation et le stockage à l'arrêt comme ci-dessus (« Bornes »). À cela s'ajoute, comme avant, le forfait de téléchargement (1,04 USD au plus), hors du compte de la règle. **Ce point est à faire accepter par Lazar avec le seuil.**

## 2. Versement par lot : la phrase vraie
Les passages « écrits, scellés et poussés lot par lot » (§ 3, « Versement par lot »), « sorties scellées et poussées » (§ 5 étape 4) et « scellés et poussés » (§ 7) se lisent ainsi, d'après le code à 43d6d067 :
- chaque lot est écrit et scellé **sur le disque de la machine** ;
- l'amorce ne **pousse** qu'au départ, à la fin normale, sur une sortie en erreur du lanceur, par la minuterie (55 USD ou échéance), et à un second démarrage ;
- à la coupure propre, rien n'est poussé : les lots restent sur le disque de la machine arrêtée. Leur rapatriement demande de redémarrer la machine (chemin « run interrompu » de l'amorce, qui pousse puis demande la destruction), **sur le mot de la mère**.

Corriger la poussée par lot dans le code est remis à la course, avec la consignation du repli du cache.

## 3. Commande de relance, pour l'exécutante, au mot de Lazar seulement
**Où vit le seuil** : dans le code, côté session exécutante (`$DEPOT/src/controle_ia/iib/session_v5.py`, lu par `python3 -I -B` à chaque relevé). Ni la configuration scellée, ni l'amorce, ni la machine ne changent ; aucun paramètre de sous-commande ne porte le seuil. On ne relance donc **que la surveillance**, sur un `$DEPOT` portant le correctif 0013. La surveillance relit `$DEPOT/src` à chaque relevé, mais le correctif touche aussi le lanceur de session, qu'elle exécute en ce moment : **on ne modifie jamais `$DEPOT` pendant qu'elle tourne** (un relevé pendant l'extraction peut lire un état mêlé, refuser, et arrêter la machine).

Tout se fait **au mot de Lazar seulement, porté par la mère**, et **avant que la dépense comptée n'atteigne 12 USD** (sinon la surveillance v2 coupe d'abord, ce qui est le comportement de l'ordre v2 tel quel). L'interruption de la surveillance dure quelques minutes ; pendant ce temps, la minuterie de la machine (55 USD ou échéance) reste seule garde, comme prévu par l'ordre.

1. **Attendre un relevé « RIEN »** à la dernière ligne de `$D/surveillance.txt` (`tail -n 1 "$D/surveillance.txt"`), où `$D` est le dossier de la session de l'étalonnage en cours. Relever la dépense comptée qu'il dit ; si elle atteint 11 USD, ne rien faire et le dire à la mère.
2. **Arrêter la surveillance par son numéro de processus** (R10), celui relevé à son lancement : `kill <PID>` ; vérifier `kill -0 <PID>` en échec ; consigner l'heure et le numéro. Jamais par motif de ligne de commande. Si un `stop instance` est en cours, ne rien toucher et le dire à la mère.
3. **Porter le correctif dans `$DEPOT`**, à la tête `43d6d0673edd5055917f536e5310ea99c15ab75e` (le vérifier par `git -C "$DEPOT" rev-parse HEAD` et `git -C "$DEPOT" status --porcelain` vide) :
   ```
   P=0013-Organisme-retenu-du-saboteur-budget-code-en-version-.patch
   git -C "$DEPOT" fetch origin claude/iib-reconception-oracle-v1
   git -C "$DEPOT" show FETCH_HEAD:brouillons/ii-b-saboteur-budget-v5/code-v5/correctif-0013/$P > "$D/$P"
   echo "8538c203b4bc39cf01b5cb4cd987b4688427975456ab254bde06811d0f76e907  $D/$P" | sha256sum -c -
   git -C "$DEPOT" am --keep-cr "$D/$P"
   test "$(git -C "$DEPOT" rev-parse 'HEAD^{tree}')" = d1cc1d75b06a3c5f372ad4c1cf0f184026a23744 && echo ARBRE_CONFORME
   ```
   Tout écart (empreinte, conflit, arbre) : `git -C "$DEPOT" am --abort` s'il le faut, relancer la surveillance **telle qu'avant** (étape 5, sur 43d6d067 intact) et le dire à la mère ; aucun repli.
4. **Essai à blanc de la règle** sur `$DEPOT` (cas sain, artefact, phase illisible ; R5), avec un fichier de progrès vide (la dépense se compte alors depuis la création) et un prix de 1 USD/h :
   ```
   SESSION="import sys; sys.path.insert(0, '$DEPOT/src'); from controle_ia.iib import session_v5; sys.exit(session_v5.main(sys.argv[1:]))"
   V="$D/essai-blanc-coupure-16-progres-vide.txt"; : > "$V"
   python3 -I -B -c "$SESSION" coupure-etalonnage etalonnage "$V" 1000057564 1 0 1000000000   # attendu : RIEN … 15.99 USD < 16 USD
   python3 -I -B -c "$SESSION" coupure-etalonnage etalonnage "$V" 1000057600 1 0 1000000000   # attendu : ARRET … 16.00 USD ≥ 16 USD
   python3 -I -B -c "$SESSION" coupure-etalonnage inconnue   "$V" 1000057600 1 0 1000000000   # attendu : REFUS (code 1)
   ```
   Ces trois sorties ont été obtenues à l'identique le 22 novembre par la session de reconception sur le code du correctif 0013. Toute autre sortie : revenir à 43d6d067 (`git -C "$DEPOT" reset --keep 43d6d0673edd5055917f536e5310ea99c15ab75e`), relancer comme avant, le dire à la mère.
5. **Relancer la surveillance à l'identique**, en tâche de fond, avec le même environnement `ENVI`, le même identifiant, le même dossier et, s'il y en avait un, le même quatrième argument (et la même valeur d'`INTERVALLE` s'il était posé), depuis `$DEPOT` :
   ```
   "${ENVI[@]}" bash scripts/lancer_iib_v3.sh surveillance <identifiant> "$D" [FACTURE_USD]
   ```
   Consigner le numéro de processus. Vérifier dans `$D/surveillance.txt` la ligne « règle de coupure de l'étalonnage : phase etalonnage … ; seuil 16 USD … » puis, au relevé suivant, une ligne « RIEN : dépense comptée de l'étalonnage … < 16 USD ».
6. **Compte rendu à la mère** : heures d'arrêt et de relance, deux numéros de processus, dépense comptée au dernier relevé avant l'arrêt, nouvelle tête de `$DEPOT` et son arbre (`d1cc1d75…`), les trois sorties de l'essai à blanc, la première ligne « RIEN … < 16 USD ». Le commit de lancement scellé (43d6d067) reste celui de la machine et de la configuration ; la tête de `$DEPOT` côté session n'est que celle de la surveillance.
