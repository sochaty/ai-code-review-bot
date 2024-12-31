# tests/test_analyzer.py


from src.code_analyzer.analyzer import CodeAnalyzer


def test_analyze():
    analyzer = CodeAnalyzer()
    code = """# No module docstring

print('Hello, World!')"""  # Code snippet with missing module docstring
    results = analyzer.analyze(code)
    print(results)
    assert any(
        "missing-module-docstring" in line for line in results), "Expected 'missing-module-docstring' in results"
