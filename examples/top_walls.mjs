// Biggest Hyperliquid liquidation levels for a coin (Node 18+).
//   node top_walls.mjs ETH
// Live map: https://hyperperps.app/hyperliquid-liquidation-heatmap
const symbol = (process.argv[2] ?? "BTC").toUpperCase();
const res = await fetch(`https://hyperperps.app/api/public/heatmap/${symbol}`);
const data = await res.json();

const { as_of, age_seconds, stale } = data._meta;
console.log(`${symbol} as of ${as_of} (${age_seconds}s old, stale=${stale})`);
for (const side of ["longs", "shorts"]) {
  console.log(`\n${side} liquidation levels:`);
  for (const l of data.liquidations[side].slice(0, 5)) {
    console.log(`  ${l.price}  $${Math.round(l.notional_usd).toLocaleString()}  ${l.distance_pct}%  ${l.wallet_count} wallets`);
  }
}
