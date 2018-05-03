# -*- coding: utf-8 -*-

import unittest
import sys
sys.path.append('..')
from marker import marker

class TestMarkupRespone(unittest.TestCase):

	text_en = u"""
		The United States completed its shipment of Javelin anti-tank
		missiles to Ukraine on Monday, finalizing a sale that was 
		reluctantly approved by President Donald Trump in November.
		The deal was widely reported as a rebuke to Russian President
		Vladimir Putin, who annexed Crimea and invaded eastern Ukraine
		in 2014. “This decision … reflects our country’s longstanding
		commitment to Ukraine in the face of ongoing Russian aggression,”
		Republican Senator Bob Corker said late last year."""

	text_de = u"""
		Der Etatentwurf der Bundesregierung war für Verteidigungsministerin
		Ursula von der Leyen kein Grund zur Freude: Die CDU-Politikern 
		braucht aus ihrer Sicht wesentlich mehr Geld, als ihr Finanzminister
		Olaf Scholz (SPD) zur Verfügung stellen will. Nun mischt sich 
		SPD-Parteichefin Andrea Nahles in den Streit ein."""

	def create_markup_request(self, text, lang, class_):
		return {
			'tokens': text.split(),
			'inputs': {
				'lang': lang,
				'class': class_
			}
		}		

	def test_determine_language_code_en(self):
		markup_request = self.create_markup_request('lorem', 'English', None)
		code = marker.determine_language_code(markup_request)
		self.assertTrue(code == 'en')

	def test_determine_language_code_de(self):
		markup_request = self.create_markup_request('lorem', 'German', None)
		code = marker.determine_language_code(markup_request)
		self.assertTrue(code == 'de')

	def test_determine_ne_label_en_per(self):
		markup_request = self.create_markup_request('lorem', None, 'Persons')
		label = marker.determine_ne_label(markup_request, 'en')
		self.assertTrue(label == 'PERSON')

	def test_determine_ne_label_de_per(self):
		markup_request = self.create_markup_request('lorem', None, 'Persons')
		label = marker.determine_ne_label(markup_request, 'de')
		self.assertTrue(label == 'PER')

	def test_markup_en_per(self):
		markup_request = self.create_markup_request(
			TestMarkupRespone.text_en, 'English', 'Persons')
		markup_response = marker.get_markup(markup_request)
		self.assertTrue(len(markup_response['markup']) > 0) 

	def test_markup_de_per(self):
		markup_request = self.create_markup_request(
			TestMarkupRespone.text_de, 'German', 'Persons')
		markup_response = marker.get_markup(markup_request)
		self.assertTrue(len(markup_response['markup']) > 0)

if __name__ == '__main__':
	unittest.main()



