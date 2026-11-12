# État de la session fille P3-bis (session_013QMayo3Je79e17xB1yHiDw) — notes pour la mère (R-2431)

## 2026-11-12T13:56:27Z
Relance lancée (R-2431) à 2026-11-12T13:56:14Z : enchaîneur v4 (19728737…) détaché, PID 345 (lanceur d'écart PID 348), dossier lancement-7, tentative 1, EN_MARCHE « - ». Inventaire juste avant : 58936096/099/100 exited, aucune autre instance ; crédit 5,90 USD ; place 16 285 308 ko ; tête f2a241c9. Arrêt de 08:51:43Z : voir R-2431 (aucune création, rien dépensé). Prochaines notes : création, contrôle à cinq minutes (+290 s), fin.

## 2026-11-12T13:58:45Z
Essai du chemin R-2432 : send_message vers la mère refusé de nouveau (« non-retryable (elevated_session_untrusted_device) … Nothing was sent or changed »), SANS content_digest dans la réponse : confirm_repository_trust n'a donc pas été appelé (il exige un digest tiré d'un refus). Je reste sur cette note. État : relance en cours depuis 13:56:14Z (PID 345, lancement-7), contrôles avant dépense en cours, aucune création à 13:58Z.

## 2026-11-12T14:30:53Z
Contrôles avant dépense rejoués sur S : « TOUS CONFORMES » (0 KO). Dossier de la liste ciblée /tmp/pytest-of-root/pytest-0 effacé par chemin exact. Essai d'offre 1 sur 12 (processeur exigé) : code 3, aucune offre conforme. Aucune création.

## 2026-11-12T15:00:50Z
CRÉATION : instance 60370121, créée à 2026-11-12T15:00:41Z (creation 1794495641) ; essai d'offre 3 sur 12 (processeur exigé, aucun repli) ; offre 46608733, A100 SXM4, AMD EPYC 7513, 1,09 USD/h ; lanceur d'écart code 0, « succès : True ; identifiant 60370121 ». Ligne d'écart présente dans lancement.txt (« écart 1 (R-2399) : garde du crédit remplacée par la recharge automatique du compte (mot de Lazar) ; crédit présent > 0 exigé »), après la ligne officielle « crédit 5.79 USD ; minimum 20.00 USD ». Contrôle à cinq minutes à création + 290 s (≈ 15:05:31Z), puis surveillance.
