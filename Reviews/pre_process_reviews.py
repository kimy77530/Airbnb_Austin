def preprocess_model(text):
  '''
  The function, performs various preprocessing
  steps on a given text. It cleans and modifies
  the text to prepare it for further analysis or modeling.

  parameter:
    text (str): The input text to be preprocessed.
  Returns:
    Preprocessed text is returned as the output of the function.
  '''

  if text == '':
    return text

  # Remove non-alphanumeric characters except periods,
  # exclamation marks,comas and, apostrophes and question marks
  text = re.sub(r"[^a-zA-Z0-9.,!?']+|\s+", " ", text)

  # remove extra commas and semi-colons
  text = text.replace(".,",".")
  text = text.replace("..",".")
  text = text.replace(".;",".")

  text = text.replace("!,","!")
  text = text.replace("!.","!")
  text = text.replace("!;","!")

  text = text.replace("?,","!")
  text = text.replace("?.","!")
  text = text.replace("?;","!")

  text = text.replace(". ,",".")
  text = text.replace(". .",".")
  text = text.replace(". ;",".")

  text = text.replace("! ,","!")
  text = text.replace("! .","!")
  text = text.replace("! ;","!")

  text = text.replace("? ,","?")
  text = text.replace("? .","?")
  text = text.replace("? ;","?")

  # Other common issues

  # remove first character if it is a punctuation
  if text[0] in string.punctuation:
    text = text[1:]

  # remove extra commas in text
  text = re.sub(r'[.]+[\n]+[,]',".\n", text)

  # remove extra semi-colons in text
  text = re.sub(r'[.]+[\n]+[;]',".\n", text)

  # remove extra exclamation points in text
  text = re.sub(r'[.]+[\n]+[!]',".\n", text)

  # remove extra interrogation points in text
  text = re.sub(r'[.]+[\n]+[?]',".\n", text)

  # Replace new line with space
  text = text.replace("\n"," ")

  # Replace tab with space
  text = text.replace("\t"," ")

  # Remove random new line + comma
  text = text.replace("\n,","")

  # Replace multiple spaces with a single space
  text = re.sub(' +', ' ', text)

  # Remove trailing characters if it does not end with .
  while len(text) > 2 and text[-1] != '.':
    text = text[:-1]

  # Remove the single character hanging between any two spaces
  text = re.sub("(\s+.\s+)", " ", str(text)).lower()

  # Remove initial characters if they are space or puctuation
  while len(text) > 0 and (text[0] in string.punctuation or text[0] == ' '):
    text = text[1:]

  return text


def is_english(text):
  '''
  The function checks if a given text
  contains only English alphabetic characters.
  It returns True if all characters are English letters
  and False if it contains characters from
  another language or is not a string.
  Parameters:
    text (str): The input text to be checked for English alphabetic characters.
  Returns:
    New column consisting of a Boolean value indicating whether the given
    text consists entirely of English alphabetic characters.
  '''
  if isinstance(text, str):
    for c in text:
      if c.isalpha():
        if unicodedata.category(c) != 'Lu' and unicodedata.category(c) != 'Ll':
          return False
    return True
  else:
    return False




def expand_contractions(text, contraction_map=contractions_dict):
  '''
  The function takes a text string with contractions and
  replaces them with their expanded forms, returning the expanded text as the output.
  ex: you're --> you are

  Parameters:
    text (str): The input text containing contractions that need to be expanded.
    contraction_map: An optional argument that specifies a
    dictionary mapping contractions to their expanded forms.
    If not provided, it uses a default contractions_dict.
  Returns:
    Expanded form of the text contraction.

  '''
  # Using regex for getting all contracted words
  contractions_keys = '|'.join(contraction_map.keys())
  contractions_pattern = re.compile(f'({contractions_keys})', flags=re.DOTALL)

  def expand_match(contraction):
    # Getting entire matched sub-string
    match = contraction.group(0)
    expanded_contraction = contraction_map.get(match)
    if not expand_contractions:
      print(match)
      return match
    return expanded_contraction

  expanded_text = contractions_pattern.sub(expand_match, text)
  expanded_text = re.sub("'", "", expanded_text)
  return expanded_text


def preprocess_text2(text):
  '''
  The function applies lowercase conversion, removes
  URLs/HTML tags/numbers, removes punctuation, tokenizes
  the text, removes stopwords, replaces emojis, removes
  remaining punctuation, and reduces consecutive spaces
  in the text. The result is a cleaned and processed
  version of the input text.

  parameter:
    text (str): The input text to be preprocessed.

  Returns:
    Preprocessed text is returned as the output of the function.
  '''
  # Lower casing
  # text = text.lower()
  # Removal of URLs/HTML tags/numbers
  text = re.sub(r'<.*?>|http\S+|www\S+|\d+\.\d+', '', text)

  # Removal of "br" and "br br"
  text = text.replace("br", "").replace("br br", "")

  #Removal of punctuation
  text = text.translate(str.maketrans('', '', string.punctuation))

  # Tokenization
  tokens = word_tokenize(text)

  # Removal of stopwords
  stop_words = set(stopwords.words('english'))
  tokens = [word for word in tokens if not word in stop_words]

  # Replace emojis with string
  try:
    tokens = [emoji.demojize(word) for word in tokens]
  except IndexError:
    pass

  # Joining the tokens
  text = ' '.join(tokens)

  #Removal of punctuation left from emojis
  text = re.sub(r"[`~',.;:@#?!&$_]+\ *", " ", text)


  # Replace extra space
  text = re.sub(r"\s+", ' ', text)

  return text
