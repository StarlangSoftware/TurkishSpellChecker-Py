from setuptools import setup

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

setup(
    name='NlpToolkit-SpellChecker',
    version='1.0.26',
    packages=['SpellChecker'],
    package_data={'SpellChecker.data': ['*.txt']},
    url='https://github.com/StarlangSoftware/TurkishSpellChecker-Py',
    license='',
    author='olcaytaner',
    author_email='olcay.yildiz@ozyegin.edu.tr',
    description='Turkish Spell Checker Library',
    install_requires=['NlpToolkit-MorphologicalAnalysis', 'NlpToolkit-NGram'],
    long_description=long_description,
    long_description_content_type='text/markdown'
)
