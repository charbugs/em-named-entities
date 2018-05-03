import spacy

def get_setup():
	return {
		'title': 'Highlight Personal Names',
		'description': 'Highlights personal names.',
		'inputs': [
			{ 
				'id': 'lang', 
				'type': 'select',
				'values': ['English', 'German'],
				'label': 'Website Language'
			},
		]
	}

def get_markup(markup_request):

	if markup_request['inputs']['lang'] == 'German':
		nlp = spacy.load('de')
	else:
		nlp = spacy.load('en')

	tokens = markup_request['tokens']
	doc = spacy.tokens.Doc(nlp.vocab, tokens)
	nlp.entity(doc)

	markup = [ { 'group': { 'first': ent.start, 'last': ent.end-1 } } 
					for ent in doc.ents if ent.label_ in [u'PERSON', u'PER'] ]

	return { 'markup': markup }