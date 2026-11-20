# Note — versement tardif des journaux du lanceur de la ligne 1 (arrêt A9) — v1

Pièce de travail (classe C), écrite par la session du compte organisme le 2026-11-20. Ne remplace rien.

- **Omission de la session** : l'addendum scellé (`c29628a0…`, § 9, point 5) voulait le journal du lanceur et `journal-etalonner.log` versés à côté des morceaux. Ils étaient restés dans le dossier de sortie hors dépôt (`/home/user/runs-banc-a-ligne1-v2/`). Le lecteur de cause l'a relevé (`compte-rendu-cause-arret-A9-ligne-1-v1.md`, `2f8f2f074f0bc8f6394e178abebeb31122b78ffea41c0d78ff0dc4024214c836`) et a déduit l'exception du code et de la sortie.
- **Versés maintenant**, copiés sans changement (empreintes égales à celles du dossier de sortie), scellés, dans `journaux-course-ligne1-v2-arret-A9-20261120/` :
  - `lanceur.log` (`a9729c836191a6fefe559e692656b9d5b1e014fc14ab12b314aac8fb3da4d6b2`) : « étape etalonner : code de retour 3 ; voir journal-etalonner.log ; chaîne arrêtée » ;
  - `journal-etalonner.log` (`30c6c9f477d17db3d036590a02309434533896aaf0a0e1b0fceba48e533d8be5`) : « ARRÊT GardeA9Etalonnage : garde A9 : porte de prise manquée (banc sans prise) : arrêt, retour à la mère » ;
  - `etat-lancement-ligne1-v2.json` (`08748499cd1c0427212ec3bd08d938f43351b5784bcb41c51ae19c8c3f8b5b74`) : début 2026-11-19T23:56:02.497218Z, étape « etalonner », code 3, 584,42 s ;
  - `heure-lancement-session-v1.txt` (`68335565aa6918d1e8466bb728c55ef6505cb26bdda2b4c69bf0606065d54910`).
- **Effet sur le compte rendu** : le message et le code de sortie confirment le déclencheur que le lecteur a déduit (garde A9, porte de prise). Rien d'autre n'en dépend. Le manifeste du versement (`acc4192e…`) ne les liste pas ; il n'est pas réécrit (R12).
