# Erratum 1 à `lecture-tarif-et-limite-kimi-v1.md` (`b1e4f3f0…`, gardée sans modification)

Écrit le 2026-11-22 vers 10:10Z par la session de l'organisme. La contre-lecture du transport réel l'a relevé (`docs/notes/organisme-essaim-communicant-v1/transport-kimi-reel-v1/contre-lecture-v1/`). Je l'ai vérifié sur les pages officielles gardées dans ce dossier.

## Ce qui était faux
Le § 2 de la v1 disait : « La page ne décrit **aucun plafond de dépense réglable** dans la console. » C'est juste pour la page lue (« Recharge and Rate Limiting »), mais **faux pour la plateforme**.

## Ce que disent les pages officielles
- `org-best-practice-2026-11-22.md` (https://platform.kimi.ai/docs/guide/org-best-practice.md), l. 193 à 201 :
  - « After creating a project, open **Project Settings** to configure its budgets and rate limits. »
  - « Monthly and daily consumption budgets | Daily and monthly budgets accumulate over the calendar day and month. When spending reaches a configured budget greater than 0, subsequent API requests for that project are rejected. Consumption statistics and limit enforcement may be delayed, and charges incurred during the delay must still be paid. »
  - L. 21 : « All projects in an organization share the organization's account balance and rate limits. »
- `project-spend-limits-2026-11-22.md` (https://platform.kimi.ai/docs/admin-api/project-spend-limits.md), l. 16 et 17 : même règle ; montants en millièmes de cent (100 000 = 1 USD) ; `null` = sans limite ; `0` = budget nul.
- `docs-llms-2026-11-22.txt` (https://platform.kimi.ai/docs/llms.txt) : index de la documentation. On y trouve aussi la liste des requêtes interrompues (`client_disconnected`) et le détail par requête, disponible à J+1 à 07:00 (UTC+8). Ces deux sources servent au rapprochement de H1 et H4.

## Lettre corrigée du § 2, pour la limite de 204 USD
1. **Projet dédié.** Le directeur crée un projet dédié à la course dans la console Kimi. Il y fait la clé de la course, et il règle dans **Project Settings → Project Budget/Rate Limit Settings** un budget **mensuel et quotidien de 204 USD au plus** (ou plus bas pour la fumée, par exemple 1 USD).
2. **Retard de l'application.** Le budget n'est pas une borne exacte : l'application peut avoir du retard, et ce qui est dépensé pendant ce retard reste dû. Il faut donc garder les deux bornes :
   - le budget du projet ;
   - un solde prépayé limité, puisque le solde est partagé entre tous les projets de l'organisation.
3. **Clé actuelle.** Le projet auquel appartient la clé `KIMI_API_KEY` actuelle n'est pas connu ici. Si cette clé sert à d'autres projets ou à d'autres courses, une clé neuve du projet dédié est préférable. Elle entrerait dans l'environnement sous un nom neuf, que le directeur choisit.
