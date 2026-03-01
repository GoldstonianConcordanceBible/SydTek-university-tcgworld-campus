import type { GateConfig, VerifyResult } from "./types.js";
import { getSplTokenBalanceUi } from "./solana_balance.js";

function uniq(arr: string[]): string[] {
  return Array.from(new Set(arr));
}

export async function verifyWalletAgainstConfig(opts: {
  rpcUrl: string;
  wallet: string;
  config: GateConfig;
}): Promise<VerifyResult> {
  try {
    if (opts.config.token.network !== "solana") {
      return {
        ok: false,
        network: "solana",
        wallet: opts.wallet,
        mint: opts.config.token.mint,
        decimals: 0,
        balance_raw: "0",
        balance_ui: 0,
        matched_gates: [],
        roles: [],
        error: "Unsupported network"
      };
    }

    const { decimals, balanceRaw, balanceUi } = await getSplTokenBalanceUi({
      rpcUrl: opts.rpcUrl,
      wallet: opts.wallet,
      mint: opts.config.token.mint
    });

    const matched = opts.config.gates
      .filter((g) => balanceUi >= g.min_balance)
      .map((g) => ({
        gate_id: g.gate_id,
        roles_granted: g.roles_granted,
        min_balance: g.min_balance
      }));

    const roles = uniq(matched.flatMap((m) => m.roles_granted));

    return {
      ok: true,
      network: "solana",
      wallet: opts.wallet,
      mint: opts.config.token.mint,
      decimals,
      balance_raw: balanceRaw.toString(),
      balance_ui: balanceUi,
      matched_gates: matched,
      roles
    };
  } catch (e: any) {
    return {
      ok: false,
      network: "solana",
      wallet: opts.wallet,
      mint: opts.config.token.mint,
      decimals: 0,
      balance_raw: "0",
      balance_ui: 0,
      matched_gates: [],
      roles: [],
      error: e?.message ?? String(e)
    };
  }
}