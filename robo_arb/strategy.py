import asyncio
import time
import logger


logger = logger.get_logger('[Trade Events]')


async def price_analyze(bnc, ftx, diff, margin) -> None:
    """
    The function compares prices and, if necessary, sends a trade command.

    :param bnc: Binance update
    :param ftx: FTX update
    :param diff: min price difference to arbitrage
    :param margin: margin value for trade
    :return: None
    """
    # we have 2 cases for arbitrage trade: 'Binance case' and 'FTX case'
    # Binance case: bid on FTX is more
    # FTX case: bid on Binance is more

    try:
        # comparing prices and volumes for 'Binance case'
        check, pnl = await check_conditions(ftx['data']['bid'],
                                            ftx['data']['bidSize'],
                                            float(bnc['a']),
                                            float(bnc['A']),
                                            diff, margin, 'BINANCE')
        if check:  # commands to execute trade
            print('There is opportunity to arbitration.\n'
                  f'Estimated PnL: {pnl}')
            await binance_execute('BUY', margin)
            await ftx_execute('SELL', margin)
            return

        # comparing prices and volumes for 'FTX case'
        check, pnl = await check_conditions(float(bnc['b']),
                                            float(bnc['B']),
                                            ftx['data']['ask'],
                                            ftx['data']['askSize'],
                                            diff, margin, 'FTX')
        if check:  # commands to execute trade
            await ftx_execute('BUY', margin)
            await binance_execute('SELL', margin)
            return

        else:  # all conditions is False. Just print JSONs
            print(bnc)
            print(ftx)

    except KeyError:
        # because the first update contains headers
        print('Starting observe')


async def check_conditions(bid, bid_size, ask, ask_size, min_diff, margin, case) -> tuple:
    """Checking prices and volumes for arbitrage"""

    current_prices_difference = bid - ask

    # comparing prices
    if current_prices_difference > min_diff:
        # comparing volume
        if (bid * bid_size > margin) and (ask * ask_size > margin):
            pnl = (margin / ask) * bid - margin
            event = f'\n{time.asctime()} -- Case: {case}\nEstimated PnL: {pnl}'
            print(event)
            logger.info(event)
            return True, pnl
        else:
            return False, None
    else:
        return False, None


async def binance_execute(action, margin) -> None:
    """Execute trade command..."""

    event = f'BINANCE {action}. Margin: {margin}'
    print(event)
    logger.info(event)


async def ftx_execute(action, margin) -> None:
    """Execute trade command..."""

    event = f'FTX {action}.     Margin: {margin}'
    print(event)
    logger.info(event)
