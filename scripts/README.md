# Data processing scripts

To add automatic annotation to files not having morphosyntactic annotation (in `no-morph` directories), run the following commands:
1. `cp -R data annotated-data`
1. `find data/genres/ -wholename "*/no-morph/*.conllup" | xargs -I@ -n 1 ./scripts/annotate.sh @ annotated-@`