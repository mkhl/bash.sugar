#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup
import py2app
import os, glob

def data_files(dirname = 'xml'):
	"""Figure out the sugar structure and massage it into data_files format."""
	def data_file(component):
		return (os.path.join('..', '..', component),
		        glob.glob(os.path.join(dirname, component, '*')))
	
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
	for subdir in dirs.intersection(set(os.listdir(dirname))):
		result.append(data_file(subdir))
	return result

def sources(dirname):
	"""Find (re)source files for our bundle and massage them into data_files format."""
	return glob.glob(os.path.join(dirname, '*'))

setup(
	name = 'Bash',
	version = '0.0',
	author = u'Martin Kühl',
	author_email = 'martin.kuehl@gmail.com',
	url = 'http://github.com/mkhl/bash.sugar',
	description = 'A Sugar adding sweet Bash support for Espresso',
	data_files = sources('res') + data_files('xml'),
	plugin = sources('src'),
	options = dict(
		py2app = dict(
			extension = '.sugar',
			# semi_standalone = True,
			plist = dict(
				CFBundleVersion = '0.0',
				CFBundleIdentifier = 'org.purl.net.mkhl.bash',
				CFBundleGetInfoString = u'Bash sugar for Espresso v0.0α',
				NSHumanReadableCopyright = u'(c) 2009 Martin Kühl. Released under the MIT license.',
			),
		),
	),
)
