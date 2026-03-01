import { Connection, PublicKey } from "@solana/web3.js";

/**
 * Reads SPL token balance for (wallet, mint) by scanning token accounts.
 * Read-only RPC calls; no signing.
 */
export async function getSplTokenBalanceUi(opts: {
  rpcUrl: string;
  wallet: string;
  mint: string;
}): Promise<{ decimals: number; balanceRaw: bigint; balanceUi: number }> {
  const connection = new Connection(opts.rpcUrl, "confirmed");

  const walletPk = new PublicKey(opts.wallet);
  const mintPk = new PublicKey(opts.mint);

  // Get all token accounts owned by wallet for this mint
  const tokenAccounts = await connection.getTokenAccountsByOwner(walletPk, {
    mint: mintPk
  });

  let decimals = 0;
  let balanceRaw = 0n;

  for (const acc of tokenAccounts.value) {
    const parsed = await connection.getParsedAccountInfo(acc.pubkey);
    const data: any = (parsed.value as any)?.data;

    // parsed format: data.parsed.info.tokenAmount
    const tokenAmount = data?.parsed?.info?.tokenAmount;
    if (!tokenAmount) continue;

    decimals = Number(tokenAmount.decimals ?? decimals);
    const amountStr = String(tokenAmount.amount ?? "0");
    balanceRaw += BigInt(amountStr);
  }

  const balanceUi = Number(balanceRaw) / Math.pow(10, decimals || 0);
  return { decimals, balanceRaw, balanceUi };
}