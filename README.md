# NerKor
The home repository of the NerKor corpus, a Hungarian gold standard named entity annotated corpus containing 1 million tokens. 

## License and usage

The corpus creation was funded by the Research Institute for Linguistics. The project leaders were Eszter Simon and Noémi Vadász. 

The corpus is available under the license CC-BY-SA 4.0. If you use this corpus, please mention this GitHub repo with URL (we do not have a published paper yet). 

## Data

Corpus files are under the 'data' folder. They are grouped by genre: fiction, legal, news, web, wikipedia. A ~200,000 tokens subcorpus contains gold standard morphological annotation besides NE labels. 

The fiction subcorpus contains i) novels from MEK (Hungarian Electronic Library) and Project Gutenberg; and ii) subtitles from OpenSubtitles. 

The legal texts come from EU sources: it is a selection from the EU Constitution, documents from the European Economic and Social Committee, DGT-Acquis and JRC-Acquis.

The sources of the news subcorpus are: Press Release Database of European Commission, Global Voices and NewsCrawl Corpus. 

Web texts contain a selection from the [Hungarian Webcorpus 2.0](https://hlt.bme.hu/en/resources/webcorpus2). 

Wikipedia texts are from the Hungarian Wikipedia. :)

## Token numbers

| genre | morph/no-morph | token number |
|---------|--------|------------|
| fiction | morph | 0 |
|  | no-morph | 203216 |
|  | sum | 203216 |
| legal | morph | 0 |
|  | no-morph | 202195 |
|  | sum | 202195 |
| news | morph | 9178 |
|  | no-morph | 204478 |
|  | sum | 213656 |
| web | morph | 187232 |
|  | no-morph | 0 |
|  | sum | 187232 |
| wikipedia | morph | 26764 |
|  | no-morph | 194033 |
|  | sum | 220797 |
| altogether | morph | 223174 |
|  | no-morph | 803922 |
|  | sum | 1027096 |

## Data format

The format of data files are CoNLL-U Plus with the standard .conllup file extension. 

## Guidelines

Annotation guidelines and Annotation scheme are available in the Guidelines folder. (Only in Hungarian.)
