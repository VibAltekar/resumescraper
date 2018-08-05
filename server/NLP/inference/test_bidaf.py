
from allennlp.models.archival import load_archive
from allennlp.service.predictors import Predictor


class TestBidafPredictor():
    def test_uses_named_inputs(self,inputs=None):
        if inputs==None:
                inputs = {
                        "question": "What is the Volt doing at night?",
                        "passage": "The Chevy Volt is charging during the day at peak hours. It sits quiet during the night."
                }

        archive = load_archive('../models/bidaf.model')
        predictor = Predictor.from_archive(archive, 'machine-comprehension')

        result = predictor.predict_json(inputs)
        #print(inputs)
        print("----------")
        best_span_str = result.get("best_span_str")
        print(best_span_str)
        best_span_str.replace("<","")
        best_span_str.replace(">","")
        best_span_str.replace("`","")
        best_span_str.replace('"',"")
        best_span_str.replace("'","")
        best_span_str.replace("(","")
        '''print("---------")
        print(result.keys())
        print((result["span_start_probs"]))
        print((inputs["passage"].split(" ")))
        print(best_span_str)
        print("---------")'''
        best_span = result.get("best_span")
        #print(best_span)
        assert best_span is not None
        assert isinstance(best_span, list)
        assert len(best_span) == 2
        assert all(isinstance(x, int) for x in best_span)
        assert best_span[0] <= best_span[1]

        best_span_str = result.get("best_span_str")
        #print(best_span_str)
        assert isinstance(best_span_str, str)
        assert best_span_str != ""

        return best_span_str

    def test_batch_prediction(self,inputs=None):
        inputs = [
                {
                        "question": "What kind of test succeeded on its first attempt?",
                        "passage": "One time I was writing a unit test, and it succeeded on the first attempt."
                },
                {
                        "question": "What kind of test succeeded on its first attempt at batch processing?",
                        "passage": "One time I was writing a unit test, and it always failed!"
                }
        ]

        archive = load_archive('/Users/vibhav/Workspace_8_17/VigneshAmazon/personal/bid_store/bidaf.model')
        predictor = Predictor.from_archive(archive, 'machine-comprehension')

        results = predictor.predict_batch_json(inputs)
        assert len(results) == 2

        for result in results:
            best_span = result.get("best_span")
            best_span_str = result.get("best_span_str")
            start_probs = result.get("span_start_probs")
            end_probs = result.get("span_end_probs")
            assert best_span is not None
            assert isinstance(best_span, list)
            assert len(best_span) == 2
            assert all(isinstance(x, int) for x in best_span)
            assert best_span[0] <= best_span[1]

            assert isinstance(best_span_str, str)
            assert best_span_str != ""




if __name__ == "__main__":
    t = TestBidafPredictor()
    print(t.test_uses_named_inputs())
