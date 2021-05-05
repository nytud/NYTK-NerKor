#!/bin/bash

VERSION="4.0.6"

input_file=$1
output_file=$2``
tmp_file=./tmp/emtsv/$(basename "$input_file")

echo "Processing \"$input_file\""
mkdir -p ./tmp/emtsv

# Store emtsv results in a temp file
awk 'BEGIN {print "form"} {print}' "${input_file}" \
  | grep -v "^#" \
  | cut -f 1 \
  | docker run --rm -i mtaril/emtsv:${VERSION} emMorph,emTag,emmorph2ud 2>>error.log \
  | awk -F $'\t' 'BEGIN {OFS = FS} FNR>1 {print $3,$5,$4,$6}' > "$tmp_file"

# Merge the original file w/ the emtsv result
paste <(grep -v "^#" "$input_file" | cut -f 1) \
      <(grep -v "^#" "$tmp_file") \
      <(grep -v "^#" "$input_file" | cut -f 6) \
  | awk 'BEGIN {print "# global.columns = FORM LEMMA UPOS XPOS FEATS CONLL:NER"} {print}' \
  > "$output_file"

rm "$tmp_file"
