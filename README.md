# badger-multisig

This repo is where all EVM multisig operations take place for the Badger DAO.

It relies heavily on [`ganache-cli`](https://docs.nethereum.com/en/latest/ethereum-and-clients/ganache-cli/), [`eth-brownie`](https://github.com/eth-brownie/brownie), [`gnosis-py`](https://github.com/gnosis/gnosis-py) and a custom developed evolution of [`ape-safe`](https://github.com/banteg/ape-safe); [`great-ape-safe`](https://github.com/gosuto-ai/great-ape-safe).

A good overview of all its tickets and their status can be found here: https://github.com/orgs/Badger-Finance/projects/25.

Read more about the Badger DAO and its community at https://badger.com/dao-and-community.

![f](https://badger.com/images/badger-logo.svg)


# Multisig Adresses

| Label | Description | Address (Links) |
|-|-|-|
|`dev`|Governance/admin rights; set parameters on vaults and strategies, queue/execute timelock txs, etc.|Mainnet: `0xB65cef03b9B89f99517643226d76e286ee999e77` ([Etherscan](https://etherscan.io/address/0xB65cef03b9B89f99517643226d76e286ee999e77), [Gnosis Safe](https://gnosis-safe.io/app/eth:0xB65cef03b9B89f99517643226d76e286ee999e77/), [Zapper](https://zapper.fi/account/0xB65cef03b9B89f99517643226d76e286ee999e77))|
|||Arbitrum: `0xb364bAb258ad35dd83c7dd4E8AC78676b7aa1e9F` ([Arbiscan](https://arbiscan.io/address/0xb364bAb258ad35dd83c7dd4E8AC78676b7aa1e9F), [Gnosis Safe](https://gnosis-safe.io/app/arb1:0xb364bAb258ad35dd83c7dd4E8AC78676b7aa1e9F/), [Zapper](https://zapper.fi/account/0xb364bAb258ad35dd83c7dd4E8AC78676b7aa1e9F))|
|||Binance Smart Chain: `0x329543f0F4BB134A3f7a826DC32532398B38a3fA` ([BscScan](https://bscscan.com/address/0x329543f0F4BB134A3f7a826DC32532398B38a3fA), [Gnosis Safe](https://gnosis-safe.io/app/bnb:0x329543f0F4BB134A3f7a826DC32532398B38a3fA/), [Zapper](https://zapper.fi/account/0x329543f0F4BB134A3f7a826DC32532398B38a3fA))|
|||Polygon: `0x4977110Ed3CD5eC5598e88c8965951a47dd4e738` ([PolygonScan](https://polygonscan.com/address/0x4977110Ed3CD5eC5598e88c8965951a47dd4e738), [Gnosis Safe](https://gnosis-safe.io/app/matic:0x4977110Ed3CD5eC5598e88c8965951a47dd4e738/), [Zapper](https://zapper.fi/account/0x4977110Ed3CD5eC5598e88c8965951a47dd4e738))|
|||Fantom: `0x4c56ee3295042f8A5dfC83e770a21c707CB46f5b` ([FTMScan](https://ftmscan.com/address/0x4c56ee3295042f8A5dfC83e770a21c707CB46f5b), [Fantom Safe](https://safe.fantom.network/#/safes/0x4c56ee3295042f8A5dfC83e770a21c707CB46f5b/), [Zapper](https://zapper.fi/account/0x4c56ee3295042f8A5dfC83e770a21c707CB46f5b))|
|`techops`|Controller for the DAO. Call internal system functions; set emission schedules.|Mainnet: `0x86cbD0ce0c087b482782c181dA8d191De18C8275` ([Etherscan](https://etherscan.io/address/0x86cbD0ce0c087b482782c181dA8d191De18C8275), [Gnosis Safe](https://gnosis-safe.io/app/eth:0x86cbD0ce0c087b482782c181dA8d191De18C8275/), [Zapper](https://zapper.fi/account/0x86cbD0ce0c087b482782c181dA8d191De18C8275))|
|||Arbitrum: `0x292549E6bd5a41aE4521Bb8679aDA59631B9eD4C` ([Arbiscan](https://arbiscan.io/address/0x292549E6bd5a41aE4521Bb8679aDA59631B9eD4C), [Gnosis Safe](https://gnosis-safe.io/app/arb1:0x292549E6bd5a41aE4521Bb8679aDA59631B9eD4C/), [Zapper](https://zapper.fi/account/0x292549E6bd5a41aE4521Bb8679aDA59631B9eD4C))|
|||Binance Smart Chain: `0x777061674751834993bfBa2269A1F4de5B4a6E7c` ([BscScan](https://bscscan.com/address/0x777061674751834993bfBa2269A1F4de5B4a6E7c), [Zapper](https://zapper.fi/account/0x777061674751834993bfBa2269A1F4de5B4a6E7c))|
|||Polygon: `0xeb7341c89ba46CC7945f75Bd5dD7a04f8FA16327` ([PolygonScan](https://polygonscan.com/address/0xeb7341c89ba46CC7945f75Bd5dD7a04f8FA16327), [Gnosis Safe](https://gnosis-safe.io/app/matic:0xeb7341c89ba46CC7945f75Bd5dD7a04f8FA16327/), [Zapper](https://zapper.fi/account/0xeb7341c89ba46CC7945f75Bd5dD7a04f8FA16327))|
|||Fantom: `0x781E82D5D49042baB750efac91858cB65C6b0582` ([FTMScan](https://ftmscan.com/address/0x781E82D5D49042baB750efac91858cB65C6b0582), [Fantom Safe](https://safe.fantom.network/#/safes/0x781E82D5D49042baB750efac91858cB65C6b0582/), [Zapper](https://zapper.fi/account/0x781E82D5D49042baB750efac91858cB65C6b0582))|
|`treasury_vault`|Treasury long-term holdings; bitcoin, ether (gas), treasury controlled liquidity (TCL), farming positions, uncirculating $BADGER.|Mainnet: `0xD0A7A8B98957b9CD3cFB9c0425AbE44551158e9e` ([Etherscan](https://etherscan.io/address/0xD0A7A8B98957b9CD3cFB9c0425AbE44551158e9e), [Gnosis Safe](https://gnosis-safe.io/app/eth:0xD0A7A8B98957b9CD3cFB9c0425AbE44551158e9e/), [Zapper](https://zapper.fi/account/0xD0A7A8B98957b9CD3cFB9c0425AbE44551158e9e))|
|||Fantom: `0x45b798384c236ef0d78311D98AcAEc222f8c6F54` ([FTMScan](https://ftmscan.com/address/0x45b798384c236ef0d78311D98AcAEc222f8c6F54), [Fantom Safe](https://safe.fantom.network/#/safes/0x45b798384c236ef0d78311D98AcAEc222f8c6F54/), [Zapper](https://zapper.fi/account/0x45b798384c236ef0d78311D98AcAEc222f8c6F54))|
|`treasury_ops`|Treasury short-term holdings; beneficiary of DAO's fees and treasury's yield. Processes these incoming tokens into long-term holdings for the treasury vault.|Mainnet: `0x042B32Ac6b453485e357938bdC38e0340d4b9276` ([Etherscan](https://etherscan.io/address/0x042B32Ac6b453485e357938bdC38e0340d4b9276), [Gnosis Safe](https://gnosis-safe.io/app/eth:0x042B32Ac6b453485e357938bdC38e0340d4b9276/), [Zapper](https://zapper.fi/account/0x042B32Ac6b453485e357938bdC38e0340d4b9276))|
|||Fantom: `0xf109c50684EFa12d4dfBF501eD4858F25A4300B3` ([FTMScan](https://ftmscan.com/address/0xf109c50684EFa12d4dfBF501eD4858F25A4300B3), [Fantom Safe](https://safe.fantom.network/#/safes/0xf109c50684EFa12d4dfBF501eD4858F25A4300B3/), [Zapper](https://zapper.fi/account/0xf109c50684EFa12d4dfBF501eD4858F25A4300B3))|
|`fin_ops`|Financial txs such as payments to contractors, contributors, expenses, bounties, advisors, etc. Also handles gas refills.|Mainnet: `0xD4868d98849a58F743787c77738D808376210292` ([Etherscan](https://etherscan.io/address/0xD4868d98849a58F743787c77738D808376210292), [Gnosis Safe](https://gnosis-safe.io/app/eth:0xD4868d98849a58F743787c77738D808376210292/), [Zapper](https://zapper.fi/account/0xD4868d98849a58F743787c77738D808376210292))|
|`politician`|Processor of all bribes/incentives received from platforms such as Convex and Votium.|Mainnet: `0x6F76C6A1059093E21D8B1C13C4e20D8335e2909F` ([Etherscan](https://etherscan.io/address/0x6F76C6A1059093E21D8B1C13C4e20D8335e2909F), [Gnosis Safe](https://gnosis-safe.io/app/eth:0x6F76C6A1059093E21D8B1C13C4e20D8335e2909F/), [Zapper](https://zapper.fi/account/0x6F76C6A1059093E21D8B1C13C4e20D8335e2909F))|
|`bveCVX Treasury Voting`|Voting weight allocated to the treasury as per [BIP 87](https://forum.badger.finance/t/bip-87-bvecvx-restructure-voting-strategy-and-emissions-revised-with-community-feedback/5521)|Mainnet: `0xA9ed98B5Fb8428d68664f3C5027c62A10d45826b` ([Etherscan](https://etherscan.io/address/0xA9ed98B5Fb8428d68664f3C5027c62A10d45826b), [Gnosis Safe](https://gnosis-safe.io/app/eth:0xA9ed98B5Fb8428d68664f3C5027c62A10d45826b/), [Zapper](https://zapper.fi/account/0xA9ed98B5Fb8428d68664f3C5027c62A10d45826b))|
|`ibbtc`|Internal wallet which claims yield on behalf of the [ibBTC contract](https://etherscan.io/address/0x41671BA1abcbA387b9b2B752c205e22e916BE6e3), only to redistribute it again as emissions.|Mainnet: `0xB76782B51BFf9C27bA69C77027e20Abd92Bcf3a8` ([Etherscan](https://etherscan.io/address/0xB76782B51BFf9C27bA69C77027e20Abd92Bcf3a8), [Gnosis Safe](https://gnosis-safe.io/app/eth:0xB76782B51BFf9C27bA69C77027e20Abd92Bcf3a8/), [Zapper](https://zapper.fi/account/0xB76782B51BFf9C27bA69C77027e20Abd92Bcf3a8))|
|`recovered`|Used to retrieve tokens lost during the [exploit](https://badger.com/technical-post-mortem). Now serves to process yield from the stable vaults into $BADGER for $remBADGER holders.|Mainnet: `0x9faA327AAF1b564B569Cb0Bc0FDAA87052e8d92c` ([Etherscan](https://etherscan.io/address/0x9faA327AAF1b564B569Cb0Bc0FDAA87052e8d92c), [Gnosis Safe](https://gnosis-safe.io/app/eth:0x9faA327AAF1b564B569Cb0Bc0FDAA87052e8d92c/), [Zapper](https://zapper.fi/account/0x9faA327AAF1b564B569Cb0Bc0FDAA87052e8d92c))|
