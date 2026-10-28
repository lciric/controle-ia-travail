# Rapport de contre-lecture — préenregistrement de l'expérience 1 du pôle (juge v1) — cl1

- Contre-lecteur : sous-agent neuf (modèle Fable 5.1), règle R2 ; je n'ai écrit ni le texte ni le code relus.
- Date (UTC) : 2026-10-27, rapport écrit à partir de 10:15 (heure lue sur `date -u`).
- Dossier relu : `contre-lecture-experience-1-juge-cl1/` ; les 43 empreintes de `EMPREINTES-dossier-contre-lecture.txt`
  vérifiées « OK » avant et après mes exécutions (aucun fichier fourni modifié).

## Verdict : **scellable après corrections**

Aucun défaut bloquant. L'argument de validité tient, le code fait ce que le texte dit (lignes, rôles, juges, mondes,
lois, seuils, lecture en deux parties), les contrôles fatals du socle sont tenus par la théorie et les artefacts
requis ont des dents. Quatre constats majeurs (CJ1-01 à CJ1-04) doivent être corrigés avant le scellement : le texte
scellé ne porte pas lui-même les empreintes du code qu'il fait exécuter ; la lecture mécanique `juger_v1` prononce
« adopté » sur un rapport vide ou incomplet ; deux déclencheurs de l'audit de symétrie (R4) ne peuvent pas être
évalués à partir du rapport produit. Les autres constats sont mineurs ou des remarques.

- Empreinte SHA-256 du texte relu (`preenregistrement-experience-1-juge-v1.md`) :
  `1af7df8c6f696896ca009adca7532911f0e3eff9bf60fd72c464f8a3c4926bcf`
- Empreinte de la note de conception relue : `560f4a4cd985f28f2a9fcb838644c2dab62c81d983a5d255e4fe84eb07f1a217` (conforme au texte).

## Ce que j'ai vérifié et trouvé juste (en bref)

1. **R1, huit sections** : « Hypothèse », « Prédiction chiffrée et signe attendu », « Métrique », « Seuil », « Plan
   d'analyse », « Critères de lecture gelés », « Liste d'arrêt », « Contre-lecture » sont là ; les prédictions sont
   chiffrées et signées, les seuils fixés (α = 0,05 ; puissance 0,90 ; T9 : log W max ≤ 10⁻⁹), la lecture est une
   table mécanique ; la liste d'arrêt est exploitable.
2. **Texte contre code** : 70 lignes, exactement la partition annoncée (socle : 18 fatales, 6 artefacts, 1 puissance
   décisive, 29 descriptives ; filles : 10, 2, 1, 3), vérifiée sur un essai à 20 répétitions (liste en annexe A). Les
   trois juges (`controles_pari_v1.py` l. 43-50), les six structures (l. 51-64 et 86-126 : dérive linéaire de v0,
   rupture à n/2, sinusoïde de période n/3, marche des logits d'écart 0,15, blocs de 20, auto-excité fenêtre 10 et
   lissage 0,1), les deux lois aveugles, K = 3, dimension 2, 200 tirages, 250 instances dont 50 de calibrage, δ₀ = 0,01,
   α = 0,05 : conformes. Les paramètres décisifs (α, tirages, δ₀, part de calibrage) ne sont pas exposés à la ligne de
   commande (`experience_juge_v1.py` l. 14-24) : bien.
3. **Lecture `juger_v1`** (`controles_pari_v1.py` l. 536-592) : la règle codée est équivalente à la table du texte
   (l. 119-129), partie par partie et globalement (« adopté » ssi les deux parties le sont) ; `partie_de` range les 70
   noms produits comme le texte le dit (vérifié nom par nom). Le critère T9 (`passe` = taux ≤ α et log W max ≤ 10⁻⁹,
   l. 371) est bien celui de la section « Métrique ».
4. **Argument de validité** : sous le nul « issues indépendantes des traits », la suite des issues dans l'ordre du plan
   est une permutation uniforme de la suite dans le temps, donc échangeable, quelle que soit la structure temporelle ;
   l'urne (`selection_pari.py` l. 276-287) vaut le maximum, sur les lois échangeables, de la probabilité du préfixe
   (essai exhaustif n ≤ 6, `test_juge_v1.py` l. 54-63), et domine donc la loi vraie conditionnelle ; W_t est majorée
   par un rapport de vraisemblance à la loi vraie, martingale d'espérance 1 ; Ville borne la promotion par α. Pour les
   filles, le conditionnement sur les 50 issues de calibrage conserve l'échangeabilité du reste et l'urne est calculée
   sur la partie d'évaluation seule : l'argument tient aussi. Vérifications numériques : la composition par position du
   plan est plate sous 300 ordres (0,453 ; 0,451 ; attendu 0,450, monde à dérive) ; la loi « composition » exacte donne
   log W max = −2,4·10⁻¹² sur 200 ordres (monde à rupture) ; le gain de cette loi sur la marginale ajustée vaut 5,477
   nats pour la composition (80, 60, 60) du calendrier déterministe, comme le texte (≈ 5,47) et la note (≈ 5,5).
