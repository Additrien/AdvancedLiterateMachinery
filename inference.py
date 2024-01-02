from DocumentUnderstanding.GeoLayoutLM.model.geolayoutlm_vie import GeoLayoutLMVIEModel

model = GeoLayoutLMVIEModel()

for name, param in model.named_parameters():
    print(name, model.shape)