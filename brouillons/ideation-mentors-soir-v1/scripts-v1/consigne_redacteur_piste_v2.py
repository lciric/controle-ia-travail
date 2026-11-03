"""v2 : quinzième argument = numéro de version des fichiers écrits par le rédacteur. Fabrique la consigne d'un rédacteur neuf à piste fixée par la règle gelée (mentors du soir, Kirchner Q2 en modèle)."""
import hashlib, sys, json
R = '/home/claude/controle-ia-travail/'
def h(p): return hashlib.sha256(open(p if p.startswith('/') else R + p, 'rb').read()).hexdigest()
slug, mentor, lignes_q, question, lignes_r, limite, rapport, dossier, choix_p, groupes_md, classement_md, coord, extra, sortie_consigne, vers = sys.argv[1:16]
commun = open(R + 'brouillons/reprise-conv-audit-2026-11-02-nuit/prompts-sous-agents/redaction-finale-jang-feng-v1.md').read()
bloc = commun[commun.index("- Affirmations déjà vérifiées"):commun.index("- Deux idées candidates")]
choix = json.load(open(choix_p))
t = f"""Tu es un **rédacteur neuf** d'une réponse de Lazar Ciric au formulaire Pivotal (dépôt ce soir, 23:00 UTC). Tu n'as écrit aucune version de ses réponses. Notes en français, sans sigle non développé ; la réponse elle-même en anglais ; toute heure vient de `date -u`. Vise **40 minutes**.

## La question
- Mentor : **{mentor}** ; question (texte exact, `{R}brouillons/candidature-pivotal-v16/formulaire-site-colle-par-lazar-2026-11-03-1209.txt`, {lignes_q}) : « {question} » ; {limite}.

## Les règles de Lazar (mots du 3 novembre, heure de Paris)
- 13:05 et 13:06 : « on sélectionne d'abord la piste la plus fructueuse, les arguments les plus forts et les plus fertiles, on repart de zéro, page blanche, je ne veux pas de ma réponse générique » ; « jamais de structure préétablie ».
- **Sa réponse actuelle** (même fichier, {lignes_r}) n'est qu'un réservoir de faits : ni sa structure, ni son ordre, ni ses phrases.

## La piste est déjà choisie (règle gelée ; tu ne la changes pas)
- Un rapport d'idées (tour d'un collisionneur de quatre modèles, fiches du matin, moisson de nouveauté, classement par paires) a donné des fiches, groupées à l'aveugle. La règle gelée choisit le groupe **« {choix['piste']} »**. Lecture de contrôle (meilleure fiche seule) : groupe « {choix['controle_meilleure_fiche']['groupe']} » ({'concorde' if choix['controle_meilleure_fiche']['concorde'] else 'diverge'}) ; tu peux t'en servir en une phrase si elle renforce la piste, sans en faire la piste.
- **Dossier de piste** (fiches complètes avec objections, moisson, notes, drapeaux ; puis les autres en une ligne) : `{dossier}` (sha256 `{h(dossier)}`) ; définitions des groupes : `{groupes_md}` ; classement : `{classement_md}`.
- **Dans la piste, tu gardes les arguments qui ont un appui dans les résultats publics de Lazar et une mesure qui tue** ; une fiche à drapeau rouge ne se reprend que corrigée de ce que dit le drapeau, ou pas du tout. Les chiffres d'une fiche ne sont pas vérifiés : prends tout fait du mentor dans le rapport de lecture ci-dessous ou sur sa source primaire, jamais dans une fiche.

## Sources (lis-les avant d'écrire)
- Ce que fait le mentor : `{R}brouillons/candidature-pivotal-v16/lecture-approfondie-v1/{rapport}`.
- Résultats publics de Lazar : `{R}brouillons/ideation-kirchner-q2-v1/piece-nos-resultats-v1.md` ; `{R}brouillons/ideation-mentors-soir-v1/piece-sycophancie-publique-v1.md` ; README public `/home/claude/ideation-organism/README.md`.
- Corrections établies par une lectrice indépendante : `{R}brouillons/canal-fable-v1/fable_2026-11-03_n001.md`.
{bloc}- **Coordination** : {coord}
{extra}Tous les chemins relatifs partent de `{R}`.

## Ce que tu fais
1. **Arguments** : dans la piste, les deux ou trois plus forts (raisons en cinq lignes).
2. **Registre des affirmations** : chaque affirmation, sa source (chemin et sha256, ou papier et page) et sa force (« publique et vérifiée » ; « interne vérifiée » ; « non vérifiée » : interdite). Un travail non fait n'entre que dit comme tel.
3. **La réponse**, en anglais, à la première personne de Lazar, qui répond à ce que la question demande en clair ; simple, concret, phrases courtes, sans titres ni listes ; chaque nombre dans le registre ; liens publics quand ils aident ; aucune citation de plus de quatorze mots.
4. **Relis-toi** comme le mentor : la phrase qu'il contredirait de ses travaux ; corrige.

## Ce que tu écris (fichiers neufs, `{R}brouillons/redaction-finale-v1/{slug}/`)
`note-piste-v{vers}.md` (français), `registre-affirmations-v{vers}.md`, `reponse-v{vers}.md` (la réponse seule, puis son compte de mots par script).

## Interdits
Aucun commit, aucun `.sha256`, aucun fichier existant modifié ; rien sous `donnees/` ; aucun `git fetch` ; aucun appel de modèle autre que toi ; `WebFetch` seulement pour vérifier un fait que les sources ne donnent pas ; rien sous `/home/claude/coffre-*` ; résultats internes du nul v9 interdits (R-1307) ; niveau méthode pour toute triche.

## Rendu
Réponse finale : les arguments retenus en une ligne ; le compte de mots ; le registre résumé ; ce qui reste à confirmer par Lazar ; chemins et sha256.
"""
open(sortie_consigne, 'w').write(t); print(sortie_consigne, hashlib.sha256(t.encode()).hexdigest())
