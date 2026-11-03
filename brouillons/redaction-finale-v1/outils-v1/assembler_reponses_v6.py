"""v6 : chaque section nomme le mentor et cite la question exacte du formulaire. Assemblage final v5 pour Lazar (3 novembre 2026, nuit) : une section par question, corps au-dessus du premier trait de chaque fichier,
compte par blancs, empreinte, statut. Heimersheim Q1 : texte de Lazar tel quel (aucune phrase anglaise du directeur) puis les remarques en français.
Usage : assembler_reponses_v5.py SORTIE HEURE_UTC"""
import hashlib, sys, os
D = '/home/claude/controle-ia-travail/brouillons/redaction-finale-v1/'
def sha(p): return hashlib.sha256(open(D + p, 'rb').read()).hexdigest()
def corps(p): return open(D + p).read().split('\n---\n')[0].strip()
sortie, heure = sys.argv[1:3]
QT = {'Stefan Heimersheim — question 1 sur 2': "Pick an interpretability direction from this list and explain the most likely reasons the research direction might fail (won't solve interpretability / won't achieve its goal), and why you think that — ta direction : (c) Activation steering against eval awareness.", 'Stefan Heimersheim — question 2 sur 2': 'Why do you want to work on Mechanistic Interpretability? Max. 150 words; spend the majority of time on Q1', 'Jan Hendrik Kirchner — question 1 sur 2': 'Describe an empirical research project you drove yourself. What was the question, what did you build or run, and what was the most surprising thing you found? If relevant, you may choose your project answer from the main application.', 'Jan Hendrik Kirchner — question 2 sur 2': 'Pick an open problem in AI alignment you think is underrated. What experiment would you run first, and what result would change your mind?', 'Lujain Ibrahim — question 1 sur 2': "Pick one of the two projects and briefly describe the first experiment you'd run. Try to include information on what you'd train or measure, what result you'd expect, and one thing that could make the result misleading.", 'Lujain Ibrahim — question 2 sur 2': 'Describe a technical project where you trained or evaluated LLMs (feel free to link to code or any public documentation/write up if you have something to share).', 'Jérémy Scheurer — question unique': "Your task is to come up with a research proposal which describes how we could get a scaling trend for misaligned behaviors such as scheming, deception, misalignment, swarm misalignment, control, or monitoring. (… texte complet dans le formulaire : tendance du type de l'horizon de tâches de METR.)", 'Paul Colognese et Francis Rhys Ward — question 1 sur 2': 'Describe an ML experiment you ran end to end (fine-tuning, RL or evals). What did you find, and what would you do differently? (max 200 words)', 'Paul Colognese et Francis Rhys Ward — question 2 sur 2 (facultative)': '(Optional) Read this post. Should we have done anything differently? What was the most interesting finding in your view and why?', 'Shi Feng et Eyon Jang — question unique': 'What are your thoughts on the value of white-box monitors and white-box methods for auditing? What do you see as their current limitations?'}
Q = [
 ("Stefan Heimersheim — question 1 sur 2", "heimersheim-q1/reponse-lazar-v1.md", "Aucune limite au formulaire.",
  "**Ton texte, tel quel.** Règle du mentor : 100 % écrit par toi ; je n'y ai écrit aucun mot. Les corrections de fond sont à faire par toi, d'après les remarques en français qui suivent le texte (vérificateur neuf compris).", True),
 ("Stefan Heimersheim — question 2 sur 2", "heimersheim-q2/reponse-v6.md", "Limite dure : 150 mots au plus.",
  "Ton texte, fond corrigé au minimum, raccourci sous la limite ; vérifié par un vérificateur neuf (0 inexact) ; 150 mots au pire cas avec le lien raccourci au dossier épinglé. À confirmer : « at the amounts I tested ».", False),
 ("Jan Hendrik Kirchner — question 1 sur 2", "kirchner-q1/reponse-v5.md", "Aucune limite écrite.",
  "Ton texte, fond corrigé au minimum (14 points, dont deux inversions de sens), puis trois affirmations ramenées à leur source par le vérificateur neuf.", False),
 ("Jan Hendrik Kirchner — question 2 sur 2", "kirchner-q2/reponse-v3.md", "Aucune limite écrite.",
  "Inchangée depuis l'assemblage v3 (tu ne l'as pas reformulée) ; vérifiée.", False),
 ("Shi Feng et Eyon Jang — question unique", "jang-feng/reponse-v7.md", "Aucune limite écrite.",
  "Inchangée ; nouvelle piste « Perturbation et témoin bénin » ; vérifiée. Repli vérifié : `jang-feng/reponse-v4.md`.", False),
 ("Jérémy Scheurer — question unique", "scheurer/reponse-v3.md", "Aucune limite écrite (visée 500).",
  "Inchangée ; fondée sur le tour seul. La course sans Claude a été lue (fiches brutes envoyées), triée, moissonnée et groupée, mais **le classeur a été interrompu par la limite du compte** : la règle de piste n'a pas pu être appliquée à l'ensemble.", False),
 ("Lujain Ibrahim — question 1 sur 2", "ibrahim-q1/reponse-v6.md", "Aucune limite écrite (visée 450 ; 556 ici).",
  "Ton texte (contenu de la v4), fond corrigé au minimum puis par le vérificateur neuf (14 points en tout). À confirmer : « sealed subset ». Replis vérifiés : `reponse-v4.md` ; la variante « survie » v3, que la règle de piste désignait (R-1436, à un point, non robuste).", False),
 ("Lujain Ibrahim — question 2 sur 2", "ibrahim-q2/reponse-v4.md", "Aucune limite écrite.",
  "Ton texte, fond corrigé au minimum (9 points, dont trois graves), chaque correction prise dans les rapports de la v3 vérifiée. **Le vérificateur neuf a été interrompu par la limite du compte** : vérification par moi seul. Repli vérifié : `reponse-v3.md`. À trancher : « AI coding agents wrote the code ».", False),
 ("Paul Colognese et Francis Rhys Ward — question 1 sur 2", "colognese-ward-q1/reponse-v3.md", "Limite : 200 mots au plus.",
  "Inchangée ; vérifiée. Variante courte (179 mots) dans l'assemblage v3.", False),
 ("Paul Colognese et Francis Rhys Ward — question 2 sur 2 (facultative)", "colognese-ward-q2/reponse-v3.md", "Aucune limite écrite (visée 300).",
  "Inchangée ; piste confirmée par la course v2 ; vérifiée.", False),
]
L = [f"# Réponses finales pour Pivotal — assemblage v5 (mentor et question nommés)", "",
     f"Conv-audit, 3 novembre 2026, {heure} UTC (`date -u`). Remplace les assemblages v3 et v4. Dix réponses pour six mentors, dans l'ordre du formulaire : Heimersheim (2), Kirchner (2), Feng et Jang (1), Scheurer (1), Ibrahim (2), Colognese et Ward (2). **Ne colle que le texte entre les deux filets de chaque réponse.**", "",
     "Statuts publics revérifiés à 23:01 UTC : têtes de `main` inchangées (`sycophancy-psychophysical-law` `b3ecaec`, `sycophancy-construct-validity` `146b2a4`, `ideation-organism` `faff48b`) ; R8 toujours en mesure, R9 non lancé : les phrases qui le disent restent justes.", ""]
for titre, f, lim, note, h1 in Q:
    c = open(D + f).read().strip() if h1 else corps(f)
    L += [f"## {titre}", "", f"**Question du formulaire** : « {QT[titre]} »", "", f"Fichier `{f}` (sha256 `{sha(f)[:16]}…`) ; **{len(c.split())} mots** (par blancs) ; {lim}", "", note, "", "━━━━━━━━━━━━━━━━━━━━", "", c, "", "━━━━━━━━━━━━━━━━━━━━", ""]
    if h1:
        r = open(D + 'heimersheim-q1/remarques-fond-texte-lazar-v2.md').read().strip()
        L += ["### Remarques de fond sur ta question 1 (en français ; à appliquer par toi)", "", f"Fichier `heimersheim-q1/remarques-fond-texte-lazar-v2.md` (sha256 `{sha('heimersheim-q1/remarques-fond-texte-lazar-v2.md')[:16]}…`).", "", r.split('\n', 1)[1].strip(), ""]
assert not os.path.exists(sortie)
open(sortie, 'w').write('\n'.join(L) + '\n'); print(sortie, hashlib.sha256(open(sortie, 'rb').read()).hexdigest())
