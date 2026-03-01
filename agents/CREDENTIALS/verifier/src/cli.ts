import { loadConfig } from "./config.js";
import { verifyWalletAgainstConfig } from "./verify.js";

function getArg(name: string): string | undefined {
  const idx = process.argv.indexOf(name);
  if (idx === -1) return undefined;
  return process.argv[idx + 1];
}

function usage(): never {
  console.error("Usage: tsx src/cli.ts --wallet <WALLET> --config <PATH> [--rpc <RPC_URL>]");
  process.exit(2);
}

const wallet = getArg("--wallet");
const configPath = getArg("--config");
const rpc = getArg("--rpc") || process.env.SOLANA_RPC_URL || "https://api.mainnet-beta.solana.com";

if (!wallet || !configPath) usage();

const config = loadConfig(configPath);
const result = await verifyWalletAgainstConfig({ rpcUrl: rpc, wallet, config });

process.stdout.write(JSON.stringify(result, null, 2) + "\n");

// Exit non-zero if failed verification call (not if user simply doesn’t meet gate)
if (!result.ok) process.exit(1);