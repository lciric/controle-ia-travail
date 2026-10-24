import json
def swarm_assimilate_discoveries(memory_store: dict, generation_idx: int, unit_traces: list) -> dict:
    memory_store.setdefault('generational_distillations', {})[f'G_{generation_idx}'] = [
        tr.get('unit_name', '') for tr in unit_traces
    ]
    return memory_store

def swarm_project_knowledge_for_next_generation(memory_store: dict, target_generation_idx: int) -> str:
    return json.dumps({
        'target_generation': target_generation_idx,
        'axioms': memory_store.get('epigenetic_generational_axioms', [])[-8:],
        'concepts': memory_store.get('discovered_mathematical_concepts', [])[-12:],
        'closed_flaws': (memory_store.get('literature_and_forum_flaws_eliminated', []) + memory_store.get('novel_beyond_labs_flaws_eliminated', []))[-15:]
    }, ensure_ascii=False, indent=2)
