import fs from "node:fs";
import path from "node:path";
import type { GateConfig } from "./types.js";

export function loadConfig(configPath: string): GateConfig {
  const abs = path.isAbsolute(configPath) ? configPath : path.resolve(process.cwd(), configPath);
  const raw = fs.readFileSync(abs, "utf-8");
  const json = JSON.parse(raw) as GateConfig;

  if (!json?.token?.mint) throw new Error("Invalid config: token.mint missing");
  if (json.token.network !== "solana") throw new Error("Only solana network is supported in verifier v1");
  if (!Array.isArray(json.gates)) throw new Error("Invalid config: gates missing");

  return json;
}