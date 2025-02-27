from llama_index.core.llms.base import BaseLLM
from llama_index.llms.sagemaker_endpoint import SageMakerLLM


def test_embedding_class():
    names_of_base_classes = [b.__name__ for b in SageMakerLLM.__mro__]
    assert BaseLLM.__name__ in names_of_base_classes
