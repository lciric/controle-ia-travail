# Vérification des corrections : collisionneur v9 version 8d

Écrite le 21 novembre 2026, de 21:24Z à 21:35Z (`date -u`), par Claude Opus 5.5 (`claude-opus-5-5`), le vérificateur qui a écrit `verification-collisionneur-v9-v8c-opus-v1.md` (`a0ff6a76…`), relue en entier, surtout sa section 8. Pièce d'instrument (classe B) : vérification des corrections par le même contre-lecteur.

Ce que je n'ai pas fait :
- aucun envoi réel ;
- aucune clé lue : essais sous `env -u` des sept clés ;
- aucun commit ;
- aucun fichier du dépôt modifié, hors cette pièce et son sceau.

Mutations et contrôle sur des copies, dans mon bloc-notes.

## Verdict

**Conforme.**
- C-1 et C-2 sont portées aux textes exacts de ma section 8, au caractère près.
- Rien d'autre ne change que l'en-tête, `VERSION`, les lignes d'emploi, le chemin des essais et l'essai qui lit la version.
- La garde v3 est inchangée.
- Essais rejoués sans clés : 405 passés, 1 sauté.
- Mes mutations M1 et M2 sont prises toutes les deux. M2, qui survivait à la v8c, est prise par l'essai témoin neuf.

## 1. Empreintes

Recalculées par `sha256sum`. Chacune est égale à son compagnon `.sha256` et au préfixe donné par la mère.

| fichier | empreinte |
|---|---|
| `docs/notes/collisionneur-v9/verification-collisionneur-v9-v8c-opus-v1.md` | `a0ff6a766415c3ac772a3738622a21e7ca2e44d355f2c23713c2246dd9d112e8` |
| `docs/notes/collisionneur-v9/collisionneur_v9_v8d.py` | `b780383874598f12b24c79e4087d335c8e01cda685e295f5116898fa3b1715ac` |
| `docs/notes/collisionneur-v9/test_collisionneur_v9_v8d.py` | `6c2204f1c5c5126a23a57ee41160a6932f87f627c35eef1aac115de270230841` |
| `docs/notes/collisionneur-v9/rapport-developpeur-collisionneur-v9-v8d-v1.md` | `ee277e45db81ad4fc63d5cb3abf799d582ec7a5f7df14d298c4ddcd055d12aba` |
| `src/controle_ia/garde_google_v3.py` (inchangée) | `923679b51cfc84b65ff7cfc65296378d08e6d4e64f6b427823d23ba24f4afe91` |
| `tests/test_garde_google_v3.py` (inchangé) | `aceabdb2b35ec62fedf982281b1de76a6a02f651ff5cfa3391831e05825a122a` |
| pour comparaison : `collisionneur_v9_v8c.py` (intact) | `a3fc279ed1754db250016131656671d0639d03749bc62dff88b99a2b72b5b531` |
| pour comparaison : `test_collisionneur_v9_v8c.py` (intact) | `f7136092c5d76533227dff87c9403eb29f33cb803377497f0f999bf524274f7e` |

## 2. Différences de la v8c à la v8d

J'ai comparé les fichiers par `diff`, sur le script puis sur les essais. Je les ai aussi comparés à ma copie corrigée de la vérification précédente (`fbdba2ca…`). Il ne reste que les seules différences attendues.

