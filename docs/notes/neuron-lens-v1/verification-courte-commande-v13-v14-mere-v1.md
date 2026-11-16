# Vérification courte du différentiel v13 → v14 de la commande du volet A (« Neuron Lens »)

Date : 2026-11-14 16:50 UTC (`date -u`). Lecteur neuf. Référence `refs/remotes/origin/prep/neuron-lens-v1`, tête `e1ada56f`.
v14 : `14fe638334ece83a5f5f6927b49e1e1aaea2a74953b6f3747ba01c76bd1eb26a` (empreinte recalculée, conforme).
Lu : différentiel v13/v14 (7 hunks), contre-lecture 13 (retouches T-1 à T-6, T-8), v14 entière (destructions, étape 3), lignes R-2788, R-2789 et GO-2026-11-14-05 (existence et contenu pertinent). Non lus (hors périmètre) : les scripts de minuterie v3, de garde v4 et de suivi v6.

## Verdict : conforme avec mineurs
Aucun constat bloquant ni majeur. Le passage v13 → v14 n'est que du texte (en-tête, renvois, cellules de table, deux lignes d'empreintes) ; aucune commande, borne, arrêt ni consigne de sécurité n'est modifié.

## Retouches
| Retouche | Appliquée ? | Constat |
|---|---|---|
| T-1 (secrets avec `"`, `\`, saut de ligne, tabulation non reconnus par le balayage) | oui, limite déclarée | En-tête l.8-10 et réserve l.38-39 ; code inchangé, comme la contre-lecture l'autorisait (« ou déclarer la limite »). Le relevé « quatre secrets, `[A-Za-z0-9_-]` seulement » vient de la note de la session de reprise de la contre-lecture 13, pas d'un relevé refait ici (non vérifiable sans lire l'environnement). |
| T-2 (puce « toute destruction » cite minuterie v2) | oui | l.47-49 : « minuterie **v3** », script `…_v3.sh`, « essai v3 ». Le reste de la puce est inchangé. |
| T-3 (« écrit partout » faux, cinq cellules « aussitôt ») | oui | Les cinq cellules (l.244-248) portent « selon l'étape 13 » ; l.21 corrigée en « aux étapes 7 et 8 … (et, en v14, dans la table) ». Les deux autres occurrences de « aussitôt » (l.191, minuterie « posée aussitôt ») sont sans rapport. |
| T-4 (62 → 67 essais ; « v4 » → « v5 ») | oui | l.56 « à la place de la v5 (67 essais) ». Aucun « 62 essais » ni suivi v4/v5 d'emploi ne subsiste dans le texte courant (les v4/v5 restent seulement dans le tableau d'empreintes, pièces archivées). |
| T-5 (minuterie v3 : liste non vide sans témoin → code 6 sur une destruction réussie) | oui, réserve | l.37-38 : fausse alerte possible, tranchée à la main à l'étape 13. L'étape 13 prévoit déjà le cas « plus aucune instance » (`absente <ID>` sur `[]`, et le dire). |
| T-6 (`_derniere`, dernière ligne seule balayée) | oui, limite déclarée | Même texte que T-1 (l.8-10, l.38-39). Code inchangé. |
| T-8 (info : garde v4 sans import de suivi) | consigné | En-tête l.11 ; reprend la note de la session de reprise, non revérifié ici (script non lu). |

## Destructions dans la v14 entière
| Étape | `-y` | Preuve d'absence |
|---|---|---|
| 6 (échec de création, l.189) | oui : `vastai destroy instance <ID> -y < /dev/null` | oui : `suivi_vast_v6 absente <ID> --temoin <témoin>`, code 0 exigé, relancer sinon |
| 7 (minuterie, l.197-203) | porté par le script v3 (non lu) ; si non armée : renvoi à l'étape 13 | prouvée par la minuterie v3 (liste non vide, `--non-vide`, code 6 sinon) selon l'en-tête ; non revérifié dans le script |
| 8 (garde, l.212-213) | porté par la garde v4 (non lue) ; en repli : renvoi à l'étape 13 « avec `-y` et absence prouvée » | « vérifiée à 90 % », code 4 si échec ; mécanisme dans le code non lu |
| 13 (fin, l.262-264) | oui : `vastai destroy instance <ID> -y < /dev/null`, avec la note « sans `-y`, abandon en silence, code 0 » | oui : `absente <ID> --temoin …`, code 0 exigé ; replis `--non-vide` ou liste `[]` énoncés |
| Table de destruction (l.244-248) | renvoi à l'étape 13 | idem étape 13 |
Aucune autre destruction trouvée (les autres occurrences de « destroy »/« détruire » sont de l'histoire ou des renvois). Aucune destruction sans `-y` ; aucune tenue pour faite sur le seul code de sortie. Mineur : le texte l.213 (« destruction réessayée et vérifiée ») ne dit pas `-y` ; il repose sur le code de `garde_depense_v4.py`, que la v14 dit passer `-y` (l.28-29, écart de docstring déclaré). Non vérifié ici faute de lecture du script.

## Étape 3 (l.154-157)
Conforme : exige `can_pay` vrai, `has_billing` vrai, `billing_failed` faux, « un champ absent ou nul vaut arrêt », sinon arrêt avec message à la mère ; seuls les champs listés sont imprimés. Cohérent avec R-2788 (mot direct de Lazar « vast se recharge seul go », même condition). Plafond 10 USD, échéance 30 novembre et exigence d'un feu écrit de la mère de GO-2026-11-14-05 : inchangés (l.114 ; seule la citation « cette v14 » change).

## Hunks du différentiel
| Hunk | Expliqué ? |
|---|---|
| 1 (titre « v14 » + paragraphe d'en-tête) | oui (T-1 à T-6, T-8 ; déclare l'absence de relecture après coup) |
| 2 (l.21 : S-3 précisé) | oui (T-3) |
| 3 (réserves T-5, T-1/T-6) | oui |
| 4 (puce « toute destruction » : v2 → v3) | oui (T-2) |
| 5 (« v5 », « 67 essais ») | oui (T-4) |
| 6 (« cette v13 » → « cette v14 » dans la phrase du feu) | oui, nécessaire (le feu cite la version et ses empreintes) |
| 7 (cinq cellules de la table) | oui (T-3) |
| 8 (deux lignes d'empreintes ajoutées : contre-lecture 13, v13 archivée) | mineur : non annoncé dans l'en-tête, mais bénin (références, empreintes citées) ; empreintes non recalculées ici |

## Réserves de ce lecteur
- Non vérifié : les empreintes de la contre-lecture 13 et de la v13 inscrites au tableau (hors périmètre de lecture) ; le contenu des scripts v3 et v4 et du suivi v6.
- Les retouches ne changent ni fond, ni bornes de dépense, ni arrêts, ni sécurité.
