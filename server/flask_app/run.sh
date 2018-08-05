python -m allennlp.service.server_simple \
    --archive-path tests/fixtures/model.tar.gz \
    --predictor paper-classifier \
    --include-package my_library \
    --title "Academic Paper Classifier" \
    --field-name title \
    --field-name paperAbstract \
    --static-dir static_html
