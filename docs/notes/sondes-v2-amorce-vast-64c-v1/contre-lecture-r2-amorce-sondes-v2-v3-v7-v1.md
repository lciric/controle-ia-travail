# Contre-lecture R2 et vérification (classe B) — amorce Vast.ai 64+ cœurs sondes v2 (v3 -> v7)

- Date (UTC) : 2026-11-26
- Accords : GO-2026-11-24-02, GO-2026-11-24-49, GO-2026-11-25-07
- Pièce initiale relue : `amorce-sondes-v2-v3.sh` (`a092c8bdf4e62d79e8083c26c517628f6196a0f41299209e3460cb3dfa600660`)
- Pièce finale vérifiée : `amorce-sondes-v2-v7.sh` (`ce537b64b91c312fa7836f48d9e3af0f517c293bb2920916306305ed27cd684e`)
- Suite d'essais R5 : `test_amorce_sondes_v2_r5_v10.py` (`be2c1ce0275ef0b00bacc47bf90066f2c80e0df21a9c0def87fd38d866a7ea6f`) — 100 % passés (`rc=0`)

## Constats levés et vérifiés
1. **CLB-01 (majeur, R-3661)** : sauvegarde automatique (`partiel-erreur-rc`) avant autodestruction en cas d'arrêt hors minuterie.
2. **CLB-02 (moyen, GO-2026-11-25-07)** : garde `MIN_WORKERS` paramétrable (`64` exigé en production) et `N_WORKERS` explicite.
3. **CLB-03 (moyen, GO-2026-11-25-07)** : minuterie interne abaissée à `20700` s (`5 h 45`, sous la coupure dure de `6 h`).
4. **CLB-04 (mineur, R12)** : verrou `.amorce_deja_lancee` contre tout redémarrage du conteneur et écriture binaire LF stricte (`write_bytes`, `core.autocrlf=false`).

## Verdict
**CONFORME POUR LANCEMENT SOUS GO-2026-11-25-07**.
