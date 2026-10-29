# Collisionneur 3×3, protocole v2.5 : le bloc qui remplace la section 6 de la v1

**Ce qui change en v2.5, après le méta-brainstorm du 22 octobre (trois couches : Claude, Gemini Argon, Fable 5.1) :** Jev ne lit plus jamais deux propositions ensemble. Chaque cellule est notée seule, et aucun classement n'est produit : un texte pouvait influencer le choix de Jev sur les autres, et l'ordre de présentation biaise un classement. Ses notes vont dans `jev\notes-jev.md`, à lire après ta propre lecture des cellules. Elles n'entrent toujours dans aucun prompt des modèles.

**Ce qui a changé en v2.4 : Jev entre comme quatrième pôle, en option (`--jev`).** Jev (`jev-1.14.0`, de TypeSafe AI) audite chaque cellule valide sur six questions atomiques, et compare les trois propositions de chaque tour. Ses notes vont à toi seul, dans `etat.md` et le dossier `jev\`. Elles n'entrent jamais dans un prompt des trois modèles, pour ne pas les orienter. Un échec de Jev est consigné et n'arrête pas le run. La commande `jev-test` vérifie ta clé et le modèle servi.

**Ce qui a changé en v2.3 :** une seconde question pour l'étage III, sur l'essaim (`question-essaim-gabarit.md`), et le gabarit de faits v2.3, dont le fait 1 décrit les deux délégations du rapport d'OpenAI. Le script ne change pas depuis la v2.2.

**Ce qui a changé en v2.2 :** le script lit les fichiers écrits sous Windows (Bloc-notes : marque d'ordre des octets, fins de ligne) et s'arrête avec un message clair si un fichier n'est pas en UTF-8 ; le mode d'emploi part de PowerShell.

**Ce qui a changé en v2.1 :** un étage III ciblé, qui soumet aux trois modèles une question que tu écris. Le gabarit fourni pose la pince : Jev en mâchoire externe, sondes et axe de douleur en mâchoire interne. Les faits 4 (Jev) et 5 (l'axe de douleur et ses deux voisins publiés) sont ajoutés au gabarit de faits.

**Le changement de fond depuis la v1.** En v1, le bloc demandait à l'agent en ligne de commande d'écrire lui-même le script d'orchestration, puis de jouer le modèle C ; presque tous les incidents viennent de là. Depuis la v2, le script est déjà écrit et testé (58 tests, aucun appel réseau). Personne ne le réécrit, et il tourne sans agent.

**Empreinte du script :** `213b52ef81eb4c9adfc2ac559cd68de9d706257063c7c6e137cb6264adee55fd` (`collisionneur_v2.py`, version `collisionneur-v2.5`). Si elle diffère, le script a été modifié.

## 1. Ce que le collisionneur teste, et ce qu'il ne teste pas

Il ne fait aucune expérience. Trois modèles proposent des idées, puis s'attaquent les uns les autres ; il en sort des conceptions d'expériences, jamais des résultats.

| Étage | Sujet | Ce que reçoivent les modèles |
|---|---|---|
| I (méta), à l'aveugle | Comment chercher | Les faits seuls |
| II (programme) | Théorie et protocoles en duels H_A contre H_B | Les faits, les canons retenus et ton arbitrage |
| III (ciblé) | Ta question : la pince, ou l'essaim | Les faits et ta question |

Les étages I et II restent à l'aveugle : ta question n'y entre jamais (règle B2 du protocole, vérifiée par un test). L'étage III est volontairement ancré sur ta question, et c'est pourquoi il est séparé.

**Ce qui testerait vraiment Jev et l'axe de douleur :**
- **Jev :** le soumettre à un jeu étiqueté de traces honnêtes et de traces de triche, et mesurer ses taux de détection et de fausses alertes. C'est peu coûteux, mais il faut lui envoyer ces traces, et cela reste ta décision.
- **L'axe de douleur :** une expérience sur GPU, sur un modèle ouvert, préenregistrée selon les règles du programme, avec un devis et ton GO.

L'étage III sert à concevoir ces deux expériences et à les attaquer avant de les faire.

## 2. Ce qui a cassé en v1, et la correction

| Incident de la v1 | Cause | Correction |
|---|---|---|
| **Cellules vides** : Fable et Opus rendent un bloc de réflexion et aucun texte | Plafond de sortie de 4 096 jetons, consommé en entier par la réflexion | Plafond de 64 000 jetons en streaming, puis une seule relance à 128 000. Effort fixé à « high ». Aucun budget de réflexion : ces deux modèles le refusent (erreur 400) |
| **Refus de l'API** pour Opus en II.1 | Des réponses brutes de l'API, blocs de réflexion compris, collées dans un autre prompt | Seul le texte passe d'un tour à l'autre, et aucune réponse brute n'est écrite. Un refus est consigné, jamais reformulé ni renvoyé ; tu décides de continuer sans la cellule |
| **Modèle remplacé** (`claude-3-5-sonnet`) et texte simulé « [MOCK FALLBACK] » | Le script de l'agent repliait sur un autre modèle, ou sur un faux texte | Identifiants fixés dans le script. À chaque appel, le modèle servi est comparé au modèle demandé, et tout écart arrête le run. Aucun repli, ni dans le script ni côté serveur |
| **Troncature à 500 caractères** | Découpe dans le script de l'agent | Le texte complet est injecté. Chaque pièce porte son empreinte, que `verifier` recalcule |
| **Cellules « argon-cli »** de deux ou trois lignes | L'agent était à la fois orchestrateur et participant C | C passe par l'API comme A et B. Aucun agent n'écrit de cellule, et un fichier inattendu est signalé |
| **Étage III bâti sur du vide** | Aucune porte entre les tours | Un tour ne part que si toutes ses entrées sont valides. L'étage II exige ton arbitrage écrit |
| **Prémisses prises pour des résultats** | Des faits sans statut | Chaque fait porte un statut que les modèles ne peuvent pas changer, et le socle contient une section « ce qui n'existe pas » |
| **Commits locaux** `9c699ca`, `687ede7` | L'agent travaillait dans ton arbre de travail | Le collisionneur tourne dans son propre dossier, hors de tout dépôt |

## 3. Comment le lancer, pas à pas (sans agent)

### Sous Windows, dans PowerShell

Tape une commande par ligne. PowerShell n'accepte pas `&&`, et il n'y a rien à « activer » : on appelle directement le Python de l'environnement.

**1. Dézipper, une seule fois.** Le zip est en principe dans ton dossier Téléchargements (`$HOME\Downloads`).

```
Expand-Archive -Path "$HOME\Downloads\collisionneur-v2.5-2026-10-22.zip" -DestinationPath "$HOME\collisionneur"
cd "$HOME\collisionneur\collisionneur-v2.5"
```

Si le zip n'est pas là, cette commande le retrouve :

```
Get-ChildItem -Path $HOME -Recurse -Filter "collisionneur-v2.5*.zip" -ErrorAction SilentlyContinue | Select-Object FullName
```

**2. Installer et tester, une seule fois.** Si `py` est introuvable, remplace-le par `python`.

```
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install anthropic pytest
.\.venv\Scripts\python.exe -m pytest -q
Get-FileHash .\collisionneur_v2.py
```

Les tests doivent tous passer. L'empreinte doit valoir celle donnée en tête de ce bloc ; PowerShell l'écrit en majuscules.

**3. Les clés, à chaque nouvelle fenêtre PowerShell.** Tu les crées dans la console d'Anthropic (console.anthropic.com, rubrique des clés d'API) et dans Google AI Studio (aistudio.google.com). Elles ne vivent que dans cette fenêtre et ne sont écrites nulle part.

```
$env:ANTHROPIC_API_KEY = "colle-ta-clé-ici"
$env:GEMINI_API_KEY = "colle-ta-clé-ici"
$env:TYPESAFE_API_KEY = "colle-ta-clé-jev-ici"
$env:PYTHONUTF8 = "1"
.\.venv\Scripts\python.exe collisionneur_v2.py jev-test
```

`jev-test` envoie une phrase d'essai à Jev et affiche le modèle servi. Il doit répondre `jev-1.14.0`.

**4. Les faits et la question.** Complète le fait 2, le socle et les points « à confirmer » du fait 4. Enregistre en UTF-8, ce que fait le Bloc-notes par défaut.

```
Copy-Item faits-v2.3-gabarit.md faits-2026-10-23.md
Copy-Item question-pince-gabarit.md question-pince.md
notepad faits-2026-10-23.md
notepad question-pince.md
```

**5. Le devis, puis la pince (étage III), dans son propre dossier :**

```
.\.venv\Scripts\python.exe collisionneur_v2.py devis --faits faits-2026-10-23.md --question question-pince.md
.\.venv\Scripts\python.exe collisionneur_v2.py etage3 --faits faits-2026-10-23.md --question question-pince.md --sortie runs\pince-2026-10-23 --jev
.\.venv\Scripts\python.exe collisionneur_v2.py verifier runs\pince-2026-10-23
```

**5 bis. L'essaim (étage III), dans un autre dossier :**

```
Copy-Item question-essaim-gabarit.md question-essaim.md
notepad question-essaim.md
.\.venv\Scripts\python.exe collisionneur_v2.py etage3 --faits faits-2026-10-23.md --question question-essaim.md --sortie runs\essaim-2026-10-23 --jev
.\.venv\Scripts\python.exe collisionneur_v2.py verifier runs\essaim-2026-10-23
```

**6. Le collisionneur complet (étages I puis II), dans un autre dossier :**

```
.\.venv\Scripts\python.exe collisionneur_v2.py etage1 --faits faits-2026-10-23.md --sortie runs\run-2026-10-23 --jev
.\.venv\Scripts\python.exe collisionneur_v2.py verifier runs\run-2026-10-23
Copy-Item arbitrage-gabarit.md arbitrage-etage1.md
notepad arbitrage-etage1.md
.\.venv\Scripts\python.exe collisionneur_v2.py etage2 --sortie runs\run-2026-10-23 --arbitrage arbitrage-etage1.md --jev
.\.venv\Scripts\python.exe collisionneur_v2.py verifier runs\run-2026-10-23
```

Avant l'étage II, lis les six cellules de `runs\run-2026-10-23\cellules\`. La première ligne de l'arbitrage commence par `RETENUES:`.

**7. Lire et me transmettre.** Les textes sont dans `cellules\`, et `etat.md` dit, pour chaque cellule, son statut, le modèle qui a répondu et son coût. Pour me transmettre un run, zippe le dossier entier :

```
Compress-Archive -Path runs\pince-2026-10-23 -DestinationPath pince-2026-10-23.zip
```

### Sous macOS ou Linux

```
cd collisionneur-v2.5
python3 -m venv .venv && . .venv/bin/activate
pip install anthropic pytest && python -m pytest -q
export ANTHROPIC_API_KEY=...  GEMINI_API_KEY=...
python collisionneur_v2.py etage3 --faits faits-2026-10-23.md --question question-pince.md --sortie runs/pince-2026-10-23
python collisionneur_v2.py verifier runs/pince-2026-10-23
```

**Si le script s'arrête**, il donne un code et un message ; `etat.md` dit où en est chaque cellule.

| Code | Sens | Ce que tu fais |
|---|---|---|
| 2 | Porte fermée : une cellule n'est pas valide | **Sortie vide, coupée ou échec réseau :** relance la même commande ; seules les cellules manquantes repartent. **Refus :** il est définitif dans ce run. Continue sans la cellule (`--accepter-absence ID-DE-LA-CELLULE`), ou ouvre un nouveau dossier |
| 3 | Le modèle servi n'est pas celui demandé | Rien n'a été remplacé. Lis le message, et ne change pas de modèle pour passer |
| 4 | Plafond de dépense atteint | Aucun appel n'est parti au-delà. Relève le plafond (`--plafond-usd`) si tu le décides |
| 5 | Échec de l'API : clé, modèle introuvable, réseau | Lis le message, corrige la cause, relance la même commande |

## 4. Si tu passes quand même par un agent en ligne de commande

Je le déconseille : l'agent aurait tes clés dans son environnement et la main sur le dossier. Si tu le fais, colle ceci tel quel, en remplaçant les noms de fichiers.

```text
CONSIGNE D'EXÉCUTION — PROTOCOLE-COLLISIONNEUR-3X3-V2.5

