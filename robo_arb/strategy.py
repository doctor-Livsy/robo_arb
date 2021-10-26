

async def price_analyze(binance, ftx, diff):
    try:
        if float(binance['a']) - ftx['data']['bid'] > diff:
            print('There is opportunity to arbitration.\n'
                  '==Binance BUY===FTX SELL==')

        elif ftx['data']['ask'] - float(binance['b']) > diff:
            print('There is opportunity to arbitration.\n'
                  '==FTX BUY===Binance SELL==')

        else:
            print(binance)
            print(ftx)
    except KeyError:
        print('Observing start')
