export type GateConfig = {
  version: number;
  token: {
    name: string;
    symbol: string;
    network: "solana" | "base" | "ethereum";
    mint: string;
    source: string;
  };
  gates: Array<{
    gate_id: string;
    min_balance: number; // in UI units (e.g., 1 token)
    roles_granted: string[];
    description: string;
  }>;
};

export type VerifyResult = {
  ok: boolean;
  network: "solana";
  wallet: string;
  mint: string;
  decimals: number;
  balance_raw: string; // bigint as string
  balance_ui: number;
  matched_gates: Array<{
    gate_id: string;
    roles_granted: string[];
    min_balance: number;
  }>;
  roles: string[];
  error?: string;
};