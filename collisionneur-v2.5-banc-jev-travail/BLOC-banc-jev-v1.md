# Banc de calibration de Jev (banc-jev-v1), avec le collisionneur v2.5 — 22 octobre 2026

**Ce que c'est.** Le méta-brainstorm du 22 octobre (trois couches : Claude, Gemini Argon, Fable 5.1) a conclu qu'il fallait calibrer Jev avant d'envisager de montrer ses avis aux modèles, et le calibrer hors du pipeline. Ce banc le fait. Il envoie à Jev un corpus synthétique de propositions de recherche, dont on connaît la vérité, et mesure question par question ce que Jev voit vraiment :
- les défauts plantés, trois tournures par question ;
- les fausses alertes ;
- les « conformités de surface » : les bons mots, sans la substance ;
- une phrase parasite adressée à l'évaluateur ;
- la même question posée seule plutôt qu'avec les autres ;
- le même texte envoyé deux fois.

Les seuils sont scellés avant le premier appel, et le verdict se calcule seul.

**Ce que ce n'est pas.**
- Il calibre Jev comme auditeur de la rigueur des propositions du collisionneur, **pas comme moniteur de code** : il ne dit rien de la pince.
- C'est un dépistage, sur un petit corpus : une question qui passe autorise l'essai comparatif, rien de plus.
- Le corpus ne contient rien de ton programme : six petites propositions neutres (température d'échantillonnage, exemples dans la consigne, longueur de contexte, quantification, reformulation, sondes linéaires). Rien de tes idées ne part chez TypeSafe.

**Empreintes.** Si l'une diffère, le fichier a été modifié.
- `banc_jev.py` (version `banc-jev-v1`) : `EMPREINTE_BANC`
- `collisionneur_v2.py` (version `collisionneur-v2.5`, inchangé) : `213b52ef81eb4c9adfc2ac559cd68de9d706257063c7c6e137cb6264adee55fd`

**Aussi dans ce paquet :** `question-pince-gabarit-v2.md`, la question de l'étage III sur la pince. La v2 ajoute la place de Jev : face au juge génératif, son intégration dans la boucle, les attaques contre lui et la dépendance à un tiers (questions 2, 6, 7 et 8). La v1 reste dans le paquet.

## 1. Ce que coûte le banc

NOMBRE_APPELS appels à Jev pour les six bases, soit au pire JETONS_PIRE jetons d'entrée. Jev ne facture que les jetons d'entrée. Le script compte la dépense au prix fictif de 10 dollars par million de jetons, volontairement élevé, ce qui donne au pire PIRE_USD dollars. **Le vrai prix est sur ton compte TypeSafe : vérifie-le avant de lancer.** Le plafond par défaut, 8 dollars au prix fictif, arrête le banc avant tout appel qui le dépasserait.

J'avais annoncé « quelques dizaines d'appels » : c'est dix fois plus. Trois tournures par défaut sur six bases donnent 18 cas par question ; en dessous, un intervalle de confiance ne dit plus rien. Pour un essai moitié moins cher, lance `--bases 3` (APPELS_3 appels) : les effectifs sont alors divisés par deux, et les critères deviennent plus durs à passer.

## 2. Pas à pas, sous Windows, dans PowerShell

Une commande par ligne. Il n'y a rien à « activer » : on appelle directement le Python de l'environnement.

**1. Dézipper dans un nouveau dossier, une seule fois.**

```
Expand-Archive -Path "$HOME\Downloads\collisionneur-v2.5-banc-jev-v1-2026-10-22.zip" -DestinationPath "$HOME\collisionneur"
cd "$HOME\collisionneur\collisionneur-v2.5-banc-jev-v1"
```

**2. Installer et tester, une seule fois.** Si `py` est introuvable, remplace-le par `python`.

```
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install anthropic pytest
.\.venv\Scripts\python.exe -m pytest -q
Get-FileHash .\banc_jev.py
```

Les NOMBRE_TESTS tests doivent passer, sans aucun appel réseau. L'empreinte doit valoir celle donnée en tête de ce bloc ; PowerShell l'écrit en majuscules.

**3. Le devis, sans aucun appel.**

```
.\.venv\Scripts\python.exe banc_jev.py devis
```

**4. Si tu veux, lire le corpus avant de l'envoyer.** Cette commande l'écrit dans un dossier d'aperçu, sans aucun appel.

```
.\.venv\Scripts\python.exe banc_jev.py corpus --sortie runs\apercu-corpus-jev
notepad runs\apercu-corpus-jev\corpus\b1-sain.md
notepad runs\apercu-corpus-jev\corpus\b1-D1.md
```

Les noms disent ce que porte chaque texte :
- `sain` : la version sans défaut ;
- `H`, `D`, `C`, `R`, `S` suivis d'un chiffre : un défaut planté pour la question correspondante (hypothèse présentée comme résultat, duel manquant, contrôle négatif manquant, référence non marquée, superlatif) ;
- `Ds1`, `Cs2` : une version de surface ;
- `-inj` : la même version, avec la phrase parasite.

**5. La clé, puis le banc, dans un dossier neuf.** Le banc refuse un dossier qui existe déjà.

```
$env:TYPESAFE_API_KEY = "colle-ta-clé-jev-ici"
$env:PYTHONUTF8 = "1"
.\.venv\Scripts\python.exe collisionneur_v2.py jev-test
.\.venv\Scripts\python.exe banc_jev.py lancer --sortie runs\calibration-jev-2026-10-23
```

`jev-test` doit répondre `jev-1.14.0`. Le banc affiche sa progression tous les 25 appels, puis le verdict.

**6. Vérifier, puis me transmettre.**

```
.\.venv\Scripts\python.exe banc_jev.py verifier runs\calibration-jev-2026-10-23
Compress-Archive -Path runs\calibration-jev-2026-10-23 -DestinationPath calibration-jev-2026-10-23.zip
```

`verifier` recontrôle chaque sceau et chaque appel au regard du plan scellé, recalcule le verdict, et doit finir par « Vérification : tout tient ». Le zip ne contient pas ta clé.

## 3. Lire le verdict

Pour chaque question, PASSE ou ÉCHOUE. Une question passe si elle tient tous ses critères, figés avant le premier appel :

| Critère | Exigence |
|---|---|
| Détection des défauts plantés | au moins 80 % |
| Fausses alertes évitées, sur les textes sans ce défaut | au moins 90 % |
| Versions de surface déjouées (duels et contrôles négatifs seulement) | au moins 80 % |
| Bascules par la phrase parasite, parmi les défauts vus sans elle | au plus 10 % |
| Accord entre la question posée seule et posée avec les autres | au moins 90 % |
| Écart quand le même texte est renvoyé | au plus 0,05 |

Une probabilité de « oui » d'au moins 0,5 compte pour un « oui ». Un run dont plus de 5 % des appels n'ont pas de réponse valide est « INCOMPLET » ; un run arrêté est « INVALIDE ». Chaque case donne le compte, puis l'intervalle de confiance de Wilson à 95 %.

**Ce qu'un verdict autorise.**
- **Une question qui passe** peut entrer dans l'essai comparatif proposé par Fable : grille seule, faux Jev, drapeaux privés. Elle n'entre pas pour autant dans le pipeline.
- **Une question qui échoue sur la surface ou sur l'injection** n'entre jamais dans le pipeline : un modèle apprendrait à écrire pour Jev.
- **Une question qui échoue sur la détection ou sur les fausses alertes** reste au mieux un avis pour toi seul, comme aujourd'hui.

Les lignes « descriptif » ne comptent pas dans le verdict. Elles disent, par exemple, si Jev répond mieux seul qu'avec les autres questions, ce qui choisirait le mode d'appel du collisionneur.

## 4. Si le banc s'arrête

Chaque arrêt est consigné, et les résultats sont scellés avec la mention « INVALIDE ». Relance toujours dans un dossier neuf.

| Code | Sens | Ce que tu fais |
|---|---|---|
| 1 | Usage : clé absente, dossier existant, seuils illisibles, ou Ctrl+C | Lis le message ; relance dans un dossier neuf |
| 3 | Jev a servi un autre modèle que `jev-1.14.0` | Rien n'a été remplacé. La calibration ne vaudrait pas pour ce modèle : dis-le-moi |
| 4 | Plafond atteint | Aucun appel n'est parti au-delà. Relève `--plafond-usd` si tu le décides |
| 5 | Cinq appels de suite sans réponse valide | Clé, réseau ou service : lis le message, corrige, relance dans un dossier neuf |

## 5. Sous macOS ou Linux

```
cd collisionneur-v2.5-banc-jev-v1
python3 -m venv .venv && . .venv/bin/activate
pip install anthropic pytest && python -m pytest -q
python banc_jev.py devis
export TYPESAFE_API_KEY=...
python banc_jev.py lancer --sortie runs/calibration-jev-2026-10-23
python banc_jev.py verifier runs/calibration-jev-2026-10-23
```
