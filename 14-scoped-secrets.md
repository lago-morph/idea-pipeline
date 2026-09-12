# Secrets Bundling

**Source:** handwritten notes, 2026-08-10

---

## Raw transcription

Secrets bundling                                        2026-08-10

  secrets bundles for ephemeral envs.
    - Dev Containers
    - Agent Sandboxes

                                              w/secrets
  mgmt (github, AWS, cloudflare, etc.)
  Different profiles specified @ startup

    |_ Pattern for storing secrets for dev on CF        [highlighted]
       and having one key for that                      [highlighted]

  - CLI or environment-based vault w/ cloud storage
    of encrypted store.  I want to start a session,
    give a password, all secrets available
    transiently (Github, AI svcs, DNS host, Pluralsight, real AWS
                                                         account)
