# Consigne — session fille « Neuron Lens » : essai sur un modèle publié et reproduction sur un modèle du programme — v1

Écrite par la session mère `session_01XJ6Mgn4MZR4nxqK44C8Ea3` le 13 novembre 2026 à 12:59 UTC (`date -u`), sur les mots directs
de Lazar (R-2528) : « go tester neuron lens sur un autre modele; et j'aimerais aussi reproduire ce qu'ils ont fait avec neuron
lens sur un de nos modeles prevus...lance une nouvelle session pour ca ». Langue : français, tutoiement avec Lazar, presque
aucun acronyme. La continuité vit dans les fichiers.

## 0. Règles (sans exception)
- Lis d'abord `CLAUDE.md`, puis en entier `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-0500-v1/interdits-communs-v2.md`
  (`1ee3b37075aacb278864e6eeda99b72e0d1babe9d6d02bd4a0c0aff26131337f`) ; ses règles valent pour toi, avec les écarts écrits ici.
- **Jamais** : `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`, `docs/notes/bras-attaque/`, `registres/index-bras-attaque*`,
  `anteriorite-bras-informe*`, la branche `claude/compassionate-meitner-d4ryyk` ; aucun `diag/` ni `runs/` de 7a ou 7b ;
  **aucun préenregistrement ni résultat de T0.6, T0.7, P3 ou P3-bis** ; `verifier-arbre` ne se lance pas (il traverse des chemins
  interdits). Clés : jamais une valeur, lues par leur nom seulement ; jamais `env`, `printenv`, `set` sans argument, `export -p`,
  `/proc/*/environ`. Heures par `date -u` seulement. Jamais de `git fetch` sans refspec. Garde des secrets à 0 avant chaque
  commit (motif de `CLAUDE.md` de la mère : `sk-ant-`, `sk-`, `ghp_`, `hf_`, `AKIA`, `AIza`). Ne jamais pousser vers
  `lciric/controle-ia`. Ne jamais contourner, reformuler ni confier à une autre session un refus de permission ou de classifieur.
- **Machines** : ne touche aucune instance Vast ni aucun serveur Hetzner qui n'est pas le tien (nommément jamais 58936096,
  58936099, 58936100, 60480302, 60492378). Arrêts par identifiant (R10).
- **Dépense : aucune ligne de GO n'existe encore pour ce travail.** Tu ne loues rien, tu n'appelles aucun modèle payant, tant
  qu'une ligne n'est pas inscrite dans `registres/go.md` par la mère sur un mot direct de Lazar. Ta première livraison est le
  plan et le devis.
- Tu écris sur une branche à toi, `prep/neuron-lens-v1`, poussée vers `lciric/controle-ia-travail` ; tu n'écris pas sur `main`
  et tu ne touches pas aux registres : tu proposes les lignes à la mère (`send_message` vers `session_01XJ6Mgn4MZR4nxqK44C8Ea3`),
  qui consigne. Tout dépôt reçoit son compagnon `.sha256` (`PYTHONPATH=src python3 -m controle_ia.scellement sceller FICHIER`).
- Rôles : tu ne seras lecteur ni de T0.7, ni de P3-bis, ni de G0.

## 1. Ce qui existe déjà
- Site archivé : `docs/sources/web-neuron-lens-20261113/llms.txt` (`7cc1f486…`). Dépôt de recherche public
  `stdlogits/neuron-lens` (à attacher en lecture ; jamais d'écriture) ; catalogue et lentilles sur Hugging Face (CC BY 4.0 selon
  le site ; licence du code à vérifier).
- Un lecteur neuf écrit `docs/notes/lecture-voisin-neuron-lens-v1.md` (méthode, solidité, portabilité à Llama 3.1 8B, usages) :
  la mère te préviendra quand elle sera sur `main` ; ne refais pas sa lecture, sers-t'en et corrige-la si le code la dément.
- Première lecture de la mère (R-2525) : catalogue de lecture des neurones (par signe) et des têtes de Qwen3-8B et Gemma 4 12B
  par deux lentilles tirées des poids (R : ce qu'une direction fait dire ; S : quels jetons d'entrée y mènent) ; pas un
  moniteur ; ni article ni réplication ; étiquettes et juges de la famille Claude. R4 : trop beau = réserve.

## 2. Mission, en deux volets
**Volet A — essayer Neuron Lens tel que publié, sur un de ses modèles** (Qwen3-8B de préférence ; changement de modèle permis
pour ce seul volet par le mot de Lazar) : dire, par une expérience petite et honnête, si la lecture par lentille apporte quelque
chose **à un moniteur** : (i) lire par les lentilles la **direction d'une sonde linéaire** entraînée sur un contraste simple et
public (pas nos données réservées) : ce qu'elle fait dire, quels jetons d'entrée la portent — audit de fuite textuelle ;
(ii) des **neurones comme traits** d'un détecteur, comparés à une sonde sur le flux résiduel, sur le même contraste.
**Volet B — reproduire leur chaîne sur un modèle prévu du programme** (lis `docs/programme-controle-ia-v2.md` pour la liste ;
Llama 8B est celui des sondes actuelles) : ajuster les lentilles R et S, refaire la passe d'activations, et reproduire leurs
mesures de validité (lecture contre effet du pilotage, par couche, contre leurs témoins : autre neurone, lentille des logits),
sans l'étiquetage complet par modèle (un échantillon suffit, à chiffrer).

## 3. Livraisons, dans cet ordre
1. **Plan et devis** (`docs/notes/neuron-lens-v1/plan-et-devis-v1.md`, scellé) : ce que le code permet sans réécriture ;
   licences ; pour chaque volet : étapes, machine (type de processeur graphique, heures, prix relevé le jour même), stockage,
   appels de modèles éventuels, **pire cas en USD**, et ce qui peut se faire sans dépense ; plan d'analyse **écrit d'avance**
   pour chaque mesure : hypothèse, métrique, témoin, seuil de lecture, ce qui serait « non reproduit » (R1, R3 : aucun run
   visant un signe ; R4). Propose une ligne de GO par volet (objet, plafond, échéance).
2. Envoie à la mère le verdict en cinq lignes et les deux plafonds. **Puis attends** : la mère soumet à Lazar.
3. Après inscription d'une ligne : exécution sous `GO_ID=…` (garde `.claude/hooks/garde_calcul.py`), manifeste par run (R9),
   résultats bruts scellés, machine détruite par son identifiant à la fin, dépense relevée ; rapport
   `docs/notes/neuron-lens-v1/rapport-v1.md` : reproduit ou non, avec chaque chiffre renvoyé à un fichier empreinté.
4. Passation R14 dans `docs/notes/neuron-lens-v1/passations/` à chaque arrêt.

## 4. Ce qui reste un nœud (tu t'arrêtes et tu écris à la mère)
Toute dépense hors ligne inscrite ; tout usage dans une expérience préenregistrée du programme ; toute affirmation publique ;
tout contact avec les auteurs (tu rédiges, Lazar envoie).
