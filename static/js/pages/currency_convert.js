const cleave = new Cleave('#amountField', {
    numeral: true,
    numeralThousandsGroupStyle: 'thousand',
    numeralDecimalMark: '.',
    numeralDecimalScale: 2,
    prefix: '฿ ',
    rawValueTrimPrefix: true
});