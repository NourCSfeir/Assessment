from django import forms

CRYPTO_CHOICES = {
    'bitcoin': 'Bitcoin (BTC)',
    'ethereum': 'Ethereum (ETH)',
    'tether': 'Tether USDt (USDT)',
    'bnb': 'BNB (BNB)',
    'solana': 'Solana (SOL)',
    'usdc': 'USDC (USDC)',
    'xrp': 'XRP (XRP)',
    'dogecoin': 'Dogecoin (DOGE)',
    'toncoin': 'Toncoin (TON)',
    'cardano': 'Cardano (ADA)',
}

CHOICES = [(key, value) for key, value in CRYPTO_CHOICES.items()]

class ConversionForm(forms.Form):
    amount = forms.DecimalField(label='Amount', max_digits=20, decimal_places=8)
    from_currency = forms.ChoiceField(label='From Currency', choices=CHOICES)
    to_currency = forms.ChoiceField(label='To Currency', choices=CHOICES)
