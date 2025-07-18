from typing import List, Dict, Optional

class Memory:
    def __init__(self):
        self.items = []

    def add_memory(self, memory: dict):
        """Add memory to working memory"""
        self.items.append(memory)

    def get_memories(self, limit: Optional[int] = None) -> List[Dict]:
        """Get formatted conversation history for prompt"""
        if limit:
            return self.items[-limit:]
        return self.items

    def copy_without_system_memories(self):
        """Return a copy of the memory without system memories"""
        filtered_items = [m for m in self.items if m["type"] != "system"]
        memory = Memory()
        memory.items = filtered_items
        return memory