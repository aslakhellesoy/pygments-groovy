# -*- coding: utf-8 -*-
"""
Groovy Pygments Lexer plugin setup file for setuptools
"""
from setuptools import setup

setup(
    name='Groovy Pygments Lexer',
    version='0.1',
    author='Matthew Taylor',
    author_email='matt.taylor@springsource.com',
    description=__doc__,
    license='BSD',
    url='http://weblog.dangertree.net/pygments-groovy-lexer',
    keywords='groovy grails syntax highlighting',
    packages=['groovy_lexer'],
    entry_points='''[pygments.lexers]
groovylexer = groovy_lexer:GroovyLexer
    '''
)
