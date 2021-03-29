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

|genre | morph/no-morph | file | sentence | token|
|------|----------------|------|----------|------|
|fiction | morph  | 0 | 0 | 0|
| | no-morph | 123 | 24535 | 203216|
| | sum | 123 | 24535 | 203216|
|legal | morph  | 0 | 0 | 0|
| | no-morph | 40 | 7632 | 202195|
| | sum | 40 | 7632 | 202195|
|news | morph  | 36 | 477 | 9178|
| | no-morph | 48 | 9280 | 204478|
| | sum | 84 | 9757 | 213656|
|web | morph  | 399 | 10886 | 188250|
| | no-morph | 0 | 0 | 0|
| | sum | 399 | 10886 | 188250|
|wikipedia | morph  | 86 | 1618 | 26764|
| | no-morph | 73 | 13096 | 194033|
| | sum | 159 | 14714 | 220797|
|altogether | morph  | 521 | 12981 | 224192|
| | no-morph | 284 | 54543 | 803922|
| | sum | 805 | 67524 | 1028114|


## Data format

The format of data files are [CoNLL-U Plus](https://universaldependencies.org/ext-format.html) with the standard `.conllup` file extension. The first line in each file is: `# global.columns = FORM LEMMA UPOS XPOS FEATS CONLL:NER`, where:

`FORM`: the token itself;

`LEMMA`: the lemma of the token;

`UPOS`: UD POS tags; 

`XPOS`: full morphological annotation (POS + meorphosyntactic features) provided by [emMorph](https://github.com/dlt-rilmta/emMorph); 

`FEATS`: UD morphosyntactic features;

`CONLL:NER`: NE annotation.

The NE annotation follows the CoNLL2002 labelling standard. The four NE categories are: `PER`, `LOC`, `MISC`, `ORG`. The tags are in the `IOB2` format: a `B-` prefix denotes the first item of a NE phrase and an `I-` prefix any non-initial word. Non-names are marked by an `O` label. 

## Guidelines

Annotation guidelines, WebAnno guidelines and Annotation scheme are available in the Guidelines folder. (Only in Hungarian.)
