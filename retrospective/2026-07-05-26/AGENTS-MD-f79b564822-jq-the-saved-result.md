# agent instruction

**jq the saved result.** When an MCP tool result exceeds the token cap and is saved to a file, probe its structure and extract only the fields you need (`jq -r '.valid'`), guided by the schema in the error message. Never Read the raw file into context.

*Grounded in: the Mermaid validator returning 177,747 characters (rendered SVG/PNG inline) for a diagram whose only needed answer was `valid: true`.*

# justification

The needed answer was one boolean; the payload was ~45k tokens of SVG. One `jq` call retrieved it. The failure mode is an agent flooding its own context with base64 pixels and losing the working state that mattered.
