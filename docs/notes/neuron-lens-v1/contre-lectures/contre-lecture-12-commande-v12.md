# Contre-lecture 12, ciblée, de la commande v12 (minuterie v2, garde de dépense v4, suivi v5) — rapport (résumé fidèle)

Contre-lecteur : sous-agent neuf, « modèle D », lancé au commit `5f405a3c` de `prep/neuron-lens-v1` par la session de reprise, après
l'arrêt du 14 novembre (journal de la course du volet A) ; rapport lu vers 16:40 UTC ; lecture seule ; essais de la garde v4 et du suivi
v5 (75 passés), essai de la minuterie v2 rejoué (conforme, 0 écart), essai en mémoire du suivi avec un faux jeton ; aucun appel réseau,
ni outil réel, ni variable secrète. Résumé fidèle ; suites dans l'en-tête de la commande v13.

**Empreintes** (vérifié) : compagnons des neuf pièces conformes ; les 26 lignes du tableau de la v12 conformes.

**Verdicts** : commande v12 après corrections mineures ; minuterie v2, essai v2 et journal après corrections mineures ; garde v4 et son
test après corrections mineures ; suivi v5 et son test **après corrections (S-1)**.

**Remarques**
- **S-1. Moyenne, bloquante pour le scellement du suivi v5.** `suivi_vast_v5.py` l.185 (`str(d[k])[:200]`), et `_derniere` l.94 depuis
  la v4 : `error` et `msg` tronqués à 200 caractères **avant** le balayage ; un jeton à cheval sur la coupure n'est plus trouvé et son
  début sort. Preuve : faux jeton placé à cheval sur le 200ᵉ caractère de `msg` → code 1, balayage muet, sortie terminée par
  `GH_TOKEN=ghp_FAK`. Un message d'erreur du loueur qui répète la requête suffirait. Correction : balayer avant de tronquer (champ par
  champ, ou refuser la sortie brute) ; idem pour `_derniere` et `derniere_ligne` ; essai du jeton à cheval sur la coupure.
- **S-2. Mineure.** L'en-tête de la v12 dit « Changements, et seulement eux », mais le tableau des empreintes et son paragraphe ont
  d'autres changements non annoncés (lignes retirées : contre-lecture 10, commandes v8 à v10, pièce `pip` v1 ; paragraphe réécrit avec
  `3a470fa4`, `799a8a32…`, `cf64f75d…` ; versions précédentes déplacées vers « archivées ») ; fichiers cités conformes ; paquet non
  vérifiable dans son périmètre (supposé). Ajouter une puce ou retirer « seulement ».
- **S-3. Mineure.** v12 l.163-164 et 173 : « destruction aussitôt » sans rappeler `-y < /dev/null` ni la preuve d'absence ; écrire
  « destruction selon l'étape 13 ».
- **S-4. Mineure.** Étape 3 : un champ absent rend `None` (arrêt) ; l'écrire.
- **S-5. Info (supposé).** Crédit non borné ; à 4,99 USD, sous le seuil de rechargement, la création a échoué le même jour (motif non
  lu) ; un nouvel échec est possible, sans danger ; le plafond de 10 USD borne la dépense, pas le crédit : un crédit épuisé en cours de
  course pourrait faire arrêter l'instance avant la poussée finale ; à signaler à la mère et à Lazar.
- **S-6. Mineure.** Minuterie v2 l.43 : `absente <ID>` sans `--temoin` ni `--non-vide` : une liste `[]` rendue à tort au code 0
  prouverait une absence fausse ; passer `--non-vide` (ou un témoin facultatif).
- **S-7. Info.** Code 6 de la minuterie sans avertissement ; demander à l'étape 13 de lire son journal.
- **S-8. Info.** Le faux outil reproduit fidèlement le défaut (sans `-y` : invite, « Aborted. », code 0, instance gardée) ; la v1 rejouée
  le reproduit ; tous les cas passent ; `-y` testé en quatrième position seulement (l'ordre éprouvé) ; la lisibilité de la liste réelle
  après destruction repose sur le journal (supposé).
- **S-9. Pas d'écart (vérifié).** Vérification d'absence saine dans le processus détaché (interprète vérifié, `PYTHONPATH` et
  `VASTAI_OUTIL` posés, jeton hérité exigé, cas « suivi sans jeton » au code 6).
- **S-10. Mineure.** Docstring de `garde_depense_v4.py` (l.15) : destruction écrite sans `-y` ; aligner sur le code (l.125).
- **S-11. Moyenne, héritée de la v3, fermée sur l'échec.** La garde vérifie l'absence par `vastai show instance <id> --raw`, non éprouvé
  pour une instance détruite : au pire fausse alerte (code 4) ; risque inverse (`{}` rendu à tort pour une instance « loading » →
  « instance_absente », minuterie seule) ; le changement v4 « sortie vide = illisible » est sans effet nouveau (la v3 rendait déjà `nan`
  par `JSONDecodeError`), inoffensif et testé. Vérifier par `absente` avec témoin, ou garder en réserve.
- **S-12. Info.** Étape 6 : en cas d'échec, conserver l'identifiant et l'heure dans `pids-volet-a-v1.txt`.

**Destructions** : aucun appel `vastai destroy instance` sans `-y` dans la v12 (étapes 6, 13), la minuterie v2 (l.41) ni la garde v4
(l.125) ; aucune destruction tenue pour faite sur un code de sortie.

**Bloquant pour la location : oui**, à cause de S-1 (correction courte : balayer avant de tronquer, essai, rescellement, nouvelle
contre-lecture ciblée) ; S-2 et S-3 à corriger dans le même passage ; le reste mineur ou info.
