from setuptools import setup

setup(
    name='NlpToolkit-SpellChecker',
    version='1.0.12',
    packages=['SpellChecker'],
    url='https://github.com/olcaytaner/TurkishSpellChecker-Py',
    license='',
    author='olcaytaner',
    author_email='olcaytaner@isikun.edu.tr',
    description='Turkish Spell Checker Library',
    install_requires=['NlpToolkit-MorphologicalAnalysis', 'NlpToolkit-NGram']
)
