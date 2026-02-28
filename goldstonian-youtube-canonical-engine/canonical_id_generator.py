def generate_canonical_id(book_code, chapter):
    return f"GCB-{book_code}-CH{int(chapter):02d}"

# Example
print(generate_canonical_id("GEN", 1))
# Output: GCB-GEN-CH01