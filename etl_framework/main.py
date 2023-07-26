from extractor import Extractor
from loader import Loader

extractor = Extractor("csv")
extracted_file = extractor.extract()


loader = Loader("excel")
loader.load(extracted_file)
