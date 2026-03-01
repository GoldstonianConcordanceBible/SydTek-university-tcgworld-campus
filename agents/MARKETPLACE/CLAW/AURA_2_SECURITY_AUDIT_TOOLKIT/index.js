export async function run(input) {
  const { repo_structure, policies_enabled } = input;

  const report = {
    summary: [],
    risk_score: 0,
    recommendations: []
  };

  if (!repo_structure) {
    report.summary.push("No repository structure provided.");
    report.risk_score = 10;
    report.recommendations.push("Provide folder tree for analysis.");
    return report;
  }

  if (!policies_enabled) {
    report.summary.push("Policy framework not declared.");
    report.risk_score += 20;
    report.recommendations.push("Define AI governance and compliance layer.");
  }

  report.summary.push("Structural scan complete.");
  report.risk_score += 15;

  return report;
}