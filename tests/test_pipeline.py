from batteryhealthforecast import ForecastPipeline


def test_pipeline_creation():

    pipe = ForecastPipeline()

    assert pipe is not None
