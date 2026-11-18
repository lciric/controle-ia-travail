# Artifact: Can a search hold its own bar?

In-loop accounting layer (objective, stopping, and feedback
registries over a recorded ledger state), statistical instruments,
replay auditor, frozen experiment configurations, committed result
JSONs, deterministic figure/table/audit generators, and the manifest
and complete recorded trace of each of the 53 audited runs reported
in the paper.

The discovery platform (registry tool surface, feature library,
strategy archetypes, backtest engine, data pipeline) is not part of
this archive; it is available from the author on reasonable request
for research verification purposes.

## Verify

    pip install numpy pandas matplotlib pytest
    pytest tests -q

Replay any run's in-loop decisions from its trace:

    python -c "from backtest_agents.experiments.replay import audit_search_replay; \
        import json, pathlib; \
        t = json.loads(pathlib.Path('runs/<RUN>/refine_trace.json').read_text()); \
        print(audit_search_replay(t))"

The 37 accounting (gate/treatment) runs replay bit-exactly. The 16
control runs use the accounting-inactive default configuration,
record no `search` block, and correctly report nothing to replay;
that 37/16 split is the paper's own run inventory.

Regenerate the paper's numbers from committed sources:

    python scripts/p2_audit_paper_numbers.py

Regenerate the paper's figures and tables (matplotlib is needed
only for this step):

    python scripts/p2_figures.py

The correlation and effective-N endpoint fields are carried by the
committed paper/paper2/endpoints.json; recomputing those specific
fields needs the per-run candidate matrices, which are available
from the author on reasonable request.

## License

Code: MIT (see LICENSE). Data (configurations, result JSONs, run
manifests and traces): CC BY 4.0.
