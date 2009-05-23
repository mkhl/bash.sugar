#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Foundation import objc

class BashFuncItem(objc.lookUpClass('ESBaseItem')):
	"""Itemizer for functions"""
	pass

class BashCodeBlockItem(objc.lookUpClass('ESCodeBlockItem')):
	"""Itemizer for code blocks"""
	
	def isTextualizer(self):
		return True
	
	def title(self):
		return '%s %s' % (u'{…}', self.text())
		
	
