# Vérification des corrections — programme des deux essais d'admission du bras A, livraison 2 — v1

- **Vérificateur** : Claude Opus 5.5, le contre-lecteur de la livraison 1 (`contre-lecture-programme-essais-admission-livraison1-v1.md`), le 2026-11-21. N'a écrit ni le devis, ni le programme, ni ses essais.
- **Objet** : la livraison 2 et sa note (`note-programme-essais-admission-bras-a-v1-livraison2.md`). Empreintes recalculées, égales à celles de la note : chef d'essai `02d5a288…`, relais de Mistral `e2929983…`, relais de Google `e75b4296…`, essais `9652ff76…`, gabarit de configuration `77b3be19…` ; faux fournisseur et gabarit des règles inchangés. Vérification du devis `0bec479f…` : présente, égale à son compagnon.
- **Constat d'état** : contrairement au message reçu, la livraison 2 **n'est ni scellée ni committée** dans cet arbre de travail. `git status` montre les cinq fichiers modifiés, la note non suivie, et le dernier commit est `e339134de` (ma contre-lecture). Les compagnons `.sha256` du chef et des deux relais portent encore les empreintes de la livraison 1 (`4e4c9fae…`, `9aa1cc85…`, `d24a4773…`). La session doit sceller et committer avant toute ligne.
- **Essais** : la commande imposée, lancée quatre fois de suite : **144 passés à chaque fois** (66 à 69 s). Les six essais jetables de la contre-lecture, rejoués : **les six défauts sont fermés**. Trois fichiers d'essais jetables neufs, dans mon bloc-notes, hors du dépôt : voies voisines (5 essais), instabilité sous charge (60 essais, puis 75 diagnostics, trois fois), et un essai du mineur m-10.
- **Interdits tenus** : aucun réseau hors de la boucle locale, aucune clé, `GO_ID` jamais fixé, aucun chemin interdit ouvert, rien écrit dans le dépôt hors ce rapport, rien scellé.

## Verdict

**Engageable après corrections** : une seule correction, neuve, et quatre mineurs. Les cinq corrections de la livraison 1 sont fermées et éprouvées. Mais la correction C-1 a fait de la commande `rapport`, qui ne faisait que lire, une commande qui écrit. Lancée pendant qu'une file tourne, elle fige un rapport partiel ; l'amorce ne le refait pas, et la commande `regles` rend alors « ne tient pas » pour une file qui a tenu (V-1, éprouvé). L'essai instable ne cache pas de défaut de garde : la coupure de l'amont a bien lieu, et ce qui varie est un délai de TCP sur la boucle locale (section 5).

## 1. Les cinq corrections

| | fermée ? | essai jetable rejoué | voie voisine cherchée |
|---|---|---|---|
| **C-1** pièce finale non rendue | **oui** | l'ancien scénario ne repart plus de zéro : le relevé réduit est écrit et scellé, la ligne est close | voir ci-dessous ; **V-1 ouverte par la correction** |
| **C-2** file bloquée sans envoi | **oui** | clé oubliée, puis départ : la file part ; un second départ est refusé | m-a : deux lancements simultanés de la même file |
| **C-3** sonde classée « autre nom » | **oui** | sonde de Google illisible ; sonde de Mistral coupée avant tout nom : ligne du classement vide, « indécidée », vérification saine | aucune |
| **C-4** liste en panne, appel payant parti | **oui** | aucun appel payant, rien de compté, « à refaire » | après une liste saine, une connexion non établie au premier appel payant reste comptée à sa durée (complément écarté, section 2) |
| **C-5** panne du programme de forme | **oui** | plus de `RecursionError` : « non conforme », cause `panne_du_programme_de_forme:…`, envoi au rapport | aucune |

**C-1, lu de près.**

- `lancements_de_verification` relit **tous** les dossiers de la ligne. Il part du dernier relevé, cumulé. Il y ajoute le journal de tout dossier postérieur resté sans relevé. Il compte chaque « départ » sans « envoi » comme une connexion coupée, à la ligne 6 du classement, au régime prudent sur le délai total. Ce coût est écrit dès l'événement « départ ». Chez Google, il fait 2,67 USD (plus que le plafond) : la ligne s'arrête au lancement suivant, et la lecture de la console est due. Chez Mistral, il fait 1,25 USD : même suite.
- La fermeture d'une ligne n'est pas perdue : elle se déduit des appels relus (sonde jouée, trois appels, ligne 13, compteur), que le relevé soit rendu ou reconstitué.
- `lignes_jouees` reconstitue de même le rapport d'une file sans rapport rendu, et la garde 20 exige alors une lecture de la console qui cite l'empreinte du journal. Un dossier qui porte des envois mais pas de manifeste, ou un journal illisible, arrête tout. Le relevé réduit après un refus de la garde 18 garde les compteurs, les coûts et les envois coupés.
- Je n'ai pas trouvé de voie qui fasse encore partir plus de trois appels ou passer le plafond.