**Script.**
- L'en-tête gagne un paragraphe v9-v8d, de six lignes de commentaire.
- Les sept lignes d'emploi passent de `collisionneur_v9_v8c.py` à `collisionneur_v9_v8d.py`.
- `VERSION = "collisionneur-v9-v8d"`.
- C-1 est portée en trois lieux, chacun au texte exact de ma section 8 :
  - `devis` : la phrase « jusqu'au double » est remplacée ;
  - `pire_tours_2_3` : le commentaire C-1 est ajouté, avec `relances = 2 if m["fournisseur"] == "gemini" and reglage_de_relance(m)[1] else 1`, `pire + relances * relance` et le champ `"relances"` ;
  - `devis_reprise` : « si chaque cellule épuisait ses relances (deux chez une espèce de Google à plafonds égaux… ».
- Aucune autre ligne ne change.

**Essais.**
- La docstring de tête est préfixée ; l'en-tête des essais v8c y reste inchangé.
- La ligne de lancement, `CHEMIN` et le nom du module chargé passent à la v8d.
- L'assertion de `VERSION` dans l'essai qui la lit passe à la v8d.
- Deux essais sont ajoutés en fin de fichier : `test_opus_c1_devis_avec_relances_compte_deux_relances_chez_google` et `test_opus_m2_plancher_de_texte_en_appel_non_diffuse`. Leur texte est celui de ma section 8 ; seul le bandeau de commentaire qui les précède diffère de ma copie.
- Aucun essai existant n'est changé.

## 3. Essais rejoués

De 21:24:51Z à 21:25:29Z, `--basetemp` neuf dans mon bloc-notes :

```
env -u OPENAI_API_KEY -u OPENAI_API_KEY_2 -u GEMINI_API_KEY -u GEMINI_API_KEY_2 -u GEMINI_API_KEY_3 -u GEMINI_API_KEY_FREE -u MISTRAL_API_KEY PYTHONPATH=src timeout 1500 .venv/bin/python -B -m pytest -q docs/notes/collisionneur-v9/test_collisionneur_v9_v8d.py tests/test_garde_google_v3.py -p no:cacheprovider --basetemp=…/verif-v8d-opus/basetemp-temoin -rs
```

**405 passés, 1 sauté, en 37,81 s** (code 0).
- Cela fait 361 et 44, les comptes du développeur : les 359 de la v8c, plus mes deux essais.
- Le sauté est la copie « dopamine », non désignée (`COPIE_RUN_DOPAMINE`).

## 4. Mutations M1 et M2 rejouées

L'outil est celui de la vérification précédente. Seules les suites visées passent à la v8d (outil `mutations_garde_v3_opus_v8d.py`, `2211238b…`). Chaque mutation est faite sur une copie de la garde v3, dans un dossier neuf. Les deux suites tournent entières sur la copie (`-o pythonpath`), sans clés, avec arrêt au premier échec. L'empreinte de la garde scellée est vérifiée avant et après.

| mutation | résultat | premier essai en échec | prise |
|---|---|---|---|
| témoin, sans mutation | 405 passés, 1 sauté | aucun | témoin sain |
| M1 : limite de mots comparée au plafond entier (`>= plafond` au lieu de `>= texte`) | 1 échec après 296 passés | `test_v8_garde_reglages_sain_pour_le_catalogue[carbon]` | oui |
| M2 : plancher de 16 000 contrôlé en flux seulement | 1 échec après 360 passés | `test_opus_m2_plancher_de_texte_en_appel_non_diffuse` | **oui** (non prise sur la v8c) |

**Contrôle de C-1.** Sur une copie de la v8d, j'ai rétabli la ligne de la v8c : `totaux["avec_relances"] += pire + relance`. La copie a l'empreinte `e3ad3fd8…`. Elle se lance avec `DEPOT_COLLISIONNEURS` pointé sur le dépôt, pour que la copie lise la branche des journaux.
- L'essai C-1 échoue sur `assert 34.985408 == 42.559124`.
- Ce sont les chiffres du dossier « percée » de ma section 6 : 34,99 et 42,56.

L'essai C-1 tient donc le défaut qu'il vise.

## 5. Remarques (non bloquantes)

1. **Commentaires anciens.** Les commentaires de ma remarque 1 restent tels quels dans la v8d :
   - ligne 414, « × 1,6 » ;
   - lignes 85 et 1096, « garde_google_v1.py » ;
   - ligne 1809, « relancés une seule fois » ;
   - ligne 1815, « l'unique relance » ;
   - ligne 1914, « Au plus deux essais » ;
   - l'écran « relance corrigée » pour une relance identique.

   Je n'avais pas donné de texte exact. Le développeur les a donc laissés en réserve, et il le déclare. C'est conforme à la consigne « seuls C-1 et C-2 changent ». À accorder dans la prochaine version qui touchera ces lieux. Aucun n'agit sur un envoi.
2. **Mes remarques 2 à 9 restent ouvertes**, telles qu'écrites dans `a0ff6a76…` et reprises par le développeur. Avant tout appel, ma section 10 vaut toujours, sauf son point 1, maintenant rempli :
   - essai réel d'un envoi par modèle de Google ;
   - mesure de Neon ;
   - `verifier` avant et après, pour chaque dossier.
3. **Témoin de la série du développeur.** Il annonce 402 passés, 3 sautés et 1 désélectionné, contre 405 passés et 1 sauté sous la commande donnée. L'écart tient sans doute à son outil, qui lance dans un dossier temporaire où la branche des journaux n'est pas trouvée. Je ne l'ai pas vérifié, et cela ne change pas ma lecture : mon témoin et mes mutations tournent sur les suites entières.
4. **Mutations du développeur.** Je n'ai pas rejoué sa série de 64 mutations (outil `dev-v8/outils/mutations_v8d.py`). Je n'ai rejoué que mes mutations M1 et M2 et le contrôle de C-1.

## Limites

- Aucun appel réel.
- Mes outils sont dans mon bloc-notes, non durable :
  - `/tmp/claude-0/-home-user-controle-ia-travail/2eb82089-3810-5ff8-881f-da5f24b622eb/scratchpad/verif-v8d-opus/outils/mutations_garde_v3_opus_v8d.py` (`2211238b…`) ;
  - la copie de contrôle de C-1 `/tmp/claude-0/-home-user-controle-ia-travail/2eb82089-3810-5ff8-881f-da5f24b622eb/scratchpad/verif-v8d-opus/controle-c1/docs/notes/collisionneur-v9/collisionneur_v9_v8d.py` (`e3ad3fd8…`).
