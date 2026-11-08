# Passation de la fille idéation 1 vers la fille idéation 2

Session fille idéation 1 : `session_016QhUrujoj3FTuFNoYshNYB`.
Branche : `rapports/fille-ideation-1-v1`.
Date : 8 novembre 2026 ≈ 13:05 UTC.

## 1. Commande externe d'Argon v3d

- **Commande** : `commande_argon_v3d.py` (version 3d : v3c corrigée, `totalTokenCount` lu, code 11 « usage incohérent »)
- **Chemin dans le dépôt de travail** : `docs/notes/ideation-organisme-v1/argon-recherche-v1/commande_argon_v3d.py`
- **Empreinte** : `46c91df41b77a6d4cb7f5141993fda4a894118b5dd4ad1e5ba21a17dc2d67e46`
- **Absent du dépôt public** (`lciric/ideation-organism`) : ne vit que dans le dépôt de travail.
- Demande toujours `gemini-4-argon`, rend `modele_servi`, codes de sortie 0 à 11.

### Lanceur (enveloppe)

- **Fichier** : `docs/notes/ideation-organisme-v1/argon-recherche-v1/appel-argon-v4d.sh`
- **Empreinte** : `abce8e5849b3f485a6cfb5a1d4a463a6eaaf1f330f82cc95dc562c8be43af3f8`
- Installé dans `/opt/argon/` (noyau, hors session) ; tourne sous l'utilisateur `argon`.
- Réglages figés après `"$@"` (la commande garde la dernière occurrence, le noyau ne peut donc ni baisser les prix ni régler certaines bornes) :
  ```
  --prix-entree 8.3 --prix-sortie 41.5 --prix-requete-web-usd 0.05 \
  --max-requetes-web-pire-cas 20 --provision-outil-jetons 32768 \
  --url-base http://127.0.0.1:8788/v1beta
  ```
- `--delai-s 1500` est posé avant `"$@"` ; `timeout -k 20 1700` borne le processus.

### Relais Gemini v2

- **Fichier** : `docs/notes/ideation-organisme-v1/argon-recherche-v1/relais_gemini_v2.py`
- **Empreinte** : `2b0043bcab8b3922c65a4008e719408c52781d7544064b5a29a23d7ef60c1aeb`
- Écoute sur `127.0.0.1:8788` ; masque la vraie clé dans les en-têtes ET dans le corps relayé (changement v2/v1).
- Modèles en liste blanche : `--modele` (défaut `gemini-4-argon`).
- Refuse : chemin hors `generateContent` et `countTokens`, modèle hors liste, au-delà de `--max-appels` (défaut 64), corps > `--max-octets-corps` (défaut 8 Mo).

### Appel depuis le noyau

Le noyau appelle le lanceur via `--commande-externe` du lanceur d'idéation, par exemple :
```
--commande-externe "sudo -u argon /opt/argon/appel-argon-v4d.sh"
```

## 2. Relais de clé du noyau (Claude)

- **Fichier dans le dépôt public** : `orchestrator/pole/relais_reel.py`
- **Chemin local** (clone du dépôt public) : `<clone>/orchestrator/pole/relais_reel.py`
- **Version** : 0.6.0, v47 (R-764, barrière 3)
- **Empreinte** : `1b90b020287e575b5564508f9ba33b87bbc051c1015f4198e6b6e648d50ee153`
- `--modeles-permis` opérationnel (lignes 178-190, 400-403) : liste exacte de noms (`lire_modeles_permis`), refus 403 avant envoi pour tout modèle absent.

### Ligne de lancement vérifiée

```
python -I -B pole/relais_reel.py \
    --port PORT \
    --plafond-usd 12.0 \
    --modeles-permis claude-opus-5-5,claude-fable-5-1 \
    --fichier-cle CHEMIN_CLE
```

(Remplacer `PORT` et `CHEMIN_CLE`.) Si Fable refuse à la sonde, retirer `claude-fable-5-1` de `--modeles-permis`.

## 3. Références (à reconstruire sur la machine de la fille 2)

### Liste blanche

- **Fichier** : `docs/notes/ideation-pilier-attaque-v1/organisme-v1/pre-vol/liste-blanche-fille-v1.json`
- **Empreinte** : `5b38c68475d64599cc3d9198ed634afcf30f19692937af04277c8a684fe4bed7`
- Contenu : 3 fichiers — question (`29870ac9…`), synthèse (`48adeac0…`), témoins (`7db0d82b…`).
- Logique : `{os.path.realpath(chemin): sha256_fichier(chemin)}` + `ecrire_json_scelle` (même logique que `construire_liste_blanche` dans `ideation_v2.py` ligne 2745).
- **La fille 2 doit reconstruire la sienne** sur sa machine (les `realpath` diffèrent).

### Script de sonde réelle

- **Fichier** : `docs/notes/ideation-pilier-attaque-v1/organisme-v1/pre-vol/sonde-garde-reelle-v1.py`
- **Empreinte** : `3c26dac0d141fa1c5414308705a6ad3d40200c9a9fc6b5f74be47d019f3395ef`
- Teste Opus 5.5 et Fable 5.1 via le relais Claude, Argon via `appel-argon-v4d.sh`.
- Coût estimé : ≈ 0,003 USD (trois appels courts).
- **Référence seulement** : la fille 2 peut utiliser `--mesurer-consignes` du lanceur si le classifieur le permet dans sa session.

## 4. Variables de clé (noms seulement, jamais de valeur)

| Composant | Variable / argument | Défaut | Rôle |
|---|---|---|---|
| Relais Claude (`relais_reel.py`) | `--variable-cle` | `ANTHROPIC_API_KEY` | Variable d'environnement lue au démarrage, effacée ensuite |
| Relais Claude (`relais_reel.py`) | `--fichier-cle` | aucun | Fichier à lecture unique (mode 600), supprimé après lecture ; **préféré** à la variable |
| Relais Gemini (`relais_gemini_v2.py`) | `--variable-cle` | `GEMINI_API_KEY` | Variable d'environnement lue au démarrage, effacée ensuite |
| Enveloppe Argon (`appel-argon-v4d.sh`) | `GEMINI_API_KEY` | `factice-relais` | Posée à la valeur factice par l'enveloppe ; la vraie clé est dans le relais Gemini uniquement |

**`GEMINI_API_KEY_2` est réservée à l'étiqueteur : jamais utilisée pour la course.**

## 5. Cinq écarts de ligne de commande (CR-05, R-1797)

Identifiés dans le CR-05 (non reproduits ici — voir `rapports/fille-ideation-1-v1/compte-rendu-fille-ideation-1-v1-05.md`).