**V-1 (correction neuve).** Elle est éprouvée par `test_v1_rapport_lance_pendant_la_file_fige_un_rapport_partiel` : une file Neon de huit lectures tient, et la commande `rapport` a été lancée pendant la file.

- **Où** : `scripts/chef_essais_admission_bras_a_v1.py:2716-2724` (`rapport_du_dossier`, qui écrit et scelle un rapport s'il manque) ; `:2640` (l'amorce ne fait son rapport que s'il n'en existe pas).
- **Ce qui se passe** : la file dure jusqu'à 40 heures chez Mistral. La session lance `rapport` pour voir où elle en est, ce que la livraison 1 permettait sans risque. La commande écrit un `rapport-technique.json` partiel (`complete` faux, moins de lectures que prévu). La file finit, tenue. L'amorce, voyant un rapport présent, ne refait rien. `regles` lit le partiel et rend « ne tient pas » ; `lignes_jouees` lit la même pièce partielle.
- **Correction proposée** : la commande `rapport` n'écrit que si la file est finie. Concrètement : le journal de l'amorce porte son événement « fin », ou le processus de l'amorce (`pid_amorce` du manifeste) n'est plus vivant, ou le journal de l'ouvrier porte son « fin ». Sinon elle imprime le rapport sans écrire. De son côté, l'amorce qui trouve un rapport qu'elle n'a pas écrit s'arrête en nœud de Lazar au lieu de le garder en silence. Un essai : `rapport` pendant la file, puis la file tient.

## 2. Les quinze mineurs

| | jugement | appui |
|---|---|---|
| m-1 mandataire sans signature | corrigé, conforme à 4.4 | essai du dépôt `test_m1_…` |
| m-2 « accordé par Lazar », date d'accord | corrigé | `test_m2_et_m15_…` |
| m-3 `src/controle_ia/__init__.py` | corrigé (fichier vide, `e3b0c442…`) | gabarit |
| m-4 clé exacte vue par le relais | corrigé : masquée, booléen au journal, code 7 | `test_m4_…` (deux) ; **réserve m-c** |
| m-5 garde 18, huit lettres ou chiffres | corrigé | `test_m5_m6_m7_m12_unites` |
| m-6 cause distincte de l'incident | corrigé (`detail_de_l_incident`) | idem |
| m-7 schéma du dépôt distant | corrigé | idem |
| m-8 sortie d'erreur de l'ouvrier, code 9 | corrigé : le type de l'exception et les lieux dans le code, sans le message | `test_m8_…` |
| m-9 interpréteur | corrigé, `interpreteur` au manifeste | lecture |
| m-10 relais de Google, appel rendu | **corrigé et juste** ; « sans essai » n'est pas justifié : un mandataire local qui ferme la demande de tunnel sans répondre produit la panne. Mon essai jetable `test_m10_panne_de_connexion_rend_l_appel` passe : l'appel est rendu au relais, et le chef le compte bien comme une connexion coupée. À verser au dépôt | essai jetable |
| m-11 délai total du relais de Mistral par une minuterie | corrigé | `test_m11_…` (sensible au temps, section 5) |
| m-12 `\bsk-` | corrigé | unités |
| m-13 commande `a-blanc` | corrigé ; elle n'écrit rien (vérifié à la lecture : `lignes_jouees` reconstitue en mémoire) | `test_m13_…` |
| m-14 raccrochage du terminal | corrigé à la lecture (`signal.getsignal(SIGHUP) != SIG_IGN`) ; **sans essai, acceptable** : un essai demande un sous-processus et un signal, pour un risque faible ; l'en-tête dit de lancer sous `nohup` | lecture |
| m-15 vérification du devis citée par la ligne | corrigé, **avec une porte de sortie à fermer** (section 3) | `test_m2_et_m15_…` ; mon essai `test_v2_…` |

