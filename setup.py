from setuptools import setup, find_packages


setup(
    name="pygal_maps_uk",
    version="0.1.0",
    description="United Kingdom maps for pygal",
    author="Mostly Oxygen",
    url="",
    author_email="",
    licence="GNU LGPL v3+",
    platforms="Any",
    packages=find_packages(),
    provides=["pygal_maps_uk"],
    keywords=["svg", "chart", "graph", "maps", "uk"],
    package_data={"pygal_maps_uk": ["*.svg"]},
    install_requires=["pygal>=1.9.9"],
    entry_points={
        "pygal.maps": [
            "uk = pygal_maps_uk.maps",
        ]
    }
)
