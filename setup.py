from setuptools import setup

setup(
    name='NlpToolkit-SpellChecker',
    version='1.0.18',
    packages=['SpellChecker'],
    url='https://github.com/StarlangSoftware/TurkishSpellChecker-Py',
    license='',
    author='olcaytaner',
    author_email='olcay.yildiz@ozyegin.edu.tr',
    description='Turkish Spell Checker Library',
    install_requires=['NlpToolkit-MorphologicalAnalysis', 'NlpToolkit-NGram']
)
