# Vérification des corrections des outils de la fusion (v2) — v1

- **Nature** : vérification par le contre-lecteur d'origine (Claude Sonnet 5.5), 22 novembre 2026, du commit `9eef8fbd` : `listes_lecture_v2.py`, `recherche_bornee_v4.py`, `partition_journal_v2.py`, `manifestes_fin_v2.py`, `test_fusion_outils_v2.py`. Même cloisonnement de lecture ; aucun fichier existant modifié ; essais dans des dépôts jetables sous `/tmp/cl/` (`q1.py`, `r2`, `m2`). Les 110 essais fournis passent.

## Verdict : corrections vérifiées, sauf deux restes (un à corriger, un à trancher)

| Défaut v1 | État | Preuve |
|---|---|---|
| B1 préfixe `registres/veille*` | corrigé | `veille-de-cap-v1/…`, `veille-de-cap.jsonl`, `veille-de-capx/`, `veille/`, `veilleur/` : refusés (stricte) ; `veille.md[.sha256]` et extraits communs : autorisés |
| C1 source dossier | corrigé | source dossier → « n'est pas un fichier ordinaire » ; lien symbolique → refusé |
| C2 types de `mots` | corrigé | chaîne et dictionnaire → refus ; `nom` chaîne exigée |
| C3 noms exclus | corrigé | `quarantaine`, `matiere-premiere`, `lot/compte-4`, `sauvegarde/` refusés dans `nom` (voir R3 pour les autres champs) |
| C4 plantage | corrigé | `commit` liste → « commit mal formé », le programme continue |
| C5 valeurs fermées | corrigé pour la forme | chemin écrit normalisé (`registres/decisions.md`) ; `etat`, `evenement`, `issue` fermés ; `sert`/`quand` dictionnaire refusés ; > 300 signes refusés |
| C6 fiches | corrigé | `I-1` refusé ; marque `" i-0001 "` arrête `I-0001` ; une fiche mal formée de même identifiant met la fiche en « mère » |
| C7 commit hors principale | corrigé par défaut, contournable (R1) | commit de `lot/compte-4-v1` : `ARRET … ancêtre de la branche principale` |
| C8 `commune/` | corrigé | seuls `journal-commun-AAAA-MM-JJTHHMMZ.jsonl[.sha256]` ; `notes.md`, sous-dossiers, `.en-cours`, double `.sha256` refusés ; liens et sous-modules invisibles à l'outil |
| C9 accents | corrigé | `décision-é.md` listé et lu |
| C10 manifestes | corrigé | seuls `debut_utc`, `fin_utc`, `code`, `sortie_existe`, `cree_le` ; valeurs « SECRET », « x 0.37 », « résultat perdu » → « non conforme » ; lien symbolique → « illisible » |
| C11 a, c | corrigé | `versement-journal-*-v2`, `liste-exhaustive-…-v2` refusés ; `canaux-sessions-v6.md` plein |
| Remarques 2 à 8 | corrigées | plus de variable d'environnement ; nom de sortie imposé (`--horodatage`), refus d'écraser (R12) ; extrait de 6 mots et 30 signes sur frontières ; en-tête d'avertissement ; ordre des journaux sans effet ; binaires en « noms seuls » pour la boucle |

## Restes

### R1 — À corriger : `--ref-principale` est choisi par l'appelant, ce qui rouvre C7
- `recherche_bornee_v4.py` l. 51-56, 79, 87 ; `partition_journal_v2.py` l. 74, 198.
- Scénario (réel) : dépôt jetable, branche `lot/compte-4-v1` avec une ligne propre à cette branche. Sans option : `ARRET … ancêtre de la branche principale`. Avec `--ref-principale lot/compte-4-v1` : `lire registres/decisions.md --bras memo` montre la ligne « Un texte exclusif de la branche exclue… ». Même nature que la remarque 1 (bras choisi par l'appelant), mais ici la garde ajoutée pour C7 s'annule par un argument ; la déclaration « limite jugée par la porte de périmètre » ne couvre que le bras, dont le journal garde la trace ; `--ref-principale` n'est pas journalisé.
- Correction : retirer l'option (références fixes `origin/main`, `main`), ou ne l'accepter que dans cette liste ; à défaut, la consigner au journal de l'outil. Ajouter l'essai.

### R2 — À trancher par la mère / à corriger : exclusion « 24 » par motif de nom encore incomplète
- `listes_lecture_v2.py` l. 42, `RX_24 = (demande|reponse)[-_ ]?24(?![0-9])`.
- Attrapés : `demande-24`, `reponse_24a`, `Réponse 24`. Non attrapés (boucle : `plein`) : `demandes-24-v1.md`, `reponses-24.md`, `demande-024`, et `docs/notes/bras-a-moniteurs-v1/reponses-sans-interne-demandes-18-19-24a-v1.md` (ma première lecture l'avait signalé ; la réponse du coordinateur ne le mentionne pas ; je ne l'ai pas ouvert). Pour la stricte, ce dernier est déjà hors liste.
- Correction : `(demandes?|reponses?)[-_ ]?(?:\d+[-_ ])*0*24` ou la liste exacte des fichiers décidée par la mère ; et décision explicite sur ce fichier.

## Remarques (non bloquantes)
- **R3** : `repere`, `sert`, `quand`, `reveil` sont bornés (chaîne de 300 signes) mais ne passent pas la garde des noms exclus (essai : `repere="consigne-privee: seuil 0.37"` et `sert="consigne-privee seuil 0.37"` → commune). La spécification ne confie la garde qu'à `nom` et `mots` ; je l'avais suggérée pour tous les champs textuels. À étendre, ou à déclarer comme laissée à la relecture de la mère.
- **R4** : `nom` ne retient pas un `lot/autre` générique (seulement `lot/compte-4`) : conforme au texte, pas de défaut.
- **R5** : `RX_COMMUNE` utilise `\d` (chiffres Unicode admis, ex. chiffres arabes) : sans effet de fuite (le fichier doit exister sous `commune/`), mais passer en `[0-9]`.
- **R6** : la dérogation D-1 reste sensible à la casse (`Liste-exhaustive-x.md` autorisé) ; `reecriture-v3/` et `questions-fond-v1/` renvoyés à la mère (déclaré).
- **R7** : en cas d'arrêt entre l'écriture du compagnon et le renommage, un compagnon orphelin bloque la relance (R12) ; à nettoyer à la main. Aucun fichier de sortie lisible n'est exposé entre-temps (`.en-cours` n'est pas autorisé).
- **R8** : l'historique git (§ 2.2.5) reste sans outil, déclaré.