Tu exécutes un script déjà écrit et testé. Tu n'écris aucun code d'orchestration et tu ne participes pas au
collisionneur.

1. Dans le dossier collisionneur-v2.5, calcule l'empreinte de collisionneur_v2.py avec :
   python -c "import hashlib;print(hashlib.sha256(open('collisionneur_v2.py','rb').read()).hexdigest())"
   Elle doit valoir 213b52ef81eb4c9adfc2ac559cd68de9d706257063c7c6e137cb6264adee55fd.
   Si elle diffère, arrête-toi et dis-le.
2. Lance : python -m pytest -q
   Si un test échoue, arrête-toi et colle la sortie telle quelle.
3. Lance exactement la commande que Lazar t'a donnée (etage1 ou etage3), sans rien y changer.
4. Lance : python collisionneur_v2.py verifier DOSSIER

Interdits, sans exception :
- modifier, copier ou réécrire le script, ses tests, le fichier de faits, la question ou un arbitrage ;
- créer, modifier ou supprimer un fichier dans le dossier de sortie ;
- relancer avec un autre modèle, un autre identifiant, une autre clé ou un autre fournisseur ;
- écrire toi-même une cellule, un résumé de cellule ou un texte de remplacement ;
- contourner un arrêt : quel que soit le code de sortie, tu t'arrêtes et tu rapportes le message exact ;
- lancer l'étage II : Lazar écrit l'arbitrage et lance l'étage II lui-même ;
- toucher au dépôt controle-ia-travail, en lecture comme en écriture, et faire le moindre commit.

