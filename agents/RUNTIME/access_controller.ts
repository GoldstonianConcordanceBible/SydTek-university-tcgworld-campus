import { verifyWalletAgainstConfig } from "../CREDENTIALS/verifier/src/verify.js";
import { loadConfig } from "../CREDENTIALS/verifier/src/config.js";

export async function resolveAccess({
  wallet,
  rpcUrl,
  configPath
}: {
  wallet?: string;
  rpcUrl: string;
  configPath: string;
}) {
  if (!wallet) {
    return {
      roles: [],
      unlocked_shelves: ["PUBLIC"],
      message: "No wallet connected. Public access only."
    };
  }

  const config = loadConfig(configPath);

  const result = await verifyWalletAgainstConfig({
    rpcUrl,
    wallet,
    config
  });

  const shelves = ["PUBLIC"];

  if (result.roles.includes("GCB_MEMBER")) {
    shelves.push("GATED_MEMBER");
  }

  if (result.roles.includes("GCB_SUPPORTER")) {
    shelves.push("GATED_SUPPORTER");
  }

  return {
    roles: result.roles,
    unlocked_shelves: shelves,
    token_balance: result.balance_ui
  };
}