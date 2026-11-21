# Contre-lecture externe de la réponse de Fable aux méthodes de mathématiques nouvelles par Carbon et Astra — synthèse — v1

- **Nature** : pièce de travail (classe C). Écrite par Claude Opus 5.5 (sous-agent de la session mère), le 21 novembre 2026 vers 11:40 UTC, sous GO-2026-11-21-38 et -39.
- **Verdict** : **aucune contre-lecture reçue.** Les deux appels ont échoué sans rendre de texte ; aucune remarque n'est donc à juger sur pièce. Conformément au mandat (« si un appel est refusé ou si le script refuse, s'arrêter et le dire ; pas de contournement »), aucun appel n'a été relancé, le script n'a pas été modifié, aucun réglage n'a été baissé.

## Ce qui a été envoyé

Version servie neutre `note-servie-v1.md` (`b656ac3bb67d11af284fc61cc380654a9c27241f14830138dd342181d7424827`), passée à la garde de motifs du collisionneur v9 v3 (liste vide), scellée avant envoi. Script employé, lu avant lancement : `docs/notes/papier-dopamine-moniteur-v1/approfondissement-v1/appel_modeles_externes_v3.py` (`8aee878d0cc0c46e9cc6443dbb749a1f450389f093650610ab13c819ba52af8e`, empreinte vérifiée), le même que pour les réponses externes du brainstorm. Clés lues par leur nom seulement.

## Ce qui est revenu

| modèle | réglage | issue | jetons (entrée / sortie et réflexion) | durée | coût |
|---|---|---|---|---|---|
| Gemini 4 Carbon (`gemini-4-carbon`, servi tel quel) | réflexion « high », la plus haute du script | fin `MAX_TOKENS` : les 32 000 jetons du plafond de sortie du script ont été pris par la réflexion ; **aucun texte de réponse** ; le script sort en échec, sans fichier de réponse | 11 336 / 32 000 | 424,9 s | prix haut du script 0,6853 USD ; **0,3427 USD au prix public du jour** (2 USD le million en entrée, 10 en sortie, réflexion comprise, jusqu'au 30 novembre ; page versée sous `docs/sources/pdf/mathematiques-nouvelles-methodes-v1/verification-memoire-v1/prix-du-jour/`) |
| GPT-6.2 Astra (`gpt-6.2-astra`) | effort « xhigh », mode d'arrière-plan | statut final `failed` après 22,1 s ; usage déclaré nul ; le script ne garde ni l'identifiant de la réponse ni le message d'erreur : **la cause n'est pas connue** (refus du fournisseur, erreur de service ou autre : non établi) | 0 / 0 | 22,1 s | 0 USD déclaré par l'usage rendu |

Coût réel des deux appels : **≈ 0,34 USD** au prix public du jour (0,69 USD au prix haut du script), sous le plafond de 4 USD par appel.

## Ce que la mère pourrait décider (rien n'est engagé)

1. Carbon : l'échec vient du plafond de sortie du script (32 000), non d'un refus ; une nouvelle version du script (plafond plus haut ou réflexion bornée) serait une pièce d'instrument à contre-lire, puis un nouvel appel sous le même GO si son plafond le permet.
2. Astra : relire l'issue de la réponse côté fournisseur demande son identifiant, que le script v3 ne garde pas ; une version qui journalise l'identifiant et le champ d'erreur permettrait de savoir s'il s'agit d'un refus.
3. À défaut, la contre-lecture peut être confiée à un sous-agent neuf d'une autre lignée, selon la règle des pièces de classe C (aucune contre-lecture requise).

## Fichiers

- `appel-carbon-contre-lecture-v1.json`, `appel-carbon-contre-lecture.log` ; `appel-astra-contre-lecture-v1.json`, `appel-astra-contre-lecture.log` (même dossier, scellés).
