from extractor import Extractor
from loader import Loader

extractor = Extractor("csv")
extracted_file = extractor.extract()

loader = Loader("sqlite")
loader.load(extracted_file)
