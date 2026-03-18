def load_policy(filepath="policies.txt"):
    with open(filepath, "r") as f:
        text = f.read()

    raw_chunks = text.strip().split("\n\n")
    chunks = [c.strip() for c in raw_chunks if c.strip()]
    return chunks

def search_policy(query, chunks, top_k=2):
    keywords = [w.lower() for w in query.split() if len(w) > 3]
    scored = []
    for chunk in chunks:
        score = sum(1 for kw in keywords if kw in chunk.lower())
        score.append((score, chunk))

    scored.sort(key=lambda x: x[0], reverse=True)
    top = [chunk for score, chunk in scored[:top_k] if score > 0]
    return top if top else [chunks[0]]

POLICY_CHUNKS = load_policy()