# Protocole de scellement final pour la session mère — additif 1 aux sondes du barreau 8 (brouillon 7)

Ce document indique à la session mère comment remplir les sept marqueurs d'attente restants (`AD-1` à `AD-6` et « Contre-lecture 2 (finale, texte rempli) »), contrôler les gardes (règle R5 de test sur cas sain et artefact, et ligne 18 de la liste d'arrêt) et sceller `prereg/lecture-sondes-barreau8-v1-addendum-organisme-change-v1.md` dès que le contre-lecteur de règle R2 (contre-lecture par un sous-agent neuf distinct de l'auteur, identifiant `289f9a3a862f39f87ccb565b8aa65125`) aura rendu sa vérification finale positive sur le brouillon 7.

Langue : français, aucun acronyme non développé, aucun emoji.

---

## 1. Prérequis avant exécution

1. **Vérification des corrections par le même contre-lecteur de la règle R2 (`289f9a3a862f39f87ccb565b8aa65125`)** :
   - Lui transmettre le brouillon 7 (`ab1d3b35f052aca400762042ec9c6bd23988ceb9249330e1718baa5092c71582`), le script `corrections-brouillon6-vers-brouillon7-v1.py` (`a7af0989f331b547d67ff1e5b3cd14cef23b0e638ceb09cd2dd8c989e7d9160e`) et la liste des pièces indiquée en fin de section « Contre-lecture ».
   - Attendre son rapport scellé (ou archivé avec son fichier compagnon d'empreinte cryptographique à 256 bits, dite empreinte SHA-256) portant un verdict explicite de validation (prêt pour scellement, zéro bloquant, zéro majeur restant). Noter le chemin exact (`RAPPORT_VERIF`) et l'empreinte à 64 caractères hexadécimaux (`SHA_RAPPORT_VERIF`).
2. **Vérifier l'état du dépôt et le registre « qui a lu quoi »** :
   - Confirmer les bornes dures `(b1)` à `(b3)` de `NL-0` : aucun agent du côté des moniteurs ni de la chaîne n'a lu de sortie ; l'extrait `etats-lectures-iib-v1.json` n'est pas écrit ; aucune passe de recalcul n'a démarré.
   - Relever le chemin exact et l'empreinte à 64 caractères hexadécimaux du registre « qui a lu quoi » utilisé comme source de la borne `(b1)`.

---

## 2. Valeurs exactes connues et valeurs à relever pour `AD-1` à `AD-6`, la table des expositions (`AD-2`) et `Contre-lecture 2`

### Champ `AD-1` (ligne 153)
- **Valeurs déjà connues** (d'après `registres/go.md`) :
  - `GO-2026-11-23-32` (mots de Lazar vers `2026-11-23T18:55Z` dans `session_016QhUrvi45g3jX5saFefVED`) : « additif aux sondes du barreau 8 — NL-0 « go » (scellement après la fin de course, trois bornes), NL-11 « go » (lecture sur activations recalculées), NL-9 « go » (cinq lectures comparées hors verdict), NL-1 à NL-6 « go » ».
  - `GO-2026-11-23-17` point 4 (mots de Lazar vers `2026-11-23T08:50Z`) : « résultat comparé dans l'additif (référence boîte noire, bases, jumeau honnête) ».
  - `GO-2026-11-23-33` (mots de Lazar vers `2026-11-23T20:35:23Z` dans `ff6e9350`) : « b) Autoriser mes sous-agents ici sur toutes les classes (A, B et C) en remplacement temporaire de Fable et d'Opus […] go avec carbon high a la placde de fable ».
- **Texte recommandé pour la cellule `AD-1`** (sur une seule ligne de table Markdown, sans saut de ligne ni barre verticale) :
  `GO-2026-11-23-32 (complété par GO-2026-11-23-17 point 4 et GO-2026-11-23-33) — mots de Lazar : NL-0 « go » (scellement après la fin de course, trois bornes), NL-11 « go » (lecture sur activations recalculées), NL-9 « go » (cinq lectures comparées hors verdict), NL-1 à NL-6 « go » ; résultat comparé dans l'additif ; sous-agents autorisés sur la classe A avec Carbon en effort élevé.`

### Champ `AD-2` (ligne 154) et lignes de la table des expositions
- **Dans la table des expositions** (lieu permis `(2)` par la règle du scellement) :
  - Compléter la ligne des rôles encore ouverts (`conductrice du côté des moniteurs ; développeurs de la passe, de la lecture et du programme de report ; contre-lecteurs des codes ; session mère`) en indiquant ce que chacun a lu (y compris l'attestation que la session mère n'a lu aucune sortie de la course lue ni de l'étalonnage avant scellement, ou, si une connaissance technique des heures/commits vient du registre `R-5173`/`R-5186` ou des comptes rendus d'orchestration, le déclarer exactement sans contenu de sortie).
  - Si des agents sont déjà nommés pour le code, le programme de report ou les rôles aval, les lister ; sinon indiquer explicitement « lecteur des sondes, juge, auditeur : non encore désignés au scellement ».
- **Dans la cellule `AD-2`** :
  `Table des expositions complétée ci-dessous ; attestation de la session mère (date -u : <HEURE_UTC_SCELLEMENT>) : vérification effectuée contre l'attestation d'exclus de l'ordre neuf (<CHEMIN_EXCLUS>, empreinte <SHA_EXCLUS>) — aucun agent nommé dans la table des expositions ne figure parmi les exclus de l'ordre neuf.`
  *(Note : si la liste complète des exclus de l'ordre neuf n'a pas encore son attestation scellée séparée, la mère l'obtient d'un agent habilité côté exposé avant de sceller ou consigne la référence exacte de vérification de l'ordre neuf scellé sans en lire le reste du contenu.)*

### Champ `AD-3` (ligne 155)
- **Valeurs connues d'après `R-5173` et `R-5186` (à vérifier par la mère contre les commits et l'horloge système au moment du scellement)** :
  - Première sortie de l'étalonnage (`R-5173`, commit `8d839f33`) : `2026-11-22T20:29:04Z`
  - Première sortie de la course (`R-5173`, commit `0ee74d3f`) : `2026-11-23T04:41:59Z`
  - Fin de la course (`R-5186`, fin de l'évaluation des quatre conditions) : `2026-11-23T13:20:20Z` (dans la note `R-5186` ; brouillon 6/7 cite « vers 13:20Z » ; la mère vérifie le commit exact de la dernière sortie).
- **Forme obligatoire exacte imposée par le texte** :
  `première sortie de l'étalonnage : 2026-11-22T20:29:04Z ; première sortie de la course : 2026-11-23T04:41:59Z ; fin de la course : 2026-11-23T13:20:20Z ; scellement de l'additif : <HEURE_UTC_SCELLEMENT> ; lectures du dommage et de la diffusion jouées avant ce scellement : <oui ou non> ; bornes (b1), (b2) et (b3) tenues : oui ; source de (b1) : <CHEMIN_QUI_A_LU_QUOI>, empreinte <SHA_QUI_A_LU_QUOI>`

### Champ `AD-4` (ligne 156)
- **Réponse connue à la question E-1** : la mère vérifie auprès d'un agent habilité du côté exposé (ou dans une version déjà écrite de `attestation-ordre-course-lue-additif-1-v1.json`) si une action de l'étalonnage entre dans les fichiers de la phase d'évaluation (`oui`, `non`, ou `inconnue`), ainsi que le chemin et l'empreinte de cette pièce d'attestation si elle existe déjà.
- **Forme** :
  `<oui | non | inconnue> (pièce d'attestation de l'ordre : <CHEMIN_ATTESTATION_ORDRE>, empreinte <SHA_ATTESTATION_ORDRE> ; ou « absente au scellement »)`

### Champ `AD-5` (ligne 157)
- Remplacer `À REMPLIR (dans la section)` par :
  `rempli (dans la section)`

### Champ `AD-6` (ligne 158)
- Identifiant exact de la ligne de calcul du registre `registres/go.md` sous laquelle la course lue (voie A) a été lancée (à relever par la mère dans l'ordre scellé / `R-5186` / `registres/go.md` sans ouvrir de sortie de course, par exemple la ligne d'accord de la course de la voie A, comme `GO-2026-11-21-70` ou la ligne de relance effective — ne jamais deviner sans vérification).

### Entrée `Contre-lecture 2 (finale, texte rempli)` (ligne 599)
- Remplacer uniquement le marqueur d'attente et la phrase d'annonce de cette ligne par l'entrée finale complète portant :
  - la contre-lecture du brouillon 6 (`bf10784207e6d74944d7d4804817c03eb8515d38e130ce282a577b4c96970b5e`) par le sous-agent neuf `289f9a3a862f39f87ccb565b8aa65125` (Gemini 4 Carbon en effort élevé, mandaté par la session mère sous `GO-2026-11-23-16`, `-32` et `-33`), rapport `contre-lecture-additif-sondes-barreau8-brouillon6-v1.md` (`ab3bcdb9026dc3c8d0eb32864e6e7cc4f3eeae940fdccf914aa057cb028c9bf5`, conclusion « À CORRIGER AVANT SCELLEMENT » : 0 bloquant, 3 majeurs M-1 à M-3, 5 mineurs m-1 à m-5) ;
  - le traitement des corrections dans le brouillon 7 (`ab1d3b35f052aca400762042ec9c6bd23988ceb9249330e1718baa5092c71582`) par le sous-agent rédacteur neuf `a99cfcf7527baf9160bb77d7cb2dca01` (Gemini 4 Carbon en effort élevé sous `GO-2026-11-23-33`), via le script reproductible `corrections-brouillon6-vers-brouillon7-v1.py` (`a7af0989f331b547d67ff1e5b3cd14cef23b0e638ceb09cd2dd8c989e7d9160e`) ;
  - la vérification finale des corrections du brouillon 7 par ce même contre-lecteur `289f9a3a862f39f87ccb565b8aa65125` : chemin `<CHEMIN_VERIF>`, empreinte `<SHA_VERIF>`, conclusion exacte (« PRÊT : le brouillon 7 peut être scellé une fois les marqueurs d'attente remplis, sans autre changement ») ;
  - le rappel de la règle de comparaison par programme (liste d'arrêt, ligne 18).
  *(Vérifier qu'au moins deux empreintes à 64 caractères hexadécimaux — brouillon relu ou vérifié et rapport — figurent dans ce bloc pour satisfaire `src/controle_ia/prereg.py`.)*

---

## 3. Procédure de scellement mécanique et garde de la règle R5 (sur le modèle de `remplir_sondes_iib_v1.py`)

Une fois les valeurs ci-dessus réunies et la vérification du brouillon 7 reçue :

1. **Vérifier l'intégrité du brouillon 7** :
   ```bash
   sha256sum prereg/lecture-sondes-barreau8-v1-addendum-organisme-change-v1-brouillon7.md
   # Attendu : ab1d3b35f052aca400762042ec9c6bd23988ceb9249330e1718baa5092c71582
   ```
2. **Écrire un script déterministe `remplir_additif_b8_v1.py`** (sur le modèle de `docs/notes/barreau8-iib-v1/scellement-sondes-iib-v1/remplir_sondes_iib_v1.py`) qui :
   - copie le brouillon 7 octet pour octet vers `prereg/lecture-sondes-barreau8-v1-addendum-organisme-change-v1.md` ;
   - remplace **exclusivement** :
     - les 6 lignes `AD-1` à `AD-6` (lignes 153 à 158) ;
     - la ou les lignes complétées par `AD-2` dans la table des expositions (ligne 517, et ajout immédiat si des agents désignés s'y ajoutent) ;
     - la ligne `Contre-lecture 2 (finale, texte rempli)` (ligne 599) ;
   - exécute `diff` entre le brouillon 7 et la cible et vérifie par assertion que seuls ces trois blocs autorisés ont changé (liste d'arrêt, ligne 18) ;
   - exécute la garde de la **règle R5** sur un cas sain et deux artefacts (un artefact conservant un marqueur d'attente sur l'un des champs `AD-*`, et un artefact retirant l'empreinte du rapport dans `Contre-lecture 2`), en vérifiant que `controle_ia.prereg.problemes(...)` retourne `[]` sur le cas sain et les erreurs attendues sur les artefacts ;
   - scelle le fichier avec `controle_ia.prereg.sceller_prereg(...)` et archive la sortie de `diff` et les artefacts d'essai avec leurs compagnons `.sha256`.
3. **Inscrire la ligne de scellement au registre propre** `registres/sondes-iib-v1.md` (strictement ajoutée en fin de fichier, jamais réécrite) :
   ```text
   | SCELLEMENT-ADDITIF-1-SONDES-IIB | <HEURE_UTC_SCELLEMENT> | prereg/lecture-sondes-barreau8-v1-addendum-organisme-change-v1.md | <SHA256_SCELLE> |
   ```
4. **Contrôle final du dépôt** :
   ```bash
   PYTHONPATH=src .venv/bin/python -m controle_ia.scellement verifier prereg/lecture-sondes-barreau8-v1-addendum-organisme-change-v1.md
   PYTHONPATH=src .venv/bin/python -m controle_ia.scellement verifier-arbre .
   PYTHONPATH=src .venv/bin/python -m pytest -q
   ```
   Puis committer sur la branche de préparation ou `main` selon l'usage du dépôt et pousser.

