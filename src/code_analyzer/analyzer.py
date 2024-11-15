# src/code_analyzer/analyzer.py

import pylint.lint


class CodeAnalyzer:
    def analyze(self, code):
        results = []
        # Run pylint on the code snippet
        # Disable certain warning categories
        pylint_opts = ["--from-stdin", "--disable=C,R"]
        pylint_output = pylint.lint.run_pylint(code, pylint_opts)

        for message in pylint_output:
            results.append(f"{message.msg_id}: {message.msg}")

        return results
