# Hyperliquid Liquidation Heatmap MCP Server

Live Hyperliquid liquidation heatmap for AI assistants. Ask Claude, ChatGPT, Codex, Cursor or any MCP client where BTC, ETH, SOL and HYPE traders get liquidated, where their stop-losses and take-profits are stacked, and whether the crowd is net long or short.

**See the live map:** [hyperperps.app/hyperliquid-liquidation-heatmap](https://hyperperps.app/hyperliquid-liquidation-heatmap)

```
https://hyperperps.app/mcp
```

Remote MCP server (Streamable HTTP). Read-only. No install, no account, no API key.

## What it shows

Built from every Hyperliquid leaderboard account plus every account seen trading BTC, ETH, SOL and HYPE. Liquidation prices are recalculated about every 2 minutes, and the map updates about every 15 seconds with the latest price.

- **Liquidation levels:** where longs (below price) and shorts (above price) get force-closed, with notional, wallet count and distance from price.
- **Stop-loss pools and take-profit walls:** resting orders that fuel moves or cap them.
- **Crowd positioning:** net open-interest lean, whales vs retail, trapped size, leverage, fresh money, cascade mass.

All data is anonymized into price levels. No individual wallets are shown.

## Connect

| Client | How |
|---|---|
| Claude Code | `claude mcp add --transport http hyperperps https://hyperperps.app/mcp` |
| Claude Code (plugin, adds a skill) | `/plugin marketplace add velinxs/hyperperps-heatmap-plugin` then `/plugin install hyperperps-liquidation-heatmap@hyperperps` |
| Claude.ai / Claude Desktop | Settings → Connectors → Add custom connector → `https://hyperperps.app/mcp` |
| ChatGPT | Plugins → **+** → Add custom MCP server → `https://hyperperps.app/mcp/chatgpt`, authentication: none |
| Codex | `codex mcp add hyperperps --url https://hyperperps.app/mcp` |
| Cursor | [`configs/cursor.json`](configs/cursor.json) → `~/.cursor/mcp.json` |
| VS Code | [`configs/vscode.json`](configs/vscode.json) → `.vscode/mcp.json` |
| Windsurf and others | [`configs/generic.json`](configs/generic.json) |

ChatGPT has its own endpoint (`/mcp/chatgpt`) so each ChatGPT user gets a separate daily allowance.

## Tools

### `get_liquidation_heatmap`

| Argument | Required | Meaning |
|---|---|---|
| `symbol` | yes | `BTC`, `ETH`, `SOL` or `HYPE` |
| `range` | no | Percent from price to include, e.g. `10`, or `all` |
| `levels` | no | Levels per side, biggest first, e.g. `50`, or `all` |

Default: levels within 5% of price, the biggest per side.

### `get_heatmap_field_definitions`

No arguments. Returns what every field means, the sign conventions and the supported markets, straight from the live server.

### Example prompts

- "Where are the biggest BTC liquidation clusters on Hyperliquid right now?"
- "Show ETH stop-loss pools and take-profit walls within 10% of price."
- "Is the HYPE crowd net long or short, and how much of it is underwater?"
- "Give me SOL's full liquidation ladder."

## HTTP API

The same data without MCP:

```bash
curl https://hyperperps.app/api/public/heatmap/BTC
curl "https://hyperperps.app/api/public/heatmap/ETH?range=all"
```

One liquidation level looks like this:

```json
{
  "price": 58461.28,
  "notional_usd": 20544830,
  "wallet_count": 88,
  "distance_pct": -4.5,
  "top_wallet_share": 0.906
}
```

`distance_pct` is signed: negative below price, positive above. `top_wallet_share` is the largest single wallet's share of the level; a high value means one position could pull the whole wall. Check `_meta.stale` and `_meta.age_seconds` before trusting a snapshot.

Examples: [Python](examples/top_walls.py) · [JavaScript](examples/top_walls.mjs) · [shell](examples/curl.sh). Full field list: [`https://hyperperps.app/api/public/heatmap`](https://hyperperps.app/api/public/heatmap).

Free use is 500 calls a day per IP. Keys for higher limits: [hyperperps.app/api-access](https://hyperperps.app/api-access).

## Links

- Live heatmap: [Hyperliquid liquidation heatmap](https://hyperperps.app/hyperliquid-liquidation-heatmap)
- Whale positioning: [hyperperps.app/whales](https://hyperperps.app/whales)
- Official MCP Registry: `app.hyperperps/liquidation-heatmap`
- Claude Code plugin: [velinxs/hyperperps-heatmap-plugin](https://github.com/velinxs/hyperperps-heatmap-plugin)
- Discord: https://discord.gg/KWKK6Nfpy8
- [Privacy](https://hyperperps.app/privacy) · [Terms](https://hyperperps.app/terms)

Anonymized market data. Not financial advice.

## License

MIT. The server is hosted by [HyperPerps](https://hyperperps.app); this repository holds the docs, client configs and examples.
