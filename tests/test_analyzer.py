# tests/test_analyzer.py

from src.code_analyzer.analyzer import CodeAnalyzer

def test_analyze():
    analyzer = CodeAnalyzer()
    code = "print('Hello, World!')"  # Example code snippet
    results = analyzer.analyze(code)
    assert "missing-module-docstring" in results
