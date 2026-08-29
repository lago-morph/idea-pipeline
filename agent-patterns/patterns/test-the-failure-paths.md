---
id: test-the-failure-paths
title: Test the failure paths
type: pattern
status: adopted
durability: structural
scope: interactive
tools: both
category: review-quality
verified: 2026-08-29
models: [claude-5, gpt-5.6]
confidence: medium
sources: [every-2026-08-10-vibe-coded-security-risk, osmani-2026-code-review-ai]
related: [tier-review-by-risk, agentic-manual-testing]
aliases: []
---
# Test the failure paths

**Use when:** the change exposes a surface someone else can reach — an endpoint, a connector, a login, a payment, anything handling untrusted input.

**Do:**
- Write down what should be *refused*, then test that: the unauthenticated caller, the wrong user's data, the malformed payload, the expired session.
- Treat the happy-path test as proof the feature works, never as proof it is safe.
- Name the field you have wandered into (auth, payments, crypto) and learn its basic principles before deploying into it.
- Put auth, payments, secrets, and untrusted-input changes through a human threat-model pass plus a security scanner, whatever the agent's tests say.
- After an incident, write the lesson into the instructions file the agent reads next time.

**Why:** people naturally probe what a program should do rather than how it can fail, and an agent prompted with the feature's goal inherits exactly that bias. The gap is the question nobody knew to ask.

**Don't / when not:** internal scratch code with no reachable surface — but check that assumption before relying on it.

**Evidence:**
- [every-2026-08-10-vibe-coded-security-risk] the author tested what the connector was supposed to do but never whether someone who should not connect could; a public registration route stayed live for weeks.
- [osmani-2026-code-review-ai] auth, payments, secrets, and untrusted-input paths are a standing category requiring a human threat model plus a security tool pass, citing elevated rates of security flaws in AI-written code.