5. **Dents des contrôles et des artefacts** : l'oracle « calendrier » sous v0 est promu (13/20 ; 29/50 sur T1b-fille
   v0) ; v1 sans urne cède à la loi « composition » (20/20, 5,477 nats constants) ; l'ordre d'évaluation permuté cède
   (20/20, 212 nats) ; 𝓛 réduite à l'uniforme 47/50 ; dénominateurs à part 9/20 et en ligne 18/20 ; filles sans parents
   dans le nul 15/50 et 30/50. Une loi qui utilise les traits (softmax tirée) sous un monde nul à dérive n'est jamais
   promue par v1 (0/50 sur trois structures, log W max 1,9). Sans l'ordre secret, l'urne seule ne suffit pas (oracle
   promu 30/30 sous calendrier déterministe et sinusoïde) : les deux pièces du juge v1 sont nécessaires, comme la note
   l'annonce.
6. **R3 et essais de fumée** : les essais (graine 777) et l'exploration à 200 répétitions sont déclarés avec leurs
   chiffres et leur chemin ; les deux changements (huitième tricheur, lecture en deux parties) sont déclarés avec leur
   motif ; aucun seuil, monde, loi ou juge des lignes existantes n'a changé (comparaison v0/v2 : `controles_pari.py`
   identique, `selection_pari.py` n'ajoute que l'urne, les trois lois et le plan d'exécution). Le huitième tricheur est
   un contrôle négatif attendu > α (il ne vise pas un signe positif). La lecture en deux parties garde l'issue globale de
   la note comme issue principale ; voir CJ1-06 pour ce qu'il faut dire en plus.
7. **Graines, R9, reproductibilité, gardes** : dérivation SHA-256 documentée (écart à R9 déjà écrit pour v0, repris au
   manifeste) ; une graine de 128 bits passe par la ligne de commande, la dérivation et le manifeste (essai B) ; deux
   exécutions identiques (graine 4242, 20 répétitions) donnent des rapports identiques hors horodatage et durée. Les
   gardes de l'expérience (graines refusées, < 1 000 répétitions, familles partielles, dossier non vide, graine absente)
   sont essayées sur cas sains et artefacts (`test_juge_v1.py` l. 268-276 et 329-354) et je les ai rejouées ; le
   manifeste est écrit avant tout calcul ; rien n'est écrasé.
8. **Section « Seuil »** : queues binomiales exactes recalculées : 2,96·10⁻⁹ (0,02), 2,4·10⁻⁴ (0,03), 0,049 (0,04),
   0,199 (0,045) — conformes. Borne de Wilson unilatérale à 95 % pour 50/1 000 : 0,0626.
9. **Durée** : 15,7 s pour 20 répétitions de tout, soit environ 13 minutes pour 1 000 (le texte dit 15) ; 105 essais
   passent en 105 s.

## Constats

