import cProfile, pstats, sys, time
sys.argv = ["x"]
import runpy
src = open("/tmp/claude-0/-home-user-controle-ia-travail/6e2b0069-d4f4-5fd1-be63-f516f6a3ee23/scratchpad/dev-code-v5/fumee.py").read()
cProfile.run(compile(src, "fumee", "exec"), "/tmp/claude-0/-home-user-controle-ia-travail/6e2b0069-d4f4-5fd1-be63-f516f6a3ee23/scratchpad/dev-code-v5/prof.out")
p = pstats.Stats("/tmp/claude-0/-home-user-controle-ia-travail/6e2b0069-d4f4-5fd1-be63-f516f6a3ee23/scratchpad/dev-code-v5/prof.out"); p.sort_stats("cumulative").print_stats(28)
