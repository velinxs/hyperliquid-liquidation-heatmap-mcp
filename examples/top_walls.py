"""Biggest Hyperliquid liquidation levels for a coin.

    python top_walls.py ETH

Live map: https://hyperperps.app/hyperliquid-liquidation-heatmap
"""
import json
import sys
import urllib.request

symbol = (sys.argv[1] if len(sys.argv) > 1 else "BTC").upper()
url = f"https://hyperperps.app/api/public/heatmap/{symbol}"
req = urllib.request.Request(url, headers={"User-Agent": "heatmap-example/1"})
with urllib.request.urlopen(req, timeout=15) as r:
    data = json.load(r)

meta = data["_meta"]
print(f"{symbol} as of {meta['as_of']} ({meta['age_seconds']}s old, stale={meta['stale']})")
for side in ("longs", "shorts"):
    print(f"\n{side} liquidation levels:")
    for lvl in data["liquidations"][side][:5]:
        print(f"  {lvl['price']:>12,.2f}  ${lvl['notional_usd']:>14,.0f}  "
              f"{lvl['distance_pct']:+.2f}%  {lvl['wallet_count']} wallets")
