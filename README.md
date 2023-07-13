# NYTK-NerKor
The home repository of the NYTK-NerKor corpus, a Hungarian gold standard named entity annotated corpus containing 1 million tokens. 

## License and usage

The corpus creation was funded by the Hungarian Research Centre for Linguistics (Nyelvtudományi Kutatóközpont, NYTK). The project leaders were Eszter Simon and Noémi Vadász. 

The corpus is available under the license CC-BY-SA 4.0. If you use this corpus, please cite our paper (see below). 

## Data

Corpus files are under the [data](data) folder. The [train](data/train), [devel](data/devel) and [test](data/test) subfolders contain the data files grouped by genre: fiction, legal, news, web, wikipedia. 

The corpus contains gold standard morphological annotation besides NE labels. 

The proportion of train, devel and test sets is around 80%-10%-10%. All sets provide a balanced selection from all genres and sources. For exact numbers, see the train-devel-test table below. 
 
The fiction subcorpus contains i) novels from MEK (Hungarian Electronic Library) and Project Gutenberg; and ii) subtitles from OpenSubtitles. 
 
The legal texts come from EU sources: it is a selection from the EU Constitution, documents from the European Economic and Social Committee, DGT-Acquis and JRC-Acquis.
 
The sources of the news subcorpus are: Press Release Database of European Commission, Global Voices and NewsCrawl Corpus. 

Web texts contain a selection from the [Hungarian Webcorpus 2.0](https://hlt.bme.hu/en/resources/webcorpus2). 

Wikipedia texts are from the Hungarian Wikipedia. :)

## Token numbers

| genre          | file | sentence | token   |
|----------------|------|----------|---------|
| fiction        | 122  | 24690    | 203014  |
| legal          | 39   | 7272     | 191984  |
| news           | 82   | 9767     | 213157  |
| web            | 398  | 10886    | 187853  |
| wikipedia      | 157  | 14702    | 221332  |
| altogether     | 798  | 67317    | 1017340 |

## NE labels and density

| genre      | PER   | LOC   | ORG   | MISC  | NE    | NE density    |
|------------|-------|-------|-------|-------|-------|---------------|
| fiction    | 5206  | 1010  | 212   | 281   | 6709  | 0.03304698198 |
| legal      | 249   | 1247  | 6536  | 1798  | 9830  | 0.05120218352 |
| news       | 4588  | 2309  | 5325  | 3681  | 15903 | 0.07460697983 |
| web        | 2826  | 1343  | 1789  | 2434  | 8392  | 0.04467322854 |
| wikipedia  | 8897  | 9156  | 5386  | 4403  | 27842 | 0.1257929265  |
| altogether | 21766 | 15065 | 19248 | 12597 | 68676 | 0.0675054554  |

## Train-devel-test sets

| genre      | train  | devel  | test   |
|------------|--------|--------|--------|
| fiction    | 161318 | 20903  | 20793  |
| legal      | 151910 | 20454  | 19620  |
| news       | 170747 | 20673  | 21737  |
| web        | 150725 | 18401  | 18727  |
| wikipedia  | 176515 | 22667  | 22150  |
| altogether | 811215 | 103098 | 103027 |

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

## Citation

If you use this resource or any part of its documentation, please refer to:


Simon, Eszter; Vadász, Noémi. (2021) Introducing NYTK-NerKor, A Gold Standard Hungarian Named Entity Annotated Corpus. In: Ekštein K., Pártl F., Konopík M. (eds) Text, Speech, and Dialogue. TSD 2021. Lecture Notes in Computer Science, vol 12848. Springer, Cham. https://doi.org/10.1007/978-3-030-83527-9_19


```
@inproceedings{DBLP:conf/tsd/SimonV21,
  author    = {Eszter Simon and
               No{\'{e}}mi Vad{\'{a}}sz},
  editor    = {Kamil Ekstein and
               Frantisek P{\'{a}}rtl and
               Miloslav Konop{\'{\i}}k},
  title     = {Introducing NYTK-NerKor, {A} Gold Standard Hungarian Named Entity
               Annotated Corpus},
  booktitle = {Text, Speech, and Dialogue - 24th International Conference, {TSD}
               2021, Olomouc, Czech Republic, September 6-9, 2021, Proceedings},
  series    = {Lecture Notes in Computer Science},
  volume    = {12848},
  pages     = {222--234},
  publisher = {Springer},
  year      = {2021},
  doi       = {10.1007/978-3-030-83527-9\_19},
}
```
