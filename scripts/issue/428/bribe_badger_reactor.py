from brownie import Contract, web3, interface

from great_ape_safe import GreatApeSafe
from helpers.addresses import registry


def main():
    safe = GreatApeSafe(registry.eth.badger_wallets.treasury_ops_multisig)
    badger = interface.ERC20(
        registry.eth.treasury_tokens.BADGER, owner=safe.account
    )

    safe.take_snapshot([badger])

    bribe_vault = interface.IBribeVault(
        registry.eth.hidden_hand.bribe_vault, owner=safe.account
    )
    tokenmak_briber = interface.ITokenmakBribe(
        registry.eth.hidden_hand.tokenmak_briber, owner=safe.account
    )

    # https://etherscan.io/address/0x7816b3d0935d668bcfc9a4aab5a84ebc7ff320cf#code#L935
    prop = web3.solidityKeccak(['address'], [badger.address])

    badger.approve(bribe_vault, 50_000e18)
    tokenmak_briber.depositBribeERC20(
        prop, # bytes32 proposal
        badger, # address token
        50_000e18, # uint256 amount
    )

    safe.print_snapshot()
    safe.post_safe_tx(call_trace=True)
