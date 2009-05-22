#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup
import py2app
import os

def data_files(dirname = '.'):
	"""Figure out the sugar structure and massage it into data_files format."""
	def data_file(name):
		return (os.path.join('..', '..', name),
		        [os.path.join(dirname, name, file)
		         for file in os.listdir(os.path.join(dirname, name))
		         if not file.startswith('.')])
	
	base = ['LICENSE', 'README.mdown', 'Languages.xml']
	result = [(os.path.join('..', '..'), base)]
	dirs = set([
		'CodeSenseLibraries',
		'CodeSenseProviders',
		'ContextualSettings',
		'FileActions',
		'Itemizers',
		'PlaceholderThemes',
		'Syntaxes',
		'SyntaxInjections',
		'TextActions',
	])
	for name in dirs.intersection(set(os.listdir(dirname))):
		result.append(data_file(name))
	return result

setup(
	name = 'Bash',
	version = '0.0',
	author = u'Martin Kühl',
	author_email = 'martin.kuehl@gmail.com',
	url = 'http://github.com/mkhl/bash.sugar',
	description = 'A Sugar adding sweet Bash support for Espresso',
	data_files = data_files('xml'),
	plugin = ['src/Itemizers.py'],
	options = {
		'py2app': {
			'extension': '.sugar',
			'plist': {
				'CFBundleVersion': '0.0',
				'CFBundleIdentifier': 'org.purl.net.mkhl.bash',
				'NSHumanReadableCopyright': u'(c) 2009 Martin Kühl. Released under the MIT license.',
			},
		}
	}
)
