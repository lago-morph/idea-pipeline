# Process Comments

**Source:** `ai-utils/process-comments/README.me`, `ai-utils/process-comments/process-command.md`

---

The idea here is to create a prompt template or AI guidance, or something to support the following work flow

1) Read a file
2) Find the first line that starts with "#C".  This will be referred to as "the comment" or "the comment line"
3) Read the rest of the comment line and use it as the first part of a prompt
8) If session logging is enabled, include this comment line in the session log of the initiating prompt, clearly indicating that it is a comment line and providing information about where it was located in the document (e.g., if it was inline with a requirement, indicate which requirement it was in the log)
4) Append to the prompt instructions to ask the user clarifying questions about the prompt
5) Append to the prompt that after getting all clarifications, the final understanding of the prompt and clarifications is to be restated back to the user, and that all files that are intended to be changed are listed for the user before doing anything else.
6) Submit the prompt to be processed by the AI agent to make the requested adjustments to the documents indicated in the summary back to the user.  If any additional documents need to be changed, you must ask (even if you have prior permission) to change those documents.
7) After the changes have been made, remove the comment line from the source document.  Do not do it along with the requested changes, to preserve the comment if the session is interrupted.
8) If session logging is enabled, log all of the user interaction and summaries of what was done as instructed elsewhere.

---

## Process Comments Command

### Usage
```
/process-comment [document-name]
```

### Description
This command processes special comment lines that start with "#C" in the specified document and creates an interactive workflow to handle the requested changes.

### Implementation

When this command is executed:

1. **Read the specified document**
   - Load the file content from the provided document-name
   - If no document name provided, prompt user to specify one

2. **Find the first "#C" comment line**
   - Scan through the document line by line
   - Locate the first line that starts with "#C"
   - Extract the full comment text (everything after "#C")

3. **Create interactive prompt**
   - Use the comment text as the foundation for a new prompt
   - Append clarifying question instructions
   - Append requirement to restate understanding and list files before changes

4. **Process with safeguards**
   - Ask user clarifying questions about the comment request
   - Restate final understanding back to user
   - List all files that will be modified
   - Wait for explicit user approval before making changes

5. **Execute and cleanup**
   - Make the requested document changes
   - Remove the processed "#C" comment line from source document
   - Log session activity if logging is enabled

### Example Usage

If a document contains:
```
#C Update the user authentication section to include two-factor authentication requirements
```

The command would:
1. Extract this comment
2. Ask clarifying questions about 2FA requirements
3. Confirm understanding and list files to change
4. Make the updates after approval
5. Remove the "#C" line

### Safety Features
- No changes made without explicit user approval
- Comment line preserved until changes are successfully completed
- All file modifications are listed before execution
- Session logging captures comment location and context
