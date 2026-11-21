# Addendum 1 à la contre-lecture de la consigne v4 — vérification des corrections dans la v5

- **Lecteur** : Claude Fable 5.1 (`claude-fable-5-1`), auteur de `contre-lecture-consigne-v4-v1.md` (`e10ffe24…`), même
  contre-lecteur (GO-2026-11-19-26, classe B). Heures (`date -u`) : début 2026-11-21T07:19:11Z.
- **Objet** : `consigne-poste-local-lean-d1a-v5.md`, empreinte recalculée
  `427584c7f2c32a2521ce2fa9f3685295473f4791160ac1bc4ef2e34a863245bd` ; `differentiel-consigne-v4-v5.diff`,
  `3ddad747ef408ff4fdc68f65e32f1dc379caf3c790a00c3db8c3ae28075054fe` ; les deux compagnons `.sha256` conformes.
- Lecture seule ; rien lancé, rien loué, aucun `rm`.

## Verdict (une ligne)

**Exécutable.** C1, C2 et C3 sont reprises à la lettre ; la remarque ajoutée au mandat 4 est juste ; rien d'autre ne change
hors le titre et la ligne d'en-tête de la v5.

## Contrôles

1. **Différentiel rejoué** : `diff -u v4 v5` identique au différentiel versé (hors les deux lignes d'en-tête de fichiers) ;
   le différentiel appliqué à la v4 par `patch` redonne l'empreinte `427584c7…` de la v5.
2. **C1** (Dépense, premier point) : texte de la contre-lecture repris mot pour mot (seul le retour à la ligne diffère) :
   destruction en section 5 par `MV7 detruire --identifiant N`, en section 4 par `MV7 detruire --pas d1a` (étiquettes
   fixes et nom), « toujours par l'identité de l'instance chez le loueur, jamais par un motif (R10) ».
3. **C2** (mandat 1, contrôle `ls-remote`) : « code 0 et aucune ligne ; une ligne rendue … ou un code non nul … : arrêt,
   compte rendu, aucune préparation » — mot pour mot.
4. **C3** (« Avant de lancer », point 12) : rappel personnel à `H + 1 h` et accès à la console de Hetzner pour le code 3 —
   mot pour mot.
5. **Remarque du mandat 4** (« en tâche jusqu'à ») : juste. Avec la garde d'heure limite, L1 le 30 novembre tombe entre
   00:00Z et 17:59Z ; `H − 1 h` = L1 + 45 h tombe entre le 1er décembre 21:00Z et le 2 décembre 14:59Z, toujours sous
   `création + 48 h` ; l'échéance de la minuterie et la ligne « en tâche jusqu'à » dépassent donc l'échéance du GO
   (2026-11-30) dès que L1 tombe le 30 novembre, et au plus tard le 2 décembre. La garde du code par jour UTC
   (`garde_go_v1`) ne regarde que la préparation et la création : la remarque ne contredit rien.
6. **Rien d'autre** : les cinq blocs du différentiel sont le titre (v4 → v5), la ligne d'en-tête de la v5 (sources et
   empreintes justes : v4 `834016a2…`, contre-lecture `e10ffe24…`), C3, C1, C2 et la remarque du mandat 4. Le reste de la
   v4 (donc de la v3) est inchangé.

## Remarque, sans effet

- La v5 et ses compagnons doivent être sur `origin/main` avant le lancement : la session du poste y vérifie l'empreinte de
  la consigne qu'on lui donne (mandat 1).
