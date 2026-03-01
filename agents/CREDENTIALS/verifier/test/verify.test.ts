import { describe, it, expect, vi } from "vitest";
import type { GateConfig } from "../src/types.js";

// Mock the balance call so tests are deterministic (no RPC).
vi.mock("../src/solana_balance.js", () => {
  return {
    getSplTokenBalanceUi: async () => ({
      decimals: 6,
      balanceRaw: 1500000n, // 1.5 tokens in 6 decimals
      balanceUi: 1.5
    })
  };
});

import { verifyWalletAgainstConfig } from "../src/verify.js";

describe("verifyWalletAgainstConfig", () => {
  it("matches gates based on balance", async () => {
    const config: GateConfig = {
      version: 1,
      token: {
        name: "Goldstonian Concordance Bible",
        symbol: "GCB",
        network: "solana",
        mint: "E68E27Y72FHTJH1MycB6KjX5PQAyKPYsRGZjMEx9",
        source: "https://pump.fun/coin/E68E27Y72FHTJH1MycB6KjX5PQAyKPYsRGZjMEx9pump"
      },
      gates: [
        { gate_id: "GATE_GCB_MEMBER", min_balance: 1, roles_granted: ["GCB_MEMBER"], description: "" },
        { gate_id: "GATE_GCB_SUPPORTER", min_balance: 1000, roles_granted: ["GCB_SUPPORTER"], description: "" }
      ]
    };

    const res = await verifyWalletAgainstConfig({
      rpcUrl: "https://example-rpc.invalid",
      wallet: "11111111111111111111111111111111",
      config
    });

    expect(res.ok).toBe(true);
    expect(res.balance_ui).toBe(1.5);
    expect(res.roles).toContain("GCB_MEMBER");
    expect(res.roles).not.toContain("GCB_SUPPORTER");
    expect(res.matched_gates.map((g) => g.gate_id)).toEqual(["GATE_GCB_MEMBER"]);
  });
});