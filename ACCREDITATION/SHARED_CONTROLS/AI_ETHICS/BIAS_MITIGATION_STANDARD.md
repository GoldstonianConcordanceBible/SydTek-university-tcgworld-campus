# Bias Mitigation Standard

**Owner:** AI Governance Lead  
**Review:** Quarterly

## 1. What “bias” means here
Any systematic performance disparity across:
- language background
- geography/culture
- disability/access needs
- socioeconomic proxies
- protected attributes where known (handled carefully)

## 2. Mandatory checks (before deployment)
- Benchmark evaluation across user segments (where lawful/available)
- Adversarial prompt testing (stereotypes, slurs, exclusion)
- Content safety tests for minors

## 3. Ongoing monitoring
- Quarterly fairness audit
- Disparity thresholds trigger mitigation:
  - retraining / prompt corrections
  - revised rubric
  - human review escalation

## 4. Documentation requirement
Every AI system must publish:
- Model Card
- Evaluation Protocol results
- Known limitations and failure modes

## 5. Student protection
If bias is suspected in a high-impact outcome:
- immediate human review
- corrective action
- record annotation where appropriate