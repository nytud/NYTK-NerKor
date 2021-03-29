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

## NE labels and density

|genre | morph/no-morph |       PER | LOC | ORG | MISC | NE | NE density |
|fiction | morph  |     0 | 0 | 0 | 0 | 0 |  |
| | no-morph |  5224 | 1042 | 217 | 287 | 6770 | 0,03331430596 |
| | sum |      5224 | 1042 | 217 | 287 | 6770 | 0,03331430596 |
|legal | morph  |       0 | 0 | 0 | 0 | 0 |  |
| | no-morph |  255 | 1302 | 6840 | 1871 | 10268 | 0,0507826603 |
| | sum |      255 | 1302 | 6840 | 1871 | 10268 | 0,0507826603 |
|news | morph  |        220 | 168 | 183 | 63 | 634 | 0,06907823055 |
| | no-morph |  4368 | 2161 | 5111 | 3636 | 15276 | 0,07470730348 |
| | sum |      4588 | 2329 | 5294 | 3699 | 15910 | 0,07446549594 |
|web | morph  | 2826 | 1343 | 1788 | 2434 | 8391 | 0,04457370518 |
| | no-morph |  0 | 0 | 0 | 0 | 0 |  |
| | sum |      2826 | 1343 | 1788 | 2434 | 8391 | 0,04457370518 |
|wikipedia | morph  |   571 | 400 | 203 | 324 | 1498 | 0,05597070692 |
| | no-morph |  8321 | 8714 | 5159 | 3929 | 26123 | 0,1346317379 |
| | sum |      8892 | 9114 | 5362 | 4253 | 27621 | 0,1250968084 |
|altogether | morph  |  3617 | 1911 | 2174 | 2821 | 10523 | 0,04693744647 |
| | no-morph |  18168 | 13219 | 17327 | 9723 | 58437 | 0,07268988782 |
| | sum |      21785 | 15130 | 19501 | 12544 | 68960 | 0,06707427386 |



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
