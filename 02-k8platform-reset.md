# Spec: k8-platform Remaining Iterations (Reset)

**Phase 2 of the high-level plan**
**Repo:** `lago-morph/k8-platform`

---

## What It Is

k8-platform is a production-like, three-tier Kubernetes platform on AWS being built as
a learning reference and eventual blog series. It defines a management cluster (EKS +
ArgoCD + Crossplane) that provisions platform services and workload clusters declaratively.

Iterations 0 (base environment) and 1 (management cluster) are complete. Iterations 2–6
need to be replanned to use the batch-job skill from Phase 1 as the execution mechanism
for privileged operations — replacing the ad-hoc GitHub Actions approach used so far.

**Remaining iterations:**
- Iteration 2: Crossplane foundations (PlatformSecret claim → ASM secret + K8s Secret)
- Iteration 3: Platform services cluster (ingress, ExternalDNS, cert-manager)
- Iteration 4: Observability (Grafana, cross-cluster metrics)
- Iteration 5: Authentication (ArgoCD + Grafana SSO via Keycloak → Cognito)
- Iteration 6: First workload cluster (one Crossplane claim + one Git commit)

---

## Current State

- Iterations 0–1 complete; ArgoCD UI live at `argocd.management.<domain>` with TLS
- `terraform/base/` and `terraform/management/` are done; everything else is GitOps from here
- `argocd/`, `crossplane/`, `clusters/`, `platform-services/` directories exist but are
  sparsely populated
- `ai/DESIGN.md` and `ai/REQUIREMENTS.md` document the architecture rationale
- Iterations 0–1 were executed using an early informal version of what became
  poc-github-ai-sandbox

---

## Recommended Changes / Additions

- **Rewrite the iteration plan** as structured work items in the batch-job format — each
  iteration becomes an issue with a typed job body, not a manual runbook
- **Add the k8s-infra command set** to the poc-github-ai-sandbox command registry (as
  noted in the batch-job skill spec) before starting iteration 2
- This repo is the **infrastructure substrate for agent-os** — document that dependency
  explicitly in the README so future implementers understand the priority
- Consider adding a **validation job** at the end of each iteration that runs the
  architecture-level tests from agent-os (once that testing framework exists)

---

## Open Questions

- What specifically from each iteration requires privileged execution (Terraform apply,
  Helm install, kubectl apply) vs what can be committed to Git and reconciled by ArgoCD?
  Need to map this per-iteration before replanning.
- Iterations 3–6 depend on Crossplane being functional (iteration 2). Is iteration 2
  parallelizable at all, or is it fully sequential?
- Are there any cost implications of leaving partially-provisioned AWS infrastructure
  between sessions while the batch-job skill is being formalized?

---

## Recommended Pivot

The pivot from iterations 0–1's approach to the batch-job skill is not a code rewrite —
it's a **replanning of execution**. The Terraform and Helm configs stay the same. What
changes is that instead of running `terraform apply` locally or via an ad-hoc workflow,
agents submit a structured batch job and the runner executes with stored credentials.
This makes every infrastructure operation auditable, restart-safe, and agent-executable.

---

## What Needs to Happen Next

1. Wait for Phase 1 (batch-job skill) and the k8s-infra command variant
2. Map each remaining iteration: which ops are privileged, which are GitOps
3. Rewrite iteration 2–6 plans as structured batch-job work items
4. Execute iteration 2 first as the proof that the new approach works end-to-end

---

## Dependencies

**Depends on:** Phase 1 (batch-job skill), `poc-github-ai-sandbox` (execution protocol)
**Enables:** `agent-os` (requires k8-platform as baseline), agent software factory testing
