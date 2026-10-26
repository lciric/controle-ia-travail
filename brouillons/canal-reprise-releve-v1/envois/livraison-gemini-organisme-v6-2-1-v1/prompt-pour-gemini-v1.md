Gemini, voici la dernière version de l'organisme « la Fusée » : la v6.2.1, c'est-à-dire ta v6.2 (commit 3bbb78c1991baf17feb421529fa1957be7edec59) avec quatre corrections C-14 à C-17 faites par la lignée conv-audit sur mon accord. Va la chercher toi-même dans le dépôt, vérifie-la, lis-la, et ne modifie rien.

Tout est sur GitHub, dépôt privé lciric/controle-ia-travail (tu y as déjà poussé tes versions). Fais ceci dans PowerShell, depuis ton clone du dépôt :

```powershell
git fetch origin canal/conv-audit-organisme-v6-2-1 canal/conv-audit-n04
# 1) l'organisme v6.2.1 au commit exact, dossier organisme/ seul (26 fichiers)
git cat-file -t 7ea32705c5437d91ed071dd95fb3209bb0b0035e        # doit répondre : commit
New-Item -ItemType Directory -Force -Path .\recu-v6-2-1 | Out-Null
git archive 7ea32705c5437d91ed071dd95fb3209bb0b0035e organisme/ -o .\recu-v6-2-1\organisme-v6-2-1.tar
tar -xf .\recu-v6-2-1\organisme-v6-2-1.tar -C .\recu-v6-2-1
# 2) la note et la liste d'empreintes de la livraison (branche canal/conv-audit-n04, commit ca5857e)
git show ca5857e28a393458548dfbd2246bcc9c3a3f233e:brouillons/canal-reprise-releve-v1/envois/livraison-gemini-organisme-v6-2-1-v1/LISEZMOI-pour-gemini-v1.md | Out-File -Encoding utf8 .\recu-v6-2-1\LISEZMOI-pour-gemini-v1.md
git show ca5857e28a393458548dfbd2246bcc9c3a3f233e:brouillons/canal-reprise-releve-v1/envois/livraison-gemini-organisme-v6-2-1-v1/EMPREINTES-organisme-v6-2-1-v1.txt | Out-File -Encoding utf8 .\recu-v6-2-1\EMPREINTES-organisme-v6-2-1-v1.txt
# 3) vérification : chaque fichier de organisme/ a l'empreinte attendue (26 lignes « organisme/… » de la liste)
Set-Location .\recu-v6-2-1
Get-Content .\EMPREINTES-organisme-v6-2-1-v1.txt | Where-Object { $_ -match '^([0-9a-f]{64})\s+(organisme/.+)$' } | ForEach-Object {
  $attendu = $Matches[1]; $chemin = $Matches[2]
  $calcule = (Get-FileHash -Algorithm SHA256 -Path $chemin).Hash.ToLower()
  if ($calcule -eq $attendu) { "OK      $chemin" } else { "ECART   $chemin" }
}
Set-Location ..
```

Attendu : 26 lignes « OK », aucun « ECART ». Si un seul écart apparaît, arrête-toi et dis-le-moi, sans rien utiliser.

Ensuite :
1. Lis `LISEZMOI-pour-gemini-v1.md`, puis `organisme/CORRECTIONS-v5.md` (les quatre corrections, leurs essais `tests/test_corrections_v5.py`, l'essai hérité adapté et pourquoi), et le code corrigé dans `organisme/principal.py`. `CORRECTIONS-v1.md` à `v4.md` (C-01 à C-13) valent toujours.
2. Confirme-moi en quelques lignes : les 26 fichiers vérifiés, l'empreinte d'arbre `4f13647a7070b3941b660d60c428620df6b4e0e31cea1d2c63d71b8606e6214d` (si tu disposes du noyau à `8e5e2f7b`, par `essaim_m3.noyau.boucle.empreinte_arbre` ; sinon les 26 empreintes de fichiers suffisent), et ce que tu comprends de chaque correction.
3. **Toute version suivante (v6.3) part de cette v6.2.1**, garde `CORRECTIONS-v5.md` et ses essais, déclare ce qu'elle change et pourquoi, sur une branche à part, sans aucune clé, avec ses essais ; tu ne retouches pas C-14 à C-17 sans le dire explicitement.

Ce paquet ne contient aucun score : ceux de la part finale ne sont servis à aucun organisme ; ceux de la part `test` seulement sur ma décision.
