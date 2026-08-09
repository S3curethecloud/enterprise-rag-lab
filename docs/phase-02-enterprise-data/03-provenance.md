# Provenance

Provenance describes where information came from and how it entered the knowledge system.

## Questions Provenance Helps Answer

For any piece of retrieved information:

```text
Where did this originate?
Who owns it?
Which source system supplied it?
When was it retrieved?
When was it last updated?
Was it transformed?
Can we trace the answer back to the source?
Example
{
  "source_system": "sharepoint",
  "source_uri": "sharepoint://hr/policies/compensation",
  "ingested_at": "2026-08-09T00:00:00Z",
  "content_hash": "...",
  "version": "2026.08"
}
Why Provenance Matters

Provenance supports:

trust decisions;
incident investigation;
source citations;
stale-content detection;
poisoning investigation;
re-indexing;
audit evidence.
Secure RAG Principle

Retrieved content should be treated as data, not as an authority merely because it was found in the knowledge store.

Knowing the source helps the platform decide how much trust to place in that content.