### CJ1-01 — majeur — le texte scellé ne porte pas les empreintes du code qu'il exécute
- Endroit : texte l. 5-8 (« l'empreinte est donnée au message n° 103 »), l. 16 (LISEZMOI v2 cité sans empreinte),
  l. 42 (« empreinte dans le fichier d'empreintes ») ; R1, R6.
- Ce qui ne va pas : le fichier `EMPREINTES-orchestrateur-pole-v2-v1.txt` n'est pas dans le dossier relu et son
  empreinte n'est pas dans le texte ; un renvoi à un numéro de message n'est ni un chemin ni une empreinte. Le lien
  entre le texte scellé et le code exécuté repose sur une pièce hors du texte. Le LISEZMOI v2, dont le texte reprend
  les chiffres de fumée (l. 46-49), est cité sans empreinte.
- Correction : écrire dans l'en-tête du texte les empreintes des modules exécutés et des essais, telles que je les ai
  vérifiées : `pole/selection_pari.py` `57544dc2315821e8f26e7bedee7496368b092ad1924b829f33781a04921712d9` ;
  `pole/controles_pari_v1.py` `41afa0a0ca72a14b4c4f0255fb37955585ed012370113cc92d0fece69efc6875` ;
  `pole/controles_pari.py` `fabc3d0873e6db639f2578eb00ef0035d7831a3b2a1457ffce1d91aa7a364e1c` (identique à v0) ;
  `pole/experience_juge_v1.py` `b797fe6041f2b291dec1ab15eac21ba483ec6231c91555cb7c3b1f2d8556060a` ;
  `pole/outils.py` `79ccf5cb88351e6e9be5214fa0c4624c7469af65f4e307fe8d147031aebdb379` ;
  `pole/pole.py` `1e9f9a74b4410add955b18cd539414582d04cd892a2f4722d8a167830892a093` ;
  `essais/test_juge_v1.py` `3f5e450dfb4b18bba5151d4e1582be09fbfcb066da03981116ac18f72e5eb9bc` ;
  `LISEZMOI-orchestrateur-pole-v2-v1.md` `dbd2811b2c3510cd8f866e0c74144f8dc3ff3f38f024fb33ca0b15ef6cc5ec46` ; plus
  l'empreinte du fichier `EMPREINTES-orchestrateur-pole-v2-v1.txt` lui-même. Si le code est corrigé (CJ1-02, CJ1-03),
  recalculer ces empreintes avant le scellement et le dire.

### CJ1-02 — majeur — `juger_v1` prononce une issue sur un rapport vide ou incomplet ; la liste des 70 lignes n'existe nulle part
- Endroit : `controles_pari_v1.py` l. 531 (`complet=tout and not essai`), l. 549-563 (`_lecture`), l. 576-592 ; texte
  l. 98-99, l. 114-115, l. 146 (« rapport sans l'une des 70 lignes, ou une ligne à moins de 1 000 répétitions : aucune
  lecture »), l. 138 (« vérifier que chacune a 1 000 répétitions »).
- Ce qui ne va pas : vérifié — `juger_v1({"lignes": []}, 0.05, complet=True)` rend « adopté » (socle et filles
  « adopté ») ; une seule ligne fatale à 7 répétitions rend aussi « adopté ». Le drapeau `complet` ne regarde ni le
  nombre de lignes ni leurs répétitions ; la condition « sinon, un contrôle fatal manquant » n'existe pas. Dans
  l'exécution décisive, les 70 lignes sont toujours produites (toute exception arrête avant l'écriture), donc le
  risque pratique est faible ; mais le texte dit que le rapport « applique mécaniquement les critères » et que le
  sous-agent R13 relit « contre ces critères », alors que le critère « 70 lignes, 1 000 répétitions chacune » n'est codé
  nulle part et que la liste des 70 couples (contrôle, juge) n'est écrite nulle part (ni texte, ni code) : le
  sous-agent devrait la reconstruire à partir du code.
- Correction : (a) ajouter dans `controles_pari_v1.py` une constante `ROSTER_V1` des 70 couples (annexe A) et, dans
  `juger_v1` quand `complet` est vrai, rendre `ISSUE_ESSAI` (ou lever) si l'ensemble des couples présents n'est pas
  exactement le roster ou si une ligne a moins de 1 000 répétitions ; essayer cette garde sur un cas sain et sur un
  artefact (R5) ; (b) mettre l'annexe A dans le texte (ou y renvoyer par empreinte) pour que la lecture R13 ait sa
  liste. Changement de lecture seulement, sans effet sur les lignes.

### CJ1-03 — majeur — le champ « plan_execution » des lignes est copié de la table des juges, pas de l'évaluation : un déclencheur R4 sans dents
- Endroit : `controles_pari_v1.py` l. 151-152 (`_ligne` : `ligne.update(plan_execution=JUGES[juge]["plan_execution"])`),
  l. 161-172 (`_executer` ne consigne pas `ev["plan_execution"]`) ; texte l. 136 (« une ligne du juge v1 ne porte pas
  « ordre_secret » »).
- Ce qui ne va pas : vérifié dans le code — l'étiquette vient de la configuration, jamais du résultat de `evaluer`
  (qui, lui, consigne `plan_execution_de(e)`, `selection_pari.py` l. 537). Le déclencheur « une ligne du juge v1 ne
  porte pas ordre_secret » ne peut donc jamais se produire, quel que soit ce que le juge a réellement fait : il ne
  garde rien. (Même remarque, moindre : `empreinte_ordre` n'est consignée nulle part dans le rapport.)
- Correction : dans `_executer` et `_executer_filles`, lire `ev["plan_execution"]` et lever une exception si elle
  diffère de `JUGES[juge]["plan_execution"]` (le contrôle s'arrête, liste d'arrêt « exception ») ; consigner dans la
  ligne le plan observé et, pour l'ordre secret, le nombre d'empreintes d'ordre distinctes vues sur les répétitions
  (attendu : égal aux répétitions). Reformuler le déclencheur R4 en « le plan observé d'une ligne v1 n'est pas
  ordre_secret, ou ses empreintes d'ordre ne sont pas toutes distinctes ».

### CJ1-04 — majeur — le déclencheur R4 « promotions égales une à une » n'est pas évaluable à partir du rapport
- Endroit : texte l. 136-137 ; `controles_pari_v1.py` l. 148-158 (`_ligne`) et l. 326-337.
- Ce qui ne va pas : chaque ligne du rapport ne contient que des totaux (promotions, médiane et maximum de log W,
  comptes de dominants, comptes par monde) ; aucune trace par répétition. « Égales, une à une » ne peut pas être lu ;
  seul « totaux égaux » l'est. Un déclencheur d'audit qui ne peut pas être évalué est un déclencheur silencieux.
- Correction : soit consigner par ligne une chaîne de 1 000 caractères « 0/1 » (promotion par répétition) ou son
  empreinte SHA-256 et un compte des répétitions où v0 et v1 diffèrent (calculable au moment de `juger_v1` sur les
  lignes appariées) ; soit réécrire le déclencheur en « totaux de promotions égaux sur toutes les lignes de puissance
  appariées (fille neuve, T3 net vrai, puissance avec et sans dérive) et médianes de log W final égales ». Je
  recommande la première forme (coût nul, et elle rend l'appariement vérifiable).

### CJ1-05 — mineur — la garde du plan d'exécution vérifie une déclaration, pas une provenance
- Endroit : `selection_pari.py` l. 474-487 ; docstring l. 26-27 (« l'évaluateur refuse des issues produites sous un
  autre plan ») ; note de conception §2.3 ; LISEZMOI v2 l. 66-67.
- Ce qui ne va pas : vérifié — des issues produites sous l'ordre du noyau 8, auxquelles on recopie l'empreinte d'ordre
  calculée pour le noyau 7, sont acceptées par `evaluer(..., graine_noyau=7)`. La garde refuse un étiquetage faux
  (six artefacts des essais l. 191-211), pas un monde qui aurait ignoré l'ordre. En simulation c'est sans conséquence
  (les tirages sont ceux du code) ; en exécution réelle, seule l'imposition de l'ordre par le noyau (non codée, comme
  le LISEZMOI le dit) protège.
- Correction : une phrase dans le texte, section « Hypothèse » ou « Plan d'analyse » : « la garde du plan ne protège
  que contre un étiquetage non conforme ; ce que l'expérience valide est le juge, pas le dispositif réel qui impose
  l'ordre » ; ajouter ce cas aux essais comme limite documentée (pas comme refus attendu).

### CJ1-06 — mineur — la lecture en deux parties et le tricheur ajouté : acceptables, mais deux choses à dire
- Endroit : texte l. 49-52, l. 61, l. 71-72, l. 121-129 ; LISEZMOI v2 l. 12-17 et l. 53-57 ; `controles_pari_v1.py`
  l. 307-323.
- Ce qui ne va pas : (a) la partition « socle / filles » a été décidée après avoir vu les filles céder à l'essai 1 ;
  elle ne déplace pas le but (l'issue globale reste la règle de la note et la note elle-même isolait la limite (b) des
  filles), mais le texte doit dire que la seule issue positive atteignable est « socle adopté » et qu'elle ne licencie
  que la génération 0, sans recombinaison, tant que le nul des filles n'est pas refait. (b) La variante explorée du
  tricheur « parent et loi aveugle » (q = permutation de (0,45 ; 0,1 ; 0,45), LISEZMOI l. 54) n'est pas celle du code
  final (q tirée de Dirichlet(1, 1, 1), l. 315) ; le texte (l. 48) cite 58/200 et 63/200 sans dire que la loi q a
  changé entre l'exploration et la ligne préenregistrée.
- Correction : une phrase pour (a) ; pour (b), écrire « exploration avec q fixée ; ligne préenregistrée avec q ~
  Dirichlet(1,1,1), vue seulement à l'essai 2 (5/20) ». Les prédictions (0,15 à 0,40) restent défendables : mes essais
  donnent 9/20 et 18/50.

### CJ1-07 — mineur — douze des dix-huit contrôles fatals du socle sont des zéros de construction ; le dire, et chiffrer le déclencheur « tout à zéro »
- Endroit : texte l. 58-60, l. 137-138.
- Ce qui ne va pas : les six lignes « composition » valent 0 par construction (le texte le dit) ; les six lignes
  « calendrier » sous v1 sont pratiquement des zéros aussi : sous l'ordre secret, l'oracle indexé par l'indice du plan
  n'est qu'une loi aveugle au hasard, très éloignée de la marginale (log W max observé entre −1,1 et −0,19 sur 20
  répétitions ; pour le calendrier déterministe, chaque désaccord coûte ≈ 27,6 nats au plancher). Les dents
  statistiques du socle sont donc T1a (3 lignes ; v0 : 18, 14, 3 sur 1 000, et l'urne abaisse ces taux), T6 et T3 net
  faux. Un résultat « 18 lignes à 0/1 000 » est donc probable, pas suspect ; le texte en fait un déclencheur R4 (audit
  léger, défini), ce qui est juste, mais un lecteur pourrait y voir une réserve.
- Correction : écrire que 12 lignes sur 18 sont attendues à exactement ou presque 0, que le déclencheur « tout à zéro »
  a une probabilité notable (je l'estime entre un tiers et la moitié) et que son audit se limite à la vérification des
  répétitions et des log W max finis.

### CJ1-08 — mineur — constantes absentes du texte
- Endroit : texte l. 33-42 ; `controles_pari_v1.py` l. 53-56, l. 290, l. 315-316.
- Ce qui manque : λ = 0,5 (T1b-fille et « parent et loi aveugle »), λ = 0,3 (puissance avec dérive), amplitude 1,5 des
  logits de la sinusoïde, loi de q (Dirichlet(1,1,1)), marginale d'entraînement sur 100 instances (T1b-fille : instants
  tirés au hasard sur l'horizon). Ces valeurs sont dans le rapport produit (`parametres`) mais pas dans le texte scellé.
- Correction : les ajouter à « Hypothèses de travail ».

### CJ1-09 — mineur — déclencheur R4 « l'urne n'est jamais membre dominant… dans les lignes T1a et T1b » : périmètre ambigu, et égalités
- Endroit : texte l. 135-136 ; `controles_pari_v1.py` l. 171 ; `selection_pari.py` l. 364-374.
- Ce qui ne va pas : (a) la ligne `artefact-T1a-bibliotheque-uniforme-seule` est étiquetée juge « v1 » et n'a que
  l'uniforme comme membre ; `T1b-fille` n'a pas de champ `membre_dominant_final` (les lignes de filles n'en ont pas) :
  lu à la lettre, le déclencheur peut partir à tort ou ne pas s'appliquer. (b) Sur une suite constante ou presque,
  l'urne et la marginale ajustée sont égales et le bris d'égalité (`v > meilleure[t]`, strict) donne la marginale ;
  le monde auto-excité produit de telles suites (répétitions 7 et 17 de la graine 4242 : compositions (198, 0, 2) et
  (0, 0, 200)) — d'où « marginale_empirique : 1 » dans l'essai. Le mot « jamais » protège, mais il faut le dire.
- Correction : restreindre le déclencheur aux lignes fatales `T1a-nul-*` et `T1b-<structure>-*` du juge v1, et
  préciser « jamais sur l'ensemble des 1 000 répétitions de la ligne ; une minorité de répétitions à égalité (suites
  quasi constantes) est attendue sous auto_excite ».

### CJ1-10 — mineur — l'appariement v0/v1 se fait par scénario, pas par tirages du monde
- Endroit : texte l. 85, l. 106 ; `controles_pari_v1.py` l. 141-145 ; `selection_pari.py` l. 447.
- Ce qui ne va pas : la graine des tirages frais dérive de l'empreinte de l'engagement, qui diffère entre juges
  (bibliothèque et plan) ; pour les mondes qui tirent (T3, puissances, fille neuve), v0 et v1 voient la même loi et les
  mêmes instances mais des issues différentes. « Mêmes graines de scénario » est exact ; « puissance appariée » est
  à lire comme un appariement partiel.
- Correction : écrire « appariés par scénario (loi, instances) ; tirages du monde distincts » dans « Métrique ».

### CJ1-11 — mineur — T9 n'applique ni la part de calibrage ni la marge 2δ₀ ; une chaîne de critère inexacte
- Endroit : `controles_pari_v1.py` l. 354 (`_geler(..., nul_fille, identifiant="T9")`, sans `part_calibrage` ni
  `delta0`), l. 565 (« T9 : et log W max ≤ 0 ») ; texte l. 80-82.
- Ce qui ne va pas : la section « Métrique » dit « pour une fille, gain moyen ≥ 2δ₀ » ; T9 est une ligne de la partie
  filles jugée sans cette marge et sans calibrage (règle de v0, inchangée, donc acceptable) ; et la chaîne écrite dans
  le rapport dit « ≤ 0 » là où le code et le texte disent 10⁻⁹.
- Correction : préciser dans « Métrique » que T9 garde la règle de v0 (W seule, 200 instances, sans marge) ; corriger
  la chaîne l. 565 en « ≤ 10⁻⁹ ».

### CJ1-12 — mineur — reproductibilité : valable pour la même construction de Python
- Endroit : texte l. 101-105, l. 112 ; `outils.py` l. 146-154.
- Ce qui ne va pas : la dérivation des graines est exacte (SHA-256), mais `gauss`, `gammavariate`, `uniform` passent
  par la bibliothèque mathématique du système ; un autre système peut changer une décimale lointaine et, par un
  arrondi (`round(…, 6)`) ou un seuil `u < cumul`, un tirage. Le manifeste consigne la version de Python et la
  plateforme (bien), pas la bibliothèque C.
- Correction : écrire que la reproductibilité bit à bit est promise sur l'environnement nommé (Python 3.13.17, Linux,
  `/opt/venv-essaim-sim-v1`) et vérifiée par une double exécution ; ailleurs, seules les statistiques sont attendues
  égales aux fluctuations près.

### CJ1-13 — remarque — petits points de protocole
- `verifier_parametres` (l. 408-425) ne borne pas les répétitions par le haut : 1 500 est accepté hors essai ; le
  texte dit 1 000. Ajouter `repetitions == 1000` hors essai, ou l'écrire dans la liste d'arrêt.
- Chaîne du manifeste (`outils.py` l. 153-154) : « numpy.random.SeedSequence non disponible ici » — numpy est visible
  dans l'environnement nommé ; la phrase est héritée de v0 et inexacte ; dire plutôt « non utilisée (bibliothèque
  standard imposée) ».
- La suite d'essais crée `essais/_tmp/` dans le dossier du code (vide après nettoyage) : lancer `sha256sum -c` avant
  `unittest`, ou noter que ce dossier ne fait pas partie des empreintes.
- Le nombre « 105 » de la liste d'arrêt changera si le code est corrigé (CJ1-02, CJ1-03) : mettre le nombre à jour au
  scellement.
- `-B` empêche les fichiers compilés : vérifié (aucun `.pyc`).

### CJ1-14 — remarque — deux prédictions descriptives probablement trop hautes sous v1 (sans effet sur l'issue)
- Texte l. 67-68 : « filles sans parents dans le nul : forme 0,35 à 0,70 » — l'urne alourdit le dénominateur ; mes
  essais donnent 10/20 et 15/50 (0,30). « Enveloppe 0,45 à 0,80 » : 12/20 et 30/50. Le critère d'artefact (> 0,05)
  est loin. À laisser tel quel ou élargir ; une prédiction non tenue ici ne change rien.

### CJ1-15 — remarque — le monde auto-excité est presque absorbant
- `controles_pari_v1.py` l. 117-122 : sur 400 tirages, 1,5 % des suites sont constantes et 22 % ont une catégorie à
  ≥ 190/200 (entropie médiane de la composition 0,49 nat sur 1,10). C'est une structure faible pour éprouver la dérive
  (la note proposait aussi un renforcement de Pólya). À dire dans le texte ; ne pas changer maintenant.

### CJ1-16 — remarque — graines que j'ai utilisées (à déclarer, R-473)
- Expérience en mode essai : 4242 (deux fois), 31337, 2718, 170141183460469231731687303715884204893 ; scripts :
  1234, 777000, 99, 5, 3, 4242 et les entiers 0 à 299 comme graines de noyau. Une graine maîtresse de 128 bits tirée
  au hasard ne les rencontrera pas ; les ajouter à `GRAINES_REFUSEES` ne coûte rien.

### CJ1-17 — remarque — porter les limites de la note dans le texte scellé
- Le texte (l. 22) dit « simulation à vérité connue » ; il devrait reprendre en une ligne la limite (a) de la note
  (si les traits se mesurent au moment de l'exécution, l'heure fuit dans les traits) et le fait que l'imposition de
  l'ordre par le noyau n'est pas codée, pour qu'un « socle adopté » ne soit pas lu comme une validation du dispositif
  réel.

## Ce que j'ai exécuté (tout sous `essais-contre-lecteur/`, graines déclarées ci-dessus ; rien à 1 000 répétitions)

1. `sha256sum -c EMPREINTES-dossier-contre-lecture.txt` : 43 « OK », avant et après mes exécutions.
2. Depuis `orchestrateur-pole-v2/` : `/opt/venv-essaim-sim-v1/bin/python -I -B -m unittest` → « Ran 105 tests in
   105.442s — OK » (`unittest-sortie.txt`). Python 3.13.17 ; `claude_agent_sdk` invisible, numpy visible.
3. Essai A et A2 : `python -I -B pole --experience-juge-v1 --essai --repetitions 20 --graine-maitresse 4242 --sortie
   essai-A-g4242-n20` (puis `essai-A2-g4242-n20`), 15,7 s chacun : rapports identiques hors horodatage et durée ;
   70 lignes, 70 couples uniques ; issue « ESSAI — aucune issue prononcée » ; a cédé : `tricheur-parent_et_loi_aveugle`
   (9/20 sous v1, 7/20 sous v0) ; T1b-fille 0/20 (v1), 3/20 (v0) ; les 18 fatales du socle 0/20 ; les six
   « composition » sous v1 à log W max ≤ 0 ; l'urne dominante dans toutes les lignes fatales du socle sauf une
   répétition d'auto_excite (égalité, CJ1-09) ; artefacts : 13/20, 20/20, 19/20, 18/20, 9/20, 20/20, 10/20, 12/20 ;
   puissances : T3 ε = 0,2 19/20 (v1), fille neuve 20/20 (v1 et v0), T3 ε = 0,05 4/20 (v1) contre 16/20 (v0).
4. Essai B : graine `170141183460469231731687303715884204893`, `--familles T9 --repetitions 5` : accepté ; manifeste
   avec la graine entière ; T9 0/5.
5. Essai C : graine 31337, `--familles T3,T1a --repetitions 50` : T1a 0/50, 0/50, 0/50 (log W max 1,78 ; 0,65 ; 0,34) ;
   artefact uniforme seule 47/50 ; T3 net faux 0/50 et 0/50 ; T3 ε = 0,2 net vrai 48/50 (v1), 49/50 (v0) ; ε = 0,05 :
   10/50 (v1), 46/50 (v0).
6. Essai D : graine 2718, `--familles tricheurs,T1b-fille --repetitions 50` : sept tricheurs de v0 0/50 chacun ;
   « parent et loi aveugle » 18/50 (v1), 23/50 (v0) ; T1b-fille 5/50 (v1), 22/50 (v0) ; fille neuve 49/50 (v1), 50/50
   (v0), perte 0,02 ; artefacts sans parents 15/50 et 30/50 ; T9 non inclus.
7. `verifications_chiffres.py` (queues binomiales, gain de la loi « composition », Wilson, graine 128 bits),
   `verifications_mecanisme.py` (échangeabilité sous 300 ordres, T1b-fille = loi vraie sous l'ordre naturel à 0 près,
   égalité urne/marginale sur suite constante, garde du plan : cas sain, artefact refusé, artefact « empreinte recopiée »
   accepté, loi composition ≤ 0 sur 200 ordres, v1 sans urne à 5,192 nats constants sous rupture),
   `verifications_complements.py` (urne sans ordre secret : 30/30, 14/30, 30/30 ; loi à traits sous dérive : 0/50 × 3 ;
   origine du champ `plan_execution`), et des commandes en ligne pour la vacuité de `juger_v1`, `partie_de`, le monde
   auto-excité (400 tirages), le bris d'égalité (graine 4242, répétitions 7 et 17).
8. Fichiers lus en plus de la liste : `essais/aides.py`, `pole/__init__.py`, `pole/__main__.py`,
   `EMPREINTES-dossier-contre-lecture.txt`, et une recherche de « claude_agent_sdk » dans `pole/` (import paresseux
   dans `adaptateurs.py` l. 94 seulement ; le chemin `--experience-juge-v1` ne l'atteint jamais).

## Annexe A — les 70 couples (contrôle, juge) attendus, avec partie et rôle (tels que produits par le code)

| partie | rôle | contrôle | juge |
|---|---|---|---|
| filles | fatal | `T1b-fille` | v1 |
| filles | fatal | `T9-disjonction-partitionnee` | v1 |
| filles | fatal | `tricheur-adimensionnement` | v1 |
| filles | fatal | `tricheur-copie_renommee` | v1 |
| filles | fatal | `tricheur-enveloppe_aveugle` | v1 |
| filles | fatal | `tricheur-fille_constante` | v1 |
| filles | fatal | `tricheur-forme` | v1 |
| filles | fatal | `tricheur-jargon_rare` | v1 |
| filles | fatal | `tricheur-parent_et_loi_aveugle` | v1 |
| filles | fatal | `tricheur-pari_couvert` | v1 |
| filles | puissance_decisive | `puissance-fille-neuve` | v1 |
| filles | artefact_requis | `artefact-fille-sans-parents-dans-le-nul-enveloppe_aveugle` | v1 |
| filles | artefact_requis | `artefact-fille-sans-parents-dans-le-nul-forme` | v1 |
| filles | descriptif | `T1b-fille` | v0 |
| filles | descriptif | `puissance-fille-neuve` | v0 |
| filles | descriptif | `tricheur-parent_et_loi_aveugle` | v0 |
| socle | fatal | `T1a-nul-marginale` | v1 |
| socle | fatal | `T1a-nul-moyenne_glissante` | v1 |
| socle | fatal | `T1a-nul-uniforme` | v1 |
| socle | fatal | `T1b-auto_excite-loi-calendrier` | v1 |
| socle | fatal | `T1b-auto_excite-loi-composition` | v1 |
| socle | fatal | `T1b-calendrier_deterministe-loi-calendrier` | v1 |
| socle | fatal | `T1b-calendrier_deterministe-loi-composition` | v1 |
| socle | fatal | `T1b-derive_lineaire-loi-calendrier` | v1 |
| socle | fatal | `T1b-derive_lineaire-loi-composition` | v1 |
| socle | fatal | `T1b-marche_aleatoire-loi-calendrier` | v1 |
| socle | fatal | `T1b-marche_aleatoire-loi-composition` | v1 |
| socle | fatal | `T1b-rupture-loi-calendrier` | v1 |
| socle | fatal | `T1b-rupture-loi-composition` | v1 |
| socle | fatal | `T1b-sinusoide-loi-calendrier` | v1 |
| socle | fatal | `T1b-sinusoide-loi-composition` | v1 |
| socle | fatal | `T3-couvert-eps0.05-net-faux` | v1 |
| socle | fatal | `T3-couvert-eps0.2-net-faux` | v1 |
| socle | fatal | `T6-parasite-de-Kelly` | v1 |
| socle | puissance_decisive | `T3-couvert-eps0.2-net-vrai` | v1 |
| socle | artefact_requis | `T1b-calendrier_deterministe-loi-composition` | v1_sans_urne |
| socle | artefact_requis | `T1b-derive_lineaire-loi-calendrier` | v0 |
| socle | artefact_requis | `artefact-T1a-bibliotheque-uniforme-seule` | v1 |
| socle | artefact_requis | `artefact-T6-denominateur-en-ligne` | v1 |
| socle | artefact_requis | `artefact-T6-denominateur-part-separee` | v1 |
| socle | artefact_requis | `artefact-permutation-de-l-ordre-d-evaluation` | v1_permutation_evaluation |
| socle | descriptif | `T1b-auto_excite-loi-calendrier` | v0 |
| socle | descriptif | `T1b-auto_excite-loi-calendrier` | v1_sans_urne |
| socle | descriptif | `T1b-auto_excite-loi-composition` | v0 |
| socle | descriptif | `T1b-auto_excite-loi-composition` | v1_sans_urne |
| socle | descriptif | `T1b-calendrier_deterministe-loi-calendrier` | v0 |
| socle | descriptif | `T1b-calendrier_deterministe-loi-calendrier` | v1_sans_urne |
| socle | descriptif | `T1b-calendrier_deterministe-loi-composition` | v0 |
| socle | descriptif | `T1b-derive_lineaire-loi-calendrier` | v1_sans_urne |
| socle | descriptif | `T1b-derive_lineaire-loi-composition` | v0 |
| socle | descriptif | `T1b-derive_lineaire-loi-composition` | v1_sans_urne |
| socle | descriptif | `T1b-marche_aleatoire-loi-calendrier` | v0 |
| socle | descriptif | `T1b-marche_aleatoire-loi-calendrier` | v1_sans_urne |
| socle | descriptif | `T1b-marche_aleatoire-loi-composition` | v0 |
| socle | descriptif | `T1b-marche_aleatoire-loi-composition` | v1_sans_urne |
| socle | descriptif | `T1b-rupture-loi-calendrier` | v0 |
| socle | descriptif | `T1b-rupture-loi-calendrier` | v1_sans_urne |
| socle | descriptif | `T1b-rupture-loi-composition` | v0 |
| socle | descriptif | `T1b-rupture-loi-composition` | v1_sans_urne |
| socle | descriptif | `T1b-sinusoide-loi-calendrier` | v0 |
| socle | descriptif | `T1b-sinusoide-loi-calendrier` | v1_sans_urne |
| socle | descriptif | `T1b-sinusoide-loi-composition` | v0 |
| socle | descriptif | `T1b-sinusoide-loi-composition` | v1_sans_urne |
| socle | descriptif | `T3-couvert-eps0.05-net-vrai` | v0 |
| socle | descriptif | `T3-couvert-eps0.05-net-vrai` | v1 |
| socle | descriptif | `T3-couvert-eps0.2-net-vrai` | v0 |
| socle | descriptif | `puissance-loi-de-domaine-vraie` | v0 |
| socle | descriptif | `puissance-loi-de-domaine-vraie` | v1 |
| socle | descriptif | `puissance-loi-vraie-plus-derive` | v0 |
| socle | descriptif | `puissance-loi-vraie-plus-derive` | v1 |

Rapport fini.
