# Brief de reprise d'une session mère neuve, sur un autre compte — 2026-11-18, version 1

Écrit par la session mère sortante `session_01XJ6Mgr8BN6UanALsQatc5E`, à la demande de Lazar (vers 10:40Z). Passation qui
va avec : `registres/passations/2026-11-18-1045.md`.

## A. Avant d'ouvrir la session (gestes de Lazar sur le nouveau compte)

1. **Dépôt** : la session doit s'ouvrir sur `lciric/controle-ia-travail` (privé), pour que le crochet de garde de calcul
   `.claude/hooks/garde_calcul.py` se charge (il ne se charge que depuis le dossier d'origine du dépôt de travail). Le compte
   neuf doit avoir l'accès GitHub à ce dépôt, et à `lciric/ideation-organism` pour le clone épinglé de l'orchestrateur
   (relais Claude). **Jamais** `lciric/controle-ia` (copie publique expurgée).
2. **Variables d'environnement**, par leur nom seulement, à recopier dans l'environnement du compte neuf (valeurs jamais
   tapées dans une conversation) : `VAST_API_KEY`, `HCLOUD_TOKEN`, `CONTROLE_IA_GITHUB_TOKEN_2`, `HF_TOKEN`,
   `RR_ANTHROPIC_API_KEY_RIGAUD`, `RR_ANTHROPIC_API_KEY_MINUIT`, `GEMINI_API_KEY`, `OPENAI_API_KEY`, `KIMI_API_KEY` ; et, si les
   sessions sœurs y migrent aussi, les autres variables de l'environnement actuel. Accès réseau : celui de l'environnement
   actuel (sans restriction).
3. **Modèle** : Opus 5.5 (Fable est épuisé jusqu'au 22 novembre 02:00 UTC sur le compte sortant).

## B. Texte de lancement à coller dans la session neuve

> Tu es la **session mère** du programme « Contrôle boîte blanche des menaces diffuses » de Lazar (directeur). Dépôt de
> travail `lciric/controle-ia-travail`. Le `CLAUDE.md` t'est chargé : français, tutoiement avec Lazar, quasi aucun sigle seul,
> règles gelées R1 à R14, hiérarchie de décision, interdits.
>
> 1. Fais la **routine de reprise R14** (empreintes de lancement, arbre d'empreintes, `registres/etat.md`, dernière passation
>    par nom, défauts échus, inventaire des instances du loueur et des serveurs de l'hébergeur allemand en lecture seule,
>    essais).
> 2. Lis **`registres/passations/2026-11-18-1045.md`** en entier, puis `docs/procedures/brief-reprise-nouvelle-mere-2026-11-18-v1.md`
>    et `docs/procedures/orientation-sessions-v1.md`.
> 3. **Inscris-toi** au registre des décisions sous **R-3284**, avec ton identifiant de session (outil `get_session`) ; commite,
>    recopie la branche sur `main`, pousse. La mère sortante arrête sa relève horaire dès qu'elle voit cette ligne.
> 4. **Avant 2026-11-18T22:59:59Z** : lance l'**opérateur de l'étape B bis au premier plan** (sous-agent, pas en arrière-plan),
>    qui joue à la lettre le feu en vigueur `registres/t07-etape-b-bis/feu-bbis-v7.txt` (`9b41b040…`, R-3268) depuis un tour
>    neuf, avec préavis d'une ligne à Lazar : la demande d'approbation de la commande de création (geste 14) doit s'afficher à
>    Lazar, qui l'approuve lui-même (R-3272, R-3282). Puis rappels, suivi horaire et destruction par toi.
> 5. Ensuite : **course d'auto-conception** (GO-2026-11-18-20 et -21), selon la passation § 2, point 2.
> 6. Règles du jour : aucun GO inscrit sur un mot rapporté par une autre session ; jamais contourner un refus de l'outil de
>    sécurité ; un sous-agent à la fois (régime sobre) ; cloisonnement tenu (aucun résultat de 7a, 7b, T0.6, étape B, étape
>    B bis, P3-bis ; sujets des organismes saboteurs discrets et du bras d'attaque par nom et état seulement).
>
> Écris à Lazar seulement pour un prononcé, une réserve, une divergence, une demande de GO ou une dépense ; verdict d'abord.

## C. Ce que la session neuve ne peut pas faire depuis un autre compte

- Écrire aux sessions sœurs par la messagerie entre sessions, ni les lister : elles sont sur le compte sortant. Coordination
  par le dépôt (registres sur `main`, passations des sessions sous `docs/notes/…`) et par Lazar, ou réouverture des sessions
  sœurs sur le compte neuf avec leur propre brief.
- Lire les tâches programmées du compte sortant (relève `trig_01AN1YMoyGXxyjWLUBvPHMG7`, filet déjà tombé) : elle pose les
  siennes.
