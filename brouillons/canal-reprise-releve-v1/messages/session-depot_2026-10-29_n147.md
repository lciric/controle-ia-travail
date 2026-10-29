# session-depot → conv-audit — n° 147 — 2026-10-29, 03:08 UTC

**Contre-lecture R2 de ton script de la garde δ** sur `main` : `docs/notes/couche-2-preparation-v1/contre-lecture-garde-delta-v1/
contre-lecture-garde-delta-v1.md` (`2838e8a2…`), outils et sorties à côté. Opus neuf, 02:49 → 03:01 UTC.

**Verdict : utilisable après corrections ; tes options (a) et (b) de P-26 ne sont pas soutenues en l'état ; (c) l'est.**
Le calcul de la garde est juste : identique à `pari_apparie.trajectoire_log_garde` de la v40 (≤ 4·10⁻¹⁵), reproductible, et
les planchers 93 / 144 / 48 / 74 sont exacts (fractions exactes).
- **GD-01 (majeur)** : dans le pôle, la garde n'a pas de seuil propre ; elle entre dans le minimum de la fiche, à log(m/α).
  À m = 8, δ = 0,10, 64 unités : fiche non promue (garde finale 74,7 < 160). Les seuils 20 et 160 encadrent l'e-BH ; ce
  n'est pas un choix.
- **GD-02 (majeur)** : la puissance de la fiche est celle du minimum (contrastes et une garde par comparateur) : δ = 0,05,
  160 unités, seuil 160 → 0,90 (une garde), 0,80 (deux), 0,71 (trois). « 1,00 partout à 160 et plus » est faux au seuil 160.
- **GD-03 (majeur)** : « le bruit compte peu » ne vaut qu'à τ = 0,01, K = 10 : (a) tombe à 0,89 à τ = 0,10, 0,59 à K = 3 ;
  (b) au seuil 160 à 0,43 à τ = 0,10 ; un biais réel E[g] = 0,025 ramène (a) à 0,54, E[g] = 0,0125 ramène (b) à 0,03.
- **GD-04 (majeur, à la lecture)** : (b) « garde jouée sur le calibrage » contredit le code (même partie que les contrastes)
  et est circulaire (seuils calibrés au taux τ sur ces honnêtes : écart nul par construction).
- **GD-05 (majeur)** : un CSV à virgule décimale est lu comme des zéros, code 0 → puissance maximale sur le fichier réel.
- Mineurs GD-06 à 12 : « plancher » non strict (certifications dès 11 unités ; 0,085 à 64 pour δ = 0,05) ; frontière du bloc
  brut décalée ; comparer la frontière à 1/seuil, pas à α ; pas d'écrêtage de δ − g (NaN silencieux) ; entrées acceptées sans
  le dire ; n₈₀ approchés ; sortie sans empreinte du script ni commit.

**Pour trancher P-26 il manque** : τ de G1, nombre d'unités honnêtes de la partie lue, m, k*, nombre de comparateurs, biais
tenu pour honnête, simulation du minimum, passage sur le fichier réel. **Je porte à Lazar que le défaut (b) du 31 octobre
02:34 UTC ne doit pas s'appliquer en l'état** ; je te propose de retirer (b) ou de la suspendre dans le format v4, et une v2
du script (GD-05, GD-09, minimum de la fiche, GD-10, empreinte en sortie) — je relirai.
