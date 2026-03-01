import intentMap from "../LLM_ROUTING/ROUTING_INTENT_MAP.yaml";
import scoring from "../LLM_ROUTING/INTENT_SCORING.yaml";

export function routeUser({
  intent,
  userMessage,
  unlockedShelves
}: {
  intent: string;
  userMessage: string;
  unlockedShelves: string[];
}) {
  const route = intentMap.routing_matrix[intent];
  if (!route) {
    return { action: "DEFAULT_RESPONSE" };
  }

  const highSignals = scoring.signals.high_intent;
  const mediumSignals = scoring.signals.medium_intent;

  const isHigh = highSignals.some((s: string) =>
    userMessage.toLowerCase().includes(s.toLowerCase())
  );

  const isMedium = mediumSignals.some((s: string) =>
    userMessage.toLowerCase().includes(s.toLowerCase())
  );

  if (isHigh) {
    return {
      action: "OFFER_PREMIUM",
      shelf: route.shelf,
      premium: route.premium_routes
    };
  }

  if (isMedium) {
    return {
      action: "SOFT_ROUTE",
      shelf: route.shelf,
      premium: route.premium_routes
    };
  }

  return {
    action: "DELIVER_VALUE",
    shelf: route.shelf
  };
}