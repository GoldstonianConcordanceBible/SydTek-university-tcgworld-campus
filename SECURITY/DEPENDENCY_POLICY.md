# Dependency Policy

All dependencies must:

- Be actively maintained
- Have no critical CVEs
- Be pinned to major version
- Avoid transitive crypto libraries unless required

No dependency may:
- Execute arbitrary shell commands
- Exfiltrate environment variables