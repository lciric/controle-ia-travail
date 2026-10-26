Gemini, voici l'analyse par la lignée conv-audit (Claude) de ta méta-conception v6.3 et de ton relais des 18 générations (commit 5512513). Elle est sur GitHub, dépôt privé lciric/controle-ia-travail, branche à part canal/conv-audit-pour-gemini-meta-conception-v1 (commit ce22a89dd232c9e1f769932d011620626dde4730). Va la chercher, vérifie-la, lis-la en entier, et ne modifie rien sur cette branche.

Dans PowerShell, depuis ton clone du dépôt :

```powershell
git fetch origin canal/conv-audit-pour-gemini-meta-conception-v1
git cat-file -t ce22a89dd232c9e1f769932d011620626dde4730        # doit répondre : commit
New-Item -ItemType Directory -Force -Path .\recu-relecture-v6-3 | Out-Null
git archive ce22a89dd232c9e1f769932d011620626dde4730 pour-gemini/ -o .\recu-relecture-v6-3\pour-gemini.tar
tar -xf .\recu-relecture-v6-3\pour-gemini.tar -C .\recu-relecture-v6-3
Set-Location .\recu-relecture-v6-3\pour-gemini
Get-Content .\EMPREINTES-v1.txt | Where-Object { $_ -match '^([0-9a-f]{64})\s+(.+)$' } | ForEach-Object {
  $attendu = $Matches[1]; $chemin = $Matches[2]
  $calcule = (Get-FileHash -Algorithm SHA256 -Path $chemin).Hash.ToLower()
  if ($calcule -eq $attendu) { "OK      $chemin" } else { "ECART   $chemin" }
}
Set-Location ..\..
```

Attendu : 9 lignes « OK », aucun « ECART ». Au moindre écart, arrête-toi et dis-le-moi.

Ensuite :
1. Lis `RAPPORT-CONV-AUDIT-POUR-GEMINI-META-CONCEPTION-V6-3-v1.md` en entier, puis `ADDENDUM-retrodiction-v1.md` (résultat du test sur la littérature réelle), puis les pièces sous `pieces/` (les chiffres viennent d'essais rejouables, scripts sur la branche canal/conv-audit-n04).
2. Réponds-moi en quelques lignes : ce que tu acceptes, et ce que tu contestes — chaque contestation avec le chiffre qui la fonde et un test qui pourrait échouer, pas un argument d'autorité.
3. Si ta version de travail contient `_score_pertinence_texte` et le calcul de Cholesky ou de log-déterminant dans `mitose_spectrale.py` (absents de la v6.2.1), pousse-la telle quelle sur une branche à part, sans clé : les briques seront retestées sur ce code.
4. Pour une v6.3 : pars de la v6.2.1, suis le § 5 du rapport, déclare chaque changement, sur une branche à part, avec essais ; et remplace partout le sigle du financeur par « programme » dans les noms de dossiers et les textes.
