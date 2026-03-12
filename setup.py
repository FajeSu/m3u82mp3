from setuptools import setup


def requirements_file_to_list(fn='requirements.txt'):
    with open(fn, 'r') as f:
        return [x.rstrip() for x in list(f) if x and not x.startswith('#')]


setup(
    name='m3u82mp3',
    version='1.1',
    python_requires='>=3.7, <4',
    install_requires=requirements_file_to_list(),
    keywords=['m3u82mp3', 'm3u8-to-mp3'],
)
