/**
 * Minimal serverless-style handler (works for many runtimes).
 * POST JSON: { wallet: string }
 * Loads config from env CONFIG_PATH (default ../gcb_token_config.json)
 */
import { loadConfig } from "./config.js";
import { verifyWalletAgainstConfig } from "./verify.js";

export async function handler(req: { method: string; body?: any }) {
  if (req.method !== "POST") {
    return { statusCode: 405, body: JSON.stringify({ error: "Method Not Allowed" }) };
  }

  const wallet = req.body?.wallet;
  if (!wallet) {
    return { statusCode: 400, body: JSON.stringify({ error: "Missing wallet" }) };
  }

  const rpcUrl = process.env.SOLANA_RPC_URL || "https://api.mainnet-beta.solana.com";
  const configPath = process.env.CONFIG_PATH || "../gcb_token_config.json";

  const config = loadConfig(configPath);
  const result = await verifyWalletAgainstConfig({ rpcUrl, wallet, config });

  return { statusCode: 200, body: JSON.stringify(result) };
}