""" Example application using lseg.data module to open a session and retrieve data from ISIN."""
import lseg.data as ld
from lseg.data.content import symbol_conversion

if __name__ == '__main__':
    try:
        ld.open_session()
        print('Session opened successfully.')
    except Exception as e:
        print(f'Failed to open session: {e}')

    print('Application is running...')
    # Symbol types:
    # - symbol_conversion.RIC => RIC
    # - symbol_conversion.ISIN => IssueISIN
    # - symbol_conversion.CUSIP => CUSIP
    # - symbol_conversion.SEDOL => SEDOL
    # - symbol_conversion.TICKER_SYMBOL => TickerSymbol
    # - symbol_conversion.OA_PERM_ID => IssuerOAPermID
    # - symbol_conversion.LIPPER_ID => FundClassLipperID

    response = symbol_conversion.Definition(
        symbols=['US0378331005', 'US5949181045',
                 'US0231351067', 'US02079K3059', 'US88160R1014'],
        from_symbol_type=symbol_conversion.SymbolTypes.ISIN,
        to_symbol_types=[
            symbol_conversion.SymbolTypes.RIC
        ],
    ).get_data()

    # Print response
    print(f' Converting ISIN to RIC:\n {response.data.df}')
    # Convert RIC column to List
    RICs_list = list(response.data.df['RIC'])

    data = ld.get_data(universe=RICs_list, fields=['CF_CURR', 'BID', 'ASK'])
    print(f'Retrieve data:\n {data}')
