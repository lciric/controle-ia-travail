# Vérification des corrections de la contre-lecture du lanceur v4 : lanceur v5, rangement v2, amorce v6, dépôt réduit v6, commande v10 — v1, 2026-11-22

Contre-lecteur de `contre-lecture-lanceur-v4-commande-v9-v1.md` (`2b223595…`), sous le même mandat
(`mandat-contre-lecteur-lanceur-v4-commande-v9-reajustement-v1.md`, `03325372…`), mêmes règles et même cloisonnement. Auteur d'aucune des
corrections. Branche `claude/brave-galileo-jhp684`, tête `c8cb7cdf8` (commits du développeur `2355c9bd7` pour le code, `ca865a030` pour la
commande et les journaux).

## Verdict
**À corriger, dans le texte seulement.** C-1 est fait, juste et éprouvé (cas sain et artefact). C-2 à C-6 sont faits. C-7 et C-8 sont
écrits en réserve, correctement. Rien d'autre n'a changé. Le nœud N-5 est acceptable. **Une correction, non bloquante pour le code** : la
commande v10 n'écrit pas la décision de la mère sur N-2 (R-4770, option (a)) ; elle dit encore « non tranché ici ». Le comportement du
code est bien celui de l'option (a) : aucune ligne de code à changer, aucun essai à blanc à refaire (la commande n'est pas dans l'arbre
réduit). Confiance : haute.

## Pièces et empreintes
`empreintes-lanceur-v4-v2.txt` (`5781984b…`, scellé, vérifié) : ses 16 lignes sont égales aux fichiers (`sha256sum -c` : 16 OK).
`corrections-contre-lecture-lanceur-v4-v1.md` (`a6341c66…`) vérifié. Le code n'a pas changé depuis `2355c9bd7`, commit source de l'essai
à blanc v5 : la liste `c20d3bac…` tient.
**Essais rejoués** (`.venv`, ligne demandée) : `test_neuron_lens_b_beta_lancer_v5.py`, `…_etapes_b_beta_v7.py`,
`…_montage_b_beta_v5.py` : **84 passed** ; arbre propre ensuite. Comptes seulement.

## Points 1 à 6

### 1. C-1 — fait, juste, éprouvé : tenu
`envoyer_verifie` du rangement v2 attend avant chaque reprise : 60 s avant le deuxième essai d'un fichier, 300 s avant le troisième. Les
essais sont comptés sur toute la course, `deja` compris (`ATTENTES_S[min(essais, 2) - 1]`). Le premier essai n'attend jamais. `attendre`
absent signifie la vraie attente (`_dormir`), jamais la rafale. Le lanceur v5 passe `Contexte.attendre` (`None` sur la machine) à
`_copie` et à `cloture`.
- **Cas sains** : premier essai sans attente ; coupure de 90 s → essais aux instants 0, 60 et 360 s, copie faite au troisième ; une
  reprise après des essais déjà faits (clôture) attend aussi.
- **Artefacts** : coupure longue → trois essais, pas plus, attentes [60, 300], et la clôture ne tente plus rien ; cinq fichiers en
  coupure → attente cumulée ≤ 1 200 s, deux reprises remises à la clôture puis faites.
- **Câblage** : le lanceur passe son attente aux deux appels ; une vraie attente lève dans les essais.
- **Banc v5** : 45 altérations tuées sur 45, dont 9 pour C-1 (rafale, attentes nulles, même attente à chaque reprise, borne absente ou à
  3 600 s, reprise remise comptée, rafale quand l'attente est absente, lanceur sans l'attente aux copies ou à la clôture) ; le témoin
  passe.
- **Essai à blanc v5** : conforme, 0 écart, liste `c20d3bac…`, nominal « 256 passed, 3 deselected ». Il ne joue pas les vraies attentes :
  son faux lanceur n'appelle pas le rangement. C'est déclaré dans la commande v10.

### 2. C-2 à C-8 : tenus
- **C-2** : `relire` rend **4** et écrit une sortie neuve « sans_objet » quand l'inventaire clos a `prevus` et `non_copies` vides. Dans
  ce cas, aucune clé n'est lue : le test est fait avant la lecture de la clé. La table de destruction a une ligne neuve, et l'étape 14 bis
  admet le code 4. Essai sain et artefacts (inventaire non clos, ancien inventaire sans `prevus`, fichier prévu non copié → 2) ; 3
  altérations tuées.
- **C-3** : le libellé dit maintenant « taille rendue et empreinte déclarée par l'envoyeur, relues à la révision rendue (non recalculée
  par la plateforme : relecture en flux maintenue) ». Réserve écrite ; la relecture en flux reste le défaut. Essai fait, altération tuée.
- **C-4** : `table-items-lanceur-v4-v2.md` : sa dernière ligne est maintenant vraie (bancs 32 sur 32 et 45 sur 45).
- **C-5** : commande v10, étape 14 : le commit du 18 est récupéré avant **tout** rejeu des 311 essais du programme de comparaison v4, y
  compris avant la création ; `git cat-file -e 5e5cb65b…` est exigé au code 0.
