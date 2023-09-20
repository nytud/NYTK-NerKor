# Morphology in two tagsets
The native tagset of NerKor morphology is the tagset of [emMorph](https://github.com/dlt-rilmta/emMorph), but we aimed to provide the data also in the tagset according to the [Universal Dependencies](https://universaldependencies.org/) guidelines.
This is because we wanted to make the corpus accessible to as many possible users as possible by introducing an international standard tagset.

## First approach: conversion
Within the framework of the project [panmorph](https://github.com/nytud/panmorph), we examined the existing Hungarian morphological tagsets, and also created converters between several tagsets.
Our assumption was that lossless conversion between UD and emMorph tagsets is possible, therefore our first approach was to use the [emmorph2ud2](https://github.com/vadno/emmorph2ud2) converter.
When creating the converter, we relied on the tags of [Hungarian UD treebank](https://universaldependencies.org/treebanks/hu_szeged/index.html), which is the only official Hungarian UD corpus.

As usual, it soon became clear that the task was not so simple.
The converted POS-tags and morphosyntactic features and their corresponding word forms and lemmas were compared with the Szeged Treebank equivalents, pointing to the following problems:

1. we have to deal not only with POS-tags and morphosyntactic features, but also with lemmas. The lemmatization scheme of the taggers producing emMorph tags differs from the basic principles of lemmatization required by the UD guideline, so even if we convert the POS-tags and features, it is still not certain that a valid UD corpus will be created
1. for the lemma and morphological tag of proper names in NerKor, we used a scheme different from that of UD
1. annotation errors in NerKor
1. design problems and bugs in emmorph2ud2

The differences belonging to the first two categories were corrected in the corpus using dictionaries and rules, see the details below.

We correct annotation errors in NerKor that are revealed with the help of this test. These errors can also occur with lemmas and emmorph tags.

Finally, based on the lessons learned here, we will also correct the errors and bugs of the emmorph2ud2 converter, at the same time, it is important to note that the converter only deals with the POS-tags and morphosyntactic features, it will not be able to solve lemmatization according to UD.

In addition to all this, this work also provides an opportunity to review the current Hungarian UD guidelines, possibly propose amendments, and to point out and correct annotation errors in the Szeged Treebank, if there are any.

## Dictionary and rule-based correction


### Proper names

The lemma and emmorph tag of proper names in NerKor reflects that we wanted to highlight proper names from the sentence structure.
We did not want to display the internal structure of multi-word proper names, if any, at the level of tags, so we handled them according to the following principles:
* the lemma of the proper noun is the same as the word form (the token itself), so neither the derivation nor the inflection are removed from it
* all proper nouns get a noun + case tag, and the last elements of multi-word proper nouns get a mere noun tag

This handling of proper names does not comply with UD's [guidelines](https://universaldependencies.org/u/pos/PROPN.html) for proper names.
Since the corpus contains more than 68,000 proper nouns, it was not possible to lemmatize and analyze them manually.
Instead, we parsed the corpus with the [HuSpaCy](https://github.com/huspacy/huspacy) parser and matched the lemma, POS-tag, and features issued by HuSpaCy to tokens that contained a proper name tag in the `CONLL:NER` field.

### Lemmatization

The different lemmatization principles cannot be reconciled, and since both were important to us (to match the lemmatization scheme for the native tagset of the corpus and also to meet UD's expectations), the user gets the lemma according to both schemes. According to the UD file format  ([CoNLL-U Plus](https://universaldependencies.org/ext-format.html)), the lemma column contains the stem corresponding to the UD requirements, while the `EMMORPH:LEMMA` column appearing as an optional field contains the lemma corresponding to the original lemmatization scheme.
Of course, the content of the `LEMMA` can be matched with the content of the `UPOS` and `FEATS` fields, while the content of the `EMMORPH:LEMMA` field can be matched with the content of `XPOS`.

For changing the lemmas rules and dictionaries were used.
The dictionaries were created by extracting the relevant word groups from NerKor and entering the corresponding UD lemma by hand.

#### Past, present and future participles

Present and past participles: dictionaries were used for inflected adjectival participles, and singular nominatives were catched by rules (`Case=Nom|Degree=Pos|Number=Sing|VerbForm=PartPast`) and (`VerbForm=PartPres`).

Furute participles: there are not many of these, we modified the ud lemma based on the label (`Case=Nom|Degree=Pos|Number=Sing|VerbForm=PartFut`).

#### Adverbial participles

Adverbial participles were treated based on the tag (`VerbForm=Conv`).



#### Relative pronouns

Originally the lemma of the relative pronouns _mely_, _mikor_ is the word form starting with _a-_ (_amely_, _amikor_), and this distinguishes them from the interrogative pronoun with the same word form.
We found that in Szeged Treebank the lemma of this relative pronouns are identical to the interrogative counterparts', 

#### Personal pronouns

However, it is not always clear, on what basis the lemmas were assigned to the different personal pronouns in the Szeged Treebank, we tried to bring the lemmas of the personal pronouns of the two corpora as close as possible.
in the table you can see what lemma the personal pronouns with different case markers received in the Szeged Treebank.
It happened that some pronouns were not lemmatized uniformly, in which case we indicated the number of occurrences of each solution.
It is important to note that not all possible personal pronouns occur in the corpus, and those that do occur with very low frequencies, therefore, based on the results, we could not learn the rules for lemmatization of the personal pronouns.

| E/1	    | 	      | E/2	      | 	    | E/3	       | 	                  | T/1	      | 	       | T/2	        | 	        | T/3	      |
|---------|--------|-----------|------|------------|--------------------|-----------|---------|-------------|----------|-----------|
| token   | 	lemma	    | token     | 	lemma	 | token      | 	lemma                | 	token    | 	lemma	    | token	      | lemma	      | token     |	lemma |
| tőlem   |        | 		tőled	  |      | 	tőle      | 	                  | tőle      | 	tőlünk | 		          | tőletek  |           |		tőlük|	tőle|
| engem   | 	én	   | téged     | 	te  | 	őt        | 	ő                 | 	minket   | 	       | 	titeket    | 	        | 	őket     | 	ők     |
| nálam	  | 	      | nálad     | 	    | 	nála	     |                    | 	nálunk	  | mi	     | nálatok     |          | 		náluk	  |  |
| hozzám  | 	      | 	hozzád   | 		   | hozzá	     | ő (9) / hozzá (4)	 | hozzánk	  | 	       | hozzátok    | 	        | 	hozzájuk | 	ők     |
| nekem   | 	én	   | neked	    |      | 	neki      | 	ő (4) / neki ( 4) | 	nekünk	  | mi      | 	nektek	    |          | 	nekik	   | ők      |
| rólam   | 	róla	 | rólad	    |      | 	róla      | 	róla              | 	rólunk	  |         | 	rólatok	   |          | 	róluk	   |  |            
| belőlem | 	      | 	belőled	 |      | 	belőle    | 	belőle	           | belőlünk  | 	       | 	belőletek	 | 	        | belőlük   | 	belőle |
| belém	  | 	      | beléd	    |      | 	belé/bele | 	ő (3) / bele (1)  | 	belénk   | 	       | 	belétek	   |          | 	beléjük	 ||
| bennem  | 	én    | 	benned		 |      | benne      | 	ő	                | bennünk	  |         | 	bennetek	  |          | 	bennük	  |      |       
| velem	  | vele   | 	veled	   |      | 	vele	     | vele	              | velünk	   |         | vele        | 	veletek | 	         | 	velük	 |vele  |     
| rám     | 	      | 	rád	     |      | 	rá        | 	ő (1) / rá (11)   | 	ránk	    |         | 	rátok	     |          | 	rájuk    | 	rá       |          
| rajtam  | 	      | 	rajtad	  |      | 	rajta	    | rajta	             | rajtunk		 |         | rajtatok	   |          | 	rajtuk	  |          | 

The lemmas of the personal pronouns were treated with a dictionary based on the lemmas found in the Szeged Treebank.

#### Substantives and auxiliaries

We found many differences in the two corpora that affected substantives and auxiliaries.
In the present work, we tried to bring the two corpora closer together, although it will certainly be necessary to revise the Hungarian UD guidelinein relation to these word classes.
At present, the lemma of the modal use of _lesz_ and _van_ differs in the two layers, as well as in cases some other verbs (the variants of _fog, lesz, volt_).

#### Numerals

There were some errors in NerKor regarding the numerals, plus the UD guideline differ from the principles used in NerKor.
Consequently, the lemma of ordinal and fractional numerals also differs.
We also corrected these with the help of dictionaries.

#### Causatives

The lemma of causatives originally is the dictionary form, but since UD tags do not contain derivational features, the UD lemma is the derivational form. The lemma of causatives were corrected using dictionary and rules as well.

#### Adjectivizer suffix -i 

Adjectivizer suffix -i falls into the same category as causatives, but the lemma of adjectives with -i suffix were corrected only by rules. 

#### Comparatives and superlatives

Even though there are features for the comparative and superlative suffix in the UD feats, the lemma is still the form containing the comparative or superlative suffix in the Szeged treebank.

### POS and Features

In some cases, it turned out that we had to apply manual correction not only for lemmas, but also for POS-tags and UD features. This is primarily due to errors in the emmorph2ud2 converter or annotation errors, but at the same time, we also need to examine how reliable the data in the Szeged Treebank is, since the Szeged Treebank annotation may also contain errors, and in the case of certain phenomena, the UD Hungarian guideline may also be worthwhile revise.

#### Preverbs

In Szeged Treebank some preverbs (_vissza, össze, le, ki, fel, elő, be_) have `Degree=Pos` feature, however, according to UD these words are not tagged as preverbs, but adverbs.
Other preverbs does not have this feature.

#### Other

There were smaller errors regarding the UD feats and POS-tags, mostly in connection with adverbs, determiners and pronouns, e.g. the quantificational determiner use of _minden_ was mishandled.
It turned out that the comparison of the two corpora and the guidelines provides a good basis for improving the emmorph2ud2 converter, but this work has not yet been done.
