import express from "express";
import { resolveAccess } from "./access_controller.js";
import { routeUser } from "./intent_router.js";
import { buildSystemPrompt } from "./aurelia_runtime_prompt_builder.js";

const app = express();
app.use(express.json());

app.post("/chat", async (req, res) => {
  const { wallet, intent, message } = req.body;

  const access = await resolveAccess({
    wallet,
    rpcUrl: process.env.SOLANA_RPC_URL!,
    configPath: "../CREDENTIALS/gcb_token_config.json"
  });

  const route = routeUser({
    intent,
    userMessage: message,
    unlockedShelves: access.unlocked_shelves
  });

  const monetizationMode =
    route.action === "OFFER_PREMIUM"
      ? "offer"
      : route.action === "SOFT_ROUTE"
      ? "soft"
      : "none";

  const systemPrompt = buildSystemPrompt({
    roles: access.roles,
    unlockedShelves: access.unlocked_shelves,
    monetizationMode
  });

  res.json({
    systemPrompt,
    routing: route,
    access
  });
});

app.listen(3000, () => {
  console.log("Aurelia runtime listening on port 3000");
});