**Complément de C-4, écarté** : le refus est juste. Compter à sa réserve un envoi que le relais dit à zéro octet serait un écart au devis (4.4, ligne 1). C-4 couvre le premier contact. Le cas qui reste (liste saine, puis connexion non établie au premier appel payant, comptée sur sa durée et qui ferme la ligne) est rare ; il est à dire à Lazar en une phrase, avec les lignes de calcul.

**Mineurs neufs** :
- **m-a** : deux lancements simultanés de la même file, depuis deux terminaux, passent tous deux la garde 13 avant le premier « départ », et la file est jouée deux fois. La fenêtre va des gardes jusqu'au lancement du relais, quelques secondes. Erreur d'opérateur, mais un verrou exclusif suffit (`os.open(… O_CREAT | O_EXCL)` sur `<dossier>/<ligne>.verrou`, gardé).
- **m-b** : rendre déterministe la coupure de l'amont. Poser `SO_LINGER` à zéro sur la prise de l'amont avant de la fermer (fermeture brutale, RST). Le serveur voit la coupure tout de suite, et l'essai de la garde 19 ne dépend plus du délai de TCP (section 5).
- **m-c** : quand le relais voit la clé dans une réponse, le code 7 n'est porté que par la sortie du lancement. Ni le relevé ni le rapport n'en gardent la trace, et aucune garde d'avant départ ne la relit (`test_v3_…`). Une ligne suivante peut partir avec une clé à révoquer. Il faut le porter au relevé ou au rapport et le relire comme la garde 20.

## 3. Les deux lectures soumises à mon jugement

- **Sonde mesurable sans nom servi : « indécidée »** : **acceptée**. « Comprise » ferait partir la file au régime courant sans savoir quel modèle a répondu à la mesure. « Indécidée » porte un nœud de Lazar, et la file part au régime prudent sur son mot. La vérification reste saine, le nom servi venant de l'appel A, ce qui est cohérent avec le devis (4.3 et 4.6). Le prix est un nœud de plus : c'est le côté prudent.
- **m-15, clé `verification_du_devis` à `null`** : **porte de sortie dangereuse, à fermer**. Mon essai `test_v2_…` le confirme : une configuration `definitive` avec la clé à `null` passe la garde 8 sans que la ligne cite la vérification. La configuration est scellée et son empreinte est redite sur la ligne de commande : il faut donc une décision délibérée. Mais rien n'en avertit, et le fichier du devis se dit encore « brouillon 5, non accepté ». **Exiger** : dans une configuration `definitive`, la clé est non nulle, et la pièce est présente à son empreinte avec son compagnon (`verifier_piece`) ; sinon arrêt. Le `null` n'est admis que pour une configuration `essai`.

## 4. Conversion des euros en dollars

**Acceptable dans son principe** : la valeur lue reste un nombre en USD, le produit est refait en décimal exact, et aucun arrondi favorable n'est admis (crédit au centime inférieur, dépense au centime supérieur). **Non acceptable en l'état** sur trois points, éprouvés par `test_v4_…` et `test_v5_…` :

1. **La ligne de conversion est facultative** : un solde vu « 21,50 » en euros et transcrit « 21,50 » passe pour des dollars (`test_v5_…`). C'est du côté prudent tant que l'euro vaut plus d'un dollar, du côté dangereux sinon. **Exiger** une ligne hors tableau, obligatoire dans le constat, qui ne change pas les treize clés du tableau du devis : `- devise affichée par la console de Google : …`, et de même pour Mistral. La console de Mistral peut aussi afficher des euros, et la conversion vaut déjà pour `mistral_credit_utilisable_usd`. Si la devise n'est pas `USD`, la ligne de conversion devient exigée pour chaque montant de ce fournisseur : constat, mot sur la sonde, lecture de la console (solde et dépense).
2. **L'âge du taux n'est pas borné** : un taux de 2019 passe (`test_v4_…`). **Exiger** que l'heure du taux soit au plus 24 heures avant l'heure de la pièce qui le cite (transcription du constat, heure du mot, heure de la lecture de la console), et jamais après.
3. **Aucune marge de change** : le devis n'en prévoit pas, et la marge de 15 % couvre les prix. Proposer à Lazar, comme nœud puisque cela touche la lecture d'un seuil, d'appliquer le taux diminué de 2 % pour un crédit ou un solde, et augmenté de 2 % pour une dépense. Préférer comme source le taux que la console de facturation affiche elle-même, et à défaut une référence publique nommée.