- **C-6** : commande v10, étape 10 bis : chaque appel de la garde de priorité à l'outil de suivi porte le préfixe de la clé restreinte.
- **C-7 et C-8** : écrits aux réserves de la commande v10, fidèlement. C-7 : un commit par fichier envoyé, nombre de fichiers des exports
  non écrit, limites de la plateforme par commit non publiées ; le regroupement des exports est non fait, pour une raison dite. C-8 :
  aucun délai propre sur un envoi qui pend (la lecture en flux en a un de 600 s) ; non fait, pour une raison dite.

### 3. Rien d'autre n'a changé : tenu
- **Lanceur v5 contre v4 (`diff`)** : en-tête, import du rangement v2, constante `MODULES` (fichiers vérifiés à la préparation : v5 et
  rangement v2), champ `Contexte.attendre`, et l'argument `attendre` dans `_copie` et dans `cloture`. Rien d'autre.
- **Essai qui le garde** : `set(v4) == set(v5)`, et seules `Contexte`, `_copie` et `cloture` diffèrent. Les huit fonctions changées
  depuis la v3 sont les mêmes qu'en v4.
- **Texte de `_split_half_64`** : empreinte `a5495c68…` inchangée.
- **Rangement v2 contre v1** : seulement C-1, C-2 et C-3.
- **Amorce v6 contre v5** : en-tête, nom du lanceur, essais embarqués.
- **Dépôt réduit v6 contre v5** : en-tête, lanceur v5 et rangement v2 à la place du lanceur v4 et du rangement v1, amorce v6, essais. Le
  lanceur v3 reste dans l'arbre.
- **Commande v10 contre v9** : seulement C-1 à C-8, les noms neufs, la liste neuve et l'essai à blanc v5.

### 4. N-5 : acceptable, pas un écart
La borne d'attente cumulée est de 1 200 s par appel. Au-delà, la reprise est remise à la clôture, sans être comptée.
- **Le devis n'est pas dépassé** : il borne les reprises à deux au plus par fichier et n'en exige aucun minimum. N-5 ne fait jamais plus
  de deux reprises ; il peut en laisser une non faite si la clôture atteint elle aussi sa borne. La conséquence est alors la règle
  existante : « COPIE EN ECHEC », puis pas de destruction sans la mère.
- **Coût au pire** : 1 200 + 360 + 1 200 + 360 s ≈ 52 minutes sur la course (copies de R et de S, puis clôture de R et de S). Le chiffre
  de la commande est juste, et il tient dans la marge de 1,3 h du pire cas.
- **Avantage** : une reprise remise à la clôture se fait des heures plus tard en variante B, ce qui vaut mieux contre une panne longue.
- **À dire à la mère, qui peut changer la borne** (nouvelle version du rangement) : pendant une panne longue sur des exports à nombreux
  fichiers, l'attente de `copie-R` est épuisée après quelques fichiers. Les fichiers suivants n'ont plus alors qu'un essai sans attente
  pendant `copie-R`, et leurs reprises vont à la clôture.

### 5. N-2, option (a) de la mère : à corriger
La décision existe au registre de la branche principale : `registres/decisions.md`, R-4770, 2026-11-22T05:53:03Z, sous GO-2026-11-22-06.
Elle n'est pas dans le registre de la branche de travail. L'option (a) retenue : reprises sur la machine seulement (deux au plus, avec
attente, C-1) ; si la relecture échoue, pas de destruction sans la mère, machine en attente dans la limite de l'arrêt dur ; écart à la
lettre du devis v9 (§ 5, point 3) déclaré ; aucun canal descendant vers la machine.

La commande v10 **ne le dit pas** : en-tête, « N-2 n'est pas tranché ici (la mère le tranche) : comportement inchangé » ; nœuds,
« v10 : non tranché ici ; à trancher par la mère avant la création » ; préalables, « le nœud N-2 tranché par la mère ». Le comportement
écrit est exactement celui de l'option (a) : reprises sur la machine avec attente, table de destruction « relecture en échec : pas sans
la mère, dans la limite de l'arrêt dur ». Seule la mention de la décision manque.

### 6. Autres écarts : aucun bloquant
- La commande v10 dit encore, aux préalables, « celle des corrections reste à faire » : ce texte sera périmé une fois cette vérification
  scellée. À reprendre avec la correction V-1.
- Les 214 échecs de `tests/test_neuron_lens_*.py` sont les mêmes qu'au développement v4, par les mêmes causes (rapport du développeur, non
  rejoué ici).

## Correction demandée
- **V-1 (texte, non bloquante pour le code)** : dans une commande v11, ou dans le feu écrit de la mère qui cite la v10, écrire que
  « N-2 est tranché par la mère, option (a), R-4770 (GO-2026-11-22-06) », avec la phrase de la décision, et retirer « non tranché ici ».
  Mettre à jour la ligne des préalables sur la contre-lecture des corrections. Aucune pièce de l'arbre réduit n'est touchée, donc la liste
  `c20d3bac…` et l'essai à blanc v5 restent valides.

## Expositions et déclarations
- Rien loué, lancé ni dépensé ; aucune requête au loueur ni à la plateforme de modèles ; aucune clé lue (noms seulement).
- Requêtes réseau : `git fetch` de `claude/brave-galileo-jhp684` (déjà à jour) et de `main` (lecture de la seule ligne R-4770 du registre
  des décisions).
- Rien lu de `diag/`, `runs/`, `docs/verdicts/`, des branches interdites ni des pièces interdites.
- Aucun refus d'outil pendant cette vérification. Non committé.
