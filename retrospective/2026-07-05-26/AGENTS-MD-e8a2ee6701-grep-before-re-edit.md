# agent instruction

**Grep before re-Edit.** If an Edit fails with "string not found" on a file written earlier in the session, do not retype from memory — grep the target region (`grep -n -C 4 'anchor phrase' file`) and rebuild old_string from the output, respecting the actual line breaks.

*Grounded in: an Edit to the A-VS definition failing because the remembered line-wrap point differed from the file's; one grep recovered the exact text and the retry succeeded.*

# justification

Prose written at one wrap width and edited from memory at another fails string-matching even when every word is right. The recovery is mechanical and always the same; encoding it saves the second and third blind retry.
