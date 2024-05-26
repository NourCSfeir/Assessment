from django.shortcuts import render
from .forms import ConversionForm
from decimal import Decimal

#Conversion rates relative to a common currency: USD
conversion_rates = {
    'bitcoin': Decimal('67859.48'),  
    'ethereum': Decimal('3720.17'),   
    'tether': Decimal('0.999374'),    
    'bnb': Decimal('598.24'),        
    'solana': Decimal('168.27'),   
    'usdc': Decimal('0.999952'), 
    'xrp': Decimal('0.535467'),        
    'dogecoin': Decimal('0.167156'),   
    'toncoin': Decimal('6.25'),    
    'cardano': Decimal('0.461182')     
}
currency_symbols = {
    'bitcoin': 'BTC',
    'ethereum': 'ETH',
    'tether': 'USDT',
    'bnb': 'BNB',
    'solana': 'SOL',
    'usdc': 'USDC',
    'xrp': 'XRP',
    'dogecoin': 'DOGE',
    'toncoin': 'TON',
    'cardano': 'ADA'
}

def get_conversion_rate(from_currency, to_currency):
     
    if from_currency == to_currency:
        return Decimal('1')

    if from_currency in conversion_rates and to_currency in conversion_rates:
        #Convert from `from_currency` to USD and then from USD to `to_currency`
        from_rate = conversion_rates[from_currency]
        to_rate = conversion_rates[to_currency]
        return from_rate / to_rate

    return None

def converter(request):
    form = ConversionForm()
    converted_amount = None
    rate = None
    from_currency = to_currency = None
    from_symbol = to_symbol = None
    error = None

    if request.method == 'POST':
        form = ConversionForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            from_currency = form.cleaned_data['from_currency']
            to_currency = form.cleaned_data['to_currency']
            rate = get_conversion_rate(from_currency, to_currency)
            if rate:
                converted_amount = amount * rate
                from_symbol = currency_symbols[from_currency]
                to_symbol = currency_symbols[to_currency]

            else:
                error = f"Conversion rate for {from_currency} to {to_currency} is not available."

    return render(request, 'converter/converter.html', {
        'form': form,
        'rate': rate,
        'converted_amount': converted_amount,
        'from_currency': from_currency,
        'to_currency': to_currency,
        'from_symbol': from_symbol,
        'to_symbol': to_symbol,
        'error': error
    })
