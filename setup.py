import setuptools

setuptools.setup(
    name="magicbox",
    version="0.1",
    author="Paul Lebel",
    author_email="plebel@alumni.stanford.edu",
    description="A small platform for parent-configurable child entertainment and education.",
    url="https://github.com/paul-lebel/magic-music-box",
    #packages=setuptools.find_packages(exclude=["*.tests", "*.tests.*",
    #                                           "tests.*", "tests"]),
        
    # Non-pip requirements: inky phat, circuitpython, adafruit-circuitpython-neopixel
    install_requires=[
        'gTTS',
        'RPi.GPIO',
        'font_fredoka_one'
    ]

    #test_suite="tests",
    #classifiers=[
    #    "CZ Biohub :: Bioengineering",
    #],
)
