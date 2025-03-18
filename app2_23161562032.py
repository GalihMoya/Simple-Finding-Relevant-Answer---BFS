from collections import deque

def find_relevant_answer(faq_graph, question):
    queue = deque([question])
    visited = set()

    while queue:
        node = queue.popleft()
        
        if node in faq_graph.get("answers", {}):
            return faq_graph["answers"][node]
        
        visited.add(node)
        
        for neighbor in faq_graph.get(node, []):
            if neighbor not in visited:
                queue.append(neighbor)

    return "Sorry, no relevant answer found."

faq_graph = {
    "What is AI?": ["Machine Learning", "Deep Learning"],
    "Machine Learning": ["Supervised Learning", "Unsupervised Learning"],
    "Deep Learning": ["Neural Networks"],
    "answers": {
        "Neural Networks": "Neural Networks are AI models inspired by the human brain.",
        "Supervised Learning": "Supervised Learning uses labeled data for training."
    }
}

user_question = "What is AI?"
result = find_relevant_answer(faq_graph, user_question)
print("Relevant Answer:", result)
