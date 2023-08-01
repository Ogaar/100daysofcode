from extractor import Extractor
from loader import Loader
from transformer import Transformer

extractor = Extractor("csv")
extracted_file = extractor.extract()

transformer = Transformer(extracted_file)
extracted_file = transformer.clear_duplicate_values(extracted_file)
cleaned_file = transformer.clear_row_if_empty_column(extracted_file)

loader = Loader("csv")
loader.load(cleaned_file)