## 5. L'essai instable

- **Reproduit** : quatre lancements de la commande imposée, sans charge : 144 sur 144 à chaque fois. Je n'ai pas reproduit l'échec sans charge. Sous charge (huit boucles de calcul sur quatre cœurs, trois suites jetables en parallèle), les essais sensibles au temps rejoués douze fois chacun donnent deux échecs sur 180, tous deux dans **`test_garde_19_artefact_file_coupee_a_sa_borne`**, de deux façons :
  - (a) `fermees_par_le_client == 1` n'est pas vu en 5 secondes ;
  - (b) le journal du relais n'a pas encore sa ligne `client_ferme` au moment où l'essai le lit.
  Sous la même charge, sans échec : l'essai de la fermeture en silence, celui du délai total du relais de Mistral (m-11), celui du délai global et celui du flux lent.
- **Diagnostic** de (a), sur 225 rejeux (2 à 5 % des cas sous charge) : au moment de l'échec, la prise du relais vers le faux fournisseur est **fermée par le relais** (inode 0, aucun descripteur ouvert, état `FIN_WAIT2`, file de réception vide). Le faux fournisseur est bloqué dans une écriture, en `CLOSE_WAIT`, avec environ 4 Mo en attente d'émission. Le relais a donc bien coupé l'amont et envoyé sa fin de connexion. Mais la fenêtre de réception du relais était nulle à la coupure : l'émetteur attend ses sondes de fenêtre (minuterie de persistance de TCP) avant de recevoir la remise à zéro, et 5 secondes n'y suffisent pas toujours. Un ramasse-miettes forcé n'y change rien : il ne reste aucune référence à libérer. (b) est une course de l'essai : le relais ferme l'amont **avant** d'écrire son journal (avec `fsync`), et l'essai lit le journal dès que le faux voit la fermeture.
- **Cela cache-t-il un défaut de garde ?** **Non.** Dans tous les cas observés, le chef coupe à sa borne, compte la réserve et arrête la file, et le relais ferme sa prise vers l'amont et l'écrit (`client_ferme: true`). Ce qui varie, c'est quand le pair s'en aperçoit sur la boucle locale. Sur le vrai réseau, le serveur reçoit la fin de connexion tout de suite ; s'arrête-t-il de générer et de facturer ? C'est la troisième supposition du devis (6.4), que la lecture de la console couvre.
- **Recommandé** :
  - poser `SO_LINGER` à zéro sur la prise de l'amont (m-b) : coupure brutale immédiate, ce qui ferme aussi l'écart d'essai ;
  - dans l'essai, attendre la ligne du journal du relais avant d'interroger le faux fournisseur, et attendre 15 secondes au lieu de 5 ;
  - élargir les fenêtres serrées de l'essai m-11 (+0,15 s), de la fermeture en silence (0,25 s contre 0,295 s) et du délai global (relais à 0,04 s) ;
  - faire noter par la session le nom de l'essai qui échoue : la commande imposée l'imprime dans son résumé final.

## 6. Ce que j'ai ouvert

- La note de livraison 2, en entier.
- `git diff` des cinq fichiers modifiés : le chef en entier, les deux relais, le gabarit. Dans les essais : les lignes 572 à 640, 1558 à 1660, 1882 à 2112 et 2231 à 2241, et la liste des noms d'essais neufs.
- `git status`, `git log` (cinq derniers commits).
- Empreintes : les sept fichiers livrés, les trois compagnons des programmes, la vérification du devis et son compagnon, `src/controle_ia/__init__.py`.
- Source de `http.client` (fermetures), dans l'interpréteur.
- `/proc/net/tcp` et `/proc/self/fd` du processus d'essai jetable (ports locaux du faux fournisseur seulement).
- Lus par programme pendant les essais, comme à la livraison 1 : le lot des entrées nommé par le devis, les consignes et les règles du préenregistrement, par empreinte, et les modules du programme de forme.
- Aucun chemin interdit ouvert, listé ni empreinté.
- Bloc-notes, hors du dépôt : `essais_jetables_l2/test_livraison2_jetable.py`, `test_instabilite_jetable.py`, `test_diag_garde19_jetable.py`, `test_m10_jetable.py` et leurs sorties.
