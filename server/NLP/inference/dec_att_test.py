# pylint: disable=no-self-use,invalid-name
import math

from pytest import approx

from allennlp.common.testing import AllenNlpTestCase
from allennlp.models.archival import load_archive
from allennlp.predictors import Predictor



# reuslts vector
# 'label_probs': [0.00033908727345988154, 0.9735873341560364, 0.026073550805449486]

# 0.0 97.358 2.607
# entailment contradiction neutral




class TestDecomposableAttentionPredictor(AllenNlpTestCase):
    def test_uses_named_inputs(self):
        inputs = {
                "premise": "Two women are wandering along the shore drinking iced tea.",
                "hypothesis": "Two women are sitting on a blanket near some rocks talking about politics."
        }

        #archive = load_archive(self.FIXTURES_ROOT / 'decomposable_attention' / 'serialization' / 'model.tar.gz')
        archive= load_archive("../models/dec_att_elmo.model")
        predictor = Predictor.from_archive(archive, 'textual-entailment')
        result = predictor.predict_json(inputs)

        # Label probs should be 3 floats that sum to one
        label_probs = result.get("label_probs")
        assert label_probs is not None
        assert isinstance(label_probs, list)
        assert len(label_probs) == 3
        assert all(isinstance(x, float) for x in label_probs)
        assert all(x >= 0 for x in label_probs)
        assert sum(label_probs) == approx(1.0)

        # Logits should be 3 floats that softmax to label_probs
        label_logits = result.get("label_logits")
        assert label_logits is not None
        assert isinstance(label_logits, list)
        assert len(label_logits) == 3
        assert all(isinstance(x, float) for x in label_logits)

        exps = [math.exp(x) for x in label_logits]
        sumexps = sum(exps)
        for e, p in zip(exps, label_probs):
            assert e / sumexps == approx(p)

        return result

    def test_batch_prediction(self):
        batch_inputs = [
                {
                        "premise": "I always write unit tests for my code.",
                        "hypothesis": "One time I didn't write any unit tests for my code."
                },
                {
                        "premise": "I also write batched unit tests for throughput!",
                        "hypothesis": "Batch tests are slower."
                },
        ]

        archive = load_archive(self.FIXTURES_ROOT / 'decomposable_attention' / 'serialization' / 'model.tar.gz')
        predictor = Predictor.from_archive(archive, 'textual-entailment')
        results = predictor.predict_batch_json(batch_inputs)
        print(results)
        assert len(results) == 2

        for result in results:
            # Logits should be 3 floats that softmax to label_probs
            label_logits = result.get("label_logits")
            # Label probs should be 3 floats that sum to one
            label_probs = result.get("label_probs")
            assert label_probs is not None
            assert isinstance(label_probs, list)
            assert len(label_probs) == 3
            assert all(isinstance(x, float) for x in label_probs)
            assert all(x >= 0 for x in label_probs)
            assert sum(label_probs) == approx(1.0)

            assert label_logits is not None
            assert isinstance(label_logits, list)
            assert len(label_logits) == 3
            assert all(isinstance(x, float) for x in label_logits)

            exps = [math.exp(x) for x in label_logits]
            sumexps = sum(exps)
            for e, p in zip(exps, label_probs):
                assert e / sumexps == approx(p)


if __name__ == "__main__":
    T = TestDecomposableAttentionPredictor()
    print(T.test_uses_named_inputs())
