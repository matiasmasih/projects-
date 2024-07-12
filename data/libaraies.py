libraries = [
    "numpy",
    "pandas",
    "matplotlib",
    "scipy",
    "sklearn",
    "tensorflow",
    "keras",
    "requests",
    "flask",
    "django",
    "bs4",  # beautifulsoup4
    "torch",  # PyTorch
    "cv2",  # OpenCV
    "nltk",
    "sqlalchemy"
]

for lib in libraries:
    try:
        module = __import__(lib)
        version = module.__version__ if hasattr(module, '__version__') else 'Version not available'
        print(f"{lib} is installed. Version: {version}")
    except ImportError:
        print(f"{lib} is NOT installed.")
