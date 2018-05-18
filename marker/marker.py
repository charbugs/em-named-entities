import spacy

code_map = {
	'English': 'en',
	'German': 'de'
}

corpus_map = {
	'en': 'en_core_web_sm',
	'de': 'de_core_news_sm'	
}

label_map = {
	'en': { 
		'Persons': 'PERSON',
		'Locations': 'LOC',
		'Organisations': 'ORG'
	},
	'de': {
		'Persons': 'PER',
		'Locations': 'LOC',
		'Organisations': 'ORG'
	}
}

def get_setup():
	return {
		'title': 'Named Entities',
		'description': 'Highlights names of persons, locations or organisations.',
		'inputs': [
			{ 
				'id': 'lang', 
				'type': 'select',
				'values': ['English', 'German'],
				'label': 'Website Language'
			},
			{
				'id': 'class',
				'type': 'select',
				'values': ['Persons', 'Locations', 'Organisations'],
				'label': 'Named Entity Class'
			}
		],
        'supportedLanguages': 'English, German',
        'homepage': 'https://github.com/charbugs/em-named-entities'
	}

def get_markup(markup_request):

	tokens = markup_request['tokens']
	code = determine_language_code(markup_request)
	label = determine_ne_label(markup_request, code)

	nlp = spacy.load(corpus_map[code])
	doc = spacy.tokens.Doc(nlp.vocab, tokens)
	nlp.entity(doc)

	markup = [ { 'group': { 'first': ent.start, 'last': ent.end-1 } } 
					for ent in doc.ents if ent.label_ == label ]

	report = "<div>%d matches for <i>%s</i></div>" % (
		len(markup),
		markup_request['inputs']['class']
	)

	return { 'markup': markup,  'report': report }

def determine_language_code(markup_request):
	lang = markup_request['inputs']['lang']
	code = code_map[lang]
	return code

def determine_ne_label(markup_request, language_code):
	class_ = markup_request['inputs']['class']
	label = label_map[language_code][class_]
	return label