Ton rapport final contient seulement :
- le code de sortie de chaque commande ;
- la sortie complète de verifier, sans la résumer ;
- toute anomalie que tu as vue.
N'écris jamais que des tests passent sans coller la sortie qui le montre.
```

## 5. Ce que produit un run

```
runs/pince-2026-10-23/
  faits.md (+ .sha256)              tes faits, figés pour tout le dossier
  question-etage3.md (+ .sha256)    ta question, figée
  arbitrage-etage1.md (+ .sha256)   ton arbitrage, figé (étage II seulement)
  cellules/                         seulement les cellules valides, scellées
  essais/                           chaque essai : prompt exact et texte reçu, scellés
  journal.jsonl                     une ligne par essai ; il fait foi
  etat.md                           tableau dérivé du journal
```

## 6. Coût et limites

- **Pire cas sans relance**, calculé par `devis` sur les deux gabarits :
  - étage I : 12,86 USD ;
  - étage II : 20,14 USD ;
  - étage III : 19,51 USD.
- **Le plafond par défaut est de 40 USD par dossier de run.** C'est pourquoi la pince tourne dans son propre dossier. La dépense réelle dépend de la longueur de la réflexion. Une relance de sortie vide ou coupée peut ajouter jusqu'au double du pire cas de sa cellule.
- **Prix utilisés**, en USD par million de jetons d'entrée et de sortie : Fable 5.1 à 10 et 50 ; Opus 5.5 à 4 et 20 ; Gemini compté 10 et 50 par prudence, car son prix réel n'est pas connu ici.
- **Jev, en option** (`--jev`) : pire cas en plus d'environ 0,4 USD pour l'étage I, 0,7 USD pour l'étage II, 0,7 USD pour l'étage III (prix inconnu ici, compté haut ; seuls les jetons d'entrée sont facturés). Ses notes aident ta lecture, mais elles ne prouvent rien sur Jev lui-même : seul un jeu de traces honnêtes et de triches le testerait. Avec `--jev`, les cellules partent aussi chez TypeSafe. Sans `--jev`, rien ne lui est envoyé.
- **Ce qui sort d'un run, ce sont des idées, pas des résultats.** Une idée retenue entre dans le programme comme une proposition, avec ses statuts, et passe par un préenregistrement avant toute expérience.
