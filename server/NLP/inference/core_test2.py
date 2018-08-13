from allennlp.common.testing import AllenNlpTestCase
import sys
import json
from allennlp.models.archival import load_archive
from allennlp.predictors import Predictor

# just need clusters from result

class TestCorefPredictor(AllenNlpTestCase):
    def test_uses_named_inputs(self,inputs=None):
        if inputs == None:
            inputs = {"document": "This is a single string document about a test. Sometimes it "
                          "contains coreferent parts."}
        #archive = load_archive(""self.FIXTURES_ROOT / 'coref' / 'serialization' / 'model.tar.gz""')
        archive = load_archive("../models/coref.model")
        predictor = Predictor.from_archive(archive, 'coreference-resolution')

        result = predictor.predict_json(inputs)

        document = result["document"]
        '''assert document == ['This', 'is', 'a', 'single', 'string',
                            'document', 'about', 'a', 'test', '.', 'Sometimes',
                            'it', 'contains', 'coreferent', 'parts', '.']'''

        clusters = result["clusters"]
        assert isinstance(clusters, list)
        for cluster in clusters:
            assert isinstance(cluster, list)
            for mention in cluster:
                # Spans should be integer indices.
                assert isinstance(mention[0], int)
                assert isinstance(mention[1], int)
                # Spans should be inside document.
                #assert 0 < mention[0] <= len(document)
                #assert 0 < mention[1] <= len(document)
        return result
if __name__ == "__main__":
    t = TestCorefPredictor()
    data = {"document": "The woman reading a newspaper sat on the bench with her dog."}
    print(t.test_uses_named_inputs())
    print(t.test_uses_named_inputs(data))
