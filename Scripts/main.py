import json
from pathlib import Path

# Define path to memory
MEMORY_PATH = Path("../memory/project_von_memory.json")

# Load memory
with open(MEMORY_PATH, 'r', encoding='utf-8') as f:
    memory = json.load(f)

# Print goals
print("\n=== USER GOALS ===")
for goal in memory.get('userGoals', []):
    print(f"ID: {goal['id']}")
    print(f"Description: {goal['description']}")
    print(f"Progress: {goal.get('progressPercent')}%")
    print("-" * 40)

    # Example: update progress on goal 1
for goal in memory.get('userGoals', []):
    if goal['id'] == 1:
        goal['progressPercent'] += 5

# Save to a new file
with open(MEMORY_PATH.parent / "project_von_memory_UPDATED.json", 'w', encoding='utf-8') as f:
    json.dump(memory, f, indent=2)

print("\n✅ Progress updated and saved!")
