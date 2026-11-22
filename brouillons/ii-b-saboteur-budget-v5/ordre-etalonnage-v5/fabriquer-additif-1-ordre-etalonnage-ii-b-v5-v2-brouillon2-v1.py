"""Fabrique l'additif 1 à l'ordre v2 de l'étalonnage, brouillon 2, depuis le brouillon 1, par remplacements à ancre comptée.
Changements : (1) la vérification du correctif 0013 remplie (note conforme, b8c8db48…) ; (2) la borne du seuil corrigée d'après
l'observation m1 du vérificateur : 17 USD n'est pas un plafond mais la dépense tenue à la coupure 12 (devis scellé § 3, 12 + 0,92
+ 3,84 = 16,76) ; à 16 la dépense tenue devient 20,76 USD, au-dessus des 17 de l'étape 1, sous 55 et 60 ; (3) la commande de
relance de la surveillance écrite selon la procédure sûre du vérificateur, essai à blanc compris. Rien d'autre.
Usage : python3 fabriquer-additif-1-ordre-etalonnage-ii-b-v5-v2-brouillon2-v1.py (depuis ce dossier)."""
import hashlib, pathlib

ICI = pathlib.Path(__file__).resolve().parent
SOURCE = ICI / "additif-1-ordre-etalonnage-ii-b-v5-v2-brouillon1.md"
CIBLE = ICI / "additif-1-ordre-etalonnage-ii-b-v5-v2-brouillon2.md"
t = SOURCE.read_text(encoding="utf-8")
assert hashlib.sha256(t.encode("utf-8")).hexdigest().startswith("f546a6ea"), "brouillon 1 inattendu"

C13 = "brouillons/ii-b-saboteur-budget-v5/code-v5/correctif-0013/"
EN_TETE = (
    "\n> **Brouillon 2, fabriqué par programme** depuis le brouillon 1 (`additif-1-ordre-etalonnage-ii-b-v5-v2-brouillon1.md`, "
    "`f546a6ea8894feb460563e19d919897d67b798b637bb2b79eaa0c00a55fb60cb`, intact, R12) par "
    "`fabriquer-additif-1-ordre-etalonnage-ii-b-v5-v2-brouillon2-v1.py`. Ce qui change : la vérification du correctif 0013 "
    "remplie ; la borne du seuil corrigée (17 USD n'est pas un plafond, voir § 1) ; la commande de relance écrite (§ 3).\n"
)
BORNES_A = ("- **Bornes** : 16 USD reste sous le plafond de 17 USD de l'étape 1 au devis scellé (`devis-ii-b-v5-scelle-v1.md`, "
            "cb881522…) et sous la ligne `GO-2026-11-21-70` (plafond 60, coupure de la ligne à 55, qui reste et prime).")
BORNES_N = (
    "- **Bornes** : le devis scellé (`devis-ii-b-v5-scelle-v1.md`, cb881522…, § 3) dit que 17 USD « n'est pas une seconde "
    "ligne » : c'est la dépense tenue par les gardes à la coupure de 12 si la course ne part pas (12 + consignation au plus 0,92 "
    "+ 48 h de stockage à l'arrêt 3,84 = 16,76). **À 16, la dépense tenue devient 16 + 0,92 + 3,84 = 20,76 USD : au-dessus des "
    "17 USD de l'étape 1 au devis**, toujours sous la coupure de la ligne `GO-2026-11-21-70` (55, qui reste et prime) et sous "
    "son plafond (60). La dépense de la tentative 1 (environ 1,3 USD) et celle de la première course n'y entrent pas. "
    "**Ce dépassement de l'étape 1 est à faire accepter par Lazar avec le seuil.** La documentation de "
    "`session_v5.py` au correctif 0013 dit encore « sous le plafond de 17 USD de l'étape 1 » : phrase de commentaire inexacte, "
    "sans effet sur le code ; elle n'est pas corrigée ici, pour ne pas changer l'arbre vérifié (ce paragraphe prime).")
FIN_A = ("la dépense réelle à la coupure serait d'environ 16,1 à 16,4 USD, sous le plafond de 17 USD de l'étape 1. À cela "
         "s'ajoute, comme avant, le forfait de téléchargement (1,04 USD au plus), hors du compte de la règle. **Ce point est à "
         "faire accepter par Lazar avec le seuil.**")
FIN_N = ("la dépense réelle à la coupure serait d'environ 16,1 à 16,4 USD, puis la consignation et le stockage à l'arrêt comme "
         "ci-dessus (« Bornes »). À cela s'ajoute, comme avant, le forfait de téléchargement (1,04 USD au plus), hors du compte "
         "de la règle. **Ce point est à faire accepter par Lazar avec le seuil.**")
