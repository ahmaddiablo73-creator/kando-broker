import chromadb
import os

class KandoMemory:
    def __init__(self):
        # ایجاد حافظه محلی در پوشه kando_db
        self.client = chromadb.PersistentClient(path="kando_db")
        self.collection = self.client.get_or_create_collection(name="evolution_history")

    def store_evolution(self, command, code_snippet):
        # ذخیره دستور و کدِ مرتبط برای آینده
        self.collection.add(
            documents=[code_snippet],
            metadatas=[{"command": command}],
            ids=[str(len(self.collection.get()['ids']))]
        )

    def recall_evolution(self, query):
        # بازیابیِ دانشِ گذشته برای تصمیم‌گیریِ جدید
        results = self.collection.query(query_texts=[query], n_results=1)
        return results['documents'][0] if results['documents'] else None

if __name__ == '__main__':
    mem = KandoMemory()
    print("KANDO-CORE: Memory Bank Initialized.")
