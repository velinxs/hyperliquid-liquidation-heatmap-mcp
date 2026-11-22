#!/usr/bin/env sh
# Hyperliquid liquidation heatmap, BTC: biggest long and short liquidation levels.
# Live map: https://hyperperps.app/hyperliquid-liquidation-heatmap
curl -s https://hyperperps.app/api/public/heatmap/BTC |
  jq '{as_of: ._meta.as_of, stale: ._meta.stale,
       longs: .liquidations.longs[:3], shorts: .liquidations.shorts[:3]}'