VERIF_A = "Vérification : `<<VERIFICATION_CORRECTIF_0013>>`."
VERIF_N = (
    f"Vérification par un Opus 5.5 neuf : `{C13}note-verification-0013-cl1-v1.md` "
    "(`b8c8db48d33fd559cdde65dc6a6529430c2154f31f6a7e202a0106de03b3d6b3`), **conforme** ; seule observation de fond, m1, "
    "portée ci-dessus (« Bornes »). Commit du correctif : `530240333699579912fb8610dc12ace3e85e221a` (sur 887561b7). "
    "Appliqué sur le commit de lancement `43d6d0673edd5055917f536e5310ea99c15ab75e`, il s'applique sans conflit et rend "
    "l'arbre **`d1cc1d75b06a3c5f372ad4c1cf0f184026a23744`** (relevé à nouveau le 22 novembre par `git apply --cached` sur "
    "un index de 43d6d067). Fichiers touchés : `scripts/lancer_iib_v3.sh` (un message), `src/controle_ia/iib/session_v5.py` "
    "(constante et documentation), deux fichiers d'essais."
)
CMD_A = "`<<COMMANDE_RELANCE_SURVEILLANCE>>`"
CMD_N = f"""**Où vit le seuil** : dans le code, côté session exécutante (`$DEPOT/src/controle_ia/iib/session_v5.py`, lu par `python3 -I -B` à chaque relevé). Ni la configuration scellée, ni l'amorce, ni la machine ne changent ; aucun paramètre de sous-commande ne porte le seuil. On ne relance donc **que la surveillance**, sur un `$DEPOT` portant le correctif 0013. La surveillance relit `$DEPOT/src` à chaque relevé, mais le correctif touche aussi le lanceur de session, qu'elle exécute en ce moment : **on ne modifie jamais `$DEPOT` pendant qu'elle tourne** (un relevé pendant l'extraction peut lire un état mêlé, refuser, et arrêter la machine).

Tout se fait **au mot de Lazar seulement, porté par la mère**, et **avant que la dépense comptée n'atteigne 12 USD** (sinon la surveillance v2 coupe d'abord, ce qui est le comportement de l'ordre v2 tel quel). L'interruption de la surveillance dure quelques minutes ; pendant ce temps, la minuterie de la machine (55 USD ou échéance) reste seule garde, comme prévu par l'ordre.

1. **Attendre un relevé « RIEN »** à la dernière ligne de `$D/surveillance.txt` (`tail -n 1 "$D/surveillance.txt"`), où `$D` est le dossier de la session de l'étalonnage en cours. Relever la dépense comptée qu'il dit ; si elle atteint 11 USD, ne rien faire et le dire à la mère.
2. **Arrêter la surveillance par son numéro de processus** (R10), celui relevé à son lancement : `kill <PID>` ; vérifier `kill -0 <PID>` en échec ; consigner l'heure et le numéro. Jamais par motif de ligne de commande. Si un `stop instance` est en cours, ne rien toucher et le dire à la mère.
3. **Porter le correctif dans `$DEPOT`**, à la tête `43d6d0673edd5055917f536e5310ea99c15ab75e` (le vérifier par `git -C "$DEPOT" rev-parse HEAD` et `git -C "$DEPOT" status --porcelain` vide) :
   ```
   P=0013-Organisme-retenu-du-saboteur-budget-code-en-version-.patch
   git -C "$DEPOT" fetch origin claude/iib-reconception-oracle-v1
   git -C "$DEPOT" show FETCH_HEAD:{C13}$P > "$D/$P"
   echo "8538c203b4bc39cf01b5cb4cd987b4688427975456ab254bde06811d0f76e907  $D/$P" | sha256sum -c -
   git -C "$DEPOT" am --keep-cr "$D/$P"
   test "$(git -C "$DEPOT" rev-parse 'HEAD^{{tree}}')" = d1cc1d75b06a3c5f372ad4c1cf0f184026a23744 && echo ARBRE_CONFORME
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
   "${{ENVI[@]}}" bash scripts/lancer_iib_v3.sh surveillance <identifiant> "$D" [FACTURE_USD]
   ```
   Consigner le numéro de processus. Vérifier dans `$D/surveillance.txt` la ligne « règle de coupure de l'étalonnage : phase etalonnage … ; seuil 16 USD … » puis, au relevé suivant, une ligne « RIEN : dépense comptée de l'étalonnage … < 16 USD ».
6. **Compte rendu à la mère** : heures d'arrêt et de relance, deux numéros de processus, dépense comptée au dernier relevé avant l'arrêt, nouvelle tête de `$DEPOT` et son arbre (`d1cc1d75…`), les trois sorties de l'essai à blanc, la première ligne « RIEN … < 16 USD ». Le commit de lancement scellé (43d6d067) reste celui de la machine et de la configuration ; la tête de `$DEPOT` côté session n'est que celle de la surveillance."""

REMPLACEMENTS = [
    ("versement par lot dit selon le code (brouillon 1)", "versement par lot dit selon le code (brouillon 2)", 1),
    (BORNES_A, BORNES_N, 1),
    (FIN_A, FIN_N, 1),
    (VERIF_A, VERIF_N, 1),
    (CMD_A, CMD_N, 1),
]
for ancien, nouveau, n in REMPLACEMENTS:
    assert t.count(ancien) == n, (ancien[:70], t.count(ancien))
    t = t.replace(ancien, nouveau)
ligne1, reste = t.split("\n", 1)
t = ligne1 + "\n" + EN_TETE + reste
assert "<<" not in t and ">>" not in t, "champ non rempli"
CIBLE.open("x", encoding="utf-8").write(t)
print(CIBLE.name, hashlib.sha256(t.encode("utf-8")).hexdigest())
