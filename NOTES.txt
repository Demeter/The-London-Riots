======================
 First Implementation
======================

For this first pass at data analysis, articles and exchange rate data will
be downloaded on three currency pairs: USD<->AUD, USD<->GBP, GBP<->AUD.

Feature Extraction
==================

The HTML of the articles will first be preprocessed to exclude all items
not in a <p> tag, and then to remove all HTML markup.

The text will have the named entities identified by the NLTK and then the
proper nouns counted. Only nouns appearing three or more times will
be retained.

The resulting word lists will represent a sparse feature matrix, and
unique words will be assigned dimensions. The currency pairs each also
represent one of three dimensions.

An article is assumed to affect average of the opening and closing
exchange rates of a currency pair the trading day following the
publication of the article, and the fractional increase over the previous
day's opening and closing price is used as the value of the feature matrix
for the SVR.

