# THX Modules

This repo describes THX Modules Proposals (TMPs) for the THX pool design based on the Diamond standard.

# Use pools

`assetpool.yaml` example

Create hardhat project at $folder, `npx hardhat init`.

With the following dependencies in your `package.json`

```json
 "dependencies": {
    "@openzeppelin/contracts": "^3.3.0",
    "diamond-2": "^1.4.0"
  }
```


Run `python3 scripts/pool.py $folder/contracts/  pools/assetpool.yaml `