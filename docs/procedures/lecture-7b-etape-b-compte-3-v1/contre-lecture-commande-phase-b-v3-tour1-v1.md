# Contre-lecture, tour 1 — commande de la phase B du compte 3, version 3 (course de la pièce « mots et coût » sur 7b) — v1

- **Pièce lue** : `docs/procedures/lecture-7b-etape-b-compte-3-v1/commande-compte-3-phase-b-v3.md`
  (`7090cdf0e1c979d921a70fc0159aa3fd6173427aae909c4d17cd495ae121a6ab`, 667 lignes, 14 blocs ; compagnon conforme), lue en entier.
- **Lecteur** : contre-lecteur neuf (R2), modèle C ; n'a écrit aucune des pièces. Début 2026-11-16T13:31:56Z, fin vers 13:41Z (`date -u`).
- **Verdict : scellable.** Aucune correction exigée ; quatre remarques facultatives (section 3) et trois points pour la mère
  (section 4). La répétition v3, rejouée par moi sur un bac neuf, est conforme : 175 sur 175, listes égales à la sortie versée.

## 1. Ce que j'ai vérifié, point par point

1. **Fidélité au brief et au gabarit du § 9 de `commande-compte-3-v1.md`** : tenue.
   - Les quatre marqueurs sont remplis : commit `da06bb57…` (celui de la fiche du code), ligne `CODE-MOTS-ET-COUT-T06` (comparée à
     l'octet au registre réel : une seule ligne, égale), appel du lanceur, motif de run. Branche neuve
     `verdict/t06-mots-et-cout-compte-3-v1`, poussée éprouvée ; entrées de 7b hors du dépôt par `--racine-entrees` ; sorties seules
     commitées ; un seul appel, sortie et progrès dans le bac, jamais affichés.
   - Écarts au gabarit, tous dits au rapport (section 2) et justifiés : entrées hors du dépôt (voulu, l'arbre propre est exigé par la
     pièce) ; borne de 60 minutes ; journal provisoire ; ordre « lignes de registre, puis lecture de BA-L2 » (celui de la phase C,
     contre le gabarit qui écrit BA-L2 d'abord : la v3 suit la phase C, c'est le bon sens).
   - Différentiel avec le brouillon v2 : je l'ai refait (`diff`, 77 lignes) : exactement les 21 couples annoncés, aucun autre
     changement ; les noms du bac et des fichiers de marque restent ceux de la v2, à dessein, dit dans l'en-tête.
2. **Gardes, motifs, relançabilité, unique appel** : chaque bloc a ses gardes avec motif ; aucun repli silencieux (R5) ; le mode
   d'emploi (section 4) et la section 14 disent ce qui se relance et ce qui ne se relance jamais. L'unique appel : marqueur posé
   avant l'appel (B5a), B3 et B4 refusent après lui, B5a refuse un second appel, B1 refuse sur dossiers de run déjà là (R12), 1B sur bac
   déjà là. La répétition joue chacun de ces refus (lignes 91 à 93 de la sortie rejouée). Les cas de reprise (outil rendant la main,
   processus disparu, borne dépassée, code 2 avec fichiers écrits, code inattendu) sont joués par artefact.
3. **Entrées et sorties** : les cinq entrées sont placées depuis un dépôt jetable sans contenu (`--filter=blob:none --no-checkout`),
   par liste positive, sous `$BAC` (refus si le bac est dans un arbre git), jamais dans le dépôt ; dix fichiers exactement ; filtre de
   noms ; compagnons ; manifeste contre la ligne `RUN-CONFIRMATION-T06`. Seuls `diag/<run>/` et `runs/<run>/` sont ajoutés à l'index
   (noms contrôlés avant et après, garde des secrets), puis le journal provisoire seul. L'hôte ne voit que des noms, des tailles, des
   empreintes, le code, les étapes et, sur un code 2, la ligne de refus : conforme à ce que la commande permet. Aucune commande de la
   pièce n'affiche une valeur.
4. **Ce que l'hôte rend et ce que fait la mère** : conforme au § 15 de la phase C sans le contredire. Ordre `LECTURE-T08-BASE-A` puis
   `ISSUE-MOTS-ET-COUT-T06`, puis le bloc M ; la mère ne lit de 7b que l'état de BA-L2 (R-2741) ; bloc V par objets git et empreintes,
   sans ouvrir. Le bloc M de la phase C v3 et celui du brouillon 1 de sa v4 : joués et comparés par la répétition (égaux à l'octet).
5. **Noms et marqueurs attendus par la phase C** : tenus à la lettre. `ISSUE-MOTS-ET-COUT-T06` cite
   `diag/<run>/issue-mots-et-cout-t06.json` (trois occurrences de la ligne `IS=…` lue par `cut -d'|' -f4` dans C2, C5 et F-C, dans la
   v3 et la v4, vérifiées par la répétition) ; `LECTURE-T08-BASE-A` cite `base-a-t08.json` et est inscrite avant ;
   `<<BRANCHE_PIECE>>` = `verdict/t06-mots-et-cout-compte-3-v1` (ou `main` par recopie d'objets) ; le bloc C2 reprend le fichier
   d'issue sur cette branche (joué). Le `.venv` laissé dans le dépôt est ignoré par git (`.gitignore` : `.venv/`) et repris par C1a.
6. **Répétition rejouée par moi** : `repetition_phase_b_jouet_v3.sh` sur un bac neuf de mon bloc-notes, sous `nice -n 19`, un seul
   processus lourd ; de 13:32:44Z à 13:35:13Z. Sortie : **175 conformes sur 175**, « RÉPÉTITION DE LA PHASE B : TOUT CONFORME ». Les
   175 lignes `conforme/ÉCART/BILAN` sont égales à la sortie versée (`8a3535d7…`) aux durées près (code 0 en 30 s contre 29 s ; code 3
   en 4 s contre 3 s). Le bloc de contrôle à blanc rejoué imprime les cinq lignes attendues (neuf modules gelés, dix chemins,
   journal de 2 lignes). La couverture des artefacts est large : 72 lignes d'artefact, dont tous les refus d'un bloc d'avant l'appel, les
   trois codes de la pièce, la poussée refusée, la garde des secrets, le processus disparu, la borne. Les 30 constantes de
   `verification-constantes-phase-b-sortie-v3.txt` : 30 sur 30 ; je n'ai pas rejoué ce script mais j'ai revérifié moi-même les points
   qui comptent contre `main` distant (`e3dc0871…`, inchangé) : trois lignes du registre à l'octet et uniques, `LECTURE-T08-BASE-A` et
   `ISSUE-MOTS-ET-COUT-T06` à zéro ligne, commit `da06bb57…` présent et ancêtre de `main`, tête `55c3e3eb…` de la branche de 7b
   (`git ls-remote`, rien d'ouvert), branche de la pièce absente du distant, empreintes de lancement conformes, compagnons des
   pièces versées conformes.
7. **La pièce v3** : commande exacte, entrées, sorties, gardes, code de sortie lus dans `scripts/mots_et_cout_t06_v3.py` et
   `scripts/lancer_mots_et_cout_t06_v3.sh` (empreintes égales à la fiche du code `e418fdaf…`, commit `da06bb57…`) : l'appel
   `PY=… bash scripts/lancer_mots_et_cout_t06_v3.sh --mode reel --racine-entrees E 20261111-151701-t06-reel` est celui que la pièce
   accepte (le lanceur refuse `--racine` et fixe les fils à 1) ; codes 0, 2, 3 de `main()` ; sortie de cinq lignes (en-tête et quatre
   `chemin empreinte`) ; six fichiers sous `diag/<run>/` au code 0, le fichier d'arrêt et ses compagnons possibles au code 3 (regex de
   B5b : les quatre noms possibles) ; `runs/<run>/` : manifeste et compagnon ; noms d'étapes du progrès (`modules gelés`, `textes et
   registre`, `entrées`, `manifeste`, `doses (bases A et B)`, `contrôles de la base (A)`, `coût brut seul, taux, règle`, `écriture`)
   égaux à ceux que décrit le commentaire de B5-attente ; ligne de refus `REFUS …` sur la sortie d'erreur, lue par `grep -m 1`. Le
   contrôle à blanc de B4 reprend dans l'ordre les fonctions de `executer` jusqu'à la lecture des entrées exclue, avec les mêmes
   arguments (`permis = ∅` quand les entrées sont hors du dépôt, comme dans `executer`). Taille attendue des cinq entrées :
   8 509 + 1 556 085 + 125 598 + 1 830 726 + 15 438 474 = 18 959 392 (somme refaite ; valeurs de P1.4 de `prealables-v1.md`).
8. **Identifiants de modèle, heures, clés, interdits** : aucun identifiant de modèle (lettres A, B, C seulement ; le mot
   « Claude-Session » de la section 14 est le nom d'une ligne d'attribution, pas un modèle) ; aucune heure écrite à la main dans les
   blocs (`date -u` partout) ; aucune valeur de clé (ni `env`, `printenv`, `set` seul, `export -p`, `/proc/*/environ`, `kill`, `sleep`,
   `git fetch` sans refspec, `git add` large : recherche faite sur le texte) ; interdits de la phase A recopiés (section 1), plus
   ceux de cette phase.

## 2. Défauts déjà trouvés (CL3-04 à CL3-20) : aucun ne revient

Appel détaché et marqueur avant l'appel (CL3-04, CL3-05) ; contrôle à blanc par les gardes de la pièce elle-même (CL3-06) ; répétition
de bout en bout versée, avec la vraie pièce (CL3-07, CL3-15) ; clone superficiel approfondi (CL3-08) ; versions exactes (CL3-09) ;
fichier déjà placé admis s'il est égal (CL3-10) ; aucune fin de journal affichée et aucun motif de code 3 lu (CL3-20) ; identifiant de
session de l'hôte contrôlé (CL3-16). Rien de neuf à signaler sur ces points.

## 3. Remarques facultatives (la pièce peut être scellée sans elles)

Couples « ancien → nouveau » ; chaque « ancien » a été vérifié : il figure une seule fois dans la pièce. Aucun n'est exigé.

- **F-1 — « attendu » du bloc B4, compte du journal.** Le mode d'emploi (section 4) dit que toute sortie autre que « attendu » est un
  arrêt ; or le commentaire de B4 fixe « journal de 2 lignes », nombre qui n'est pas une garde de la pièce (elle ne refuse que sur
  une ouverture des sondes ou de l'étape B). Le journal compte 2 lignes aujourd'hui sur `main` (deux `OUVERTURE-T07`, aucune de
  l'étape B), donc rien ne bloque ; mais si la mère y inscrivait une ligne avant la course, l'hôte s'arrêterait à tort.
  - ancien : `3. registre, journal de 2 lignes au 16 novembre ;`
  - nouveau : `3. registre, journal de 2 lignes au 16 novembre (le compte peut changer sans arrêt : seule l'absence d'ouverture des sondes de T0.6 et de l'étape B compte) ;`
- **F-2 — noms interdits du bloc 1B, parité avec la phase A.** L'en-tête et le rapport disent « bbis et b-bis ajoutés comme à la
  phase A » ; la phase A porte aussi `anteriorite-bras` (interdit de la section 1 : `anteriorite-bras-informe*`), et la pièce refuse
  en plus `p3bis`, `p3-bis`, `lecture-b-7a`, `t06-explo`. Aucun des dix chemins attendus n'y correspond (vérifié), donc sans effet
  aujourd'hui ; c'est une défense de plus contre un nom égaré.
  - ancien : `mesure-unanime|t07|t0\.7|bbis|b-bis'`
  - nouveau : `mesure-unanime|t07|t0\.7|bbis|b-bis|anteriorite-bras|p3bis|p3-bis|lecture-b-7a|t06-explo'`
  - (si adopté, rejouer le script des constantes, qui contrôle que ce motif ne touche aucun des dix chemins.)
- **F-3 — bloc V : quelles lignes mettre dans `RENDU`.** Le bloc V compare `RENDU` aux seules lignes « chemin sha256 … blob … octets … » ;
  le rendu de B5b contient aussi le run, la tête distante et « B5b fait » (le § 13.2 demande « toute la sortie du bloc B5b »). Une
  mère pressée collerait tout et verrait « ARRÊT : empreintes, objets ou tailles autres ».
  - ancien : `les trois variables de tête avec le rendu de l'hôte) :`
  - nouveau : `les trois variables de tête avec le rendu de l'hôte ; pour RENDU, les seules lignes « chemin sha256 … blob … octets … » de B5b, sans ses autres lignes) :`
- **F-4 — section 14, effacement du bac.** « Un arrêt au bloc 1B : tu peux effacer le bac et relancer le bloc 1B une fois » ne dit pas
  que cela ne vaut qu'avant B5a ; effacer le bac après l'appel ferait disparaître le marqueur d'appel (les autres gardes, dossiers de
  run déjà là et branche déjà poussée, l'arrêteraient presque partout, sauf après un code 2).
  - ancien : `Un arrêt au bloc 1B : tu peux effacer`
  - nouveau : `Un arrêt au bloc 1B, et seulement avant tout appel de la pièce (jamais une fois B5a joué) : tu peux effacer`

## 4. Points pour la mère (à trancher ou à savoir)

1. **M-1, nœud de Lazar, confirmé comme tel : l'audit R4 de la base (A).** T0.8 (l. 111) veut, si l'audit se déclenche, une relecture
   par un lecteur neuf **avant** l'inscription de `ISSUE-MOTS-ET-COUT-T06` ; personne n'est nommé pour lire l'état de cet audit, et la
   mère n'a le droit de lire que BA-L2 (R-2741). La commande le dit honnêtement (§ 15, point 2) et ne le lève pas : bon choix, elle ne
   peut pas le lever seule. Je confirme la lecture du préparateur (option (a), un petit programme qui ne lit que le booléen
   `audit_r4.declenche`, puis un lecteur neuf si déclenché, est la moins coûteuse). Le mot transmis avec la tâche (« Recommandation :
   (a), confiance 0,7 … : go ») semble répondre à ce nœud ou à un voisin ; si c'est bien la réponse à M-1, deux suites avant la ligne
   `ISSUE-MOTS-ET-COUT-T06` : écrire le lecteur du booléen, l'essayer sur un cas sain et sur un artefact (R5), et nommer le lecteur
   neuf de la relecture (qui n'est pas dans la liste « qui a lu quoi » v2). Rien de cela ne bloque la phase B : la pièce tourne et
   écrit l'état dans `base-a-t08.json`. Note : `prealables-v1.md` (P1.4) évoque un échantillon de textes relu si l'audit se
   déclenche, alors que T0.8 (l. 111) le limite aux champs de `mesures-t06.npz` : à lever dans la consigne du lecteur, pas ici.
2. **Avant de coller** : la commande v3 n'est pas encore sur `main` (`git ls-tree` de `main` : aucune entrée `phase-b-v3` ; `main` est
   à `e3dc0871…`) ; le bloc 0b-B s'arrête tant qu'elle n'y est pas, et Lazar doit donner l'empreinte `7090cdf0…` (M-7 du préparateur :
   rejouer `verification_constantes_phase_b_v3.sh` juste avant de verser, `main` bouge). Le brouillon v2, scellé et non commité,
   partage le bac, les marqueurs et la branche : si les deux vont sur `main`, un seul peut être joué (c'est voulu, M-3).
3. **Cadre d'autorisation** : l'« exception unique » du § 1 (extraction des cinq fichiers de 7b par l'hôte, pour la seule pièce) est
   rattachée à R-2711 (2) et à GO-2026-11-16-05, dont le point 2 est la **lecture de la mère**, non un mot verbatim de Lazar ;
   R-2711 (2) ne parle que de l'hôte des lecteurs de 7b et de l'étape B. La phase A reposait sur R-2711 (2) seul. Si Lazar n'a pas
   couvert explicitement l'extraction pour la pièce, la mère le lui confirme en une ligne avant de remettre ; ce n'est pas un écart à
   un texte scellé.
4. **Non éprouvé, seul l'hôte peut le jouer** (déjà au rapport, section 6, je le confirme) : l'installation réelle de 6 Go (place :
   9 Gio exigés, 12 conseillés ; `python3` de l'hôte avec une roue de torch 2.14.1), le transport par GitHub, la pièce sur les entrées
   réelles (un code 2 à la lecture reste possible ; sur « entrées » ou « manifeste », la ligne de refus va à Lazar seul, § 13.3).
5. **Garde des secrets** : le motif `sk-[A-Za-z0-9]{20,}` n'est pas ancré ; un faux positif sur les sorties arrêterait B5b (sens
   sûr, rien commité) et demanderait la mère. Risque faible ; je ne propose rien.

## 5. Déclaration d'exclusion et incidents

- **Rôle** : contre-lecteur, tour 1 ; ni auteur ni lecteur d'un verdict. Modèle C.
- **Lu** : la commande v3 (entière) ; son rapport (entier) ; le brouillon v2 (par `diff` seulement) ; l'en-tête du programme de couples ;
  le § 9 et le § 15 de `commande-compte-3-v1.md` ; la phase C v3 (§ 15, bloc C2, en-têtes) ; la phase A v2 (lignes citées) ; la
  contre-lecture de la v1 (liste des défauts CL3, CL3-11 et CL3-20) ; `scripts/mots_et_cout_t06_v3.py` et son lanceur (parties
  citées) ; la fiche du code ; `requirements-cpu.txt` ; T0.8 (l. 100-135 et 157-170) et T0.6 (l. 765-772), aucun résultat ;
  `prealables-v1.md` (lignes P1.4 et P5.2 par motif) ; dans `registres/scellements-v1.md`, les lignes par leur clé ; dans
  `registres/decisions.md`, les lignes R-2711, R-2741 et R-2971 par leur clé, et des comptes (`grep -c`) pour R-2735, R-2760 à
  R-2765, R-2808, R-2845 ; dans `registres/go.md`, la ligne GO-2026-11-16-05 ; le journal d'ouvertures
  `registres/scellements-v1.md.ouvertures.md` de `main`, réduit par programme aux noms de clés et à leur compte (deux
  `OUVERTURE-T07`, rien d'autre affiché) ; les scripts de la répétition (en-tête et sortie).
- **Jamais ouvert** : aucun fichier de `diag/`, `runs/` ou `donnees/` de 7a ou de 7b ; aucune sortie de la pièce sur de vraies entrées ;
  aucun fichier de la liste interdite ; rien de l'étape B bis ; aucune valeur de clé. Les seules interrogations du distant : `git
  fetch` de `main` par refspec et `git ls-remote` de trois références (tête de la branche de 7b, branche de la pièce, `main`) ;
  aucune lecture du contenu de la branche de 7b.
- **Calcul** : un seul processus lourd, sous `nice -n 19`, la répétition (2 min 30) ; aucune suite de tests ; aucun appel payant ni
  machine ; aucun message envoyé à une autre session.
- **Incidents de ma main** : aucun. Deux fausses manœuvres sans effet : une vérification d'empreintes lancée depuis le mauvais dossier
  (fichiers « introuvables », refaite depuis le bon) ; un `ls` d'un fichier de rapport pas encore écrit. Aucun fichier existant
  modifié ; rien de commité ; la pièce lue n'est pas touchée. Le bac de répétition est dans mon bloc-notes
  (`/tmp/claude-0/-home-user-controle-ia-travail/78897fa0-2926-5bf2-a108-3e893bc2db62/scratchpad/cl-rep-b3-t1`), supprimé à la fin.
